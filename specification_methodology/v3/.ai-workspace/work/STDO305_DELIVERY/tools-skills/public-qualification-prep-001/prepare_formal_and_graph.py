from pathlib import Path
import json
import run_observed as o

p = Path(__file__).absolute().parent
h = json.loads((p / 'SELECTED_HANDOFF.json').read_bytes()); b = Path(h['workspace']); native = Path(h['native_root']); ac = b / 'runtime/a_c'
py = json.loads((b / 'dependencies/graphify/RUNTIME.json').read_bytes())['python']
assert (p / 'HOST_SELECTIONS.json').is_file(), 'Early actual initializer and MCP checks must precede full formal work'
formal = p / 'formal'; formal.mkdir(exist_ok=False)

def run(*args, **kwargs):
    receipt, result = o.run(*args, **kwargs)
    assert receipt['execution']['returncode'] == 0, receipt
    return receipt, result

archive = native / 'standards/documentation/proofs/transport/TRANSPORT.json'
archive_ref = 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/cohort-recovery-020/archives/current-transport/TRANSPORT.json'
assert o.sha(archive) == '442c29433b39c0ec95846305b6de16d4a01286d0c8eb92c9e739b5b85455004c'
run('recover-construction-proof', [py, '-I', '-B', native / 'standards/documentation/proofs/materialize.py',
    'materialize', '--destination', b / 'construction-evidence'],
    'specification_methodology/v3/build_tenants/common-tools/proof_evidence.py',
    inputs=[(archive, archive_ref)],
    output_files=[b / 'construction-evidence/manifest.json', b / 'construction-evidence/result.json'])
request = formal / 'request.json'
run('portable-request', [py, '-I', '-B', native / 'standards/documentation/proofs/materialize.py', 'request',
    '--evidence', b / 'construction-evidence', '--output', request],
    'specification_methodology/v3/build_tenants/common-tools/proof_evidence.py',
    inputs=[(archive, archive_ref), b / 'construction-evidence/result.json', b / 'construction-evidence/input.json', b / 'construction-evidence/supplied-views.json'],
    output_files=[request])
selected = json.loads(request.read_bytes())
assert selected['input']['path'] == str(b / 'construction-evidence/input.json')
assert selected['input']['raw_sha256'] == '0efcfe8ce9fb8c8abad1db75ee53982b50460d3048ff7060eb3c94ef5b472a2e'
checker = json.loads((b / 'formal/checker.json').read_bytes())
(formal / 'runtime-identity.json').write_bytes(o.encoded(checker['runtime_identity']))
construction = json.loads((b / 'construction-evidence/result.json').read_bytes())['runtime_identity']
differences = {key: {'construction': construction['pins'].get(key), 'installed': checker['runtime_identity']['pins'].get(key)}
               for key in construction['pins'].keys() | checker['runtime_identity']['pins'].keys()
               if construction['pins'].get(key) != checker['runtime_identity']['pins'].get(key)}
assert all(key in ['.cache/formal-origin-v1/selection.json', 'profiles/proof-support-v1.json'] for key in differences), differences
(formal / 'RUNTIME_CORRESPONDENCE.json').write_bytes(o.encoded({'schema': 'stdo305.runtime-causal-comparison/1',
    'construction_runtime': construction['sha256'], 'current_runtime': checker['runtime_identity']['sha256'],
    'differences': differences, 'standing': 'Actual source pin comparison only; no current execution verdict is inferred.'}))
selections = o.REPO / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/representation/repair-002/formal-selections.json'
model = b / 'source-tools/stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/model.json'
carrier = model.with_name('carrier.json')
run('actual-upstream-roundtrip', [py, '-B', ac / 'build_tenants/graphify/code/ac_upstream.py', '--model', model,
    '--carrier', carrier, '--selections', selections, '--upstream', b / 'dependencies/graphify/graphify',
    '--runtime', b / 'dependencies/graphify/RUNTIME.json', '--output', b / 'graphify/current-roundtrip'],
    'a_c/build_tenants/graphify/code/ac_upstream.py',
    inputs=[(model, 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/model.json'),
            (carrier, 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/carrier.json'), selections,
            b / 'dependencies/graphify/RUNTIME.json'], output_tree=b / 'graphify/current-roundtrip')
print(json.dumps({'status': 'actual_current_request_graph_and_runtime_ready', 'request': o.ref(request),
                  'runtime_identity': checker['runtime_identity']['sha256']}))
