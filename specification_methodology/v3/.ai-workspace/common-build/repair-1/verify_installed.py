import hashlib, importlib.metadata, json, pathlib, sys
from jsonschema import Draft202012Validator
from stdo_toolchain.manifest import manifest_bytes, standards_member_set_sha256, verify_materialization
root = pathlib.Path(sys.argv[1])
installed_schema = pathlib.Path(sys.argv[2])
inventory_path = pathlib.Path(sys.argv[3])
sha = lambda data: hashlib.sha256(data).hexdigest()
manifest_raw = (root / 'manifest.json').read_bytes()
manifest = json.loads(manifest_raw)
schema_results = []
for label, path in [('installed_basis_schema', installed_schema), ('candidate_schema', root / 'standards/schemas/installed-release-manifest.schema.json')]:
    document = json.loads(path.read_bytes())
    Draft202012Validator.check_schema(document)
    errors = [{'path': list(error.absolute_path), 'message': error.message} for error in Draft202012Validator(document).iter_errors(manifest)]
    schema_results.append({'label': label, 'path': str(path), 'sha256': sha(path.read_bytes()), 'valid': not errors, 'errors': errors})
failures = verify_materialization(root, manifest)
frozen_raw = inventory_path.read_bytes()
frozen = json.loads(frozen_raw)
expected = {member['path']: member['sha256'] for member in frozen['members']}
actual = {path.relative_to(root).as_posix(): sha(path.read_bytes()) for path in root.rglob('*') if path.is_file() and path.relative_to(root).as_posix() != 'manifest.json'}
canonical = manifest_bytes(manifest) == manifest_raw
aggregate = standards_member_set_sha256(manifest['standards']['members']) == manifest['standards']['member_set_sha256']
valid = not failures and all(item['valid'] for item in schema_results) and expected == actual and canonical and aggregate
modules = {}
for name, module in sorted(sys.modules.items()):
    if name == 'stdo_toolchain' or name.startswith('stdo_toolchain.'):
        file = getattr(module, '__file__', None)
        if file:
            path = pathlib.Path(file).resolve()
            modules[name] = {'path': str(path), 'sha256': sha(path.read_bytes())}
result = {
    'kind': 'stdo.common-exact-candidate-materialization-verification',
    'valid': valid,
    'manifest_sha256': sha(manifest_raw),
    'inventory_sha256': sha(frozen_raw),
    'installed_verifier_failures': failures,
    'schema_validation': schema_results,
    'canonical_manifest_bytes_match': canonical,
    'canonical_standards_digest_match': aggregate,
    'complete_frozen_candidate_members_match': expected == actual,
    'candidate_member_count': len(expected),
    'materialized_candidate_member_count': len(actual),
    'standards_member_count': manifest['standards']['member_count'],
    'plugin_member_count': manifest['auxiliary']['plugin']['member_count'],
    'standards_member_set_sha256': manifest['standards']['member_set_sha256'],
    'runtime': {'executable': sys.executable, 'python_version': sys.version, 'stdo_toolchain_version': importlib.metadata.version('stdo-toolchain'), 'jsonschema_version': importlib.metadata.version('jsonschema')},
    'observed_toolchain_module_pins': modules,
    'scope': 'Exact candidate bytes in an isolated canonical layout with fictional cut/ref and absent-tag sentinel. No release-source attestation or installation.',
    'source_pin_limit': 'Observed loaded STDO-toolchain source files, schemas and declared runtime identities; not authentication of the entire Python or dependency closure.',
}
print(json.dumps(result, sort_keys=True))
raise SystemExit(0 if valid else 1)
