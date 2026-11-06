from pathlib import Path
import hashlib,json,os,platform,resource,subprocess,sys,time
here=Path(__file__).resolve().parent
repo=here.parents[5]
selection=json.loads((here/'graphify-bootstrap-current-selection.json').read_text())
destination=Path(selection['destination'])
argv=[sys.executable,'-B',str(repo/'a_c/scripts/bootstrap.py'),'graphify','--destination',str(destination)]
started=time.time_ns(); before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (here/'graphify-bootstrap-current.stdout.log').open('wb') as out,(here/'graphify-bootstrap-current.stderr.log').open('wb') as err:
 result=subprocess.run(argv,stdout=out,stderr=err,cwd=repo)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
record={'schema':'stdo305.execution/1','argv':argv,'cwd':str(repo),'exit_code':result.returncode,'started_ns':started,'ended_ns':time.time_ns(),'elapsed_seconds':(time.time_ns()-started)/1e9,'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss,'platform':platform.platform(),'python':sys.version,'environment_names':['PATH','PYTHONDONTWRITEBYTECODE'],'scope':'isolated dependency acquisition, shared project Git and global host configuration untouched'}
for name in ['stdout','stderr']:
 p=here/('graphify-bootstrap-current.'+name+'.log');record[name]={'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
if result.returncode==0:
 record['runtime']=json.loads((destination/'RUNTIME.json').read_text())
 p=subprocess.run([str(destination/'venv/bin/python'),'-m','pip','freeze','--all'],capture_output=True,check=True)
 (here/'graphify-bootstrap-current.packages.txt').write_bytes(p.stdout)
 record['packages_sha256']=hashlib.sha256(p.stdout).hexdigest()
(here/'graphify-bootstrap-current.execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
raise SystemExit(result.returncode)
