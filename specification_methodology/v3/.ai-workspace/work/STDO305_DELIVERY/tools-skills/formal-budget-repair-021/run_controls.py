"""Focused resource/selection controls; no compiler or support establishment."""
from pathlib import Path
import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
import unittest

REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).absolute().parent
LEAN = REPO / 'a_c/build_tenants/lean'
WORK = HERE.parent

def ref(path):
    path = Path(path); raw = path.read_bytes()
    return {'path': path.relative_to(REPO).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def save(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')

spec = importlib.util.spec_from_file_location('selected_gate_controls', LEAN / 'tests/test_formal_gate.py')
tests = importlib.util.module_from_spec(spec); spec.loader.exec_module(tests)

class SelectedControls(tests.FormalGateTests):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(dir=HERE)
        cls.directory = Path(cls.tmp.name)
        cls.model = tests.new_subject(cls.directory / 'subject')
        cls.imported = tests.bridge.import_model(cls.model)

names = ['test_selected_default_and_api_override_reach_timeout_without_claims',
         'test_malformed_limits_refuse_before_effect_or_compiler',
         'test_resource_byte_limit_is_incomplete']
result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(SelectedControls(n) for n in names))
if not result.wasSuccessful():
    raise SystemExit(1)

sys.path.insert(0, str(REPO / 'a_c/build_tenants/graphify/code'))
import ac_formal_gate as adapter
old_path = WORK / 'current-formal-020-preparation/SELECTED_CHECKER.json'
old = json.loads(old_path.read_bytes())
forbidden = HERE / 'old-selection-prohibited-output'
assert not forbidden.exists()
try:
    adapter.verify(old, b'{}', 'model', [], None, None, forbidden)
except adapter.GateError as error:
    refusal = {'status': error.status, 'reason': str(error)}
else:
    raise AssertionError('Changed source accepted an old selected checker')
assert refusal['status'] == 'refused' and not forbidden.exists(), refusal

selected_path = HERE / 'source-proof/SELECTED_CHECKER.json'
argv = [sys.executable, '-B', str(REPO / 'a_c/scripts/ac.py'), 'formal-select',
        '--lean-root', str(LEAN), '--python', sys.executable,
        '--timeout-seconds', '7200', '--output', str(selected_path)]
started = time.time_ns()
selected_run = subprocess.run(argv, cwd=REPO, capture_output=True, timeout=60)
ended = time.time_ns()
(HERE / 'selection.stdout').write_bytes(selected_run.stdout)
(HERE / 'selection.stderr').write_bytes(selected_run.stderr)
save(HERE / 'selection.execution.json', {'argv': argv, 'cwd': str(REPO),
     'returncode': selected_run.returncode, 'started_ns': started, 'ended_ns': ended,
     'elapsed_seconds': (ended-started)/1e9, 'stdout': ref(HERE / 'selection.stdout'),
     'stderr': ref(HERE / 'selection.stderr'), 'producer': ref(REPO / 'a_c/scripts/ac.py'),
     'adapter': ref(REPO / 'a_c/build_tenants/graphify/code/ac_formal_gate.py'),
     'entry': ref(LEAN / 'scripts/formal_gate.py')})
assert selected_run.returncode == 0, selected_run.stderr
selected = json.loads(selected_path.read_bytes())
assert selected['timeout_seconds'] == 7200
changed = {name: {'before': old['runtime_identity']['pins'].get(name), 'after': value}
           for name, value in selected['runtime_identity']['pins'].items()
           if value != old['runtime_identity']['pins'].get(name)}
assert set(changed) == {'scripts/formal_gate.py'}, changed
assert set(selected['runtime_identity']['pins']) == set(old['runtime_identity']['pins'])
bad_limits = [0, -1, True, 1.5, '7200', None]
for value in bad_limits:
    malformed = copy.deepcopy(selected); malformed['timeout_seconds'] = value
    try:
        adapter.validate_config(malformed)
    except adapter.GateError as error:
        assert error.status == 'unsupported'
    else:
        raise AssertionError(('Malformed selector accepted', value))
sys.path.insert(0, str(LEAN / 'scripts'))
import formal_reuse
assert not formal_reuse.compatible(old['runtime_identity'], selected['runtime_identity'])

# Inspect executable call sites, not a parallel plan value. Unchanged cleanup
# and worker effect limits are also visible in the retained exact operator diff.
operator_calls = []
for path in (HERE / 'source-proof/run_current_formal.py', HERE / 'operators/run_current_full_supervised.py'):
    tree = ast.parse(path.read_text())
    waits = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == 'wait'
             and any(k.arg == 'timeout' and isinstance(k.value, ast.Constant) and k.value.value == 7200 for k in node.keywords)]
    assert len(waits) == 1
    operator_calls.append({'source': ref(path), 'actual_process_wait_seconds': 7200})
path = HERE / 'operators/current_context.py'; tree = ast.parse(path.read_text())
for operation in ('contract.preflight', 'dispatch.start'):
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Name) and node.func.id == 'invoke' and node.args
             and isinstance(node.args[0], ast.Constant) and node.args[0].value == operation
             and any(k.arg == 'timeout' and isinstance(k.value, ast.Constant) and k.value.value == 7500 for k in node.keywords)]
    assert len(calls) == 1, operation
    operator_calls.append({'source': ref(path), 'actual_public_operation': operation, 'timeout_seconds': 7500})
save(HERE / 'CONTROLS.json', {'schema': 'stdo305.concrete-budget-controls/1',
     'tests': names, 'tests_run': result.testsRun, 'skipped': len(result.skipped),
     'old_selector': ref(old_path), 'old_selection_refusal': refusal, 'prohibited_output_absent': True,
     'actual_public_selection': ref(selected_path), 'selection_execution': ref(HERE / 'selection.execution.json'),
     'runtime_pin_delta': changed, 'old_runtime_compatible': False,
     'malformed_selector_values_refused': bad_limits, 'operator_callsite_audit': operator_calls,
     'standing': 'Three focused test methods include default/API override, forced incomplete and malformed limits. Actual public formal-select and old-selection refusal executed without a compiler. Operator callsite audit is static; full proof and installed/Context execution remain pending.'})
print(json.dumps({'status': 'focused_controls_passed', 'record': ref(HERE / 'CONTROLS.json'),
                  'runtime_identity': selected['runtime_identity']['sha256']}))
