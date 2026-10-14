#!/usr/bin/env python3
"""Bounded author checks, deliberately not an independent fidelity evaluator."""
import json, pathlib, hashlib, subprocess, datetime, sys
P=pathlib.Path(__file__).resolve().parent
R=next(p for p in P.parents if (p/'AGENTS.md').exists() and (p/'.git').exists())
PREFIX='specification_methodology/v3/build_tenants/codex/'
def sha(b):return hashlib.sha256(b).hexdigest()
def git_read(commit,path):return subprocess.check_output(['git','show',commit+':'+path],cwd=R)
D=json.loads((P/'bindings.json').read_text()); B={x['id']:x for x in D['bindings']}
a_raw=git_read(D['input_account_commit'],PREFIX+'qualification/C3/iteration-3/DETERMINATIONS.json')
assert sha(a_raw)==D['input_account_sha256']
A=json.loads(a_raw); AR={r['id']:r for r in A['determinations']}; assigned={r['id'] for r in AR.values() if r['owner']['path'] in D['owner_paths']}
assert set(B)==assigned and len(B)==len(D['bindings'])==107
source_checks=[]
for s in D['source_members']:
 raw=git_read(D['source_commit'],PREFIX+'successor/'+s['path']); assert sha(raw)==s['sha256']; assert len(raw)==s['bytes']; lines=raw.splitlines(keepends=True)
 ids=[]
 for id,b in B.items():
  if b['owner']['path']!=s['path']:continue
  o=AR[id]['owner']; observed=sha(b''.join(lines[o['start_line']-1:o['end_line']])); assert observed==b['owner_body_sha256']==o['body_sha256']; ids.append(id)
 source_checks.append({**s,'verified_body_count':len(ids)})
required=['id','owner_body_sha256','representation_kind','interpretation_standing','applicability','predicate','obligations','permissions_exceptions','dependencies','result_mapping','argument','external_inputs']
for id,b in B.items():
 assert all(k in b for k in required),id
 assert b['applicability']['scope_ref'] in D['owner_scopes']; assert b['applicability']['trigger']
 assert all(dep['id'] in AR and dep['kind'] for dep in b['dependencies'])
 assert b['argument']['additional_policy'] and b['argument']['premises']
 assert b['argument']['conditional_consequence']['contract_ref'] in D['argument_contracts']
 assert all('input_ref' not in i or i['input_ref'] in D['external_input_catalog'] for i in b['external_inputs'])
 if b['representation_kind']=='definition_data': assert b['predicate'] is None and b['definition']['declared_meaning'] and b['result_mapping']['kind']=='definition_data'
 elif b['representation_kind']=='non_deciding_locator': assert b['predicate'] is None and b['result_mapping']['kind']=='none_for_locator'
 else: assert b['predicate'] and b['result_mapping']['contract_ref']=='core_result'
assert len(D['coverage']['pending_resolved_ids'])==98
assert len(D['coverage']['ready_inspected_and_replaced_ids'])==7
assert D['coverage']['unchanged_ready_ids']==D['coverage']['unfinished_units']==[]
# These small reference evaluators exercise selected source discriminants, not all prose meanings.
def conjoin(vs):
 if 'falsified' in vs:return 'falsified'
 if 'invalid_basis' in vs:return 'invalid_basis'
 if 'out_of_frame' in vs:return 'out_of_frame'
 if not vs or any(v is None or v=='indeterminate' for v in vs):return 'indeterminate'
 assert all(v=='satisfied' for v in vs),vs
 return 'satisfied'
def truth(v):return 'indeterminate' if v is None else 'satisfied' if v else 'falsified'
def assess(c):
 k=c['kind']; x=c['input']
 if k=='entity_admission':
  return {'eligibility':conjoin([x['surfaces'].get(s) for s in ['identity','boundary','authority','state','evidence','treatment','covariance','ambiguity']]+[x.get('discrimination')]),'requires_overlay':False}
 if k=='overlay_eligibility':
  if x['selected'] is False:return {'applicable':False,'eligibility':None}
  v=[truth(x.get('declared_space')),truth(x.get('paired_evidence')),truth(x.get('extraction') in ['mean_offset','supervised_mean_offset']) if x.get('extraction') else 'indeterminate',x.get('verification'),x.get('uniqueness'),x.get('transfer'),truth(x.get('stored_surfaces'))]
  return {'applicable':True,'eligibility':conjoin(v),'statistical_standing':x.get('statistical_standing','candidate')}
 if k=='direction_composition':return {'verdict':truth(x.get('same_space'))}
 if k=='statistical_promotion':return {'verdict':x['conditional_independence'],'publication_verified':x['publication_verified']}
 if k=='local_ephemera':
  # Each actual forbidden condition is sufficient adverse evidence, even if another is unknown.
  return {'local_cell_allowed':conjoin([truth(None if x.get(n) is None else not x[n]) for n in ['other_view_observes','product_state','unmount_consequence']])}
 if k=='product_action':return {'action_eligible':truth(x.get('admitted_carrier'))}
 if k=='effect_and_replay':
  replay=truth(x.get('expected_trace_matches'))
  if x.get('hidden_dependency'): replay='falsified'
  if x.get('performance')!='performed' and replay=='satisfied':replay='indeterminate'
  effect=x.get('observed_effect') or ('unknown' if x.get('possible_effect') else 'not_requested' if x.get('established_effect_free') else 'unknown')
  return {'replay':replay,'performance':x['performance'],'effect':effect}
 if k=='scaffold':return {'exemption_valid':conjoin([truth(x.get(n)) for n in ['scope','operations','mutation_bound','visible_label','superseding_surface','retirement_ticket_condition','nonclosure']])}
 if k=='escrow':return {'escrow_eligible':truth(x.get('local_allowed_debt') and not x.get('forbidden_semantic_change'))}
 if k=='sprint_close':
  return {'sprint_close':conjoin([truth(x.get(n)) for n in ['all_classified','debt_permitted','followup_durable','no_unclassified_carrier_continuation_authority']]),'item_compliance':x['item_compliance'],'method_closure':conjoin(x['applicable_ux_checks'])}
 if k=='treatment':return {'decision':truth(x.get('actual_mandate_and_conditions')),'compliance':x['compliance'],'effect':x['effect'],'treatment':x['treatment']}
 raise AssertionError(k)
cases=json.loads((P/'cases.json').read_text()); case_results=[]
for c in cases:
 assert all(i in B for i in c['unit_ids']),c['id']
 observed=assess(c); assert observed==c['expected'],(c['id'],observed,c['expected'])
 case_results.append({'id':c['id'],'kind':c['kind'],'observed':observed,'status':'matched_authored_expectation'})
report={'schema':'stdo.author-semantic-check.v1','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'standing':'Author pin/coverage and selected source-discriminant checks only; no independent fidelity or acceptance claim.','bindings_sha256':sha((P/'bindings.json').read_bytes()),'input_account_sha256':sha(a_raw),'source_checks':source_checks,'coverage':{'assigned':len(assigned),'constructed_pending':98,'ready_inspected_replaced':7,'unchanged_ready':0,'unfinished':0},'checks':['input account pin','member pins','107 exact body pins','107 stable IDs exactly once','typed dependency IDs exist','shared contract/input references resolve','definitions and locators create no Boolean law','all pending and prior-ready coverage named','selected positive/adverse/unknown examples preserve independent result boundaries'],'case_count':len(cases),'cases':case_results,'limits':['Reference evaluators cover selected discriminants only and are authored with the bindings.','Passing them does not prove all natural-language semantics, usefulness of integrated representation, or any live Product conformance.']}
(P/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['cases','source_checks','limits','checks']},indent=2))
