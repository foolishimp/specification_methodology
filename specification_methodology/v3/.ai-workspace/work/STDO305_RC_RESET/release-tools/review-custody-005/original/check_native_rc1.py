from pathlib import Path
import hashlib,json,stat,subprocess
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET';O=Path(__file__).parent
sha=lambda raw:hashlib.sha256(raw).hexdigest()
def load(ref):
 p=Path(ref['path']);p=p if p.is_absolute() else R/p;b=p.read_bytes();assert sha(b)==ref['sha256'] and len(b)==ref['bytes'];return json.loads(b)
def git(*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(R),*args]).decode().strip()
hraw=(D/'release-tools/native-transaction-001/HANDOFF.json').read_bytes();assert sha(hraw)=='129bc5867587eecfc6c4f7f61c0223f067faad84ddd5f9c92fa2c6e39bba8920';h=json.loads(hraw);native=Path(h['native_root']);m=load(h['native_manifest']);assert h['transport_mode']==h['acquisition']['mode']=='local_prepublication'
assert h['native_commit']==m['release']['commit'] and h['native_tag_object']==m['release']['tag_object'];assert h['native_root_tree']==m['release']['tree'];assert m['release']['cut']=='v3.0.5-rc.1'
assert git('rev-parse',h['native_tag'])==h['native_tag_object'];assert git('rev-parse',h['native_tag']+'^{commit}')==h['native_commit'];assert git('rev-parse',h['native_commit']+'^{tree}')==h['native_root_tree']
assert git('rev-list','--parents','-n','1',h['native_commit']).split()==[h['native_commit'],'16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'];assert git('rev-parse','refs/tags/specification_methodology/v3.0.4^{commit}')=='16bc30d215915a4b7b3ed2f13e52e14510ae1c9d'
assert git('rev-parse',h['source_checkpoint']+':specification_methodology/v3/build_tenants/common')==git('rev-parse',h['native_commit']+':specification_methodology/v3')==h['source_package_tree']
annotation=git('cat-file','-p',h['native_tag_object']);assert 'Frozen-Source-Commit: '+h['source_checkpoint'] in annotation and 'Frozen-Source-Tree: '+h['source_package_tree'] in annotation and 'native RC cut' in annotation
(O/'native-rc1-tag.txt').write_text(annotation+'\n')
rows=json.loads((D/'release-tools/packaging-001/NATIVE_INPUT_INVENTORY.json').read_bytes())['files'];expected={r['path']:r for r in rows};expected['manifest.json']={'path':'manifest.json','sha256':h['native_manifest']['sha256'],'bytes':h['native_manifest']['bytes'],'git_mode':'100644'}
observed=[]
for name,row in expected.items():
 p=native/name;s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_size==row['bytes'] and sha(p.read_bytes())==row['sha256'];assert stat.S_IMODE(s.st_mode)==0o444;observed.append({'path':str(p),'sha256':row['sha256'],'bytes':s.st_size,'mode':oct(stat.S_IMODE(s.st_mode)),'mtime_ns':s.st_mtime_ns})
paths=list(native.rglob('*'));assert not any(p.is_symlink() for p in paths);assert {p.relative_to(native).as_posix() for p in paths if p.is_file()}==set(expected)
a=load(h['installed_byte_attestation']);assert a['exact_payload_and_manifest'] and a['files']==len(expected)==174 and a['manifest_sha256']==h['native_manifest']['sha256']
e=load(h['verify']);v=load(e['stdout']);assert e['returncode']==0 and v['valid'] is True and v['failures']==[] and v['manifest']==m and v['manifest_sha256']==h['native_manifest']['sha256'] and v['path']==str(native)
assert e['argv']==[h['manager']['manager']['path'],'--store',h['store'],'verify','v3.0.5-rc.1','--manifest-sha256',h['native_manifest']['sha256']]
manager=load(h['manager']['source_match']);identities=load(h['manager']['identities']);assert manager['status']=='verified' and manager['version']==identities['manager_version']=='3.0.5rc1';assert {r['name']:r['version'] for r in identities['dependencies']}==h['manager']['selected_distribution_population'];assert len(manager['members'])==13
for name,digest in manager['members'].items():assert sha((Path(manager['site'])/name).read_bytes())==digest
assert sha(Path(h['manager']['manager']['path']).read_bytes())==h['manager']['manager']['sha256']
result={'kind':'stdo.independent-rc-native-followthrough/1','assessor':'/root/stdo305_integration_review','conclusion':'satisfied within actual local native/manager scope','findings':[],'source_checkpoint':h['source_checkpoint'],'native_commit':h['native_commit'],'native_tag_object':h['native_tag_object'],'native_manifest_sha256':h['native_manifest']['sha256'],'native_root':str(native),'source_native_tree_identity':h['source_package_tree'],'sole_native_parent':'16bc30d215915a4b7b3ed2f13e52e14510ae1c9d','files':len(observed),'manager_sources':len(manager['members']),'manager_distributions':len(identities['dependencies']),'actual_verify_receipt_sha256':h['verify']['sha256'],'members':observed,'limits':['Local prepublication transport only; no public claim.','Existing manager verify receipt independently checked; no install/verify rerun.','Browser, current runtime and actual installed proof remain separate pending evidence.']}
p=O/'NATIVE_CHECK.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'path':str(p),'sha256':sha(p.read_bytes()),'native_files':len(observed),'conclusion':result['conclusion']}))
