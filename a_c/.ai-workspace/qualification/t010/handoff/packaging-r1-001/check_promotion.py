"""Scoped copy/vector/link and reconciled preservation checks; no qualification replay."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import gzip,hashlib,json,os,re,stat,subprocess
B=Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';H=B/'.ai-workspace/qualification/t010/handoff/packaging-r1-001';R=Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021');V=Path('/Users/jim/tmp/a_c-common-rc1-packaging-review-20261021')
REPAIR=B/'.ai-workspace/qualification/t010/packaging/repair-002';REVIEW=B/'.ai-workspace/qualification/t010/package-review/packaging-r1-001'
ID='a_c-stdo-v3-common-35fb4824-packaging-r1';counts=Counter()
def ident(p):
 raw=p.read_bytes();return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def save(p,value):p.write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
def vector(root):return [{'path':p.relative_to(root).as_posix(),**ident(p)} for p in sorted(root.rglob('*')) if p.is_file()]
applied=json.loads((H/'applied-promotion-manifest.json').read_text());review=json.loads((H/'review-copy-vector.json').read_text());closed=json.loads((R/'proof/CLOSED.json').read_text())
for row in applied['entries']:
 assert ident(Path(row['destination']))=={k:row[k] for k in ['bytes','sha256']},row['destination']
 if row['operation']=='replaced_exact_preimage':assert ident(Path(row['preimage']['preserved_preimage_path']))==row['preimage']['existing']
for row in review:assert ident(Path(row['source']))==ident(Path(row['destination']))=={k:row[k] for k in ['bytes','sha256']}
for row in json.loads((H/'preimages.json').read_text()):assert ident(Path(row['preserved_as']))=={k:row[k] for k in ['bytes','sha256']}
expected=json.loads((R/'proof/frozen-bundle-files.json').read_text());actual=vector(A/'bundle'/ID);assert actual==expected and len(actual)==213
vector_sha=hashlib.sha256(json.dumps(actual,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest();assert vector_sha=='22def4fbec18e4ec543d01ddf2ae71a59fc1cf5e2d20c3601b09ede4f84df6fd'
for key in ['archive','external_checksum']:
 original=Path(closed[key]['path']);target=A/'dist'/original.name;assert ident(original)==ident(target)=={k:closed[key][k] for k in ['bytes','sha256']}
assert ident(A/'package_release.py')['sha256']=='324fe8242ecb4f67c6f6ed77c6ff3f674245f53c73f17ba1029f0e9f03b28ccb'
assert ident(A/'release_tools/public_receipts.py')['sha256']=='ab91aae1bd08d64c167833095735735235919e0dd32a040b39d95c60291cf3b3'
for row in json.loads((R/'proof/candidate-app-files.json').read_text()):assert ident(R/'app'/row['path'])=={k:row[k] for k in ['bytes','sha256']}
for row in json.loads((R/'proof/frozen-input-files.json').read_text()):assert ident(R/'inputs'/row['path'])=={k:row[k] for k in ['bytes','sha256']}
assert ident(R/'proof/CLOSED.json')['sha256']=='dfae7c7fbe60c1f8f81b6383fc31ea2796bef13cdcf1ee23fbf09c6fdd06be04'
assert ident(V/'assessment-001/CLOSED.json')['sha256']=='63fc340c0530f663b43c909355b3aa64f53010c2c48480474d4d6e19214f9b52'
assert len(vector(REVIEW))==28
# The sole live execution is an overlap refusal before source/model evaluation or output effects.
output=H/'disposable/would-create/bundle';assert not output.parent.exists()
args=['/Users/jim/src/apps/specification_methodology/a_c/.venv/bin/python3','-B',str(A/'package_release.py'),'build','--proposal',str(A/'run/repaired-proposal'),'--public-evidence',str(A/'build/authoring-public.json'),'--review',str(REVIEW/'assessment-001/CLOSED.json'),'--upstream','/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout','--bundle',str(output),'--dist',str(output/'dist')]
p=subprocess.run(args,cwd=H,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
assert p.returncode==2 and 'archive output/checksum overlaps the bundle' in p.stderr and not output.parent.exists()
save(H/'live-overlap-refusal.json',{'argv':args,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'output_parent_absent':True,'claim':'Cheap live entrypoint overlap refusal before any receipt/model/input evaluation; no qualification replay'})
# Local links in changed/current Markdown and exact copied review reports only.
docs=[A/'README.md',A/'RELEASE-PREPARATION.md',B/'.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md',REPAIR/'README.md',REVIEW/'preparation/REVIEW.md',REVIEW/'assessment-001/REVIEW.md']
links=[]
for doc in docs:
 for label,target in re.findall(r'\[([^\]]+)\]\(([^\)]+)\)',doc.read_text()):
  target=target.strip().split(' "',1)[0].strip('<>')
  if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',target) or target.startswith('#'):continue
  path=Path(target.split('#',1)[0]);path=path if path.is_absolute() else doc.parent/path
  assert path.exists(),f'{doc}: {target}'
  links.append({'document':str(doc.relative_to(B)),'label':label,'target':target,'exists':True})
for doc in docs[:4]:
 text=doc.read_text();assert 'not_ready' in text and 'unverified' in text.lower();assert 'source-only' not in text
native=Path('/Users/jim/tmp/STDOv3-3.0.0-rc.1-test-20261020/README.md');assert ident(native)['sha256']=='415dca07bf2fa1350c61f398782179409ca33cb3afa1786318822093de66bb5d'
# Reconcile only the five explicitly granted original replacements and named new territories.
changed={Path(row['destination']).resolve():{k:row[k] for k in ['bytes','sha256']} for row in applied['entries'] if row['operation'] in ['replaced_exact_preimage','update_exact_granted_document']};assert len(changed)==5
new_files={Path(row['destination']).resolve() for row in applied['entries'] if row['operation'] not in ['replaced_exact_preimage','update_exact_granted_document']}|{Path(row['destination']).resolve() for row in review}
new_prefixes=[H,REPAIR,REVIEW,A/'bundle'/ID]
def granted_new(path):return path.resolve() in new_files or any(path.resolve().is_relative_to(prefix.resolve()) for prefix in new_prefixes)
def check_entry(path,row):
 counts[row['kind']]+=1
 if row['kind']=='absent':assert not path.exists() and not path.is_symlink(),str(path);return
 info=path.lstat()
 if 'mode' in row:assert oct(stat.S_IMODE(info.st_mode))==row['mode'],str(path)
 if row['kind']=='file':
  assert stat.S_ISREG(info.st_mode),str(path)
  expected=changed.get(path.resolve(),{k:row[k] for k in ['bytes','sha256']});assert ident(path)==expected,str(path)
 elif row['kind']=='symlink':assert path.is_symlink() and os.readlink(path)==row['target'],str(path)
 elif row['kind']=='directory':assert stat.S_ISDIR(info.st_mode),str(path)
 else:raise AssertionError(row['kind'])
ref=json.loads((R/'proof/trial-guard-reference.json').read_text());assert ident(Path(ref['path']))=={k:ref[k] for k in ['bytes','sha256']}
baseline=json.loads(gzip.decompress(Path(ref['path']).read_bytes()))
def git(root,args):return subprocess.run(['git','--no-optional-locks',*args],cwd=root,capture_output=True,check=True).stdout
repo_results={}
for name in ['owning_repo','common_worktree']:
 row=baseline[name];root=Path(row['path'])
 for rel,entry in row['files'].items():check_entry(root/rel,entry)
 for entry in row['git_metadata'].values():check_entry(Path(entry['path']),entry)
 assert git(root,['rev-parse','HEAD']).decode().strip()==row['head']
 assert hashlib.sha256(git(root,['for-each-ref','--format=%(refname) %(objectname) %(*objectname)'])).hexdigest()==row['refs_sha256']
 status=git(root,['status','--porcelain=v1','-z','--untracked-files=all']).decode()
 filtered=[];added=[]
 for entry in status.split('\0'):
  if not entry:continue
  rel=entry[3:]
  if rel not in row['files']:
   assert entry.startswith('?? ') and granted_new(root/rel),(name,entry);added.append(rel)
  else:filtered.append(entry)
 restored='\0'.join(filtered)+('\0' if filtered else '');assert restored==row['status_porcelain_v1_z'],name+' status outside grants changed'
 assert hashlib.sha256(git(root,['diff','--binary'])).hexdigest()==row['worktree_diff_sha256']
 assert hashlib.sha256(git(root,['diff','--cached','--binary'])).hexdigest()==row['index_diff_sha256']
 repo_results[name]={'old_paths_checked':len(row['files']),'tracked_count_unchanged':row['tracked_count'],'head_unchanged':row['head'],'new_status_paths_at_check':len(added),'only_granted_new_paths':True,'refs_index_config_status_and_diffs_preserved':True}
for name in ['default_store','prepared_representation']:
 row=baseline[name];root=Path(row['path']);check_entry(root,row['root'])
 for rel,entry in row['entries'].items():check_entry(root/rel,entry)
 for p in root.rglob('*'):
  if p.relative_to(root).as_posix() not in row['entries']:assert name=='prepared_representation' and granted_new(p),str(p)
for path,entry in baseline['configuration_files'].items():check_entry(Path(path),entry)
cli=baseline['cli_entrypoint'];check_entry(Path(cli['path']),cli['entry']);check_entry(Path(cli['resolved_path']),cli['resolved'])
for rel,entry in baseline['toolchain_python_sources']['files'].items():check_entry(Path(baseline['toolchain_python_sources']['path'])/rel,entry)
own=json.loads((R/'proof/original-guards.json').read_text())
for rel,entry in own['tracked_files'].items():assert ident(Path(baseline['owning_repo']['path'])/rel)==entry
for path,expected in changed.items():assert ident(path)==expected
old_vector=json.loads((B/'.ai-workspace/qualification/t010/packaging/final-001/sealed-bundle-files.json').read_text());assert vector(A/'bundle/a_c-stdo-v3-common-35fb4824')==old_vector
assert ident(A/'dist/a_c-stdo-v3-common-35fb4824.tar.gz')['sha256']=='2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386'
result={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Exact materialization/vector/integrity/local links, reconciled original preservation and one pre-effect live refusal only','materialized_entries':len(applied['entries']),'review_copies_exact':len(review),'new_bundle_files':len(actual),'new_bundle_bytes':sum(x['bytes'] for x in actual),'new_bundle_vector_sha256':vector_sha,'new_archive':ident(A/'dist'/(ID+'.tar.gz')),'new_sidecar':ident(A/'dist'/(ID+'.tar.gz.sha256')),'local_links_resolved':len(links),'links':links,'five_allowed_original_replacements':[{ 'path':str(path),**expected} for path,expected in changed.items()],'all_other_original_entries_unchanged_by_kind':dict(counts),'repositories':repo_results,'preexisting_tracked_modifications_unchanged':len(own['tracked_files']),'old_bundle_213_files_and_archive_preserved':True,'old_source_model_manifests_receipts_SOURCE_READINESS_and_proofs_preserved':True,'default_store_config_tool_ref_index_preserved':True,'frozen_repair_and_review_subjects_preserved':True,'native_readme_exact':ident(native),'native_canonical_outputs_mutated':False,'no_git_or_export_rebuild_model_browser_server_install_effects':True}
save(H/'checks.json',result)
applied['status']='applied_and_verified';applied['verification_report']=str(H/'checks.json');save(H/'applied-promotion-manifest.json',applied)
print(json.dumps({k:v for k,v in result.items() if k not in ['links','five_allowed_original_replacements']},indent=2))
