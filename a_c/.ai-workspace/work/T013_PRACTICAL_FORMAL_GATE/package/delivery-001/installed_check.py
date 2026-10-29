"""One selected installed identity observation and one actual small cold fallback.

The installed reviewed adapter bounds the public CLI at 600 seconds. No source,
origin, proof support, key, or retained input is changed by this launcher.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import os
import platform
import resource
import sys
import time
import types

D = Path(__file__).resolve().parent
T = D.parents[1]
W = Path('/private/tmp/ac-t013-lean-package-001')
INSTALLED = W/'operational/a_c/build_tenants/lean'
GRAPHIFY = W/'operational/a_c/build_tenants/graphify'
PYTHON = Path('/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12')
PYTHON_SHA = 'a7f5b535d61d1c7326824204ac80f045a97a652abb154421e2c74fcc365a3539'
PORTABLE = '07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601'
ORIGIN_PIN = '.cache/formal-origin-v1/selection.json'
BUNDLE = T/'reuse/qualification-001/small-cold'
OUT = D/'installed-small-evidence'


def sha(path):
    with Path(path).open('rb') as stream: return hashlib.file_digest(stream, 'sha256').hexdigest()

def save(name, value):
    with (D/name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def adapter():
    path = GRAPHIFY/'code/ac_formal_gate.py'
    assert sha(path) == 'd37de63f2b809e7a02d88d560b29b4900e8cda6217cfbc32e5796f40065659b8'
    module = types.ModuleType('installed_package_adapter')
    module.__file__ = str(path)
    module.__package__ = ''
    sys.modules[module.__name__] = module
    exec(compile(path.read_bytes(),str(path),'exec',dont_inherit=True),module.__dict__)
    return module

mode = sys.argv[1]
assert mode in ('identity','fallback')
label = 'installed-identity' if mode == 'identity' else 'installed-small-fallback'
record = {'schema':'a_c.T013.installed-package-invocation/1','label':label,
          'started_utc':datetime.now(timezone.utc).isoformat(),'installed_root':str(INSTALLED),
          'outer_seconds':600,'checking_seconds':90,'lean_memory_mb':4096,'physical_rss_cap':False,
          'rss_scope':'Darwin bytes: isolated launcher self peak and cumulative peak over reaped children of this single invocation; child peak is not stage attributed.',
          'measurement_scope':'Whole reviewed adapter invocation through complete CLI exit and final evidence publication; excludes writing this external measurement receipt.'}
started = None
try:
    assert Path(sys.executable).resolve()==PYTHON.resolve() and sha(PYTHON)==PYTHON_SHA
    assert platform.system()+'-'+platform.machine()=='Darwin-arm64'
    assert not (INSTALLED/'.cache/formal-origin-v1').exists()
    manifest=json.loads((D/'SOURCE_PACKAGE.json').read_bytes())
    assert manifest['portable_runtime_identity']['sha256']==PORTABLE
    config=copy.deepcopy(json.loads((T/'package/selection-001/CHECKER.json').read_bytes()))
    config['root']=str(INSTALLED)
    config['runtime_identity']=manifest['portable_runtime_identity']
    config['timeout_seconds']=600
    a=adapter()
    if mode=='identity':
        args=['identity']
    else:
        assert not OUT.exists()
        assert json.loads((D/'installed-identity.stdout').read_bytes())==manifest['portable_runtime_identity']
        assert sha(BUNDLE/'result.json')=='f0a223baff83392913a076ddd47747dfdcf5296fcd1dee32e4c5dac2987e223f'
        old=json.loads((BUNDLE/'result.json').read_bytes())
        assert old['runtime_identity']==manifest['freeze']['runtime_identity']
        assert {k:v for k,v in old['runtime_identity']['pins'].items() if k!=ORIGIN_PIN}==config['runtime_identity']['pins']
        assert set(old['runtime_identity']['pins'])-set(config['runtime_identity']['pins'])=={ORIGIN_PIN}
        args=['check-evidence','--bundle',str(BUNDLE),'--output',str(OUT)]
    record['argv']=[str(PYTHON),'-I','-S','-B','-X','pycache_prefix='+os.devnull,str(INSTALLED/'scripts/formal_gate.py'),*args]
    record['origin_before']='absent (installed metadata only)'
    started=time.monotonic()
    process=a._invoke(config,args)
    record['external_invocation_seconds']=time.monotonic()-started
    record['returncode']=process.returncode
    for suffix,raw in (('stdout',process.stdout),('stderr',process.stderr)):
        with (D/(label+'.'+suffix)).open('xb') as stream:stream.write(raw)
        record[suffix+'_sha256']=sha(D/(label+'.'+suffix))
    result=json.loads(process.stdout)
    record['returned_status']=result.get('status','identity')
    assert process.returncode==0, 'installed CLI did not pass: '+process.stderr.decode()
    if mode=='identity':
        assert result==manifest['portable_runtime_identity']
        save('INSTALLED-CHECKER.json',config)
    else:
        retained=json.loads((OUT/'result.json').read_bytes())
        assert result==retained and result['status']=='verified'
        assert result['runtime_identity']==manifest['portable_runtime_identity']
        assert result['requested_claims']==result['checked_claims']
        observed=result['observations']
        assert observed['records']==6 and observed['reuse'].startswith('none; fresh dynamic obligations')
        assert observed['current_dynamic_proof_invocations']==7
        assert observed['current_kernel_replay_invocations']==1
        assert observed['current_runtime_invocations']==1
        assert observed['limits']=={'timeout_seconds':90,'memory_mb':4096,'max_input_bytes':33554432,'max_selections':64}
        stage_names=[x['stage'] for x in observed['stages']]
        expected=['GateData','GateLocalNames','GateExternalNames','GateIdentities','GateBounds','GateModel','GateViews','dynamic-kernel-replay','actual-runtime']
        assert [x for x in stage_names if x in expected]==expected
        assert all(x.get('exit_code',0)==0 for x in observed['stages'])
        actual=json.loads((OUT/'actual-runtime.log').read_bytes())
        assert len(actual['model']['records'])==6 and len(actual['views'])==1
        assert actual['views'][0]['status']=='verified' and len(actual['views'][0]['projection']['records'])==6
        assert json.loads((OUT/'view-comparison.json').read_bytes())['status']=='equal'
        assert sha(OUT/'supplied-views.json')==sha(BUNDLE/'supplied-views.json')
        assert not (OUT/'local-origin.json').exists()
        assert sha(OUT/'manifest.json')==result['evidence']['manifest_sha256']
        for name,h in result['evidence']['members'].items():assert sha(OUT/name)==h,name
        record['assertions']={'actual_cold_fallback':True,'origin_only_identity_difference':True,'model_records':6,
            'view_records':6,'requested_checked_claims_equal':True,'current_proof_kernel_runtime_invocations':[7,1,1],
            'normal_cold_stages':expected,'supplied_view_exact':True,'private_origin_or_public_hint_created':False}
        record['result_sha256']=sha(OUT/'result.json')
        record['evidence_manifest_sha256']=sha(OUT/'manifest.json')
    assert not (INSTALLED/'.cache/formal-origin-v1').exists()
    record['origin_after']='absent (installed metadata only)'
    record['status']='PASS'
except Exception as exc:
    if started is not None and 'external_invocation_seconds' not in record:
        record['external_invocation_seconds']=time.monotonic()-started
    record['status']='FAIL'
    record['error']=type(exc).__name__+': '+str(exc)
    save('FAILURE.json',{'stage':label,'error':record['error'],'retry':'not attempted'})
finally:
    record['finished_utc']=datetime.now(timezone.utc).isoformat()
    record['launcher_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    record['reaped_children_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    save(label+'.external.json',record)
    print(json.dumps({k:record.get(k) for k in ('label','status','returncode','external_invocation_seconds','launcher_peak_rss_bytes','reaped_children_peak_rss_bytes','result_sha256','error')}),flush=True)
if record['status']!='PASS':raise SystemExit(1)
