"""Select only closed reviewed source and its ordinary custody; no Git effects."""
import hashlib,json,os,stat,subprocess
from pathlib import Path
R=Path.cwd();W=R/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET/release-tools';T=W.parent/'tools-skills';P=R/'specification_methodology/v3/.ai-workspace/work/STDO305_POST_RELEASE_CORRECTIONS';OUT=W/'source-checkpoint-001'

def load(p):return json.loads(p.read_bytes())
def digest(raw):return hashlib.sha256(raw).hexdigest()
def put(p,value):
 p.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n');return {'path':p.relative_to(R).as_posix(),'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size}
def git(*args):return subprocess.check_output(['git','--no-optional-locks',*args],cwd=R)
OUT.mkdir(exist_ok=True)
# Each later source slice explicitly supersedes matching earlier source pins.
source={}
def add(rows):
 for row in rows:source[row['path']]=row
add(load(P/'skills/FREEZE.json')['source']);add(load(P/'release-docs/FREEZE.json')['source_and_derived'])
add(load(W/'profile-review-001/FREEZE.json')['source'])
add(load(T/'PORTABLE_003.json')['files']);add(load(T/'SOURCE_FREEZE_003.json')['source'])
x=load(T/'REBIND_FREEZE_004.json');add(x['source']);add(x['outputs'])
add([row['source'] for row in load(T/'REBIND_SOURCE_SUCCESSOR_005.json')['changes']])
add(load(W/'guide-projection-review-002/FREEZE.json')['source']);add(load(W/'rebind-consumer-review-001/FREEZE.json')['source'])
for name,row in source.items():
 p=R/name;assert p.is_file() and not p.is_symlink();raw=p.read_bytes();assert digest(raw)==row['sha256'],name
selected=set(source)
for root in [P,W]:
 for p in root.rglob('*'):
  if p.is_file() and not p.is_relative_to(OUT):
   assert not p.is_symlink() and p.suffix!='.pyc',p;selected.add(p.relative_to(R).as_posix())
allowed_groups={'model-rebind-001','model-rebind-002','model-rebind-003','model-rebind-004','native-profile-tests-001','native-target-tests-002','profile-wording-002','rebind-docs-005','reset-preimage','reviewed-preimage','skills-tests-001','upstream-version-003'}
allowed_files={'ACTIVATION.json','DESIGN.json','PORTABLE.json','PORTABLE_002.json','PORTABLE_003.json','PRIOR_PATCH_CUSTODY.json','REBIND_FREEZE_004.json','REBIND_SOURCE_SUCCESSOR_005.json','SOURCE_FREEZE_001.json','SOURCE_FREEZE_002.json','SOURCE_FREEZE_003.json','SOURCE_PREIMAGE.json','basis-stdo_a_c.json','basis-stdo_representation.json','basis-stdo_skills.json','record_rebind_004.py'}
for p in T.rglob('*'):
 if p.is_file() and (p.relative_to(T).parts[0] in allowed_groups or p.parent==T and p.name in allowed_files):
  assert not p.is_symlink() and p.suffix!='.pyc';selected.add(p.relative_to(R).as_posix())
# Current package's original sixteen source files, plus its new manifest.
for row in load(R/'stdo_skills/release/3.0.5-rc.1/manifest.json')['files']:selected.add('stdo_skills/'+row['path'])
index=git('ls-files','-s','-z');index_rows={}
for item in index.split(b'\0'):
 if item:
  meta,name=item.split(b'\t',1);mode,oid,stage=meta.decode().split();assert stage=='0';index_rows[name.decode()]={'git_mode':mode,'git_blob':oid}
assert not git('diff','--cached','--name-only')
head=git('rev-parse','HEAD').decode().strip();assert head=='6edfffb2f8a35b244782749383fb19105d9227d9';assert git('symbolic-ref','HEAD').decode().strip()=='refs/heads/main'
rows=[];unchanged=[]
for name in sorted(selected):
 p=R/name;mode=p.lstat().st_mode;assert stat.S_ISREG(mode),name;raw=p.read_bytes();assert len(raw)<100*1024*1024,name
 row={'path':name,'sha256':digest(raw),'bytes':len(raw),'git_mode':'100755' if mode&0o111 else '100644','git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'preimage':index_rows.get(name)}
 if row['preimage']=={k:row[k] for k in ('git_mode','git_blob')}:unchanged.append(name)
 else:rows.append(row)
source_ref=put(OUT/'SOURCE_SELECTION.json',{'source':[{k:v for k,v in row.items() if k in {'path','sha256','bytes'}} for name,row in sorted(source.items())],'unchanged_selected_paths':unchanged,'excluded':['All in-progress or newly closed construction proof/Graphify/Axiom006 receipts reserved for later payload checkpoint','All unrelated pre-existing untracked artifacts','External runtime/dependency/private origins and raw compiled evidence'],'source_checkpoint_only':True})
paths_ref=put(OUT/'PATHS.json',{'files':rows,'bytes':sum(x['bytes'] for x in rows),'largest':max(rows,key=lambda x:x['bytes']),'head':head,'index_logical_sha256':digest(index)})
controls=[OUT/name for name in ('SOURCE_SELECTION.json','PATHS.json','stage-paths.z','PLAN.json')]
names=sorted([row['path'] for row in rows]+[p.relative_to(R).as_posix() for p in controls]);assert len(names)==len(set(names));nul=b'\0'.join(n.encode() for n in names)+b'\0';(OUT/'stage-paths.z').write_bytes(nul)
plan={'kind':'stdo.reviewed-source-checkpoint/1','authority':'Owner-authorized unadopted305 reset and Root source-checkpoint assignment; execute only after exact guide/projection and rebind consumer reviews are satisfied.','head':head,'branch':'refs/heads/main','index_logical_sha256':digest(index),'source':source_ref,'paths':paths_ref,'nul':{'path':(OUT/'stage-paths.z').relative_to(R).as_posix(),'sha256':digest(nul),'bytes':len(nul)},'stage_paths':len(names),'commit_message':'Establish reviewed STDO 3.0.5-rc.1 source and coordinate binding','effects':['Stage exact selected paths using NUL pathspec; verify complete staged object/mode set','Commit once on main with sole parent preimage; no push or tag at this source checkpoint'],'required_reviews':['guide-projection-review-002/FREEZE.json','rebind-consumer-review-001/FREEZE.json','Tools source003 and rebind004/doc005'],'whitespace':'Authored live source defects stop. Exact frozen historical/source-copy/evidence whitespace is retained and classified, not edited.','limits':'Not a native or public release; new documentation links will select the actual resulting immutable source commit.'}
plan_ref=put(OUT/'PLAN.json',plan);print(json.dumps({'plan':plan_ref,'paths':paths_ref,'nul':plan['nul'],'payload_files':len(rows),'stage_files':len(names),'bytes':sum(x['bytes'] for x in rows),'largest':max(rows,key=lambda x:x['bytes'])},indent=2))
