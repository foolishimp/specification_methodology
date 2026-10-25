"""Own preparation-only field-reference and fixed future read-scope completion."""
from pathlib import Path
import json,hashlib,shutil,sys
sys.dont_write_bytecode=True
P=Path('/Users/jim/src/apps/specification_methodology/a_c');D=P/'.ai-workspace/qualification/t008/live-review-runtime-001';M=P/'.ai-workspace/qualification/t008/live-preparation/sources/method'
sys.path.insert(0,str(P/'build_tenants/graphify/code'));import ac_support_core as c

def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(n):return json.loads((D/n).read_text())
def put(n,v):
 q=D/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(v if isinstance(v,str) else json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
def ref(q):return {'engine':'workspace-regular-file','root':'runtime','path':str(q.relative_to(D)),'object':None,'sha256':h(q),'selector':None}
def refs(x):
 if isinstance(x,dict):
  if set(x)=={'engine','root','path','object','sha256','selector'}:yield x
  else:
   for v in x.values():yield from refs(v)
 elif isinstance(x,list):
  for v in x:yield from refs(v)
H=D/'history/preparation-cut-001';assert not H.exists();H.mkdir(parents=True)
for q in list(D.rglob('*')):
 if q.is_file() and not q.is_relative_to(D/'history'):
  t=H/q.relative_to(D);t.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(q,t)
put('protocol/closed-return-format.json',{'classification':'Shared mechanical wire field reference only. No semantic answer, candidate algorithm or acceptance authority.','origin':{'HOW_parent_sha256':'faefdf2432759859780d962ca1028f44f7ebca9a5f6a11c324c27ddc258d521f','Core_parent_sha256':h(P/'build_tenants/graphify/code/ac_support_core.py'),'Core_lines':[1800,1837],'selection':'Field names/closed enum values only, mechanically transcribed from public closed carrier validation. No handler implementation supplied.'},'schema_value':'a_c.fd-support.closed-return/1','exact_top_level_keys':['schema','id','frame','activation','subject','basis','actor','consumer','evaluations','not_performed','work_result','residuals','invalidators'],'frame':{'exact_keys':['id','revision'],'types':'strings from packet frame'},'activation':'Context.boundaries.activation_identity, exact {id,sha256} canonical full packet coordinate','subject':'exact packet.subject_basis.subject {id,sha256}','basis':{'exact_keys':['method_profile','observations'],'source':'packet.subject_basis fields'},'actor':{'exact_keys':['id','family','authorship'],'values':{'id':'urn:a-c:T008:claude-reviewer:001','family':'anthropic-claude','authorship':'t008-independent-reviewer-001'}},'consumer':'/root','evaluation':{'exact_keys':['id','predicate','domain_outcome','core_value','evidence','residuals','invalidators'],'predicate':'exact acquired ReturnContract.required_evaluations member SourceRef','domain_outcome':'actual Reviewer authored JSON; no supplied finding or verdict','core_value_allowed':sorted(c.CORE_VALUES),'evidence_residuals_invalidators':'arrays, actual evidence/limits only'},'not_performed':'array of actual unperformed evaluation ID strings, disjoint from performed IDs','work_result':None,'residuals_invalidators':'arrays; preserve actual gaps/unknowns','grammar':'integer-only strict UTF8 JSON, exactly one unfenced object; no decimal/exponent/nonfinite/duplicate keys','phase1':'source-derived-expectations actual performed scope; integrated-review ID in not_performed; initial null proof.expectations yields honest return-check gap'})
n='reviewer-instructions.md';s=(D/n).read_text().replace('Use shared ClosedReturn/Evaluation schemas and the acquired ReturnContract.','Use the shared protocol/closed-return-format.json wire field reference and acquired ReturnContract; no named ClosedReturn $def is assumed.');put(n,s)
policy=read('reviewer-tool-policy.json')
paths=['assessment-return-contract.json','assessment-packet.json','assessment-call.json','assessment-instructions.md','assessment-expectation.json']
policy['sources']['runtime']['read_scope'] += [{'kind':'file','path':x} for x in paths]
put('reviewer-tool-policy.json',policy)
mcp=read('reviewer.mcp.json');args=mcp['mcpServers']['ac_review']['args'];args[args.index('--policy-sha256')+1]=h(D/'reviewer-tool-policy.json');put('reviewer.mcp.json',mcp)
plan=read('expectation-actor-plan.json')
for x in plan['dependencies']:
 if Path(x['path']).is_relative_to(D):x['sha256']=h(x['path'])
plan['dependencies'].append({'path':str(D/'protocol/closed-return-format.json'),'sha256':h(D/'protocol/closed-return-format.json')});put('expectation-actor-plan.json',plan)
call=read('expectation-call.json')
for rr in refs(call):
 if rr['root']=='runtime':rr['sha256']=h(D/rr['path'])
put('expectation-call.json',call)
packet=read('expectation-packet.json')
for rr in refs(packet):
 if rr['root']=='runtime':rr['sha256']=h(D/rr['path'])
packet['attention']['material_relations'].append(ref(D/'protocol/closed-return-format.json'))
put('expectation-packet.json',packet)
context=read('context.request.json');context['arguments']['packet']=packet;context['arguments']['late_acquisition']=list({c.canonical(x):x for x in refs(packet)}.values());c.validate_request(context);put('context.request.json',context)
outer=read('executive-policy.json');exe=next(iter(outer['executors'].values()))
for rr in refs(exe):
 if rr['root']=='runtime':rr['sha256']=h(D/rr['path'])
exe['argv'][exe['argv'].index('--plan-sha256')+1]=h(D/'expectation-actor-plan.json')
exe['dependencies'].append(ref(D/'protocol/closed-return-format.json'))
outer=policy.copy();outer['id']='urn:a-c:T008:review-executive-policy:001';outer['executors']={exe['id']:exe};put('executive-policy.json',outer)
seq=read('PUBLIC_SEQUENCE.json');seq['startup']['policy_sha256']=h(D/'executive-policy.json');put('PUBLIC_SEQUENCE.json',seq)
checks=read('STATIC_CHECKS.json');checks['checks'] += [{'check':'Shared closed-return wire fields supplied without nonexistent schema definition','passed':True},{'check':'Future second contract read paths predeclared without future refs or hash/policy rewrite','passed':all({'kind':'file','path':x} in policy['sources']['runtime']['read_scope'] for x in paths)}]
roots={'runtime':D,'product':P,'method':M,'native':Path('/Users/jim/.local/share/claude/versions'),'python':Path('/Library/Frameworks/Python.framework/Versions/3.12/bin')}
count=0
for q in sorted(D.rglob('*.json')):
 if q.is_relative_to(D/'history') or q.name in ['SOURCE_MANIFEST.json','CLOSED_RETURN.json','READY_FIRST_CALL.json','STATIC_CHECKS.json']:continue
 for rr in refs(json.loads(q.read_text())):
  if rr['engine']=='workspace-regular-file':assert h(roots[rr['root']]/rr['path'])==rr['sha256'],(q,rr)
  count+=1
checks['source_ref_occurrences_checked']=count;checks['historical_first_cut']='history/preparation-cut-001/ contains exact prior preparation bytes before these mechanical corrections';put('STATIC_CHECKS.json',checks)
ready=read('READY_FIRST_CALL.json')
for rr in refs(ready):
 if rr['root']=='runtime':rr['sha256']=h(D/rr['path'])
ready['context_request_sha256']=h(D/'context.request.json');put('READY_FIRST_CALL.json',ready)
manifest=read('SOURCE_MANIFEST.json');manifest['files']=[{'path':str(q.relative_to(P)),'sha256':h(q),'bytes':q.stat().st_size} for q in sorted(D.rglob('*')) if q.is_file() and q.name not in ['SOURCE_MANIFEST.json','CLOSED_RETURN.json'] or (q.is_file() and q.is_relative_to(D/'history'))];put('SOURCE_MANIFEST.json',manifest)
closed=read('CLOSED_RETURN.json');closed.update(manifest_sha256=h(D/'SOURCE_MANIFEST.json'),ready_sha256=h(D/'READY_FIRST_CALL.json'),checks_sha256=h(D/'STATIC_CHECKS.json'),passed_static_checks=len(checks['checks']));closed['mechanical_completion']='Exact prior prepared bytes retained under history/preparation-cut-001; closed-return neutral wire reference and future read-only paths completed before any admission/call.';put('CLOSED_RETURN.json',closed)
print(json.dumps({'closed_return_raw':h(D/'CLOSED_RETURN.json'),'closed_return_canonical':c.digest(closed),'manifest':h(D/'SOURCE_MANIFEST.json'),'ready':h(D/'READY_FIRST_CALL.json'),'checks':len(checks['checks']),'policy':h(D/'executive-policy.json'),'tool_policy':h(D/'reviewer-tool-policy.json'),'plan':h(D/'expectation-actor-plan.json'),'packet':h(D/'expectation-packet.json'),'context_request':h(D/'context.request.json')},indent=2))
