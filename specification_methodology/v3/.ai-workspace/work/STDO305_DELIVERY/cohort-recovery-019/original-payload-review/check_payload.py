from pathlib import Path
import hashlib,io,json,re,stat,subprocess,time
R=Path('/Users/jim/src/apps/specification_methodology')
B=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/cohort-recovery-019'
C=R/'specification_methodology/v3/build_tenants/common'
OUT=Path(__file__).parent
START=time.monotonic()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def read(p): return json.loads(p.read_bytes())
def save(n,v): (OUT/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def check_ref(row,base=R):
 p=base/row['path']; st=p.lstat(); assert stat.S_ISREG(st.st_mode),str(p)
 raw=p.read_bytes(); assert sha(raw)==row['sha256'],str(p)
 if 'bytes' in row: assert len(raw)==row['bytes'],str(p)
 return {'path':str(p),'sha256':sha(raw),'bytes':len(raw),'mode':stat.S_IMODE(st.st_mode),'mtime_ns':st.st_mtime_ns}
def oldraw(rel): return subprocess.check_output(['git','show','327bb14af2ee5c1673a5f66bca6a6ec1bfcde402:'+rel],cwd=R)
F=read(B/'PAYLOAD_REVIEW_FREEZE.json')
assert sha((B/'PAYLOAD_REVIEW_FREEZE.json').read_bytes())=='0ce9dd9361ab428d501091157f491da20b87a0e010968cb1d2664a3a38e09a44'
refs=[F['subject'],*F['metadata_refs'],*F['transport_parts'],*F['changed_native_files']]
before={r['path']:check_ref(r) for r in refs}
inv=read(B/'NATIVE_INPUT_INVENTORY.json')['files']; assert len(inv)==171
native={r['path']:check_ref(r,C) for r in inv}
assert {p.relative_to(C).as_posix() for p in C.rglob('*') if p.is_file()}==set(native)
assert all(not p.is_symlink() for p in C.rglob('*'))
for r in inv:
 raw=(C/r['path']).read_bytes(); assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==r['git_blob']
 assert ('100755' if native[r['path']]['mode']&0o111 else '100644')==r['git_mode']
assert sum(v['bytes'] for v in native.values())==290060754
oldinv={r['path']:r for r in read(B.parent/'native-recovery-018/NATIVE_INPUT_INVENTORY.json')['files']}
assert set(oldinv)==set(native)
changed=[r['path'] for r in inv if r!=oldinv[r['path']]]
assert len(changed)==14
assert set(changed)=={r['path'].removeprefix(C.relative_to(R).as_posix()+'/') for r in F['changed_native_files']}
predelta=read(B/'PRE_COPY_DELTA.json')
assert {r['path'] for r in predelta['changed']}==set(changed)
for row in predelta['changed']:
 assert row['before']['sha256']==oldinv[row['path']]['sha256']
 assert row['after']['sha256']==native[row['path']]['sha256']
 assert sha((R/row['generated_source']).read_bytes())==native[row['path']]['sha256']
save('NATIVE_CHECK.json',{'frozen_refs':before,'native_before':native,'changed':changed,'unchanged':171-len(changed),'bytes':sum(v['bytes'] for v in native.values())})
P=C/'standards/documentation/proofs'; T=read(P/'transport/TRANSPORT.json')
archive=b''.join((P/'transport'/row['path']).read_bytes() for row in T['parts'])
assert len(archive)==T['archive_bytes'] and sha(archive)==T['archive_sha256']
for row in T['parts']: check_ref(row,P/'transport'); assert row['bytes']<=64*1024*1024
zs=zipfile=None
import zipfile
with zipfile.ZipFile(io.BytesIO(archive)) as z:
 assert len(z.infolist())==len(set(z.namelist()))==61
 assert set(z.namelist())==set(T['members'])
 got={}
 for info in z.infolist():
  assert not info.is_dir() and not (info.external_attr>>16)&stat.S_IFLNK==stat.S_IFLNK
  h=hashlib.sha256(); total=0
  with z.open(info) as fp:
   for chunk in iter(lambda:fp.read(1048576),b''):h.update(chunk);total+=len(chunk)
  got[info.filename]={'bytes':total,'sha256':h.hexdigest()}
 assert got==T['members'] and sum(x['bytes'] for x in got.values())==T['expanded_bytes']
 manifest=z.read('manifest.json'); result=z.read('result.json')
 assert sha(manifest)==T['manifest_sha256'] and sha(result)==T['result_sha256']
 assert manifest==(B.parent/'tools-skills/current-formal-008/cold/manifest.json').read_bytes()
 assert result==(P/'evidence/result.json').read_bytes()==(B.parent/'tools-skills/current-formal-016/cold/result.json').read_bytes()
 manifestobj=json.loads(manifest); map59=manifestobj.get('members',manifestobj)
 assert len(map59)==59
 assert {k:v['sha256'] for k,v in got.items() if k not in ['manifest.json','result.json']}==map59
save('TRANSPORT_CHECK.json',{'archive_sha256':sha(archive),'archive_bytes':len(archive),'members':got,'mathematical_manifest_sha256':sha(manifest),'mathematical_59_equal_008':True,'result_sha256':sha(result)})
del archive
# Exact source archive transport, owning source copies, and four approved changes.
U=C/'standards/tooling'; tooling=read(U/'TOOLING.json'); selection=read(U/'SELECTION.json')
assert sha((U/'SELECTION.json').read_bytes())==tooling['selection_sha256']
owner={x['path']:x for v in selection['owners'].values() for x in v['members']}
assert len(owner)==240
with zipfile.ZipFile(U/'sources.zip') as new,zipfile.ZipFile(io.BytesIO(oldraw((U/'sources.zip').relative_to(R).as_posix()))) as old:
 assert len(new.namelist())==len(set(new.namelist()))==240
 assert set(new.namelist())==set(old.namelist())==set(owner)
 source_changes=[]
 for row in tooling['sources']:
  name=row['archive_path']; raw=new.read(name); prev=old.read(name)
  assert sha(raw)==row['sha256']==owner[name]['sha256'] and len(raw)==row['bytes']==owner[name]['bytes']
  assert raw==(R/name).read_bytes()
  if raw!=prev:source_changes.append({'path':name,'before':sha(prev),'after':sha(raw)})
 assert sorted(source_changes,key=lambda x:x['path'])==sorted(read(B/'PACKAGING_COMMANDS_002.json')['portable_changed_rows'],key=lambda x:x['path'])
 assert len(source_changes)==4
save('SOURCE_ARCHIVE_CHECK.json',{'members':240,'changed':source_changes,'other_236_exact_A2':True})
# Reader data and HTML joins; only expected proof/runtime/custody details change.
catalog=read(P/'PROOFS.json'); prior=json.loads(oldraw((P/'PROOFS.json').relative_to(R).as_posix()))
changed_keys=[k for k in sorted(set(catalog)|set(prior)) if catalog.get(k)!=prior.get(k)]
assert set(changed_keys)=={'members','observations','result_sha256','runtime_identity','selection_sha256','transport','transport_sha256'}
for row in catalog['members']:check_ref(row,P)
result=json.loads(result); inspect=read(P/'inspection.json')
assert result['status']=='verified' and inspect['status']=='consistent'
assert result['checked_claims']==result['requested_claims']==catalog['checked_claims']==inspect['required_claims']
assert result['runtime_identity']==catalog['runtime_identity']==inspect['runtime_identity']
assert result['runtime_identity']['sha256']=='a79596f2aad2e8133291751e489d5a118ad21438d84ca068c0f7fbe0d9a9a237'
assert result['observations']==catalog['observations']
assert result['observations']['limits']['timeout_seconds']==600
assert [result['observations'][k] for k in ['current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations']]==[7,1,1]
assert catalog['result_sha256']==T['result_sha256']==inspect['evidence']['result_sha256']
assert catalog['transport']==T and catalog['transport_sha256']==sha((P/'transport/TRANSPORT.json').read_bytes())
assert catalog['selection_sha256']==sha((P/'SELECTION.json').read_bytes())
assert catalog['runtime_identity']['pins']['scripts/formal_gate.py']==sha((P/'machinery/scripts/formal_gate.py').read_bytes())
assert (P/'machinery/scripts/formal_gate.py').read_bytes()==(R/'a_c/build_tenants/lean/scripts/formal_gate.py').read_bytes()
for row in catalog['sources']:
 assert sha((P/row['file']).read_bytes())==row['sha256']
html=(P/'index.html').read_text(); oldhtml=oldraw((P/'index.html').relative_to(R).as_posix()).decode()
pattern=r'(<script id="proof-data" type="application/json">)(.*?)(</script>)'
m=re.search(pattern,html,re.S); om=re.search(pattern,oldhtml,re.S); assert m and om
payload=json.loads(m.group(2)); oldpayload=json.loads(om.group(2)); assert payload['catalog']==catalog
assert re.sub(pattern,r'\1REPLACED\3',html,flags=re.S)==re.sub(pattern,r'\1REPLACED\3',oldhtml,flags=re.S)
assert {k:v for k,v in payload.items() if k!='catalog'}=={k:v for k,v in oldpayload.items() if k!='catalog'}
doc=read(C/'standards/documentation/DOCUMENTATION.json')
assert doc['proof_catalog_sha256']==sha((P/'PROOFS.json').read_bytes())
for row in doc['members']:check_ref(row,C/'standards/documentation')
assert catalog['source_identity_sha256']==doc['source']['source_identity_sha256']==tooling['source_identity_sha256']=='0f4d2d5f77c5a635a553a8517787f1f52bf3e43a1dd150a940360e878ea4f1ba'
save('READER_JOIN.json',{'changed_catalog_keys':changed_keys,'unchanged_catalog_keys':sorted(set(catalog)-set(changed_keys)),'html_scaffold_and_embedded_source_data_equal_A2':True,'current_result':catalog['result_sha256'],'current_runtime':catalog['runtime_identity']['sha256'],'reader':sha(html.encode()),'scope_limits':catalog['limits'],'observations':{k:result['observations'][k] for k in ['current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations','limits','elapsed_seconds']}})
# Seven retained executions and the original current proof/owner-inspection witness.
commands=read(B/'PACKAGING_COMMANDS_002.json')['commands']; receipts=[]
for operation in commands:
 p=B/'packaging-execution'/(operation['id']+'.execution.json'); receipt=read(p)
 assert receipt['exit_code']==0 and receipt['argv']==operation['argv']
 for k in ['stdout','stderr']:check_ref(receipt[k])
 receipts.append({'operation':operation['id'],'receipt_sha256':sha(p.read_bytes()),'exit_code':receipt['exit_code'],'elapsed_seconds':receipt.get('elapsed_seconds'),'result':receipt.get('result')})
current=read(B.parent/'tools-skills/current-formal-016/CURRENT_FORMAL.json')
for k in ['result','execution','inspection','inspection_execution','supervision','request','bundle_manifest','selected_checker']:check_ref(current[k])
execution=read(R/current['execution']['path']); execution=execution['execution']; ins_exec=read(R/current['inspection_execution']['path'])['execution']
assert execution['returncode']==0 and ins_exec['returncode']==0
for e in [execution,ins_exec]:
 for row in e['inputs']:check_ref(row)
 for k in ['stdout','stderr']:
  if k in e and isinstance(e[k],dict) and 'path' in e[k]:check_ref(e[k])
assert len(execution['outputs'])==61
outputmap={Path(x['path']).name:{'sha256':x['sha256'],'bytes':x['bytes']} for x in execution['outputs']}
assert outputmap==got
save('EXECUTION_JOIN.json',{'packaging':receipts,'current_execution_sha256':current['execution']['sha256'],'current_execution_returncode':execution['returncode'],'current_execution_elapsed_seconds':execution['elapsed_seconds'],'current_61_output_identities_equal_transport':True,'inspection_execution_sha256':current['inspection_execution']['sha256'],'inspection_returncode':ins_exec['returncode'],'qualification_limits':read(B/'QUALIFICATION_LIMIT_BINDING.json')['selected_existing_api']})
# Final currentness: only selected frozen metadata, native payload and current selected source files.
after={r['path']:check_ref(r) for r in refs}; native_after={r['path']:check_ref(r,C) for r in inv}
assert before==after and native==native_after
save('AFTER.json',{'frozen_refs':after,'native_after':native_after,'same_before_after':True,'elapsed_seconds':time.monotonic()-START})
print(json.dumps({'status':'passed','changed_native':changed,'native_members':len(native),'source_archive_changed':source_changes,'proof_archive_members':len(got),'catalog_changed_keys':changed_keys,'elapsed_seconds':time.monotonic()-START}))
