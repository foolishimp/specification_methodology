"""Serialize this bounded author return from frozen inputs; no source/account edits."""
import collections
import copy
import json
import re
from pathlib import Path

from acquire import ACCOUNT_COMMIT, ACCOUNT_PATH, BASE, HERE, SOURCE_COMMIT
from acquire import account, git_bytes, sha, sources, unit

COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
GRANT = 'fc1229d398b4293e1283371da30695cbc6bb4a0a'


def write(name, value):
    raw = (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()
    (HERE / name).write_bytes(raw)
    return sha(raw)


def main():
    a = account()
    rows = a['determinations']
    by_id = {r['id']: r for r in rows}
    positions = {r['id']: n for n, r in enumerate(rows)}
    empty = [r for r in rows if not r.get('consumers')]
    raw = sources(rows)
    units = {r['id']: unit(r, raw[r['owner']['path']]) for r in rows}
    acquired = json.loads((HERE / 'ACQUIRED_SLICES.json').read_text())
    best = {}
    for item in acquired:
        if item['bytes'] > best.get(item['id'], {}).get('bytes', -1):
            best[item['id']] = item

    def source_ref(identifier):
        r, u = by_id[identifier], units[identifier]
        return dict(commit=SOURCE_COMMIT, path=BASE+'successor/'+r['owner']['path'],
                    anchor=r['owner'].get('anchor',''), byte_start=u['byte_start'],
                    byte_end=u['byte_end'], start_line=u['start_line'],
                    end_line=u['end_line'], body_sha256=sha(u['body']))

    def account_ref(identifier, field=None, index=None):
        ptr = '/determinations/' + str(positions[identifier])
        if field is not None:
            ptr += '/' + field
        if index is not None:
            ptr += '/' + str(index)
        return dict(commit=ACCOUNT_COMMIT, path=ACCOUNT_PATH, pointer=ptr,
                    row_id=identifier)

    reverse = collections.defaultdict(set)
    for r in rows:
        for d in r.get('dependencies', []):
            reverse[d].add(r['id'])
    diagnostics, updates = [], []
    for r in rows:
        current = r.get('consumers', [])
        missing = sorted(reverse[r['id']] - set(current))
        retained = sorted(set(current) - reverse[r['id']])
        if missing or retained:
            diagnostics.append(dict(id=r['id'], preimage_present='consumers' in r,
                                    preimage_consumers=current,
                                    missing_authored_dependency_inverses=missing,
                                    retained_positive_without_reciprocal_dependency=retained,
                                    disposition='add supported inverse projections; preserve all existing positives; unmatched positives require source-owner reconciliation'))
        if missing:
            evidence = []
            for consumer in missing:
                dep = by_id[consumer]
                evidence.append(dict(
                    consumer_id=consumer,
                    kind='existing_authored_contract_dependency',
                    account=account_ref(consumer,'dependencies',dep['dependencies'].index(r['id'])),
                    consumer_source=source_ref(consumer),
                    consumer_source_unchanged_from_authored_account=
                        sha(units[consumer]['body']) == dep['owner']['body_sha256'],
                    scope='Reuses the already-authored dependency under its existing applicability and typed relations; adds no semantic dependency or new operational requirement.'))
            updates.append(dict(id=r['id'], field='consumers',
                                preimage_present='consumers' in r, preimage=current,
                                replacement=current + missing, evidence=evidence,
                                source=source_ref(r['id'])))
    inverse = dict(
        kind='authored_account_patch_proposal', producer='RC1-CONSUMERS',
        source_commit=SOURCE_COMMIT, account_commit=ACCOUNT_COMMIT,
        account_path=ACCOUNT_PATH, common_input=COMMON,
        field_contract=a['field_semantics']['consumers'],
        meaning='Restore missing inverse projections of existing authored dependencies. This is one stale-projection class, not one newly discovered semantic defect per pair.',
        preserve='Every prior positive consumer remains, including positives without a current reciprocal dependency.',
        limits=['No independent judgment of the 100 existing semantic dependencies.',
                'All dependency-declaring immediate source bodies are unchanged from the authored account.',
                'Eleven unmatched prior positive pairs remain unresolved; this addition-only proposal does not make the relation an exact inverse.'],
        updates=updates)
    inverse_hash = write('INVERSE_PROJECTION_PATCH.json',inverse)
    after_inverse = {r['id']: list(r.get('consumers', [])) for r in rows}
    for u in updates:
        after_inverse[u['id']] = u['replacement']

    calls = [
        ('CARRIER.plugins.spec.skills.stdo-help.SKILL.md', 'CARRIER.plugins.spec.references.PRODUCT_BASIS.md', 'before routing or answering'),
        ('CARRIER.plugins.spec.skills.stdo-review.SKILL.md', 'CARRIER.plugins.spec.references.PRODUCT_BASIS.md', 'before activating review'),
        ('CARRIER.plugins.spec.skills.stdo-status.SKILL.md', 'CARRIER.plugins.spec.references.PRODUCT_BASIS.md', 'before reporting status'),
        ('CARRIER.plugins.spec.skills.stdo-ticket.SKILL.md', 'CARRIER.plugins.spec.references.PRODUCT_BASIS.md', 'before proposing or mutating ticket state'),
        ('CARRIER.plugins.spec.claude-skills.refresh.SKILL.md', 'CARRIER.plugins.spec.references.REFRESH.md', 'manual-only refresh invocation'),
    ]
    call_evidence, reciprocal_updates = [], []
    new_consumers = collections.defaultdict(list)
    for consumer, owner, when in calls:
        r = by_id[consumer]
        body = units[consumer]['body']
        if 'claude-skills' in consumer:
            needle = b'Read and follow'
            start = body.index(needle)
            end = body.index(b'\n\n', start)
        else:
            start = body.index(b'Read and apply')
            end = body.index(b'\n\n', start)
        quote = body[start:end]
        call_applicability = ('The user explicitly invokes the manual-only /spec:refresh adapter; disable-model-invocation is true.'
                              if 'claude-skills' in consumer else r['applicability'])
        ev = dict(consumer_id=consumer, owner_id=owner,
                  relation='required_procedure_call_within_selected_workflow',
                  modal_force='Required after this workflow is selected; no general workflow invocation or effect authority is created.',
                  required_when=call_applicability, existing_account_applicability=r['applicability'], operation_boundary=when,
                  provenance_only=False, source=source_ref(consumer),
                  quote=quote.decode(), quote_byte_start=units[consumer]['byte_start']+start,
                  quote_byte_end=units[consumer]['byte_start']+end, quote_sha256=sha(quote),
                  owner_source=source_ref(owner),
                  applicability_preservation='The consumer row already binds this workflow applicability. Its mandatory call is inside that existing boundary; the owner procedure supplies its own stops and read-only limits.')
        call_evidence.append(ev)
        reciprocal_updates.append(dict(id=consumer,field='dependencies',
            preimage_present='dependencies' in r,preimage=r.get('dependencies',[]),
            replacement=r.get('dependencies',[])+[owner], evidence=[ev]))
        new_consumers[owner].append(consumer)
    for owner, consumers in new_consumers.items():
        reciprocal_updates.append(dict(id=owner,field='consumers',
            preimage_present=True,preimage=after_inverse[owner],
            replacement=after_inverse[owner]+consumers,
            evidence=[ev for ev in call_evidence if ev['owner_id']==owner]))
    reciprocal = dict(
        kind='authored_account_patch_proposal',producer='RC1-CONSUMERS',
        source_commit=SOURCE_COMMIT,account_commit=ACCOUNT_COMMIT,account_path=ACCOUNT_PATH,
        required_patch=dict(filename='INVERSE_PROJECTION_PATCH.json',sha256=inverse_hash),
        purpose='Five explicit procedure calls missing from the authored dependency graph; reciprocal consumers are updated in the same selected transaction.',
        boundary='Separate Executive disposition before integration; source-supported author proposal, not acceptance or qualification.',
        limits=['No other source links become dependencies.',
                'These calls preserve existing workflow selection, read-only acquisition, refusal and effect boundaries.',
                'The existing broad workflow applicability for the manual-only Claude adapter is not widened by this edge; its source remains manual-only.'],
        updates=reciprocal_updates)
    reciprocal_hash = write('RECIPROCAL_CALL_PATCH.json', reciprocal)

    explicit = collections.defaultdict(list)
    # These contracts expressly select the rules as decision evidence. A mere
    # occurrence of a Markdown link elsewhere is not used as this inference.
    design_consumer = 'DESIGN_MODULE_METHOD.14-design-review-questions'
    design_body = units[design_consumer]['body'].decode()
    design_targets = set(re.findall(r'\]\(#([^)]*)\)', design_body))
    for r in empty:
        if r['owner']['path']=='standards/DESIGN_MODULE_METHOD.md' and r['owner'].get('anchor') in design_targets:
            explicit[r['id']].append(dict(consumer=design_consumer,
                relation='applicable_design_review_decision_evidence',
                condition='Only at review of the exact adopted boundary and applicable claim; language and profile triggers remain owned by the selected rule.',
                evidence=source_ref(design_consumer),
                reason='The consumer expressly requires applicable owners with the actual design and implementation, and selects this owner in its decision-evidence table.',
                graph_patch_proposed=False))
    for r in empty:
        if r['id'].startswith('AXIOMATIC_CALCULUS.ac-'):
            explicit[r['id']].append(dict(consumer='AXIOMATIC_CALCULUS.conformance-obligations',
                relation='law_conformance_case_selection',
                condition='Review and qualification of the fundamental standard; positive and refusal cases for every fundamental law.',
                evidence=source_ref('AXIOMATIC_CALCULUS.conformance-obligations'),
                reason='The consumer names every fundamental law as a conformance population, including identity, authority, residual, closure and overlay distinctions.',
                graph_patch_proposed=False))
    for owner in ['UX_METHOD.9-view-shape-rule','UX_METHOD.12-realization-discretion']:
        explicit[owner].append(dict(consumer='UX_METHOD.15-review-questions',
            relation='applicable_ux_review_question',condition='Review of an adopted UX surface.',
            evidence=source_ref('UX_METHOD.15-review-questions'),
            reason='The review asks for pure View behavior and the selected realization stack with preserved process model; these are the named rule decisions, not a generic related link.',
            graph_patch_proposed=False))
    for r in empty:
        for consumer in sorted(reverse[r['id']]):
            explicit[r['id']].append(dict(consumer=consumer,
                relation='existing_authored_contract_dependency',
                condition='The existing consumer applicability, source binding and typed dependency relations apply.',
                evidence=dict(account=account_ref(consumer,'dependencies'),source=source_ref(consumer)),
                graph_patch_proposed=True))
    for ev in call_evidence:
        explicit[ev['owner_id']].append(dict(consumer=ev['consumer_id'],
            relation=ev['relation'],condition=ev['required_when'],evidence=ev,
            graph_patch_proposed=True))

    argument_rows = {
        'AXIOMATIC_CALCULUS.fundamental-laws','FOUNDATIONS.core-contract-derivations',
        'SPEC_METHOD.method-families','TICKET_METHOD.carrier-families'}
    pure_data = {
        'REFERENCE_FRAME_METHOD.activated-frame','REFERENCE_FRAME_METHOD.active-frame-configuration',
        'REFERENCE_FRAME_METHOD.coverage-dimensions','REFERENCE_FRAME_METHOD.evaluation',
        'REFERENCE_FRAME_METHOD.material-relation-manifold','REFERENCE_FRAME_METHOD.minimal-evaluation-result',
        'REFERENCE_FRAME_METHOD.role-persona-abstraction-and-component',
        'WORLD_MODEL_METHOD.adjoint-mapping','WORLD_MODEL_METHOD.app','WORLD_MODEL_METHOD.assurance',
        'WORLD_MODEL_METHOD.attribute-ledger','WORLD_MODEL_METHOD.composed-world-model',
        'WORLD_MODEL_METHOD.covariance-edge','WORLD_MODEL_METHOD.domains-are-functional-surfaces',
        'WORLD_MODEL_METHOD.fragment','WORLD_MODEL_METHOD.projection',
        'WORLD_MODEL_METHOD.published-domain-artifact','WORLD_MODEL_METHOD.world-model-object',
        'WORLD_MODEL_METHOD.world-models-externalize-expert-cognition'}
    titles = {'ODD_METHOD.odd-method',
        'TRAVERSAL_OCCURRENCE_PROFILE.the-a_c-traversal-occurrence-profile-over-mutable-subjects',
        'UX_METHOD.ux-method','WORLD_MODEL_METHOD.world-model-method'}
    preambles = {'FOUNDATIONS.stdo-foundations','RELEASE_METHOD.release-method',
        'SPEC_METHOD.spec-driven-homeostatic-methodology','TICKET_METHOD.ticket-method',
        'TRANSFORMATION_LIBRARY.transformation-library','WRITING_GUIDE.writing-guide'}
    classified=[]
    for r in empty:
        identifier=r['id']; kind=r['representation_kind']; u=units[identifier]
        observed=best.get(identifier)
        if kind=='non_deciding_locator':
            if identifier in titles:
                role='title_locator'
                why='The exact immediate body is a title and profile-binding marker; child headings own their separate bodies. No independent rule is asserted in this immediate-body scope.'
            elif 'canonical-compression' in identifier:
                role='non_deciding_synopsis'
                why='This canonical compression is a summary of owned decisions. Its material content still requires projection fidelity; an empty inverse list neither proves fidelity nor removes the underlying duties.'
            else:
                role='illustrative_example'
                why='The body is an illustrative lawful/unlawful case or an explicitly non-normative worked binding. Its explanatory use is not another independently owned assessment predicate.'
            materiality='not_an_additional_independent_law; source and projection fidelity remain material where used'
        elif kind=='constraint':
            role='material_constraint_or_task_gate'
            why='The source-owned predicate and applicability select a concrete admission, construction, assessment, publication, identity or presentation decision. Its own application scope is accounted; a separate rule consumer is not inferred from that fact.'
            materiality='material_within_owned_applicability'
        elif kind=='consumer_binding':
            role='member_entry_binding' if identifier in preambles else 'conditional_task_or_contract_binding'
            why='This row imports or applies named owner decisions at its declared entry or domain boundary. Its outgoing authored dependencies describe that use. An empty incoming inverse list does not negate its consuming role or establish absence of later use.'
            materiality='material_binding_within_owned_applicability; not_an_independent_restatement_of_imported_law'
        elif identifier.startswith('CARRIER.'):
            role='conditional_schema_or_template_carrier'
            why='The schema/template is instantiated or checked under its selected Product and owning contracts. Its existing predicate is conditional carrier conformance, not a new universal law or an unconditional instruction to instantiate it.'
            materiality='material_when_selected_or_instantiated'
        elif identifier in argument_rows:
            role='source_argument_and_provenance'
            why='The source table groups conditional arguments and names additional policy owners. Its argument references are provenance for law/fidelity assessment, not an unconditional operational dependency or a second law owner.'
            materiality='material_to_argument_or_fidelity_assessment; no_independent_operational_predicate'
        elif identifier in pure_data:
            role='definition_or_descriptive_value'
            why='This body defines a term, relation, lens or result-carrier shape. The absence of an independent assessment predicate is correct for that data role; uses of its meaning may still be material and remain a separate relation question.'
            materiality='semantic_definition_material_where_used; no_separate_assessment_predicate_asserted'
        elif identifier=='RELEASE_METHOD.open-questions':
            role='explicit_unresolved_policy_questions'
            why='The body explicitly leaves Product-class qualification and compatibility policy questions open. It cannot be converted into completed policy or a proved absence of consumers.'
            materiality='unresolved_policy_scope'
        elif identifier=='WORLD_MODEL_METHOD.method-flow':
            role='structural_stage_heading'
            why='The immediate body announces the following stages. Each stage body is a separate accounting unit; this heading supplies no independent assessment predicate.'
            materiality='not_an_additional_independent_law_in_immediate_body'
        else:
            role='definition_with_material_conditions_or_scope'
            why='Definition/data classification does not establish non-materiality. This source also carries required shape, scope, applicability, authority, lifecycle or publication conditions; retain those conditions at the source and its existing account binding. This return does not promote all descriptive language into an independent law.'
            materiality='material_conditions_or_scope_retained; complete_embedded_duty_consumer_coverage_not_claimed'
        covered=bool(explicit[identifier])
        if covered:
            standing='named_consumer_relation_supported_with_stated_scope'
        elif role in {'title_locator','illustrative_example','structural_stage_heading'}:
            standing='no_independent_law_consumer_required_for_this_immediate_unit'
        elif role=='non_deciding_synopsis':
            standing='projection_role_accounted; actual_use_and_fidelity_remain_external'
        else:
            standing='owner_role_and_applicability_accounted; separate_consumer_relation_unresolved'
        classified.append(dict(
            id=identifier, account_row=account_ref(identifier),
            preimage_consumers_present='consumers' in r, preimage_consumers=r.get('consumers',[]),
            representation_kind=kind, accounting_role=role,
            materiality=materiality, reason=why,
            source=source_ref(identifier), acquired_slice=observed,
            existing_applicability=r.get('applicability',a.get('owner_families',{}).get(r['owner']['path'],{}).get('applicability')),
            existing_predicate_ref=account_ref(identifier,'predicate'),
            existing_dependencies=r.get('dependencies',[]),
            argument_ref=account_ref(identifier,'argument'),
            supported_named_consumers=explicit[identifier],
            coverage_standing=standing,
            absence_scope=('Only the independently deciding role of this exact immediate body is absent; children/owning laws remain separate.'
                if role in {'title_locator','illustrative_example','structural_stage_heading'} else
                'No global or source-level absence of consumers established. Empty inverse extraction is only a fact about this authored graph.'),
            residuals=([] if role in {'title_locator','illustrative_example','structural_stage_heading'} else [
                'Additional affected consumers and semantic adequacy beyond the named evidence remain unproved.',
                'Long-body acquisition and existing author arguments do not supply independent complete-clause fidelity or acceptance.'])))
    role_counts=collections.Counter(r['accounting_role'] for r in classified)
    standing_counts=collections.Counter(r['coverage_standing'] for r in classified)
    classification=dict(
        kind='bounded_author_consumer_account',producer='RC1-CONSUMERS',
        source_commit=SOURCE_COMMIT,account_commit=ACCOUNT_COMMIT,
        query='determinations rows for which consumers is absent or empty',
        population=len(classified),source_account_population=len(rows),
        representation_counts=dict(collections.Counter(r['representation_kind'] for r in classified)),
        role_counts=dict(role_counts),coverage_counts=dict(standing_counts),
        field_semantics={k:a['field_semantics'][k] for k in ['consumers','dependencies','empty_fields','representation_kind','predicate','argument']},
        bounds=['This is one evidence report over the one authored account, not a second owner or replacement semantic inventory.',
                'Classification is complete for the 389 queried rows; complete material consumer coverage and independent qualification are not established.',
                'Named source calls are supported only where the source explicitly makes that determination relevant to the actual consuming question.',
                'Direct owner applicability and nondeciding role are distinct from proof that no separate consumer exists.',
                'Existing source-family arguments and dependencies remain author evidence at their exact account pointers; no linked argument is promoted to an independently proved entailment.'],
        rows=classified)
    classification_hash=write('CLASSIFICATION.json',classification)
    diag_hash=write('GRAPH_DIAGNOSTICS.json',dict(
        source_commit=SOURCE_COMMIT,account_commit=ACCOUNT_COMMIT,
        field_contract=a['field_semantics']['consumers'],
        mismatch_rows=len(diagnostics),missing_pairs=sum(len(d['missing_authored_dependency_inverses']) for d in diagnostics),
        retained_unmatched_positive_pairs=sum(len(d['retained_positive_without_reciprocal_dependency']) for d in diagnostics),
        interpretation='One stale inverse-projection class is established. Whether each unmatched positive is stale or instead names a missing dependency requires source-owner reconciliation; none is deleted.',
        rows=diagnostics))

    # Deduplicate byte intervals rather than claiming exact-slice equality is
    # enough when a longer acquisition contains an earlier prefix.
    intervals=collections.defaultdict(list)
    for e in acquired:
        intervals[(e['source_commit'],e['path'])].append((e['byte_start'],e['byte_end']))
    novel=0
    for spans in intervals.values():
        merged=[]
        for lo,hi in sorted(spans):
            if merged and lo<=merged[-1][1]:merged[-1]=(merged[-1][0],max(hi,merged[-1][1]))
            else:merged.append((lo,hi))
        novel+=sum(hi-lo for lo,hi in merged)
    total=sum(e['bytes'] for e in acquired)
    measurement=dict(
        boundary='Instrumented raw-source text submitted by acquire.py, beginning after authority/account reconnaissance. Byte spans are half-open and repeats use interval overlap.',
        newly_presented_source_bytes=novel,repeated_source_bytes=total-novel,
        total_instrumented_source_bytes=total,unique_source_rows=len(best),
        full_immediate_bodies_acquired=sum(e['full_immediate_body'] for e in best.values()),
        earlier_uninstrumented=['root and v3 AGENTS; frozen grant; Product Definition, README, Goals, Intent, Product, frame basis and tenant entry contract',
            'selected requirements lines, installed bootstrap, account_protocol helper and selected authored-account fields'],
        end_to_end_bytes=None,
        limitation='Early tool outputs were selected/truncated without a byte ledger. Their delivered unique/repeated byte split cannot be certified retrospectively. No end-to-end 512 KiB fit claim is made. Subsequent source reads stopped after the bounded classification and explicit-call witnesses.',
        native_local_tools_only=True,paid_calls=0,subdelegations=0,
        output_truncation='The first definition-data batch contained long JSON schemas and was tool-truncated. Schema classifications use carrier identity/selected applicability, not a claimed complete semantic reading of those JSON bodies.')
    measurement_hash=write('ACQUISITION.json',measurement)
    # Concrete internal artifact checks only; no test suite or qualification run.
    assert len(classified)==389 and len(set(r['id'] for r in classified))==389
    assert set(r['id'] for r in classified)==set(r['id'] for r in empty)
    assert len(updates)==29 and sum(len(u['replacement'])-len(u['preimage']) for u in updates)==100
    assert len(calls)==5 and len(reciprocal_updates)==7
    assert all(set(u['preimage'])<=set(u['replacement']) for u in updates+reciprocal_updates)
    assert all(ev['consumer_source_unchanged_from_authored_account'] for u in updates for ev in u['evidence'])
    assert 'SPEC_METHOD.construction-assessment-and-delegation' not in {u['id'] for u in updates+reciprocal_updates}
    result=dict(
        activation='RC1-CONSUMERS',standing='author construction; no independent grade or qualification',
        common_input=COMMON,grant_commit=GRANT,account_commit=ACCOUNT_COMMIT,source_commit=SOURCE_COMMIT,
        overall_result=dict(verdict='satisfied',predicate='The complete queried population is classified with exact coordinates, bounded evidence, explicit unknowns and minimal additive proposals; no source/current account/Git mutation was performed.',
                            performance='performed',effects='Only files under qualification/C3/rc1/consumer-account/ were created.'),
        complete_material_coverage=dict(verdict='indeterminate',reason='The named consumer witnesses establish only their stated scope; separate consumer relations, long-body completeness, unmatched prior positives and independent fidelity remain unresolved.'),
        work_result='candidate_ready',population=389,coverage_counts=dict(standing_counts),
        inverse_projection=dict(rows=29,existing_dependency_pairs=100,previously_empty_rows=4,
                                retained_unmatched_positive_pairs=11),
        reciprocal_calls=dict(required_within_selected_workflow=5,dependency_updates=5,consumer_updates=2,
                              preserves_existing_invocation_and_effect_limits=True),
        files={'CLASSIFICATION.json':classification_hash,'INVERSE_PROJECTION_PATCH.json':inverse_hash,
               'RECIPROCAL_CALL_PATCH.json':reciprocal_hash,'GRAPH_DIAGNOSTICS.json':diag_hash,
               'ACQUISITION.json':measurement_hash},
        verification='Population identity/count, 100 inverse additions, 5 source-call witnesses, monotone preservation, exact dependency-owner body reuse and exclusion of the generic assessment row checked locally.',
        integration='Executive selects proposal groups; integrator authenticates return and field preimages, applies to the one current account, and reconciles source coordinates at its final freeze.',
        residuals=['11 existing positive consumer pairs lack reciprocal dependency entries and are preserved for source-owner reconciliation.',
                   'Material consumer completeness is not inferred from a nonempty list, a source link, a heading count or an absence search.',
                   'Specific source task-use witnesses outside the five workflow calls are evidence-only and do not add packaged semantic edges.',
                   'End-to-end acquisition-byte measurement is incomplete for early uninstrumented reconnaissance; no fabricated envelope-fit claim.'])
    write('RETURN.json',result)
    print(json.dumps(dict(population=389,role_counts=dict(role_counts),coverage_counts=dict(standing_counts),
                         inverse_rows=29,inverse_pairs=100,retained_positives=11,reciprocal_calls=5,
                         instrumented_new_source_bytes=novel,instrumented_repeats=total-novel),indent=2))


if __name__=='__main__':main()
