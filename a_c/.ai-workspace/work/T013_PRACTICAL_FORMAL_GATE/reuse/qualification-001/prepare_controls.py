"""Create copied public adversarial evidence only inside this qualification run.

No production source, original public bundle, origin key, or private entry is
changed. Refreshing public hashes deliberately tests authenticated binding.
"""
from pathlib import Path
import copy
import hashlib
import json
import shutil

Q = Path(__file__).resolve().parent
SOURCE = Q / 'small-cold'
CONTROLS = Q / 'controls'


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True,
                               indent=2, allow_nan=False) + '\n', encoding='utf-8')


def inventory(directory):
    result = {}
    for path in sorted(directory.rglob('*')):
        assert not path.is_symlink(), path
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = sha(path)
    return result


def refresh(directory, result):
    manifest = read(directory / 'manifest.json')
    manifest['members'] = {name: sha(directory / name)
                           for name in manifest['members']}
    write(directory / 'manifest.json', manifest)
    result['evidence'] = {'manifest_sha256': sha(directory / 'manifest.json'),
                          'members': manifest['members']}
    write(directory / 'result.json', result)


assert not CONTROLS.exists()
before = inventory(SOURCE)
CONTROLS.mkdir()
descriptions = []
for name in ('omitted-residual', 'runtime-tamper', 'typed-context', 'stale-pin'):
    destination = CONTROLS / name
    shutil.copytree(SOURCE, destination, copy_function=shutil.copy2)
    assert inventory(destination) == before
    result = read(destination / 'result.json')
    original = read(destination / 'request.json')
    replay = read(destination / 'replay-request.json')
    record = {'control': name, 'public_copy': str(destination),
              'expected_status': 'refused', 'expected_exit': 2}
    if name == 'omitted-residual':
        views = read(destination / 'supplied-views.json')
        view = views[0]
        assert len(view['populations']['residuals']) == 1
        residual = view['populations']['residuals'][0]['id']
        assert residual in view['included']
        assert view['boundary']['unresolved_residuals'] == [residual]
        view['populations']['residuals'] = []
        view['boundary']['unresolved_residuals'] = []
        view['included'].remove(residual)
        view['excluded'].append(residual)
        view['excluded'].sort()
        write(destination / 'supplied-views.json', views)
        raw_hash = sha(destination / 'supplied-views.json')
        original['supplied_views']['raw_sha256'] = raw_hash
        replay['supplied_views']['raw_sha256'] = raw_hash
        result['inputs']['supplied_views']['raw_sha256'] = raw_hash
        result['inputs']['supplied_views']['bytes'] = (destination / 'supplied-views.json').stat().st_size
        record['mutation'] = 'Remove unresolved residual from included identities, residual population, and unresolved boundary; move its identity to excluded.'
        record['omitted_identity'] = residual
    elif name == 'runtime-tamper':
        actual = read(destination / 'actual-runtime.log')
        value = actual['views'][0]['projection']['records'][0]
        payload = json.loads(value['payload'])
        payload['qualification_tamper'] = True
        value['payload'] = canonical(payload).decode()
        write(destination / 'actual-runtime.log', actual)
        record['mutation'] = 'Alter one projected runtime record payload while retaining well-formed JSON.'
        record['changed_identity'] = value['identity']
    elif name == 'typed-context':
        assert type(original['context_binding']['activation_identity']['trial_ordinal']) is int
        assert original['context_binding']['activation_identity']['trial_ordinal'] == 1
        original['context_binding']['activation_identity']['trial_ordinal'] = True
        replay['context_binding']['activation_identity']['trial_ordinal'] = True
        result['context_binding'] = copy.deepcopy(original['context_binding'])
        record['mutation'] = 'Replace integer trial_ordinal 1 with boolean true in original/replay requests and saved context binding.'
        record['canonical_request_changed'] = canonical(original) != canonical(read(SOURCE / 'request.json'))
        assert record['canonical_request_changed']
    else:
        result['runtime_identity']['pins']['scripts/gate_codegen.py'] = '0' * 64
        result['runtime_identity']['sha256'] = hashlib.sha256(canonical(result['runtime_identity']['pins'])).hexdigest()
        record['mutation'] = 'Replace non-origin deciding generator source pin and recompute aggregate runtime identity.'
    if name in ('omitted-residual', 'typed-context'):
        write(destination / 'request.json', original)
        write(destination / 'replay-request.json', replay)
        result['request_sha256'] = hashlib.sha256(canonical(original)).hexdigest()
    refresh(destination, result)
    after = inventory(destination)
    record['changed_public_files'] = {name: {'before': before[name], 'after': after[name]}
                                      for name in before if before[name] != after[name]}
    record['refreshed_public_hashes'] = True
    record['expected_reason'] = ('Evidence verifier/proof/profile pins are stale'
                                 if name == 'stale-pin' else 'Exact local establishment binding changed')
    descriptions.append(record)

typed = read(Q / 'small-request.json')
typed['selections'][0]['budget_records'] = True
write(CONTROLS / 'boolean-budget-request.json', typed)
descriptions.append({'control': 'boolean-budget', 'request': str(CONTROLS / 'boolean-budget-request.json'),
                     'mutation': 'Set budget_records to boolean true in a fresh public request.',
                     'expected_status': 'refused', 'expected_exit': 2,
                     'expected_reason': 'Budget must be a nonnegative record count or null'})
assert inventory(SOURCE) == before, 'Original cold public bundle changed'
write(Q / 'CONTROLS-PREPARED.json', {
    'schema': 'a_c.T013.public-controls-preparation/1',
    'source_bundle': str(SOURCE), 'original_bundle_members': before,
    'original_bundle_unchanged': True, 'private_entry_mutation': False,
    'production_source_mutation': False, 'controls': descriptions})
print(json.dumps({'prepared': len(descriptions), 'original_bundle_unchanged': True}))
