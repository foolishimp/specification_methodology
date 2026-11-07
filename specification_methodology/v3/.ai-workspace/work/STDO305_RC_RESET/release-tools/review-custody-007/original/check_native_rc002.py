from pathlib import Path
import hashlib,json,stat,subprocess,zipfile
R=Path('/Users/jim/src/apps/specification_methodology');D=R/'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET';O=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def load(ref):
 p=Path(ref['path']);p=p if p.is_absolute() else R/p;b=p.read_bytes();assert sha(b)==ref['sha256'] and len(b)==ref['bytes'];return json.loads(b)
def git(*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(R),*args]).decode().strip()
hraw=(D/'release-tools/native-transaction-002/HANDOFF.json').read_bytes();assert sha(hraw)=='c609ba3e1ea650c3dd9a563aaf9d32c1aa36ec684419ab607e17cf87d1c46e51';h=json.loads(hraw);native=Path(h['native_root']);m=load(h['native_manifest']);assert sha((native/'manifest.json').read_bytes())==h['native_manifest']['sha256'];assert h['transport_mode']=='local_prepublication'
assert h['native_commit']==m['release']['commit'] and h['native_tag_object']==m['release']['tag_object'] and h['native_root_tree']==m['release']['tree'];assert m['release']['cut']=='v3.0.5-rc.1'
assert git('rev-parse',h['native_tag'])==h['native_tag_object'];assert git('rev-parse',h['native_tag']+'^{commit}')==h['native_commit'];assert git('rev-list','--parents','-n','1',h['native_commit']).split()==[h['native_commit'],'16bc30d215915a4b7b3ed2f13e52e14510ae1c9d']
assert git('rev-parse',h['source_checkpoint']+':specification_methodology/v3/build_tenants/common')==git('rev-parse',h['native_commit']+':specification_methodology/v3')==h['source_package_tree']
annotation=git('cat-file','-p',h['native_tag_object']);assert 'Frozen-Source-Commit: '+h['source_checkpoint'] in annotation and 'Frozen-Source-Tree: '+h['source_package_tree'] in annotation;(O/'native-tag.txt').write_text(annotation+'\n')
delta=json.loads((D/'release-tools/anchor-repair-005/PRE_COPY_DELTA.json').read_bytes());names={r['after']['path'] for r in delta['changed']};assert len(names)==4
actual={n.removeprefix('specification_methodology/v3/') for n in git('diff','--name-only','64cf9cc8a380d429297416f7d1c19f95e513906d',h['native_commit'],'--','specification_methodology/v3').splitlines()};assert actual==names
for row in delta['changed']:
 x=row['after'];p=native/x['path'];b=p.read_bytes();assert sha(b)==x['sha256'] and len(b)==x['bytes'];assert stat.S_IMODE(p.stat().st_mode)==0o444
assert sha((native/'standards/tooling/setup.py').read_bytes())=='d5411f3377faa010c2a25afebff6e52eb5c9e083e5cc9768d0c35ccca4ea8c74'
old=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/local-001/store/releases/v3.0.5-rc.1')
t=json.loads((native/'standards/tooling/TOOLING.json').read_bytes());ot=json.loads((old/'standards/tooling/TOOLING.json').read_bytes());oldrows={x['archive_path']:x for x in ot['sources']};newrows={x['archive_path']:x for x in t['sources']};assert len(oldrows)==len(newrows)==243 and oldrows.keys()==newrows.keys();changed=[n for n in oldrows if oldrows[n]!=newrows[n]];assert changed==['stdo_representation/build_tenants/axiom_indexer/representation/stdo-v3.0.5-rc.1/source-corpus.json']
with zipfile.ZipFile(native/'standards/tooling/sources.zip') as z:
 assert len(z.namelist())==243 and set(z.namelist())==set(newrows);b=z.read(changed[0]);assert sha(b)=='bd374a3fe8f5fd30c165104c23e024cd0de5cc41eb47ac4a364d592cf62d08b3'==newrows[changed[0]]['sha256'];assert b==(R/changed[0]).read_bytes()
a=load(h['installed_byte_attestation']);assert a['exact_payload_and_manifest'] and a['files']==174 and a['manifest_sha256']==h['native_manifest']['sha256']
e=load(h['verify']);v=load(e['stdout']);assert e['returncode']==0 and v['valid'] is True and v['failures']==[] and v['manifest']==m and v['manifest_sha256']==h['native_manifest']['sha256'] and v['path']==str(native);assert e['argv']==[h['manager']['manager']['path'],'--store',h['store'],'verify','v3.0.5-rc.1','--manifest-sha256',h['native_manifest']['sha256']]
files=[p for p in native.rglob('*') if p.is_file()];assert len(files)==174 and not any(p.is_symlink() for p in native.rglob('*'))
stats=[{'path':str(p),'bytes':p.stat().st_size,'mode':oct(stat.S_IMODE(p.stat().st_mode)),'mtime_ns':p.stat().st_mtime_ns} for p in files]
result={'kind':'stdo.independent-rc-native-successor-followthrough/1','assessor':'/root/stdo305_integration_review','verdict':'satisfied','findings':[],'handoff_sha256':sha(hraw),'source_checkpoint':h['source_checkpoint'],'native_commit':h['native_commit'],'native_tag_object':h['native_tag_object'],'native_manifest_sha256':h['native_manifest']['sha256'],'native_root':str(native),'source_native_tree':h['source_package_tree'],'changed_native_members':sorted(names),'unchanged_native_members':169,'changed_archive_member':changed[0],'exact_archive_population':243,'actual_verify_receipt_sha256':h['verify']['sha256'],'attestation_sha256':h['installed_byte_attestation']['sha256'],'members':stats,'limits':['Only four changed native bytes rehashed independently. Remaining169 bytes conserved by exact Git tree comparison and actual complete manager verification/attestation, not a repeated full byte scan.','Local prepublication installation only. Runtime/proof/host/public remain separate.']}
(O/'NATIVE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'satisfied','report':str(O/'NATIVE_CHECK.json'),'sha256':sha((O/'NATIVE_CHECK.json').read_bytes())}))
