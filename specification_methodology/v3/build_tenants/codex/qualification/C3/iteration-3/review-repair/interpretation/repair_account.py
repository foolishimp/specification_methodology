"""Apply the EC03 source-first account repairs to an exact documentary freeze.

The predecessor account stays at its immutable commit. This transform writes
only the successor account and its own report; it refuses unreviewed source drift.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
TENANT = Q.parents[2]
PACKAGE = TENANT / 'successor'
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE, text=True).strip())
PREIMAGE = '0517eb2771b18a7369c69e52570a3db3e36f8229'
DOCUMENTARY = '2476713d315c00ac61d336a3281d67e4a384d4ce'
ROUTES_PATH = HERE.parent / 'source/ARGUMENT_ROUTES.json'
ACCOUNT_PATH = str((Q / 'DETERMINATIONS.json').relative_to(REPO))
spec = importlib.util.spec_from_file_location('build_interpretation', Q / 'build_interpretation.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def packed(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n').encode()


def git_bytes(commit, relative):
    return subprocess.check_output(['git', 'show', commit + ':' + relative], cwd=REPO)


def heading_units(raw):
    """Immediate Markdown bodies with byte and diagnostic-line coordinates."""
    lines = raw.splitlines(keepends=True)
    found, counts, offset, fence = [], {}, 0, None
    for number, line in enumerate(lines, 1):
        value = line.decode('utf-8')
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', value)
        if marker:
            mark = marker[1]
            if fence is None:
                fence = (mark[0], len(mark))
            elif fence[0] == mark[0] and len(mark) >= fence[1]:
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', value)
            if match:
                stem = build.slug(match[2]); n = counts.get(stem, 0); counts[stem] = n + 1
                found.append({'anchor': stem + ('-' + str(n) if n else ''), 'start_line': number,
                              'byte_start': offset, 'level': len(match[1]), 'heading': match[2]})
        offset += len(line)
    for index, item in enumerate(found):
        following = found[index + 1] if index + 1 < len(found) else None
        item['byte_end'] = following['byte_start'] if following else len(raw)
        item['end_line'] = following['start_line'] - 1 if following else len(lines)
        item['body'] = raw[item['byte_start']:item['byte_end']]
    return {item['anchor']: item for item in found}


def make_owner(path, unit, raw):
    if unit is None:
        return {'path': path, 'anchor': '', 'body_sha256': digest(raw), 'unit_scope': 'whole_member'}
    return {'path': path, 'anchor': unit['anchor'], 'start_line': unit['start_line'],
            'end_line': unit['end_line'], 'body_sha256': digest(unit['body'])}


def local_source_body(row, source):
    owner = row['owner']
    if owner.get('unit_scope') == 'whole_member':
        return source, 0, len(source)
    unit = heading_units(source).get(owner['anchor'])
    if unit is None:
        raise ValueError('Owner heading no longer resolves: ' + row['id'])
    return unit['body'], unit['byte_start'], unit['byte_end']


def remap_blocks(row, old_raw, new_raw, unit):
    """Keep exact surviving spans; changed spans use an honest whole-body route.

    No old paragraph hash is assigned to changed text. A role attached to a
    changed paragraph is explicitly rebound to the complete current owned body,
    retaining its semantic target while abandoning unsupported fine precision.
    """
    new_body = unit['body'] if unit else new_raw
    base = unit['byte_start'] if unit else 0
    old_unit = heading_units(old_raw).get(row['owner']['anchor']) if unit else None
    old_body = old_raw if unit is None else (old_unit or {}).get('body', b'')
    old_base = old_unit['byte_start'] if old_unit else 0
    blocks, replacements = [], {}
    for block in row.get('source_clauses', []):
        prior = old_raw[block['byte_start']:block['byte_end']]
        if digest(prior) != block['sha256']:
            raise ValueError('Preimage block drift: ' + row['id'] + '#' + block['id'])
        positions = ([block['byte_start'] - old_base] if old_body == new_body else
                     [m.start() for m in re.finditer(re.escape(prior), new_body)] if prior else [])
        if len(positions) == 1:
            mapped = dict(block, byte_start=base + positions[0], byte_end=base + positions[0] + len(prior))
            blocks.append(mapped)
        else:
            replacements[block['id']] = 'body'
    if replacements or not blocks or digest(old_body) != digest(new_body):
        blocks.append({'id': 'body', 'sha256': digest(new_body), 'byte_start': base,
                       'byte_end': base + len(new_body), 'roles': ['source_owned_body']})
    def translate(value):
        if isinstance(value, list):
            return [translate(v) for v in value]
        if isinstance(value, dict):
            return {k: translate(v) for k, v in value.items()}
        if isinstance(value, str):
            if value in replacements:
                return replacements[value]
            prefix = row['id'] + '#'
            if value.startswith(prefix) and value[len(prefix):] in replacements:
                return prefix + replacements[value[len(prefix):]]
        return value
    # Only source-coordinate structures use local block names. Do not rewrite
    # a coincidentally equal string in the actual predicate or domain data.
    for field in ('source_clause_ids', 'source_clause_roles', 'semantic_roles'):
        if field in row:
            row[field] = translate(row[field])
    if row.get('argument', {}).get('clause_arguments'):
        for argument in row['argument']['clause_arguments']:
            for field in ('source_block_ref', 'source_clause_id'):
                if field in argument:
                    argument[field] = translate(argument[field])
    row['source_clauses'] = blocks
    pins = {b['id']: b for b in blocks}
    for relation in row.get('source_clause_roles', []):
        block = pins[relation['source_block_id']]
        relation.update(source_clause_id=row['id'] + '#' + block['id'], source_block_sha256=block['sha256'],
                        source_byte_start=block['byte_start'], source_byte_end=block['byte_end'])
    if 'source_clause_ids' in row:
        row['source_clause_ids'] = list(dict.fromkeys(row['source_clause_ids']))
        if 'body' in pins and row['id'] + '#body' not in row['source_clause_ids']:
            row['source_clause_ids'].append(row['id'] + '#body')
    return sorted(replacements)


def add_dependency(row, target, kind='contract_application', required_when=None, binding=None):
    row.setdefault('dependencies', [])
    if target not in row['dependencies']:
        row['dependencies'].append(target)
    rel = {'id': target, 'kind': kind}
    if required_when:
        rel['required_when'] = required_when
    if binding:
        rel['binding'] = binding
    relations = row.setdefault('dependency_relations', [])
    if rel not in relations:
        relations.append(rel)


def repair_composition_acquisition(row):
    """Retain the Composition law's domain conditions at each occurrence.

    A repeated owner is still a relation occurrence. A prose grouping name does
    not encode an acquisition condition for the compiler.
    """
    domains = row['definition']['clauses'][0]['conditional_domain_owners']
    conditions = {
        'design_declarations': 'design composition',
        'complete_transition_admission_and_semantic_commit': 'consequential admission',
        'frame_relations': 'frame-governed composition',
        'typed_calculus_paths': 'a_c composition',
    }
    if set(domains) != set(conditions):
        raise ValueError('Composition domain account changed; reconcile with its source')
    for domain, when in conditions.items():
        value = domains[domain]
        if isinstance(value, dict):
            if value.get('required_when') != when:
                raise ValueError('Composition domain condition drift: ' + domain)
            continue
        domains[domain] = {'required_when': when,
                           'owners': value if isinstance(value, list) else [value]}


def repair_odd_entry_binding(row, source):
    """Keep section 19's recommendation and sufficiency judgments separate."""
    recommendation = ('The cold actor can readily recover the Product source-to-outcome semantic chain; '
                      'typed assets/nodes; public graph functions, machine-readable catalog and GTL module; '
                      'ABG/Product split; and the exact loop, dispositions and proof lane.')
    sufficient = ('The acquired local Product subjects and selected owning contracts let the actor determine '
                  'source coherence and structural-drift refusal, execution-authority containment, '
                  'observation-to-action control, replay-visible yield, outer closure with missing inner proof, '
                  'and lawful agentic traversal with deterministic artifact admission for this ODD entry.')
    recommended_result = copy.deepcopy(row['result_mapping'])
    recommended_result['bound_predicate'] = recommendation
    recommended_result['satisfied'] = 'A performed evaluation with admissible evidence establishes the stated recommended recoverability; this is not an entry-sufficiency result.'
    recommended_result['falsified'] = 'Admissible counterevidence defeats the stated recoverability predicate; this does not by itself falsify entry sufficiency.'
    recommended_result['indeterminate'] = 'Whether the actor can recover the named distinctions is unresolved without deciding counterevidence or a supported scope/basis diagnosis; this is not an entry-sufficiency result.'
    recommended_result['normative_force'] = ('This evaluates attainment of the source recommendation only when that question is selected. '
                                             'A result does not convert should into a mandatory entry prerequisite or grant an action.')
    row['predicate'] = sufficient
    row['obligations'] = [
        'Acquire the actual local Product subjects and the owning contracts selected by section 16 under the cold-start route.',
        'Claim sufficient entry only when the acquired material supports every named required determination; apply Contract application to that claim.',
        'An established unanswered required relation means the Product is not sufficiently specified for this entry; a glossary or generic rule packet cannot supply the actual subject.']
    row['permissions_exceptions'] = [
        'Readily recovering the listed distinctions is a should recommendation, retained in its own binding; its result alone does not decide entry sufficiency.',
        'The reading route does not require unrelated corpus or an unselected profile.']
    row['applicability']['when'] = 'A cold actor enters a concrete ODD Product and sufficiency of that entry is claimed or assessed.'
    row['result_mapping']['bound_predicate'] = sufficient
    row['result_mapping']['falsified'] = ('Admissible counterevidence defeats entry sufficiency, including an established unanswered required relation. '
                                        'Retain that failure even if another required relation is unresolved.')
    row['result_mapping']['indeterminate'] = ('Evidence about whether the acquired material supports a required determination is unresolved, '
                                            'without an established unanswered relation, other deciding counterevidence or a supported scope/basis diagnosis.')
    row['contract_bindings'] = [
        {'name': 'ramp_up_recommendation', 'modality': 'should',
         'applicability': 'A cold actor enters a concrete ODD Product under the declared cold-start route, whether or not entry sufficiency is claimed.',
         'predicate': recommendation, 'source_clause_ids': ['ramp_up_recommendation'],
         'assessment_when': 'The selected question assesses attainment of the recommended recoverability, separately from entry sufficiency.',
         'result_mapping': recommended_result},
        {'name': 'entry_sufficiency', 'modality': 'required_for_claim',
         'contract': 'TRANSFORMATION_LIBRARY.contract-application',
         'predicate_ref': '/predicate', 'applicability_ref': '/applicability',
         'result_mapping_ref': '/result_mapping', 'source_clause_ids': ['c2']}]
    start = source.index(b'A cold actor should readily recover', source.index(b'## 19. Ramp-Up Checklist'))
    end = source.index(b'\n\n', start)
    block = {'id': 'ramp_up_recommendation', 'sha256': digest(source[start:end]),
             'roles': ['recommendation', 'scope'], 'byte_start': start, 'byte_end': end}
    row['source_clauses'] = [c for c in row['source_clauses'] if c['id'] != block['id']] + [block]
    row['source_excerpt'] = source[start:end].decode('utf-8')
    add_dependency(row, 'FOUNDATIONS.result-algebra', kind='result_contract')


def repair_documentary_deltas(rows):
    """Reconcile the 39 changed owned bodies, rather than merely their pins."""
    changed = set()
    def take(identifier):
        changed.add(identifier)
        return rows[identifier]
    def append(identifier, field, value):
        r = take(identifier)
        if value not in r.setdefault(field, []):
            r[field].append(value)
        return r

    r = take('FOUNDATIONS.workspace-and-context')
    r['obligations'].append('Context fit and attention adequacy are distinct predicates: the execution binding declares the resource envelope and measurement boundary; bytes/tokens establish fit only for measured context. Actual use establishes adequate application of relevant material for the selected task under those conditions. Neither proves the other, and no universal attention score follows.')
    r['obligations'][3] += ' Production and invalidation of relied-on support remain recoverable.'
    r['permissions_exceptions'][2] = 'A function, component, role, conversation, status or resumption boundary alone is not an invalidator; the continuing consumer checks exact applicability.'

    r = take('FOUNDATIONS.judgment-and-authority')
    r['obligations'].append('Semantic result remains separate from authoritative construction disposition; its domain conditions are owned by Spec proportional disposition.')
    add_dependency(r, 'SPEC_METHOD.proportional-disposition', 'conditional_contract_application',
                   'an authoritative construction disposition is being interpreted or selected')
    r = take('FOUNDATIONS.orthogonal-descriptions')
    r['obligations'].append('Conformance to the declared contract, functorial preservation, semantic equivalence and computational equivalence are distinct claims. Categorical equivalence additionally requires the stated quasi-inverse and natural isomorphisms on its domain.')
    r = take('FOUNDATIONS.result-conjunction')
    r['argument']['associativity_argument'] = {
        'domain': 'The same authenticated leaf predicates and material joins, normalized disjoint effect parts, and no intermediate basis failure hidden by grouping.',
        'steps': ['Set union retains identical authenticated leaves under either grouping.',
                  'Selecting the highest applicable diagnostic in the declared precedence over those leaves gives the same result.',
                  'Normalized disjoint effect observations retain identical parts, so the stated unknown and completion conditions decide the same aggregate.'],
        'limit': 'Intermediate results retain leaves and parts; a bare verdict is insufficient. A different operator needs its own preservation/associativity demonstration.',
        'evidence_class': 'mathematical_argument_not_mechanized_theorem'}

    r = take('TRANSFORMATION_LIBRARY.acquire')
    r['obligations'][0] = 'Apply Workspace/context: bind subject, requirements, grant and destination; resolve sufficient authentic material and dependencies; reconcile stale summaries. The owner distinguishes context-fit and attention-adequacy predicates and their evidence boundaries. Capacity misfit uses the admitted finite-capacity response rule; do not omit material to fit.'
    add_dependency(r, 'FOUNDATIONS.workspace-and-context')
    for identifier in ('TRANSFORMATION_LIBRARY.composition-law', 'AXIOMATIC_CALCULUS.ac-016-typed-composition'):
        r = take(identifier)
        r['obligations'] = [o for o in r['obligations'] if not ('categorical' in o.lower() and ('demonstration' in o or 'declare domain objects' in o))]
        r['obligations'].append('A categorical claim applies the complete Foundations Orthogonal descriptions demonstration standard. Contract preservation alone establishes no category, functor, categorical equivalence or proof of those claims.')
        add_dependency(r, 'FOUNDATIONS.orthogonal-descriptions', 'conditional_contract_application', 'a categorical claim is made')

    r = take('SPEC_METHOD.spec-driven-homeostatic-methodology')
    r['obligations'].append('Categorical claims use the complete Foundations demonstration standard; ordinary contract preservation alone does not establish that claim.')
    add_dependency(r, 'FOUNDATIONS.orthogonal-descriptions', 'conditional_contract_application', 'a categorical claim is made')
    r = take('SPEC_METHOD.canonical-compression')
    r['definition'] = {'meaning': 'Derived synopsis of the selected Goals-to-realization/observation chain, WHAT/HOW separation, authority, governing meaning and lawful re-entry. Code and Events are selected software/runtime forms, not universal realization or evidence requirements.'}
    r = take('SPEC_METHOD.manifesto')
    r['obligations'].append('Realization implements decisions; code is its software binding. Observe through the selected realization and evidence contract; a log is not a universal requirement.')
    r = take('SPEC_METHOD.spec-drivenness-litmus')
    r['predicate'] = r['predicate'].replace('code behavior has authority', 'realized behavior has authority')
    r['obligations'].append('The Product selects the realization and observation forms; Code/Events apply where that binding selects them.')
    r = take('SPEC_METHOD.reconstruction-litmus')
    r['predicate'] = r['predicate'].replace('Code from Requirements+Design', 'the selected realization from Requirements+Design')
    r['permissions_exceptions'][0] = 'Different lawful designs and realizations may conform; software codebases are one realization case.'
    r = take('SPEC_METHOD.method')
    r['obligations'][0] = r['obligations'][0].replace('retained code', 'retained implementation')
    r['obligations'][1] = r['obligations'][1].replace('retained code', 'retained implementation').replace('design/code/tests', 'design/implementation/applicable proof')
    r['obligations'][2] = 'Bootstrap resolves the Product definition, exact install, declared entrypoint and current Goals; derive bound Intent/Product and the sole live requirement authority at the Product-selected what locations. Individual requirements or grouped families are permitted; requirements/ is a default convention. Record major ambiguity before downstream realization.'
    r['obligations'] += ['Construct the selected realization under its design/execution binding and reconcile realized behavior with applicable proof before promotion or closure; Code is the software case.',
                         'Observe realized state through declared evidence sources and compare against requirements. Events/projection/delta apply where selected; adequate direct observation remains lawful.']
    for rel in r['dependency_relations']:
        if rel['id'] == 'DESIGN_MODULE_METHOD.proportional-design-sequencing':
            rel['required_when'] = 'Design Method applies to the affected realization'
    r = append('SPEC_METHOD.consistency-gate-rule', 'obligations',
               'Conjoin the actually required consistency predicates once at their declared scope; duplicate invocations do not create independent evidence or another authority.')
    r = append('SPEC_METHOD.ambiguity-governance-rule', 'obligations',
               'An established hard-stop prerequisite violation falsifies the admissibility predicate. It does not by itself falsify the intended outcome: retain invalid_basis for an unusable intended-outcome basis or indeterminate for unacquired material, preserving independently admissible outcome counterevidence and actual effects.')
    r = take('SPEC_METHOD.what-how-and-work-carriers')
    r['obligations'][1] = 'Declare material context, time, memory, communication, human-effort and spend units and measurement boundary in the execution binding. Apply Foundations Workspace/context for distinct context-fit and attention-adequacy predicates and their evidence boundaries.'
    r['obligations'].append('Retain applicable human decisions, authority, independence, failure and recovery conditions when choosing a realization; broader executor choices do not silently remove those obligations.')
    add_dependency(r, 'FOUNDATIONS.workspace-and-context')

    r = take('DESIGN_MODULE_METHOD.governing-relations')
    r['applicability'] = {'when': 'Generic UP-016–019 and module-derived unit-proof law applies where Spec selects the declared design/proof relation. Remaining realization-profile policy applies only at the boundary adopting it and under its stated conditions and exceptions.',
        'unknown': 'Undecided applicability is retained before dependent reliance; reading generic law does not establish optional-profile adoption.'}
    r['obligations'].append('Keep generic design-contract law separate from adopted Ontology, Prime/IACS, functional-realization, diagram and language policies; selecting a generic relation does not adopt the remaining profile.')
    generic_design = {
        'transformation-admission-completeness-stdo-up-016': 'a consequential entity-transition admission relation is designed',
        'bounded-frame-conservation-stdo-up-017': 'an action is proposed inside the causally affected governing relation M(B)',
        'invariant-reconstruction-sufficiency-stdo-up-018': 'reconstruction or bounded action conformance is claimed',
        'computational-realization-projection-stdo-up-019': 'a material semantic or algorithmic realization relation is claimed, including method execution materially affecting the supported outcome under Spec UP-014',
        '6a-design-to-module-to-implementation-unit-tests-evidence-route': 'a new or materially changed realization boundary claims the module-derived proof relation',
        '6b-module-derived-unit-test-rule': 'a module is implemented or its unit-proof or closure relation is claimed',
    }
    for anchor, trigger in generic_design.items():
        r = take('DESIGN_MODULE_METHOD.' + anchor)
        r['applicability']['when'] = 'This declared design/proof law is selected by Spec and ' + trigger + '. Optional realization-profile policies remain conditional on their own adoption and scope.'
        r['applicability']['unknown'] = 'Undecided selection, claim scope or material trigger remains unresolved before dependent reliance; generic-law selection does not imply optional-profile adoption.'
        r['permissions_exceptions'].append('Selecting the generic design/proof relation does not adopt the remaining Ontology, Prime/IACS, functional-realization, diagram or language policies; their own conditions and exceptions remain.')
    r = append('DESIGN_MODULE_METHOD.4-functional-bias-without-language-mandate', 'obligations', 'Each function has one clear owner and a declared responsibility; admission, semantics and effects do not mix behind a convenience helper.')
    r = take('DESIGN_MODULE_METHOD.bounded-frame-conservation-stdo-up-017')
    r['obligations'] = [o.replace('violates, duplicates or silently reinterprets', 'violates or silently reinterprets') for o in r.get('obligations', [])]
    r['obligations'][1] = 'Do not violate or silently reinterpret an affected governing invariant; duplication requires UP-018 action classification and explicit disposition.'
    r['obligations'].append('Duplication uses UP-018 action classification and explicit disposition; an undisposed duplicate cannot establish preservation.')
    add_dependency(r, 'DESIGN_MODULE_METHOD.invariant-reconstruction-sufficiency-stdo-up-018')
    r = take('DESIGN_MODULE_METHOD.invariant-reconstruction-sufficiency-stdo-up-018')
    r['obligations'] = [o.replace('Test named cases', 'Where boundary sufficiency is tested, use named cases') for o in r.get('obligations', [])]
    r['permissions_exceptions'].append('The private-history-withheld discriminator is required where boundary sufficiency is tested; it is not an extra universally executed artifact or stage.')

    r = take('RELEASE_METHOD.release-publication-context')
    r['definition'] = {'meaning': 'urn:stdo:bounded-context:release-publication owns identities/transitions for qualifying, publishing and selecting released cuts, including the selector/adoption protocol under the complete STDO basis. Consumer Product meaning and its decision to adopt remain at the consumer governing authority under Spec.'}
    r['obligations'] = ['Do not assign the consumer Product meaning or decision to adopt to this publication context. Publication and selector/adoption protocol are owned here.']
    r['argument']['policy_choices'] = ['Release owns immutable publication and selector/adoption protocol; consumer governing authority owns the decision to adopt.']
    r = take('RELEASE_METHOD.exact-cut-qualification')
    r['predicate'] = r['predicate'].replace('evidence/verdict/gaps', 'evidence subjects, assessment results, owner decisions and unresolved gaps')
    r['obligations'][2] = 'Qualifying-byte changes retain the old assessment result on the old RC and require a higher RC; owner acceptance does not move the selector or create a final carrier.'
    r['obligations'].append('Apply core result/conjunction law for missing reasons, absent judgments, actual performance and effects; release labels define no alternative rule.')
    add_dependency(r, 'FOUNDATIONS.result-conjunction')
    r = take('IDENTITY_METHOD.governing-relations')
    r['argument']['premises'] = ['F2', 'F3', 'F4', 'F6']
    r['argument']['conditional_consequence'] = 'Interpreted identity, current subject, composition and evidence/authority require a consumer to distinguish a subject from its representation and preserve admitted authority through composition, given the declared kind/owner/lifecycle.'

    for identifier in ('REFERENCE_FRAME_METHOD.minimal-frame-activation-binding', 'REFERENCE_FRAME_METHOD.minimal-frame-declaration', 'CARRIER.standards.templates.PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md'):
        r = take(identifier)
        r['obligations'].append('The selected evaluation uses the applicable core-result predicate or declared refinement, not an independently selected second result algebra.')
    r = rows['CARRIER.standards.templates.PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md']
    r['obligations'].append('Priority/promotion assessment uses a sufficient bounded Product view and current mandate, acquiring material dependencies as needed; completeness of the entire corpus is not the context condition.')
    r = take('STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation')
    r['obligations'][2] = 'A harness, fixture, expected-value builder, proof script, assurance evaluator or Reviewer cannot construct parallel owner state from raw payloads, events, logs, filenames, labels or implementation fragments.'
    r = append('STDO_REFERENCE_FRAME_BASELINE.profile-qualification', 'obligations', 'The Executive trial consumes exact technical triage with the sufficient bounded delivery view and current MVP/release mandate, preserving severity, priority, frame result and promotion-boundary effect.')
    r = append('STDO_REFERENCE_FRAME_BASELINE.closure', 'obligations', 'This profile supplies no new execution authority, local constitution, actor topology, runtime or universal completeness claim; selected configuration/effects stay within existing grants.')
    r = append('TICKET_METHOD.bounded-context-term-binding', 'obligations', 'Repository, filesystem, implementation, tool, organization, local terminology and reviewer familiarity cannot supply an undeclared semantic owner or substitute for the actual bounded context.')

    r = take('TRAVERSAL_OCCURRENCE_PROFILE.closed-constraint-judgment-residual-and-stop-kinds')
    for constraint in r['definition']['constraints']:
        if constraint['kind'] == 'transition_subject_complete':
            constraint['falsified_mapping'] = 'refused plus refusal on completeness; intended outcome is invalid_basis when the incomplete subject is unusable, or indeterminate when material is merely unacquired'
    r['definition']['transition_subject_predicates'] = {
        'prerequisite': 'transition_subject_complete; demonstrated failure retains its counterexample and original refused decision',
        'intended_outcome': 'invalid_basis when the incomplete subject is unusable for this evaluation; indeterminate with unobserved_subject_state when material is merely unacquired',
        'preservation': 'Neither diagnosis proves outcome falsity or no effects. Separately admissible outcome counterevidence retains its predicate, valid basis and citations; actual effects retain their observations.'}
    r['obligations'].append('Keep subject completeness and intended-outcome predicates distinct, including original refusal, independent counterevidence and actual effects.')
    r = take('WORLD_MODEL_METHOD.composition-law')
    r['obligations'].append('Do not build one central monolith first.')
    r['permissions_exceptions'][0] = 'Detailed mesh topology may remain Product-local while the line develops. Method mesh law should be ratified only when the reusable node/edge model is stable; stability grants no ratification authority.'
    r = take('WORLD_MODEL_METHOD.projection-law')
    r['applicability']['trigger'] = 'Relying on a world-model projection for a declared source-to-consumer fidelity claim; the general should-traceability preference remains separately stated.'
    r['permissions_exceptions'].append('All world-model projections should remain traceable to governing objects, evidence, treatments, covariance edges, adjoint mappings and applicable temporal references. This general should is not an unconditional must-fidelity verdict.')
    for rel in r['dependency_relations']:
        if rel['id'] == 'TRANSFORMATION_LIBRARY.faithful-projection' and rel['kind'] == 'contract_application':
            rel['required_when'] = 'a declared source-to-consumer fidelity claim relies on this projection'
    r = take('CARRIER.plugins.spec.references.PRODUCT_BASIS.md')
    r['obligations'] += ['Resolve workflow member routes relative to the verified immutable basis URI using stdo resolve on the member URI without its fragment; read the returned installed member and then its exact heading.',
                         'Check membership and digest against the verified manifest. A missing member/heading remains unavailable; any permitted owning-source alternative stays on that basis, never a nearby checkout/plugin/newer cut.',
                         'An explicitly selected source assessment candidate has a separate frozen package identity/member inventory and root. It does not replace the installed governing method basis; issued cuts need their own verified routes.']
    add_dependency(r, 'GLOSSARY_GUIDE.acquisition-use')
    r = take('CARRIER.plugins.spec.skills.stdo-work.SKILL.md')
    r['obligations'] += ['Use Product Basis Selection Acquire A Member From The Selected Basis for every member/section route; the verified basis root is independent of plugin/current-directory layout.',
                         'Select the responsibility route from the verified standards index and accepted frame basis: work/recovery, triage/carrier, constitutional derivation or relevant exact owners. Missing curated views permit only available exact owners on that same selected basis.',
                         'An interpretation projection requires its exact document-source inventory and encoding/checker basis; unresolved conditions re-enter named owners. Structural validity is neither permission nor fidelity, and an assessment source package remains distinct from the installed governing method.']
    add_dependency(r, 'CARRIER.plugins.spec.references.PRODUCT_BASIS.md')
    return changed


def family_argument_routes(rows, source, routes):
    """Bind actual source-table arguments to their declared consumer scopes.

    Table cells remain source-owned data. They are not a second set of predicate
    laws and are not permission to load every named consumer of the family.
    Existing section-specific arguments take precedence over family fallbacks.
    """
    changed, bindings, grouped, consumer_arguments = set(), [], {}, {}
    for route in routes['argument_routes']:
        member, anchor = route['member'], route['argument_heading']
        path = 'standards/' + member + '.md'
        lines = source[path].decode().splitlines()
        raw = lines[route['source_row_line'] - 1]
        if digest(raw.encode()) != route['source_row_sha256']:
            raise ValueError('Source argument row changed: ' + route['row_label'])
        cells = [c.strip() for c in raw.strip().strip('|').split('|')]
        if len(cells) != 3:
            raise ValueError('Unrecognized source argument table: ' + route['row_label'])
        record = {'family': route['row_label'], 'declared_consumer_scope': cells[0],
                  'premises': route['premises'], 'conditional_consequence': cells[1],
                  'additional_policy_and_owner': cells[2],
                  'source_row': {'path': path, 'anchor': anchor, 'line': route['source_row_line'],
                                 'sha256': route['source_row_sha256']},
                  'source_refs': [member + '.' + anchor]}
        grouped.setdefault(member + '.' + anchor, []).append(record)
        selected = set(route['existing_determination_ids'])
        label = route['row_label']
        if member == 'REFERENCE_FRAME_METHOD' and not selected:
            numbers = {
                'Evaluation boundary, acquisition and compression': {1, 2, 3, 4, 5, 13, 14, 17},
                'Authority and overlapping meaning': {6, 7, 8},
                'Configuration and material combination': {9, 10, 11, 16},
                'Closed results and uncertainty': {12, 15},
            }.get(label, set())
            selected = {identifier for identifier in rows if identifier.startswith(member + '.rf-')
                        and int(identifier.split('.rf-')[1][:3]) in numbers}
        elif member == 'ODD_METHOD':
            prefixes = {
                'Typed graph and Product boundaries': ['4-', '5-', '6-', '7-', '8-', '111-', '112-', '112a-', '113-', '114-', '116-', '118-'],
                'Observation, lineage and recovery': ['115-', '115a-', '115b-', '115c-'],
                'Closure across refinement': ['119-'],
                'Process and authority-path proof': ['9-', '117-', '117a-', '117b-', '12-', '13-', '14-', '15-', '16-'],
                'Invocation and acquisition': ['17-', '18-', '19-'],
            }.get(label, [])
            selected |= {identifier for identifier in rows if any(identifier.startswith(member + '.' + p) for p in prefixes)}
            # A0..A16 are source-owned clauses of this one immediate heading,
            # not independent invented determinations. Retain each scoped row.
            if any(token in route['consumer_scope_as_written'] for token in ('A0', 'A1,', 'A2,', 'A4,', 'A6,')):
                selected.add('ODD_METHOD.115d-constructive-evaluation-and-yield-loop')
        elif member == 'DESIGN_MODULE_METHOD':
            selectors = {
                'Ontology, constructability and admission': (['up-002', 'up-016'], ['4b-', '5e-']),
                'Prime, IACS and boundary cost': (['up-003', 'up-005'], ['5-', '5a-', '5b-', '5c-']),
                'Affected frames and reconstruction': (['up-017', 'up-018'], []),
                'Computational realization and foundation selection': (['up-019', 'up-023'], []),
                'Functional realization and seams': ([], ['3-', '3a-', '3b-', '4-', '4a-', '7-', '8-', '9-', '10-', '11-', '11a-', '12-', '13-']),
                'Module proof, lifecycle and review': ([], ['5d-', '6a-', '6b-', '6c-', '11b-', '11c-', '11d-', '14-', '14a-']),
            }
            suffixes, prefixes = selectors[label]
            selected |= {identifier for identifier in rows if identifier.startswith(member + '.') and
                         (any(identifier.endswith(s) for s in suffixes) or any(identifier.startswith(member + '.' + p) for p in prefixes))}
        # Bind every real local subheading of the listed owner, not similarly
        # named fields or headings nested in fenced examples/templates.
        units = list(heading_units(source[path]).values())
        roots = (set(route['explicit_consumer_roots']) if route['explicit_consumer_roots'] else
                 {rows[identifier]['owner']['anchor'] for identifier in selected if identifier in rows})
        root_units = [unit for unit in units if unit['anchor'] in roots]
        for index, unit in enumerate(units):
            if unit['anchor'] not in roots:
                continue
            following = next((u for u in units[index + 1:] if u['level'] <= unit['level']), None)
            end = following['byte_start'] if following else len(source[path])
            selected |= {identifier for identifier, row in rows.items() if row['owner']['path'] == path
                         and row['owner'].get('anchor') in {u['anchor'] for u in units if unit['byte_start'] < u['byte_start'] < end}}
        if not selected:
            raise ValueError('No actual account consumers for source family: ' + member + '/' + label)
        for identifier in sorted(selected):
            if identifier not in rows:
                raise ValueError('Source return names missing determination: ' + identifier)
            r = rows[identifier]
            body = heading_units(source[path])[r['owner']['anchor']]['body'].decode()
            local_premises = re.search(r'\bF[1-6]\b', body) is not None
            own = next(u for u in units if u['anchor'] == r['owner']['anchor'])
            ancestors = [u for u in root_units if u['byte_start'] <= own['byte_start']
                         and not any(v['byte_start'] <= own['byte_start'] and v['byte_start'] > u['byte_start']
                                     and v['level'] <= u['level'] for v in units)]
            distance = min((own['level'] - u['level'] for u in ancestors), default=0)
            consumer_arguments.setdefault(identifier, []).append((distance, copy.deepcopy(record), local_premises))
    for identifier, candidates in consumer_arguments.items():
        nearest = min(c[0] for c in candidates)
        selected = [c for c in candidates if c[0] == nearest]
        r = rows[identifier]
        entries = [c[1] for c in selected]
        r['argument']['source_family_arguments'] = entries
        # More-specific table rows beat a broader containing heading, just as
        # an explicit section argument beats a table fallback. For example
        # UP-017 does not inherit optional Ontology policy merely because it is
        # printed under section 4B; its exact argument is the affected-frame row.
        if not selected[0][2]:
            r['argument']['premises'] = sorted({p for entry in entries for p in entry['premises']})
            r['argument']['conditional_consequence'] = ('Apply the exact source-family argument(s) below only in their declared consumer scope. Their consequence does not imply their additional chosen policies.')
            r['argument']['policy_choices'] = [entry['additional_policy_and_owner'] for entry in entries]
        changed.add(identifier)
        for _, entry, local in selected:
            bindings.append({'consumer': identifier,
                             'family_owner': entry['source_refs'][0],
                             'row_sha256': entry['source_row']['sha256'],
                             'local_argument_retained': local})
    for identifier, records in grouped.items():
        member, anchor = identifier.split('.', 1); path = 'standards/' + member + '.md'
        if identifier not in rows:
            unit = heading_units(source[path])[anchor]
            rows[identifier] = {'id': identifier, 'family': member + ' source argument routes',
                'owner': make_owner(path, unit, source[path]), 'supporting_sources': [],
                'representation_kind': 'definition_data', 'predicate': None,
                'definition': {}, 'applicability': 'The explicitly listed source families and consumers, retaining more specific local arguments.',
                'obligations': ['Retain each chosen policy and its owner separately from premises and conditional consequences.'],
                'permissions_exceptions': ['A family route does not make every consumer an acquisition or execution prerequisite.'],
                'dependencies': ['FOUNDATIONS.foundational-commitments'],
                'result_mapping': {'kind': 'source_argument_data', 'conditions': 'These are the source-owned arguments and choices, not a verdict or acceptance. A separate assessment binds its predicate and the core result contract.', 'owner_refs': ['FOUNDATIONS.result-algebra']},
                'argument': {'premises': [], 'conditional_consequence': 'The source declares conditional arguments under specific premises; the separate policy choices are not derived merely from finite capacity.', 'policy_choices': [], 'source_refs': [identifier]},
                'inputs': [], 'coverage_standing': 'bounded_author_binding', 'interpretation_standing': 'bounded_semantic_binding'}
        r = rows[identifier]
        if not isinstance(r.get('definition'), dict):
            r['definition'] = {'source_family_arguments': records}
        else:
            r['definition']['source_family_arguments'] = records
        r['argument']['source_table_scope'] = 'Each exact row applies only to its named consumer scope; local source-specific arguments remain more specific.'
        if identifier == 'REFERENCE_FRAME_METHOD.reference-frame-laws':
            r['applicability'] = 'The listed RF laws and the engagement, conjunction, discovery and qualification procedures in their actual scopes.'
        changed.add(identifier)

    # Two reviewed specific counterexamples take precedence over all table
    # fallbacks. These source paragraphs are unchanged; the old account was wrong.
    for identifier, premises, consequence, choices in [
        ('TICKET_METHOD.core-model', ['F1', 'F3', 'F5', 'F6'],
         'For work whose obligations survive an activation, continued reliance requires recoverable identity, state and authority; carrier names/states cannot supply a grant.',
         ['Ticket chooses Goals, tickets, sprints, run contracts, the smallest-carrier rule and UP-006 milestone truth; Product and ticket-state authorities bind them.']),
        ('SPEC_METHOD.complete-enclosing-relation-admission-stdo-up-021', ['F2', 'F3', 'F4', 'F6'],
         'With a consequential transition and actual admission owners, local evidence cannot establish an unsupported enclosing join or grant; the admission specialization applies the shared relation.',
         ['UP-021 adds exact basis, trust-boundary validation and complete-or-none semantic commit. Design owns supported forms and declared coherent compositions.']),
        ('SPEC_METHOD.ambiguity-governance-rule', ['F1', 'F2', 'F5', 'F6'],
         'A material unresolved interpretation cannot become an established result or permission; apply Contract application to the affected claim.',
         ['Spec chooses mandatory detection, lifecycle sufficiency and the stated hard stops. Product risk policy chooses which remaining ambiguities may be carried, resolved or escalated.'])]:
        r = rows[identifier]
        r['argument'].update(premises=premises, conditional_consequence=consequence, policy_choices=choices)
        changed.add(identifier)
    return changed, bindings


def repair_semantics(rows, source):
    """Named source counterexamples; no broad result or policy remapping."""
    changed = set()
    def row(identifier):
        changed.add(identifier)
        return rows[identifier]

    r = row('AXIOMATIC_CALCULUS.ac-009-residual-conservation')
    r['predicate'] = 'Every material uncertainty, omission, translation loss, unresolved boundary or unproven relation remains in X until an authorized disposition creates an exact successor model. Absence from a projection is not resolution.'
    r['obligations'] = [r['predicate']]
    r['permissions_exceptions'] = []
    r['argument']['policy_choices'] = []
    r['argument']['source_consequences'] = ['Absence from a projection is not resolution.']

    r = row('RELEASE_METHOD.open-questions')
    r['representation_kind'] = 'definition_data'
    r['interpretation_standing'] = 'source_owned_unresolved_choices'
    r['definition'] = {'questions': ['What exact qualification bundle is mandatory for each Product class?',
                                    'What version-line compatibility rule requires a new <version> rather than a higher RC ordinal?'],
                       'standing': 'unresolved_source_choices',
                       'scope': 'The shared method has not settled these choices. An actual Product may supply its own authorized policy; this does not settle the shared question or excuse a missing required decision.'}
    r['argument'] = {'premises': [], 'conditional_consequence': 'The owner states questions rather than settled policy. Any claim depending on a particular answer needs that answer from its competent owner.',
                     'policy_choices': [], 'source_refs': [r['id']]}
    r['source_residuals'] = [
        {'id': 'qualification-bundle', 'kind': 'unresolved', 'detail': r['definition']['questions'][0],
         'dependent_claim': 'A claim that this shared method fixes one exact mandatory qualification bundle for the selected Product class; obtain the competent Product/class policy before relying on such an answer.'},
        {'id': 'version-line-compatibility', 'kind': 'unresolved', 'detail': r['definition']['questions'][1],
         'dependent_claim': 'A claim that this shared question supplies the compatibility boundary choosing a new version line over an RC ordinal; obtain the competent version policy before the dependent decision.'}]

    r = row('TICKET_METHOD.multi-build-tenant-review-rule')
    r['applicability'] = 'Review of backlog/active tickets when the same work item is processed across multiple build tenants.'
    r['predicate'] = 'The review checks that each tenant has its own suffixed ticket naming build_tenant, its own proof surface and closure law; sibling green does not discharge closure; reopen, repricing and successor work stay tenant-local unless the upstream source/product/design ticket itself must change.'
    r['obligations'] = [r['predicate']]
    r['permissions_exceptions'] = ['Upstream source/product/design ticket change is the explicit exception to tenant-local reopening, repricing and successor work.']

    r = row('TICKET_METHOD.future-extensions')
    r['obligations'] = ['The durable local-file model remains the default and must remain valid when selected.',
        'Another carrier need not reproduce its folders; it must preserve the same ticket authority and refusal laws.']
    r['permissions_exceptions'] = ['The listed boards, dependency checks, links, external sync and message-board integration are possible extensions, not mandatory adoption.']
    r['result_mapping']['conditions'] = 'Extension possibilities remain data. Assess the separately stated preservation predicate when a carrier is selected; retaining the local-file default and authority/refusal laws is mandatory in its declared scope.'

    r = row('WORLD_MODEL_METHOD.6-bound')
    r['argument']['additional_policy'] = ['Reject schema-first modeling and vocabulary-cluster modeling. Define local boundaries in terms of function, authority, state and adjacency.']

    r = row('IDENTITY_METHOD.2-uniqueness-law')
    r['obligations'] = list(dict.fromkeys(r.get('obligations', []) +
        ['Serialization must preserve enough hierarchy to prevent accidental collision.']))

    r = row('CARRIER.plugins.spec.skills.stdo-review.SKILL.md')
    r['obligations'] = list(dict.fromkeys(r.get('obligations', []) + [
        'Read the frozen subject and governing source; do not use the Worker summary as evidence.',
        'Bind the threat model and applicable independent review responsibility to the actual subject.',
        'Distinguish a repair within the existing governing contract from a change that requires upstream repricing.']))

    r = row('TRANSFORMATION_LIBRARY.workrecovery-specialization')
    executive = 'STDO_REFERENCE_FRAME_BASELINE.executive-attention-evaluation-and-action'
    for step in r['argument'].get('clause_arguments', [])[0].get('conditional_steps', []):
        if executive in step.get('contracts', []):
            step['contracts'].remove(executive)
            step['conditional_contracts'] = [{'id': executive, 'required_when': 'Baseline coordination is adopted and lawfully activated',
                                             'binding': 'Optional owner-qualified coordination; the generic recovery contract grants no Baseline role.'}]
    r = row('SPEC_METHOD.proportional-method-and-delivery-stdo-up-014')
    for rel in r['dependency_relations']:
        if rel['id'] == 'DESIGN_MODULE_METHOD.computational-realization-projection-stdo-up-019':
            rel['required_when'] = 'method execution materially affects the supported outcome'

    for r in rows.values():
        argument = r.get('argument', {})
        if argument.get('standing') == 'source_owned_policy_with_conditional_argument_route':
            if argument.get('policy_choices') == r.get('permissions_exceptions'):
                argument['policy_choices'] = []
                argument['policy_owner_rule'] = 'The referenced source argument identifies separately owned choices; a permission, exception or corollary in the local row is not thereby an additional policy choice.'
                changed.add(r['id'])
    return changed


def new_glossary_rows(source):
    path = 'standards/GLOSSARY_GUIDE.md'; units = heading_units(source[path])
    result = []
    for anchor, predicate, obligations in [
        ('index-contract', 'Each index row resolves its bounded-context identity and exact owning clause in the selected complete basis; an invalid route has no fallback authority.',
         ['Equal spelling, proximity and index membership confer no identity, inheritance, import, equivalence or authority.',
          'An unresolved context or owning clause invalidates the row; the index cannot repair it.']),
        ('acquisition-use', 'Resolve the locator in its exact selected basis and scope, using bounded-context semantic resolution before concluding ambiguity; report the actual route-resolution predicate through the core result with its reason.',
         ['Acquire the material owning clause; irrelevant members are not a condition of resolution.',
          'Resolution is satisfied; established invalidity or demonstrated lack of a required unique owner falsifies route resolution.',
          'Partial acquisition or undecided ambiguity is indeterminate; unusable basis is invalid_basis; a route outside evaluation scope is out_of_frame.',
          'Missing reasons follow the core rule; no route-resolution outcome is semantic acceptance.'])]:
        result.append({'id': 'GLOSSARY_GUIDE.' + anchor, 'family': 'Glossary acquisition',
            'owner': make_owner(path, units[anchor], source[path]), 'supporting_sources': [],
            'representation_kind': 'constraint', 'applicability': 'Using the glossary as a locator in a selected complete STDO basis.',
            'predicate': predicate, 'definition': None, 'obligations': obligations, 'permissions_exceptions': [],
            'dependencies': ['SPEC_METHOD.bounded-context-semantic-resolution', 'FOUNDATIONS.workspace-and-context', 'FOUNDATIONS.result-algebra'],
            'dependency_relations': [{'id': i, 'kind': 'contract_application'} for i in
                ['SPEC_METHOD.bounded-context-semantic-resolution', 'FOUNDATIONS.workspace-and-context', 'FOUNDATIONS.result-algebra']],
            'result_mapping': {'kind': 'predicate_result', 'owner_refs': ['FOUNDATIONS.result-algebra'],
                'conditions': 'The retrieval predicate has the original route outcome and reason; neither route acquisition nor a satisfied retrieval result grants meaning acceptance.'},
            'argument': {'premises': ['F2', 'F3', 'F5'], 'conditional_consequence': 'Interpreted names need exact scoped owners and sufficient bounded acquisition; these premises do not supply a missing route or source meaning.',
                'policy_choices': ['The guide selects the glossary locator convention and its source-owned retrieval contract.'],
                'source_refs': ['GLOSSARY_GUIDE.acquisition-use', 'FOUNDATIONS.foundational-commitments']},
            'inputs': [{'kind': 'task', 'description': 'The occurrence, selected complete basis, actual route and acquisition observations.',
                        'required_when': 'resolving a route', 'standing': 'external_required'}],
            'coverage_standing': 'bounded_author_binding', 'interpretation_standing': 'bounded_semantic_binding'})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    resolved = subprocess.check_output(['git', 'rev-parse', args.source_commit + '^{commit}'], cwd=REPO, text=True).strip()
    if resolved != args.source_commit:
        raise ValueError('The full immutable documentary commit is required')
    if resolved != DOCUMENTARY:
        raise ValueError('This repair is authored for the admitted documentary freeze only')
    original = git_bytes(PREIMAGE, ACCOUNT_PATH)
    account = json.loads(original); rows = {r['id']: copy.deepcopy(r) for r in account['determinations']}
    paths = {s['path'] for r in rows.values() for s in [r['owner'], *r.get('supporting_sources', [])]} | {'standards/GLOSSARY_GUIDE.md'}
    source, old_source = {}, {}
    for path in sorted(paths):
        relative = str((PACKAGE / path).relative_to(REPO))
        source[path] = git_bytes(resolved, relative)
        old_source[path] = git_bytes(PREIMAGE, relative)
        if (PACKAGE / path).read_bytes() != source[path]:
            raise ValueError('Documentary freeze differs from working subject: ' + path)
    changed = repair_semantics(rows, source)
    for row in new_glossary_rows(source):
        rows[row['id']] = row; changed.add(row['id'])
    changed |= repair_documentary_deltas(rows)
    routes = json.loads(ROUTES_PATH.read_text())
    frozen_routes = git_bytes(DOCUMENTARY, str(ROUTES_PATH.relative_to(REPO)))
    if packed(routes) != packed(json.loads(frozen_routes)):
        raise ValueError('Source return route manifest differs from documentary freeze')
    for pin in routes['source_pins']:
        path = pin['path']
        if path.startswith('successor/'):
            path = path[len('successor/'):]
        if path not in source or digest(source[path]) != pin['sha256']:
            raise ValueError('Source Writer pin differs: ' + path)
    family_changed, family_bindings = family_argument_routes(rows, source, routes)
    changed |= family_changed
    repinned = []
    coarsened_roles = []
    for row in rows.values():
        path, anchor = row['owner']['path'], row['owner'].get('anchor', '')
        unit = heading_units(source[path]).get(anchor) if anchor else None
        if anchor and unit is None:
            raise ValueError('Required owner heading disappeared: ' + row['id'])
        previous_owner = row['owner']
        row['owner'] = make_owner(path, unit, source[path])
        remapped = remap_blocks(row, old_source[path], source[path], unit)
        if 'owner_body_sha256' in row:
            row['owner_body_sha256'] = row['owner']['body_sha256']
        if 'source_member_sha256' in row:
            row['source_member_sha256'] = digest(source[path])
        # Replaced semantic structures cannot retain nonexistent old leaf
        # coordinates. Keep their exact source span, explicitly widen only the
        # representation pointer to the nearest extant object, and report it.
        for relation in row.get('source_clause_roles', []):
            for binding in relation['represented_at']:
                pointer = binding['pointer']
                parts = pointer.strip('/').split('/')
                value, valid = row, []
                for part in parts:
                    key = part.replace('~1', '/').replace('~0', '~')
                    try:
                        value = value[int(key)] if isinstance(value, list) else value[key]
                        valid.append(part)
                    except (KeyError, IndexError, ValueError, TypeError):
                        break
                if len(valid) != len(parts):
                    if not valid:
                        raise ValueError('No surviving semantic parent for ' + row['id'] + pointer)
                    binding['pointer'] = '/' + '/'.join(valid)
                    coarsened_roles.append({'id': row['id'], 'previous_pointer': pointer,
                                            'pointer': binding['pointer'], 'source_block': relation['source_block_id']})
        for support in row.get('supporting_sources', []):
            support_path, support_anchor = support['path'], support.get('anchor', '')
            support_unit = heading_units(source[support_path]).get(support_anchor) if support_anchor else None
            support.update(make_owner(support_path, support_unit, source[support_path]))
            for field in ('member_sha256', 'sha256'):
                if field in support:
                    support[field] = digest(source[support_path])
        if previous_owner['body_sha256'] != row['owner']['body_sha256'] or remapped:
            repinned.append({'id': row['id'], 'previous_body_sha256': previous_owner['body_sha256'],
                             'body_sha256': row['owner']['body_sha256'], 'coarsened_block_routes': remapped})
    # Bind the two current section-19 paragraphs after historical block remapping.
    # Fresh block coordinates must never be interpreted against the old source.
    repair_odd_entry_binding(rows['ODD_METHOD.19-ramp-up-checklist'], source['standards/ODD_METHOD.md'])
    changed.add('ODD_METHOD.19-ramp-up-checklist')
    repair_composition_acquisition(rows['TRANSFORMATION_LIBRARY.composition-law'])
    changed.add('TRANSFORMATION_LIBRARY.composition-law')
    # Every changed meaning needs an authored repair or a named reviewed
    # preservation decision. This guard is completed from the Source return.
    pending = [r['id'] for r in repinned if r['id'] not in changed]
    if pending:
        raise ValueError('Changed source bodies await source-return reconciliation: ' + ', '.join(pending))
    account['determinations'] = [rows[key] for key in sorted(rows)]
    account['subject'].update(source_commit=resolved, source_preimage=PREIMAGE,
        common_input=build.COMMON_INPUT, activation='I3-R3-INTERPRETATION', activation_commit='0b02eaf8b7a7c9970f0ddefbe194fee6b4d4a6cf')
    pins = {pin['path']: pin for pin in account['source_members']}
    for path, raw in source.items():
        pins[path] = {'path': path, 'bytes': len(raw), 'sha256': digest(raw)}
    account['source_members'] = [pins[path] for path in sorted(pins)]
    account['coverage']['source_units'] = len(rows)
    account['coverage']['bounded_bindings'] = sorted(k for k, row in rows.items() if row['representation_kind'] != 'non_deciding_locator')
    account['coverage']['owner_partition'] = [{'owner_path': path, 'binding_ids': sorted(k for k, row in rows.items() if row['owner']['path'] == path)}
                                             for path in sorted(pins)]
    account['coverage']['source_bound_residuals'] = [r['id'] for r in rows.values() if r.get('source_residuals')]
    for entry in account['coverage']['outside_raw_standard_account']:
        relative = str((PACKAGE / entry['path']).relative_to(REPO))
        raw = git_bytes(resolved, relative)
        if (PACKAGE / entry['path']).read_bytes() != raw:
            raise ValueError('Documentary view differs from freeze: ' + entry['path'])
        entry.update(bytes=len(raw), sha256=digest(raw))
        if entry['path'] == 'standards/GLOSSARY_GUIDE.md':
            entry['kind'] = 'owned_acquisition_constraints_and_locator_index'
            entry['represented_ids'] = ['GLOSSARY_GUIDE.index-contract', 'GLOSSARY_GUIDE.acquisition-use']
    current, exclusions = build.semantic_projection(account)
    build.validate_account(current)
    report = {'valid': True, 'preimage_commit': PREIMAGE, 'preimage_account_sha256': digest(original),
              'document_source_commit': resolved, 'common_input': build.COMMON_INPUT,
              'semantic_repairs': sorted(changed), 'repinned_bodies': repinned,
              'source_family_bindings': family_bindings, 'coarsened_semantic_pointers': coarsened_roles,
              'source_units': len(rows), 'source_residual_units': account['coverage']['source_bound_residuals'],
              'account_sha256': digest(packed(account)),
              'limits': ['Authored source reconciliation, not independent acceptance or completeness.',
                         'Changed paragraph routes may be conservatively widened to their exact current owned body; original coordinates remain in the frozen preimage.']}
    if args.write:
        (Q / 'DETERMINATIONS.json').write_bytes(packed(account))
        (HERE / 'ACCOUNT_REPAIR.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
