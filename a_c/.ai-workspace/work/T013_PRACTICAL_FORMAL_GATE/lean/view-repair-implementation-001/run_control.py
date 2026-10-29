"""Selected component compiler controls; no public gate or actor invocation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,resource,sys,time
OUT=Path(__file__).resolve().parent
BASELINE=json.loads((OUT/'BASELINE.json').read_bytes())
ROOT=OUT.parents[4]/'build_tenants/lean'
BUNDLE=Path(BASELINE['frozen_bundle'])
sys.path.insert(0,str(ROOT/'scripts'))
import formal_support,runtime_process
mode=sys.argv[1]
sources={'actual-29':'actual-29/GateViews.lean','unknown-parent':'negatives/UnknownParent.lean','missing-edge':'negatives/MissingEdge.lean','omitted-residual':'negatives/OmittedResidual.lean'}
source=OUT/sources[mode]
label=mode+'-attempt-'+sys.argv[2]
assert not (OUT/(label+'.external.json')).exists(),'Attempt already recorded'
if mode!='actual-29':
 positive=json.loads((OUT/'actual-29-attempt-001.external.json').read_bytes())
 assert positive['returncode']==0 and positive['audit_status']=='PASS','Actual positive must pass first'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
prefix,env,_=formal_support.proof_environment(BUNDLE)
command=[str(prefix/'bin/lean'),'-j','1','-M','4096','-R',str(source.parent),'-o',str(source.with_suffix('.olean')),str(source)]
record={'schema':'a_c.T013.view-repair-component-control/1','label':label,'started_utc':datetime.now(timezone.utc).isoformat(),'argv':command,'cwd':str(ROOT),'LEAN_PATH':env['LEAN_PATH'],'source_sha256':sha(source),'timeout_seconds':90,'physical_rss_cap':False,'evidence_kind':'Actual kernel-checked generated component; not complete public gate qualification','rss_scope':'Darwin native bytes: isolated launcher self and RUSAGE_CHILDREN high-water field for the reaped compiler; no simultaneous total-RSS claim.'}
start=time.monotonic()
try:
 with (OUT/(label+'.log')).open('xb') as log:
  process=runtime_process.run(command,cwd=ROOT,env=env,stdout=log,timeout=90)
 record['returncode']=process.returncode
 record['compile_status']='compiled' if process.returncode==0 else 'did-not-compile'
 text=(OUT/(label+'.log')).read_text()
 record['resource_failure']='memory_exception' in text or process.returncode<0
 if mode=='actual-29' and process.returncode==0:
  import formal_gate
  audit=formal_gate._audit(text,['AC.GateData.'+p+'0' for p in ('checked','set','reachability','result','execution_matches_project')])
  record['audit']={name:sorted(axioms) for name,axioms in audit.items()}
  record['audit_status']='PASS'
except Exception as exc:
 record['compile_status']='incomplete';record['error']=type(exc).__name__+': '+str(exc)
 record['resource_failure']=isinstance(exc,TimeoutError) or 'TimeoutExpired' in type(exc).__name__
record['seconds']=time.monotonic()-start
record['finished_utc']=datetime.now(timezone.utc).isoformat()
record['launcher_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
record['reaped_child_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
record['log_sha256']=sha(OUT/(label+'.log'))
record['produced']={p.name:sha(p) for p in source.parent.glob(source.stem+'.*') if p.is_file() and p.suffix!='.lean'}
with (OUT/(label+'.external.json')).open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({k:record.get(k) for k in ('label','compile_status','returncode','audit_status','resource_failure','seconds','reaped_child_peak_rss_bytes','error')}),flush=True)
