"""Run only selected immutable packaging operations; stop on first failure."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

D = Path(__file__).resolve().parent
T = D.parents[1]
REPO = T.parents[3]
W = Path('/private/tmp/ac-t013-lean-package-001')
PYTHON = '/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12'
TOOL = T / 'package/repair-002/package_source.py'
SELECTION = T / 'package/selection-001/SOURCE_PACKAGE.json'
MANIFEST = 'e981245097c06f693fcbe89565d5724db2103982fdb7891e8413a8a6cdc86ee4'

def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def save(name, value):
    with (D / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

records = []
steps = [
 ('build', TOOL, ['build', '--source-root', REPO, '--selection', SELECTION, '--output', W/'bundle']),
 ('verify-bundle', TOOL, ['verify-tree', '--tree', W/'bundle']),
 ('archive', TOOL, ['archive', '--tree', W/'bundle', '--output', W/'source-package.tar']),
 ('verify-archive', TOOL, ['verify-archive', '--archive', W/'source-package.tar']),
 ('extract-pristine', TOOL, ['extract', '--archive', W/'source-package.tar', '--output', W/'pristine']),
 ('verify-pristine', TOOL, ['verify-tree', '--tree', W/'pristine']),
 ('repack-pristine', W/'pristine/package_source.py', ['archive', '--tree', W/'pristine', '--output', W/'source-repack.tar']),
 ('verify-repack', TOOL, ['verify-archive', '--archive', W/'source-repack.tar']),
 ('extract-operational', TOOL, ['extract', '--archive', W/'source-package.tar', '--output', W/'operational']),
 ('verify-operational-source', TOOL, ['verify-tree', '--tree', W/'operational'])]
try:
    for label, tool, args in steps:
        assert sha(tool) == '9907d7245372af188276384cc5ab710b9a77328b92047a277a94e1ed5ab40117'
        command = [PYTHON, '-I', '-S', '-B', str(tool), *(str(x) for x in args), '--manifest-sha256', MANIFEST]
        start = time.monotonic()
        process = subprocess.run(command, cwd=W, capture_output=True, timeout=60, check=False)
        for suffix, raw in (('stdout', process.stdout), ('stderr', process.stderr)):
            with (D / (label + '.' + suffix)).open('xb') as stream: stream.write(raw)
        item = {'step': label, 'argv': command, 'returncode': process.returncode,
                'seconds': time.monotonic() - start, 'stdout_sha256': sha(D/(label+'.stdout')),
                'stderr_sha256': sha(D/(label+'.stderr'))}
        records.append(item)
        assert process.returncode == 0, label + ': ' + process.stderr.decode()
        item['returned'] = json.loads(process.stdout)
        print(json.dumps({'step':label,'status':item['returned']['status'],'seconds':item['seconds']}), flush=True)
    archive_sha = sha(W/'source-package.tar')
    assert sha(W/'source-repack.tar') == archive_sha
    with (D/'source-package.tar').open('xb') as dest, (W/'source-package.tar').open('rb') as source:
        while data := source.read(1024 * 1024): dest.write(data)
    with (D/'SOURCE_PACKAGE.json').open('xb') as dest: dest.write(SELECTION.read_bytes())
    assert sha(D/'source-package.tar') == archive_sha
    assert sha(D/'SOURCE_PACKAGE.json') == MANIFEST
    save('PACKAGE.json', {'schema':'a_c.T013.source-package-delivery/1','status':'PASS',
         'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_root':str(REPO),
         'manifest_sha256':MANIFEST,'source_member_count':65,'archive_member_count':66,
         'archive_sha256':archive_sha,'archive_bytes':(W/'source-package.tar').stat().st_size,
         'repacked_archive_sha256':sha(W/'source-repack.tar'),'byte_identical_repacking':True,
         'pristine_tree':str(W/'pristine'),'operational_tree':str(W/'operational'),
         'retained_archive':str(D/'source-package.tar'),'records':records})
    print(json.dumps({'status':'PASS','archive_sha256':archive_sha,'archive_bytes':(W/'source-package.tar').stat().st_size,'identical_repacking':True}),flush=True)
except Exception as exc:
    save('FAILURE.json',{'stage':'packaging','error':type(exc).__name__+': '+str(exc),'completed_steps':records,'retry':'not attempted'})
    raise
