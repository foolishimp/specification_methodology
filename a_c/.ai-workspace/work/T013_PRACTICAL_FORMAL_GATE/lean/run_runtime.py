from pathlib import Path
import sys,json,time,resource,os
root=Path(__file__).resolve().parents[4]/'build_tenants/lean';sys.path.insert(0,str(root/'scripts'))
import formal_support as s
import runtime_process
folder=Path(sys.argv[1]).resolve();module=sys.argv[2];source=folder/(module+'.lean')
prefix,env,_=s.proof_environment(folder);env['LEAN_PATH']=str(folder.parent/'public-positive-001')+os.pathsep+env['LEAN_PATH']
cmd=[str(prefix/'bin/lean'),'-j','1','-M','4096','--run',str(source)];result={'command':cmd,'timeout_seconds':90,'lean_memory_mb':4096,'os_rss_cap':False,'source_sha256':s.sha(source),'status':'incomplete'};start=time.monotonic()
try:
 with (folder/(module+'.log')).open('xb') as log:r=runtime_process.run(cmd,cwd=root,env=env,stdout=log,timeout=90)
 result.update(returncode=r.returncode,status='passed' if r.returncode==0 else 'incomplete')
except Exception as e:result['error']=type(e).__name__+': '+str(e)
result.update(seconds=time.monotonic()-start,child_high_water_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
(folder/(module+'.result.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));print((folder/(module+'.log')).read_text()[-3000:])
