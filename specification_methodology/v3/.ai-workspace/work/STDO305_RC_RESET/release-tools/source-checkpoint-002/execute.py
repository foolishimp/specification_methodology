import hashlib,json,os,re,subprocess,time
from pathlib import Path
R=Path.cwd();O=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,x):(O/name).write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def git(*args,env=None):
 return subprocess.run(['git','-c','gc.auto=0','-c','maintenance.auto=false',*args],cwd=R,env=env,capture_output=True)
def checked(*args,env=None):
 p=git(*args,env=env);assert p.returncode==0,(args,p.stderr.decode());return p.stdout
plan_raw=(O/'PLAN.json').read_bytes();assert sha(plan_raw)=='55aa4fe1953e7ef4ec8f068b015225f248ec851226d62b61abf395ff5164d46e';plan=json.loads(plan_raw)
assert sha((R/plan['paths']['path']).read_bytes())==plan['paths']['sha256'];paths=json.loads((R/plan['paths']['path']).read_bytes())
assert sha((R/plan['nul']['path']).read_bytes())==plan['nul']['sha256']
assert checked('rev-parse','HEAD').decode().strip()==plan['head'];assert checked('symbolic-ref','HEAD').decode().strip()==plan['branch']
assert sha(checked('ls-files','-s','-z'))==plan['index_logical_sha256'];assert not checked('diff','--cached','--name-only')
assert os.statvfs(R).f_bavail*os.statvfs(R).f_frsize>=2*1024**3
expected={}
for row in paths['files']:
 p=R/row['path'];raw=p.read_bytes();mode='100755' if p.stat().st_mode&0o111 else '100644';assert not p.is_symlink();assert (sha(raw),len(raw),mode)==(row['sha256'],row['bytes'],row['git_mode']);expected[row['path']]=(mode,row['git_blob'])
for name in ['SOURCE_SELECTION.json','PATHS.json','stage-paths.z','PLAN.json']:
 p=O/name;raw=p.read_bytes();expected[p.relative_to(R).as_posix()]=('100644',hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())
assert set((O/'stage-paths.z').read_bytes().decode().strip('\0').split('\0'))==set(expected)
save('PRECONDITIONS.json',{'status':'matched','head':plan['head'],'index_logical_sha256':plan['index_logical_sha256'],'plan_sha256':sha(plan_raw),'stage_paths':len(expected),'free_bytes':os.statvfs(R).f_bavail*os.statvfs(R).f_frsize})
env=dict(os.environ);env['GIT_LITERAL_PATHSPECS']='1';started=time.time();checked('add','-f','--pathspec-from-file='+str(O/'stage-paths.z'),'--pathspec-file-nul',env=env)
actual_names=set(checked('diff','--cached','--name-only','-z').decode().strip('\0').split('\0'));assert actual_names==set(expected)
index={}
for item in checked('ls-files','-s','-z').split(b'\0'):
 if item:
  info,name=item.split(b'\t',1);mode,oid,stage=info.decode().split();assert stage=='0';index[name.decode()]=(mode,oid)
assert all(index[name]==value for name,value in expected.items())
p=git('diff','--cached','--check');(O/'diff-check.stdout').write_bytes(p.stdout);(O/'diff-check.stderr').write_bytes(p.stderr)
bad=[]
for line in p.stdout.decode().splitlines():
 match=re.match(r'(.+?):\d+: (?:trailing whitespace|new blank line at EOF|space before tab in indent)',line)
 if match:bad.append(match[1])
allowed=lambda name: '/.ai-workspace/work/' in name or '/representation/stdo-v3.0.5-rc.1/source/' in name
assert p.returncode in (0,2) and (p.returncode==0 or bad and all(allowed(name) for name in bad)),(p.returncode,bad,p.stdout.decode()[:3000])
save('WHITESPACE.json',{'returncode':p.returncode,'reported_paths':sorted(set(bad)),'disposition':'Exact sealed historical/source-copy evidence retained; no authored live source defect.'})
print('STAGED_VERIFIED',len(expected),round(time.time()-started,3),flush=True)
p=git('commit','-m',plan['commit_message']);(O/'commit.stdout').write_bytes(p.stdout);(O/'commit.stderr').write_bytes(p.stderr);assert p.returncode==0,p.stderr.decode()
commit=checked('rev-parse','HEAD').decode().strip();assert checked('show','-s','--format=%P',commit).decode().strip()==plan['head'];assert not checked('diff','--cached','--name-only')
readback={}
for item in checked('ls-tree','-r','-z',commit).split(b'\0'):
 if item:
  info,name=item.split(b'\t',1);mode,kind,oid=info.decode().split();readback[name.decode()]=(mode,oid)
assert all(readback[name]==value for name,value in expected.items())
save('RESULT.json',{'kind':'stdo.reviewed-source-checkpoint-result/1','status':'committed','commit':commit,'parent':plan['head'],'plan_sha256':sha(plan_raw),'stage_paths':len(expected),'staged_readback_exact':True,'source_immutable_target':commit,'elapsed_seconds':time.time()-started,'effects':'One local main commit only; no refs/tags, push, publication, install or global configuration effects.'})
print('SOURCE_CHECKPOINT',commit,flush=True)
