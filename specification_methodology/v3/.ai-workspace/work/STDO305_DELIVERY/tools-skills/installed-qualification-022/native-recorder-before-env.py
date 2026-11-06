"""One selected native session with the approved900s private-group boundary."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,resource,signal,subprocess,time
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace'])
a=argparse.ArgumentParser();a.add_argument('host',choices=['codex','claude']);args=a.parse_args();host=args.host
contracts=json.loads((o.REPO/h['commands']['path']).read_bytes());bound=json.loads((o.REPO/h['native_host_bound']['path']).read_bytes());command=next(x for x in contracts['commands'] if x['id']==host+'-native-session');argv=command['argv'];case=b/'hosts'/host/'cases';workspace=case.parent;stdin=case/'host-prompt.txt';selected=json.loads((case/'SELECTION.json').read_bytes())
assert (case/'uncertain/PRIOR_ATTEMPT.json').is_file(),'Actual uncertain prior must be seeded before host launch'
assert (b/'hosts/codex/cases/current-context/operator-controls-dispatch/DELIVERY.json').is_file(),'Context delivery must close before any model session'
assert o.sha(o.REPO/h['commands']['path'])==h['commands']['sha256'];assert o.sha(o.REPO/h['native_host_bound']['path'])==h['native_host_bound']['sha256']
helper=b/'runtime/a_c/build_tenants/graphify/code/ac_formal_gate.py';assert o.sha(helper)==bound['observer_source']['sha256'];spec=importlib.util.spec_from_file_location('selected_native_observer',helper);observer=importlib.util.module_from_spec(spec);spec.loader.exec_module(observer)
selection=next(x for x in bound['sessions'] if x['id']==host+'-native-session');stdout=Path(selection['stdout']);stderr=Path(selection['stderr']);limit=selection['wall_timeout_seconds'];assert limit==900
for x in [stdout,stderr]:assert not x.exists() and not x.is_symlink()
record=p/'executions'/(host+'-native-session');record.mkdir(exist_ok=False);executable=Path(argv[0]);physical=executable.resolve(strict=True);assert physical.is_file()
inputs=[stdin,case/'WORKER_INTAKE.json',case/'REVIEW_INTAKE.json',case/'SELECTION.json',Path(selected['configuration']['path']),case/'uncertain/PRIOR_ATTEMPT.json'];invocation={'schema':'stdo.native-host-invocation/1','argv':argv,'cwd':str(workspace),'stdin':o.ref(stdin),'inputs':[o.ref(x) for x in inputs],'executable':{'invocation':str(executable),'physical':str(physical),'sha256':o.sha(physical)},'requested_model':argv[argv.index('--model')+1],'requested_effort':'xhigh','observed_resolved_model':'unproven before actual session','wall_timeout_seconds':limit,'observer':o.ref(helper,canonical='a_c/build_tenants/graphify/code/ac_formal_gate.py'),'recorder':o.ref(Path(__file__)),'environment':'Inherited without inspecting or recording credentials; no HOME/CODEX_HOME override.'}
(record/'invocation.json').write_bytes(o.encoded(invocation));before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.time_ns();deadline=time.monotonic()+limit;groups=set();notes=[];timed=False;cleanup_needed=False;unresolved=[]
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
for name in ['HOST_RETURN.md','REVIEW_RETURN.json','codex-final.txt']:
 if (case/name).is_file():o.ref(case/name)
print(json.dumps({'phase':host+'-native-session','returncode':code,'timed_out':timed,'seconds':result['elapsed_seconds'],'known_groups_absent':not remaining_groups,'cleanup_needed':cleanup_needed,'standing':'Process observation only; required case assessment pending.'}),flush=True)
raise SystemExit(0 if code==0 and not timed and not cleanup_needed and not unresolved and not remaining_groups else 4)
