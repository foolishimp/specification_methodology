#!/usr/bin/env python3
"""Reproducible author checks; structural/source checks do not establish semantics."""
from pathlib import Path
import json,hashlib,sys
HERE=Path(__file__).resolve().parent
TENANT=HERE.parents[4]
ACCOUNT=HERE.parents[1]/'DETERMINATIONS.json'
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((HERE/'bindings.json').read_text()); raw=ACCOUNT.read_bytes(); a=json.loads(raw); rows={r['id']:r for r in a['determinations']}; errors=[]
def check(test,msg):
 if not test:errors.append(msg)
check(sha(raw)==d['input_account_sha256'],'input account changed')
check(a['schema_version']=='stdo.determinations.v1.3','account schema changed')
check(d['schema']=='stdo.semantic-contribution.v1','contribution schema')
check(d['source_commit']==a['subject']['source_commit'],'source commit mismatch')
check(len(d['bindings'])==len({r['id'] for r in d['bindings']}),'duplicate binding IDs')
check(len(d['ready_unchanged_ids'])==len(set(d['ready_unchanged_ids'])),'duplicate unchanged IDs')
assigned={i for i,r in rows.items() if r['owner']['path'] in d['assigned_owner_paths']}
written={r['id'] for r in d['bindings']}; unchanged=set(d['ready_unchanged_ids']); unfinished={r['id'] for r in d['unfinished_units']}
check(not(written&unchanged or written&unfinished or unchanged&unfinished),'partitions overlap')
check(written|unchanged|unfinished==assigned,'assigned partition not exact')
for id in unchanged:check(rows[id]['interpretation_standing'].startswith('bounded_'),'unchanged row was not ready: '+id)
member_checks=[]
for member in a['source_members']:
 if member['path'] not in d['assigned_owner_paths']:continue
 data=(TENANT/'successor'/member['path']).read_bytes(); valid=sha(data)==member['sha256']; check(valid,'source member mismatch: '+member['path']); member_checks.append({'path':member['path'],'bytes':len(data),'sha256':sha(data),'matches_account':valid})
for r in d['bindings']:
 id=r['id']; check(id in assigned,'out-of-cone ID '+id)
 if id not in rows:continue
 source=rows[id]; own=source['owner']; check(r['owner_body_sha256']==own['body_sha256'],'owner body pin mismatch: '+id)
 lines=(TENANT/'successor'/own['path']).read_bytes().splitlines(keepends=True)
 check(sha(b''.join(lines[own['start_line']-1:own['end_line']]))==own['body_sha256'],'source body byte mismatch: '+id)
 for k in ['representation_kind','interpretation_standing','applicability','predicate','definition','obligations','permissions_exceptions','dependency_relations','result_mapping','argument','required_unknown_inputs']:check(k in r,'missing '+k+': '+id)
 check(bool(r['applicability']),'missing applicability: '+id)
 check(r['argument']['source_refs']==[id],'row-local argument source mismatch: '+id)
 expected_premises=[{'id':q['id'],'kind':q['kind'],'binding':q['binding']} for q in r['dependency_relations'] if q['kind'] in ['adopted_premise','contract_application','governing_scope']]
 check(r['argument']['premises']==expected_premises,'row-local premise binding mismatch: '+id)
 for item in r['required_unknown_inputs']:
  check(item['required_when']==r['applicability'],'row-local input scope mismatch: '+id)
  check(item['standing']=='required_at_instance_not_missing_source','misclassified source-available input: '+id)
 if r['representation_kind'] in ['definition_data','non_deciding_locator']:check(r['predicate'] is None,'invented predicate on definition/locator: '+id)
 if r['representation_kind']=='definition_data':check(bool(r['definition'] and r['definition']['meaning']),'empty definition: '+id)
 if r['representation_kind'] in ['constraint','consumer_binding']:check(bool(r['predicate']),'empty deciding predicate: '+id)
 for rel in r['dependency_relations']:
  check(rel['id'] in rows,'unresolved dependency '+rel['id']+' in '+id)
  check(bool(rel['kind'] and rel['binding']),'untyped/unbound dependency: '+id)
 check(r['dependencies']==[q['id'] for q in r['dependency_relations'] if q['kind'] in ['contract_application','semantic_import','governing_scope']],'dependency projection mismatch: '+id)
 if 'contract_ref' in r['result_mapping']:check(r['result_mapping']['contract_ref'] in d['shared_contracts'],'unresolved local result contract: '+id)
for u in d['unfinished_units']:
 check(u['owner_body_sha256']==rows[u['id']]['owner']['body_sha256'],'unfinished pin mismatch: '+u['id'])
 check(rows[u['id']]['owner']['path']=='standards/STDO_REFERENCE_FRAME_BASELINE.md','unexpected unfinished owner')
check(len(d['bindings'])==93,'expected 93 authored rows')
check(len(unchanged)==81,'expected 81 unchanged ready rows')
check(len(unfinished)==67,'expected 67 unfinished Baseline rows')
check(all(rows[id]['interpretation_standing']!='source_available_construction_pending' or id in written for id in assigned if not id.startswith('STDO_REFERENCE_FRAME_BASELINE.')),'five-owner pending unit unrepresented')
cases=json.loads((HERE/'AUTHOR_CASES.json').read_text())
for case in cases['cases']:
 for ref in case['binding_ids']:check(ref in written or ref in unchanged,'case binding missing: '+ref)
check(cases['standing']=='author semantic inspection; not executable independent oracle','case standing inflated')
result={'schema':'stdo.semantic-contribution-author-check.v1','input_account_sha256':sha(raw),'bindings_sha256':sha((HERE/'bindings.json').read_bytes()),'passed':not errors,'errors':errors,'checks':['exact account hash/schema/source commit','six immutable source member pins','authored immediate-body hash recomputation','stable IDs and exact disjoint assignment partition','complete five-owner pending-ID accounting','definition/locator versus deciding representation','typed dependency resolution and declared consumer binding','shared result contract resolution','explicit unfinished-unit pins','author-case references','all row-local argument source IDs, typed premise bindings and exact input applicability'],'counts':{'assigned_rows':len(assigned),'authored_replacements':len(written),'unchanged_ready':len(unchanged),'unfinished_units':len(unfinished),'pending_units_authored':sum(rows[x]['interpretation_standing']=='source_available_construction_pending' for x in written),'author_cases':len(cases['cases'])},'source_members':member_checks,'semantic_limit':'Mechanical checks establish identities, shape and coverage accounting only. AUTHOR_CASES records source-specific author inspection, not independent evidence or semantic acceptance.'}
(HERE/'AUTHOR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['passed','errors','counts','bindings_sha256']},indent=2))
sys.exit(bool(errors))
