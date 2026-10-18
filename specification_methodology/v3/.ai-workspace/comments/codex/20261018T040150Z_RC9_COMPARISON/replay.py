import os
import json,hashlib,subprocess,pathlib,shutil,time,os,re
from stdo_toolchain.manifest import verify_materialization,standards_member_set_sha256
base=pathlib.Path(os.environ['STDO_RC9_REPLAY_ROOT']); cl=base/'claude/specification_methodology/v3/build_tenants/claude'; cx=base/'codex/specification_methodology/v3/build_tenants/codex/successor'
py='/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python'; checker=base/'axiom_indexer/build_tenants/core/code/ac.py'; theory=pathlib.Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
results=[]
def run(name,args,cwd=None):
 t=time.monotonic(); p=subprocess.run(args,cwd=cwd,capture_output=True,text=True); r={'name':name,'command':args,'exit':p.returncode,'seconds':round(time.monotonic()-t,3),'stdout':p.stdout,'stderr':p.stderr};results.append(r);print(name,p.returncode,p.stdout[:500],p.stderr[:200]);return p
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
# Compare generation to frozen bytes, never to a claim in a receipt.
cl_initial={str(p.relative_to(cl)):sha(p) for p in (cl/'a_c/i3').rglob('*') if p.is_file()}
run('claude_assemble_check',[py,'-I','a_c/i3/tools/assemble.py','--check'],cl)
run('claude_frames_check',[py,'-I','qualification/instruments/generate_frames.py','--check'],cl)
run('claude_build_fragments',[py,'-I','a_c/i3/tools/build_fragments.py','--dispositions'],cl)
run('claude_assemble',[py,'-I','a_c/i3/tools/assemble.py'],cl)
changes=[p for p,h in cl_initial.items() if sha(cl/p)!=h]
results.append({'name':'claude_regeneration_comparison','changed_files':changes});print('claude_regeneration_changes',changes)
# Materialize only the released manifest set, then call the actual installed verifier.
m=json.loads((cl/'release/manifest.json').read_text()); installed=base/'claude-manifest-set';installed.mkdir()
for root,rows in [('standards',m['standards']['members']),('plugins/spec',m['auxiliary']['plugin']['members'])]:
 for row in rows:
  src=cl/root/row['path'];dst=installed/root/row['path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
for src,dst in [('LICENSE','LICENSE'),('release/release-note.md','release/release-note.md'),('release/manifest.json','manifest.json')]:
 (installed/dst).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(cl/src,installed/dst)
failures=verify_materialization(installed,m)
r={'name':'claude_actual_materialization_verifier','files':sum(p.is_file() for p in installed.rglob('*')),'failures':failures,'declared_member_set_sha256':m['standards']['member_set_sha256'],'required_member_set_sha256':standards_member_set_sha256(m['standards']['members'])};results.append(r);print(json.dumps(r))
# Published Codex binding and native checker acquisition; external RC2 stays a distinct verified basis.
p=run('codex_published_bindings',[py,'-B',str(cx/'interpretation/bindings.py'),'--theory-root',str(theory)],cx)
(base/'codex-bindings.json').write_text(p.stdout)
run('codex_native_validate',[py,'-B',str(checker),'validate','--program',str(cx/'interpretation/program.json'),'--bindings',str(base/'codex-bindings.json'),'--output',str(base/'codex-validation.json'),'--emit-map',str(base/'codex-map.json')],cx)
results.append({'name':'codex_native_map_reproduction','same':(base/'codex-map.json').read_bytes()==(cx/'interpretation/map.json').read_bytes()})
# For Claude use its published bindings without alteration: captures machine-path dependence separately.
run('claude_native_validate',[py,'-B',str(checker),'validate','--program',str(cl/'a_c/i3/axiomatic-program.json'),'--bindings',str(cl/'a_c/i3/bindings.json'),'--output',str(base/'claude-validation.json'),'--emit-map',str(base/'claude-map.json')],cl)
results.append({'name':'claude_native_map_reproduction','same':(base/'claude-map.json').read_bytes()==(cl/'a_c/i3/logical-constraint-map.json').read_bytes()})
(base/'replay-results.json').write_text(json.dumps(results,indent=2))
print('REPORT',base/'replay-results.json')
