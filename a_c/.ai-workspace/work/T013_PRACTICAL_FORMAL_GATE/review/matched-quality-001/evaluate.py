"""Independent quality checks on read-and-reviewed neutral disposable copies."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

R = Path(__file__).resolve().parent
W = R.parents[1]
G = W / 'real-use/runtime-preparation-003/execution-002/grading'
E = W / 'real-use/evaluation'
sha = lambda raw: hashlib.sha256(raw).hexdigest()
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as f:
        f.write(json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + '\n')
def reject(value):
    raise ValueError('non-finite')
def unique(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError('duplicate key')
        out[k] = v
    return out
def parse(raw):
    return json.loads(raw.decode('utf-8'), parse_float=Decimal,
                      parse_constant=reject, object_pairs_hook=unique)
def equal(a, b):
    if type(a) in (int, Decimal) and type(b) in (int, Decimal):
        return Decimal(a) == Decimal(b)
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(equal(x, y) for x, y in zip(a, b))
    return a == b
def oracle(raw):
    data = parse(raw)
    status = data['status']
    categories = {'verified': 'verified_claims_reported', 'unsupported': 'unsupported_contract',
                  'incomplete': 'check_incomplete'}
    reasons = {'Insufficient record budget; verified refusal, no truncated projection': 'record_budget_refusal',
               'Supplied Graphify view differs from actual formal result/boundary mapping': 'supplied_view_mismatch',
               'signature: expected object': 'malformed_model'}
    elapsed = (data.get('observations') or {}).get('elapsed_seconds')
    state = 'unknown' if elapsed is None else 'invalid'
    if type(elapsed) in (int, Decimal) and elapsed >= 0:
        state = 'reported'
    return {'schema': 't013.gate-result-report/1',
            'source': {'raw_sha256': sha(raw), 'bytes': len(raw)}, 'reported': data,
            'summary': {'status': status, 'category': categories.get(status, reasons.get(data.get('reason'), 'other_refusal')),
                        'checked_claim_count': len(data['checked_claims']) if 'checked_claims' in data else None,
                        'requested_claim_count': len(data['requested_claims']) if 'requested_claims' in data else None},
            'cost': {'elapsed_seconds': {'state': state, 'value': elapsed if state == 'reported' else None},
                     'tokens': {'state': 'unknown', 'value': None}, 'money_usd': {'state': 'unknown', 'value': None}},
            'standing': {'input_authenticated': False, 'grants_authority': False, 'establishes_semantic_acceptance': False}}
def snapshot(path):
    return {str(p.relative_to(path)): sha(p.read_bytes()) for p in sorted(path.rglob('*')) if p.is_file()}

pins = json.loads((G / 'INPUT-PINS.json').read_bytes())
assert sha((G / 'INPUT-PINS.json').read_bytes()) == '335e9b465d1fbe5a0acf632b09256e03def0055f49c335972646b1426d61cfff'
origin_pins = json.loads((W / 'real-use/PINS.json').read_bytes())
assert sha((W / 'real-use/PINS.json').read_bytes()) == '623a138c2cbf198a08c96c2481d29953cd22c5d606851b8b0f64ed18596b73fd'
for name, record in origin_pins['files'].items():
    if name.startswith('evaluation/'):
        raw = (W / 'real-use' / name).read_bytes()
        assert sha(raw) == record['sha256'] and len(raw) == record['bytes']
hidden = parse((E / 'CASES.json').read_bytes())
cases = []
for c in hidden['cases']:
    cases.append({'id': c['id'], 'group': 'predeclared-hidden',
                  'raw': (E / c['input']).read_bytes(), 'exit': c['expected_exit'],
                  'source': str((E / c['input']).relative_to(W)), 'reason': 'Unchanged predeclared evaluator input'})
for p in sorted((G / 'A/inputs/examples').glob('*.json')):
    cases.append({'id': 'PUBLIC-' + p.stem, 'group': 'supplied-example', 'raw': p.read_bytes(),
                  'exit': 0, 'source': str(p.relative_to(G)), 'reason': 'Required genuine/authored shared examples'})
def add(name, raw, expected=0, reason='Source-derived TASK discriminator'):
    cases.append({'id': name, 'group': 'independent', 'raw': raw, 'exit': expected, 'reason': reason})
def authored(status='verified', **fields):
    return json.dumps({'schema': 'a_c.formal-gate.result/1', 'status': status, **fields}, ensure_ascii=False).encode()
for status in ('verified', 'refused', 'unsupported', 'incomplete'):
    add('I-minimal-' + status, authored(status))
for i, value in enumerate((None, 0, 0.0, True, False, -1, '3', [], {})):
    add('I-elapsed-' + str(i), authored(observations={'elapsed_seconds': value}, tokens=99, money_usd=10))
add('I-stage-only', authored(observations={'stages': [{'seconds': 100}]}, tokens={'reported': 99}))
for reason in ('signature: expected object ', 'SIGNATURE: EXPECTED OBJECT',
               'Insufficient record budget; verified refusal, no truncated projection additional'):
    add('I-exact-reason-' + str(len(cases)), authored('refused', reason=reason))
nullable = {k: None for k in ('reason', 'request_sha256', 'selections', 'inputs', 'model',
                            'runtime_identity', 'evidence', 'observations', 'context_binding')}
add('I-null-fields-extensions', authored(**nullable, checked_claims=[], requested_claims=['unchecked'],
    limits=['still unresolved'], extension={'ordered': [None, False, 0, True, 'Ω', {'id': ' Case/Sensitive '}],
                                          'integer': 9007199254740993}))
for key in ('reason', 'request_sha256', 'checked_claims', 'requested_claims', 'limits', 'inputs',
            'model', 'runtime_identity', 'evidence', 'observations', 'context_binding', 'selections'):
    add('I-wrong-type-' + key, authored(**{key: False}), 2)
for key in ('checked_claims', 'requested_claims', 'limits'):
    add('I-string-array-' + key, authored(**{key: [None]}), 2)
for name, raw in [('utf8', b'\xff'), ('root-list', b'[]'), ('root-null', b'null'),
                  ('missing-schema', b'{"status":"verified"}'), ('missing-status', b'{"schema":"a_c.formal-gate.result/1"}'),
                  ('status-list', authored(status=[])), ('status-number', authored(status=1))]:
    add('I-invalid-' + name, raw, 2)
for name, token in [('Infinity', 'Infinity'), ('negative-Infinity', '-Infinity')]:
    add('I-nonfinite-' + name, ('{"schema":"a_c.formal-gate.result/1","status":"verified","x":' + token + '}').encode(), 2)
add('I-escaped-duplicate', b'{"schema":"a_c.formal-gate.result/1","status":"verified","x":{"a":1,"\\u0061":2}}', 2)
for name, number in [('precision', '0.123456789012345678901'), ('negative-underflow', '-1e-400'),
                     ('positive-underflow', '1e-400'), ('finite-large', '1e400')]:
    add('I-number-' + name, ('{"schema":"a_c.formal-gate.result/1","status":"verified","x":' + number + ',"observations":{"elapsed_seconds":' + number + '}}').encode(),
        reason='Finite JSON values and negative/zero cost distinctions must survive parsing and reporting')
# This short input tests the Decimal adapter exception boundary without allocating
# the represented magnitude. It is assessed separately from ordinary numeric fidelity.
add('I-number-decimal-exponent-boundary', b'{"schema":"a_c.formal-gate.result/1","status":"verified","x":1e9999999999999999999}',
    reason='Short finite JSON token beyond Decimal exponent capacity; check reporting/error boundary')

case_manifest = []
for c in cases:
    file = R / 'case-inputs' / (c['id'] + '.json')
    file.parent.mkdir(exist_ok=True)
    file.write_bytes(c['raw'])
    record = {k: v for k, v in c.items() if k != 'raw'}
    record.update(input_path=str(file.relative_to(R)), raw_sha256=sha(c['raw']), bytes=len(c['raw']))
    case_manifest.append(record)
save(R / 'CASE-MANIFEST.json', {'cases': case_manifest, 'hidden_cases_sha256': sha((E / 'CASES.json').read_bytes()),
    'oracle': 'TASK-derived exact field oracle with Decimal numeric comparison; no candidate imports or self-test assertions',
    'scope': 'Additional cases are reviewer-authored test data, not gate receipts'})

env = os.environ.copy()
env.pop('PYTHONPATH', None)
env['PYTHONDONTWRITEBYTECODE'] = '1'
tmp = R / 'tmp'; tmp.mkdir()
env['TMPDIR'] = str(tmp)
results = {}
for arm in ('A', 'B'):
    original = snapshot(G / arm)
    assert original == {k: v['sha256'] for k, v in pins['trees'][arm].items()}
    copy = R / 'copies' / arm
    shutil.copytree(G / arm, copy)
    before = snapshot(copy)
    arm_results = []
    for c in cases:
        argv = [sys.executable, '-I', '-S', '-B', str(copy / 'gate_report.py'), str(R / 'case-inputs' / (c['id'] + '.json'))]
        start = time.monotonic()
        process = subprocess.run(argv, cwd=copy, env=env, capture_output=True, timeout=5)
        elapsed = time.monotonic() - start
        logdir = R / 'runs' / arm / c['id']; logdir.mkdir(parents=True)
        (logdir / 'stdout').write_bytes(process.stdout); (logdir / 'stderr').write_bytes(process.stderr)
        failures = []
        if process.returncode != c['exit']:
            failures.append('exit: expected ' + str(c['exit']) + ', actual ' + str(process.returncode))
        if c['exit'] == 2:
            if process.stdout: failures.append('invalid input produced stdout')
            if not process.stderr: failures.append('invalid input lacked stderr')
            if b'Traceback' in process.stderr: failures.append('unhandled traceback')
        elif process.returncode == 0:
            if process.stderr: failures.append('valid report wrote stderr')
            if not process.stdout.endswith(b'\n') or process.stdout.count(b'\n') != 1:
                failures.append('output is not one JSON line plus newline')
            actual = parse(process.stdout)
            expected = oracle(c['raw'])
            if actual.keys() != expected.keys(): failures.append('top-level field set')
            for field in expected:
                if field not in actual or not equal(actual[field], expected[field]):
                    failures.append(field + ' differs from TASK oracle')
            hidden_case = next((h for h in hidden['cases'] if h['id'] == c['id']), None)
            if hidden_case:
                for k, field in [('expected_summary', 'summary'), ('expected_cost', 'cost'), ('standing', 'standing')]:
                    if k in hidden_case and not equal(actual[field], hidden_case[k]):
                        failures.append('predeclared ' + k + ' mismatch')
        record = {'id': c['id'], 'group': c['group'], 'argv': argv, 'cwd': str(copy), 'exit': process.returncode,
                  'expected_exit': c['exit'], 'seconds': elapsed, 'stdout_sha256': sha(process.stdout),
                  'stderr_sha256': sha(process.stderr), 'status': 'FAIL' if failures else 'PASS', 'failures': failures}
        save(logdir / 'receipt.json', record)
        arm_results.append(record)
    for name, args in [('no-argument', []), ('missing-file', [str(copy / 'absent-input.json')]),
                       ('extra-argument', [str(copy / 'inputs/examples/verified.json'), 'extra'])]:
        argv = [sys.executable, '-I', '-S', '-B', str(copy / 'gate_report.py'), *args]
        start = time.monotonic(); process = subprocess.run(argv, cwd=copy, env=env, capture_output=True, timeout=5)
        d = R / 'runs' / arm / ('CLI-' + name); d.mkdir(parents=True)
        (d / 'stdout').write_bytes(process.stdout); (d / 'stderr').write_bytes(process.stderr)
        okay = process.returncode == 2 and not process.stdout and bool(process.stderr) and b'Traceback' not in process.stderr
        record = {'id': 'CLI-' + name, 'group': 'independent', 'argv': argv, 'exit': process.returncode,
                  'seconds': time.monotonic() - start, 'stdout_sha256': sha(process.stdout), 'stderr_sha256': sha(process.stderr),
                  'status': 'PASS' if okay else 'FAIL'}
        save(d / 'receipt.json', record); arm_results.append(record)
    assert snapshot(copy) == before, 'CLI changed files'
    wrapper = "import sys,unittest;sys.path.insert(0,sys.argv[1]);s=unittest.defaultTestLoader.discover(sys.argv[1],pattern='test_gate_report.py');r=unittest.TextTestRunner(verbosity=2).run(s);sys.exit(0 if r.wasSuccessful() else 1)"
    argv = [sys.executable, '-I', '-S', '-B', '-c', wrapper, str(copy)]
    start = time.monotonic(); tests = subprocess.run(argv, cwd=copy, env=env, capture_output=True, timeout=30)
    td = R / 'runs' / arm / 'worker-tests'; td.mkdir(parents=True)
    (td / 'stdout').write_bytes(tests.stdout); (td / 'stderr').write_bytes(tests.stderr)
    test_receipt = {'argv': argv, 'exit': tests.returncode, 'seconds': time.monotonic() - start,
                    'stdout_sha256': sha(tests.stdout), 'stderr_sha256': sha(tests.stderr),
                    'scope': 'Additional self-test reproduction, not independent acceptance oracle; frozen scratch directory preserved'}
    save(td / 'receipt.json', test_receipt)
    assert snapshot(copy) == before and snapshot(G / arm) == original
    results[arm] = {'cases': arm_results, 'worker_tests': test_receipt, 'unchanged_copy_and_frozen_input': True,
        'pass': sum(c['status'] == 'PASS' for c in arm_results), 'fail': sum(c['status'] == 'FAIL' for c in arm_results)}
result = {'schema': 'a_c.T013.independent-neutral-quality-execution/1', 'interpreter': sys.executable,
          'python_version': sys.version, 'results': results, 'operational_mapping_costs_transcripts_read': False,
          'network_install_build_model_agent_calls': 0, 'candidate_repairs': 0,
          'note': 'Wall durations are independent reviewer check costs only; no actual Worker operational ledger was read'}
save(R / 'RESULTS.json', result)
print(json.dumps({arm: {'pass': v['pass'], 'fail': v['fail'], 'worker_tests_exit': v['worker_tests']['exit'],
    'failed_cases': [{'id': c['id'], 'failures': c.get('failures')} for c in v['cases'] if c['status'] != 'PASS']} for arm, v in results.items()}, sort_keys=True))
