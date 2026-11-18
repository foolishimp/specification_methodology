from pathlib import Path
import json,hashlib
here=Path(__file__).resolve().parent;r=here.parents[3];product=r/'stdo_representation';oldrel='build_tenants/a_c/representation/stdo-v3.1.0-rc.2';newrel='build_tenants/a_c/representation/stdo-v3.1.0-rc.3';old=product/oldrel;new=product/newrel
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
def inventory(base,paths):return [{'path':name,'sha256':sha(base/name),'bytes':(base/name).stat().st_size} for name in sorted(set(paths))]
assert read(here/'browser-rc3-01/RESULT.json')['status']=='passed'
assert all(read(p)['exit_code']==read(p)['expected_exit_code'] for p in (here/'final-checks-001').glob('[0-9]*.json'))
binding=read(new/'SOURCE_BINDING.json');generation=read(new/'GENERATION.json');native=binding['represented_source'];oldrecipe=read(product/'scripts/visual_31_rc2_annotations.json');newrecipe=read(product/'scripts/visual_31_rc3_annotations.json');assert oldrecipe['annotations']==newrecipe['annotations']
comparison={'kind':'stdo.rc3-visual-predecessor-comparison/1','predecessor':'3.1.0-rc.2','successor':'3.1.0-rc.3','selected_sources':[{'path':x['path'],'before_sha256':sha(old/'source'/x['path']),'after_sha256':sha(new/'source'/x['path']),'bytes_equal':(old/'source'/x['path']).read_bytes()==(new/'source'/x['path']).read_bytes()} for x in binding['selected_native_members']],'annotation_records_equal':True,'annotation_count':len(newrecipe['annotations']),'claims':'Navigation is regenerated against current exact source. Selected annotation payloads are unchanged; changed source bodies require separate source-semantic applicability assessment. No byte-equality assertion for changed native owners.','limits':['Source section navigation and selected SDLC/carrier/context relations only.','Unrepresented body meaning remains explicit in every section residual.','No whole-method semantics, code correctness, formal proof or general visual usefulness established.']};save(here/'PREDECESSOR_COMPARISON.json',comparison)
(new/'README.md').write_text(f'''# STDO 3.1.0-rc.3 visual documentation

This bounded artifact binds native commit `{native['release']['commit']}`,
manifest `{native['manifest_sha256']}`, and model
`{generation['model']['id']}` (`{generation['model']['sha256']}`).

[Open the offline reader](run/generation/proposal/explorer.html).
It presents source-section navigation over ACTIVATION, SDLC_DEFAULTS and TICKETS,
plus 24 explicitly authored work/carrier/context annotations. Every section
retains a visible residual for meaning outside this bounded interpretation.
Original source remains authoritative. Counts, structural validation and
reversible conversion establish neither source fidelity nor whole-method coverage.

The current source is regenerated through `scripts/build_31_rc3_visual.py`.
The exact source/provider and generation identities are retained in
[SOURCE_BINDING.json](SOURCE_BINDING.json) and [GENERATION.json](GENERATION.json).
The cohort records actual source-semantic assessment and browser observations.
Earlier artifacts and assessments retain their original subjects.
''')
(new/'COVERAGE.md').write_text((old/'COVERAGE.md').read_text().replace('3.1.0-rc.2','3.1.0-rc.3').replace('visual_31_rc2_annotations.json','visual_31_rc3_annotations.json'))
files=[x.relative_to(product).as_posix() for x in new.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.name!='.DS_Store']
manifest=read(product/'PUBLIC_MANIFEST.json');manifest.update(version='3.1.0-rc.3',represented_source=native,model=generation['model'],entrypoint=newrel+'/run/generation/proposal/explorer.html',regeneration='scripts/build_31_rc3_visual.py',source_binding=newrel+'/SOURCE_BINDING.json',generation_binding=newrel+'/GENERATION.json',scope=binding['scope'],limits=binding['limits'])
for key,name in [('representation_tools','a_c'),('optional_axiom_conversion','axiom_indexer')]:manifest['dependencies'][key].update(version='3.1.0-rc.3',public_manifest_sha256=sha(r/name/'PUBLIC_MANIFEST.json'))
manifest['files']=inventory(product,['VERSION','stdo_representation.json','scripts/build_31_rc3_visual.py','scripts/visual_31_rc3_annotations.json',*files]);save(product/'PUBLIC_MANIFEST.json',manifest)
selection=read(r/'.ai-workspace/work/STDO_3_1_RC2_2026-11-15/visual/PACKAGE_SELECTION.json');selection.update(version='3.1.0-rc.3',native_manifest_sha256=native['manifest_sha256'],standing='Exact RC3 visual members with actual native/provider bindings; finite checks and separate semantic assessment retain their declared scopes.')
for name,entry in selection['products'].items():
 paths=[x for x in entry['member_paths'] if not x.startswith(oldrel+'/')];paths=[x.replace('releases/v3.1.0-rc.2.md','releases/v3.1.0-rc.3.md').replace('build_31_rc2_visual.py','build_31_rc3_visual.py').replace('visual_31_rc2_annotations.json','visual_31_rc3_annotations.json') for x in paths]
 if name=='stdo_representation':paths+=files
 entry['member_paths']=sorted(set(paths));entry['members']=inventory(r/name,paths);entry['member_count']=len(entry['members']);entry['inventory_sha256']=hashlib.sha256(json.dumps(entry['members'],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
save(here/'PACKAGE_SELECTION.json',selection);save(here/'RESULT.json',{'status':'constructed-and-mechanically-checked','native':native,'model':generation['model'],'checks':{'pipeline_commands':6,'artifact_commands':9,'browser_checks':len(read(here/'browser-rc3-01/RESULT.json')['checks'])},'selection_sha256':sha(here/'PACKAGE_SELECTION.json'),'semantic_standing':'Separately assessed; Writer check is not a semantic verdict.','limits':comparison['limits']});print({name:x['member_count'] for name,x in selection['products'].items()})
