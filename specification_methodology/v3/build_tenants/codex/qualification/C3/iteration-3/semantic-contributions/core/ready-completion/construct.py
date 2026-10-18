#!/usr/bin/env python3
"""Reproduce this bounded authored contribution; all effects stay beside this file.

Semantic statements below are author constructions, not an independent oracle.
Frozen-source extraction and identity checks do not establish semantic fidelity.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / '.git').exists())
TENANT = 'specification_methodology/v3/build_tenants/codex/'
ACCOUNT_PATH = TENANT + 'qualification/C3/iteration-3/DETERMINATIONS.json'
OBSERVED = 'a6d5f00c484e4366e2efed35dc76c1b13ee5620a'
OBSERVED_SHA = '74b4140f328446ae60fd5a4a3ec17483264c1cef30086e391ebf8310e3d46044'
D1 = 'f2cb3e593757d094d008102551925e871a0204ff'
D2 = '6bcc4126efd54c41e412affc29e3801dc9deeb5b'
BASE_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
GRANT_COMMIT = 'ef2ab0a05379e3bf74482f62601580ca9d329a61'
COMMON = '355aa8655cca9c6ba6cf5c414f9bea3032ae89fd'
MANIFEST = '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
BUILD_STARTED = '2026-10-14T11:59:41.521667+00:00'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def frozen(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=REPO)

account_bytes = frozen(OBSERVED, ACCOUNT_PATH)
assert sha(account_bytes) == OBSERVED_SHA
account = json.loads(account_bytes)
by_id = {r['id']: r for r in account['determinations']}
selected = [r for r in account['determinations'] if r.get('unrepresented_scope')]
assert len(selected) == 25
selected_ids = {r['id'] for r in selected}
sources = {}

def source(r):
    path = r['owner']['path']
    if path not in sources:
        sources[path] = frozen(D2, TENANT + 'successor/' + path)
    return sources[path]

def body(r):
    o = r['owner']
    b = b''.join(source(r).splitlines(keepends=True)[o['start_line']-1:o['end_line']])
    assert sha(b) == o['body_sha256'], r['id']
    return b

for r in selected:
    body(r)
    assert source(r) == frozen(D1, TENANT + 'successor/' + r['owner']['path'])
    for c in r['source_clauses']:
        assert sha(source(r)[c['byte_start']:c['byte_end']]) == c['sha256']

BINDINGS = []
COMPARISONS = []

def inp(kind, description, when='when this contract is instantiated or its claim evaluated'):
    return {'kind': kind, 'description': description, 'required_when': when,
            'standing': 'external_required_at_instance_not_missing_source'}

def dep(id, binding, kind='contract_application', when='within the declared applicability'):
    assert id in by_id, id
    return {'id': id, 'kind': kind, 'binding': binding, 'required_when': when}

def add(id, scope, predicate, facts, inputs, deps, premises, consequence, policy,
        why, structures=None, definition_kind=None, result=None):
    assert id in selected_ids and id not in {x['id'] for x in BINDINGS}, id
    old = by_id[id]
    definition = None
    if definition_kind or any(f[1] == 'D' for f in facts):
        definition = {'kind': definition_kind or 'supporting_definitions',
                      'structures': structures or {}, 'clauses': []}
    if predicate is None:
        assert definition is not None, id
    argument = {
        'premises': [{'id': p, 'kind': 'foundational_premise',
                      'owner': 'FOUNDATIONS.foundational-commitments'} for p in premises],
        'conditional_consequence': consequence,
        'policy_choices': policy, 'source_refs': [id, 'FOUNDATIONS.foundational-commitments'],
        'clause_arguments': [],
        'standing': 'authored_conditional_argument_not_independent_entailment_proof'
    }
    mapping = {
        'kind': 'definition_with_embedded_constraints' if predicate is None else 'constraint_assessment',
        'contract_ref': 'core.shared_contracts.definition_data' if predicate is None else 'core.shared_contracts.core_evaluation',
        'evaluation_contract_ref': 'core.shared_contracts.core_evaluation',
        'owner_refs': ['FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction'],
        'conditions': ('The definition or argument is data, not a verdict. Evaluate only the separately named embedded application or preservation claims, retaining their predicates.' if predicate is None else 'Evaluate this exact predicate and its scoped required conditions; retain all qualified domain outcomes, actual evaluation performance, material effect observations, and absent coverage.'),
        'rules': [],
        'standing': 'author_semantic_mapping_not_independently_qualified'
    }
    if result:
        mapping.update(result)
    r = {
        'id': id, 'owner_body_sha256': old['owner']['body_sha256'],
        'source_member_sha256': sha(source(old)), 'owner': old['owner'],
        'representation_kind': 'definition_data' if predicate is None else 'consumer_binding',
        'interpretation_standing': 'bounded_semantic_binding',
        'applicability': scope, 'predicate': predicate, 'definition': definition,
        'obligations': [], 'permissions_exceptions': [],
        'dependencies': [], 'dependency_relations': [],
        'inputs': inputs, 'required_unknown_inputs': [],
        'result_mapping': mapping, 'argument': argument,
        'source_clause_ids': [id + '#' + c['id'] for c in old['source_clauses']],
        'source_clause_roles': [], 'unrepresented_scope': []
    }
    pointers = {c['id']: [] for c in old['source_clauses']}
    for n, role, statement in facts:
        clause = 'c' + str(n)
        assert clause in pointers, (id, clause)
        if role == 'D':
            target = r['definition']['clauses']; prefix = '/definition/clauses/'
        elif role == 'O':
            target = r['obligations']; prefix = '/obligations/'
        elif role == 'P':
            target = r['permissions_exceptions']; prefix = '/permissions_exceptions/'
        elif role == 'A':
            target = r['argument']['clause_arguments']; prefix = '/argument/clause_arguments/'
        elif role == 'R':
            target = r['result_mapping']['rules']; prefix = '/result_mapping/rules/'
        else:
            raise ValueError(role)
        pointers[clause].append({'role': role, 'pointer': prefix + str(len(target))})
        target.append(statement)
    for c in old['source_clauses']:
        assert pointers[c['id']], (id, c['id'])
        r['source_clause_roles'].append({
            'source_clause_id': id + '#' + c['id'], 'source_block_id': c['id'],
            'source_block_sha256': c['sha256'],
            'source_byte_start': c['byte_start'], 'source_byte_end': c['byte_end'],
            'source_roles': c['roles'], 'represented_at': pointers[c['id']],
            'standing': 'author_source_to_representation_mapping_not_fidelity_verdict'
        })
    for d in deps:
        if d['id'] not in r['dependencies']:
            r['dependencies'].append(d['id'])
        r['dependency_relations'].append(d)
    foundation = 'FOUNDATIONS.foundational-commitments'
    if foundation not in r['dependencies']:
        r['dependencies'].append(foundation)
        r['dependency_relations'].append(dep(foundation, 'F1-F6 retain their source-owned premise meanings; only the named subset is used by the conditional argument.', 'conditional_foundation_argument'))
    for scope_ref in old.get('scope_refs', []):
        if scope_ref not in r['dependencies']:
            r['dependencies'].append(scope_ref)
            r['dependency_relations'].append(dep(scope_ref, 'Enclosing source scope and authority conditions govern this row; proximity creates no adoption.', 'governing_scope'))
    BINDINGS.append(r)
    COMPARISONS.append({'id': id, 'owner_body_sha256': old['owner']['body_sha256'],
                        'preimage_row_sha256': sha(json.dumps(old, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()),
                        'preimage_unrepresented_scope': old['unrepresented_scope'],
                        'source_comparison_findings_and_repairs': why,
                        'remaining_material_source_omissions': []})

F = 'FOUNDATIONS.'
A = 'AXIOMATIC_CALCULUS.'
L = 'TRANSFORMATION_LIBRARY.'
R = 'REFERENCE_FRAME_METHOD.'
S = 'SPEC_METHOD.'
D = 'DESIGN_MODULE_METHOD.'
T = 'TICKET_METHOD.'
B = 'STDO_REFERENCE_FRAME_BASELINE.'

add(A+'ac-016-typed-composition',
    'Composition of the two exact a_c traversal contracts F_K2[w] compose F_K1[v].',
    'The exact traversal composition establishes its declared outer predicate through compatible typed intermediate results and all material required joins.', [
        (1,'O','Apply the shared Composition law to both exact traversal contracts.'),
        (2,'D',{'composition_expression': 'F_K2[w] compose F_K1[v]', 'first_traversal': 'v', 'dependent_traversal': 'w'}),
        (3,'O',"v's result type and judgment must satisfy w's domain and preconditions. Bind the outer predicate to required leaf predicates, intermediate results and material joins; retain both traversal identities, judgments, evidence, authority, provenance and stop states."),
        (3,'R','Use core conjunction or the declared operator selected by that outer predicate. The composite effect boundary includes all material traversal effects under the shared currentness law.'),
        (4,'P','No universal F_P -> F_D -> F_H sequence is required. Applications choose a lawful topology and outer operator while preserving the constituent predicates, distinct proposal/evaluation/human-decision contracts and AC-007 refinements.'),
        (4,'O','A categorical composition claim additionally satisfies the library demonstration conditions.')],
    [inp('traversal_pair','Exact v and w contracts, typed result and judgment of v, domain/preconditions of w, intermediate results, and required leaf/join predicates.'), inp('composition_evidence','Outer operator declaration, preservation argument, producer provenance, evidence and stop states for both traversals, actual grants, material effect parts and currentness support.')],
    [dep(L+'composition-law','Shared compatibility and composition admission, including categorical claims.'), dep(F+'result-conjunction','Outer predicate determines conjunction or declared-operator semantics.'), dep(F+'workspace-and-context','Currentness and uncertain effect reliance.'), dep(A+'ac-007-constraint-and-refusal','Preserve each original predicate and reason-sensitive outcome refinement.'), dep(A+'traversals-and-functor-kinds','Exact traversal coordinates and distinct kind contracts.', 'definition_dependency')],
    ['F2','F4','F5','F6'], 'Typed interpretation and conservation require intermediate compatibility and retained judgments, stops and authority before a composite claim can be supported.',
    ['Applications select their lawful topology and outer operator; the calculus does not derive a universal kind sequence or categorical law.'],
    ['Replaces unspecified applicability with the exact pair composition; adds result-type plus judgment compatibility, both identities/provenance/stops, effect currentness, AC-007 preservation and conditional categorical demonstration.'])

add(A+'ac-017-interpretation-fidelity',
    'An a_c interpretation of exact subject declarations under its selected signature/interpretation contract, and task projections that rely on M_subject.',
    "This interpretation preserves each required declaration's material meaning for its declared use under the interpretation contract and admitted loss.", [
        (1,'O','Apply Faithful projection: source is the exact subject declarations; target meaning is the selected signature and interpretation contract; consumer is the declared use of M_subject. Every admitted record has exact subject provenance or is explicitly model-local under competent authority. Every evaluated declaration receives retained, omitted, residual, inapplicable or refused treatment; omission and inapplicability retain their basis and authority.'),
        (2,'D',{'declaration_treatments': ['retained','omitted','residual','inapplicable','refused'], 'kind': 'declaration-treatment data, not verdicts'}),
        (2,'R',"Evaluate separately for each claimed treatment: 'this treatment preserves the declaration material meaning for the declared use under the interpretation contract'. Established preservation including authorized omission/admitted loss is satisfied; admissible fidelity counterexample is falsified; undecided preservation, authority or materiality is indeterminate; missing evaluation scope/capability is out_of_frame; unusable subject/interpretation basis is invalid_basis. Missing reason uses AC-007/core handling. Conjoin required declaration and dependency predicates. Faithful representation of source uncertainty can satisfy fidelity while source truth remains unresolved. Refused-treatment permission is a separate predicate."),
        (3,'D',{'populations': {'O':'subject objects and meanings','E':'typed dependency and preservation relations','C':'predicates and consequences','L':'permitted and forbidden variation','X':'unresolved conditions and consequences','V':'operations','T':'transformations','J':'judgments'}, 'qualifiers':'Signature-defined sorts, qualifiers and predicates distinguish premises, derived consequences, policy choices, observations and unresolved claims.'}),
        (3,'P','The interpretation adds no record family and imposes no fixed dependency-tree shape.'),
        (4,'O','A consuming task uses AC-011: select Z for its question and R for material dependency closure. M_Z and Boundary_Z instantiate the Constraint surface so obligations, permitted choices, required evidence and open conditions remain recoverable. Separately acquire the actual material subject and authoritative inputs under the applicable acquisition owner; only an activated frame consumer thereby uses Frame Method. Model facts retain source/currentness support and are neither world state nor an effect grant. Changed observations reopen affected reliance while unchanged independent support remains reusable.'),
        (5,'O','Fidelity evidence compares source and model on independently specified permissible, prohibited and unresolved decisions for the exact claimed scope. Retain latitude material to that use unless loss is admitted with basis and authority. Required-premise omission, unknown-as-permission and narrowing to a preferred implementation without admitted loss defeat fidelity despite valid structure. Bind evidence to exact source, interpretation, projection and approximation bounds.')],
    [inp('interpretation_binding','Exact declarations and provenance, selected signature and interpretation contract, declared use, each treatment and its reason/basis/authority, model-local content authority.'), inp('model_and_projection','O/E/C/L/X/V/T/J populations and signature distinctions; task Z, dependency relation R, M_Z and Boundary_Z, actual subject inputs and currentness support.'), inp('fidelity_evidence','Independently specified source decisions covering permissible/prohibited/unresolved material distinctions, comparison evidence and any authorized end-to-end approximation bound.')],
    [dep(L+'faithful-projection','Source-to-model relation and independent fidelity evidence.'), dep(L+'constraint-surface','Recoverable task obligations, latitude and unknowns.'), dep(A+'ac-011-projection','Exact task selector, material closure and Boundary_Z.'), dep(A+'ac-007-constraint-and-refusal','Treatment reason map, separate permission claims and missing causes.'), dep(F+'result-conjunction','Conjoin required declaration and dependency predicates.'), dep(F+'workspace-and-context','Model claim currentness, subject acquisition and supported reuse.'), dep(R+'position','Frame acquisition governs only an activated reference-frame consumer.', 'domain_specialization','a reference-frame consumer is activated')],
    ['F1','F2','F3','F4','F5','F6'], 'Purpose-bound interpreted claims must preserve material source distinctions and typed dependencies without converting representations or uncertainty into source truth or grants.',
    ['Calculus populations, treatment vocabulary and AC-011 selector structure are adopted calculus choices; source authority chooses admissible loss.'],
    ['Adds the exact source/target/consumer relation, five data treatments with predicate-sensitive verdict cases, all model population roles, task acquisition relation, reuse rule and independent decision-based fidelity falsifiers.'])

add(A+'traversals-and-functor-kinds',
    'Definition and use of a_c traversal contracts and the three functor-kind identities; categorical status applies only when separately claimed.', None, [
        (1,'A','F2/F6 separate evidence, proposals and authorized decisions; F4 requires typed preservation of constituent claims; F5 requires undecidable-work handling. These support exact traversal contracts and preserved stops/joins. Choosing exactly F_D/F_P/F_H and bracketed syntax is additional calculus policy; application topology/operator remain application-owned and no categorical law follows from the classification.'),
        (2,'D','A traversal is a typed contract, not a role name or unqualified operation.'),
        (3,'D',{'traversal_record_fields':['id','domain','codomain','context','owner','scope','basis','preconditions','postconditions','authority','evidence','provenance','stop_states']}),
        (4,'D','There are exactly three fundamental functor-kind identities in this calculus.'),
        (5,'D',{'F_D':'urn:stdo:concept:axiomatic-calculus:f-d','F_P':'urn:stdo:concept:axiomatic-calculus:f-p','F_H':'urn:stdo:concept:axiomatic-calculus:f-h'}),
        (6,'D','Application notation binds a kind and one exact traversal identity.'),
        (7,'D',{'application':'F_K[v](X_v) -> Y_v | Omega_v'}),
        (8,'D',{'F_K':'one declared kind','v':'one exact traversal identity','X_v':'typed input domain','Y_v':'typed result domain','Omega_v':'closed stop refinement'}),
        (8,'O','Map every Y_v or Omega_v outcome to one core verdict on an explicit predicate while preserving the original outcome. The declared domain handles graceful refusal, uncertainty and recovery or termination for undecidable observations; this total handling does not guarantee termination of an external actor or world.'),
        (9,'D',{'F_D':'Deterministic evaluation or proof over declared properties; returns judgment without doing the judged domain construction.','F_P':'Bounded probabilistic interpretation, construction or proposal under an exact traversal; utility/repeatability gives no semantic, admission, acceptance or closure authority.','F_H':'Explicit human adjudication under exact identity, grant, subject, basis and decision contract; human presence grants no ambient authority.'}),
        (10,'O','Distinguish actor, executor, domain operation and functor kind. Encode/Interpret/Serialize/Measure are not kind aliases. Traversals sharing a kind do not thereby share identity, meaning, inputs, outputs, grants or evidence.'),
        (11,'D','Functor Kind names this a_c classification, not a proved category-theoretic functor.'),
        (11,'O','A categorical functor claim declares source/target categories and proves identity and composition preservation.'),
        (12,'R','Availability of an exact candidate, its conformance and its acceptance are separate predicates with their own evidence. A completed human decision records the exact decision and does not make a rejected candidate conform.')],
    [inp('traversal_contract','All traversal-record coordinates and the chosen exact kind, typed input/result and complete stop outcomes.', 'when a traversal is applied'), inp('outcome_mapping','Declared predicates and reason-sensitive maps, admissible evidence, actual grants/performance/effects for each result or stop.', 'when a traversal returns or its outcome is relied on'), inp('categorical_demonstration','Source and target categories, object/arrow action and identity/composition preservation proofs.', 'only when a category-theoretic functor claim is made')],
    [dep(F+'result-algebra','Total predicate-bound outcomes with actual performance and effects.'), dep(L+'composition-law','Application-owned lawful topology and composition.'), dep(F+'orthogonal-descriptions','Conditional categorical proof obligations.'), dep(A+'ac-015-functor-classification','Application binds one kind and bracketed exact traversal identity.')],
    ['F2','F4','F5','F6'], 'Distinct evidence, proposals and decisions with typed joins and finite handling motivate exact traversal contracts; they do not uniquely derive the three chosen kinds.',
    ['Exactly three functor kinds and bracketed notation are calculus-owned choices. Application owners select lawful topology and operator.'],
    ['Restores a definition rather than a generic compliance predicate; supplies every traversal field, exact URNs and application sorts, total-stop obligations, kind-specific authority boundaries and separate categorical/conformance claims.'], definition_kind='typed_traversal_and_kind_definitions')

add(F+'bounded-construction',
    'Purposeful construction from the observed material state A toward a selected destination constraint set Z, including decomposition, control responses, progress, retry and closure claims.',
    'The bounded transition preserves the selected destination constraints, its material outer obligations and joins, and truthfully handles each admitted control state.', [
        (1,'D',{'A':'Current material state and what is justified about it.','Z':'Selected constraints and acceptance conditions, potentially satisfied by many states.','intermediate_states':'S0 -> S1 -> ...; Z remains the destination constraint set; name any satisfying endpoint separately.','transition_coordinates':['preconditions','permitted effects','result predicate','outer obligations']}),
        (1,'O','Intent, Product and Specification refine Z only under owning authority. Refine work into supported state transitions when one activation lacks sufficient context or attention.'),
        (2,'A','Finite capacity motivates bounded acquisition. Purpose choosing the outcome, identity of the work, compatibility and assurance for composition are additional premises, not consequences of a resource bound.'),
        (2,'O','Decomposition preserves every material outer obligation and join. Local success establishes the outer outcome only with required coverage and a preservation argument.'),
        (3,'O','A total control contract responds to every admitted state: unavailable input, unknown world conditions, failed preconditions, partial effects, exhausted capability and revoked/exhausted authority. Responses use the core algebra and the actual grant. Deterministic, probabilistic and human operations keep their selected outcome models; enclosing control reports the observation truthfully.'),
        (3,'P','Repair, re-entry, refusal, yield and termination may be available under the actual grant. Total control neither solves every problem nor guarantees external-process termination.'),
        (4,'D','Progress is supported movement toward the selected destination; discovery may enlarge the known frontier and counts are not a distance metric.'),
        (4,'O','Distinguish lawful stopping from completion. Completion requires current-candidate evidence and acceptance conditions. A changed Z requires its owner and does not prove the old destination reached. Repeating a failed relation needs a supported causal change; elapsed activity is not repair.')],
    [inp('work_state','Current material A with justification, selected Z/acceptance conditions and owning authority, named intermediate and endpoint states.'), inp('transition_contract','Preconditions, allowed effects, predicate, outer obligations, actor capability, material joins and preservation/coverage evidence.'), inp('control_observations','Admitted control domain, observed outcomes and effects, available response grants and authority/capability exhaustion facts.'), inp('progress_or_retry_evidence','Current-candidate completion/acceptance evidence, supported movement or expanded frontier and causal change to a previously failed relation.', 'when claiming progress/completion or repeating a failed relation')],
    [dep(F+'result-algebra','Truthful control and progress/stop results.'), dep(F+'workspace-and-context','Current A, supported evidence reuse and observed effects.'), dep(F+'typed-composition-and-conservation','Material joins and outer-contract preservation.'), dep(F+'purpose-and-interfaces','Selected outcome remains with its owner.')],
    ['F1','F3','F4','F5','F6'], 'Purpose, work identity and compatibility combine with finite capacity to require supported bounded transitions without losing outer obligations; completion needs its separate evidence.',
    ['The purpose owner selects Z and acceptance conditions; the operation grant selects responses and domain outcome models.'],
    ['Adds A/Z/intermediate-state definitions, extra premises beyond finite capacity, every admitted-control-state class, failed-relation causal-change condition and current-candidate completion boundary.'])

add(F+'configuration',
    'Allocation or reconfiguration of operations and information among capable actors and task frames, including any optimality claim about that arrangement.',
    'The selected configuration preserves material dependencies, outstanding obligations, observed and uncertain effects, admitted grants and required independence.', [
        (1,'D','A configuration allocates operations and information to capable actors and declares material dependencies between their frames.'),
        (1,'O','Assign effects only within grants the allocator holds and may delegate. Explain the allocation in the existing design/frame record against operations, dependencies, capabilities, assurance, resources and failure assumptions.'),
        (1,'A','Finite context and attention, fallibility, communication cost and required assurance constrain allocation but do not uniquely derive hierarchy or a role inventory.'),
        (1,'P','One actor, peers, hierarchy or supported adaptive allocation may be adequate.'),
        (2,'O','Producing, checking and accepting are different responsibilities even when one actor may do several. Required independent review retains authorship and evidence conditions; a new context alone is insufficient. Role names confer no grant. Keep functional decomposition, communication, authority and evaluation dependency distinct.'),
        (3,'P','The Executive arrangement is an optional profile for longer-term delivery through bounded worker results; its procedure and grants remain with that profile.'),
        (3,'O','Fixed and adaptive allocations and reconfigurations preserve dependencies, open obligations, known/uncertain effects, grants and independence. Claiming optimality additionally names objective, constraints, comparison scope and supporting evidence.')],
    [inp('allocation','Operations, information flows, actor capabilities, frame dependencies, resource/failure assumptions and design/frame rationale.'), inp('delegation_and_assurance','Allocator grant and delegability, operation grants, responsibility assignment, required independent authorship/evidence and observed/uncertain effects.'), inp('optimality_evidence','Explicit objective, constraints, comparison scope and evidence.', 'only when claiming optimality of an arrangement')],
    [dep(F+'bounded-construction','Bounded supported work and total-handling duties.'), dep(F+'judgment-and-authority','Separate responsibilities, actual authority and required independence.'), dep(B+'executive-attention-evaluation-and-action','Optional delivery configuration; neither adoption nor grants arise here.', 'domain_specialization','the consumer adopts and lawfully activates the Executive arrangement')],
    ['F4','F5','F6'], 'Material composition, finite resources and assurance constrain allocations and reconfigurations while preserving effects and grants; they do not choose a unique topology.',
    ['Tenant/operational design chooses topology and assurance mechanisms; optional Executive adoption and any optimization objective are separate choices.'],
    ['Adds allocator delegability, required existing-record rationale and failure assumptions, context-versus-independence distinction, optional-profile scope and explicit optimality inputs.'])

add(F+'orthogonal-descriptions',
    'Algorithmic, informational and computational accounts and any refinement, category, functor, equivalence or stronger mathematical claim about them.', None, [
        (1,'D',{'algorithmic':'Selected transformation.','informational':'Interpreted distinctions and their preservation.','computational':'Concrete execution environment: software/hardware, people/communication, or mixed, with material effects and resource costs.','relation':'Simultaneous accounts, not successive SDLC stages.'}),
        (2,'D',{'category_requirements':['domain','objects','typed arrows','arrow equality','identities','associative composition'],'functor_requirements':['action on objects','action on arrows','identity preservation','composition preservation'],'proposed_names':{'A':'algorithmic account','I':'interpreted informational account','C_H':'computational realization on declared architecture H'},'proposed_span':['A -> I','A -> C_H'],'distinct_claims':['Sigma_contract conformance','semantic equivalence','computational equivalence'],'categorical_equivalence_requirements':['stated domain','appropriate quasi-inverse','natural isomorphisms']}),
        (2,'O','A/I/C_H name categories only after the required objects/arrows/laws are supplied. Analogy or matching output is insufficient for categorical equivalence.'),
        (3,'O','Each refinement states and discharges its preservation relation. Exact rewriting preserves meaning; approximation supplies an adequacy relation and end-to-end bound because local tolerances alone do not compose. Use laws valid on the subject; without additional laws only universally valid steps are licensed. Represent method laws, records and maps in a_c with premises, consequences and choices distinct; calculus, interpretation and carriers retain separate identities.'),
        (3,'D',{'evidence_classes':['mechanically checked','mathematically argued','tested against an independently specified oracle','unresolved']}),
        (3,'O','Classify each claim by its actual evidence class; structural validation is no semantic proof. Claiming categorical construction capability requires a worked algorithm-to-computation join. An unproved categorical account remains a hypothesis.'),
        (4,'D',{'distinct_claims':['state sufficiency for one selected decision','statistical Markov properties','conditional independence','mathematical Markov category','runtime monad']}),
        (4,'P','No universal assertion or rejection of these stronger claims follows; supply each domain, laws and falsifiers before using it as proof.')],
    [inp('accounts','Selected transformation, informational distinctions, architecture H and computational realization, material resource/effect boundary.', 'when relating the three accounts'), inp('claimed_mathematical_structure','For the selected claim: its domain, objects/arrows/equality/identities/composition, functor action and preservation, or equivalence quasi-inverse/natural isomorphisms; each required proof and falsifier.', 'only for the corresponding category/functor/equivalence/Markov/independence/monad claim'), inp('refinement_evidence','Exact preservation or approximation adequacy relation and end-to-end bound, applicable laws, a_c premise/consequence/choice account and classified evidence.', 'when a refinement is claimed'), inp('worked_join','Worked algorithm-to-computation join.', 'when claiming the method categorical construction capability')],
    [dep(F+'foundational-commitments','Purpose, interpretation, composition and evidence premises.', 'conditional_foundation_argument')],
    ['F1','F2','F4','F6'], 'Distinct interpretations and realization claims require explicit preservation and appropriate evidence; similar outcomes or structure do not establish their equivalence.',
    ['The claim owner selects domain, equality, architecture, approximation and adequacy; the method chooses the three accounts and declared evidence distinctions.'],
    ['Replaces a broad predicate with account/category/evidence definitions; adds functor and equivalence laws, whole-path approximation, universal-law restriction, worked join and conditional stronger-claim proof inputs.'], definition_kind='orthogonal_accounts_and_proof_requirements')

add(F+'result-algebra',
    'Definition, construction, projection and reliance on a result about one named predicate on an exact subject/basis, including domain refinements, stops, performance and material effects.', None, [
        (1,'D',{'result_fields':['predicate','exact subject','exact basis','verdict','performance','original qualified domain outcome','supporting evidence and citations','unresolved obligations','material effect observations'],'carrier':'Semantic coordinates, not a mandatory serialization or additional work carrier; references may carry them if meaning and availability survive.'}),
        (2,'D','The core verdict set has exactly five values.'),
        (3,'D',{'verdict_meanings':{'satisfied':'Admissible evidence establishes the predicate under its declared rule.','falsified':'Admissible evidence establishes a counterexample or failure of that predicate.','indeterminate':'Available admissible evidence does not decide the predicate.','out_of_frame':'Predicate is outside bound evaluation scope/capability; retain the wider obligation.','invalid_basis':'Subject, governing basis or required interpretation is invalid for this claimed evaluation.'}}),
        (4,'D','Performance concerns whether the named evaluation was actually undertaken, separately from dispatch/admission or work being assessed. Retain its observed extent, interruption and conclusion.'),
        (5,'D',{'legal_performance_verdict_pairs':{'performed':['satisfied','falsified','indeterminate','out_of_frame','invalid_basis'],'not_performed':['falsified','indeterminate','out_of_frame','invalid_basis'],'unconfirmed':['falsified','indeterminate','out_of_frame','invalid_basis']},'meaning':{'performed':'Evidence establishes evaluation undertaken, including a scoped basis/capability diagnosis; extent and conclusion remain separate.','not_performed':'Evidence establishes evaluation not undertaken; dispatch/admission is insufficient.','unconfirmed':'Whether evaluation was undertaken is not established.'}}),
        (6,'O','Interruption preserves undertaking and admissible evidence. A suite aborted after witnessed failure is performed at that extent and falsifies all-tests-pass. A completed load test unable to generate required load is performed but indeterminate on requested service performance. Neither is never-run. Satisfaction still requires all evidence and completion conditions in the predicate rule; performed is insufficient.'),
        (7,'R','For not_performed or unconfirmed evaluation, separately admissible counterevidence can establish falsified, and established basis/scope diagnosis can establish invalid_basis/out_of_frame, on the same predicate with independent support identified and without inventing execution. Otherwise use indeterminate. Absent return proves neither non-performance nor undecidable evaluation; retain the absent slot and known facts.'),
        (8,'O','A missing required judgment stays an absent coverage slot with known performance or uncertainty, never a fabricated child. Distinguish performed-undecidable, known-unperformed and unconfirmed. Plans select required predicates; preconditions support the dependent evaluation unless separately required as predicates. Concluding diagnosis on P returns invalid_basis/out_of_frame on P, not a substituted admission predicate. Admission may conclude while work does not; an abort preserves authenticated counterexamples. Projections retain original predicate and all these coordinates; verdict-only handoff is insufficient where performance matters.'),
        (9,'D',{'effect_values':['not_requested','not_started','completed','partial','reverted','unknown'],'boundary':'Every materially possibly affected part under the supported operating model and any observed departure, including requested, unintended and irreversible external effects.','not_started':'Evidence no requested selected effect began, including authenticated pre-mutation rejection.','not_requested':'Established effect-free scope; an unrequested possible part observed not to begin contributes here with that observation and prior uncertainty. Absence of a request alone is insufficient.','reverted':'At least one part began and every begun part is observed reversed; retain reversal and any unstarted remainder.','partial':'Observed completed part plus observed requested but unexecuted or reverted remainder.','unknown':'Insufficient completion observation on any material remainder, including lost acknowledgment after possible execution; retain completed parts as evidence.','completed':'Observed completion at the declared boundary; does not establish intended Product outcome.'}),
        (9,'O','Transport dispatch, empty local log and discarded context prove neither effect absence nor completion. Never omit irreversible or unintended parts to improve classification. A requested part observed not to begin remains not_started; an unrequested possible part observed not to begin is not an uncompleted requested remainder.'),
        (10,'D',{'refined_value':['original qualified domain outcome','cause in declared reason domain including explicit missing-reason case'],'mapping':'Total and reason-sensitive into the core record; domain meaning remains domain-owned.'}),
        (10,'R','A coarse outcome such as refused/ready/accepted needs its required cause; never guess from its label. Missing cause gives indeterminate and inadmissible deciding support for that slot, retaining raw outcome and unresolved authentication. Independently admissible counterevidence or basis/scope diagnosis can decide the same predicate under legal performance pairs; do not invent execution/completion. Unconfirmed stays unconfirmed and insufficiently observed requested or possibly unintended effects stay unknown. No refinement upgrades failure, undecidability, non-performance or unknown effects; a new predicate result does not overwrite the earlier result.'),
        (11,'R',{'separate_predicates':['candidate availability','candidate fitness','authorized acceptance','lawful yielding','Product completion'],'decision_predicate':'Disposition D on subject S at basis B was made under mandate M by its bound authority.','examples':'candidate_ready may satisfy availability while fitness is false/unassessed; lawful yield can satisfy its own contract while completion is unresolved; lawful rejection may satisfy decision law while fitness is undecided.','applicability':'Not-applicable requires supported applicability judgment; never stands for missing evaluation.','authority':'Recording a decision does not confer it.'}),
        (12,'R','A stop reports the actual destination/task predicate, reason, observed effects and outstanding obligations. Use indeterminate if undecided, falsified on admissible defeat, or the established scope/basis diagnosis. Lawfulness of stopping is a separately evaluated decision predicate.')],
    [inp('result_subject','Exact named predicate, subject, basis, governing evaluation rule and completion conditions.', 'when producing or relying on a result'), inp('evaluation_evidence','Whether the named evaluation ran, observed extent/interruption/conclusion, independently admissible counterevidence/diagnoses, producer and citations, planned/absent coverage.', 'when producing or relying on a result'), inp('domain_refinement','Original qualified domain outcome plus declared cause or explicit missing reason, total map and authentication support.', 'when a domain outcome is refined'), inp('effect_observations','Supported operating model, actual boundary and every requested/possible unintended material part, observations of start/completion/reversal and any insufficiently observed remainder.', 'when effects are material'), inp('decision_or_applicability','Exact mandate/bound decision authority for a decision predicate, or evidence for a not-applicable classification.', 'when those separate claims are made')],
    [dep(F+'foundational-commitments','Interpretation, evidence/authority and truthful finite handling support distinct result coordinates.', 'conditional_foundation_argument')],
    ['F1','F2','F5','F6'], 'Purpose-bound evidence requires one exact predicate while finite handling and authority separation retain undecidability, non-performance and effects rather than promoting them.',
    ['The five verdicts, three performance states, legal pairs, six effect values and reason-sensitive mapping law are explicit choices of this owner.'],
    ['Restores the core semantic record as structured definition, all five verdicts and legal performance pairs, missing-slot/admission distinctions, complete effect boundary and edge cases, total cause mapping, separate decision/availability/stop predicates.'], definition_kind='core_result_record_and_refinement_algebra')

add(F+'result-conjunction',
    'Aggregation of results for exact required leaf predicates and material joins on a declared composite subject/basis; declared alternative operators and lawful regroupings have their stated additional conditions.', None, [
        (1,'D','Conjunction evaluates all required predicates and their material joins on the composite subject/basis. The aggregate is another core result; retain contributors, authentication, predicate mapping, cited failures, uncovered obligations, uncertain effects and invalidators through sufficient references. A summary does not replace them.'),
        (2,'R','Applying the combining rule makes aggregate evaluation performed without altering component performance. Declare composite effect boundary/parts; resolve each current part observation with contributing identities/order and supported supersession. A later timestamp alone is insufficient. Conflicting/insufficient observations are unknown. Normalize every possibly affected material part, including parts owned by absent evaluations, under Result algebra; requested-unstarted and unrequested-observed-not-begun remain distinct.'),
        (3,'O','Map sequential observations about the same part to its current state at the composite boundary before joining labels. Deployment then complete rollback gives reverted; subsequent complete reapplication gives completed while retaining rollback history. Preserve all external irreversible parts; local reversal cannot remove them.'),
        (4,'D',{'effect_join_order_over_normalized_disjoint_parts':[
            {'when':'any part unknown','result':'unknown'},
            {'when':'all parts not_requested','result':'not_requested'},
            {'when':'at least one completed, all others completed or not_requested','result':'completed'},
            {'when':'at least one not_started, all others not_started or not_requested','result':'not_started'},
            {'when':'at least one reverted, all others reverted/not_started/not_requested','result':'reverted'},
            {'when':'every remaining fully observed mixture','result':'partial'}],
            'retention':'Keep each part and component contribution; a nonmutating combiner cannot label an effectful composite not_requested.'}),
        (5,'O','Authenticate contributions against producer, exact subject/basis and required plan membership. Unauthenticated claims discharge no obligation. Distinguish a missing planned judgment with known/unknown performance from uncovered required coverage outside an authenticated plan. Invalid contributions cannot erase independently authenticated findings.'),
        (6,'D','The following conjunction verdict ordering assumes an interpretable composite predicate and governing basis.'),
        (7,'D',{'conjunction_verdict_order':[
            {'when':'authenticated applicable falsification of required leaf or material join','result':'falsified','retain':'other missing/undecidable coverage'},
            {'when':'no such falsification and invalid required basis','result':'invalid_basis'},
            {'when':'no such falsification/invalid basis and required out_of_frame','result':'out_of_frame'},
            {'when':'otherwise unresolved applicability, missing evaluation, undecidable predicate or material join','result':'indeterminate'},
            {'when':'all applicable obligations/joins authentically satisfied and coverage established','result':'satisfied'}],
            'empty_case':'An empty list supplies no satisfaction unless the declared required set is established empty.'}),
        (8,'O','Declare each relation as admission condition or material predicate join in this evaluation. Admission failure prevents interpretation; false required join is counterevidence in an admitted interpretation and cannot be relabeled missing basis. Uninterpretable composite subject/basis yields invalid_basis while exposing independently valid component failures. Unknown effects prevent satisfaction only where known effect state is material to that predicate; relevance requires a dependency relation.'),
        (9,'D',{'declared_operator':'Truth and falsity conditions over exact leaf predicates/joins must be disjoint and exhaustive on the fully decided admitted domain, including failure of required joins.','malformed':'Overlapping, incomplete or uninterpretable declaration is invalid_basis.','unresolved_wellformedness':'indeterminate, deciding neither truth nor falsity; valid leaves stay visible.','admitted_operator_order':'Once well-formed: authenticated established truth with its material joins/coverage gives satisfied; established falsity gives falsified; otherwise material invalid_basis then material out_of_frame then remaining uncertainty gives indeterminate. Only dependencies needed to decide that predicate enter the ordering.','retained_rules':'Authentication, original failures, performance and normalized effect composition use the same core law.'}),
        (9,'O','Negation/disjunction concern a different predicate and cannot erase failed leaves or masquerade as all-leaf conjunction. First-nonfailure cannot promote an undecided fallback to success.'),
        (10,'O','Sequential unreturned dependent evaluations remain absent slots with actual performance/extent and missing conclusion. Lawful regrouping holds fixed interpretable composite basis, required leaves/joins, normalized effect parts and authentication, hiding no intermediate basis failure. On that domain component sets union, conjunction precedence and normalized-disjoint-part effect join are associative. An arbitrary operator needs its own proved associativity and same outer predicate. Invalid intermediate join defeats that rewrite; reordering additionally needs effect independence.'),
        (11,'R','Sequential operations retain their design UP-016/017 or calculus AC-016 owning contracts. Apply the selected operator to the outer predicate with preservation argument and component results. All-stage-postcondition pipelines use conjunction; a recovery path need not make a failed earlier test true. Unexecuted stages remain coverage facts. Missing outer interpretation/join gives the applicable unresolved/invalid-basis result, not guessed success.')],
    [inp('composite_declaration','Exact composite subject/basis, required leaf predicate set, material joins versus admission conditions, selected conjunction/alternative operator and coverage plan.', 'when an aggregate is evaluated'), inp('authenticated_components','Producer/subject/basis/plan-membership evidence, original outcomes and predicates, actual performance/extent, failures/citations, absent slots and uncovered/unresolved obligations.', 'when an aggregate is evaluated'), inp('normalized_effect_parts','Complete material part boundary, current per-part observations, identities/order/supported supersession and evidence of any overlap normalization.', 'when effects are material to an aggregate'), inp('rewrite_proof','Fixed-domain preservation and any operator associativity or effect-independence proof.', 'only when regrouping, reordering or claiming concurrent equivalence')],
    [dep(F+'result-algebra','Core result/performance and per-part effect normalization; no second effect classifier.'), dep(D+'transformation-admission-completeness-stdo-up-016','Design sequential contracts remain design-owned.', 'domain_specialization','design composition is selected'), dep(D+'bounded-frame-conservation-stdo-up-017','Design material outer relation preservation.', 'domain_specialization','design composition is selected'), dep(A+'ac-016-typed-composition','Exact calculus traversal join.', 'domain_specialization','a_c traversal composition is selected')],
    ['F2','F3','F4','F6'], 'Interpreted authenticated components and typed outer conservation require failure/coverage/effect retention; the stated precedence and associative domains are explicit owner laws.',
    ['The owner selects conjunction precedence, normalized effect join and declared-operator admission. Domain owners select outer predicates and additional composition policies.'],
    ['Adds exact effect normalization and complete join algorithm, plan/outside-plan missingness, precedence, admission-versus-join roles, alternative-operator truth/falsity admission and fixed-domain associativity/reordering limits.'], definition_kind='core_conjunction_and_declared_operator_contract')

add(F+'workspace-and-context',
    'Acquisition, continuation and reuse against a bound workspace/subject and authoritative external state, including currentness-sensitive effects and dependent retries.',
    'This reliance or next authorized operation has sufficient support on its bound subject/basis, applicable reusable evidence and sufficiently observed material effects.', [
        (1,'D',{'workspace':'Continuing material construction state including authoritative requirements, work products and durable records.','external_state':'Observed through the owning interface.','actor_context':'Fallible disposable bounded account acquired from those sources.'}),
        (1,'O','Observe the subject/basis actually bound, including selected frozen snapshots. Admissible contrary current evidence reopens affected claims through drift/re-entry and does not silently change the selected basis. Current observations correct stale belief but cannot authorize weakening requirements to match implementation; what exists and what must exist remain distinct.'),
        (2,'O','Bind task, subject, destination, authority and relevant observations. Include known material dependencies directly or through declared available inputs; exclude irrelevant material unless needed to establish irrelevance. Rules without the actual subject, digests without accessible meaning and stale unsupported summaries are insufficient. Absence from a partial projection/sparse checkout/empty local record does not prove bound-subject absence: obtain authoritative evidence or retain indeterminacy.'),
        (3,'O','Each observation identifies source and time/version. If state may change before effect, supply material freshness/concurrency support through re-observation, revision comparison, protected snapshot or uncertainty. Never assume a stale read remains current.'),
        (3,'P','No universal isolation scheme is prescribed.'),
        (4,'D',{'cycle':['acquire from current state','bounded authorized operation','observe result','acquire for next operation'],'result_owner':'FOUNDATIONS.result-algebra'}),
        (4,'P','The cycle may stop after any operation without completion. Context may be discarded; resume by reconstructing sufficient context from continuing work and authoritative inputs, preserving progress without needing every previous transcript.'),
        (5,'O','Reuse requires same claim scope, adequate current basis/evidence, valid dependencies and required independent authorship. Changed support reopens affected dependent claims and invalidates their reliance while preserving history. Unchanged independent work remains usable; inspect the wider affected scope when independence is unproved. A stored green label is insufficient; the continuing consumer checks exact applicability.'),
        (5,'P','A role, conversation or resumption change alone is not an invalidator.'),
        (6,'O','Before dependent repetition with uncertain effects, observe/reconcile sufficiently to decide the next action. Otherwise choose another permitted action or return unresolved. Retained partial progress does not imply idempotence.'),
        (6,'P','Retry a granted operation when idempotence is established for this actual subject and effect. Event logs may support observation, audit or domain reconstruction; they are neither universally the work state nor a mandatory recovery algorithm.')],
    [inp('current_subject','Selected task, subject/basis including frozen selection, destination and authority; material workspace/external-state sources through owning interfaces.'), inp('observations_and_dependencies','Source/time/version, actual subject observations, accessible material dependency inputs, supported irrelevance and any contrary evidence.'), inp('currentness_and_reuse','Applicable freshness/concurrency conditions, prior claim scope/evidence/basis/dependencies/required independence and changed-support impact.'), inp('uncertain_effects','Material effect observations/reconciliation and actual retry grant plus subject/effect-specific idempotence proof, or alternative permitted response.', 'before action depending on an uncertain prior effect')],
    [dep(F+'result-algebra','Truthful cycle, performance and effect results.'), dep(F+'judgment-and-authority','Required independent authorship and grants survive reuse.')],
    ['F2','F3','F5','F6'], 'A fallible finite context cannot replace continuing identity/state and authoritative support; currentness and observations determine safe reliance under actual grants.',
    ['Domain owners choose sufficient observation, freshness/concurrency and any stronger replay requirements; no universal isolation or transcript is required.'],
    ['Adds selected-frozen-basis conservation, sparse/projection absence limits, complete observation coordinates, concurrency alternatives, reuse invalidation scope and bounded idempotence/event-log permissions.'])

add(R+'rf-012-closed-results',
    'Frame evaluation results, activation-admission attempts and separately planned downstream work under Reference Frame Method.',
    'This frame evaluation returns the core result on its exact frame, activation, subject, basis and declared predicate without conflating admission, work or missing execution.', [
        (1,'O','Return the single core result bound to exact frame, activation, subject, basis and predicate. Preserve each frame-specific original outcome with one explicit predicate-bound core mapping. Missing reason, unmapped outcome or absent mapping support uses the core missing-reason rule; the label alone decides nothing.'),
        (2,'R',{'activation_predicate':'This frame may be activated for this actor, subject and basis.','admission_cases':{'established_failed_condition':'falsified','unresolved_admissibility':'indeterminate'},'checked_conditions':['capability','authority','basis','topology'],'distinction':'These are conditions under test, not the admission evaluator own capability/basis. Established ambiguity preventing admission falsifies admission; uncertain existence of that ambiguity is indeterminate. Only lack of scope/usable basis in the admission check itself uses core diagnosis; missing causes use core missing-reason handling.'}),
        (3,'R','If the plan requires downstream work, a separately established capability/basis diagnosis may report out_of_frame/invalid_basis on that work predicate with actual performance. Otherwise its planned slot remains absent with observed performance; invent no Worker return. Admission prohibition alone does not falsify downstream fitness. Successful activation satisfies admission only; downstream work is not_performed until undertaken. Preserve performance and known effects for each actual result.'),
        (4,'O','Unconfirmed execution retains core unconfirmed performance; an absent return cannot establish that the invoked operation did not run.'),
        (5,'O','A domain refinement may add detail but cannot erase failure, unknown, refusal, non-performance or uncertain effects, or promote availability to fitness, acceptance or authority.')],
    [inp('frame_evaluation','Exact frame/activation/subject/basis/predicate and original outcome with supported cause and explicit mapping.'), inp('admission_attempt','Actor, subject/basis, capability/authority/topology conditions, admission evidence, and separately the admission check own scope/basis.'), inp('downstream_plan','Which downstream predicates are required, actual performance/extent, missing return slots, separately established diagnoses/counterevidence and material effects.', 'when admission relates to planned downstream work')],
    [dep(F+'result-algebra','Single verdict, cause, performance, absent-slot and effect contract.'), dep(F+'result-conjunction','Required result composition.'), dep(R+'rf-005-exact-basis-and-coordinates','Frame result coordinates remain exact.')],
    ['F2','F5','F6'], 'Interpretation and truthful handling distinguish the evaluated admission proposition from downstream work and preserve unknown execution without manufacturing authority or fitness.',
    ['Frame Method binds exact frame/activation coordinates and its admission predicate; each domain owns its explicit refinement.'],
    ['Adds the admission-specific reason map, condition-under-test versus evaluator-diagnosis distinction, planned downstream absent-slot handling and non-performance/unconfirmed rules.'])

add(R+'operational-full-coverage',
    'Operational coverage claims about a declared frame set for the exact Coverage(W,G,B,E,S,T) tuple.',
    'The declared frame set has operational full coverage for Coverage(W,G,B,E,S,T) under the eight source criteria.', [
        (1,'D',{'claim':'Operational full coverage is a property of one declared tuple.','tuple_ref':'REFERENCE_FRAME_METHOD.coverage-basis'}),
        (2,'O',{'required_criteria':[
            'Every known material evaluation has at least one capable frame.',
            'Every material interaction has a declared evaluation, conjunction, translation or composition relation.',
            'Every evaluation has semantic and decision authority; every material operation has its inherited operation authority.',
            'Every mandatory claim has an admissible evidence and refusal path.',
            'Required independently activated overlaps and assurance-independence conditions are present.',
            'Aggregation hides no unresolved frame-result conflict.',
            'Excluded evaluations cite governing authority.',
            'Uncovered/unknown residuals are explicit and compatible with the claim.']}),
        (3,'R','Evaluate each applicable criterion and required seam through RF-012 and core conjunction. Satisfied requires supported satisfaction of all required criteria. Demonstrated uncovered mandatory evaluation, unlawful exclusion or another defeated criterion is falsified. Undecided required truth, applicability, conflict or residual compatibility is indeterminate unless core precedence retains established failure or diagnosis. Unusable evaluation basis is invalid_basis; material scope/capability outside the coverage evaluator is out_of_frame. Missing causes/unsupported state labels use core missing-reason handling. Retain ledger, leaves, actual performance and effects: a successful audit can falsify coverage; an absent audit stays absent.'),
        (4,'P','Coverage is relative to the declared tuple and does not claim that no undiscovered evaluation exists.')],
    [inp('coverage_tuple','W workspace; G governed outcome; B exact basis; E known evaluation inventory; S declared frame set; T time/immutable checkpoint.'), inp('coverage_ledger','Each evaluation predicate/materiality source, subject/basis, capable frames and actor envelope, semantic/operation/decision authority, evidence/refusal path, material seams, supported states and residuals.'), inp('coverage_evaluations','Criterion/seam results with reasons, actual performance/effects, independent overlap/assurance evidence, conflict treatment, authoritative exclusions and residual-compatibility evidence.')],
    [dep(R+'coverage-basis','Exact tuple definition and material-change invalidation.', 'definition_dependency'), dep(R+'coverage-ledger','Coverage states are input data, not core verdicts.', 'definition_dependency'), dep(R+'workspace-coverage','Known-evaluation boundary and owner-selected inventory/independence.', 'governing_scope'), dep(R+'rf-012-closed-results','Bind criteria/seam evaluations and real missing slots.'), dep(F+'result-conjunction','Conjoin required criteria and material seams with retained failures.')],
    ['F1','F2','F3','F4','F5','F6'], 'Purpose, exact current evidence, material interaction and owned authority require supported coverage with residual boundaries; a finite inventory proves no universal absence of unknown work.',
    ['Frame Method selects eight criteria and ledger vocabulary; human frame-set authority selects inventory and required independence under the outcome.'],
    ['Replaces vague coverage summary with all eight exact criteria, tuple components, genuine ledger/criterion inputs and predicate-specific results preserving absent audit and audit-finding distinction.'])

add(L+'contract-application',
    'A responsible consumer deciding admissibility of a proposed operation or reliance under an explicitly bound contract in the library purposeful construction domain.',
    'This proposed operation or reliance is admissible under this bound contract.', [
        (1,'D',{'contract_coordinates':['input domain','output domain','intended predicate','governing constraints','material relations','evidence rule','actual grants','coordinate owners','current basis'],'carrier':'Semantic coordinates may come from an existing design, frame, function or work carrier; no additional carrier or validation stage.'}),
        (2,'D','Contract admissibility differs from whether the operation achieves its intended outcome. Apply the following conditions once at the responsible consumer.'),
        (3,'O',{'conditions':{
            'Binding':'Identify actual subject/intended predicate, governing interpretation, applicable policy and source/current-state coordinates; names/equal bytes alone confer neither identity, standing nor applicability.',
            'Support':'Account for conditions and material dependencies that can change the determination. Inspect affected seams until governing obligations are covered or far-side independence is evidenced. Task boundaries, partial listings and no observed failure do not prove independence. Domain-owned completeness/sufficiency may not be silently narrowed.',
            'Preservation':'Establish input/output/cross-boundary relations under declared compatibility or translation, retaining material identity, meaning, lifecycle, producer/evidence coordinates, constraints, authority and effects. Lawful differences require the admitted instance relation; neither universal field equality nor invented translation decides compatibility.',
            'Authority':'Establish actual operation/decision grant for selected effect. Keep owners of meaning, evidence, operation and disposition distinct; code, source reference or satisfied judgment supplies no grant. Preserve required independence.',
            'Currentness':'Apply Workspace/context to evidence reuse, observation, concurrency and uncertain effects. Supported changed dependency reopens affected determination; unsupported currentness remains unresolved. Supported unchanged premises permit reuse without rechecking fixed graphs/every unchanged relation on every event.',
            'Result':'Apply core result/conjunction to actual predicates; retain failures, absent coverage, basis/scope diagnoses, original outcomes, performance and effects. Unknown applicability is not non-applicability; other uncertainty cannot erase supported failure.'}}),
        (4,'O','Each consumer binds these conditions to its own decision and domain exceptions using existing dependency/authority evidence; do not create a second generic-rule owner. Exceptions must be named in owning policy; application cannot invent one.'),
        (4,'P','One library helper may implement several consumers, retaining their separate subjects, evidence and powers.'),
        (5,'R','These are admissibility conditions, not a universal predicate decision algorithm. Insufficient support yields applicable core uncertainty/scope/basis result and known violations retain evidence. Supported admissibility permits only the already-granted operation and predicts neither success nor termination; the control contract handles the actual outcome separately.')],
    [inp('bound_contract','Actual subject, input/output domains, intended predicate, interpretation, governing policy/constraints, current-state/source identity, owners and evidence rule.'), inp('material_support','Complete domain-selected dependency/seam set, far-side coverage or independence, compatibility/translation and material identity/lifecycle/evidence/effect preservation evidence.'), inp('grants_and_currentness','Actual operation/decision mandates, required independent assessment, observation/concurrency/reuse validity and unknown-effect support.'), inp('consumer_conditions','Named domain exceptions, admitted differences and exact result predicates with supporting/missing/defeating evidence.')],
    [dep(F+'workspace-and-context','Owns currentness/reuse/observation/uncertain effects.'), dep(F+'result-algebra','Actual predicate result and no authority promotion.'), dep(F+'result-conjunction','Required condition/coverage/failed-join composition.'), dep(L+'foundational-contract','Parameter meanings and conditional F1-F6 source-to-contract argument.', 'definition_dependency')],
    ['F1','F2','F3','F4','F5','F6'], 'Purpose/interpreted evidence, state identity, material composition and actual grants require supported admissibility on this subject without proving the eventual outcome or choosing a universal decision algorithm.',
    ['Domain owners select predicate, completeness, sufficiency, compatibility/loss, exceptions and grants; existing carriers may supply coordinates.'],
    ['Adds full semantic contract definition, six complete consumer conditions, once-at-consumer responsibility, far-side-independence rule, no invented exceptions and admissibility versus outcome/termination distinction.'])

add(L+'constraint-surface',
    'The bound contract for a current task subject/basis and representations or task views of its permitted work and unresolved obligations.', None, [
        (1,'D','A task constraint surface is the work permitted by bound constraints and grants together with unresolved obligations, distinguishing permitted choices from owner-reserved choices.'),
        (1,'O','Missing conditions are not freedom. A proven task-irrelevant condition need not be loaded again while that proof remains applicable.'),
        (2,'P','The surface may use prose, typed relations, predicates, a_c or a faithful task view. Dependency graphs need not be trees or prescribe an execution order.'),
        (2,'O','Distinguish established facts, assumed premises, discretionary choices and unknowns. Constraint satisfaction authenticates neither observations nor actor appointment. AC-017 owns a_c source-to-model fidelity and its independent evidence.'),
        (3,'P','Different implementations may both satisfy the surface; selection uses declared outcome, cost and owner criteria.'),
        (3,'O','Do not replace those criteria with a hidden requirement for the author preferred implementation. Acquire sufficient constraints and the actual material subject; an abstract surface alone is not a complete activation.')],
    [inp('task_contract','Current subject/basis, constraints, grants, owner-reserved choices, unresolved obligations and supported irrelevance.', 'when constructing or using a task surface'), inp('interpretation_and_choice','Representation fidelity, fact/premise/choice/unknown distinctions and declared outcome/cost/owner selection criteria.', 'when selecting or relying on a surface'), inp('actual_subject','Actual material subject plus sufficient constraints and applicable activation authority.', 'when work is activated')],
    [dep(L+'contract-application','Bound operation admissibility defines the permitted surface.'), dep(A+'ac-017-interpretation-fidelity','Independent source-to-model fidelity for an a_c representation.', 'domain_specialization','the surface uses a_c')],
    ['F1','F2','F4','F5','F6'], 'An interpreted purpose-bound contract delimits choices while preserving material unknowns and real grants; abstract satisfaction cannot authenticate external observations or appoint actors.',
    ['Task/subject owners select constraints and permitted latitude; representation and implementation remain within supported freedom.'],
    ['Restores the surface as definition/data, owner-reserved freedom, fact/premise/choice/unknown distinctions, representation alternatives, actor-appointment limit and selection criteria.'], definition_kind='task_constraint_surface')

add(L+'faithful-projection',
    'A declared authoritative-source-to-consumer projection or interpretation, exact or an admitted approximation.',
    'The source-to-consumer relation preserves the material determinations required for its declared consumer task under its interpretation and admitted loss.', [
        (1,'O','Apply Contract application to the source-to-consumer relation. Bind authoritative source/selector, target interpretation, task, required distinctions, admitted loss/approximation and invalidators. Preserve separate source/target identities; domain owners retain extra publication/adoption duties.'),
        (2,'O','Exact projection lets the consumer recover the same material determinations as the source. Approximation needs an adequacy relation and evidence for its end-to-end bound; local tolerances alone do not compose. Lost authority, weaker conditions and unknown-as-permission are fidelity defects.'),
        (3,'P','The relation may require full reproduction, a narrower sufficient view or an available authentic reference; task-irrelevant material may stay at its owner. No rule requires copying every source body into every event.'),
        (3,'O','Material omissions, stale source or unavailable references prevent corresponding reliance. A view cannot change source meaning. Establish currentness from selected source/dependency state, not merely label or generation timestamp.'),
        (4,'O','Check at least material permissible/prohibited/unresolved decisions independently specified from source. Model self-consistency, schema, checksum and generated diff prove different relations. On failure re-enter the first owning defect: source ambiguity, interpretation, projection, producer or consumer; never change source merely to match its view.')],
    [inp('projection_binding','Authoritative source/selector and target identities, interpretation, consumer task, material distinctions, invalidators and any publication/adoption conditions.'), inp('fidelity_and_loss_evidence','Exact recovery or admitted approximation adequacy and end-to-end bound, independent source-decision comparisons and loss authority.'), inp('reference_and_currentness','Resolution meaning/availability of any referenced material and evidence for selected source/dependency currentness.')],
    [dep(L+'contract-application','Shared source-to-consumer admissibility relation.'), dep(F+'workspace-and-context','Selected-source currentness and reuse.')],
    ['F2','F3','F4','F6'], 'Material interpreted meaning and ownership must survive a source-to-consumer relation; independently specified source decisions, not representational checks, support fidelity.',
    ['Domains select permitted loss, adequacy, publication/adoption conditions and whether reproduction, view or reference is sufficient.'],
    ['Adds exact versus approximate recovery obligations, source/target identity and ownership, currentness evidence, independent three-way decision cases and first-owning-defect re-entry.'])

add(L+'workrecovery-specialization',
    'Conditional specialization for interrupted purposeful work with admitted identity, persistent workspace, selected outcome, actual grants and a material uncertain effect.', None, [
        (1,'D',{'instance_premises':['admitted work identity','persistent workspace','selected outcome','actual grants','material uncertain effect'],'status':'Explicit instance premises; none is derived from finite capacity alone.'}),
        (2,'A',{'conditional_steps':[
            {'premises':['F1','F2','selected outcome','current subject'],'consequence':'Current claims need the actual predicate and support, not a remembered green status.','contracts':['SPEC_METHOD.agentic-construction-execution-stdo-up-020','REFERENCE_FRAME_METHOD.rf-005-exact-basis-and-coordinates'],'extra_choice':'Purpose owner selects outcome; UP-020 binds target/checkpoint and RF-005 basis.'},
            {'premises':['F2','F5','coupled material obligations','finite actor'],'consequence':'Acquire sufficient material or return admitted uncertainty; omitted support cannot satisfy.','contracts':['REFERENCE_FRAME_METHOD.rf-003-material-sufficiency','REFERENCE_FRAME_METHOD.rf-014-capability-fit'],'extra_choice':'Ordinary work entry locates a responsibility view; selection and configuration need independent grants.'},
            {'premises':['F3','F4','persistent work','affected dependencies'],'consequence':'Re-enter from observed current state, retain applicable progress and reconsider changed support.','contracts':['SPEC_METHOD.computed-classification-and-treatment','TICKET_METHOD.work-carrier-to-execution-rule'],'extra_choice':'Owning rules bind applicability/invalidation and wider frontier when independence is unproved; concrete freshness is domain policy.'},
            {'premises':['F2','F3','F6','uncertain effect','possible duplicate on repeat'],'consequence':'Intent or timeout proves neither completion nor safe-repeat authority; observe/reconcile, choose a permitted alternative or return unresolved.','contracts':['FOUNDATIONS.workspace-and-context','SPEC_METHOD.computed-classification-and-treatment'],'extra_choice':'Grant supplies observation/repair; idempotence must be established for the actual operation.'},
            {'premises':['F1','F4','F6','required results','current mandate'],'consequence':'Retain failures, uncovered obligations and uncertainty; choose only already-authorized continuation or truthful stop.','contracts':['SPEC_METHOD.agentic-construction-execution-stdo-up-020','FOUNDATIONS.result-conjunction','STDO_REFERENCE_FRAME_BASELINE.executive-attention-evaluation-and-action'],'extra_choice':'Independent assurance, decision rule and optional Baseline adoption are separately owned.'}]}),
        (3,'P','This chain argues only under its stated premises, not every source clause. Carrier layout, actor count, numeric budgets, optional Baseline adoption, release procedure and domain enums remain independent choices; the chain adds no mandatory ledger.'),
        (4,'O','Recovery uses sufficient projected clauses plus the actual subject. After basis selection the ordinary work entry locates material; its projection is no rival authority and guarantees no different task sufficiency.'),
        (4,'P','A recovery activation need not load this complete argument, every method or all historical event bodies.')],
    [inp('recovery_instance','Admitted work identity, continuing workspace/current subject, selected outcome, actual grants and the material uncertain effect.', 'when applying this conditional chain'), inp('current_support','Required predicates/checkpoint, current basis, coupled dependencies, actor capability, affected prior results and evidence for valid reuse/independence.', 'when applying this conditional chain'), inp('recovery_decision','Permitted observations/repair/continuation, effect reconciliation and any actual idempotence evidence, decision rule and required independent assurance.', 'when choosing next recovery action')],
    [dep(L+'contract-application','Generic contract specialized by explicit work premises.'), dep(F+'workspace-and-context','Generic currentness and unknown-effect handling.'), dep(S+'agentic-construction-execution-stdo-up-020','Target/checkpoint and delegated construction disposition.', 'domain_specialization'), dep(R+'rf-005-exact-basis-and-coordinates','Exact current basis in the selected frame.'), dep(R+'rf-003-material-sufficiency','Sufficient material acquisition.'), dep(R+'rf-014-capability-fit','Admitted response to capacity misfit.'), dep(S+'computed-classification-and-treatment','Product-context invalidation/reuse and current treatment.'), dep(T+'work-carrier-to-execution-rule','Carrier continuity and recorded obligations.'), dep(F+'result-conjunction','Retain failed/missing required results.'), dep(B+'executive-attention-evaluation-and-action','Optional adopted coordination specialization.', 'domain_specialization','adopted and lawfully activated')],
    ['F1','F2','F3','F4','F5','F6'], 'Under the explicitly supplied work/recovery premises, current support and uncertain effects constrain lawful continuation; they do not select the carrier, topology or outcome authority.',
    ['Carrier layout, actors, budgets, optional Baseline, release procedure, domain enums, concrete freshness and assurance/decision rules are separately owned choices.'],
    ['Replaces an invented general outcome predicate with all five conditional argument steps, exact instance premises and each source-owned extra choice; restores optional adoption and bounded acquisition permissions.'], definition_kind='conditional_work_recovery_argument', result={'kind':'argument_data_with_embedded_constraints','conditions':'This argument has no local result enum. Instance acquisition, treatment, continuation and authority claims use their named deciding owners and the shared core result contract.'})

add(L+'transformation-admission-specialization',
    'Conditional specialization for a consequential entity transition with identified current predecessor, declared candidate family, durable commit boundary and actual admission authority.', None, [
        (1,'D',{'instance_premises':['consequential entity transition','identified current predecessor','declared candidate family','durable commit boundary','actual admission authority'],'extra_policy':'These supplement F1-F6; foundations do not select predicate, quorum or supported topology.'}),
        (2,'A',{'conditional_steps':[
            {'premises':['F2','F3','material current entity/predecessor'],'consequence':'A candidate/judgment about another identity or superseded basis cannot establish this transition.','owner':'DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016','extra_policy':'UP-016 declares basis continuity and enclosing joins; domain selects identity/currentness law.'},
            {'premises':['F4','material governing seams crossed'],'consequence':'Local validity cannot establish an unexamined affected relation; omitted support stays unresolved.','owners':['DESIGN_MODULE_METHOD.bounded-frame-conservation-stdo-up-017','SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021'],'extra_policy':'UP-017 declares affected network/invariants and design seams; each UP-021 owner independently derives/validates complete enclosing relation and claimed far-side independence.'},
            {'premises':['F6','distinct proposal/judgment/durable admission'],'consequence':'Projection or satisfied judgment provides evidence, not a missing admission grant.','owners':['DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016','SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021'],'extra_policy':'UP-016 declares admitters/cardinality/competing-path disposition; UP-021 alone owns admission and standing-test semantics.'},
            {'premises':['F2','F5','unresolved supported forms/commit effects'],'consequence':'Missing support proves neither admission nor non-applicability; preserve unknown effects before dependent use.','owner':'DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016','extra_policy':'UP-016 declares supported boundaries, partial-failure coverage and reconstruction; actual admission relation owns concrete outcomes.'}]}),
        (3,'O','The design admission consumer binds Contract application to its transition relation and distinguishes valid support from a merely shape-correct candidate missing material basis or authority.'),
        (3,'P','Predicate, refinement, commit-unit decomposition and permitted direct/composite/nested forms remain domain policy. This argument derives none of those choices and adds no validation pass; shared Contract application owns the decision and design binds domain obligations.')],
    [inp('admission_instance','Consequential transition, exact entity/current predecessor, candidate family, durable commit boundary and actual admission authority.', 'when instantiating the argument'), inp('design_and_support','UP-016 admission relation/cardinality/boundaries/partial-failure/reconstruction declarations; UP-017 affected governing network, preserved invariants and seam support/independence.', 'when instantiating admission'), inp('actual_admission','UP-021 authoritative complete relation/basis and participant/join validation, concrete outcome/cause and observed commit effects.', 'when evaluating or relying on admission')],
    [dep(L+'contract-application','Shared admissibility applied to exact transition.'), dep(D+'admission-contract-use','Design consumer binding and concrete predicate/refinement.'), dep(D+'transformation-admission-completeness-stdo-up-016','Design relation, basis continuity, cardinality, boundaries and reconstruction.'), dep(D+'bounded-frame-conservation-stdo-up-017','Affected network, invariants and seam declarations.'), dep(S+'complete-enclosing-relation-admission-stdo-up-021','Sole admission/standing-test semantic owner; complete relation and actual authority.')],
    ['F2','F3','F4','F5','F6'], 'With the named transition premises, exact current identity, enclosing support and actual authority constrain admission; a local shape check cannot decide those joins.',
    ['Design/domain choose predicate, quorum/cardinality, topology, result refinement and commit-unit decomposition; UP-021 chooses admission and standing-test semantics.'],
    ['Restores the row as a conditional argument with four premise/consequence/policy rows, separate UP-016/017/021 ownership and explicit transition assumptions instead of an invented local admission predicate.'], definition_kind='conditional_transition_admission_argument', result={'kind':'argument_data_with_embedded_constraints','conditions':'No local admission enum or new assessment is defined here. The concrete admission predicate/refinement and separate decision/commit claims remain at UP-021 and its design consumer.'})

add(L+'bind',
    'Binding current instance coordinates for a selected library operation or reliance.',
    'The selected instance has supported current purpose, subject identity, governing specification, role, authority, state and material relations.', [
        (1,'O','Recover current purpose, subject identity, governing specification, role, authority, state and required relations. Return conflicts, missing bindings and stale bindings explicitly; a name, path, cached result or available tool is not a grant.')],
    [inp('instance_coordinates','Current purpose, subject identity, governing specification/basis, actor role, actual grants, current state and required relations with their authoritative support.')],
    [dep(L+'foundational-contract','Bind supplies the other responsibilities current instance coordinates.', 'definition_dependency'), dep(L+'contract-application','Current binding and actual admissibility conditions.'), dep(F+'result-algebra','Conflicting/missing/stale coordinates retain predicate-bound cause and diagnosis.')],
    ['F1','F2','F3','F6'], 'Interpreted purpose and state require actual current coordinates, while available names/tools cannot supply authority.',
    ['The instance chooses its domain-specific operation and purpose; Bind imposes no stage or actor topology.'],
    ['Adds explicit missing/conflicting/stale result handling and names/paths/cache/tool grant exclusions; supplies concrete binding input coordinates.'])

add(L+'acquire',
    'Acquisition for a selected task under its execution binding and actual grant.',
    'This acquisition supplies sufficient authentic material and dependencies for the selected task on its bound current subject, requirements, grant and destination.', [
        (1,'O','Apply Workspace/context: bind current subject, requirements, grant and destination; resolve sufficient authentic material and dependencies; reconcile stale summaries against observations. Measure context where selected by the execution binding and assess actual adequacy separately. Capacity misfit uses the admitted finite-capacity response rule; do not omit material to fit.'),
        (1,'P','The actual grant selects available refinement, reassignment or escalation. A context measurement is neither an automatic adequacy result nor an unstated universal measurement requirement.')],
    [inp('acquisition_target','Current task/subject/basis, requirements, destination, grant, accessible authentic material and material dependency support.'), inp('fit_and_response','Actor capability, actual acquired material/adequacy evidence, execution-selected context measurement boundary and any authorized misfit response.')],
    [dep(F+'workspace-and-context','Owns acquisition/currentness and subject-versus-summary relation.'), dep(F+'finite-capacity-and-total-handling','Owns admitted misfit response without supplying a configuration/delegation grant.'), dep(L+'foundational-contract','Acquire returns adequate support or the applicable core result on its own exact acquisition predicate.', 'definition_dependency')],
    ['F1','F2','F3','F4','F5','F6'], 'A finite actor needs sufficient current support for the selected task; a capacity bound does not justify missing material or authorize a new configuration.',
    ['The execution binding selects measurements; existing grants choose lawful responses and the domain defines sufficiency.'],
    ['Adds requirements/grant binding, stale-summary reconciliation, selected measurement versus actual adequacy, exact capacity-response dependency and its grant limit.'])

add(L+'transform',
    'Construction or effect performance under the selected bound X-to-Y contract; optional Baseline Worker and a_c transformation bindings apply only when selected.',
    'This transformation constructs its declared output or performs its allowed effects while preserving the bound contract material relations and original producer/input/effect evidence.', [
        (1,'O','Construct output or perform effects within the bound contract. Preserve original producer, material inputs and observed effects; return the instance-owned domain outcome with its core mapping. Apply Workspace/context unknown-effect law.'),
        (1,'P','A consumer-adopted, lawfully activated Baseline WorkerResult retains its own outcomes; an AC-013 instance retains that owner outcomes. Worker internal search is HOW inside, and cannot widen, the outer outcome/effect grant.')],
    [inp('transformation_contract','Bound input/output domains, current material inputs, original producer, outer outcome, preservation relations and exact operation/effect grant.'), inp('actual_outcome','Produced output or actual observed effect parts, domain outcome/cause, core mapping and uncertain-effect support.'), inp('selected_specialization','Adopted and lawfully activated Baseline Worker contract or exact AC-013 traversal/model transformation contract.', 'only when the instance selects that specialization')],
    [dep(L+'contract-application','Transformation admissibility and material preservation.'), dep(F+'workspace-and-context','Unknown-effect observation before dependent action.'), dep(F+'result-algebra','Qualified original outcome, evidence, actual performance/effects.'), dep(B+'derived-worker-frame','Conditional adopted WorkerResult, not a generic library enum.', 'domain_specialization','consumer adopts and lawfully activates Baseline Worker'), dep(A+'ac-013-transformation','Exact model-delta/transformation relation, not a generic rewrite.', 'domain_specialization','an AC-013 transformation instance is selected')],
    ['F1','F2','F3','F4','F5','F6'], 'The selected X-to-Y contract conserves material relations and actual effect truth under the grant; a useful output does not grant acceptance.',
    ['The instance owns its outcome domain and internal search; selected domain profiles own their additional contracts.'],
    ['Restores conditional Worker/AC-013 ownership, unknown-effect dependency and explicit construction/effect inputs; avoids inventing a universal Worker enum.'])

add(L+'evaluate',
    'Evaluation of a declared predicate under its domain evidence rule, including UP-020 assessments where selected.',
    'The exact predicate is evaluated on its exact subject and basis under its owning evidence rule with original outcome, performance, effects and residual coverage retained.', [
        (1,'O','Apply the core algebra to exact predicate/subject/basis. Keep original domain outcome, performance, effect observations, citations and residual coverage. The domain evidence rule, including required independent authorship, decides that predicate and adds no parallel result algebra or new grant.'),
        (1,'P','A function may exercise decision authority already admitted by its own contract; a Baseline Reviewer retains only the grant owned by that adopted profile.'),
        (2,'R','For UP-020, the assessor classification is a reason-qualified domain outcome on the exact cone-preservation predicate. Spec proportional-disposition alone owns its map and conditions; a separately bound decision authority returns the authorized disposition. This library defines no second remedy table.')],
    [inp('evaluation','Exact predicate, subject, basis, domain evaluation/evidence rule, required independent authorship and admissible observations/citations.'), inp('performance_and_effects','Observed evaluation extent/conclusion, original domain outcome and cause, actual effects and residual/absent coverage.'), inp('domain_decision','UP-020 cone-preservation assessment/refinement and separate decision authority, or a specifically adopted profile grant.', 'when the selected evaluation or decision uses those domain contracts')],
    [dep(F+'result-algebra','Single predicate-bound evidence and performance/effect law.'), dep(S+'proportional-disposition','Sole UP-020 reason-qualified assessment map, separate from applied decision.', 'domain_specialization','UP-020 assessment is selected'), dep(F+'judgment-and-authority','Evaluation supplies no new grant; admitted domain decisions retain their own mandate.'), dep(B+'derived-reviewer-frame','The adopted Baseline Reviewer has its profile-defined bounded evaluation grant; no decision grant follows from review access.', 'domain_specialization','Baseline Reviewer is adopted and lawfully activated')],
    ['F1','F2','F5','F6'], 'Evidence supports one exact interpreted claim while finite handling retains uncertainty; evaluation is distinct from actual operation and decision grants.',
    ['Domain owners select evidence/independence rules and original outcomes; Spec owns UP-020 remedy refinements.'],
    ['Adds exact domain evidence rule and independence, existing decision-function permission, profile grant scope and single-owned UP-020 mapping.'])

add(L+'conjoin',
    'Combining required evaluation results for a selected composite predicate, coverage plan and material joins.',
    'The selected composite predicate is evaluated under its declared core conjunction or explicit alternative operator with authentic contributions and preserved coverage.', [
        (1,'O','Apply Result conjunction to the exact composite predicate, required coverage and joins. Authenticate contributors and preserve their predicates, original outcomes and evidence. Retain known failure and required uncovered coverage together; distinguish missing planned judgments from required coverage outside an authenticated plan.'),
        (1,'P','Another declared logical operator uses the same core record on its own predicate and cannot silently weaken all-required conjunction.')],
    [inp('composite_contract','Exact outer predicate/subject/basis, required coverage and plan, material joins and declared conjunction/alternative operator.'), inp('contributions','Authenticated producer/subject/basis/membership, original predicates/outcomes/evidence, known failures, absent planned slots, outside-plan uncovered obligations and material effects.')],
    [dep(F+'result-conjunction','Owns authentication, verdict precedence, alternative operators and normalized effect composition.')],
    ['F2','F3','F4','F6'], 'Typed composition of interpreted authenticated claims must retain failures and required missing coverage rather than creating satisfaction through aggregation.',
    ['The outer claim selects its required predicates and any explicit alternate operator; the shared owner determines composition semantics.'],
    ['Adds missing-plan versus outside-plan coverage and exact authentic contribution inputs while referring all aggregate semantics to their single owner.'])

add(L+'dispose',
    'A bound decision actor consuming closed work/evaluation results under a current mandate; UP-020, Ticket and Release classifications apply only within their owning domains.',
    'Disposition D on the exact subject S and basis B is selected under its actual mandate M and bound authority.', [
        (1,'O','Consume exact closed work/evaluation results under current mandate. An agentic construction instance selects accept/local_repair/re_enter/reject for its declared cone under UP-020. Do not change upstream meaning or take a reserved owner decision. Accept binds an exact checkpoint and does not imply release; Product-outcome acceptance intervals remain governed by UP-013.'),
        (1,'P','Choose a next already-authorized action or stop within the instance permitted outcomes; domain-specific yielding remains at its owner.'),
        (2,'O','Other instances keep their original domain classifications. Distinguish recorded state, evaluation outcome and decision disposition, each evaluation/decision bound to its own exact core predicate. A recorded status is neither judgment nor grant. Ticket owns sprint/paydown/work-carrier closure; Release owns conserved/superseded/intentionally removed/not applicable. Shared Dispose machinery changes no class or grant.'),
        (2,'P','A bound operation authority may record condition-based closure only where its owning contract permits it.'),
        (3,'O','Apply UP-020 accept/local-repair/re-entry/reject conditions once at Spec proportional-disposition; this library does not redefine them.')],
    [inp('decision_binding','Exact subject/cone/checkpoint/basis, current mandate, bound decision or closure-operation authority and reserved-owner limits.'), inp('closed_results','Exact closed work/evaluation results with original classifications, reasons, evidence, performance/effects and outstanding obligations.'), inp('domain_conditions','UP-020 disposition conditions and applicable UP-013 acceptance interval, or exact Ticket/Release/other classification contract; any already-authorized next action or local yield permission.')],
    [dep(F+'result-algebra','Decision predicate is separate from fitness and recorded status.'), dep(S+'agentic-construction-execution-stdo-up-020','Agentic construction cone/checkpoint disposition.', 'domain_specialization','UP-020 instance'), dep(S+'proportional-disposition','Single deciding owner for UP-020 conditions and assessment/decision separation.', 'domain_specialization','UP-020 instance'), dep(S+'product-outcome-conservation-stdo-up-013','Product-outcome acceptance interval and exhaustion.', 'domain_specialization','Product-outcome acceptance'), dep(T+'work-carrier-to-execution-rule','Ticket domain carrier/closure authority boundary.', 'domain_specialization','Ticket-owned closure'), dep('RELEASE_METHOD.successor-baseline-conservation-stdo-up-015','Release domain conservation/replacement/removal/applicability classifications.', 'domain_specialization','predecessor-claim disposition')],
    ['F1','F2','F3','F6'], 'Exact current evidence informs a decision under an existing mandate; neither result labels nor machinery grant disposition or upstream meaning changes.',
    ['Each domain owns its classifications, decision rules, permitted yields and closure effects. UP-020 selects four remedies; UP-013 owns the outcome interval.'],
    ['Adds exact mandate/checkpoint and release distinction, conditional next-action/yield permission, separate Ticket/Release classifications and condition-based closure authority.'], result={'predicate_binding':'The applied decision predicate, not candidate fitness or mere status recording.'})

add(L+'composition-law',
    'Composition T:X->Y followed by S:Y->Z under a declared outer predicate, with domain specialization and categorical claims only where selected.',
    'This composite conserves its declared outer predicate and every material typed join under the admitted compatibility relation.', [
        (1,'O','Apply Contract application to the outer predicate and all material joins. Bind which outputs satisfy which preconditions, allowed effects of each step and composite preservation relations. Local correctness cannot establish an unsupported join; distinct authorities remain distinct.'),
        (1,'P','Distinct bases may compose under an admitted coherent topology.'),
        (2,'D',{'conditional_domain_owners':{'design_declarations':['DESIGN_MODULE_METHOD.transformation-admission-completeness-stdo-up-016','DESIGN_MODULE_METHOD.bounded-frame-conservation-stdo-up-017'],'complete_transition_admission_and_semantic_commit':'SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021','frame_relations':'REFERENCE_FRAME_METHOD.using-frames-in-conjunction','typed_calculus_paths':'AXIOMATIC_CALCULUS.ac-016-typed-composition'},'scope':'Extra domain policies are part of the selected composite contract; they do not become generic law for every composition.'}),
        (3,'O','Evaluation results use core conjunction or an explicit alternative operator. Effect combination retains actual boundaries and observations. Regrouping, reordering and concurrent execution are distinct claims; associativity permits neither reordered effects nor concurrency. The computational binding supplies any additional independence/effect equations it relies on.'),
        (4,'O','For a categorical claim declare domain objects, arrows, equality, identities and composition and discharge those laws. Contract preservation alone establishes neither a category nor a functor or proof of them.')],
    [inp('composed_contracts','Exact T:X->Y and S:Y->Z contracts, outer predicate, output-to-precondition joins, allowed effects, preservation relations, authorities and admitted basis topology.'), inp('component_evidence','Actual intermediate outputs/judgments, selected operator, authentication, material effect boundary/observations and required domain specialization support.'), inp('additional_composition_laws','Independence/effect equations for reordering or concurrency; categorical objects/arrows/equality/identities/composition and proofs.', 'only for the corresponding additional claim')],
    [dep(L+'contract-application','Outer predicate and material-join admissibility.'), dep(F+'result-conjunction','Evaluation-result operator and effect combination.'), dep(F+'orthogonal-descriptions','Conditional categorical demonstration.'), dep(D+'transformation-admission-completeness-stdo-up-016','Design declarations only.', 'domain_specialization','design composition'), dep(D+'bounded-frame-conservation-stdo-up-017','Design affected-frame preservation only.', 'domain_specialization','design composition'), dep(S+'complete-enclosing-relation-admission-stdo-up-021','Complete-transition admission/semantic commit only.', 'domain_specialization','consequential admission'), dep(R+'material-composition','Frame relation binding.', 'domain_specialization','frame-governed composition'), dep(A+'ac-016-typed-composition','Exact calculus traversal paths.', 'domain_specialization','a_c composition')],
    ['F2','F3','F4','F6'], 'Typed outer conservation requires compatible intermediate relations with preserved authorities; local validity cannot establish unexamined joins or mathematical laws.',
    ['Instances choose coherent topology and outer predicate/operator; domain policies and computational effect equations remain explicit additions.'],
    ['Adds typed output/precondition join, coherent distinct-basis permission, all conditional domain ownerships, concurrency distinction and explicit categorical domain proof conditions.'])

add(L+'recovery-law',
    'Selecting the next dependent action after interruption, changed support, context loss or uncertain effects; continuity independent of private actor state is a conditional additional claim.',
    'The next dependent action relies on current work identity and state, applicable retained support and sufficiently observed or reconciled effects under its existing grant.', [
        (1,'O','Apply Workspace/context before the next dependent action: bind current work identity, observe changed material state, retain applicable work, reconsider affected support and preserve unknown effects until sufficiently observed/reconciled. Context is replaceable; workspace survives the actor.'),
        (2,'O','Bounded construction owns progress, stop, total handling and the causal-change condition for retry. Spec owns Product progress/re-entry, Ticket owns carrier use, and adopted profiles retain additional recovery duties.'),
        (2,'P','Process restart is acquisition and does not prove construction restart or workspace deletion is required.'),
        (3,'O','Select proof capable of falsifying the affected relation with its required independence; apply UP-014 for cost selection. To claim continuity independent of private actor state, exclude that state and compare the reconstructed decision to current material reality. Same-context exercise cannot establish that claim.')],
    [inp('recovery_state','Current work identity, changed material state, prior outputs/support and their current applicability, outstanding obligations and observed/uncertain effects.'), inp('next_action','Exact current grant, selected next dependent operation, causal change for failed-relation retry and any adopted profile/carrier duties.'), inp('proof_selection','Affected relation, falsifying discriminator, required independence and UP-014 cost basis; state-excluding reconstruction and reality comparison for private-state-independent continuity claims.')],
    [dep(F+'workspace-and-context','Current-state acquisition/reuse/effect reconciliation.'), dep(F+'bounded-construction','Progress/stop/total handling and causal-change retry condition.'), dep(T+'work-carrier-to-execution-rule','Carrier and persistent obligation continuity.'), dep(S+'computed-classification-and-treatment','Product-specific affected-support and owning-layer re-entry.'), dep(S+'proportional-method-and-delivery-stdo-up-014','Adequate proof cost selection.')],
    ['F1','F2','F3','F4','F5','F6'], 'Continuing work identity and material current evidence support recovery without erasing progress; uncertainty constrains dependent action, and private-state independence needs evidence that excludes that state.',
    ['Product/carrier/adopted profiles own extra recovery policy; proof choices use declared independence and proportionality, not a universal restart/replay rule.'],
    ['Adds profile/Spec/Ticket owner boundaries, supported causal-change retry, adequate falsifying proof and the state-excluding continuity test missing from the retained binding.'])

add(L+'cost-and-contraction',
    'A method-burden, computational/handoff cost or contraction claim under its selected outcome and measurement boundary.',
    'This burden or contraction claim is justified under UP-014 using the measures material to the claim while preserving required meaning, authority, adequacy and independent evaluations.', [
        (1,'O','UP-014 owns method-burden justification. Apply its deciding definition rather than raw counts. Computational or handoff claims select the measures material to their stated claim.'),
        (1,'D',{'illustrative_measures':['transferred/acquired bytes','attention','I/O','CPU','addressable memory','critical-path elapsed time','aggregate work','displaced human assurance'],'status':'Illustrative choices, not all-fields requirements, universal quotas or another accounting carrier.'}),
        (2,'O','A reference reduces storage only if its resolution preserves adequacy. Smaller documents or faster local preparation do not prove whole-path improvement. Contract duplicated meaning/authority only while preserving required distinctions and independent evaluations.')],
    [inp('burden_claim','Selected outcome, exact cost/contraction claim and comparison/measurement boundary; ambiguity removed versus effective reasoning complexity under UP-014.'), inp('measures_and_preservation','Material selected measures and comparison evidence, reference-resolution adequacy, whole-path effects and preservation of distinctions/authority/required independent checks.')],
    [dep(S+'proportional-method-and-delivery-stdo-up-014','Sole proportionality definition and method burden/cost-selection law.'), dep(L+'faithful-projection','Reference resolution preserves material adequacy when contraction uses references.')],
    ['F1','F2','F4','F5','F6'], 'Finite resources make purpose-related burden relevant, but supported adequacy and evidence determine whether contraction improves the whole claimed path.',
    ['UP-014 selects proportionality; each claim selects material resource measures and comparison scope without a universal quota or carrier.'],
    ['Adds the complete illustrative measure set with its nonmandatory standing, reference-resolution adequacy and whole-path/independence conservation conditions.'])

# Only the material entry selector was read, not the rest of the candidate skill.
entry_dependency = dep('CARRIER.plugins.spec.skills.stdo-work.SKILL.md',
    'The exact #acquire-the-responsibility-frame selector locates sufficient owner clauses after basis selection; it is not source law, adoption, an effect grant or a universal sufficiency guarantee.',
    'acquisition_route', 'using the ordinary work entry for recovery')
for r in BINDINGS:
    if r['id'] == L+'workrecovery-specialization':
        r['dependencies'].append(entry_dependency['id'])
        r['dependency_relations'].append(entry_dependency)

# These exact owner excerpts were exposed during source acquisition. Full member
# byte reads by this program are mechanical hash/extraction work, not claims that
# every clause of every dependency member was semantically acquired.
ACQUIRED_DEPENDENCY_IDS = [
    F+'foundational-commitments', F+'purpose-and-interfaces',
    F+'typed-composition-and-conservation', F+'finite-capacity-and-total-handling',
    F+'judgment-and-authority', A+'position', A+'ac-007-constraint-and-refusal',
    A+'ac-011-projection', A+'ac-013-transformation', A+'ac-015-functor-classification',
    L+'transformation-library', L+'foundational-contract',
    R+'position', R+'rf-003-material-sufficiency', R+'rf-005-exact-basis-and-coordinates',
    R+'rf-014-capability-fit', R+'using-frames-in-conjunction', R+'workspace-coverage',
    R+'coverage-basis', R+'coverage-ledger', R+'material-composition',
    D+'admission-contract-use', D+'bounded-frame-conservation-stdo-up-017',
    D+'transformation-admission-completeness-stdo-up-016',
    S+'agentic-construction-execution-stdo-up-020',
    S+'complete-enclosing-relation-admission-stdo-up-021',
    S+'computed-classification-and-treatment', S+'proportional-disposition',
    S+'proportional-method-and-delivery-stdo-up-014',
    S+'product-outcome-conservation-stdo-up-013',
    'RELEASE_METHOD.successor-baseline-conservation-stdo-up-015',
    T+'work-carrier-to-execution-rule', B+'derived-worker-frame',
    B+'derived-reviewer-frame', B+'executive-attention-evaluation-and-action'
]

def source_record(r):
    o = r['owner']
    b = body(r)
    return {'id': r['id'], 'owner': o, 'source_member_sha256': sha(source(r)),
            'owner_bytes': len(b), 'source_clause_count': len(r.get('source_clauses', []))}

def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def construct():
    assert {r['id'] for r in BINDINGS} == selected_ids
    ordered = sorted(BINDINGS, key=lambda r: r['id'])
    observation = {'commit': OBSERVED, 'path': ACCOUNT_PATH, 'sha256': OBSERVED_SHA,
                   'selection': 'All and only determinations with nonempty unrepresented_scope in these frozen bytes.',
                   'selected_count': 25}
    contribution = {
        'schema': 'stdo.semantic-contribution.v1',
        'schema_version': 'stdo.semantic-contribution.v1',
        'input_account_sha256': BASE_SHA, 'source_commit': D1,
        'documentary_source_commit': D2, 'observed_preimage_account': observation,
        'grant': 'I3-R2-CORE-READY-COMPLETE-01', 'grant_record_commit': GRANT_COMMIT,
        'execution_contract': 'EC-CODEX-I3-02', 'common_input': COMMON,
        'installed_builder': 'v2.5.1-rc.2', 'installed_builder_manifest_sha256': MANIFEST,
        'assigned_owner_paths': sorted({r['owner']['path'] for r in selected}),
        'standing': 'Authored completion of the exact 25 observed source omissions. No independent fidelity, instance satisfaction, acceptance or release is claimed.',
        'shared_contract_references': ['core.shared_contracts.core_evaluation', 'core.shared_contracts.definition_data'],
        'bindings': ordered, 'ready_unchanged_ids': [], 'unfinished_units': [],
        'completion': {'assigned_ids': sorted(selected_ids), 'completed_ids': sorted(selected_ids),
                       'unfinished_ids': [], 'source_omissions': [],
                       'scope': 'Only the 25 selected source units; dependencies are referenced at their owners, not rewritten.',
                       'meaning': 'Author source comparison and construction complete; independent fidelity and actual-instance judgments remain separate.'}
    }
    write_json('bindings.json', contribution)
    selected_sources = [source_record(r) for r in selected]
    dep_sources = [source_record(by_id[i]) for i in ACQUIRED_DEPENDENCY_IDS]
    entry_path = 'plugins/spec/skills/stdo-work/SKILL.md'
    entry = frozen(D2, TENANT + 'successor/' + entry_path)
    start = entry.index(b'## Acquire The Responsibility Frame')
    end = entry.find(b'\n## ', start + 1)
    end = len(entry) if end < 0 else end
    entry_excerpt = entry[start:end]
    write_json('SOURCE_SCOPE.json', {
        'schema': 'stdo.scoped-author-source-account.v1',
        'grant': contribution['grant'], 'observed_preimage_account': observation,
        'integration_source_commit': D1, 'documentary_source_commit': D2,
        'common_input': COMMON, 'selected_owner_members_identical_D1_D2': True,
        'selected_source_units': selected_sources,
        'acquired_dependency_owner_excerpts': dep_sources,
        'additional_acquired_selector': {'path': entry_path, 'anchor': 'acquire-the-responsibility-frame',
                                         'source_member_sha256': sha(entry), 'byte_start': start,
                                         'byte_end': end, 'bytes': len(entry_excerpt), 'sha256': sha(entry_excerpt)},
        'acquisition_measurement': {
            'selected_owner_bytes_unique': sum(r['owner_bytes'] for r in selected_sources),
            'dependency_owner_bytes_unique': sum(r['owner_bytes'] for r in dep_sources),
            'additional_entry_selector_bytes': len(entry_excerpt),
            'boundary': 'Unique exact source-owner excerpts and one material entry selector. Tool formatting, repeat reads, old representation, bootstrap/governing Product/grant reads and inherited context are not included.',
            'total_cumulative_acquisition_bytes': None,
            'active_retained_context': 'not instrumented; no actor-fit claim',
            'supplied_context_bytes': None,
            'construction_timer_start_utc': BUILD_STARTED,
            'pre_timer_source_acquisition_elapsed': 'not instrumented',
            'paid_actor_calls': 0,
            'platform_spend': 'not instrumented'
        },
        'other_acquisition_disclosures': [
            'Read governing bootstrap, Product Definition, Product/frame basis and admitted grant at ef2ab0a.',
            'Read core/method contribution key shapes and one example row each for schema compatibility only; no peer candidate or oracle expectations were acquired.',
            'A broad initial routing search exposed oracle ACTIVATION metadata in tool output, not task bodies, expected answers, cases or author reasoning; it was not used.',
            'The parent supplied two closed F01 review examples after the result-algebra/conjunction definitions had been constructed. They confirm source-owned conditions already represented; no independence claim is made.',
            'A lightweight memory lookup supplied release-resolution procedure only; installed rc.2 was verified live. Historical substantive source facts were not used.'
        ]
    })
    write_json('COMPARISON.json', {
        'schema': 'stdo.scoped-author-comparison.v1',
        'observed_preimage_account': observation, 'source_commit': D2,
        'standing': 'Author comparison findings, not independent review.',
        'rows': sorted(COMPARISONS, key=lambda r: r['id'])
    })
    print(json.dumps({'written': ['bindings.json', 'SOURCE_SCOPE.json', 'COMPARISON.json'],
                      'bindings': len(ordered),
                      'source_clauses': sum(len(r['source_clause_ids']) for r in ordered),
                      'definition_rows': sum(r['predicate'] is None for r in ordered),
                      'unfinished': 0, 'bindings_sha256': sha((HERE/'bindings.json').read_bytes())}))

if __name__ == '__main__':
    construct()
