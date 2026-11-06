import importlib.util,json,sys,tempfile,hashlib,io
from pathlib import Path
from unittest.mock import patch
root=Path('/Users/jim/src/apps/specification_methodology');sys.path[:0]=[str(root/'scripts'),str(root/'tests')]
import check_stack_release as api
fixture=root/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tooling-review-001/source/tests/test_stable_stack_release.py'
spec=importlib.util.spec_from_file_location('frozen_probe_fixtures',fixture);fixtures=importlib.util.module_from_spec(spec);spec.loader.exec_module(fixtures)
fixtures.ROOT=root
EvidenceTests,PublicationTests,put=fixtures.EvidenceTests,fixtures.PublicationTests,fixtures.put
selected=Path(sys.argv[1]);spec=importlib.util.spec_from_file_location('probe_gate',selected);gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
results=[]
def probe(name,fn):
 try: fn(); results.append({'case':name,'accepted':True})
 except Exception as e:results.append({'case':name,'accepted':False,'exception':type(e).__name__,'reason':str(e)})
t=EvidenceTests();t.setUp()
t.result={'status':'verified','version':'3.0.4','source_identity_sha256':'0'*64,'store':'old/store'};r=put(t.root,'run/result.json',t.result);t.record['result']=r;t.record['execution']['outputs']=[r];t.record['execution']['argv']=['python3','tools/qualifier.py','--help'];t.record['execution']['environment']={'version':'3.0.4'};t.record['observations']=[{'pointer':'/status','equals':'verified'}]
probe('S2-installed-help-stale-output',lambda:gate.evidence(t.view,put(t.root,'evidence.json',t.record),'installed_graphify',t.manifest,api))
x=EvidenceTests();x.setUp();result,record=x.lean();result['requested_claims']=result['checked_claims']=['unrelated-trivial-claim'];result['runtime_identity']={'pins':{'lean':'unknown-old-runtime'}};result['evidence']={'members':[{'path':'GateModel.olean','sha256':'0'*64}]};rr=put(x.root,'run/lean.json',result);record['result']=rr;record['execution']['outputs']=[rr]
probe('S2-lean-trivial-missing-proof-unknown-runtime',lambda:gate.evidence(x.view,put(x.root,'evidence.json',record),'exact_candidate_lean_result',x.manifest,api))
p=PublicationTests();p.setUp();p.remote['refs/tags/v3.0.5-rc.1']='9'*40;p.manifest['publication']['preserved_immutable_refs']['refs/tags/v3.0.5-rc.1']='9'*40
probe('S3-bare-same-version-RC-preserved',lambda:gate.ref_graph(p.root,p.manifest,p.carrier,'refs','origin',p.adapter))
v=EvidenceTests();v.setUp();v.manifest['native']={'manifest':{'sha256':'a'*64}};v.record['claim']='complete_installed_cohort';v.result={'status':'verified','version':'3.0.4','installed_manifest_sha256':'0'*64,'store':'old/store'};rr=put(v.root,'run/result.json',v.result);v.record['result']=rr;v.record['execution']['outputs']=[rr];v.record['observations']=[{'pointer':'/status','equals':'verified'}];ev=put(v.root,'evidence.json',v.record)
base='https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5/'
asset={'name':'manager.whl','url':base+'manager.whl',**put(v.root,'assets/manager.whl',b'wheel')};v.manifest['publication']['assets']=[asset];raw=api.canonical_json_bytes(v.manifest);put(v.root,'frozen.json',raw);external=v.manifest['publication']['external_manifest_asset'];receipt={'kind':'stdo.public-cohort-readback/1','status':'verified','source_identity_sha256':v.manifest['source']['source_identity_sha256'],'unauthenticated':True,'assets':[asset],'fresh_store':'new/fresh/store','installed_manifest_sha256':'a'*64,'external_manifest':{**external,'sha256':api.sha256(raw)},'installed_qualification':ev};ref=put(v.root,'readback.json',receipt)
def public():
 with patch.object(gate.urllib.request,'urlopen',side_effect=[io.BytesIO(b'wheel'),io.BytesIO(raw)]):gate.public(v.view,v.manifest,'frozen.json',ref['path'],ref['sha256'],api)
probe('S2-public-single-asset-single-product-old-store',public)
print(json.dumps({'subject':str(selected),'subject_sha256':api.sha256(selected.read_bytes()),'cases':results},indent=2))
for o in(t,x,p,v):o.tmp.cleanup()
