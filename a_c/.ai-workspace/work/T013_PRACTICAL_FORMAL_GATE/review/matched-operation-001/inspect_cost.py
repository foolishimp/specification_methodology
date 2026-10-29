#!/usr/bin/env python3
"""Reconcile retained cost observations only. No executable candidate imports."""
from pathlib import Path
import json, hashlib, math
from datetime import datetime
W=Path(__file__).resolve().parents[2];R=Path(__file__).resolve().parent
A=W/'real-use/runtime-preparation-003/execution-001';B=W/'real-use/runtime-preparation-003/execution-002';F=W/'real-use/runtime-preparation-002/execution-001';P=W/'real-use/runtime-preparation-001/execution'
def load(p):return json.loads(p.read_bytes())
def dt(v):return datetime.fromisoformat(v)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
ca=load(A/'COST.json');cb=load(B/'operational/COST.json');cf=load(F/'COST.json');o=load(R/'OPERATION-CHECKS.json')
phases={}
for name,root,expected in [('failed_phase_a',F,cf['public_operation_wall_seconds_sum']),('successful_phase_a',A,ca['public_operation_wall_sum_seconds']),('phase_b',B,cb['public_operation_wall_sum_seconds'])]:
 ps=[load(p) for p in sorted((root/'observations').rglob('PROCESS.json'))];total=sum(p['whole_invocation_wall_seconds'] for p in ps)
 assert math.isclose(total,expected,abs_tol=1e-9);phases[name]={'public_operations':len(ps),'summed_public_process_seconds':total,'first_start':min(p['started_utc'] for p in ps),'last_finish':max(p['finished_utc'] for p in ps)}
 if name=='phase_b':
  for row in cb['public_operations']:
   p=load(root/row['path']);assert row['whole_invocation_wall_seconds']==p['whole_invocation_wall_seconds'] and row['started_utc']==p['started_utc'] and row['finished_utc']==p['finished_utc']
  phases[name]['first_dispatch_to_last_capture_wall_seconds']=(dt(phases[name]['last_finish'])-dt(phases[name]['first_start'])).total_seconds()
assert math.isclose(sum(x['summed_public_process_seconds'] for x in phases.values()),cb['retained_phase_a_plus_b_public_wall_sum_seconds'],abs_tol=1e-9)
rows={}
for arm in ('ungated','gated'):
 t=P/'actor-transports'/f't013-report-{arm}-worker-001';native=load(t/'process.json');usage=json.loads((t/'vendor.stdout').read_text().splitlines()[-1])['usage'];row=cb['arms'][arm]
 assert usage==row['provider_reported_terminal_usage']
 native_seconds=(native['ended_ns']-native['started_ns'])/1e9;assert native_seconds==row['native_call_seconds']
 events=sum([load(B/'observations'/arm/f'observe-{i:03d}/response.json')['result']['value']['events'] for i in (1,2)],[])
 output=next(e['data'] for e in events if e['kind']=='output_finalized');interval=load(P/'evidence/objects'/(output['stdout']['sha256']+'.json'))['payload']['interval'];start=interval['started_ns'];end=interval['ended_ns'];assert end==output['process_end']['ended_ns']
 helper=(end-start)/1e9;assert helper==row['registered_helper_interval_seconds']
 d=load(B/'observations'/arm/'dispatch/PROCESS.json'); c=load(B/'observations'/arm/'return-capture/PROCESS.json')
 capture=(dt(c['finished_utc'])-dt(d['started_utc'])).total_seconds();assert abs(capture-row['dispatch_request_to_authenticated_capture_end_seconds'])<1e-6
 observed_end=end/1e9-dt(d['started_utc']).timestamp();assert abs(observed_end-row['dispatch_request_to_observed_helper_end_seconds'])<1e-6
 rows[arm]={'usage':usage,'derived_uncached_input_tokens':usage['input_tokens']-usage['cached_input_tokens'],'native_seconds':native_seconds,'registered_helper_seconds':helper,'dispatch_cli_seconds':d['whole_invocation_wall_seconds'],'dispatch_to_helper_end_seconds':observed_end,'dispatch_to_capture_end_seconds':capture,'summed_public_operation_seconds':row['public_operation_wall_sum_seconds']}
pre=W/'checkpoint/final-delivery-001/preimages/.ai-workspace/tickets/active/T-013-practical-formal-gate.md';assert sha(pre)=='c5c8ed56ebfef3f51406be4b63d7d1fd3976de294ce0a64c801ea3f4da44fefc';assert hashlib.sha256(b''.join(pre.read_bytes().splitlines(keepends=True)[148:225])).hexdigest()=='4846a79958e343f5e7e302044ae169eaa50cb44a992a4c290f58f660d420fb6b'
result={'schema':'a_c.T013.independent-cost-reconciliation/1','phases':phases,'arms':rows,'successful_cold':{'whole_preflight_seconds':ca['gate_public_preflight_wall_seconds'],'checking_only_seconds':ca['gate_checking_only_seconds'],'aggregate_child_high_water_bytes':ca['gate_child_maxrss_native_bytes_darwin'],'source_batch_seconds':ca['source_batch_wall_seconds'],'comparison_seconds':ca['context_comparison_wall_seconds'],'finalizer_seconds':ca['finalizer_wall_seconds']},'reuse_checking_seconds':cb['current_reuse_checking_seconds'],'failed_phase_a':{'whole_preflight_seconds':cf['gate_public_preflight_wall_seconds'],'checking_only_seconds':cf['gate_checking_only_seconds'],'standing':'incomplete; no actor; retained cost, not invalid model'},'quality_check_process_seconds':load(W/'review/matched-quality-001/QUALITY.json')['review_check_process_seconds'],'owner_preimage_sha256':sha(pre),'arithmetic_total_public_process_seconds':sum(x['summed_public_process_seconds'] for x in phases.values()),'all_invocation_intervals_additive':False,'money':None,'actual_worker_models':None,'coordination_tokens':None,'unmeasured':['Total preparation/diagnostic/design/review/package effort','Operator and Reviewer model usage/cost','Provider hidden retries or unreported usage','Whole engagement wall time','Worker peak RSS/CPU/energy','Future output repair cost'],'interpretation':['Cached input is a subset of input, not an extra chargeable token count. Reasoning output is preserved separately without a billing assumption.','Native/helper/reuse/dispatch/capture intervals overlap; request-to-capture includes operator polling and analysis.','Summed public process durations are accounting of observations, not end-to-end wall time; source batches may overlap.','Cold and failed Phase A, operator corrections and assessment are retained; they are not zero because recurring reuse is cheaper.','-M4096 is a Lean allocation option, not a measured physical 4 GiB process cap. Darwin child RSS is aggregate high-water, not a per-stage or simultaneous total.','Only two ordered actual outputs were observed. Different absolute prompt layout, provider-cache state, unknown model identity and no random arm order prevent causal quality/cost inference.']}
(R/'COST-CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','phases':phases,'whole_economic_cost_known':False}))
