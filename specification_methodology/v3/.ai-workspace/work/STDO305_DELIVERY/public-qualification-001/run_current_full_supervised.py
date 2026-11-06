"""One actual installed public full proof with explicit7200s outer supervision."""
from pathlib import Path
import importlib.util,json,os,platform,resource,signal,subprocess,time
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);ac=b/'runtime/a_c';py=json.loads((b/'dependencies/graphify/RUNTIME.json').read_bytes())['python'];request=p/'formal/request.json';q=json.loads(request.read_bytes());checker=json.loads((b/'formal/checker.json').read_bytes());bundle=b/'formal/current-full'
assert (p/'HOST_SELECTIONS.json').is_file() and json.loads((p/'executions/actual-upstream-roundtrip/result.json').read_bytes())['status']=='verified'
assert checker['timeout_seconds']==7200 and checker['runtime_identity']['pins']['scripts/formal_gate.py']=='4fb6daab9d1b9a14be797d1595f201e3dab1f1e5800d96babb130259b1234b2c'
assert q['selections']==json.loads((o.REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/representation/repair-002/formal-selections.json').read_bytes())
assert q['input']['raw_sha256']=='0efcfe8ce9fb8c8abad1db75ee53982b50460d3048ff7060eb3c94ef5b472a2e'
assert o.sha(Path(q['input']['path']))==q['input']['raw_sha256'] and o.sha(Path(q['supplied_views']['path']))==q['supplied_views']['raw_sha256']
helper=ac/'build_tenants/graphify/code/ac_formal_gate.py';assert o.sha(helper)=='d37de63f2b809e7a02d88d560b29b4900e8cda6217cfbc32e5796f40065659b8'
spec=importlib.util.spec_from_file_location('current_installed_supervisor',helper);sup=importlib.util.module_from_spec(spec);spec.loader.exec_module(sup);sup.validate_config(checker);sup._pins(checker)
assert not bundle.exists();record=p/'executions/installed-full-current-verify';record.mkdir(exist_ok=False)
producer=ac/'build_tenants/lean/scripts/formal_gate.py';argv=[py,'-I','-S','-B',str(producer),'verify','--request',str(request),'--output',str(bundle)]
inputs=[request,Path(q['input']['path']),Path(q['supplied_views']['path'])];physical=Path(py).resolve();python={'invocation':py,'executable_realpath':str(physical),'sha256':o.sha(physical),'version':platform.python_version()}
(record/'invocation.json').write_bytes(o.encoded({'schema':'stdo.execution-invocation/1','argv':argv,'cwd':str(b),'producer':o.ref(producer,canonical='a_c/build_tenants/lean/scripts/formal_gate.py'),'python':python,'inputs':[{'actual_path':str(x),'retained':o.ref(x)} for x in inputs],'outer_timeout_seconds':7200,'per_stage_timeout_seconds':1800,'recorder':o.ref(Path(__file__)),'supervisor_helper':o.ref(helper,canonical='a_c/build_tenants/graphify/code/ac_formal_gate.py')}))
stdout=record/'stdout.txt';stderr=record/'stderr.txt';before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.time_ns();timed_out=False;cleanup=[]
print(json.dumps({'phase':'installed-full-current-verify','status':'started','argv':argv}),flush=True)
with stdout.open('xb') as out,stderr.open('xb') as err:
 process=subprocess.Popen(argv,cwd=b,env={'PATH':os.defpath,'HOME':os.environ.get('HOME','')},stdout=out,stderr=err,start_new_session=True,close_fds=True)
 (record/'PROCESS.json').write_bytes(o.encoded({'pid':process.pid,'private_process_group':process.pid,'started_ns':start}))
 try:code=process.wait(timeout=7200)
 except subprocess.TimeoutExpired:
  timed_out=True;groups,notes=sup._owned_groups(process.pid);cleanup.extend(notes)
  for sig,grace in ((signal.SIGTERM,10),(signal.SIGKILL,2)):
   if sig==signal.SIGKILL:found,notes=sup._owned_groups(process.pid);groups.update(found);cleanup.extend(notes)
   for group in sorted(groups,reverse=True):
    try:os.killpg(group,sig);cleanup.append(signal.Signals(sig).name+' sent to owned group '+str(group))
    except ProcessLookupError:cleanup.append('owned group absent '+str(group))
   try:process.wait(timeout=grace)
   except subprocess.TimeoutExpired:cleanup.append('parent remained after '+str(grace)+'s')
   live=[]
   for group in groups:
    try:os.killpg(group,0);live.append(group)
    except ProcessLookupError:pass
   if not live:break
  cleanup.append('remaining observed groups: '+str(live)+'; unobserved reparented descendants not established absent');code=process.poll()
end=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN);outputs=[o.ref(stdout),o.ref(stderr)]
if bundle.is_dir():outputs.extend(o.ref(x,archived=True) for x in sorted(bundle.iterdir()) if x.is_file() and x.name!='local-origin.json')
try:result=json.loads(stdout.read_bytes())
except (ValueError,UnicodeError):result=None
if result is not None:(record/'result.json').write_bytes(o.encoded(result));outputs.append(o.ref(record/'result.json'))
receipt={'schema':'stdo.execution-observation/1','producer':o.ref(producer,canonical='a_c/build_tenants/lean/scripts/formal_gate.py'),'result':o.ref(record/'result.json') if result is not None else o.ref(stdout),'observed_input_paths':[{'actual_path':str(x),'retained':o.ref(x)} for x in inputs],'execution':{'argv':argv,'cwd':str(b),'returncode':code,'started_ns':start,'ended_ns':end,'elapsed_seconds':(end-start)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss,'environment':{'python':python,'additions':{}},'inputs':[o.ref(x) for x in inputs],'outputs':outputs,'stdout':o.ref(stdout),'stderr':o.ref(stderr)}}
(record/'execution.json').write_bytes(o.encoded(receipt));(record/'SUPERVISION.json').write_bytes(o.encoded({'outer_timeout_seconds':7200,'outer_timeout_occurred':timed_out,'cleanup_observations':cleanup,'process_id':process.pid,'standing':'Actual selected bound and observed cleanup; no fabricated verifier verdict.'}))
passed=code==0 and not timed_out and isinstance(result,dict) and result.get('status')=='verified' and result.get('runtime_identity')==checker['runtime_identity']
name='PENDING_INSPECTION.json' if passed else 'INCOMPLETE.json';(p/'formal'/name).write_bytes(o.encoded({'execution':o.ref(record/'execution.json'),'result':o.ref(bundle/'result.json',archived=True) if (bundle/'result.json').is_file() else None,'standing':'Actual fresh installed proof completed; owner inspection remains pending.' if passed else 'Actual failed/incomplete attempt retained; no retry or release consumer may consume it as success.'}))
print(json.dumps({'status':result.get('status') if isinstance(result,dict) else 'unreadable','returncode':code,'seconds':(end-start)/1e9,'outer_timeout':timed_out,'execution':str(record/'execution.json')}),flush=True)
raise SystemExit(0 if passed else 4)
