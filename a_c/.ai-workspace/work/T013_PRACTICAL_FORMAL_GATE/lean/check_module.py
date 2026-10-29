"""Bounded implementation check. Every invocation has a retained source/log/result."""
from pathlib import Path
import sys,json,time,resource,os
root=Path(__file__).resolve().parents[4]/'build_tenants/lean'
sys.path.insert(0,str(root/'scripts'))
import formal_support as s
import runtime_process
folder=Path(sys.argv[1]).resolve();source=Path(sys.argv[2]).resolve();output=Path(sys.argv[3]).resolve();label=sys.argv[4]
folder.mkdir(parents=True,exist_ok=True)
prefix,env,_=s.proof_environment(source.parent)
if len(sys.argv)>5:env['LEAN_PATH']=os.pathsep.join(sys.argv[5:])+os.pathsep+env['LEAN_PATH']
cmd=[str(prefix/'bin/lean'),'-j','1','-M','4096','-R',str(root if source.is_relative_to(root/'AC') else source.parent),'-o',str(output),str(source)]
result={'command':cmd,'source_sha256':s.sha(source),'compiler_sha256':s.sha(prefix/'bin/lean'),'lean_memory_mb':4096,'timeout_seconds':90,'rss_limit':False}
(folder/(label+'.source.lean')).write_bytes(source.read_bytes())
start=time.monotonic()
try:
 with (folder/(label+'.log')).open('xb') as f:r=runtime_process.run(cmd,cwd=root,env=env,stdout=f,timeout=90)
 result['returncode']=r.returncode
except Exception as e:result['error']=type(e).__name__+': '+str(e)
result.update(seconds=time.monotonic()-start,child_high_water_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
(folder/(label+'.result.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));print((folder/(label+'.log')).read_text())
