from __future__ import annotations
from collections import Counter,defaultdict
import base64,gzip,hashlib,html.parser,importlib.util,io,json,os,pathlib,re,shutil,subprocess,sys,tarfile,tempfile,time
sys.dont_write_bytecode=True
B=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');A=B/'applications/stdo-v3-common-35fb4824';P=B/'.ai-workspace/qualification/t010/package-review/final-003';ART='a_c-stdo-v3-common-35fb4824';archive=A/'dist'/f'{ART}.tar.gz';live=A/'bundle'/ART
S=pathlib.Path(tempfile.mkdtemp(prefix='ac-common-package-review-'));env={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')};(S/'cache').mkdir();os.environ['PYTHONDONTWRITEBYTECODE']='1'
PYTHON='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';controls=[]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while chunk:=f.read(1024*1024):h.update(chunk)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
def check(name,ok,expected=None,observed=None):
 controls.append({'name':name,'passed':bool(ok),'expected':expected,'observed':observed});save(P/'controls-progress.json',{'scratch':str(S),'controls':controls})
 if not ok:raise AssertionError(name)
def progress(text):print(json.dumps({'progress':text,'controls_passed':len(controls),'scratch':str(S)}),flush=True)
sealpath=B/'.ai-workspace/qualification/t010/build/construction-artifacts-sealed.json';seal=json.loads(sealpath.read_text());check('exact-five-artifact-seal',sha(sealpath)=='9690964649fa2d6a0deb7a4278cf698a874995940d6b094d18968d07094b86e9',observed=sha(sealpath))
reviewroot=B/'.ai-workspace/qualification/t010/semantic-review/assessment-001';check('semantic-review-closure-coordinate',sha(reviewroot/'CLOSED.json')=='1b81f8599de3ec38e7fe8748d1c6a3022d24664d15ccb3c2756ea5360d120145',observed=sha(reviewroot/'CLOSED.json'))
initial=json.loads((B/'.ai-workspace/qualification/t010/packaging/initial-guards.json').read_text());mismatch=[]
for row in initial['guarded_files']:
 p=B/row['path']
 if not p.is_file() or p.stat().st_size!=row['bytes'] or sha(p)!=row['sha256']:mismatch.append(row['path'])
check('all-original-preexisting-custody-guards',not mismatch,expected={'files':len(initial['guarded_files']),'mismatches':[]},observed={'mismatches':mismatch})
# Independently preflight every archive destination before extraction.
with tarfile.open(archive) as tar:
 members=tar.getmembers();names=[r.name for r in members];prefix=ART+'/'
 safe=all(m.isfile() and not m.issym() and not m.islnk() and m.name.startswith(prefix) and not pathlib.PurePosixPath(m.name).is_absolute() and pathlib.PurePosixPath(m.name).as_posix()==m.name and all(x not in ('','..','.') for x in pathlib.PurePosixPath(m.name).parts) and '\\' not in m.name for m in members)
 check('archive-safe-canonical-regular-unique-sorted-members',safe and names==sorted(set(names)),observed={'members':len(members)})
 check('archive-fixed-metadata',all(m.mode==0o644 and m.uid==m.gid==m.mtime==0 and m.uname==m.gname=='' for m in members))
 extracted=S/'extracted';extracted.mkdir();tar.extractall(extracted,filter='data')
E=extracted/ART
files=lambda root:sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
check('extracted-exactly-matches-frozen-bundle',files(E)==files(live) and all(sha(E/n)==sha(live/n) for n in files(E)),observed={'files':len(files(E))})
check('external-archive-checksum', (A/'dist'/f'{ART}.tar.gz.sha256').read_text()==f'{sha(archive)}  {ART}.tar.gz\n')
progress('Safe fresh extraction and archive/live custody match')
# Explicit logs contain public artifact CLI results only.
def cli(label,argv,expect=0):
 begin=time.monotonic();p=subprocess.run([PYTHON,'-S','-B',*argv],cwd=E,env=env,capture_output=True,text=True)
 save(P/'commands'/f'{label}.json',{'argv':[PYTHON,'-S','-B',*argv],'cwd':'fresh extracted bundle','returncode':p.returncode,'elapsed_seconds':time.monotonic()-begin,'stdout':p.stdout,'stderr':p.stderr})
 check('public-cli:'+label,p.returncode==expect,expected=expect,observed={'returncode':p.returncode,'stderr':p.stderr[:600]})
 return json.loads(p.stdout) if p.returncode==0 else None
replay=cli('bundle-check',['release_tools/bundle_check.py','.']);check('portable-check-exact-model-and-extent',replay['model']==seal['model'] and replay['records']==1987 and replay['source']['files']==81 and replay['source']['semantic_files']==58,observed=replay)
# Import only the exact copied stdlib codec for independent static data checks.
codecpath=E/'codec/ac_graph.py';check('exact-codec-copied',sha(codecpath)=='2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667')
spec=importlib.util.spec_from_file_location('final_review_exact_codec',codecpath);ac=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ac;spec.loader.exec_module(ac)
doc=json.loads((E/'model.json').read_text());model=ac.validate(doc);check('canonical-model-sealed',model.sha256==seal['model']['sha256'] and model.identity==seal['model']['id'])
for name,row in seal['artifacts'].items():
 check('sealed-raw-artifact:'+name,(E/name).stat().st_size==row['bytes'] and sha(E/name)==row['sha256'] and sha(A/'run/repaired-proposal'/name)==row['sha256'],observed={'bytes':(E/name).stat().st_size,'sha256':sha(E/name)})
custody=json.loads((E/'package-custody.json').read_text());semantic=json.loads((E/'source-manifest.json').read_text());classification=json.loads((E/'source-classification.json').read_text())
sourcebad=[]
for row in custody['members']:
 data=(E/'source'/row['path']).read_bytes();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256'] or blob!=row['git_blob'] or sha(A/'source'/row['path'])!=row['sha256']:sourcebad.append(row['path'])
check('all-eightyone-source-members-sealed-and-git-blob-exact',len(custody['members'])==81 and not sourcebad,observed={'files':len(custody['members']),'bytes':sum(r['bytes'] for r in custody['members']),'mismatches':sourcebad})
check('explicit-source-scope-58-13-10',{k:v['member_count'] for k,v in classification['classes'].items()}=={'primary_semantic':58,'derived_frames':13,'host_legal_release_metadata':10})
for n in ['source-manifest.json','source-classification.json','package-custody.json']:
 check('source-manifest-exact:'+n,sha(E/n)==sha(A/n))
construction=E/'evidence/authoring-public.json';review=E/'evidence/reviews/review-001/receipt.json'
check('actual-public-construction-receipt-pin',sha(construction)=='1f19d4ab142bd857694e4ab2a10f978bb290d99cbf68dd028f50f37a1268373c' and sha(construction)==sha(A/'build/authoring-public.json'))
check('actual-public-bounded-review-receipt-pin',sha(review)=='542c2330eca15ff9a3804e186b7d31b83ef3ae62f5d7dfdc2073f793a1d3dbdd' and sha(review)==sha(reviewroot/'bounded-review.json'))
receipt=json.loads(review.read_text());reportbad=[]
for row in receipt['reports']:
 p=review.parent/row['path']
 if p.stat().st_size!=row['bytes'] or sha(p)!=row['sha256'] or sha(p)!=sha(reviewroot/row['path']):reportbad.append(row['path'])
check('four-readable-review-reports-unchanged',len(receipt['reports'])==4 and not reportbad,observed={'reports':len(receipt['reports']),'mismatches':reportbad})
sections=json.loads((E/'release_tools/source-sections.json').read_text())['sections'];bysec={r['id']:r for r in sections};sourcelines={r['path']:(E/'source'/r['path']).read_text().splitlines(keepends=True) for r in semantic['files']}
check('all-eighthundredfortyfive-source-sections-exact',len(sections)==len(bysec)==845 and all(hashlib.sha256(''.join(sourcelines[r['path']][r['start_line']-1:r['end_line']]).encode()).hexdigest()==r['sha256'] for r in sections))
coverage=json.loads((E/'coverage.json').read_text());dispositions=[r for chunk in coverage['section_dispositions'] for r in chunk['dispositions']]
check('all-eighthundredfortyfive-section-dispositions-present',len(dispositions)==845 and {r['section_id'] for r in dispositions}==set(bysec),observed=dict(Counter(r['decision'] for r in dispositions)))
def grounds(v):
 out=[]
 if isinstance(v,dict):
  if {'path','section','start_line','end_line','quote'}<=v.keys():out.append(v)
  for x in v.values():out.extend(grounds(x))
 elif isinstance(v,list):
  for x in v:out.extend(grounds(x))
 return out
physical=[];mirror=0
for family,rows in doc['populations'].items():
 for record in rows:
  physical.extend(grounds(record))
  if family=='latitude' and record['allowed_variation']['grounding']==record['forbidden_variation']['grounding']:mirror+=len(record['allowed_variation']['grounding'])
bad=[]
for n,g in enumerate(physical):
 sec=bysec.get(g['section']);valid=sec is not None and g['path']==sec['path'] and sec['start_line']<=g['start_line']<=g['end_line']<=sec['end_line']
 if not valid or not g['quote'] or g['quote'] not in ''.join(sourcelines[g['path']][g['start_line']-1:g['end_line']]):bad.append(n)
check('every-grounding-occurrence-replays-exact-source',not bad and len(physical)==2491,expected={'physical':2491,'bad':[]},observed={'physical':len(physical),'mirror_encoded_latitude':mirror,'authored_entries_without_mirrored_encoding':len(physical)-mirror,'bad':bad})
counts={k:len(v) for k,v in doc['populations'].items()};check('eight-populations-and-declared-inert-fragment',sum(counts.values())==1987 and len(counts)==8 and all(counts[x]==0 for x in ['traversals','transformations','judgments']),observed=counts)
progress('Portable stdlib checker, exact source/receipts/reports,845sections and2491physical grounding occurrences passed')
validation=cli('validate',['codec/ac_graph.py','validate','model.json']);check('cli-fragment-claims-bounded','no semantic acceptance' in validation['claim'])
for name in ['carrier.json','graph.json']:
 out=S/('decoded-'+name);reply=cli('decode-'+name,['codec/ac_graph.py','decode',name,'--out',str(out)]);check('public-decode-document-equality:'+name,json.loads(out.read_text())==doc and reply['model']==seal['model'])
found=cli('find',['codec/ac_graph.py','find','carrier.json','admission']);check('public-find-actual-literal-matches',bool(found['matches']) and all('admission' in ac.canonical(model.records[x['id']].fields).decode().casefold() for x in found['matches']),observed={'matches':len(found['matches']),'scope':found['scope']})
seed=found['matches'][0]['id'];inspected=cli('inspect',['codec/ac_graph.py','inspect','carrier.json',seed]);check('public-inspect-exact-record',inspected['record']==model.records[seed].fields and inspected['parent']==seal['model'])
projected=cli('project',['codec/ac_graph.py','project','carrier.json','--seed',seed,'--budget','1987','--out',str(S/'projection.json')]);check('public-projection-parent-selection-and-boundaries',projected['parent']==seal['model'] and seed in projected['included'] and set(projected['included']+projected['excluded'])==set(model.records) and 'not a replacement complete model' in projected['claim'],observed={'included':len(projected['included']),'excluded':len(projected['excluded']),'boundary_keys':list(projected['boundary'])})
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
