from pathlib import Path
import subprocess,hashlib,json,shutil
w=Path(__file__).resolve().parent;r=w.parents[2];m=w/'manager-checks';m.mkdir();a=w/'assets';a.mkdir();src=w/'manager-source';src.mkdir()
for n in ['pyproject.toml','README.md','LICENSE','src']:
 s=r/'specification_methodology/v2'/n
 if s.is_dir():shutil.copytree(s,src/n,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.egg-info'))
 else:shutil.copy2(s,src/n)
commands=[]
def run(name,argv):
 p=subprocess.run(list(map(str,argv)),cwd=r,capture_output=True);(m/(name+'.stdout')).write_bytes(p.stdout);(m/(name+'.stderr')).write_bytes(p.stderr);commands.append({'name':name,'argv':list(map(str,argv)),'exit':p.returncode});(m/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(name,p.returncode,flush=True);p.check_returncode()
run('wheel',['/opt/homebrew/bin/python3.13','-m','pip','wheel','--no-deps','--wheel-dir',a,src])
pre=Path('/Users/jim/src/apps/specification_methodology-3.1-rc2/.ai-workspace/work/STDO_3_1_RC2_2026-11-15/assets/stdo-manager-runtime-v3.1.0-rc.2-macos-arm64-cp313.zip');assert hashlib.sha256(pre.read_bytes()).hexdigest()=='f542be7b025bc5d178925a5c3503d5ca884c5f6a86dd3688885dfd944a73b25e'
run('runtime',['python3','-B',r/'releases/3.1.0-rc.3/tools/runtime_bundle.py','--predecessor',pre,'--wheel',a/'stdo_toolchain-3.1.0rc3-py3-none-any.whl','--out',a/'runtime-build'])
shutil.copy2(a/'runtime-build/constraints-python313.txt',a/'stdo-manager-constraints-v3.1.0-rc.3-python313.txt')
run('venv',['/opt/homebrew/bin/python3.13','-m','venv',w/'manager'])
py=w/'manager/bin/python'
run('offline-install',[py,'-m','pip','install','--no-index','--find-links',a/'runtime-build/wheels','--require-hashes','--no-deps','-r',a/'runtime-build/requirements-macos-arm64-cp313.txt'])
run('pip-check',[py,'-m','pip','check']);run('version',[w/'manager/bin/stdo','--version'])
print('Manager build and isolated offline install passed')
