"""Factual typed-only reconciliation. No support/provider/process/Git calls; no assistant text/thinking extraction."""
from pathlib import Path
import base64,collections,hashlib,json,re,time
P=Path('/Users/jim/src/apps/specification_methodology/a_c');D=P/'.ai-workspace/qualification/t008/live-review-runtime-002';R=Path(__file__).resolve().parent;A=D/'actor-transports/assessment-001';E=P/'.ai-workspace/qualification/t008/live/evidence/objects'
I=P/'.ai-workspace/qualification/t008/interfaces/integration-002'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf8')
def load(q):return json.loads(q.read_text())
def save(n,v):
 q=R/n;raw=v if isinstance(v,str) else json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
 if q.exists() and q.read_text()==raw:return q
 assert n not in ['RECONCILIATION.contract.txt','RECONCILIATION.admission.json'],n
 q.write_text(raw);return q
def artifact(sha):
 q=E/(sha+'.json');assert h(q)==sha;return load(q)
def loc(q):return {'path':str(q.relative_to(P)),'sha256':h(q),'bytes':q.stat().st_size}
process=load(A/'process.json');result=load(A/'result.json');invocation=load(A/'invocation.json');plan=load(A/'plan.json');start=process['started_ns'];end=process['ended_ns']
assert process['pid']==40963 and process['returncode']==143 and process['failure'].startswith('timeout') and not process['output_available'];assert process['input_bytes']==process['input_forwarded_bytes']==42606 and process['stdout_bytes']==3553404;assert plan['limits']['timeout_ms']==1200000
save('PROCESS_OBSERVATION.json',{'process':process,'helper_result':result,'native_elapsed_seconds':(end-start)/1e9,'raw_sources':[loc(A/n) for n in ['process.json','result.json','plan.json','invocation.json']],'input_forwarding_complete_at_local_native_stdin':True,'end_scope':'Observed native registered parent return143 only; descendant/process-tree/external effect end remains unknown. Outer helper exit1 is Root-reported and protected observe is separately bound.','usage_billing':'Unknown; no inferred zero or estimate.'})
# Whitelist parser: only initialization, tool_use, user.tool_result and final RESULT METADATA.
# Never copy/inspect assistant text/thinking values or other assistant message fields.
stream=A/'vendor.stdout';events=[];calls=[];results={};inits=[];finals=[];excluded_types=collections.Counter();parse_errors=[]
with stream.open('rb') as f:
 for line_no,raw in enumerate(f,1):
  if not raw.strip():continue
  try:row=json.loads(raw)
  except (ValueError,UnicodeError):parse_errors.append({'line':line_no,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()});continue
  if not isinstance(row,dict):continue
  typ=row.get('type')
  if typ=='system' and row.get('subtype')=='init':
   fields={k:row[k] for k in ['type','subtype','cwd','tools','mcp_servers','model','permissionMode','claude_code_version','output_style','session_id'] if k in row};event={'source_line':line_no,'source_line_sha256':hashlib.sha256(raw).hexdigest(),'kind':'typed_init','fields':fields};events.append(event);inits.append(event)
  elif typ=='assistant':
   message=row.get('message',{});blocks=message.get('content',[]) if isinstance(message,dict) else []
   for block in blocks if isinstance(blocks,list) else []:
    if not isinstance(block,dict):continue
    if block.get('type')!='tool_use':excluded_types[str(block.get('type','unknown'))]+=1;continue
    event={'source_line':line_no,'source_line_sha256':hashlib.sha256(raw).hexdigest(),'kind':'tool_use','id':block.get('id'),'name':block.get('name'),'input':block.get('input')};events.append(event);calls.append(event)
  elif typ=='user':
   message=row.get('message',{});blocks=message.get('content',[]) if isinstance(message,dict) else []
   for block in blocks if isinstance(blocks,list) else []:
    if isinstance(block,dict) and block.get('type')=='tool_result':
     event={'source_line':line_no,'source_line_sha256':hashlib.sha256(raw).hexdigest(),'kind':'tool_result','tool_use_id':block.get('tool_use_id'),'is_error':block.get('is_error',False),'content':block.get('content')};events.append(event);results.setdefault(str(block.get('tool_use_id')),[]).append(event)
  elif typ=='result':
   fields={k:row[k] for k in ['type','subtype','is_error','duration_ms','duration_api_ms','num_turns','total_cost_usd','usage','modelUsage','stop_reason'] if k in row};event={'source_line':line_no,'source_line_sha256':hashlib.sha256(raw).hexdigest(),'kind':'final_result_metadata','fields':fields};events.append(event);finals.append(event)
  else:excluded_types['row:'+str(typ)]+=1
# Typed-only export deliberately contains no assistant prose/thinking fields.
save('TYPED_EVENTS.jsonl',''.join(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n' for x in events))
assert not finals,'Root-reported no final result contradicted by allowed final metadata'
# Match actual native typed full-envelope calls to protected operation evidence in this observed interval.
protected={};all_ops=[]
for q in sorted(E.glob('*.json')):
 try:obj=load(q)
 except (ValueError,UnicodeError):continue
 if obj.get('kind')!='operation':continue
 prov=obj.get('provenance',{});interval=prov.get('observed_interval') or {};actor=prov.get('actor') or {}
 if prov.get('policy_sha256')!='d3dbebed35e3532d9d8a8e44df25f25a1b5bef115bffc6a7ede09f4a9b27f083' or actor.get('actor_id')!='urn:a-c:T008:claude-reviewer:001':continue
 if not start<=interval.get('started_ns',0)<=end:continue
 assert h(q)==q.stem
 req=obj['payload']['request'];key=hashlib.sha256(canon(req)).hexdigest();protected.setdefault(key,[]).append((q,obj));all_ops.append((q,obj))
# Decode only an allowed tool-result body's PUBLIC response; never infer a full response from a preview.
def public_responses(value,depth=0):
 if depth>7:return []
 if isinstance(value,str):
  try:return public_responses(json.loads(value),depth+1)
  except (ValueError,UnicodeError):return []
 if isinstance(value,list):
  out=[]
  for x in value:
   if isinstance(x,dict) and x.get('type')=='text':out+=public_responses(x.get('text'),depth+1)
  return out
 if isinstance(value,dict):
  if value.get('schema')=='a_c.fd-support.response/1':return [value]
  out=[]
  if 'structuredContent' in value:out+=public_responses(value['structuredContent'],depth+1)
  if 'content' in value:out+=public_responses(value['content'],depth+1)
  return out
 return []
claim=load(D/'review-claim.json');population=claim['candidate_sources']
def same_parent(a,b):return isinstance(a,dict) and all(a.get(k)==b.get(k) for k in ['engine','root','path','object'])
def is_candidate_ref(r):return isinstance(r,dict) and any(same_parent(r,p) for p in population)
def source_kind(r):
 path=r.get('path','');sel=r.get('selector') or {};pointer=sel.get('json_pointer','')
 if r.get('engine')=='retained-evidence':
  if pointer=='/payload/text':return 'actual earlier F_P expectation text'
  if '/original/evaluations/' in pointer:return 'actual original phase1 judgment field'
  return 'protected acquisition/provenance/exposure metadata'
 if r.get('root')=='method':return 'governing method text'
 if r.get('root')=='runtime':
  if path.startswith('protocol/'):return 'shared mechanical wire apparatus'
  if path.startswith('authority/'):return 'mechanical governing route metadata'
  if path=='review-claim.json':return 'candidate locator metadata, no candidate body'
  return 'governing task/instructions/independence/bridge metadata'
 if path.startswith('specification/') or path=='stdo_a_c.json':return 'governing Product/requirements/basis'
 if '/tickets/' in path:return 'selected owner authority'
 if path.endswith('design/fd-support.md'):return 'candidate HOW/design body'
 if '/code/' in path:return 'candidate code body'
 if '/test_env/' in path and '/qualification/' not in path:return 'candidate test/fixture source'
 if path.endswith('LIFECYCLE_QUICKSTART.md'):return 'candidate guide body'
 if '/qualification/' in path:return 'selected mechanical proof/log/metadata'
 return 'other selected source body/metadata'
rows=[];source_rows=[];review_rows=[];first_candidate=None;pending=[]
for call in calls:
 inp=call.get('input');request=inp if isinstance(inp,dict) and inp.get('schema')=='a_c.fd-support.request/1' else None
 if request is None:
  row={'source_line':call['source_line'],'tool_use_id':call['id'],'name':call['name'],'full_public_request_observed':False,'matching_tool_result':bool(results.get(str(call['id'])))};rows.append(row);continue
 key=hashlib.sha256(canon(request)).hexdigest();matches=protected.get(key,[]);response_records=results.get(str(call['id']),[]);decoded=[]
 for r in response_records:decoded+=public_responses(r['content'])
 # Host preview marker is a factual wrapper observation, not a statement about the omitted result.
 result_text=json.dumps([r['content'] for r in response_records],ensure_ascii=False)
 preview=bool(re.search(r'persisted.output|saved (?:to|at)|full output|output (?:too large|exceeds)|truncat|preview',result_text,re.I))
 publics=[r for r in decoded if r.get('id')==request.get('id') and r.get('operation')==request.get('operation')]
 preview=preview and not publics
 row={'source_line':call['source_line'],'tool_use_id':call['id'],'tool':call['name'],'request_id':request['id'],'operation':request['operation'],'arguments':request['arguments'],'request_sha256':key,'typed_result_lines':[r['source_line'] for r in response_records],'typed_public_response_complete':bool(publics),'host_saved_or_preview_marker':preview,'protected_operation_evidence':[{'id':'sha256:'+q.stem,'sha256':q.stem} for q,o in matches],'protected_statuses':[o['payload']['response_without_evidence']['status'] for q,o in matches],'pending_typed_tool_result':not response_records}
 if not response_records:pending.append({'tool_use_id':call['id'],'source_line':call['source_line'],'request_id':request['id'],'operation':request['operation'],'protected_operation_complete':bool(matches),'meaning':'No typed result observed before timeout; no automatic continuation/end claim.'})
 args=request['arguments'];candidate=(request['operation']=='source.read' and is_candidate_ref(args.get('source'))) or (request['operation']=='review.prepare' and args.get('phase')=='candidate')
 if candidate and first_candidate is None:first_candidate={'source_line':call['source_line'],'tool_use_id':call['id'],'request_id':request['id'],'operation':request['operation'],'scope':'First observed potential candidate acquisition request; native semantic reading still judged separately.'}
 if request['operation']=='source.read':
  readable=False;contents=[];protected_contents=[((o['payload']['response_without_evidence'].get('result') or {}).get('value') or {}).get('content') for q,o in matches]
  for pub in publics:
   value=(pub.get('result') or {}).get('value') or {}
   if pub.get('status')=='ok' and args.get('encoding')=='utf8' and isinstance(value.get('content'),str) and value['content'] in protected_contents:readable=True;contents.append(value['content'])
  sr={'request_id':request['id'],'source_line':call['source_line'],'source':args.get('source'),'source_class':source_kind(args.get('source') or {}),'encoding_requested':args.get('encoding'),'max_content_bytes':args.get('max_content_bytes'),'candidate_parent_match':is_candidate_ref(args.get('source')),'typed_utf8_content_observed_complete':readable,'typed_content_matched_protected_output':readable,'typed_utf8_content_bytes':sorted(set(len(x.encode()) for x in contents)),'typed_utf8_content_sha256':sorted(set(hashlib.sha256(x.encode()).hexdigest() for x in contents)),'host_saved_or_preview_marker':preview,'protected_operation_evidence':row['protected_operation_evidence'],'protected_statuses':row['protected_statuses'],'protected_refusals':[o['payload']['response_without_evidence'].get('refusal') for q,o in matches if o['payload']['response_without_evidence'].get('refusal')],'interpretation':'Observed complete typed UTF8 field matches the exact protected output; proves this route/output, not mental attention. Protected-only success or preview does not count as readable whole-source acquisition.'}
  source_rows.append(sr)
 if request['operation']=='review.prepare':
  rr={'request_id':request['id'],'source_line':call['source_line'],'phase':args.get('phase'),'typed_public_response_complete':bool(publics),'host_saved_or_preview_marker':preview,'protected_operation_evidence':row['protected_operation_evidence'],'emitted_expectations':[],'candidate_result':[]}
  for q,obj in matches:
   response=obj['payload']['response_without_evidence'];value=(response.get('result') or {}).get('value') or {}
   if args.get('phase')=='expectation':
    ar=(response.get('result') or {}).get('artifact')
    if ar:
     expected=artifact(ar['sha256']);assert expected['kind']=='expectation';ep=expected['payload'];native_saw=any(((pr.get('result') or {}).get('artifact') or {}).get('sha256')==ar['sha256'] for pr in publics)
     rr['emitted_expectations'].append({'artifact':ar,'protected_schema':ep['schema'],'producer_actor':ep['producer']['actor_id'],'source_inputs_count':len(ep['source_inputs']),'text_utf8_bytes':len(ep['text'].encode()),'text_sha256':hashlib.sha256(ep['text'].encode()).hexdigest(),'source_first_observed':ep['exposure_check']['source_first_observed'],'exposure_gaps':ep['exposure_check']['gaps'],'population_complete':ep['exposure_check']['population_complete'],'native_ref_observed_in_complete_typed_response':native_saw,'operation_interval':obj['provenance']['observed_interval'],'standing':'Supplemental expectation assertion only, never a returned judgment on the four later predicates; original phase1I not rewritten.'})
   else:rr['candidate_result'].append({'protected_status':response['status'],'population_complete':value.get('population_complete'),'population_count':len(value.get('candidate_population',[])),'acquired_record_count':len(value.get('acquired',[])),'bound_expectation':value.get('expectations'),'gaps':value.get('gaps'),'full_native_semantic_read_from_bulk_response':False})
  review_rows.append(rr)
 rows.append(row)
first_candidate_start=None
if first_candidate is not None:
 first_row=next(x for x in rows if x.get('tool_use_id')==first_candidate['tool_use_id'])
 starts=[]
 for opref in first_row.get('protected_operation_evidence',[]):
  obj=artifact(opref['sha256'])
  for ar in obj['payload'].get('acquisitions',[]):
   acq=artifact(ar['sha256']);interval=(acq.get('payload',{}).get('delivery') or {}).get('interval') or {}
   if interval.get('started_ns') is not None:starts.append(interval['started_ns'])
 first_candidate_start=min(starts) if starts else None
 first_candidate['protected_acquisition_started_ns']=first_candidate_start
for rr in review_rows:
 if rr['phase']=='expectation':
  rr['emitted_before_first_potential_candidate_request']=first_candidate is not None and rr['source_line']<first_candidate['source_line'] and first_candidate_start is not None and all(x['operation_interval']['ended_ns']<first_candidate_start for x in rr['emitted_expectations'])
save('CLIENT_CALL_INDEX.json',{'actual_tool_uses':len(calls),'typed_user_results':sum(len(x) for x in results.values()),'rows':rows,'pending':pending,'scope':'Full typed request/result pair and protected completed operation match; absent/preview responses remain unknown. No assistant narrative extracted.'})
save('SOURCE_ACQUISITION.json',{'source_read_calls':len(source_rows),'complete_typed_utf8_results':sum(x['typed_utf8_content_observed_complete'] for x in source_rows),'rows':source_rows,'first_potential_candidate':first_candidate,'coverage_limit':'Exact requested selectors/ranges or whole-source request identity only. Readable typed result is observed transport content, not mental receipt or conformance. Metadata pointers and source/proof bodies are distinguished; no automatic whole-parent coverage from slices/manifest/base64/preview.'})
coverage={}
for row in source_rows:
 ref=row['source'];parent={k:v for k,v in ref.items() if k!='selector'};key=canon(parent).decode();g=coverage.setdefault(key,{'parent':parent,'source_class':row['source_class'],'source_read_requests':0,'complete_typed_utf8_results':0,'observed_line_ranges':[],'observed_json_pointers':[],'whole_parent_utf8_result_observed':False,'refusal_codes':[]});g['source_read_requests']+=1
 g['refusal_codes'] += [x['code'] for x in row['protected_refusals']]
 if row['typed_utf8_content_observed_complete']:
  g['complete_typed_utf8_results']+=1;sel=ref['selector']
  if sel is None:g['whole_parent_utf8_result_observed']=True
  elif 'lines' in sel:g['observed_line_ranges'].append(sel['lines'])
  else:g['observed_json_pointers'].append(sel['json_pointer'])
for g in coverage.values():
 merged=[]
 for first,last in sorted(g['observed_line_ranges']):
  if merged and first<=merged[-1][1]+1:merged[-1][1]=max(merged[-1][1],last)
  else:merged.append([first,last])
 g['observed_line_ranges']=merged;g['observed_json_pointers']=sorted(set(g['observed_json_pointers']));g['refusal_codes']=dict(collections.Counter(g['refusal_codes']))
save('READABLE_SCOPE_INDEX.json',{'parents':list(coverage.values()),'source_classes':dict(collections.Counter(row['source_class'] for row in source_rows)),'limit':'Only complete typed UTF8 results matching protected outputs contribute. Line unions and JSON pointers are observed source selections, not semantic coverage/full-frame acceptance. No full parent inferred from partial ranges; no assistant prose/thinking findings.'})
save('REVIEW_PHASES.json',{'original_phase1_expectation':{'id':'sha256:4387cefa103592b5a76c96d288da403f9211bc3107843bc8dbfa63c501653f61','sha256':'4387cefa103592b5a76c96d288da403f9211bc3107843bc8dbfa63c501653f61'},'original_phase1_semantic_value':'indeterminate / performed_partial; unchanged','actual_review_prepare_calls':review_rows,'first_potential_candidate_request':first_candidate,'later_four_returned_semantic_values':None,'scope':'Only actual typed public review.prepare/protected expectation/acquisition facts. No final phase2 evaluation exists; supplemental expectation is not an assessment.'})
# Snapshot tail is typed whitelist only, with no full source contents in the tail summary.
tail=[]
for event in events[-16:]:
 if event['kind']=='tool_result':tail.append({'source_line':event['source_line'],'kind':'tool_result','tool_use_id':event['tool_use_id'],'is_error':event['is_error'],'allowed_content_bytes':len(canon(event['content'])),'allowed_content_sha256':hashlib.sha256(canon(event['content'])).hexdigest()})
 elif event['kind']=='tool_use':tail.append({'source_line':event['source_line'],'kind':'tool_use','id':event['id'],'name':event['name'],'input':event['input']})
 else:tail.append(event)
save('TYPED_TAIL.json',{'events':tail,'pending_observed_MCP_calls':pending,'native_final_result_records':len(finals),'partial_or_unparseable_JSONL_lines':parse_errors,'unknown':'No parent exit/EOF or pending-call absence establishes process-tree/external end.'})
save('NATIVE_INIT.json',{'observed_typed_initialization':inits,'observed_final_result_metadata':finals,'usage_billing':'Unknown; no final-result usage/cost record. No assistant usage fields read/summed and no guessed billing.','requested_effort':plan['settings'].get('requested_effort'),'requested_flags':{'restricted':'--restricted' in plan['argv'],'no_builtins':'--tools=' in plan['argv'],'strict_explicit_MCP':'--strict-mcp-config' in plan['argv'],'dontAsk':'dontAsk' in plan['argv'],'permission_prompts_none':'none' in plan['argv'],'no_session_persistence':'--no-session-persistence' in plan['argv']},'fixed_tool_policy_sha256':'d3dbebed35e3532d9d8a8e44df25f25a1b5bef115bffc6a7ede09f4a9b27f083','automatic_external_host_managed_memory_exposure':'unknown'})
# Protected actual capture/check preserves the empty final slot and lack of evaluations.
return_sha='50bec87c3984506ef82b1005647753cfc7513cc038ddf5437cfa8c97c3e24c91';captured=artifact(return_sha);check=artifact('59a8c56af235933a1cbe6f664aed0b51b20e4c8c127aa4a830d954c81e4cb908');observe=artifact('b17cf63cfe28404fd552a5c200a6eeac2822219a00e2d45d77977525668d99ee');captureop=artifact('19d794f91fbe7054d2ac46d483e7e9f489d0129fd2efe20af256a512e4647ffa');assert captured['payload']['original'] is None and captured['payload']['binding_checks']['format_valid'] is False;assert check['payload']['response_without_evidence']['result']['value']['consumable'] is False
helper_stdout=artifact('28602ed21ccb0c23c971395f9bc71a3926f65b747b462e19d58cf34feab8ba0b');helper_stderr=artifact('171543fae493477515127f7ade653251d422a2237688836f4b66edb879ef369c');stdout_bytes=base64.b64decode(helper_stdout['payload']['bytes_base64']);stderr_bytes=base64.b64decode(helper_stderr['payload']['bytes_base64']);assert stdout_bytes==b'' and len(stderr_bytes)==96
save('HELPER_STREAMS.json',{'stdout_artifact':'28602ed21ccb0c23c971395f9bc71a3926f65b747b462e19d58cf34feab8ba0b','stdout_bytes':len(stdout_bytes),'stdout_complete_capture':helper_stdout['payload']['complete'],'stderr_artifact':'171543fae493477515127f7ade653251d422a2237688836f4b66edb879ef369c','stderr_bytes':len(stderr_bytes),'stderr_utf8':stderr_bytes.decode('utf8'),'distinction':'These are registered helper public process streams. The native partial vendor stream3553404bytes is separate and opaque-excluded. Complete capture of an empty stdout slot is not a complete semantic result.'})
original_phase1=artifact('6a48c9e86a5a538371ebee8dabeace22aafbf010647296619d4763bd90b2c9a5');assert original_phase1['payload']['original']['evaluations'][0]['core_value']=='indeterminate'
save('PUBLIC_RETURN.json',{'Attempt':{'id':'sha256:502505b98e84e42e69bc40696fba780d7601d2bd59e7b9ce51e57e67fb49573b','sha256':'502505b98e84e42e69bc40696fba780d7601d2bd59e7b9ce51e57e67fb49573b'},'Context':'47592bbe919422bac56b2e112dc2dc6fb5c87afd355fa944c8cd794a3f5322d8','activation':'84a072e08fc992f668688326d857aed08534ad8bcc740f26669be630645017ff','Preflight':'9a8d4cac6e63cd7291f0e008e3a1c127e8b7257db147f99c61dfa420fd8e40e0','final_observe_evidence':'b17cf63cfe28404fd552a5c200a6eeac2822219a00e2d45d77977525668d99ee','CapturedReturn':{'id':'sha256:'+return_sha,'sha256':return_sha},'capture_operation':'19d794f91fbe7054d2ac46d483e7e9f489d0129fd2efe20af256a512e4647ffa','check_operation':'59a8c56af235933a1cbe6f664aed0b51b20e4c8c127aa4a830d954c81e4cb908','original':None,'format_valid':False,'binding_gaps':captured['payload']['binding_checks']['gaps'],'authenticated_registered_producer':captured['payload']['producer']['authenticated'],'transport':captured['payload']['transport'],'consumable':False,'four_later_semantic_values':None,'native_helper_output_available':False,'outer_helper_exit_code_Root_reported':1,'meaning':'Actual final stdout capture is empty; no final F_P closed return or acceptance verdict. Partial tool activity/expectations cannot be promoted into four later semantic results.'})
# Source custody/currentness only, no code/HOW semantic assessment.
guards=[]
for mf in [D/'SOURCE_MANIFEST.json',D/'assessment-001/SOURCE_MANIFEST.json']:
 m=load(mf);mismatches=[x['path'] for x in m['files'] if not (P/x['path']).is_file() or h(P/x['path'])!=x['sha256']];guards.append({'manifest':loc(mf),'members':len(m['files']),'mismatches':mismatches});assert not mismatches
subject=load(I/'CLOSED_SUBJECT.json');sourceguards=[{'path':rel,'expected':sha,'actual':h(P.parent/rel),'matches':h(P.parent/rel)==sha} for rel,sha in subject['required_sources'].items()];assert all(x['matches'] for x in sourceguards)
for dep in plan['dependencies']:assert h(dep['path'])==dep['sha256']
save('CURRENT_GUARDS.json',{'frozen_manifests':guards,'source_guards':sourceguards,'plan_dependencies_match':True,'actual_plan_sha256':h(A/'plan.json'),'prepared_plan_sha256':h(D/'assessment-001/actor-plan.json'),'same_fixed_native_tool_policy':h(D/'reviewer-tool-policy.json'),'same_claim':h(D/'review-claim.json'),'scope':'Exact byte/current setup provenance, no independent semantic acceptance.'})
save('EXTRACTION_AUDIT.json',{'opaque_excluded_partial_vendor_stream':loc(stream),'retained_vendor_file_is_complete_provider_stream':False,'whitelist':['system.init selected metadata','assistant content blocks type tool_use only','user content blocks type tool_result only','result selected final metadata only'],'excluded_assistant_content_type_counts':dict(excluded_types),'extraction':'Other assistant content values are never copied/inspected for semantic findings. Whole retained partial vendor file hashed, not exported. Typed events carry exact original line SHA/line route.','typed_events':len(events),'typed_tool_uses':len(calls),'typed_tool_results':sum(len(x) for x in results.values()),'final_result_records':len(finals),'partial_JSONL_line_metadata':parse_errors,'support_native_Git_calls_by_reconciliation':0,'usage_cost_assumption':'unknown, no estimates'})
summary={'native_elapsed_seconds':round((end-start)/1e9,6),'tool_uses':len(calls),'source_read_calls':len(source_rows),'complete_typed_utf8_source_results':sum(x['typed_utf8_content_observed_complete'] for x in source_rows),'review_prepare_calls':len(review_rows),'supplemental_expectation_refs':[x['artifact'] for r in review_rows for x in r['emitted_expectations']],'candidate_prepare_calls':sum(x['phase']=='candidate' for x in review_rows),'pending_typed_tool_results':len(pending),'protected_phase2_operations':len(all_ops)}
save('SUMMARY.json',summary)
supplemental_count=len(summary['supplemental_expectation_refs']);before=sum(r.get('emitted_before_first_potential_candidate_request') is True for r in review_rows if r['emitted_expectations']);candidate_rows=[r for r in review_rows if r['phase']=='candidate']
report=f'''# Factual phase2 public-path reconciliation

The actual registered native assessment timed out at its configured1200000ms limit. Native PID40963 returned143 after{(end-start)/1e9:.3f}s; the helper produced no final payload. Root captured the empty final stdout: original=null, format_valid=false, consumable=false. No semantic values were returned for design-conservation, implementation-conservation, guide-task-criteria or public-use-qualification. The original phase1 source-derived-expectations judgment remains indeterminate/performed_partial, unchanged. No acceptance verdict or retry/extension follows.

The typed trace contains{len(calls)} tool uses and{len(source_rows)} source.read requests;{sum(x['typed_utf8_content_observed_complete'] for x in source_rows)} requests have complete UTF8 content observed in whitelisted tool results and matching protected outputs. The other23 source requests were refused; they are not claimed readable. SOURCE_ACQUISITION.json records exact selectors, refusal codes and source classes; READABLE_SCOPE_INDEX.json merges only observed readable line ranges/JSON pointers and separates metadata from governing/candidate bodies. Complete typed output is route/content evidence, not mental attention or whole-parent coverage from slices. Protected successful acquisition and preview/saved paths are distinguished.

Actual emitted supplemental expectation artifacts:{supplemental_count}; expectation calls completed before the first observed potential candidate request:{before}, checked against typed order and protected acquisition times. REVIEW_PHASES.json binds each actual ref, source-input count, structural exposure facts and native receipt/preview status. Original phase1I is not rewritten or raised. Candidate prepare calls:{len(candidate_rows)}. Their protected population/acquisition results and native preview limits are separately recorded; bulk base64/preview is never counted as whole semantic proof reading. All these records describe performed tool activity, not a missing final assessment.

The final typed tail and{len(pending)} pending typed result(s) are preserved. Recorded native parent termination/return does not establish descendant/process-tree/external end; pending MCP continuations and later side effects remain unknown. Final-result usage/billing is unavailable and is not guessed. The opaque retained partial vendor stream is3553404bytes, hash-bound and excluded; no internal assistant text/thinking is used as reported findings.

All frozen118 preparation members,19 assessment preparation members, current18 source guards and plan dependencies match. The same fixed d3db Reviewer policy, registered actor and163-member claim remain selected. This is factual currentness/producer/source-history evidence, not semantic acceptance. The254-test/strict9/upstream9/demo10 mechanical qualification remains its bounded earlier result; phase2 public F_P qualification did not close. Efficiency, complete calculus, installation and RC remain unqualified.

Root's separately delegated native-platform source-first code/design reviews are a distinct workstream. They neither count as a successful public FDV trial nor erase this actual timeout/missing-return evidence. No source/policy/status/Git/support/native call or retry was performed by this reconciliation.
'''
save('REPORT.md',report)
checks={'configured_timeout_and_observed_partial_native_process':True,'no_final_vendor_result_metadata':not finals,'protected_empty_return_and_consumable_false':captured['payload']['original'] is None and not check['payload']['response_without_evidence']['result']['value']['consumable'],'original_phase1I_unchanged':True,'all_frozen_current_guards_match':all(not x['mismatches'] for x in guards) and all(x['matches'] for x in sourceguards),'same_fixed_policy_and_claim':h(D/'reviewer-tool-policy.json')=='d3dbebed35e3532d9d8a8e44df25f25a1b5bef115bffc6a7ede09f4a9b27f083' and h(D/'review-claim.json')=='5c894a92550f981cb564a8d36882255e7fcb0a295ec1f0eafeac54fc209774db','only_whitelisted_typed_events_exported':True,'no_reconciliation_calls_or_other_writes':True};assert all(checks.values());save('CHECKS.json',{'checks':checks,'actual_operations_or_native_Git_calls':0})
files=[loc(q) for q in sorted(R.iterdir()) if q.is_file() and q.name not in ['SOURCE_MANIFEST.json','CLOSED_RETURN.json']];save('SOURCE_MANIFEST.json',{'files':files,'readonly_actual_sources':[loc(A/n) for n in ['process.json','result.json','plan.json','invocation.json']],'opaque_exclusion':loc(stream)})
closed=save('CLOSED_RETURN.json',{'state':'Factual timeout/partial/missing-return reconciliation closed; no phase2 semantic acceptance','manifest_sha256':h(R/'SOURCE_MANIFEST.json'),'report_sha256':h(R/'REPORT.md'),'source_acquisition_sha256':h(R/'SOURCE_ACQUISITION.json'),'review_phases_sha256':h(R/'REVIEW_PHASES.json'),'typed_tail_sha256':h(R/'TYPED_TAIL.json'),'checks':len(checks),'actual_four_later_returned_semantic_values':None,'original_phase1':'indeterminate/performed_partial unchanged','native_elapsed_seconds':round((end-start)/1e9,6),'native_returncode':143,'helper_outer_exit_Root_reported':1,'captured_original':None,'consumable':False,'summary':summary,'actual_calls_by_reconciliation':0,'not_qualified':['public phase2 F_P assessment closure','efficiency','complete calculus','installation','RC/release'],'remaining_unknowns':['actual unreturned semantic work/findings','pending MCP/result continuation and descendant/process-tree/external end','final provider usage/billing and host/managed/memory exposure'],'no_internal_assistant_text_findings':True})
print(json.dumps({'closed_return':h(closed),'manifest':h(R/'SOURCE_MANIFEST.json'),'report':h(R/'REPORT.md'),'summary':summary,'first_candidate':first_candidate,'supplemental_before_candidate':before,'candidate_prepare_count':len(candidate_rows),'checks':len(checks)},indent=2))
