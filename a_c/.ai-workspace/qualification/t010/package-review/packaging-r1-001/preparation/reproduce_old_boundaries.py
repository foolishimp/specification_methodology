from __future__ import annotations
import copy,hashlib,importlib.util,json,os,pathlib,shutil,subprocess,sys,tarfile,tempfile,types,datetime
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';O=pathlib.Path('/Users/jim/tmp/a_c-common-rc1-packaging-review-20261021/preparation');S=pathlib.Path(tempfile.mkdtemp(prefix='ac-common-package-review-'));ART='a_c-stdo-v3-common-35fb4824';archive=A/'dist'/f'{ART}.tar.gz'
os.environ['PYTHONDONTWRITEBYTECODE']='1';os.environ['TMPDIR']=str(S);os.environ['XDG_CACHE_HOME']=str(S/'cache');(S/'cache').mkdir()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while block:=f.read(1024*1024):h.update(block)
 return h.hexdigest()
def save(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
def snapshot(root):
 rows={}
 for p in sorted(root.rglob('*')):
  name=p.relative_to(root).as_posix()
  if p.is_symlink():rows[name]={'kind':'symlink','target':os.readlink(p)}
  elif p.is_file():rows[name]={'kind':'file','bytes':p.stat().st_size,'sha256':sha(p)}
  elif p.is_dir():rows[name]={'kind':'directory'}
 return rows
# Copy only immutable old code. No fixed Worker directory or trial root is read.
code=S/'old-code';code.mkdir();(code/'release_tools').mkdir()
for n in ['package_release.py','release_tools/bundle_check.py','release_tools/public_receipts.py']:
 target=code/n;target.write_bytes((A/n).read_bytes())
spec=importlib.util.spec_from_file_location('old_packager_preparation',code/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
r=pkg.receipts
with tarfile.open(archive) as tar:
 members=tar.getmembers();names=[x.name for x in members]
 assert len(names)==213 and names==sorted(set(names)) and all(x.isfile() and x.name.startswith(ART+'/') and not pathlib.PurePosixPath(x.name).is_absolute() and '..' not in pathlib.PurePosixPath(x.name).parts for x in members)
 extracted=S/'frozen';extracted.mkdir();tar.extractall(extracted,filter='data')
E=extracted/ART
live=A/'bundle'/ART
bundle_guard={str(p):sha(p) for p in live.rglob('*') if p.is_file()};assert len(bundle_guard)==213;save(O/'ORIGINAL-BUNDLE-GUARDS.json',{'files':bundle_guard})
# Exact actual213-file archive overlap reproduces the reported214-member result.
overlap=S/'actual-overlap'/ART;shutil.copytree(E,overlap);before_count=sum(p.is_file() for p in overlap.rglob('*'));out=overlap/'dist/self-including.tar.gz';result=pkg.archive(overlap,out)
with tarfile.open(out) as tar:
 bad_members=tar.getmembers();bad_names=[x.name for x in bad_members];self_member=ART+'/dist/self-including.tar.gz';assert self_member in bad_names
 bad_extract=S/'self-extracted';bad_extract.mkdir();tar.extractall(bad_extract,filter='data')
python='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')}
p=subprocess.run([python,'-S','-B',str(code/'release_tools/bundle_check.py'),'.'],cwd=bad_extract/ART,env=env,capture_output=True,text=True)
assert before_count==213 and len(bad_members)==214 and p.returncode==2 and 'missing or extra' in p.stderr
actual_overlap={'old_helper_result':'returned_successfully','returned':result,'input_files_before':before_count,'archive_members':len(bad_members),'self_included_member':self_member,'embedded_archive_bytes':next(x.size for x in bad_members if x.name==self_member),'extracted_cli':{'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr},'heavy_decode_reached':False,'boundary':'Full build not repeated; direct old archive helper over exact valid213-file extracted bytes reproduces its final packaging failure.'}
# Cheap direct helper matrix captures actual path-resolution/effect boundaries.
path_cases=[]
for label in ['dist-equals-bundle','nested-dist','resolved-dotdot-dist','symlink-alias-dist','safe-sibling-dist','safe-parent-dist','protected-existing-archive','protected-existing-sidecar']:
 root=S/'path-cases'/label;bundle=root/'bundle';bundle.mkdir(parents=True);(bundle/'one.txt').write_text('one\n');(bundle/'two.json').write_text('{"two":2}\n')
 if label=='dist-equals-bundle':output=bundle/'artifact.tar.gz'
 elif label=='nested-dist':output=bundle/'dist/artifact.tar.gz'
 elif label=='resolved-dotdot-dist':output=bundle/'staging/../artifact.tar.gz'
 elif label=='symlink-alias-dist':
  alias=root/'alias';alias.symlink_to(bundle,target_is_directory=True);output=alias/'artifact.tar.gz'
 elif label=='safe-parent-dist':output=root/'artifact.tar.gz'
 else:output=root/'dist/artifact.tar.gz'
 if label=='protected-existing-archive':output.parent.mkdir();output.write_bytes(b'KEEP ARCHIVE BYTES')
 if label=='protected-existing-sidecar':output.parent.mkdir();output.with_name(output.name+'.sha256').write_bytes(b'KEEP CHECKSUM BYTES')
 before=snapshot(root);failure=None
 try:returned=pkg.archive(bundle,output);accepted=True
 except (ValueError,OSError) as ex:accepted=False;failure=str(ex);returned=None
 after=snapshot(root);members=None
 if accepted:
  with tarfile.open(output) as tar:members=[x.name for x in tar.getmembers()]
 inside=output.resolve().is_relative_to(bundle.resolve())
 path_cases.append({'case':label,'resolved_output_inside_bundle':inside,'old_accepted':accepted,'refusal':failure,'filesystem_changed':before!=after,'archive_members':members,'old_result':returned})
 if inside:assert accepted and before!=after and len(members)==3
 elif label.startswith('protected-'):assert not accepted and before==after
 else:assert accepted and len(members)==2
# Direct formatter proves exact old portable input is an unsupported second-generation input.
original=(A/'SOURCE-READINESS.md').read_bytes();portable=(E/'SOURCE-READINESS.md').read_bytes();assert sha(A/'SOURCE-READINESS.md')=='114a4580a344daa1cf32bcbc19246ab189c26b3f50b58d47c105ae7a2b54bd1d'
assert pkg.source_readiness_projection(original).encode()==portable
readiness=[]
inputs={'exact-original':original,'exact-extracted-portable':portable,'mutated-portable-prefix':portable.replace(b'captured-workspace projection',b'captured-workspace projection ALTERED',1),'mutated-portable-version':portable.replace(b'Common V3',b'Common V4',1),'mutated-portable-open-gate':portable.replace(b'not_ready',b'ready',1),'portable-with-appended-claim':portable+b'\nOwner accepted.\n'}
for label,data in inputs.items():
 try:value=pkg.source_readiness_projection(data);accepted=True;reason=None
 except ValueError as ex:accepted=False;reason=str(ex);value=None
 readiness.append({'case':label,'input_sha256':hashlib.sha256(data).hexdigest(),'old_accepted':accepted,'reason':reason,'output_sha256':hashlib.sha256(value.encode()).hexdigest() if value is not None else None})
assert readiness[0]['old_accepted'] and not readiness[1]['old_accepted']
# Derive the receipt gate's expected object from actual frozen model/source/raw files.
doc=json.loads((E/'model.json').read_text());canonical=hashlib.sha256(json.dumps(doc,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest();assert canonical=='691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf'
model=types.SimpleNamespace(document=doc,identity=doc['id'],sha256=canonical);expected=r.expected_bindings(E,model,{n:E/n for n in r.ARTIFACTS});assert expected==json.loads((E/'evidence/authoring-public.json').read_text())['bindings']
assert r.bundle_evidence(E,expected)['bounded_review_receipts']==1
baseline={n:(E/n).read_bytes() for n in ['RELEASE.json','inventory.json','SHA256SUMS']}
def reindex():
 inv=json.loads((E/'inventory.json').read_text());names=sorted(p.relative_to(E).as_posix() for p in E.rglob('*') if p.is_file() and p.name not in ['inventory.json','SHA256SUMS']);inv['files']=[{'path':n,'bytes':(E/n).stat().st_size,'sha256':sha(E/n)} for n in names];save(E/'inventory.json',inv);(E/'SHA256SUMS').write_text(''.join(f'{sha(E/n)}  {n}\n' for n in sorted(names+['inventory.json'])))
 listed=[x['path'] for x in inv['files']];assert sorted(listed+['inventory.json','SHA256SUMS'])==sorted(p.relative_to(E).as_posix() for p in E.rglob('*') if p.is_file());assert all((E/x['path']).stat().st_size==x['bytes'] and sha(E/x['path'])==x['sha256'] for x in inv['files'])
 assert (E/'SHA256SUMS').read_text()==''.join(f'{sha(E/n)}  {n}\n' for n in sorted(listed+['inventory.json']))
release_cases=[]
for field in ['source_commit','package_tree']:
 for operation in ['wrong-zero','missing']:
  release=json.loads(baseline['RELEASE.json']);wanted=release[field]
  if operation=='wrong-zero':release[field]='0'*40
  else:del release[field]
  save(E/'RELEASE.json',release);reindex()
  try:result=r.bundle_evidence(E,expected);accepted=True;reason=None
  except (ValueError,KeyError,TypeError) as ex:accepted=False;reason=str(ex);result=None
  release_cases.append({'field':field,'operation':operation,'expected':wanted,'supplied':release.get(field),'outer_inventory_and_checksums_consistent':True,'old_gate_accepted':accepted,'gate_result':result,'reason':reason});assert accepted
  for n,data in baseline.items():(E/n).write_bytes(data)
# Existing subject/model enforcement stays demonstrated as a positive refusal control.
for field in ['subject','model']:
 release=json.loads(baseline['RELEASE.json'])
 if field=='subject':release[field]='urn:other:subject'
 else:release[field]['sha256']='0'*64
 save(E/'RELEASE.json',release)
 try:r.bundle_evidence(E,expected);accepted=True;reason=None
 except (ValueError,KeyError,TypeError) as ex:accepted=False;reason=str(ex)
 release_cases.append({'field':field,'operation':'existing-negative-control','old_gate_accepted':accepted,'reason':reason});assert not accepted
 for n,data in baseline.items():(E/n).write_bytes(data)
assert r.bundle_evidence(E,expected)['bounded_review_receipts']==1
# Never mutate or promote old artifacts. Only named original bytes are hashed here.
mismatches=[]
for proof in ['ORIGINAL-GUARDS.json','ORIGINAL-BUNDLE-GUARDS.json']:
 for path,wanted in json.loads((O/proof).read_text())['files'].items():
  p=pathlib.Path(path)
  if not p.is_file() or sha(p)!=wanted:mismatches.append(path)
assert not mismatches
result={'status':'preparation_complete','fixed_candidate_exposed':False,'scratch':str(S),'actual_overlap':actual_overlap,'path_matrix':path_cases,'readiness':{'original_raw_sha256':hashlib.sha256(original).hexdigest(),'portable_raw_sha256':hashlib.sha256(portable).hexdigest(),'direct_old_formatter_cases':readiness,'actual_second_generation_full_build':'not performed during preparation; direct exact formatter input/call-path refusal reproduced, fixed actual rebuild requires separately bound subject'},'release_duplicate_source_fields':{'cases':release_cases,'genuine_gate_passed':True,'full_portable_checker_with_wrong_duplicate_fields':'not performed to avoid heavy unchanged carrier decode; direct old invoked gate plus independently consistent outer inventory reproduced omitted field checks'},'original_guard_mismatches':mismatches,'original_archive_sha256':sha(archive),'new_artifact_expected':'a_c-stdo-v3-common-35fb4824-packaging-r1','native_LLM_calls':0,'network_browser_server_install_git_effects':0,'independent_STDO_trial_access':False,'limits':['No fixed code copy/output exposure or judgment','No heavy carrier decode','No original artifact mutation/promotion','No semantic/acceptance/release/UI assessment']}
save(O/'OLD-BOUNDARIES.json',result);print(json.dumps({'status':result['status'],'actual_overlap_members':len(bad_members),'valid_original_members':213,'inside_path_variants_old_accepted':sum(x['resolved_output_inside_bundle'] and x['old_accepted'] for x in path_cases),'portable_readiness_old_refused':not readiness[1]['old_accepted'],'duplicate_source_wrong_or_missing_old_accepted':4,'original_guard_mismatches':mismatches,'fixed_candidate_exposed':False,'scratch':str(S)}))
