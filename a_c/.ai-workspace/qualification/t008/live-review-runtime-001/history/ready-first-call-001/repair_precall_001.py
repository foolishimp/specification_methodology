"""Bounded pre-call successor only. No Runtime or support operation executes."""
from pathlib import Path
import json,hashlib,shutil,sys,base64
sys.dont_write_bytecode=True
P=Path('/Users/jim/src/apps/specification_methodology/a_c');D=P/'.ai-workspace/qualification/t008/live-review-runtime-001';M=P/'.ai-workspace/qualification/t008/live-preparation/sources/method'
sys.path.insert(0,str(P/'build_tenants/graphify/code'));import ac_support_core as c
h=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
def read(n):return json.loads((D/n).read_text())
def put(n,v):
 q=D/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(v if isinstance(v,str) else json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
def refs(o):
 if isinstance(o,dict):
  if set(o)=={'engine','root','path','object','sha256','selector'}:yield o
  else:
   for v in o.values():yield from refs(v)
 elif isinstance(o,list):
  for v in o:yield from refs(v)
roots={'runtime':D,'product':P,'method':M,'native':Path('/Users/jim/.local/share/claude/versions'),'python':Path('/Library/Frameworks/Python.framework/Versions/3.12/bin')}
def fresh(o):
 for rr in refs(o):
  if rr['root']=='runtime':rr['sha256']=h(D/rr['path'])
 return o

def rf(n):return dict(engine='workspace-regular-file',root='runtime',path=n,object=None,sha256=h(D/n),selector=None)
contract='''Root intake verifiesall77manifest+plan/dependency/scratch pins, but found concrete PRE-CALL preparation issue: population82 includes full vendor.stdout1,566,183bytes (third-partyhidden-reasoning/rawinternalstream) plus rawselectedfiles2,977,630bytes +8protectedArtifactstotal; review.prepare candidate autoacquiresALL population and base64returnsit, likely exceeds4MiB output bound. Fullhiddenrawstream is not needed for semanticreview and should notbedeliveredtoReviewer. NEW boundedpre-call successorgrant sameownprefix/history exact priorfreeze preserved: remove whole vendor.stdout fromclaim/population (and source permission ifappropriate) while retaining actualsafeCLIENT_TOOLS/native.metadata/publicWriterrequest/response/protectedWriterproof/process/capture/check as selectedrawprovenance; exactoriginalstreamhash/line routes remain inmetadata, no rawthinkingcopy. Canuse safe existingextractedrawWriter.tool-use etc notwholeStream. Declare omittedwholevendorstreamscope explicitly (noall-provider-event review); candidatecomplete finitepopclaimnewidentity. Quantifypure upperboundbase64candidate_response bytes vs4MiB; protectedenvelope rawcanonicalbytesincluded. Keepallcore/HOW/guide/test/qualification selectedcoverage; don'taddproof. Also Rootselectschunkbudget max_content_bytes8192 asdocumentedconservativecallerbound (selected31KBactualdescriptions delivered;49KBresponsepersisted;8KBraw+metadata comfortablybelow), instead1536 toreduceunnecessarycalls; instructions10-80lineswithadaptiveboundedrefusal smaller exactchunks no truncationclaim. Noactivepolicy/Actor torepin (nonecalled); preserve001closedready/manifestfilesexactbeforemechanicalsuccessor, noeditbaseadmissionreceipts. Recomputeaffectedacyclicfirst-callpins,17checks plusbytebound/excludedhiddenstream, closedsuccessorreturn. Secondstillheld, noRootorActoroperationsbyyou. Needminimalrepairreturnpromptly, notscopeexpansion. Noothermetadatachanges.
'''
assert h(D/'CLOSED_RETURN.json')=='d85f7310f7924a5eebd8662cf1f485833f7304c27438ca54d993fc697e19e52c'
put('precall-successor-001/REPAIR.contract.txt',contract)
put('precall-successor-001/REPAIR.admission.json',{'reported_by':'/root','activation':'T008-precall-successor-001','prior_closed_return_sha256':h(D/'CLOSED_RETURN.json'),'prior_manifest_sha256':h(D/'SOURCE_MANIFEST.json'),'writes':'Own preparation prefix/history only; no source/code/HOW/guide/T008/global/Git edits','permitted':['Exclude whole vendor.stdout from selected claim and source permission','8192-byte adaptive small readable source chunks','Pure public4MiB/MCP8MiB response measurements','Recompute affected acyclic pins and close successor'],'not_authorized':['support operations','provider/model/CLI/MCP/dispatch calls','second call finalization','further proof removal/addition']})
put('precall-successor-001/BOUND.selection.txt','Root: Agreed: retain separate actual public4MiB versus MCPmessage8MiB bound; no further population removal. Oversized native preview after candidate phase is explicit and must not count readable whole proof; independent UTF8 chunk route decides actual coverage. No semantic recap answer in phase1. Close minimal measured successor then Root starts ordinary calls.\n')
H=D/'history/ready-first-call-001';assert not H.exists();H.mkdir(parents=True)
for q in list(D.rglob('*')):
 if q.is_file() and not q.is_relative_to(D/'history') and not q.is_relative_to(D/'precall-successor-001'):
  t=H/q.relative_to(D);t.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(q,t)
# Verify all77 historical manifest members still exact before changing prepared bytes.
old=read('SOURCE_MANIFEST.json');assert len(old['files'])==77
assert all(h(P/x['path'])==x['sha256'] for x in old['files'])
omitted_path='.ai-workspace/qualification/t008/live-runtime-prep-002/actor-transports/worker-001/vendor.stdout'
claim=read('review-claim.json');old_population=claim['candidate_sources'];excluded=[x for x in old_population if x['root']=='product' and x['path']==omitted_path];assert len(excluded)==1
claim['candidate_sources']=[x for x in old_population if x not in excluded];assert len(claim['candidate_sources'])==81;put('review-claim.json',claim)
cm=read('candidate-manifest.json');cm['population']=claim['candidate_sources'];cm['members']=[x for x in cm['members'] if x['source'] not in excluded]
cm['scope'] += ' Whole vendor.stdout is deliberately excluded: no all-provider-event/internal-stream review or delivery. Its exact original hash and source line routes remain in selected safe acquisition/provenance metadata. Selected safe CLIENT_TOOLS/native metadata, Writer request/response/tool-use, process/capture/check remain available. No other declared coverage removed.'
cm['excluded_whole_vendor_stream']={'source':excluded[0],'bytes':(P/omitted_path).stat().st_size,'reason':'Whole third-party internal stream not needed or delivered for this semantic review; selected safe raw provenance remains. No raw thinking copy.'};put('candidate-manifest.json',cm)
# Adaptive caller budget only; grammar/path/hash/runtime semantics unchanged.
s=(D/'reviewer-instructions.md').read_text().replace('normally 10–20 lines, max_content_bytes 1536 or lower','normally 10–80 lines, max_content_bytes 8192 or lower').replace('Split further if needed.','Adapt to exact line lengths; split further after bounded refusal or preview.');put('reviewer-instructions.md',s)
# New claim -> independence -> ReturnContract -> policy -> MCP -> helper -> call -> packet -> outer.
ind=fresh(read('independence-policy.json'));put('independence-policy.json',ind)
rc=fresh(read('expectation-return-contract.json'));put('expectation-return-contract.json',rc)
held=fresh(read('assessment.HELD.json'));put('assessment.HELD.json',held)
policy=fresh(read('reviewer-tool-policy.json'));sc=policy['sources']['product']['read_scope'];policy['sources']['product']['read_scope']=[x for x in sc if x['path']!=omitted_path];put('reviewer-tool-policy.json',policy)
mcp=read('reviewer.mcp.json');a=mcp['mcpServers']['ac_review']['args'];a[a.index('--policy-sha256')+1]=h(D/'reviewer-tool-policy.json');put('reviewer.mcp.json',mcp)
plan=read('expectation-actor-plan.json')
for x in plan['dependencies']:
 if Path(x['path']).is_relative_to(D):x['sha256']=h(x['path'])
put('expectation-actor-plan.json',plan)
call=fresh(read('expectation-call.json'));put('expectation-call.json',call)
packet=fresh(read('expectation-packet.json'));packet['subject_basis']['subject']['sha256']=h(D/'review-claim.json');put('expectation-packet.json',packet)
context=read('context.request.json');context['arguments']['packet']=packet;context['arguments']['late_acquisition']=list({c.canonical(x):x for x in refs(packet)}.values());c.validate_request(context);put('context.request.json',context)
outer=read('executive-policy.json');exe=fresh(next(iter(outer['executors'].values())));exe['argv'][exe['argv'].index('--plan-sha256')+1]=h(D/'expectation-actor-plan.json');outer=policy.copy();outer['id']='urn:a-c:T008:review-executive-policy:001';outer['executors']={exe['id']:exe};put('executive-policy.json',outer)
seq=read('PUBLIC_SEQUENCE.json');seq['startup']['policy_sha256']=h(D/'executive-policy.json');put('PUBLIC_SEQUENCE.json',seq)
# Pure exact source-byte reconstruction for the one planned initial candidate response.
# It neither calls read_source nor instantiates a Runtime. All source selectors are null.
def raw(rr):
 if rr['engine']=='retained-evidence':return (P/'.ai-workspace/qualification/t008/live/evidence/objects'/f"{rr['sha256']}.json").read_bytes()
 return (roots[rr['root']]/rr['path']).read_bytes()
request_refs=[rf('review-claim.json')]+claim['candidate_sources'];acquired=[]
for rr in request_refs:
 b=raw(rr);assert hashlib.sha256(b).hexdigest()==rr['sha256'];assert rr['selector'] is None
 acquired.append({'source':rr,'parent_sha256':rr['sha256'],'selected_sha256':rr['sha256'],'size_bytes':len(b),'content_base64':base64.b64encode(b).decode('ascii'),'coordinates':None,'acquisition':None})
# Fixed-width sizing-only sentinel, never emitted as a runnable future reference.
sentinel={'id':'sha256:'+'f'*64,'sha256':'f'*64}
value={'phase':'candidate','claim':rf('review-claim.json'),'candidate_population':claim['candidate_sources'],'population_complete':True,'acquired':acquired,'expectations':sentinel,'exposure':[],'comparison':None,'independence':{'selected_policy':rf('independence-policy.json'),'semantic_independence':'not certified','external_exposure':'unknown','governing_conditions':ind},'gaps':[],'limits':['acquisition/diff/exposure facts only; no severity, disposition or mental-independence certificate']}
boundary=c.operation_outcome('review.prepare');boundary['predicate']='B(review.prepare)[request_sha256='+'f'*64+']: declared output availability'
response={'schema':'a_c.fd-support.response/1','id':'t008-review-candidate-001','operation':'review.prepare','status':'ok','result':{'artifact':sentinel,'value':value},'refusal':None,'operation_outcome':boundary,'evidence':sentinel}
response_bytes=len(c.canonical(response));wire={'jsonrpc':'2.0','id':1,'result':{'content':[{'type':'text','text':c.canonical(response).decode('utf8')}],'structuredContent':response,'isError':False}}
wire_bytes=len(c.canonical(wire))+1
# Reserve for future dynamic request ID/history/gap metadata. Bound is conditional, not false unconditional future fit.
reserve=1024*1024;public_bound=response_bytes+reserve;mcp_bound=wire_bytes+2*reserve+65536
sizes={'schema':'a_c.T008.pure-candidate-response-byte-bound/1','method':'Reconstructed exact pinned read_source/public response/MCP shapes from frozen bytes using pure serialization only; no support operation/Runtime/provider call','scope':'Planned first candidate-phase request with claim plus complete81-member population, no added sources/proof/comparison; clean prior candidate-exposure history. Actual expectation/hash/OperationEvidence use fixed-width sizing surrogate only, not a future ref or runnable request.','selected_workspace_members':len(cm['members']),'selected_workspace_bytes':sum(x['bytes'] for x in cm['members']),'protected_canonical_envelopes':8,'protected_canonical_bytes':sum(len(raw(x)) for x in claim['candidate_sources'] if x['engine']=='retained-evidence'),'claim_bytes':len(raw(rf('review-claim.json'))),'all_acquired_raw_bytes':sum(x['size_bytes'] for x in acquired),'base64_content_bytes':sum(len(x['content_base64']) for x in acquired),'skeleton_public_response_utf8_bytes':response_bytes,'skeleton_MCP_wire_utf8_bytes':wire_bytes,'dynamic_public_metadata_reserve_bytes':reserve,'MCP_extra_framing_reserve_bytes':65536,'conditional_public_upper_bound_bytes':public_bound,'public_comparison_bound_bytes':4194304,'conditional_MCP_upper_bound_bytes':mcp_bound,'MCP_policy_max_message_bytes':policy['limits']['max_message_bytes'],'public_under4MiB':public_bound<4194304,'MCP_under8MiB':mcp_bound<8388608,'conditions':['Additional actual public request-id/history/exposure/gap data must fit1MiB reserve; if exceeded, this bound is inapplicable and must be remeasured/refused without truncation','No added sources/proof/comparison outside frozen population; no generic output/all-provider-event proof','MCP duplicates response in text and structuredContent; actual native wrapper may still preview/save despite protocol byte bound','Bulk review.prepare is metadata/evidence route only; actual semantic coverage depends independent readable UTF8 chunks, never base64/preview/saved path'],'actual_execution':False}
assert sizes['public_under4MiB'] and sizes['MCP_under8MiB'],sizes
put('precall-successor-001/CANDIDATE_BYTE_BOUND.json',sizes)
checks=read('STATIC_CHECKS.json');checks['candidate_members']=81
checks['checks'] += [{'check':'Whole vendor.stdout excluded from claim/population and read permission; exact hash retained in metadata','passed':not any(x.get('path')==omitted_path for x in claim['candidate_sources']) and not any(x['path']==omitted_path for x in policy['sources']['product']['read_scope'])},{'check':'Selected caller chunk budget8192 with adaptive exact10-80-line acquisition and preview rejection','passed':'max_content_bytes 8192' in s},{'check':'Pure conditional public response upper bound below4MiB and doubled MCP wire below8MiB, protected envelopes included','passed':sizes['public_under4MiB'] and sizes['MCP_under8MiB']}]
count=0
for q in D.rglob('*.json'):
 if q.is_relative_to(D/'history') or q.name in ['SOURCE_MANIFEST.json','CLOSED_RETURN.json','READY_FIRST_CALL.json','STATIC_CHECKS.json']:continue
 for rr in refs(json.loads(q.read_text())):
  if rr['engine']=='workspace-regular-file':assert h(roots[rr['root']]/rr['path'])==rr['sha256'],(q,rr)
  elif rr['engine']=='retained-evidence':assert hashlib.sha256(raw(rr)).hexdigest()==rr['sha256']
  count+=1
checks['source_ref_occurrences_checked']=count;checks['historical_ready_cut']='history/ready-first-call-001/ preserves prior d85f7310 cut; earlier history remains exact';checks['candidate_byte_bound_sha256']=h(D/'precall-successor-001/CANDIDATE_BYTE_BOUND.json');put('STATIC_CHECKS.json',checks)
ready=fresh(read('READY_FIRST_CALL.json'));ready['context_request_sha256']=h(D/'context.request.json');ready['precall_successor']='precall-successor-001';ready['candidate_byte_bound_sha256']=h(D/'precall-successor-001/CANDIDATE_BYTE_BOUND.json');put('READY_FIRST_CALL.json',ready)
manifest=read('SOURCE_MANIFEST.json');manifest['files']=[{'path':str(q.relative_to(P)),'sha256':h(q),'bytes':q.stat().st_size} for q in sorted(D.rglob('*')) if q.is_file() and (q.is_relative_to(D/'history') or q.name not in ['SOURCE_MANIFEST.json','CLOSED_RETURN.json'])];put('SOURCE_MANIFEST.json',manifest)
closed=read('CLOSED_RETURN.json');closed.update(manifest_sha256=h(D/'SOURCE_MANIFEST.json'),ready_sha256=h(D/'READY_FIRST_CALL.json'),checks_sha256=h(D/'STATIC_CHECKS.json'),passed_static_checks=len(checks['checks']),exact_candidate_population_members=81,predecessor_closed_return_sha256='d85f7310f7924a5eebd8662cf1f485833f7304c27438ca54d993fc697e19e52c',candidate_byte_bound_sha256=h(D/'precall-successor-001/CANDIDATE_BYTE_BOUND.json'));closed['mechanical_completion']='Pre-call successor excludes only whole vendor.stdout and changes caller chunk budget8192; all prior ready bytes retained under history/ready-first-call-001. Acyclic pins recomputed, no active Attempt existed.';put('CLOSED_RETURN.json',closed)
print(json.dumps({'closed_raw':h(D/'CLOSED_RETURN.json'),'closed_canonical':c.digest(closed),'manifest':h(D/'SOURCE_MANIFEST.json'),'ready':h(D/'READY_FIRST_CALL.json'),'checks':len(checks['checks']),'population':81,'policy':h(D/'executive-policy.json'),'tool_policy':h(D/'reviewer-tool-policy.json'),'plan':h(D/'expectation-actor-plan.json'),'packet':h(D/'expectation-packet.json'),'context_request':h(D/'context.request.json'),'public_skeleton_bytes':response_bytes,'public_upper_bound':public_bound,'MCP_skeleton_bytes':wire_bytes,'MCP_upper_bound':mcp_bound},indent=2))
