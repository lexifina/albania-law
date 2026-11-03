"""Albania: laws, Council of Ministers decisions, instructions and orders in force, from QBZ.

Reads only a local copy of Qendra e Botimeve Zyrtare's open API (qbz.gov.al/api/v1) and writes corpus.d parts
(SCHEMA.md). Deterministic: the same inputs give the same bytes. No network.

    python -X utf8 parse_acts.py --cache <folder> [--published <data/versions.json>] [--retrieved YYYY-MM-DD]
                                 [--memo <folder>] [--report holds.jsonl] [--publish-history] [--publish-ministerial]

The local copy (--cache) holds each response gzip'd at <sha256(url)[:2]>/<sha256(url)>.gz: the act listing
(/acts?size=100&page=N), each act's relations (/acts/{id}/relations) and versions (/acts/{id}/versions), each
Fletorja Zyrtare issue record (/gazettes/{year}/{number}) and each text, whose .docx is kept as its word/document.xml
(the .docx bytes were checked against the sha256 that names them in QBZ's URL, so that hash is the source hash); a
legacy .doc is kept as the text `antiword -m UTF-8.txt -w 0` gives for it (one paragraph per line), after the same check.

What becomes an act here: a base act ("Akt bazë") of these kinds, slug <kind>-<year>-<id>:
- a law of the Assembly (Ligj): ligj-<year>-<number>;
- a decision of the Council of Ministers (Vendim, Këshilli i Ministrave): vendim-<year>-<number>;
- an instruction (Udhëzim) or an order (Urdhër) of a minister or another body: udhezim-/urdher-<year>-<MMDD>-<number>
  (numbers repeat across ministries; the adoption day keeps them apart, and a clash holds both).

Without consolidated versions in QBZ, its one version is the text as published, in force from the day its own clause
gives, counted from the publication day of its Fletorja Zyrtare issue: "hyn në fuqi pas botimit" or "menjëherë" = the
publication day (laws: Kushtetuta, neni 84, pika 4; the normative acts of the Council of Ministers and of ministers:
neni 117, pika 1, legal force only once published), "N ditë / N muaj pas botimit" = that much later, or the calendar
day it names (not before publication). It is held back, not published, when any of these is true (the reason goes to
the report):
- QBZ links an act as changing or repealing it (relations CHANGES/REPEALS, direction in);
- the title of another act in QBZ's listing cites it ("vendimin nr. N, datë D", "ligjin nr. N/YYYY", "udhëzimin nr.
  N, datë D") and that act changes, adds to, corrects or repeals something;
- a text held here cites it and the words after the citation say it is amended or repealed ("i ndryshuar",
  "shfuqizohet", ...);
- two QBZ records give the same kind, number and year (day, for instructions and orders);
- its issue's publication day is missing, before its adoption or more than 120 days after it;
- the text's own header does not give the record's number and date, or carries QBZ's amendment notes;
- its in-force clause is missing, or not one of the forms above (for example "i shtrin efektet nga ...");
- (laws) the repository already holds it under its earlier name (ligji-<number>-<year>), or it is an annual budget
  law for a year before the retrieval year.

With consolidated versions (QBZ /acts/{id}/versions, each naming the act that changed it), the act is published with
its history only when every act QBZ links as changing it has a version and none repeals it: first the text as
published (dated as above), then each consolidated text, credited to the changing act and in force from the day that
act took effect (its own clause from its issue's publication day; a Constitutional Court decision on publication,
Kushtetuta, neni 132; any other kind of changing act holds the act). QBZ's validFrom is the changing act's adoption
day, not an in-force day, and is not used. QBZ's notes are kept out of the text; a changed provision is credited when
a note on it or the changing act's text names it, otherwise it is recorded as unexplained (publisher); a version
mostly unexplained holds the act. Parts: 40-vendime, 41-ligje, 44-udhezime, 45-urdhra (as published) and 42-, 43-,
46-, 47- (with histories), one per year; <part>.PUBLISH marks a part checked (histories and instructions/orders only
with the flags).
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import io
import json
import os
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = HERE / 'corpus.d'
API = 'https://qbz.gov.al/api/v1'
SITE = 'https://qbz.gov.al'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
VERSION = 'parse_acts 1'
CODE_SIG = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]
MUAJ = ['janar', 'shkurt', 'mars', 'prill', 'maj', 'qershor', 'korrik', 'gusht', 'shtator', 'tetor', 'nëntor', 'dhjetor']
LICENCE = ('Official texts of the Republic of Albania; legal acts and their official collections are not subject to '
           'copyright (ligji nr. 35/2016, neni 12, pika 1, shkronja “b”).')

RE_NOTE = re.compile(r'^\(\s*;?\s*(?:Ndryshuar|Shtuar|Shfuqizuar|Zëvendësuar|Riformuluar|i përditësuar|pezulluar)', re.I)
RE_NENI = re.compile(r'^Neni\s+(\d+)(?:\s*/\s*(\d+))?\s*$')
RE_HEAD = re.compile(r'^(KREU|SEKSIONI|PJESA|TITULLI)\s+([IVXLC]+)\s*$')
RE_POINT = re.compile(r'^(\d{1,3})\s*\.\s*(\S.*)?$')
RE_ITEM = re.compile(r'^(\d+(/\d+)?\.|[a-zçë]{1,2}\)|[ivx]+\))\s')
RE_VENDOSI = re.compile(r'\bVENDOSI\s*:?\s*$', re.I)
RE_SIGN_VKM = re.compile(r'^(?:P\.\s*|Z\.\s*|ZV\.?\s*|ZËVENDËS)?\s*KRYEMINIST(?:RI|ËR|ER|RA)?\b\.?$', re.I)
RE_FOOT_LAW = re.compile(r'^(Miratuar më datë|Miratuar në datën|Shpallur me dekretin|KRYETARI?$)')
STEMS = re.compile(r'(ndrysh|shfuqiz|shtes|zëvendës|korrigj|pezull)', re.I)
CHANGE_TITLE = re.compile(r'(ndrysh|shfuqiz|shtes|zëvendës|korrigj|pezull|ndreqje)', re.I)
BUDGET = re.compile(r'buxhet\w* (e |të )?(shtetit )?(të |e )?vitit (\d{4})', re.I)
DATE = r'(?:datë|date|data|dt\.?)\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})'
CITE_VKM = re.compile(r'\b(?:vendim(?:i|in|it)?|VKM(?:-?(?:në|ja|së|ve))?)\s+(?:e\s+)?(?:Këshillit të Ministrave\s+)?'
                      r'nr\.?\s*(\d+(?:-\d+)?)\s*,?\s*' + DATE, re.I)
CITE_LAW = re.compile(r'\bligj(?:i|in|it)?\s+nr\.?\s*(\d+)\s*(?:/\s*(\d{4})|,?\s*' + DATE + ')', re.I)
PART = {'vendim': '40-vendime', 'ligj': '41-ligje', 'udhezim': '44-udhezime', 'urdher': '45-urdhra'}
HIST_PART = {'vendim': '42-vendime-histori', 'ligj': '43-ligje-histori', 'udhezim': '46-udhezime-histori',
             'urdher': '47-urdhra-histori'}
MINISTERIAL = {'Udhëzim': 'udhezim', 'Urdhër': 'urdher'}  # instructions and orders (ministers and other bodies)
WHO = {'vendim': 'vendim', 'ligj': 'ligj', 'udhezim': 'udhëzim', 'urdher': 'urdh[eë]r'}
OPERATIVE_WIDE = {'vendim': r'(?<![a-zë])VENDOSI|^VENDOS', 'udhezim': r'(?<![a-zë])UDHËZO[JN]|^UDHËZOJ',
                  'urdher': r'(?<![a-zë])URDHËRO[JN]|^URDHËROJ'}
OPERATIVE = {'vendim': r'VENDOSI', 'udhezim': r'UDHËZOJ', 'urdher': r'URDHËROJ'}
CITE_MIN = re.compile(r'\b(udhëzim|urdh[eë]r|urdhr)(?:i|in|it)?\s+(?:e\s+)?nr\.?\s*(\d+)\s*,?\s*' + DATE, re.I)
NEXT_CITE = re.compile(r'\bnr\.?\s*\d', re.I)


class Hold(Exception):
    pass


def norm(s: str) -> str:
    s = unicodedata.normalize('NFC', s)
    s = s.replace('\xa0', ' ').replace('\xad', '').replace('\t', ' ')
    s = s.replace('–', '-').replace('—', '-').replace('‑', '-')
    s = s.replace('‘', '’').replace("'", '’')
    s = s.replace('„', '“').replace('"', '”')
    return re.sub(r'\s{2,}', ' ', s).strip()


def cpath(cache: Path, url: str) -> Path:
    h = hashlib.sha256(url.encode('utf-8')).hexdigest()
    return cache / h[:2] / f'{h}.gz'


TOUCHED: list | None = None  # while an act is computed: every input file it reads (for --result-cache)


def read(cache: Path, url: str) -> bytes | None:
    p = cpath(cache, url)
    if TOUCHED is not None:
        TOUCHED.append(str(p))
    return gzip.decompress(p.read_bytes()) if p.exists() else None


def read_json(cache: Path, url: str):
    b = read(cache, url)
    return None if b is None else json.loads(b)


def listing(cache: Path) -> list[dict]:
    first = read_json(cache, f'{API}/acts?size=100&page=0')
    out: dict[int, dict] = {}
    for i in range((first['total'] + 99) // 100):
        d = read_json(cache, f'{API}/acts?size=100&page={i}')
        if d is None:
            raise SystemExit(f'listing page {i} missing from the cache')
        for it in d['items']:
            out[it['id']] = it
    return [out[k] for k in sorted(out)]


def paras_of(xml: bytes) -> list[str]:
    root = ET.fromstring(xml)
    out = []
    for p in root.iter(W + 'p'):
        t = ''.join((n.text or '') if n.tag == W + 't' else (' ' if n.tag in (W + 'tab', W + 'br') else '')
                    for n in p.iter())
        t = norm(t)
        if t:
            out.append(t)
    return out


def text_of(cache: Path, memo: Path | None, a: dict) -> list[str] | None:
    url = SITE + a['word']['url']
    if TOUCHED is not None:
        TOUCHED.append(str(cpath(cache, url)))
    if memo:
        m = memo / f'{a["word"]["sha256"]}.json.gz'
        if m.exists():
            d = json.loads(gzip.decompress(m.read_bytes()))
            if d.get('v') == VERSION:
                return d['paras']
    x = read(cache, url)
    if x is None:
        return None
    if url.endswith('.doc'):
        paras = [t for t in (norm(ln) for ln in x.decode('utf-8', 'replace').splitlines()) if t]
    else:
        try:
            paras = paras_of(x)
        except ET.ParseError:
            return None
    if memo:
        memo.mkdir(parents=True, exist_ok=True)
        tmp = m.with_suffix(f'.{os.getpid()}.tmp')
        tmp.write_bytes(gzip.compress(json.dumps({'v': VERSION, 'paras': paras}, ensure_ascii=False).encode('utf-8'), 6))
        try:
            tmp.replace(m)
        except OSError:  # another run wrote the same memo at the same moment: its copy is identical
            tmp.unlink(missing_ok=True)
    return paras


def iso(d: str, m: str, y: str) -> str | None:
    try:
        return dt.date(int(y), int(m), int(d)).isoformat()
    except ValueError:
        return None


def dmy(day: str) -> str:
    y, m, d = day.split('-')
    return f'{int(d)}.{int(m)}.{y}'


def cites(text: str):
    """(('vkm', number, day) | ('law', number, year), start, end) for every act citation in a text."""
    for m in CITE_VKM.finditer(text):
        day = iso(m.group(2), m.group(3), m.group(4))
        if day:
            yield ('vkm', m.group(1), day), m.start(), m.end()
    for m in CITE_LAW.finditer(text):
        year = m.group(2) or m.group(5)
        if year:
            yield ('law', m.group(1), year), m.start(), m.end()
    for m in CITE_MIN.finditer(text):
        day = iso(m.group(3), m.group(4), m.group(5))
        if day:
            yield ('udhezim' if m.group(1).lower().startswith('udh') else 'urdher', m.group(2), day), m.start(), m.end()


def ident(a: dict):
    if a['type'] == 'Ligj':
        return ('law', a['number'].split('-')[0], a['date'][:4])
    if a['type'] in MINISTERIAL:
        return (MINISTERIAL[a['type']], a['number'].split('-')[0], a['date'])
    return ('vkm', a['number'], a['date'])


def kind_of(a: dict) -> str | None:
    if a['kind'] != 'Akt bazë' or not a.get('word') or not a['word']['url'].endswith(('.docx', '.doc')):
        return None
    if a['type'] == 'Vendim' and a.get('institution') == 'Këshilli i Ministrave':
        return 'vendim'
    if a['type'] == 'Ligj':
        return 'ligj'
    if a['type'] in MINISTERIAL:
        return MINISTERIAL[a['type']]
    return None


def title_of(a: dict) -> str:
    t = norm(re.sub(r'\s+', ' ', a['title'])).rstrip('.')
    if t.isupper():
        t = t[:1] + t[1:].lower()
    return t


def short_of(title: str) -> str:
    s = re.sub(r'^Për\s+', '', title)
    s = s[:1].upper() + s[1:]
    return s[:120]


def add_days(day: str, n: int) -> str:
    return (dt.date.fromisoformat(day) + dt.timedelta(days=n)).isoformat()


def add_months(day: str, n: int) -> str:
    d = dt.date.fromisoformat(day)
    y, mo = divmod(d.month - 1 + n, 12)
    return d.replace(year=d.year + y, month=mo + 1).isoformat()


def in_force(kind: str, text: str, published: str) -> tuple[str, str]:
    who = WHO[kind]
    found = re.findall(r'\bKy ' + who + r' hyn në fuqi\s*([^\n]*)', text, re.I)
    if not found:
        raise Hold('in_force_clause_missing')
    if len(set(found)) > 1:
        raise Hold('in_force_clause_twice')
    c = found[0].strip()
    c1 = c.rstrip('.').strip()
    fz = r'(?:në|ne)\s+Fletore(?:n)?\s+Zyrtare'
    fz0 = r'(?:(?:në|ne)\s+)?Fletore(?:n)?\s+Zyrtare'
    on_pub = (r'(?:(?:pas|me)\s+(?:botim|publikim)(?:it|in)(?:\s+e\s+tij)?|pasi\s+(?:botohet|publikohet))\s+' + fz0 +
              r'|menjëherë(?:\s*,?\s*(?:dhe\s+)?(?:botohet|publikohet)\s+' + fz0 + ')?')
    # in force on publication, its effects reaching back to a stated day: dated by its entry into force
    m = re.fullmatch(r'(?:' + on_pub + r')\s*,?\s*dhe\s+(?:i\s+)?shtrin\s+efektet(?:\s+financiare)?\s+(?:nga|prej)\s+'
                     r'(?:data\s+|datës\s+)?(\d{1,2}(?:\.\d{1,2}\.\d{4}|\s+[a-zë]+\s+\d{4}))', c1, re.I)
    if m:
        return published, f'"hyn në fuqi {c1}": the publication day (its effects reach back to {m.group(1)})'
    if re.search(r'efekt|zbatohet|fillon|përveç|me përjashtim|deri', c, re.I):
        raise Hold(f'in_force_clause_unhandled:{c[:80]}')
    if re.fullmatch(on_pub, c1, re.I):
        return published, f'"hyn në fuqi {c1}": the publication day'
    m = re.fullmatch(r'(?:më|në)\s+(?:datë|datën)\s+(\d{1,2})\.(\d{1,2})\.(\d{4})(?:\s*,?\s*dhe\s+botohet\s+' + fz0 + ')?', c1, re.I)
    if m:
        day = iso(m.group(1), m.group(2), m.group(3))
        if day and day >= published:
            return day, f'"hyn në fuqi {c1}"'
        raise Hold(f'in_force_day_before_publication:{c1[:60]}')
    if re.fullmatch(r'(?:pas|me)\s+botim(?:it|in)\s+' + fz, c1, re.I) or \
            re.fullmatch(r'(?:ditën e|në ditën e|nga dita e|nga data e|në datën e)\s+botimit(?:\s+' + fz + ')?', c1, re.I):
        return published, f'"hyn në fuqi {c1}": the publication day'
    if re.fullmatch(r'menjëherë(?:\s*,?\s*(?:dhe\s+)?botohet\s+' + fz + r')?(?:\s*,?\s*pas\s+botimit\s+' + fz + ')?', c1, re.I):
        return published, f'"hyn në fuqi {c1}": the publication day'
    m = re.fullmatch(r'(\d+)\s*\(?[a-zë ]*\)?\s+ditë\s+(?:pas|nga)\s+botimit(?:\s+' + fz + ')?', c1, re.I)
    if m:
        return add_days(published, int(m.group(1))), f'"hyn në fuqi {c1}"'
    m = re.fullmatch(r'(\d+)\s+muaj\s+pas\s+botimit(?:\s+' + fz + ')?', c1, re.I)
    if m:
        return add_months(published, int(m.group(1))), f'"hyn në fuqi {c1}"'
    m = re.fullmatch(r'(?:më|nga data|në datën|nga|datë|në)?\s*(\d{1,2})\s+(' + '|'.join(MUAJ) + r')\s+(\d{4})'
                     r'(?:\s*,?\s*dhe\s+botohet\s+' + fz0 + ')?', c1, re.I)
    if m:
        day = iso(m.group(1), str(MUAJ.index(m.group(2).lower()) + 1), m.group(3))
        if day and day >= published:
            return day, f'"hyn në fuqi {c1}"'
        raise Hold(f'in_force_day_before_publication:{c1[:60]}')
    raise Hold(f'in_force_clause_unhandled:{c[:80]}')


def unit(units: dict, order: list, key: str, label: str, kind: str, lines: list[str]) -> str:
    base, i = key, 2
    while key in units:
        key = f'{base}-{i:02d}'
        i += 1
    units[key] = {'label': label, 'kind': kind, 'lines': lines}
    order.append(key)
    return key


def roman(s: str) -> int:
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    n = 0
    for i, ch in enumerate(s):
        v = vals[ch]
        n += -v if i + 1 < len(s) and vals[s[i + 1]] > v else v
    return n


def split(paras: list[str], kind: str, notes: dict | None = None) -> dict:
    """Units: hyrje (header, title, preamble), kreu-NN / neni-NNN or (a decision without articles) pika-NNN, the
    signature or adoption block (zz-nenshkrimi / zz-miratuar) and everything after it (shtojca).
    notes: for a consolidated text, QBZ's note lines ("(Ndryshuar me ...)") are kept out of the text and collected
    here by unit."""
    if notes is not None:
        kept, owner = [], []
        for p in paras:
            if RE_NOTE.match(p):
                owner.append((len(kept), p))
            else:
                kept.append(p)
        paras = kept
    if kind in MINISTERIAL.values():
        # the paragraph after the in-force clause is the signer's office
        clause = next((i for i, p in enumerate(paras) if re.search(r'\bKy ' + WHO[kind] + r' hyn në fuqi', p, re.I)), None)
        foot_at = clause + 1 if clause is not None and clause + 1 < len(paras) and len(paras[clause + 1]) < 120 else None
    else:
        sign = RE_SIGN_VKM if kind == 'vendim' else RE_FOOT_LAW
        foot_at = next((i for i, p in enumerate(paras) if sign.match(p)), None)
    if foot_at is None:
        raise Hold('signature_not_found')
    body, tail = paras[:foot_at], paras[foot_at:]
    has_neni = any(RE_NENI.match(p) for p in body)
    units: dict[str, dict] = {}
    order: list[str] = []
    cur = unit(units, order, 'hyrje', 'Hyrje', 'preamble', [])
    started = kind == 'ligj'
    last_point = 0
    expect_title = False
    where: list[str] = []  # the unit each paragraph of body went to
    op_at = None
    if kind != 'ligj':
        op_at = next((i for i, p in enumerate(body) if re.search(r'\b' + OPERATIVE[kind] + r'\s*:?\s*$', p, re.I)), None)
        if op_at is None:  # letter-spaced ("V E N D O S I:") or third person ("UDHËZON:", "URDHËRON:")
            op_at = next((i for i, p in enumerate(body)
                          if re.search(r'(?:' + OPERATIVE_WIDE[kind] + r'):?$', ''.join(p.split()), re.I)), None)
    for i_p, p in enumerate(body):
        where.append(cur)
        if kind != 'ligj' and not started:
            units[cur]['lines'].append(p)
            if i_p == op_at:
                started = True
                # what the Council decided, until its first numbered point (all of it, when it has none)
                cur = unit(units, order, 'pika-000', 'Vendimi', 'body', [])
            continue
        m_n = RE_NENI.match(p) if has_neni else None
        m_h = RE_HEAD.match(p) if has_neni else None
        m_p = RE_POINT.match(p) if not has_neni and kind != 'ligj' else None
        if m_n:
            n, sub = int(m_n.group(1)), m_n.group(2)
            key, label = f'neni-{n:03d}', f'Neni {n}'
            if sub:
                key, label = f'{key}-{int(sub):02d}', f'{label}/{int(sub)}'
            cur = where[-1] = unit(units, order, key, label, 'art', [f'# {label}'])
            expect_title = True
            continue
        if m_h:
            k, num = m_h.group(1), m_h.group(2)
            cur = where[-1] = unit(units, order, f'{k.lower()}-{roman(num):02d}', f'{k.capitalize()} {num}', 'heading', [p])
            expect_title = True
            continue
        if m_p and int(m_p.group(1)) == last_point + 1:
            last_point += 1
            cur = where[-1] = unit(units, order, f'pika-{last_point:03d}', f'Pika {last_point}', 'point', [p])
            continue
        if expect_title and units[cur]['kind'] in ('art', 'heading') and len(units[cur]['lines']) == 1 \
                and not RE_ITEM.match(p) and len(p) < 200:
            units[cur]['lines'].append(p)
            expect_title = False
            continue
        expect_title = False
        units[cur]['lines'].append(p)
    if kind != 'ligj' and not started:
        raise Hold('vendosi_not_found')
    # The signature: the office line and the name under it (or, for a law, the adoption and promulgation lines).
    foot = [tail[0]]
    i = 1
    if kind != 'ligj':
        while i < len(tail) and i < 2 and len(tail[i]) < 60 and not tail[i].endswith(('.', ':')) \
                and not re.match(r'^(ANEKS|SHTOJC|LIDHJ|TABEL|RREGULLORE|Aneks|Shtojc|Lidhj|Tabel)', tail[i]):
            foot.append(tail[i])
            i += 1
        unit(units, order, 'zz-nenshkrimi', 'Nënshkrimi', 'enactment', ['# Nënshkrimi'] + foot)
    else:
        while i < len(tail) and (RE_FOOT_LAW.match(tail[i]) or (foot[-1].startswith('KRYETAR') and len(tail[i]) < 40
                                                                 and not tail[i].endswith('.'))):
            foot.append(tail[i])
            i += 1
        unit(units, order, 'zz-miratuar', 'Miratimi dhe shpallja', 'enactment', ['# Miratimi dhe shpallja'] + foot)
    if i < len(tail):
        unit(units, order, 'zz-shtojca', 'Shtojca', 'annex', ['# Shtojca'] + tail[i:])
    if not units['hyrje']['lines']:
        raise Hold('no_header')
    if notes is not None:
        tail_units = [k for k in order if k.startswith('zz-')]
        for idx, line in owner:
            # a note follows the provision it annotates: the unit of the paragraph before it
            k = where[idx - 1] if 0 < idx <= len(where) else (tail_units[-1] if tail_units and idx > len(where) else 'hyrje')
            notes.setdefault(k, []).append(line)
    if kind == 'vendim' and not has_neni and last_point == 0 and len(order) < 3:
        pass  # a decision of one unnumbered paragraph: its text stays in hyrje's VENDOSI block and after it
    return {k: {'label': units[k]['label'], 'kind': units[k]['kind'], 'text': '\n'.join(units[k]['lines']) + '\n'}
            for k in order if units[k]['lines']}


def header_ok(kind: str, a: dict, paras: list[str]) -> bool:
    head = ' '.join(paras[:6])
    num = re.escape(a['number'].split('-')[0])
    if kind != 'ligj':
        m = re.search(r'\bNr\.?\s*' + num + r'\b(?:\s*-\s*\d+)?\s*,?\s*' + DATE, head, re.I)
        return bool(m) and iso(m.group(1), m.group(2), m.group(3)) == a['date']
    m = re.search(r'\bNr\.?\s*' + num + r'\s*(?:/\s*(\d{4})|,?\s*' + DATE + ')', head, re.I)
    if not m:
        return False
    if m.group(1):
        return m.group(1) == a['date'][:4]
    return iso(m.group(2), m.group(3), m.group(4)) == a['date']


def label_of(kind: str, a: dict) -> str:
    if kind in MINISTERIAL.values():
        word = 'Udhëzimi' if kind == 'udhezim' else 'Urdhri'
        return f'{word} nr. {a["number"]}, datë {dmy(a["date"])} ({a.get("institution") or ""})'
    if kind == 'vendim':
        return f'Vendimi i Këshillit të Ministrave nr. {a["number"]}, datë {dmy(a["date"])}'
    num = a['number'].split('-')[0]
    return f'Ligji nr. {num}/{a["date"][:4]}' if int(a['date'][:4]) >= 2009 else f'Ligji nr. {num}'


AMBIG: set = set()      # (family, year, number) that QBZ gives to more than one act
PUB_URL: dict = {}      # act slug on main -> its url, so a key already published never changes


def family(x: dict) -> str | None:
    if x['type'] == 'Ligj':
        return 'ligj'
    if x['type'] == 'Vendim' and x.get('institution') == 'Këshilli i Ministrave':
        return 'vendim'
    if x['type'] == 'Vendim' and x.get('institution') == 'Gjykata Kushtetuese':
        return 'vendim-gjk'
    if x['type'] == 'Akt normativ':
        return 'akt-normativ'
    return None


def set_ambiguous(L: list) -> None:
    seen: dict = defaultdict(set)
    for x in L:
        f = family(x)
        if f:
            seen[(f, x['date'][:4], x['number'].split('-')[0] if f != 'vendim' else x['number'].lower())].add(x['date'])
    AMBIG.clear()
    AMBIG.update(k for k, days in seen.items() if len(days) > 1)


def year_key(f: str, x: dict) -> str:
    """<family>-<year>-<number>, or with -<MMDD> when QBZ gives that number in that year to more than one act (a key
    already on main for this very act is kept)."""
    num = x['number'].split('-')[0] if f != 'vendim' else x['number'].lower()
    plain = f'{f}-{x["date"][:4]}-{num}'
    if (f, x['date'][:4], num) not in AMBIG:
        return plain
    url = f'{SITE}{x["eliPath"]}' if x.get('eliPath') else None
    if plain in PUB_URL and PUB_URL[plain] == url:
        return plain
    return f'{plain}-{x["date"][5:7]}{x["date"][8:10]}'


def law_ref(x: dict) -> tuple[str, str, str]:
    """(law key, label, kind) for any QBZ act that changes another."""
    num = x['number'].split('-')[0]
    y = x['date'][:4]
    if x['type'] == 'Ligj':
        return year_key('ligj', x), label_of('ligj', x), 'law'
    if x['type'] == 'Vendim' and x.get('institution') == 'Këshilli i Ministrave':
        return year_key('vendim', x), label_of('vendim', x), 'decree'
    if x['type'] == 'Vendim' and x.get('institution') == 'Gjykata Kushtetuese':
        return year_key('vendim-gjk', x), f'Vendimi i Gjykatës Kushtetuese nr. {num}, datë {dmy(x["date"])}', 'court'
    if x['type'] in MINISTERIAL:
        k = MINISTERIAL[x['type']]
        # numbers repeat across ministries: the QBZ record id keeps two such acts of one day apart
        return f'{k}-{y}-{x["date"][5:7]}{x["date"][8:10]}-{num}-q{x["id"]}', label_of(k, x) + f' [QBZ {x["id"]}]', 'decree'
    if x['type'] == 'Akt normativ':
        return year_key('akt-normativ', x), f'Akti normativ nr. {num}, datë {dmy(x["date"])}', 'decree'
    t = unicodedata.normalize('NFKD', x['type']).encode('ascii', 'ignore').decode().lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return f'{t}-{y}-{x["date"][5:7]}{x["date"][8:10]}-{num}', f'{x["type"]} nr. {num}, datë {dmy(x["date"])} ({x.get("institution") or ""})', 'decree'


def names_act(note: str, x: dict) -> bool:
    """Does a QBZ note name act x ("nr. 77/2024", "nr. 77, datë 13.6.2024")?"""
    num = re.escape(x['number'].split('-')[0])
    d = dt.date.fromisoformat(x['date'])
    return bool(re.search(rf'nr\.?\s*{num}\s*/\s*{d.year}\b', note) or
                re.search(rf'nr\.?\s*{num}\s*,?\s*(?:datë|date|data)\s*0?{d.day}\s*\.\s*0?{d.month}\s*\.\s*{d.year}', note))


def why_changed(key: str, notes: list, x: dict, xtext: str | None) -> str | None:
    """Why a provision changes in a version: a QBZ note naming the changing act, or the changing act naming the
    article, point or annex; None when neither does."""
    if any(names_act(n, x) for n in notes):
        return 'noted'
    if xtext:
        body = '\n'.join(ln for ln in xtext.split('\n') if not RE_NENI.match(ln))
        m = re.match(r'neni-(\d+)', key)
        if m and re.search(rf'\b(?:[Nn]eni|[Nn]enit|[Nn]enin|[Nn]enet|[Nn]eneve)\s+{int(m.group(1))}\b', body):
            return 'article named in the act'
        m = re.match(r'pika-(\d+)$', key)
        if m and int(m.group(1)) and re.search(rf'\b(?:[Pp]ika|[Pp]ikës|[Pp]ikën|[Pp]ikat|[Pp]ikave)\s+{int(m.group(1))}\b', body):
            return 'point named in the act'
        if key == 'zz-shtojca' and re.search(r'([Ss]htojc|[Aa]neks|[Ll]idhj)', xtext):
            return 'annex named in the act'
    return None


def history(cache: Path, memo: Path | None, x: dict, kind: str, byid: dict, published: str, base_paras: list[str],
            laws: dict, decisions: list) -> list[dict]:
    """The act as published, then each QBZ consolidated version (dated by QBZ's validFrom, credited to the act QBZ
    names as changing it); raises Hold when the history is not complete or does not read cleanly."""
    rel = read_json(cache, f'{API}/acts/{x["id"]}/relations') or []
    vs = read_json(cache, f'{API}/acts/{x["id"]}/versions')
    if vs is None:
        raise Hold('versions_not_fetched')
    vs = sorted(vs, key=lambda v: v['versionNo'])
    changes_in = {r['actId'] for r in rel if r.get('type') == 'CHANGES' and r.get('direction') == 'in'}
    by = {(v.get('changedBy') or {}).get('id') for v in vs}
    if None in by:
        raise Hold('version_without_changing_act')
    if not changes_in <= by:
        raise Hold('versions_incomplete:' + ','.join(map(str, sorted(changes_in - by)[:5])))
    day0, how0 = in_force(kind, '\n'.join(base_paras), published)
    prev = split(base_paras, kind)
    if kind == 'ligj' and not any(k.startswith('neni-') for k in prev):
        raise Hold('no_articles')
    g = x['gazette']
    out = [{'from': day0, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'], 'units': prev,
            'credits': {}, 'note': f'As published in the Fletorja Zyrtare nr. {g["number"]}/{g["year"]} ({published}); '
                                   f'in force from {day0}: {how0}.'}]
    last = day0
    for v in vs:
        cb = byid.get(v['changedBy']['id'])
        if TOUCHED is not None:
            TOUCHED.append(f'id:{v["changedBy"]["id"]}')
        if cb is None:
            raise Hold('changing_act_not_listed')
        w = v.get('word') or {}
        if not w.get('url', '').endswith(('.docx', '.doc')) or not v.get('validFrom'):
            raise Hold(f'version_{v["versionNo"]}_no_text_or_day')
        vp = text_of(cache, memo, {'word': w})
        if vp is None:
            raise Hold('version_text_not_fetched')
        notes: dict[str, list[str]] = {}
        units = split(vp, kind, notes)
        # QBZ's validFrom is the changing act's adoption day; the version takes effect when the changing act does.
        cg = cb.get('gazette') or {}
        cgr = read_json(cache, f'{API}/gazettes/{cg.get("year")}/{cg.get("number")}') if cg.get('number') else None
        cpub = ((cgr or {}).get('gazette') or {}).get('publishDate')
        if not cpub or not (cb['date'] <= cpub <= add_days(cb['date'], 120)):
            raise Hold(f'version_{v["versionNo"]}_changing_act_publication_day:{cpub}')
        xt = text_of(cache, memo, cb) if cb.get('word') else None
        xtext = '\n'.join(xt) if xt else None
        if cb['type'] == 'Vendim' and cb.get('institution') == 'Gjykata Kushtetuese':
            day, how = cpub, 'a Constitutional Court decision takes effect on its publication (Kushtetuta, neni 132)'
        elif kind_of(dict(cb, kind='Akt bazë')) in WHO:
            if xtext is None:
                raise Hold(f'version_{v["versionNo"]}_changing_act_text_not_fetched')
            day, how = in_force(kind_of(dict(cb, kind='Akt bazë')), xtext, cpub)
        else:
            raise Hold(f'version_{v["versionNo"]}_changing_act_kind:{cb["type"]}')
        if day < last:
            raise Hold(f'version_{v["versionNo"]}_day_out_of_order:{day}')
        for k in list(units):
            if k in prev and prev[k]['text'] != units[k]['text'] and \
                    ''.join(prev[k]['text'].split()) == ''.join(units[k]['text'].split()):
                units[k] = prev[k]  # differs only in spacing: the earlier text stays
        changed = sorted(k for k in set(prev) | set(units)
                         if (prev.get(k) or {}).get('text') != (units.get(k) or {}).get('text'))
        lk, label, lkind = law_ref(cb)
        laws[lk] = {'label': label, 'title': title_of(cb), 'kind': lkind, 'enacted': cb['date'], 'published': cpub,
                    'url': f'{SITE}{cb["eliPath"]}' if cb.get('eliPath') else None,
                    'temporary_until': None, 'restores': None, 'note': None}
        credits, unexplained = {}, []
        for k in changed:
            if why_changed(k, notes.get(k, []), cb, xtext):
                credits[k] = [lk]
            else:
                unexplained.append(k)
        if changed and len(unexplained) > max(3, len(changed) // 2):
            raise Hold(f'version_{v["versionNo"]}_mostly_unexplained:{len(unexplained)}/{len(changed)}')
        for k in unexplained:
            decisions.append(f'{label_of(kind, x)}: QBZ’s consolidated version {v["versionNo"]} changes '
                             f'{(units.get(k) or prev.get(k))["label"]}, which neither a QBZ note nor {label} names; '
                             f'the change is recorded as unexplained, from the publisher.')
        ver = {'from': day, 'source_url': SITE + w['url'], 'sha256': w['sha256'],
               'changes': {k: units.get(k) for k in changed}, 'credits': credits,
               'note': f'QBZ consolidated version {v["versionNo"]}, after {label} (Fletorja Zyrtare nr. '
                       f'{cg.get("number")}/{cg.get("year")}, {cpub}); in force from {day}: {how}.'}
        if day == last:
            ver['same_day'] = True
        out.append(ver)
        prev, last = units, day
    return out


def changed_cites(text: str) -> list:
    """Acts this text cites as amended or repealed (a change word in the 300 characters after the citation)."""
    out = []
    for ref, _, e in cites(text):
        nxt = NEXT_CITE.search(text, e)
        if STEMS.search(text[e:min(e + 300, nxt.start() if nxt else len(text))]):
            out.append(list(ref))
    return out


def load_results(path: str | None) -> dict:
    """--result-cache: {'cites': {text key: refs}, 'acts': {act id: [record sig, input sigs, result]}}."""
    if path and Path(path).exists():
        import pickle
        try:
            d = pickle.loads(gzip.decompress(Path(path).read_bytes()))
            if d.get('v') == VERSION + CODE_SIG:
                return d
        except Exception:  # noqa: BLE001  (a damaged cache is rebuilt)
            pass
    return {'v': VERSION + CODE_SIG, 'cites': {}, 'acts': {}}


def save_results(path: str | None, rc: dict) -> None:
    if not path:
        return
    import pickle
    tmp = Path(f'{path}.{os.getpid()}.tmp')
    tmp.write_bytes(gzip.compress(pickle.dumps(rc, protocol=pickle.HIGHEST_PROTOCOL), 1))
    os.replace(tmp, path)


def _sig(item: str, byid: dict):
    if item.startswith('id:'):
        r = byid.get(int(item[3:]))
        return json.dumps(r, sort_keys=True, ensure_ascii=False) if r else None
    try:
        st = os.stat(item)
        return (st.st_size, st.st_mtime_ns)
    except OSError:
        return None


def cached_result(rc: dict, x: dict, byid: dict):
    e = rc['acts'].get(x['id'])
    if not e or e[0] != json.dumps(x, sort_keys=True, ensure_ascii=False):
        return None
    if any(_sig(item, byid) != sig for item, sig in e[1]):
        return None
    return e[2]


def store_result(rc: dict, x: dict, byid: dict, files: list, res: tuple) -> None:
    items = list(dict.fromkeys(files))
    rc['acts'][x['id']] = [json.dumps(x, sort_keys=True, ensure_ascii=False), [(i, _sig(i, byid)) for i in items], res]


PARTIAL = re.compile(r'\b(pika|pikat|pikës|pikën|nen|neni|nenet|nenin|nenit|neneve|shkronj\w*|paragraf\w*|kre\w*|'
                     r'aneks\w*|lidhj\w*|shtojc\w*|fjal\w*|togfjal\w*|alinea\w*|rreshti\w*|kapitull\w*|'
                     r'seksion\w*|tabel\w*|ndryshim\w*)\b', re.I)


def repeal_version(cache: Path, memo: Path | None, x: dict, rx: dict | None, versions: list, laws: dict) -> dict:
    """The repeal QBZ links (REPEALS): an empty version on the day the repealing act took effect, credited to it.
    Only a whole repeal: the repealing act's own text must cite this act in a paragraph that says "shfuqiz..." with no
    provision named before the citation."""
    if TOUCHED is not None and rx:
        TOUCHED.append(f'id:{rx["id"]}')
    if rx is None or not rx.get('word'):
        raise Hold('repealer_not_listed')
    rk = kind_of(dict(rx, kind='Akt bazë'))
    if rk not in WHO:
        raise Hold(f'repealer_kind:{rx["type"]}')
    rp = text_of(cache, memo, rx)
    if rp is None:
        raise Hold('repealer_text_not_fetched')
    ref = ident(x)
    whole = False
    for para in rp:
        for cref, st, en in cites(para):
            if cref != ref:
                continue
            head = para[:st]
            head = head[max(head.rfind('. '), head.rfind(';'), head.rfind(':')) + 1:]
            if re.search(r'shfuqiz', para, re.I) and not PARTIAL.search(head) and \
                    not PARTIAL.search(para[en:en + 40].split(',')[0]):
                whole = True
    if not whole:
        raise Hold('repeal_not_whole_or_not_cited')
    rg = rx.get('gazette') or {}
    rgr = read_json(cache, f'{API}/gazettes/{rg.get("year")}/{rg.get("number")}') if rg.get('number') else None
    rpub = ((rgr or {}).get('gazette') or {}).get('publishDate')
    if not rpub or not (rx['date'] <= rpub <= add_days(rx['date'], 120)):
        raise Hold(f'repealer_publication_day:{rpub}')
    day, how = in_force(rk, '\n'.join(rp), rpub)
    last = versions[-1]['from']
    if day < last:
        raise Hold(f'repeal_before_last_version:{day}')
    lk, label, lkind = law_ref(rx)
    laws[lk] = {'label': label, 'title': title_of(rx), 'kind': lkind, 'enacted': rx['date'], 'published': rpub,
                'url': f'{SITE}{rx["eliPath"]}' if rx.get('eliPath') else None,
                'temporary_until': None, 'restores': None, 'note': None}
    held: dict = {}
    for v in versions:
        if 'units' in v:
            held = dict(v['units'])
        for k, u in (v.get('changes') or {}).items():
            if u is None:
                held.pop(k, None)
            else:
                held[k] = u
    ver = {'from': day, 'source_url': SITE + rx['word']['url'], 'sha256': rx['word']['sha256'], 'units': {},
           'credits': {k: [lk] for k in sorted(held)},
           'note': f'Repealed by {label} (Fletorja Zyrtare nr. {rg.get("number")}/{rg.get("year")}, {rpub}); '
                   f'in force from {day}: {how}.'}
    if day == last:
        ver['same_day'] = True
    return ver


def compute(cache: Path, memo: Path | None, x: dict, kind: str, hist: bool, byid: dict) -> tuple:
    """The act's part, slug, law record, act record and (for a history) the changing acts' records and decisions;
    raises Hold. Reads only x's own inputs (recorded in TOUCHED for --result-cache)."""
    hlaws: dict = {}
    hdec: list = []
    rel = read_json(cache, f'{API}/acts/{x["id"]}/relations')
    if rel is None:
        raise Hold('relations_not_fetched')
    repealers = sorted({r['actId'] for r in rel if r.get('direction') == 'in' and r.get('type') == 'REPEALS'})
    if not hist and any(r.get('direction') == 'in' and r.get('type') == 'CHANGES' for r in rel):
        raise Hold('qbz_changed_or_repealed')
    if len(repealers) > 1:
        raise Hold('repealed_by_several:' + ','.join(map(str, repealers[:5])))
    if True:
        if True:
            g = read_json(cache, f'{API}/gazettes/{x["gazette"]["year"]}/{x["gazette"]["number"]}')
            if g is None:
                raise Hold('gazette_not_fetched')
            published = (g.get('gazette') or {}).get('publishDate')
            if not published:
                raise Hold('publication_day_missing')
            if not (x['date'] <= published <= add_days(x['date'], 120)):
                raise Hold(f'publication_day_inconsistent:{published} vs {x["date"]}')
            paras = text_of(cache, memo, x)
            if paras is None:
                raise Hold('text_not_fetched')
            if any(RE_NOTE.match(p) for p in paras):
                raise Hold('qbz_amendment_notes')
            if not header_ok(kind, x, paras):
                raise Hold('header_mismatch')
            if hist:
                versions = history(cache, memo, x, kind, byid, published, paras, hlaws, hdec)
            else:
                text = '\n'.join(paras)
                day, how = in_force(kind, text, published)
                units = split(paras, kind)
                if kind == 'ligj' and not any(k.startswith('neni-') for k in units):
                    raise Hold('no_articles')
                if repealers:  # as published, then the repeal
                    g0 = x['gazette']
                    versions = [{'from': day, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'],
                                 'units': units, 'credits': {},
                                 'note': f'As published in the Fletorja Zyrtare nr. {g0["number"]}/{g0["year"]} '
                                         f'({published}); in force from {day}: {how}.'}]
            if repealers:
                versions.append(repeal_version(cache, memo, x, byid.get(repealers[0]), versions, hlaws))
                hist = True
        year = x['date'][:4]
        slug = year_key(kind, x) if kind in ('vendim', 'ligj') else \
            f'{kind}-{year}-{x["date"][5:7]}{x["date"][8:10]}-{x["number"].split("-")[0]}'
        title = title_of(x)
        url = f'{SITE}{x["eliPath"]}' if x.get('eliPath') else None
        law = {'label': label_of(kind, x), 'title': title, 'kind': 'law' if kind == 'ligj' else 'decree',
               'enacted': x['date'], 'published': published, 'url': url, 'temporary_until': None,
               'restores': None, 'note': None}
        g = x['gazette']
        if hist:
            return (f'{HIST_PART[kind]}-{year}', slug, law,
                    {'slug': slug, 'short': short_of(title), 'title': title, 'url': url,
                     'first_law': slug, 'earlier_laws': [], 'versions': versions}, hlaws, hdec)
        return (f'{PART[kind]}-{year}', slug, law, {
            'slug': slug, 'short': short_of(title), 'title': title, 'url': url, 'first_law': slug,
            'earlier_laws': [],
            'versions': [{'from': day, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'],
                          'units': units, 'credits': {},
                          'note': f'As published in the Fletorja Zyrtare nr. {g["number"]}/{g["year"]} ({published}); '
                                  f'in force from {day}: {how}. QBZ links no act as changing or repealing it.'}]}, {}, [])



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', required=True)
    ap.add_argument('--published', help="the repository's data/versions.json: laws it holds under earlier names")
    ap.add_argument('--retrieved', default=None)
    ap.add_argument('--memo', help='folder for extracted paragraphs (speeds up repeat runs)')
    ap.add_argument('--report')
    ap.add_argument('--out', help='write the parts here instead of corpus.d (a scratch run)')
    ap.add_argument('--result-cache', help='file keeping per-text and per-act results between runs (same output)')
    ap.add_argument('--publish-ministerial', action='store_true', help='also mark instructions and orders (44-47) as verified')
    ap.add_argument('--publish-history', action='store_true',
                    help='also mark the parts with consolidated histories (42-, 43-) as verified')
    a = ap.parse_args()
    if a.out:
        global PARTS
        PARTS = Path(a.out)
    cache = Path(a.cache)
    memo = Path(a.memo) if a.memo else None
    L = listing(cache)
    set_ambiguous(L)
    retrieved = a.retrieved or max((x['date'] for x in L), default='')
    held_old: set[tuple[str, str]] = set()
    if a.published and Path(a.published).exists():
        for act in json.loads(Path(a.published).read_text(encoding='utf-8')).get('acts', []):
            PUB_URL[act['slug']] = act.get('url')
            m = re.fullmatch(r'ligji-(\d+)-(\d{4})', act['slug'])
            if m:
                held_old.add((m.group(1), m.group(2)))
            for v in act.get('versions', [])[:1]:
                pass
    labels: dict[str, str] = {}  # law key -> label across every part: one key never names two acts
    for p in sorted((HERE / 'corpus.d').glob('*.json')):
        if p.name[:2] in ('40', '41', '42', '43', '44', '45', '46', '47'):
            continue
        d = json.loads(p.read_text(encoding='utf-8'))
        labels.update({k: v['label'] for k, v in d.get('laws', {}).items()})
        for key in d.get('laws', {}):
            m = re.fullmatch(r'ligji-(\d+)-(\d{4})', key)
            if m and any(x.get('first_law') == key for x in d.get('acts', [])):
                held_old.add((m.group(1), m.group(2)))
        for s in d.get('sources', []):
            m = re.search(r'/acts/(\d+)/', s.get('url', ''))
            if m:
                held_old.add(('id', m.group(1)))

    # Citations that say an act was changed: other acts' titles, then the texts held here.
    named: dict[tuple, set[int]] = defaultdict(set)
    for x in L:
        t = norm(x['title'])
        if x['kind'] != 'Akt bazë' or CHANGE_TITLE.search(t):
            for ref, _, _ in cites(t):
                named[ref].add(x['id'])
    count = defaultdict(int)
    for x in L:
        if kind_of(x):
            count[(kind_of(x), ident(x))] += 1
    rc = load_results(a.result_cache)
    cited_changed: dict[tuple, set[int]] = defaultdict(set)
    for x in L:
        if not kind_of(x):
            continue
        key = f'{VERSION}:{x["word"]["sha256"]}'
        refs = rc['cites'].get(key)
        if refs is None:
            ps = text_of(cache, memo, x)
            if ps is None:
                continue
            refs = changed_cites('\n'.join(ps))
            rc['cites'][key] = refs
        for ref in refs:
            cited_changed[tuple(ref)].add(x['id'])

    parts: dict[str, dict] = defaultdict(lambda: {'laws': {}, 'acts': []})
    holds = []
    byid = {x['id']: x for x in L}
    for x in L:
        kind = kind_of(x)
        if not kind:
            continue
        ref = ident(x)
        hist = bool(x.get('versions'))
        hlaws: dict = {}
        hdec: list = []
        try:
            if ('id', str(x['id'])) in held_old or (kind == 'ligj' and (ref[1], ref[2]) in held_old):
                continue  # on main already, under its earlier name
            if count[(kind, ref)] > 1:
                raise Hold('duplicate_number')
            if kind == 'ligj':
                m = BUDGET.search(x['title'])
                if m and m.group(4) < retrieved[:4]:
                    raise Hold('spent_budget_law')
            if not hist:
                own = {x['id']}
                if (named.get(ref, set()) | cited_changed.get(ref, set())) - own:
                    rel0 = read_json(cache, f'{API}/acts/{x["id"]}/relations') or []
                    own |= {r['actId'] for r in rel0 if r.get('direction') == 'in' and r.get('type') == 'REPEALS'}
                if named.get(ref, set()) - own:
                    raise Hold('named_in_changing_title:' + ','.join(map(str, sorted(named[ref] - own)[:5])))
                if cited_changed.get(ref, set()) - own:
                    raise Hold('cited_as_changed:' + ','.join(map(str, sorted(cited_changed[ref] - own)[:5])))
            res = cached_result(rc, x, byid)
            if res is None:
                global TOUCHED
                TOUCHED = []
                try:
                    res = ('ok',) + compute(cache, memo, x, kind, hist, byid)
                except Hold as h:
                    res = ('hold', str(h))
                files, TOUCHED = TOUCHED, None
                store_result(rc, x, byid, files, res)
            if res[0] == 'hold':
                raise Hold(res[1])
        except Hold as h:
            holds.append({'id': x['id'], 'kind': kind, 'number': x['number'], 'date': x['date'],
                          'title': x['title'][:160], 'reason': str(h)})
            continue
        _, part_name, slug, law, act, hlaws, hdec = res
        clash = [k for k, v in [(slug, law)] + list((hlaws or {}).items()) if labels.get(k, v['label']) != v['label']]
        if clash:
            holds.append({'id': x['id'], 'kind': kind, 'number': x['number'], 'date': x['date'],
                          'title': x['title'][:160], 'reason': 'law_key_clash:' + ','.join(clash[:3])})
            continue
        labels[slug] = law['label']
        labels.update({k: v['label'] for k, v in (hlaws or {}).items()})
        part = parts[part_name]
        part['laws'][slug] = law
        if hlaws:
            part['laws'].update(hlaws)
        if part_name[:2] in ('42', '43', '46', '47'):
            part.setdefault('extra_decisions', []).extend(hdec)
        part['acts'].append(act)
    save_results(a.result_cache, rc)
    PARTS.mkdir(exist_ok=True)
    written = []
    for name in sorted(parts):
        p = parts[name]
        p['laws'] = dict(sorted(p['laws'].items()))
        p['acts'].sort(key=lambda r: (r['versions'][0]['from'], r['slug']))
        vkm = not name.startswith('41-')
        what = {'40': 'decisions of the Council of Ministers', '41': 'laws', '44': 'instructions (udhëzime)',
                '45': 'orders (urdhra)', '42': 'decisions of the Council of Ministers', '43': 'laws',
                '46': 'instructions (udhëzime)', '47': 'orders (urdhra)'}[name[:2]]
        p['sources'] = [{
            'name': 'Qendra e Botimeve Zyrtare (qbz.gov.al): ' +
                    f'{what} in force, as published',
            'url': f'{API}/acts', 'retrieved': retrieved, 'licence': LICENCE,
            'notes': 'Each act’s .docx as published in the Fletorja Zyrtare, its issue’s publication day and QBZ’s '
                     'relations (no act changing or repealing it).'}]
        p['decisions'] = [
            f'One of these {what}' +
            ' is published here only when QBZ links no act as changing or repealing it, no other act’s title in '
            'QBZ’s listing cites it as changed, and no text held here cites it as amended or repealed; its one '
            'version is the text as published in the Fletorja Zyrtare.',
            ('Its in-force day: the publication day of its Fletorja Zyrtare issue when its clause says “hyn në fuqi '
             'pas botimit” or “menjëherë” (Kushtetuta, neni 117, pika 1: the normative acts of the Council of '
             'Ministers and of ministers take legal force only once published), N days after it for “N ditë pas '
             'botimit”, or the day it names. A clause that puts it in force on publication and extends its effects back to an earlier day (“i shtrin efektet nga ...”) dates it by its entry into force, the publication day, and the version note gives the day of effect; any other clause holds it back.') if vkm else
            ('Its in-force day comes from its own clause, counted from the publication day of its Fletorja Zyrtare '
             'issue (“menjëherë”: the publication day, Kushtetuta, neni 84, pika 4); any other clause holds it back.'),
            'The publication day of an issue is QBZ’s gazette record; an act whose issue day is missing, before its '
            'adoption or more than 120 days after it is held back.']
        if name[:2] in ('42', '43', '46', '47'):
            p['sources'] = [{
                'name': f'Qendra e Botimeve Zyrtare (qbz.gov.al): {what} as published and their consolidated versions',
                'url': f'{API}/acts', 'retrieved': retrieved, 'licence': LICENCE,
                'notes': 'Each act’s .docx as published, its issue’s publication day, QBZ’s consolidated versions '
                         '(/acts/{id}/versions: one .docx per version, its validFrom day and the act that changed '
                         'it) and the changing acts’ texts.'}]
            p['decisions'] = [
                'The first version is the act as published in the Fletorja Zyrtare, in force from the day its own '
                'clause gives (counted from its issue’s publication day, as for acts without versions).',
                'Each later version is QBZ’s consolidated text, credited to the act QBZ names as having changed it and '
                'in force from the day that act took effect: its own clause counted from its issue’s publication day '
                '(the same rules as above), or for a Constitutional Court decision its publication day (Kushtetuta, '
                'neni 132). QBZ’s validFrom is the changing act’s adoption day and is not used as an in-force day. '
                'A version made by any other kind of act holds the act back. QBZ’s notes (“Ndryshuar me ...”) are kept out of '
                'the text. A provision is credited when a note on it or the changing act’s own text names it; any '
                'other change is recorded as unexplained. A provision whose words differ only in spacing keeps the '
                'earlier words.',
                'An act is published with its history only when every act QBZ links as changing it has a '
                'consolidated version, no act repeals it, its versions are in date order, and no version is mostly '
                'unexplained.'] + p.pop('extra_decisions', [])
        p['ai_use'] = ['none']
        f = PARTS / f'{name}.json'
        data = json.dumps(p, ensure_ascii=False, indent=1) + '\n'
        if not f.exists() or f.read_text(encoding='utf-8') != data:
            tmp = f.with_suffix(f'.{os.getpid()}.tmp')
            tmp.write_text(data, encoding='utf-8', newline='\n')
            for attempt in range(20):  # a reader (the publishing loop) may hold the part open for a moment
                try:
                    tmp.replace(f)
                    break
                except PermissionError:
                    import time
                    time.sleep(0.5)
            else:
                tmp.unlink(missing_ok=True)
                raise SystemExit(f'could not replace {f}')
        # Verified: every act has units, one version, a day on or after adoption; the part reads back identically.
        ok = all(r['versions'][0]['units'] and r['versions'][0]['from'] >= p['laws'][r['slug']]['enacted']
                 for r in p['acts']) and json.loads(f.read_text(encoding='utf-8')) == p
        pub = PARTS / f'{name}.PUBLISH'
        if ok and (name[:2] not in ('42', '43', '46', '47') or a.publish_history) and \
                (name[:2] not in ('44', '45', '46', '47') or a.publish_ministerial):
            msg = (f'{name}: {len(p["acts"])} acts as published, each checked by parse_acts.py against QBZ’s '
                   f'relations, listing titles and the texts held (no change or repeal found).\n')
            if not pub.exists() or pub.read_text(encoding='utf-8') != msg:
                pub.write_text(msg, encoding='utf-8', newline='\n')
        elif pub.exists():
            pub.unlink()
        written.append((name, len(p['acts'])))
    if a.report:
        Path(a.report).write_text(''.join(json.dumps(h, ensure_ascii=False) + '\n' for h in holds), encoding='utf-8')
    reasons = defaultdict(int)
    for h in holds:
        reasons[h['reason'].split(':')[0]] += 1
    print(json.dumps({'published': sum(n for _, n in written), 'held': len(holds), 'held_by_reason': dict(reasons),
                      'parts': len(written)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
