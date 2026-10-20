from pathlib import Path
from datetime import datetime,timezone
import hashlib,importlib.util,json,os,re,shlex,shutil,subprocess,sys,tarfile,time

R=Path('/Users/jim/tmp/a_c-common-rc1-packaging-repair-20261021')
APP=R/'app'; PROOF=R/'proof/actual'; PROOF.mkdir(parents=True)
OUT=R/'out'; OUT.mkdir()
PY=Path('/Users/jim/src/apps/specification_methodology/a_c/.venv/bin/python3')
UP=Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
OLD=Path('/Users/jim/src/apps/specification_methodology/a_c/applications/stdo-v3-common-35fb4824/bundle/a_c-stdo-v3-common-35fb4824')
ID='a_c-stdo-v3-common-35fb4824-packaging-r1'
MODEL_SHA='691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf'
RAW_MODEL_SHA='70feb48cf657bcb20231dbfffe0c2076e5e69b24aeb0f226a001a22957b7f56a'
RECORD='urn:a-c:generation:0657852b6fd1fa48457c3f7d:record:5fec0f21265016ca449d4389511dce49'
ENV=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',XDG_CACHE_HOME=str(R/'caches'),TMPDIR=str(R/'tmp'))
operations=[]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,value): path.write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
def run(name,args,cwd=R,expected=0,reason=None):
    print('START '+name,flush=True); start=time.monotonic()
    result=subprocess.run([str(x) for x in args],cwd=cwd,env=ENV,capture_output=True,text=True)
    record={'argv':[str(x) for x in args],'cwd':str(cwd),'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'elapsed_seconds':round(time.monotonic()-start,3)}
    save(PROOF/(name+'.json'),record)
    assert result.returncode==expected,(name,record)
    if reason is not None: assert reason in result.stderr,(name,record)
    operations.append({'operation':name,'outcome':'passed','returncode':result.returncode,'elapsed_seconds':record['elapsed_seconds']})
    print('PASS '+name+' '+str(record['elapsed_seconds'])+'s',flush=True)
    return record

def vector(root):
    return [{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file()]

def extract(archive,destination):
    destination.mkdir(parents=True)
    with tarfile.open(archive,'r:gz') as data:
        names=data.getnames(); assert len(names)==213
        assert all(name.startswith(ID+'/') and '..' not in Path(name).parts for name in names)
        data.extractall(destination,filter='data')
    operations.append({'operation':'safe_actual_archive_extraction','outcome':'passed','files':len(names)})
    return destination/ID

def rehash(root):
    inv=json.loads((root/'inventory.json').read_text())
    for row in inv['files']:
        p=root/row['path']; row['bytes']=p.stat().st_size;row['sha256']=sha(p)
    save(root/'inventory.json',inv)
    names=sorted([row['path'] for row in inv['files']]+['inventory.json'])
    (root/'SHA256SUMS').write_text(''.join(sha(root/name)+'  '+name+'\n' for name in names))

first_bundle=OUT/'first/bundle'/ID; first_dist=OUT/'first/dist'
base_args=['--proposal',R/'inputs/proposal','--public-evidence',R/'inputs/authoring-public.json','--review',R/'inputs/review/bounded-review.json','--upstream',UP]
run('01-first-build',[PY,'-B',APP/'package_release.py','build',*base_args,'--bundle',first_bundle,'--dist',first_dist])
archive=first_dist/(ID+'.tar.gz'); first=extract(archive,OUT/'extracted-first')
run('02-extracted-stdlib-check',[PY,'-B','-S',first/'release_tools/bundle_check.py',first])

recovered=OUT/'recovered'; recovered.mkdir()
for number,carrier in enumerate(['carrier.json','graph.json'],3):
    target=recovered/(carrier+'-model.json')
    run(f'{number:02d}-decode-'+carrier,[PY,'-B','-S',first/'codec/ac_graph.py','decode',first/carrier,'--out',target])
    assert sha(target)==RAW_MODEL_SHA
run('05-find',[PY,'-B','-S',first/'codec/ac_graph.py','find',first/'carrier.json','admission'])
run('06-inspect',[PY,'-B','-S',first/'codec/ac_graph.py','inspect',first/'carrier.json',RECORD])
run('07-project',[PY,'-B','-S',first/'codec/ac_graph.py','project',first/'carrier.json','--seed',RECORD,'--out',OUT/'selected-projection.json'])
run('08-source-reentry',[PY,'-B','-S',first/'release_tools/source_reentry.py','standards/ACTIVATION.md','--start','1','--end','30'],cwd=first)

sys.path.insert(0,str(APP))
import package_release as package
repacked=OUT/'repacked'/archive.name
repack=package.archive(first,repacked)
assert sha(repacked)==sha(archive)
save(PROOF/'09-deterministic-repack.json',{'archive':str(archive),'repacked':str(repacked),'sha256':sha(archive),'bytes':archive.stat().st_size,'exact_match':True,'helper_result':repack})
operations.append({'operation':'09-deterministic-repack','outcome':'passed'})

readme=(first/'README.md').read_text()
blocks=re.findall(r'```sh\n(.*?)\n```',readme,re.S)
recipe=next(block for block in blocks if block.startswith('python3 -B package_release.py build'))
argv=shlex.split(recipe.replace('\\\n',' ')); assert argv[:4]==['python3','-B','package_release.py','build']
assert argv[argv.index('--proposal')+1]=='.'
assert argv[argv.index('--public-evidence')+1]=='evidence/authoring-public.json'
assert argv[argv.index('--review')+1]=='evidence/reviews/review-001/receipt.json'
argv[0]=str(PY)
second_bundle=OUT/'second/bundle'/ID;second_dist=OUT/'second/dist'
for flag,value in [('--upstream',UP),('--bundle',second_bundle),('--dist',second_dist)]:argv[argv.index(flag)+1]=str(value)
save(PROOF/'10-documented-extracted-build-input-closure.json',{'source_readme_sha256':sha(first/'README.md'),'documented_recipe':recipe,'executed_argv':argv,'cwd':str(first),'only_external_build_dependencies':{'existing_python_networkx_environment':str(PY),'graphify_checkout':str(UP),'graphify_commit':package.UPSTREAM},'all_source_readiness_model_source_and_receipt_inputs':'Bundled relative inputs in extracted first archive; no omitted originating-workspace document/private run required'})
run('10-documented-extracted-build',argv,cwd=first)
second_archive=second_dist/archive.name
first_vector=vector(first);second_vector=vector(second_bundle)
assert first_vector==second_vector
assert archive.read_bytes()==second_archive.read_bytes()
save(PROOF/'11-second-generation-equivalence.json',{'all_files_byte_equal':True,'files':len(first_vector),'bytes':sum(x['bytes'] for x in first_vector),'first_archive_sha256':sha(archive),'second_archive_sha256':sha(second_archive),'archives_byte_equal':True,'same_source_model_receipts_and_projected_source_readiness':True})
operations.append({'operation':'11-second-generation-equivalence','outcome':'passed'})

# Rehash the outer inventory after each mutation so the negative reaches the source-index binding.
tamper=OUT/'metadata-tamper';shutil.copytree(first,tamper)
original_release=(first/'RELEASE.json').read_bytes()
for number,key,value in [(12,'source_commit','0'*40),(13,'package_tree','0'*40),(14,'source_commit',None),(15,'package_tree',None)]:
    release=json.loads(original_release)
    if value is None:del release[key]
    else:release[key]=value
    save(tamper/'RELEASE.json',release);rehash(tamper)
    run(f'{number:02d}-rehash-'+('missing-' if value is None else 'wrong-')+key,[PY,'-B','-S',tamper/'release_tools/bundle_check.py',tamper],expected=2,reason='release-preparation source commit/package tree differs')

# Actual public constructor refusal for altered portable input, before any output creation.
(tamper/'RELEASE.json').write_bytes(original_release)
(tamper/'SOURCE-READINESS.md').write_bytes((tamper/'SOURCE-READINESS.md').read_bytes()+b'\n')
rehash(tamper)
bad_bundle=OUT/'bad-portable-input/bundle';bad_dist=OUT/'bad-portable-input/dist'
run('16-modified-portable-input-refusal',[PY,'-B',tamper/'package_release.py','build','--proposal',tamper,'--public-evidence',tamper/'evidence/authoring-public.json','--review',tamper/'evidence/reviews/review-001/receipt.json','--upstream',UP,'--bundle',bad_bundle,'--dist',bad_dist],expected=2,reason='sealed original or portable source-readiness record changed')
assert not bad_bundle.parent.exists()

bad_bundle=OUT/'overlap-prohibited/bundle'
run('17-public-overlap-refusal',[PY,'-B',APP/'package_release.py','build',*base_args,'--bundle',bad_bundle,'--dist',bad_bundle/'dist'],expected=2,reason='archive output/checksum overlaps the bundle')
assert not bad_bundle.parent.exists()

# Only packaging code, guide, revision labels and inventories change; display/source payloads are conserved.
conserved=['model.json','carrier.json','graph.json','coverage.json','result.json','records.json','records.html','records-graph.json','graph.html','view-scope.json','SOURCE-READINESS.md','codec/ac_graph.py','source-manifest.json','package-custody.json','source-classification.json','evidence/authoring-public.json','evidence/reviews/review-001/receipt.json']
conserved += [p.relative_to(OLD).as_posix() for p in sorted((OLD/'source-view').rglob('*')) if p.is_file()]
conserved += [p.relative_to(OLD).as_posix() for p in sorted((OLD/'source').rglob('*')) if p.is_file()]
conserved += [p.relative_to(OLD).as_posix() for p in sorted((OLD/'release_tools/vendor').rglob('*')) if p.is_file()]
conserved += [p.relative_to(OLD).as_posix() for p in sorted((OLD/'evidence/reviews/review-001').glob('*.md'))]
for name in conserved:assert (first/name).read_bytes()==(OLD/name).read_bytes(),name
scope=json.loads((first/'view-scope.json').read_text()); assert len(scope['included'])==1987 and len(scope['omitted'])==0
save(PROOF/'18-static-display-source-evidence-conservation.json',{'all_selected_files_byte_equal_to_original_delivered_artifact':True,'conserved_paths':conserved,'displayed_records':1987,'omitted_records':0,'interactive_behavior':'UNVERIFIED; no browser/server/headless activity','static_javascript_and_html_payloads':'Byte-conserved from the already statically checked artifact; no new interactive qualification claim'})
operations.append({'operation':'18-static-display-source-evidence-conservation','outcome':'passed','selected_conserved_files':len(conserved)})
save(PROOF/'first-bundle-files.json',first_vector)
save(PROOF/'summary.json',{'status':'all_selected_actual_controls_passed','artifact':ID,'archive':{'path':str(archive),'bytes':archive.stat().st_size,'sha256':sha(archive)},'bundle':{'path':str(first_bundle),'files':len(first_vector),'bytes':sum(x['bytes'] for x in first_vector)},'second_generation_archive':{'path':str(second_archive),'bytes':second_archive.stat().st_size,'sha256':sha(second_archive)},'model_canonical_sha256':MODEL_SHA,'raw_model_recovered_sha256':RAW_MODEL_SHA,'operations':operations,'source_model_receipts_and_display_conserved':True,'interactive_behavior':'UNVERIFIED','independence':'Author self-controls only; nonauthor assessment downstream'})
print('CLOSED_ACTUAL '+json.dumps({'archive_sha256':sha(archive),'archive_bytes':archive.stat().st_size,'bundle_files':len(first_vector),'bundle_bytes':sum(x['bytes'] for x in first_vector),'second_generation_exact':True}),flush=True)
