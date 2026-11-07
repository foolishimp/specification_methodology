"""Root-selected one-field unpublished carrier reconciliation; preserve all originals."""
import hashlib,json,os,subprocess,time
from pathlib import Path
R=Path.cwd();C=Path(__file__).resolve().parent;O=C/'manifest-reconciliation-001'
G=['git','-c','gc.auto=0','-c','maintenance.auto=false'];sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,input=None):
 p=subprocess.run([*G,*args],cwd=R,input=input,capture_output=True);assert p.returncode==0,(args,p.stderr.decode());return p.stdout
def ref(p):
 b=p.read_bytes();return {'path':str(p.relative_to(R)),'sha256':sha(b),'bytes':len(b)}
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
 return ref(p)
def load(p):return json.loads(p.read_bytes())
assert git('rev-parse','HEAD').decode().strip()=='0e17859eeb32940e5285e7e5754575f558462c52'
assert not git('diff','--cached','--name-only');assert not git('diff','--name-only')
assert os.statvfs(R).f_bavail*os.statvfs(R).f_frsize>=2*1024**3
O.mkdir(exist_ok=False)
forms=load(C/'publication/OPERATION_TEMPLATES.json');oldrefs=load(C/'publication-execution/LOCAL_REFS.json')['selected']
remote=git('ls-remote','--heads','--tags',forms['commands'][4].get('repository_url','https://github.com/foolishimp/specification_methodology.git'))
(O/'remote-before.txt').write_bytes(remote);observed={line.split('\t')[1]:line.split('\t')[0] for line in remote.decode().splitlines()}
assert all(observed.get(k)==v for k,v in forms['expected_remote'].items())
assert all(observed.get(k)==v for k,v in forms['preserved_immutable_refs'].items())
eight={k:v for k,v in oldrefs.items() if k.startswith('refs/tags/') and '/archive/' not in k and not k.startswith('refs/tags/specification_methodology/')}
assert len(eight)==8
custody=[]
for i,(name,oid) in enumerate(sorted(eight.items())):
 assert git('rev-parse',name).decode().strip()==oid
 p=O/'predecessor'/f'tag-{i:02d}.txt';p.parent.mkdir(exist_ok=True);p.write_bytes(git('cat-file','tag',oid));custody.append({'ref':name,'object':oid,'raw':ref(p)})
old=(R/'stack_release.json').read_bytes();assert sha(old)=='5bf81643453e56083cb21e3e82a18934c34888ceda318d63312c8f77c7affe94'
(O/'predecessor/stack_release.json').write_bytes(old)
(O/'predecessor/carrier-commit.txt').write_bytes(git('cat-file','commit','0e17859eeb32940e5285e7e5754575f558462c52'))
value=json.loads(old);value['cohort']['status']='candidate';new=(json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
save(O/'PLAN.json',{'kind':'stdo.manifest-assembly-reconciliation/1','authority':'Root explicitly assigned one literal correction and unpublished-only eight-ref CAS; original failed gate and D retained.','parent':'0e17859eeb32940e5285e7e5754575f558462c52','before_sha256':sha(old),'after_sha256':sha(new),'delta':{'/cohort/status':['complete','candidate']},'static_check':'Corrected in-memory value passed every existing stable_stack_release.check_shape predicate before effects.','predecessor_tags':custody,'remote':ref(O/'remote-before.txt'),'unchanged':'All Product/source/native/component/qualification records, mathematical evidence, native tag and five archive refs; no remote mutation here.'})
(R/'stack_release.json').write_bytes(new)
selected={'stack_release.json',str((C/'execute_publication_002.py').relative_to(R)),str(Path(__file__).relative_to(R))}
for root in (O,C/'publication-execution',C/'final-carrier'):
 for p in root.rglob('*'):
  if p.is_file() and not p.is_symlink():selected.add(str(p.relative_to(R)))
tracked={x.decode() for x in git('ls-files','-z').split(b'\0') if x};changed={x.decode() for x in git('diff','--name-only','-z').split(b'\0') if x}
selected={p for p in selected if p not in tracked or p in changed}
nul=O/'stage-paths.z';selected.add(str(nul.relative_to(R)));nul.write_bytes(b''.join(p.encode()+b'\0' for p in sorted(selected)))
git('add','-f','--pathspec-from-file='+str(nul),'--pathspec-file-nul')
assert {p.decode() for p in git('diff','--cached','--name-only','-z').split(b'\0') if p}==selected
check=subprocess.run([*G,'diff','--cached','--check'],cwd=R,capture_output=True);(O/'diff-check.txt').write_bytes(check.stdout);assert check.returncode==0,check.stdout.decode()
out=git('commit','-m','Correct RC cohort manifest status before publication');(O/'commit.stdout').write_bytes(out)
current=git('rev-parse','HEAD').decode().strip();assert git('show','-s','--format=%P',current).decode().strip()=='0e17859eeb32940e5285e7e5754575f558462c52'
tagger=git('var','GIT_COMMITTER_IDENT').decode().strip();newrefs={}
for category in ('cut_annotations','selector_annotations'):
 for product,row in forms[category].items():
  if row['ref'] not in eight:continue
  body='\n'.join([f'object {current}','type commit','tag '+row['ref'].removeprefix('refs/tags/'),'tagger '+tagger,'',*row['annotation_lines'],''])
  (O/(category+'-'+product+'.txt')).write_text(body)
  newrefs[row['ref']]=git('mktag',input=body.encode()).decode().strip()
lines=['start']+[f'update {name} {oid} {eight[name]}' for name,oid in sorted(newrefs.items())]+['prepare','commit','']
(O/'update-ref.stdin').write_text('\n'.join(lines));(O/'update-ref.stdout').write_bytes(git('update-ref','--stdin',input='\n'.join(lines).encode()))
assert all(git('rev-parse',name).decode().strip()==oid for name,oid in newrefs.items())
assert all(git('rev-parse',name).decode().strip()==oid for name,oid in oldrefs.items() if name not in eight and name!='refs/heads/main')
selected_refs={**oldrefs,**newrefs,'refs/heads/main':current}
save(O/'RESULT.json',{'status':'reconciled','commit':current,'parent':'0e17859eeb32940e5285e7e5754575f558462c52','manifest_sha256':sha(new),'stage_paths':len(selected),'selected':selected_refs,'limits':'Only exact one-field manifest metadata and eight unpublished peer annotations changed; no source/proof/native/archive/remote effect.'})
print('RECONCILED',current,sha(new),flush=True)
