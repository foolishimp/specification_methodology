"""Read-only byte/ref/config/default-store conservation against frozen Root guards."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import gzip,hashlib,json,os,stat,subprocess

R=Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021')
PROOF=R/'proof'
REFERENCE=json.loads((PROOF/'trial-guard-reference.json').read_text())
GUARD_PATH=Path(REFERENCE['path']);RAW=GUARD_PATH.read_bytes()
assert hashlib.sha256(RAW).hexdigest()==REFERENCE['sha256']
BASELINE=json.loads(gzip.decompress(RAW));failures=[];counts=Counter()

def require(condition,message):
    if not condition:failures.append(message)

def check_entry(path,row):
    kind=row['kind'];counts[kind]+=1
    if kind=='absent':
        require(not path.exists() and not path.is_symlink(),f'expected absent: {path}');return
    try: info=path.lstat()
    except FileNotFoundError:failures.append(f'missing: {path}');return
    if 'mode' in row:require(oct(stat.S_IMODE(info.st_mode))==row['mode'],f'mode changed: {path}')
    if kind=='file':
        require(stat.S_ISREG(info.st_mode),f'file kind changed: {path}')
        if not stat.S_ISREG(info.st_mode):return
        raw=path.read_bytes();require(len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'],f'bytes changed: {path}')
    elif kind=='symlink':require(path.is_symlink() and os.readlink(path)==row['target'],f'symlink changed: {path}')
    elif kind=='directory':require(stat.S_ISDIR(info.st_mode),f'directory changed: {path}')
    else:failures.append(f'unknown guard kind {kind}: {path}')

def run(repo,args):
    return subprocess.run(['git','--no-optional-locks',*args],cwd=repo,check=True,capture_output=True).stdout

repos={}
for name in ['owning_repo','common_worktree']:
    row=BASELINE[name];root=Path(row['path'])
    for rel,entry in row['files'].items():check_entry(root/rel,entry)
    for entry in row['git_metadata'].values():check_entry(Path(entry['path']),entry)
    head=run(root,['rev-parse','HEAD']).decode().strip();require(head==row['head'],name+' HEAD changed')
    refs=run(root,['for-each-ref','--format=%(refname) %(objectname) %(*objectname)'])
    require(hashlib.sha256(refs).hexdigest()==row['refs_sha256'],name+' refs changed')
    status_bytes=run(root,['status','--porcelain=v1','-z','--untracked-files=all'])
    require(hashlib.sha256(status_bytes).hexdigest()==row['status_sha256'],name+' status changed')
    worktree_diff=run(root,['diff','--binary']);index_diff=run(root,['diff','--cached','--binary'])
    require(hashlib.sha256(worktree_diff).hexdigest()==row['worktree_diff_sha256'],name+' worktree diff changed')
    require(hashlib.sha256(index_diff).hexdigest()==row['index_diff_sha256'],name+' index diff changed')
    repos[name]={'paths':len(row['files']),'tracked_count':row['tracked_count'],'untracked_count':row['untracked_count'],'head':head,'refs_status_metadata_and_diffs_unchanged':True}
for name in ['default_store','prepared_representation']:
    row=BASELINE[name];root=Path(row['path']);check_entry(root,row['root'])
    for rel,entry in row['entries'].items():check_entry(root/rel,entry)
for path,entry in BASELINE['configuration_files'].items():check_entry(Path(path),entry)
cli=BASELINE['cli_entrypoint'];check_entry(Path(cli['path']),cli['entry']);check_entry(Path(cli['resolved_path']),cli['resolved'])
tool=BASELINE['toolchain_python_sources']
for rel,entry in tool['files'].items():check_entry(Path(tool['path'])/rel,entry)

# Current activation's exact app/default-store set and the 23 preexisting tracked bytes.
own=json.loads((PROOF/'original-guards.json').read_text())
for field,pathkey in [('application_files','original_app'),('default_store_files','default_store')]:
    root=Path(own[pathkey]);expected=own[field]
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() or p.is_symlink()}
    require(actual==set(expected),field+' path set changed')
    for rel,entry in expected.items():
        p=root/rel
        if 'symlink' in entry:require(p.is_symlink() and os.readlink(p)==entry['symlink'],f'own symlink changed: {p}')
        else:
            raw=p.read_bytes();require(len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256'],f'own bytes changed: {p}')
repo=Path(BASELINE['owning_repo']['path'])
for rel,entry in own['tracked_files'].items():
    raw=(repo/rel).read_bytes();require(len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256'],f'tracked bytes changed: {rel}')
result={'status':'passed' if not failures else 'failed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'root_baseline_guard':REFERENCE,'repositories':repos,'root_baseline_entries_checked_by_kind':dict(counts),'own_application_files_unchanged':len(own['application_files']),'own_default_store_files_unchanged':len(own['default_store_files']),'preexisting_tracked_modifications_unchanged':len(own['tracked_files']),'configuration_files_unchanged':len(BASELINE['configuration_files']),'default_store_path':BASELINE['default_store']['path'],'failures':failures,'scope':'No original repository/app/common/default-store/config/ref writes; private STDO trial root not modified or recaptured'}
(PROOF/'original-guards-final.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));assert not failures,failures
