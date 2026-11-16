"""Rebuild visualisations/e-drejta-shqiptare-ne-20-grafike.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF] [--skip-extract]

Steps (all read-only on the repository; scratch output goes to visualisations/src/.build/):
  1. git log of REF, streamed: one line per commit with its author, dates, subject and the trailers the charts use
                                                    -> .build/log.tsv
  2. git log --name-status of REF, streamed: one line per file a commit adds, changes or deletes
                                                    -> .build/names.tsv
  3. the blobs the charts read, listed from the tree of REF: the tables data/laws.csv, registry/data/laws.csv and
     data/held.json; the preamble (hyrje.md), the approval or signature block (zz-miratuar.md, zz-nenshkrimi.md) of
     every law, normative act, decision, instruction and order; the README of each act whose provisions were removed
     (it keeps the act's title)                     -> .build/repo/ and .build/heads.jsonl
  4. the texts of the Council of Ministers' decisions on the minimum wage and on pensions, each as its last version
     (most were later repealed, so they are read from the commit before the repeal)   -> .build/numbers.jsonl
  5. prep.py turns those into .build/data.json; build.py fills page.tpl.html with it.
In a partial (blobless) clone the missing blobs are fetched in one batch per step; nothing is held in memory at once:
the history and the texts are streamed line by line.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--out', default=os.path.join(HERE, '..', 'e-drejta-shqiptare-ne-20-grafike.html'))
ap.add_argument('--skip-extract', action='store_true', help='reuse .build/ from a previous run (prep and build only)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
os.makedirs(B, exist_ok=True)
NOLAZY = dict(os.environ, GIT_NO_LAZY_FETCH='1')


def git(*args, **kw):
    return subprocess.run(['git', '-C', a.repo, *args], check=True, capture_output=True, **kw).stdout


ref = a.ref
if not ref:
    ref = 'origin/main' if subprocess.run(['git', '-C', a.repo, 'rev-parse', '--verify', '-q', 'origin/main'], capture_output=True).returncode == 0 else 'HEAD'
sha = git('rev-parse', ref).decode().strip()
print('ref', ref, sha)


def fetch_missing(oids):
    """one batched fetch for the blobs a partial clone does not have yet"""
    oids = sorted(set(oids))
    chk = subprocess.run(['git', '-C', a.repo, 'cat-file', '--batch-check'], input=''.join(o + '\n' for o in oids).encode(),
                         capture_output=True, env=NOLAZY).stdout.decode().split('\n')
    missing = [l.split()[0] for l in chk if l.endswith(' missing')]
    if missing:
        print('fetching', len(missing), 'blobs')
        subprocess.run(['git', '-C', a.repo, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                        '--recurse-submodules=no', '--filter=blob:none', '--stdin'], input=''.join(m + '\n' for m in missing).encode(), check=False)


def read_blobs(items):
    """yield (path, bytes) for (oid, path) pairs, one blob at a time"""
    p = subprocess.Popen(['git', '-C', a.repo, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=NOLAZY)
    for oid, path in items:
        p.stdin.write((oid + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        if len(head) < 3:
            sys.exit('cannot read ' + path)
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        yield path, data
    p.stdin.close(); p.wait()


def ls_tree(treeish, *paths):
    out = []
    for e in git('ls-tree', '-r', '-z', treeish, '--', *paths).split(b'\0'):
        if not e:
            continue
        meta, path = e.split(b'\t', 1)
        _, typ, oid = meta.split()
        if typ == b'blob':
            out.append((oid.decode(), path.decode('utf-8')))
    return out


TRAILERS = ['Kind', 'In-force', 'Enacted', 'Published', 'Act', 'Act-path', 'Law']
if not a.skip_extract:
    # 1. the history, streamed
    fmt = '%x1e%H%x1f%an%x1f%ad%x1f%s%x1f%(trailers:unfold,separator=%x1d)'
    lg = subprocess.Popen(['git', '-C', a.repo, 'log', ref, '--date=short', '--format=' + fmt], stdout=subprocess.PIPE)
    n, buf = 0, b''
    with open(os.path.join(B, 'log.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        out.write('\t'.join(['sha', 'author', 'date', 'subject'] + TRAILERS) + '\n')

        def emit(rec):
            global n
            rec = rec.decode('utf-8', 'replace').strip('\n')
            if not rec:
                return
            parts = rec.split('\x1f')
            tr = {}
            for t in (parts[4] if len(parts) > 4 else '').split('\x1d'):
                k, _, v = t.partition(': ')
                k = k.strip()
                if k and k not in tr:
                    tr[k] = v.strip()
            row = parts[:4] + [tr.get(k, '') for k in TRAILERS]
            out.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for x in row) + '\n')
            n += 1
        for chunk in iter(lambda: lg.stdout.read(1 << 16), b''):
            buf += chunk
            *recs, buf = buf.split(b'\x1e')
            for r in recs:
                emit(r)
        emit(buf)
    lg.wait()
    print('commits', n)

    # 2. the files of each commit, streamed
    lg = subprocess.Popen(['git', '-C', a.repo, 'log', ref, '--format=@@C %H', '--name-status', '--no-renames'], stdout=subprocess.PIPE)
    nf = 0
    with open(os.path.join(B, 'names.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        cur = None
        for raw in lg.stdout:
            l = raw.decode('utf-8', 'replace').rstrip('\n')
            if l.startswith('@@C '):
                cur = l[4:]
                continue
            if l and cur:
                st, _, f = l.partition('\t')
                out.write(f'{cur}\t{st[:1]}\t{f}\n')
                nf += 1
    lg.wait()
    print('file changes', nf)

    # 3. tables and the head files of every act at REF
    TABLES = {'data/laws.csv', 'registry/data/laws.csv', 'data/held.json'}
    items = [(o, p) for o, p in ls_tree(ref, 'data', 'registry/data') if p in TABLES]
    acts = ls_tree(ref, 'ligj', 'aktnormativ', 'vendim', 'udhezim', 'urdher')
    folders = {}
    for o, p in acts:
        folders.setdefault(p.rsplit('/', 1)[0], []).append((o, p))
    heads = []
    for f, fs in folders.items():
        names = {p.rsplit('/', 1)[1] for _, p in fs}
        for o, p in fs:
            nm = p.rsplit('/', 1)[1]
            if nm in ('hyrje.md', 'zz-miratuar.md', 'zz-nenshkrimi.md') or (nm == 'README.md' and names <= {'README.md', 'record.json'}):
                heads.append((o, p))
    print('tables', len(items), 'head files', len(heads))
    fetch_missing([o for o, _ in items + heads])
    R = os.path.join(B, 'repo')
    for path, data in read_blobs(items):
        dst = os.path.join(R, *path.split('/'))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as fh:
            fh.write(data)
    with open(os.path.join(B, 'heads.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
        for path, data in read_blobs(heads):
            t = data.decode('utf-8', 'replace')
            if path.endswith('README.md'):
                t = t.split('\n', 1)[0]  # the title line is all the charts need
            out.write(json.dumps({'p': path, 't': t}, ensure_ascii=False) + '\n')

    # 4. the minimum wage and pension decisions, each at its last version
    NUM = re.compile(r'pag[ëe]s minimale|pag[ëe]n minimale|indeksimin e pensioneve|rritjen e pensioneve$|rritjen e pensioneve\b(?! suplementare)', re.I)
    want = {}
    with open(os.path.join(B, 'log.tsv'), encoding='utf-8') as fh:
        head = fh.readline().rstrip('\n').split('\t')
        for line in fh:
            r = dict(zip(head, line.rstrip('\n').split('\t')))
            title = r['Act'] or r['subject']
            if r['author'].startswith('Vendimi i Këshillit të Ministrave') and NUM.search(title) and r['Kind'] in ('decree', 'as-enacted'):
                m = re.search(r'nr\. (\d+), datë \d+\.\d+\.(\d{4})', r['author'])
                if m:
                    want[f'vendim/{m.group(2)}/{m.group(1)}'] = None
    last = {}
    with open(os.path.join(B, 'names.tsv'), encoding='utf-8') as fh:  # newest first
        for line in fh:
            h, st, f = line.rstrip('\n').split('\t')
            fo = f.rsplit('/', 1)[0]
            if fo in want and fo not in last and st in ('A', 'M') and not f.endswith(('README.md', 'record.json')):
                last[fo] = h
    nums = []
    for fo, h in last.items():
        nums += [(o, p) for o, p in ls_tree(h, fo) if not p.endswith(('README.md', 'record.json'))]
    print('number decisions', len(last), 'files', len(nums))
    fetch_missing([o for o, _ in nums])
    with open(os.path.join(B, 'numbers.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
        for path, data in read_blobs(nums):
            out.write(json.dumps({'p': path, 't': data.decode('utf-8', 'replace')}, ensure_ascii=False) + '\n')

# 5. prep + build
env = dict(os.environ, HEAD_SHA=sha)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py'), B], check=True, env=env)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py'), os.path.join(B, 'data.json'), os.path.abspath(a.out)], check=True)
