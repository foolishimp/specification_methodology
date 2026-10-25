from __future__ import annotations
import hashlib, html.parser, json, os, pathlib, shutil, subprocess, tarfile, sys, importlib.util
sys.dont_write_bytecode=True
BASE=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c');APP=BASE/'applications/stdo-v3-common-35fb4824';PROOF=BASE/'.ai-workspace/qualification/t010/package-review'
first=json.loads((PROOF/'first-controls.json').read_text());S=pathlib.Path(first['scratch']);bundle=pathlib.Path(first['build']['bundle']);archive=S/'dist/a_c-stdo-v3-common-35fb4824.tar.gz';python=pathlib.Path('/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12')
clean={'PATH':'/usr/bin:/bin','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(S),'XDG_CACHE_HOME':str(S/'cache')}
controls=[]
def rec(name,ok,detail=None):
 controls.append({'name':name,'passed':ok,'detail':detail});assert ok,name
spec=importlib.util.spec_from_file_location('packager_extension',APP/'package_release.py');pkg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pkg;spec.loader.exec_module(pkg)
checks=pkg.checks
with tarfile.open(archive) as tar:
 rows=tar.getmembers();names=[m.name for m in rows]
 rec('archive-safe-relative-regular-sorted-members',names==sorted(names) and all(m.isfile() and not pathlib.PurePosixPath(m.name).is_absolute() and '..' not in pathlib.PurePosixPath(m.name).parts and m.name.startswith(pkg.ARTIFACT+'/') for m in rows),{'members':len(rows)})
 rec('archive-fixed-metadata',all(m.mode==0o644 and m.uid==m.gid==m.mtime==0 and m.uname==m.gname=='' for m in rows))
 extract=S/'extracted';extract.mkdir();tar.extractall(extract,filter='data')
extracted=extract/pkg.ARTIFACT
p=subprocess.run([str(python),'-S','-B',str(extracted/'release_tools/bundle_check.py'),'.'],cwd=extracted,env=clean,capture_output=True,text=True)
rec('clean-extraction-stdlib-replay',p.returncode==0,{'returncode':p.returncode,'stderr':p.stderr,'result':json.loads(p.stdout) if p.returncode==0 else p.stdout})
new=pkg.archive(bundle,S/'repack.tar.gz');rec('archive-byte-reproducible',archive.read_bytes()==(S/'repack.tar.gz').read_bytes(),new)
for name,relative,operation in [('missing-model','model.json','remove'),('tampered-model','model.json','append'),('tampered-carrier','carrier.json','append'),('tampered-source','source/standards/ACTIVATION.md','append'),('tampered-runtime',checks.VIS_LOCAL,'append'),('missing-review','evidence/review-001.json','remove')]:
 root=S/name;shutil.copytree(extracted,root);target=root/relative
 if operation=='remove':target.unlink()
 else:target.write_bytes(target.read_bytes()+b'\n# changed by bounded reviewer control\n')
 p=subprocess.run([str(python),'-S','-B',str(root/'release_tools/bundle_check.py'),'.'],cwd=root,env=clean,capture_output=True,text=True)
 rec(name+'-refused',p.returncode==2,{'returncode':p.returncode,'stderr':p.stderr.strip()})
for name in ['../escape','/absolute','a//b','a/./b','a/../b','a\\b','']:
 try:checks.safe_path(name);ok=False
 except ValueError:ok=True
 rec('unsafe-member-refused:'+repr(name),ok)
redirect=S/'symlink-fixture';redirect.mkdir();(redirect/'link').symlink_to(extracted/'model.json')
try:checks.files(redirect);ok=False
except ValueError:ok=True
rec('symlink-archive-input-refused',ok)
class Assets(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.references=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for field in ['src','href']:
   if field in a:self.references.append((tag,field,a[field]))
parser=Assets();parser.feed((extracted/'graph.html').read_text())
external=[row for row in parser.references if row[1]=='src' and row[2].startswith(('http:','https:','//'))]
rec('graph-no-external-runtime-source',not external,parser.references)
text=(extracted/'graph.html').read_text();rec('runtime-sri-retained',checks.VIS_SRI in text)
rec('no-private-run-files',not any(part in ('actors','run','events.jsonl','invocation.json','actor-settings.json','stderr.txt') for p in checks.files(extracted) for part in pathlib.PurePosixPath(p).parts))
release=json.loads((extracted/'RELEASE.json').read_text());rec('standing-honest',release['semantic_acceptance']=='not_issued' and release['publication']=='not_performed' and release['source_method_release']=='unaccepted_unpublished_not_ready' and release['product_version'] is None)
source_page=extracted/'source-view/standards/ACTIVATION.md.html';raw=(extracted/'source/standards/ACTIVATION.md').read_text();page=source_page.read_text();rec('source-line-addresses-present',all(f'id="L{i}"' in page for i,_ in enumerate(raw.splitlines(),1)),{'lines':len(raw.splitlines())})
node=shutil.which('node')
if node:
 template=(APP/'release_tools/records-template.html').read_text();js=template.rsplit('<script>',1)[1].split('</script>',1)[0];path=S/'record-browser-script.js';path.write_text(js)
 p=subprocess.run([node,'--check',str(path)],env=clean,capture_output=True,text=True);rec('record-browser-js-syntax',p.returncode==0,{'stderr':p.stderr})
else:controls.append({'name':'record-browser-js-syntax','passed':None,'detail':'Node unavailable; no package installed'})
report={'status':'bounded_controls_passed','scratch':str(S),'controls':controls,'interactive_behavior':'unverified; no browser or server launched','actual_common_final_bundle':'not yet available; synthetic fixture only','wrong_review_binding_finding_retained':True}
(PROOF/'extended-controls.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print(json.dumps({'controls':len(controls),'passed':sum(x['passed'] is True for x in controls),'interactive':'unverified','wrong_review_binding':'actionable gap retained'}))
