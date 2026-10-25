from __future__ import annotations
import copy,hashlib,importlib.util,json,os,pathlib,re,shutil,subprocess,sys,tarfile,tempfile,types
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';P=B/'.ai-workspace/qualification/t010/package-review';D=P/'documentation-002'
prior=json.loads((P/'delta-001/controls.json').read_text());old=pathlib.Path(prior['scratch']);first=json.loads((P/'first-controls.json').read_text());proposal=pathlib.Path(first['scratch'])/'synthetic-proposal';S=pathlib.Path(tempfile.mkdtemp(prefix='ac-common-package-review-'))
os.environ['PYTHONDONTWRITEBYTECODE']='1';os.environ['TMPDIR']=str(S);os.environ['XDG_CACHE_HOME']=str(S/'cache');(S/'cache').mkdir()
spec=importlib.util.spec_from_file_location('docs_delta_packager',A/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
c=pkg.checks
public=old/'inputs/construction.json';review=old/'inputs/review.json';upstream=pathlib.Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':ok,'detail':detail});assert ok,name
bindings=pkg.receipt_bindings(types.SimpleNamespace(proposal=proposal,graph=proposal/'graph.json'))
check('receipt-bindings-unchanged',bindings['bindings']==json.loads(public.read_text())['bindings'])
args=types.SimpleNamespace(upstream=upstream,proposal=proposal,graph=proposal/'graph.json',public_evidence=public,review=[review],bundle=S/'bundle'/pkg.ARTIFACT,dist=S/'dist',display_limit=7)
result=pkg.build(args);check('exact-bound-positive-failed-review-remains-accepted',result['checks']['status']=='passed')
archive=S/'dist'/f'{pkg.ARTIFACT}.tar.gz';ex=S/'extracted';ex.mkdir()
with tarfile.open(archive) as tar:tar.extractall(ex,filter='data')
e=ex/pkg.ARTIFACT;text=(e/'SOURCE-READINESS.md').read_text();original=(A/'SOURCE-READINESS.md').read_text()
check('original-workspace-readiness-conserved',sha(A/'SOURCE-READINESS.md')=='114a4580a344daa1cf32bcbc19246ab189c26b3f50b58d47c105ae7a2b54bd1d')
check('portable-label-hash-and-route-explicit','captured-workspace projection' in text and '114a4580a344daa1cf32bcbc19246ab189c26b3f50b58d47c105ae7a2b54bd1d' in text and 'python3 -B release_tools/bundle_check.py .' in text)
check('original-helper-commands-explicitly-unavailable','unavailable in this archive' in text and 'workspace-only records, not commands' in text and not (e/'freeze_sources.py').exists())
# Recover the originating source account by undoing only four explicitly scoped navigation edits.
first_body='\n\nThe complete common candidate'
assert first_body in original and first_body in text
recovered=original.split(first_body,1)[0]+first_body+text.split(first_body,1)[1]
oldstart='## Reproduce the custody checks';newstart='## Originating-workspace custody checks';after=' The second re-enters the fixed source and payload'
old_navigation=original[original.index(oldstart):original.index(after)]
recovered=recovered[:recovered.index(newstart)]+old_navigation+recovered[recovered.index(after):]
recovered=recovered.replace('`a_c/.ai-workspace/qualification/t010/source/` (external originating-workspace custody route; not included in this archive)','[the source proof](../../.ai-workspace/qualification/t010/source/)')
recovered=recovered.replace('`a_c/.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md` (external originating-workspace ticket route; not included in this archive)','[T-010](../../.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md)')
check('all-source-facts-and-open-gates-byte-preserved-outside-navigation',recovered==original)
links=[]
for target in re.findall(r'\]\(([^)]+)\)',text):
 p=(e/target.split('#',1)[0]).resolve();links.append({'target':target,'exists':p.exists(),'within_bundle':p.is_relative_to(e.resolve())})
check('all-six-local-markdown-links-resolve',len(links)==6 and all(r['exists'] and r['within_bundle'] for r in links),links)
check('workspace-proof-ticket-hyperlinks-removed','](../../.ai-workspace' not in text and text.count('external originating-workspace')==2)
python='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')}
p=subprocess.run([python,'-S','-B','release_tools/bundle_check.py','.'],cwd=e,env=env,capture_output=True,text=True)
check('advertised-portable-check-runs-after-clean-extraction',p.returncode==0,{'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
readiness=(e/'README.md').read_text();check('top-level-guide-explains-captured-workspace-scope','labelled captured-workspace documentation projection' in readiness and 'explicitly workspace-only' in readiness)
raw=json.loads(review.read_text());raw['bindings']['source']['subject_id']='urn:other:source';wrong=S/'wrong-source-review.json';save(wrong,raw);bad=copy.copy(args);bad.review=[wrong];bad.bundle=S/'bad-bundle'/pkg.ARTIFACT;bad.dist=S/'bad-dist'
try:pkg.build(bad);ok=False;reason='accepted'
except (ValueError,KeyError,TypeError,OSError) as x:ok=True;reason=str(x)
check('wrong-source-review-still-refused-before-output',ok and not bad.bundle.exists(),reason)
pkg.archive(pathlib.Path(result['bundle']),S/'repeat.tar.gz');check('deterministic-archive-bytes',archive.read_bytes()==(S/'repeat.tar.gz').read_bytes())
closure=json.loads((B/'.ai-workspace/qualification/t010/packaging/documentation-repair-001/CLOSED.json').read_text());guard=[{'path':r['path'],'matched':sha(A/r['path'])==r['sha256']} for r in closure['unchanged_bindings_checker_and_contract']];check('three-manifests-and-helper-checker-contract-pins-conserved',all(r['matched'] for r in guard),guard)
custody=json.loads((A/'package-custody.json').read_text());check('all-eightyone-source-files-exact',len(custody['members'])==81 and all(sha(A/'source'/r['path'])==r['sha256'] and sha(e/'source'/r['path'])==r['sha256'] for r in custody['members']))
check('private-proof-and-ticket-not-copied',not any('.ai-workspace' in pathlib.PurePosixPath(f).parts for f in c.files(e)))
act=json.loads((D/'ACTIVATION.json').read_text());check('frozen-doc-subject-pins-still-exact',all(sha(A/r['path'])==r['expected'] for r in act['frozen_subjects']))
save(D/'controls.json',{'status':'passed','scope':'F002 frozen docs-only delta, conserved synthetic fixture','scratch':str(S),'checks':checks,'passed':len(checks),'bundle_source_readiness_sha256':sha(e/'SOURCE-READINESS.md'),'original_source_readiness_sha256':sha(A/'SOURCE-READINESS.md'),'findings':[],'actual_common_semantic_model_reviewed':False,'browser_server_native_network_effects':False});print(json.dumps({'status':'passed','controls':len(checks),'scratch':str(S),'findings':[]}))
