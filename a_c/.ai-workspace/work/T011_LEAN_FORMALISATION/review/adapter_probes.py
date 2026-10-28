"""Independent bounded adapter review; writes only its adjacent result file."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('/Users/jim/src/apps/specification_methodology')
TENANT = ROOT / 'a_c/build_tenants/lean'
spec = importlib.util.spec_from_file_location('reviewed_adapter', TENANT / 'scripts/import_fixture.py')
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)
FAMILIES = ('objects', 'relations', 'constraints', 'latitude', 'residuals', 'traversals', 'transformations', 'judgments')
VARIANTS = {'objects': ('sorts', 'sort'), 'relations': ('relation_kinds', 'kind'),
            'constraints': ('constraint_kinds', 'kind'), 'residuals': ('residual_kinds', 'kind'),
            'judgments': ('judgment_kinds', 'kind')}
results = []


def record(name, detail):
    results.append({'probe': name, 'result': 'passed', 'detail': detail})


def refused(name, thunk):
    try:
        thunk()
    except adapter.Refusal as exc:
        record(name, str(exc))
        return
    raise AssertionError(name + ': unexpected success')


def independent_mapping(source):
    records = [(family, ordinal, value) for family in FAMILIES
               for ordinal, value in enumerate(source['populations'][family])]
    positions = {value['id']: index for index, (_, _, value) in enumerate(records)}
    refs = []

    def follow(value, schema, path, owner):
        if schema['type'] == 'ref':
            refs.append({'owner': owner, 'path': path, 'target': positions.get(value, value),
                         'governing': schema['governing'], 'domain': schema['domain'], 'schema': schema})
        elif schema['type'] == 'array':
            for ordinal, item in enumerate(value):
                follow(item, schema['items'], path + [ordinal], owner)
        elif schema['type'] == 'object':
            for field, field_schema in schema['fields'].items():
                follow(value[field], field_schema, path + [field], owner)

    definition = source['signature']['definition']
    for index, (family, _, value) in enumerate(records):
        schema = dict(definition['fields'][family])
        if family in VARIANTS:
            group, selector = VARIANTS[family]
            schema.update(definition[group][value[selector]])
        for field, field_schema in schema.items():
            follow(value[field], field_schema, [field], index)
    edges = {(r['owner'], r['target']) for r in refs if r['governing'] and type(r['target']) is int}
    required_kinds = source['dependency_contract']['required_relation_kinds']
    for index, (family, _, value) in enumerate(records):
        if family == 'relations' and value['kind'] in required_kinds:
            if value['source'] in positions:
                edges.add((positions[value['source']], index))
                edges.add((index, positions[value['source']]))
            if value['target'] in positions:
                edges.add((index, positions[value['target']]))
        if family in ('constraints', 'latitude', 'residuals'):
            for subject in [value['subject']] if family == 'residuals' else value['applies_to']:
                if subject in positions:
                    edges.add((positions[subject], index))
    return records, refs, edges


for fixture in ('stdo-3.0.2', 'toy'):
    source = json.loads((TENANT / 'fixtures' / fixture / 'MODEL.json').read_text())
    imported = adapter.import_model(source)
    records, refs, edges = independent_mapping(source)
    assert edges == {tuple(edge) for edge in imported['edges']}
    key = lambda x: json.dumps(x, sort_keys=True, ensure_ascii=False)
    assert sorted(map(key, refs)) == sorted(map(key, imported['references']))
    assert imported['envelope'] == {key: value for key, value in source.items() if key != 'populations'}
    for index, (family, ordinal, value) in enumerate(records):
        assert imported['records'][index] == {'index': index, 'family': family, 'ordinal': ordinal, 'record': value}
    record(fixture + ': independent source mapping', {'records': len(records), 'references': len(refs), 'edges': len(edges)})

    seeds = [4, 7] if fixture == 'stdo-3.0.2' else [11, 13]
    expected = set(seeds)
    while True:
        next_set = expected | {target for owner, target in edges if owner in expected}
        if next_set == expected:
            break
        expected = next_set
    projection = adapter.closure_certificate(imported, seeds, len(expected))
    assert projection['included'] == sorted(expected)
    assert projection['excluded'] == sorted(set(range(len(records))) - expected)
    residual_indices = {i for i, (family, _, _) in enumerate(records) if family == 'residuals'}
    assert set(projection['boundary']['retained_residuals']) == residual_indices & expected
    assert set(projection['boundary']['excluded_residuals']) == residual_indices - expected
    record(fixture + ': independent multiseed closure and residual partition', {'seeds': seeds, 'included': sorted(expected)})
    refused(fixture + ': one below exact local-record budget', lambda: adapter.closure_certificate(imported, seeds, len(expected) - 1))

    changed = copy.deepcopy(source)
    # A different valid payload has a different exact model digest. Reusing the
    # old full projection must fail even when every identity and edge is equal.
    changed['populations']['objects'][4 if fixture == 'stdo-3.0.2' else 1]['value'][
        'definition' if fixture == 'stdo-3.0.2' else 'text'] += ' Independent review content change.'
    changed_import = adapter.import_model(changed)
    assert changed_import['edges'] == imported['edges']
    assert changed_import['model_sha256'] != imported['model_sha256']
    refused(fixture + ': stale full projection on equal-edge changed content', lambda: adapter.check_certificate(changed_import, projection))

source = adapter.read_json(TENANT / 'fixtures/stdo-3.0.2/MODEL.json')
imported = adapter.import_model(source)
projection = adapter.closure_certificate(imported, [2], 2)
assert projection['included'] == [2, 15]
assert 3 not in projection['included']
assert any(item['index'] == 10 for item in projection['boundary']['crossing_relations'])
record('declared direction: PC03 does not acquire PC04', {'included': [2, 15], 'crossing_relation': 10})

bad_derived = copy.deepcopy(imported)
bad_derived['edges'].append([2, 3])
refused('stale derived reverse edge', lambda: adapter.closure_certificate(bad_derived, [2]))
bad_projection = copy.deepcopy(projection)
bad_projection['boundary']['excluded_residual_records'][0]['record']['consequence'] = 'Resolved by projection.'
refused('excluded residual payload/standing alteration', lambda: adapter.check_certificate(imported, bad_projection))
bad_projection = copy.deepcopy(projection)
bad_projection['envelope']['interpretation']['authority']['id'] = 'urn:review:false-authority'
refused('projection envelope authority alteration', lambda: adapter.check_certificate(imported, bad_projection))

origin = ROOT / 'specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/native-release/release-run-01/supplement-bundle'
raw = {}
for name in ('MODEL.json', 'CARRIER.json', 'GRAPHIFY_EXTRACTION.json'):
    original = (origin / name).read_bytes()
    copied = (TENANT / 'fixtures/stdo-3.0.2' / name).read_bytes()
    assert copied == original
    raw[name] = hashlib.sha256(copied).hexdigest()
record('published original bytes equal all three tenant copies', raw)

for args, expected_code in ((['--seed', '2', '--budget', '2'], 0),
                            (['--seed', '2', '--budget', '1'], 2),
                            (['--toy', '--seed', '11', '--budget', '10'], 0)):
    run = subprocess.run([sys.executable, '-B', str(TENANT / 'scripts/import_fixture.py'), *args],
                         cwd=TENANT, capture_output=True, text=True)
    assert run.returncode == expected_code, run.stderr
    output = json.loads(run.stdout)
    assert output['status'] == ('checked' if expected_code == 0 else 'refused')
    if expected_code:
        assert 'result' not in output
    record('public CLI ' + ' '.join(args), {'exit': run.returncode, 'status': output['status'],
                                          'included': output.get('result', {}).get('included'),
                                          'reason': output.get('reason')})

report = {'subject_manifest_sha256': '5f97e749909b60a58e072ea9b36ce40e5cebab2612fef39940ec98ee6d70aca5',
          'reviewer': '/root/ac_lean_review', 'scope': 'Python adapter only; no Lean proof or runtime assessment',
          'results': results}
Path(__file__).with_name('adapter_probe_results.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
