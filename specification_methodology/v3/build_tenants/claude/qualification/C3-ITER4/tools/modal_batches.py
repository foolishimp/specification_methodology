"""Write the I4-04 reading batches: for every frontier row flagged modal_conversion in
frontier/REVIEW.json, and every row WC-2 judged only from a delta (mark D in
qualification/C3-ITER3/reassess/rows.md), the predecessor section text at rc.2 and the
successor locus text at the current tree. Batches are at most LIMIT bytes, grouped by member.
Run from the tenant root with python3 -I.
"""
import json, os, re
RC2 = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'
LIMIT = 90_000
exec(open('qualification/C3-ITER4/tools/frontier_review.py').read().split('assess = {}')[0])
rev = json.load(open('frontier/REVIEW.json')); byid = {r['id']: r for r in rev['rows']}
want = {r['id']: 'modal' for r in rev['rows'] if r['modal_conversion']}
# WC-2 rows marked D: anchors in rows whose first cell ends with ' D'
dn = 0; unmatched = []
title2id = {}; member = None
for line in open('frontier/PREDECESSOR_CLAIMS.md', encoding='utf-8'):
    if line.startswith('## '): member = line[3:].strip(); continue
    if not line.startswith('| '): continue
    c = [x.strip() for x in line.rstrip('\n').strip('|').split(' | ')]
    am = re.search(r'`#([^`]+)`', c[1]) if len(c) > 5 else None
    if am: title2id.setdefault(re.sub(r'^(&nbsp;)+', '', c[0]).strip().lower(), []).append(f'{member}#{am.group(1)}')
for line in open('qualification/C3-ITER3/reassess/rows.md', encoding='utf-8'):
    m = re.match(r'\| (\d+) (.+?) D \|', line)
    if not m: continue
    title = m.group(2).strip().lower()
    hits = title2id.get(title) or [i for t, ids in title2id.items() if t.endswith(' ' + title) or t == title for i in ids]
    if not hits: unmatched.append(m.group(2)); continue
    for i in hits:
        if i not in want: want[i] = 'delta-judged'; dn += 1
print('delta-judged unmatched titles:', unmatched)
cache = {}
def text(member_file, anchor, root):
    k = (root, member_file)
    if k not in cache:
        p = os.path.join(root, member_file); cache[k] = sections(p) if os.path.exists(p) else {}
    return cache[k].get(anchor)
items = []
for i, why in want.items():
    r = byid[i]; pm = r['source_member']; pa = r['source_anchor'][1:]
    pt = text(pm, pa, RC2) or '(predecessor anchor not resolved at rc.2; tenant child row)'
    st = []
    for l in r['successor_loci']:
        mf, a = l['locus'].split('#', 1); st.append((l['locus'], text(mf, a, 'standards') or '(locus not resolved)'))
    body = f"\n\n### Row `{i}` ({why}; disposition `{r['disposition']}`)\n\nPredecessor, `{pm}#{pa}` at rc.2:\n\n```text\n{pt.strip()}\n```\n"
    for loc, t in st: body += f"\nSuccessor, `{loc}`:\n\n```text\n{t.strip()}\n```\n"
    items.append((pm, i, body))
items.sort()
batches, cur, size, n = [], [], 0, 0
for pm, i, body in items:
    if cur and size + len(body) > LIMIT: batches.append(cur); cur, size = [], 0
    cur.append((pm, i, body)); size += len(body)
if cur: batches.append(cur)
for k, b in enumerate(batches, 1):
    with open(f'qualification/C3-ITER4/reassess/batch-{k:02d}.md', 'w') as f:
        f.write(f"# I4-04 reading batch {k:02d}\n\nRows: {len(b)}. Members: {sorted({pm for pm,_,_ in b})}. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.\n")
        for _, _, body in b: f.write(body)
    print(f'batch-{k:02d}', len(b), 'rows', round(sum(len(x[2]) for x in b)/1024), 'KB', sorted({pm for pm,_,_ in b}))
print('rows', len(items), 'modal', sum(1 for v in want.values() if v=='modal'), 'delta-judged added', dn)
