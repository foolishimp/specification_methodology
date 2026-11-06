from pathlib import Path
import hashlib,json,os,stat,subprocess,time
R=Path('/Users/jim/src/apps/specification_methodology');B=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY';O=Path(__file__).parent
sha=lambda x:hashlib.sha256(x).hexdigest()
def get(p):return json.loads(p.read_bytes())
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def save(n,v):(O/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def check(row):
 p=Path(row['path']);p=p if p.is_absolute() else R/p;raw=p.read_bytes();assert sha(raw)==row['sha256'];assert len(raw)==row['bytes'];return p
p=B/'native-recovery-execution-019/HANDOFF.json';assert sha(p.read_bytes())=='8fbbefa09eb50d4de5e45a678d5f734acb80c23366913fae4ee924465a678b17';h=get(p)
A=h['native_commit'];C=h['source_checkpoint'];tag=h['native_tag'];native=Path(h['native_root']); prefix='specification_methodology/v3';source='specification_methodology/v3/build_tenants/common'
assert C=='ec0c09474a1d42084ddd1ba2b97c9479affb0220' and A=='ef1af5c6f2aab90c7042266e4d5f6047029c2827'
assert git('rev-parse',tag).decode().strip()==h['native_tag_object']=='d40a147f5b2e5f5cd638c71646232e0d4df95249'
assert git('rev-parse',tag+'^{commit}').decode().strip()==A
assert git('show','-s','--format=%P',A).decode().strip()=='16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'
assert git('rev-parse',A+'^{tree}').decode().strip()==h['native_root_tree']
assert git('rev-parse',C+':'+source).decode().strip()==h['source_package_tree']==git('rev-parse',A+':'+prefix).decode().strip()
annotation=git('cat-file','-p',tag);header,message=annotation.split(b'\n\n',1)
assert ('object '+A).encode() in header.splitlines()
assert message==(B/'native-release/cut-003/tag-message.txt').read_bytes()
trailers={'Frozen-Source-Commit':C,'Frozen-Source-Path':source,'Frozen-Source-Tree':h['source_package_tree'],'Predecessor-Native-Commit':'16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'}
for k,v in trailers.items():assert (k+': '+v).encode() in message.splitlines()
assert b'STDO-Release-Profile: stable-v1' in message.splitlines()
inv=get(B/'cohort-recovery-019/NATIVE_INPUT_INVENTORY.json')['files'];expected={prefix+'/'+r['path']:(r['git_mode'],'blob',r['git_blob']) for r in inv}
actual={}
for rec in git('ls-tree','-rz',A).split(b'\0'):
 if not rec:continue
 meta,name=rec.split(b'\t',1);actual[name.decode()]=tuple(meta.decode().split())
assert actual==expected
manifestpath=check(h['native_manifest']); assert (native/'manifest.json').read_bytes()==manifestpath.read_bytes()
rows=inv+[{'path':'manifest.json','sha256':h['native_manifest']['sha256'],'bytes':h['native_manifest']['bytes'],'git_mode':'100644'}]
def snapshot():
 result={}
 for row in rows:
  q=native/row['path'];st=q.lstat();assert stat.S_ISREG(st.st_mode)
  raw=q.read_bytes();assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
  result[row['path']]={'sha256':sha(raw),'bytes':len(raw),'mode':stat.S_IMODE(st.st_mode),'mtime_ns':st.st_mtime_ns}
 assert {x.relative_to(native).as_posix() for x in native.rglob('*') if x.is_file()}==set(result)
 assert not any(x.is_symlink() for x in native.rglob('*'))
 return result
before=snapshot();save('INSTALLED_BEFORE.json',before)
check(h['manager']['manager']);source_match=get(check(h['manager']['source_match']));identities=get(check(h['manager']['identities']))
manager_python=Path(h['manager']['python']['invocation'])
sourcecheck="import stdo_toolchain, json; print(json.dumps({'module':stdo_toolchain.__file__,'version':stdo_toolchain.__version__}))"
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
probe=subprocess.run([str(manager_python),'-B','-c',sourcecheck],capture_output=True,cwd=O,env=env);assert probe.returncode==0
mp=json.loads(probe.stdout);assert mp['version']=='3.0.5';manager_root=Path(mp['module']).parent
managerfiles=list((R/'specification_methodology/v2/src/stdo_toolchain').rglob('*.py'));assert len(managerfiles)==13
for q in managerfiles:assert q.read_bytes()==(manager_root/q.relative_to(R/'specification_methodology/v2/src/stdo_toolchain')).read_bytes()
cmd=[h['manager']['manager']['path'],'--store',h['store'],'verify','v3.0.5','--manifest-sha256',h['native_manifest']['sha256']]
t=time.monotonic();run=subprocess.run(cmd,cwd=O,env=env,capture_output=True);elapsed=time.monotonic()-t
(O/'manager-verify.stdout').write_bytes(run.stdout);(O/'manager-verify.stderr').write_bytes(run.stderr)
assert run.returncode==0;v=json.loads(run.stdout);assert v['valid'] is True and v['failures']==[]
after=snapshot();assert before==after
report={'kind':'stdo305.independent-native-followthrough/1','assessor':'/root/stdo305_integration_review','conclusion':'satisfied','findings':[],
'handoff_sha256':sha(p.read_bytes()),'source_checkpoint':C,'source_package_tree':h['source_package_tree'],'native_commit':A,'native_tag_object':h['native_tag_object'],'native_root_tree':h['native_root_tree'],'native_manifest_sha256':h['native_manifest']['sha256'],'actual_annotation_sha256':sha(annotation),'actual_annotation':annotation.decode(),'sole_parent':'16bc30d215915a4b7b3ed2f13e52e14510ae1c9d','native171_tree_equals_reviewed_inventory':True,'installed172_exact_before_after':True,'manager13_sources_exact':True,'manager_invocation':cmd,'manager_result':{'returncode':run.returncode,'valid':v['valid'],'failures':v['failures'],'elapsed_seconds':elapsed,'stdout_sha256':sha(run.stdout),'stderr_sha256':sha(run.stderr)},'limits':['Read-only native/tag/source relation and local installation, not final complete runtime/host/public qualification.','No repository changes, Git effects, compiler/Lean/support scan.','Browser observation recorded separately at actual local003 paths.']}
save('NATIVE_CHECK.json',report);print(json.dumps({'status':'satisfied','native_files':len(rows),'manager_verify_seconds':elapsed,'report':str(O/'NATIVE_CHECK.json'),'report_sha256':sha((O/'NATIVE_CHECK.json').read_bytes())}))
