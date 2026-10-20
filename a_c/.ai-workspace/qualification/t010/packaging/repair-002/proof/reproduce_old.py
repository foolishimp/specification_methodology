from pathlib import Path
import gzip, hashlib,json,os,shutil,subprocess,sys,tarfile
R=Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021')
APP=R/'app'; RED=R/'proof/red'; PY=Path('/Users/jim/src/apps/specification_methodology/a_c/.venv/bin/python3')
UP=Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
ORIG=Path('/Users/jim/src/apps/specification_methodology/a_c/applications/stdo-v3-common-35fb4824')
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',XDG_CACHE_HOME=str(R/'caches'),TMPDIR=str(R/'tmp'))

def run(name,args,cwd=None):
 result=subprocess.run([str(x) for x in args],cwd=cwd or R,env=env,capture_output=True,text=True)
 value={'argv':[str(x) for x in args],'cwd':str(cwd or R),'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
 (RED/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
 return value

def extract(archive,target):
 target.mkdir(parents=True)
 with tarfile.open(archive,'r:gz') as f:
  names=f.getnames(); f.extractall(target,filter='data')
 return names

def rehash(root):
 p=root/'inventory.json'; inv=json.loads(p.read_text())
 for row in inv['files']:
  raw=(root/row['path']).read_bytes(); row['bytes']=len(raw); row['sha256']=hashlib.sha256(raw).hexdigest()
 p.write_text(json.dumps(inv,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
 names=sorted([row['path'] for row in inv['files']]+['inventory.json'])
 (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in names))

command=[PY,'-B',APP/'package_release.py','build','--proposal',R/'inputs/proposal','--public-evidence',R/'inputs/authoring-public.json','--review',R/'inputs/review/bounded-review.json','--upstream',UP,'--bundle',RED/'overlap/bundle','--dist',RED/'overlap/bundle/dist']
a=run('F1-build-overlap',command); assert a['returncode']==0,a
archive=RED/'overlap/bundle/dist/a_c-stdo-v3-common-35fb4824.tar.gz'
names=extract(archive,RED/'overlap-extracted')
after=run('F1-extracted-check',[PY,'-B','-S',RED/'overlap-extracted/a_c-stdo-v3-common-35fb4824/release_tools/bundle_check.py',RED/'overlap-extracted/a_c-stdo-v3-common-35fb4824'])
assert len(names)==214 and after['returncode']==2
assert 'missing or extra unlisted files' in after['stderr']

extract(ORIG/'dist/a_c-stdo-v3-common-35fb4824.tar.gz',RED/'old-extracted')
old=RED/'old-extracted/a_c-stdo-v3-common-35fb4824'
b=run('F2-extracted-build',[PY,'-B',old/'package_release.py','build','--proposal',old,'--public-evidence',old/'evidence/authoring-public.json','--review',old/'evidence/reviews/review-001/receipt.json','--upstream',UP,'--bundle',RED/'portable-rebuild/bundle','--dist',RED/'portable-rebuild/dist'])
assert b['returncode']==2 and 'sealed originating-workspace source-readiness record changed' in b['stderr'],b

release=old/'RELEASE.json'; original=release.read_bytes(); (RED/'F3-original-RELEASE.json').write_bytes(original)
value=json.loads(original);value['source_commit']='0'*40;release.write_text(json.dumps(value,sort_keys=True,indent=2)+'\n');rehash(old)
c=run('F3-rehashed-wrong-commit-check',[PY,'-B','-S',old/'release_tools/bundle_check.py',old]);assert c['returncode']==0,c
summary={'status':'all_three_reproduced_on_unchanged_old_code','F1':{'constructor_reported_success':True,'archive_members':len(names),'expected_files':213,'extracted_checker_refused':True},'F2':{'actual_extracted_build_refused':True,'reason':'sealed originating-workspace source-readiness record changed'},'F3':{'wrong_zero_commit_after_outer_rehash_accepted':True},'original_code_sha256':hashlib.sha256((APP/'package_release.py').read_bytes()).hexdigest(),'original_receipts_helper_sha256':hashlib.sha256((APP/'release_tools/public_receipts.py').read_bytes()).hexdigest()}
(RED/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
