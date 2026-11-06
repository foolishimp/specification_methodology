"""Narrow C3 evidence inventory; no proof, archive extraction or support scan."""
from pathlib import Path
import hashlib,json,os,stat,time
REPO=Path('/Users/jim/src/apps/specification_methodology')
DELIVERY=REPO/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
WORK=DELIVERY/'tools-skills'; OUT=Path(__file__).resolve().parent
GROUPS=['installed-qualification-015','installed-qualification-prep-015','formal-budget-recovery-016','formal-budget-review-016','current-formal-016','current-formal-016-preparation','installed-qualification-prep-017']
def relative(path):return Path(path).relative_to(REPO).as_posix()
def digest(path):
 with Path(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def row(path):
 path=Path(path);before=path.lstat();assert stat.S_ISREG(before.st_mode) and not path.is_symlink(),str(path)
 value={'path':relative(path),'sha256':digest(path),'bytes':before.st_size,'mode':'100755' if before.st_mode&0o111 else '100644'}
 after=path.lstat();assert (before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns),('moving file',str(path));return value
transport_path=DELIVERY/'cohort-recovery-019/archives/cold016-transport/TRANSPORT.json'
transport=json.loads(transport_path.read_text());transport_ref=row(transport_path)
cold=WORK/'current-formal-016/cold';manifest=json.loads((cold/'manifest.json').read_text())
assert digest(cold/'manifest.json')==transport['manifest_sha256']
assert transport['members']['result.json']['sha256']==digest(cold/'result.json')
assert set(transport['members'])==set(manifest['members'])|{'result.json','manifest.json'}
for name,h in manifest['members'].items():assert transport['members'][name]['sha256']==h
# This is only the nonsecret public selection, never its key or origin store.
origin=REPO/'a_c/build_tenants/lean/.cache/formal-origin-v1/selection.json';raw=origin.read_bytes();public=json.loads(raw)
assert set(public)=={'schema','origin_id','key_sha256','store_relative'} and public['schema']=='a_c.formal-gate.local-origin-selection/1'
assert hashlib.sha256(raw).hexdigest()=='a6f7cce1d1654d43c4cc7c05445a39c090e3ff4b490bf7646d8870835ae1c8af'
with (OUT/'public-origin-selection.json').open('xb') as stream:stream.write(raw)
include=[];exclude=[];populations={}
for group in GROUPS:
 root=WORK/group;files=sorted(q for q in root.rglob('*') if q.is_file() or q.is_symlink());populations[group]=len(files)
 for q in files:
  assert not q.is_symlink(),('unmapped symlink',str(q))
  if q.parent==cold and q.name in manifest['members']:
   selected=transport['members'][q.name];assert q.stat().st_size==selected['bytes']
   exclude.append({'path':relative(q),**selected,'member':q.name,'transport_descriptor':transport_ref,'reason':'Exact full raw proof archived duplicate. Original result/manifest remain selected ordinary files; all59 members recover from the complete existing61-file transport.'});continue
  if q.name=='local-origin.json':
   exclude.append({'path':relative(q),'bytes':q.stat().st_size,'reason':'Optional private local-origin lookup/custody hint excluded. The public selection is separately retained; no origin key or authentication state is selected.'});continue
  public_selection=(group=='installed-qualification-015' and q.relative_to(root).as_posix()=='observed/runtime/a_c/build_tenants/lean/.cache/formal-origin-v1/selection.json')
  if any(part in ('.git','__pycache__','.toolchain','venv') for part in q.parts) or ('.cache' in q.parts and not public_selection):
   exclude.append({'path':relative(q),'bytes':q.stat().st_size,'reason':'Private/runtime/cache byte population, not an ordinary portable evidence claim.'});continue
  entry=row(q);assert entry['bytes']<100*1024*1024,('ordinary oversized file',entry['path']);include.append(entry)
for q in (WORK/'a_c-portable-016.json',OUT/'assemble.py',OUT/'public-origin-selection.json'):include.append(row(q))
partial=[];aliases=[]
request=WORK/'installed-qualification-015/formal/request.json';request_ref=row(request)
for attempt,command in [('current-full','installed-full-current-verify'),('current-full-002','installed-full-current-verify-002')]:
 base=WORK/'installed-qualification-015/observed/formal'/attempt;result=json.loads((base/'result.json').read_text());m=json.loads((base/'manifest.json').read_text());execution=WORK/'installed-qualification-015/executions'/command/'execution.json';record=json.loads(execution.read_text());members=[]
 assert result['status']=='incomplete' and result['checked_claims']==[] and result['reason']=='GateData exceeded selected time limit'
 compiled=[name for name in m['members'] if any(name.endswith(s) for s in ('.olean','.olean.private','.olean.server','.ir','.ir.sig'))];assert not compiled
 for observed in record['execution']['outputs']:
  target=REPO/observed['path']
  if target.exists():continue
  member=target.name;assert member in m['members'] and m['members'][member]==observed['sha256']
  actual=Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-002/formal')/attempt/member
  assert actual.is_file() and actual.stat().st_size==observed['bytes']
  if member=='request.json':
   assert observed['sha256']==request_ref['sha256'] and observed['bytes']==request_ref['bytes'];recovery={'kind':'ordinary-retained-byte-alias','source':request_ref}
  else:
   assert transport['members'][member]=={'sha256':observed['sha256'],'bytes':observed['bytes']};recovery={'kind':'existing-transport-member-byte-alias','descriptor':transport_ref,'member':member}
  alias={'recorded_output':observed,'actual_external_path':str(actual),'recovery':recovery,'standing':'Recovers only the exact bytes already pinned by this incomplete execution. No successful proof status, compiled object, runtime identity or execution verdict is borrowed from016.'};members.append(alias);aliases.append(alias)
 assert len(members)==15
 partial.append({'attempt':attempt,'status':result['status'],'reason':result['reason'],'checked_claims':[],'runtime_identity':result['runtime_identity']['sha256'],'execution':row(execution),'result':row(base/'result.json'),'manifest':row(base/'manifest.json'),'generated_member_count':15,'compiled_member_count':0,'recovered_aliases':members,'validation':'Original retained execution/member hashes compared with current transport descriptor hashes; original external files observed present/size-matching. No duplicate archive or fresh proof is created.'})
# Exact diagnostic compiler outputs also coincide with already transported bytes.
diagnostic=json.loads((WORK/'formal-budget-recovery-016/RESULT.json').read_text());diagnostic_aliases=[]
for output in diagnostic['outputs']:
 names=[name for name,item in transport['members'].items() if item=={'sha256':output['sha256'],'bytes':output['bytes']}]
 assert names,('diagnostic output has no existing portable bytes',output)
 member=Path(output['path']).name if Path(output['path']).name in names else ('GateData.log' if 'GateData.log' in names else names[0])
 diagnostic_aliases.append({'actual_output':output,'recovery':{'descriptor':transport_ref,'member':member},'standing':'Byte recovery for the isolated600s compiler diagnostic only; not a whole-proof or release verdict.'})
parts=[]
for item in transport['parts']:
 path=transport_path.parent/item['path'];assert path.is_file() and not path.is_symlink() and path.stat().st_size==item['bytes'];parts.append({**item,'path':relative(path),'mode':'100755' if path.stat().st_mode&0o111 else '100644'})
unsplit=transport_path.parent.parent/'cold016.zip';assert unsplit.stat().st_size==transport['archive_bytes']
exclude.append({'path':relative(unsplit),'sha256':transport['archive_sha256'],'bytes':transport['archive_bytes'],'reason':'Oversized unsplit duplicate archive is preserved locally and excluded. Existing bounded parts reconstruct these exact archive bytes. This path belongs to the common Writer; listed as a coordinated exclusion.'})
source_alias={'recorded_source':'a_c/build_tenants/lean/scripts/formal_gate.py','recorded_sha256':'39a0527792ba6f9a08407e77350a7e68eb32ed8cea8950b8b1f5e52f8bdfabaa','retained_preimage':row(WORK/'formal-budget-recovery-016/source-before/a_c/build_tenants/lean/scripts/formal_gate.py'),'standing':'Historical015 producer pin resolves to retained exact pre-change source, not the changed live600s source. A1/A2 results are not reclassified current.'}
assert source_alias['recorded_sha256']==source_alias['retained_preimage']['sha256']
index={'schema':'stdo305.tools-skills.evidence-custody/2','status':'sealed_completed_C3_delta','scope':'Only the eight named new/updated tools evidence groups since C2; prior005/008/toy/raw exclusions continue unchanged under previous custody.','created_ns':time.time_ns(),'previous_index':row(WORK/'evidence-custody-009/INDEX.json'),'source_scope':'No Product source or external runtime changed by this pass. Current source acceptance is budget016 plus portable016; current proof/inspection have their own exact result/runtime.','include':sorted(include,key=lambda x:x['path']),'exclude':sorted(exclude,key=lambda x:x['path']),'observations':{'group_populations':populations,'included_files':len(include),'included_bytes':sum(x['bytes'] for x in include),'largest_included_bytes':max(x['bytes'] for x in include),'excluded_entries':len(exclude),'unmapped_nonregular_paths':[]},'transports':[{'descriptor':transport_ref,'parts':parts,'raw_root':relative(cold),'archive_sha256':transport['archive_sha256'],'archive_bytes':transport['archive_bytes'],'expanded_bytes':transport['expanded_bytes'],'recoverable_members':len(transport['members']),'manifest_sha256':transport['manifest_sha256'],'result_sha256':transport['members']['result.json']['sha256'],'observed_here':'Small descriptor/result/manifest hashes and exact member map checked; raw member/part sizes observed. Full archive/part/member validation is the already completed owner pack/split/materialization check, not rerun in this metadata pass.'}],'partial015':partial,'diagnostic016_byte_recovery':diagnostic_aliases,'historical_producer_aliases':[source_alias],'current_public_origin':{'original_path':str(origin),'retained':row(OUT/'public-origin-selection.json'),'standing':'Nonsecret public selection only; origin private key/store/entry certificates remain excluded.'},'private_external_runtime_rule':'All external local001/local002 native stores, dependency checkouts/venvs, compiled support/toolchains/caches and private origin keys remain preserved in place and outside Git selection. Their retained exact runtime receipts/pins are evidence, not a claim those private trees are portable Git members. Public selection records are explicit exceptions.','moving_files':[],'pending':[],'snapshot_boundary':'All selected completed evidence and prep017 is fixed. Future local003/A3 qualification will use a new separately authorized directory and is outside this checkpoint. INDEX.json itself must be selected by the consuming Writer using its returned exact digest; it is intentionally not self-listed.','effects':'Read/hash ordinary selected evidence and write only this new handoff/control directory. No Git/source/external effects, proof runs, archive duplication/extraction or support scan.'}
with (OUT/'INDEX.json').open('x') as stream:stream.write(json.dumps(index,sort_keys=True,indent=2)+'\n')
print(json.dumps({'index':row(OUT/'INDEX.json'),'included_files':len(include),'included_bytes':sum(x['bytes'] for x in include),'excluded':len(exclude),'partial_aliases':len(aliases),'diagnostic_aliases':len(diagnostic_aliases),'moving_files':[]},indent=2))
