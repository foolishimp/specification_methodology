from pathlib import Path
import ast,hashlib,importlib.util,json,os,subprocess,sys
repo=Path('/Users/jim/src/apps/specification_methodology');b=repo/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/model-evidence-repair-016';out=Path(__file__).resolve().parent/'gate016';out.mkdir(exist_ok=False)
d=json.loads((b/'SUBJECT.json').read_text());refs=[v[k]for v in d['sources']for k in ('current','frozen')]+d['evidence']
def verify():
 for row in refs:
  raw=(repo/row['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['sha256']and len(raw)==row['bytes'],row['path']
verify();old=(b/'predecessor-stable_release_evidence.py').read_bytes();new=(repo/'scripts/stable_release_evidence.py').read_bytes()
def other(raw):
 tree=ast.parse(raw);tree.body=[n for n in tree.body if not isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))or n.name!='representation'];return ast.dump(tree,include_attributes=False)
assert other(old)==other(new)
sys.path.insert(0,str(repo/'scripts'));import check_stack_release as api;import stable_release_evidence as owner
manifest=json.loads((b/'manifest-fixture.json').read_text());record=json.loads((b/'source-current-model.json').read_text());actual=owner.representation(api.View(repo,None),record,'source_current_model',manifest,api)
assert (b/'before.json').read_bytes()==(b/'after.json').read_bytes();snap=json.loads((b/'after.json').read_text())
for row in snap:
 p=repo/row['path'];raw=p.read_bytes();st=p.stat();assert hashlib.sha256(raw).hexdigest()==row['sha256']and len(raw)==row['bytes']and st.st_mode==row['mode']and st.st_mtime_ns==row['mtime_ns'],row['path']
# Re-consume the same actual receipt with frozen predecessor code; never invoke the owner BUILD.
legacy=type(sys)('review_legacy016');legacy.__file__=str(b/'predecessor-stable_release_evidence.py');exec(compile(old,legacy.__file__,'exec'),legacy.__dict__)
try:legacy.representation(api.View(repo,None),record,'source_current_model',manifest,api);raise AssertionError('predecessor unexpectedly accepts')
except ValueError as e:predecessor=str(e)
assert predecessor=='execution input closure omits a prescribed current input'
argv=[sys.executable,'-B','-m','unittest','discover','-s','tests','-p','test_representation_evidence.py','-v'];p=subprocess.run(argv,cwd=repo,capture_output=True,timeout=30);(out/'tests.stdout').write_bytes(p.stdout);(out/'tests.stderr').write_bytes(p.stderr);assert p.returncode==0,p.stderr.decode()
spec=importlib.util.spec_from_file_location('review_fixture016',repo/'tests/test_representation_evidence.py');fixture=importlib.util.module_from_spec(spec);spec.loader.exec_module(fixture)
controls=[]
def run_case(name,change,expected):
 t=fixture.RepresentationEvidenceTests();t.setUp()
 try:
  change(t)
  try:t.check();raise AssertionError('negative accepted: '+name)
  except ValueError as e:message=str(e)
  assert expected in message,(name,message);controls.append({'name':name,'refusal':message})
 finally:t.doCleanups()
def coherent_source_omission(t):
 t.rewrite_fact('source_manifest',lambda v:v.update(files=[]));t.rewrite_fact('generation_plan',lambda v:v.update(files=[]));t.rewrite_fact('project',lambda v:v.update(files=[],manifest_sha256=t.facts['source_manifest']['sha256'],plan_sha256=t.facts['generation_plan']['sha256']));t.rewrite_result(lambda v:v.update(project_sha256=t.facts['project']['sha256'],source_manifest_sha256=t.facts['source_manifest']['sha256']))
def coherent_plan_subject(t):
 t.rewrite_fact('generation_plan',lambda v:v.update(subject_id='different'));t.rewrite_fact('project',lambda v:v.update(plan_sha256=t.facts['generation_plan']['sha256']));t.rewrite_result(lambda v:v.update(project_sha256=t.facts['project']['sha256']))
def wrong_readback_role(t):
 row=t.facts['generated_model'];t.record['execution']['inputs']=[r for r in t.record['execution']['inputs']if r!=row];t.record['execution']['outputs'].append(row)
run_case('coherently-rehashed-source-omission',coherent_source_omission,'complete exact semantic source')
run_case('rehash-plan-and-project-with-wrong-subject',coherent_plan_subject,'complete exact semantic source')
run_case('reused-model-output-without-read-input',wrong_readback_role,'produced/read-back role')
verify();r={'kind':'independent.model-evidence016-recheck/1','subject_sha256':hashlib.sha256((b/'SUBJECT.json').read_bytes()).hexdigest(),'source_refs_before_after':len(refs),'production_sha256':hashlib.sha256(new).hexdigest(),'delta':'Only representation() changed; prior function-excluded AST is identical.','actual_record_sha256':hashlib.sha256((b/'source-current-model.json').read_bytes()).hexdigest(),'actual_adapter_result':actual,'predecessor_refusal':predecessor,'readback_files_current_unchanged_bytes_modes_mtimes':len(snap),'focused_tests':{'argv':argv,'returncode':p.returncode,'stderr':p.stderr.decode()},'independent_deeper_negative_controls':controls,'limits':'Receipt interpretation only; actual owner BUILD readback was performed by Writer exactly once. Reviewer did not rerun BUILD, generation, Lean, native actors or any repository mutation.'};(out/'REVIEW.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'report':str(out/'REVIEW.json'),'sha256':hashlib.sha256((out/'REVIEW.json').read_bytes()).hexdigest(),'controls':controls,'verdict':'satisfied'}))
