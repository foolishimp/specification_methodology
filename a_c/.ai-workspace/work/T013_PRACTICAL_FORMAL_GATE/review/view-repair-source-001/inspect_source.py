"""Read-only stdlib source/retained-evidence comparison; no product imports or runs."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import re

REVIEW = Path(__file__).resolve().parent
WORK = REVIEW.parents[1]
ROOT = WORK.parents[2]
TENANT = ROOT / 'build_tenants/lean'
IMPL = WORK / 'lean/view-repair-implementation-001'
PLAN = WORK / 'lean/view-repair-001'
read = lambda p: p.read_text(encoding='utf-8')
load = lambda p: json.loads(p.read_bytes())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
text_sha = lambda t: hashlib.sha256(t.encode()).hexdigest()
checks = {}

expected = {
    'CLOSED.json': 'be5621baa8dcd9177389201fd6319d27b054e5260a089ea2844f0c45edf8f60d',
    'SOURCE-PINS.json': 'f19d592d81a76a4c8c1153e867982aba750c46838fd7a827fc6cebdf08ecd242',
    'candidate.patch': '0cd1075e317593bcfc37f648828bd1b256f3f3d5c84ed8e453b5f22996983aa1',
}
for name, pin in expected.items():
    assert sha(IMPL / name) == pin, name
pins = load(IMPL / 'PINS.json')['members']
for name, pin in pins.items():
    assert sha(IMPL / name) == pin, name
checks['selected_artifact_hashes'] = {'members': len(pins), 'bytes': sum((IMPL / p).stat().st_size for p in pins), 'status': 'PASS'}

source = load(IMPL / 'SOURCE-PINS.json')
baseline = load(IMPL / 'BASELINE.json')
bundle = Path(baseline['frozen_bundle'])
patch = ''
for name, pair in source['changed_files'].items():
    after = ROOT / name
    assert sha(after) == pair['after_sha256'], name
    before = IMPL / 'before' / name
    prior = '' if pair['before_sha256'] is None else read(before)
    if pair['before_sha256'] is not None:
        assert sha(before) == pair['before_sha256']
    patch += ''.join(difflib.unified_diff(prior.splitlines(True), read(after).splitlines(True),
        fromfile='/dev/null' if pair['before_sha256'] is None else 'a/' + name, tofile='b/' + name))
assert patch == read(IMPL / 'candidate.patch')
checks['exact_patch_and_live_sources'] = {'status': 'PASS', 'changed_files': source['changed_files']}

portable = source['origin_free_identity']['pins']
for name, pin in portable.items():
    assert not name.startswith('.cache/')
    assert sha(TENANT / name) == pin, name
for name, pin in source['conservation']['unchanged_runtime_sources'].items():
    assert baseline['public_runtime_pins'][name] == portable[name] == pin
assert set(portable) - set(source['conservation']['unchanged_runtime_sources']) == {'scripts/formal_gate.py', 'scripts/gate_codegen.py'}
for coordinate in ('runtime_identity', 'origin_free_identity'):
    identity = source[coordinate]
    canonical = json.dumps(identity['pins'], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    assert text_sha(canonical) == identity['sha256']
assert {k: v for k, v in source['runtime_identity']['pins'].items() if k != '.cache/formal-origin-v1/selection.json'} == portable
checks['source_conservation'] = {'status': 'PASS', 'portable_coordinates_hashed': len(portable),
    'conserved_coordinates': len(source['conservation']['unchanged_runtime_sources']),
    'support_descriptor_only': portable['profiles/proof-support-v1.json'],
    'private_origin_acquired': False, 'large_support_members_rehashed': False}

old_codegen = read(IMPL / 'before/build_tenants/lean/scripts/gate_codegen.py')
new_codegen = read(TENANT / 'scripts/gate_codegen.py')
def rest_without_views(text):
    tree = ast.parse(text)
    tree.body = [n for n in tree.body if not isinstance(n, ast.FunctionDef) or n.name != 'views_source']
    return ast.dump(tree, include_attributes=False)
assert rest_without_views(old_codegen) == rest_without_views(new_codegen)
old_gate = read(IMPL / 'before/build_tenants/lean/scripts/formal_gate.py')
new_gate = read(TENANT / 'scripts/formal_gate.py')
assert old_gate.count('views_source(cases)') == 1
assert old_gate.replace('views_source(cases)', 'views_source(imported,cases)') == new_gate
checks['minimal_deciding_delta'] = 'PASS: only views_source implementation and its single caller differ; generic/runtime logic conserved'

positive = read(IMPL / 'actual-29/GateViews.lean')
proposal = read(PLAN / 'PROPOSED_GateViews.lean')
assert positive == proposal.replace('-- PROPOSAL ONLY: not compiled or qualified in this activation.\n', '', 1)
old_view = read(bundle / 'GateViews.lean')
assert sha(bundle / 'GateViews.lean') == baseline['frozen_members']['GateViews.lean']
assert positive.split('theorem witness_edge0_0')[0] == old_view.split('theorem checked0')[0]
suffix = positive[positive.index('theorem set0'):]
assert suffix == old_view[old_view.index('theorem set0'):]
assert text_sha(suffix) == source['conservation']['normal_29_suffix_sha256']
for name in ('budget-28-new.lean', 'budget-28-old.lean'):
    text = read(IMPL / name)
    assert text_sha(text[text.index('theorem set0'):]) == source['conservation']['one_below_28_suffix_sha256']
for token in ('sorry', 'native_decide', 'axiom '):
    assert token not in positive
assert 'set_option debug.skipKernelTC false' in positive
checks['generated_proposal_and_suffix'] = {'status': 'PASS', 'positive_source_sha256': sha(IMPL / 'actual-29/GateViews.lean'),
    'same_prefix_seeds_trace_included': True, 'normal_and_underbudget_suffix_conserved': True}

parents = load(PLAN / 'PARENT-WITNESSES.json')
assert sha(PLAN / 'PARENT-WITNESSES.json') == 'c9ef73dc41a0d57f420e1f0cd5efccfca87eb63d39456afb0707f8b8866fac82'
edges = re.findall(r'theorem witness_edge0_(\d+) : (\d+) ∈ model.dependencies (\d+) := by decide \+kernel', positive)
assert len(edges) == 27
known = set(parents['seeds'])
for (step, child, parent), row in zip(edges, parents['rows']):
    assert (int(step), int(child), int(parent)) == (row['ordinal'], row['target'], row['parent'])
    assert sorted(known) == row['known_before'] and int(parent) in known
    known.add(int(child))
assert sorted(known) == parents['included'] and len(known) == 29
assert 1867 not in [r['parent'] for r in parents['rows']]
checks['conserved_independent_parent_analysis'] = {'status': 'PASS', 'rows': 27,
    'prior_review_closure': '69b7a119bfa5dcd7cf3ca29fd490ec1b15bf3533ee9811638a5a4aab53d8812b',
    'meaning': 'Same exact witnesses as prior independent 3995-edge analysis; no repetition of full source census'}

for name in ('certificates.json', 'request.json', 'supplied-views.json'):
    assert sha(bundle / name) == baseline['frozen_members'][name]
checks['same_selection_custody'] = {name: sha(bundle / name) for name in ('certificates.json', 'request.json', 'supplied-views.json')}

external = load(IMPL / 'actual-29-attempt-001.external.json')
log = read(IMPL / 'actual-29-attempt-001.log')
audits = {name: sorted(x.strip() for x in values.split(',')) for name, values in
    re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]", log)}
expected_names = {'AC.GateData.' + p + '0' for p in ('checked', 'set', 'reachability', 'result', 'execution_matches_project')}
assert set(audits) == expected_names and audits == external['audit']
assert all(v == ['Classical.choice', 'Quot.sound', 'propext'] for v in audits.values())
assert external['returncode'] == 0 and external['audit_status'] == 'PASS'
assert external['source_sha256'] == sha(IMPL / 'actual-29/GateViews.lean') and external['log_sha256'] == sha(IMPL / 'actual-29-attempt-001.log')
assert external['timeout_seconds'] == 90 and external['argv'][1:5] == ['-j', '1', '-M', '4096']
assert external['LEAN_PATH'].split(':')[0] == str(bundle)
checks['actual_positive_component'] = {'status': 'PASS', 'seconds': external['seconds'],
    'audit': audits, 'uses_conserved_prior_model_objects': True, 'fresh_public_replay_or_runtime': False}

negatives = [('unknown-parent', 'UnknownParent', '181 ∈ seeds0'),
             ('missing-edge', 'MissingEdge', '1122 ∈ model.dependencies 278'),
             ('omitted-residual', 'OmittedResidual', 'Closed model.dependencies (traceSet seeds0 trace0)')]
negative_results = []
for label, filename, predicate in negatives:
    receipt = load(IMPL / (label + '-attempt-001.external.json'))
    log_path = IMPL / (label + '-attempt-001.log')
    log = read(log_path)
    assert receipt['source_sha256'] == sha(IMPL / ('negatives/' + filename + '.lean'))
    assert receipt['log_sha256'] == sha(log_path)
    assert receipt['returncode'] == 1 and not receipt['resource_failure']
    assert receipt['timeout_seconds'] == 90 and receipt['argv'][1:5] == ['-j', '1', '-M', '4096']
    assert log.count('error:') == 1 and 'Tactic `decide` proved that the proposition' in log and predicate + '\nis false' in log
    negative_results.append({'label': label, 'predicate': predicate, 'seconds': receipt['seconds'], 'status': 'intended kernel refusal'})
checks['affected_kernel_negatives'] = negative_results

python = load(IMPL / 'PYTHON-RESULTS.json')
python_log = read(IMPL / 'python-controls.log')
assert (python['tests'], python['failures'], python['errors'], python['skips']) == (77, 0, 0, 0)
assert 'test_later_parent_in_internal_trace_is_retained_as_incomplete' in python_log
assert re.search(r'Ran 77 tests in [0-9.]+s\s+OK', python_log)
checks['conserved_python_controls'] = {'status': 'PASS', 'tests': 77, 'skips': 0,
    'reviewer_rerun': False, 'scope': 'Retained author controls; exact live source attribution and harness inspection; unit support/reuse stubs remain unit evidence'}

result = {'schema': 'a_c.T013.independent-view-repair-source-checks/1', 'status': 'PASS', 'checks': checks,
    'effects': 'Read-only stdlib file/hash/AST/text comparisons; output only in active review directory; no product imports or compiler/proof/actor/Context/Git/private-origin operations',
    'remaining': 'Actual full public same-model 29-view cold proof/replay/runtime and current source/checker/Context/authority bindings; repair discharge remains open'}
with (REVIEW / 'CHECKS.json').open('x', encoding='utf-8') as f:
    f.write(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': len(checks), 'artifact_members': len(pins), 'source_pins': len(portable), 'checks_sha256': sha(REVIEW / 'CHECKS.json')}, sort_keys=True))
