"""Actual old-selection refusal and owner compatibility, without support/Lean execution."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).absolute().parent
WORK = HERE.parent
LEAN = REPO / 'a_c/build_tenants/lean'
sys.path.insert(0, str(REPO / 'a_c/build_tenants/graphify/code'))
import ac_formal_gate as adapter


def pin(path):
    raw = Path(path).read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


selection_path = WORK / 'formal-budget-recovery-016/SELECTED_CHECKER.json'
selected = json.loads(selection_path.read_bytes())
assert selected['runtime_identity']['pins']['scripts/formal_support.py'] == '20a8010b47c3d330f4ba07b398413acc9ad77bea5c5f9ecf817963b948ca98f6'
request_path = WORK.parent / 'representation/repair-002/formal-request.json'
request = json.loads(request_path.read_bytes())
output = HERE / 'old-selection-prohibited-output'
assert not output.exists()
try:
    adapter.verify(selected, Path(request['input']['path']).read_bytes(), 'model', request['selections'],
                   json.loads(Path(request['supplied_views']['path']).read_bytes()), None, output)
except adapter.GateError as error:
    refused = {'status': error.status, 'reason': str(error)}
else:
    raise AssertionError('Old checker selection unexpectedly accepted changed support machinery')
assert refused['status'] == 'refused' and 'formal_support.py' in refused['reason'], refused
assert not output.exists()
argv = [sys.executable, '-I', '-S', '-B', str(LEAN / 'scripts/formal_gate.py'), 'identity']
observed = subprocess.run(argv, cwd=REPO, capture_output=True, timeout=30)
(HERE / 'identity-002.stdout').write_bytes(observed.stdout)
(HERE / 'identity-002.stderr').write_bytes(observed.stderr)
assert observed.returncode == 0
current = json.loads(observed.stdout)
old_result = WORK / 'current-formal-016/cold/result.json'
old = json.loads(old_result.read_bytes())['runtime_identity']
sys.path.insert(0, str(LEAN / 'scripts'))
import formal_reuse
assert formal_reuse.compatible(old, current) is False
changed = {name: {'before': old['pins'].get(name), 'after': value}
           for name, value in current['pins'].items() if value != old['pins'].get(name)}
assert set(current['pins']) == set(old['pins'])
assert set(changed) == {'scripts/formal_support.py', 'scripts/runtime_process.py'}, changed
result = {'schema': 'stdo305.support-budget-currentness/1', 'selection': pin(selection_path),
          'request': pin(request_path), 'old_selection_observed': refused, 'output_absent': True,
          'identity_argv': argv, 'identity_returncode': observed.returncode,
          'identity_stdout': pin(HERE / 'identity-002.stdout'), 'identity_stderr': pin(HERE / 'identity-002.stderr'),
          'old_result': pin(old_result), 'owner_compatible': False, 'runtime_pin_delta': changed,
          'standing': 'Actual Graphify verify API refuses old source selection before output or compiler; actual owner compatible() rejects old evidence machinery. Identity reads source/profile pins only; no compiled-support check or proof ran.'}
with (HERE / 'CURRENTNESS_002.json').open('x') as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write('\n')
print(json.dumps({'status': 'expected_stale_refusals', 'observed': refused, 'runtime_pin_delta': changed}))
