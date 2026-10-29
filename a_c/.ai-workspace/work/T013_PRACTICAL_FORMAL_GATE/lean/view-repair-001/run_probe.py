"""At most three separate compiler component probes; no gate or support rebuild."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import resource
import sys
import time

OUT=Path(__file__).resolve().parent
SUBJECT=json.loads((OUT/'SUBJECT.json').read_bytes())
ROOT=Path(SUBJECT['source_root'])
BUNDLE=Path(SUBJECT['frozen_bundle'])
sys.path.insert(0,str(ROOT/'scripts'))
import formal_support
import runtime_process
name=sys.argv[1]
ordinal={'ProbeWitness':1,'ProbeClosed':2,'ProbeDecomposed':3}[name]
assert not (OUT/(name+'.external.json')).exists(),'No probe repeat granted'
assert all((OUT/(prior+'.external.json')).exists() for prior in ('ProbeWitness','ProbeClosed')[:ordinal-1])
source=OUT/(name+'.lean');assert source.is_file()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
prefix,env,_=formal_support.proof_environment(BUNDLE)
command=[str(prefix/'bin/lean'),'-j','1','-M','4096','-R',str(OUT),'-o',str(OUT/(name+'.olean')),str(source)]
record={'schema':'a_c.T013.view-component-probe/1','ordinal':ordinal,'name':name,'started_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(source),'argv':command,'cwd':str(ROOT),'LEAN_PATH':env['LEAN_PATH'],'timeout_seconds':90,'physical_rss_cap':False,'retained_compiled_inputs':str(BUNDLE),'kernel_typecheck':'debug.skipKernelTC=false; decide +kernel only','rss_scope':'Darwin bytes: isolated launcher self and RUSAGE_CHILDREN high-water field for reaped compiler child; not simultaneous total or stage-attributed RSS.'}
start=time.monotonic()
try:
 with (OUT/(name+'.log')).open('xb') as log:
  process=runtime_process.run(command,cwd=ROOT,env=env,stdout=log,timeout=90)
 record['returncode']=process.returncode
 record['status']='compiled' if process.returncode==0 else 'did-not-compile'
except Exception as exc:
 record['status']='incomplete';record['error']=type(exc).__name__+': '+str(exc)
record['external_seconds']=time.monotonic()-start
record['finished_utc']=datetime.now(timezone.utc).isoformat()
record['launcher_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
record['reaped_child_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
record['log_sha256']=sha(OUT/(name+'.log'))
record['produced']={p.name:sha(p) for p in OUT.glob(name+'.*') if p.is_file() and p.suffix not in ('.lean','.log','.json')}
with (OUT/(name+'.external.json')).open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({k:record.get(k) for k in ('ordinal','name','status','returncode','external_seconds','reaped_child_peak_rss_bytes','error')}),flush=True)
