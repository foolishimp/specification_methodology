"""Narrow executable projections. They neither observe the world nor grant effects."""
def F(name): return {'fact':name}
def E(name,value): return {'eq':[F(name),value]}
def A(*args): return {'all':list(args)}
def N(arg): return {'not':arg}

def model(rid, question, rules, default='indeterminate'):
    b=next(b for b in bindings if b['id']==rid)
    b['bounded_discriminator_projection']={
        'question':question,
        'standing':'author_executable_projection_for_named_discriminators_only',
        'scope':'Facts are supplied test inputs, not acquired observations or minted grants. All conditions outside this named projection must independently be established for full-owner satisfaction. Unknown facts remain unknown.',
        'rules':[{'when':expr,'then':out} for expr,out in rules],
        'otherwise':default}

# Carrier selection makes the explicit ticket-state instruction an actual branch.
model('TICKET_METHOD.work-carrier-to-execution-rule','Which source carrier is selected, independently of execution admission?',[
    (E('upstream_authority',False),'no_admitted_contract'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',True)),'reuse_exact_ticket'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',False),E('explicit_record_instruction',True),E('ticket_state_authority',True)),'durable_ticket'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',False),E('surviving_state',True),E('ticket_state_authority',False)),'retain_on_authorized_result_surface_and_withhold_ticket_dependent_closure'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',False),E('surviving_state',True),E('ticket_state_authority',True)),'durable_ticket'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',False),E('explicit_record_instruction',False),E('surviving_state',False),E('admitted_sprint',True)),'manifest_local_entry'),
    (A(E('upstream_authority',True),E('exact_admitted_ticket',False),E('explicit_record_instruction',False),E('surviving_state',False),E('admitted_sprint',False)),'intake_run_contract')])
model('TICKET_METHOD.condition-based-closure-and-reuse','Does the exact work claim meet its currently required closure predicates?',[
    (E('governing_basis_interpretable',False),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('authenticated_failure',True)),'falsified'),
    (A(E('governing_basis_interpretable',True),E('authenticated_failure',False),E('required_invalid_basis',True)),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('authenticated_failure',False),E('required_invalid_basis',False),E('required_out_of_frame',True)),'out_of_frame'),
    (A(E('governing_basis_interpretable',True),E('authenticated_failure',False),E('required_invalid_basis',False),E('required_out_of_frame',False),E('all_applicable_obligations_satisfied',True),E('required_coverage_complete',True),E('active_nonclosure',False),E('required_acceptance_satisfied',True)),'satisfied')])
model('SPEC_METHOD.bounded-context-semantic-resolution','Does this occurrence have exactly one admissible meaning?',[
    (E('valid_semantic_address',False),'invalid_basis'),
    (A(E('valid_semantic_address',True),E('within_capability',False)),'out_of_frame'),
    (A(E('valid_semantic_address',True),E('within_capability',True),E('candidate_set_complete',True),E('admissible_concept_count',1)),'satisfied'),
    (A(E('valid_semantic_address',True),E('within_capability',True),E('candidate_set_complete',True),N(E('admissible_concept_count',1))),'falsified')])
model('SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021','Is this interpretable complete transition admissible, separate from semantic commit?',[
    (E('composite_basis_interpretable',False),'invalid_basis'),
    (A(E('composite_basis_interpretable',True),E('demonstrated_violation',True)),'falsified'),
    (A(E('composite_basis_interpretable',True),E('all_participants_and_joins_established',True),E('currentness_established',True),E('actual_trust_boundary_validation_established',True),E('grant_established',True),E('demonstrated_violation',False)),'satisfied')])
model('RELEASE_METHOD.selector-and-consumer-adoption','May a channel-selected plan be applied under its exact acceptance?',[
    (E('governing_basis_interpretable',False),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('demonstrated_gate_violation',True)),'falsified'),
    (A(E('governing_basis_interpretable',True),E('observed_remote_complete',True),E('annotated_selector_and_cut',True),E('selector_matches_highest_published_ordinal',True),E('same_line_downgrade',False),E('plan_current',True),E('exact_plan_accepted_by_authority',True),E('demonstrated_gate_violation',False)),'satisfied')])
model('RELEASE_METHOD.exact-cut-qualification','Does this exact-cut item establish its claimed property?',[
    (E('governing_basis_interpretable',False),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('admissible_counterevidence',True)),'falsified'),
    (A(E('governing_basis_interpretable',True),E('performance','performed'),E('all_exact_claim_evidence',True),E('coverage_complete',True),E('admissible_counterevidence',False)),'satisfied')])
model('TICKET_METHOD.sprint-close-review','Is sprint close eligible even if permitted local paydown remains?',[
    (E('governing_basis_interpretable',False),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('demonstrated_close_violation',True)),'falsified'),
    (A(E('governing_basis_interpretable',True),E('all_items_and_debt_classified',True),E('remaining_debt_permitted',True),E('followup_durable',True),E('required_close_review_performed',True),E('demonstrated_close_violation',False)),'satisfied')])
model('RELEASE_METHOD.successor-baseline-conservation-stdo-up-015','Does the claimed disposition predicate hold (separate from retention and decision authority)?',[
    (E('governing_basis_interpretable',False),'invalid_basis'),
    (A(E('governing_basis_interpretable',True),E('semantic_counterexample',True)),'falsified'),
    (A(E('governing_basis_interpretable',True),E('disposition','conserved'),E('retains_meaning',True)),'satisfied'),
    (A(E('governing_basis_interpretable',True),E('disposition','superseded'),E('named_replacement_relation_holds',True)),'satisfied'),
    (A(E('governing_basis_interpretable',True),E('disposition','intentionally removed'),E('excluded_from_governing_set',True)),'satisfied'),
    (A(E('governing_basis_interpretable',True),E('disposition','not applicable'),E('supported_no_successor_effect',True)),'satisfied')])

# Bind consumed design contracts without duplicating their local law.
extra_deps={
 'SPEC_METHOD.sufficient-execution-intake':['DESIGN_MODULE_METHOD.bounded-frame-conservation-stdo-up-017','DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016','DESIGN_MODULE_METHOD.invariant-reconstruction-sufficiency-stdo-up-018','DESIGN_MODULE_METHOD.computational-realization-projection-stdo-up-019'],
 'SPEC_METHOD.method':['DESIGN_MODULE_METHOD.proportional-design-sequencing'],
 'SPEC_METHOD.reconstruction-litmus':['DESIGN_MODULE_METHOD.5e-ontology-and-three-view-behavioral-design-gate'],
 'SPEC_METHOD.proportional-method-and-delivery-stdo-up-014':['DESIGN_MODULE_METHOD.computational-realization-projection-stdo-up-019'],
 'SPEC_METHOD.testing-strategy-taxonomy':['DESIGN_MODULE_METHOD.6a-design-to-module-to-implementation-unit-tests-evidence-route']}
for rid,deps in extra_deps.items():
    b=next(b for b in bindings if b['id']==rid)
    for dep in deps:
        assert dep in rows
        if dep not in b['dependencies']:
            b['dependencies'].append(dep)
            b['dependency_relations'].append({'id':dep,'kind':'conditional_contract_application'})

taxonomy=next(b for b in bindings if b['id']=='SPEC_METHOD.recursive-product-taxonomy')
taxonomy['concept_identities']={name:'urn:stdo:concept:recursive-product-taxonomy:'+slug for name,slug in [('Substrate','substrate'),('Development Product','development-product'),('Source Project','source-project'),('Release Cut','release-cut'),('Product','product'),('Install','install'),('Artifact','artifact'),('Product Definition','product-definition')]}
