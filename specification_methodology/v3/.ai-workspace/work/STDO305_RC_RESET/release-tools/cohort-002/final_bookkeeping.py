"""Prepare or execute the authorized final bookkeeping-only main commit/push."""
import hashlib,json,os,re,subprocess,sys,time
from pathlib import Path
R=Path.cwd();C=Path(__file__).resolve().parent;Q=C.parent.parent;P=Q/'public-qualification-001';O=Q/'closure'
G=['git','-c','gc.auto=0','-c','maintenance.auto=false'];sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,input=None):
 p=subprocess.run([*G,*args],cwd=R,input=input,capture_output=True);assert p.returncode==0,(args,p.stderr.decode());return p.stdout
def load(p):return json.loads(p.read_bytes())
def ref(p):
 b=p.read_bytes();return {'path':str(p.relative_to(R)),'sha256':sha(b),'bytes':len(b),'mode':'100755' if p.stat().st_mode&0o111 else '100644'}
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
 return ref(p)
latest=load(P/'LATEST_CONFIRMED.json');assert latest['status']=='confirmed_latest'
carrier=latest['carrier'];selection=load(C/'manifest-reconciliation-002/RESULT.json')['selected'];forms=load(C/'publication/OPERATION_TEMPLATES.json')
assert selection['refs/heads/main']==carrier
assert os.statvfs(R).f_bavail*os.statvfs(R).f_frsize>=2*1024**3
def remote():
 raw=git('ls-remote','--heads','--tags','https://github.com/foolishimp/specification_methodology.git')
 return raw,{line.split('\t')[1]:line.split('\t')[0] for line in raw.decode().splitlines()}
if sys.argv[1]=='prepare':
 assert git('rev-parse','HEAD').decode().strip()==carrier and not git('diff','--cached','--name-only')
 tracked={p.decode() for p in git('ls-files','-z').split(b'\0') if p}
 changes={p.decode() for p in git('diff','--name-only','-z').split(b'\0') if p}
 navigation={'README.md','specification_methodology/v3/README.md','specification_methodology/v3/specification/GOALS.md'}
 assert changes==navigation,changes
 manifest=load(R/'stack_release.json');protected={r['path']:r for product in manifest['products'].values() for r in product['subject']['members']}
 assert not navigation.intersection(protected)
 for name,row in protected.items():
  p=R/name;actual=ref(p);assert not p.is_symlink() and actual['sha256']==row['sha256'] and actual['bytes']==row['bytes'],name
  if 'mode' in row:assert actual['mode']==row['mode'],name
 assert sha((R/'stack_release.json').read_bytes())==load(C/'manifest-reconciliation-002/RESULT.json')['manifest_sha256']
 assert (R/'specification_methodology/v3/stdo_3.json').read_bytes()==git('show',carrier+':specification_methodology/v3/stdo_3.json')
 selected=set(navigation);excluded=[]
 for root in (P,C,O):
  for p in root.rglob('*'):
   if not p.is_file() and not p.is_symlink():continue
   name=str(p.relative_to(R))
   if '__pycache__' in p.parts or p.suffix=='.pyc' or p.name=='local-origin.json' or ('proof-retention/archives' in name and p.name=='full.zip'):
    excluded.append({'path':name,'reason':'Preserved local duplicate archive, bytecode, or private origin hint; portable proof descriptor/parts and actual result records are selected.'});continue
   assert not p.is_symlink(),name
   if name not in tracked or name in changes:selected.add(name)
 for p in (Q/'RESULT.json',Q/'RELEASED.md'):selected.add(str(p.relative_to(R)))
 assert (P/'ordinary-custody/INDEX.json').is_file(), 'Await closed ordinary public inventory; no extra execution required'
 rows=[]
 for name in sorted(selected):
  row=ref(R/name);assert row['bytes']<100*1024**2,name;rows.append(row)
 paths_ref=save(O/'PATHS.json',{'kind':'stdo.exact-bookkeeping-paths/1','parent':carrier,'files':rows,'exclusions':excluded,'protected_product_members':len(protected),'source_builder_unchanged':True})
 controls=[str((O/n).relative_to(R)) for n in ('PATHS.json','stage-paths.z','PLAN.json')]
 (O/'stage-paths.z').write_bytes(b''.join(name.encode()+b'\0' for name in sorted(selected|set(controls))))
 logical=git('ls-files','--stage','-z')
 plan=save(O/'PLAN.json',{'kind':'stdo.final-bookkeeping-transaction/1','status':'ready','parent':carrier,'paths':paths_ref,'nul':ref(O/'stage-paths.z'),
  'logical_index_sha256':sha(logical),'stage_paths':len(selected|set(controls)),'free_space_floor_bytes':2*1024**3,
  'preserve':{'manifest_sha256':sha((R/'stack_release.json').read_bytes()),'refs':{k:v for k,v in selection.items() if k!='refs/heads/main'},'historical':forms['preserved_immutable_refs']},
  'commands':[['git','add','-f','--pathspec-from-file='+str(O/'stage-paths.z'),'--pathspec-file-nul'],[*G,'commit','-m','Record public STDO 3.0.5 RC1 qualification and closure'],[*G,'push','--atomic','--force-with-lease=refs/heads/main:'+carrier,'https://github.com/foolishimp/specification_methodology.git','ACTUAL_BOOKKEEPING_COMMIT:refs/heads/main']],
  'authority':'Owner/Root standing final bookkeeping grant after actual public gate and same-ID Latest. One main commit/push; no immutable cut, selector, archive, native, asset, builder, or unrelated work mutation. Per-command auto-GC/maintenance disabled; no cleanup.'})
 print(json.dumps({'plan':plan,'paths':paths_ref,'nul':ref(O/'stage-paths.z')}),flush=True)
elif sys.argv[1]=='execute':
 assert sha((O/'PLAN.json').read_bytes())==sys.argv[2]
 plan=load(O/'PLAN.json');assert git('rev-parse','HEAD').decode().strip()==carrier and sha(git('ls-files','--stage','-z'))==plan['logical_index_sha256']
 assert not git('diff','--cached','--name-only')
 for row in load(O/'PATHS.json')['files']:assert ref(R/row['path'])==row,row['path']
 raw,before=remote();(O/'remote-before.txt').write_bytes(raw)
 assert all(before.get(k)==v for k,v in selection.items()) and all(before.get(k)==v for k,v in forms['preserved_immutable_refs'].items())
 git('add','-f','--pathspec-from-file='+str(O/'stage-paths.z'),'--pathspec-file-nul')
 staged={x for x in git('diff','--cached','--name-only','-z').split(b'\0') if x};expected={x for x in (O/'stage-paths.z').read_bytes().split(b'\0') if x};assert staged==expected
 check=subprocess.run([*G,'diff','--cached','--check'],cwd=R,capture_output=True);(O/'diff-check.txt').write_bytes(check.stdout)
 if check.returncode:
  warnings=[line for line in check.stdout.decode().splitlines() if re.match(r'^[^+].+:\d+: ',line)]
  assert check.returncode==2 and warnings
  for line in warnings:
   path=re.split(r':\d+: ',line,1)[0];assert path.startswith(str(Q.relative_to(R))+'/') and Path(path).suffix in ('.txt','.stdout','.stderr','.log'),line
 save(O/'DIFF_CHECK_CLASSIFICATION.json',{'returncode':check.returncode,'basis':'Live source/navigation must be clean. Only byte-preserved execution log/diagnostic whitespace under the release evidence territory is admitted; original bytes unchanged.','stdout':ref(O/'diff-check.txt')})
 (O/'commit.stdout').write_bytes(git('commit','-m','Record public STDO 3.0.5 RC1 qualification and closure'))
 commit=git('rev-parse','HEAD').decode().strip();assert git('show','-s','--format=%P',commit).decode().strip()==carrier
 assert not git('diff','--cached','--name-only') and not git('diff','--name-only')
 assert sha((R/'stack_release.json').read_bytes())==plan['preserve']['manifest_sha256']
 assert all(git('rev-parse',name).decode().strip()==oid for name,oid in plan['preserve']['refs'].items())
 argv=[*G,'push','--atomic','--force-with-lease=refs/heads/main:'+carrier,'https://github.com/foolishimp/specification_methodology.git',commit+':refs/heads/main']
 save(O/'push-invocation.json',{'argv':argv,'cwd':str(R),'parent':carrier,'commit':commit})
 print('BOOKKEEPING_COMMIT',commit,flush=True)
 with (O/'push.stdout').open('xb') as out,(O/'push.stderr').open('xb') as err:result=subprocess.run(argv,cwd=R,stdout=out,stderr=err)
 save(O/'push-execution.json',{'returncode':result.returncode,'stdout':ref(O/'push.stdout'),'stderr':ref(O/'push.stderr'),'commit':commit})
 assert result.returncode==0,'Uncertain/failed push: retain and reconcile; no automatic retry.'
 raw,after=remote();(O/'remote-after.txt').write_bytes(raw)
 assert after.get('refs/heads/main')==commit and all(after.get(k)==v for k,v in plan['preserve']['refs'].items()) and all(after.get(k)==v for k,v in forms['preserved_immutable_refs'].items())
 git('fetch','--no-tags','origin','main:refs/remotes/origin/main')
 assert git('rev-parse','origin/main').decode().strip()==commit
 assert git('rev-list','--left-right','--count','HEAD...origin/main').decode().strip()=='0\t0'
 result=save(O/'GIT_COMPLETION.json',{'status':'pushed_verified','bookkeeping_commit':commit,'release_carrier':carrier,'remote_main':after['refs/heads/main'],'tracking_main':commit,'ahead_behind':[0,0],'immutable_refs_unchanged':plan['preserve']['refs'],'limits':'Selected source/navigation/evidence is committed and pushed. Unrelated inherited artifacts, private origins/runtime/cache and duplicate proof ZIPs remain preserved locally; no clean-worktree claim.'})
 print('GIT_COMPLETION',result['sha256'],commit,flush=True)
else:raise ValueError('prepare or execute required')
