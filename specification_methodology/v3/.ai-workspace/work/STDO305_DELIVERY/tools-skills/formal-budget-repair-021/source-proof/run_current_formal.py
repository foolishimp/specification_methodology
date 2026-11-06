"""Prospective actual CLI recorder; no source/runtime alteration or proof reuse."""
from pathlib import Path
import hashlib, importlib.util, json, os, platform, resource, signal, subprocess, sys, time
HERE=Path(__file__).resolve().parent
PLAN=HERE/'PLAN.json'
REPO=Path('/Users/jim/src/apps/specification_methodology')
def ref(path):
 path=Path(path).absolute();raw=path.read_bytes()
 return {'path':path.relative_to(REPO).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
def pinned(row):
 path=REPO/row['path'];assert ref(path)==row,('changed prepared input',row['path']);return path
def save(path,value):
 with path.open('x') as stream:stream.write(json.dumps(value,sort_keys=True,indent=2)+'\n')
def main():
 plan=json.loads(PLAN.read_text())
 for row in plan['required_files']:pinned(row)
 config=json.loads(pinned(plan['selection']).read_text())
 helper=pinned(plan['supervisor_helper'])
 spec=importlib.util.spec_from_file_location('selected_supervisor',helper)
 supervisor=importlib.util.module_from_spec(spec);spec.loader.exec_module(supervisor)
 supervisor.validate_config(config);supervisor._pins(config)
 physical=Path(plan['argv'][0]).resolve(strict=True)
 assert hashlib.sha256(physical.read_bytes()).hexdigest()==config['python']['sha256']
 assert config['timeout_seconds']==plan['outer_timeout_seconds']==7200
 output=Path(plan['output']);record=Path(plan['record_directory']);subject=output.parent
 assert not subject.exists(),('fresh subject required',str(subject))
 subject.mkdir();record.mkdir()
 save(record/'INVOCATION.json',{'plan':ref(PLAN),'recorder':ref(Path(__file__)),'argv':plan['argv'],'cwd':plan['cwd'],'selected_environment':plan['selected_environment'],'outer_timeout_seconds':7200,'input_files':plan['inputs']})
 stdout=record/'stdout.json';stderr=record/'stderr.log';cleanup=[];outer_timeout=False
 before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.time_ns()
 with stdout.open('xb') as out,stderr.open('xb') as err:
  process=subprocess.Popen(plan['argv'],cwd=plan['cwd'],env=plan['selected_environment'],stdout=out,stderr=err,start_new_session=True,close_fds=True)
  save(record/'PROCESS.json',{'pid':process.pid,'private_process_group':process.pid,'started_ns':start})
  try:code=process.wait(timeout=7200)
  except subprocess.TimeoutExpired:
   outer_timeout=True
   groups,observations=supervisor._owned_groups(process.pid);cleanup.extend(observations)
   for signum,grace in ((signal.SIGTERM,10),(signal.SIGKILL,2)):
    if signum==signal.SIGKILL:
     observed,notes=supervisor._owned_groups(process.pid);groups.update(observed);cleanup.extend(notes)
    for group in sorted(groups,reverse=True):
     try:os.killpg(group,signum);cleanup.append(signal.Signals(signum).name+' sent to observed owned group '+str(group))
     except ProcessLookupError:cleanup.append('observed owned group absent: '+str(group))
    try:process.wait(timeout=grace)
    except subprocess.TimeoutExpired:cleanup.append('parent remained after '+str(grace)+' seconds')
    live=[]
    for group in groups:
     try:os.killpg(group,0);live.append(group)
     except ProcessLookupError:pass
    if not live:break
   cleanup.append('remaining observed groups: '+str(live)+'; unobserved reparented descendants are not established absent')
   code=process.poll()
 end=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN)
 inputs=[pinned(row) for row in plan['inputs']]
 outputs=[stdout,stderr]+([q for q in output.iterdir() if q.is_file() and q.name!='local-origin.json'] if output.is_dir() else [])
 result=output/'result.json'
 record_value={'schema':'stdo.execution-observation/1','producer':plan['producer'],'result':ref(result) if result.is_file() else ref(stdout),'execution':{'argv':plan['argv'],'cwd':plan['cwd'],'returncode':code,'environment':{'python':{'invocation':plan['argv'][0],'executable_realpath':str(physical),'sha256':config['python']['sha256'],'version':platform.python_version()}},'inputs':[ref(q) for q in sorted(set(inputs))],'outputs':[ref(q) for q in sorted(set(outputs))],'stdout':ref(stdout),'stderr':ref(stderr),'started_ns':start,'ended_ns':end,'elapsed_seconds':(end-start)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss}}
 save(record/'execution.json',record_value)
 save(record/'SUPERVISION.json',{'outer_timeout_seconds':7200,'outer_timeout_occurred':outer_timeout,'selected_checker':plan['selection'],'supervisor_helper':plan['supervisor_helper'],'process_id':process.pid,'cleanup_observations':cleanup,'standing':'Outer operator supervision only; actual verifier stdout/result decides mathematical status. No verdict is manufactured on timeout.'})
 print(json.dumps({'execution':ref(record/'execution.json'),'returncode':code,'elapsed_seconds':(end-start)/1e9,'outer_timeout':outer_timeout}),flush=True)
 return code if isinstance(code,int) and code>=0 and not outer_timeout else 4
if __name__=='__main__':raise SystemExit(main())
