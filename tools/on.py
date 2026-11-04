"""Prints the law as it stood on a day, read from this repository's history.

    python tools/on.py 2015-06-01                         # every act's commit in force that day
    python tools/on.py 2015-06-01 kushtetuta              # the whole act on that day (by its id)
    python tools/on.py 2015-06-01 kushtetuta/1998         # the same act, by its folder
    python tools/on.py 2015-06-01 kushtetuta neni-064     # one provision (a file name without .md)
    python tools/on.py 2015-06-01 kushtetuta 64           # the same, by article number
    python tools/on.py --law 2015-06-01 kushtetuta neni-064  # also name the law behind the version shown

Each commit carries the day its change took effect in an `In-force:` trailer. That trailer, not the commit date, is
the source of truth: git cannot store dates before 1970, and reading the trailer avoids time-zone edge cases. The text
in force on a day is the last commit on or before it that touches the act. Laws published but not yet in force live on
the future branch, which is read for days after the newest commit on main. Merge commits are ignored.

Acts live in folders named by their official identifier (<kind>/<year>/<number>/: ligj/2000/8569/, kushtetuta/1998/),
listed in registry/data/paths.json (every act) and data/paths.json (the earlier build's acts). Before the layout move
each act's folder was named by its id (ligji-8569-2000/, kushtetuta/); this tool reads both, so any day gives the
right text. An id whose copy was removed as a duplicate (data/paths.json, "replaced") reads as the copy kept.
Standard library only.
"""
import datetime as dt
import json
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def branches() -> tuple[str, str | None]:
    """main, and the future branch named in data/repo.json (local or origin/), if it exists."""
    try:
        name = json.loads(git('show', 'main:data/repo.json')).get('future_branch')
    except (subprocess.CalledProcessError, ValueError):
        name = None
    if not name:
        return 'main', None
    for ref in (name, f'origin/{name}'):
        if subprocess.run(['git', 'rev-parse', '-q', '--verify', ref], capture_output=True).returncode == 0:
            return 'main', ref
    return 'main', None


_INDEX = None


def index() -> tuple[dict[str, str], dict[str, dict]]:
    """({act id: folder}, {removed id: {"by": kept id, "path": folder}}) from the paths files on main ({} before the
    layout move)."""
    global _INDEX
    if _INDEX is None:
        paths, replaced = {}, {}
        for f in ('registry/data/paths.json', 'data/paths.json'):
            try:
                d = json.loads(git('show', f'main:{f}'))
            except (subprocess.CalledProcessError, ValueError):
                continue
            paths.update({k: v for k, v in d.get('paths', {}).items() if k not in paths})
            replaced.update(d.get('replaced', {}))
        _INDEX = (paths, replaced)
    return _INDEX


def paths() -> dict[str, str]:
    return index()[0]


def kept(act: str) -> str:
    """The id to read: an id removed as a duplicate reads as the copy kept (said once on stderr)."""
    act = act.strip('/')
    rep = index()[1].get(act)
    if rep:
        print(f'({act} was published twice; the copy kept is {rep["by"]}, in {rep["path"]}/)', file=sys.stderr)
        return rep['by']
    return act


def folders(act: str) -> list[str]:
    """Every folder an act has had: its folder now, then its id (its folder before the layout move)."""
    act = act.strip('/')
    p = paths()
    if act in p:
        return list(dict.fromkeys([p[act], act]))
    back = {v: k for k, v in p.items()}
    if act in back:
        return [act, back[act]]
    return [act]


def variants(path: str) -> list[str]:
    """A file path under every folder its act has had (kushtetuta/1998/neni-064.md and kushtetuta/neni-064.md)."""
    best = None
    for act, folder in paths().items():
        for root in (folder, act):
            if (path == root or path.startswith(root + '/')) and (best is None or len(root) > len(best[2])):
                best = (act, folder, root)
    if best is None:
        return [path]
    act, folder, root = best
    rest = path[len(root):]
    return list(dict.fromkeys([folder + rest, act + rest]))


def history(branch: str, *targets: str) -> list[tuple[str, str, str]]:
    """(commit, in-force day, author) for every commit touching any of the paths, newest first."""
    out = git('log', '--no-merges', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)%x09%an', branch,
              '--', *targets)
    rows = []
    for line in out.splitlines():
        h, d, a = (line.split('\t') + ['', ''])[:3]
        if d.strip():
            rows.append((h, d.strip(), a))
    return rows


def commit_on(day: str, target: str) -> tuple[str, str, str] | None:
    main, future = branches()
    targets = folders(target) if not target.endswith('.md') else variants(target)
    rows = history(main, *targets)
    if future and (not rows or day > rows[0][1]):
        rows = history(future, *targets) or rows
    for h, d, a in rows:
        if d <= day:
            return h, d, a
    return None


def folder_at(commit: str, act: str) -> str | None:
    """The folder the act had at that commit."""
    for f in folders(act):
        if git('ls-tree', '--name-only', commit, f'{f}/').strip():
            return f
    return None


def resolve(commit: str, act: str, unit: str) -> str | None:
    root = folder_at(commit, act)
    if root is None:
        return None
    files = git('ls-tree', '-r', '--name-only', commit, f'{root}/').split('\n')
    exact = f'{root}/{unit}.md'
    if exact in files:
        return exact
    m = re.fullmatch(r'(\d+)(.*)', unit)
    if m:
        want = re.compile(rf'{re.escape(root)}/[a-z-]*0*{int(m.group(1))}{re.escape(m.group(2))}\.md$')
        hits = [f for f in files if want.match(f)]
        # A bare number means the article: "19" is neni-019, not a transitional provision numbered 19.
        arts = [f for f in hits if f[len(root) + 1:].startswith(('neni-', 'art-', 'art'))]
        if len(arts) == 1:
            return arts[0]
        if len(hits) == 1:
            return hits[0]
        if hits:
            sys.exit(f'{unit} is ambiguous in {act}: {", ".join(h[len(root) + 1:-3] for h in hits)}. Give the file name.')
    return None


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    show_law = '--law' in args
    args = [a for a in args if a != '--law']
    if not args:
        sys.exit(__doc__)
    day = args[0]
    try:
        dt.date.fromisoformat(day)
    except ValueError:
        sys.exit(f'{day!r} is not a date (YYYY-MM-DD).')
    if len(args) == 1:
        acts = sorted(paths()) or sorted({p.split('/')[0] for p in git('ls-tree', '-r', '--name-only', 'main').split('\n')
                                         if '/' in p and p.split('/')[0] not in ('data', 'tools', 'registry')})
        for act in acts:
            hit = commit_on(day, act)
            print(f'{act}\t' + (f'{hit[1]}\t{hit[0][:10]}\t{hit[2]}' if hit else 'not in force yet'))
        return
    act = kept(args[1])
    hit = commit_on(day, act)
    if not hit:
        sys.exit(f'{act} is not in the record on {day}: it took effect later, or the name is wrong (see `python tools/on.py {day}`).')
    commit = hit[0]
    if len(args) > 2:
        path = resolve(commit, act, args[2])
        if not path:
            sys.exit(f'{act}/{args[2]} was not in the text on {day} (it may have been inserted later or removed earlier).')
        if show_law:
            last = commit_on(day, path)
            print(f'# in force from {last[1]}, last changed by {last[2]} ({last[0][:10]})\n')
        sys.stdout.write(git('show', f'{commit}:{path}'))
        return
    root = folder_at(commit, act)
    files = [f for f in git('ls-tree', '-r', '--name-only', commit, f'{root}/').split('\n')
             if f.endswith('.md') and not f.endswith('/README.md')]
    for f in sorted(files):
        sys.stdout.write(git('show', f'{commit}:{f}') + '\n')


if __name__ == '__main__':
    main()
