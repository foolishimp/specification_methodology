"""Record actual public formal executions; no report is synthesized as execution."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import resource
import subprocess
import sys
import time

REPO=Path(__file__).resolve().parents[6]
PRODUCER=REPO/'a_c/build_tenants/lean/scripts/formal_gate.py'

def ref(path):
    path=Path(path).absolute();raw=path.read_bytes()
    return {'path':path.relative_to(REPO).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}

def execute(mode,request,output,record_dir,bundle=None):
    request=Path(request).absolute();output=Path(output).absolute();record_dir=Path(record_dir).absolute()
    record_dir.mkdir(parents=True,exist_ok=False)
    argv=[sys.executable,'-I','-S','-B',str(PRODUCER)]
    if mode=='verify':argv+=['verify','--request',str(request),'--output',str(output)]
    else:argv+=['check-evidence','--fresh','--bundle',str(Path(bundle).absolute()),'--output',str(output)]
    req=json.loads(request.read_text());inputs=[request]
    for key in ('input','supplied_views'):
        if req[key] is not None:
            p=Path(req[key]['path']);inputs.append(p if p.is_absolute() else request.parent/p)
    if bundle is not None:inputs.extend(p for p in Path(bundle).iterdir() if p.is_file())
    stdout=record_dir/'stdout.json';stderr=record_dir/'stderr.log'
    started=time.time_ns();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with stdout.open('wb') as out,stderr.open('wb') as err:r=subprocess.run(argv,cwd=REPO,stdout=out,stderr=err)
    ended=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN)
    physical=Path(sys.executable).resolve()
    outputs=[stdout,stderr]+[p for p in output.iterdir() if p.is_file()] if output.is_dir() else [stdout,stderr]
    result=output/'result.json'
    record={'schema':'stdo.execution-observation/1','producer':ref(PRODUCER),'result':ref(result) if result.exists() else ref(stdout),
            'execution':{'argv':argv,'cwd':str(REPO),'returncode':r.returncode,
                'environment':{'python':{'invocation':sys.executable,'executable_realpath':str(physical),'sha256':hashlib.sha256(physical.read_bytes()).hexdigest(),'version':platform.python_version()}},
                'inputs':[ref(p) for p in sorted(set(inputs))],'outputs':[ref(p) for p in sorted(set(outputs))],
                'stdout':ref(stdout),'stderr':ref(stderr),'started_ns':started,'ended_ns':ended,'elapsed_seconds':(ended-started)/1e9,
                'user_seconds':after.ru_utime-before.ru_utime,'system_seconds':after.ru_stime-before.ru_stime,'child_maxrss_native_units':after.ru_maxrss}}
    (record_dir/'execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'record':str(record_dir/'execution.json'),'exit_code':r.returncode,'seconds':(ended-started)/1e9}),flush=True)
    return r.returncode

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--request',type=Path,required=True);p.add_argument('--root',type=Path,required=True);a=p.parse_args()
    a.root=a.root.absolute();a.root.mkdir(parents=True,exist_ok=False)
    code=execute('verify',a.request,a.root/'cold',a.root/'cold-execution')
    if code:raise SystemExit(code)
    raise SystemExit(execute('fresh',a.request,a.root/'fresh',a.root/'fresh-execution',a.root/'cold'))
