#!/usr/bin/env python3
"""Bounded author checks; these are not independent semantic qualification."""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[8]
BASE='specification_methodology/v3/build_tenants/codex/'
SOURCE='f2cb3e593757d094d008102551925e871a0204ff'
ACCOUNT='ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
def sha(b): return hashlib.sha256(b).hexdigest()
def show(c,p): return subprocess.check_output(['git','-C',str(ROOT),'show',c+':'+p])
ab=show('fe4fcbe',BASE+'qualification/C3/iteration-3/DETERMINATIONS.json')
assert sha(ab)==ACCOUNT
a=json.loads(ab)
raw=(HERE/'bindings.json').read_bytes()
d=json.loads(raw)
assert d['schema_version']=='stdo.semantic-contribution.v1'
assert d['input_account_sha256']==ACCOUNT and d['source_commit']==SOURCE
assert d['common_input']=='355aa8655cca9c6ba6cf5c414f9bea3032ae89fd'
assert d['installed_builder_manifest_sha256']=='3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
rows={r['id']:r for r in a['determinations']}
bs={b['id']:b for b in d['bindings']}
assert len(bs)==len(d['bindings'])
selected={rid for rid,r in rows.items() if r['owner']['path'] in d['owner_paths']}
assert set(bs)==selected
assert not d['unfinished_source_ids'] and not d['unchanged_ready_ids']
cache={}
source_checks=[]
for path in d['owner_paths']:
    blob=show(SOURCE,BASE+'successor/'+path)
    pin=next(m for m in a['source_members'] if m['path']==path)
    assert sha(blob)==pin['sha256'] and len(blob)==pin['bytes']
    live=ROOT/BASE/'successor'/path
    assert live.read_bytes()==blob, 'live documentary source differs: '+path
    cache[path]=blob
    source_checks.append({'path':path,'bytes':len(blob),'sha256':sha(blob),'live_equals_frozen':True})
clause_count=0
changed_kind=[]
for rid,b in bs.items():
    r=rows[rid]; owner=r['owner']; blob=cache[owner['path']]
    body=b''.join(blob.splitlines(keepends=True)[owner['start_line']-1:owner['end_line']])
    assert sha(body)==owner['body_sha256']==b['owner_body_sha256']
    assert b['owner']==owner and b['source_member_sha256']==sha(blob)
    assert b['applicability'] and b['argument']['conditional_consequence'] and b['argument']['policy_choices']
    assert b['interpretation_standing']!='source_available_construction_pending'
    assert b['representation_kind'] in ['constraint','definition_data','consumer_binding','non_deciding_locator']
    assert not b['unrepresented_scope']
    if b['representation_kind'] in ['definition_data','non_deciding_locator']:
        assert b['predicate'] is None and b['definition'] is not None
    else:
        assert isinstance(b['predicate'],str) and b['predicate'].strip()
    assert all(dep in rows for dep in b['dependencies'])
    assert all(rel['id'] in rows and rel['kind'] for rel in b['dependency_relations'])
    assert not set(r.get('dependencies',[]))-set(b['dependencies']), rid
    assert b['source_clause_ids']==[rid+'#'+c['id'] for c in r['source_clauses']]
    for c in r['source_clauses']:
        assert sha(blob[c['byte_start']:c['byte_end']])==c['sha256']
        clause_count+=1
    if b['representation_kind']!=r['representation_kind']:
        changed_kind.append({'id':rid,'before':r['representation_kind'],'after':b['representation_kind']})

def eval_expr(x,facts):
    if not isinstance(x,dict): return x
    if 'fact' in x:return facts.get(x['fact'])
    if 'eq' in x:
        left,right=(eval_expr(v,facts) for v in x['eq'])
        return None if left is None or right is None else left==right
    if 'not' in x:
        value=eval_expr(x['not'],facts)
        return None if value is None else not value
    if 'all' in x:
        vals=[eval_expr(v,facts) for v in x['all']]
        return False if False in vals else (None if None in vals else True)
    raise AssertionError('unrecognized expression '+repr(x))
def decide(rid,facts):
    m=bs[rid]['bounded_discriminator_projection']
    for rule in m['rules']:
        if eval_expr(rule['when'],facts) is True:return rule['then']
    return m['otherwise']

cases=[]
def case(name,rid,kind,base,changes,expected,distinction):
    facts={**base,**changes}
    actual=decide(rid,facts)
    cases.append({'name':name,'source_id':rid,'case_kind':kind,'facts':facts,'expected':expected,'actual':actual,'distinction':distinction,'passed':actual==expected})

rid='TICKET_METHOD.work-carrier-to-execution-rule'
b={'upstream_authority':True,'exact_admitted_ticket':False,'explicit_record_instruction':False,'ticket_state_authority':True,'surviving_state':False,'admitted_sprint':False}
case('ticket.explicit-authority-selects-durability',rid,'positive',b,{'explicit_record_instruction':True},'durable_ticket','An exact ticket-state instruction selects durable record despite no surviving state; this says nothing about execution admission.')
case('ticket.no-authority-no-execution-carrier',rid,'adverse',b,{'upstream_authority':False},'no_admitted_contract','Carrier creation cannot replace work authority.')
case('ticket.unknown-lifetime-is-not-one-run',rid,'unknown',b,{'surviving_state':None},'indeterminate','Unknown surviving obligations cannot be guessed absent.')
case('ticket.exact-ticket-reuse',rid,'positive',b,{'exact_admitted_ticket':True,'surviving_state':True},'reuse_exact_ticket','Existing exact ticket takes priority over new durable ticket.')
case('ticket.missing-ticket-authority-retains-debt',rid,'adverse',b,{'surviving_state':True,'ticket_state_authority':False},'retain_on_authorized_result_surface_and_withhold_ticket_dependent_closure','Missing ticket authority does not erase a surviving obligation or grant record creation.')

rid='TICKET_METHOD.condition-based-closure-and-reuse'
b={'governing_basis_interpretable':True,'authenticated_failure':False,'required_invalid_basis':False,'required_out_of_frame':False,'all_applicable_obligations_satisfied':True,'required_coverage_complete':True,'active_nonclosure':False,'required_acceptance_satisfied':True}
case('closure.writer-with-no-reserved-review',rid,'positive',b,{},'satisfied','No invented review or Executive appointment when all actual obligations including applicable decision law hold.')
case('closure.failure-survives-missing-slot',rid,'adverse',b,{'authenticated_failure':True,'all_applicable_obligations_satisfied':False,'required_coverage_complete':False},'falsified','Known failure remains visible beside uncovered required evidence.')
case('closure.unconfirmed-owner-acceptance',rid,'unknown',b,{'required_acceptance_satisfied':None},'indeterminate','A lawful other disposition or recorded review cannot supply required acceptance.')
case('closure.required-out-of-frame',rid,'adverse',b,{'required_out_of_frame':True,'all_applicable_obligations_satisfied':False},'out_of_frame','Required scope diagnosis is not silently omitted.')

rid='SPEC_METHOD.bounded-context-semantic-resolution'
b={'valid_semantic_address':True,'within_capability':True,'candidate_set_complete':True,'admissible_concept_count':1}
case('meaning.unique-address',rid,'positive',b,{},'satisfied','One complete admissible candidate set permits meaning selection.')
case('meaning.known-collision',rid,'adverse',b,{'admissible_concept_count':2},'falsified','Equal spelling with multiple meanings does not choose one.')
case('meaning.partial-search-not-zero',rid,'unknown',b,{'candidate_set_complete':False,'admissible_concept_count':0},'indeterminate','Incomplete acquisition is not a proved zero-candidate result.')

rid='SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021'
b={'composite_basis_interpretable':True,'demonstrated_violation':False,'all_participants_and_joins_established':True,'currentness_established':True,'actual_trust_boundary_validation_established':True,'grant_established':True}
case('admission.coherent-composite',rid,'positive',b,{},'satisfied','Coherent composite bases are permitted; satisfaction does not prove semantic commit.')
case('admission.stale-predecessor',rid,'adverse',b,{'demonstrated_violation':True,'currentness_established':False},'falsified','Stale predecessor on interpretable basis is violation, not invalid_basis.')
case('admission.unchanged-assertion-crosses-trust',rid,'unknown',b,{'actual_trust_boundary_validation_established':None},'indeterminate','Unchanged assertion still needs actual trust-boundary validation.')
case('admission.uninterpretable-mixed-basis',rid,'adverse',b,{'composite_basis_interpretable':False},'invalid_basis','No interpretable composite basis differs from an incompatible join on a coherent basis.')

rid='RELEASE_METHOD.selector-and-consumer-adoption'
b={'governing_basis_interpretable':True,'demonstrated_gate_violation':False,'observed_remote_complete':True,'annotated_selector_and_cut':True,'selector_matches_highest_published_ordinal':True,'same_line_downgrade':False,'plan_current':True,'exact_plan_accepted_by_authority':True}
case('release.accepted-current-channel-plan',rid,'positive',b,{},'satisfied','The gate is satisfied independently of whether adoption effect completed.')
case('release.stale-plan-refuses',rid,'adverse',b,{'plan_current':False,'demonstrated_gate_violation':True},'falsified','Prior digest acceptance does not authorize changed target/definition bytes.')
case('release.unavailable-remote',rid,'unknown',b,{'observed_remote_complete':None},'indeterminate','Unknown remote state cannot become latest-release evidence.')
case('release.channel-downgrade',rid,'adverse',b,{'same_line_downgrade':True,'demonstrated_gate_violation':True},'falsified','Channel downgrade is refused; explicitly pinned old-cut sync is a separate allowed route.')

rid='RELEASE_METHOD.exact-cut-qualification'
b={'governing_basis_interpretable':True,'performance':'performed','all_exact_claim_evidence':True,'coverage_complete':True,'admissible_counterevidence':False,'raw_label':'passed'}
case('qualification.exact-cut-performed',rid,'positive',b,{},'satisfied','Actual exact-claim coverage and evidence, rather than passed label, establish the property.')
case('qualification.failure-not-erased-by-green',rid,'adverse',b,{'admissible_counterevidence':True},'falsified','A stale green label cannot overwrite current admissible counterevidence.')
case('qualification.cached-green-unconfirmed',rid,'unknown',b,{'raw_label':'cached green','performance':'unconfirmed','all_exact_claim_evidence':None},'indeterminate','Cached label supplies neither performance nor deciding support.')

rid='TICKET_METHOD.sprint-close-review'
b={'governing_basis_interpretable':True,'demonstrated_close_violation':False,'all_items_and_debt_classified':True,'remaining_debt_permitted':True,'followup_durable':True,'required_close_review_performed':True,'item_compliance':'falsified','paydown_open':True}
case('sprint.lawful-close-with-open-paydown',rid,'positive',b,{},'satisfied','Close eligibility can hold while item compliance is false and debt remains unpaid.')
case('sprint.hidden-authority-drift',rid,'adverse',b,{'remaining_debt_permitted':False,'demonstrated_close_violation':True},'falsified','Durable ticket cannot make forbidden debt acceptable.')
case('sprint.unknown-followup-durability',rid,'unknown',b,{'followup_durable':None},'indeterminate','Classification words cannot substitute for durable follow-up.')

rid='RELEASE_METHOD.successor-baseline-conservation-stdo-up-015'
b={'governing_basis_interpretable':True,'semantic_counterexample':False,'disposition':'intentionally removed','retains_meaning':False,'excluded_from_governing_set':True,'actual_removal_decision_authorized':True}
case('conservation.authorized-removal-is-not-retention',rid,'positive',b,{},'satisfied','The exclusion predicate can hold without retained predecessor meaning; actual decision remains separate.')
case('conservation.false-retention',rid,'adverse',b,{'disposition':'conserved','semantic_counterexample':True},'falsified','Recording conserved does not establish retained semantics.')
case('conservation.unknown-no-effect',rid,'unknown',b,{'disposition':'not applicable','supported_no_successor_effect':None},'indeterminate','Unknown applicability cannot become non-applicability.')

assert all(c['passed'] for c in cases), [c for c in cases if not c['passed']]
for model_id in {c['source_id'] for c in cases}:
    assert {c['case_kind'] for c in cases if c['source_id']==model_id}>={'positive','adverse','unknown'}
repro=subprocess.run([sys.executable,str(HERE/'author_bindings.py'),'--check'],env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
assert repro.returncode==0,repro.stdout+repro.stderr
installed=json.loads(subprocess.check_output(['stdo','verify','v2.5.1-rc.2','--manifest-sha256',d['installed_builder_manifest_sha256']]))
assert installed['valid'] and not installed['failures']
report={
 'schema_version':'stdo.semantic-contribution-author-check.v1',
 'standing':'bounded_author_checks_only_not_independent_acceptance',
 'source_commit':SOURCE,'input_account_sha256':ACCOUNT,'bindings_sha256':sha(raw),
 'checks':{'source_member_pins':True,'live_source_preserved':True,'body_hashes':len(bs),'clause_hashes':clause_count,'stable_id_coverage':len(selected),'unfinished':0,'all_21_ready_rows_reauthored':sum(rows[rid]['interpretation_standing']=='bounded_semantic_binding' for rid in bs),'typed_dependency_targets_resolve':True,'reproduction':True,'installed_rc2_pin_verified':True},
 'source_members':source_checks,'representation_kind_corrections':changed_kind,
 'discriminator_cases':cases,'discriminator_case_count':len(cases),
 'limits':['Structural/source integrity checks are complete for the five selected owner members, not semantic completeness proof.','The 8 executable projections cover only named distinctions with supplied facts; they do not observe external state, decide all 173 predicates, confer grants or execute effects.','The author selected and assessed these cases; they are not the withheld oracle, independent source-first review, Product acceptance or release.']}
(HERE/'AUTHOR_CHECK.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'bindings':len(bs),'clauses':clause_count,'ready_reauthored':report['checks']['all_21_ready_rows_reauthored'],'discriminators':len(cases),'all_passed':True,'bindings_sha256':sha(raw)},indent=2))
