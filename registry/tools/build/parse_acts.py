"""Albania: laws, Council of Ministers decisions and acts with the force of law, instructions and orders, from QBZ.

Reads only a local copy of Qendra e Botimeve Zyrtare's open API (qbz.gov.al/api/v1) and writes corpus.d parts
(SCHEMA.md). Deterministic: the same inputs give the same bytes. No network.

    python -X utf8 parse_acts.py --cache <folder> [--published <data/versions.json>] [--retrieved YYYY-MM-DD]
                                 [--memo <folder>] [--report holds.jsonl] [--publish-history] [--publish-ministerial]

The local copy (--cache) holds each response gzip'd at <sha256(url)[:2]>/<sha256(url)>.gz: the act listing
(/acts?size=100&page=N), each act's relations (/acts/{id}/relations) and versions (/acts/{id}/versions), each
Fletorja Zyrtare issue record (/gazettes/{year}/{number}), the PDF of an issue whose day needs checking, and each text,
whose .docx is kept as its word/document.xml (the .docx bytes were checked against the sha256 that names them in QBZ's
URL, so that hash is the source hash); a legacy .doc is kept as the text `antiword -m UTF-8.txt -w 0` gives for it
(one paragraph per line), after the same check.

What becomes an act here: a base act ("Akt bazë") of these kinds, slug <kind>-<year>-<id>:
- a law of the Assembly (Ligj): ligj-<year>-<number>;
- a decision of the Council of Ministers (Vendim, Këshilli i Ministrave): vendim-<year>-<number>;
- an act with the force of law of the Council of Ministers (Akt normativ, Kushtetuta, neni 101):
  aktnormativ-<year>-<number>, only when a law in QBZ's listing approves it within 45 days (otherwise it lost its
  force from the start);
- a normative decree of the President (Dekret on the organisation of the courts: districts, territorial jurisdiction,
  number of judges, special sections, the start of new courts): dekret-<year>-<number>; individual decrees are left out;
- an instruction (Udhëzim) or an order (Urdhër) of a minister or another body: udhezim-/urdher-<year>-<MMDD>-<number>
  (numbers repeat across ministries; the adoption day keeps them apart, a number N-1, N-2 ... given to acts of one
  day keeps its suffix, and any other clash holds both).

Without consolidated versions in QBZ, its one version is the text as published, in force from the day its own clause
gives, counted from the publication day of its Fletorja Zyrtare issue: "hyn në fuqi pas botimit" or "menjëherë" = the
publication day (laws: Kushtetuta, neni 84, pika 4; the normative acts of the Council of Ministers and of ministers:
neni 117, pika 1, legal force only once published), "N ditë / N muaj / N vjet pas botimit" = that much later, "të
nesërmen e botimit" = the day after, or the calendar day it names (not before publication); a clause that also says
its effects reach back to or start on a day ("i shtrin / i fillon efektet nga ...") is dated by its entry into force
and the note gives that day; a law without any in-force clause enters into force 15 days after publication (neni 84,
pika 3). Misspellings of the clause's words are read (in_force_more) only where the strict forms read nothing. It is
held back, not published, when any of these is true (the reason goes to the report):
- QBZ links an act as changing it (relations CHANGES, direction in);
- the title of another act in QBZ's listing cites it ("vendimin nr. N, datë D", "ligjin nr. N/YYYY", "udhëzimin nr.
  N, datë D", "aktin normativ nr. N, datë D") and that act changes, adds to, corrects or repeals something (an act
  cited as the one that made an earlier change, as a basis, or as the approver of an agreement or contract is not
  the act changed);
- a text held here cites it and a change word follows the citation in its own paragraph, outside the cited title
  ("i ndryshuar", "shfuqizohet", ...); or, for plural and qualified citations ("Vendimet nr. A, ..., nr. B",
  "Urdhri i ministrit ... nr. N"), "i ndryshuar / u shfuqizua" right after it or a finite verb right after the list;
  or a finite change verb before the citation in its own clause ("Shfuqizohet vendimi nr. ...") or in the opening
  line of the list that holds it ("Shfuqizohen: a) ..."), not in a title or a plan of draft acts;
- two QBZ records give the same kind, number and year (day, for instructions and orders);
- its issue's day cannot be confirmed: QBZ's record is missing or before the adoption or more than 120 days after it,
  and neither the issue's own masthead (page 1 of its PDF: a full day) nor, where the masthead prints only a month or
  the issue is an "Ekstra" one (some print acts left unpublished at the time), its colophon ("Doli nga shtypi më
  D.M.YYYY": QBZ's own day, or a day in the masthead's month) dates it; or the issue's contents do not list the act;
  or the act predates the 1998 Constitution; or it was printed that way more than 120 days after adoption or in an
  Ekstra issue and its in-force clause is a bare "menjëherë" rather than counting from publication or naming a day;
- the text's own header does not give the record's number and date, or carries QBZ's amendment notes;
- its in-force clause is missing or not one of the forms above;
- (laws) the repository already holds it under its earlier name (ligji-<number>-<year>), or it is an annual budget
  law for a year before the retrieval year.

A repeal (QBZ relation REPEALS, or the repealing act's own text alone when every act citing this one as changed
repeals it as a whole there) adds a last, empty version on the day the repealing act took effect, credited to it.

With consolidated versions (QBZ /acts/{id}/versions, each naming the act that changed it), the act is published with
its history only when every act QBZ links as changing it has a version: first the text as published (dated as above),
then each consolidated text, credited to the changing act and in force from the day that act took effect (its own
clause from its issue's publication day; a Constitutional Court decision on publication, Kushtetuta, neni 132; an act
with the force of law only when approved in time; any other kind of changing act holds the act). QBZ's validFrom is
the changing act's adoption day, not an in-force day, and is not used. QBZ's notes are kept out of the text; a changed
provision is credited when a note on it or the changing act's text names it, otherwise it is recorded as unexplained
(publisher); a version mostly unexplained holds the act. Parts: 40-vendime, 41-ligje, 44-udhezime, 45-urdhra,
48-akte-normative (as published) and 42-, 43-, 46-, 47-, 49- (with histories), one per year; <part>.PUBLISH marks a
part checked (histories and instructions/orders only with the flags).
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
RE_SIGN_PRES = re.compile(r'^PRESIDENTI(?:\s+I\s+REPUBLIKËS(?:\s+SË\s+SHQIPËRISË)?)?\s*$', re.I)
# read only when the strict forms find no signature: the Prime Minister's office misspelt, with a Cyrillic "І" or run
# together with the name ("KRYEMINISTRI Sali Berisha"); a law's adoption lines with "dekret" or a letter-spaced
# "K R Y E T A R I"
RE_SIGN_VKM_LOOSE = re.compile(r'^(?:P\.\s*|Z\.\s*|ZV\.?\s*|ZËVENDËS\s*)?K\s*R?\s*Y\s*E\s*M\s*I\s*N\s*[A-ZËÇ]{0,8}\.?'
                               r'(?P<name>(?:\s+[A-ZËÇ][a-zëç]+){1,3})?$', re.I)
RE_FOOT_LAW_LOOSE = re.compile(r'^(Miratuar m[ëё] dat[ëё]|Miratuar n[ëё] dat[ëё]n|Shpallur me dekret(?:in)?\b|'
                               r'K\s*R\s*Y\s*E\s*T\s*A\s*R\s*(?:E|I)?\s*$)')
STEMS = re.compile(r'(ndrysh|shfuqiz|shtes|zëvendës|korrigj|pezull)', re.I)
CHANGE_TITLE = re.compile(r'(ndrysh|shfuqiz|shtes|zëvendës|korrigj|pezull|ndreqje)', re.I)
BUDGET = re.compile(r'buxhet\w* (e |të )?(shtetit )?(të |e )?vitit (\d{4})', re.I)
DATE = r'(?:datë|date|data|dt\.?)\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})'
CITE_VKM = re.compile(r'\b(?:vendim(?:i|in|it)?|VKM(?:-?(?:në|ja|së|ve))?)\s+(?:e\s+)?(?:Këshillit të Ministrave\s+)?'
                      r'nr\.?\s*(\d+(?:-\d+)?)\s*,?\s*' + DATE, re.I)
CITE_LAW = re.compile(r'\bligj(?:i|in|it)?\s+nr\.?\s*(\d+)\s*(?:/\s*(\d{4})|,?\s*' + DATE + ')', re.I)
PART = {'vendim': '40-vendime', 'ligj': '41-ligje', 'udhezim': '44-udhezime', 'urdher': '45-urdhra',
        'aktnormativ': '48-akte-normative', 'dekret': '50-dekrete'}
HIST_PART = {'vendim': '42-vendime-histori', 'ligj': '43-ligje-histori', 'udhezim': '46-udhezime-histori',
             'urdher': '47-urdhra-histori', 'aktnormativ': '49-akte-normative-histori', 'dekret': '51-dekrete-histori'}
OUR_PARTS = ('40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51')
HIST_PARTS = ('42', '43', '46', '47', '49', '51')
# a decree of the President is published only when it is normative: the organisation of the courts (districts, their
# territorial jurisdiction and seats, the number of judges, special sections, the start of new courts); individual
# decrees (citizenship, appointments, honours, pardons, promulgation of laws ...) are not acts in force of that kind
DEKRET_NORMATIVE = re.compile(r'KRIJIMIN E RRETHEVE|KOMPETENCAVE TOKËSORE|NUMRIT TË GJYQTARËVE|SEKSIONEVE|'
                              r'FILLIMIN E FUNKSIONIMIT TË GJYKATAVE', re.I)
MINISTERIAL = {'Udhëzim': 'udhezim', 'Urdhër': 'urdher'}  # instructions and orders (ministers and other bodies)
WHO = {'vendim': 'vendim', 'ligj': 'ligj', 'udhezim': 'udhëzim', 'urdher': 'urdh[eë]r', 'aktnormativ': 'akt normativ',
       'dekret': 'dekret'}
OPERATIVE_WIDE = {'vendim': r'(?<![a-zë])VENDOSI|^VENDOS', 'udhezim': r'(?<![a-zë])UDHËZO[JN]|^UDHËZOJ',
                  'urdher': r'(?<![a-zë])URDHËRO[JN]|^URDHËROJ', 'aktnormativ': r'(?<![a-zë])VENDOSI|^VENDOS',
                  'dekret': r'(?<![a-zë])DEKRETOJ|^DEKRETOJ'}
OPERATIVE = {'vendim': r'VENDOSI', 'udhezim': r'UDHËZOJ', 'urdher': r'URDHËROJ', 'aktnormativ': r'VENDOSI',
             'dekret': r'DEKRETOJ'}
# a joint instruction or order speaks in the plural, and some bodies use another operative verb of the same family
OPERATIVE_MIN_ANY = r'(?:UDHËZO(?:J|N|JMË|JNË)|URDHËRO(?:J|N|JMË|JNË)|VENDOS(?:A|I|ËM|IN))'
CITE_MIN = re.compile(r'\b(udhëzim|urdh[eë]r|urdhr)(?:i|in|it)?\s+(?:e\s+)?nr\.?\s*(\d+)\s*,?\s*' + DATE, re.I)
# an act with the force of law of the Council of Ministers (Kushtetuta, neni 101)
CITE_DEK = re.compile(r'\bdekret(?:i|in|it)?\s+(?:(?:i|të)\s+Presidentit(?:\s+të\s+Republikës)?\s*,?\s*)?(?:nr\.?\s*)?'
                      r'(\d+)\s*,?\s*' + DATE, re.I)
CITE_AN = re.compile(r'\bakt(?:i|in|it)?\s+normativ(?:\s*,\s*|\s+)(?:me\s+fuqinë\s+e\s+ligjit\s*,?\s*)?'
                     r'(?:të\s+Këshillit\s+të\s+Ministrave\s*,?\s*)?nr\.?\s*(\d+)\s*,?\s*' + DATE, re.I)
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
    for m in CITE_AN.finditer(text):
        day = iso(m.group(2), m.group(3), m.group(4))
        if day:
            yield ('aktnormativ', m.group(1), day), m.start(), m.end()
    for m in CITE_DEK.finditer(text):
        day = iso(m.group(2), m.group(3), m.group(4))
        if day:
            yield ('dekret', m.group(1), day), m.start(), m.end()


def ident(a: dict):
    if a['type'] == 'Ligj':
        return ('law', a['number'].split('-')[0], a['date'][:4])
    if a['type'] in MINISTERIAL:
        return (MINISTERIAL[a['type']], a['number'].split('-')[0], a['date'])
    if a['type'] == 'Akt normativ':
        return ('aktnormativ', a['number'].split('-')[0], a['date'])
    if a['type'] == 'Dekret':
        return ('dekret', a['number'].split('-')[0], a['date'])
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
    if a['type'] == 'Akt normativ':
        return 'aktnormativ'
    if a['type'] == 'Dekret' and DEKRET_NORMATIVE.search(norm(re.sub(r'\s+', ' ', a['title'])).upper()):
        return 'dekret'
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
    try:
        return d.replace(year=d.year + y, month=mo + 1).isoformat()
    except ValueError:  # "N muaj pas botimit" from a day the later month lacks (31 → 30): ambiguous, held
        raise Hold(f'in_force_month_end:{day}+{n} months') from None


def in_force(kind: str, text: str, published: str) -> tuple[str, str]:
    """The in-force day: the forms read by in_force_strict, then (only when those find none) the further forms of
    in_force_more."""
    try:
        return in_force_strict(kind, text, published)
    except Hold as h:
        why = str(h)
        if why != 'in_force_clause_missing' and not why.startswith('in_force_clause_unhandled'):
            raise
        r = in_force_more(kind, text, published)
        if r is None:
            raise
        return r


ACT_WORD = r'(?:vendim|udhëzim|udhezim|urdh[eë]r|akt\s+normativ|ligj)'
WHO_LOOSE = {'vendim': r'vend(?:im|imi|imit|in|m)', 'ligj': r'ligj(?:i)?', 'udhezim': r'udh[eë]zim(?:i)?',
             'urdher': r'urdh(?:[eë]r|ri)', 'aktnormativ': r'akt\s*norm\w*', 'dekret': r'dekret(?:i)?'}
NUMWORD = {'një': 1, 'dy': 2, 'tre': 3, 'tri': 3, 'katër': 4, 'pesë': 5, 'gjashtë': 6, 'shtatë': 7, 'tetë': 8,
           'nëntë': 9, 'dhjetë': 10, 'pesëmbëdhjetë': 15, 'njëzet': 20, 'tridhjetë': 30, 'gjashtëdhjetë': 60}


def in_force_more(kind: str, text: str, published: str) -> tuple[str, str] | None:
    """Clauses in_force_strict does not read: its own word misspelt ("Ku", "nё", "ne"), another act word ("Ky vendim"
    in an order) when that is the text's only clause and its last paragraph or the one before a short signature line,
    quotes or typos around "Fletoren Zyrtare", the day after publication, months or years in words, "i fillon efektet
    nga X", a day without "datë"; a law without any clause enters into force 15 days after its publication
    (Kushtetuta, neni 84, pika 3). None: still not read."""
    paras = text.split('\n')
    found = re.findall(r'\b(?:Ky|Ku)\s+' + WHO[kind] + r'\s+hyn\s+n[eëё]\s+fuqi\s*([^\n]*)', text, re.I)
    if not found:  # the act's own word misspelt ("Ky vendm", "Ky aktnormativ"), or "Ky X botohet ... dhe hyn në fuqi ..."
        found = re.findall(r'\b(?:Ky|Ku)\s+' + WHO_LOOSE[kind] + r'\s*,?\s+(?:(?:botohet|publikohet)\s+në\s+Fletore'
                           r'(?:n|s)?\s+Zyrtare\s+dhe\s+)?hyn\s+n[eëё]\s+fuqi\s*([^\n]*)', text, re.I)
    if not found:  # "Udhëzimi hyn në fuqi ..." opening its own paragraph (after its number)
        found = re.findall(r'(?:^|\n)\s*(?:\d+\s*[.)]\s*|[IVX]+\.\s*)?' + WHO_LOOSE[kind] + r'\s+hyn\s+n[eëё]\s+fuqi\s*'
                           r'([^\n]*)', text, re.I)
    if not found:
        hits = [(i, m) for i, p in enumerate(paras)
                for m in [re.search(r'\b(?:Ky|Ku)\s+' + ACT_WORD + r'(?:i)?\s+hyn\s+n[eëё]\s+fuqi\s*(.*)$', p, re.I)] if m]
        if len({m.group(1).strip() for _, m in hits}) == 1:
            i = hits[-1][0]
            if i == len(paras) - 1 or (len(paras[i + 1]) < 60 and not paras[i + 1].rstrip().endswith(('.', ':', ';'))):
                found = [hits[-1][1].group(1)]
    if not found:
        if kind == 'ligj' and not re.search(r'hyn\s+n[eëё]\s+fuqi', text, re.I):
            return add_days(published, 15), ('no in-force clause: 15 days after publication (Kushtetuta, neni 84, '
                                             'pika 3)')
        return None
    if len({f.strip() for f in found}) > 1:
        raise Hold('in_force_clause_twice')
    c0 = found[0].strip()
    s = c0.replace('“', '').replace('”', '').replace('’', '')
    s = re.sub(r'\.\s+[A-ZËÇ][A-ZËÇ ]{3,}.*$', '.', s)  # the signer's office run into the clause
    s = re.sub(r'\b(?:psa|mbas)\b', 'pas', s, flags=re.I)
    s = re.sub(r'\b(?:Zyrtre|Zyrare)\b', 'Zyrtare', s, flags=re.I)
    s = re.sub(r'\b(?:Fetoren|Fletores)\b', 'Fletoren', s, flags=re.I)
    s = re.sub(r'\bbotimi\b', 'botimit', s, flags=re.I)
    s = re.sub(r'\bn[eё](?=\s)', 'në', s)
    s = s.replace('ё', 'ë')
    s = re.sub(r'\bmenjehere\b', 'menjëherë', s, flags=re.I)
    s = re.sub(r'\s+', ' ', s).strip(' ,.;')
    if re.search(r'përveç|përjashtim|\bderi\b|zbatohet|hyrjes në fuqi|hyrjen në fuqi', s, re.I):
        return None
    fz = r'(?:\s+(?:në|të)\s+Fletore(?:n|s)?(?:\s+Zyrtare)?)?'
    pub = (r'(?:(?:pas|me)\s+(?:botim|publikim)(?:it|in)(?:\s+(?:e|të)\s+tij)?' + fz +
           r'|pasi\s+(?:botohet|publikohet)' + fz + r'|(?:në\s+|nga\s+)?(?:ditën|data|datën)\s+e\s+botimit' + fz + ')')
    imm = (r'menjëherë(?:\s*,?\s*(?:dhe\s+)?(?:me\s+botimin(?:\s+e\s+tij)?|pas\s+botimit|pasi\s+botohet|botohet|'
           r'publikohet|dërgohet\s+për\s+botim)' + fz + ')?')
    eff = (r'(?:\s*,?\s*(?:dhe\s+)?(?:botohet' + fz + r'\s*,?\s*(?:dhe\s+)?)?(?:i\s+|e\s+)?(?:fillon|shtrin)\s+'
           r'efekt(?:et|in|e)(?:\s+(?:financiar[e]?|juridike|e\s+tij|e\s+zbatimit(?:\s+të\s+tij)?))*\s+'
           r'(?:nga|prej|më|në)\s+(?:data\s+|datën\s+|datës\s+|datë\s+)?(\d{1,2}(?:\.\d{1,2}\.\d{4}|\s+[a-zë]+\s+\d{4})))?')
    m = re.fullmatch(r'(?:' + pub + '|' + imm + ')' + eff, s, re.I)
    if m:
        extra = f' (its effects run from {m.group(1)})' if m.group(1) else ''
        return published, f'"hyn në fuqi {c0}": the publication day{extra}'
    if re.fullmatch(r'(?:të|në)\s+nesërmen\s+e\s+botimit' + fz, s, re.I):
        return add_days(published, 1), f'"hyn në fuqi {c0}": the day after publication'
    m = re.fullmatch(r'(\d+|' + '|'.join(NUMWORD) + r')\s*(?:\([a-zë ]+\)\s*)?(ditë|muaj|vit|vjet)\s+(?:pas|nga)\s+botimit' + fz +
                     eff, s, re.I)
    if m:
        n = int(m.group(1)) if m.group(1).isdigit() else NUMWORD[m.group(1).lower()]
        unit_ = m.group(2).lower()
        try:
            day = add_days(published, n) if unit_ == 'ditë' else add_months(published, n if unit_ == 'muaj' else 12 * n)
        except ValueError:  # no such day in that month (31 January + 1 month): not read
            raise Hold(f'in_force_month_end:{c0[:60]}')
        extra = f' (its effects run from {m.group(3)})' if m.group(3) else ''
        return day, f'"hyn në fuqi {c0}"{extra}'
    m = re.fullmatch(r'(?:më|në)\s+(?:datë\s+|datën\s+)?(\d{1,2})\.(\d{1,2})\.(\d{4})(?:\s*,?\s*dhe\s+(?:botohet|publikohet)' + fz + ')?',
                     s, re.I)
    if m:
        day = iso(m.group(1), m.group(2), m.group(3))
        if day and day >= published:
            return day, f'"hyn në fuqi {c0}"'
        raise Hold(f'in_force_day_before_publication:{c0[:60]}')
    # a day with its month in words ("më 1 dhjetor 2023", "në datën 1 janar 2014"), after "Ky X botohet në Fletoren
    # Zyrtare dhe hyn në fuqi" as well as before "dhe botohet ..."
    m = re.fullmatch(r'(?:më|në|nga)\s+(?:datë\s+|datën\s+|data\s+)?(\d{1,2})\s+(' + '|'.join(MUAJ) + r')\s+(\d{4})'
                     r'(?:\s*,?\s*dhe\s+(?:botohet|publikohet)' + fz + ')?', s, re.I)
    if m:
        day = iso(m.group(1), str(MUAJ.index(m.group(2).lower()) + 1), m.group(3))
        if day and day >= published:
            return day, f'"hyn në fuqi {c0}"'
        raise Hold(f'in_force_day_before_publication:{c0[:60]}')
    return None


def in_force_strict(kind: str, text: str, published: str) -> tuple[str, str]:
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


MASTHEAD_DAY = re.compile(r'(?<![\d/.])(?<!Nr\.)(?<!Nr\. )(?<!Ekstra )(\d{1,2})\s+(' + '|'.join(MUAJ) + r')\s+(\d{4})', re.I)


def issue_day(cache: Path, a: dict) -> tuple[str, str]:
    """(publication day of act a's Fletorja Zyrtare issue, a note for the version). QBZ's gazette record when its day
    is on or after the adoption and at most 120 days later; otherwise the day the issue's own masthead prints (page 1
    of the issue's PDF), when it prints a full day, the issue's contents list the act (number and date), the issue is
    not an "Ekstra" issue (some of them print acts left unpublished at the time, "Akte të papublikuara") and the act was
    adopted under the 1998 Constitution (neni 117: legal force only once published). Raises Hold otherwise."""
    g = a.get('gazette') or {}
    rec = read_json(cache, f'{API}/gazettes/{g.get("year")}/{g.get("number")}') if g.get('number') else None
    if rec is None:
        raise Hold('gazette_not_fetched')
    G = rec.get('gazette') or {}
    pub = G.get('publishDate')
    if pub and a['date'] <= pub <= add_days(a['date'], 120):
        return pub, ''
    why = f'publication_day_inconsistent:{pub} vs {a["date"]}' if pub else 'publication_day_missing'
    pdf = read(cache, SITE + G['pdf']['url']) if (G.get('pdf') or {}).get('url') else None
    if pdf is None:
        raise Hold(why)
    import fitz  # PyMuPDF
    doc = fitz.open(stream=pdf, filetype='pdf')
    first = re.sub(r'\s+', ' ', doc[0].get_text()).strip()
    cut = re.search(r'P\s*Ë\s*R\s*M\s*B\s*A\s*J\s*T\s*J\s*A', first)
    head = first[:cut.start()] if cut else ''
    toc = ' '.join(re.sub(r'\s+', ' ', doc[i].get_text()) for i in range(min(10, doc.page_count)))
    toc = re.sub(r'(\d) (\d{3})\b', r'\1\2', toc)
    base = a['number'].split('-')[0]
    listed = any(re.split(r'[/-]', nr)[0] == base and iso(d, mo, y) == a['date'] for nr, d, mo, y in re.findall(
        r'nr\.?\s*([\d/-]+)\s*,?\s*(?:datë|date|dt\.?)\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})', toc, re.I))
    try:
        if not re.search(r'FLETORJA\s+ZYRTARE', head, re.I):
            raise Hold('issue_masthead_not_read:' + why)
        if re.search(r'papublikuar', head, re.I):
            raise Hold('issue_of_acts_unpublished_at_the_time:' + why)
        if re.search(r'\bEkstra\b', head, re.I):
            raise Hold('issue_ekstra:' + why)  # a special issue; whether it first published the act is not stated
        m = MASTHEAD_DAY.search(head)
        if not m:
            raise Hold('issue_masthead_without_day:' + why)
        day = iso(m.group(1), str(MUAJ.index(m.group(2).lower()) + 1), m.group(3))
        if not day:
            raise Hold('issue_masthead_without_day:' + why)
    except Hold as h:
        # The issue's colophon (its last pages: "Doli nga shtypi më D.M.YYYY", the day it came off the press) dates
        # the issue when it gives QBZ's own day for it, or a day in the month and year its masthead prints.
        day, note = colophon_day(doc, first, pub, a, str(h))
        if not listed:
            raise Hold('act_not_in_issue_contents:' + why)
        if a['date'] < '1998-11-28':
            raise Hold(f'adopted_before_1998_constitution:{why}')
        late = bool(re.search(r'papublikuar|\bEkstra\b', first[:400], re.I)) or day > add_days(a['date'], 120)
        LATE[a['id']] = late
        return day, note
    if not listed:
        raise Hold('act_not_in_issue_contents:' + why)
    if not day or day < a['date']:
        raise Hold(f'issue_masthead_day_before_adoption:{day} vs {a["date"]}')
    if a['date'] < '1998-11-28':
        raise Hold(f'adopted_before_1998_constitution:{why}')
    return day, ('; the issue’s day as printed on its masthead' +
                 (f', QBZ’s record giving {pub}' if pub and pub != day else ''))


LATE: dict = {}  # act id -> dated by its colophon and printed > 120 days after adoption or in an Ekstra issue
COLOPHON = re.compile(r'Doli\s+nga\s+shtypi\s+më\s+(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})', re.I)


def colophon_day(doc, first: str, pub: str | None, a: dict, held: str) -> tuple[str, str]:
    """The day an issue came off the press, from its colophon ("Doli nga shtypi më 6.6.2010" on its last pages),
    accepted only when it equals QBZ's day for the issue or falls in the month and year printed on the issue's
    masthead, and is not before the act's adoption. Raises the original hold otherwise."""
    tail = ' '.join(re.sub(r'\s+', ' ', doc[i].get_text()) for i in range(max(0, doc.page_count - 2), doc.page_count))
    found = {iso(d, m, y) for d, m, y in COLOPHON.findall(tail)} - {None}
    if len(found) != 1:
        raise Hold(held)
    day = found.pop()
    mh = re.search(r'\b(' + '|'.join(MUAJ) + r')\s+(\d{4})\b', first[:300], re.I)
    month_ok = bool(mh) and day[:7] == f'{int(mh.group(2)):04d}-{MUAJ.index(mh.group(1).lower()) + 1:02d}'
    if not (day == pub or month_ok) or day < a['date']:
        raise Hold(held)
    return day, ('; the issue’s day as printed in its colophon (“Doli nga shtypi”)' +
                 (f', QBZ’s record giving {pub}' if pub and pub != day else ''))


def late_clause_ok(kind: str, text: str, act_id) -> None:
    """An act printed long after its adoption (more than 120 days, or in an Ekstra issue of earlier acts) is dated by
    its in-force clause only when the clause itself counts from publication ("pas botimit", "me botimin", "pasi
    botohet", "N ditë pas botimit", "ditën e botimit") or names a calendar day; a bare "menjëherë" (immediately) is
    held: for an act printed years later it does not say whether it took effect on adoption or on publication."""
    if not LATE.get(act_id):
        return
    found = re.findall(r'\bKy ' + WHO_LOOSE.get(kind, WHO.get(kind, kind)) + r'\s+hyn\s+në\s+fuqi\s*([^\n]*)', text, re.I)
    c = found[0] if found else ''
    if re.search(r'(?:pas|me)\s+(?:botim|publikim)|pasi\s+(?:botohet|publikohet)|(?:ditën|datën|nesërmen)\s+e\s+'
                 r'(?:botimit|publikimit)|\d{1,2}\.\d{1,2}\.\d{4}|\d{1,2}\s+(?:' + '|'.join(MUAJ) + r')\s+\d{4}', c, re.I) \
            and not re.match(r'\s*menjëherë', c, re.I):
        return
    raise Hold('late_publication_clause_not_tied_to_publication:' + c[:60])


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
    """split_once with the strict forms; only when those find no signature or no operative word, with the loose
    forms (RE_SIGN_VKM_LOOSE, RE_FOOT_LAW_LOOSE, OPERATIVE_MIN_ANY, an instruction or order whose in-force clause
    is its last paragraph, without a signer's line)."""
    try:
        return split_once(paras, kind, notes)
    except Hold as h:
        if str(h) not in ('signature_not_found', 'vendosi_not_found'):
            raise
        return split_once(paras, kind, notes, loose=True)


def split_once(paras: list[str], kind: str, notes: dict | None = None, loose: bool = False) -> dict:
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
        if clause is None and loose:
            clause = next((i for i, p in enumerate(paras)
                           if re.search(r'\b(?:Ky|Ku)\s+' + ACT_WORD + r'(?:i)?\s+hyn\s+n[eëё]\s+fuqi', p, re.I)), None)
        foot_at = clause + 1 if clause is not None and clause + 1 < len(paras) and len(paras[clause + 1]) < 120 else None
        if foot_at is None and loose and clause is not None and clause == len(paras) - 1:
            foot_at = len(paras)  # no signer's line under the clause
    else:
        sign = RE_SIGN_VKM if kind in ('vendim', 'aktnormativ') else RE_SIGN_PRES if kind == 'dekret' else RE_FOOT_LAW
        if loose:
            sign = RE_SIGN_VKM_LOOSE if kind in ('vendim', 'aktnormativ') else RE_SIGN_PRES if kind == 'dekret' \
                else RE_FOOT_LAW_LOOSE
        if not loose:
            foot_at = next((i for i, p in enumerate(paras) if sign.match(p)), None)
        else:
            foot_at = next((i for i, p in enumerate(paras)
                            if sign.match(p.replace('І', 'I').replace('і', 'i')) and
                            (len(p) < 60 or kind not in ('vendim', 'aktnormativ'))), None)
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
        if op_at is None and loose and kind in MINISTERIAL.values():
            op_at = next((i for i, p in enumerate(body) if len(p) < 40 and
                          re.fullmatch(OPERATIVE_MIN_ANY + r':?', ''.join(p.split()), re.I)), None)
    elif not has_neni:
        # a law of one provision without articles ("Për miratimin e aktit normativ ..."): what the Assembly decided,
        # after its "VENDOSI:"
        op_at = next((i for i, p in enumerate(body) if re.fullmatch(r'VENDOSI:?', ''.join(p.split()), re.I)), None)
        started = op_at is None
    for i_p, p in enumerate(body):
        where.append(cur)
        if not started:
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
    foot = tail[:1]
    i = len(foot)
    m0 = (RE_SIGN_VKM_LOOSE.match(tail[0].replace('І', 'I').replace('і', 'i'))
          if loose and tail and kind in ('vendim', 'aktnormativ') else None)
    named = bool(m0 and m0.group('name'))
    foot_law = RE_FOOT_LAW_LOOSE if loose else RE_FOOT_LAW
    if kind != 'ligj':
        while foot and not named and i < len(tail) and i < 2 and len(tail[i]) < 60 and not tail[i].endswith(('.', ':')) \
                and not re.match(r'^(ANEKS|SHTOJC|LIDHJ|TABEL|RREGULLORE|Aneks|Shtojc|Lidhj|Tabel)', tail[i]):
            foot.append(tail[i])
            i += 1
        if foot:
            unit(units, order, 'zz-nenshkrimi', 'Nënshkrimi', 'enactment', ['# Nënshkrimi'] + foot)
    else:
        while i < len(tail) and (foot_law.match(tail[i]) or ((''.join(foot[-1].split()) if loose else foot[-1]).startswith('KRYETAR')
                                                              and len(tail[i]) < 40 and not tail[i].endswith('.'))):
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
    """The text's own header gives the record's number and date (header_strict), or does so with the number's digits
    spaced ("10 160"), a "/" for QBZ's "-" in the number (the same suffix when the record has one), a comma after
    "datë" or a space for the last dot of the date."""
    if header_strict(kind, a, paras):
        return True
    head = ' '.join(paras[:6])
    base, _, suffix = a['number'].partition('-')
    num = r'\s?'.join(re.escape(ch) for ch in base)
    suf = (r'\s*[-/]\s*' + re.escape(suffix) + r'\b') if suffix and kind != 'ligj' else \
        (r'(?:\s*[-/]\s*\d+\b)?' if kind != 'ligj' else '')
    date2 = r'(?:datë|date|data|dt\.?)\s*,?\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*(?:\.\s*|\s+)(\d{4})'
    if kind != 'ligj':
        m = re.search(r'\bNr\.?\s*' + num + r'(?![\d])' + suf + r'\s*,?\s*' + date2, head, re.I)
        return bool(m) and iso(m.group(1), m.group(2), m.group(3)) == a['date']
    m = re.search(r'\bNr\.?\s*' + num + r'(?![\d])\s*(?:/\s*(\d{4})|,?\s*' + date2 + ')', head, re.I)
    if not m:
        return False
    if m.group(1):
        return m.group(1) == a['date'][:4]
    return iso(m.group(2), m.group(3), m.group(4)) == a['date']


def header_typeset(kind: str, a: dict, paras: list[str]) -> bool:
    """Only when header_ok reads nothing: the record's number and date in the header's first "Nr." with typesetting
    slips that leave both intact: a Cyrillic "ё" in "datё", a dot for the comma after the number ("Nr.31. datë"), a
    dot after "datë" ("datë. 9.7.2019"), no "datë" ("Nr.9063, 8.5.2003"), a doubled dot or a space in the date
    ("23.4..2008", "19.1 2005"), a stray "1" before the year ("5.11.12004"), a leading zero in QBZ's number ("02"), or
    a law's "N-YYYY" for "N/YYYY". The number (and a "/n" suffix, when the record has one) must match exactly."""
    head = ' '.join(paras[:6]).replace('ё', 'ë').replace('Ё', 'Ë')
    m = re.search(r'\bNr\.?\s*((?:\d\s?)+)(?:\s*[-/]\s*(\d+))?\s*[,.]?\s*(?:(?:datë|date|data|dt)\s*\.?\s*,?\s*)?'
                  r'(\d{1,2})\s*\.{1,2}\s*(\d{1,2})\s*(?:\.{1,2}\s*|\s+)(1?)(\d{4})(?!\d)', head, re.I)
    if not m:
        if kind == 'ligj':
            m2 = re.search(r'\bNr\.?\s*(\d+)\s*-\s*(\d{4})(?!\d)', head, re.I)
            base = a['number'].split('-')[0]
            return bool(m2) and base.isdigit() and int(m2.group(1)) == int(base) and m2.group(2) == a['date'][:4]
        return False
    num, suffix = re.sub(r'\s', '', m.group(1)), m.group(2)
    base, _, rsuf = a['number'].partition('-')
    if not base.isdigit() or int(num) != int(base):
        return False
    if kind == 'ligj':
        if suffix and suffix != a['date'][:4]:
            return False
    elif (suffix or '') != rsuf:
        return False
    if m.group(5) and m.group(6) != a['date'][:4]:
        return False
    return iso(m.group(3), m.group(4), m.group(6)) == a['date']


def header_strict(kind: str, a: dict, paras: list[str]) -> bool:
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
    if kind == 'dekret':
        return f'Dekreti nr. {a["number"].split("-")[0]}, datë {dmy(a["date"])}'
    if kind == 'aktnormativ':
        return f'Akti normativ nr. {a["number"].split("-")[0]}, datë {dmy(a["date"])}'
    if kind in MINISTERIAL.values():
        word = 'Udhëzimi' if kind == 'udhezim' else 'Urdhri'
        return f'{word} nr. {a["number"]}, datë {dmy(a["date"])} ({a.get("institution") or ""})'
    if kind == 'vendim':
        return f'Vendimi i Këshillit të Ministrave nr. {a["number"]}, datë {dmy(a["date"])}'
    num = a['number'].split('-')[0]
    return f'Ligji nr. {num}/{a["date"][:4]}' if int(a['date'][:4]) >= 2009 else f'Ligji nr. {num}'


AMBIG: set = set()      # (family, year, number) that QBZ gives to more than one act
INERT: dict = {}        # QBZ id -> why that act changed nothing (changes_nothing), or None
APPROVED: dict = {}     # ('aktnormativ', number, day) -> the listing record of the law approving that act
PUB_URL: dict = {}      # act slug on main -> its url, so a key already published never changes
_PUB_URLS = None


def ON_MAIN_URL(x: dict) -> bool:
    """Whether an act with this record's official page is on main already (2026-11-09)."""
    global _PUB_URLS
    if _PUB_URLS is None:
        _PUB_URLS = set(PUB_URL.values())
    return bool(x.get('eliPath')) and f'{SITE}{x["eliPath"]}' in _PUB_URLS


def family(x: dict) -> str | None:
    if x['type'] == 'Ligj':
        return 'ligj'
    if x['type'] == 'Vendim' and x.get('institution') == 'Këshilli i Ministrave':
        return 'vendim'
    if x['type'] == 'Vendim' and x.get('institution') == 'Gjykata Kushtetuese':
        return 'vendim-gjk'
    if x['type'] == 'Akt normativ':
        return 'aktnormativ'
    if x['type'] == 'Dekret':
        return 'dekret'
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
        return year_key('aktnormativ', x), label_of('aktnormativ', x), 'decree'
    if x['type'] == 'Dekret':
        return year_key('dekret', x), label_of('dekret', x), 'decree'
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


NOTE_NR = re.compile(r'\bnr\.?\s*(\d{1,3}(?:\s\d{3})+|\d+)(?:\s*/\s*(\d{4}))?(?:\s*,?\s*(?:datë|date|data|datё)\s*'
                     r'(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4}))?', re.I)
NUM_DATE: dict = {}     # (number, day) -> listing records; (number, year) -> laws: the acts QBZ's notes can name
LISTING_FILES: list = []  # the listing's cache files (an act read through NUM_DATE depends on all of them)


def noted_acts(notes: list[str], x: dict) -> set | None:
    """The QBZ records every "nr. N, datë D" / "nr. N/YYYY" in QBZ's notes names (a law by number and year), or None
    when one names no record or more than one."""
    out = set()
    for n in notes:
        for m in NOTE_NR.finditer(n):
            num = m.group(1).replace(' ', '')
            if m.group(3):
                day = iso(m.group(3), m.group(4), m.group(5))
                hits = NUM_DATE.get((num, day), [])
            elif m.group(2):
                hits = NUM_DATE.get((num, m.group(2)), [])
            else:
                return None
            hits = [h for h in hits if h['id'] != x['id']]
            if len(hits) != 1:
                return None
            out.add(hits[0]['id'])
    return out


def changing_day(cache: Path, memo: Path | None, cb: dict) -> tuple[str, str, str, str]:
    """(in-force day, how, publication day, its note) of an act that changes another, as for a QBZ version's act."""
    cpub, cnote = issue_day(cache, cb)
    if cb['type'] == 'Vendim' and cb.get('institution') == 'Gjykata Kushtetuese':
        return cpub, 'a Constitutional Court decision takes effect on its publication (Kushtetuta, neni 132)', cpub, cnote
    ck = kind_of(dict(cb, kind='Akt bazë'))
    if ck not in WHO:
        raise Hold(f'changing_act_kind:{cb["type"]}')
    xt = text_of(cache, memo, cb) if cb.get('word') else None
    if xt is None:
        raise Hold('changing_act_text_not_fetched')
    if ck == 'aktnormativ':
        approved_in_time(cb, 'changing_act_')
    day, how = in_force(ck, '\n'.join(xt), cpub)
    late_clause_ok(ck, '\n'.join(xt), cb['id'])
    return day, how, cpub, cnote


def nameless_differs(cache: Path, memo: Path | None, u: dict, kind: str, units: dict) -> bool:
    """Does QBZ version u (naming no changing act) read differently from units (spacing aside)? A version without a
    text does not count."""
    w = u.get('word') or {}
    if not w.get('url', '').endswith(('.docx', '.doc')):
        return False
    up = text_of(cache, memo, {'word': w})
    if up is None:
        return True
    try:
        uu = split(up, kind, {})
    except Hold:
        return True
    flat = lambda d: {k: ''.join(d[k]['text'].split()) for k in d}  # noqa: E731
    return flat(uu) != flat(units)


def late_start(cache: Path, memo: Path | None, x: dict, kind: str, byid: dict, vs: list, changes_in: set,
               published: str, pub_note: str, day0: str, laws: dict, gap: str) -> tuple[int, dict, dict, str]:
    """When QBZ's versions do not give the text after each change (gap: a version names no changing act, or an act QBZ
    links as changing this one has no version), the oldest version that can be published: the first QBZ version s
    such that every later version names its changing act, and every change it holds is known and dated: the acts QBZ
    links as changing the act, other than those of later versions (an act with a version up to s and a later one rules
    s out, as does an earlier version naming no act whose text differs), and every act its notes name ("nr. N, datë D",
    "nr. N/YYYY", each one record in QBZ's listing), each named by a note of that version and none of them the act of
    a later version. In force from the day the last of them took effect (not before the act itself). Returns
    (s, its version, its units, that day); raises Hold(gap) when no version qualifies."""
    if TOUCHED is not None:
        TOUCHED.extend(LISTING_FILES)
    g = x['gazette']
    for s_at, v in enumerate(vs):
        later = vs[s_at + 1:]
        if any(not (u.get('changedBy') or {}).get('id') for u in later):
            continue
        later_by = {u['changedBy']['id'] for u in later}
        if {(u.get('changedBy') or {}).get('id') for u in vs[:s_at + 1]} & later_by:
            continue  # an act with a version here and a later one: this version is not before it
        w = v.get('word') or {}
        if not w.get('url', '').endswith(('.docx', '.doc')):
            continue
        vp = text_of(cache, memo, {'word': w})
        if vp is None:
            continue
        notes: dict[str, list[str]] = {}
        try:
            units = split(vp, kind, notes)
        except Hold:
            continue
        if kind == 'ligj' and not any(k.startswith(('neni-', 'pika-')) for k in units):
            continue
        # an earlier version naming no changing act whose text differs from this one: a change QBZ dates to no act
        if not (v.get('changedBy') or {}).get('id') and any(
                not (u.get('changedBy') or {}).get('id') and nameless_differs(cache, memo, u, kind, units)
                for u in vs[:s_at]):
            continue
        all_notes = [n for k in sorted(notes) for n in notes[k]]
        noted = noted_acts(all_notes, x)
        if noted is None or noted & later_by:
            continue
        inc = ((set(changes_in) | {(u.get('changedBy') or {}).get('id') for u in vs[:s_at + 1]} | noted)
               - {None} - later_by)
        if not inc or any(i not in byid for i in inc) or \
                any(not any(names_act(n, byid[i]) for n in all_notes) for i in inc):
            continue
        dated = []
        try:
            for i in sorted(inc):
                if TOUCHED is not None:
                    TOUCHED.append(f'id:{i}')
                dated.append(changing_day(cache, memo, byid[i]) + (byid[i],))
        except Hold:
            continue
        dated.sort(key=lambda t: (t[0], t[4]['date'], t[4]['id']))
        day, how, cpub, cnote, cb = dated[-1]
        if day < day0:
            continue
        for _, _, dpub, _, db in dated:
            lk, label, lkind = law_ref(db)
            laws[lk] = {'label': label, 'title': title_of(db), 'kind': lkind, 'enacted': db['date'], 'published': dpub,
                        'url': f'{SITE}{db["eliPath"]}' if db.get('eliPath') else None,
                        'temporary_until': None, 'restores': None, 'note': None}
        names = ', '.join(law_ref(t[4])[1] for t in dated)
        cg = cb.get('gazette') or {}
        ver = {'from': day, 'source_url': SITE + w['url'], 'sha256': w['sha256'], 'units': units, 'credits': {},
               '_earlier': [law_ref(t[4])[0] for t in dated],
               'note': f'QBZ consolidated version {v["versionNo"]}, the oldest version published here: the act as '
                       f'published in the Fletorja Zyrtare nr. {g["number"]}/{g["year"]} ({published}{pub_note}; in '
                       f'force from {day0}) with the changes made by {names}, each named in its notes. QBZ’s versions '
                       f'do not give the text after each of these changes ({gap.split(":")[0].replace("_", " ")}), so '
                       f'they are not published one by one. In force from {day}, the day the last of them took '
                       f'effect ({law_ref(cb)[1]}, Fletorja Zyrtare nr. {cg.get("number")}/{cg.get("year")}, '
                       f'{cpub}{cnote}: {how}).'}
        return s_at, ver, units, day
    raise Hold(gap)


def history(cache: Path, memo: Path | None, x: dict, kind: str, byid: dict, published: str, base_paras: list[str],
            laws: dict, decisions: list, pub_note: str = '') -> list[dict]:
    """The act as published, then each QBZ consolidated version (dated by QBZ's validFrom, credited to the act QBZ
    names as changing it); raises Hold when the history is not complete or does not read cleanly."""
    rel = read_json(cache, f'{API}/acts/{x["id"]}/relations') or []
    vs = read_json(cache, f'{API}/acts/{x["id"]}/versions')
    if vs is None:
        raise Hold('versions_not_fetched')
    vs = sorted(vs, key=lambda v: v['versionNo'])
    changes_in = {r['actId'] for r in rel if r.get('type') == 'CHANGES' and r.get('direction') == 'in'}
    by = {(v.get('changedBy') or {}).get('id') for v in vs}
    gap = 'version_without_changing_act' if None in by else \
        'versions_incomplete:' + ','.join(map(str, sorted(changes_in - by)[:5])) if not changes_in <= by else None
    # 2026-11-09: QBZ's base-act text is itself one of its consolidated versions (its text "as published" is not on
    # QBZ): the act starts from the oldest version available, as for any other gap. An act already on main with that
    # text as its first version keeps it and is labelled (see compute()).
    if not gap and not ON_MAIN_URL(x) and \
            x['word']['sha256'] in {(v.get('word') or {}).get('sha256') for v in vs}:
        gap = 'base_text_is_a_consolidated_version'
    day0, how0 = in_force(kind, '\n'.join(base_paras), published)
    late_clause_ok(kind, '\n'.join(base_paras), x['id'])
    prev = split(base_paras, kind)
    if kind == 'ligj' and not any(k.startswith(('neni-', 'pika-')) for k in prev):
        raise Hold('no_articles')
    g = x['gazette']
    out = [{'from': day0, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'], 'units': prev,
            'credits': {}, 'note': f'As published in the Fletorja Zyrtare nr. {g["number"]}/{g["year"]} ({published}{pub_note}); '
                                   f'in force from {day0}: {how0}.'}]
    last = day0
    if gap:  # QBZ's versions do not give the text after each change: start from the oldest complete one
        s_at, ver0, prev, last = late_start(cache, memo, x, kind, byid, vs, changes_in, published, pub_note, day0,
                                            laws, gap)
        out, vs = [ver0], vs[s_at + 1:]
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
        try:
            cpub, cnote = issue_day(cache, cb)
        except Hold as h:
            raise Hold(f'version_{v["versionNo"]}_changing_act_publication_day:{h}')
        xt = text_of(cache, memo, cb) if cb.get('word') else None
        xtext = '\n'.join(xt) if xt else None
        if cb['type'] == 'Vendim' and cb.get('institution') == 'Gjykata Kushtetuese':
            day, how = cpub, 'a Constitutional Court decision takes effect on its publication (Kushtetuta, neni 132)'
        elif kind_of(dict(cb, kind='Akt bazë')) in WHO:
            if xtext is None:
                raise Hold(f'version_{v["versionNo"]}_changing_act_text_not_fetched')
            ck = kind_of(dict(cb, kind='Akt bazë'))
            if ck == 'aktnormativ':
                approved_in_time(cb, f'version_{v["versionNo"]}_changing_act_')
            try:
                day, how = in_force(ck, xtext, cpub)
                late_clause_ok(ck, xtext, cb['id'])
            except Hold as h:
                raise Hold(f'version_{v["versionNo"]}_changing_act_{h}')
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
                       f'{cg.get("number")}/{cg.get("year")}, {cpub}{cnote}); in force from {day}: {how}.'}
        if day == last:
            ver['same_day'] = True
        out.append(ver)
        prev, last = units, day
    return out


CHANGE_WORDS = re.compile(r'(?<![a-zë])(?:ndrysh(?!m|ëm)\w*|shfuqiz\w*|shtes\w*|zëvendës\w*|'
                          r'korrigj\w*|pezull\w*)', re.I)


def unquoted(s: str) -> str:
    """s without the words inside “...” (nested quotes too: a cited act's own title); an unclosed quote keeps the
    rest."""
    out, depth, start, opened = [], 0, 0, 0
    for i, ch in enumerate(s):
        if ch == '“':
            if depth == 0:
                out.append(s[start:i])
                opened = i
            depth += 1
        elif ch == '”' and depth:
            depth -= 1
            if depth == 0:
                start = i + 1
    out.append(s[opened:] if depth else s[start:])
    return ' '.join(out)


TYPE_ALL = re.compile(r'\b(vendim\w*|vkm\w*|udhëzim\w*|udhezim\w*|urdh[eë]r\w*|urdhr\w*|ligj\w*|dekret\w*|'
                      r'akt\w*\s+normativ\w*)', re.I)
PLURAL_TYPE = re.compile(r'(?:vendimet|vendimeve|vkm-të|vkm-ve|udhëzimet|udhëzimeve|urdhrat|urdhrave|urdhërat|ligjet|'
                         r'ligjeve|dekretet|dekreteve|aktet\s+normative|akteve\s+normative)$', re.I)
NOT_AN_ACT = re.compile(r'kontrat|marrëveshj|statut|rregullor|protokoll|projekt|licenc|\blej|certifikat|shkres|'
                        r'gjykat|kërkes|prot\.|regjistr|faturë|kodi\b', re.I)


def cites_all(text: str):
    """(ref, start, end, governing start) for every act citation: cites(), and a "nr. N, datë D" (a "/n" suffix allowed)
    governed by the act type word before it on its line, either a singular one with only its qualifiers between
    ("Urdhri i ministrit të ... nr. N", "vendimit të Këshillit të Ministrave nr. N") or a plural one heading a list
    ("Vendimet nr. A, datë ..., “...”, dhe nr. B, datë ..."), with no other kind of document named between."""
    spans = []
    for ref, st, en in cites(text):
        spans.append((st, en))
        yield ref, st, en, st
    for m in BARE_NR.finditer(text):
        if any(a <= m.start() < b for a, b in spans):
            continue
        line_start = text.rfind('\n', 0, m.start()) + 1
        words = list(TYPE_ALL.finditer(text, max(line_start, m.start() - 600), m.start()))
        if not words:
            continue
        wm = words[-1]
        gap = text[wm.end():m.start()]
        if NOT_AN_ACT.search(unquoted(gap)) or re.match(r'\s*,?\s*(?:i|e|të)\s+gjykat', text[m.end():m.end() + 40], re.I):
            continue
        if not PLURAL_TYPE.search(wm.group(1)) and (len(gap) > 80 or re.search(r'[,;:“”]', gap)):
            continue
        day = iso(m.group(2), m.group(3), m.group(4))
        if not day:
            continue
        w = wm.group(1).lower()
        if w.startswith('ligj'):
            ref = ('law', m.group(1), m.group(4))
        elif w.startswith(('udhëzim', 'udhezim')):
            ref = ('udhezim', m.group(1), day)
        elif w.startswith('urdh'):
            ref = ('urdher', m.group(1), day)
        elif w.startswith('dekret'):
            ref = ('dekret', m.group(1), day)
        elif w.startswith('akt'):
            ref = ('aktnormativ', m.group(1), day)
        else:
            ref = ('vkm', m.group(1), day)
        yield ref, m.start(), m.end(), wm.start()


HEAD_CHANGE = re.compile(r'\b(?:shfuqizohe[tn]|shfuqizim(?:in|i|it)?|revokohe[tn]|ndryshohe[tn]|ndryshim(?:in|et|e)\s+'
                         r'në|ndryshime\s+dhe\s+shtesa\s+në|shtesa?\s+(?:dhe\s+ndryshime\s+)?në|shtohe[tn]\s+në|'
                         r'zëvendësohe[tn]|pezullohe[tn]|pezullim(?:in|i)?|korrigjohe[tn]|korrigjim\w*)\b', re.I)
FINITE_CHANGE = (r'\b(?:shfuqizohe[tn]|ndryshohe[tn]|revokohe[tn]|pezullohe[tn]|zëvendësohe[tn]|korrigjohe[tn]|'
                 r'shtohe[tn]\s+në)\b')
# a title ("Për disa ndryshime në vendimin nr. ...") or a draft ("Projektvendim ...") quoted without quote marks, as in
# the government's plans of draft acts: not a change made by this text
TITLE_FORM = re.compile(r'(?:\bP[ëe]r\s+(?:disa|një|ca)?\s*$|projekt\w*|program\w*|plan\w*)', re.I)
VERB_AFTER_LIST = re.compile(r'[\s,]*(?:dhe[\s,]+)?(?:(?:i|të)\s+Këshillit\s+të\s+Ministrave[\s,]*)?'
                             r'(?:shfuqizohe[tn]|ndryshohe[tn]|revokohe[tn]|pezullohe[tn]|zëvendësohe[tn])', re.I)


def changed_cites(text: str) -> list:
    """Acts this text cites as amended or repealed: a change word after the citation, in its own paragraph, before the
    next citation and within 300 characters, outside the quoted title of the cited act ("të ndryshme", different, is
    not a change word)."""
    out = []
    for ref, _, e in cites(text):
        nxt = NEXT_CITE.search(text, e)
        end = min(e + 300, nxt.start() if nxt else len(text))
        nl = text.find('\n', e)
        if nl != -1:
            end = min(end, nl)
        if CHANGE_WORDS.search(unquoted(text[e:end])):
            out.append(list(ref))
    # also, in the strong forms only (plans and reports cite drafts and acts in every other way):
    # - a finite change verb governing the citation in its own clause ("Shfuqizohet vendimi nr. ...", "Ndryshohet
    #   urdhri i ministrit nr. ..."), not in a title or a plan ("Për disa ndryshime ...", "Projektvendim ...");
    # - for a citation only cites_all reads: "i/të ndryshuar" or "u shfuqizua/u ndryshua" right after it (its cited
    #   title left out), or a finite verb right after the last item of the plural list it is in;
    # - an item of a list opened by a line with a finite change verb ending in ":" ("Shfuqizohen aktet e mëposhtme:")
    found = list(cites_all(text))
    ends = sorted(en for _, _, en, _ in found)
    for ref, st, en, gov in found:
        if list(ref) in out:
            continue
        line_start = text.rfind('\n', 0, gov) + 1
        if text[line_start:gov].count('“') > text[line_start:gov].count('”'):
            continue  # inside a quoted title (a draft in a plan, another act's title): not this text's own words
        line_end = text.find('\n', en)
        line_end = len(text) if line_end == -1 else line_end
        if TITLE_FORM.search(text[line_start:gov]):
            continue
        seps = [line_start + m.end() for m in re.finditer(r'(?<![Nn][Rr])\.\s|;|:', text[line_start:gov])]
        cut = max([line_start] + seps + [x for x in ends if line_start <= x <= gov])
        head = unquoted(text[cut:gov])
        changed = bool(re.search(r'(?:' + FINITE_CHANGE + r')[^,;:.]{0,40}$', head, re.I))
        after = unquoted(text[en:line_end])
        if not changed and gov != st:
            changed = bool(re.match(r'\s*,?\s*(?:(?:i|të|e)\s+ndryshuar|u\s+(?:shfuqizua|ndryshua|pezullua))', after, re.I))
            if not changed and PLURAL_TYPE.search(text[gov:st].split(' nr')[0].split(' e ')[0].strip()):
                tail = re.split(r'(?<![Nn][Rr])\.\s|;', BARE_NR.sub(' ', after), maxsplit=1)[0]
                changed = bool(VERB_AFTER_LIST.match(tail))
        if not changed and LIST_ITEM.match(text[line_start:]) and \
                not LIST_ITEM.sub('', text[line_start:gov], count=1).strip():
            k = line_start
            for _ in range(60):
                if k <= 0:
                    break
                prev_start = text.rfind('\n', 0, k - 1) + 1
                prev = text[prev_start:k - 1]
                if prev.rstrip().endswith(':'):
                    changed = bool(re.search(FINITE_CHANGE, unquoted(prev), re.I)) and not TITLE_FORM.search(prev)
                    break
                if not LIST_ITEM.match(prev):
                    break
                k = prev_start
        if changed:
            out.append(list(ref))
    return out


RULES = {
    'masthead': 'An act whose issue day in QBZ’s gazette record is missing, before its adoption or more than 120 days '
                'after it is dated by the day printed on the masthead of the issue’s own PDF, when the masthead prints '
                'a full day and the issue’s contents list the act; otherwise it is held back, as are the acts of the '
                '“Ekstra” issues (some print acts left unpublished at the time, “Akte të papublikuara”) and acts adopted '
                'before the 1998 Constitution. The same applies to the act that changes or repeals it.',
    'law_default': 'A law with no in-force clause enters into force 15 days after its publication (Kushtetuta, neni '
                   '84, pika 3).',
    'effects': 'A clause that puts an act in force on publication and starts its effects on a stated day (“i fillon '
               'efektet nga ...”) dates it by its entry into force, the publication day; the version note gives the '
               'day its effects run from.',
    'text_repeal': 'A repeal QBZ does not link is taken from the repealing act’s own text when every act citing this '
                   'one as changed repeals it as a whole there: an empty last version on the day the repealing act '
                   'took effect, credited to it.',
    'aktnormativ': 'An act with the force of law of the Council of Ministers (akt normativ, Kushtetuta, neni 101) is '
                   'published only when a law in QBZ’s listing approves it no later than 45 days after its adoption '
                   '(otherwise it loses its force from the start); it is in force from the day its own clause gives, '
                   'counted from its publication (neni 117, pika 1).',
}
RULES['dekret'] = ('A decree of the President is published only when it is normative (the organisation of the '
                   'courts: districts, territorial jurisdiction and seats, the number of judges, special sections, '
                   'the start of new courts); individual decrees (citizenship, appointments, honours, pardons, '
                   'promulgation of laws) are left out. It is in force from the day its own clause gives, counted '
                   'from its publication.')
RULES['colophon'] = ('Where the masthead settles nothing (it prints only a month, or it is an “Ekstra” issue, some of '
                     'which print acts left unpublished at the time), the issue is dated by its colophon, the day it '
                     'came off the press (“Doli nga shtypi më …”), when that day is QBZ’s own day for the issue or '
                     'falls in the month and year on the masthead, and the issue’s contents list the act. An act '
                     'printed that way more than 120 days after its adoption, or in an Ekstra issue, is published '
                     'only when its own clause counts from publication (“pas botimit”, “me botimin”, “N ditë pas '
                     'botimit”) or names a day; “menjëherë” alone does not say whether it took effect on adoption '
                     'or on publication, so such acts are held. Acts printed in two issues are held.')
RULES['inert_title'] = ('An act whose title names this one as changed does not hold it back when its own text shows '
                         'it changed nothing: a Constitutional Court decision whose ruling only rejects the request, '
                         'declares it inadmissible or ends the case (“Rrëzimin / Mospranimin e kërkesës”, “Pushimin e '
                         'gjykimit”), or a decision of the Assembly that only overrides the President’s decree '
                         'returning a law for reconsideration (“Rrëzimin e dekretit ...”) or does not approve a draft law '
                         '(“Mosmiratimin e projektligjit ...”). The version note names it; any other act its title '
                         'names as changing this one still holds it back.')
RULES['oldest_available'] = (
    'When QBZ’s consolidated versions do not give the text after each change (a version names no changing act, or '
    'an act QBZ links as changing the act has no version of its own), the act is published from the first QBZ '
    'version that holds every such change and after which every version names its changing act: the acts QBZ links '
    'as changing it and every act its notes name (each one record in QBZ’s listing, dated as a changing act is), each '
    'named in that version’s notes. That version is the oldest one published (“oldest version available”, credited '
    'to the publisher, with the act as published and those changing acts as earlier laws), in force from the day the '
    'last of those changes took effect; the versions after it follow as usual. The text in force before that day is '
    'not published.')
RULES['header_typeset'] = (
    'An act whose header prints its number and date with a typesetting slip that leaves both intact (a Cyrillic “ё” in '
    '“datё”, a dot for a comma, a doubled dot, a missing “datë”, a stray “1” before the year, a leading zero in QBZ’s '
    'number, a law’s “N-YYYY”) is read as QBZ’s record gives them; the version note quotes the header. Any other '
    'difference between the header and QBZ’s record holds the act back.')
RULE_ORDER = [(k, None) for k in ('aktnormativ', 'dekret', 'masthead', 'colophon', 'law_default', 'effects',
                                  'text_repeal', 'inert_title', 'oldest_available', 'header_typeset')]
RULE_MARKS = [('masthead', 'as printed on its masthead'), ('colophon', 'as printed in its colophon'),
              ('law_default', 'no in-force clause: 15 days after'),
              ('effects', '(its effects run from '), ('inert_title', ', but its own text shows it changed nothing:'),
              ('oldest_available', ', the oldest version published here:'),
              ('header_typeset', 'with a typesetting slip (“')]

INERT_RULING = re.compile(r'(?:Rrëzimin|Mospranimin|Pushimin|Refuzimin)\s+e\s+(?:kërkesës|gjykimit|çështjes|pretendimit)\b',
                          re.I)
INERT_ASSEMBLY = re.compile(r'(?:Rrëzimin\s+e\s+dekretit\b.*\bkthimin\b|Mosmiratimin\s+e\s+projektligjit\b)', re.I)


def changes_nothing(cache: Path, memo: Path | None, n: dict) -> str | None:
    """Why act n, whose title names another act as changed, changed nothing (None when its text does not show that):
    a Constitutional Court decision whose ruling (after its last "VENDOSI:", up to its in-force line) has only items
    rejecting the request, declaring it inadmissible or ending the case; or a decision of the Assembly whose ruling
    only overrides the President's decree returning a law or does not approve a draft law."""
    court = n['type'] == 'Vendim' and n.get('institution') == 'Gjykata Kushtetuese'
    assembly = n['type'] == 'Vendim' and n.get('institution') == 'Kuvendi i Shqipërisë'
    if not (court or assembly) or not n.get('word'):
        return None
    ps = text_of(cache, memo, n)
    if not ps:
        return None
    ops = [i for i, p in enumerate(ps) if re.fullmatch(r'VENDOSI:?', ''.join(p.split()), re.I)]
    if not ops or (assembly and len(ops) != 1):
        return None
    items = []
    for p in ps[ops[-1] + 1:]:
        q = re.sub(r'^(?:-|•|\d+\s*\.|[IVX]+\s*\.)\s*', '', p).strip()
        if re.match(r'Ky\s+vendim\s+(?:është\s+përfundimtar|hyn\s+në\s+fuqi)', q, re.I):
            break
        items.append(q)
    else:
        return None
    if not items:
        return None
    if court and all(INERT_RULING.match(q) and not re.search(r'shfuqiz|pranimin\s+e\s+kërkesës\s*(?:$|[.,;])|'
                                                             r'papajtueshm', q, re.I) for q in items):
        return 'its ruling only rejects the request, declares it inadmissible or ends the case'
    if assembly and len(items) == 1 and INERT_ASSEMBLY.match(items[0]):
        return ('it only overrides the President’s decree returning a law for reconsideration' if items[0].lower().startswith('rrëz')
                else 'it only does not approve a draft law')
    return None


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


def cached_result(rc: dict, x: dict, byid: dict):  # x: the listing record, with main()'s own inputs under '_'
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


def repeals_whole(paras: list[str], ref: tuple) -> bool:
    """Does this text repeal the act ref as a whole: a paragraph citing it that says "shfuqiz...", with no provision
    named before the citation (in its sentence) or right after it?"""
    for para in paras:
        for cref, st, en in cites(para):
            if cref != ref:
                continue
            head = para[:st]
            head = head[max(head.rfind('. '), head.rfind(';'), head.rfind(':')) + 1:]
            if re.search(r'shfuqiz', para, re.I) and not PARTIAL.search(head) and \
                    not PARTIAL.search(para[en:en + 40].split(',')[0]):
                return True
    return False


TYPE_WORD = re.compile(r'\b(vendim\w*|vkm\w*|udhëzim\w*|udhezim\w*|urdh[eë]r\w*|urdhr\w*|ligj\w*|akt\w*\s+normativ\w*)', re.I)
BARE_NR = re.compile(r'\bnr\.?\s*(\d+)(?:\s*/\s*\d+)?\s*,?\s*(?:i\s+datës\s+|datë\s*|date\s*|data\s*|dt\.?\s*)'
                     r'(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})', re.I)
LIST_ITEM = re.compile(r'^\s*(?:[a-zë]{1,2}\)|-|•|\d+(?:\.\d+)*\s*[.)])')


def cites_wide(text: str):
    """cites(), and every "nr. N, datë D" (a "/n" suffix allowed) whose act type is the nearest type word before it
    on its line ("Vendimet nr. 1, datë ..., nr. 2, datë ...", "Urdhri i ministrit ... nr. 3, datë ..."). Only for
    reading a repeal QBZ links."""
    yield from cites(text)
    for m in BARE_NR.finditer(text):
        line_start = text.rfind('\n', 0, m.start()) + 1
        words = list(TYPE_WORD.finditer(text, max(line_start, m.start() - 250), m.start()))
        if not words:
            continue
        w = words[-1].group(1).lower()
        day = iso(m.group(2), m.group(3), m.group(4))
        if not day:
            continue
        if w.startswith('ligj'):
            ref = ('law', m.group(1), m.group(4))
        elif w.startswith(('udhëzim', 'udhezim')):
            ref = ('udhezim', m.group(1), day)
        elif w.startswith(('urdh',)):
            ref = ('urdher', m.group(1), day)
        elif w.startswith('akt'):
            ref = ('aktnormativ', m.group(1), day)
        else:
            ref = ('vkm', m.group(1), day)
        yield ref, m.start(), m.end()


def repeals_whole_wide(paras: list[str], ref: tuple) -> bool:
    """For confirming a repeal QBZ links, beyond repeals_whole: a citation cites_wide reads, outside any quoted title,
    whose own sentence (its cited title and a title broken over lines left out) says "shfuqizohet/n" or "revokohet/n"
    with no provision named before it; an item of a list whose opening line repeals ("Shfuqizohen ... si më
    poshtë:"); or an act a title names as repealed ("PËR SHFUQIZIMIN E URDHRIT NR. ...; URDHRIT NR. ...")."""
    joined, i = [], 0
    while i < len(paras):
        para, j = paras[i], i
        while para.count('“') > para.count('”') and j + 1 < len(paras) and j - i < 3:
            j += 1
            para = para + ' ' + paras[j]
        joined.append(para)
        i = j + 1
    for k, para in enumerate(joined):
        for cref, st, en in cites_wide(para):
            if cref != ref or para[:st].count('“') > para[:st].count('”'):
                continue
            head = para[:st]
            head = unquoted(head[max(head.rfind('. '), head.rfind(';'), head.rfind(':')) + 1:])
            tail = re.split(r'(?<![Nn][Rr])\.\s|;|:', unquoted(para[en:]), maxsplit=1)[0]
            if PARTIAL.search(head) or PARTIAL.search(tail.split(',')[0]):
                continue
            if re.search(r'shfuqi-?z|revokohe[tn]', head + ' ' + tail, re.I) and not re.search(r'ndrysh', tail, re.I):
                return True
            back = k - 1
            if LIST_ITEM.match(para):
                while back >= 0 and LIST_ITEM.match(joined[back]) and k - back < 60:
                    back -= 1
                if back >= 0 and joined[back].rstrip().endswith(':') and re.search(r'shfuqiz', joined[back], re.I) \
                        and not PARTIAL.search(unquoted(joined[back])):
                    return True
            back = k
            while back >= 0 and k - back <= 8 and (back == k or joined[back].rstrip().endswith((';', ',', '”', 'dhe'))):
                if re.match(r'P[ËE]R\s+SHFUQIZIMIN\s+E\s+(?:URDHR|UDHËZIM|VENDIM|LIGJ|AKT)', joined[back], re.I):
                    first = next(iter(cites_wide(joined[back])), None)
                    if first and not PARTIAL.search(joined[back][:first[1]]):
                        return True
                back -= 1
    return False


def approved_in_time(a: dict, prefix: str = '') -> None:
    """An act with the force of law (Kushtetuta, neni 101) loses its force from the start unless the Assembly
    approves it within 45 days: hold unless a law in QBZ's listing approves it no later than 45 days after it."""
    ap = APPROVED.get(ident(a))
    if TOUCHED is not None and ap:
        TOUCHED.append(f'id:{ap["id"]}')
    if not ap:
        raise Hold(f'{prefix}aktnormativ_approval_not_found')
    if ap['date'] > add_days(a['date'], 45):
        raise Hold(f'{prefix}aktnormativ_approved_after_45_days:{ap["date"]}')


REPEAL_HEAD = re.compile(r'(?:\d+(?:\.\d+)*\s*[.)]\s*)?(?:[a-zë]{1,2}\)\s*)?(?:Me\s+hyrjen\s+në\s+fuqi\s+të\s+këtij\s+'
                         r'\w+\s*,\s*)?(?:shfuqizohe[tn]\s*:?\s*)?(?:dhe\s+)?', re.I)
REPEAL_NOT_WHOLE = re.compile(r'ndrysh|bien\s+ndesh|kundërshtim|për\s+aq\s+sa|pjes|përveç|përjashtim|dispozit|'
                              r'përcaktime|\bpik|\bnen|shkronj|paragraf|kre\w*\b|aneks|shtojc|lidhj', re.I)


def repeals_whole_strictly(paras: list[str], ref: tuple) -> bool:
    """repeals_whole_strictly_once, or the same sentence read through cites_all (plural lists, qualified citations), or
    an item of a list whose opening line says "Shfuqizohen ...:" with nothing in the item naming a part of the act."""
    return repeals_whole_strictly_once(paras, ref) or repeals_whole_listed(paras, ref)


def repeals_whole_listed(paras: list[str], ref: tuple) -> bool:
    for k, para in enumerate(paras):
        for cref, st, en, gov in cites_all(para):
            if cref != ref or para[:st].count('“') > para[:st].count('”'):
                continue
            head = para[:gov]
            head = head[max(head.rfind('. '), head.rfind(';'), head.rfind(':')) + 1:]
            rest = para[en:]
            if REPEAL_HEAD.fullmatch(head.strip()):
                m = re.search(r'\bshfuqizohe[tn]\b', rest, re.I)
                if re.search(r'shfuqizohe[tn]', head, re.I):
                    between = re.split(r'(?<![Nn][Rr])[.;]\s', unquoted(rest))[0]
                elif m:
                    between = unquoted(rest[:m.start()])
                else:
                    between = None
                if between is not None:
                    between = BARE_NR.sub(' ', between)
                    if not REPEAL_NOT_WHOLE.search(between) and not NEXT_CITE.search(between) and \
                            not REPEAL_NOT_WHOLE.search(unquoted(para[gov:st])):
                        return True
            pre = LIST_ITEM.sub('', para[:gov], count=1).strip() if LIST_ITEM.match(para) else None
            if pre is not None and len(pre) < 40 and ',' not in pre and not any(True for _ in cites(pre)):
                item = unquoted(rest)
                if REPEAL_NOT_WHOLE.search(item) or REPEAL_NOT_WHOLE.search(unquoted(head)):
                    continue
                back = k - 1
                while back >= 0 and LIST_ITEM.match(paras[back]) and not paras[back].rstrip().endswith(':') \
                        and k - back < 60:
                    back -= 1
                if back >= 0 and paras[back].rstrip().endswith(':') and \
                        re.search(r'\bshfuqizohe[tn]\b|\bshfuqizimin\b', paras[back], re.I) and \
                        not REPEAL_NOT_WHOLE.search(unquoted(paras[back])):
                    return True
    return False


def repeals_whole_strictly_once(paras: list[str], ref: tuple) -> bool:
    """For a repeal QBZ does not link: a paragraph of the repealing act whose sentence starts with the citation of
    act ref (after its number, "Me hyrjen në fuqi të këtij ...," or "Shfuqizohet") and says "shfuqizohet/n", with
    nothing between the citation (outside the cited title) and that word naming a part of it, a condition ("që bien
    ndesh", "në kundërshtim") or an earlier amendment ("i ndryshuar")."""
    for para in paras:
        for cref, st, en in cites(para):
            if cref != ref:
                continue
            head = para[:st]
            head = head[max(head.rfind('. '), head.rfind(';'), head.rfind(':')) + 1:]
            if not REPEAL_HEAD.fullmatch(head.strip()):
                continue
            rest = para[en:]
            m = re.search(r'\bshfuqizohe[tn]\b', rest, re.I)
            if re.search(r'shfuqizohe[tn]', head, re.I):
                between = unquoted(rest[:m.start()] if m else rest)
                between = re.split(r'[.;]\s', between)[0]
            elif m:
                between = unquoted(rest[:m.start()])
            else:
                continue
            if not REPEAL_NOT_WHOLE.search(between) and not NEXT_CITE.search(between):
                return True
    return False


def repeal_version(cache: Path, memo: Path | None, x: dict, rx: dict | None, versions: list, laws: dict,
                   strict: bool = False) -> dict:
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
    if strict:
        if not ((repeals_whole(rp, ident(x)) and repeals_whole_strictly_once(rp, ident(x))) or
                repeals_whole_listed(rp, ident(x))):
            raise Hold('repeal_not_whole_or_not_cited')
    elif not repeals_whole(rp, ident(x)) and not repeals_whole_wide(rp, ident(x)):
        raise Hold('repeal_not_whole_or_not_cited')
    if rk == 'aktnormativ':
        approved_in_time(rx, 'repealer_')
    rg = rx.get('gazette') or {}
    try:
        rpub, rnote = issue_day(cache, rx)
    except Hold as h:
        raise Hold(f'repealer_publication_day:{h}')
    try:
        day, how = in_force(rk, '\n'.join(rp), rpub)
        late_clause_ok(rk, '\n'.join(rp), rx['id'])
    except Hold as h:
        raise Hold(f'repealer_{h}')
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
           'note': f'Repealed by {label} (Fletorja Zyrtare nr. {rg.get("number")}/{rg.get("year")}, {rpub}{rnote}); '
                   f'in force from {day}: {how}.'}
    if day == last:
        ver['same_day'] = True
    return ver


def inert_note(inert: tuple, byid: dict) -> str:
    """The version note's words on the acts whose titles name this one as changed but which changed nothing."""
    return ''.join(f' {law_ref(byid[i])[1]} names it in its title, but its own text shows it changed nothing: {why}.'
                   for i, why in inert)


def amended_marks(ids: list, byid: dict) -> dict:
    """2026-11-09: {'amended_by': [...], 'label': ...} for an act published as enacted that later acts change."""
    if not ids:
        return {}
    out = []
    for i in ids:
        b = byid.get(i) or {}
        out.append({'ref': f'qbz:{i}', 'title': f'{law_ref(b)[1]}: {title_of(b)}' if b else f'QBZ act {i}',
                    'url': f'{SITE}{b["eliPath"]}' if b.get('eliPath') else None, 'date': b.get('date')})
    return {'amended_by': out, 'label': 'amended, not consolidated'}


def compute(cache: Path, memo: Path | None, x: dict, kind: str, hist: bool, byid: dict, extra: tuple = (),
            full_number: bool = False, inert: tuple = (), amended: tuple = ()) -> tuple:
    """The act's part, slug, law record, act record and (for a history) the changing acts' records and decisions;
    raises Hold. Reads only x's own inputs (recorded in TOUCHED for --result-cache)."""
    hlaws: dict = {}
    hdec: list = []
    rel = read_json(cache, f'{API}/acts/{x["id"]}/relations')
    if rel is None:
        raise Hold('relations_not_fetched')
    repealers = sorted({r['actId'] for r in rel if r.get('direction') == 'in' and r.get('type') == 'REPEALS'} | set(extra))
    # 2026-11-09 (Romania standard): QBZ links an act as changing this one but keeps no consolidated version: the act
    # is published as enacted, labelled "amended, not consolidated" with the changing acts (was: held back).
    changers = sorted({r['actId'] for r in rel if r.get('direction') == 'in' and r.get('type') == 'CHANGES'})         if not hist else []
    if len(repealers) > 1:
        raise Hold('repealed_by_several:' + ','.join(map(str, repealers[:5])))
    if True:
        if True:
            published, pub_note = issue_day(cache, x)
            if kind == 'aktnormativ':
                approved_in_time(x)
            paras = text_of(cache, memo, x)
            if paras is None:
                raise Hold('text_not_fetched')
            if any(RE_NOTE.match(p) for p in paras):
                raise Hold('qbz_amendment_notes')
            tnote = ''
            if not header_ok(kind, x, paras):
                if not header_typeset(kind, x, paras):
                    raise Hold('header_mismatch')
                tnote = (' Its header prints its number and date with a typesetting slip (“' +
                         next(p for p in paras[:6] if re.search(r'\bNr\.?', p, re.I))[:60] +
                         '”); they are read as QBZ’s record gives them.')
            if hist:
                versions = history(cache, memo, x, kind, byid, published, paras, hlaws, hdec, pub_note)
            else:
                text = '\n'.join(paras)
                day, how = in_force(kind, text, published)
                late_clause_ok(kind, text, x['id'])
                units = split(paras, kind)
                if kind == 'ligj' and not any(k.startswith(('neni-', 'pika-')) for k in units):
                    raise Hold('no_articles')
                if repealers:  # as published, then the repeal
                    g0 = x['gazette']
                    versions = [{'from': day, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'],
                                 'units': units, 'credits': {},
                                 'note': f'As published in the Fletorja Zyrtare nr. {g0["number"]}/{g0["year"]} '
                                         f'({published}{pub_note}); in force from {day}: {how}.'}]
            if repealers:
                versions.append(repeal_version(cache, memo, x, byid.get(repealers[0]), versions, hlaws,
                                               strict=repealers[0] in extra))
                hist = True
        if tnote:
            if hist:
                versions[0]['note'] += tnote
        if inert and hist:
            versions[0]['note'] += inert_note(inert, byid)
        year = x['date'][:4]
        slug = year_key(kind, x) if kind in ('vendim', 'ligj', 'aktnormativ', 'dekret') else \
            f'{kind}-{year}-{x["date"][5:7]}{x["date"][8:10]}-{x["number"] if full_number else x["number"].split("-")[0]}'
        title = title_of(x)
        url = f'{SITE}{x["eliPath"]}' if x.get('eliPath') else None
        law = {'label': label_of(kind, x), 'title': title, 'kind': 'law' if kind == 'ligj' else 'decree',
               'enacted': x['date'], 'published': published, 'url': url, 'temporary_until': None,
               'restores': None, 'note': None}
        g = x['gazette']
        if hist:
            earlier = versions[0].pop('_earlier', None)
            marks = {}
            vs_q = read_json(cache, f'{API}/acts/{x["id"]}/versions') or []
            q = next((v for v in vs_q if (v.get('word') or {}).get('sha256') == x['word']['sha256']), None)
            if q and versions and versions[0].get('sha256') == x['word']['sha256']:
                # 2026-11-09: an act on main whose first version is QBZ's consolidated text (see history())
                marks = {'label': 'first version is a later consolidated text',
                         'label_note': f'QBZ gives no text of this act as published: its base-act file is its '
                                       f'consolidated version {q.get("versionNo")} (after '
                                       f'{(q.get("changedBy") or {}).get("number") or "a change QBZ does not name"}). '
                                       f'The version dated {versions[0]["from"]} therefore shows that later text.'}
            return (f'{HIST_PART[kind]}-{year}', slug, law,
                    {'slug': slug, 'short': short_of(title), 'title': title, 'url': url,
                     'first_law': None if earlier is not None else slug,
                     'earlier_laws': [slug] + earlier if earlier is not None else [], 'versions': versions,
                     **marks}, hlaws, hdec)
        return (f'{PART[kind]}-{year}', slug, law, {
            'slug': slug, 'short': short_of(title), 'title': title, 'url': url, 'first_law': slug,
            'earlier_laws': [],
            'versions': [{'from': day, 'source_url': SITE + x['word']['url'], 'sha256': x['word']['sha256'],
                          'units': units, 'credits': {},
                          'note': f'As published in the Fletorja Zyrtare nr. {g["number"]}/{g["year"]} ({published}{pub_note}); '
                                  f'in force from {day}: {how}. '
                                  + ('QBZ links later acts as changing it, but publishes no consolidated text: this is '
                                     'the act as published.' if changers or amended else
                                     'QBZ links no act as changing or repealing it.')
                                  + inert_note(inert, byid) + tnote}],
            **amended_marks(sorted(set(changers) | set(amended)), byid)}, {}, [])



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
    ap.add_argument('--kept', help='JSON {QBZ id: {slug, reason}}: acts already published that a citation found later '
                                   'would now hold; their one version keeps coming out exactly as published')
    ap.add_argument('--publish-history', action='store_true',
                    help='also mark the parts with consolidated histories (42-, 43-) as verified')
    a = ap.parse_args()
    kept = json.loads(Path(a.kept).read_text(encoding='utf-8')) if a.kept and Path(a.kept).exists() else {}
    if a.out:
        global PARTS
        PARTS = Path(a.out)
    cache = Path(a.cache)
    memo = Path(a.memo) if a.memo else None
    L = listing(cache)
    set_ambiguous(L)
    NUM_DATE.clear()
    for x in L:
        NUM_DATE.setdefault((x['number'].split('-')[0], x['date']), []).append(x)
        if x['type'] == 'Ligj':
            NUM_DATE.setdefault((x['number'].split('-')[0], x['date'][:4]), []).append(x)
    LISTING_FILES[:] = [str(cpath(cache, f'{API}/acts?size=100&page={i}'))
                        for i in range((read_json(cache, f'{API}/acts?size=100&page=0')['total'] + 99) // 100)]
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
        if p.name[:2] in OUR_PARTS:
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

    # Laws approving an act with the force of law ("Për miratimin e aktit normativ, me fuqinë e ligjit, nr. N, datë D").
    APPROVED.clear()
    for x in L:
        t = norm(x['title'])
        m = re.match(r'P[ëe]r\s+miratimin\s+e\s+aktit\s+normativ', t, re.I)
        if x['type'] == 'Ligj' and m:
            for ref, st, _ in cites(t):
                if ref[0] == 'aktnormativ' and st < 40:
                    if ref not in APPROVED or x['date'] < APPROVED[ref]['date']:
                        APPROVED[ref] = x
    # Citations that say an act was changed: other acts' titles, then the texts held here. In a title, an act cited
    # as the one that made an earlier change or ratification ("të ndryshuar me ligjin nr. ...", "ratifikuar me ..."),
    # as a basis ("në zbatim të", "sipas", ...), or as the act that approved an agreement or contract now amended
    # ("marrëveshja ..., miratuar me vendimin nr. ...") is not the act changed; nor is the act a law approves ("Për
    # miratimin e aktit normativ nr. ...").
    named: dict[tuple, set[int]] = defaultdict(set)
    for x in L:
        t = norm(x['title'])
        if x['kind'] != 'Akt bazë' or CHANGE_TITLE.search(t):
            approval = re.match(r'P[ëe]r\s+miratimin\s+e\s+aktit\s+normativ', t, re.I)
            agreement = re.search(r'marrëveshj|kontrat|memorand|protokoll|garanci', t, re.I) and \
                not re.search(r'rregullor|statut|\bkod|udhëzim|list|normativ|shtojc|aneks|tarif', t, re.I)
            for ref, st, _, gov in cites_all(t):
                before = t[max(0, gov - 40):gov]
                if gov != st and (t[:gov].count('“') > t[:gov].count('”') or not CHANGE_TITLE.search(t[:gov]) or
                                  re.search(r'zbatim', t[:gov], re.I)):
                    # a citation only cites_all reads counts in a title only after the change word and outside any
                    # quoted title or act being implemented
                    continue
                if re.search(r'(?:\b(?:ndryshuar[a]?|ratifikuar[a]?)\s+me|\bnë\s+zbatim\s+të|\bnë\s+mbështetje\s+të|'
                             r'\bsipas|\bbazuar\s+në)\s*$', before, re.I):
                    continue
                if agreement and re.search(r'\bmiratuar[a]?\s+me\s*$', before, re.I):
                    continue
                if approval and ref[0] == 'aktnormativ' and st < 40:
                    continue
                named[ref].add(x['id'])
    count = defaultdict(int)
    numbers: dict[tuple, set] = defaultdict(set)
    for x in L:
        if kind_of(x):
            count[(kind_of(x), ident(x))] += 1
            numbers[(kind_of(x), ident(x))].add(x['number'])
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
        # 2026-11-09: a base act of a kind published here that QBZ gives only as a PDF (or with no file) is listed,
        # not dropped silently.
        if not kind and x['kind'] == 'Akt bazë' and kind_of(dict(x, word={'url': '.docx', 'sha256': ''})):
            holds.append({'id': x['id'], 'kind': kind_of(dict(x, word={'url': '.docx', 'sha256': ''})),
                          'number': x['number'], 'date': x['date'], 'title': x['title'][:160],
                          'reason': 'no_word_text:' + ('pdf_only' if x.get('pdf') else 'no_file')})
            continue
        if not kind:
            continue
        ref = ident(x)
        hist = bool(x.get('versions'))
        hlaws: dict = {}
        hdec: list = []
        kept_now = False
        try:
            if ('id', str(x['id'])) in held_old or (kind == 'ligj' and (ref[1], ref[2]) in held_old):
                continue  # on main already, under its earlier name
            # instructions or orders of one day numbered N-1, N-2, ... (N/1, N/2 in their texts): each keeps its full
            # number in its slug; any other repeat of a number holds every act that has it
            full_number = False
            if count[(kind, ref)] > 1:
                if kind in MINISTERIAL.values() and len(numbers[(kind, ref)]) == count[(kind, ref)] and \
                        all('-' in n for n in numbers[(kind, ref)]):
                    full_number = True
                else:
                    raise Hold('duplicate_number')
            if kind == 'ligj':
                m = BUDGET.search(x['title'])
                if m and m.group(4) < retrieved[:4]:
                    raise Hold('spent_budget_law')
            extra: tuple = ()
            inert: list = []
            amended: tuple = ()
            if not hist:
                own = {x['id']}
                if (named.get(ref, set()) | cited_changed.get(ref, set())) - own:
                    rel0 = read_json(cache, f'{API}/acts/{x["id"]}/relations') or []
                    own |= {r['actId'] for r in rel0 if r.get('direction') == 'in' and r.get('type') == 'REPEALS'}
                others = (named.get(ref, set()) | cited_changed.get(ref, set())) - own
                # an act whose title names this one but whose own text shows it changed nothing (changes_nothing)
                for i in sorted(others):
                    if i in named.get(ref, set()) and i not in cited_changed.get(ref, set()):
                        if i not in INERT:
                            INERT[i] = changes_nothing(cache, memo, byid[i])
                        if INERT[i]:
                            inert.append((i, INERT[i]))
                others -= {i for i, _ in inert}
                # a repeal QBZ does not link: every act citing it as changed repeals it as a whole in its own text
                if others and all(repeals_whole_strictly(text_of(cache, memo, byid[i]) or [], ref) for i in sorted(others)
                                  if byid[i].get('word')) and all(byid[i].get('word') for i in others):
                    extra = tuple(sorted(others))
                    others = set()
                # An act already published (listed in --kept) that such a citation found later would hold keeps its
                # one version as published: right on its day, its later versions are added only from QBZ's texts or,
                # when every act citing it repeals it as a whole (extra), as that repeal.
                # 2026-11-09 (Romania standard): named as changed in a later act's title, or cited as changed by a
                # later text, and QBZ keeps no consolidated version: published as enacted and labelled (was: held),
                # an act already published as well.
                if others:
                    amended = tuple(sorted(others))
                if str(x['id']) in kept and others:
                    extra, others, kept_now = (), set(), True
            xk = x
            if extra or kind == 'aktnormativ' or full_number or inert or amended:
                xk = dict(x, _extra=list(extra), _approved=(APPROVED.get(ref) or {}).get('id'), _full=full_number)
                if amended:
                    xk['_amended'] = list(amended)
                if inert:
                    xk['_inert'] = [list(t) for t in inert]
            res = cached_result(rc, xk, byid)
            if res is None:
                global TOUCHED
                TOUCHED = []
                try:
                    res = ('ok',) + compute(cache, memo, x, kind, hist, byid, extra, full_number,
                                                   tuple(inert), amended)
                except Hold as h:
                    res = ('hold', str(h))
                files, TOUCHED = TOUCHED, None
                store_result(rc, xk, byid, files, res)
            if res[0] == 'hold':
                raise Hold(res[1])
        except Hold as h:
            holds.append({'id': x['id'], 'kind': kind, 'number': x['number'], 'date': x['date'],
                          'title': x['title'][:160], 'reason': str(h)})
            continue
        _, part_name, slug, law, act, hlaws, hdec = res
        if kept_now:
            if slug != kept[str(x['id'])].get('slug'):
                holds.append({'id': x['id'], 'kind': kind, 'number': x['number'], 'date': x['date'],
                              'title': x['title'][:160], 'reason': 'kept_act_changed:' + slug})
                continue
            if len(act['versions']) == 1:  # with a repeal QBZ links, it goes on as a history in its usual part
                part_name = part_name[:2] + '-mbajtur'
        notes =' '.join(v.get('note') or '' for v in act['versions'])
        used = [k for k, mark in RULE_MARKS if mark in notes]
        if extra:
            used.append('text_repeal')
        if kind == 'aktnormativ':
            used.append('aktnormativ')
        if kind == 'dekret':
            used.append('dekret')
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
        if part_name[:2] in HIST_PARTS:
            part.setdefault('extra_decisions', []).extend(hdec)
        if used:
            part.setdefault('rules', set()).update(used)
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
                '46': 'instructions (udhëzime)', '47': 'orders (urdhra)',
                '48': 'acts with the force of law of the Council of Ministers (akte normative)',
                '49': 'acts with the force of law of the Council of Ministers (akte normative)',
                '50': 'normative decrees of the President (dekrete)',
                '51': 'normative decrees of the President (dekrete)'}[name[:2]]
        rules = p.pop('rules', set())
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
        if name[:2] in ('50', '51'):
            p['decisions'][1] = ('Its in-force day comes from its own clause, counted from the publication day of its '
                                 'Fletorja Zyrtare issue (“menjëherë”: the publication day, the first day the published '
                                 'decree can bind), or the day it names; any other clause holds it back.')
        if name.endswith('-mbajtur'):
            p['sources'][0]['notes'] = 'Each act’s .docx as published in the Fletorja Zyrtare and its issue’s publication day.'
            p['decisions'][0] = (
                f'These {what} were published here, as published in the Fletorja Zyrtare, when QBZ linked no act as '
                'changing or repealing them and no text held here cited them as changed. A text read since cites '
                'each in words that may mean it was changed. Each keeps its one version exactly as published; a later '
                'version is added only from QBZ’s consolidated texts.')
        if name[:2] in HIST_PARTS:
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
        p['decisions'] += [RULES[k] for k, _ in RULE_ORDER if k in rules]
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
        if ok and (name[:2] not in HIST_PARTS or a.publish_history) and \
                (name[:2] not in ('44', '45', '46', '47') or a.publish_ministerial):
            msg = (f'{name}: {len(p["acts"])} acts as published, each checked by parse_acts.py against QBZ’s '
                   f'relations, listing titles and the texts held (no change or repeal found).\n') \
                if not name.endswith('-mbajtur') else \
                (f'{name}: {len(p["acts"])} acts published earlier, kept as published (parse_acts.py --kept).\n')
            if not pub.exists() or pub.read_text(encoding='utf-8') != msg:
                pub.write_text(msg, encoding='utf-8', newline='\n')
        elif pub.exists():
            pub.unlink()
        written.append((name, len(p['acts'])))
    # A kept-acts part this run did not write (its acts released or none kept) must not linger beside their new part.
    for f in PARTS.glob('4?-mbajtur.json'):
        if f.stem not in {n for n, _ in written}:
            f.unlink()
            f.with_suffix('.PUBLISH').unlink(missing_ok=True)
    if a.report:
        Path(a.report).write_text(''.join(json.dumps(h, ensure_ascii=False) + '\n' for h in holds), encoding='utf-8')
    reasons = defaultdict(int)
    for h in holds:
        reasons[h['reason'].split(':')[0]] += 1
    print(json.dumps({'published': sum(n for _, n in written), 'held': len(holds), 'held_by_reason': dict(reasons),
                      'parts': len(written)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
