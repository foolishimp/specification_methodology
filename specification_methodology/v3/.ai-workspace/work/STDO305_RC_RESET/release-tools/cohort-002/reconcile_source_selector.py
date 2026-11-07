"""Root-authorized removal of one redundant source selector field before publication."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
R=Path.cwd();C=Path(__file__).resolve().parent;O=C/'manifest-reconciliation-002'
G=['git','-c','gc.auto=0','-c','maintenance.auto=false'];sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,input=None):
 p=subprocess.run([*G,*args],cwd=R,input=input,capture_output=True);assert p.returncode==0,(args,p.stderr.decode());return p.stdout
def load(p):return json.loads(p.read_bytes())
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
prior=load(C/'manifest-reconciliation-001/RESULT.json');parent=prior['commit'];oldrefs=prior['selected']
assert parent=='9c48bea849f23b5102caafff1a318472b590b0a8' and git('rev-parse','HEAD').decode().strip()==parent
assert not git('diff','--cached','--name-only') and not git('diff','--name-only')
assert load(O/'DIRECT_CHECKS.json')['status']=='passed'
assert os.statvfs(R).f_bavail*os.statvfs(R).f_frsize>=2*1024**3
raw=(R/'stack_release.json').read_bytes();assert sha(raw)==prior['manifest_sha256']
(O/'predecessor-stack_release.json').write_bytes(raw)
(O/'predecessor-commit.txt').write_bytes(git('cat-file','commit',parent))
value=json.loads(raw);assert value['source'].pop('bytes')==13899
configuration=load(R/value['native_preparation']['configuration']['path']);assert value['source']==configuration['source']
changed=(json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
eight={k:v for k,v in oldrefs.items() if k.startswith('refs/tags/') and '/archive/' not in k and not k.startswith('refs/tags/specification_methodology/')};assert len(eight)==8
for i,(name,oid) in enumerate(sorted(eight.items())):
 assert git('rev-parse',name).decode().strip()==oid
 (O/f'predecessor-tag-{i:02d}.txt').write_bytes(git('cat-file','tag',oid))
save(O/'RECONCILIATION.json',{'authority':'Root explicitly approved removing only optional B.source.bytes, preserving frozen configuration/native/source/proof and failed receipts, with exact unpublished eight-ref CAS.','parent':parent,'before_sha256':sha(raw),'after_sha256':sha(changed),'delta':{'/source/bytes':{'before':13899,'after':'absent'}},'predecessor_refs':eight,'direct_checks':'DIRECT_CHECKS.json'})
(R/'stack_release.json').write_bytes(changed)
selected={'stack_release.json',str(Path(__file__).relative_to(R)),str((C/'execute_publication_004.py').relative_to(R))}
for root in (O,C/'publication-execution/014-refs-successor',C/'manifest-reconciliation-001'):
 for p in root.rglob('*'):
  if p.is_file() and not p.is_symlink():selected.add(str(p.relative_to(R)))
tracked={x.decode() for x in git('ls-files','-z').split(b'\0') if x};changed_paths={x.decode() for x in git('diff','--name-only','-z').split(b'\0') if x}
selected={p for p in selected if p not in tracked or p in changed_paths}
# Preserved diagnostic whitespace is classified, not altered or reinterpreted as source.
selected.discard(str((C/'manifest-reconciliation-001/diff-check.txt').relative_to(R)))
nul=O/'stage-paths.z';selected.add(str(nul.relative_to(R)));nul.write_bytes(b''.join(p.encode()+b'\0' for p in sorted(selected)))
git('add','-f','--pathspec-from-file='+str(nul),'--pathspec-file-nul')
assert {x.decode() for x in git('diff','--cached','--name-only','-z').split(b'\0') if x}==selected
git('diff','--cached','--check')
(O/'commit.stdout').write_bytes(git('commit','-m','Conserve exact frozen RC native source selector'))
current=git('rev-parse','HEAD').decode().strip();assert git('show','-s','--format=%P',current).decode().strip()==parent
forms=load(C/'publication/OPERATION_TEMPLATES.json')
remote=git('ls-remote','--heads','--tags','https://github.com/foolishimp/specification_methodology.git');(O/'remote-before-cas.txt').write_bytes(remote)
observed={line.split('\t')[1]:line.split('\t')[0] for line in remote.decode().splitlines()}
assert all(observed.get(k)==v for k,v in forms['expected_remote'].items()) and all(observed.get(k)==v for k,v in forms['preserved_immutable_refs'].items())
tagger=git('var','GIT_COMMITTER_IDENT').decode().strip();newrefs={}
for category in ('cut_annotations','selector_annotations'):
 for product,row in forms[category].items():
  if row['ref'] not in eight:continue
  body='\n'.join([f'object {current}','type commit','tag '+row['ref'].removeprefix('refs/tags/'),'tagger '+tagger,'',*row['annotation_lines'],''])
  (O/(category+'-'+product+'.txt')).write_text(body);newrefs[row['ref']]=git('mktag',input=body.encode()).decode().strip()
lines=['start']+[f'update {name} {oid} {eight[name]}' for name,oid in sorted(newrefs.items())]+['prepare','commit','']
(O/'update-ref.stdin').write_text('\n'.join(lines));(O/'update-ref.stdout').write_bytes(git('update-ref','--stdin',input='\n'.join(lines).encode()))
selected_refs={**oldrefs,**newrefs,'refs/heads/main':current}
assert all(git('rev-parse',name).decode().strip()==oid for name,oid in selected_refs.items())
save(O/'RESULT.json',{'status':'reconciled','commit':current,'parent':parent,'manifest_sha256':sha(changed),'selected':selected_refs,'stage_paths':len(selected),'limits':'One optional selector key removed, eight unpublished peer annotations CAS-rebound; source/native/proof/archives/remote unchanged.'})
sys.path.insert(0,str(R/'scripts'));import check_stack_release as api,stable_stack_release as s
ref_check=s.ref_graph(R,value,current,'refs','origin',api)
save(O/'REF_PREFLIGHT.json',{'status':'passed','operation':'existing stable_stack_release.ref_graph after exact successor commit and local CAS','commit':current,'qualified_push_sha256':ref_check['qualified_push_sha256']})
print('RECONCILED',current,sha(changed),flush=True)
