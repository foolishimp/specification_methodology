from pathlib import Path
import datetime, hashlib, json, os, subprocess, time
ROOT=Path('/Users/jim/src/apps/specification_methodology')
EVIDENCE=ROOT/'a_c/.ai-workspace/qualification/t008/upstream'
PYTHON=ROOT/'a_c/.venv/bin/python'
BEFORE=json.loads((EVIDENCE/'baseline_subject_before.json').read_text())
ACQUISITION=json.loads((EVIDENCE/'acquisition.json').read_text())
assert ACQUISITION['exact_clean_checkout']
CHECKOUT=Path(ACQUISITION['checkout'])
OVERRIDES={**ACQUISITION['environment_overrides'],'AC_GRAPHIFY_UPSTREAM':str(CHECKOUT),'PYTHONPATH':str(ROOT/'a_c/build_tenants/graphify/test_env'),'PYTHONUNBUFFERED':'1'}
ENV={**os.environ,**OVERRIDES}
STATE={'activation':'T-008-upstream-001','scope':'Existing baseline codec/source-generation/grounding/repair only; no new FD modules qualified','checkout':str(CHECKOUT),'upstream_commit':ACQUISITION['head'],'source_preimages':BEFORE['source_files'],'environment_overrides':OVERRIDES,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'steps':[]}
def hashes():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in BEFORE['source_files']}
def expected():
    return {p:v['sha256'] for p,v in BEFORE['source_files'].items()}
def save():
    (EVIDENCE/'baseline_verification_attempts.json').write_text(json.dumps(STATE,sort_keys=True,indent=2)+'\n')
def run(name,argv,timeout=240):
    assert hashes()==expected(), 'baseline source changed before '+name
    started=datetime.datetime.now(datetime.timezone.utc).isoformat(); clock=time.monotonic()
    try:
        p=subprocess.run(argv,cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
        code=p.returncode; out=p.stdout; err=p.stderr; expired=False
    except subprocess.TimeoutExpired as e:
        code=None; out=e.stdout or b''; err=e.stderr or b''; expired=True
    (EVIDENCE/(name+'.stdout')).write_bytes(out)
    (EVIDENCE/(name+'.stderr')).write_bytes(err)
    STATE['steps'].append({'name':name,'argv':argv,'cwd':str(ROOT),'environment_overrides':OVERRIDES,'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-clock,'returncode':code,'timeout':expired,'stdout':name+'.stdout','stderr':name+'.stderr','stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest(),'source_preimages_unchanged_after':hashes()==expected()}); save()
    print(json.dumps({'step':name,'returncode':code,'timeout':expired,'source_preimages_unchanged':STATE['steps'][-1]['source_preimages_unchanged_after']}),flush=True)
    if code!=0 or not STATE['steps'][-1]['source_preimages_unchanged_after']:
        raise SystemExit(2)
    return out,err
save()
run('08-actual-upstream-checker',[str(PYTHON),str(ROOT/'a_c/build_tenants/graphify/test_env/check_upstream.py'),'--upstream',str(CHECKOUT),'--out',str(EVIDENCE/'actual_upstream_report.json')])
run('09-baseline-unit-tests',[str(PYTHON),'-m','unittest','-v','test_ac_graph','test_ac_generate','test_ac_grounding','test_ac_repair'])
STATE['source_preimages_unchanged_final']=hashes()==expected()
STATE['completed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
STATE['all_execution_steps_passed']=all(s['returncode']==0 and not s['timeout'] and s['source_preimages_unchanged_after'] for s in STATE['steps'])
save()
print(json.dumps({'status':'completed','all_execution_steps_passed':STATE['all_execution_steps_passed'],'checkout':str(CHECKOUT)}),flush=True)
