"""Compute every number for the 20 charts into <build>/data.json.

    python prep.py <build-dir>

Reads, from <build> (written by make.py): log.tsv (one line per commit), names.tsv (the files of each commit),
heads.jsonl (the preamble, the approval or signature block and, for removed acts, the title line of each act),
numbers.jsonl (the texts of the minimum wage and pension decisions) and repo/ (data/laws.csv, registry/data/laws.csv,
data/held.json). Every rule that reads a category out of a title or a text is in this file.
"""
import collections, csv, json, os, re, statistics, sys
from datetime import date, timedelta

B = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '.build')
R = os.path.join(B, 'repo')
OUT, PROFILE = {}, {}
D = lambda s: date.fromisoformat(s[:10])
MED = lambda v: statistics.median(v) if v else None


def dd(s):
    """'14.7.2000' -> date"""
    m = re.match(r'\s*(\d{1,2})\s*\.\s*(\d{1,2})\s*\.\s*(\d{4})', s or '')
    if not m:
        return None
    try:
        return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()


# ------------------------------------------------------------------ the history
C = []  # newest first
with open(os.path.join(B, 'log.tsv'), encoding='utf-8') as fh:
    head = fh.readline().rstrip('\n').split('\t')
    for line in fh:
        r = dict(zip(head, line.rstrip('\n').split('\t')))
        r['f'] = []
        C.append(r)
BY = {r['sha']: r for r in C}
with open(os.path.join(B, 'names.tsv'), encoding='utf-8') as fh:
    for line in fh:
        h, st, f = line.rstrip('\n').split('\t')
        BY[h]['f'].append((st, f))
print('commits', len(C))

OLD = {'kushtetuta': 'kushtetuta/1998', 'pastrimi-i-parave': 'ligj/2008/9917', 'shtetesia': 'ligj/2020/113', 'tatimi-mbi-te-ardhurat': 'ligj/2023/29'}
KINDS = ('ligj', 'vendim', 'udhezim', 'urdher', 'aktnormativ', 'dekret', 'kushtetuta', 'local', 'caselaw', 'kerkese', 'rezolute', 'rregullore',
         'deklarate', 'autorizim', 'konvente', 'marreveshje', 'njoftim', 'licenca', 'memorandum')


def act_id(f):
    """the act folder of a file, the same for both layouts of the history (before and after 4 November 2026)"""
    p = f.split('/')
    if p[0] == 'kushtetuta':
        return 'kushtetuta/1998'
    if p[0] in OLD and len(p) == 2:
        return OLD[p[0]]
    m = re.match(r'^ligji-(\d+)-(\d{4})$', p[0])
    if m:
        return f'ligj/{m.group(2)}/{m.group(1)}'
    if p[0] in KINDS and len(p) > 2:
        return '/'.join(p[:-1])
    return None


SKIP_KIND = {'', 'layout', 'documentation', 'correction'}
PROV = lambda f: not f.endswith(('README.md', 'record.json'))
first = {}      # act -> first commit carrying its text or record
events = collections.defaultdict(dict)  # act -> {in-force day: [authors]} for later versions
removed = {}    # act -> (day, author, commit) of the last removal of its text
for c in reversed(C):  # oldest first
    if c['Kind'] in SKIP_KIND:
        continue
    acts = collections.defaultdict(set)
    for st, f in c['f']:
        a = act_id(f)
        if a and (PROV(f) or c['Kind'] in ('metadata', 'caselaw')):
            acts[a].add(st)
    day = c['In-force'] or c['date']
    for a, sts in acts.items():
        if a not in first:
            first[a] = c
            continue
        if 'D' in sts and not ({'A', 'M'} & sts):
            removed[a] = (day, c['author'], c)
            continue
        if a in removed and ({'A'} & sts):
            removed.pop(a, None)  # put back (a correction or a later version)
        if day[:10] != (first[a]['In-force'] or first[a]['date'])[:10] and c['Kind'] not in ('metadata', 'caselaw'):
            events[a].setdefault(day[:10], []).append(c['author'])
print('acts', len(first), 'with later versions', len(events), 'removed', len(removed))

# the tree at the tip: which act folders still hold text
live = set()
gone = set()
state = {}
for c in C:  # newest first: the first status seen for a file is its state at the tip
    for st, f in c['f']:
        if f not in state:
            state[f] = st
for f, st in state.items():
    a = act_id(f)
    if a and PROV(f) and st != 'D':
        live.add(a)
for a in first:
    if a not in live:
        gone.add(a)
heads = collections.defaultdict(dict)
with open(os.path.join(B, 'heads.jsonl'), encoding='utf-8') as fh:
    for line in fh:
        r = json.loads(line)
        a, nm = r['p'].rsplit('/', 1)
        heads[a][nm] = r['t']
print('heads', len(heads))


def title_of(a):
    """the full title of an act: preamble title lines, else the README title, else the commit's subject or Act trailer"""
    h = heads.get(a, {})
    if 'hyrje.md' in h:
        lines = [l.strip() for l in h['hyrje.md'].split('\n') if l.strip()]
        tl = []
        for l in lines:
            if re.match(r'(?i)(n[ëe] mb[ëe]shtetje|n[ëe] zbatim|bazuar n[ëe]|kuvendi\b|k\s*u\s*v\s*e\s*n\s*d\s*i)', l):
                break
            if re.match(r'(?i)^(l\s*i\s*g\s*j|ligj|v\s*e\s*n\s*d\s*i\s*m|vendim|akt normativ|udhëzim|urdh[ëe]r|nr\.?\s*\d)', l) and len(l) < 60:
                continue
            tl.append(l)
        t = clean(' '.join(tl))
        if t:
            return t
    if 'README.md' in h:
        t = clean(h['README.md'].lstrip('# '))
        if t:
            return t
    c = first.get(a)
    if not c:
        return ''
    s = c['subject']
    if c['Kind'] in ('as-enacted', 'consolidated', 'metadata'):
        return clean(s)
    return clean(c['Act'] or re.sub(r'\s*\(.*$', '', s))


def pick(rules, t, default='other'):
    """the first rule whose pattern matches at the start of a word in t (so 'sport' does not match 'transportit')"""
    return next((k for k, rx in rules if re.search(r'(?<!\w)(?:' + rx + ')', t)), default)


def rd(path):
    return list(csv.DictReader(open(os.path.join(R, path), encoding='utf-8')))


LAWCSV = rd('registry/data/laws.csv') + rd('data/laws.csv')
HELD = json.load(open(os.path.join(R, 'data/held.json'), encoding='utf-8'))['acts']

# ------------------------------------------------------------------ I. laws: every law the repository knows, by number
LAW = {}  # (number, year) -> {t, adopted, src}


def law_add(n, y, src, t=None, adopted=None):
    try:
        k = (int(n), int(y))
    except ValueError:
        return
    d = LAW.setdefault(k, {'t': '', 'adopted': None, 'src': set()})
    d['src'].add(src)
    if t and not t.startswith('(') and len(t) > len(d['t']):
        d['t'] = t
    if adopted and not d['adopted']:
        d['adopted'] = adopted


law_folder = {}
for a in first:
    p = a.split('/')
    if p[0] == 'ligj' and len(p) == 3 and p[2].isdigit():
        law_folder[(int(p[2]), int(p[1]))] = a
for (n, y), a in law_folder.items():
    law_add(n, y, 'folder', title_of(a))
for r in LAWCSV:
    m = re.match(r'Ligji nr\. (\d+)(?:/(\d{4}))?', r['label'])
    if m and (m.group(2) or r['enacted'][:4]):
        law_add(m.group(1), m.group(2) or r['enacted'][:4], 'csv', clean(r['title']), dd(r['label'].split('datë')[-1]) if 'datë' in r['label'] else (D(r['enacted']) if r['enacted'] else None))
for h in HELD:
    if h['kind'] == 'ligj' and h['number'].isdigit():
        law_add(h['number'], h['date'][:4], 'held', clean(h['title']), D(h['date']))
print('laws known', len(LAW))

# adoption dates and promulgation: the block "Miratuar në datën ... Shpallur me dekretin nr. ..., datë ... Presidentit ..., <name>"
PRES = [('alia', r'Ramiz\s+Alia'), ('berisha', r'Sali\s+Berisha'), ('meidani', r'Rexhep\W*Meidani'), ('moisiu', r'A[lf]+red\s+Moisiu'),
        ('topi', r'Bamir\s+Topi'), ('nishani', r'Bujar(\s+nishani)?\b'), ('meta', r'Ilir\s+Meta'), ('begaj', r'Bajram\s+Begaj')]


def promulgation(t):
    tt = clean(t)
    o = {'said': bool(re.search(r'Shpallur', tt, re.I))}
    m = re.search(r'Miratuar\s+(?:në\s+datën|më\s+datë|me\s+datë|n[ëe]\s+daten|më|në)\s*:?\s*(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{4})', tt, re.I)
    if m:
        o['adopted'] = dd(m.group(1))
    m = re.search(r'Shpallur\s+me\s+dekret(?:in)?\s*(?:nr\.?)?\s*([\d.\s]*?)\s*,?\s*(?:datë|date|dt\.?)\s*(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{4})(.*)', tt, re.I)
    if m:
        o['decree'] = dd(m.group(2))
        o['no'] = re.sub(r'\D', '', m.group(1))
        for k, rx in PRES:
            if re.search(rx, m.group(3), re.I):
                o['pres'] = k
                break
    return o


for (n, y), a in law_folder.items():
    h = heads.get(a, {})
    c = first.get(a)
    en = D(c['Enacted']) if c and c['Enacted'] else None
    pr = promulgation(h['zz-miratuar.md']) if 'zz-miratuar.md' in h else None
    LAW[(n, y)]['adopted'] = (pr or {}).get('adopted') or en or LAW[(n, y)]['adopted']
    LAW[(n, y)]['pr'] = pr
    LAW[(n, y)]['pub'] = D(c['Published']) if c and c['Published'] else None

# c01a: laws adopted each year, from the numbers they were given; the laws whose text the repository holds
nums = collections.defaultdict(list)
for (n, y) in LAW:
    nums[y].append(n)
issued = {}
for y in range(2012, 2027):  # since 2012 each year's laws are numbered from 1
    v = sorted(nums.get(y, []))
    top = [x for i, x in enumerate(v) if i and x - v[i - 1] <= 25]  # the last number in the dense run (a typo far above is not a law)
    issued[y] = top[-1] if top else (v[-1] if v else 0)


def boundary(lo, hi):
    """the first number of year hi: the cut between the numbers dated lo and hi that misplaces the fewest"""
    a, b = sorted(nums.get(lo, [])), sorted(nums.get(hi, []))
    best = None
    for cut in sorted(set(a + b)):
        err = sum(1 for x in a if x >= cut) + sum(1 for x in b if x < cut)
        if best is None or err < best[0]:
            best = (err, cut)
    return best[1]


cut = {y: boundary(y - 1, y) for y in range(2000, 2012)}
for y in range(2000, 2011):
    issued[y] = cut[y + 1] - cut[y]
v11 = sorted(x for x in nums[2011] if x >= cut[2011])
issued[2011] = v11[-1] - cut[2011] + 1
held_by_year = collections.Counter(y for (n, y) in law_folder)
OUT['c01'] = {'laws': [{'y': y, 'n': issued[y], 'held': held_by_year[y]} for y in range(2000, 2027)]}
print('c01 laws', [(r['y'], r['n'], r['held']) for r in OUT['c01']['laws']])

# c01b: decisions of the Council of Ministers (numbered from 1 each year)
VKM = collections.defaultdict(set)
vkm_folder = {}
for a in first:
    p = a.split('/')
    if p[0] == 'vendim' and len(p) == 3 and p[1].isdigit() and p[2].isdigit():
        VKM[int(p[1])].add(int(p[2]))
        vkm_folder[(int(p[2]), int(p[1]))] = a
for r in LAWCSV:
    m = re.match(r'Vendimi i Këshillit të Ministrave nr\. (\d+), datë ([\d.]+)', r['label'])
    if m and dd(m.group(2)):
        VKM[dd(m.group(2)).year].add(int(m.group(1)))
for h in HELD:
    if h['kind'] == 'vendim' and h['number'].isdigit():
        VKM[int(h['date'][:4])].add(int(h['number']))
for c in C:
    m = re.match(r'Vendimi i Këshillit të Ministrave nr\. (\d+), datë ([\d.]+)', c['author'])
    if m and dd(m.group(2)):
        VKM[dd(m.group(2)).year].add(int(m.group(1)))
vrows = []
for y in range(2000, 2027):
    v = sorted(VKM[y])
    top = [x for i, x in enumerate(v) if i and x - v[i - 1] <= 40]
    vrows.append({'y': y, 'n': top[-1] if top else 0, 'held': sum(1 for (n, yy) in vkm_folder if yy == y)})
OUT['c01']['vkm'] = vrows
print('c01 vkm', [(r['y'], r['n'], r['held']) for r in vrows])

# c02: when the Assembly adopts laws: month and weekday of adoption
cal = collections.Counter()
wd = collections.Counter()
for (n, y), d in LAW.items():
    ad = d['adopted']
    if not ad or ad.year != y or not (2000 <= y <= 2026):
        continue
    cal[(y, ad.month)] += 1
    wd[ad.weekday()] += 1
OUT['c02'] = {'grid': [[y, m, cal[(y, m)]] for y in range(2000, 2027) for m in range(1, 13)], 'wd': [wd[i] for i in range(7)], 'n': sum(cal.values())}
print('c02', OUT['c02']['n'], OUT['c02']['wd'], [sum(cal[(y, m)] for y in range(2000, 2027)) for m in range(1, 13)])

# ------------------------------------------------------------------ law types read from titles (word boundaries; "Other" stays visible)
RATIF = re.compile(r'\b(ratifikim|aderim)\w*|\bmiratimin e (marrëveshj|konvent|protokoll|amendament)', re.I)
APPR101 = re.compile(r'\bmiratimin e aktit normativ', re.I)
AMEND = re.compile(r'^(për\s+)?(disa\s+|një\s+)?(ndryshim|ndryshime|shtes[ëa]|plotësim|plotësime|shfuqizim)\w*\b', re.I)
BUDGET = re.compile(r'\bbuxhet', re.I)


def law_type(t, pre=''):
    t = clean(t)
    if APPR101.search(t) or re.search(r'\b101\b', pre):
        return 'appr'
    if RATIF.search(t) or re.search(r'\b121\b', pre):
        return 'ratif'
    if AMEND.search(t):
        return 'amend'
    if BUDGET.search(t):
        return 'budget'
    return 'new'


# c03: how long new laws are (articles in the text as enacted)
c03 = collections.defaultdict(list)
c03ex = collections.Counter()
PER = [('p1', 2000, 2004), ('p2', 2005, 2009), ('p3', 2010, 2014), ('p4', 2015, 2019), ('p5', 2020, 2026)]
for (n, y), a in law_folder.items():
    c = first.get(a)
    if not c or not c['author'].startswith('Ligji nr.') or not re.search(r'\b' + str(n) + r'\b', c['author']):
        continue  # the first version must be the law as enacted
    arts = sum(1 for st, f in c['f'] if st == 'A' and act_id(f) == a and re.match(r'neni-\d+\.md$', f.rsplit('/', 1)[1]))
    if not arts:
        continue
    pre = clean(heads.get(a, {}).get('hyrje.md', ''))[:700]
    ty = law_type(LAW[(n, y)]['t'], re.search(r'mbështetje të (.*?)Kushtetutës', pre).group(1) if re.search(r'mbështetje të (.*?)Kushtetutës', pre) else '')
    if ty != 'new':
        c03ex[ty] += 1
        continue
    per = next((k for k, lo, hi in PER if lo <= y <= hi), None)
    if per:
        c03[per].append([arts, n, y])
OUT['c03'] = {'rows': [{'k': k, 'lo': lo, 'hi': hi, 'pts': c03[k], 'med': MED([p[0] for p in c03[k]])} for k, lo, hi in PER], 'excluded': dict(c03ex)}
print('c03', [(r['k'], len(r['pts']), r['med']) for r in OUT['c03']['rows']], dict(c03ex))

# c04: the Assembly's acts other than laws (decisions, resolutions, declarations), 2000-2010
KUV = [('decree', r'\bdekret'), ('elect', r'\b(zgjedhj\w*|zgjedhur|emërim\w*|shkarkim\w*|lirim\w*|pëlqim\w*|mosdhënie\w*|mandat\w*|largim\w*|ngarkim\w*|zëvendësim\w*|vërtetim\w*|caktim\w* e (anëtar|kryetar|zëvendës|përfaqësues|sekretar))\b'),
       ('committee', r'\bkomision\w*|\bkomitet\w*|\bgrup\w* (parlamentar|pune)|\bnënkomision')]
kuv = collections.defaultdict(collections.Counter)
kuv_ex = collections.defaultdict(list)
for a, c in first.items():
    p = a.split('/')
    if p[0] not in ('vendim', 'rezolute', 'deklarate') or len(p) < 2 or p[1] != 'kuvendi-i-shqiperise':
        continue
    y = int((c['Enacted'] or c['date'])[:4])
    if not 2000 <= y <= 2010:
        continue
    t = clean(c['subject'])
    if p[0] == 'deklarate':
        k = 'decl'
    elif p[0] == 'rezolute':
        k = 'res'
    elif re.match(r'^(vendim|rezolutë|deklaratë)\s+nr\.', t, re.I) or not re.search(r'[a-zë]{4}', t.lower()):
        k = 'untitled'
    else:
        k = pick(KUV, t.lower())
    kuv[y][k] += 1
    kuv_ex[k].append(t[:120])
OUT['c04'] = [{'y': y, **kuv[y]} for y in range(2000, 2011)]
print('c04', OUT['c04'])
for k, v in kuv_ex.items():
    print('   c04', k, len(v), v[:3])

# c05: promulgation of laws by decree of the President (art. 84)
pdates = collections.defaultdict(list)
rows05 = []
for (n, y), a in law_folder.items():
    d = LAW[(n, y)]
    pr = d.get('pr')
    if pr is None:
        continue
    ad = d['adopted']
    if not ad or not 2000 <= ad.year <= 2026:
        continue
    if pr.get('decree'):
        days = (pr['decree'] - ad).days
        if -1 <= days <= 400:
            k = 'd20' if days <= 20 else 'dlate'
            if pr.get('pres'):
                pdates[pr['pres']].append(pr['decree'])
        else:
            k, days = 'unread', None  # a date that cannot be the decree's (a typo in the text)
    elif pr['said']:
        k, days = 'unread', None
    else:
        k, days = 'nodec', None
    rows05.append({'a': a, 'n': n, 'y': y, 'ad': ad.isoformat(), 'k': k, 'days': days, 'p': pr.get('pres'), 'no': pr.get('no'), 'type': law_type(d['t'])})
# each President's span: runs of consecutive decrees signed by the same President (a run of fewer than 10 is a typo in a date)
seqp = sorted((d, p) for p, ds in pdates.items() for d in ds)
runs = []
for d, p in seqp:
    if runs and runs[-1][0] == p:
        runs[-1][2] = d
        runs[-1][3] += 1
    else:
        runs.append([p, d, d, 1])
TERMS = {}
for p, lo, hi, n in [r for r in runs if r[3] >= 10]:
    if p in TERMS:
        TERMS[p][1] = hi.isoformat()
    else:
        TERMS[p] = [lo.isoformat(), hi.isoformat()]
order = ['meidani', 'moisiu', 'topi', 'nishani', 'meta', 'begaj']


def pres_on(day):
    """the President whose decrees span the day; between two spans, the later one"""
    for p in order:
        if p in TERMS and TERMS[p][0] <= day <= TERMS[p][1]:
            return p
    for p in order:
        if p in TERMS and day < TERMS[p][0]:
            return p
    return order[-1]


for r in rows05:
    if not r['p']:
        r['p'] = pres_on(r['ad'])
yr05 = collections.defaultdict(collections.Counter)
for r in rows05:
    yr05[int(r['ad'][:4])][r['k']] += 1
cards05 = {}
for p in order:
    v = [r for r in rows05 if r['p'] == p]
    cards05[p] = {'n': len(v), 'dec': sum(1 for r in v if r['k'] in ('d20', 'dlate')), 'late': sum(1 for r in v if r['k'] == 'dlate'),
                  'nodec': sum(1 for r in v if r['k'] == 'nodec'), 'med': MED([r['days'] for r in v if r['days'] is not None])}
OUT['c05'] = {'years': [{'y': y, **yr05[y]} for y in range(2000, 2027)], 'terms': {p: TERMS[p] for p in order if p in TERMS}, 'cards': cards05,
              'nodec': [[r['n'], r['y'], r['ad'], LAW[(r['n'], r['y'])]['t'][:140], r['p']] for r in sorted(rows05, key=lambda r: r['ad']) if r['k'] == 'nodec']}
print('c05', [(y, dict(yr05[y])) for y in range(2017, 2024)], cards05, TERMS)

# ------------------------------------------------------------------ II. the government
# Prime Ministers: the signature on the decisions of the Council of Ministers ("KRYEMINISTRI Edi Rama")
PMS = [('meta', r'Ilir\s+Meta'), ('majko', r'Pandeli\s+Majko'), ('nano', r'Fatos\s+Nano'), ('berisha', r'Sali\s+Berisha'), ('rama', r'Edi\s+Rama')]
pmd = collections.defaultdict(list)
for (n, y), a in vkm_folder.items():
    s = heads.get(a, {}).get('zz-nenshkrimi.md', '')
    c = first.get(a)
    if not s or not c or not c['Enacted']:
        continue
    for k, rx in PMS:
        if re.search(rx, s):
            pmd[k].append(D(c['Enacted']))
            break
# terms: runs of consecutive decisions signed by the same Prime Minister (a run of fewer than 15 is a stray signature)
seq = sorted((d, k) for k, ds in pmd.items() for d in ds)
runs = []
for d, k in seq:
    if runs and runs[-1][0] == k:
        runs[-1][2] = d
        runs[-1][3] += 1
    else:
        runs.append([k, d, d, 1])
merged = []
for r in [r for r in runs if r[3] >= 15]:
    if merged and merged[-1][0] == r[0]:
        merged[-1][2] = r[2]
        merged[-1][3] += r[3]
    else:
        merged.append(list(r))
PMT = [[k, lo.isoformat(), hi.isoformat(), n] for k, lo, hi, n in merged]
print('PM terms', PMT)


def pm_on(day):
    """the Prime Minister whose run of signatures covers the day (until the next run begins)"""
    for i, (k, lo, hi, n) in enumerate(PMT):
        nxt = PMT[i + 1][1] if i + 1 < len(PMT) else '9999'
        if day < nxt:
            return k
    return PMT[-1][0]


# c06: normative acts with the force of law (art. 101) and their approval by the Assembly
NA = {}


def na_add(nr, d, src, title=None, appr=None):
    if not d:
        return
    k = (int(nr), d.isoformat())
    x = NA.setdefault(k, {'src': set(), 't': '', 'appr': None})
    x['src'].add(src)
    if title and len(clean(title)) > len(x['t']):
        x['t'] = clean(title)
    if appr and (not x['appr'] or appr[1] < x['appr'][1]):
        x['appr'] = appr


NARX = re.compile(r'miratimin e aktit normativ\W+(?:me fuqin[ëe] e ligjit\W+)?nr\.?\s*(\d+)\s*,?\s*dat[ëe]\s*(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{4})(.*)', re.I)
for (n, y), d in LAW.items():
    m = NARX.search(d['t'])
    if m and d['adopted']:
        inner = re.sub(r'^[^“"«”]*[“"«”]+', '', m.group(3)).strip(' ”"“')
        na_add(m.group(1), dd(m.group(2)), 'approval', inner, (f'{n}/{y}', d['adopted'].isoformat()))
for r in LAWCSV:
    m = re.match(r'Akti normativ nr\. (\d+), datë ([\d.]+)', r['label'])
    if m:
        na_add(m.group(1), dd(m.group(2)), 'csv', r['title'] if not r['title'].lower().startswith('akt normativ') else None)
for h in HELD:
    if h['kind'] == 'aktnormativ' and h['number'].isdigit():
        na_add(h['number'], D(h['date']), 'held', h['title'])
for a, c in first.items():
    p = a.split('/')
    if p[0] == 'aktnormativ' and len(p) == 3 and c['Enacted']:
        na_add(p[2], D(c['Enacted']), 'folder', title_of(a))
TOPIC = [('covid', r'covid|pandemi|epidemi|infeksion|karantin|vaksin|pfizer|human vaccine|sputnik|sinovac|astrazeneca|coronavirus'),
         ('quake', r'tërmet|fatkeqësi\w* natyrore|rindërtim|të pastreha|strehim'),
         ('tax', r'tatim|taks\w*|akciz|tvsh|vlerës së shtuar|doganor|fiskal|kontribut'),
         ('budget', r'buxhet|financim|fondi?\b|fondit|shpenzim|huamarrje|garanci'),
         ('mil', r'forcave të armatosura|forcave ushtarake|ushtarak|misionin|\bnato\b|kontingjent|seebrig|afganistan')]
c06 = []
for (nr, d), x in sorted(NA.items(), key=lambda kv: kv[0][1]):
    t = x['t'].lower()
    tp = pick(TOPIC, t)
    days = (D(x['appr'][1]) - D(d)).days if x['appr'] else None
    c06.append({'nr': nr, 'd': d, 't': x['t'][:180], 'tp': tp, 'pm': pm_on(d), 'law': x['appr'][0] if x['appr'] else None,
                'ld': x['appr'][1] if x['appr'] else None, 'days': days})
OUT['c06'] = {'acts': c06, 'pmt': PMT, 'maxnr': {}}
mx = collections.defaultdict(int)
for r in c06:
    mx[int(r['d'][:4])] = max(mx[int(r['d'][:4])], r['nr'])
OUT['c06']['maxnr'] = {str(y): v for y, v in sorted(mx.items())}
print('c06', len(c06), collections.Counter(r['tp'] for r in c06), collections.Counter(r['d'][:4] for r in c06).most_common(6),
      collections.Counter(r['pm'] for r in c06))
print('c07 days', MED([r['days'] for r in c06 if r['days'] is not None]), [r for r in c06 if r['days'] is not None and r['days'] > 45])

# c08: who proposes the Council of Ministers' decisions (the preamble: "me propozimin e ministrit të ...")
AREA = [('rec', r'rindërtim'), ('fin', r'financ|ekonomi'), ('def', r'ministri\w* (?:të|i) mbrojtjes\b(?! sociale| së konsumatorit| së mjedisit)'),
        ('int', r'brendshëm|brendshme|rendit publik|pushtetit vendor|decentraliz'), ('jus', r'drejtësi'),
        ('for', r'punëve të jashtme|punët e jashtme|evropën|europën|integrim'),
        ('hea', r'shëndet|mirëqenie|mbrojtjes sociale|çështjeve sociale|punës\b|shanseve|sociale'), ('edu', r'arsim|shkenc|sport|rini'),
        ('inf', r'infrastruktur|energji|energjetik|transport|punëve publike|telekomunikacion|industri'), ('agr', r'bujqësi|ushqim|zhvillimit rural'),
        ('env', r'mjedis|turizm|pyje|ujërave|territor|zhvillimit urban|urbanistik'), ('cul', r'kultur'),
        ('pm', r'kryeministr|zëvendëskryeministr')]
c08 = collections.defaultdict(collections.Counter)
c08n = collections.Counter()
for (n, y), a in vkm_folder.items():
    pre = clean(heads.get(a, {}).get('hyrje.md', ''))
    if not pre or not 2000 <= y <= 2026:
        continue
    m = re.search(r'me\s+propozim(?:in)?\s+(?:e|të)?\s*(.{0,120})', pre, re.I)
    if not m:
        c08[y]['none'] += 1
        continue
    s = m.group(1).lower()
    s = re.split(r',?\s*këshilli i ministrave|\bvendosi\b', s)[0]
    k = pick(AREA, s)
    c08[y][k] += 1
    c08n[k] += 1
OUT['c08'] = {'years': [{'y': y, **c08[y]} for y in range(2000, 2027)], 'tot': dict(c08n)}
print('c08', c08n.most_common())

# c09: days from adoption to the Official Journal: decisions of the Council of Ministers, and laws
pub = collections.defaultdict(list)
publ = collections.defaultdict(list)
same = collections.Counter()
for (n, y), a in vkm_folder.items():
    c = first[a]
    if c['Enacted'] and c['Published'] and c['Kind'] in ('decree', 'as-enacted', 'publisher'):
        dd_ = (D(c['Published']) - D(c['Enacted'])).days
        if 0 <= dd_ <= 3650 and D(c['Enacted']).year == y:
            pub[y].append(dd_)
        if c['In-force']:
            same['same' if c['In-force'][:10] == c['Published'][:10] else 'other'] += 1
for (n, y), a in law_folder.items():
    c = first[a]
    ad = LAW[(n, y)]['adopted']
    if ad and c['Published'] and ad.year == y:
        dd_ = (D(c['Published']) - ad).days
        if 0 <= dd_ <= 3650:
            publ[y].append(dd_)
q = lambda v, f: sorted(v)[int(f * (len(v) - 1))] if v else None
OUT['c09'] = [{'y': y, 'n': len(pub[y]), 'med': MED(pub[y]), 'q1': q(pub[y], .25), 'q3': q(pub[y], .75), 'w7': sum(1 for x in pub[y] if x <= 7),
               'ln': len(publ[y]), 'lmed': MED(publ[y])} for y in range(2000, 2027)]
PROFILE['vkm_same_day'] = [same['same'], same['same'] + same['other']]
print('c09', [(r['y'], r['n'], r['med'], r['lmed']) for r in OUT['c09']], dict(same))

# c10: expropriations for public interest (decisions of the Council of Ministers, by the project named in the title)
EXP = [('road', r'\brrug\w*|autostrad|\bunaz\w*|by-?pass|mbikalim|\bnyj\w*|\bsegment\w*|\bure\b|\burës\b|\bxhiro'),
       ('energy', r'\bhec\b|hidrocentral|transmetim|nënstacion|energji|elektrik|gazsjellës|\btap\b|gazit|fotovolt|parku? (diellor|i erës)'),
       ('water', r'ujësjellës|kanalizim|ujëra|ujërave|vaditj|kullim|\bdig\w*|rezervuar|argjinatur|\blumi\w*|\bpotok|liqen|ujit'),
       ('rail', r'hekurudh|\bport\w*|aeroport|terminal|stacion\w*'),
       ('urban', r'shesh|rikualifikim|shkoll\w*|spital\w*|godin\w*|qendr\w*|stadium|\bpark\w*|zhvillim\w* urban|banes\w*|rindërtim|zona e re|zonës së re|kopsht|institut|varreza|muze|teat[ëe]r|lagje|kampus|universitet')]
c10 = collections.defaultdict(collections.Counter)
c10n = 0
for (n, y), a in vkm_folder.items():
    t = title_of(a).lower()
    if not re.search(r'\bshpronësim', t) or AMEND.search(t) or not 2000 <= y <= 2026:
        continue
    k = pick(EXP, t)
    dec = '00' if y < 2010 else '10' if y < 2020 else '20'
    c10[k][dec] += 1
    c10n += 1
OUT['c10'] = {'rows': [{'k': k, **c10[k]} for k in ['road', 'energy', 'water', 'rail', 'urban', 'other']], 'n': c10n,
              'years': dict(collections.Counter(y for (n, y), a in vkm_folder.items() if re.search(r'\bshpronësim', title_of(a).lower()) and not AMEND.search(title_of(a).lower())))}
print('c10', c10n, {k: dict(v) for k, v in c10.items()})

# c11: concessions and public-private partnerships (decisions and laws), by sector
CON = [('hpp', r'\bhec\b|hidrocentral|hidroenergji|centrale\w* hidro'), ('energy', r'energji|elektrik|fotovolt|diellor|\berës\b|gaz\w*|naft\w*|hidrokarbur|termocentral'),
       ('transport', r'rrug\w*|\bport\w*|aeroport|autostrad|hekurudh|tunel|unaz\w*|marina'), ('health', r'shëndet\w*|spital\w*|laborator\w*|dializ|kirurgji|check-?up|mjekësor|sterilizim'),
       ('mining', r'miner\w*|minier\w*|bakër|krom\w*|gurore|vendburim')]
c11 = collections.defaultdict(collections.Counter)
c11ex = collections.defaultdict(list)
for key, a in list(vkm_folder.items()) + list(law_folder.items()):
    t = title_of(a).lower()
    if not re.search(r'koncesion\w*|\bppp\b|partneritet\w* publik', t):
        continue
    y = key[1]
    if not 2000 <= y <= 2026:
        continue
    k = pick(CON, t)
    c11[y][k] += 1
    c11ex[k].append(t[:100])
OUT['c11'] = [{'y': y, **c11[y]} for y in range(2000, 2027)]
print('c11', sum(sum(v.values()) for v in c11.values()), {k: len(v) for k, v in c11ex.items()})
print('   c11 other', c11ex['other'][:6])

# ------------------------------------------------------------------ III. ministers' instructions and orders
ISS = []
for a, c in first.items():
    p = a.split('/')
    if p[0] not in ('udhezim', 'urdher'):
        continue
    m = re.search(r'\(([^()]*)\)\s*(\[QBZ \d+\])?\s*$', c['author'])
    ISS.append((a, p[0], m.group(1).strip() if m else '', int((c['Enacted'] or c['date'])[:4])))
MIN = [('agr', r'bujqësi'), ('edu', r'arsim'), ('inf', r'infrastruktur'), ('fin', r'financ'), ('int', r'brendshme'), ('jus', r'drejtësi'),
       ('hea', r'shëndetësi'), ('env', r'turizm|mjedis'), ('eco', r'ekonomi'), ('for', r'evropën|punët e jashtme'), ('def', r'mbrojtjes'),
       ('cm', r'këshilli i ministrave|kryeministri')]
c12 = collections.defaultdict(collections.Counter)
for a, kind, iss, y in ISS:
    k = pick(MIN, iss.lower())
    c12[k][kind] += 1
OUT['c12'] = {'rows': [{'k': k, **c12[k]} for k in [m[0] for m in MIN] + ['other']], 'n': len(ISS),
              'issuers': collections.Counter(iss for a, kind, iss, y in ISS).most_common(60)}
print('c12', {k: dict(v) for k, v in c12.items()})

# c13: the agriculture ministry's orders against animal diseases ("Disa masa mbrojtëse ndaj sëmundjes së ..., të shfaqur në shtetin e ...")
DIS = [('hpai', r'in\w*u?en\w*s?ës? aviare|influenzës aviare|gripit aviar'), ('bt', r'gjuh\w* blu'), ('asf', r'murtaj\w* afrikane'), ('nd', r'pseudopest'),
       ('pox', r'li[sj]\w* së dhenve|li[sj]\w* e dhenve|variola'), ('fmd', r'aft\w* epizootike'), ('ppr', r'ruminant\w* të vegjël|ruminatëve'),
       ('lsd', r'dermatoz\w* nodulare|lumpy'), ('bse', r'encefalopati')]
CTRY_VET = [('PL', 'poloni'), ('GR', 'greqi'), ('IT', 'itali'), ('ES', 'spanj'), ('HU', 'hungari'), ('UA', 'ukrain'), ('BG', 'bullgari'), ('DE', 'gjermani'),
            ('RO', 'rumani'), ('GB', 'mbretëri\\w* e bashkuar|mbretërinë e bashkuar|britani'), ('HR', 'kroaci'), ('TR', 'turqi'), ('FR', 'franc'), ('LV', 'letoni'),
            ('MD', 'moldavi'), ('AT', 'austri'), ('LT', 'lituani'), ('MK', 'maqedoni'), ('EE', 'estoni'), ('RS', 'serbi'), ('CZ', 'çeki|çeke'),
            ('BA', 'bosnj|hercegovin'), ('SK', 'sllovaki'), ('SI', 'slloveni'), ('XK', 'kosov'), ('NL', 'holand|vendeve të ulëta|niderland'),
            ('BE', 'belgjik'), ('PT', 'portugali'), ('DK', 'danimark'), ('SE', 'suedi'), ('IE', 'irland'), ('ME', 'malit të zi|mali i zi'),
            ('CY', 'qipro'), ('RU', 'rusi'), ('BY', 'bjellorusi'), ('GE', 'gjeorgji'), ('FI', 'finland'), ('CH', 'zvicr'), ('US', 'shteteve të bashkuara|amerik'),
            ('IL', 'izrael'), ('EG', 'egjipt'), ('IR', 'iran'), ('CN', 'kin[ëe]'), ('JP', 'japoni'), ('KR', 'kore'), ('MN', 'mongoli'), ('ZA', 'afrikës së jugut'),
            ('LU', 'luksemburg'), ('SA', 'saudite'), ('AZ', 'azerbajxhan'), ('KZ', 'kazakistan'), ('TN', 'tunizi'), ('MA', 'marok'), ('DZ', 'algjeri'), ('LY', 'libi'),
            ('IQ', 'irak'), ('NO', 'norvegji'), ('IN', 'indi')]
vet = []
for a, kind, iss, y in ISS:
    t = title_of(a)
    tl = t.lower()
    if not re.search(r'sëmundj', tl) or not re.search(r'masa\w* (mbrojtëse|kufizuese|paraprake|emergjente)', tl):
        continue
    if not re.search(r'shfaqur|evidentuar|konstatuar|\bnë shtetin\b|\bnë republikën\b|\bnë mbretërinë\b', tl):
        continue  # orders that name a country where the disease appeared
    dk = pick(DIS, tl)
    where = re.split(r'shfaqur|evidentuar|konstatuar', tl)[-1]
    cs = [k for k, rx in CTRY_VET if re.search(r'(?<!\w)(?:' + rx + ')', where)]
    c = first[a]
    start = c['In-force'] or c['Enacted']
    end = removed.get(a, (None,))[0]
    vet.append({'a': a, 'd': start[:10], 'dis': dk, 'c': cs, 'end': end[:10] if end and a in gone else None})
OUT['c13'] = {'orders': [[v['d'], v['dis'], ','.join(v['c']), v['end']] for v in sorted(vet, key=lambda v: v['d'])]}
life = [(D(v['end']) - D(v['d'])).days for v in vet if v['end']]
print('c13', len(vet), collections.Counter(v['dis'] for v in vet), 'repealed', len(life), 'median', MED(life),
      collections.Counter(c for v in vet for c in v['c']).most_common(12), 'no country', sum(1 for v in vet if not v['c']))

# c14: the minimum wage and pension indexation, as the Council of Ministers set them
NUMS = collections.defaultdict(dict)
with open(os.path.join(B, 'numbers.jsonl'), encoding='utf-8') as fh:
    for line in fh:
        r = json.loads(line)
        a, nm = r['p'].rsplit('/', 1)
        NUMS[a][nm] = r['t']
wage, pens, wage_known = [], [], []
for a, files in NUMS.items():
    if 'hyrje.md' in files:
        hy = clean(files['hyrje.md'])
        body = '\n'.join(t for nm, t in sorted(files.items()) if nm not in ('hyrje.md', 'zz-nenshkrimi.md', 'zz-shtojca.md'))
    else:  # a single-file act: the preamble ends at "VENDOSI:"
        hy, _, body = files.get('tekst.md', '').partition('VENDOSI')
        hy = clean(hy)
    c = first.get(a)
    if not c:
        continue
    t = re.split(r'(?i)n[ëe] mb[ëe]shtetje', hy)[0].lower()  # the title only, not the legal basis
    eff = re.search(r'efektet financiare (?:nga|duke filluar nga|prej)\s*(?:data|datës)?\s*(\d{1,2}\s*\.\s*\d{1,2}\s*\.\s*\d{4}|1\s+\w+\s+\d{4})', body)
    start = c['In-force'] or c['Enacted']
    MONTHS = ['janar', 'shkurt', 'mars', 'prill', 'maj', 'qershor', 'korrik', 'gusht', 'shtator', 'tetor', 'nëntor', 'dhjetor']
    if eff:
        e = eff.group(1)
        dt = dd(e)
        if not dt:
            m2 = re.match(r'(\d{1,2})\s+(\w+)\s+(\d{4})', e)
            if m2 and m2.group(2).lower() in MONTHS:
                dt = date(int(m2.group(3)), MONTHS.index(m2.group(2).lower()) + 1, int(m2.group(1)))
        if dt:
            start = dt.isoformat()
    n_, y_ = int(a.split('/')[2]), int(a.split('/')[1])
    if re.search(r'pag[ëe][ns] (?:bazë )?minimale\w* në shkallë vendi|pagës minimale, në shkallë vendi', t) and 'kontribut' not in t and 'mësimit' not in t:
        m = re.search(r'minimale[^\n]{0,260}?(?:të jetë|bëhet|është)\s+(\d{1,3}(?:[  .]\d{3})+|\d{4,6})', body, re.I | re.S)
        if m:
            wage.append({'a': f'{n_}/{y_}', 'd': start[:10], 'v': int(re.sub(r'\D', '', m.group(1))), 'pub': c['Published'], 'en': c['Enacted']})
    elif re.search(r'(rritjen|indeksimin) e pensioneve(?! suplementare)', t) and 'suplementare' not in t and not AMEND.search(re.sub(r'^\W*(v\s*e\s*n\s*d\s*i\s*m|vendim)\s+nr\.?\s*[\d\s]+,?\s*datë\s*[\d.\s]+', '', t, flags=re.I).strip()):
        if re.search(r'deri në [\d  ]+ lekë rriten', body):
            continue  # rates set by pension bracket (2000): no single rate
        m = re.search(r'(?:në masën|rriten|rritet|indeksohen|indeksimin)\s+(?:me\s+)?(\d{1,2}(?:[.,]\d{1,2})?)\s*(?:për ?qind|%)', body)
        if m:
            pens.append({'a': f'{n_}/{y_}', 'd': start[:10], 'v': float(m.group(1).replace(',', '.')), 'en': c['Enacted']})
# decisions on the minimum wage the record names but whose text the repository does not hold
for r in LAWCSV:
    m = re.match(r'Vendimi i Këshillit të Ministrave nr\. (\d+), datë ([\d.]+)', r['label'])
    if m and re.search(r'pag\w* (?:bazë )?minimale\w*(?: mujore)?,? në shkallë vendi|pag[ëe]n minimale', r['title'], re.I) and 'kontribut' not in r['title'].lower() and 'mësimit' not in r['title'].lower():
        wage_known.append([f'{m.group(1)}/{dd(m.group(2)).year}', dd(m.group(2)).isoformat()])
for h in HELD:
    if h['kind'] == 'vendim' and re.search(r'pag[ëe]s minimale', h['title'], re.I):
        wage_known.append([f"{h['number']}/{h['date'][:4]}", h['date']])
have = {w['a'] for w in wage}
wage_missing = sorted({tuple(x) for x in wage_known if x[0] not in have}, key=lambda x: x[1])
OUT['c14'] = {'wage': sorted(wage, key=lambda w: w['d']), 'missing': wage_missing, 'pens': sorted(pens, key=lambda p: p['d'])}
print('c14 wage', [(w['a'], w['d'], w['v']) for w in OUT['c14']['wage']])
print('c14 missing', wage_missing)
print('c14 pens', [(p['a'], p['d'], p['v']) for p in OUT['c14']['pens']])

# ------------------------------------------------------------------ IV. how acts change and end
GROUPK = {'ligj': 'law', 'kushtetuta': 'law', 'aktnormativ': 'law', 'vendim': 'vkm', 'udhezim': 'min', 'urdher': 'min'}
vetset = {v['a'] for v in vet}
ch = collections.defaultdict(collections.Counter)
for a, days in events.items():
    p = a.split('/')
    if p[0] == 'vendim' and not p[1].isdigit():
        continue  # decisions of other bodies
    g = GROUPK.get(p[0])
    if not g:
        continue
    for d in days:
        y = int(d[:4])
        if 2000 <= y <= 2026:
            ch[y][g] += 1
rp = collections.defaultdict(collections.Counter)
for a, (d, an, c) in removed.items():
    p = a.split('/')
    if a not in gone or an == 'Lexifina' or (p[0] == 'vendim' and not p[1].isdigit()):
        continue
    g = GROUPK.get(p[0])
    if not g:
        continue
    y = int(d[:4])
    if 2000 <= y <= 2026:
        rp[y]['vet' if a in vetset else g] += 1
OUT['c15'] = {'ch': [{'y': y, **ch[y]} for y in range(2000, 2027)], 'rp': [{'y': y, **rp[y]} for y in range(2000, 2027)]}
print('c15 ch', [(y, dict(ch[y])) for y in (2008, 2020, 2025)], 'rp', [(y, dict(rp[y])) for y in (2008, 2020, 2024, 2025, 2026)])

# c16: the acts changed most often (days on which a new version took effect)
cand = [(len(d), a) for a, d in events.items() if a.split('/')[0] in ('ligj', 'vendim', 'udhezim', 'urdher', 'aktnormativ', 'kushtetuta')
        and not (a.startswith('vendim/') and not a.split('/')[1].isdigit())]
cand.sort(key=lambda x: (-x[0], x[1]))
c16 = []
for n, a in cand[:20]:
    by = collections.Counter(int(d[:4]) for d in events[a])
    c16.append({'a': a, 't': title_of(a)[:200], 'n': n, 'by': {str(y): v for y, v in by.items()}, 'from': (first[a]['In-force'] or first[a]['date'])[:10],
                'live': a in live, 'authors': collections.Counter(re.sub(r',? datë.*$', '', x) for d in events[a] for x in events[a][d]).most_common(3)})
OUT['c16'] = c16
print('c16', [(r['a'], r['n'], r['t'][:50]) for r in c16])

# ------------------------------------------------------------------ V. the Constitution, the courts and international agreements
# c17: the Constitution: provisions each amending law added, changed or removed, by part
PARTS = [('p01', 1, 14), ('p02', 15, 63), ('p03', 64, 85), ('p04', 86, 94), ('p05', 95, 107), ('p06', 108, 115), ('p07', 116, 123), ('p08', 124, 134),
         ('p09', 135, 147), ('p10', 148, 149), ('p11', 150, 152), ('p12', 153, 154), ('p13', 155, 161), ('p14', 162, 165), ('p15', 166, 169),
         ('p16', 170, 176), ('p17', 177, 177), ('p18', 178, 183)]


def part_of(nm):
    if nm.startswith('aneks'):
        return 'annex'
    if nm.startswith('kalimtare'):
        return 'p18'
    m = re.match(r'pjesa-(\d+)', nm)
    if m:
        return 'p%02d' % int(m.group(1))
    m = re.match(r'neni-(\d+)', nm)
    if m:
        n = int(m.group(1))
        return next(k for k, lo, hi in PARTS if lo <= n <= hi)
    return None


c17 = []
for c in reversed(C):
    if c['Kind'] != 'law':
        continue
    fs = [(st, f.rsplit('/', 1)[1]) for st, f in c['f'] if act_id(f) == 'kushtetuta/1998' and PROV(f)]
    if not fs or c['author'] == 'Ligji nr. 8417':
        continue
    cells = collections.defaultdict(collections.Counter)
    for st, nm in fs:
        if nm.startswith('pjesa'):
            continue  # a heading, not a provision
        cells[part_of(nm.replace('.md', ''))][st] += 1
    c17.append({'law': c['author'], 'd': c['In-force'], 'cells': {k: dict(v) for k, v in cells.items()}, 'n': sum(sum(v.values()) for v in cells.values()),
                'files': sorted(nm.replace('.md', '') for st, nm in fs)})
OUT['c17'] = c17
print('c17', [(r['law'], r['d'], r['n']) for r in c17])

# c18: court decisions published in the Official Journal (records in caselaw/)
COURT = {'gjykata-kushtetuese': 'cc', 'gjykata-e-larte': 'hc', 'gjykata-europiane-e-te-drejtave-te-njeriut': 'echr', 'gjykata-evropiane-e-te-drejtave-te-njeriut': 'echr',
         'gjykata-te-rretheve-gjyqesore': 'dc'}
c18 = collections.defaultdict(collections.Counter)
c18d = collections.defaultdict(list)
for a, c in first.items():
    p = a.split('/')
    if p[0] != 'caselaw' or len(p) < 3:
        continue
    k = COURT.get(p[1])
    if not k or not c['Enacted']:
        continue
    y = D(c['Enacted']).year
    c18[y][k] += 1
    if k == 'cc' and c['Published']:
        dd_ = (D(c['Published']) - D(c['Enacted'])).days
        if 0 <= dd_ <= 3650:
            c18d[y].append(dd_)
y0 = min(c18)
OUT['c18'] = {'years': [{'y': y, **c18[y]} for y in range(y0, 2027)], 'days': {str(y): [len(v), MED(v)] for y, v in c18d.items()},
              'cc_changes': sorted({c['author'] for c in C if c['Kind'] == 'court'} | {r['label'] for r in LAWCSV if r['label'].startswith('Vendimi i Gjykatës Kushtetuese')})}
print('c18', [(y, dict(c18[y])) for y in sorted(c18)][:3], len(OUT['c18']['cc_changes']))

# c19, c20: laws ratifying or acceding to international agreements: the other party, the subject and the lender
CTRY = [('IT', r'itali'), ('GR', r'greqi|helen'), ('TR', r'turqi'), ('XK', r'kosov'), ('MK', r'maqedoni'), ('ME', r'malit të zi|mali i zi|mal të zi'), ('RS', r'serbi'),
        ('HR', r'kroaci'), ('BA', r'bosnj|hercegovin'), ('BG', r'bullgari'), ('RO', r'rumani'), ('HU', r'hungari'), ('AT', r'austri'), ('DE', r'gjermani|gjerman\w*|kreditanstalt|\bkfw\b'),
        ('FR', r'franc[ëe]s\b|francë\b|franceze'), ('ES', r'spanj'), ('PT', r'portugali'), ('BE', r'belgjik'), ('NL', r'holand|vendeve të ulëta|niderland'), ('LU', r'luksemburg'),
        ('CH', r'zvicr|zviceran'), ('GB', r'mbretëri\w* (?:e|së) bashkuar|britani|\banglis'), ('IE', r'irland'), ('DK', r'danimark'), ('SE', r'suedi'), ('NO', r'norvegji'),
        ('FI', r'finland'), ('IS', r'island[ëe]s|islandë\b'), ('PL', r'poloni'), ('CZ', r'çeki\b|çekisë|republikës çeke|çeke\b'), ('SK', r'sllovaki'), ('SI', r'slloveni'), ('EE', r'estoni'),
        ('LV', r'letoni'), ('LT', r'lituani'), ('RU', r'\brusi|federatës ruse|ruse\b'), ('UA', r'ukrain'), ('BY', r'bjellorus'), ('MD', r'moldavi'), ('GE', r'gjeorgji'), ('AM', r'armeni'),
        ('AZ', r'azerbajxhan'), ('KZ', r'kazakistan'), ('UZ', r'uzbekistan'), ('CN', r'kin[ëe]s\b|kinë\b|kineze'), ('JP', r'japoni'), ('KR', r'kore'), ('IN', r'\bindi(së|ë)\b|\bindisë\b'),
        ('ID', r'indonezi'), ('MY', r'malajzi'), ('SG', r'singapor'), ('TH', r'tajland'), ('VN', r'vietnam'), ('US', r'shteteve të bashkuara|shtetet e bashkuara|\bshba\b|amerikës'),
        ('CA', r'kanad'), ('MX', r'meksik'), ('BR', r'brazil'), ('AR', r'argjentin'), ('CL', r'\bkili\b|\bkilit\b'), ('AU', r'australi'), ('IL', r'izrael'), ('EG', r'egjipt'),
        ('MA', r'marok'), ('TN', r'tunizi'), ('DZ', r'algjeri'), ('LY', r'\blibi(së|a)\b'), ('QA', r'katar'), ('KW', r'kuvajt'), ('AE', r'emirate'), ('SA', r'arabi\w* saudite|saudit\w*'),
        ('JO', r'jordani'), ('IR', r'\biran'), ('IQ', r'\birak'), ('PK', r'pakistan'), ('MT', r'\bmalt(?:a|ës|ën|ë)\b|maltez'), ('CY', r'qipro'), ('SM', r'san marino'), ('MC', r'monak'),
        ('LI', r'lihtenshtajn'), ('VA', r'selisë së shenjtë|selia e shenjtë|vatikan'), ('AD', r'andorr'), ('SY', r'\bsiri'), ('LB', r'liban'), ('OM', r'\boman'), ('TM', r'turkmenistan'),
        ('MN', r'mongoli'), ('CU', r'\bkub[ëe]s\b'), ('NZ', r'zelandës së re'), ('ZA', r'afrikës së jugut'), ('BH', r'bahrein'), ('KG', r'kirgiz')]
LEND = [('wb', r'bank\w* botërore|bankës ndërkombëtare për rindërtim|bankën ndërkombëtare për rindërtim|shoqat\w* ndërkombëtare (?:për|të) zhvillim|\bida\b|\bibrd\b'),
        ('eu', r'komunitet\w* (?:evropian|europian)|komision\w* (?:evropian|europian)|bashkim\w* (?:evropian|europian)|\bipa\b'),
        ('ebrd', r'bankës (?:evropiane|europiane) për rindërtim|\bberzh\b|\bebrd\b'), ('eib', r'bankës (?:evropiane|europiane) (?:të|e) investimeve|\bbei\b|\beib\b'),
        ('ceb', r'bankës së zhvillimit të këshillit të (?:evropës|europës)|bankës për zhvillim të këshillit|\bbzhke\b|\bceb\b'), ('kfw', r'kreditanstalt|\bkfw\b'),
        ('isdb', r'bankës islamike'), ('arab', r'\bopec\b|fondi\w* (?:saudit|kuvajtian|arab)|abu dhabi|fondit të kuvajtit|fondit saudit'), ('imf', r'fondi\w* monetar')]
SUBJ = [('loan', r'\bhua\w*|\bkredi\w*|financim\w*|\bgrant\w*|financiar\w*|garanci\w*|dhurim\w*|asistenc\w* (?:financiare|teknike)|\bfondi\w* monetar|borxh\w*|riskedulim\w*|'
                  r'ndihm\w* për objektiva zhvillimi|\bcards\b|mandatim\w*|obligacion\w*|eurobond'),
        ('eu', r'stabiliz\w*|asociim\w*|komunitet\w* (?:europian|evropian)|bashkim\w* (?:europian|evropian)|komision\w* (?:europian|evropian)'),
        ('tax', r'tatim\w*|taksim\w*|dyfisht'), ('invest', r'investim\w*|koncesion\w*|hipotekim\w*'),
        ('justice', r'ekstradim|ndihm\w* (?:juridike|gjyqësore)|drejtësi\w*|provave|detyrimet ushqimore|hagës|ligjore|transferim\w* (?:e|të) (?:personave|të dënuar)|gjykat\w*|gjykim\w*|arbitrazh|vendimeve gjyqësore'),
        ('security', r'polic\w*|krim\w*|terror\w*|drog\w*|psikotrop|narkotik|trafik\w*|ripranim\w*|viz(?:a|ave|ës|at|ash)\b|kufi(?:j|t|ri|tar)\w*|informacion\w* (?:e|të) klasifikuar|korrupsion|pastrim\w* të parave|emigrac|migrac|falsifikim\w*|monedh\w*'),
        ('defence', r'ushtar\w*|(?:fush\w*|çështje\w*|sektor\w*|industri\w*) (?:e|të) mbrojtjes|partneritet\w* për paqe|ministri\w* (?:e|të|i) mbrojtjes|mbrojtj\w* (?:e|së) përbashkët|nato\b|forc\w* (?:të|e) armatosura|paqeruajt|fuqive aleate|shape\b|arm[ëe]\w*|armatim\w*|municion\w*|bërthamor\w*|eksploziv|minave'),
        ('transport', r'transport\w*|ajror\w*|detar\w*|rrugor\w*|hekurudh\w*|lundrim\w*|aviacion|anije\w*|eurocontrol|portual\w*|automjet\w*|mjeteve me|kërkim-shpëtim\w*|telekomunikacion\w*'),
        ('trade', r'tregti\w*|doganor\w*|dogan\w*|cefta|tarif\w*|eksport|patent\w*|origjin\w*|pronës\w* (?:industriale|intelektuale)|markave|tregues\w* gjeografik|ekonomik\w*|disenjo\w*|obpi|fonogram\w*'),
        ('social', r'sigurim\w* shoqëror\w*|mbrojtj\w* shoqëror\w*|pun[ëe]s\b|punësim|pension\w*|shëndet\w*|sociale|punëtor\w*|farmakope\w*'),
        ('culture', r'kultur\w*|arsim\w*|shkenc\w*|rini\w*|sport\w*|turiz\w*|universitet|kinematograf\w*|trashëgimi\w*|muze\w*|arkiv\w*|gjuhëve|kolegj\w*|rinor\w*|antidoping'),
        ('env', r'mjedis\w*|energji\w*|klim\w*|ndotj\w*|ozon|bimë|kafsh|natyr|ujër\w*|detit|pyje|peshkim\w*|mesdhe|gazsjell\w*|hidrocentral\w*|lënd\w* drusore|ndotës\w*|fatkeqësi\w*'),
        ('rights', r'të drejt\w* (?:e|të) njeriut|diskriminim|fëmij\w*|gra\b|grave|tortur|refugjat|pakic|personave me aftësi|shtetësi\w*')]


def partners(t):
    tl = t.lower()
    tl = re.sub(r'republik\w* (?:e|së|të) shqipërisë|shqipëri\w*|shqiptar\w*|këshillit të ministrave', ' ', tl)
    cs = [k for k, rx in CTRY if re.search(r'(?:^|[^a-zçë])(?:' + rx + ')', tl)]
    ls = [k for k, rx in LEND if re.search(r'(?<!\w)(?:' + rx + ')', tl)]
    return cs, ls


rat = []
for (n, y), d in LAW.items():
    t = d['t']
    if not t or not (2000 <= y <= 2026):
        continue
    if not re.search(r'\b(ratifikim|aderim)\w*', t, re.I):
        continue
    cs, ls = partners(t)
    if len(set(cs)) > 3:
        cs = []  # a title naming many states is a multilateral agreement
    tl = t.lower()
    sj = pick(SUBJ, tl)
    rat.append({'n': n, 'y': y, 'c': sorted(set(cs)), 'l': sorted(set(ls)), 's': sj})
dec = lambda y: '00' if y < 2010 else '10' if y < 2020 else '20'
pc = collections.defaultdict(collections.Counter)
for r in rat:
    for k in r['c']:
        pc[k][dec(r['y'])] += 1
OUT['c19'] = {'rows': sorted([{'k': k, 'n': sum(v.values()), 'by': dict(v)} for k, v in pc.items()], key=lambda r: -r['n']), 'n': len(rat),
              'bilateral': sum(1 for r in rat if r['c']), 'multi': sum(1 for r in rat if not r['c'] and not r['l']),
              'de_kfw': sum(1 for r in rat if 'DE' in r['c'] and 'kfw' in r['l'])}
sc = collections.defaultdict(collections.Counter)
lc = collections.defaultdict(collections.Counter)
for r in rat:
    sc[r['s']][dec(r['y'])] += 1
    if r['s'] == 'loan':
        for k in (r['l'] or (['state'] if r['c'] else ['other'])):
            lc[k][dec(r['y'])] += 1
OUT['c20'] = {'subj': [{'k': k, **sc[k]} for k in [s[0] for s in SUBJ] + ['other']], 'lend': [{'k': k, **lc[k]} for k in [l[0] for l in LEND] + ['state', 'other']], 'n': len(rat)}
print('c19', OUT['c19']['n'], OUT['c19']['bilateral'], [(r['k'], r['n']) for r in OUT['c19']['rows'][:20]])
print('c20', {k: dict(v) for k, v in sc.items()}, {k: sum(v.values()) for k, v in lc.items()})

# ------------------------------------------------------------------ profile
cnt = collections.Counter()
for a in first:
    p = a.split('/')
    if p[0] == 'vendim' and not p[1].isdigit():
        cnt['vendim_other'] += 1
    else:
        cnt[p[0]] += 1
PROFILE.update({
    'commits': len(C), 'head': os.environ.get('HEAD_SHA', ''), 'built': date.today().isoformat(),
    'acts': cnt, 'laws': len(law_folder), 'laws_live': sum(1 for a in law_folder.values() if a in live), 'laws_known': len(LAW),
    'vkm': len(vkm_folder), 'vkm_live': sum(1 for a in vkm_folder.values() if a in live), 'minis': len(ISS),
    'na': len(c06), 'versions_after_first': sum(len(v) for v in events.values()), 'held': len(HELD),
    'cc': sum(r.get('cc', 0) for r in OUT['c18']['years']), 'local': cnt['local'],
    'last_in_force': max((c['In-force'] for c in C if c['In-force'] and c['In-force'] <= date.today().isoformat()), default=''),
})
json.dump({'charts': OUT, 'profile': PROFILE}, open(os.path.join(B, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'), default=list)
print('profile', PROFILE)
