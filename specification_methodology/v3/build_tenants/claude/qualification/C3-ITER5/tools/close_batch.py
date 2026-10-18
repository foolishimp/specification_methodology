"""Close one iteration 5 reading batch: check the result covers every row of the batch exactly once, merge
the rows not yet assessed into frontier/REVIEW_ASSESSMENTS.json (rows already assessed are listed as a
second reading, agreeing or not), regenerate frontier/REVIEW.json, and print a summary.
Usage, from the tenant root: python3 -I qualification/C3-ITER5/tools/close_batch.py NN
"""
import json, re, subprocess, sys
from collections import Counter
n = sys.argv[1]
md = open(f'qualification/C3-ITER5/reassess/batch-{n}.md', encoding='utf-8').read()
want = re.findall(r'^### Row `([^`]+)`', md, re.M)
b = json.load(open(f'qualification/C3-ITER5/reassess/batch-{n}.json'))
got = [r['id'] for r in b['rows']]
missing, extra = sorted(set(want) - set(got)), sorted(set(got) - set(want))
dups = [i for i, c in Counter(got).items() if c > 1]
if missing or extra or dups:
    raise SystemExit(f'refusal: batch {n}: missing {missing[:5]} extra {extra[:5]} duplicated {dups[:5]}')
path = 'frontier/REVIEW_ASSESSMENTS.json'
A = json.load(open(path)); prior = {a['id']: a for a in A['assessments']}
label = f"{b.get('reviewer', 'fable, same-family nonauthor, fresh context')}, I5-03 batch {n}"
second = []
for r in b['rows']:
    if r['id'] in prior:
        second.append((r['id'], prior[r['id']]['semantic_review']['result'], r['result'])); continue
    A['assessments'].append({'id': r['id'], 'semantic_review': {
        'result': r['result'], 'modal_force': r.get('modal_force', 'not_applicable'), 'assessed_by': label,
        'record': f'qualification/C3-ITER5/reassess/batch-{n}.json',
        'scope': 'owning text comparison on the batch texts (whole sections); consumer bindings not read',
        'what_changed': r.get('what_changed', ''), 'counterexample': r.get('counterexample', ''), 'smallest_repair': r.get('smallest_repair', '')}})
json.dump(A, open(path, 'w'), indent=1, ensure_ascii=False)
subprocess.run([sys.executable, '-I', 'qualification/C3-ITER4/tools/frontier_review.py'], check=True, capture_output=True)
counts = Counter(r['result'] for r in b['rows'])
print(f'batch {n}: {len(got)} rows {dict(counts)}; merged {len(got) - len(second)}; second readings {len(second)}')
for i, old, new in second:
    print(f'  second reading {i}: earlier {old}, now {new}')
for r in b['rows']:
    if r['result'] == 'changed':
        print(f'  CHANGED {r["id"]}: {r.get("what_changed", "")[:160]} | counterexample: {r.get("counterexample", "")[:200]} | repair: {r.get("smallest_repair", "")[:160]}')
    elif r['result'] == 'indeterminate':
        print(f'  indeterminate {r["id"]}: {r.get("what_changed", "")[:200]}')
rev = json.load(open('frontier/REVIEW.json')); print('frontier assessed:', rev['counts']['assessed'])
