"""Record existing Axiom stdout routes; preserve prior output-file observations."""
from pathlib import Path
import hashlib, json, resource, subprocess, sys, time
REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).resolve().parent
OLD = HERE/'model-rebind-003/public/axiom-validate-map/execution.json'
ROOT = HERE/'model-rebind-006'

def ref(path):
    path=Path(path).absolute(); raw=path.read_bytes()
    return {'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
def save(path,value):
    with path.open('x') as stream: stream.write(json.dumps(value,sort_keys=True,indent=2)+'\n')

prior=json.loads(OLD.read_bytes()); argv=prior['execution']['argv']; index=argv.index('--output'); del argv[index:index+2]
producer=Path(argv[2]); program=Path(argv[argv.index('--program')+1]); bindings=Path(argv[argv.index('--bindings')+1]); mapped=Path(argv[argv.index('--emit-map')+1])
ROOT.mkdir(); before_map=mapped.read_bytes(); (ROOT/'logical-constraint-map.preimage.json').write_bytes(before_map)
assert Path(sys.executable).resolve()==Path(argv[0]).resolve()
python={'invocation':argv[0],'executable_realpath':str(Path(argv[0]).resolve()),'sha256':ref(Path(argv[0]).resolve())['sha256'],'version':sys.version}
for phase in ('map','index'):
    actual=argv if phase=='map' else argv[:argv.index('--emit-map')]
    record=ROOT/phase;record.mkdir(); inputs=[ref(program),ref(bindings)]
    save(record/'INVOCATION.json',{'argv':actual,'cwd':str(REPO),'producer':ref(producer),'inputs':inputs,'environment':{'python':python},'predecessor':ref(OLD),'timeout_seconds':180})
    start=time.time_ns();usage=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (record/'stdout.json').open('xb') as out,(record/'stderr.log').open('xb') as err:
        process=subprocess.run(actual,cwd=REPO,stdout=out,stderr=err,timeout=180)
    end=time.time_ns();after=resource.getrusage(resource.RUSAGE_CHILDREN)
    outputs=[record/'stdout.json',record/'stderr.log']+([mapped] if phase=='map' else [])
    save(record/'execution.json',{'schema':'stdo.execution-observation/1','producer':ref(producer),'result':ref(record/'stdout.json'),'execution':{'argv':actual,'cwd':str(REPO),'returncode':process.returncode,'environment':{'python':python},'inputs':inputs,'outputs':[ref(p) for p in outputs],'stdout':ref(record/'stdout.json'),'stderr':ref(record/'stderr.log'),'started_ns':start,'ended_ns':end,'elapsed_seconds':(end-start)/1e9,'user_seconds':after.ru_utime-usage.ru_utime,'system_seconds':after.ru_stime-usage.ru_stime,'child_maxrss_native_units':after.ru_maxrss}})
    assert process.returncode==0,phase
    assert inputs==[ref(program),ref(bindings)],'input changed'
    assert mapped.read_bytes()==before_map,'canonical map bytes changed'
save(ROOT/'CORRESPONDENCE.json',{'predecessor':ref(OLD),'preimage':ref(ROOT/'logical-constraint-map.preimage.json'),'current_map':ref(mapped),'exact_raw_bytes_equal':True,'actual_map':ref(ROOT/'map/execution.json'),'actual_index':ref(ROOT/'index/execution.json'),'scope':'Same current program/bindings through existing stdout APIs. Original --output execution retained; no model change or new semantic claim.'})
print(json.dumps({'correspondence':ref(ROOT/'CORRESPONDENCE.json'),'map':ref(ROOT/'map/execution.json'),'index':ref(ROOT/'index/execution.json')}))
