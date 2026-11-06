"""Read-only custody inventory; output is the sole newly created INDEX.json."""
from pathlib import Path
import hashlib
import json
import os

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
REPO = next(p for p in WORK.parents if (p / 'a_c').is_dir() and (p / 'stdo_skills').is_dir())


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def pin(path):
    return {'path': str(path.relative_to(REPO)), 'sha256': digest(path), 'bytes': path.stat().st_size}


def main():
    output = HERE / 'INDEX.json'
    if output.exists(): raise ValueError('Freeze is immutable; select a successor custody directory')
    archived = {}
    transports = []
    archive_root = WORK.parent / 'packaging-integration-001/archives'
    for raw_relative, transport_name, actual_absence_control in [
        ('current-formal-005/cold', 'cold', True),
        ('current-formal-005/controls/budget/evidence', 'budget', True),
        ('current-formal-005/controls/omission/evidence', 'omission', True),
        ('current-formal-008/cold', 'cold008', False),
    ]:
        raw_root = WORK / raw_relative
        descriptor = archive_root / (transport_name + '-transport/TRANSPORT.json')
        data = json.loads(descriptor.read_text())
        parts = []
        combined = hashlib.sha256()
        for part in data['parts']:
            path = descriptor.parent / part['path']
            actual = pin(path)
            assert actual['sha256'] == part['sha256'] and actual['bytes'] == part['bytes'], path
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b''): combined.update(block)
            parts.append(actual)
        assert combined.hexdigest() == data['archive_sha256'], descriptor
        assert sum(p['bytes'] for p in parts) == data['archive_bytes']
        manifest = json.loads((raw_root / 'manifest.json').read_text())
        assert set(data['members']) == set(manifest['members']) | {'manifest.json', 'result.json'}
        for name, declared in data['members'].items():
            path = raw_root / name
            actual = pin(path)
            assert actual['sha256'] == declared['sha256'] and actual['bytes'] == declared['bytes'], path
            if name not in ('manifest.json', 'result.json'):
                archived[actual['path']] = {**actual, 'member': name,
                    'transport_descriptor': str(descriptor.relative_to(REPO)),
                    'reason': 'Exact full-proof archived duplicate; original manifest and result remain ordinary selected files.'}
        transports.append({'raw_root': str(raw_root.relative_to(REPO)), 'descriptor': pin(descriptor),
            'archive_sha256': data['archive_sha256'], 'archive_bytes': data['archive_bytes'],
            'manifest_sha256': data['manifest_sha256'], 'result_sha256': data['result_sha256'],
            'recoverable_members': len(data['members']), 'parts': parts,
            'observed_here': 'Every original member and every transport part hashed; concatenated archive digest matched.',
            'raw_unavailable_control': 'Passed with originals absent; retained in raw-unavailable-portability-001.' if actual_absence_control else
                                       'Not repeated for successor008; exact compressed transport and owner inspection are separately retained by common writer.'})
    included, excluded, unexpected = [], [], []
    private_names = {'origin.key', 'local-origin.json'}
    private_dirs = {'.git', '.venv', '.toolchain', '.lake', '.cache', '__pycache__'}
    for directory, names, files in os.walk(WORK, followlinks=False):
        parent = Path(directory)
        for name in list(names):
            path = parent / name
            if path.is_symlink() or name in private_dirs:
                names.remove(name)
                excluded.append({'path': str(path.relative_to(REPO)), 'reason': 'Private runtime/cache/nested repository or symlink tree; not a Git-retained evidence claim.'})
        for name in files:
            path = parent / name
            relative = str(path.relative_to(REPO))
            if path == output: continue
            if path.is_symlink():
                excluded.append({'path': relative, 'reason': 'Symlink is not selected as portable evidence.'}); continue
            if name in private_names:
                excluded.append({'path': relative, 'bytes': path.stat().st_size,
                                 'reason': 'Private local origin authority/certificate; not a declared proof manifest member. No private contents read or hashed.'}); continue
            if relative in archived:
                excluded.append(archived[relative]); continue
            if not path.is_file():
                unexpected.append(relative); continue
            item = pin(path)
            if item['bytes'] >= 100 * 1024 * 1024: raise ValueError('Unarchived oversized evidence: ' + relative)
            included.append(item)
    assert not unexpected, unexpected
    for selected in ('code-metadata-008.json', 'a_c-portable-008.json'):
        inventory = json.loads((WORK / selected).read_text())
        for item in inventory['files']:
            actual = pin(REPO / item['path'])
            assert actual['sha256'] == item['sha256'] and actual['bytes'] == item['bytes'], item['path']
    data = {'schema': 'stdo305.tools-skills.evidence-custody/1',
        'status': 'frozen_snapshot_current008_transport_and_preparation_complete_actual_installed_qualification_pending',
        'scope': str(WORK.relative_to(REPO)), 'previous_index': pin(WORK / 'evidence-custody-008/INDEX.json'),
        'source_scope': 'Product source remains accepted metadata008. Source package selection is portable008 plus Skills manifest006. No Git effects performed.',
        'transports': transports, 'include': sorted(included, key=lambda row: row['path']),
        'exclude': sorted(excluded, key=lambda row: row['path']), 'pending': [],
        'snapshot_boundary': 'This index binds files observed at generation; later actual nativeA/host evidence needs a successor. INDEX.json itself is pinned by its consumer, avoiding self-inclusion.',
        'private_external_runtime_rule': 'Graphify checkout/venv, Lean support/compiler/cache and origin keys stay external. Recorded paths/pins do not claim those trees are Git members. Public origin selection is separately retained when referenced.',
        'observations': {'included_files': len(included), 'included_bytes': sum(p['bytes'] for p in included),
                         'excluded_entries': len(excluded), 'unmapped_nonregular_paths': unexpected,
                         'largest_included_file_bytes': max(p['bytes'] for p in included)}}
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'index': pin(output), 'observations': data['observations']}))


if __name__ == '__main__': main()
