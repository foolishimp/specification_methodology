import json, re, sys
P, C, X = sys.argv[1:4]
member = None; body = []; nonbody = []
section = None
for line in open(P):
    m = re.match(r'^## (\S+\.md)\s*$', line)
    if m: member = m.group(1); section = 'body'; continue
    if line.startswith('## '): member = None; section = 'nonbody'; continue
    if not line.startswith('| ') or line.startswith('| Section') or line.startswith('|---'): continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if section == 'body' and member:
        a = re.search(r'`(#[^`]+)`', cells[1]) if len(cells) > 1 else None
        if a: body.append(f'{member}{a.group(1)}')
    elif section == 'nonbody':
        a = re.match(r'`([^`]+)`', cells[0])
        if a: nonbody.append(a.group(1))
c = {r['id'] for r in json.load(open(C))['rows']}
x = {r['id'] for r in json.load(open(X))['rows']}
B, N = set(body), set(nonbody)
print('common body rows', len(body), 'unique', len(B), '| non-body rows', len(N))
for name, s in (('claude', c), ('codex', x)):
    print(f'{name}: covers body {len(B & s)}/{len(B)}; non-body {len(N & s)}/{len(N)}; ids outside inventory {len(s - B - N)}')
    miss = sorted(B - s)
    if miss: print('  body rows missing:', miss)
    extra = sorted(s - B - N)
    if extra: print('  outside inventory:', extra)
