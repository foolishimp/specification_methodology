from pathlib import Path
import hashlib,json,re,stat,subprocess,time
R=Path('/Users/jim/src/apps/specification_methodology');B=R/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/cohort-recovery-020';C=R/'specification_methodology/v3/build_tenants/common';O=Path(__file__).parent
P=C/'standards/documentation/proofs';U=C/'standards/tooling'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(p):return json.loads(p.read_bytes())
def save(n,v):(O/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def check_ref(row,base=R):
 p=base/row['path'];st=p.lstat();assert stat.S_ISREG(st.st_mode),str(p);raw=p.read_bytes();assert sha(raw)==row['sha256'],str(p)
 if 'bytes' in row:assert len(raw)==row['bytes'],str(p)
 return {'path':str(p),'sha256':sha(raw),'bytes':len(raw),'mode':stat.S_IMODE(st.st_mode),'mtime_ns':st.st_mtime_ns}
def oldraw(rel):return subprocess.check_output(['git','show','ec0c09474a1d42084ddd1ba2b97c9479affb0220:'+rel],cwd=R)
T=read(P/'transport/TRANSPORT.json');catalog=read(P/'PROOFS.json');prior=json.loads(oldraw((P/'PROOFS.json').relative_to(R).as_posix()))
changed_keys=[k for k in sorted(set(catalog)|set(prior)) if catalog.get(k)!=prior.get(k)]
assert set(changed_keys)=={'members','observations','result_sha256','runtime_identity','selection_sha256','transport','transport_sha256'}
for row in catalog['members']:check_ref(row,P)
result=read(P/'evidence/result.json');inspection=read(P/'inspection.json')
assert result['status']=='verified' and inspection['status']=='consistent'
assert result['checked_claims']==result['requested_claims']==catalog['checked_claims']==inspection['required_claims']
assert result['runtime_identity']==catalog['runtime_identity']==inspection['runtime_identity']
assert result['runtime_identity']['sha256']=='0eb147c86f6d8d1abb1749281c3c70d188cad1fa8e07c27ae6a452532b446e26'
assert result['observations']==catalog['observations'] and result['observations']['limits']['timeout_seconds']==1800
assert [result['observations'][k] for k in ['current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations']]==[7,1,1]
assert catalog['result_sha256']==T['result_sha256']==inspection['evidence']['result_sha256']
assert catalog['transport']==T and catalog['transport_sha256']==sha((P/'transport/TRANSPORT.json').read_bytes())
assert catalog['selection_sha256']==sha((P/'SELECTION.json').read_bytes())
for name in ['formal_gate.py','formal_support.py','runtime_process.py']:
 raw=(P/'machinery/scripts'/name).read_bytes();assert sha(raw)==catalog['runtime_identity']['pins']['scripts/'+name]
 assert raw==(R/'a_c/build_tenants/lean/scripts'/name).read_bytes()
for row in catalog['sources']:assert sha((P/row['file'].replace('library/','machinery/',1).replace('current/','evidence/',1)).read_bytes())==row['sha256']
html=(P/'index.html').read_text();oldhtml=oldraw((P/'index.html').relative_to(R).as_posix()).decode();pattern=r'(<script id="proof-data" type="application/json">)(.*?)(</script>)'
m=re.search(pattern,html,re.S);om=re.search(pattern,oldhtml,re.S);assert m and om
payload=json.loads(m.group(2));oldpayload=json.loads(om.group(2));assert payload['catalog']==catalog
assert re.sub(pattern,r'\1REPLACED\3',html,flags=re.S)==re.sub(pattern,r'\1REPLACED\3',oldhtml,flags=re.S)
assert {k:v for k,v in payload.items() if k!='catalog'}=={k:v for k,v in oldpayload.items() if k!='catalog'}
doc=read(C/'standards/documentation/DOCUMENTATION.json');tooling=read(U/'TOOLING.json')
assert doc['proof_catalog_sha256']==sha((P/'PROOFS.json').read_bytes())
for row in doc['members']:check_ref(row,C/'standards/documentation')
assert catalog['source_identity_sha256']==doc['source']['source_identity_sha256']==tooling['source_identity_sha256']=='0f4d2d5f77c5a635a553a8517787f1f52bf3e43a1dd150a940360e878ea4f1ba'
selection=read(U/'SELECTION.json');portable=read(B.parent/'tools-skills/formal-budget-repair-021/PORTABLE.json')
assert len(portable['files'])==len(selection['owners']['a_c']['members'])==112
expected={x['path']:(x['sha256'],x['bytes']) for x in portable['files']};actual={x['path']:(x['sha256'],x['bytes']) for x in selection['owners']['a_c']['members']};assert expected==actual
save('READER_JOIN.json',{'changed_catalog_keys':changed_keys,'unchanged_catalog_keys':sorted(set(catalog)-set(changed_keys)),'html_scaffold_and_embedded_source_data_equal_A3':True,'current_result':catalog['result_sha256'],'current_runtime':catalog['runtime_identity']['sha256'],'reader':sha(html.encode()),'scope_limits':catalog['limits'],'reference_scope':catalog['reference_scope'],'observations':{k:result['observations'][k] for k in ['current_dynamic_proof_invocations','current_kernel_replay_invocations','current_runtime_invocations','limits','elapsed_seconds']},'accepted112_ac_inventory_matches_tooling':True})
commands=read(B/'PACKAGING_COMMANDS_021.json')['commands'];receipts=[]
bindings={'${PROOF_SELECTION_SHA256}':sha((B/'current-proof-selection.json').read_bytes()),'${DOCUMENTATION_SELECTION_SHA256}':sha((B/'current-documentation-selection.json').read_bytes())}
for op in commands:
 p=B/'execution'/(op['id']+'.execution.json');rec=read(p)
 if 'argv' in op:
  assert rec['exit_code']==0 and rec['argv']==[bindings.get(x,x) for x in op['argv']]
  for k in ['stdout','stderr']:check_ref(rec[k])
 else:
  assert rec['kind']=='stdo.packaging-binding/1';check_ref(rec['predecessor']);check_ref(rec['output'])
  prev=read(R/rec['predecessor']['path']);now=read(R/rec['output']['path']);changed={k for k in set(prev)|set(now) if prev.get(k)!=now.get(k)}
  if op['id']=='bind-proof-selection':
   assert changed=={'result','standing','inspector','bundle_archive'}
   for k,v in op['fixed_fields'].items():assert now[k]==v
   assert now['bundle_archive']['sha256']==catalog['transport_sha256']
  else:assert changed=={'proof_catalog'} and now['proof_catalog']['sha256']==sha((P/'PROOFS.json').read_bytes())
 receipts.append({'operation':op['id'],'receipt_sha256':sha(p.read_bytes()),'exit_code':rec.get('exit_code'),'kind':rec['kind'],'seconds':rec['elapsed_seconds']})
current=read(B.parent/'tools-skills/current-formal-021/CURRENT_FORMAL.json')
for k in ['result','execution','inspection','inspection_execution','supervision','request','bundle_manifest','selected_checker']:check_ref(current[k])
e=read(R/current['execution']['path'])['execution'];ie=read(R/current['inspection_execution']['path'])['execution'];assert e['returncode']==ie['returncode']==0
for run in [e,ie]:
 for row in run['inputs']:check_ref(row)
 for k in ['stdout','stderr']:check_ref(run[k])
got=read(O/'TRANSPORT_CHECK.json')['members'];outputmap={Path(x['path']).name:{'sha256':x['sha256'],'bytes':x['bytes']} for x in e['outputs'] if Path(x['path']).name in got}
assert outputmap==got and len(e['outputs'])==63
supervision=read(R/current['supervision']['path']);assert supervision['outer_timeout_seconds']==7200 and not supervision['outer_timeout_occurred'] and not supervision['cleanup_observations']
assert json.loads((R/e['stdout']['path']).read_bytes())==result
assert json.loads((R/ie['stdout']['path']).read_bytes())==inspection
save('EXECUTION_JOIN.json',{'packaging':receipts,'current_execution_sha256':current['execution']['sha256'],'current_execution_returncode':0,'current_execution_elapsed_seconds':e['elapsed_seconds'],'current_61_output_identities_equal_transport':True,'execution_extra_outputs':'stdout.json and stderr.log','inspection_execution_sha256':current['inspection_execution']['sha256'],'inspection_returncode':0,'actual_limits':current['limits'],'outer_seconds':current['outer_seconds'],'native_validation':read(B/'PAYLOAD_INVARIANTS.json')})
F=read(B/'PAYLOAD_REVIEW_FREEZE.json');refs=[F['subject'],*F['references'],*F['transport_parts']];first=read(O/'NATIVE_CHECK.json');after={r['path']:check_ref(r) for r in refs};native={r['path']:check_ref(r,C) for r in F['native_members']};assert after==first['frozen_refs'] and native==first['native_before']
semantic=read(B.parent/'source-freeze-002.json')
for row in semantic['members']+semantic['native_contracts']:assert sha((C/row['path']).read_bytes())==row['sha256']
save('AFTER.json',{'frozen_refs':after,'native_after':native,'same_before_after':True,'semantic68_same':True})
print(json.dumps({'status':'reader_execution_final_currentness_passed','catalog_changed_keys':changed_keys,'packaging':receipts,'source_proof_seconds':e['elapsed_seconds'],'frozen_refs':len(after),'native_files':len(native)}))
