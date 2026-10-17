"""Write the iteration 5 conservation reading batches: every `conserved` frontier row whose semantic
review is still `indeterminate`, with the predecessor section at rc.2 (whole, with subsections) and the
successor locus text at the current tree (whole). Batches are at most LIMIT bytes, grouped by member.
Run from the tenant root with python3 -I; writes qualification/C3-ITER5/reassess/batch-NN.md.
"""
import json, os, re, sys
RC2 = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'
LIMIT = 200_000
def slug(h): return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
def sections_whole(path):
    out, seen, code = {}, {}, False
    lines = open(path, encoding='utf-8').read().split('\n'); heads = []
    for i, line in enumerate(lines):
        if line.startswith('```'): code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            sl = slug(m.group(2)); n = seen.get(sl, 0); seen[sl] = n + 1
            heads.append((i, len(m.group(1)), sl if n == 0 else f'{sl}-{n}'))
    for k, (i, lvl, a) in enumerate(heads):
        end = len(lines)
        for j, l2, _ in heads[k+1:]:
            if l2 <= lvl: end = j; break
        out[a] = '\n'.join(lines[i:end])
    return out
rev = json.load(open('frontier/REVIEW.json'))
rows = [r for r in rev['rows'] if r['disposition'] == 'conserved' and r.get('semantic_review', {}).get('result') == 'indeterminate']
cache = {}
def text(member_file, anchor, root):
    k = (root, member_file)
    if k not in cache:
        p = os.path.join(root, member_file); cache[k] = sections_whole(p) if os.path.exists(p) else {}
    return cache[k].get(anchor)
items = []
for r in rows:
    pm, pa = r['source_member'], r['source_anchor'][1:]
    pt = text(pm, pa, RC2) or '(predecessor anchor not resolved at rc.2; tenant child row: judge on the successor text alone, answer indeterminate)'
    body = f"\n\n### Row `{r['id']}` (disposition `conserved`)\n\nPredecessor, `{pm}#{pa}` at rc.2:\n\n```text\n{pt.strip()}\n```\n"
    for l in r['successor_loci']:
        mf, a = l['locus'].split('#', 1); body += f"\nSuccessor, `{l['locus']}`:\n\n```text\n{(text(mf, a, 'standards') or '(locus not resolved)').strip()}\n```\n"
    items.append((pm, r['id'], body))
items.sort()
batches, cur, size = [], [], 0
for pm, i, body in items:
    if cur and size + len(body) > LIMIT: batches.append(cur); cur, size = [], 0
    cur.append((pm, i, body)); size += len(body)
if cur: batches.append(cur)
for k, b in enumerate(batches, 1):
    with open(f'qualification/C3-ITER5/reassess/batch-{k:02d}.md', 'w', encoding='utf-8') as f:
        f.write(f"# I5-03 reading batch {k:02d}\n\nRows: {len(b)}. Members: {sorted({pm for pm,_,_ in b})}. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.\n")
        for _, _, body in b: f.write(body)
    print(f'batch-{k:02d}', len(b), 'rows', round(sum(len(x[2]) for x in b)/1024), 'KB', sorted({pm for pm,_,_ in b}))
print('rows', len(items), 'batches', len(batches))
