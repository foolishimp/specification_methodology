import hashlib,importlib.util,json,os,stat,subprocess,sys,time
from pathlib import Path
R=Path.cwd();O=Path(__file__).resolve().parent;COMMON=R/'specification_methodology/v3/build_tenants/common';TOOLS=COMMON.parent/'common-tools'
sha=lambda b:hashlib.sha256(b).hexdigest()
def ref(p):
 raw=p.read_bytes();return {'path':p.relative_to(R).as_posix(),'sha256':sha(raw),'bytes':len(raw)}
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2,sort_keys=True);f.write('\n')
 return ref(p)
def load(p):return json.loads(p.read_bytes())
def inventory(root):
 rows=[]
 for p in sorted(root.rglob('*')):
  if p.is_dir():assert not p.is_symlink();continue
  assert stat.S_ISREG(p.lstat().st_mode) and not p.is_symlink();raw=p.read_bytes();rows.append({'path':p.relative_to(root).as_posix(),'sha256':sha(raw),'bytes':len(raw),'git_mode':'100755' if p.stat().st_mode&0o111 else '100644'})
 return rows
plan=load(O/'PLAN.json');assert ref(O/'PLAN.json')['sha256']=='9573f8c6c6934f4c889e05f6976fe8d0cd391872130bee692f4df0a3112a331d'
assert subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD']).decode().strip()==plan['source_checkpoint']
for row in plan['fixed_inputs']:assert ref(R/row['path'])==row,row['path']
for name in plan['absent']:assert not (O/name).exists(),name
assert sha(Path(plan['python']['invocation']).read_bytes())==plan['python']['sha256']
(O/'execution').mkdir();env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
for name in ['PYTHONPATH','PYTHONHOME','STDO_STORE']:env.pop(name,None)
dynamic={};receipts=[]
for operation in plan['commands']:
 name=operation['id'];start=time.time_ns();print('START',name,flush=True)
 if 'argv' in operation:
  argv=[dynamic.get(v,v) for v in operation['argv']];stdout=O/'execution'/f'{name}.stdout';stderr=O/'execution'/f'{name}.stderr'
  with stdout.open('xb') as out,stderr.open('xb') as err:p=subprocess.run(argv,cwd=R,env=env,stdout=out,stderr=err)
  record={'kind':'stdo.packaging-execution/1','operation':name,'argv':argv,'cwd':str(R),'returncode':p.returncode,'python':plan['python'],'stdout':ref(stdout),'stderr':ref(stderr),'elapsed_seconds':(time.time_ns()-start)/1e9}
  if p.returncode==0:record['result']=load(stdout)
  receipts.append(save(O/'execution'/f'{name}.json',record));assert p.returncode==0,(name,p.returncode,stderr.read_text())
 else:
  if name=='bind-proof':
   x=load(O/'proof-selection-template.json');x['bundle_archive']={k:v for k,v in ref(O/'archives/transport/TRANSPORT.json').items() if k!='bytes'};out=save(O/'proof-selection.json',x);dynamic['${PROOF_SHA}']=out['sha256']
  elif name=='bind-docs':
   x=load(O/'documentation-selection-template.json');x['proof_catalog']={k:v for k,v in ref(O/'proofs/PROOFS.json').items() if k!='bytes'};out=save(O/'documentation-selection.json',x);dynamic['${DOCS_SHA}']=out['sha256']
  else:raise ValueError(name)
  record={'kind':'stdo.packaging-binding/1','operation':name,'output':out,'elapsed_seconds':(time.time_ns()-start)/1e9};receipts.append(save(O/'execution'/f'{name}.json',record))
 print('DONE',name,round(record['elapsed_seconds'],3),flush=True)
complete=save(O/'execution/COMPLETE.json',{'kind':'stdo.packaging-completion/1','status':'seven_operations_succeeded','plan':ref(O/'PLAN.json'),'operations':receipts})
before=load(R/plan['native_preimage']['path'])['files'];assert inventory(COMMON)==before,'common preimage drift';old={row['path']:row for row in before};generated={}
for directory,prefix in [(O/'documentation','standards/documentation/'),(O/'tooling','standards/tooling/')]:
 for row in inventory(directory):
  name=prefix+row['path'];assert name not in generated;generated[name]=(directory/row['path'],{**row,'path':name})
assert set(generated)=={name for name in old if name.startswith(('standards/documentation/','standards/tooling/'))},'auxiliary member closure differs'
changed=[{'before':old[name],'after':row} for name,(_,row) in sorted(generated.items()) if old[name]!=row]
delta=save(O/'PRE_COPY_DELTA.json',{'kind':'stdo.rc-native-auxiliary-delta/1','source_preimage':plan['native_preimage'],'packaging':complete,'changed':changed,'native_files':len(before),'unchanged_files':len(before)-len(changed)})
for row in changed:
 name=row['before']['path'];p=COMMON/name;oldraw=p.read_bytes();assert sha(oldraw)==row['before']['sha256'];assert ('100755' if p.stat().st_mode&0o111 else '100644')==row['before']['git_mode'];raw=generated[name][0].read_bytes();assert sha(raw)==row['after']['sha256'];p.write_bytes(raw);p.chmod(0o755 if row['after']['git_mode']=='100755' else 0o644)
after=inventory(COMMON);expected={**old,**{name:row for name,(_,row) in generated.items()}};assert after==[expected[name] for name in sorted(expected)]
copy=save(O/'COPY_RESULT.json',{'status':'copied','delta':delta,'changed_paths':[x['after']['path'] for x in changed]});native_inventory=save(O/'NATIVE_INPUT_INVENTORY.json',{'files':after})
print('COPIED',len(changed),'of',len(after),'members',flush=True)
sys.path.insert(0,str(TOOLS));spec=importlib.util.spec_from_file_location('selected_native',TOOLS/'native_release.py');native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native);native.configure(R/plan['configuration']['path'],plan['configuration']['sha256']);data={row['path']:(COMMON/row['path']).read_bytes() for row in after};start=time.monotonic();native.validate_payload(after,data);duration=time.monotonic()-start
freeze=load(R/load(R/plan['configuration']['path'])['source']['path']);assert all(sha(data[row['path']])==row['sha256'] for row in freeze['members']+freeze['native_contracts'])
result=save(O/'PAYLOAD_VALIDATION.json',{'kind':'stdo.rc-native-payload-validation/1','status':'passed','source_checkpoint':plan['source_checkpoint'],'configuration':plan['configuration'],'native_inventory':native_inventory,'copy_result':copy,'native_files':len(after),'native_bytes':sum(x['bytes'] for x in after),'changed_files':len(changed),'semantic_members_unchanged':68,'tooling_members':243,'validation_seconds':duration,'construction':plan['construction'],'limitations':'Actual construction package validation only; native commit/install/public qualification pending.'});print('NATIVE_PAYLOAD_VALID',duration,result['sha256'],flush=True)
