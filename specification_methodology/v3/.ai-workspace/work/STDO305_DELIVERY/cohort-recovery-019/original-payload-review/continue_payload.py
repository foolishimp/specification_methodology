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
refs=[F['subject'],*F['metadata_refs'],*F['transport_parts'],*F['changed_native_files']]
first=read(OUT/'NATIVE_CHECK.json'); before=first['frozen_refs']; native=first['native_before']; changed=first['changed']
inv=read(B/'NATIVE_INPUT_INVENTORY.json')['files']
P=C/'standards/documentation/proofs'; T=read(P/'transport/TRANSPORT.json')
got=read(OUT/'TRANSPORT_CHECK.json')['members']
result=(P/'evidence/result.json').read_bytes()
U=C/'standards/tooling'; tooling=read(U/'TOOLING.json')
source_changes=read(OUT/'SOURCE_ARCHIVE_CHECK.json')['changed']
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
 assert sha((P/row['file'].replace('library/','machinery/',1).replace('current/','evidence/',1)).read_bytes())==row['sha256']
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
