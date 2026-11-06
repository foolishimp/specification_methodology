from pathlib import Path
import json, hashlib, time
R=Path('/Users/jim/src/apps/specification_methodology')
D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
Q=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-004')
C=Q/'hosts/codex/cases/current-context'
OUT=Path(__file__).parent
seen={}
def sha(b): return hashlib.sha256(b).hexdigest()
def canon(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',', ':'),allow_nan=False).encode()
def raw(p):
 p=Path(p); b=p.read_bytes(); seen[str(p)]={'path':str(p),'sha256':sha(b),'bytes':len(b)}; return b
def read(p): return json.loads(raw(p))
def ref(v):
 p=Path(v['path']);p=p if p.is_absolute() else R/p
 b=raw(p);assert sha(b)==v['sha256'],p
 if 'bytes' in v:assert len(b)==v['bytes'],p
 return p
def obj(v):
 p=C/'evidence/objects'/(v['sha256']+'.json');z=read(p)
 assert sha(canon(z))==v['sha256'] and v['id']=='sha256:'+v['sha256'];return z
start=time.time_ns()
ret=read(D/'tools-skills/installed-qualification-022/FORMAL_CONTEXT_RETURN.json')
for sec in ('full','context'):
 for z in ret[sec].values():
  if isinstance(z,dict) and 'path' in z and 'sha256' in z:ref(z)
full=read(ref(ret['full']['result']));inspection=read(ref(ret['full']['inspection']));src=read(D/'tools-skills/current-formal-021/cold/result.json')
assert full['status']=='verified' and inspection['status']=='consistent'
assert full['checked_claims']==src['checked_claims']==inspection['required_claims'] and len(full['checked_claims'])==5
assert all(full[k]==inspection[k] for k in ('model','selections','inputs','runtime_identity','context_binding'))
assert all(full[k]==src[k] for k in ('model','selections','checked_claims'))
assert inspection['evidence']['result_sha256']==ret['full']['result']['sha256']
pins=full['runtime_identity']['pins'];spins=src['runtime_identity']['pins']
delta={k:{'source':spins.get(k),'installed':pins.get(k)} for k in pins.keys()|spins.keys() if pins.get(k)!=spins.get(k)}
assert set(delta)=={'profiles/proof-support-v1.json','.cache/formal-origin-v1/selection.json'}
for k in ('scripts/formal_gate.py','scripts/formal_support.py','scripts/runtime_process.py','.cache/formal-origin-v1/selection.json'):
 assert sha(raw(Q/'runtime/a_c/build_tenants/lean'/k))==pins[k]
manifest=read(ref(ret['full']['manifest']));assert sha(raw(Q/'formal/current-full/manifest.json'))==full['evidence']['manifest_sha256']
memberdiff=[k for k in src['evidence']['members'].keys()|full['evidence']['members'].keys() if src['evidence']['members'].get(k)!=full['evidence']['members'].get(k)]
assert memberdiff==['request.json']
for name in ('request.json','replay-request.json','GateViews.lean','GateViews.log','GateRun.lean','dynamic-kernel-replay.log','view-comparison.json'):
 assert sha(raw(Q/'formal/current-full'/name))==full['evidence']['members'][name]
assert set(x for xs in full['observations']['theorem_audit'].values() for x in xs)<= {'propext','Quot.sound','Classical.choice'}
fe=read(ref(ret['full']['execution']));ie=read(ref(ret['full']['inspection_execution']))
for e in (fe,ie):
 assert e['execution']['returncode']==0
 for k in ('stdout','stderr'):ref(e['execution'][k])
 assert e['execution']['argv'][0]==str(Q/'dependencies/graphify/venv/bin/python')
 assert e['execution']['argv'][4]==str(Q/'runtime/a_c/build_tenants/lean/scripts/formal_gate.py')
assert fe['execution']['elapsed_seconds']==366.497637
supervision=read(D/'tools-skills/installed-qualification-022/executions/installed-full-current-verify/SUPERVISION.json');assert not supervision['outer_timeout_occurred'] and supervision['outer_timeout_seconds']==7200
pre=read(ref(ret['context']['preflight']));controls=read(ref(ret['context']['controls']));delivery=read(ref(ret['context']['delivery']))
context=obj(pre['context'])['payload'];pref=obj(pre['preflight'])['payload'];formal=obj(pre['formal_evidence'])['payload']
cr=read(ref(pre['formal_result']));views=read(ref(pre['views']));request=read(ref(pre['request']))
assert pref['decision']==pref['contract_state']=='admitted'
assert pref['context']==pre['context'] and pref['formal_evidence']==pre['formal_evidence']
assert cr['status']=='verified' and cr['context_binding']==request['context_binding']==formal['binding']
assert cr['runtime_identity']==full['runtime_identity'] and cr['checked_claims']==full['checked_claims']
assert context['projections'][0]['views']==views
assert cr['selections']==context['projections'][0]['selections']
assert len(views)==1 and len(views[0]['included'])==21 and controls['omitted_required_record'] in views[0]['included']
assert controls['omitted_required_record'] in {r['id'] for r in views[0]['populations']['residuals']}
received=raw(ref(delivery['received_stdin']));received_views=raw(ref(delivery['received_views']))
assert received==context['rendered_utf8'].encode() and sha(received)==context['rendered_sha256']==cr['context_binding']['rendered_sha256']
assert received_views==canon([p['views'] for p in context['projections']])
assert raw(C/'workspace/outputs/count')==b'1'
assert delivery['count']==1 and delivery['observation']['process_end']['returncode']==0
assert delivery['observation']['effect']['value']=='completion_unknown' and not delivery['observation']['effect']['end_established']
actual_calls=[]
for label,code,status in [('004-dispatch.start',2,'refused'),('005-dispatch.start',2,'refused'),('006-dispatch.start',0,'ok')]:
 e=read(C/'operator-controls-dispatch'/label/'execution.json');z=read(ref(e['stdout']));ref(e['request']);ref(e['producer']);ref(e['policy']);ref(e['configuration']);ref(e['stderr'])
 assert e['returncode']==code and not e['timed_out'] and z['status']==status
 assert e['argv'][0]==str(Q/'dependencies/graphify/venv/bin/python') and e['argv'][2]==str(Q/'runtime/a_c/build_tenants/graphify/code/ac_support.py')
 actual_calls.append({'label':label,'returncode':code,'status':status,'timeout_seconds':e['timeout_seconds'],'started_ns':e['started_ns'],'ended_ns':e['ended_ns']})
 if label.startswith('004'):assert z==controls['omission_response']
 if label.startswith('005'):assert z==controls['stale_response']
 if label.startswith('006'):assert z['result']['artifact']==delivery['attempt'] and e['timeout_seconds']==7500
assert actual_calls[0]['ended_ns']<actual_calls[1]['started_ns']<actual_calls[1]['ended_ns']<actual_calls[2]['started_ns']
omitted=read(C/'operator-controls-dispatch/omitted-context.adversarial-envelope.json')['payload']
assert len(omitted['projections'][0]['views'][0]['included'])==20 and controls['omitted_required_record'] not in omitted['projections'][0]['views'][0]['included']
assert omitted['rendered_sha256']!=context['rendered_sha256']
assert raw(ref(controls['stale_copy']))==raw(ref(controls['original_result']))+b'\n'
assert controls['recipient_effects_after_controls']==0
uses=[delivery['observation']['anchor']['formal_use']]+[e['data']['formal_use'] for e in delivery['observation']['events'] if e['kind']=='formal_gate_verified']
rechecks=[]
for u in uses:
 z=obj(u)['payload'];assert z['context']==pre['context'] and z['formal_evidence']==pre['formal_evidence']
 for replay in z['replays']:
  rr=read(Path(replay['bundle'])/'result.json');o=rr['observations'];assert rr['status']=='verified' and rr['context_binding']==cr['context_binding'] and rr['runtime_identity']==cr['runtime_identity']
  assert [o[k] for k in ('current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations')]==[0,0,0]
  assert o['original_establishment']['result_sha256']==pre['formal_result']['sha256'] and o['reuse']=='local-origin'
  assert sha(raw(Path(replay['bundle'])/'origin-result.json'))==pre['formal_result']['sha256']
  rechecks.append({'stage':z['stage'],'runtime':rr['runtime_identity']['sha256'],'invocations':[0,0,0],'origin_result_sha256':pre['formal_result']['sha256']})
assert len(rechecks)==2
completion=read(D/'cohort-binding-004/installed-owner-checks/COMPLETION.json');assert completion['native_commit']=='d1f13c53ab733a73993615498f66251041a74073'
owner=[]
for label,z in completion['records'].items():
 e=read(ref(z['execution']));res=read(ref(z['result']));assert e['execution']['returncode']==0 and res['status']=='checked' and res['model']=={'id':full['model']['id'],'profile':'a_c.graphify.model/1','sha256':full['model']['sha256']}
 for k in ('stdout','stderr'):ref(e['execution'][k])
 assert str(Q/'store/releases/v3.0.5') in e['execution']['argv'][-1]
 owner.append({'label':label,'argv':e['execution']['argv'],'result':z['result']})
for p,z in list(seen.items()):assert sha(Path(p).read_bytes())==z['sha256'],('changed-during-review',p)
report={'schema':'stdo305.independent-closed-local004-review-check/1','assessor':'/root/stdo305_integration_review','started_ns':start,'ended_ns':time.time_ns(),'standing':'Bounded closed proof/Context and owner-record review only; no native-host or final aggregate verdict. No compiler, support-tree scan, actor or browser execution.','full_result':ret['full']['result'],'runtime_delta':delta,'full_vs_source_evidence_difference':memberdiff,'actual_calls':actual_calls,'view':{'records':21,'required_residual':controls['omitted_required_record'],'rendered_sha256':sha(received),'delivered_bytes':len(received),'exact_ordered_projection':True,'recipient_counter':1,'effect':delivery['observation']['effect']['value']},'rechecks':rechecks,'owner_checks':owner,'files_before_after':list(seen.values()),'findings':[]}
p=OUT/'CLOSED_LOCAL004_CHECK.json';p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({'path':str(p),'sha256':sha(p.read_bytes()),'files_before_after':len(seen),'findings':[]},indent=2))
