"""Bounded source inspection only; no product imports or runtime operations.

The 19 MB public proof-support manifest and 260 MB native binary are not re-read.
Their exact selected hashes are cross-checked as records; live currentness and
actual execution remain obligations. Only this review's output may be written.
"""
import ast
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
W = HERE.parents[1]
PRODUCT = W.parents[2]
CHECKOUT = PRODUCT.parent
PKG = W / 'package/selection-001'
RUN = W / 'real-use/runtime-preparation-002'
PREVIOUS = W / 'real-use/runtime-preparation-001'
checks = []
omitted_byte_rechecks = []


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_bytes())


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def check(name, value):
    assert value, name
    checks.append({'condition': name, 'outcome': 'passed'})


for folder, closure_sha, pins_sha in (
    (PKG, '8fb08dac5489e39b280547ce5dfd56185526e0ff4d6631773f4b3ec85a907b9e', '9c6be557640a75cdedc0ef37a2a112845f45fcd59ec2c50f2e835bbb7b114299'),
    (RUN, '3ddc0345172a81c8cf511570c2c183ff600d8c28436947e95e62e9491cf30e33', '21e5ff740361f2b825293e433f1b7322c0e15dd0ee6c3c1da129e40e99a26f76')):
    check(str(folder.relative_to(W)) + ' exact closure and pins', sha(folder / 'CLOSED.json') == closure_sha and sha(folder / 'PINS.json') == pins_sha)
    check(str(folder.relative_to(W)) + ' all preparation members', all(sha(folder / n) == h for n, h in read(folder / 'PINS.json')['members'].items()))
check('prior package assessment conserved', sha(W / 'review/package-transport-final-001/CLOSED.json') == '4a460c957bca7dba55ba2ed6b50407dd65cbcc8fd845d7f2d943139d8954b3a7')
check('prior runtime preparation assessment conserved', sha(W / 'review/runtime-preparation-001/CLOSED.json') == '516ecc52f04ae2507b1bb0a0fdf6732d7fae2895131aacae314850172f89d03b')
for name in ('package_source.py', 'test_package_source.py'):
    check('reviewed packager source conserved: ' + name, (PKG / name).read_bytes() == (W / 'package/repair-002' / name).read_bytes())
for name in ('prepare_runtime.py', 'request_builder.py', 'compare_contexts.py'):
    check('reviewed runtime builder conserved: ' + name, (RUN / name).read_bytes() == (PREVIOUS / name).read_bytes())

manifest = read(PKG / 'SOURCE_PACKAGE.json')
plan = read(PKG / 'INVENTORY_PLAN.json')
prior_plan = read(W / 'package/repair-002/INVENTORY_PLAN.json')
files = {row['path']: row for row in manifest['files']}
prior_paths = {row['path'] for row in prior_plan['entries']}
added = set(files) - prior_paths
check('65 exact destinations and only two intended additions', len(files) == len(manifest['files']) == 65 and prior_paths <= set(files) and added == {'a_c/build_tenants/lean/scripts/formal_reuse.py', 'a_c/build_tenants/lean/tests/test_formal_reuse.py'})
check('no case-colliding destination', len({n.casefold() for n in files}) == len(files))
check('manifest exactly realizes explicit plan', [{k: row[k] for k in ('source', 'path', 'role')} for row in manifest['files']] == plan['entries'])
check('declared payload size', sum(row['bytes'] for row in files.values()) == 22272112)
for row in files.values():
    for name in (row['path'], row['source']):
        parts = Path(name).parts
        check('safe public member ' + name, not Path(name).is_absolute() and not any(x in ('.', '..', '.cache', '.lake', '.toolchain', 'formal-origin-v1') for x in map(str.casefold, parts)) and not name.casefold().endswith(('.key', '.olean', '.ir')))
    path = CHECKOUT / row['source']
    check('regular current source length ' + row['path'], path.is_file() and not path.is_symlink() and path.stat().st_size == row['bytes'])
    if row['bytes'] <= 1000000:
        check('current source bytes ' + row['path'], sha(path) == row['sha256'])
    else:
        omitted_byte_rechecks.append({'path': row['source'], 'sha256': row['sha256'], 'bytes': row['bytes'], 'reason': 'Large public support map: selected record cross-check only; no duplicate support verification during benchmark.'})
for directory in plan['closed_directories']:
    actual = {str(p.relative_to(CHECKOUT)) for p in (CHECKOUT / directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    expected = {row['source'] for row in files.values() if row['source'].startswith(directory + '/')}
    check('closed namespace ' + directory, actual == expected)

freeze = read(PKG / 'FREEZE.json')
full = freeze['runtime_identity']
public_pins = {k: v for k, v in full['pins'].items() if k != '.cache/formal-origin-v1/selection.json'}
portable = {'sha256': hashlib.sha256(canonical(public_pins)).hexdigest(), 'pins': public_pins}
check('source freeze exact and source-only', manifest['freeze'] == freeze and manifest['freeze_sha256'] == hashlib.sha256(canonical(freeze)).hexdigest() and 'qualification pending' in freeze['selection_ref'])
check('fixed origin-only portable identity', len(full['pins']) == 25 and len(public_pins) == 24 and portable == manifest['portable_runtime_identity'] and portable['sha256'] == '07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601')
check('full identity aggregate', hashlib.sha256(canonical(full['pins'])).hexdigest() == full['sha256'] == '065648e6cc971be7edc75c1fa7b0428351357fe312146059b71fb788842313a7')
check('all 24 public deciding pins at original payload coordinates', all(files['a_c/build_tenants/lean/' + n]['sha256'] == h for n, h in public_pins.items()))
check('public support identity conserved from independently reviewed scale', public_pins['profiles/proof-support-v1.json'] == '7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363')
check('package and runtime use same public checker bytes', (PKG / 'CHECKER.json').read_bytes() == (RUN / 'CHECKER.json').read_bytes())
checker = read(RUN / 'CHECKER.json')
check('selected checker exact', sha(RUN / 'CHECKER.json') == '9203ff1e38087e0d9bf668f24fc796286dd115e3ee1fcecc527e91ddb80bf341' and checker['runtime_identity'] == full)
gate_tree = ast.parse((PRODUCT / 'build_tenants/lean/scripts/formal_gate.py').read_bytes())
script_value = next(n.value for n in gate_tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SCRIPT_FILES' for t in n.targets))
assert isinstance(script_value, ast.Call) and isinstance(script_value.func, ast.Name) and script_value.func.id == 'frozenset'
assert isinstance(script_value.args[0], ast.GeneratorExp)
script_names = frozenset(n + '.py' for n in ast.literal_eval(script_value.args[0].generators[0].iter))
check('exact eleven-script CLI namespace fully packaged', len(script_names) == 11 and {'a_c/build_tenants/lean/scripts/' + n for n in script_names} == {n for n in files if n.startswith('a_c/build_tenants/lean/scripts/')})
new_tree = ast.parse((PRODUCT / 'build_tenants/lean/scripts/formal_reuse.py').read_bytes())
stdlib_new = {a.name.split('.')[0] for n in ast.walk(new_tree) if isinstance(n, ast.Import) for a in n.names} | {n.module.split('.')[0] for n in ast.walk(new_tree) if isinstance(n, ast.ImportFrom) and n.module}
check('new helper introduces only inspected stdlib imports', stdlib_new <= {'__future__', 'hashlib', 'hmac', 'json', 'os', 're', 'secrets', 'stat', 'pathlib'})

runtime_manifest = read(RUN / 'templates-001/MANIFEST.json')
selection = read(RUN / 'templates-001/execution-selection.json')
owner = read(RUN / 'owner-binding/SELECTED.json')
receipt = read(RUN / 'owner-binding/RECEIPT.json')
ticket = PRODUCT / '.ai-workspace/tickets/active/T-013-practical-formal-gate.md'
definition = PRODUCT / 'stdo_a_c.json'
check('actual Product and current T013 owner sources', sha(ticket) == receipt['ticket_after_sha256'] == 'c5c8ed56ebfef3f51406be4b63d7d1fd3976de294ce0a64c801ea3f4da44fefc' and sha(definition) == receipt['definition_sha256'])
start, end = receipt['selected_owner_lines']
selected_bytes = ''.join(ticket.read_text().splitlines(keepends=True)[start - 1:end]).encode()
check('actual selected owner lines and exact content', (start, end) == (149, 225) and json.loads(selected_bytes) == owner and hashlib.sha256(selected_bytes).hexdigest() == receipt['selected_json_sha256'])
check('actual Product locator resolves owner ticket', (PRODUCT / read(definition)['reference_frame_bases'][0]['authority'][6].split('#')[0]).resolve() == ticket.resolve())
check('owner mechanism implementation is current reviewed Core', owner['mechanism']['implementation_sha256'] == sha(PRODUCT / 'build_tenants/graphify/code/ac_support_core.py') == '024470f433a891d5ecdef3f4e08e5d8cfa5b66df16bf36270d2865d6b1450b5b')
old_owner = read(PREVIOUS / 'owner-binding/SELECTED.json')
old_owner['mechanism']['implementation_sha256'] = owner['mechanism']['implementation_sha256']
check('owner scope and result surface otherwise conserved', old_owner == owner)
check('reviewed TASK and PROTOCOL conserved', sha(W / 'real-use/TASK.md') == owner['scope']['task_sha256'] == '33e08813021b43a259dc72aa35f904f82b370de25faff64488f29ee4d4495829' and sha(W / 'real-use/PROTOCOL.md') == owner['scope']['protocol_sha256'] == '547a73826a8bd28721661361106d5a8e53844ca3a3a8b2a10dd5b66d7a2ae4f6')
check('pending templates do not claim executable selection', runtime_manifest['template_only'] is True and selection['state'] == 'pending' and selection['maximum_invocations_per_arm'] == 1 and selection['automatic_retry'] is False)
check('canonical checker configuration selected', selection['checker_config_sha256'] == hashlib.sha256(canonical(checker)).hexdigest() and runtime_manifest['checker_config'] == checker)
check('current support source pins', all(sha(n) == h for n, h in runtime_manifest['source_pins'].items()))

def refs(value):
    if isinstance(value, dict):
        if set(value) == {'engine', 'root', 'path', 'object', 'sha256', 'selector'}:
            yield value
        for child in value.values():
            yield from refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from refs(child)

arm_data = {}
source_ref_count = 0
for arm in ('ungated', 'gated'):
    folder = RUN / 'templates-001' / arm
    policy, shape, packet, context, actor, instruction = (read(folder / n) for n in ('policy.template.json', 'policy.shape-only.json', 'packet.json', 'context.request.json', 'actor-plan.json', 'return-instructions.json'))
    roots = policy['sources']; workspace = Path('/private/tmp/ac-t013-report-001') / arm
    check(arm + ' exact intended fresh workspace still absent', roots['task']['path'] == actor['cwd'] == str(workspace) and not workspace.exists())
    check(arm + ' role and null acceptance/publication authorities', packet['actor_authority']['role'] == 'Worker' and packet['actor_authority']['actor_id'] == 't013-report-' + arm + '-worker-001' and all(packet['actor_authority'][k] is None for k in ('decision', 'acceptance', 'publication')))
    check(arm + ' shape policy cannot execute or admit', shape['executors'] == shape['grants'] == {} and 'formal_gate' not in shape and shape['principals']['executive']['operations'] == ['tools.describe', 'source.read'])
    check(arm + ' exact current checker and required-target treatment', policy['formal_gate'] == {'checker': checker, 'required_targets': ['worker'] if arm == 'gated' else []})
    check(arm + ' owner result and transport paths preserved', policy['evidence_root'] == owner['result_surface']['root'] and actor['evidence_directory'] == str(Path(owner['result_surface']['root']).parent / 'actor-transports' / packet['actor_authority']['actor_id']))
    check(arm + ' explicit actor and supervisor bounds', actor['limits'] == {'max_input_bytes': 2097152, 'max_output_bytes': 16777216, 'termination_grace_ms': 2000, 'timeout_ms': 900000} and policy['executors']['actor']['settings']['timeout_ms'] == 1000000)
    check(arm + ' native executable and exact plan/stdin route', policy['executors']['actor']['stdin_mode'] == 'context-utf8' and '--ignore-user-config' in actor['argv'] and '--ephemeral' in actor['argv'] and actor['argv'][-1] == '-' and actor['dependencies'][0]['path'] == str(folder / 'return.schema.json') and actor['dependencies'][0]['sha256'] == sha(folder / 'return.schema.json'))
    check(arm + ' pending selection reaches actual executor predicate', policy['executors']['actor']['settings']['execution_selection'] == selection and policy['predicates']['executive-selected']['expression']['args'][1] == {'literal': 'selected'})
    seen = set()
    for ref in refs([policy, context]):
        key = canonical(ref)
        if key in seen: continue
        seen.add(key); source_ref_count += 1
        base = Path(roots[ref['root']]['path']); path = base / ref['path']
        allowed = any(ref['path'] == s['path'] or (s['kind'] == 'directory' and ref['path'].startswith(s['path'] + '/')) for s in roots[ref['root']]['read_scope'])
        check(arm + ' source declared within actual root/scope: ' + ref['path'], allowed and not Path(ref['path']).is_absolute() and '..' not in Path(ref['path']).parts)
        if path.stat().st_size <= 1000000:
            check(arm + ' source raw pin: ' + ref['path'], sha(path) == ref['sha256'])
        else:
            omitted_byte_rechecks.append({'path': str(path), 'sha256': ref['sha256'], 'bytes': path.stat().st_size, 'reason': 'Large pinned model/native subject; source coordinate checked, live acquisition remains required.'})
    arm_data[arm] = {'prepared': [s for s in context['arguments']['sources'] if s['root'] == 'prepared'], 'models': context['arguments']['models'], 'instruction': instruction['instruction']}
check('both arms have exactly equal substantive references, view selection and instructions', arm_data['ungated'] == arm_data['gated'])
model_selection = read(W / 'real-use/shared/MODEL_SELECTION.json')
view = read(W / 'real-use/shared/model-view.json')
check('frozen 29-record actual-view bytes conserved', sha(W / 'real-use/shared/model-view.json') == model_selection['view']['raw_sha256'] == '5b106c80072d06dc407dc06673d68730312cecb9535ff0aa1e99d5597c2a0d79' and len(view) == 1 and len(view[0]['included']) == 29)
delivery = read(W / 'real-use/transport/DELIVERY_INPUTS.json')['files']
check('all exact delivery inputs remain current and task-local', all(sha(W / 'real-use' / row['from']) == row['sha256'] and row['to'].startswith('inputs/') and '..' not in Path(row['to']).parts for row in delivery))
check('two named actual calls only', [(x['arm'], x['count']) for x in owner['scope']['actor_calls']] == [('ungated', 1), ('gated', 1)] and owner['scope']['bounds']['automatic_retry'] is False)

# Extract only the unchanged builder's refusal guard; never import preparation.
for name, function_name, args in (('request_builder.py', 'build', (RUN / 'templates-001', 'ungated', 'context.assemble')),
                                  ('compare_contexts.py', 'compare', (RUN / 'templates-001', {}))):
    tree = ast.parse((RUN / name).read_bytes())
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function_name)
    scope = {'prep': SimpleNamespace(read=lambda path: runtime_manifest)}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(RUN / name), 'exec'), scope)
    try:
        scope[function_name](*args)
    except ValueError as exc:
        check('actual pending guard: ' + name, 'template' in str(exc).lower() or 'finalized' in str(exc).lower())
    else:
        raise AssertionError('Pending guard accepted: ' + name)

print(json.dumps({'schema': 'a_c.independent-pre-execution-source-checks/1', 'checks': checks,
                  'count': len(checks), 'source_ref_count': source_ref_count,
                  'omitted_large_byte_rechecks': omitted_byte_rechecks,
                  'runtime_or_origin_calls': 0, 'operation_grant': False,
                  'scope': 'Source records, bounded small-file hashes, path/namespace metadata and two extracted pending refusal guards; no actual Context, preflight, proof, actor, archive or support verification.'}, indent=2, sort_keys=True))
