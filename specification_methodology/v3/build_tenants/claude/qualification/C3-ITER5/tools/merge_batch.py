"""Merge one iteration 5 reading batch result into frontier/REVIEW_ASSESSMENTS.json.
Usage, from the tenant root: python3 -I qualification/C3-ITER5/tools/merge_batch.py <batch file> "<assessor label>" [--replace]
Then regenerate frontier/REVIEW.json with qualification/C3-ITER4/tools/frontier_review.py.
"""
import json, os, sys
from collections import Counter
path_in, label = sys.argv[1], sys.argv[2]
replace = '--replace' in sys.argv
b = json.load(open(path_in))
path = 'frontier/REVIEW_ASSESSMENTS.json'
A = json.load(open(path)) if os.path.exists(path) else {'kind': 'claude-frontier-review-assessments', 'assessments': []}
ids = {r['id'] for r in b['rows']}
have = {a['id'] for a in A['assessments']}
dup = ids & have
if dup and not replace:
    raise SystemExit(f'refusal: {len(dup)} rows already assessed; pass --replace to supersede: {sorted(dup)[:5]}')
A['assessments'] = [a for a in A['assessments'] if a['id'] not in ids]
for r in b['rows']:
    A['assessments'].append({'id': r['id'], 'semantic_review': {
        'result': r['result'], 'modal_force': r.get('modal_force', 'not_applicable'), 'assessed_by': label, 'record': path_in,
        'scope': r.get('scope', 'owning text comparison on the batch texts; consumer bindings not read'),
        'what_changed': r.get('what_changed', ''), 'counterexample': r.get('counterexample', ''), 'smallest_repair': r.get('smallest_repair', '')}})
json.dump(A, open(path, 'w'), indent=1, ensure_ascii=False)
print('merged', len(b['rows']), 'rows; assessments now', len(A['assessments']), Counter(a['semantic_review']['result'] for a in A['assessments']))
