from __future__ import annotations
from collections import defaultdict
import copy,hashlib,importlib.util,json,pathlib,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';P=B/'.ai-workspace/qualification/t010/package-review/final-003';ART='a_c-stdo-v3-common-35fb4824'
phase=json.loads((P/'phase-001.json').read_text());S=pathlib.Path(phase['scratch']);E=pathlib.Path(phase['extracted']);env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')};python='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';controls=[]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while block:=f.read(1024*1024):h.update(block)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
def check(name,ok,expected=None,observed=None):
 controls.append({'name':name,'passed':bool(ok),'expected':expected,'observed':observed});save(P/'phase-002-progress.json',{'controls':controls,'scratch':str(S)})
 if not ok:raise AssertionError(name)
def run(label,root,argv,expected=2):
 start=time.monotonic();p=subprocess.run([python,'-S','-B',*argv],cwd=root,env=env,capture_output=True,text=True);log={'argv':[python,'-S','-B',*argv],'cwd':str(root),'returncode':p.returncode,'elapsed_seconds':time.monotonic()-start,'stdout':p.stdout,'stderr':p.stderr};save(P/'commands'/f'{label}.json',log);check(label,p.returncode==expected,expected=expected,observed={'returncode':p.returncode,'stderr':p.stderr[:1500]});return p
# Independently compute the documented governing closure for the already executed public selection.
spec=importlib.util.spec_from_file_location('final_tamper_exact_codec',E/'codec/ac_graph.py');ac=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ac;spec.loader.exec_module(ac)
doc=json.loads((E/'model.json').read_text());model=ac.validate(doc);projection=json.loads((S/'projection.json').read_text());dependency=defaultdict(set);required=set(doc['dependency_contract']['required_relation_kinds'])
for ref in model.references:
 if ref.target in model.records and ref.schema['governing']:dependency[ref.owner].add(ref.target)
for record in model.records.values():
 r=record.fields
 if record.family=='relations' and r['kind'] in required:dependency[r['source']].update([record.identity,r['target']])
 if record.family in doc['dependency_contract']['attachment_families']:
  targets=[r['subject']] if record.family=='residuals' else r['applies_to']
  for target in targets:
   if target in model.records:dependency[target].add(record.identity)
expected=set(projection['selection']['seeds']);pending=list(expected)
while pending:
 current=pending.pop()
 for target in dependency[current]-expected:expected.add(target);pending.append(target)
check('actual-public-projection-complete-declared-finite-closure',set(projection['included'])==expected and set(projection['excluded'])==set(model.records)-expected and projection['populations']=={family:[r for r in rows if r['id'] in expected] for family,rows in doc['populations'].items()},observed={'included':len(expected),'seeds':projection['selection']['seeds']})
# The actual full-carrier decoder must reject a contradictory derived display field.
carrier=json.loads((E/'carrier.json').read_text());record=next(n for n in carrier['nodes'] if n.get('ac_role')=='record');record['label']+=' [altered by bounded reviewer tamper control]';tampered=S/'tampered-carrier.json';save(tampered,carrier);unexpected=S/'unexpected-tampered-recovery.json'
run('actual-carrier-derived-label-tamper-refused',E,['codec/ac_graph.py','decode',str(tampered),'--out',str(unexpected)])
check('tampered-carrier-does-not-create-output',not unexpected.exists())
# Ordinary checksum repair cannot change fixed source or exact receipt bindings.
def reindex(root):
 names=sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name not in ('inventory.json','SHA256SUMS'))
 inv=json.loads((root/'inventory.json').read_text());inv['files']=[{'path':n,'bytes':(root/n).stat().st_size,'sha256':sha(root/n)} for n in names];save(root/'inventory.json',inv)
 (root/'SHA256SUMS').write_text(''.join(f'{sha(root/n)}  {n}\n' for n in sorted(names+['inventory.json'])))
sourcecase=S/'tamper-source-reindexed';shutil.copytree(E,sourcecase);member=sourcecase/'source/standards/ACTIVATION.md';member.write_bytes(member.read_bytes()+b'\nReviewer controlled source tamper.\n');reindex(sourcecase)
run('actual-source-tamper-refused-after-inventory-reindex',sourcecase,['release_tools/bundle_check.py','.'])
receiptcase=S/'tamper-review-reindexed';shutil.copytree(E,receiptcase);path=receiptcase/'evidence/reviews/review-001/receipt.json';receipt=json.loads(path.read_text());receipt['bindings']['model']['sha256']='0'*64;save(path,receipt);release=json.loads((receiptcase/'RELEASE.json').read_text());release['review_receipts'][0]['sha256']=sha(path);save(receiptcase/'RELEASE.json',release);reindex(receiptcase)
print(json.dumps({'progress':'Actual projection/carrier tamper/source reindexed tamper passed; actual wrong-model receipt with refreshed outer hashes now running','controls_passed':len(controls)}),flush=True)
run('actual-wrong-model-review-refused-after-release-and-inventory-reindex',receiptcase,['release_tools/bundle_check.py','.'])
# Re-enter every named immutable subject and all preexisting source/study guards.
seal=json.loads((B/'.ai-workspace/qualification/t010/build/construction-artifacts-sealed.json').read_text());check('sealed-five-raw-artifacts-unchanged-after-review',all((A/'run/repaired-proposal'/n).stat().st_size==r['bytes'] and sha(A/'run/repaired-proposal'/n)==r['sha256'] and sha(E/n)==r['sha256'] for n,r in seal['artifacts'].items()))
act=json.loads((P/'ACTIVATION.json').read_text());check('named-code-pins-unchanged-after-review',all(sha(A/r['path'])==r['expected'] for r in act['frozen_subjects']))
source=json.loads((A/'package-custody.json').read_text());check('source-eightyone-members-unchanged-after-review',all(sha(A/'source'/r['path'])==r['sha256'] for r in source['members']))
guard=json.loads((B/'.ai-workspace/qualification/t010/packaging/initial-guards.json').read_text());bad=[]
for r in guard['guarded_files']:
 p=B/r['path']
 if not p.is_file() or p.stat().st_size!=r['bytes'] or sha(p)!=r['sha256']:bad.append(r['path'])
check('all4296-preexisting-source-study-guards-conserved-after-review',not bad,observed={'guarded_files':len(guard['guarded_files']),'mismatches':bad})
verification=json.loads((B/'.ai-workspace/qualification/t010/packaging/final-001/verified-inputs-and-guards.json').read_text());trackedbad=[]
for r in verification['preexisting_tracked_modifications']:
 p=B.parent/r['path']
 if not p.is_file() or p.stat().st_size!=r['bytes'] or sha(p)!=r['sha256']:trackedbad.append(r['path'])
check('preexisting-tracked-modified-bytes-conserved',not trackedbad,observed={'entries':len(verification['preexisting_tracked_modifications']),'mismatches':trackedbad})
archive=A/'dist'/f'{ART}.tar.gz';check('exact-frozen-archive-size-and-sha-unchanged',archive.stat().st_size==10087425 and sha(archive)=='2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386',observed={'bytes':archive.stat().st_size,'sha256':sha(archive)})
live=A/'bundle'/ART;names=sorted(p.relative_to(E).as_posix() for p in E.rglob('*') if p.is_file());check('baseline-extraction-and-live-bundle-unchanged',names==sorted(p.relative_to(live).as_posix() for p in live.rglob('*') if p.is_file()) and all(sha(E/n)==sha(live/n) for n in names),observed={'files':len(names)})
save(P/'phase-002.json',{'status':'passed','controls':controls,'controls_passed':len(controls),'scratch':str(S),'actual_artifact_tamper_cases':3,'finding':None,'timing_scope':'Observed times describe these checks only; no benchmark or efficiency inference','interactive_behavior':'unverified; browser/server not used'});print(json.dumps({'status':'passed','controls_passed':len(controls),'actual_tamper_cases':3,'findings':[]}))
