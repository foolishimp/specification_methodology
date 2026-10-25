from __future__ import annotations
import copy,hashlib,importlib.util,json,os,pathlib,shutil,subprocess,sys,tarfile,tempfile,types
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';P=B/'.ai-workspace/qualification/t010/package-review';D=P/'delta-001'
old=json.loads((P/'first-controls.json').read_text());proposal=pathlib.Path(old['scratch'])/'synthetic-proposal';S=pathlib.Path(tempfile.mkdtemp(prefix='ac-common-package-review-'))
os.environ['PYTHONDONTWRITEBYTECODE']='1';os.environ['TMPDIR']=str(S);os.environ['XDG_CACHE_HOME']=str(S/'cache');(S/'cache').mkdir()
spec=importlib.util.spec_from_file_location('delta_packager',A/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
c=pkg.checks;r=pkg.receipts;ac=c.codec(A/'build/implementation/code/ac_graph.py');model=ac.validate(ac.read_json(proposal/'model.json'))
assert model.sha256==old['packaged_model']['sha256']
def save(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
source=json.loads((A/'source-manifest.json').read_text());custody=json.loads((A/'package-custody.json').read_text());inventory=model.document['basis']['subject']['inventory']
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
expected={'source':{'subject_id':c.SUBJECT,'commit':'35fb4824a064a84df5af214a0d0e2da597c18ac6','package_tree':'7f2070b61c848b42b4dfb3af1e0ce53869de1aa1','source_manifest_sha256':sha(A/'source-manifest.json'),'semantic_files_sha256':digest([{k:row[k] for k in ['path','sha256','bytes']} for row in source['files']]),'section_inventory_sha256':digest(inventory),'source_reentry_sha256':digest({'files':[{k:row[k] for k in ['path','sha256','bytes']} for row in source['files']],'sections':inventory})},'model':{'id':model.identity,'sha256':model.sha256},'artifacts':{n:{'bytes':(proposal/n).stat().st_size,'sha256':sha(proposal/n)} for n in ['model.json','carrier.json','graph.json','coverage.json','result.json']}}
assert r.expected_bindings(A,model,{n:proposal/n for n in r.ARTIFACTS})==expected
construction={'kind':r.CONSTRUCTION,'receipt_id':'urn:reviewer:synthetic:construction','issuer':'urn:reviewer:synthetic:constructor','bindings':expected,'scope':'Synthetic packaging contract control only; not the common semantic model.','details':{'fixture':'Conserved14record toy; exact common source coordinates; no semantic-fitness claim.'},'construction_state':'complete','private_material_included':False}
report=S/'inputs/reports/assessment.md';report.parent.mkdir(parents=True);report.write_text('Synthetic bounded review found a deliberately failed fixture. No acceptance.\n')
review={'kind':r.REVIEW,'receipt_id':'urn:reviewer:synthetic:review','issuer':'urn:reviewer:synthetic:assessor','bindings':expected,'scope':'Synthetic binding control; no actual common semantic review.','details':{'assessment':'Changes requested: deliberately failed synthetic semantic case.','not_acceptance':True},'review_state':'closed','outcome':'changes_requested','independence':{'relation':'nonauthor of packager; no provider-family independence claimed'},'reports':[{'path':'reports/assessment.md','bytes':report.stat().st_size,'sha256':sha(report)}]}
public=S/'inputs/construction.json';reviewpath=S/'inputs/review.json';save(public,construction);save(reviewpath,review)
upstream=pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
def args(label,pub=public,reviews=None):return types.SimpleNamespace(upstream=upstream,proposal=proposal,graph=proposal/'graph.json',public_evidence=pub,review=[reviewpath] if reviews is None else reviews,bundle=S/(label+'-bundle')/pkg.ARTIFACT,dist=S/(label+'-dist'),display_limit=7)
controls=[]
def record(name,ok,details=None):controls.append({'name':name,'passed':ok,'details':details});assert ok,name
positive=pkg.build(args('positive'));record('constructor-accepts-exact-bound-failed-review-without-acceptance',positive['checks']['status']=='passed',positive['checks']['public_evidence'])
bundle=pathlib.Path(positive['bundle']);release=c.load(bundle/'RELEASE.json');record('failed-outcome-preserved',c.load(bundle/'evidence/reviews/review-001/receipt.json')['outcome']=='changes_requested' and release['semantic_acceptance']=='not_issued')
originalwrong=pathlib.Path(old['scratch'])/'review.json'
try:pkg.build(args('original-wrong',reviews=[originalwrong]));ok=False;reason='accepted'
except (ValueError,KeyError,TypeError,OSError) as e:ok=True;reason=str(e)
record('original-untyped-wrong-model-review-refused',ok,reason)
# Make every changed coordinate independently stale while retaining all unaffected fields.
cases=[]
for field in expected['source']:
 v=copy.deepcopy(review);v['bindings']['source'][field]='urn:other:source' if field=='subject_id' else '0'*len(expected['source'][field]);cases.append(('review-source-'+field,v))
for field in expected['model']:
 v=copy.deepcopy(review);v['bindings']['model'][field]='urn:other:model' if field=='id' else '0'*64;cases.append(('review-model-'+field,v))
for artifact in expected['artifacts']:
 for field in ['bytes','sha256']:
  v=copy.deepcopy(review);v['bindings']['artifacts'][artifact][field]=0 if field=='bytes' else '0'*64;cases.append(('review-artifact-'+artifact+'-'+field,v))
for name,mutate in [('wrong-kind',lambda v:v.update(kind=r.CONSTRUCTION)),('unfinished-review',lambda v:v.update(review_state='active')),('duplicate-report-path',lambda v:v['reports'].append(copy.deepcopy(v['reports'][0]))),('missing-bound-report',lambda v:v['reports'][0].update(path='missing.md')),('stale-report-digest',lambda v:v['reports'][0].update(sha256='0'*64)),('duplicate-construction-identity',lambda v:v.update(receipt_id=construction['receipt_id']))]:
 v=copy.deepcopy(review);mutate(v);cases.append((name,v))
for name,v in cases:
 path=S/'inputs'/('case-'+name+'.json');save(path,v)
 try:pkg.build(args(name,reviews=[path]));ok=False;reason='accepted'
 except (ValueError,KeyError,TypeError,OSError) as e:ok=True;reason=str(e)
 record('constructor:'+name,ok,reason)
# Wrong construction bindings and missing/duplicate receipt controls.
for name,kind in [('wrong-construction-model','model'),('wrong-construction-source','source')]:
 v=copy.deepcopy(construction);v['bindings'][kind]['id' if kind=='model' else 'subject_id']='urn:other:identity';path=S/'inputs'/(name+'.json');save(path,v)
 try:pkg.build(args(name,pub=path));ok=False;reason='accepted'
 except (ValueError,KeyError,TypeError,OSError) as e:ok=True;reason=str(e)
 record('constructor:'+name,ok,reason)
for name,reviews in [('missing-review',[]),('duplicate-review',[reviewpath,reviewpath])]:
 try:pkg.build(args(name,reviews=reviews));ok=False;reason='accepted'
 except (ValueError,KeyError,TypeError,OSError) as e:ok=True;reason=str(e)
 record('constructor:'+name,ok,reason)
python='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')}
archive=S/'positive-dist'/f'{pkg.ARTIFACT}.tar.gz';ex=S/'extracted';ex.mkdir()
with tarfile.open(archive) as tar:tar.extractall(ex,filter='data')
extracted=ex/pkg.ARTIFACT
p=subprocess.run([python,'-S','-B',str(extracted/'release_tools/bundle_check.py'),'.'],cwd=extracted,env=env,capture_output=True,text=True);record('clean-extracted-stdlib-replay',p.returncode==0,{'stdout':p.stdout,'stderr':p.stderr})
second=pkg.archive(bundle,S/'second.tar.gz');record('repaired-recipe-deterministic',archive.read_bytes()==(S/'second.tar.gz').read_bytes(),second)
def refresh(root):
 rel=c.load(root/'RELEASE.json');path=root/'evidence/authoring-public.json';rel['public_authoring_receipt_sha256']=sha(path)
 for row in rel['review_receipts']:
  p=root/row['path'];row['sha256']=sha(p)
 save(root/'RELEASE.json',rel)
 rows=[{'path':name,'bytes':(root/name).stat().st_size,'sha256':sha(root/name)} for name in c.files(root) if name not in ['inventory.json','SHA256SUMS']]
 inv=c.load(root/'inventory.json');inv['files']=rows;save(root/'inventory.json',inv)
 (root/'SHA256SUMS').write_text(''.join(f'{sha(root/name)}  {name}\n' for name in sorted([r['path'] for r in rows]+['inventory.json'])))
portable=[]
for name,v in cases:portable.append((name,'review',v))
portable.extend([('original-untyped-wrong-model','review',json.loads(originalwrong.read_text())),('untyped-construction','construction',{'not':'a typed receipt'}),('wrong-construction-model','construction',{**construction,'bindings':{**expected,'model':{'id':'urn:other:model','sha256':'0'*64}}})])
for index,(name,target,value) in enumerate(portable):
 root=S/'portable'/str(index);shutil.copytree(extracted,root);path=root/('evidence/reviews/review-001/receipt.json' if target=='review' else 'evidence/authoring-public.json');save(path,value);refresh(root)
 p=subprocess.run([python,'-S','-B',str(root/'release_tools/bundle_check.py'),'.'],cwd=root,env=env,capture_output=True,text=True);record('portable-reindexed:'+name,p.returncode==2,p.stderr.strip())
for index,mode in enumerate(['changed-readable-report','missing-readable-report','missing-review-index','duplicate-review-index','extra-unbound-file']):
 root=S/'portable-extra'/str(index);shutil.copytree(extracted,root)
 if mode=='changed-readable-report':(root/'evidence/reviews/review-001/reports/assessment.md').write_text('Changed after review; inventory deliberately refreshed.\n')
 elif mode=='missing-readable-report':(root/'evidence/reviews/review-001/reports/assessment.md').unlink()
 elif mode=='missing-review-index':
  rel=c.load(root/'RELEASE.json');rel['review_receipts']=[];save(root/'RELEASE.json',rel)
 elif mode=='duplicate-review-index':
  rel=c.load(root/'RELEASE.json');rel['review_receipts'].append(copy.deepcopy(rel['review_receipts'][0]));save(root/'RELEASE.json',rel)
 else:(root/'evidence/unbound.txt').write_text('Unbound public evidence.\n')
 refresh(root);p=subprocess.run([python,'-S','-B',str(root/'release_tools/bundle_check.py'),'.'],cwd=root,env=env,capture_output=True,text=True);record('portable-reindexed:'+mode,p.returncode==2,p.stderr.strip())
# Original13-obligation oracle is conserved; only changed bindings and affected replay evaluated.
activation=json.loads((D/'ACTIVATION.json').read_text());post=[]
for row in activation['frozen_subjects']:post.append({'path':row['path'],'matched':sha(A/row['path'])==row['expected']})
assert all(row['matched'] for row in post)
result={'status':'passed','stage':'frozen-binding-repair-delta','scratch':str(S),'synthetic_model':{'id':model.identity,'sha256':model.sha256},'controls':controls,'controls_passed':len(controls),'original_F001_counterexample':'now refused by constructor and portable checker even after ordinary index/inventory refresh','frozen_post_checks':post,'actual_common_model_bundle_reviewed':False,'interactive_behavior':'unverified; no browser or server effects','findings':[]}
save(D/'controls.json',result);print(json.dumps({'status':result['status'],'controls_passed':len(controls),'scratch':str(S),'findings':[]}))
