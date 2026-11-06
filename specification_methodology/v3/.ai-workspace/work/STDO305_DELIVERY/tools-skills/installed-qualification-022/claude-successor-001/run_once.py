"""One explicitly assigned,600-second Read/Write-only rationale/report successor."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,resource,signal,subprocess,time
from types import SimpleNamespace

def sha(path):
 with Path(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def ref(path):
 path=Path(path).absolute();assert path.is_file() and not path.is_symlink()
 return {'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
def encoded(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
def ordinary_parents(path):
 for ancestor in Path(path).parents:assert ancestor.is_dir() and not ancestor.is_symlink(),str(ancestor)
a=argparse.ArgumentParser();a.add_argument('--plan',required=True);a.add_argument('--plan-sha256',required=True);args=a.parse_args()
planpath=Path(args.plan);assert sha(planpath)==args.plan_sha256
plan=json.loads(planpath.read_bytes());assert sha(__file__)==plan['recorder']['sha256']
for selected in plan['inputs']:
 path=Path(selected['path']);ordinary_parents(path);assert ref(path)==selected,('changed input',str(path))
for output in plan['case_outputs']:
 path=Path(output);ordinary_parents(path);assert not path.exists() and not path.is_symlink(),str(path)
record=Path(plan['record_directory']);ordinary_parents(record);assert not record.exists() and not record.is_symlink()
argv=plan['argv'];workspace=Path(plan['cwd']);stdin=Path(plan['stdin']['path']);limit=plan['wall_timeout_seconds'];host='claude-rationale-report';assert limit==600
assert argv[argv.index('--tools')+1]=='Read,Write'
assert argv[argv.index('--allowedTools')+1:argv.index('--effort')]==['Read','Write']
environment_additions=plan['environment_additions'];assert environment_additions=={'STDO_STORE':str(workspace/'deliberately-unselected-store')}
physical=Path(argv[0]).resolve(strict=True);assert ref(physical)==plan['physical_executable']
helper=Path(plan['observer']['path']);assert ref(helper)==plan['observer'];spec=importlib.util.spec_from_file_location('selected_native_observer',helper);observer=importlib.util.module_from_spec(spec);exec(compile(helper.read_bytes(),str(helper),'exec'),observer.__dict__)
o=SimpleNamespace(ref=ref,encoded=encoded)
record.mkdir(exist_ok=False);stdout=record/'stdout.jsonl';stderr=record/'stderr.log'
invocation={'schema':'stdo.native-host-invocation/1','argv':argv,'cwd':str(workspace),'stdin':ref(stdin),'inputs':plan['inputs'],'executable':{'invocation':argv[0],'physical':str(physical),'sha256':sha(physical)},'requested_model':'opus','requested_effort':'xhigh','observed_resolved_model':'unproven before actual session','wall_timeout_seconds':limit,'observer':ref(helper),'recorder':ref(__file__),'plan':ref(planpath),'environment':'Authentication inherited without inspection; no environment dump or HOME override.','environment_additions':environment_additions,'case_outputs':plan['case_outputs']}
(record/'invocation.json').write_bytes(encoded(invocation));before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.time_ns();deadline=time.monotonic()+limit;groups=set();notes=[];timed=False;cleanup_needed=False;unresolved=[]
def observe(pid):
 found,observed=observer._owned_groups(pid);groups.update(found);entry={'observed_ns':time.time_ns(),'groups':sorted(found),'notes':observed}
 with (record/'group-observations.jsonl').open('a') as f:f.write(json.dumps(entry)+'\n')
 return found
def live_groups():
 live=[]
 for group in sorted(groups):
  try:os.killpg(group,0);live.append(group)
  except ProcessLookupError:pass
  except PermissionError as error:unresolved.append({'group':group,'errno':error.errno,'operation':'probe'});live.append(group)
 return live
print(json.dumps({'phase':host+'-native-session','status':'starting','requested_model':invocation['requested_model'],'requested_effort':'xhigh','wall_timeout_seconds':limit}),flush=True)
with stdout.open('xb') as out,stderr.open('xb') as err,stdin.open('rb') as inp:
 os.environ.update(environment_additions)
 process=subprocess.Popen(argv,cwd=workspace,stdin=inp,stdout=out,stderr=err,start_new_session=True,close_fds=True)
 (record/'PROCESS.json').write_bytes(o.encoded({'pid':process.pid,'private_group':process.pid,'started_ns':started}));groups.add(process.pid)
 while True:
  observe(process.pid)
  remaining=deadline-time.monotonic()
  if remaining<=0:timed=True;break
  try:process.wait(timeout=min(10,remaining));break
  except subprocess.TimeoutExpired:continue
 observe(process.pid);remaining_groups=live_groups();cleanup_needed=bool(remaining_groups)
 if timed or remaining_groups:
  for sig,grace in [(signal.SIGTERM,10),(signal.SIGKILL,2)]:
   observe(process.pid)
   for group in live_groups():
    try:os.killpg(group,sig);notes.append({'group':group,'signal':signal.Signals(sig).name,'sent':True})
    except ProcessLookupError:notes.append({'group':group,'signal':signal.Signals(sig).name,'already_absent':True})
    except PermissionError as error:unresolved.append({'group':group,'signal':signal.Signals(sig).name,'errno':error.errno,'operation':'signal'})
   until=time.monotonic()+grace
   while time.monotonic()<until:
    process.poll()
    if not live_groups():break
    time.sleep(min(.1,max(0,until-time.monotonic())))
   if not live_groups():break
 code=process.poll();remaining_groups=live_groups()
ended=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN);result={'schema':'stdo.native-host-process-observation/1','host':host,'returncode':code,'timed_out':timed,'cleanup_needed_after_parent_exit':cleanup_needed,'cleanup_actions':notes,'unresolved_cleanup':unresolved,'remaining_known_groups':remaining_groups,'known_groups':sorted(groups),'requested_model':invocation['requested_model'],'requested_effort':'xhigh','observed_resolved_model':'Inspect actual retained host metadata; no request-derived resolution claim.','started_ns':started,'ended_ns':ended,'elapsed_seconds':(ended-started)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss,'stdout':o.ref(stdout),'stderr':o.ref(stderr),'limit':'Observed selected private groups only; unobserved reparented descendants are not proven absent. Case results and semantic quality require separate actual artifact assessment.'};(record/'result.json').write_bytes(o.encoded(result))

output_refs=[]
for output in plan['case_outputs']:
 path=Path(output)
 if path.is_file() and not path.is_symlink():
  data=path.read_bytes();retained=record/path.name
  with retained.open('xb') as stream:stream.write(data)
  output_refs.append({'actual':ref(path),'retained':ref(retained)})
changed=[selected['path'] for selected in plan['inputs'] if not Path(selected['path']).is_file() or sha(selected['path'])!=selected['sha256']]
(record/'POST_OBSERVATION.json').write_bytes(encoded({'outputs':output_refs,'changed_selected_inputs':changed,'original_timeout_preserved':True,'standing':'Actual process/output observation only; independent rationale and report closure assessment required.'}))
print(json.dumps({'phase':host,'returncode':code,'timed_out':timed,'seconds':result['elapsed_seconds'],'known_groups_absent':not remaining_groups,'changed_selected_inputs':changed,'outputs_observed':len(output_refs)}),flush=True)
raise SystemExit(0 if code==0 and not timed and not cleanup_needed and not unresolved and not remaining_groups and not changed else 4)
