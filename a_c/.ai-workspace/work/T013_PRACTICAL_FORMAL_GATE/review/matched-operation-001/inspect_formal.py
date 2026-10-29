"""Read-only exact cold/current-reuse source and output inspection."""
from pathlib import Path
from collections import deque
import ast
import copy
import hashlib
import json
import re

R = Path(__file__).resolve().parent
W = R.parents[1]
AC = W.parents[2]
LEAN = AC / 'build_tenants/lean'
A = W / 'real-use/runtime-preparation-003/execution-001'
B = W / 'real-use/runtime-preparation-003/execution-002'
def load(path):
    assert 'formal-origin-v1' not in path.parts
    return json.loads(path.read_bytes())
def sha(path):
    assert 'formal-origin-v1' not in path.parts
    with path.open('rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()
def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()
hashes = load(R / 'SELECTED-HASHES.json')['members']
def retained_hash(path):
    return hashes[path.relative_to(W).as_posix()]['sha256']

# This is the previously closed independent Reviewer calculation, inspected and
# copied as source. It does not import the candidate or run any proof/toolchain.
constants = {}
for n in ast.parse((LEAN / 'scripts/import_fixture.py').read_text()).body:
    if isinstance(n, ast.Assign):
        for target in n.targets:
            if isinstance(target, ast.Name) and target.id in ('FAMILIES', 'VARIANTS'):
                constants[target.id] = ast.literal_eval(n.value)
families, variants = constants['FAMILIES'], constants['VARIANTS']
exec(compile((R / 'reconstruct_subject.py').read_text(), str(R / 'reconstruct_subject.py'), 'exec'))

selection = load(A / 'PROOF-RESULT.json')
cold = W / selection['gate_root'] / 'bundle'
result = load(cold / 'result.json')
request = load(cold / 'request.json')
manifest = load(cold / 'manifest.json')
identity = load(W / 'lean/view-repair-implementation-001/SOURCE-PINS.json')['runtime_identity']
assert result['runtime_identity'] == identity
assert digest(identity['pins']) == 'f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9'
source_pins = {k: v for k, v in identity['pins'].items() if not k.startswith('.cache/')}
for path, pin in source_pins.items(): assert sha(LEAN / path) == pin, path
current = load(A / 'CURRENTNESS.json')
for path, pin in current['source_pins'].items(): assert sha(Path(path)) == pin
assert result['status'] == 'verified' and result['checked_claims'] == result['requested_claims'] == selection['checked_claims']
assert result['request_sha256'] == digest(request)
assert retained_hash(cold / 'result.json') == selection['result_sha256'] == '72ad6dc64938ab0e76476f5d479c9154035131354423ebbbb9fde38c8737dfe4'
assert retained_hash(cold / 'manifest.json') == selection['manifest_sha256'] == result['evidence']['manifest_sha256']
assert result['evidence']['members'] == manifest['members']
assert retained_hash(cold / 'input.json') == '70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a'
assert retained_hash(cold / 'supplied-views.json') == '70bfa0148bcb3bc10111a99a60fa42c2e87f5b99352ed446fe4c09178f419768'
assert request['selections'] == selection['selections'] and request['context_binding'] == selection['context_binding']
assert request['selections'][0]['budget_records'] == 29
assert request['context_binding']['rendered_sha256'] == 'f114593150b15dc49a5aa58c1f018f43e731f77d5d3c15eea632ebdd28a83bfa'
subject = independently_reconstruct(cold)
assert (subject['records'], subject['references'], subject['edges'], subject['external_resolutions']) == (1987, 16498, 3995, 1021)
assert len(subject['selected_indices']) == 29
assert retained_hash(cold / 'GateViews.lean') == sha(W / 'lean/view-repair-implementation-001/actual-29/GateViews.lean')
old = W / 'reuse/qualification-001/full-cold'
conserved_generated = ['GateData.lean', 'GateLocalNames.lean', 'GateExternalNames.lean', 'GateIdentities.lean', 'GateBounds.lean', 'GateModel.lean', 'GateRun.lean']
for name in conserved_generated: assert retained_hash(cold / name) == sha(old / name), name
obs = result['observations']
counts = ('current_dynamic_proof_invocations', 'current_kernel_replay_invocations', 'current_runtime_invocations')
assert tuple(obs[k] for k in counts) == (7, 1, 1)
assert obs['limits']['memory_mb'] == 4096 and obs['limits']['timeout_seconds'] == 90
assert all(s['seconds'] < 90 and s.get('exit_code', 0) == 0 for s in obs['stages'])
audits = {}
for name in ('GateLocalNames', 'GateExternalNames', 'GateIdentities', 'GateBounds', 'GateModel', 'GateViews'):
    log = (cold / (name + '.log')).read_text()
    audits.update({n: sorted(x.strip() for x in a.split(',') if x.strip()) for n, a in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)})
    audits.update({n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)})
assert audits == obs['theorem_audit'] and all(set(v) <= {'Classical.choice', 'Quot.sound', 'propext'} for v in audits.values())
reuse = load(B / 'operational/FORMAL-REUSE.json')
reuse_summaries = {}
for stage, recorded in reuse['stages'].items():
    d = W / recorded['replay_bundle']; r = load(d / 'result.json'); m = load(d / 'manifest.json'); o = r['observations']
    assert retained_hash(d / 'result.json') == recorded['result_sha256']
    assert r['evidence']['members'] == m['members'] and r['evidence']['manifest_sha256'] == retained_hash(d / 'manifest.json')
    assert r['status'] == 'verified' and r['runtime_identity'] == identity
    assert r['checked_claims'] == result['checked_claims'] and r['requested_claims'] == result['requested_claims']
    assert r['context_binding'] == result['context_binding'] and r['selections'] == result['selections']
    assert o['reuse'] == 'local-origin' and tuple(o[k] for k in counts) == (0, 0, 0)
    assert o['support'] == obs['support'] and o['limits'] == obs['limits']
    assert o['original_establishment']['result_sha256'] == retained_hash(d / 'origin-result.json') == selection['result_sha256']
    assert o['original_establishment']['manifest_sha256'] == retained_hash(d / 'origin-manifest.json') == selection['manifest_sha256']
    assert load(d / 'origin-result.json') == result
    for name in ('input.json', 'model.json', 'certificates.json', 'actual-runtime.log', 'supplied-views.json', 'view-comparison.json', *conserved_generated, 'GateViews.lean'):
        assert retained_hash(d / name) == retained_hash(cold / name), name
    stages = [s['stage'] for s in o['stages']]
    assert stages == ['acquire-import-reconstruct', 'support-pins', 'current-certificates', 'authenticated-artifacts', 'output-view-correspondence', 'support-pins-after', 'origin-currentness']
    reuse_summaries[stage] = {'result_sha256': retained_hash(d / 'result.json'), 'seconds': o['elapsed_seconds'],
        'counts': {k: o[k] for k in counts}, 'original_result_sha256': o['original_establishment']['result_sha256'],
        'entry_id': o['original_establishment']['entry_id'], 'exact_cold_source_output_view_preserved': True,
        'formal_use_artifact': recorded['formal_use_artifact']}
assert len({v['entry_id'] for v in reuse_summaries.values()}) == 1
report = {'schema': 'a_c.T013.independent-actual-formal-path-checks/1', 'status': 'PASS',
    'subject': subject, 'cold_result_sha256': retained_hash(cold / 'result.json'),
    'source_identity': identity['sha256'], 'current_public_runtime_coordinates': len(source_pins),
    'current_graphify_source_coordinates': len(current['source_pins']), 'audits_checked': len(audits),
    'cold_stages': obs['stages'], 'cold_checking_seconds': obs['elapsed_seconds'],
    'cold_counts': {k: obs[k] for k in counts}, 'reuse': reuse_summaries,
    'conserved_generated_sources': conserved_generated, 'same_reviewed_29_view_module': True,
    'scope': 'Independent full model/reference/basis/authority/residual/actual projection/source-view correspondence on new cold output; byte-identical authenticated-reuse outputs; no product/proof/native execution or private-origin acquisition',
    'not_claimed': 'No fresh library/kernel run, compiled-object recensus, semantic source adequacy or permission supplied by the theorem'}
with (R / 'FORMAL-CHECKS.json').open('x', encoding='utf-8') as f:
    f.write(json.dumps(report, sort_keys=True, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'subject': subject, 'audits': len(audits), 'reuse_stages': list(reuse_summaries)}))
