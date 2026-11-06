from pathlib import Path
import json,os,shutil,time
import run_observed as o
p=Path(__file__).absolute().parent;h=json.loads((p/'SELECTED_HANDOFF.json').read_bytes());b=Path(h['workspace']);native=Path(h['native_root']);ac=b/'runtime/a_c';lean=ac/'build_tenants/lean';py=json.loads((b/'dependencies/graphify/RUNTIME.json').read_bytes())['python']
assert o.sha(ac/'build_tenants/lean/scripts/formal_gate.py')=='4fb6daab9d1b9a14be797d1595f201e3dab1f1e5800d96babb130259b1234b2c'
source=o.REPO/'a_c/build_tenants/lean/.toolchain/lean-4.35.0-darwin_aarch64.tar.zst';destination=lean/'.toolchain'/source.name
assert source.is_file() and o.sha(source)=='c0c6f34f35ba1dcc5c4a5fd106fefab9eb5e8469712624dd2c868d51b63177c2'
destination.parent.mkdir(exist_ok=False);shutil.copyfile(source,destination);assert o.sha(destination)==o.sha(source) and not os.path.samefile(source,destination)
(p/'COMPILER_CACHE_CUSTODY.json').write_bytes(o.encoded({'schema':'stdo305.immutable-dependency-copy/1','source':str(source),'destination':str(destination),'bytes':destination.stat().st_size,'sha256':o.sha(destination),'source_inode':source.stat().st_ino,'destination_inode':destination.stat().st_ino,'samefile':False,'standing':'Exact immutable archive only; fresh bootstrap/support/currentness follows. No old runtime/support/origin/verdict copied.'}))
receipt,result=o.run('bootstrap-lean',[py,'-B',native/'standards/tooling/setup.py','bootstrap-lean','--derivation',b/'runtime/prepared.json','--derivation-sha256',o.sha(b/'runtime/prepared.json'),'--python',py,'--output',b/'runtime/bootstrap'],'specification_methodology/v3/build_tenants/common-tools/tooling_setup.py',inputs=[b/'runtime/prepared.json'],output_tree=b/'runtime/bootstrap',output_files=[lean/'profiles/proof-support-v1.json'])
assert receipt['execution']['returncode']==0 and result['status']=='support-established',receipt
receipt,result=o.run('formal-origin',[py,'-I','-S','-B',lean/'scripts/formal_gate.py','init-origin'],'a_c/build_tenants/lean/scripts/formal_gate.py',output_files=[lean/'.cache/formal-origin-v1/selection.json'])
assert receipt['execution']['returncode']==0,receipt
(b/'formal').mkdir(exist_ok=False)
receipt,result=o.run('formal-checker-selection',[py,'-B',ac/'scripts/ac.py','formal-select','--lean-root',lean,'--python',py,'--timeout-seconds','7200','--output',b/'formal/checker.json'],'a_c/scripts/ac.py',output_files=[b/'formal/checker.json'])
assert receipt['execution']['returncode']==0,receipt
checker=json.loads((b/'formal/checker.json').read_bytes());assert checker['timeout_seconds']==7200 and checker['runtime_identity']['pins']['scripts/formal_gate.py']=='4fb6daab9d1b9a14be797d1595f201e3dab1f1e5800d96babb130259b1234b2c'
print(json.dumps({'status':'fresh_support_origin_checker_ready','derivation':o.ref(b/'runtime/bootstrap/derivation.json'),'runtime':checker['runtime_identity']['sha256'],'checker':o.ref(b/'formal/checker.json')}),flush=True)
