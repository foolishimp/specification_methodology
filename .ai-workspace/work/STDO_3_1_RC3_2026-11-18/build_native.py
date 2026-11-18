from pathlib import Path
import subprocess,hashlib,json,shutil
w=Path(__file__).resolve().parent;r=w.parents[2];logs=w/'native-commands';logs.mkdir();commands=[]
def run(name,args):
 p=subprocess.run(list(map(str,args)),cwd=r,capture_output=True);(logs/(name+'.stdout')).write_bytes(p.stdout);(logs/(name+'.stderr')).write_bytes(p.stderr);commands.append({'name':name,'argv':list(map(str,args)),'exit':p.returncode});(logs/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(name,p.returncode,flush=True);p.check_returncode();return p.stdout
report=(w/'assessment/native-02/ASSESSMENT.md').read_text();assert '**Verdict: `satisfied`.**' in report
exec_record=json.loads((w/'assessment/native-02/EXECUTION.json').read_text());assert exec_record['exit_code']==0 and exec_record['result']['subtype']=='success'
source=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();inv=w/'method-02/NATIVE_READY_INVENTORY.json'
run('cut',['python3','-B',r/'releases/3.1.0-rc.3/tools/native_cut.py','--repo',r,'--source-commit',source,'--inventory',inv,'--inventory-sha256',hashlib.sha256(inv.read_bytes()).hexdigest(),'--out',w/'native'])
manager=w/'manager/bin/stdo';store=w/'native-store';cmd=[manager,'--store',store]
run('manifest',cmd+['manifest','v3.1.0-rc.3','--repository',r]);run('install',cmd+['install','v3.1.0-rc.3','--repository',r]);native_root=store/'releases/v3.1.0-rc.3';pin=hashlib.sha256((native_root/'manifest.json').read_bytes()).hexdigest()
verify=json.loads(run('verify',cmd+['verify','v3.1.0-rc.3','--manifest-sha256',pin]));assert verify['valid']
shutil.copy2(native_root/'manifest.json',w/'assets/stdo-v3.1.0-rc.3-manifest.json')
binding={'kind':'stdo.native-release-binding/1','native':json.loads((w/'native/NATIVE.json').read_text()),'installed_root':str(native_root),'manifest_sha256':pin,'manager':str(manager),'store':str(store),'verification':{'file':'native-commands/verify.stdout','valid':True}}
(w/'NATIVE_BINDING.json').write_text(json.dumps(binding,indent=2)+'\n');print(json.dumps({'native':binding['native']['native_commit'],'tag_object':binding['native']['tag_object'],'manifest_sha256':pin}))
