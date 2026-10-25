from __future__ import annotations
import copy, hashlib, importlib.util, json, os, pathlib, shutil, subprocess, sys, tempfile, types
sys.dont_write_bytecode=True
BASE=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c')
APP=BASE/'applications/stdo-v3-common-35fb4824'
PROOF=BASE/'.ai-workspace/qualification/t010/package-review'
SCRATCH=pathlib.Path(tempfile.mkdtemp(prefix='ac-common-package-review-'))
os.environ['PYTHONDONTWRITEBYTECODE']='1';os.environ['XDG_CACHE_HOME']=str(SCRATCH/'cache');os.environ['TMPDIR']=str(SCRATCH)
(SCRATCH/'cache').mkdir()
spec=importlib.util.spec_from_file_location('reviewed_packager',APP/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
checks=pkg.checks
closed=json.loads((BASE/'.ai-workspace/qualification/t010/packaging/CLOSED-PREPARATION.json').read_text())
pins=[]
for row in closed['prepared_files']:
 data=(BASE/row['path']).read_bytes();pins.append({'path':row['path'],'matched':len(data)==row['bytes'] and checks.sha(data)==row['sha256']})
assert all(row['matched'] for row in pins)
codec=checks.codec(APP/'build/implementation/code/ac_graph.py')
doc=json.loads((BASE/'build_tenants/graphify/test_env/fixtures/toy_model.json').read_text())
sections=checks.check_sections(APP)
files=[{k:r[k] for k in ('path','sha256','bytes')} for r in checks.load(APP/'source-manifest.json')['files']]
inventory=[{k:r[k] for k in ('id','sha256')} for r in sections]
doc['basis']['subject']={'id':checks.SUBJECT,'sha256':codec.digest(files),'inventory':inventory}
records=[r['id'] for family in doc['populations'].values() for r in family]
old=doc['interpretation']['dispositions'][0]
doc['interpretation']['dispositions']=[{**old,'source':r['id'],'decision':'retained' if i==0 else 'omitted','records':records if i==0 else [],'reason':'Synthetic packaging control only; never a common semantic representation.'} for i,r in enumerate(sections)]
doc['interpretation']['selection_ledger']['sha256']=codec.digest(doc['interpretation']['dispositions'])
doc['interpretation']['source_reentry']['sha256']=codec.digest({'files':files,'sections':inventory})
model=codec.validate(doc)
assert checks.check_model_source(codec,model,APP)==0
proposal=SCRATCH/'synthetic-proposal';proposal.mkdir()
def save(p,o):p.write_text(json.dumps(o,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
save(proposal/'model.json',doc)
carrier=codec.materialize(model).document
save(proposal/'carrier.json',carrier);save(proposal/'graph.json',carrier)
counts={k:len(v) for k,v in doc['populations'].items()}
coverage={'processing_complete':True,'family_counts':counts,'claim':'Synthetic control fixture, not actual common model.'}
save(proposal/'coverage.json',coverage)
result={'processing_complete':True,'model_id':model.identity,'model_sha256':model.sha256,'family_counts':counts,'files':{n:checks.sha((proposal/n).read_bytes()) for n in ['model.json','carrier.json','graph.json','coverage.json']}}
save(proposal/'result.json',result)
public=SCRATCH/'public.json';review=SCRATCH/'review.json'
save(public,{'kind':'synthetic-public-receipt','subject':checks.SUBJECT,'model':{'id':model.identity,'sha256':model.sha256},'claim':'Synthetic packaging fixture only'})
save(review,{'kind':'synthetic-model-review','subject':'urn:other:source','model':{'id':'urn:other:model','sha256':'0'*64},'decision':'unreviewed','claim':'This deliberately does not review the packaged model.'})
upstream=pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
args=types.SimpleNamespace(upstream=upstream,proposal=proposal,graph=proposal/'graph.json',public_evidence=public,review=[review],bundle=SCRATCH/'bundle'/pkg.ARTIFACT,dist=SCRATCH/'dist',display_limit=7)
result=pkg.build(args)
save(PROOF/'first-controls.json',{'scratch':str(SCRATCH),'prepared_pin_checks':pins,'fixture_kind':'synthetic full-source-coordinates toy; not real common model','packaged_model':{'id':model.identity,'sha256':model.sha256},'wrong_review':checks.load(review),'build':result,'finding':'Wrong-subject/wrong-model review entered successfully; bundle replay passed.'})
print(json.dumps({'scratch':str(SCRATCH),'build_status':result['status'],'check_status':result['checks']['status'],'wrong_review_packaged':True,'model':{'id':model.identity,'sha256':model.sha256}},indent=2))
