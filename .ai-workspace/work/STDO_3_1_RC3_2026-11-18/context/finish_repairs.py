from pathlib import Path
import json,hashlib,subprocess,sys,copy,ast
w=Path(__file__).resolve().parents[1];r=w.parents[2];c=w/'context';b=json.loads((w/'NATIVE_BINDING.json').read_text());commands=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,args):
 p=subprocess.run(list(map(str,args)),cwd=r,capture_output=True);(c/(name+'.stdout')).write_bytes(p.stdout);(c/(name+'.stderr')).write_bytes(p.stderr);commands.append({'name':name,'argv':list(map(str,args)),'exit':p.returncode});(c/'REPAIR_COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(name,p.returncode,flush=True);p.check_returncode()
ast.parse((c/'prepare_authoring.py').read_text())
sys.path.insert(0,str(r/'purpose_context/scripts'));import rebuild_release_indexes as m
au=json.loads((r/'purpose_context/authoring/release-targets/3.1.0-rc.3.json').read_text());am=au['sdlc_source_amendments']['W11'];rule=next(x for x in json.loads((r/'purpose_context/authoring/sdlc-workflow/RULES.json').read_text())['rules'] if x['id']=='W11');closure=json.loads((r/'purpose_context/authoring/sdlc-workflow/SOURCE-CLOSURE.json').read_text());paths={x['id']:'standards/'+x['path'] for x in closure['members']};checks=[]
positive=copy.deepcopy(rule);m.apply_source_amendment(positive,am,Path(b['installed_root']),paths);assert positive['text']==am['replacement_text'];checks.append({'case':'actual source and predecessor accepted','passed':True})
for name in ['mismatched-source-path','wrong-preimage','wrong-ground-digest']:
 bad=copy.deepcopy(am)
 if name=='mismatched-source-path':bad['grounds'][0]['source_id']='UNDECLARED_SOURCE_ID'
 elif name=='wrong-preimage':bad['expected_text']+=' changed'
 else:bad['grounds'][0]['sha256']='0'*64
 target=copy.deepcopy(rule)
 try:m.apply_source_amendment(target,bad,Path(b['installed_root']),paths)
 except m.core.Refusal as e:checks.append({'case':name,'passed':True,'refusal':str(e)});assert target==rule
 else:raise AssertionError(name+' was accepted')
(c/'SOURCE_AMENDMENT_CONTROLS.json').write_text(json.dumps({'status':'passed','checks':checks,'generator_sha256':sha(r/'purpose_context/scripts/rebuild_release_indexes.py')},indent=2)+'\n')
oldpin=sha(r/'purpose_context/PUBLIC_MANIFEST.json')
cmd=['python3','-B',r/'purpose_context/scripts/rebuild_release_indexes.py','--version','3.1.0-rc.3','--method-root',b['installed_root'],'--method-manifest-sha256',b['manifest_sha256'],'--predecessor-source-root','/Users/jim/Library/Application Support/STDO/releases/v3.1.0-rc.2']
run('rebuild-03',cmd);run('regeneration-check-02',cmd+['--check'])
newpin=sha(r/'purpose_context/PUBLIC_MANIFEST.json');dep=r/'stdo_skills/specification/composition/DEPENDENCIES.json';raw=dep.read_text();assert oldpin in raw;dep.write_text(raw.replace(oldpin,newpin))
stage=c/'packages-02';stage.mkdir()
run('package-context-02',['python3','-B',r/'purpose_context/scripts/package_release.py','--out',stage/'purpose_context','--version','3.1.0-rc.3','--public-manifest-sha256',newpin])
run('package-skills-02',['python3','-B',r/'stdo_skills/scripts/package.py','--out',stage/'stdo_skills','--version','3.1.0-rc.3','--method-root',b['installed_root'],'--method-manifest-sha256',b['manifest_sha256'],'--purpose-context',stage/'purpose_context'])
old=json.loads((c/'trial-hosts-01/RESULT.json').read_text())['negative_predecessor_assessment']
run('trial-hosts-02',['python3','-B',c/'run_distribution_checks.py','--products-root',stage,'--native-root',b['installed_root'],'--stdo',b['manager'],'--store',b['store'],'--python',w/'manager/bin/python','--fixture-root',c/'final-use-02/fixture','--queries-root',c/'final-use-02/queries','--predecessor-assessment',old,'--out',c/'trial-hosts-02'])
print('Repair checks and trial complete')
