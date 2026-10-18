"""Bind carrier-only mechanics to their exact data, schema and method owners.

This authoring script creates qualification evidence, not a new method owner.
"""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
TENANT = Q.parents[2]
PACKAGE = TENANT / 'successor'
SOURCE = 'f2cb3e593757d094d008102551925e871a0204ff'
ACCOUNT_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
PREFIX = str(PACKAGE.relative_to(REPO))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frozen(path):
    return subprocess.check_output(['git', 'show', SOURCE + ':' + PREFIX + '/' + path], cwd=REPO)


def emit(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


account_data = subprocess.check_output(['git', 'show', 'fe4fcbe:' + str((Q / 'DETERMINATIONS.json').relative_to(REPO))], cwd=REPO)
assert sha(account_data) == ACCOUNT_SHA
account = json.loads(account_data)
ids = {r['id'] for r in account['determinations']}
outside = account['coverage']['outside_raw_standard_account']
bindings = []
classification = []
acquired = []

SHARED = ['FOUNDATIONS.identity-state-and-evidence', 'FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.result-algebra', 'TRANSFORMATION_LIBRARY.faithful-projection']
BASIS = ['SPEC_METHOD.stdo-product-definition-overlay-and-layout-independence', 'SPEC_METHOD.shared-installed-release-basis-and-toolchain-manager']
WORK = ['SPEC_METHOD.agentic-construction-execution-stdo-up-020', 'TICKET_METHOD.work-carrier-to-execution-rule', 'TICKET_METHOD.execution-contract-admission']


def add(path, family, applicability, predicate, obligations, latitude, dependencies, definition=None):
    data = frozen(path)
    identifier = 'CARRIER.' + path.replace('/', '.').replace(' ', '-')
    dependencies = sorted(set(SHARED + dependencies))
    assert all(d in ids for d in dependencies), (path, set(dependencies) - ids)
    bindings.append({
        'id': identifier,
        'owner': {'path': path, 'anchor': '', 'body_sha256': sha(data), 'unit_scope': 'whole_member'},
        'owner_body_sha256': sha(data), 'family': family,
        'representation_kind': 'consumer_binding' if definition is None else 'definition_data',
        'interpretation_standing': 'authored_semantic_binding',
        'applicability': applicability, 'predicate': predicate, 'definition': definition,
        'obligations': obligations, 'permissions_exceptions': latitude,
        'dependencies': dependencies,
        'dependency_relations': [{'id': d, 'kind': 'source_contract_binding', 'when': applicability} for d in dependencies],
        'result_mapping': {
            'kind': 'predicate_scoped_core_result',
            'predicate': predicate,
            'relation': 'Evaluate this predicate with the core result record. Authenticated violation falsifies it; a missing required observation leaves it indeterminate; unusable subject or basis is invalid_basis; missing evaluation capability or scope is out_of_frame. True applicability and every supported required condition permit satisfied for this predicate only. Configuration data, a schema-valid object, an installed basis and a produced artifact are not execution admission, semantic acceptance or release decisions.',
            'owner_refs': ['FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction'],
        },
        'argument': {
            'premises': [{'kind': 'adopted_foundation', 'id': 'FOUNDATIONS.foundational-commitments'}],
            'conditional_consequence': 'A chosen carrier preserves the source distinctions needed by its consumer: exact identity and current evidence, bounded acquisition, and separate authority for effects and decisions. Selecting this projection does not create its governing law or authorize an instance.',
            'policy_choices': [family + ' fixes a carrier or procedure under the named owners; neither its file layout nor its host syntax follows from finite capacity alone.'],
            'source_refs': dependencies,
        },
        'inputs': [{'kind': 'instance', 'description': 'The actual selected Product definition, exact basis, task, current source observations and any effect or decision grants required by the predicate.', 'required_when': applicability, 'standing': 'external_required'}],
    })
    acquired.append({'path': path, 'bytes': len(data), 'sha256': sha(data)})
    return identifier


for member in outside:
    path, kind = member['path'], member['kind']
    data = frozen(path)
    assert sha(data) == member['sha256'], path
    classification.append({'path': path, 'sha256': sha(data), 'bytes': len(data), 'kind': kind})
    if kind in ('source_bound_view', 'host_metadata', 'license', 'verification_evidence'):
        classification[-1]['relation'] = {
            'source_bound_view': 'Source-bound acquisition view. Its selecting and fidelity relationship is governed by Faithful projection, not another deciding law. Exact excerpts and semantic summary fidelity need separate evidence.',
            'host_metadata': 'Host discovery/configuration data. Trigger and display metadata do not confer a Product, work, installation or operation grant.',
            'license': 'Distribution license data carried unchanged; legal rights and obligations remain at this exact license, not a method result or work admission.',
            'verification_evidence': 'Source/check evidence. It cannot replace the source or independently confer semantic satisfaction, authority or acceptance.',
        }[kind]
        continue
    if kind == 'structural_validation_contract':
        schema = json.loads(data)
        classification[-1]['binding'] = add(path, 'JSON schema validation',
            'An instance is claimed to conform to this exact selected schema.',
            'The complete instance satisfies every applicable keyword of the exact schema under its declared JSON Schema dialect.',
            ['Interpret the complete schema, including local $ref, required fields, types, enums, patterns, cardinalities, additional properties and conditional composition. Do not flatten the schema into only its root required list.',
             'The schema is the executable predicate; retain its exact identity and bytes. Draft 2020-12 format annotations do not by themselves assert RFC 3986 URI validity.',
             'Semantic identity uniqueness, URI/fragment resolution, complete inventory, exact basis and authority remain separate owning-method evaluations; structural validation alone grants none.'],
            ['A conforming implementation of the declared schema dialect may execute this predicate. No specific validator product is required.'], BASIS,
            {'kind': 'executable_predicate', 'dialect': schema['$schema'], 'schema_id': schema['$id'], 'source': path, 'source_sha256': sha(data), 'evaluation': 'JSONSchema(instance, exact_schema, declared_dialect)', 'output_data': 'validation findings; core evaluation is scoped to structural conformity'})
    elif kind == 'host_basis_or_acquisition_contract':
        if path.endswith('PRODUCT_BASIS.md'):
            obligations = ['Determine the requested Product from Product-owned scope and identity; search only the authorized boundary. Directory, nearest file, filename, label and recency are discovery data, not selecting authority.',
                'Require exactly one applicable definition under its WHAT, HOW, work, context and explicit composition bindings. Zero is unresolved; multiple require Product disambiguation with all remaining identities.',
                'Run read-only status verification and require returned definition path/identity, immutable basis and manifest to match, installed=true, valid=true and no failures. Any mismatch stops before calling-skill effects.',
                'Return exact selected coordinates and verification. Do not sync, install, adopt, repair or fall back as part of selection.']
            latitude = ['The calling workflow may continue only under its own effect and authority boundary after successful selection.']
        elif path.endswith('REFRESH.md'):
            obligations = ['Require exactly one of installed, immutable release or candidate basis mode. Installed selects the verified applicable definition; release resolves the exact cut; candidate explicitly labels mutable source non-operative.',
                'Use the closed registry. Default to SPEC_METHOD only when neither doc nor list is given; list returns the registry and stops.',
                'Refuse unknown names or a registry member absent from the selected basis, including successor-only views on predecessor cuts; no fallback to another source.',
                'Surface the full selected member with name, exact basis, resolved source and end marker; retained context does not become a partial constitution.']
            latitude = ['Multiple explicit calls may form a multi-document context; routine workflows acquire only material sources. Bounded views are neither Project frame bases nor work grants.']
        else:
            obligations = ['Use one verified Product definition, exact installed basis and accepted frame basis before action; acquire only material Goal, Intent, Product, requirement/design, carrier and owning method inputs.',
                'Setup and installation require their own authority, exact published cohort coordinate, independently qualified toolchain minimum, and verified inventory. Sync installs the already selected cut; adoption is a separate accepted plan.',
                'Template setup preflights every source and target before effects, refuses duplicate or pre-existing targets, stages bytes, reserves destinations exclusively, and rolls back only paths owned by that invocation. Placeholder completion is not owner ratification.',
                'Bootstrap modifies only declared marker-owned regions. Host plugin success is not identity proof: verify installed member digests against the selected cohort and qualified host route.',
                'Classify at the first changed authority layer; bind current computed facts and material judgments; reuse supported judgments without repeating them solely for a new role.',
                'Select the smallest authorized carrier and admit the exact run contract before effect; preserve durable residuals at its result surface. Follow the owner for the explicit durability exception.',
                'Derive tests from requirements/design/closure law, with live external or installed proof only where the claim needs that boundary. Separate construction, required independent assessment, Product disposition, publication and adoption.',
                'Monitoring is read-only. Report actual baseline-relative movement, evidence, uncertainty, effect state and authorized next action; counts are not completion. Unknown effects need observation before dependent repetition.']
            latitude = ['The guide is a non-deciding interaction projection; raw owners govern an omitted case.', 'Actor count, internal decomposition and layout remain open when they do not alter governed meaning, authority, evidence, safety or release; a sufficient direct Writer path remains valid.']
        classification[-1]['binding'] = add(path, 'Basis and acquisition procedure', 'This exact procedure is selected for Product entry, setup or explicit refresh.', 'The selected procedure preserves exact basis, authority and acquisition conditions through its declared return.', obligations, latitude, BASIS + WORK)
    elif kind == 'conditional_host_workflow':
        name = path.split('/')[-2]
        if 'claude-skills/refresh/' in path:
            obligations = ['Invoke only manually; follow the complete REFRESH procedure. The adapter adds no procedure, source selection or authority.']
            latitude = ['Use another exact installed-member read route when the host lacks this adapter.']
        else:
            obligations = ['Select exactly one verified Product basis through PRODUCT_BASIS before this workflow; source and basis integrity are not work authority.',
                'Resolve exact current owners and applicable accepted frame configuration. Preserve missing, ambiguous, stale and out-of-frame conditions; no mutable fallback.']
            latitude = ['Use sufficient existing grants and applicable evidence; the skill name and an actor role grant nothing.']
            details = {
                'stdo-help': ['Remain read-only. Route ticket, work, review, status or full-member reload according to requested outcome. On failed basis selection provide only read-only setup/re-entry guidance.', 'Select material sources rather than bulk corpus; add no Executive, ticket or review just for help. Return exact scope/basis, current outcome, grant, proof boundary, unresolved matter and one next authorized action.'],
                'stdo-status': ['Remain read-only; read live authoritative carriers rather than historical links or summaries. Distinguish source commit, admission record and evidence checkpoint.', 'Use an actual comparison baseline or state that none exists; preserve uncertainty and report accepted movement separately from construction, churn, readiness and regressions.', 'Technical triage cannot assign Product priority or disposition. Report requested outcome, effect observation and owner retry law separately; no-effect refusal alone proves neither completion nor need to retry.'],
                'stdo-review': ['Bind an exact claim, frozen subject/basis, exclusions, evidence population, capability and required independence before independent source-first assessment.', 'Derive applicable evaluations from owners, not merely caller lists; retain unknown applicability and missing mandatory results. Search credible counterexamples and whole producer-to-consumer paths for material recurrence/composition.', 'Return the five core verdicts with exact scope and evidence. For satisfied or invalid_basis, technical triage is not_applicable; falsified carries findings and triage or field-level unknowns; indeterminate/out_of_frame retain unresolved triage/basis.', 'Separate technical severity from Product priority and disposition. Return a closed result and stop; review supplies no repair, next activation or closure authority.'],
                'stdo-ticket': ['Require explicit ticket-state authority. Durability is selected by surviving independent state beyond sprint/run or an explicit user request; a run contract alone does not mandate a ticket.', 'Use the exact owner change class, base type/category and field schema, Product-bound lanes and unique carrier; bind additional closure/admission fields when execution admission is intended.', 'Creation, active status and lane do not admit a contract. Report drafted unless exact independent admission or human override evidence exists.', 'Apply closure conditions and scoped repricing dispositions with original owner rulings preserved; no separate judgment registry, hidden scope change or automatic implementation.'],
                'stdo-work': ['Acquire the task-bound frame and current workspace; discard private context without resetting actual progress. Material symbolic use follows the current interpretation but structural validation is not permission.', 'Compute intake/classification from exact relevant public/authority/design facts; decide only residual meaning questions and keep failed candidates distinct from changes to governing outcome.', 'Choose the owner carrier and admitted contract with exact authority, result surface and evidence. Reuse sufficient existing authorization; do not self-admit or automatically create tickets.', 'Construct only in the causal cone and write territory. Direct Writer is allowed where sufficient; coordination and independence apply when required. Executive changes to a granted Writer before effects.', 'Use adequate focused proof, preserve failures and incomplete evidence, refresh affected bindings, and return at delegated boundary with exact candidate, proof, residuals and closed/withheld outcome. Publication and adoption remain separate.'],
            }
            obligations += details[name]
        classification[-1]['binding'] = add(path, 'Conditional host workflow', 'The user explicitly selects this STDO workflow or its stated governed-task trigger applies.', 'The workflow performs only its selected source-owned responsibility under its exact basis and effect boundary.', obligations, latitude, BASIS + WORK)
    elif kind == 'conditional_starter_or_convention':
        obligations = ['Bind placeholders to the exact selected basis, Product, source layout and authority before relying on an instantiated carrier. Copying this template creates no accepted law, work admission, operation or owner decision.']
        latitude = ['The owning Product may select another carrier/layout preserving the governing relations; displayed paths and sample values are not universal Product facts.']
        deps = BASIS
        if path.endswith(('AGENTS_TEMPLATE.md', 'CLAUDE_TEMPLATE.md')):
            obligations += ['Resolve the unique applicable definition and exact immutable basis, declared bootstrap entrypoint and accepted frame basis before constitutional work.', 'Bind outcome, grant and applicable dependent evaluations; preserve unknowns and independence. Direct Writer is lawful when sufficient; Executive does not mutate files or Git without a separate Writer activation.', 'Change only declared bootstrap markers under a bootstrap grant. Cache, prompt, summary and another method version do not replace current authority.']
            deps += WORK
        elif path.endswith('PRODUCT_DEFINITION_TEMPLATE.json') or path == 'standards/templates/README.md':
            obligations += ['One definition represents one WHAT; independent realizations are build tenants. Bind exact schema/basis/manifest, source/selector, additional authorities, bootstrap, local constitution, nonempty accepted frame bases, WHAT/HOW and work carriers.', 'Resolve references from the definition; no forced layout migration. Remove inapplicable illustrative disambiguation or bind every context/candidate/selection/authority/basis/scope and cross-context relation.', 'Validate full schema plus asserted URI formats, all references/fragments, identity uniqueness, exact installed constitutional inventory, composition contracts and semantic/authority sufficiency.', 'Sync only selected basis; adoption requires separate accepted exact plan digest. Fleet writes require all, and fleet adoption its aggregate plan; bootstrap is marker-confined.']
        elif path.endswith('PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md'):
            obligations += ['Bind actual declaration/authority, exact method and optional adopted profile, Product-role/composition map, every material evaluation/applicability and required result.', 'Bind frame subject, coordinates/invariants, evidence, capability, independence, semantic/evaluation/operation/decision authority, dependencies, consumer, current workspace and invalidation.', 'Use Product-defined triage scales and hard stops. Reviewer evidence and Executive priority/disposition are separate; a cutoff cannot waive a hard stop or promote an adjacent issue into a blocker.', 'Executive topology applies only when adopted. Use the sufficient direct Writer path when allowed; no tool/child return grants another activation. Material coverage is not available frame count.', 'Recheck material locks, preserve applicable previous support and original rulings, and close only on satisfied obligations, evidence, required judgments and absent non-closure conditions. Mutable-source recovery does not mutate immutable checkpoints.']
            deps += ['SPEC_METHOD.collective-reference-frame-basis'] + WORK
        elif '/adrs/' in path:
            obligations += ['Bind one design decision boundary and its affected requirements, motivating intent, status and supersession/retained-special-case relations. ADRs are accepted design memory, not new requirement truth.', 'Use cross-tenant common scope only for decisions governing multiple tenants; otherwise use the tenant-local scope. Reprice upstream truth through triage before a design change that needs it.', 'IDs are unique within the local ADR directory; numeric default or established namespace convention is lawful. Record active/superseded/retired standing accurately; superseded records retain successor and history unless explicitly retired.', 'State concrete chosen mechanisms, consequences, tradeoffs, proof/migration effects and rejected alternatives. Optional registry is only a read model.']
            deps += ['SPEC_METHOD.adr-conventions', 'SPEC_METHOD.adr-folder-convention']
        elif path.endswith('TENANT_REGISTRY_TEMPLATE.md'):
            obligations += ['Derive registry identities/locations from how.build_tenants; the companion is not a rival registry. Common shared law is not a tenant.', 'State active realization focus; keep WHAT singleton and tenant implementations many-valued. Lifecycle labels and family/variant nesting are suggestions, not adopted release facts.']
        elif path.endswith('variant/design/README_TEMPLATE.md'):
            obligations += ['State exact adopted common design/qualification or explicit none; bind requirements to computational operations, composition, effects/resources, real environment, conformance, failure assumptions and recovery.', 'Keep author identity separate from executor and operation kind. Put tenant-local ADRs locally and cross-tenant decisions in common; F_P customization remains tenant-local.']
        elif '/design/fp/' in path:
            obligations += ['F_P tuning retains tenant-local intent, governing requirement and design references, and bounded constructive-turn constraints.', 'For an edge override retain the exact template field roles: edge, customization_intent, requirement_refs, design_refs, guidance_append, suggested_output and required_sections. Sample values do not confer runtime authority.', 'One override file addresses one edge in the tenant override root; a runtime that adopts this convention loads only that root. No generic method runtime is imposed by this optional template.']
        elif '/requirements/' in path:
            obligations += ['Declare each requirement family, lifecycle status and category from the owning method, deterministic REQ heading and actual obligation/proof authority.', 'Replace the deferred starter with actual requirements; if temporarily retained it remains deferred, not active truth.']
        elif path.endswith('PRODUCT_TEMPLATE.md'):
            obligations += ['State current Product position, end state and terms with bounded-context identities, authority, basis and scope; labels are not global concept identities.', 'Isolate same-spelled concepts or bind their authorized import/translation/equivalence/disambiguation. Relate Goals, Intent, Product and decomposable requirements.']
        elif path.endswith('GOALS_TEMPLATE.md'):
            obligations += ['State current wave concerns and active goals in present tense. Goals orient work and remain distinct from requirements, Intent, Product and release labels.']
        elif path.endswith('INTENT_TEMPLATE.md'):
            obligations += ['State present-tense purpose, required outcomes and shaping constraints at Intent authority.']
        elif '/docs/' in path:
            obligations += ['Keep explanatory/operational/supporting documentation subordinate to the constitutional requirement surface.']
        elif '/common/' in path:
            obligations += ['Common realization/design applies across multiple tenants; promote tenant-specific material only explicitly. Cross-tenant ADR conventions and local numbering apply where adopted.']
        elif '/variant/' in path:
            obligations += ['Keep this one tenant realization, design, tooling, traces and implementation in its bound territory unless explicitly promoted to common.']
        else:
            raise ValueError('Uninterpreted template: ' + path)
        classification[-1]['binding'] = add(path, 'Conditional template instantiation', 'An owning Product selects and instantiates this template or convention.', 'The instantiation supplies the selected carrier data and preserves its governing scope, authority and source-owned conditions.', obligations, latitude, deps,
            {'kind': 'template', 'source': path, 'placeholder_values': 'illustrative data until the owning Product binds them', 'adoption': 'separate actual authority and evidence'})
    else:
        raise ValueError('Unclassified package member: ' + path)

assert len({b['id'] for b in bindings}) == len(bindings)
assert len(classification) == 64
emit('bindings.json', {'schema': 'stdo.semantic-contribution.v1', 'source_commit': SOURCE, 'input_account_sha256': ACCOUNT_SHA,
    'additional_source_members': acquired, 'bindings': bindings, 'package_member_classification': classification,
    'unresolved_construction_ids': [], 'limits': ['Authored carrier binding, not independent fidelity or installed use.', 'Views, license, metadata and evidence preserve their separately named source roles rather than acquiring another method predicate.']})
emit('CHECK.json', {'schema': 'stdo.carrier-contribution-check.v1', 'source_commit': SOURCE, 'classified_members': len(classification),
    'added_bindings': len(bindings), 'dependency_ids_resolve': True, 'all_source_pins_match': True,
    'classification_counts': {k: sum(r['kind'] == k for r in classification) for k in sorted({r['kind'] for r in classification})},
    'source_acquisition_bytes': sum(r['bytes'] for r in acquired), 'source_acquisition_boundary': 'unique complete carrier members read by this reproducible source binding; excludes parent prior source reads, reasoning and host context',
    'semantic_fidelity': 'independent assessment outstanding'})
print(json.dumps({'bindings': len(bindings), 'classified_members': len(classification), 'sha256': sha((HERE/'bindings.json').read_bytes())}))
