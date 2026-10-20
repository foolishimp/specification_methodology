from __future__ import annotations
import hashlib,importlib.util,json,os,pathlib,shlex,subprocess,sys,tarfile,types
sys.dont_write_bytecode=True
O=pathlib.Path('/Users/jim/tmp/a_c-common-rc1-packaging-review-20261021/assessment-001');R=pathlib.Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021');P=O.parent/'preparation';OLD=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c/applications/stdo-v3-common-35fb4824');ART='a_c-stdo-v3-common-35fb4824-packaging-r1';archive=R/'out/first/dist'/f'{ART}.tar.gz';controls=[]
(O/'tmp').mkdir();(O/'cache').mkdir();ENV={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','PYTHONDONTWRITEBYTECODE':'1','PYTHONNOUSERSITE':'1','GIT_OPTIONAL_LOCKS':'0','TMPDIR':str(O/'tmp'),'XDG_CACHE_HOME':str(O/'cache'),'MPLCONFIGDIR':str(O/'cache/matplotlib')};os.environ.update(ENV)
PY='/Users/jim/src/apps/specification_methodology/a_c/.venv/bin/python3';UP='/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
def check(name,ok,observed=None):
 controls.append({'name':name,'passed':bool(ok),'observed':observed});save(O/'stage1-progress.json',{'controls':controls})
 if not ok:raise AssertionError(name)
def snapshot(root):
 rows={}
 for p in sorted(root.rglob('*')):
  n=p.relative_to(root).as_posix()
  if p.is_symlink():rows[n]={'symlink':os.readlink(p)}
  elif p.is_file():rows[n]={'bytes':p.stat().st_size,'sha256':sha(p)}
  elif p.is_dir():rows[n]={'directory':True}
 return rows
# Freeze read-only named candidate and original subjects before executing any code.
guards={}
for base,manifest in [(R/'app',R/'proof/candidate-app-files.json'),(R/'inputs',R/'proof/frozen-input-files.json'),(R/'out/first/bundle'/ART,R/'proof/frozen-bundle-files.json')]:
 rows=json.loads(manifest.read_text())
 for row in rows:
  p=base/row['path'];assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'];guards[str(p)]=row['sha256']
for n,w in json.loads((O/'ACTIVATION.json').read_text())['candidate_pins'].items():assert sha(R/n)==w;guards[str(R/n)]=w
for manifest in ['ORIGINAL-GUARDS.json','ORIGINAL-BUNDLE-GUARDS.json']:guards.update(json.loads((P/manifest).read_text())['files'])
preclose=json.loads((P/'CLOSED.json').read_text());guards[str(P/'CLOSED.json')]='cc8dbb8adf78599a1e36306eb136aee2042a8cff3ff93237cde688e5bba4b11e'
for n,row in preclose['proof_files'].items():guards[str(P/n)]=row['sha256']
check('named-candidate-original-and-preparation-pins-match',all(sha(pathlib.Path(n))==w for n,w in guards.items()),{'unique_paths':len(guards)});save(O/'READONLY-GUARDS.json',{'files':guards})
with tarfile.open(archive) as tar:
 members=tar.getmembers();names=[m.name for m in members]
 safe=names==sorted(set(names)) and len(names)==213 and all(m.isfile() and not m.issym() and not m.islnk() and m.name.startswith(ART+'/') and pathlib.PurePosixPath(m.name).as_posix()==m.name and not pathlib.PurePosixPath(m.name).is_absolute() and all(x not in ('..','.','') for x in pathlib.PurePosixPath(m.name).parts) for m in members)
 check('frozen-r1-safe213-member-archive',safe,{'members':len(members),'sha256':sha(archive),'bytes':archive.stat().st_size});assert safe
 ex=O/'extracted';ex.mkdir();tar.extractall(ex,filter='data')
E=ex/ART
rows=[{'path':p.relative_to(E).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(E.rglob('*')) if p.is_file()];vector=hashlib.sha256(json.dumps(rows,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest();check('actual-extracted213-file-vector-exact',rows==json.loads((R/'proof/frozen-bundle-files.json').read_text()) and sum(r['bytes'] for r in rows)==110473751 and vector=='22def4fbec18e4ec543d01ddf2ae71a59fc1cf5e2d20c3601b09ede4f84df6fd',{'files':len(rows),'bytes':sum(r['bytes'] for r in rows),'vector_sha256':vector})
check('archive-sidecar-exact',(archive.with_name(archive.name+'.sha256')).read_text()==f'{sha(archive)}  {archive.name}\n')
spec=importlib.util.spec_from_file_location('assessed_packager_r1',E/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
check('extracted-code-is-bound-repair',sha(E/'package_release.py')=='324fe8242ecb4f67c6f6ed77c6ff3f674245f53c73f17ba1029f0e9f03b28ccb' and sha(E/'release_tools/public_receipts.py')=='ab91aae1bd08d64c167833095735735235919e0dd32a040b39d95c60291cf3b3')
# Direct helper controls use real filesystem paths/effects and tiny source bundles.
cases=[]
for label in ['equal-dist','nested-dist','dotdot-dist','symlink-dist-alias','output-equals-bundle','output-is-ancestor','safe-sibling-dist','safe-parent-dist','protected-archive','protected-sidecar','protected-dangling-symlink']:
 root=O/'helper-cases'/label;bundle=root/'bundle';bundle.mkdir(parents=True);(bundle/'one.txt').write_text('one\n');(bundle/'two.txt').write_text('two\n')
 if label=='equal-dist':out=bundle/'artifact.tar.gz'
 elif label=='nested-dist':out=bundle/'dist/artifact.tar.gz'
 elif label=='dotdot-dist':out=bundle/'staging/../artifact.tar.gz'
 elif label=='symlink-dist-alias':alias=root/'alias';alias.symlink_to(bundle,target_is_directory=True);out=alias/'artifact.tar.gz'
 elif label=='output-equals-bundle':out=bundle
 elif label=='output-is-ancestor':out=root
 elif label=='safe-parent-dist':out=root/'artifact.tar.gz'
 else:out=root/'dist/artifact.tar.gz'
 if label=='protected-archive':out.parent.mkdir();out.write_bytes(b'KEEP ARCHIVE')
 if label=='protected-sidecar':out.parent.mkdir();out.with_name(out.name+'.sha256').write_bytes(b'KEEP SIDECAR')
 if label=='protected-dangling-symlink':out.parent.mkdir();out.symlink_to(root/'absent-target')
 before=snapshot(root);reason=None
 try:result=pkg.archive(bundle,out);accepted=True
 except (ValueError,OSError) as err:accepted=False;reason=str(err);result=None
 after=snapshot(root);positive=label in ['safe-sibling-dist','safe-parent-dist'];names=None
 if accepted:
  with tarfile.open(out) as tar:names=[m.name for m in tar.getmembers()]
 ok=(accepted and len(names)==2 and all(n.startswith(ART+'/') for n in names)) if positive else (not accepted and before==after)
 check('direct-archive:'+label,ok,{'accepted':accepted,'reason':reason,'filesystem_changed':before!=after,'members':names});cases.append({'case':label,'accepted':accepted,'reason':reason,'before':before,'after':after})
# Authenticate exact original AND included portable readiness without importing omitted original data into rebuild.
original=(OLD/'SOURCE-READINESS.md').read_bytes();portable=(E/'SOURCE-READINESS.md').read_bytes();check('exact-original-and-portable-readiness-accepted',pkg.source_readiness_projection(original).encode()==portable and pkg.source_readiness_projection(portable).encode()==portable)
for label,data in [('prefix',portable.replace(b'captured-workspace projection',b'captured-workspace projection ALTERED',1)),('version',portable.replace(b'Common V3',b'Common V4',1)),('gate',portable.replace(b'not_ready',b'ready',1)),('append',portable+b'\nOwner accepted.\n')]:
 try:pkg.source_readiness_projection(data);refused=False;reason=None
 except ValueError as err:refused=True;reason=str(err)
 check('mutated-readiness-refused:'+label,refused,reason)
# Parse the documented rebuild command. Replace only executable, explicit dependency and fresh output coordinates.
readme=(E/'README.md').read_text();commands=[shlex.split(block.replace('\\\n',' ')) for block in __import__('re').findall(r'```sh\n(.*?)\n```',readme,__import__('re').S) if 'package_release.py build' in block];assert len(commands)==1;documented=commands[0]
base=documented[:];base[0]=PY;base[base.index('--upstream')+1]=UP
check('documented-inputs-are-bundled-only',base[base.index('--proposal')+1]=='.' and base[base.index('--public-evidence')+1]=='evidence/authoring-public.json' and base[base.index('--review')+1]=='evidence/reviews/review-001/receipt.json' and not (E/'freeze_sources.py').exists())
cli_cases=[]
for label in ['equal-dist','nested-dist','dotdot-dist','symlink-dist-alias','protected-archive']:
 root=O/'cli-cases'/label;root.mkdir(parents=True);bundle=root/'bundle'
 if label=='equal-dist':dist=bundle
 elif label=='nested-dist':dist=bundle/'nested'
 elif label=='dotdot-dist':dist=bundle/'staging/..'
 elif label=='symlink-dist-alias':dist=root/'alias';dist.symlink_to(bundle,target_is_directory=True)
 else:
  dist=root/'dist';dist.mkdir();(dist/(ART+'.tar.gz')).write_bytes(b'KEEP EXISTING ARCHIVE')
 argv=base[:];argv[argv.index('--bundle')+1]=str(bundle);argv[argv.index('--dist')+1]=str(dist)
 before=snapshot(root);p=subprocess.run(argv,cwd=E,env=ENV,capture_output=True,text=True);after=snapshot(root);ok=p.returncode==2 and before==after
 check('public-build-pre-effect:'+label,ok,{'returncode':p.returncode,'stderr':p.stderr,'filesystem_changed':before!=after});cli_cases.append({'case':label,'argv':argv,'returncode':p.returncode,'stderr':p.stderr,'before':before,'after':after})
# Baseline data conservation; no new semantic interpretation.
seal=json.loads((pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c')/'.ai-workspace/qualification/t010/build/construction-artifacts-sealed.json').read_text());check('same-five-raw-artifacts',all((E/n).stat().st_size==r['bytes'] and sha(E/n)==r['sha256'] for n,r in seal['artifacts'].items()))
custody=json.loads((E/'package-custody.json').read_text());check('same81-source-and-three-manifests',len(custody['members'])==81 and all(sha(E/'source'/r['path'])==r['sha256'] and sha(OLD/'source'/r['path'])==r['sha256'] for r in custody['members']) and all(sha(E/n)==sha(OLD/n) for n in ['source-manifest.json','source-classification.json','package-custody.json']))
check('same-public-construction-and-semantic-review-receipts',sha(E/'evidence/authoring-public.json')=='1f19d4ab142bd857694e4ab2a10f978bb290d99cbf68dd028f50f37a1268373c' and sha(E/'evidence/reviews/review-001/receipt.json')=='542c2330eca15ff9a3804e186b7d31b83ef3ae62f5d7dfdc2073f793a1d3dbdd')
release=json.loads((E/'RELEASE.json').read_text());check('packaging-revision-and-honest-proposal-limits',release['artifact']==ART and release['product_version'] is None and release['publication']=='not_performed' and release['semantic_acceptance']=='not_issued' and release['source_method_release']=='unaccepted_unpublished_not_ready' and 'unverified' in release['interactive_verification'])
save(O/'STAGE1.json',{'status':'passed','controls':controls,'controls_passed':len(controls),'extracted':str(E),'documented_command':documented,'substituted_command_base':base,'helper_cases':cases,'public_overlap_cases':cli_cases,'candidate_file_vector_sha256':vector,'fixed_code_review':'Minimal scoped changes; overlap checks precede effects, filenames captured before archive open, readiness exact byte pins/idempotence, duplicate source fields compared with bound custody expectations. No actionable static issue found; actual rebuild/portable metadata controls pending.'});print(json.dumps({'status':'passed','controls':len(controls),'extracted':str(E),'next':'portable verifier, both recoveries, actual documented bundled-input rebuild and outer-rehashed metadata controls'}))
