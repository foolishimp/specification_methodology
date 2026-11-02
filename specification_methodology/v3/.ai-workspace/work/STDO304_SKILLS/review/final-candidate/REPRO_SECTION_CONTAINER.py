#!/usr/bin/env python3
"""Reviewer-only reproduction; writes only below this review directory."""
import hashlib,json,subprocess,sys
from pathlib import Path
base=Path(__file__).resolve().parent
scratch=base/'scratch'/'section-container'
scratch.mkdir(parents=True,exist_ok=True)
release=scratch/'release'
member=release/'standards'/'OWNER.md'
member.parent.mkdir(parents=True,exist_ok=True)
subject="## One\n> ```\n> quoted example\n## Two\nUNSELECTED TWO\n> ```\n> another quote\n## Three\nUNSELECTED THREE\n"
member.write_text(subject)
sha=lambda b:hashlib.sha256(b).hexdigest()
manifest={'standards':{'installed_root':'standards','members':[{'path':'OWNER.md','sha256':sha(member.read_bytes())}]}}
manifest_path=release/'manifest.json';manifest_path.write_text(json.dumps(manifest))
basis={'uri':'stdo://releases/review-specimen/','manifest_sha256':sha(manifest_path.read_bytes())}
definition=scratch/'definition.json';definition.write_text(json.dumps({'product':{'definition_id':'urn:review:section-container'},'constitution':{'stdo':{'basis':basis}}}))
status={'installed':True,'valid':True,'failures':[],'definition_id':'urn:review:section-container','definition':str(definition),'basis':basis['uri'],'manifest_sha256':basis['manifest_sha256'],'path':str(release)}
state={'status':status,'manifest':str(manifest_path),'member':str(member)}
(scratch/'manager-state.json').write_text(json.dumps(state))
manager=scratch/'manager'
manager.write_text('#!'+sys.executable+'\n'+"import json,sys\nfrom pathlib import Path\ns=json.loads((Path(__file__).parent/'manager-state.json').read_text())\na=sys.argv[1:]\nif a[0]=='status': print(json.dumps(s['status']))\nelif a[0]=='resolve': print(json.dumps({'uri':a[1],'path':s['manifest'] if a[1].endswith('manifest.json') else s['member']}))\nelse: sys.exit(2)\n")
manager.chmod(0o700)
reader=base/'frozen_subject/specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py'
command=[sys.executable,'-I','-B',str(reader),'read','--stdo',str(manager),'--definition',str(definition),'--member','standards/OWNER.md','--heading','One']
run=subprocess.run(command,capture_output=True,text=True,cwd=scratch)
result=json.loads(run.stdout)
expected='## One\n> ```\n> quoted example\n'
record={'subject_freeze_sha256':'66a099d5550b3ae25d84d62fb77e296c80269fed9b30826fb876d023337c4522','reader_sha256':sha(reader.read_bytes()),'reproduction_script_sha256':sha(Path(__file__).read_bytes()),'command':command,'exit':run.returncode,'stdout':result,'stderr':run.stderr,'expected_named_section':expected,'expected_first_line':1,'expected_last_line':3,'actual_contains_unselected_section':any('UNSELECTED TWO' in s['text'] for s in result.get('sections',[])),'oracle':'CommonMark 0.31.2 fenced code blocks close at the end of their containing block; https://spec.commonmark.org/0.31.2/#fenced-code-blocks','limits':'Mock manager supplies exact verified control responses; no real installed source was altered. This isolates shipped section parser behavior, not native-host behavior.'}
(base/'SECTION_CONTAINER_REPRO.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'exit':run.returncode,'status':result.get('status'),'actual_contains_unselected_section':record['actual_contains_unselected_section'],'result':str(base/'SECTION_CONTAINER_REPRO.json')},indent=2))
