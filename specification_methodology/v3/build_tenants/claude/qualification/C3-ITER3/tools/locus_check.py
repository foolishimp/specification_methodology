"""Check that every `member.md#anchor` locus in the frontier resolves to a heading in standards/.

Usage, from the tenant root: python3 -I qualification/C3-ITER3/tools/locus_check.py
"""
import glob
import sys
import os
import re


def slug(h):
    return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')


anch = {}
for f in glob.glob('standards/**/*.md', recursive=True):
    seen, a, code = {}, set(), False
    for line in open(f, encoding='utf-8'):
        if line.startswith('```'):
            code = not code
        if code:
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            seen[s] = n + 1
            a.add(s if n == 0 else f'{s}-{n}')
    anch[os.path.relpath(f, 'standards')] = a
bad = tot = 0
for n, line in enumerate(open('frontier/PREDECESSOR_CLAIMS.md', encoding='utf-8'), 1):
    if not line.startswith('| '):
        continue
    loc = line.rstrip('\n').split(' | ')[-1]
    for m in re.finditer(r'`(?:standards/)?([A-Za-z_/]+\.md)#([^`]+)`', loc):
        tot += 1
        if m.group(2) not in anch.get(m.group(1), set()):
            bad += 1
            print('BAD', n, m.group(0)[:80])
print('loci', tot, 'bad', bad)
sys.exit(1 if bad else 0)  # an unresolved locus fails the check
