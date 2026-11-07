"""Join observed clone hashes to source support and locked dependency coordinates."""
from pathlib import Path
import json
import posixpath
import subprocess
import run_observed as o

p = Path(__file__).absolute().parent
h = json.loads((p / 'SELECTED_HANDOFF.json').read_bytes())
source = o.REPO / 'a_c/build_tenants/lean'
destination = Path(h['workspace']) / 'runtime/a_c/build_tenants/lean'
directory = p / 'cache-clone-001'
result = json.loads((directory / 'RESULT.json').read_bytes())
assert result['status'] == 'cache-cloned' and result['copy_fallback'] is False
ledger_path = directory / 'members.jsonl'
assert o.sha(ledger_path) == result['ledger']['sha256']
ledger = {}
with ledger_path.open() as stream:
    for line in stream:
        row = json.loads(line)
        assert row['path'] not in ledger
        ledger[row['path']] = row
assert len(ledger) == result['entries']
profile_path = source / 'profiles/proof-support-v1.json'
assert o.sha(profile_path) == '7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363'
profile = json.loads(profile_path.read_bytes())
prefixes = ('.toolchain/', '.lake/packages/', '.cache/mathlib/')
selected = {key: value for key, value in profile['members'].items() if key.startswith(prefixes)}

def observed_hash(key):
    seen = set()
    while True:
        assert key not in seen, ('symlink cycle', key)
        seen.add(key)
        row = ledger[key]
        if row['kind'] == 'file':
            assert row['clone']['returncode'] == 0 and row['clone']['copy_fallback'] is False
            a, b = row['source_identity'], row['destination_identity']
            assert (a['device'], a['inode']) != (b['device'], b['inode'])
            return row['sha256'], key
        assert row['kind'] == 'symlink', row
        key = posixpath.normpath(posixpath.join(posixpath.dirname(key), row['link']))
        assert key.startswith(prefixes), key

join_path = directory / 'profile-member-join.jsonl'
with join_path.open('x') as stream:
    for key, expected in sorted(selected.items()):
        observed, target = observed_hash(key)
        assert observed == expected, (key, expected, observed)
        stream.write(json.dumps({'path': key, 'expected_sha256': expected,
            'observed_sha256': observed, 'ledger_file': target}, sort_keys=True) + '\n')

for name in ('toolchain-lock.json', 'lake-manifest.json', 'lean-toolchain'):
    assert (source / name).read_bytes() == (destination / name).read_bytes()
lock = json.loads((source / 'toolchain-lock.json').read_bytes())
archive = lock['lean']['archives']['Darwin-arm64']
archive_hash, archive_row = observed_hash('.toolchain/' + archive['name'])
assert archive_hash == archive['sha256']
manifest = json.loads((source / 'lake-manifest.json').read_bytes())
revisions = []
for package in manifest['packages']:
    observed = []
    for root in (source, destination):
        argv = ['git', '--no-optional-locks', '-C', str(root / '.lake/packages' / package['name']), 'rev-parse', 'HEAD']
        completed = subprocess.run(argv, text=True, capture_output=True, check=False)
        observed.append({'argv': argv, 'returncode': completed.returncode,
            'stdout': completed.stdout, 'stderr': completed.stderr})
        assert completed.returncode == 0 and completed.stdout.strip() == package['rev']
    revisions.append({'package': package['name'], 'expected_revision': package['rev'], 'observations': observed})
extras_path = directory / 'unprofiled-cache-paths.jsonl'
with extras_path.open('x') as stream:
    for key, row in sorted(ledger.items()):
        if key not in selected:
            stream.write(json.dumps({'path': key, 'kind': row['kind'],
                'sha256': row.get('sha256'), 'standing': 'Not a selected support-profile member; ordinary bootstrap decides use.'}, sort_keys=True) + '\n')
record = {'kind': 'stdo.rc-reset.cache-inventory-join/1', 'status': 'consistent',
    'source_profile': o.ref(profile_path), 'clone_result': o.ref(directory / 'RESULT.json'),
    'clone_ledger': o.ref(ledger_path), 'joined_members': len(selected),
    'join': o.ref(join_path), 'unprofiled_entries': len(ledger) - len(selected),
    'unprofiled_paths': o.ref(extras_path), 'archive': {'path': archive_row, 'sha256': archive_hash},
    'package_revisions': revisions,
    'limits': 'Metadata join to actual per-file clone observations, not a new support verdict. Cache extras include Git metadata, download cache and retained partial cache downloads; none become proof evidence by copying. New runtime support/origin/proof must be established normally.'}
(directory / 'INVENTORY_JOIN.json').write_bytes(o.encoded(record))
print(json.dumps({'status': record['status'], 'joined_members': len(selected),
    'unprofiled_entries': record['unprofiled_entries'], 'record': o.ref(directory / 'INVENTORY_JOIN.json')}), flush=True)
