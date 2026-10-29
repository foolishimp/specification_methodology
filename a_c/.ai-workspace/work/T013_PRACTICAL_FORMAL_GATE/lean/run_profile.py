"""One bounded diagnostic process; run this script fresh for each measurement."""
import hashlib,json,resource,sys,time
from pathlib import Path

REPO=Path('/Users/jim/src/apps/specification_methodology')
TENANT=REPO/'a_c/build_tenants/lean'
sys.path.insert(0,str(TENANT/'scripts'))
import formal_support as support
import runtime_process

folder=Path(sys.argv[1]).resolve();name=sys.argv[2]
prefix,env,_=support.proof_environment(folder)
command=[str(prefix/'bin/lean'),'-j','1','-M','4096','-R',str(folder),'-o',str(folder/(name+'.olean')),str(folder/(name+'.lean'))]
result={'name':name,'command':command,'source_sha256':support.sha(folder/(name+'.lean')),
        'compiler_sha256':support.sha(prefix/'bin/lean'),'support_manifest_sha256':support.sha(support.SUPPORT),
        'timeout_seconds':90,'lean_memory_mb':4096,'status':'incomplete'}
start=time.monotonic()
try:
    with (folder/(name+'.log')).open('xb') as log:
        completed=runtime_process.run(command,cwd=TENANT,env=env,stdout=log,timeout=90)
    result.update(exit_code=completed.returncode,status='passed' if completed.returncode==0 else 'incomplete')
except Exception as exc:
    result.update(error=type(exc).__name__+': '+str(exc))
result.update(seconds=time.monotonic()-start,child_high_water_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
result['log_sha256']=support.sha(folder/(name+'.log'))
with (folder/(name+'.result.json')).open('x') as out:json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
print(json.dumps(result,sort_keys=True))
