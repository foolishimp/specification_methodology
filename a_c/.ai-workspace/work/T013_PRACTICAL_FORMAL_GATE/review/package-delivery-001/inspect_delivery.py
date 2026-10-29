"""Read-only archive/source/public-evidence review. No extraction or product call.

Only the review report is written. The 3.25 GB installed support population,
native executables, private origins/keys and F_P candidate outputs are not read.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime
import hashlib
import json
import re
import tarfile

AC = Path('/Users/jim/src/apps/specification_methodology/a_c')
W = AC / '.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE'
D = W / 'package/delivery-001'
OUT = Path(__file__).resolve().parent
SCRATCH = Path('/private/tmp/ac-t013-lean-package-001')
ORIGIN = '.cache/formal-origin-v1/selection.json'
PREFIX = 'a_c/build_tenants/lean/'


def sha(path):
    assert 'formal-origin-v1' not in path.parts
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def load(path):
    assert 'formal-origin-v1' not in path.parts
    return json.loads(path.read_bytes())


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def safe(name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts and p.as_posix() == name
    assert not {x.casefold() for x in p.parts}.intersection({'.cache','.git','__pycache__','formal-origin-v1','entries','pending'})
    assert not name.casefold().endswith(('.key','.pem'))


assert sha(D / 'CLOSED.json') == 'be9537a34cca887700275396218cf3c76fba674bede662d5a2fab43b5a986ee1'
assert sha(D / 'PINS.json') == '10fc89060b165abbe08d9c528321f4ca18bfd3adda9c59b7b480d1d49dce7c6e'
pins = load(D / 'PINS.json')['members']
for name, expected in pins.items():
    safe(name)
    p = D / name
    assert p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(D)
    assert sha(p) == expected, name
assert {p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()} == set(pins) | {'CLOSED.json','PINS.json'}
assert all(not p.is_symlink() for p in D.rglob('*'))
manifest_raw = (D / 'SOURCE_PACKAGE.json').read_bytes()
manifest = json.loads(manifest_raw)
manifest_sha = hashlib.sha256(manifest_raw).hexdigest()
assert manifest_sha == 'e981245097c06f693fcbe89565d5724db2103982fdb7891e8413a8a6cdc86ee4'
assert sha(W / 'package/selection-001/SOURCE_PACKAGE.json') == manifest_sha
assert digest(manifest['freeze']) == manifest['freeze_sha256']
full = manifest['freeze']['runtime_identity']
portable = manifest['portable_runtime_identity']
assert digest(full['pins']) == full['sha256'] == '065648e6cc971be7edc75c1fa7b0428351357fe312146059b71fb788842313a7'
assert portable['pins'] == {k: v for k, v in full['pins'].items() if k != ORIGIN}
assert digest(portable['pins']) == portable['sha256'] == '07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601'
assert full == load(W / 'reuse/qualification-001/RUNTIME-IDENTITY.json')
rows = {r['path']: r for r in manifest['files']}
assert len(rows) == len(manifest['files']) == 65
expected_names = sorted([*rows, 'SOURCE_PACKAGE.json'])
assert len({n.casefold() for n in expected_names}) == len(expected_names)
payload_hashes = {}
support = None
with tarfile.open(D / 'source-package.tar', 'r:') as tar:
    members = tar.getmembers()
    assert [m.name for m in members] == expected_names
    for member in members:
        safe(member.name)
        assert member.type == tarfile.REGTYPE
        assert member.mode == 0o644 and member.uid == member.gid == member.mtime == 0
        assert member.uname == member.gname == '' and not member.linkname and not member.pax_headers
        data = tar.extractfile(member).read()  # in memory only; no extraction effects
        actual = hashlib.sha256(data).hexdigest()
        payload_hashes[member.name] = actual
        if member.name == 'SOURCE_PACKAGE.json':
            assert data == manifest_raw
        else:
            row = rows[member.name]
            assert actual == row['sha256'] and len(data) == row['bytes']
            safe(row['source'])
            assert sha(AC.parent / row['source']) == actual
        if member.name == PREFIX + 'profiles/proof-support-v1.json':
            support = json.loads(data)
    last = members[-1]
    end = last.offset_data + ((last.size + 511) // 512) * 512
with (D / 'source-package.tar').open('rb') as stream:
    stream.seek(end)
    padding = stream.read()
assert len(padding) >= 1024 and not any(padding)
archive_sha = sha(D / 'source-package.tar')
assert archive_sha == '40dbe00cc85d9c1c4a6ec88634a4318d7f9363bd2d68b025d6941872319d7ea0'
assert (D / 'source-package.tar').stat().st_size == 22353920
for name in ('source-package.tar','source-repack.tar'):
    assert sha(SCRATCH / name) == archive_sha
for tree in ('bundle','pristine','operational'):
    root = SCRATCH / tree
    for name, expected in payload_hashes.items():
        path = root / name
        assert path.is_file() and not path.is_symlink() and sha(path) == expected
    if tree != 'operational':
        actual_paths = list(root.rglob('*'))
        assert all(not p.is_symlink() for p in actual_paths)
        assert {p.relative_to(root).as_posix() for p in actual_paths if p.is_file()} == set(expected_names)
for name, expected in portable['pins'].items():
    assert payload_hashes[PREFIX + name] == expected
assert payload_hashes['package_source.py'] == '9907d7245372af188276384cc5ab710b9a77328b92047a277a94e1ed5ab40117'
assert payload_hashes['test_package_source.py'] == '48666fe8981d5d0ba569e53ae18e48d21d5069400aba5bb8ba95dff7419bf222'

package = load(D / 'PACKAGE.json')
for record in package['records']:
    step = record['step']
    assert record['returncode'] == 0 and record['seconds'] < 60
    assert record['stdout_sha256'] == pins[step + '.stdout'] and record['stderr_sha256'] == pins[step + '.stderr']
    assert load(D / (step + '.stdout')) == record['returned']
    assert record['argv'][1:4] == ['-I','-S','-B']
    assert record['argv'][-2:] == ['--manifest-sha256',manifest_sha]
    assert record['returned']['manifest_sha256'] == manifest_sha
assert package['archive_sha256'] == package['repacked_archive_sha256'] == archive_sha

custody = load(D / 'SUPPORT-CUSTODY.json')
assert custody['support_manifest_sha256'] == portable['pins']['profiles/proof-support-v1.json'] == '7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363'
assert support['platform'] == custody['platform'] == 'Darwin-arm64'
copied = {r['path']: r for r in custody['rows']}
assert len(copied) == len(custody['rows']) == len(support['members']) == 30405
assert {name: r['sha256'] for name, r in copied.items()} == support['members']
preserved = []
copied_bytes = 0
for name, row in copied.items():
    safe(name)
    assert row['source_mode'] == row['installed_mode']
    packaged = PREFIX + name in rows
    if packaged:
        assert row['action'] == 'preserved-packaged-source'
        assert row['sha256'] == rows[PREFIX + name]['sha256'] and row['bytes'] == rows[PREFIX + name]['bytes']
        preserved.append(name)
    else:
        assert row['action'] == 'copied-absent-runtime-member'
        copied_bytes += row['bytes']
assert sorted(preserved) == ['AC/Closure.lean','AC/GateProof.lean','AC/GateRuntime.lean','AC/Model.lean','AC/Projection.lean','AC/Structure.lean']
assert custody['copied_members'] == 30399 and custody['preserved_packaged_members'] == 6
assert copied_bytes == custody['copied_bytes'] == 3254927206
assert custody['production_origin_acquired'] is False and custody['support_reestablished'] is False
current = load(D / 'CURRENTNESS.json')
assert current['operational_exact_file_count'] == len(set(expected_names) | {PREFIX + n for n in copied}) == 30465
assert current['installed_cache_and_origin_absent'] and current['output_origin_hint_absent']
assert all(current['selected_source_files'][name]['sha256'] == row['sha256'] for name, row in rows.items())
assert not (SCRATCH / 'operational' / PREFIX / '.cache').exists()  # absence metadata only

installed = D / 'installed-small-evidence'
result = load(installed / 'result.json')
external = load(D / 'installed-small-fallback.external.json')
checker = load(D / 'INSTALLED-CHECKER.json')
original = W / 'reuse/qualification-001/small-cold'
original_result = load(original / 'result.json')
assert result == load(D / 'installed-small-fallback.stdout')
assert result['status'] == 'verified' and external['returncode'] == 0 and external['status'] == 'PASS'
assert sha(installed / 'result.json') == external['result_sha256'] == 'f96eec30895f019f230af22ae06854481b7fa5af98d6450f0404b080391ec516'
assert result['runtime_identity'] == checker['runtime_identity'] == portable == load(D / 'installed-identity.stdout')
assert checker['root'] == str(SCRATCH / 'operational' / PREFIX)
assert checker['entry_sha256'] == portable['pins']['scripts/formal_gate.py']
assert checker['adapter_sha256'] == payload_hashes['a_c/build_tenants/graphify/code/ac_formal_gate.py']
assert result['requested_claims'] == result['checked_claims'] == original_result['checked_claims']
for key in ('model','inputs','selections','context_binding','limits'):
    assert result[key] == original_result[key]
evidence_manifest = load(installed / 'manifest.json')
assert evidence_manifest['members'] == result['evidence']['members']
assert sha(installed / 'manifest.json') == result['evidence']['manifest_sha256'] == external['evidence_manifest_sha256']
for name, expected in evidence_manifest['members'].items():
    assert Path(name).name == name and sha(installed / name) == expected
    expected_original = 'replay-request.json' if name == 'request.json' else name
    assert sha(original / expected_original) == expected
assert {p.name for p in installed.iterdir()} == set(evidence_manifest['members']) | {'result.json','manifest.json'}
assert result['request_sha256'] == digest(load(installed / 'request.json'))
assert 'original_establishment' not in result['observations']
obs = result['observations']
assert obs['reuse'].startswith('none; fresh dynamic obligations')
assert obs['reuse_unavailable'] == 'different or absent origin selection; standalone cold verification required'
assert obs['origin_unavailable'] == 'no selected local origin'
assert [obs[k] for k in ('current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations')] == [7,1,1]
assert obs['support'] == current['actual_cold_support_rechecks'] == original_result['observations']['support']
assert obs['limits'] == dict(timeout_seconds=90,memory_mb=4096,max_input_bytes=33554432,max_selections=64)
assert [s['stage'] for s in obs['stages']] == [s['stage'] for s in original_result['observations']['stages']]
assert all(s['seconds'] < 90 and s.get('exit_code',0) == 0 for s in obs['stages'])
assert obs['theorem_audit'] == original_result['observations']['theorem_audit']
assert obs['elapsed_seconds'] <= external['external_invocation_seconds'] < 600
assert external['outer_seconds'] == 600 and external['checking_seconds'] == 90 and external['lean_memory_mb'] == 4096
assert external['physical_rss_cap'] is False
assert external['argv'][1:7] == ['-I','-S','-B','-X','pycache_prefix=/dev/null',checker['root'] + '/scripts/formal_gate.py']
assert external['argv'][7:10] == ['check-evidence','--bundle',str(original)]
assert external['argv'][10:] == ['--output',str(installed)]
assert datetime.fromisoformat(external['started_utc']) >= datetime.fromisoformat(load(D / 'WINDOW-RELEASE.json')['recorded_utc'])
assert external['origin_before'] == external['origin_after'] == 'absent (installed metadata only)'
for kind in ('identity','small-fallback'):
    e = load(D / ('installed-' + kind + '.external.json'))
    for suffix in ('stdout','stderr'):
        assert e[suffix + '_sha256'] == pins['installed-' + kind + '.' + suffix]

report = dict(status='passed', public_files_checked=len(pins), public_bytes_checked=sum((D / name).stat().st_size for name in pins), archive_sha256=archive_sha, archive_bytes=22353920, regular_archive_members=66, exact_selected_source_files=65, independently_checked_source_trees=['bundle','pristine','operational packaged files only'], exact_pristine_file_population=True, byte_identical_existing_repack=True, portable_identity=portable['sha256'], origin_coordinate_only_omission=True, support_custody_members=30405, support_newly_copied_members=30399, support_preserved_package_sources=preserved, recorded_copied_bytes=copied_bytes, support_contents_rehashed_by_reviewer=False, native_executable_rehashed_by_reviewer=False, proof_replayed_by_reviewer=False, installed_result_sha256=sha(installed / 'result.json'), installed_output_exactly_matches_previously_reviewed_small_subject=True, installed_cold_invocations=[7,1,1], installed_external_seconds=external['external_invocation_seconds'], installed_internal_seconds=obs['elapsed_seconds'], installed_reaped_children_high_water_rss_bytes=external['reaped_children_peak_rss_bytes'], installed_origin_and_hint_absent=True, fresh_machine_qualification=False, public_release=False, FP_candidate_outputs_read=False)
(OUT / 'CHECKS.json').write_text(json.dumps(report, sort_keys=True, indent=2) + '\n')
print(json.dumps(report, sort_keys=True))
