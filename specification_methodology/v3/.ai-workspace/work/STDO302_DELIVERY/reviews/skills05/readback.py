"""Read-only final Skills05 evidence readback; no native calls or package builds."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
WORK = ROOT / 'stdo_skills/.ai-workspace/work/COMPOSITION_01'
OP = WORK / 'operator-successor-05'
OBJECTS = WORK / 'operator/evidence/objects'
ACTOR = '/root/composition_proposal_writer'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text())

def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()

def rows_match(rows, root):
    for row in rows:
        path = root / row['path']
        assert sha(path) == row['sha256'], path
        if 'bytes' in row:
            assert path.stat().st_size == row['bytes'], path

candidate = WORK / 'CANDIDATE-05.json'
assert sha(candidate) == '9c153e0942e28900b53651c5fb875f5fb5639adc5610e11f16c03dba1a2ba7ee'
index = load(candidate)
rows_match(index['files'], ROOT)
instructions = load(WORK / 'INSTRUCTIONS_CANDIDATE.json')
rows_match(instructions['files'], ROOT)
assert len(instructions['files']) == 27

history = load(WORK / 'HISTORY-freeze04.json')
old_index = load(WORK / 'CANDIDATE-04.json')
assert sha(WORK / 'CANDIDATE-04.json') == history['candidate_sha256']
assert sha(WORK / history['archive']) == history['archive_sha256']
assert history['files'] == old_index['files']
preserved_objects = []
with zipfile.ZipFile(WORK / history['archive']) as archive:
    for row in history['files']:
        raw = archive.read(row['path'])
        assert hashlib.sha256(raw).hexdigest() == row['sha256']
        assert len(raw) == row['bytes']
        if '/operator/evidence/objects/' in row['path']:
            assert (ROOT / row['path']).read_bytes() == raw
            preserved_objects.append(row['path'])
    assert archive.read('stdo_skills/.ai-workspace/work/COMPOSITION_01/CANDIDATE-04.json') == (WORK / 'CANDIDATE-04.json').read_bytes()

manifest_path = ROOT / 'stdo_skills/specification/composition/SOURCE_MANIFEST.json'
manifest = load(manifest_path)
assert sha(manifest_path) == index['current_manifest_sha256']
rows_match(manifest['files'], ROOT)
for key in ['provider_freeze', 'provider_selection', 'manager_freeze', 'manager_distribution']:
    assert sha(ROOT / manifest[key]['path']) == manifest[key]['sha256']
assert sha(Path(manifest['runtime']['interpreter'])) == manifest['runtime']['interpreter_sha256']
provider = load(ROOT / manifest['provider_selection']['path'])
mapped = {r['path']: r['sha256'] for r in manifest['files']}
assert all(mapped[path] == digest for path, digest in provider['files'].items())
assert not any('/v3/build_tenants/' in row['path'] for row in manifest['files'])

roots = {'product': ROOT / 'stdo_skills', 'tool': ROOT / 'a_c',
         'method': Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1')}
routes = load(ROOT / 'stdo_skills/build_tenants/codex/skills/stdo-work/source-routes.json')
for source in routes['sources']:
    assert sha(roots[source['root']] / source['path']) == source['sha256']
    if source.get('selector'):
        start, end = source['selector']['lines']
        assert 0 < start <= end <= len((roots[source['root']] / source['path']).read_text().splitlines())

definition_path = ROOT / 'stdo_skills/stdo_skills.json'
definition = load(definition_path)
policy = load(OP / 'POLICY.json')
owner = load(OP / 'OWNER.json')
composition = load(OP / 'COMPOSITION.json')
strict = load(OP / 'COMPOSITION-strict.json')
assert definition['constitution']['stdo']['basis'] == manifest['consumer_basis'] == routes['method']
assert definition['constitution']['stdo']['basis']['uri'] == 'stdo://releases/v3.0.1-rc.1/'
assert definition['reference_frame_bases'][0]['authority'][1] == './.ai-workspace/work/COMPOSITION_01/operator-successor-05/OWNER.json'
binding = policy['product']['authority_binding']
assert binding['definition_locator'] == '/reference_frame_bases/0/authority/1'
assert binding['owner_record']['sha256'] == sha(OP / 'OWNER.json')
assert policy['product']['definition']['sha256'] == sha(definition_path)
for key in ['mechanism', 'result_surface', 'scope']:
    assert binding[key] == owner[key]
assert policy['principals']['writer']['actor_id'] == owner['scope']['actor'] == ACTOR
assert policy['evidence_root'] == str(OBJECTS.parent) == owner['result_surface']['root']
assert policy['grants'] == policy['executors'] == policy['predicates'] == {}
assert policy['principals']['writer']['operations'] == ['tools.describe','composition.inspect','source.read','context.assemble']
assert composition['bindings']['writer']['route'] == ['skills-ac-support']
assert composition['bindings']['writer']['output']['complete'] is False
assert composition['bindings']['writer']['require_complete'] is False
assert strict['bindings']['writer']['require_complete'] is True
assert composition['bindings']['writer']['clean_room'] is False

checks = load(OP / 'CHECKS.json')
operations = []
for row in checks['checks']:
    folder = OP / 'calls' / row['name']
    response = load(folder / 'stdout.json')
    request = load(folder / 'request.json')
    execution = load(folder / 'EXECUTION.json')
    assert execution == row
    receipt_path = OBJECTS / (row['evidence']['sha256'] + '.json')
    assert sha(receipt_path) == row['evidence']['sha256']
    receipt = load(receipt_path)
    payload, provenance = receipt['payload'], receipt['provenance']
    assert payload['request'] == request
    assert provenance['request_sha256'] == canonical(request)
    assert provenance['actor']['actor_id'] == ACTOR
    assert provenance['definition_sha256'] == sha(definition_path)
    assert provenance['policy_sha256'] == sha(OP / ('POLICY-strict.json' if row['name'] == 'strict-context' else 'POLICY.json'))
    assert response['status'] == row['status'] == row['expected']
    projected = dict(response); projected['evidence'] = None
    assert payload['response_without_evidence'] == projected
    operations.append({'name': row['name'], 'status': row['status'], 'receipt': row['evidence']['sha256']})

ordinary = load(OP / 'calls/ordinary-context/stdout.json')
ctx_ref = ordinary['result']['artifact']['sha256']
assert sha(OBJECTS / (ctx_ref + '.json')) == ctx_ref
ctx = load(OBJECTS / (ctx_ref + '.json'))['payload']
assert ctx['boundaries']['declared_input_provenance_complete'] is False
assert ctx['composition']['declared_input_provenance_complete'] is False
inputs = ctx['composition']['input_sources']
assert any(source.get('unknown') is True for source in inputs)
assert {'composition', 'composition-04', 'composition-05'}.issubset({source['id'] for source in inputs})
assert ctx['fit']['host_context']['state'] == 'unknown'
assert ctx['fit']['judgment'] is None
assert hashlib.sha256(ctx['rendered_utf8'].encode()).hexdigest() == ctx['rendered_sha256']
strict_outcome = load(OP / 'calls/strict-context/stdout.json')
assert strict_outcome['refusal']['code'] == 'basis_missing'
strict_receipt = load(OBJECTS / (strict_outcome['evidence']['sha256'] + '.json'))
diagnostics = [load(OBJECTS / (ref['sha256'] + '.json')) for ref in strict_receipt['payload']['artifacts']]
assert any('Unresolved provenance' in json.dumps(value) for value in diagnostics)

manager = load(WORK / 'MANAGER_CHECKS-05.json')
assert manager['wheel'] == {k: manifest['manager_distribution'][k] for k in ['path','sha256']}
assert manager['actual_import']['version'] == '0.1.6'
assert 'site-packages' in Path(manager['actual_import']['module']).parts
assert sha(Path(manager['actual_import']['module'])) == manager['actual_import']['sha256']
for row in manager['commands']:
    assert '-I' in row['argv'] and row['removed_environment'] == ['PYTHONPATH','PYTHONHOME']
positive = load(WORK / 'manager-checks-05/selected-repository-boundary.stdout.json')
negative = load(WORK / 'manager-checks-05/too-narrow-boundary.stdout.json')
assert positive['valid'] is True and negative['valid'] is False
assert positive['authority_and_semantic_adequacy'] == 'not evaluated'
edge = positive['definitions'][0]['composition'][0]
assert edge['target_definition_id'] == 'urn:stdo:product-definition:a-c-implementations'
references = [edge['references']['product_definition'], edge['references']['relation'], *edge['references']['contracts']]
for ref in references:
    assert ref['status'] == 'resolved' and sha(Path(ref['path'])) == ref['sha256']
assert all(x['code'] == 'outside_boundary' for x in negative['definitions'][0]['composition'][0]['failures'])

codex_root = ROOT / 'stdo_skills/build_tenants/codex'
codex = load(codex_root / 'inventory.json')
rows_match(codex['files'], codex_root)
claude_root = ROOT / 'stdo_skills/build_tenants/claude'
claude = re.findall(r'^\| ([^|]+?) \| ([a-f0-9]{64}) \|$', (claude_root / 'INVENTORY.md').read_text(), re.M)
assert len(claude) == 13
for path, digest in claude:
    assert sha(claude_root / path) == digest
package = load(WORK / 'PACKAGE_CHECKS-05.json')
assert all(row['exit'] == 0 for row in package['package_commands'])

rows_match(index['files'], ROOT)
result = {'candidate_sha256': sha(candidate), 'frozen_files': len(index['files']),
          'instruction_files_unchanged': len(instructions['files']), 'history_archive_files_verified': len(history['files']),
          'prior_protected_objects_unchanged': len(preserved_objects), 'runtime_contract_pins_verified': len(manifest['files']),
          'route_pins_verified': len(routes['sources']), 'provider_selection_pins_verified': len(provider['files']),
          'operation_receipts_verified': operations, 'ordinary_context': ctx_ref,
          'unknown_and_prior_versions_retained': True, 'strict_unknown_refusal': True,
          'actual_manager_wheel_receipt_verified': True, 'edge_references_verified': len(references),
          'codex_inventory_files': len(codex['files']), 'claude_inventory_files': len(claude),
          'limits': 'Readback of existing actual receipts and bytes only; no new native calls, package builds, dispatch, host qualification or publication.'}
with (HERE / 'RESULTS.json').open('x') as output:
    json.dump(result, output, indent=2); output.write('\n')
print(json.dumps(result, indent=2))
