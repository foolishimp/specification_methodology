"""Resume only after preserved diagnostic whitespace classification; no original rewrite."""
import hashlib,json,os,subprocess,time
from pathlib import Path
R=Path.cwd();C=Path(__file__).resolve().parent;O=C/'manifest-reconciliation-001'
G=['git','-c','gc.auto=0','-c','maintenance.auto=false'];sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,input=None):
 p=subprocess.run([*G,*args],cwd=R,input=input,capture_output=True);assert p.returncode==0,(args,p.stderr.decode());return p.stdout
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
def load(p):return json.loads(p.read_bytes())
assert git('rev-parse','HEAD').decode().strip()=='0e17859eeb32940e5285e7e5754575f558462c52'
plan=load(O/'PLAN.json');assert sha((R/'stack_release.json').read_bytes())==plan['after_sha256']
selected={x.decode() for x in (O/'stage-paths.z').read_bytes().split(b'\0') if x}
assert {x.decode() for x in git('diff','--cached','--name-only','-z').split(b'\0') if x}==selected
expected=str((C/'final-carrier/diff-check.stdout').relative_to(R))
check=subprocess.run([*G,'diff','--cached','--check'],cwd=R,capture_output=True)
lines=check.stdout.decode().splitlines();headers=[line for line in lines if ': trailing whitespace.' in line or ': new blank line at EOF.' in line]
assert check.returncode==2 and headers and all(line.startswith(expected+':') for line in headers),lines
save(O/'DIAGNOSTIC_CLASSIFICATION.json',{'kind':'stdo.preserved-evidence-whitespace/1','original_check_sha256':sha((O/'diff-check.txt').read_bytes()),'exact_affected_path':expected,'classification':'Unmodified frozen diagnostic output embeds earlier preserved evidence whitespace; no live source error. Existing Root custody policy applies.','warnings':len(headers),'publication_operator_successor':'execute_publication_003.py selects exact reconciled ref map rather than the original pre-reconciliation map; no gate change.'})
extra=[str((O/'DIAGNOSTIC_CLASSIFICATION.json').relative_to(R)),str(Path(__file__).relative_to(R)),str((C/'execute_publication_003.py').relative_to(R))]
git('add','--',*extra)
assert not git('diff','--name-only')
assert os.statvfs(R).f_bavail*os.statvfs(R).f_frsize>=2*1024**3
out=git('commit','-m','Correct RC cohort manifest status before publication');(O/'commit.stdout').write_bytes(out)
current=git('rev-parse','HEAD').decode().strip();assert git('show','-s','--format=%P',current).decode().strip()==plan['parent']
forms=load(C/'publication/OPERATION_TEMPLATES.json');oldrefs=load(C/'publication-execution/LOCAL_REFS.json')['selected'];eight={row['ref']:row['object'] for row in plan['predecessor_tags']}
remote=git('ls-remote','--heads','--tags','https://github.com/foolishimp/specification_methodology.git');(O/'remote-before-cas.txt').write_bytes(remote)
observed={line.split('\t')[1]:line.split('\t')[0] for line in remote.decode().splitlines()}
assert all(observed.get(k)==v for k,v in forms['expected_remote'].items())
assert all(observed.get(k)==v for k,v in forms['preserved_immutable_refs'].items())
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
save(O/'RESULT.json',{'status':'reconciled','commit':current,'parent':plan['parent'],'manifest_sha256':plan['after_sha256'],'stage_paths':len(selected)+len(extra),'selected':selected_refs,'limits':'Only exact one-field manifest metadata and eight unpublished peer annotations changed; no source/proof/native/archive/remote effect.'})
print('RECONCILED',current,plan['after_sha256'],flush=True)
