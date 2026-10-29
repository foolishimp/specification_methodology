#!/usr/bin/env python3
"""Read-only trace of frozen actual task evidence; no candidate imports/execution."""
from pathlib import Path
import base64, hashlib, json, re, shlex
from datetime import datetime
W=Path(__file__).resolve().parents[2]; R=Path(__file__).resolve().parent
A=W/'real-use/runtime-preparation-003/execution-001'; B=W/'real-use/runtime-preparation-003/execution-002'
P=W/'real-use/runtime-preparation-001/execution'
def load(p): return json.loads(p.read_bytes())
def sha(b): return hashlib.sha256(b).hexdigest()
def value(p):
 d=load(p); assert d['status']=='ok'; return d['result']['value']
ready=load(A/'READY-DISPATCH-REQUESTS.json'); sel=load(B/'EXECUTION-SELECTION.json'); mapping=load(B/'operational/ARM-MAPPING.json')['labels']; freeze=load(B/'operational/WORKSPACE-FREEZE.json'); quality=load(W/'review/matched-quality-001/QUALITY.json')
assert mapping=={'A':'ungated','B':'gated'} and sel['no_retry'] and sel['operation_allowance']=={'gated':1,'ungated':1}
assert sha((W/'review/matched-quality-001/CLOSED.json').read_bytes())=='fa50735cf15fd1aa7f01a49b90b6b6ab905ee171b506b112ca7a3e262ce487c1'
out={'schema':'a_c.T013.independent-operational-trace/1','arms':{},'mapping_after_quality_closure':mapping,'product_acceptance':False,'new_actor_calls':0,'candidate_changes':0}
contexts={}
for label,arm in mapping.items():
 rr=ready['arms'][arm]; s=sel['arms'][arm]; runtime=A/'runtime'/arm
 assert s['context']==rr['context']['artifact'] and s['preflight_receipt']==rr['preflight_receipt']
 assert sha((B/'requests'/arm/'dispatch.request.json').read_bytes())==s['dispatch_request_sha256']==rr['dispatch_request_sha256']
 policy=load(runtime/'policy.json'); assert sha((runtime/'policy.json').read_bytes())==s['policy_sha256']
 ctx=load(Path(rr['context']['path']))['payload']; contexts[arm]=ctx
 rendered=ctx['rendered_utf8'].encode(); assert sha(rendered)==ctx['rendered_sha256']==s['rendered_sha256']
 for row in ctx['sources']:
  raw=base64.b64decode(row['content_base64'],validate=True); assert sha(raw)==row['selected_sha256'] and len(raw)==row['size_bytes']
 pf=value(A/'observations'/arm/'preflight/response.json')
 assert pf['decision']==pf['contract_state']=='admitted' and pf['gaps']==[] and pf['context']==s['context']
 assert (pf['requester'],pf['target'],pf['executor_id'])==('executive','worker','actor')
 assert all(e['core_value']=='satisfied' for e in pf['evaluations'])
 assert pf['authority']==policy['product']['authority_binding']
 assert policy['grants']['task']['principals']==['executive'] and policy['grants']['task']['targets']==['worker']
 owner=policy['product']['authority_binding']['owner_record']
 ownerbytes=(W.parents[2]/owner['path']).read_bytes(); assert load(A/'CURRENTNESS.json')['ticket_sha256']==owner['sha256']
 # Later status bookkeeping may change the whole ticket; its selected authority text remains exact.
 lo,hi=owner['selector']['lines']; selected=b''.join(ownerbytes.splitlines(keepends=True)[lo-1:hi]); ownerrows=[r for r in ctx['sources'] if r['source']==owner]; assert len(ownerrows)==1 and sha(selected)==ownerrows[0]['selected_sha256']
 obs=[value(B/'observations'/arm/f'observe-{n:03d}/response.json') for n in (1,2)]
 anchor=obs[0]['anchor']; assert anchor==obs[1]['anchor'] and anchor['retry_of'] is None and anchor['reconciliation'] is None
 assert anchor['context']==s['context'] and anchor['preflight']==s['preflight_receipt']
 events=[e for o in obs for e in o['events']]; assert [e['cursor'] for e in events]==list(range(1,len(events)+1))
 assert all(e['attempt']==obs[0]['attempt'] for e in events) and all(o['history_gaps']==[] for o in obs)
 kinds=[e['kind'] for e in events]; assert kinds.count('actor_started')==kinds.count('actor_launch_intent')==1
 delivery=next(e['data'] for e in events if e['kind']=='context_delivery'); assert delivery['context']==s['context'] and delivery['complete'] and delivery['bytes']==len(rendered) and delivery['rendered_sha256']==sha(rendered)
 effect=next(e['data'] for e in events if e['kind']=='effect_observation'); assert effect['observations']=={'changes':[],'gaps':[],'observations':[]} and effect['effect']['value']=='completion_unknown'
 if arm=='gated':
  assert anchor['formal_use']['sha256']=='57c249f7ae246c67ab7cb3a33540ac44c8cd5b9d210c8369ca0d01badbe102fe'
  e=next(e for e in events if e['kind']=='formal_gate_verified'); assert e['data']['formal_use']['sha256']=='80d3e213fe2a1b8133c0e1fc3dab726fe2c99399c435846f53c42019d945f374'
  assert e['data']['context']==s['context'] and e['data']['rendered_sha256']==sha(rendered) and kinds.index('formal_gate_verified')<kinds.index('actor_launch_intent')
 else: assert 'formal_gate_verified' not in kinds and 'formal_use' not in anchor
 t=P/'actor-transports'/rr['actor_id']; inv=load(t/'invocation.json'); proc=load(t/'process.json'); dec=load(t/'decoded.json')
 assert (t/'context.bin').read_bytes()==rendered and inv['input_complete'] and inv['input_sha256']==sha(rendered) and inv['input_bytes']==len(rendered)
 assert inv['plan_sha256']==sha((runtime/'actor-plan.json').read_bytes()) and inv['cwd']==rr['workspace'] and inv['protected_environment_pass_through']=={}
 assert proc['returncode']==0 and proc['input_forwarded_bytes']==len(rendered) and proc['stdout_eof'] and proc['stderr_eof'] and proc['termination_requests']==[] and proc['failure'] is None
 native=[json.loads(line) for line in (t/'vendor.stdout').read_text().splitlines()]
 assert len(native)==16 and native[-1]['type']=='turn.completed' and len([x for x in native if x['type']=='turn.started'])==1
 commands=[x['item'] for x in native if x['type']=='item.completed' and x['item']['type']=='command_execution']; assert len(commands)==5 and all(x['exit_code']==0 for x in commands)
 final=native[dec['final_source']['event_index']]['item']['text']; payload=(t/'final.payload').read_bytes(); assert json.loads(final)==json.loads(payload) and sha(payload)==dec['payload_sha256']
 chunks=b''.join(base64.b64decode(e['data']['bytes_base64']) for e in events if e['kind']=='output_chunk' and e['data']['stream']=='stdout'); assert chunks==payload
 capture=value(B/'observations'/arm/'return-capture/response.json'); assert capture['producer']['authenticated'] and capture['producer']['principal_id']=='worker' and capture['binding_checks']=={'format_valid':True,'gaps':[]}
 assert capture['original']==json.loads(payload) and capture['attempt']==obs[0]['attempt'] and capture['transport']['complete'] and capture['transport']['raw_sha256']==sha(payload)
 assert capture['original']['actor']['id']==rr['actor_id']
 workspace=Path(rr['workspace']); neutral=B/'grading'/label
 for rel,pin in freeze['arms'][arm].items():
  assert sha((workspace/rel).read_bytes())==pin['sha256'] and (workspace/rel).stat().st_size==pin['bytes']
  # Neutral grading trees are located by their frozen input pin paths; quality closure already verified them.
 for rel,pin in quality['subjects'][label].items(): assert freeze['arms'][arm][rel]==pin
 wr=capture['original']['work_result']; assert sha((workspace/wr['candidate']['path']).read_bytes())==wr['candidate']['sha256']
 assert all(sha((workspace/e['path']).read_bytes())==e['sha256'] for e in wr['evidence'])
 # Inspect retained commands, without executing them. All emitted file bodies must equal reviewed artifacts.
 shell=[]; emitted=[]
 for item in commands:
  parsed=shlex.split(item['command']); assert parsed[:2]==['/bin/zsh','-lc'] and len(parsed)==3
  body=parsed[2]
  for match in re.finditer(r"cat > ([\w./-]+) <<'(\w+)'\n(.*?)^\2\n?",body,re.S|re.M):
   rel,_,content=match.groups(); assert (workspace/rel).read_bytes()==content.encode(); emitted.append(rel)
  shell.append({'id':item['id'],'command_sha256':sha(item['command'].encode()),'exit_code':item['exit_code']})
 assert set(emitted)=={'gate_report.py','README.md','test_gate_report.py'}
 usage=native[-1]['usage']; assert usage==load(B/'operational/COST.json')['arms'][arm]['provider_reported_terminal_usage']
 out['arms'][arm]={'neutral_label':label,'context_artifact':s['context'],'delivered_sha256':sha(rendered),'delivered_bytes':len(rendered),'source_records':len(ctx['sources']),'preflight_evaluations':len(pf['evaluations']),'attempt':obs[0]['attempt'],'events':kinds,'return_artifact':load(B/'observations'/arm/'return-capture/response.json')['result']['artifact'],'source_currentness_gaps':[],'native_invocations':1,'native_pid':proc['pid'],'native_seconds':(proc['ended_ns']-proc['started_ns'])/1e9,'native_commands':shell,'emitted_reviewed_files':emitted,'workspace_files_exact':len(freeze['arms'][arm]),'reported_terminal_usage':usage,'uncached_input_derived':usage['input_tokens']-usage['cached_input_tokens'],'raw_transport_limits':proc['unknowns']}
# Common source values and their relative order are identical; absolute ordering differs.
def commonrows(ctx): return [r for r in ctx['sources'] if not any(r['source']['path'].startswith(a+'/') for a in ('ungated','gated'))]
assert commonrows(contexts['gated'])==commonrows(contexts['ungated'])
assert contexts['gated']['projections'][0]['views']==contexts['ungated']['projections'][0]['views']
out.update({'common_acquired_records':len(commonrows(contexts['gated'])),'complete_prompt_equal':False,'absolute_source_positions_differ':True,'current_inputs_and_output_manifests_exact':True,'scope_assessment':'Manual inspection of all five native commands per arm and their complete heredoc/script bodies found only the granted local task reads, writes, tests and manifest hashing. No observed additional agent/model, network, Git, install, other-arm, evaluator or private-origin access. This is a retained-visible-command/cooperative-host assessment, not OS/provider isolation proof.','pending_metadata':'Gated Context pending describes assembly by existing formal-gate design; actual external proof is retained beside Context. Worker did not receive the verification receipt and conservatively reported it pending; no new engine defect or semantic acceptance follows.'})
(R/'OPERATION-CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','arms':list(out['arms']),'common_records':out['common_acquired_records'],'native_invocations':2,'new_executions':0}))
