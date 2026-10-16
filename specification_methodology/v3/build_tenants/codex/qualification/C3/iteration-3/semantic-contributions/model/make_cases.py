#!/usr/bin/env python3
"""Explicit author cases: expected distinctions were selected from the frozen owners."""
import json,pathlib,copy
P=pathlib.Path(__file__).resolve().parent; W='WORLD_MODEL_METHOD.'; U='UX_METHOD.'; cases=[]
def case(id,kind,ids,why,x,y):cases.append({'id':id,'kind':kind,'unit_ids':ids,'source_discriminant':why,'input':x,'expected':y})
S={s:'satisfied' for s in ['identity','boundary','authority','state','evidence','treatment','covariance','ambiguity']}
base={'surfaces':S,'discrimination':'satisfied','comparison_population':False,'repeated_contexts':False,'intervention_permission':False,'overlay_present':False,'treatment_value':'supported absence'}
case('entity_sparse_supported_absence','entity_admission',[W+'admissibility'], 'A sparse unique cut can satisfy all surfaces with supported absence; no geometric/null/intervention prerequisite.',base,{'eligibility':'satisfied','requires_overlay':False})
x=copy.deepcopy(base);x['surfaces']['treatment']='indeterminate';x['treatment_value']='absence asserted without support'
case('entity_unsupported_absence','entity_admission',[W+'admissibility'],'An absence statement needs support; spelling the field is insufficient.',x,{'eligibility':'indeterminate','requires_overlay':False})
x=copy.deepcopy(base);x['surfaces']['boundary']='falsified';x['surfaces']['evidence']=None
case('entity_failed_and_missing','entity_admission',[W+'admissibility'],'Known boundary failure remains despite a missing evidence judgment.',x,{'eligibility':'falsified','requires_overlay':False})
x=copy.deepcopy(base);x['discrimination']='indeterminate'
case('entity_unknown_discrimination','entity_admission',[W+'discrimination'],'Source availability without established discrimination cannot satisfy admission.',x,{'eligibility':'indeterminate','requires_overlay':False})
over={'selected':True,'declared_space':True,'paired_evidence':True,'extraction':'mean_offset','verification':'satisfied','uniqueness':'satisfied','transfer':'satisfied','stored_surfaces':True,'statistical_standing':'candidate','core_size_matches_null':True}
case('overlay_verified_candidate','overlay_eligibility',[W+'3-verification-by-treatment',W+'5-null-peer-discrimination'],'Treatment and null-peer success establish eligibility only, with size overlap allowed and statistical candidate standing retained.',over,{'applicable':True,'eligibility':'satisfied','statistical_standing':'candidate'})
for id,changes,expected,why in [
 ('overlay_pca_rejected',{'extraction':'pca'},'falsified','Maximum-variance directions fail even when later behavior looks favorable.'),
 ('overlay_verification_unrun',{'verification':None},'indeterminate','No acceptable treatment verification means publication eligibility stays unresolved.'),
 ('overlay_uniqueness_failed_transfer_missing',{'uniqueness':'falsified','transfer':None},'falsified','One failed required null-peer predicate remains failed while the other is missing.'),
 ('overlay_missing_space',{'declared_space':None},'indeterminate','An unknown representation binding cannot be invented.'),
 ('overlay_lost_provenance',{'stored_surfaces':False},'falsified','A storage layout losing required support is not lawful.')]:
 x=copy.deepcopy(over);x.update(changes);case(id,'overlay_eligibility',[W+'markov-object-construction-law',W+'2-identity-direction-extraction',W+'7-storage-shape'],why,x,{'applicable':True,'eligibility':expected,'statistical_standing':'candidate'})
case('overlay_not_selected','overlay_eligibility',[W+'markov-object-construction-law'],'Supported absence of overlay selection excludes only overlay duties; it creates no extra verdict.',{'selected':False},{'applicable':False,'eligibility':None})
for id,v,e,why in [('directions_same_space',True,'satisfied','Space compatibility holds for this isolated join; other joins still need evidence.'),('directions_cross_space',False,'falsified','Generic translation availability cannot waive the domain prohibition.'),('directions_space_unknown',None,'indeterminate','Unknown space identity cannot be treated as compatible.')]:
 case(id,'direction_composition',[W+'composition-law'],why,{'same_space':v,'generic_translation_available':True},{'verdict':e})
case('statistical_gate_still_failed','statistical_promotion',[W+'epistemic-status-of-the-construct'],'Publication verification cannot erase failed conditional independence.',{'conditional_independence':'falsified','publication_verified':True},{'verdict':'falsified','publication_verified':True})
case('statistical_gate_unrun','statistical_promotion',[W+'epistemic-status-of-the-construct'],'Verified publication cannot fill an unrun stronger test.',{'conditional_independence':'indeterminate','publication_verified':True},{'verdict':'indeterminate','publication_verified':True})
for id,x,e,why in [
 ('ephemera_hover_local',{'other_view_observes':False,'product_state':False,'unmount_consequence':False},'satisfied','A truly local hover flag may use a local cell.'),
 ('ephemera_shared_draft',{'other_view_observes':True,'product_state':False,'unmount_consequence':False},'falsified','A draft observed by another view needs reducer ownership.'),
 ('ephemera_lost_selection',{'other_view_observes':False,'product_state':True,'unmount_consequence':True},'falsified','Losing Product selection on unmount defeats the local-cell exception.'),
 ('ephemera_unknown_visibility',{'other_view_observes':None,'product_state':False,'unmount_consequence':False},'indeterminate','Unknown visibility does not establish the exception.')]:
 case(id,'local_ephemera',[U+'5-state-transition-law'],why,x,{'local_cell_allowed':e})
for id,v,e in [('carrier_admitted',True,'satisfied'),('carrier_known_absent',False,'falsified'),('carrier_unresolved',None,'indeterminate')]:
 case(id,'product_action',[U+'3a-ux-projection-and-constructive-carrier-boundary'], 'A product-truth action needs actual admitted carrier; a Cmd or UI label cannot supply it.',{'admitted_carrier':v},{'action_eligible':e})
for id,x,y,why in [
 ('replay_unknown_effect_correct',{'expected_trace_matches':True,'performance':'performed','possible_effect':True}, {'replay':'satisfied','performance':'performed','effect':'unknown'},'Correct replay of typed lost-acknowledgment outcome does not prove mutation absent/completed.'),
 ('replay_projection_empty_cmd',{'expected_trace_matches':True,'performance':'performed','possible_effect':False,'established_effect_free':True}, {'replay':'satisfied','performance':'performed','effect':'not_requested'},'A declared effect-free projection can prove empty Cmd trace.'),
 ('replay_hidden_state',{'expected_trace_matches':True,'performance':'performed','possible_effect':True,'hidden_dependency':True}, {'replay':'falsified','performance':'performed','effect':'unknown'},'Matching output obtained through excluded hidden state fails the replay contract.'),
 ('replay_unrun',{'expected_trace_matches':True,'performance':'not_performed','possible_effect':False,'established_effect_free':True}, {'replay':'indeterminate','performance':'not_performed','effect':'not_requested'},'A predicted matching trace cannot satisfy an unperformed replay.'),
 ('replay_missing_trace',{'expected_trace_matches':None,'performance':'unconfirmed','possible_effect':True}, {'replay':'indeterminate','performance':'unconfirmed','effect':'unknown'},'Missing trace establishes neither performance nor effects.'),
 ('replay_bad_order_known_complete_effect',{'expected_trace_matches':False,'performance':'performed','observed_effect':'completed'}, {'replay':'falsified','performance':'performed','effect':'completed'},'Actual effect completion cannot rescue a wrong ordered command trace.')]:
 case(id,'effect_and_replay',[U+'6-effect-membrane-rule',U+'8a-msg-replay-proof-requirement'],why,x,y)
sc={n:True for n in ['scope','operations','mutation_bound','visible_label','superseding_surface','retirement_ticket_condition','nonclosure']}
case('scaffold_bounded_complete','scaffold',[U+'13a-scaffold-and-exemption-law'],'All named exemption fields are established.',sc,{'exemption_valid':'satisfied'})
x=dict(sc);x['retirement_ticket_condition']=False
case('scaffold_no_retirement','scaffold',[U+'13a-scaffold-and-exemption-law'],'A visible debug label cannot replace retirement ownership.',x,{'exemption_valid':'falsified'})
x=dict(sc);x['mutation_bound']=None
case('scaffold_unknown_mutation_bound','scaffold',[U+'13a-scaffold-and-exemption-law'],'Unknown operations do not establish a bounded exemption.',x,{'exemption_valid':'indeterminate'})
case('escrow_replay_updates','escrow',[U+'13b-ux-sprint-compliance-escrow'],'Replay update debt is permitted local proof work inside an authorized sprint.',{'local_allowed_debt':True,'forbidden_semantic_change':False},{'escrow_eligible':'satisfied'})
case('escrow_new_selection_authority','escrow',[U+'13b-ux-sprint-compliance-escrow'],'Meaning-changing selection authority cannot hide in UX escrow.',{'local_allowed_debt':True,'forbidden_semantic_change':True},{'escrow_eligible':'falsified'})
sp={'all_classified':True,'debt_permitted':True,'followup_durable':True,'no_unclassified_carrier_continuation_authority':True,'item_compliance':'indeterminate','applicable_ux_checks':['satisfied','indeterminate']}
case('sprint_closed_proof_open','sprint_close',[U+'13b-ux-sprint-compliance-escrow'],'Classified permitted durable local debt allows sprint closure but not method closure.',sp,{'sprint_close':'satisfied','item_compliance':'indeterminate','method_closure':'indeterminate'})
x=dict(sp);x['item_compliance']='falsified';x['applicable_ux_checks']=['falsified','indeterminate']
case('sprint_closed_defect_retained','sprint_close',[U+'13b-ux-sprint-compliance-escrow'],'Lawful local paydown can coexist with an actual defect; the failure remains.',x,{'sprint_close':'satisfied','item_compliance':'falsified','method_closure':'falsified'})
x=dict(sp);x['no_unclassified_carrier_continuation_authority']=False
case('sprint_unclassified_continuation','sprint_close',[U+'13b-ux-sprint-compliance-escrow'],'An unclassified hidden-continuation finding blocks sprint close.',x,{'sprint_close':'falsified','item_compliance':'indeterminate','method_closure':'indeterminate'})
case('remove_lawful_compliance_unknown','treatment',[U+'13b-ux-sprint-compliance-escrow'],'A lawful removal decision is independent of compliance evidence and observed removal effects.',{'actual_mandate_and_conditions':True,'compliance':'indeterminate','effect':'unknown','treatment':'remove'},{'decision':'satisfied','compliance':'indeterminate','effect':'unknown','treatment':'remove'})
(P/'cases.json').write_text(json.dumps(cases,indent=2)+'\n');print(len(cases))
