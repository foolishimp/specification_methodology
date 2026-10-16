#!/usr/bin/env python3
"""Write authored integration instructions, never mutate the semantic account."""
import hashlib
import json
import subprocess
from pathlib import Path
from author_checks import PREIMAGE, ROOT, STANDARDS, TENANT, sections

HERE = Path(__file__).resolve().parent
DEPENDENCY_CONDITIONS = {
    ('REFERENCE_FRAME_METHOD.rf-010-composition-on-demand', 'FOUNDATIONS.result-conjunction'): 'The selected evaluation combines returned results under conjunction.',
    ('REFERENCE_FRAME_METHOD.rf-010-composition-on-demand', 'TRANSFORMATION_LIBRARY.composition-law'): 'The selected evaluation transports evidence or coordinates, or combines operations into one material execution relation.',
    ('REFERENCE_FRAME_METHOD.select-and-activate', 'REFERENCE_FRAME_METHOD.rf-001-evaluation-relativity'): 'The activation relies on a selected frame for its actual evaluation q.',
    ('REFERENCE_FRAME_METHOD.workspace-coverage', 'REFERENCE_FRAME_METHOD.applicability-and-required-results'): 'The coverage evaluation determines which inventory obligations apply to its bound scope.',
    ('REFERENCE_FRAME_METHOD.workspace-coverage', 'FOUNDATIONS.result-conjunction'): 'The coverage evaluation combines the supported results of its required predicates or material interactions.',
    ('REFERENCE_FRAME_METHOD.frame-qualification', 'FOUNDATIONS.workspace-and-context'): 'The claim reuses qualification after material change or relies on capability-fit versus task-use evidence.',
    ('STDO_REFERENCE_FRAME_BASELINE.engagement-applicability', 'FOUNDATIONS.configuration'): 'The adopted profile selects between a sufficient direct activation and coordination.',
    ('STDO_REFERENCE_FRAME_BASELINE.executive-attention-evaluation-and-action', 'REFERENCE_FRAME_METHOD.applicability-and-required-results'): 'The selected coordinated engagement derives U0 or selects M from its applicable obligations and dependencies.',
    ('STDO_REFERENCE_FRAME_BASELINE.4-executive-evaluates-the-work-result', 'FOUNDATIONS.result-conjunction'): 'Executive combines the declared required candidate/assessment results and material joins before disposition.',
    ('STDO_REFERENCE_FRAME_BASELINE.coverage-application', 'REFERENCE_FRAME_METHOD.applicability-and-required-results'): 'The adopted engagement determines applicability of a material obligation in its coverage inventory.',
    ('STDO_REFERENCE_FRAME_BASELINE.coverage-application', 'REFERENCE_FRAME_METHOD.workspace-coverage'): 'The adopted engagement claims coverage of its declared scope.',
    ('STDO_REFERENCE_FRAME_BASELINE.coverage-application', 'FOUNDATIONS.result-conjunction'): 'The adopted engagement combines its required results to decide the governed predicate.',
}
CHANGES = [
    {
        'id': 'FOUNDATIONS.foundational-commitments',
        'append_unique': {
            'obligations': ['Distinguish adopted commitments from instance premises supplied by the selected contract. Bind each family argument to its deciding owner, actual consumer and additional policy. Pillar contributions are explanatory contributions, not extra axioms or grants.'],
            'permissions_exceptions': ['An argument owns no second version of its linked law and requires no additional work record.'],
        },
        'argument_addition': 'A selected predicate, persistent workspace, material join or required independent assessment is an instance condition only when the bound contract supplies it. Finite capacity alone supplies none of them.',
    },
    {
        'id': 'FOUNDATIONS.result-algebra',
        'append_unique': {
            'obligations': ['RF-012 and domain refinements bind predicate truth, actual evaluation performance and material effect completion before consuming a refined label; a label cannot decide the other predicates.'],
            'consumers': ['REFERENCE_FRAME_METHOD.rf-012-closed-results', 'TRANSFORMATION_LIBRARY.evaluate'],
        },
        'argument_addition': 'F1 supplies the question and F2/F6 bound its answer to evidence. F3/F5 admit interruption and effects outliving an actor. Information preserves each answer meaning; computational execution supplies performance and effect observations. The five verdicts, legal performance pairs and effect vocabulary are retained choices of this owner.',
    },
    {
        'id': 'FOUNDATIONS.result-conjunction',
        'append_unique': {
            'obligations': ['The applicability and coverage contract supplies the required predicates and joins; the received-return list cannot define the required set. Missing required returns remain visible even if every received return is satisfied, and authenticated failure survives another missing slot.'],
            'consumers': ['TRANSFORMATION_LIBRARY.conjoin', 'REFERENCE_FRAME_METHOD.result-conjunction', 'STDO_REFERENCE_FRAME_BASELINE.coverage-application'],
        },
        'argument_addition': 'F4 preserves the declared required relation; F2/F6 retain authenticated counterevidence. The applicability owner chooses requirements and this owner supplies their single conjunction rule. No verdict precedence, effect join, operator declaration or regrouping law changes.',
    },
    {
        'id': 'FOUNDATIONS.core-contract-derivations',
        'set': {
            'definition.meaning': 'Eleven source-bound conditional arguments group the core decisions: interpretation, purpose/interfaces, identity/state/evidence, composition/categorical descriptions, result record, domain refinement/decision results, conjunction, workspace/context, unknown-effect recovery, bounded construction and configuration. Each binds its actual consumer, applicable pillar contribution, conditional consequence and additional owner choice.',
            'argument.conditional_consequence': 'Each stated instance premise supplies a decision-specific consequence: recoverable meaning, purpose-bound interfaces, current subject identity, supported material joins, separate truth/performance/effects, non-promoting refinements, retained failures and coverage, sufficient reacquisition, observed or lawfully idempotent retry, preserved outer outcomes, and adequate allocation without a prescribed hierarchy. These arguments do not derive their owners policy choices from finite capacity.',
        },
        'replace_table_argument_scope': True,
        'append_unique': {
            'obligations': ['Keep every argument conditional on its named instance premises and retain the linked body as the sole deciding owner. Pillar contributions describe the preserved relationship and do not imply universal derivation.'],
            'consumers': ['TRANSFORMATION_LIBRARY.foundational-contract', 'REFERENCE_FRAME_METHOD.reference-frame-laws', 'STDO_REFERENCE_FRAME_BASELINE.status-and-authority-boundary'],
        },
        'argument_addition': 'Replace the obsolete five-family description, including its premise binding text. The exact eleven rows are supplied in source_family_rows; their additional policies remain at their named owners.',
    },
    {
        'id': 'TRANSFORMATION_LIBRARY.foundational-contract',
        'set': {
            'definition.meaning': 'The existing shared contract vocabulary and six composable responsibilities, plus four conditional family arguments for Contract application, Faithful projection, Composition law and Recovery law. Each argument binds a selected instance, actual consumers, pillar contributions and additional domain choices.',
        },
        'replace_table_argument_scope': True,
        'append_unique': {
            'obligations': ['A shared implementation of Bind, Acquire, Transform, Evaluate, Conjoin or Dispose does not merge their subjects, results or authority.'],
            'consumers': ['DESIGN_MODULE_METHOD.admission-contract-use', 'REFERENCE_FRAME_METHOD.select-and-activate', 'REFERENCE_FRAME_METHOD.rf-017-proportional-compression', 'AXIOMATIC_CALCULUS.ac-017-interpretation-fidelity'],
        },
        'argument_addition': 'The four table rows bind selected operations, source-to-consumer relations, composites and interrupted work as instance premises; none follows from finite capacity. Specification, functional design, information, calculus, execution, reference-frame and authority contributions supply different preserved relations.',
    },
    {
        'id': 'TRANSFORMATION_LIBRARY.contract-application',
        'append_unique': {
            'obligations': ['Design admission binds its transition and complete enclosing relation; frame activation binds evaluation, subject, basis and actor. Both apply the six shared conditions while retaining different domain predicates. Reuse a supported condition through its validity route; a boundary crossing alone neither repeats proof nor permits omission of a changed dependency.'],
            'consumers': ['DESIGN_MODULE_METHOD.admission-contract-use', 'REFERENCE_FRAME_METHOD.select-and-activate'],
        },
        'argument_addition': 'F4 requires the relation material to the consuming decision, not a uniform predicate for unrelated consumers. F2/F3 support validity-preserving reuse. The domain supplies its commit or capability predicate, exceptions and actual authority; admission is not outcome success.',
    },
    {
        'id': 'TRANSFORMATION_LIBRARY.faithful-projection',
        'append_unique': {
            'obligations': ['RF-017 frame views preserve evaluation failure detections and capability conditions; AC-017 interpretations preserve represented predicates, dependencies and permitted latitude. Adequacy for one claim cannot establish the other without the corresponding source-to-consumer binding.'],
            'consumers': ['REFERENCE_FRAME_METHOD.rf-017-proportional-compression', 'AXIOMATIC_CALCULUS.ac-017-interpretation-fidelity'],
        },
        'argument_addition': 'F2/F4 provide the informational preservation relation. The actual consumer selects its material distinctions. Neither arbitrary predicate decidability nor a universal serialization follows.',
    },
    {
        'id': 'TRANSFORMATION_LIBRARY.workrecovery-specialization',
        'replace_table_argument_scope': True,
        'argument_addition': 'The existing five argument rows now bind their specific pillar contributions: specification/information for outcome and claim; reference frames for sufficient acquisition; identity/world models and outcome-driven development for persistent continuation; execution/evidence/authority for unknown effects; algebraic conjunction and outcome-driven development for permitted continuation or stop. Original consequences, domain policies, result refinements and exceptions remain unchanged.',
    },
    {
        'id': 'TRANSFORMATION_LIBRARY.transformation-admission-specialization',
        'replace_table_argument_scope': True,
        'argument_addition': 'The existing four argument rows now bind identity and interpreted evidence to current predecessor; algebraic composition and functional invariants to affected seams; evidence/authority to durable admission; execution and outcome-driven recovery to supported forms and effects. Existing admission predicates, quorums, commit decomposition, topology permissions and exceptions remain unchanged.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.reference-frame-laws',
        'set': {
            'definition.meaning': 'Ten conditional argument families bind evaluation-family inclusion, sufficient acquisition, basis/currentness, authority/meaning, configuration, material composition, closed results, compression, applicability/coverage, and discovery/qualification to their deciding laws and actual consumers.',
            'argument.conditional_consequence': 'A declared evaluation and its material relations are instance premises. Each law supplies the corresponding decision: family inclusion before sufficiency reliance; bounded material acquisition; basis-sensitive reuse; preserved meaning and grants; adequate allocation without hierarchy; material composition only when used; predicate-preserving closed results; faithful compression; supported required coverage; and scoped diagnosis/qualification.',
        },
        'replace_table_argument_scope': True,
        'argument_addition': 'Replace the obsolete six coarse family arguments and source table scope with the exact ten source_family_rows, including each pillar contribution and additional owner choice. Foundations retains its shared rules and this member retains frame-specific policy.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.rf-001-evaluation-relativity',
        'append_unique': {
            'obligations': ['Before relying on frame sufficiency, bind the actual evaluation to the declared family. Frame-set membership and similar task names do not establish inclusion. An out-of-family question needs a suitable frame or applicable scoped result without renaming away the original obligation.'],
            'consumers': ['REFERENCE_FRAME_METHOD.select-and-activate', 'REFERENCE_FRAME_METHOD.diagnostic-order'],
        },
        'argument_addition': 'F1 supplies the actual question and F2 its interpreted family. Specification contributes intended decision and reference frames the testable sufficiency boundary. This makes the existing family-relative applicability condition explicit; no new core result or mandatory frame partition is selected.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.rf-010-composition-on-demand',
        'append_unique': {
            'obligations': ['Apply Foundations Result conjunction to the result relation; also apply library Composition law when the actual consumer transports evidence/coordinates or combines operations into one execution. The number of frames alone does not trigger internal composition.'],
            'dependencies': ['FOUNDATIONS.result-conjunction', 'TRANSFORMATION_LIBRARY.composition-law'],
        },
        'argument_addition': 'F4 requires preservation of the material relation actually combined. Algebraic composition and functional boundaries distinguish result consumption from execution composition; the join owner supplies its additional law.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.select-and-activate',
        'append_unique': {
            'obligations': ['Bind q to declared family Q under RF-001 before relying on RF-003 material sufficiency. Available general-purpose framing does not establish fit; inspect the actual family, material inputs and actor conditions through Contract application.'],
            'dependencies': ['REFERENCE_FRAME_METHOD.rf-001-evaluation-relativity'],
        },
        'argument_addition': 'Evaluation relativity determines which relations the activation must acquire; frame availability alone cannot supply this decision. The existing activation-refusal/downstream-work split and performance/effect mappings remain unchanged.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.workspace-coverage',
        'append_unique': {
            'obligations': ['Determine inventory applicability before consuming results, then conjoin required predicates and material interactions. Distinguish scope inventory coverage, admissible support for each applicable slot and satisfaction of the governed predicate. Populated received slots alone cannot establish the other claims.'],
            'dependencies': ['REFERENCE_FRAME_METHOD.applicability-and-required-results', 'FOUNDATIONS.result-conjunction'],
            'consumers': ['STDO_REFERENCE_FRAME_BASELINE.coverage-application'],
        },
        'argument_addition': 'F1 supplies selected scope, F4 the required joins, and F2/F6 support for exclusion. Coverage is determined from governing obligations rather than from successful returned results.',
    },
    {
        'id': 'REFERENCE_FRAME_METHOD.frame-qualification',
        'append_unique': {
            'obligations': ['Apply shared currentness when reusing qualification after material source, task, actor or dependency change. Capability evidence covers only its measured or supported envelope. Successful use does not measure unknown host context; byte fit does not establish adequate attention.'],
            'dependencies': ['FOUNDATIONS.workspace-and-context'],
        },
        'argument_addition': 'F2/F3 bind qualification to actual subject/support and F5 bounds its measured envelope. Evidence and reference-frame contributions keep capability fit and task-use adequacy as distinct claims under the existing nine qualification questions.',
    },
    {
        'id': 'STDO_REFERENCE_FRAME_BASELINE.status-and-authority-boundary',
        'replace_table_argument_scope': True,
        'append_unique': {
            'obligations': ['An adopted configuration, selected work boundary and actual grants are instance premises; coordinated duties additionally depend on material work or assurance not covered by a sufficient direct activation.'],
        },
        'argument_addition': 'Replace four coarse profile arguments with eight exact source_family_rows: direct/coordinated selection, Executive frontier/action, exact basis/handoff, work-result consumption, specialist/testing/coverage, adoption, qualification, and closure. Retain definition.owned_relation_rows and every existing result mapping. The optional configuration and actual grants do not follow from finite capacity.',
    },
    {
        'id': 'STDO_REFERENCE_FRAME_BASELINE.engagement-applicability',
        'append_unique': {
            'obligations': ['Apply Foundations Configuration to actual operations, dependencies, actor capability and assurance when selecting direct entry or coordination. An available role cannot establish coordination need. Shared governing sources do not defeat required independent judgment; a fresh context does not erase authorship. Retain those conditions in intake and grants.'],
            'dependencies': ['FOUNDATIONS.configuration'],
        },
        'argument_addition': 'Reference frames allocate sufficient attention and execution binding supplies actual capability. F4/F5/F6 constrain adequacy and permitted allocation but do not prescribe an Executive or a role inventory.',
    },
    {
        'id': 'STDO_REFERENCE_FRAME_BASELINE.executive-attention-evaluation-and-action',
        'append_unique': {
            'obligations': ['Derive U0 from applicable obligations and dependencies rather than visible returns; select M after supporting dependencies. Missing results, unknown applicability and uncertain material effects remain in the durable frontier while independent work may proceed under its own sufficient grant and evidence.'],
            'dependencies': ['REFERENCE_FRAME_METHOD.applicability-and-required-results'],
        },
        'argument_addition': 'Outcome-driven development retains the continuing destination/frontier; reference frames bound the next decision. F1/F4/F5/F6 explain attention allocation without dropping outer obligations or weakening the Executive mutation prohibition.',
    },
    {
        'id': 'STDO_REFERENCE_FRAME_BASELINE.4-executive-evaluates-the-work-result',
        'append_unique': {
            'obligations': ['Apply Foundations conjunction to the declared required set and joins. Availability, fitness, required assessment and the disposition mandate retain separate conditions. A ready label supplies no missing condition; authenticated failure remains alongside absent support, with performance and effects retained before dependent action.'],
            'dependencies': ['FOUNDATIONS.result-conjunction'],
        },
        'argument_addition': 'Information/evidence preserve the actual predicates; algebraic conjunction retains required failures and gaps; execution preserves performance/effects. Review requirements and acceptance authority remain with their existing owners.',
    },
    {
        'id': 'STDO_REFERENCE_FRAME_BASELINE.coverage-application',
        'append_unique': {
            'obligations': ['Use Frame Method applicability predicates for each material obligation; the frame-routing table does not replace them. Apply Workspace Coverage to scope and conjunction to required results. Frame availability, inventory completeness and outcome satisfaction remain distinct claims.'],
            'dependencies': ['REFERENCE_FRAME_METHOD.applicability-and-required-results', 'REFERENCE_FRAME_METHOD.workspace-coverage', 'FOUNDATIONS.result-conjunction'],
        },
        'argument_addition': 'The Product outcome determines relevant evidence and material joins. Specialist/test families retain their domain claims and populations; missing required support cannot become success and irrelevant availability need not be activated.',
    },
]


def main():
    account_path = TENANT / 'qualification/C3/iteration-3/DETERMINATIONS.json'
    original = subprocess.check_output(['git', 'show', f'{PREIMAGE}:{account_path.relative_to(ROOT)}'], cwd=ROOT)
    by_id = {row['id']: row for row in json.loads(original)['determinations']}
    for change in CHANGES:
        name, key = change['id'].split('.', 1)
        path = STANDARDS / f'{name}.md'
        section = sections(path.read_text())[key]
        change['source_owner'] = f'standards/{name}.md#{key}'
        change['preimage_body_sha256'] = by_id[change['id']]['owner']['body_sha256']
        change['candidate_body_sha256'] = hashlib.sha256(section['body'].encode()).hexdigest()
        change['change_class'] = 'argument_and_consumer_clarification'
        change['predicate_change'] = 'none; existing determining conditions are made explicit'
        change['result_mapping_change'] = 'none'
        additions = change.get('append_unique', {})
        consumer_ids = additions.pop('consumers', [])
        if consumer_ids:
            change['append_source_refs'] = [
                {'source': 'standards/' + identity.split('.', 1)[0] + '.md#' + identity.split('.', 1)[1],
                 'relation': 'consumer_location', 'acquisition_role': 'provenance_only',
                 'note': 'Audit route; not an always-required input to operational application.'}
                for identity in consumer_ids]
        dependencies = additions.pop('dependencies', [])
        if dependencies:
            change['append_dependency_relations'] = [
                {'target': identity, 'relation': 'required_deciding_contract',
                 'required_when': DEPENDENCY_CONDITIONS[(change['id'], identity)]}
                for identity in dependencies]
        if change.get('replace_table_argument_scope'):
            table = [line for line in section['body'].splitlines() if line.startswith('|')]
            if name == 'STDO_REFERENCE_FRAME_BASELINE':
                start = next(i for i, line in enumerate(table) if line.startswith('| Profile family and consuming decision |'))
                table = table[start:]
            change['source_family_rows'] = {
                'columns': [s.strip() for s in table[0].strip('|').split('|')],
                'rows': [[s.strip() for s in row.strip('|').split('|')] for row in table[2:]],
                'acquisition_role': 'conditional_argument_evidence',
                'required_when': 'The activation assesses this family argument, its premise-to-consequence relation or consumer coverage. Merely applying a named operational law does not require the table or every listed consumer.',
                'consumer_locations_role': 'source_refs/provenance_only',
            }
            change['integration_instruction'] = 'Replace the obsolete family argument/definition table payload and argument.source_table_scope, preserving the account schema. Keep all unrelated definition fields, deciding predicates, result mappings and proof standing. These exact source rows are authored input, not a fidelity judgment.'
    result = {
        'schema_version': 'stdo.authored-source-account-patch.v1',
        'standing': 'Authored semantic-field amendments for integration; not a regenerated account or independent fidelity assessment.',
        'contract': 'EC-CODEX-I4-01 / I4-CORE-SOURCE',
        'source_preimage': PREIMAGE,
        'account_preimage_path': str(account_path.relative_to(TENANT)),
        'account_preimage_sha256': hashlib.sha256(original).hexdigest(),
        'integration_rules': [
            'Address existing rows by stable id; retain all 701 existing determination identities.',
            'Append unique authored fields and argument_addition without replacing unrelated semantic content.',
            'Dot-path set operations change only the named field; replace_table_argument_scope replaces stale coarse family descriptions, never the row result mapping.',
            'Resolve and refresh typed dependency/consumer references and source clauses at the frozen integration subject; source pins/ranges are not regenerated here.',
            'append_source_refs are provenance-only owner routes. Do not turn reverse consumer locations or the argument tables into unconditional required inputs. append_dependency_relations preserve their explicit required_when; unknown applicability remains unresolved under the existing contract.',
            'Argument-table acquisition is conditional on assessing that argument or its coverage. Preserve source_refs/provenance tags in definition and argument payloads; an operational application acquires only its actual deciding dependencies.',
            'Preserve original source-block roles, conditional/provenance acquisition and every I3 result/fidelity repair. Non-deciding family tables remain argument/definition data with their embedded scoped constraints.',
        ],
        'changes': CHANGES,
        'unfinished_source_bindings': [],
        'remaining_integration': ['Apply author input to the current account at the integrated source freeze.', 'Regenerate source clauses, pins, typed dependency joins, argument routes, affected frame views and interpretation; independently assess fidelity and conserved meaning.'],
    }
    (HERE / 'ACCOUNT_PATCH.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'entries': len(CHANGES), 'source_family_rows': {r['id']: len(r['source_family_rows']['rows']) for r in CHANGES if 'source_family_rows' in r}, 'result_mapping_changes': 0}))


if __name__ == '__main__':
    main()
