from pathlib import Path
import json,hashlib,subprocess
w=Path(__file__).resolve().parents[1];r=w.parents[2];c=w/'context';b=json.loads((w/'NATIVE_BINDING.json').read_text());commands=[]
def run(name,args):
 p=subprocess.run(list(map(str,args)),cwd=r,capture_output=True);(c/(name+'.stdout')).write_bytes(p.stdout);(c/(name+'.stderr')).write_bytes(p.stderr);commands.append({'name':name,'argv':list(map(str,args)),'exit':p.returncode});(c/'NO_DRIFT_REPAIR_COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');print(name,p.returncode,flush=True);p.check_returncode()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=r/'purpose_context/authoring/release-targets/3.1.0-rc.3.json';j=json.loads(p.read_text());am=j['sdlc_source_amendments']['W11'];before=am['replacement_text'];after=before.replace('realization_refactor for local realization change with no upstream drift re-enters only that surface.', 'realization_refactor for local realization change re-enters only that surface and must prove no upstream drift. A smaller change re-enters below Goals only with an explicit no-upstream-change assertion. A declared change class is never a result: realization_refactor cannot stand in for a satisfied result that no upstream drift occurred.');assert before!=after;am['replacement_text']=after;p.write_text(json.dumps(j,indent=2)+'\n');q=c/'prepare_authoring.py';assert before in q.read_text();q.write_text(q.read_text().replace(before,after))
(w/'NO_DRIFT_REPAIR.md').write_text('''# Semantic-02 F1 disposition

The reviewer falsified the triage query because W11 described realization_refactor
without preserving its required no-upstream-drift proof. The exact native source
already requires the proof. W11 now explicitly requires it, requires the smaller
change no-upstream-change assertion, and states that a declared class cannot stand
in for a satisfied result. All six class names and Product/Goals ownership remain.

Only the SDLC W11 text changes. Query facts, native A, source grounds, guards,
dependencies, exceptions, runtime and visual artifact are unchanged. Seven earlier
queries exclude W11 or use the unchanged Python index; exact applicability is
mechanically compared and separately reassessed. The failed return is preserved.
''')
oldpin=sha(r/'purpose_context/PUBLIC_MANIFEST.json');cmd=['python3','-B',r/'purpose_context/scripts/rebuild_release_indexes.py','--version','3.1.0-rc.3','--method-root',b['installed_root'],'--method-manifest-sha256',b['manifest_sha256'],'--predecessor-source-root','/Users/jim/Library/Application Support/STDO/releases/v3.1.0-rc.2'];run('rebuild-04',cmd);run('regeneration-check-03',cmd+['--check']);newpin=sha(r/'purpose_context/PUBLIC_MANIFEST.json');dep=r/'stdo_skills/specification/composition/DEPENDENCIES.json';raw=dep.read_text();assert oldpin in raw;dep.write_text(raw.replace(oldpin,newpin));stage=c/'packages-03';stage.mkdir()
run('package-context-03',['python3','-B',r/'purpose_context/scripts/package_release.py','--out',stage/'purpose_context','--version','3.1.0-rc.3','--public-manifest-sha256',newpin]);run('package-skills-03',['python3','-B',r/'stdo_skills/scripts/package.py','--out',stage/'stdo_skills','--version','3.1.0-rc.3','--method-root',b['installed_root'],'--method-manifest-sha256',b['manifest_sha256'],'--purpose-context',stage/'purpose_context'])
old=json.loads((c/'trial-hosts-01/RESULT.json').read_text())['negative_predecessor_assessment'];run('trial-hosts-04',['python3','-B',c/'run_distribution_checks.py','--products-root',stage,'--native-root',b['installed_root'],'--stdo',b['manager'],'--store',b['store'],'--python',w/'manager/bin/python','--fixture-root',c/'final-use-02/fixture','--queries-root',c/'final-use-02/queries','--predecessor-assessment',old,'--out',c/'trial-hosts-04'])
