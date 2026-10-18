"""Reproduce the source-bound author proposal input; no semantic acceptance."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ITERATION = HERE.parents[1]
sys.path.insert(0, str(ITERATION / 'tools'))
import carry_conservation as c

RAW = 'd7e6876c4a2294a18fce8db08a4bcfabc1fa5eb3'
I4_SOURCE = '01b01274b244ae6e5de10bf6bacb60087462cbb5'
PREPARATION = '352e5e29a45f1362605bfa06d97387f544626d84'
F = 'standards/FOUNDATIONS.md#'

# These are AUTHOR comparisons of exact clauses. They are not independent
# assessments, and none states that the old method permitted false proof.
CASES = [
    ('DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule', 'I5-ACCOUNT-R001', 'Q19',
     'Adds explicit assertion interpretation/observation support and separate assertion/execution provenance to the existing module-owned proof lane; implementation-discovered tests must be re-expressed and justified against module obligations before module closure.',
     'A module-owned test has the original ownership trace and actually tests its module property, but its evidence does not separately bind the assertion derivation and actual executed subject/observations. The new clause expressly requires those two support relations; this proposal records the added duty, not permission for an invalid oracle under the predecessor.',
     [F+'assertions-and-observations', F+'parallel-assurance-and-provenance']),
    ('REFERENCE_FRAME_METHOD.md#evidence', 'I5-ACCOUNT-R002', 'Q19',
     'Extends the evidence declaration with an explicit reliance contract binding the frame predicate, assertion justification, observations and actual execution provenance through Construction assurance.',
     'An admitted artifact records provenance, subject, basis and scope as the predecessor Evidence declaration requires, but its expected predicate has no separately justified derivation. Availability still grants no truth or authority in either source; I5 additionally requires the stated assertion/observation reliance bindings.',
     [F+'construction-assurance', F+'assertions-and-observations', F+'parallel-assurance-and-provenance']),
    ('REFERENCE_FRAME_METHOD.md#independently-activated-co-evaluation', 'I5-ACCOUNT-R003', 'Q20',
     'Retains non-interference between unclosed frame evaluations and adds explicit shared-cause/path justification for a mutual-assurance claim; separate activations and authorship conditions do not establish statistical independence or validate a shared expectation.',
     'Two non-interfering activations use the same erroneous fixture. They still satisfy the predecessor activation-separation condition; I5 requires their common cause to remain in the mutual-assurance account before a stronger confidence claim. This does not assert that the predecessor promised statistical independence.',
     [F+'parallel-assurance-and-provenance', F+'risk-and-assurance-selection']),
    ('SPEC_METHOD.md#transition-evidence-and-proof-cadence', 'I5-ACCOUNT-R004', 'Q21',
     'Replaces cheapest focused falsification alone as the stated selection rule with risk/impact-qualified assurance selection, supported exclusions, new obligations and mandatory gates, total selection/reassessment cost and exact evidence-retention applicability. Whole-candidate qualification retains its declared boundary and required earlier triggers.',
     'A cheap local falsifier exists but its impact analysis cannot exclude a changed fixture dependency. The old stated cadence names cheapest focused falsification and affected risk; the new selection contract expressly requires handling unknown impact and mandatory/new coverage and compares selection plus reassessment cost. Weak-property proof remains insufficient under both sources.',
     [F+'change-impact-and-evidence-retention', F+'risk-and-assurance-selection', F+'assertions-and-observations']),
    ('SPEC_METHOD.md#testing-strategy-taxonomy', 'I5-ACCOUNT-R005', 'Q19',
     'Retains the two test-authority classes, sandbox/live distinctions and applicable gates, adding separately justified assertion provenance and actual execution provenance, shared-dependency accounting and bounded standing for implementation-derived regression claims.',
     'A lane declares its admitted requirement/design source and correct breadth label, but records only execution provenance. The added relation requires the expected predicate and derivation as well; matching lane labels alone cannot discharge it. The predecessor already prohibited current implementation from authoring the expected result.',
     [F+'parallel-assurance-and-provenance', F+'assertions-and-observations']),
    ('STDO_REFERENCE_FRAME_BASELINE.md#derived-product-testing-frame-set', 'I5-ACCOUNT-R006', 'Q19',
     'Adds an explicit Construction-assurance binding for each selected testing claim, including requirement/refinement source, asserted predicate, observation basis and required assurance, while retaining profile adoption, ordinary paths, exact subjects and the four-frame configuration.',
     'A selected testing frame declares the old claim/subject/path/population/oracle/falsification tuple but does not bind assertion derivation and observation justification at its consuming decision. I5 makes those assurance relations explicit duties without requiring an extra frame or actor.',
     [F+'construction-assurance', F+'assertions-and-observations', F+'parallel-assurance-and-provenance']),
    ('STDO_REFERENCE_FRAME_BASELINE.md#combinatorial-coverage-and-testing-value-index', 'I5-ACCOUNT-R007', 'Q21',
     'Retains interaction coverage and its eight dimensions while adding risk-qualified testing selection, material consequence/uncertainty and action conditions, total analysis/acquisition/execution/assessment cost, and justified probability/dependence/calibration for quantitative confidence claims.',
     'A project supplies the predecessor interaction coordinates and a locally authorized scalar but claims operational confidence without a calibrated probability/dependence model. I5 explicitly requires that model for the confidence claim and separates it from interaction value; it does not retrospectively turn the old multiplicative interaction description into a probability theorem.',
     [F+'risk-and-assurance-selection', F+'parallel-assurance-and-provenance']),
    ('STDO_REFERENCE_FRAME_BASELINE.md#testing-evidence-composition', 'I5-ACCOUNT-R008', 'Q20',
     'Adds justified requirement/refinement assertion paths, actual execution provenance and shared-failure-cause accounting when composed testing results supply mutual assurance; repeated views of one execution do not become independent observations. Existing logical conjunction, failed/missing claims and authorship rules remain.',
     'One scenario produces UAT, end-to-end and integration results from the same run and fixture. The old rule already keeps their claims distinct and prevents substitution; I5 additionally binds their shared causes and separate assertion/execution paths before a mutual-assurance conclusion.',
     [F+'parallel-assurance-and-provenance', 'standards/TRANSFORMATION_LIBRARY.md#conjoin']),
    ('STDO_REFERENCE_FRAME_BASELINE.md#assurance-subject-acquisition-and-evaluation', 'I5-ACCOUNT-R009', 'Q19',
     'Retains exact owner-issued subject acquisition and independently derived oracle requirements, adding explicit assertion scope/implication, actual observation/checker-conformance support, acceptable-relation rather than default equality, and separate assertion/execution provenance.',
     'The correct owner-issued subject and upstream oracle source are acquired, but the check observes only a necessary condition and does not support the implication to the claimed obligation. The old source already forbids rival owner semantics; I5 expressly adds these oracle-fidelity and observation support bindings, without claiming that an unsound broader pass was previously lawful.',
     [F+'assertions-and-observations', F+'parallel-assurance-and-provenance']),
    ('TICKET_METHOD.md#test-case-authority', 'I5-ACCOUNT-R010', 'Q19',
     'Adds distinct assertion-derivation and actual execution provenance to the existing admitted-work authority chain, including justified predicate and actual checker/environment/observations, while preserving re-entry, governing-threat scope and prohibition on implementation-authored expectation.',
     'A passing test is traceable to its admitted ticket and governing source, but the record contains no separate derivation of its predicate or actual checker/environment observations. I5 now expressly requires both provenance relations in the existing carrier; no per-test ticket or new ledger is required.',
     [F+'parallel-assurance-and-provenance', F+'assertions-and-observations']),
    ('WORLD_MODEL_METHOD.md#4-assure', 'I5-ACCOUNT-R011', 'Q22',
     'Adds a mandatory assertion/observation binding for the model claim and its declared purpose, and distinguishes predictive adequacy from required construction outcome satisfaction. The original advisory assurance list keeps its should-strength.',
     'A predictive model claim has traced source observations and the original advisory disclosures but lacks a justified assertion/observation relation for its declared purpose. I5 requires that binding. Prediction error alone still cannot decide whether an external required outcome failed; the old should list is not silently rewritten as must.',
     [F+'assertions-and-observations', F+'bounded-construction']),
    ('SPEC_METHOD.md#universal-intake-triage', 'I5-ACCOUNT-R012', 'Q05',
     'Retains the earlier current-workspace/core-result replacement and extends its changed meaning with the common feedback diagnosis: distinguish defective realization, inadequate requirement/design, inaccurate prediction and insufficient observation; retain uncertain alternatives and allow evidence acquisition before repair. Severity, priority and a bug-list projection grant no new repair class or authority.',
     'The same anomaly can be explained by a faulty realization, a mistaken prediction or missing observation. The predecessor already requires supported causal localization and lawful re-entry; the I5 source adds this explicit four-way model/observation distinction and response binding. The inherited I3-R2-R020 description alone does not describe that added duty.',
     [F+'bounded-construction', F+'change-impact-and-evidence-retention']),
    ('SPEC_METHOD.md#agentic-construction-execution-stdo-up-020', 'I5-ACCOUNT-R013', 'Q23',
     'Preserves the bounded delegated-execution/assessment/disposition relation and adds its material construction-owner duties: distinguish required Z, acquired state/observations and prediction; justify the selected strategy/resource/feedback tradeoffs and supported purpose of continued work; apply preservation, feedback diagnosis and retained-evidence assurance without a prescribed runtime, role sequence, universal solver or termination guarantee.',
     'A delegated construction follows the original normative sequence, but its strategy treats prediction success as required-outcome evidence and supplies no material resource/feedback rationale. I5 explicitly binds these separate accounts and strategy duties through Bounded construction. The added duties are proposed, without claiming the predecessor permitted unsupported acceptance or that every strategy needs an exhaustive optimization.',
     [F+'bounded-construction', F+'preservation-obligations', F+'risk-and-assurance-selection', F+'change-impact-and-evidence-retention']),
]

CONSERVED = [
    ('RELEASE_METHOD.md#qualification-and-recovery',
     'For unchanged qualifying content and missing/partial remote refs, both sources require the separately observed remote relation and refuse a partial cohort. Supported reuse preserves the original subjects and cannot waive the existing release gates. The added retention route makes those conditions explicit rather than admitting a previously forbidden publication.',
     [F+'change-impact-and-evidence-retention']),
    ('SPEC_METHOD.md#evidence-rules',
     'This parent inventory unit routes its child proof obligations. I5 assigns assertion/observation support to the new shared owner while retaining operation binding and projection fidelity. Child sections have their own inventory rows; added testing duties are proposed there rather than mislabeled a new permission at this parent heading.',
     [F+'construction-assurance']),
    ('SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001',
     'A pass for a necessary weaker property cannot close the stronger target in either source: the predecessor already requires the witness-to-claim relation, nearest weaker excluded property and falsification condition. The added necessary/sufficient and observation explanation applies that same adequacy obligation; local regression scope remains available.',
     [F+'assertions-and-observations']),
    ('STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization',
     'A failed observation that does not establish violation of the claimed owner relation cannot establish the broader causal frontier in either source. The predecessor requires causal evidence, expected relations and supported violated loci; I5 explicitly routes the preliminary predicate/observation assessment through Evaluate. Unresolved alternatives and absence of repair authority remain.',
     ['standards/TRANSFORMATION_LIBRARY.md#evaluate', F+'assertions-and-observations']),
    ('TICKET_METHOD.md#condition-based-closure-and-reuse',
     'For a supposedly unchanged claim with a materially changed dependency or unknown required applicability, both sources withhold dependent closure and reopen affected reliance. Valid unrelated work survives in both. The I5 route elaborates evidence-validity/justification and mandatory/new coverage; added underlying testing obligations are counted at their owners, not treated as unchanged testing law here.',
     [F+'change-impact-and-evidence-retention']),
    ('SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014',
     'The source unit is byte-identical between I4 and the raw I5 freeze. Its predecessor already makes repeated acquisition, hashing, review and evidence work serve an identified need, binds operational assumptions and feedback cost, and permits shared family rationale without a per-clause receipt. I5 strategy duties are proposed at the UP-020 construction consumer; this proportionality relation and its no-universal-quota rule retain their meaning.',
     [F+'bounded-construction', F+'risk-and-assurance-selection']),
    ('SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021',
     'The source unit is byte-identical between I4 and the raw I5 freeze. Both retain complete participant/join validation before effect, coherent exact basis, supported applicability for reuse, mandatory independent judgments and all-or-none semantic admission. The shared preservation/retention explanation grants no partial cut, omitted participant or automatic acceptance.',
     [F+'preservation-obligations', F+'change-impact-and-evidence-retention']),
]

EXTRA_QUESTIONS = [
    {'id': 'Q19', 'title': 'Explicit assertion and execution support',
     'question': 'Accept the additional assertion-interpretation, observation/checker and separate assertion/execution provenance duties at these exact proof consumers, preserving their existing authority, scope and lane restrictions?',
     'i5_consequences_to_assess': 'Source-first comparison and receiving-line review must cover each actual proof consumer. A correct source identifier or executed test is not by itself the additional support.',
     'relation_ids': ['I5-ACCOUNT-R001','I5-ACCOUNT-R002','I5-ACCOUNT-R005','I5-ACCOUNT-R006','I5-ACCOUNT-R009','I5-ACCOUNT-R010']},
    {'id': 'Q20', 'title': 'Mutual assurance and shared failure causes',
     'question': 'Accept the explicit shared-cause and provenance conditions on mutual-assurance claims while retaining frame separation, logical conjunction and required authorship independence?',
     'i5_consequences_to_assess': 'Inspect shared fixtures, interpretations, observations and received contributions. Agreement and different actors do not establish statistical independence.',
     'relation_ids': ['I5-ACCOUNT-R003','I5-ACCOUNT-R008']},
    {'id': 'Q21', 'title': 'Risk-qualified assurance selection',
     'question': 'Accept the extended impact/risk/total-cost selection duties, required new coverage and mandatory gates, and the model/dependence/calibration conditions on quantitative assurance?',
     'i5_consequences_to_assess': 'Assess actual selection and unsupported exclusions; retain qualitative evidence and unknown numeric estimates. No universal probability threshold or automatic full-suite cadence follows.',
     'relation_ids': ['I5-ACCOUNT-R004','I5-ACCOUNT-R007']},
    {'id': 'Q22', 'title': 'Predictive claims and required outcomes',
     'question': 'Accept the added mandatory assertion/observation binding for world-model assurance and the distinction between predictive adequacy and construction outcome satisfaction, retaining the original advisory list strength?',
     'i5_consequences_to_assess': 'Review the model-purpose and observation binding and the material construction consumer; do not equate prediction error with an outcome failure.',
     'relation_ids': ['I5-ACCOUNT-R011']},
    {'id': 'Q23', 'title': 'Construction strategy and feedback obligations',
     'question': 'Accept the added required-state/prediction/observation, strategy/resource and feedback/preservation duties at the delegated construction consumer while retaining the old lawful execution and authority boundaries?',
     'i5_consequences_to_assess': 'Assess the current construction and recovery joins, supported continuation and resource rationale; preserve optional strategies and unresolved universal proofs.',
     'relation_ids': ['I5-ACCOUNT-R013']},
]


def main():
    old_bytes = c.git_bytes(c.START, (c.PRIOR/'CONSERVATION.json').relative_to(c.REPO))
    assert c.sha(old_bytes) == c.PRIOR_SHA
    old = json.loads(old_bytes); rows = {r['id']: r for r in old['rows']}
    parser = c.parser_library(); prefix = c.PACKAGE.relative_to(c.REPO)
    cache = {}
    def source(commit, member):
        key = (commit, member)
        if key not in cache:
            cache[key] = c.git_bytes(commit, prefix/member)
        return cache[key]
    def pin(commit, route):
        member, _, anchor = route.partition('#'); raw = source(commit, member)
        body = parser.section_body(raw.decode(), anchor).encode()
        return {'source_commit': commit, 'route': route, 'member_sha256': c.sha(raw),
                'body_sha256': c.sha(body), 'bytes': len(body)}
    installed = Path.home()/'Library/Application Support/STDO/releases/v2.5.1-rc.2'
    comparisons, amendments = [], []
    by_claim = {x[0]: x for x in CASES}
    retained = {x[0]: x for x in CONSERVED}
    for claim in sorted(set(by_claim)|set(retained)):
        row = rows[claim]; member = row['source_member']; anchor = row['source_anchor']
        predecessor = (installed/member).read_bytes()
        assert c.sha(predecessor) == old['source_member_pins'][member]['sha256']
        original = parser.section_body(predecessor.decode(), anchor).encode()
        route = 'standards/'+claim
        prior_body = parser.section_body(source(I4_SOURCE, member).decode(), anchor).encode()
        new_body = parser.section_body(source(RAW, member).decode(), anchor).encode()
        selected = by_claim.get(claim)
        comparison = {'claim': claim, 'predecessor_member_sha256': c.sha(predecessor),
            'predecessor_section_sha256': c.sha(original), 'predecessor_body': original.decode(),
            'i4': dict(pin(I4_SOURCE, route), body=prior_body.decode()),
            'i5_raw': dict(pin(RAW, route), body=new_body.decode()),
            'inherited_disposition': row['disposition'],
            'author_result': 'proposed_supersession' if selected else 'proposed_conserved',
            'independent_assessment': 'not_performed', 'owner_decision': None}
        if selected:
            _, rid, qid, meaning, case, owners = selected
            loci = list(dict.fromkeys([route] + row.get('successor_loci', []) + owners))
            comparison.update(current_relation_id=rid, same_case_argument=case,
                              changed_meaning=meaning, question=qid)
            relation = {'id': rid, 'predecessor_claim_id': claim, 'changed_meaning': meaning,
                'replacement_loci': loci, 'standing': 'proposed_pending_owner_decision',
                'owner_decision': None,
                'remaining_condition': 'Author proposal at raw source '+RAW+'; final documentary binding, nonauthor semantic adequacy and owner acceptance remain open.'}
            amendments.append({'claim_id': claim, 'original_row_sha256': c.sha(c.canonical(row)),
                'prior_disposition': row['disposition'],
                'supersedes_proposal_id': row.get('successor_relation', {}).get('id'),
                'question': qid, 'replacement_relation': relation,
                'successor_loci': loci,
                'owner_dependencies': [{'locus': x, 'standing': 'I5 shared owner; author proposal requires current nonauthor assessment',
                                        'acquire_when': 'evaluating this replacement or its applicability'} for x in owners],
                'source_locus_pins': [pin(RAW, x) for x in [route]+owners],
                'same_case_argument': case})
        else:
            comparison.update(same_case_argument=retained[claim][1],
                              material_owners=[pin(RAW, x) for x in retained[claim][2]])
        comparisons.append(comparison)
    paths = subprocess.check_output(['git','diff','--name-only',I4_SOURCE,RAW,'--',str(prefix/'standards')],cwd=c.REPO,text=True).splitlines()
    changed_sections = []
    for path in paths:
        member = path[len(str(prefix))+1:]
        before = source(I4_SOURCE,member).decode(); after = source(RAW,member).decode()
        prior = {x['anchor']: parser.section_body(before,x['anchor']) for x in parser.heading_rows(before)}
        for heading in parser.heading_rows(after):
            anchor=heading['anchor']; body=parser.section_body(after,anchor)
            if prior.get(anchor)!=body:
                changed_sections.append({'route':member+'#'+anchor,
                    'i4_body_sha256': c.sha(prior[anchor].encode()) if anchor in prior else None,
                    'i5_body_sha256': c.sha(body.encode()), 'new_section':anchor not in prior,
                    'i4_body':prior.get(anchor), 'i5_body':body})
    guards=[]
    for route in [F+'foundational-commitments',F+'result-algebra',F+'result-conjunction']:
        a=pin(I4_SOURCE,route);b=pin(RAW,route);assert a['body_sha256']==b['body_sha256']
        guards.append({'route':route,'i4':a,'i5':b,'author_result':'unchanged owning section; not whole-candidate semantic acceptance'})
    evidence={'kind':'stdo.i5.author-conservation-source-comparison','common_input':c.COMMON,
        'preparation_commit':PREPARATION,'i4_source':I4_SOURCE,'raw_source':RAW,
        'source_boundary':'Nine changed standards: Foundations and eight consumers. All changed raw heading units are recorded. Twenty selected predecessor clauses receive actual source comparison; remaining claims retain their evidence and unclosed semantic coverage.',
        'changed_members':[{'path':p[len(str(prefix))+1:],
            'i4_sha256':c.sha(c.git_bytes(I4_SOURCE,p)), 'i5_sha256':c.sha(c.git_bytes(RAW,p))} for p in paths],
        'changed_sections':changed_sections,'comparisons':comparisons,'unchanged_core_guards':guards,
        'shared_owner_consequences':[
            'The new preservation owner makes initial/step/join/final support explicit for claimed composition. The earlier contract already requires compatible material joins; unchanged UP-021 preserves atomic admission and no result-algebra or conjunction rule changed.',
            'New assertion/provenance/mutual-assurance/risk duties are proposed at exact deciding consumers, not treated as coordinate-only updates.',
            'The expanded bounded construction owner adds material strategy/feedback/prediction distinctions; the UP-020 carrying claim receives an explicit proposal even though its local source unit is unchanged.',
            'New assurance and testing-reassessment headings have no new predecessor identity. They require their own I5 source-account/interpretation and conformance coverage; the 691-claim predecessor population remains intact.',
            'Other inherited proposals are not owner-approved by their continued presence. Their current complete carrying relation and evidence validity still require source-first assessment; a shared owner pin alone supplies none.'],
        'standing':'Author comparison and proposals only; no independent semantic verdict, owner decision, acceptance or complete 691-row reassessment.'}
    c.write(HERE/'SOURCE_COMPARISON.json',evidence)
    proposal={'kind':'stdo.i5.explicit-conservation-proposals','schema_version':1,
        'common_input':c.COMMON,'base_conservation_sha256':c.PRIOR_SHA,
        'base_commit':c.START,'preparation_commit':PREPARATION,'raw_source_commit':RAW,
        'evidence':{'path':'source/account/SOURCE_COMPARISON.json','sha256':c.sha((HERE/'SOURCE_COMPARISON.json').read_bytes())},
        'amendments':amendments,'additional_questions':EXTRA_QUESTIONS,
        'standing':'Twelve proposed conserved-to-superseded changes and one revision of a pending proposal. Historical evidence and all owner decisions remain unchanged and open.'}
    c.write(HERE/'PROPOSALS.json',proposal)
    print(json.dumps({'changed_members':len(paths),'changed_sections':len(changed_sections),
        'predecessor_comparisons':len(comparisons),'amendments':len(amendments),
        'new_supersessions':sum(x['prior_disposition']=='conserved' for x in amendments),
        'revised_proposals':sum(x['prior_disposition']=='superseded' for x in amendments),
        'retained_comparisons':len(CONSERVED),'unchanged_core_guards':len(guards)}))


if __name__=='__main__':
    main()
