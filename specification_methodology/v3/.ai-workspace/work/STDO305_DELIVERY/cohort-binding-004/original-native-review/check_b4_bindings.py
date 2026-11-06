from pathlib import Path
import json, hashlib, time
ROOT=Path('/Users/jim/src/apps/specification_methodology')
BASE=ROOT/'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/cohort-binding-004'
OUT=Path(__file__).parent
observed={}
def sha(raw): return hashlib.sha256(raw).hexdigest()
def path(p):
 p=Path(p);return p if p.is_absolute() else ROOT/p
def read(p,expected=None):
 p=path(p);assert p.stat().st_size<2_000_000, ('metadata size boundary',str(p))
 raw=p.read_bytes(); digest=sha(raw)
 if expected: assert digest==expected, str(p)
 observed[str(p)]={'path':str(p),'sha256':digest,'bytes':len(raw)}
 return raw
def j(p,expected=None):return json.loads(read(p,expected))
def ref(r):
 raw=read(r['path'],r['sha256']);assert len(raw)==r['bytes'];return json.loads(raw)
def canonical(v):return sha(json.dumps(v,ensure_ascii=False,allow_nan=False,sort_keys=True,separators=(',',':')).encode())
start=time.time_ns()
subjects=j(BASE/'SUBJECTS.json','329d27d4028b7b8017b1a677957ab16aec7d09bf0fdee343384c33e91e4c859d')
candidate=j(BASE/'CANDIDATE_COMPONENTS.json','7f5606ceeae5c934598eda80ad320198ed1dae9d8b737e7e7f42d535d09d8ff2')
index=j(BASE/'COMPONENT_CLAIM_INDEX.json','f49b6a237917b24bce3b56e9b4e401d2ce0980f3832668eb1b5f06f5d592f7c7')
installation=j(BASE/'INSTALLATION.json','db31f308193c6c0e190590cded3c8ec92daa29ae7fb0811fc6c321c7dcd35cb7')
allrows={}
for key,s in subjects['products'].items():
 assert s['sha256']==canonical(s['members']) and s['member_count']==len(s['members'])
 assert candidate['products'][key]['subject']==s
 assert installation['subjects'][key]==s['sha256']
 for row in s['members']:assert row['path'] not in allrows;allrows[row['path']]=row
assert len(allrows)==424 and set(installation['files'])==set(allrows)
for key,s in subjects['components'].items():
 assert s['sha256']==canonical(s['members']) and s['member_count']==len(s['members'])
 assert candidate['components'][key]['subject']==s
 assert all(allrows.get(row['path'])==row for row in s['members'])
assert candidate['qualification']['evidence']=={}
join=j(BASE/'INSTALLED_SOURCE_JOIN.json','fd97dba6d3f2b80f6418dbc1f2c0f688c4551e3d6975cc42f30123181fd3c988')
ref(join['installation']);ref(join['materialization_execution'])
for row in join['members']:
 assert {k:v for k,v in row.items() if k!='installed_path'}==allrows[row['path']]
 assert installation['files'][row['path']]==row['installed_path']
wrappers={key:ref(r) for key,r in index['component_evidence'].items()}
for name in ('source_current_model','source_current_map','current_index_validation'):
 w=wrappers[name];old=ref(w['original_source_evidence'])
 for field in ('execution','producer','result','source_identity_sha256'):assert w[field]==old[field],(name,field)
 assert w['installed_source_join']['sha256']==observed[str(BASE/'INSTALLED_SOURCE_JOIN.json')]['sha256']
 ref(w['installation'])
for name in ('installed_lean','exact_candidate_lean_result'):
 w=wrappers[name];old=ref(w['original_execution'])
 assert w['execution']==old['execution'] and w['producer']==old['producer']
 assert w['result']['sha256']==old['result']['sha256']
 result=ref(w['result']);assert result['status']=='verified'
 assert len(result['checked_claims'])==5
assert wrappers['exact_candidate_lean_result']['installed_verification']==index['component_evidence']['installed_lean']
closure=j(BASE/'claim-preparation/IMPLICIT_INPUT_CLOSURE.json','1e80add31e70a8a65fabe1b76e1039875018c018f1bb1b22682b98313ec8d9d3')
for name in ('portable-request-derived.json','recover-construction-proof-derived.json'):
 w=j(BASE/'claim-preparation'/name);old=ref(w['original_execution'])
 orig=w['implicit_input_closure']['original_recorded_inputs']
 assert orig==old['execution']['inputs']
 additions=w['implicit_input_closure']['source_proven_implicit_inputs']
 assert len(additions)==1
 added=additions[0]['retained_ref'];ref(added)
 assert w['execution']['inputs']==orig+[added]
 for key in old['execution']:
  if key!='inputs':assert w['execution'][key]==old['execution'][key],(name,key)
 assert w['producer']==old['producer'] and w['result']==old['result']
 assert '--archive' not in w['execution']['argv'] and '--transport' not in w['execution']['argv']
 source=w['implicit_input_closure']['source'];read(source['path'],source['sha256'])
 actual_entry=w['execution']['argv'][3]
 assert read(actual_entry,source['sha256'])==read(source['path'])
 actual_descriptor=additions[0]['actual_path'];read(actual_descriptor,added['sha256'])
 ref(w['result'])
custody=j(BASE/'proof-retention/CUSTODY.json','c66a8176ed2fcd8a9ec11453e1a6b39b5a66e0983a2a8ec7e679818222cf91b9')
descriptors={}
for transport in custody['transports'].values():
 d=ref(transport['descriptor']);descriptors[transport['descriptor']['sha256']]=d
 assert d['archive_sha256']==transport['archive_sha256'] and d['archive_bytes']==transport['archive_bytes']
 assert len(d['members'])==61 and d['expanded_bytes']==sum(x['bytes'] for x in d['members'].values())
 assert sum(x['bytes'] for x in d['parts'])==d['archive_bytes']
 assert all(0<x['bytes']<=64*1024*1024 for x in d['parts'])
 assert 'local-origin.json' not in d['members']
 for a,b in zip(d['parts'],transport['parts']):assert a['bytes']==b['bytes'] and a['sha256']==b['sha256'] and Path(a['path']).name==Path(b['path']).name
bundles=[]
for bundle in custody['bundles']:
 manifest=ref(bundle['retained_metadata']['manifest.json']); result=ref(bundle['retained_metadata']['result.json'])
 assert manifest==ref(bundle['actual_bundle']['manifest']) and result==ref(bundle['actual_bundle']['result'])
 assert bundle['actual_bundle']['status']==result['status']=='verified'
 assert {m['member']:m['sha256'] for m in bundle['members']}==manifest['members']
 for m in bundle['members']:
  recovery=m['recovery'];assert recovery['bytes']==m['bytes'] and recovery['sha256']==m['sha256']
  d=descriptors[recovery['descriptor']['sha256']]
  assert d['members'][recovery['member']]=={'bytes':m['bytes'],'sha256':m['sha256']}
 bundles.append({'name':bundle['name'],'members':len(bundle['members']),'counts':bundle['actual_bundle']['counts'],'reuse':bundle['actual_bundle']['reuse']})
assert sum(b['members'] for b in bundles)==244
completion=ref(custody['actual_packaging']);ref(completion['plan']);assert len(completion['commands'])==4
for command in completion['commands']:
 d=ref(command);assert d['returncode']==0
 ref(d['result']);read(d['producer']['path'],d['producer']['sha256'])
frontier=j(BASE/'FINALIZATION_FRONTIER.json','509e213469a746d96181d430547c4c1dc92654314b2739897cffc26ca464d258')
for record in list(observed.values()):read(record['path'],record['sha256'])
report={'kind':'stdo.independent-b4-metadata-review/1','assessor':'/root/stdo305_integration_review','authors':['/root/stdo305_release_tools','/root/stdo305_tools_skills','/root/stdo305_representation'],'started_ns':start,'finished_ns':time.time_ns(),'conclusion':'satisfied_within_frozen_subset','open_findings':[],'subject':{'candidate_sha256':observed[str(BASE/'CANDIDATE_COMPONENTS.json')]['sha256'],'source_subjects_sha256':observed[str(BASE/'SUBJECTS.json')]['sha256'],'native_commit':'d1f13c53ab733a73993615498f66251041a74073'},'checks':['Five Product and eleven component metadata subjects match canonical row identities; all424 source mappings agree with the previously reviewed actual A4 installation. No new live source or support scan.','Source-model/map/index wrappers preserve original execution, producer and result; the112-row installed source join preserves the actual A4 route without relabelling source work as installed execution.','Installed and source Lean wrappers retain their original distinct executions and exact results.','Two default-descriptor wrappers change only declared input closure and explicit derivation metadata; actual argv uses the unchanged installed owner whose default selects the exact retained descriptor. No syscall or rerun claim.','Every244 mathematical member in four distinct bundle manifests maps to an exact selected descriptor member; all compiled members remain included. Two archives have61 entries each and two bounded parts; private origin hints excluded.','Four actual pack/split command receipts report success against the reviewed producer; this review does not repeat their archive-byte validation.','All selected small metadata/source references remained byte-identical before/after.'], 'bundles':bundles,'bounds':['Only metadata and small selected producer sources were read; no ZIP/part bytes or model/support trees were scanned. Earlier actual owner archive checks, installed proof, runtime and browser evidence remain their own evidence.','Candidate still assembling with empty final qualification map. Claude original timeout/deviations remain; reporting successor and final complete cohort/review wrappers not yet assessed.','No new release acceptance, Git operation, publication or public-install verification.'], 'references':list(observed.values())}
out=OUT/'B4_METADATA_REVIEW.json';out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({'report':str(out),'sha256':sha(out.read_bytes()),'references':len(observed),'conclusion':report['conclusion'],'findings':[],'bundles':bundles},indent=2))
