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
# Seven retained executions and the original current proof/owner-inspection witness.
commands=read(B/'PACKAGING_COMMANDS_002.json')['commands']; receipts=[]
for operation in commands:
 p=B/'packaging-execution'/(operation['id']+'.execution.json'); receipt=read(p)
 if 'argv' in operation:
  assert receipt['exit_code']==0 and receipt['argv']==operation['argv']
  for k in ['stdout','stderr']:check_ref(receipt[k])
 else:
  assert receipt['kind']=='stdo.packaging-input-binding/1'
  check_ref(receipt['predecessor']); check_ref(receipt['output'])
  prev=read(R/receipt['predecessor']['path']); now=read(R/receipt['output']['path'])
  assert sorted(k for k in set(prev)|set(now) if prev.get(k)!=now.get(k))==receipt['changed_fields']
  assert set(receipt['changed_fields'])==set(operation['field_bindings'])
 receipts.append({'operation':operation['id'],'receipt_sha256':sha(p.read_bytes()),'exit_code':receipt.get('exit_code'),'kind':receipt['kind'],'elapsed_seconds':receipt.get('elapsed_seconds'),'result':receipt.get('result',receipt.get('output'))})
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
print(json.dumps({'status':'passed','changed_native':changed,'native_members':len(native),'source_archive_changed':source_changes,'proof_archive_members':len(got),'catalog_changed_keys':read(OUT/'READER_JOIN.json')['changed_catalog_keys'],'elapsed_seconds':time.monotonic()-START}))
