import json, sys, collections
C, X, out = sys.argv[1], sys.argv[2], sys.argv[3]
c = {r['id']: r for r in json.load(open(C))['rows']}
x = {r['id']: r for r in json.load(open(X))['rows']}
def norm(d):
    d = (d or '').strip().lower()
    return {'not': 'not applicable'}.get(d, d)
print('claude rows', len(c), 'codex rows', len(x))
only_c = sorted(set(c) - set(x)); only_x = sorted(set(x) - set(c))
print('ids only in claude', len(only_c), 'only in codex', len(only_x))
tab = collections.Counter()
diff = []
for i in sorted(set(c) & set(x)):
    a, b = norm(c[i]['disposition']), norm(x[i]['disposition'])
    tab[(a, b)] += 1
    if a != b: diff.append((i, a, b))
for (a, b), n in sorted(tab.items(), key=lambda t: -t[1]): print(f'{n:4d}  claude={a:16s} codex={b}')
with open(out, 'w') as f:
    json.dump({'only_claude': only_c, 'only_codex': only_x,
               'differ': [{'id': i, 'claude': a, 'codex': b,
                           'claude_note': c[i].get('disposition_note', ''),
                           'claude_loci': [l['locus'] if isinstance(l, dict) else l for l in c[i].get('successor_loci', [])],
                           'codex_loci': x[i].get('successor_loci', []),
                           'codex_group': x[i].get('comparison_group', '')} for i, a, b in diff]}, f, indent=1)
print('differ', len(diff)); print('sample only_codex', only_x[:10]); print('sample only_claude', only_c[:10])
