"""One dependency-bound installed owner inspection, selected180s limit."""
from pathlib import Path
import json,os,platform,resource,subprocess,time
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);py=json.loads((b/'dependencies/graphify/RUNTIME.json').read_bytes())['python'];lean=b/'runtime/a_c/build_tenants/lean';bundle=b/'formal/current-full';request=p/'formal/request.json';checker=b/'formal/checker.json'
value=json.loads((bundle/'result.json').read_bytes());req=json.loads(request.read_bytes());selection=json.loads(checker.read_bytes());prior=p/'executions/installed-full-current-verify';execution=json.loads((prior/'execution.json').read_bytes());supervision=json.loads((prior/'SUPERVISION.json').read_bytes())
assert execution['execution']['returncode']==0 and value['status']=='verified' and not supervision['outer_timeout_occurred']
assert value['runtime_identity']==selection['runtime_identity'] and value['selections']==req['selections'] and value['context_binding']==req['context_binding']
assert value['inputs']['input']['raw_sha256']==req['input']['raw_sha256'] and value['inputs']['supplied_views']['raw_sha256']==req['supplied_views']['raw_sha256']
assert value['evidence']['manifest_sha256']==o.sha(bundle/'manifest.json')
try:os.killpg(supervision['process_id'],0)
except ProcessLookupError:group_absent=True
else:group_absent=False
assert group_absent,'Verifier process group remains; do not inspect/promote'
producer=lean/'scripts/formal_gate.py';assert o.sha(producer)=='4fb6daab9d1b9a14be797d1595f201e3dab1f1e5800d96babb130259b1234b2c'
argv=[py,'-I','-S','-B',str(producer),'inspect-evidence','--bundle',str(bundle),'--request',str(request)]
record=p/'executions/installed-full-owner-inspection';record.mkdir(exist_ok=False);inputs=[request,Path(req['input']['path']),Path(req['supplied_views']['path']),bundle/'result.json',bundle/'manifest.json',prior/'execution.json',prior/'SUPERVISION.json',checker]
python={'invocation':py,'executable_realpath':str(Path(py).resolve(strict=True)),'sha256':o.sha(Path(py).resolve(strict=True)),'version':platform.python_version()}
(record/'invocation.json').write_bytes(o.encoded({'schema':'stdo.execution-invocation/1','argv':argv,'cwd':str(b),'producer':o.ref(producer,canonical='a_c/build_tenants/lean/scripts/formal_gate.py'),'inputs':[{'actual_path':str(x),'retained':o.ref(x)} for x in inputs],'runtime_identity':value['runtime_identity'],'timeout_seconds':180,'verifier_private_group_absent':True,'recorder':o.ref(Path(__file__)),'cleanup_limit':'Successful compiler stages enforce owned group absence; no separate numeric identity claim for unobserved/reparented descendants.'}))
stdout=record/'stdout.txt';stderr=record/'stderr.txt';before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.time_ns();timed=False
print(json.dumps({'phase':'installed-full-owner-inspection','status':'started','argv':argv}),flush=True)
with stdout.open('xb') as out,stderr.open('xb') as err:
 try:process=subprocess.run(argv,cwd=b,env={'PATH':os.defpath,'HOME':os.environ.get('HOME','')},stdout=out,stderr=err,timeout=180);code=process.returncode
 except subprocess.TimeoutExpired:timed=True;code=None
end=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN)
try:result=json.loads(stdout.read_bytes())
except (ValueError,UnicodeError):result=None
outputs=[o.ref(stdout),o.ref(stderr)]
if result is not None:(record/'result.json').write_bytes(o.encoded(result));outputs.append(o.ref(record/'result.json'))
receipt={'schema':'stdo.execution-observation/1','producer':o.ref(producer,canonical='a_c/build_tenants/lean/scripts/formal_gate.py'),'result':o.ref(record/'result.json') if result is not None else o.ref(stdout),'observed_input_paths':[{'actual_path':str(x),'retained':o.ref(x)} for x in inputs],'execution':{'argv':argv,'cwd':str(b),'returncode':code,'started_ns':start,'ended_ns':end,'elapsed_seconds':(end-start)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss,'environment':{'python':python},'inputs':[o.ref(x) for x in inputs],'outputs':outputs,'stdout':o.ref(stdout),'stderr':o.ref(stderr)}}
(record/'execution.json').write_bytes(o.encoded(receipt));(record/'OUTCOME.json').write_bytes(o.encoded({'timed_out':timed,'returncode':code,'standing':'Actual read-only owner inspection; no new kernel verdict.'}));print(json.dumps({'phase':'installed-full-owner-inspection','returncode':code,'status':result.get('status') if isinstance(result,dict) else 'unreadable','seconds':(end-start)/1e9}),flush=True)
assert code==0 and not timed and result['status']=='consistent'
