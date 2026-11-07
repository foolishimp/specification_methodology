import hashlib,json,os,shutil,subprocess,tempfile,time,zipfile
from pathlib import Path
R=Path.cwd();O=Path(__file__).resolve().parent;D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/manager';PY='/opt/homebrew/opt/python@3.13/bin/python3.13';C='32567ff27a6a2e86ebce7a4e949729881372a1ab';V='3.0.5-rc.1';PV='3.0.5rc1';sha=lambda b:hashlib.sha256(b).hexdigest()
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
def ref(p):
 b=p.read_bytes();return {'path':p.relative_to(R).as_posix(),'sha256':sha(b),'bytes':len(b)}
work=Path(tempfile.mkdtemp(prefix='stdo-rc1-manager-build-')).resolve();source=work/'source';source.mkdir();selection=json.loads((D/'selection.json').read_bytes());members=[]
for row in selection['source_members']:
 p=R/row['path'];raw=p.read_bytes();frozen=subprocess.check_output(['git','--no-optional-locks','show',C+':'+row['path']]);assert raw==frozen;q=source/p.relative_to(R/'specification_methodology/v2');q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(raw);members.append(ref(p))
requirements=json.loads((D/'build.json').read_bytes())['build_dependency_artifacts']
for row in requirements:assert sha((D/'build-wheels'/row['name']).read_bytes())==row['sha256']
sel={'kind':'stdo.manager-build-selection/1','release_version':V,'python_distribution_version':PV,'source_commit':C,'source_members':members,'build_root':str(work),'build_dependency_artifacts':requirements};save(O/'SELECTION.json',sel)
env=dict(os.environ);env['PIP_DISABLE_PIP_VERSION_CHECK']='1';env['PYTHONDONTWRITEBYTECODE']='1';env['SOURCE_DATE_EPOCH']=subprocess.check_output(['git','show','-s','--format=%ct',C]).decode().strip()
commands=[('venv',[PY,'-m','venv',str(work/'venv')]),('build-dependencies',[str(work/'venv/bin/python'),'-m','pip','install','--no-index','--find-links',str(D/'build-wheels'),'setuptools==75.8.0','wheel==0.45.1']),('wheel',[str(work/'venv/bin/python'),'-m','pip','wheel','--no-index','--no-build-isolation','--no-deps','--wheel-dir',str(O/'dist'),str(source)])]
records=[]
for name,argv in commands:
 start=time.monotonic();p=subprocess.run(argv,cwd=R,env=env,capture_output=True,timeout=120);(O/(name+'.stdout')).write_bytes(p.stdout);(O/(name+'.stderr')).write_bytes(p.stderr);record={'argv':argv,'cwd':str(R),'returncode':p.returncode,'elapsed_seconds':time.monotonic()-start,'stdout':ref(O/(name+'.stdout')),'stderr':ref(O/(name+'.stderr'))};save(O/(name+'.json'),record);records.append(record);assert p.returncode==0,p.stderr.decode()
wheel=O/'dist'/f'stdo_toolchain-{PV}-py3-none-any.whl'
with zipfile.ZipFile(wheel) as z:
 files={name:z.read(name) for name in z.namelist() if name.startswith('stdo_toolchain/') and not name.endswith('/')};assert len(files)==13
 for name,raw in files.items():assert raw==(source/'src'/name).read_bytes()
 metadata=z.read('stdo_toolchain-'+PV+'.dist-info/METADATA').decode();assert '\nVersion: '+PV+'\n' in metadata
oldzip=D/'dist/stdo-manager-runtime-v3.0.5-macos-arm64-cp313.zip'
with zipfile.ZipFile(oldzip) as z:runtime={name:z.read(name) for name in z.namelist()}
oldwheel='wheels/stdo_toolchain-3.0.5-py3-none-any.whl';old_sha=sha(runtime.pop(oldwheel));newwheel='wheels/'+wheel.name;runtime[newwheel]=wheel.read_bytes()
x=json.loads(runtime['WHEELS.json']);x['version']=V;x['python_distribution_version']=PV
for row in x['members']:
 if row['name']=='stdo-toolchain':row.update(version=PV,path=newwheel,sha256=sha(wheel.read_bytes()),bytes=wheel.stat().st_size)
runtime['WHEELS.json']=(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();runtime['requirements-macos-arm64-cp313.txt']=runtime['requirements-macos-arm64-cp313.txt'].replace(('stdo-toolchain==3.0.5 --hash=sha256:'+old_sha).encode(),('stdo-toolchain=='+PV+' --hash=sha256:'+sha(wheel.read_bytes())).encode())
readme=runtime['README.md'].decode().replace('3.0.5',V).replace('stdo_toolchain-'+V,'stdo_toolchain-'+PV);readme+='\nRelease version '+V+' maps explicitly to Python distribution version '+PV+' (PEP440). Third-party versions remain independent.\n';runtime['README.md']=readme.encode()
assert len(runtime)==25 and len(x['members'])==21
for row in x['members']:assert sha(runtime[row['path']])==row['sha256'] and len(runtime[row['path']])==row['bytes']
artifact=O/'dist'/f'stdo-manager-runtime-v{V}-macos-arm64-cp313.zip'
with zipfile.ZipFile(artifact,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,raw in sorted(runtime.items()):
  entry=zipfile.ZipInfo(name,(1980,1,1,0,0,0));entry.create_system=3;entry.external_attr=0o100644<<16;z.writestr(entry,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
constraints=O/'dist'/f'stdo-manager-constraints-v{V}-python313.txt';constraints.write_bytes(runtime['constraints-python313.txt']);save(O/'BUILD.json',{'status':'built_and_source_matched','source_selection':ref(O/'SELECTION.json'),'wheel':ref(wheel),'runtime_archive':ref(artifact),'constraints':ref(constraints),'package_sources':13,'runtime_members':25,'distributions':21,'operations':records,'acquisition':'Existing exact build/dependency wheels reused as immutable artifacts; no existing environment or manager installation reused.'})
print('MANAGER_BUILT',sha(wheel.read_bytes()),sha(artifact.read_bytes()),flush=True)
