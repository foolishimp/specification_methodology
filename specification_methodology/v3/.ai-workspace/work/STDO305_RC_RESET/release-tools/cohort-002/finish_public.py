"""Join actual closed proof transport to the already closed public001 components."""
import copy
import hashlib
import json
from pathlib import Path
R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
C = Path(__file__).resolve().parent
O = Q / 'public-qualification-001/cohort'
TQ = Q / 'public-qualification-001'
sha = lambda b: hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(raw), 'bytes': len(raw)}
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(value, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
def recorded(p):
    value = load(p)
    assert value['execution']['returncode'] == 0
    value['original_execution'] = ref(p)
    return value
candidate = load(R / 'stack_release.json')
closed = load(O / 'CLOSED_BINDINGS.json')
installation = load(O / 'INSTALLATION.json')
subjects = {k: v['subject']['sha256'] for k, v in candidate['products'].items()}
retention = load(TQ / 'proof-retention/COMPLETION.json')
assert retention['status'] == 'passed'
proof = recorded(TQ / 'executions/installed-full-current-verify/execution.json')
inspection = recorded(TQ / 'executions/installed-full-owner-inspection/execution.json')
result = load(R / proof['result']['path'])
assert result['status'] == 'verified' and load(R / inspection['result']['path'])['status'] == 'consistent'
original_result = proof['result']
proof['result'] = next(row for row in proof['execution']['outputs'] if row['path'].endswith('/observed/formal/current-full/result.json'))
assert proof['result']['sha256'] == original_result['sha256']
proof['result_path_binding'] = {'original_recorder_result': original_result, 'selected_bundle_result': proof['result'], 'basis': 'Both actual recorded output references have identical raw bytes. Select the bundle sibling path for complete archive membership; original receipt and execution remain unchanged.'}
bundle_prefix = Path(proof['result']['path']).parent
manifest_ref = ref(R / bundle_prefix / 'manifest.json')
assert manifest_ref['sha256'] == result['evidence']['manifest_sha256']
runtime_ref = ref(TQ / 'formal/runtime-identity.json')
assert load(R / runtime_ref['path']) == result['runtime_identity']
profile_path = TQ / 'observed/runtime/a_c/build_tenants/lean/profiles/proof-support-v1.json'
support_ref = ref(profile_path)
assert support_ref['sha256'] == result['runtime_identity']['pins']['profiles/proof-support-v1.json']
def claim(name, value):
    value.update(kind='stdo.cohort-evidence/1', claim=name, category='execution', status='passed',
        source_identity_sha256=candidate['source']['source_identity_sha256'],
        subjects={p: subjects[p] for p in ('a_c', 'stdo_representation')}, installation=closed['installation'])
    return save(O / 'evidence' / (name + '.json'), value)
proof.update(verification_mode='verify_current', bundle_archive=retention['transport'], bundle_manifest=manifest_ref,
    native_bundle_directory=installation['workspace'] + '/construction-evidence', output_directory=installation['workspace'] + '/formal/current-full',
    current_request=ref(TQ / 'formal/request.json'), runtime_identity=runtime_ref, support_profile=support_ref,
    proof_materialization=recorded(TQ / 'executions/recover-construction-proof/execution.json'),
    current_request_generation=recorded(TQ / 'executions/portable-request/execution.json'),
    original_owner_inspection={'execution': ref(TQ / 'executions/installed-full-owner-inspection/execution.json'), 'result': inspection['result']},
    limits='Actual new full proof and owner inspection under independently support-established public001 runtime. All five selected structural obligations verified with seven dynamic modules, one kernel replay and one runtime comparison. This is not whole-model semantic acceptance or actor instruction assurance. Third-party acquisition used verified APFS clone caches; no support verdict or current proof was copied.')
installed_proof = claim('installed_lean', proof)
construction = load(Q / 'tools-skills/construction-proof-001/CURRENT_FORMAL.json')
source_proof = recorded(R / construction['execution']['path'])
source_proof.update(installed_verification=installed_proof,
    construction_handoff=ref(Q / 'tools-skills/construction-proof-001/CURRENT_FORMAL.json'),
    original_owner_inspection={'execution': construction['inspection_execution'], 'result': construction['inspection']},
    limits='Original current RC construction proof and inspection retained with their actual source runtime and invocation. Separate installed_verification is the new public001 execution with only allowed profile/origin identity differences. Installation is a current-subject correspondence join, not relabelling source execution as installed. The preserved semantic assessment remains bounded to coordinate-conserved content.')
source_ref = claim('exact_candidate_lean_result', source_proof)
evidence = {**closed['evidence'], 'installed_lean': installed_proof, 'exact_candidate_lean_result': source_ref}
required = {name for component in candidate['components'].values() for name in component['required_claims']}
assert set(evidence) == required, (set(evidence) - required, required - set(evidence))
for component in candidate['components'].values():
    component['evidence'] = {name: evidence[name] for name in component['required_claims']}
aggregate = {'kind': 'stdo.cohort-evidence/1', 'claim': 'complete_installed_cohort', 'category': 'installed_aggregate', 'status': 'passed',
    'source_identity_sha256': candidate['source']['source_identity_sha256'], 'subjects': subjects, 'installation': closed['installation'],
    'component_evidence': {name: value for name, value in evidence.items() if name != 'independent_semantic_review'},
    'limits': 'All fourteen selected component observations are closed for the exact corrected RC public001 cohort. Original source-side operations, independent semantic scope and installed execution identities remain distinct. Fixed host interfaces and initialized MCP were exercised; no new LLM or Context session was selected. This aggregate does not assert that the final public gate, Latest, adoption or universal behavior have occurred.'}
assert len(aggregate['component_evidence']) == 14
aggregate_ref = save(O / 'evidence/complete_installed_cohort.json', aggregate)
print(json.dumps({'aggregate': aggregate_ref, 'installation': closed['installation']}))
