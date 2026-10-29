#!/usr/bin/env python3
"""Independent custody/transport reader. No gate, compiler, actor or support execution."""
from pathlib import Path,PurePosixPath
import ast,difflib,gzip,hashlib,io,json,tarfile
W=Path(__file__).resolve().parents[2];R=Path(__file__).resolve().parent;REPO=W.parents[3]
D=W/'package/delivery-002';S=W/'package/selection-002';T=W/'checkpoint/evidence-transport-002';OLD=W/'checkpoint/evidence-transport-001'
COLD=W/'real-use/runtime-preparation-001/execution/evidence/formal/9c7303aa2c844d439da9f3eb32b8543f/bundle';E=D/'installed-29-evidence'
def load(p):return json.loads(p.read_bytes())
def rawsha(b):return hashlib.sha256(b).hexdigest()
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
checks={}
for root,pin in [(D,'ed51396f3478b6e4082a4075be8150cbefb8d980630f11c5e93ff5a5fb4553ab'),(S,'f6d54d2a94c8b8c9ca6f0486836629d620d8fa4da06d47be091b9246e04bfbe3'),(T,'399691bfb2736cf297766ea3d5479068c9e9f5bac1ea8808325510289513fd7b')]:
 assert sha(root/'CLOSED.json')==pin
 pins=load(root/'PINS.json'); rows=pins.get('members')
 if rows is not None:
  for name,h in rows.items():assert sha(root/name)==h,(root,name)
 else:
  for row in pins['files']:assert sha(root/row['path'])==row['sha256'] and (root/row['path']).stat().st_size==row['bytes']
 checks[str(root.relative_to(W))]={'closure':pin,'pins_sha256':sha(root/'PINS.json')}
manifest=load(D/'SOURCE_PACKAGE.json');assert manifest==load(S/'SOURCE_PACKAGE.json');assert sha(D/'SOURCE_PACKAGE.json')=='4e0d67ffadc9f54f6d54c2c6391123148d28608dab534ed7e5a34a84aba3a506'
assert len(manifest['files'])==66
portable=manifest['portable_runtime_identity'];full=manifest['freeze']['runtime_identity'];origin='.cache/formal-origin-v1/selection.json'
assert set(full['pins'])-set(portable['pins'])=={origin} and {k:v for k,v in full['pins'].items() if k!=origin}==portable['pins']
assert rawsha(canonical(portable['pins']))==portable['sha256']=='4f9e8402122f1722559a4bb7d7559b09ce107f8de8a38de600aedc947611072d'
assert sha(S/'package_source.py')==sha(W/'package/repair-002/package_source.py') and sha(S/'test_package_source.py')==sha(W/'package/repair-002/test_package_source.py')
rows={r['path']:r for r in manifest['files']};assert len(rows)==66 and len({s.casefold() for s in rows})==66
ban={'.cache','.lake','.toolchain','.git','formal-origin-v1','keys','entries'}
installed=Path('/private/tmp/ac-t013-lean-package-002/operational');pristine=installed.parent/'pristine'
for name,row in rows.items():
 assert not any(part in ('.','..','') for part in name.split('/')) and not name.startswith('/') and not (set(p.casefold() for p in PurePosixPath(name).parts)&ban)
 for path in (REPO/row['source'],pristine/name,installed/name):assert not path.is_symlink() and sha(path)==row['sha256'] and path.stat().st_size==row['bytes'],str(path)
assert sorted(p.relative_to(pristine).as_posix() for p in pristine.rglob('*') if p.is_file())==sorted([*rows,'SOURCE_PACKAGE.json'])
archive=D/'source-package.tar';assert sha(archive)=='5c150ab0802fbdc8efbbd30cbff5ad2fe6be2241217da42408be6f9e658b30c1'
with tarfile.open(archive,'r:') as tf:
 members=tf.getmembers();assert [m.name for m in members]==sorted([*rows,'SOURCE_PACKAGE.json'])
 for m in members:
  assert m.type==tarfile.REGTYPE and m.uid==m.gid==m.mtime==0 and m.mode==0o644 and m.uname==m.gname=='' and not m.linkname
  payload=tf.extractfile(m).read();expect=sha(D/'SOURCE_PACKAGE.json') if m.name=='SOURCE_PACKAGE.json' else rows[m.name]['sha256'];assert rawsha(payload)==expect
# Independent in-memory reconstruction from untouched extracted files; no packager call.
repacked=io.BytesIO()
with tarfile.open(fileobj=repacked,mode='w',format=tarfile.PAX_FORMAT) as tf:
 for name in sorted([*rows,'SOURCE_PACKAGE.json']):
  data=(pristine/name).read_bytes();ti=tarfile.TarInfo(name);ti.size=len(data);ti.mode=0o644;ti.mtime=0;ti.uid=ti.gid=0;ti.uname=ti.gname='';tf.addfile(ti,io.BytesIO(data))
assert rawsha(repacked.getvalue())==sha(archive)
support=load(installed/'a_c/build_tenants/lean/profiles/proof-support-v1.json');custody=load(D/'SUPPORT-CUSTODY.json');assert {r['path']:r['sha256'] for r in custody['rows']}==support['members'];assert len(custody['rows'])==30405
assert sum(r['action']=='copied-absent-runtime-member' for r in custody['rows'])==30399
assert sum(r['bytes'] for r in custody['rows'] if r['action']=='copied-absent-runtime-member')==3254927206
assert not (installed/'a_c/build_tenants/lean/.cache/formal-origin-v1').exists()
result=load(E/'result.json');prior=load(COLD/'result.json');external=load(D/'installed-29-fallback.external.json')
assert sha(E/'result.json')=='5c5f5289353968fdf454a19c85014ee86f39b48a1af8241fc18357ef159168ce'
assert result['status']=='verified' and result['runtime_identity']==portable and load(D/'installed-identity.stdout')==portable
for k in ('inputs','model','context_binding','selections','requested_claims','checked_claims','limits'):assert result[k]==prior[k],k
assert result['requested_claims']==result['checked_claims']
assert result==load(D/'installed-29-fallback.stdout')
assert load(D/'INSTALLED-CHECKER.json')['root']==str(installed/'a_c/build_tenants/lean') and load(D/'INSTALLED-CHECKER.json')['runtime_identity']==portable
for name,h in load(E/'manifest.json')['members'].items():
 if '.olean' in name or '.ir' in name:continue
 assert sha(E/name)==h
assert sha(E/'manifest.json')==result['evidence']['manifest_sha256']=='072176fee176cbfad7704dd6c3b7bd5e7e363e6700a9039e46f10755de20c3ca'
for name in ['input.json','supplied-views.json','actual-runtime.log',*[p.name for p in E.glob('*.lean')]]:assert (E/name).read_bytes()==(COLD/name).read_bytes(),name
obs=result['observations'];assert obs['theorem_audit']==prior['observations']['theorem_audit'] and len(obs['theorem_audit'])==62
assert (obs['current_dynamic_proof_invocations'],obs['current_kernel_replay_invocations'],obs['current_runtime_invocations'])==(7,1,1)
assert obs['reuse'].startswith('none; fresh dynamic obligations') and not (E/'local-origin.json').exists() and external['returncode']==0 and external['status']=='PASS'
assert all(s.get('exit_code',0)==0 for s in obs['stages']) and obs['limits']==prior['observations']['limits']
checks['package']={'source_members':66,'archive_members':67,'archive_sha256':sha(archive),'independent_in_memory_pristine_repack_equal':True,'all_source_pristine_operational_file_hashes_equal':True,'only_portability_exception':origin,'installed_result_sha256':sha(E/'result.json'),'installed_identity':portable['sha256'],'whole_seconds':external['external_invocation_seconds'],'checking_seconds':obs['elapsed_seconds'],'current_proof_replay_runtime':[7,1,1],'generated_sources_and_actual_runtime_equal_to_independently_reviewed_actual_phase_a':True,'support_rows_equal_conserved_map':30405,'support_binary_recensus_performed':False,'private_origin_or_hint_present':False}
# Transport delta is the exact finite whitelist plus one disjunction; all other mechanics conserved.
old=OLD/'transport.py';new=T/'transport.py';guard=load(T/'GUARD-SELECTION.json');assert sha(old)==guard['base_source_sha256'] and sha(new)==guard['successor_source_sha256']
tree=ast.parse(new.read_text());node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(a,ast.Name) and a.id=='EXACT_COMPILED_ALIASES' for a in n.targets));aliases=ast.literal_eval(node.value.args[0]);assert sorted(aliases)==guard['aliases'] and len(aliases)==10
text=new.read_text();start=text.index('# Exact T013 public evidence aliases');end=text.index('\n\ndef need',start);normalized=text[:start]+text[end+1:];normalized=normalized.replace('need((parts[0] in ("lean", "reuse") and name.endswith(".olean.private"))\n             or name in EXACT_COMPILED_ALIASES,','need(parts[0] in ("lean", "reuse") and name.endswith(".olean.private"),')
assert normalized==old.read_text()
selected=load(T/'SELECTED.json');transport=load(T/'payload/MANIFEST.json');assert transport['files']==selected['files'] and transport['selection_sha256']==sha(T/'SELECTED.json');assert len(transport['files'])==24
verified_payloads={}
for payload in transport['payloads']:
 p=T/'payload'/payload['path'];assert sha(p)==payload['sha256'] and p.stat().st_size==payload['bytes'] and sha(OLD/'payload'/payload['path'])==sha(p)
 h=hashlib.sha256();size=0
 with gzip.open(p,'rb') as stream:
  while block:=stream.read(1024*1024):h.update(block);size+=len(block);assert size<=payload['raw_bytes']
 assert h.hexdigest()==payload['raw_sha256'] and size==payload['raw_bytes'];verified_payloads[payload['raw_sha256']]=size
for row in transport['files']:
 assert verified_payloads[row['sha256']]==row['bytes'];assert (W/row['path']).stat().st_size==row['bytes']
for pin in selected['historical_pins']:
 source=W/pin['pin_source'];assert sha(source)==pin['pin_source_sha256']
 if pin['declared_member_sha256'] is not None:
  m=load(source)['members'];assert m[Path(pin['member_path']).name]==pin['declared_member_sha256']
 else:assert pin['member_path'].startswith('lean/correction-011/') and 'not an existing compiled-member pin' in pin['standing']
coverage=load(T/'COVERAGE.json');ignore=(W/'.gitignore').read_bytes();assert rawsha(ignore)==coverage['ignore_after_sha256'];tail=coverage['exact_appended_text'].encode();assert ignore.endswith(tail) and rawsha(ignore[:-len(tail)])==coverage['ignore_before_sha256'];assert sorted(line[1:] for line in coverage['exact_appended_text'].splitlines() if line.startswith('/'))==coverage['new_exact_aliases']
assert set(aliases)=={row['path'] for row in transport['files'] if row['path'].split('/')[0] in ('real-use','package')}
roundtrip=load(T/'ROUNDTRIP.json');assert roundtrip['all_restored_files_compared_byte_for_byte_and_sha256']==24 and roundtrip['repeat_inode_mtime_preserved'] and roundtrip['original_inode_mtime_preserved']
checks['transport']={'source_guard_only_delta':True,'new_literal_aliases':10,'mapped_files':24,'unique_payloads':len(verified_payloads),'raw_unique_bytes':sum(verified_payloads.values()),'mapped_raw_bytes':sum(r['bytes'] for r in transport['files']),'compressed_unique_bytes':sum(p['bytes'] for p in transport['payloads']),'payloads_match_prior_and_independently_decompress_to_exact_raw_hashes':True,'exact_new_ignore_paths':14,'author_roundtrip_each_alias':24,'original_compiled_alias_rehash_performed':False,'prior_transport_untouched':True}
(R/'CHECKS.json').write_text(json.dumps(checks,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','package':checks['package'],'transport':checks['transport']},indent=2))
