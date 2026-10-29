"""Fresh public command under the selected external600s fence."""
from pathlib import Path
import sys,json,time,resource
root=Path(__file__).resolve().parents[4]/'build_tenants/lean'
sys.path.insert(0,str(root/'scripts'))
import formal_support as support
import runtime_process
base=Path(__file__).resolve().parent;label=sys.argv[1];request=Path(sys.argv[2]).resolve();out=base/label
_,env,_=support.tools()
command=[sys.executable,'-I','-S','-B',str(root/'scripts/formal_gate.py'),'verify','--request',str(request),'--output',str(out)]
result={'command':command,'outer_seconds':600,'per_stage_seconds':90,'lean_memory_mb':4096,'os_rss_cap':False,'status':'incomplete'}
start=time.monotonic()
try:
 with (base/(label+'.public.log')).open('xb') as log:r=runtime_process.run(command,cwd=root,env=env,stdout=log,timeout=600)
 result['returncode']=r.returncode
 if (out/'result.json').is_file():
  gate=json.loads((out/'result.json').read_text());result.update(status=gate['status'],reason=gate['reason'],gate_elapsed_seconds=gate['observations']['elapsed_seconds'],stages=gate['observations']['stages'],gate_result_sha256=support.sha(out/'result.json'))
except Exception as exc:result['error']=type(exc).__name__+': '+str(exc)
result.update(external_elapsed_seconds=time.monotonic()-start,child_high_water_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
(base/(label+'.public-result.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
