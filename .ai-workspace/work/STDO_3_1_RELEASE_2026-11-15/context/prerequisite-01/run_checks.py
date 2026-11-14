from pathlib import Path
import copy,hashlib,json,shutil,subprocess,sys
ROOT=Path('/Users/jim/src/apps/specification_methodology-3.1-release')
WORK=Path(__file__).resolve().parent
PYTHON=Path(sys.executable)
NATIVE=Path('/Users/jim/Library/Application Support/STDO/releases/v3.0.4')
PIN='102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b'
STDO=Path('/Users/jim/.local/bin/stdo')
PC=ROOT/'purpose_context'; SK=ROOT/'stdo_skills'
results=[]
def run(name,args,expected=0):
 p=subprocess.run([str(x) for x in args],cwd=ROOT,capture_output=True,text=True)
 (WORK/(name+'.stdout')).write_text(p.stdout);(WORK/(name+'.stderr')).write_text(p.stderr)
 row={'name':name,'argv':[str(x) for x in args],'expected_returncode':expected,'returncode':p.returncode,'passed':p.returncode==expected};results.append(row)
 (WORK/'RESULT.json').write_text(json.dumps({'standing':'Mechanical prerequisite controls against actual native 3.0.4; no 3.1 target construction or public release.','operations':results},indent=2)+'\n')
 assert p.returncode==expected,(name,p.stdout,p.stderr)
 try:return json.loads(p.stdout)
 except json.JSONDecodeError:return p.stdout
base=[PYTHON,'-B',SK/'scripts/package.py']
dev=WORK/'development-package';rel=WORK/'release-mode-control-package'
run('package-development',base+['--out',dev])
run('package-release-mode-native-304',base+['--out',rel,'--version','3.0.4','--method-root',NATIVE,'--method-manifest-sha256',PIN])
run('refuse-incomplete-release-selection',base+['--out',WORK/'incomplete-output','--version','3.1.0-rc.1'],2)
run('refuse-future-label-on-304',base+['--out',WORK/'false-release-output','--version','3.1.0-rc.1','--method-root',NATIVE,'--method-manifest-sha256',PIN],2)
run('refuse-index-before-native-A',[PYTHON,'-B',PC/'scripts/rebuild_release_indexes.py','--version','3.1.0-rc.1','--method-root',NATIVE,'--method-manifest-sha256',PIN,'--predecessor-source-root',NATIVE],2)
assert not (WORK/'incomplete-output').exists() and not (WORK/'false-release-output').exists()
assert not (PC/'skills/stdo-context/indexes/stdo-3.1.0-rc.1-sdlc-workflow-v1').exists()
for mode,package,hosts in [('development',dev,['codex']),('release',rel,['codex','claude'])]:
 for host in hosts:
  name=mode+'-'+host;workspace=WORK/name;workspace.mkdir();(workspace/'unrelated.txt').write_text('retain\n')
  manage=[PYTHON,'-B',package/'scripts/manage_skills.py']
  inputs=['--package',package,'--workspace',workspace,'--host',host,'--definition',SK/'stdo_skills.json','--method-root',NATIVE,'--stdo',STDO,'--python',PYTHON,'--purpose-context',PC]
  run(name+'-plan',manage+['plan']+inputs)
  installed=run(name+'-install',manage+['install']+inputs)
  owned=['--workspace',workspace,'--host',host,'--receipt-sha256',installed['receipt_sha256']]
  run(name+'-verify',manage+['verify']+owned)
  hostroot=workspace/('.agents' if host=='codex' else '.claude')
  bundle='stdo-skills' if mode=='release' else 'stdo-skills-dev'
  run(name+'-runtime',manage+['check-runtime','--configuration',hostroot/bundle/'CONFIG.json'])
  adapter=[PYTHON,'-B',hostroot/'skills/stdo-context/scripts/provider.py']
  desc=run(name+'-describe',adapter+['describe'])
  run(name+'-indexes',adapter+['context','--','indexes','--public-manifest-sha256',desc['manifest_sha256']])
  run(name+'-collision',manage+['install']+inputs,2)
  guide=hostroot/bundle/'GETTING_STARTED.md';before=guide.read_bytes();guide.write_bytes(before+b'changed\n')
  run(name+'-changed-owned-refused',manage+['verify']+owned,2)
  run(name+'-changed-remove-refused',manage+['remove']+owned,2)
  guide.write_bytes(before)
  run(name+'-remove',manage+['remove']+owned)
  assert (workspace/'unrelated.txt').read_text()=='retain\n'
  assert not Path(installed['receipt']).exists()
# Tampered package release binding is refused despite a valid independently verified native installation.
bad=WORK/'wrong-native-pin-package';shutil.copytree(rel,bad)
p=bad/'INVENTORY.json';x=json.loads(p.read_text());x['release']['native_method']['manifest_sha256']='0'*64;p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
run('wrong-native-pin-refused',[PYTHON,'-B',bad/'scripts/manage_skills.py','plan','--package',bad,'--workspace',WORK/'wrong-native-pin-workspace','--host','codex','--definition',SK/'stdo_skills.json','--method-root',NATIVE,'--stdo',STDO,'--python',PYTHON,'--purpose-context',PC],2)
print(json.dumps({'operations':len(results),'passed':all(x['passed'] for x in results),'report':str(WORK/'RESULT.json')}))
