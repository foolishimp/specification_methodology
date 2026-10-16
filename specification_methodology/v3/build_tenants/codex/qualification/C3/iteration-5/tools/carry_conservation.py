"""Carry the frozen I4 claims without inventing I5 review or owner decisions.

--prepare preserves every historical row and groups the 69 proposed replacements.
--refresh binds their existing carrying coordinates to an exact source/account
freeze. It does not prove complete carrying relations, conservation, or reuse.
Historical helpers are imported for pure parsing only; their mains never run.
"""
import argparse
import copy
import json
from collections import Counter
from pathlib import Path

from context import (HERE, PRIOR, PACKAGE, REPO, INPUTS, sha, read, write,
                     git_bytes, library, exact_source)

COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
START = '11163991fd8525c98bdd94a36c71a2cfeb15a403'
HANDOFF = '62318d3b0be35985a0397aa39daee0ec8836eabc'
COMMON_PATH = Path('specification_methodology/v3/specification/requirements/PREDECESSOR_CLAIMS.md')
COMMON_SHA = '2b8e80c9623e746250b3c338d8afa08b6d17e033e658e4dc922965fa0b7f606a'
PRIOR_SHA = '92ef2fd3a399ede2b28c1a421b4f81cbe6460363d1056a9aad189b36e8f41fdd'
FILES = ('CONSERVATION.json', 'FRONTIER.json', 'REPLACEMENT_QUESTIONS.json')

# A question groups decisions with a common substantive issue, not a source
# family. Each exact relation remains a separate proposed decision beneath it.
QUESTIONS = [
    ('Q01', 'Shared ownership and the status of added policy',
     'Accept the stated transfer of shared result/composition/context ownership, while preserving calculus and frame specializations and distinguishing historical provenance from the chosen three-kind and profile policies?',
     ['I3-R2-R001', 'I3-R2-R038', 'I3-R2-R010', 'I3-R2-R037'],
     'Check the I5 preservation and assurance owners and their consumers; new premises or policy are not retrospectively derived from historical principles.'),
    ('Q02', 'One predicate-bound result and its profile signatures',
     'Accept the exact extended result signatures and common-core refinements, including predicate, verdict, performance, effects, residuals and cause-sensitive profile meanings?',
     ['I3-R2-R002', 'I3-R2-R003', 'I3-R2-R012', 'I3-R2-R040', 'I3-R3-R007', 'I3-R3-R008', 'I3-R2-R029', 'I3-R3-R015'],
     'Check I5 assertion, observation and provenance consumers without collapsing unperformed evaluation, indeterminate judgment, domain decision or effects.'),
    ('Q03', 'Material joins and conjunction precedence',
     'Accept the shared typed-composition and fixed conjunction rules, including authenticated failure precedence and retained conflict information, with the changed qualification discriminator?',
     ['I3-R2-R004', 'I3-R2-R013', 'I3-R2-R015', 'I3-R3-R006'],
     'Reassess step/join/end-to-end preservation and integration assumptions; the historical finite model does not prove universal construction or observation.'),
    ('Q04', 'Interpretation fidelity and translation return obligations',
     'Accept the added independently specified decision-fidelity obligations and cause-sensitive translation return contract while preserving exact coordinates, losses and provenance?',
     ['I3-R3-R001', 'I3-R3-R005'],
     'Cover the new construction/assurance interpretation and distinguish formula, structural check, discharged argument, external predicate and observation.'),
    ('Q05', 'Activation, currentness and contract admission',
     'Accept the separate activation/work predicates and current-workspace/admission bindings, preserving actual grants and the original change classes?',
     ['I3-R2-R014', 'I3-R2-R020', 'I3-R2-R025'],
     'Bind I5 feedback diagnosis, uncertain effects and targeted reassessment; a lifecycle or completed check remains no effect grant.'),
    ('Q06', 'Sufficient bounded Executive context',
     'Replace mandatory complete private Product/frontier context with the sufficient bounded delivery view at Executive entry, attention, checkpoint and template consumers?',
     ['I3-R2-R034', 'I3-R2-R022', 'I3-R2-R036', 'I3-R3-R018'],
     'Assess the actually needed I5 obligation/dependency frontier and acquisition boundaries; do not infer host-context fit from source byte counts.'),
    ('Q07', 'Optional baseline configuration and archetypes',
     'Accept the baseline inventory and twelve archetypes as selected optional profile policy, preserving required coverage and distinguishing a residual from satisfaction?',
     ['I3-R3-R012', 'I3-R3-R013'],
     'Preserve permitted human/mixed bindings and optionality under I5 construction and assurance; no universal role topology follows.'),
    ('Q08', 'Cause-qualified work returns and closure conditions',
     'Accept the reason-sensitive work-result map and closure carrying matrix, including unreturned actors and the explicit changes to invertibility and private context, while retaining every other closure restriction?',
     ['I3-R2-R023', 'I3-R2-R035', 'I3-R2-R024', 'I3-R3-R014'],
     'Keep lawful work, progress, completion and outcome satisfaction separate; account for every retained/new mandatory gate and unresolved obligation.'),
    ('Q09', 'Cross-view applicability and conformance judgments',
     'Accept the changed predicate/result contract while retaining assessment of every applicable axiom and the original cross-view gates and outcomes?',
     ['I3-R2-R007'],
     'Check I5 assertion/evidence sufficiency and unknown applicability; a reasoned exclusion is not a failed conformance conjunct or an optional skip.'),
    ('Q10', 'Human, machine and mixed realization',
     'Accept the listed generalizations from software Code/Events to selected realization/observations and durable work records, with derivability, conformance, execution and resource obligations retained?',
     ['I3-R3-R002', 'I3-R3-R009', 'I3-R2-R042', 'I3-R2-R043', 'I3-R3-R010', 'I3-R2-R044', 'I3-R2-R018', 'I3-R2-R019', 'I3-R3-R011', 'I3-R2-R045', 'I3-R2-R046', 'I3-R2-R039'],
     'Trace required Z, prediction, observation and preservation through material generic consumers; executor choice does not waive independence, authority or observations.'),
    ('Q11', 'Scoped diagnosis at design and ODD entry',
     'Accept each listed narrower diagnostic/trigger conclusion, while preserving its original question families and the ODD acquisition should-strength?',
     ['I3-R3-R003', 'I3-R3-R004'],
     'Check I5 feedback diagnosis at the actual cause/owner instead of treating every unresolved relation as coupling, imperative realization or an unqualified Product diagnosis.'),
    ('Q12', 'Observed effects across domain boundaries',
     'Accept the shared classification of actual, partial, reverted, unintended and unknown effects at the named DMM, ODD, traversal and UX consumers?',
     ['I3-R2-R008', 'I3-R2-R009', 'I3-R2-R031', 'I3-R2-R032'],
     'Reassess observation sufficiency and recovery; unknown effects and intended effects do not prove nonstart, rollback, completion or progress.'),
    ('Q13', 'Assessment, owner disposition and acceptance remain separate',
     'Accept the exact predicate-bound treatment, recorded-decision continuity and release-qualification changes while retaining their distinct decision and acceptance authorities?',
     ['I3-R2-R021', 'I3-R2-R026', 'I3-R2-R017'],
     'Bind I5 evidence retention and changed validity conditions without allowing a record, test result, publication transport or reuse link to grant acceptance.'),
    ('Q14', 'Traversal atomic admission with undecided support',
     'Accept the distinction between missing/held support and established failure while retaining the complete atomic cut, conflict refusal and duplicate policy?',
     ['I3-R2-R030', 'I3-R2-R041'],
     'Check changed assertion/observation dependencies against the exact optional profile; no shared-core change weakens its atomic admission conditions.'),
    ('Q15', 'UX outcome and replay contract',
     'Replace the mandatory binary outcome inventory with the stated extended typed outcomes and replay contract, retaining unknown effects as unknown?',
     ['I3-R3-R016', 'I3-R3-R017'],
     'Reassess I5 observation and replay consumers; replay fidelity alone does not establish completion. The common UX compliance owner decision remains separate.'),
    ('Q16', 'Identity selector follows published Release policy',
     'Accept the Identity projection repair from latest-accepted to highest-ordinal published RC on the stated contradictory predecessor case, preserving separate consumer adoption?',
     ['I4-SELECTOR-CONSERVATION-R001'],
     'Retain the accepted-rc.1/published-unaccepted-rc.2 witness and check I5 current package entry; a fresh pin does not make the changed Identity determination conserved.'),
    ('Q17', 'Compression disposition and material acquisition',
     'Decide the nine exact compression replacements, including withdrawn standalone-sufficiency claims and required acquisition of shared owners; keeping, superseding or removing a carrier remains the owner decision?',
     ['I3-R2-R048', 'I3-R2-R049', 'I3-R2-R050', 'I3-R2-R051', 'I3-R2-R052', 'I3-R2-R053', 'I3-R2-R054', 'I3-R2-R055', 'I3-R2-R056'],
     'Regenerate affected I5 projections after source freeze and assess ordinary acquisition; source-linked generation and shorter output do not establish sufficiency.'),
    ('Q18', 'Current distribution and ordinary work entry',
     'Accept the exact current-installation guide and bounded work-entry replacements, preserving recoverable owner clauses and historical publication facts without implying a current release?',
     ['I3-R2-R058', 'I3-R2-R059'],
     'Check current I5 source/interpretation/qualification entry and unreleased standing; ordinary discovery and supplied-frame actual use retain separate evidence.'),
]


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parser_library():
    # check_conservation imports this parser; verify both selected bytes first.
    library('synthesis/check_artifacts.py')
    return library('iteration-3/check_conservation.py')


def inherited():
    require(INPUTS['common_input'] == COMMON and INPUTS['starting_tenant'] == START,
            'I5 activation basis changed')
    raw = (PRIOR / 'CONSERVATION.json').read_bytes()
    frozen = git_bytes(START, (PRIOR / 'CONSERVATION.json').relative_to(REPO))
    require(raw == frozen and sha(raw) == PRIOR_SHA, 'Historical I4 conservation differs')
    common = git_bytes(COMMON, COMMON_PATH)
    require(sha(common) == COMMON_SHA and common == (REPO / COMMON_PATH).read_bytes(),
            'Common predecessor census differs')
    old = json.loads(raw)
    expected = parser_library().coordinates.common_rows(common.decode())
    validate_rows(old['rows'], expected)
    return old, expected


def validate_rows(rows, expected):
    ids = [row['id'] for row in rows]
    require(len(ids) == 691 and len(set(ids)) == 691 and set(ids) == set(expected),
            'Omitted, extra or duplicate predecessor claim')
    for row in rows:
        require(row['source_member'] == expected[row['id']], 'Predecessor member changed')
    require(Counter(r['disposition'] for r in rows) ==
            {'conserved': 621, 'superseded': 69, 'not applicable': 1},
            'A new disposition requires a separately authored proposal and assessment')


def replacement_questions(rows, source_commit=None, account_commit=None):
    relations = {}
    for row in rows:
        if row['disposition'] != 'superseded':
            continue
        rel = row['successor_relation']
        require(rel['id'] not in relations, 'Duplicate replacement relation')
        require(rel.get('owner_decision') is None and rel['standing'] == 'proposed_pending_owner_decision',
                'Owner decisions cannot be manufactured by this activation')
        require(rel.get('replacement_loci') and rel['predecessor_claim_id'] == row['id'],
                'Replacement relation lacks its exact claim or carrying loci')
        relations[rel['id']] = {'claim': row['id'], 'original_comparison_group': row['comparison_group'],
            'relation': copy.deepcopy(rel), 'dependencies': copy.deepcopy(row.get('shared_replacement_dependencies', [])),
            'owner_dependencies': copy.deepcopy(row.get('replacement_owner_dependencies', []))}
    selected = [rid for _, _, _, ids, _ in QUESTIONS for rid in ids]
    require(len(selected) == len(set(selected)) == 69 and set(selected) == set(relations),
            'Substantive questions omit or overlap a replacement')
    questions = []
    for qid, title, question, ids, consequences in QUESTIONS:
        questions.append({'id': qid, 'title': title, 'question': question,
            'decision': {'status': 'pending', 'record': None},
            'i5_consequences_to_assess': consequences,
            'rows': [relations[rid] for rid in ids]})
    return {'kind': 'stdo.i5.owner-question-input', 'schema_version': 1,
        'common_input': COMMON, 'source_commit': source_commit, 'account_commit': account_commit,
        'inherited_subject': {'handoff': HANDOFF, 'source_commit': '01b01274b244ae6e5de10bf6bacb60087462cbb5',
            'conservation_sha256': PRIOR_SHA},
        'questions': questions,
        'standing': 'Substantive grouping of 69 inherited author proposals. Each exact relation and dependency remains. No owner decision or semantic acceptance; I5 consequences await current source assessment.',
        'decision_rule': 'The common pen consolidates equivalent questions across tenants while retaining per-claim and per-tenant relations. A group is not blanket acceptance; the owner ticket decision must identify accepted changed meanings before dependent acceptance.'}


def prepared(old):
    return {'kind': 'stdo.i5.author-conservation-account', 'schema_version': 4,
        'input_commit': COMMON, 'candidate_source_commit': None, 'candidate_account_commit': None,
        'binding_state': 'awaiting_source_and_account_freeze',
        'preimage': {'commit': START, 'handoff': HANDOFF,
            'path': str((PRIOR / 'CONSERVATION.json').relative_to(REPO)), 'sha256': PRIOR_SHA},
        'source_member_pins': copy.deepcopy(old['source_member_pins']),
        'inherited_coordinates': {'source_commit': old['candidate_source_commit'],
            'successor_member_pins': copy.deepcopy(old['successor_member_pins']),
            'successor_locus_pins': copy.deepcopy(old['successor_locus_pins'])},
        'successor_member_pins': {}, 'successor_locus_pins': {},
        'rows': copy.deepcopy(old['rows']), 'affected_rows': [],
        'standing': 'Preparation only. Rows, their current_review records and carrying coordinates retain their exact I4 subjects. No I5 source binding, semantic assessment, evidence-reuse decision or owner acceptance.',
        'remaining_work': ['Bind the exact frozen I5 documentary source and authored account.',
            'Assess new/changed owners and necessary consumers; author explicit replacement proposals where I5 changes predecessor meaning.',
            'Complete nonauthor semantic conservation through supported retained and new evidence.',
            'Record owner decisions before dependent acceptance; no missing assessment is a pass.']}


def refresh(old, source_commit, account_commit):
    require(source_commit and account_commit, 'Both exact freezes are required')
    _, inventory = exact_source(source_commit)
    account_path = HERE / 'DETERMINATIONS.json'
    account_bytes = git_bytes(account_commit, account_path.relative_to(REPO))
    require(account_bytes == account_path.read_bytes(), 'Account differs from its freeze')
    account = json.loads(account_bytes)
    require(account['subject']['source_commit'] == source_commit and
            account['subject']['common_input'] == COMMON, 'Account source/basis mismatch')
    require(account['source_members'] == inventory, 'Account documentary inventory differs')
    current = prepared(old)
    cc = parser_library()
    members, loci, affected, cache = {}, {}, [], {}
    for row in current['rows']:
        changed = []
        routes = list(dict.fromkeys(row.get('successor_loci', [row.get('successor_locus')]) +
                                   row.get('successor_relation', {}).get('replacement_loci', [])))
        for route in routes:
            if not route:
                continue
            path, _, anchor = route.partition('#')
            relative = Path(path)
            require(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe carrying path')
            if path not in cache:
                body = git_bytes(source_commit, (PACKAGE / relative).relative_to(REPO))
                require(body == (PACKAGE / relative).read_bytes(), 'Carrying member differs from freeze')
                prior = git_bytes(START, (PACKAGE / relative).relative_to(REPO))
                cache[path] = (body, prior)
                members[path] = {'sha256': sha(body), 'bytes': len(body)}
            body, prior = cache[path]
            unit = cc.section_body(body.decode(), anchor).encode()
            previous = cc.section_body(prior.decode(), anchor).encode()
            loci[route] = {'sha256': sha(unit), 'bytes': len(unit), 'member_sha256': sha(body)}
            if unit != previous:
                changed.append(route)
        if row.get('successor_locus'):
            row['successor_sha256'] = members[row['successor_locus'].split('#')[0]]['sha256']
        row['inherited_current_review'] = row['current_review']
        row['current_review'] = {'source_commit': source_commit, 'account_commit': account_commit,
            'standing': 'independent_I5_assessment_not_performed', 'changed_carrying_loci': changed,
            'dependency_impact': 'not_assessed',
            'reuse': 'Historical evidence retains its subject. Direct coordinate comparison is not a complete validity-dependency assessment or semantic reuse decision.'}
        if changed:
            affected.append({'id': row['id'], 'changed_loci': changed, 'disposition': row['disposition']})
    current.update(candidate_source_commit=source_commit, candidate_account_commit=account_commit,
        account_sha256=sha(account_bytes), binding_state='coordinates_bound_assessment_pending',
        successor_member_pins=members, successor_locus_pins=loci, affected_rows=affected,
        standing='Exact I5 coordinates for inherited author dispositions and replacement relations. All original evidence and owner-decision gaps remain. Current carrying completeness, semantic conservation, dependency sufficiency and reuse are unassessed.')
    return current


def frontier(account):
    return {'kind': 'stdo.i5.frontier-projection', 'schema_version': 1,
        'source_commit': account['candidate_source_commit'], 'account_commit': account['candidate_account_commit'],
        'binding_state': account['binding_state'],
        'conservation_sha256': sha((json.dumps(account, indent=2, ensure_ascii=False) + '\n').encode()),
        'rows': [{'id': r['id'], 'disposition': r['disposition'],
            'relation': r.get('successor_relation', {}).get('id'),
            'owner_decision': r.get('successor_relation', {}).get('owner_decision'),
            'inherited_acceptance': r.get('acceptance'),
            'i5_assessment': 'not_performed', 'semantic_reuse': 'not_assessed'} for r in account['rows']],
        'standing': 'Projection of proposals and outstanding work, not acceptance.'}


def artifacts(account):
    return dict(zip(FILES, (account, frontier(account), replacement_questions(account['rows'],
        account['candidate_source_commit'], account['candidate_account_commit']))))


def validate_artifacts(values, old, expected):
    account = values['CONSERVATION.json']
    validate_rows(account['rows'], expected)
    require(account['input_commit'] == COMMON and account['preimage'] == prepared(old)['preimage'],
            'Account preimage or common input changed')
    require(account['source_member_pins'] == old['source_member_pins'], 'Predecessor pins changed')
    require(account['inherited_coordinates'] == prepared(old)['inherited_coordinates'],
            'Historical carrying coordinates changed')
    frozen = {r['id']: r for r in old['rows']}
    for row in account['rows']:
        previous = frozen[row['id']]
        allowed = {'successor_sha256', 'current_review', 'inherited_current_review'}
        require({k: v for k, v in row.items() if k not in allowed} ==
                {k: v for k, v in previous.items() if k not in allowed},
                'Inherited semantic claim, relation or evidence changed: ' + row['id'])
    if account['binding_state'] == 'awaiting_source_and_account_freeze':
        require(account == prepared(old), 'Prepared account drift or invented I5 binding')
    else:
        require(account['binding_state'] == 'coordinates_bound_assessment_pending' and
                account['candidate_source_commit'] and account['candidate_account_commit'],
                'Incomplete current binding')
        for row in account['rows']:
            require(row['inherited_current_review'] == frozen[row['id']]['current_review'],
                    'Historical current-review record changed')
            review = row['current_review']
            require(review['source_commit'] == account['candidate_source_commit'] and
                    review['account_commit'] == account['candidate_account_commit'] and
                    review['standing'] == 'independent_I5_assessment_not_performed' and
                    review['dependency_impact'] == 'not_assessed',
                    'Invented current review or dependency assessment')
    require(values['FRONTIER.json'] == frontier(account), 'Frontier differs from conservation')
    require(values['REPLACEMENT_QUESTIONS.json'] == replacement_questions(account['rows'],
            account['candidate_source_commit'], account['candidate_account_commit']),
            'Replacement grouping, exact relation or owner standing changed')


def self_check(values, old, expected):
    controls = []
    mutations = {
        'omitted_claim': lambda v: v['CONSERVATION.json']['rows'].pop(),
        'duplicate_claim': lambda v: v['CONSERVATION.json']['rows'].append(copy.deepcopy(v['CONSERVATION.json']['rows'][0])),
        'owner_approval': lambda v: v['REPLACEMENT_QUESTIONS.json']['questions'][0]['decision'].update(status='accepted', record='invented'),
        'lost_exact_relation': lambda v: v['REPLACEMENT_QUESTIONS.json']['questions'][0]['rows'].pop(),
        'weakened_meaning': lambda v: v['REPLACEMENT_QUESTIONS.json']['questions'][0]['rows'][0]['relation'].update(changed_meaning='Equivalent'),
        'fabricated_pass': lambda v: v['CONSERVATION.json']['rows'][0]['semantic_review'].update(result='satisfied'),
        'source_pin_drift': lambda v: v['CONSERVATION.json']['source_member_pins'].clear(),
    }
    for name, mutate in mutations.items():
        bad = copy.deepcopy(values)
        mutate(bad)
        try:
            validate_artifacts(bad, old, expected)
        except (ValueError, KeyError, TypeError):
            controls.append(name)
        else:
            raise ValueError('Adverse control was accepted: ' + name)
    return controls


def main():
    p = argparse.ArgumentParser(description=__doc__)
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', action='store_true')
    mode.add_argument('--refresh', action='store_true')
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--self-check', action='store_true')
    p.add_argument('--source-commit')
    p.add_argument('--account-commit')
    args = p.parse_args()
    require(args.refresh or not (args.source_commit or args.account_commit),
            'Freeze arguments belong only to refresh')
    old, expected = inherited()
    if args.check or args.self_check:
        values = {name: read(HERE / name) for name in FILES}
        account = values['CONSERVATION.json']
        if account['binding_state'] != 'awaiting_source_and_account_freeze':
            require(values == artifacts(refresh(old, account['candidate_source_commit'],
                                               account['candidate_account_commit'])),
                    'Current binding does not reproduce from its frozen objects')
    else:
        account = refresh(old, args.source_commit, args.account_commit) if args.refresh else prepared(old)
        values = artifacts(account)
    validate_artifacts(values, old, expected)
    controls = self_check(values, old, expected) if args.self_check else []
    if args.prepare or args.refresh:
        for name in FILES:
            path = HERE / name
            require(not path.is_symlink(), 'Refusing symlink output')
            if path.exists():
                prior = read(path)
                # Never silently overwrite an independently modified account.
                require(prior == values[name] or (args.refresh and prior == artifacts(prepared(old))[name]),
                        'Output differs from the exact prepared preimage: ' + name)
        for name, value in values.items():
            write(HERE / name, value)
    print(json.dumps({'rows': len(values['CONSERVATION.json']['rows']),
        'questions': len(QUESTIONS), 'replacements': 69,
        'binding_state': values['CONSERVATION.json']['binding_state'],
        'adverse_controls_rejected': controls,
        'standing': 'Author structural checks only; semantic review, reuse and owner decisions remain open.'}))


if __name__ == '__main__':
    main()
