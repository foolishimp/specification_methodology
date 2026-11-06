from pathlib import Path
import json
import run_observed as o

p = Path(__file__).absolute().parent
h = json.loads((p / 'SELECTED_HANDOFF.json').read_bytes()); b = Path(h['workspace']); ac = b / 'runtime/a_c'
py = json.loads((b / 'dependencies/graphify/RUNTIME.json').read_bytes())['python']
request = p / 'formal/request.json'; subject = json.loads(request.read_bytes())
selections = o.REPO / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/representation/repair-002/formal-selections.json'
assert subject['selections'] == json.loads(selections.read_bytes())
assert subject['input']['raw_sha256'] == '0efcfe8ce9fb8c8abad1db75ee53982b50460d3048ff7060eb3c94ef5b472a2e'
assert o.sha(Path(subject['input']['path'])) == subject['input']['raw_sha256']
assert o.sha(Path(subject['supplied_views']['path'])) == subject['supplied_views']['raw_sha256']
assert (p / 'HOST_SELECTIONS.json').is_file()
assert json.loads((p / 'executions/graphify-current-roundtrip/result.json').read_bytes())['status'] == 'verified'
bundle = b / 'formal/current-full-002'
receipt, result = o.run('installed-full-current-verify-002', [py, '-I', '-S', '-B', ac / 'build_tenants/lean/scripts/formal_gate.py',
    'verify', '--request', request, '--output', bundle], 'a_c/build_tenants/lean/scripts/formal_gate.py',
    inputs=[request, Path(subject['input']['path']), Path(subject['supplied_views']['path'])], output_tree=bundle, archived_tree=True)
if receipt['execution']['returncode'] != 0 or result['status'] != 'verified':
    (p / 'formal/INCOMPLETE_002.json').write_bytes(o.encoded({'schema': 'stdo305.actual-formal-frontier/1',
        'execution': o.ref(p / 'executions/installed-full-current-verify-002/execution.json'), 'result': o.ref(bundle / 'result.json'),
        'standing': 'Actual incomplete/refused execution retained. No dependent Context or native host case may consume this as successful proof; no automatic retry.'}))
    raise SystemExit(2)
inspection_receipt, inspection = o.run('installed-full-owner-inspection', [py, '-I', '-S', '-B',
    ac / 'build_tenants/lean/scripts/formal_gate.py', 'inspect-evidence', '--bundle', bundle, '--request', request],
    'a_c/build_tenants/lean/scripts/formal_gate.py', inputs=[request, bundle / 'result.json', bundle / 'manifest.json'])
assert inspection_receipt['execution']['returncode'] == 0 and inspection['status'] == 'consistent'
assert result['runtime_identity'] == json.loads((b / 'formal/checker.json').read_bytes())['runtime_identity']
record = {'schema': 'stdo305.current-installed-formal/1', 'installation': h['native_manifest'], 'request': o.ref(request),
    'runtime_identity': o.ref(p / 'formal/runtime-identity.json'), 'bundle': str(bundle),
    'result': o.ref(bundle / 'result.json'), 'manifest': o.ref(bundle / 'manifest.json'),
    'execution': o.ref(p / 'executions/installed-full-current-verify-002/execution.json'),
    'inspection': o.ref(p / 'executions/installed-full-owner-inspection/execution.json'),
    'standing': 'Actual fresh full-current installed verification and owner consistency inspection. Structural declared-model scope; no source-prose faithfulness or host permission enforcement proof.'}
(p / 'formal/CURRENT_FORMAL.json').write_bytes(o.encoded(record))
print(json.dumps(record))
