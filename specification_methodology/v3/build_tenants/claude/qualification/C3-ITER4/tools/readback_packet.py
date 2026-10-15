"""Build the successor-readback packet (I4-09) from reassess/successor-readback.json.
Each row gives the predecessor section at rc.2 (the row's own text), the successor loci at the
current tree with their subsections, and the extra sections the reader needs. Run from the tenant
root with python3 -I; writes qualification/C3-ITER4/reassess/batch-09.md.
"""
import json, os, re, sys
RC2 = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'
ARGS = list(sys.argv); sys.argv = [sys.argv[0], '--whole']
exec(open('qualification/C3-ITER4/tools/modal_batches.py').read().split('rev = json.load')[0])
rev = json.load(open('frontier/REVIEW.json')); byid = {r['id']: r for r in rev['rows']}
LIST = ARGS[1] if len(ARGS) > 1 else 'qualification/C3-ITER4/reassess/successor-readback.json'
OUT = ARGS[2] if len(ARGS) > 2 else 'qualification/C3-ITER4/reassess/batch-09.md'
spec = json.load(open(LIST))
cache = {}
def sec(path, anchor, whole):
    k = (path, whole)
    if k not in cache: cache[k] = (sections_whole(path) if whole else sections(path)) if os.path.exists(path) else {}
    return cache[k].get(anchor)
def extra_text(ref):
    if ref.startswith('rc2:'):
        body = ref[4:]
        if '#' in body:
            f, a = body.split('#', 1); t = sec(os.path.join(RC2, f), a, True); return f'rc.2 `{f}#{a}`', t
        f, rng = body.rsplit(':', 1); a, b = [int(x) for x in rng.split('-')]
        lines = open(os.path.join(RC2, f), encoding='utf-8').read().split('\n'); return f'rc.2 `{f}` lines {a}-{b}', '\n'.join(lines[a-1:b])
    whole = ref.startswith('whole:'); body = ref[6:] if whole else ref
    f, a = body.split('#', 1); return f'`{f}#{a}`' + (' (with its subsections)' if whole else ''), sec(f, a, whole)
out = [f"# I4-09 successor readback {OUT.rsplit('/',1)[-1][:-3]}\n\nRows: {len(spec['rows'])}. Each row gives the predecessor section at the installed rc.2 and the successor loci at the current tree with their subsections, then the extra sections the earlier reading said it needed. Judge each row under INSTRUCTIONS.md; the `why` line says what the earlier reading found.\n"]
for row in spec['rows']:
    r = byid.get(row['id'])
    if r is None: out.append(f"\n\n### Row `{row['id']}`\n\n(not a frontier row)\n"); continue
    pm, pa = r['source_member'], r['source_anchor'][1:]
    pt = sec(os.path.join(RC2, pm), pa, False) or '(predecessor anchor not resolved at rc.2; tenant child row)'
    out.append(f"\n\n### Row `{row['id']}` (earlier reading: {row['why']}; disposition `{r['disposition']}`)\n\nPredecessor, `{pm}#{pa}` at rc.2:\n\n```text\n{pt.strip()}\n```\n")
    for l in r['successor_loci']:
        mf, a = l['locus'].split('#', 1); t = sec(os.path.join('standards', mf), a, True) or '(locus not resolved)'
        out.append(f"\nSuccessor, `{l['locus']}` (with its subsections):\n\n```text\n{t.strip()}\n```\n")
    for ref in row.get('extra', []):
        label, t = extra_text(ref); out.append(f"\nExtra, {label}:\n\n```text\n{(t or '(not found)').strip()}\n```\n")
open(OUT, 'w').write(''.join(out)); print(OUT, 'rows', len(spec['rows']), 'bytes', sum(len(x) for x in out))
