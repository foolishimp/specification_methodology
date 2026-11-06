from pathlib import Path
import hashlib, importlib.util, json, sys, time
REPO=Path('/Users/jim/src/apps/specification_methodology')
WORK=Path(__file__).resolve().parent
LEAN=REPO/'a_c/build_tenants/lean'
sys.path.insert(0,str(LEAN/'scripts'))
import formal_support, formal_gate
path=REPO/'a_c/build_tenants/graphify/code/ac_formal_gate.py'
spec=importlib.util.spec_from_file_location('selected_graphify_formal_adapter',path)
adapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(adapter)
def ref(path):
 path=Path(path);raw=path.read_bytes()
 return {'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
config=json.loads((WORK/'OLD_SELECTED_CHECKER.json').read_text())
request_path=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/representation/repair-002/formal-request.json'
request=json.loads(request_path.read_text());model=Path(request['input']['path']);views=Path(request['supplied_views']['path'])
output=WORK/'old-selection-prohibited-output'
assert not output.exists()
start=time.time_ns()
try:
 adapter.verify(config,model.read_bytes(),'model',request['selections'],json.loads(views.read_text()),None,output)
except adapter.GateError as exc:
 observed={'status':exc.status,'reason':str(exc)}
else: raise AssertionError('old selection was accepted')
assert observed['status']=='refused' and 'changed' in observed['reason'],observed
assert not output.exists()
old={'schema':'stdo305.old-selection-refusal/1','selection':ref(WORK/'OLD_SELECTED_CHECKER.json'),'adapter':ref(path),'request':ref(request_path),'input':ref(model),'views':ref(views),'output':str(output),'output_absent':not output.exists(),'observed':observed,'elapsed_seconds':(time.time_ns()-start)/1e9,'standing':'Actual supported Graphify formal verify API refused the selected pre-change checker before output creation or compiler invocation.'}
(WORK/'OLD_SELECTION_REFUSAL.json').write_text(json.dumps(old,sort_keys=True,indent=2)+'\n')
print(json.dumps(old),flush=True)
start=time.time_ns();checked=formal_support.check();elapsed=(time.time_ns()-start)/1e9
current=formal_gate.runtime_identity()
oldpins=config['runtime_identity']['pins'];newpins=current['pins']
changes=[{'path':name,'before':oldpins.get(name),'after':newpins.get(name)} for name in sorted(oldpins.keys()|newpins.keys()) if oldpins.get(name)!=newpins.get(name)]
assert [r['path'] for r in changes]==['scripts/formal_gate.py'],changes
profile=json.loads(formal_support.SUPPORT.read_text())
assert not any('scripts/formal_gate.py'==name for name in profile['members'])
result={'schema':'stdo305.current-compiled-support-check/1','support_helper':ref(LEAN/'scripts/formal_support.py'),'support':ref(formal_support.SUPPORT),'result':checked,'elapsed_seconds':elapsed,'runtime_identity':current,'previous_runtime_identity':config['runtime_identity']['sha256'],'runtime_changes':changes,'support_reestablished':False,'standing':'Actual full selected compiled-support/member/import-population check. Existing compiled support is unchanged; only the formal gate Python source pin changed. This is not a new mathematical proof.'}
(WORK/'SUPPORT_CURRENTNESS.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
(WORK/'RUNTIME_IDENTITY.json').write_text(json.dumps(current,sort_keys=True,indent=2)+'\n')
print(json.dumps({'support':checked,'elapsed_seconds':elapsed,'runtime_identity':current['sha256'],'changes':changes}),flush=True)
