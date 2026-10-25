from __future__ import annotations
from collections import Counter,defaultdict
import base64,gzip,hashlib,html.parser,importlib.util,io,json,os,pathlib,re,shutil,subprocess,sys,tarfile,time
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';P=B/'.ai-workspace/qualification/t010/package-review/final-003';ART='a_c-stdo-v3-common-35fb4824';archive=A/'dist'/f'{ART}.tar.gz';live=A/'bundle'/ART
before=json.loads((P/'controls-progress.before-harness-correction.json').read_text());S=pathlib.Path(before['scratch']);E=S/'extracted'/ART
controls=[x for x in before['controls'] if x['passed']]
env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')};PYTHON='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while chunk:=f.read(1024*1024):h.update(chunk)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
def check(name,ok,expected=None,observed=None):
 if any(x['name']==name and x['passed'] for x in controls) and ok:return
 controls.append({'name':name,'passed':bool(ok),'expected':expected,'observed':observed});save(P/'controls-progress.json',{'scratch':str(S),'controls':controls})
 if not ok:raise AssertionError(name)
def progress(text):print(json.dumps({'progress':text,'controls_passed':len(controls),'scratch':str(S)}),flush=True)
def cli(label,argv,expect=0):
 logfile=P/'commands'/f'{label}.json'
 if logfile.exists():
  log=json.loads(logfile.read_text());assert log['argv']==[PYTHON,'-S','-B',*argv] and log['returncode']==expect;return json.loads(log['stdout']) if expect==0 else None
 begin=time.monotonic();p=subprocess.run([PYTHON,'-S','-B',*argv],cwd=E,env=env,capture_output=True,text=True)
 save(logfile,{'argv':[PYTHON,'-S','-B',*argv],'cwd':'fresh extracted bundle','returncode':p.returncode,'elapsed_seconds':time.monotonic()-begin,'stdout':p.stdout,'stderr':p.stderr})
 check('public-cli:'+label,p.returncode==expect,expected=expect,observed={'returncode':p.returncode,'stderr':p.stderr[:600]})
 return json.loads(p.stdout) if p.returncode==0 else None
seal=json.loads((B/'.ai-workspace/qualification/t010/build/construction-artifacts-sealed.json').read_text());codecpath=E/'codec/ac_graph.py'
spec=importlib.util.spec_from_file_location('final_review_exact_codec',codecpath);ac=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ac;spec.loader.exec_module(ac)
doc=json.loads((E/'model.json').read_text());model=ac.validate(doc)
custody=json.loads((E/'package-custody.json').read_text());receipt=json.loads((E/'evidence/reviews/review-001/receipt.json').read_text())
files=lambda root:sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
validation=cli('validate',['codec/ac_graph.py','validate','model.json']);check('cli-fragment-claims-bounded','no semantic acceptance' in validation['claim'])
for name in ['carrier.json','graph.json']:
 out=S/('decoded-'+name);reply=cli('decode-'+name,['codec/ac_graph.py','decode',name,'--out',str(out)]);check('public-decode-document-equality:'+name,json.loads(out.read_text())==doc and {k:reply['model'][k] for k in ('id','sha256')}==seal['model'])
found=cli('find',['codec/ac_graph.py','find','carrier.json','admission']);check('public-find-actual-literal-matches',bool(found['matches']) and all('admission' in ac.canonical(model.records[x['id']].fields).decode().casefold() for x in found['matches']),observed={'matches':len(found['matches']),'scope':found['scope']})
seed=found['matches'][0]['id'];inspected=cli('inspect',['codec/ac_graph.py','inspect','carrier.json',seed]);check('public-inspect-exact-record',inspected['record']==model.records[seed].fields and {k:inspected['parent'][k] for k in ('id','sha256')}==seal['model'])
projected=cli('project',['codec/ac_graph.py','project','carrier.json','--seed',seed,'--budget','1987','--out',str(S/'projection.json')]);check('public-projection-parent-selection-and-boundaries',{k:projected['parent'][k] for k in ('id','sha256')}==seal['model'] and seed in projected['included'] and set(projected['included']+projected['excluded'])==set(model.records) and 'not a replacement complete model' in projected['claim'],observed={'included':len(projected['included']),'excluded':len(projected['excluded']),'boundary_keys':list(projected['boundary'])})
source=cli('source-reentry',['release_tools/source_reentry.py','standards/ACTIVATION.md','--start','1','--end','30']);check('source-reentry-public-cli-exact-lines',source['text']==''.join((E/'source/standards/ACTIVATION.md').read_text().splitlines(keepends=True)[:30]))
progress('Documented validate/decode both carriers/find/inspect/project/source-reentry CLI path passed')
# Independently compare display occurrences and all embedded record data.
recorddata=json.loads((E/'records.json').read_text());check('full-record-browser-data-equals-core-records',recorddata['parent']==seal['model'] and recorddata['records']==[{'family':r.family,'record':r.fields} for r in model.records.values()])
scope=json.loads((E/'view-scope.json').read_text());rg=json.loads((E/'records-graph.json').read_text());expected=defaultdict(list);external=0
for ref in model.references:
 if ref.target in model.records:expected[(ref.owner,ref.target)].append({'path':list(ref.path),'governing':ref.schema['governing']})
 else:external+=1
actual={(r['source'],r['target']):r['occurrences'] for r in rg['links']}
check('readable-graph-exact-local-reference-occurrences',actual==dict(expected) and len(actual)==len(rg['links']),observed={'pairs':len(actual),'local_occurrences':sum(map(len,actual.values())),'external_occurrences_omitted':external})
check('display-exact-allrecords-partition-and-declared-omissions',len(scope['included'])==len(set(scope['included']))==1987 and set(scope['included'])==set(model.records) and scope['omitted']==[] and scope['displayed_records']==scope['full_records']==1987 and scope['aggregated_nodes']==0 and scope['displayed_reference_pairs']==scope['full_reference_pairs']==len(expected) and scope['local_reference_occurrences']==sum(map(len,expected.values())) and scope['omitted_external_reference_occurrences']==external)
check('readable-graph-exact-record-node-identities',len(rg['nodes'])==1987 and {r['id'] for r in rg['nodes']}==set(model.records) and all(r['family']==model.records[r['id']].family for r in rg['nodes']))
class Page(html.parser.HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.tags=[];self.scripts=[];self.active=None;self.line=None;self.lines={}
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if tag=='script':self.active={'attrs':a,'text':''}
  if tag=='span' and a.get('id','').startswith('L'):self.line=a['id'];self.lines[self.line]=''
 def handle_data(self,data):
  if self.active is not None:self.active['text']+=data
  if self.line is not None:self.lines[self.line]+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.active is not None:self.scripts.append(self.active);self.active=None
  if tag=='span':self.line=None
pages={}
for name in ['graph.html','records.html','index.html']:
 parser=Page();parser.feed((E/name).read_text());pages[name]=parser
recordjson=next(s['text'] for s in pages['records.html'].scripts if s['attrs'].get('id')=='record-data');check('embedded-record-json-exact',json.loads(recordjson)==recorddata)
ids={a.get('id') for _,a in pages['records.html'].tags};check('record-browser-static-anchors',{'query','family','results','details','matches','record-data'}<=ids)
graphtext=(E/'graph.html').read_text();decoder=json.JSONDecoder()
def jsdata(key):m=re.search(r'const '+key+r'\s*=\s*',graphtext);assert m;return decoder.raw_decode(graphtext[m.end():])[0]
nodes=jsdata('RAW_NODES');edges=jsdata('RAW_EDGES');check('actual-graphify-embedded-node-and-edge-populations',len(nodes)==1987 and {r['id'] for r in nodes}==set(model.records) and len(edges)==len(expected) and {(r['from'],r['to']) for r in edges}==set(expected),observed={'nodes':len(nodes),'edges':len(edges)})
check('actual-display-banner-and-parent-limits',graphtext.count(scope['banner_html'])==1 and 'complete acquisition or acceptance' in scope['claim'] and 'external coordinate plumbing omitted' in rg['claim'])
js=E/'release_tools/vendor/vis-network-9.1.6.min.js';sri='sha384-'+base64.b64encode(hashlib.sha384(js.read_bytes()).digest()).decode();sources=[a['src'] for pg in pages.values() for tag,a in pg.tags if tag=='script' and 'src' in a]
check('all-runtime-script-assets-local-and-SRI-exact',sources==['release_tools/vendor/vis-network-9.1.6.min.js'] and sri=='sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1' and sri in graphtext,observed={'scripts':sources,'sri':sri})
sourceviewbad=[]
for row in custody['members']:
 parser=Page();parser.feed((E/'source-view'/(row['path']+'.html')).read_text());lines=(E/'source'/row['path']).read_text().splitlines()
 if parser.lines!={f'L{i}':line for i,line in enumerate(lines,1)}:sourceviewbad.append(row['path'])
check('all-eightyone-line-addressed-sourceviews-exact',not sourceviewbad,observed={'pages':len(custody['members']),'mismatches':sourceviewbad})
links=[]
for p in [E/'README.md',E/'SOURCE-READINESS.md',E/'release_tools/PUBLIC-RECEIPTS.md',*E.glob('evidence/**/*.md')]:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' in target or target.startswith('#'):continue
  destination=(p.parent/target.split('#',1)[0]).resolve();links.append({'from':p.relative_to(E).as_posix(),'target':target,'exists':destination.exists(),'in_bundle':destination.is_relative_to(E.resolve())})
check('package-and-public-review-local-documentation-links',len(links)==9 and all(r['exists'] and r['in_bundle'] for r in links),observed=links)
node=shutil.which('node');check('existing-node-available-for-static-syntax',bool(node),observed=node)
syntax=[]
for page,parser in pages.items():
 for i,s in enumerate(parser.scripts):
  if s['attrs'].get('type')=='application/json' or 'src' in s['attrs']:continue
  p=S/f'{page}-inline-{i}.js';p.write_text(s['text']);q=subprocess.run([node,'--check',str(p)],cwd=S,env=env,capture_output=True,text=True);syntax.append({'script':p.name,'returncode':q.returncode,'stderr':q.stderr})
check('all-actual-inline-javascript-syntax',all(r['returncode']==0 for r in syntax),observed=syntax)
release=json.loads((E/'RELEASE.json').read_text());check('release-standing-and-basis-honest',release['semantic_acceptance']=='not_issued' and release['publication']=='not_performed' and release['source_method_release']=='unaccepted_unpublished_not_ready' and release['product_version'] is None and release['builder_basis']=='stdo://releases/v2.5.1-rc.2/' and 'unverified' in release['interactive_verification'])
allowed={'authoring-public.json','reviews/review-001/receipt.json',*[f'reviews/review-001/{r["path"]}' for r in receipt['reports']]};check('exact-explicit-public-evidence-file-set',set(files(E/'evidence'))==allowed)
privateparts={'actors','events.jsonl','invocation.json','actor-settings.json','stderr.txt','config.toml','credentials.json'};check('no-private-native-event-config-file-inclusion',not any(privateparts&set(pathlib.PurePosixPath(n).parts) for n in files(E)))
licenses=[]
for directory in ['vendor','upstream','builder_basis']:
 info=json.loads((E/'release_tools'/directory/'custody.json').read_text())
 for row in info['files']:
  if 'path' not in row:continue
  target=E/'release_tools'/directory/row['path'];licenses.append({'path':target.relative_to(E).as_posix(),'matched':target.stat().st_size==row['bytes'] and sha(target)==row['sha256']})
check('all-applicable-bundled-thirdparty-basis-license-and-custody-files-exact',all(r['matched'] for r in licenses),observed=licenses)
# Independent deterministic repack, with no dependency on repo/upstream/config.
repack=S/'independent-repack.tar.gz'
with repack.open('xb') as stream:
 with gzip.GzipFile(filename='',mode='wb',fileobj=stream,mtime=0,compresslevel=9) as gz:
  with tarfile.open(fileobj=gz,mode='w',format=tarfile.PAX_FORMAT) as tar:
   for name in files(E):
    data=(E/name).read_bytes();m=tarfile.TarInfo(ART+'/'+name);m.size=len(data);m.mode=0o644;m.uid=m.gid=m.mtime=0;m.uname=m.gname='';tar.addfile(m,io.BytesIO(data))
check('independent-deterministic-repack-identical',sha(repack)==sha(archive),observed={'bytes':repack.stat().st_size,'sha256':sha(repack)})
progress('StaticactualHTML/data/sourceviews/assets/docs/reference checks and deterministic repack passed')
save(P/'phase-001.json',{'status':'passed','scratch':str(S),'extracted':str(E),'archive_sha256':sha(archive),'canonical_model':seal['model'],'controls':controls,'controls_passed':len(controls),'interactive_behavior':'unverified; no browser/server effects','actual_source_semantics':'not re-reviewed; exact source/record transport checks only'})
