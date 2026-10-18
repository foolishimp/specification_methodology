"""Merge one I4-04 batch result into frontier/REVIEW_ASSESSMENTS.json.
Usage, from the tenant root: python3 -I qualification/C3-ITER4/tools/merge_batch.py NN "<assessor label>"
Then regenerate frontier/REVIEW.json with frontier_review.py.
"""
import json, os, sys
from collections import Counter
n, label = sys.argv[1], sys.argv[2]
replace = '--replace' in sys.argv
b = json.load(open(f'qualification/C3-ITER4/reassess/batch-{n}.json'))
path = 'frontier/REVIEW_ASSESSMENTS.json'
A = json.load(open(path)) if os.path.exists(path) else {'kind': 'claude-frontier-review-assessments', 'assessments': []}
ids = {r['id'] for r in b['rows']}
if replace: A['assessments'] = [a for a in A['assessments'] if a['id'] not in ids]
have = {a['id'] for a in A['assessments']}
added = 0
for r in b['rows']:
    if r['id'] in have: continue
    A['assessments'].append({'id': r['id'], 'semantic_review': {
        'result': r['result'], 'modal_force': r.get('modal_force'),
        'assessed_by': f'I4-04 batch {n}, {label}', 'record': f'qualification/C3-ITER4/reassess/batch-{n}.json',
        'scope': 'owning text comparison on the batch texts; consumer bindings not read',
        'what_changed': r.get('what_changed', ''), 'counterexample': r.get('counterexample', ''), 'smallest_repair': r.get('smallest_repair', '')}})
    added += 1
json.dump(A, open(path, 'w'), indent=1)
print(f'batch {n}: rows {len(b["rows"])}, added {added}, results {dict(Counter(r["result"] for r in b["rows"]))}, modal {dict(Counter(r.get("modal_force") for r in b["rows"]))}; assessments now {len(A["assessments"])}')
for r in b['rows']:
    if r['result'] != 'conserved': print('  -', r['id'], '|', r['result'], '|', r.get('what_changed', '')[:200], '| repair:', r.get('smallest_repair', '')[:150])
