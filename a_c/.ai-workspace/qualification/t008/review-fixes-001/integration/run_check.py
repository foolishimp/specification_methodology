from __future__ import annotations
import hashlib,importlib.metadata,json,os,pathlib,platform,subprocess,sys,time
P=pathlib.Path(__file__).resolve().parent
INTEGRATION=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/review-fixes-001/integration')
PRODUCT=P/'snapshot/a_c';TENANT=PRODUCT/'build_tenants/graphify'
PYTHON=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c/.venv/bin/python')
UPSTREAM=pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
name=sys.argv[1];folder=INTEGRATION/name;folder.mkdir()
TMP=P/name;TMP.mkdir()
ENV=dict(os.environ)
for key in ('A_C_CORE_QUALIFICATION_CUSTODY','AC_SUPPORT_EFFECTS_PROOF_ROOT','AC_PUBLIC_INTERFACE_TEST_EVIDENCE','AC_ACTOR_TRANSPORT_TEST_EVIDENCE'):ENV.pop(key,None)
ENV.update({'PYTHONDONTWRITEBYTECODE':'1','PYTHONPYCACHEPREFIX':str(TMP/'pycache'),'TMPDIR':str(TMP),'TMP':str(TMP),'TEMP':str(TMP),'XDG_CACHE_HOME':str(TMP/'cache'),'MYPY_CACHE_DIR':str(TMP/'mypy-cache'),'MYPYPATH':str(TENANT/'code')+':'+str(TENANT/'test_env'),'AC_GRAPHIFY_UPSTREAM':str(UPSTREAM),'GIT_OPTIONAL_LOCKS':'0'})
if name=='suite':
    ENV.update({'A_C_CORE_QUALIFICATION_CUSTODY':str(P/'custody-core'),'AC_SUPPORT_EFFECTS_PROOF_ROOT':str(P/'custody-effects'),'AC_PUBLIC_INTERFACE_TEST_EVIDENCE':str(P/'custody-public'),'AC_ACTOR_TRANSPORT_TEST_EVIDENCE':str(P/'custody-actor')})
    command=[str(PYTHON),'-B','-m','unittest','discover','-s',str(TENANT/'test_env'),'-p','test_*.py','-v']
elif name=='strict9':
    selected=['code/ac_support.py','code/ac_support_core.py','code/ac_support_effects.py','test_env/test_ac_support_core.py','test_env/test_ac_support_effects.py','test_env/test_ac_support_interfaces.py','examples/fd-support/prepare_readonly.py','examples/fd-support/actor_cli.py','test_env/support_fixtures/local_actor.py']
    command=[str(PYTHON),'-B','-m','mypy','--strict','--cache-dir',str(TMP/'mypy-cache'),*[str(TENANT/path) for path in selected]]
elif name=='compatibility9':
    command=[str(PYTHON),'-B',str(TENANT/'test_env/check_upstream.py'),'--upstream',str(UPSTREAM),'--out',str(folder/'report.json')]
else:raise ValueError(name)
wrapped=['/usr/bin/sandbox-exec','-f',str(P/'readonly-offline.sb'),*command]
selected_keys=('PYTHONDONTWRITEBYTECODE','PYTHONPYCACHEPREFIX','TMPDIR','TMP','TEMP','XDG_CACHE_HOME','MYPY_CACHE_DIR','MYPYPATH','AC_GRAPHIFY_UPSTREAM','GIT_OPTIONAL_LOCKS','A_C_CORE_QUALIFICATION_CUSTODY','AC_SUPPORT_EFFECTS_PROOF_ROOT','AC_PUBLIC_INTERFACE_TEST_EVIDENCE','AC_ACTOR_TRANSPORT_TEST_EVIDENCE')
record={'name':name,'cwd':str(PRODUCT),'command':command,'wrapper':wrapped,'selected_environment':{key:ENV[key] for key in selected_keys if key in ENV},'source_snapshot_manifest':str(INTEGRATION/'source-before.json'),'sandbox_profile_sha256':hashlib.sha256((P/'readonly-offline.sb').read_bytes()).hexdigest(),'started_ns':time.time_ns(),'repetitions':1}
(folder/'command.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
with (folder/'stdout').open('wb') as out,(folder/'stderr').open('wb') as err:
    try:
        run=subprocess.run(wrapped,cwd=PRODUCT,env=ENV,stdout=out,stderr=err,timeout=300,check=False);record['returncode']=run.returncode
    except subprocess.TimeoutExpired:
        record['returncode']=124;record['timeout']=True
record['ended_ns']=time.time_ns();record['elapsed_seconds']=(record['ended_ns']-record['started_ns'])/1e9
(folder/'execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
print(json.dumps({'name':name,'exit':record['returncode'],'elapsed_seconds':record['elapsed_seconds'],'raw_evidence':str(folder)}),flush=True)
raise SystemExit(record['returncode'])
