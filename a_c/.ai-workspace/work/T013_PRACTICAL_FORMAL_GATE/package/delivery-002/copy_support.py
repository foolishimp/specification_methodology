"""One exact local support copy; no setup, origin, or unselected dependency copy."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib
import json
import os
import shutil
import stat
import time

D = Path(__file__).resolve().parent
T = D.parents[1]
LIVE = Path('/private/tmp/ac-t013-lean-package-001/operational/a_c/build_tenants/lean')
W = Path('/private/tmp/ac-t013-lean-package-002')
TARGET = W / 'operational/a_c/build_tenants/lean'
SUPPORT_SHA = '7198879c3dfefe52ee4c980b33990197cd338eb19ac4e84cce3dd26a4cd66363'

def sha(path):
    with Path(path).open('rb') as stream: return hashlib.file_digest(stream, 'sha256').hexdigest()

def save(name, value):
    with (D/name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def regular_path(root, relative, directories):
    p = root
    parts = PurePosixPath(relative).parts
    for part in parts[:-1]:
        p = p / part
        if p not in directories:
            assert stat.S_ISDIR(p.lstat().st_mode), 'nonregular ancestor: '+str(p)
            directories.add(p)
    p = p / parts[-1]
    metadata = p.lstat()
    assert stat.S_ISREG(metadata.st_mode), 'nonregular selected member: '+str(p)
    return p, metadata

started = time.monotonic()
rows = []
try:
    support_path = LIVE/'profiles/proof-support-v1.json'
    assert sha(support_path) == SUPPORT_SHA == sha(TARGET/'profiles/proof-support-v1.json')
    support = json.loads(support_path.read_bytes())
    assert len(support['members']) == 30405 and support['platform'] == 'Darwin-arm64'
    manifest = json.loads((D/'SOURCE_PACKAGE.json').read_bytes())
    packaged = {row['path']:row['sha256'] for row in manifest['files']}
    before = {rel:sha(W/'operational'/rel) for rel in packaged}
    assert before == packaged
    directories = {LIVE}
    sources = []
    needed_bytes = 0
    for relative, expected in sorted(support['members'].items()):
        p = PurePosixPath(relative)
        assert not p.is_absolute() and relative == p.as_posix() and '..' not in p.parts
        folded = {part.casefold() for part in p.parts}
        assert not folded.intersection({'.cache','.git','__pycache__','formal-origin-v1','entries','pending'})
        assert not relative.casefold().endswith(('.key','.pem'))
        source, metadata = regular_path(LIVE, relative, directories)
        destination = TARGET/relative
        if destination.exists() or destination.is_symlink():
            assert 'a_c/build_tenants/lean/'+relative in packaged, 'unexpected destination exists'
            assert stat.S_ISREG(destination.lstat().st_mode)
        else:
            needed_bytes += metadata.st_size
        sources.append((relative, expected, source, metadata))
    assert shutil.disk_usage(W).free > needed_bytes + 1024**3, 'insufficient selected-copy free space'
    print(json.dumps({'stage':'selected-support-copy','members':len(sources),'new_bytes':needed_bytes}),flush=True)
    for ordinal,(relative, expected, source, metadata) in enumerate(sources,1):
        destination = TARGET/relative
        if destination.exists():
            assert sha(source) == expected == sha(destination), relative
            action = 'preserved-packaged-source'
        else:
            destination.parent.mkdir(parents=True,exist_ok=True)
            digest = hashlib.sha256()
            with source.open('rb') as origin, destination.open('xb') as target:
                while data := origin.read(1024*1024):
                    digest.update(data); target.write(data)
            assert digest.hexdigest() == expected, relative
            os.chmod(destination,stat.S_IMODE(metadata.st_mode))
            assert sha(destination) == expected, relative
            action = 'copied-absent-runtime-member'
        after = source.stat()
        assert (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_mode) == (metadata.st_dev,metadata.st_ino,metadata.st_size,metadata.st_mtime_ns,metadata.st_mode), relative
        actual = destination.stat()
        if action == 'copied-absent-runtime-member': assert stat.S_IMODE(actual.st_mode)==stat.S_IMODE(metadata.st_mode)
        rows.append({'path':relative,'sha256':expected,'bytes':metadata.st_size,
                     'source_mode':stat.S_IMODE(metadata.st_mode),'installed_mode':stat.S_IMODE(actual.st_mode),'action':action})
        if ordinal % 5000 == 0: print(json.dumps({'copied_or_preserved':ordinal}),flush=True)
    assert {rel:sha(W/'operational'/rel) for rel in packaged} == before
    assert sha(support_path) == SUPPORT_SHA
    actual_files = {str(p.relative_to(W/'operational')) for p in (W/'operational').rglob('*') if p.is_file()}
    expected_files = {*packaged,'SOURCE_PACKAGE.json',*('a_c/build_tenants/lean/'+x for x in support['members'])}
    assert actual_files == expected_files, {'unexpected':sorted(actual_files-expected_files),'missing':sorted(expected_files-actual_files)}
    assert not (TARGET/'.cache').exists()
    save('SUPPORT-CUSTODY.json', {'schema':'a_c.T013.exact-local-support-copy/1','status':'PASS',
         'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_root':str(LIVE),'installed_root':str(TARGET),
         'platform':'Darwin-arm64','support_manifest_sha256':SUPPORT_SHA,'selected_members':len(rows),
         'copied_members':sum(x['action']=='copied-absent-runtime-member' for x in rows),
         'preserved_packaged_members':sum(x['action']=='preserved-packaged-source' for x in rows),
         'copied_bytes':needed_bytes,'elapsed_seconds':time.monotonic()-started,
         'packaged_files_unchanged':len(packaged),'complete_operational_file_inventory_exact':True,
         'production_origin_acquired':False,'support_reestablished':False,'rows':rows})
    print(json.dumps({'status':'PASS','members':len(rows),'copied_members':sum(x['action']=='copied-absent-runtime-member' for x in rows),'preserved_packaged_members':sum(x['action']=='preserved-packaged-source' for x in rows),'copied_bytes':needed_bytes,'seconds':time.monotonic()-started}),flush=True)
except Exception as exc:
    save('FAILURE.json',{'stage':'exact-support-copy','error':type(exc).__name__+': '+str(exc),'completed_members':len(rows),'completed_custody':rows,'retry':'not attempted'})
    raise
