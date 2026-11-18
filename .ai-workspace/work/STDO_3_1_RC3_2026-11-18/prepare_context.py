from pathlib import Path
import subprocess,json,shutil,hashlib
w=Path(__file__).resolve().parent;r=w.parents[2];b=json.loads((w/'NATIVE_BINDING.json').read_text());pin=b['manifest_sha256'];pc=r/'purpose_context';stage=w/'context/packages-01';stage.mkdir();use=w/'context/final-use-01';use.mkdir();old=r/'.ai-workspace/work/STDO_3_1_RC2_2026-11-15/context/final-use-01'
for name in ['fixture','queries']:shutil.copytree(old/name,use/name)
for p in use.rglob('*'):
 if p.is_file():
  t=p.read_text();t=t.replace('3.1.0-rc.2','3.1.0-rc.3').replace('3.1-rc2','3.1-rc3').replace('STDO_3_1_RC2_2026-11-15','STDO_3_1_RC3_2026-11-18').replace('specification_methodology-3.1-rc2','specification_methodology-3.1-rc3').replace('b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4',pin);p.write_text(t)
(use/'PROFILE_SCENARIO.md').write_text('''# Hypothetical profile coverage case

This is a declared qualification scenario, not a claim of an existing Product's
adoption or a production execution grant. Consider a pure/local Python 3.12
helper refactor within accepted design of an ODD Product with a UX surface.
DESIGN_MODULE, ODD and UX apply; authority, effects, public semantics, mutation,
failure carrier and typing exceptions are unchanged/not requested. The helper
body does not acquire traversal control. Concrete graph/carrier coordinates,
Product constraints and future evidence must be acquired by any actual task.

The expected context must retain graph ownership, audit timing and triggers,
separate authority and required semantic judgment, tracking, needed transient
facts, workspace reconciliation and predicate-specific evidence. A register is
optional. No downstream named runtime, mandatory ledger, evaluator API, universal
replay or closure enum may be smuggled back in. UX's own adopted Msg replay duty
retains its separate scope. Coverage here means method constraints for this
hypothetical query, not Product conformance or implemented runtime correctness.
''')
q=json.loads((use/'queries/python.json').read_text());q['id']='stdo-3.1-rc3-hypothetical-odd-ux-profile-coverage-01';q['facts'].update(profile_odd=True,profile_ux=True,realizes_ux_surface=True,grant=str(use/'PROFILE_SCENARIO.md'),target_product='urn:stdo:qualification-scenario:rc3-odd-ux',task='Construct governing constraints for the explicitly hypothetical ODD/UX pure-helper refactor; no concrete task admission or code success asserted.');(use/'queries/profile.json').write_text(json.dumps(q,indent=2)+'\n')
commands=[]
def run(name,args):
 p=subprocess.run(list(map(str,args)),cwd=r,capture_output=True);(w/'context'/(name+'.stdout')).write_bytes(p.stdout);(w/'context'/(name+'.stderr')).write_bytes(p.stderr);commands.append({'name':name,'argv':list(map(str,args)),'exit':p.returncode});(w/'context/PACKAGE_COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(name,p.returncode,flush=True);p.check_returncode();return json.loads(p.stdout)
source_pin=hashlib.sha256((pc/'PUBLIC_MANIFEST.json').read_bytes()).hexdigest()
run('package-context',['python3','-B',pc/'scripts/package_release.py','--out',stage/'purpose_context','--version','3.1.0-rc.3','--public-manifest-sha256',source_pin])
# Source Skills binds source Context. Portable packaging records its exact distribution-pin transformation.
dep=r/'stdo_skills/specification/composition/DEPENDENCIES.json';j=json.loads(dep.read_text())
print('dependency keys',list(j),flush=True)
def repin(value):
 if isinstance(value,dict):
  for k,v in value.items():
   if isinstance(v,dict) and v.get('public_manifest')=='PUBLIC_MANIFEST.json':pass
   repin(v)
 elif isinstance(value,list):
  for v in value:repin(v)
raw=dep.read_text();oldpc=hashlib.sha256(subprocess.check_output(['git','show','2c95df2fe4656f1bbe6c4eb2d9f4be6e28446e0d:purpose_context/PUBLIC_MANIFEST.json'])).hexdigest();oldac=hashlib.sha256(subprocess.check_output(['git','show','2c95df2fe4656f1bbe6c4eb2d9f4be6e28446e0d:a_c/PUBLIC_MANIFEST.json'])).hexdigest();newac=hashlib.sha256((r/'a_c/PUBLIC_MANIFEST.json').read_bytes()).hexdigest();assert oldpc in raw and oldac in raw;dep.write_text(raw.replace(oldpc,source_pin).replace(oldac,newac))
run('package-skills',['python3','-B',r/'stdo_skills/scripts/package.py','--out',stage/'stdo_skills','--version','3.1.0-rc.3','--method-root',b['installed_root'],'--method-manifest-sha256',pin,'--purpose-context',stage/'purpose_context'])
print('ready',stage,flush=True)
