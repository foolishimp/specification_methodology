"""Close actual fixture proof and index source-selected finite operation evidence."""
from pathlib import Path
import ast,collections,hashlib,json,re,sys
sys.dont_write_bytecode=True
P=Path('/Users/jim/src/apps/specification_methodology/a_c');Repo=P.parent;D=Path(__file__).resolve().parent;T=P/'build_tenants/graphify'
sys.path.insert(0,str(T/'code'));import ac_support_core as c
h=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
def save(n,v):
 q=D/n;raw=json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
 if q.exists():
  assert q.read_text()==raw,'Existing closed metadata differs: '+n
 else:q.write_text(raw)
 return q
def loc(q):return {'path':str(q.relative_to(P)),'sha256':h(q),'bytes':q.stat().st_size}
subject=json.loads((D/'CLOSED_SUBJECT.json').read_text())
for rel,sha in subject['required_sources'].items():assert h(Repo/rel)==sha,rel
summary={}
for stage in ['interfaces','typing','suite','upstream']:
 q=D/(stage+'-001');data=json.loads((q/'command.json').read_text());assert data['returncode']==0 and data['sources_unchanged'] is True
 summary[stage]={'command':loc(q/'command.json'),'stdout':loc(q/'stdout'),'stderr':loc(q/'stderr'),'returncode':0,'sources_unchanged':True}
for stage,expected in [('suite',254),('interfaces',37)]:
 text=(D/(stage+'-001')/'stderr').read_text();matches=re.findall(r'^Ran (\d+) tests? in ([0-9.]+)s$',text,re.M);assert len(matches)==1 and int(matches[0][0])==expected and re.search(r'^OK$',text,re.M)
 summary[stage].update(tests=int(matches[0][0]),seconds=matches[0][1],skipped=0)
upstream=json.loads((D/'upstream-001/upstream-report.json').read_text());assert upstream['status']=='passed' and len(upstream['checks'])==9 and upstream['upstream']['commit']=='fe085cedddde3a18554f8749b230bfe47f3dcce7';summary['upstream'].update(checks=9,commit=upstream['upstream']['commit'])
typing=(D/'typing-001/stdout').read_text();assert 'Success: no issues found in 9 source files' in typing;summary['typing']['strict_normal_import_files']=9
demo=json.loads((D/'ordinary-demo-001/checks.json').read_text());assert len(demo['checks'])==10 and all(demo['checks'].values());assert (D/'ordinary-demo-001/sources-before.json').read_bytes()==(D/'ordinary-demo-001/sources-after.json').read_bytes();summary['ordinary_demo']={'checks':10,'all_passed':True,'sources_unchanged':True,'proof':loc(D/'ordinary-demo-001/checks.json')}
save('RESULTS.json',{'schema':'a_c.T008.mechanical-integration-results/2','subject_sha256':h(D/'CLOSED_SUBJECT.json'),'stages':summary,'historical_original_cut_tests':242,'current_tests':254,'actual_provider_calls':0,'qualification':'Current finite structural/local-process/upstream qualification only; no F_P/semantic/owner acceptance claim'})
# Scan actual retained operation envelopes from this new executed proof, keeping one exact canonical witness each.
ops=collections.defaultdict(dict);op_paths={};retry_artifacts=[]
for q in sorted(D.rglob('*.json')):
 if q.is_symlink() or not q.is_file():continue
 if q.name in ['PREPARATION.contract.txt','OPERATION_SCENARIO_MAP.pending.json']:continue
 try:d=json.loads(q.read_text())
 except (ValueError,UnicodeError):continue
 if not isinstance(d,dict) or d.get('schema')!=c.ARTIFACT:continue
 if d.get('kind')=='operation':
  payload=d.get('payload',{});request=payload.get('request',{});op=request.get('operation');response=payload.get('response_without_evidence',{})
  if op in c._ARGUMENTS:
   sha=h(q);ops[op].setdefault(sha,{'source':loc(q),'request_id':request.get('id'),'status':response.get('status'),'refusal':response.get('refusal'),'bound_value':(response.get('operation_outcome') or {}).get('value'),'scope':'actual retained local fixture envelope; not actual F_P producer or semantic acceptance'});op_paths[sha]=q
# Each positive/negative public retry row has real process request/response/execution plus protected operation ref.
retry_rows=[];selected_retry=[]
root=D/'suite-001/effects-fixtures'
for q in sorted(root.iterdir()):
 if 'PublicRetryTests_' not in q.name:continue
 calls=[]
 for cd in sorted((q/'calls').iterdir()):
  r=json.loads((cd/'request.json').read_text());out=json.loads((cd/'stdout.bin').read_text());execution=json.loads((cd/'execution.json').read_text())
  row={'operation':r['operation'],'request_id':r['id'],'response_status':out['status'],'refusal':out['refusal'],'process_returncode':execution.get('returncode'),'request':loc(cd/'request.json'),'response':loc(cd/'stdout.bin'),'execution':loc(cd/'execution.json'),'operation_evidence':out.get('evidence')}
  calls.append(row)
 # Positive: actual check, second preflight/start, final observed lifecycle and context. Negative: final actual refusing call.
 selected=[]
 if q.name.endswith('test_public_selected_retry'):
  for op in ['context.assemble','checks.evaluate','contract.preflight','dispatch.start','dispatch.observe']:
   matches=[x for x in calls if x['operation']==op]
   if matches:selected.append(matches[-1])
 else:
  selected=[calls[-1]]
 for x in selected:
  for key in ['request','response','execution']:
   selected_retry.append(x[key])
  ev=x['operation_evidence']
  if ev and ev['sha256'] in op_paths:selected_retry.append(loc(op_paths[ev['sha256']]))
 retry_rows.append({'test_fixture':q.name,'actual_calls':calls,'selected_deciding_calls':selected,'limits':'Registered deterministic process/FD evidence, not live F_P reviewer or Product acceptance'})
assert len(retry_rows)==10
# Preserve current source hash/test execution routing without claiming each literal is a public call.
executed=set(re.findall(r'^test_\w+ \(([^)]+)\) \.\.\. ok$',(D/'suite-001/stderr').read_text(),re.M))
mentions=collections.defaultdict(list)
for q in sorted((T/'test_env').glob('test_*.py')):
 tree=ast.parse(q.read_text());module=q.stem
 for cls in [x for x in tree.body if isinstance(x,ast.ClassDef)]:
  for fn in [x for x in cls.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef)) and x.name.startswith('test_')]:
   if not any(s.endswith('.'+cls.name+'.'+fn.name) for s in executed):continue
   strings={x.value for x in ast.walk(fn) if isinstance(x,ast.Constant) and isinstance(x.value,str)}
   for op in set(c._ARGUMENTS)&strings:mentions[op].append({'test':module+'.'+cls.name+'.'+fn.name,'source':str(q.relative_to(P)),'source_sha256':h(q),'line':fn.lineno,'scope':'Executed test with literal operation mention, not proof of public invocation by itself'})
old=P/'.ai-workspace/qualification/t008/interfaces/integration-001/OPERATION_SCENARIO_MAP.json';oldmap=json.loads(old.read_text());oldrows={r['operation']:r for r in oldmap['rows']};rows=[]
for op in sorted(c._ARGUMENTS):
 witnesses=list(ops[op].values());oldrow=oldrows[op];rows.append({'operation':op,'requirements':oldrow['requirements'],'current_subject_sha256':h(D/'CLOSED_SUBJECT.json'),'current_retained_operation_witnesses':witnesses,'current_witness_count':len(witnesses),'current_status_counts':dict(collections.Counter(x['status'] for x in witnesses)),'executed_test_source_literal_mentions':mentions[op],'historical_witness_count':oldrow['distinct_retained_operation_envelopes'],'historical_map_sha256':h(old),'limits':['Current test literal mentions and owning OperationEvidence are distinguished','Missing owning durable operation evidence remains an explicit qualification gap','No actual F_P source-first/semantic/benefit/acceptance claim from fixture results'],'unexecuted_variants':oldrow['unexecuted_variants']})
selected_retry=list({x['path']:x for x in selected_retry}.values())
save('PUBLIC_RETRY_PROOF_INDEX.json',{'schema':'a_c.T008.public-retry-proof-index/1','current_subject_sha256':h(D/'CLOSED_SUBJECT.json'),'actual_fixture_tests':10,'rows':retry_rows,'selected_deciding_raw_files':selected_retry,'scope':'Actual composed public CLI context/preflight/start/observe/checks.evaluate and retry/refusal controls. Original lower-layer fixture remains a separate named lower-layer test, not proof of this public route. Original old negative/history retained; no semantic acceptance.'})
save('OPERATION_SCENARIO_MAP.json',{'schema':'a_c.T008.operation-scenario-map/2','current_subject':loc(D/'CLOSED_SUBJECT.json'),'historical_map':loc(old),'historical_source_cut_tests':242,'current_source_cut_tests':254,'current_results':loc(D/'RESULTS.json'),'rows':rows,'actual_public_retry':loc(D/'PUBLIC_RETRY_PROOF_INDEX.json'),'operations_without_current_owning_evidence':[r['operation'] for r in rows if not r['current_retained_operation_witnesses']],'scope':'23 declared operations. Honest finite current/historical test and durable witness map, no implicit all-operation public/F_P/full-calculus qualification. No semantic review of every generated fixture.'})
# Current source custody manifest lists exact bytes and historical delta; no old-proof copying.
current_sources=json.loads((D/'suite-001/sources-after.json').read_text());prior=json.loads((P/'.ai-workspace/qualification/t008/interfaces/integration-001/SOURCE_MANIFEST.json').read_text())['sources'];oldsha={x['path']:x['sha256'] for x in prior}
save('SOURCE_MANIFEST.json',{'schema':'a_c.T008.closed-successor-source-manifest/2','sources':current_sources,'governing_sources':[{'path':k,'sha256':v,'bytes':(Repo/k).stat().st_size} for k,v in subject['required_sources'].items() if not k.startswith('a_c/build_tenants/graphify/')],'changes_from_historical_cut':[{'path':x['path'],'old_sha256':oldsha.get(x['path']),'current_sha256':x['sha256']} for x in current_sources if oldsha.get(x['path'])!=x['sha256']],'current_subject_sha256':h(D/'CLOSED_SUBJECT.json'),'original_tests':242,'current_tests':254,'actual_provider_calls':0})
for rel,sha in subject['required_sources'].items():assert h(Repo/rel)==sha
# Complete proof digest inventory is retained locally; selected review proof remains finite and smaller.
files=[loc(q) for q in sorted(D.rglob('*')) if q.is_file() and not q.is_symlink() and q.name!='EVIDENCE_MANIFEST.json']
links=[{'path':str(q.relative_to(P)),'target':str(q.readlink()),'kind':'symlink retained from explicit negative fixture; target not followed'} for q in sorted(D.rglob('*')) if q.is_symlink()]
save('EVIDENCE_MANIFEST.json',{'files':files,'symlinks':links,'actual_provider_calls':0,'scope':'Custody of generated mechanical proof only; no claim every member is semantically reviewed'})
save('CLOSED_RETURN.json',{'schema':'a_c.T008.integration-successor-return/2','state':'Closed current mechanical integration; F_P independent review and dispositions pending','source_manifest_sha256':h(D/'SOURCE_MANIFEST.json'),'evidence_manifest_sha256':h(D/'EVIDENCE_MANIFEST.json'),'subject_sha256':h(D/'CLOSED_SUBJECT.json'),'results_sha256':h(D/'RESULTS.json'),'operation_map_sha256':h(D/'OPERATION_SCENARIO_MAP.json'),'public_retry_index_sha256':h(D/'PUBLIC_RETRY_PROOF_INDEX.json'),'tests':254,'interface_helper_tests_separate':37,'strict_normal_import_files':9,'upstream_checks':9,'ordinary_public_demo_checks':10,'sources_unchanged':True,'operations_without_owning_durable_witness':[r['operation'] for r in rows if not r['current_retained_operation_witnesses']],'actual_provider_calls':0,'remaining':['Actual source-first nonauthor Reviewer expectation/assessment on this new exact cut','Separate ontology/design and owner dispositions','No installed/full-calculus/efficiency/release qualification']})
print(json.dumps({'closed_return':h(D/'CLOSED_RETURN.json'),'source_manifest':h(D/'SOURCE_MANIFEST.json'),'evidence_manifest':h(D/'EVIDENCE_MANIFEST.json'),'operation_map':h(D/'OPERATION_SCENARIO_MAP.json'),'retry_index':h(D/'PUBLIC_RETRY_PROOF_INDEX.json'),'selected_retry_raw_files':len(selected_retry),'selected_retry_raw_bytes':sum(x['bytes'] for x in selected_retry),'proof_files':len(files),'operation_witnesses':sum(len(v) for v in ops.values())},indent=2))
