from pathlib import Path
import hashlib,importlib.util,json,os,subprocess,sys,time
REPO=Path('/Users/jim/src/apps/specification_methodology');BASE=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/formal-budget-recovery-016';OUT=Path(__file__).resolve().parent
code=REPO/'a_c/build_tenants/graphify/code/ac_formal_gate.py';spec=importlib.util.spec_from_file_location('budget_review_formal',code);adapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(adapter)
old_path=BASE/'OLD_SELECTED_CHECKER.json';old=json.loads(old_path.read_text());request_path=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/representation/repair-002/formal-request.json';request=json.loads(request_path.read_text());output=OUT/'old-selection-prohibited-output'
start=time.monotonic()
try:
 adapter.verify(old,Path(request['input']['path']).read_bytes(),'model',request['selections'],json.loads(Path(request['supplied_views']['path']).read_text()),None,output)
except adapter.GateError as exc:
 refusal={'status':exc.status,'reason':str(exc)}
else:raise AssertionError('stale selector accepted')
assert refusal=={'status':'refused','reason':'Selected checker entry or interpreter changed'} and not output.exists(),refusal
new=OUT/'SELECTED_CHECKER.json';args=[sys.executable,'-B',str(REPO/'a_c/scripts/ac.py'),'formal-select','--lean-root',str(REPO/'a_c/build_tenants/lean'),'--python',sys.executable,'--timeout-seconds','3600','--output',str(new)]
run=subprocess.run(args,cwd=OUT,capture_output=True,timeout=30,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'));(OUT/'selection.stdout').write_bytes(run.stdout);(OUT/'selection.stderr').write_bytes(run.stderr);assert run.returncode==0,run.stderr
selected=json.loads(new.read_text());retained=json.loads((BASE/'SELECTED_CHECKER.json').read_text());assert selected==retained
assert selected['timeout_seconds']==3600 and selected['entry_sha256']=='c84ade91ab388e220de5f0b8d972789e23fcfce14f615bf65e869a60c2b4bcd2'
sys.path.insert(0,str(REPO/'a_c/build_tenants/lean/scripts'));import formal_reuse
assert not formal_reuse.compatible(old['runtime_identity'],selected['runtime_identity'])
result={'old_selection_refusal':refusal,'output_absent':True,'public_selection_argv':args,'public_selection_returncode':run.returncode,'new_selection_equals_retained':True,'selected_outer_timeout_seconds':selected['timeout_seconds'],'changed_runtime_pin_names':[p for p,h in selected['runtime_identity']['pins'].items()if old['runtime_identity']['pins'].get(p)!=h],'old_runtime_portable_compatibility':False,'elapsed_seconds':time.monotonic()-start,'scope':'Actual public selector and supported adapter stale-selection check. Identity source hashing only; no support-population scan or compiler.'};(OUT/'SELECTION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
