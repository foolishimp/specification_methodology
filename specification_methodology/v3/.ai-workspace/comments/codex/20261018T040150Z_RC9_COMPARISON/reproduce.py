"""Rebuild pinned local candidates in new scratch and reproduce package observations.
Run with the installed stdo-toolchain Python. This writes scratch only.
The three receipts are saved in scratch; original review receipts stay untouched.
"""
from pathlib import Path
import argparse, hashlib, io, json, os, subprocess, sys, tarfile, tempfile
ap=argparse.ArgumentParser()
ap.add_argument('--repo',default='/Users/jim/src/apps/specification_methodology')
args=ap.parse_args()
base=Path(tempfile.mkdtemp(prefix='stdo-rc9-replay-'))
subjects={
 'claude':('3a2097137c3588ba44b98e3ea801ac7f2be1daf0',['specification_methodology/v3/build_tenants/claude']),
 'codex':('c46e9f96381097245a6714164f03b72ad32116c0',['specification_methodology/v3/build_tenants/codex/successor','specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-5/tools/build_interpretation.py']),
 'checker':('9a9c479776ffd974fbcafcf48341980918209aef',['axiom_indexer/build_tenants/core/code'])}
for name,(commit,paths) in subjects.items():
 out=base if name=='checker' else base/name
 out.mkdir(parents=True,exist_ok=True)
 archive=subprocess.check_output(['git','-C',args.repo,'archive',commit,*paths])
 with tarfile.open(fileobj=io.BytesIO(archive)) as tar:tar.extractall(out,filter='data')
checker=base/'axiom_indexer/build_tenants/core/code/ac.py'
assert hashlib.sha256(checker.read_bytes()).hexdigest()=='5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8'
env=dict(os.environ,STDO_RC9_REPLAY_ROOT=str(base),PYTHONDONTWRITEBYTECODE='1')
for name in ['replay.py','controls.py','projections.py']:
 p=subprocess.run([sys.executable,'-B',str(Path(__file__).parent/name)],env=env,capture_output=True,text=True)
 (base/(name+'.stdout')).write_text(p.stdout)
 (base/(name+'.stderr')).write_text(p.stderr)
 if p.returncode: raise SystemExit(f'{name} failed: {p.stderr}; scratch={base}')
print(json.dumps({'scratch':str(base),'subjects':subjects,'receipts':['replay-results.json','controls-results.json','projection-results.json']},indent=2))
