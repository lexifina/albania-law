"""Prints the law of Albania as it stood on a given day, read from this repository's history.

    python tools/ne_fuqi_me.py 2008-05-21 kushtetuta 64          # art. 64 the day before law 9904/2008
    python tools/ne_fuqi_me.py 2008-05-22 kushtetuta 64          # the same article, as amended
    python tools/ne_fuqi_me.py 2016-08-11 kushtetuta 147/a       # an inserted article (147/a, 6/1, 179/b)
    python tools/ne_fuqi_me.py 2000-01-01 kushtetuta              # the whole Constitution on 1 January 2000
    python tools/ne_fuqi_me.py --law 2020-01-01 kushtetuta 131    # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. An article number (`64`, `6/1`, `147/ç`) means the article of the body of
the Constitution (`neni-064`, `neni-006-01`, `neni-147-c-ced`); annex articles are `aneks-neni-a` and so on.
Standard library only.
"""
import re
import runpy
import sys
from pathlib import Path


def article(unit: str) -> str:
    m = re.fullmatch(r'(\d+)(?:/(\d+|[a-zçë]+))?', unit.strip().lower())
    if not m:
        return unit
    key = f'neni-{int(m.group(1)):03d}'
    sub = m.group(2)
    if sub:
        key += f'-{int(sub):02d}' if sub.isdigit() else '-' + sub.replace('ç', 'c-ced').replace('ë', 'e-uml')
    return key


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
