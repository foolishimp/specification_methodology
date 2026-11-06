"""Actual public containment counterexample on a retained disposable dependency copy."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import time

REPO=Path(__file__).resolve().parents[7]
WORK=Path(__file__).resolve().parent
ENTRY=REPO/'a_c/build_tenants/graphify/code/ac_upstream.py'

def sha(raw):return hashlib.sha256(raw).hexdigest()
def snapshot(root):
    result={}
    for p in sorted(root.rglob('*')):
        name=p.relative_to(root).as_posix()
        if p.is_symlink():result[name]={'kind':'symlink','target':str(p.readlink())}
        elif p.is_file():result[name]={'kind':'file','sha256':sha(p.read_bytes())}
        elif p.is_dir():result[name]={'kind':'directory'}
    return result

def main(label):
    evidence=WORK/label;evidence.mkdir(exist_ok=False)
    private=Path(tempfile.mkdtemp(prefix='stdo305-upstream-containment-'+label+'-')).resolve()
    original=Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo305-runtime-logged-zy3qk0do/graphify/RUNTIME.json')
    runtime=json.loads(original.read_text());upstream=private/'upstream';shutil.copytree(runtime['upstream'],upstream,symlinks=True)
    runtime['upstream']=str(upstream);runtime_path=private/'runtime.json';runtime_path.write_text(json.dumps(runtime,indent=2)+'\n')
    fixtures=WORK.parent/'upstream-owner-tests';model=REPO/'a_c/build_tenants/graphify/test_env/fixtures/toy_model.json'
    argv=[runtime['python'],'-B',str(ENTRY),'--model',str(model),'--carrier',str(fixtures/'carrier.json'),'--selections',str(fixtures/'selections.json'),'--upstream',str(upstream),'--runtime',str(runtime_path),'--output',str(upstream/'review-output')]
    before=snapshot(upstream);start=time.time_ns()
    result=subprocess.run(argv,cwd=REPO,capture_output=True,timeout=60);end=time.time_ns();after=snapshot(upstream)
    (evidence/'stdout.json').write_bytes(result.stdout);(evidence/'stderr.log').write_bytes(result.stderr)
    for name,value in [('before-tree.json',before),('after-tree.json',after)]: (evidence/name).write_text(json.dumps(value,sort_keys=True,indent=2)+'\n')
    record={'schema':'stdo305.containment-execution/1','label':label,'producer_sha256':sha(ENTRY.read_bytes()),'argv':argv,'cwd':str(REPO),'exit_code':result.returncode,'started_ns':start,'ended_ns':end,'private_custody_root':str(private),'runtime_receipt_is_controlled_relocation_of':str(original),'before_tree_sha256':sha((evidence/'before-tree.json').read_bytes()),'after_tree_sha256':sha((evidence/'after-tree.json').read_bytes()),'added':sorted(set(after)-set(before)),'removed':sorted(set(before)-set(after)),'changed':sorted(k for k in before.keys()&after.keys() if before[k]!=after[k]),'stdout_sha256':sha(result.stdout),'stderr_sha256':sha(result.stderr)}
    (evidence/'execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'phase':label,'exit_code':result.returncode,'result':json.loads(result.stdout),'added':record['added'],'changed':record['changed'],'private_custody':str(private)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('label');main(p.parse_args().label)
