from __future__ import annotations
import concurrent.futures,copy,hashlib,json,pathlib,shutil,subprocess,time,datetime
O=pathlib.Path('/Users/jim/tmp/a_c-common-rc1-packaging-review-20261021/assessment-001');R=pathlib.Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021');stage=json.loads((O/'STAGE1.json').read_text());E=pathlib.Path(stage['extracted']);ART='a_c-stdo-v3-common-35fb4824-packaging-r1';PY='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';controls=[]
ENV={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','PYTHONDONTWRITEBYTECODE':'1','PYTHONNOUSERSITE':'1','GIT_OPTIONAL_LOCKS':'0','TMPDIR':str(O/'tmp'),'XDG_CACHE_HOME':str(O/'cache'),'MPLCONFIGDIR':str(O/'cache/matplotlib')}
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
def check(name,ok,observed=None):
 controls.append({'name':name,'passed':bool(ok),'observed':observed});save(O/'stage2-progress.json',{'controls':controls})
 if not ok:raise AssertionError(name)
def progress(text):print(json.dumps({'progress':text,'controls_passed':len(controls)}),flush=True)
def run(label,argv,cwd=E,expect=0):
 start=time.monotonic();p=subprocess.run(argv,cwd=cwd,env=ENV,capture_output=True,text=True);log={'argv':argv,'cwd':str(cwd),'returncode':p.returncode,'elapsed_seconds':time.monotonic()-start,'stdout':p.stdout,'stderr':p.stderr};save(O/'commands'/f'{label}.json',log);check(label,p.returncode==expect,{'returncode':p.returncode,'stderr':p.stderr[:1200]});return p
replay=run('actual-stdlib-portable-verifier',[PY,'-S','-B','release_tools/bundle_check.py','.']);replaydata=json.loads(replay.stdout);check('actual-genuine-source-and-model-replay',replaydata['status']=='passed' and replaydata['model']['sha256']=='691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf' and replaydata['source']['files']==81 and replaydata['records']==1987,replaydata)
original=json.loads((E/'model.json').read_text());(O/'recoveries').mkdir()
for name in ['carrier.json','graph.json']:
 out=O/'recoveries'/('decoded-'+name);p=run('exact-recovery-'+name,[PY,'-S','-B','codec/ac_graph.py','decode',name,'--out',str(out)]);reply=json.loads(p.stdout);recovered=json.loads(out.read_text());canonical=hashlib.sha256(json.dumps(recovered,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest();check('unchanged-document-canonical-recovery:'+name,recovered==original and canonical=='691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf' and reply['model']['id']==original['id'] and reply['model']['sha256']==canonical,reply)
progress('Fresh stdlib verifier and both exact public carrier recoveries passed')
# One actual public readiness mutation must refuse before producing fresh output trees.
mutated=O/'mutated-portable-input';shutil.copytree(E,mutated);path=mutated/'SOURCE-READINESS.md';path.write_bytes(path.read_bytes().replace(b'captured-workspace projection',b'captured-workspace projection ALTERED',1));base=stage['substituted_command_base'];bad=base[:];bad_bundle=O/'readiness-refusal-output/bundle';bad_dist=O/'readiness-refusal-output/dist';bad[bad.index('--bundle')+1]=str(bad_bundle);bad[bad.index('--dist')+1]=str(bad_dist)
p=run('actual-modified-portable-input-pre-effect-refusal',bad,cwd=mutated,expect=2);check('modified-portable-input-no-output-effects',not bad_bundle.exists() and not bad_dist.exists() and not bad_bundle.parent.exists() and 'source-readiness record changed' in p.stderr)
# Actual command comes from the extracted README, changing only executable/dependency/output coordinates.
rebuilt=O/'rebuilt/bundle'/ART;dist=O/'rebuilt/dist';command=base[:];command[command.index('--bundle')+1]=str(rebuilt);command[command.index('--dist')+1]=str(dist)
save(O/'ACTUAL-REBUILD-INPUT-CLOSURE.json',{'documented_command':stage['documented_command'],'executed_argv':command,'cwd':str(E),'bundled_inputs':['package_release.py','SOURCE-READINESS.md','codec/ac_graph.py','model.json','carrier.json','graph.json','coverage.json','result.json','source/81members','three source manifests','evidence/typedreceipts+4reports','release_tools/'],'explicit_external_dependency':{'upstream':command[command.index('--upstream')+1],'commit':'fe085cedddde3a18554f8749b230bfe47f3dcce7'},'existing_runtime':command[0],'omitted_original_workspace_readiness_imported':False,'original_private_runs_or_proofs_imported':False,'cache_and_temp':'assessment-001 only'})
result=run('actual-documented-extracted-build',command);buildreply=json.loads(result.stdout);check('actual-second-generation-build-reported-success',buildreply['status']=='local_bundle_prepared')
vector=[{'path':p.relative_to(rebuilt).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(rebuilt.rglob('*')) if p.is_file()];vectorhash=hashlib.sha256(json.dumps(vector,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();secondarchive=dist/(ART+'.tar.gz');check('actual-second-generation-all213files-and-archive-identical',vector==json.loads((R/'proof/frozen-bundle-files.json').read_text()) and vectorhash=='22def4fbec18e4ec543d01ddf2ae71a59fc1cf5e2d20c3601b09ede4f84df6fd' and sha(secondarchive)=='989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b',{'files':len(vector),'vector_sha256':vectorhash,'archive_bytes':secondarchive.stat().st_size,'archive_sha256':sha(secondarchive)})
progress('Actual README-derived second-generation bundled-input build passed; all213files and archive byte-identical')
# Independently regenerate all surrounding custody hashes for each source-identity counterexample.
def reindex(root):
 names=sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.relative_to(root).as_posix() not in ['inventory.json','SHA256SUMS']);inv=json.loads((root/'inventory.json').read_text());inv['files']=[{'path':n,'bytes':(root/n).stat().st_size,'sha256':sha(root/n)} for n in names];save(root/'inventory.json',inv);(root/'SHA256SUMS').write_text(''.join(f'{sha(root/n)}  {n}\n' for n in sorted(names+['inventory.json'])))
 assert all((root/r['path']).stat().st_size==r['bytes'] and sha(root/r['path'])==r['sha256'] for r in inv['files']);assert (root/'SHA256SUMS').read_text()==''.join(f'{sha(root/n)}  {n}\n' for n in sorted(names+['inventory.json']))
cases=[]
for field in ['source_commit','package_tree']:
 for operation in ['wrong-zero','missing']:
  root=O/'metadata-cases'/(field+'-'+operation);shutil.copytree(E,root);release=json.loads((root/'RELEASE.json').read_text());expected=release[field]
  if operation=='wrong-zero':release[field]='0'*40
  else:del release[field]
  save(root/'RELEASE.json',release);reindex(root);cases.append((field,operation,root,expected))
def verify_case(case):
 field,operation,root,expected=case;start=time.monotonic();argv=[PY,'-S','-B','release_tools/bundle_check.py','.'];p=subprocess.run(argv,cwd=root,env=ENV,capture_output=True,text=True);log={'field':field,'operation':operation,'expected':expected,'outer_inventory_checksums_independently_consistent':True,'argv':argv,'cwd':str(root),'returncode':p.returncode,'elapsed_seconds':time.monotonic()-start,'stdout':p.stdout,'stderr':p.stderr};save(O/'commands'/('actual-rehashed-'+field+'-'+operation+'.json'),log);return log
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(verify_case,cases))
for row in results:check('actual-outer-rehashed-source-refusal:'+row['field']+':'+row['operation'],row['returncode']==2 and 'source commit/package tree differs' in row['stderr'],row)
progress('All four actual portable wrong/missing duplicate-source fields refused despite independently refreshed outer hashes')
# Immutable candidate, old delivered artifact and source-first preparation conservation.
guards=json.loads((O/'READONLY-GUARDS.json').read_text())['files'];bad=[]
for name,wanted in guards.items():
 p=pathlib.Path(name)
 if not p.is_file() or sha(p)!=wanted:bad.append(name)
check('all-readonly-candidate-original-preparation-guards-unchanged',not bad,{'guarded_paths':len(guards),'mismatches':bad})
act=json.loads((O/'ACTIVATION.json').read_text());elapsed=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(act['started_at'])).total_seconds();check('within45minute-cap-zero-model-spend',elapsed<45*60,{'elapsed_seconds':elapsed,'native_model_calls':0})
save(O/'STAGE2.json',{'status':'passed','controls':controls,'controls_passed':len(controls),'second_generation_file_vector_sha256':vectorhash,'second_generation_archive_sha256':sha(secondarchive),'actual_rehashed_duplicate_source_refusals':4,'candidate_guard_mismatches':bad,'elapsed_seconds':elapsed,'timing_scope':'Artifact checks only; no benchmark/efficiency inference','native_model_network_install_browser_server_git_mutation_effects':0,'STDOtrial_native_output_access':False,'findings':[]});print(json.dumps({'status':'passed','controls':len(controls),'total_with_stage1':len(controls)+stage['controls_passed'],'elapsed_seconds':elapsed,'findings':[]}))
