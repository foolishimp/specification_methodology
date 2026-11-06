from pathlib import Path
import hashlib, json, os, platform, resource, subprocess, sys, time
HERE=Path(__file__).resolve().parent
ROOT=HERE.with_name('current-formal-020')
REPO=Path('/Users/jim/src/apps/specification_methodology')
PLAN=HERE/'POST_SUCCESS_PLAN.json'
def ref(path):
 path=Path(path).absolute();raw=path.read_bytes()
 return {'path':path.relative_to(REPO).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
def save(path,value):
 with path.open('x') as stream:stream.write(json.dumps(value,sort_keys=True,indent=2)+'\n')
def pinned(row):
 path=REPO/row['path'];assert ref(path)==row,('changed selected input',row['path']);return path
assert hashlib.sha256(PLAN.read_bytes()).hexdigest()==sys.argv[1]
plan=json.loads(PLAN.read_text());producer=pinned(plan['producer']);request=pinned(plan['request']);config=pinned(plan['selected_checker'])
selected=json.loads(config.read_text());req=json.loads(request.read_text());result=ROOT/'cold/result.json';manifest=ROOT/'cold/manifest.json';execution=ROOT/'cold-execution/execution.json';supervision=ROOT/'cold-execution/SUPERVISION.json'
value=json.loads(result.read_text());observed=json.loads(execution.read_text());outer=json.loads(supervision.read_text())
assert observed['execution']['returncode']==0 and value['status']=='verified'
assert not outer['outer_timeout_occurred'] and outer['cleanup_observations']==[]
assert value['runtime_identity']==plan['runtime_identity']==selected['runtime_identity']
assert value['selections']==req['selections'] and value['context_binding']==req['context_binding']
assert value['request_sha256']==hashlib.sha256(json.dumps(req,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
assert value['inputs']['input']['raw_sha256']==req['input']['raw_sha256']
assert value['inputs']['supplied_views']['raw_sha256']==req['supplied_views']['raw_sha256']
assert value['evidence']['manifest_sha256']==ref(manifest)['sha256']
for name,expected in selected['runtime_identity']['pins'].items():
 assert hashlib.sha256((Path(selected['root'])/name).read_bytes()).hexdigest()==expected,('changed runtime',name)
inputs=[request,Path(req['input']['path']),Path(req['supplied_views']['path']),result,manifest,execution,supervision,config]
assert ref(inputs[1])['sha256']==req['input']['raw_sha256'];assert ref(inputs[2])['sha256']==req['supplied_views']['raw_sha256']
try:os.killpg(outer['process_id'],0)
except ProcessLookupError:group_absent=True
else:group_absent=False
assert group_absent,'recorded verifier private process group still exists'
physical=Path(plan['argv'][0]).resolve(strict=True);assert hashlib.sha256(physical.read_bytes()).hexdigest()==selected['python']['sha256']
record=ROOT/'inspection';record.mkdir(exist_ok=False)
save(record/'PREINVOCATION.json',{'plan':ref(PLAN),'recorder':ref(Path(__file__)),'argv':plan['argv'],'cwd':plan['cwd'],'timeout_seconds':180,'inputs':[ref(q) for q in inputs],'runtime_identity':value['runtime_identity'],'verifier_group_absent':group_absent,'cleanup_boundary':'Actual verifier parent/private group absent; each successful compiler stage used selected runtime_process.run group-absence enforcement. No claim of separately observed numeric compiler-group identities.'})
stdout=record/'stdout.json';stderr=record/'stderr.log';started=time.time_ns();before=resource.getrusage(resource.RUSAGE_CHILDREN);timed_out=False
with stdout.open('xb') as out,stderr.open('xb') as err:
 try:process=subprocess.run(plan['argv'],cwd=plan['cwd'],env={'PATH':os.defpath,'HOME':'/Users/jim'},stdout=out,stderr=err,timeout=180);code=process.returncode
 except subprocess.TimeoutExpired:timed_out=True;code=None
ended=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN)
copy=ROOT/'cold-inspection.json';copy.write_bytes(stdout.read_bytes())
actual={'schema':'stdo.execution-observation/1','producer':plan['producer'],'result':ref(copy),'execution':{'argv':plan['argv'],'cwd':plan['cwd'],'returncode':code,'environment':{'python':{'invocation':plan['argv'][0],'executable_realpath':str(physical),'sha256':selected['python']['sha256'],'version':platform.python_version()}},'inputs':[ref(q) for q in inputs],'outputs':[ref(stdout),ref(stderr),ref(copy)],'stdout':ref(stdout),'stderr':ref(stderr),'started_ns':started,'ended_ns':ended,'elapsed_seconds':(ended-started)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss}}
save(record/'execution.json',actual);save(record/'OUTCOME.json',{'timed_out':timed_out,'returncode':code,'elapsed_seconds':(ended-started)/1e9,'standing':'Actual owner read-only inspection result; no new kernel verdict or retry.'})
print(json.dumps({'execution':ref(record/'execution.json'),'result':ref(copy),'returncode':code,'timed_out':timed_out,'elapsed_seconds':(ended-started)/1e9}),flush=True)
raise SystemExit(code if type(code) is int and code>=0 else 4)
