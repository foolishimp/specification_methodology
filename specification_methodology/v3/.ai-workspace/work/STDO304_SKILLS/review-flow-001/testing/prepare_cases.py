"""Prepare only the explicitly selected synthetic candidate-premise cases."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
META = json.loads((HERE / 'CANDIDATE.json').read_text())
BASE = Path(META['scratch'])
CANDIDATE = Path(META['candidate'])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    assert not path.exists(), path
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + '\n')


def view(root, selections):
    parts, rows = [], []
    for member, start, end in selections:
        raw = (CANDIDATE / 'standards' / member).read_bytes()
        first = ('\n' + start + '\n').encode()
        last = ('\n' + end + '\n').encode()
        assert raw.count(first) == 1 and raw.count(last) == 1
        a = raw.index(first) + 1
        b = raw.index(last, a) + 1
        body = raw[a:b]
        header = f'\nSource: standards/{member}; whole-member SHA256 {sha(raw)}; bytes [{a},{b}); exact source section below.\n\n'.encode()
        parts.append(header + body)
        rows.append({'member': member, 'start_heading': start, 'end_before': end, 'start_byte': a, 'end_byte': b, 'member_sha256': sha(raw), 'section_sha256': sha(body), 'section_bytes': len(body)})
    data = b''.join(parts)
    path = root / 'basis/OWNER_VIEW.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {'path': str(path), 'sha256': sha(data), 'bytes': len(data), 'sections': rows}


REVIEW = [
    ('EVALUATION.md', '## 3. Independent assessment', '## 5. Acceptance'),
    ('EXECUTIVE_BASELINE.md', '## 10. Derived Reviewer frame', '## 11. Derived generic specialist frame set'),
    ('TICKETS.md', '### Review findings and bug items', '### Lanes'),
]
EXECUTIVE = [
    ('EVALUATION.md', '## 5. Acceptance', '## 6. Conformance of realisations'),
    ('EXECUTIVE_BASELINE.md', '### Technical triage, severity, priority and boundary effect', '### Work result'),
    ('EXECUTIVE_BASELINE.md', '### QA cadence and repair rechecks', '### Promotion constraint projection'),
    ('TICKETS.md', '### Review findings and bug items', '### Lanes'),
    ('ACTIVATION.md', '## 7. Closed result and reuse', '### Transition evidence'),
]

requirements = '''# Export requirements

R-ARITH: Each invoice's net amount is quantity multiplied by unit_price. Tax is net multiplied by tax_rate; every amount in this fixture is exactly representable to two decimal places. Gross is net plus tax. Monetary values are decimal major currency units. Currency is AUD.

R-DATE: invoice_date is the calendar issue date rendered as YYYY-MM-DD, irrespective of the operator's locale. Source issue dates use that format.

R-IDENTITY: Every source invoice_id appears exactly once in the export, with its source quantity, unit_price, tax_rate and currency.
'''
rows = [
    {'invoice_id': 'I-41', 'issue_date': '2026-11-03', 'quantity': 2, 'unit_price': '50.00', 'tax_rate': '0.10', 'currency': 'AUD'},
    {'invoice_id': 'I-42', 'issue_date': '2026-11-03', 'quantity': 1, 'unit_price': '20.00', 'tax_rate': '0.10', 'currency': 'AUD'},
    {'invoice_id': 'I-43', 'issue_date': '2026-11-03', 'quantity': 3, 'unit_price': '10.00', 'tax_rate': '0.10', 'currency': 'AUD'},
]
export = '''invoice_id,invoice_date,quantity,unit_price,tax_rate,currency,net,tax,gross
I-41,2026-11-03,2,50.00,0.10,AUD,100.00,10.00,112.00
I-42,03/11/2026,1,20.00,0.10,AUD,20.00,2.00,22.00
I-43,2026-11-03,3,10.00,0.10,AUD,30.00,3.00,33.00
'''
repaired = export.replace('100.00,10.00,112.00', '100.00,10.00,110.00')
profile = {
    'profile_id': 'invoice-trial-profile-1',
    'standing': 'Synthetic prospective candidate-method premise, admitted only for this procedure forward test. This is not a real installed Product or an adoption operation.',
    'candidate_method': {'source_delta_sha256': META['source_delta_sha256'], 'owner_views': 'basis/OWNER_VIEW.md', 'interpretation': 'The named candidate skill and exact owner clauses are the procedure being evaluated. Installed-Product discovery/verification is a hypothetical prerequisite of the scenario, not an operation performed or claimed by this trial. No installed 3.0.4 exists in this fixture. Evaluate conditional scenario decisions under these explicit premises.'},
    'products': {'producer': 'urn:fixture:invoice-export', 'consumer': 'urn:fixture:archive-entry'},
    'severity_scale': {'S1': 'loss of source identity or widespread irreversible incorrect charging', 'S2': 'incorrect monetary amount for an invoice', 'S3': 'operational failure with a usable workaround', 'S4': 'presentation or format violation without a monetary change'},
    'priority_policy': {'selected': 'candidate Executive baseline Optional P0-P5 response policy', 'assignment': {'P1': 'monetary error in the next export delivery', 'P4': 'date presentation with an unambiguous source-date workaround'}, 'other_assignment': 'Executive records evidence, outcome and reason; no mechanical severity mapping'},
    'review_policy': {'selected': 'candidate Executive baseline QA cadence and repair rechecks', 'ratio': None, 'initial_subject': 'all three invoices and all three export requirements', 'size_reason': 'small complete population; one bounded assessment'},
    'hard_stops': ['H-CAP: capture source-fidelity claim required for publication; its fixed state alone is insufficient while its required recheck is open'],
    'acceptance_gate': {'from': 'urn:fixture:invoice-export', 'to': 'urn:fixture:archive-entry', 'relation': 'published invoice export becomes admitted archive input', 'candidate': 'EXPORT-41', 'claims': ['R-ARITH', 'R-DATE', 'R-IDENTITY'], 'required_review': 'R1 on the whole declared population, plus applicable repairs/rechecks', 'acceptance_conditions': 'all listed requirements satisfied on the exact accepted subject; all required coverage and review closed', 'decision_owner': 'E1 within this hypothetical decision grant'},
    'provisional_operations': ['Archive preview may process exact landed EXPORT-41 while retaining unresolved obligations and dependencies'],
    'landing': {'identity': 'EXPORT-41', 'operation': 'already occurred at the authorised fixture checkpoint', 'extra_review_hold': None},
    'release': 'go-live requires all selected export requirements and retained release items satisfied; no publication operation is granted',
    'carriers': {'issuing_work': 'W-41', 'review_report': 'B-41 at records/B-41.md when findings exist', 'bug_item_ledger': 'W-41 Bug items in the Executive decision payload', 'no_rival_status_surface': True},
}

fixtures = {'source_delta_sha256': META['source_delta_sha256'], 'cases': {}, 'views': []}
for name, skill, wall, budget in [('R1', 'stdo-review', 180, 4), ('E1', 'stdo-status', 240, 5), ('R2', 'stdo-review', 150, 3)]:
    root = BASE / name
    root.mkdir()
    sections = EXECUTIVE if name == 'E1' else REVIEW
    if name == 'R2':
        sections = REVIEW + [('EXECUTIVE_BASELINE.md', '### QA cadence and repair rechecks', '### Promotion constraint projection')]
    v = view(root, sections)
    fixtures['views'].append(v)
    put(root / 'PROFILE.json', profile)
    put(root / 'requirements.md', requirements)
    put(root / 'source-invoices.json', rows)
    put(root / 'export.csv', repaired if name == 'R2' else export)
    put(root / 'metadata.json', {'work_id': 'W-41', 'candidate_id': 'EXPORT-41-fixed' if name == 'R2' else 'EXPORT-41', 'candidate_sha256': sha((repaired if name == 'R2' else export).encode()), 'source_sha256': sha((root / 'source-invoices.json').read_bytes()), 'requirements_sha256': sha(requirements.encode()), 'candidate_constructed_by': 'fixture-author', 'reviewer_author_contribution': 'none; actual actor is fresh and did not construct this artifact', 'historical_fixture_observations': 'Synthetic evidence records are premises of this forward test, not claims of native Worker execution.'})
    controls = ['CONTRACT.json', 'PROFILE.json', 'metadata.json', 'basis/OWNER_VIEW.md']
    artifacts = ['requirements.md', 'source-invoices.json', 'export.csv'] if name != 'E1' else ['fix_frontier.json', 'dependencies.json', 'triage-advice.json', 'incoming/R1.json']
    direct_skill = CANDIDATE / 'plugins/spec/skills' / skill / 'SKILL.md'
    refs = [CANDIDATE / 'plugins/spec/references/COORDINATED_HANDOFF.md', CANDIDATE / 'plugins/spec/references/PRODUCT_BASIS.md']
    result = {'review_markdown': 'complete closed conditional review result', 'bug_report_markdown': 'complete named report payload if this review has findings, otherwise null'} if name != 'E1' else {'decision_markdown': 'complete conditional Executive decision and Bug items payload'}
    grant = {'case': name, 'purpose': 'candidate-procedure forward test over the stated hypothetical Product', 'premise': 'PROFILE.json', 'role': 'Executive' if name == 'E1' else 'Reviewer', 'procedure_skill': str(direct_skill), 'source_views': v['path'], 'source_view_authentication': 'Each exact verbatim slice is checked against the pinned candidate member before launch. The view is the admitted transport for those owner clauses, not another method version.', 'read_paths': [str(root / x) for x in controls + artifacts] + [str(direct_skill)] + [str(x) for x in refs], 'excluded': 'All unlisted paths, parent directories, other actor prompts/results except the declared R1 transport, capture bodies, native project discovery and global state.', 'effects': 'No actor file, shell, Git, network, ticket or publication effects. Return the specified JSON only. An explicitly admitted recorder persists the complete success result and any non-null bug report at the exact destinations below.', 'recorder': {'result': f'records/{name}.json', 'bug_report': f'records/{"B-41" if name == "R1" else "B-42"}.md' if name != 'E1' else None, 'authority': 'test Executive grant; recorder writes verbatim fields only, no independent decisions'}, 'return_json': result, 'subject': 'All R-ARITH, R-DATE and R-IDENTITY obligations for the three source/export rows' if name == 'R1' else ('Current work and boundary decisions in the supplied evidence; authority to select priority/owner/disposition and next already-admitted evaluation within this synthetic mandate; no effects beyond decision return' if name == 'E1' else 'Only R-ARITH for all three repaired export rows; the review is a required independent assessment at the named arithmetic-fix boundary. No overall export acceptance or date-format assessment is delegated.'), 'limits': {'wall_seconds': wall, 'api_budget_usd': budget, 'initial_bytes': 8192, 'distinct_admitted_text_bytes': 65536, 'completed_acquisition_bytes': 131072}, 'stop': 'Missing exact input, unreadable required source, invalidated candidate, exceeded budget, or insufficient evidence: return the bounded unresolved result; do not invent facts.'}
    if name == 'R1':
        grant['return_transport_limit_bytes'] = 8192
    if name == 'E1':
        member = CANDIDATE / 'plugins/spec/references/COORDINATED_HANDOFF.md'
        raw = member.read_bytes()
        slices, extents = [], []
        for start, end in [('## Control Intake', '## Issue'), ('## Evaluate The Return', '## Review Flow From The Selected Basis'), ('## Review Flow From The Selected Basis', '## Host Binding')]:
            a = raw.index(('\n' + start + '\n').encode()) + 1
            b = raw.index(('\n' + end + '\n').encode(), a) + 1
            body = raw[a:b]
            slices.append(f'\nSource: {member}; whole-member SHA256 {sha(raw)}; bytes [{a},{b}); exact section below.\n\n'.encode() + body)
            extents.append({'member': 'plugins/spec/references/COORDINATED_HANDOFF.md', 'start_byte': a, 'end_byte': b, 'member_sha256': sha(raw), 'section_sha256': sha(body)})
        route = root / 'basis/HANDOFF_VIEW.md'
        route.write_bytes(b''.join(slices))
        fixtures['views'].append({'path': str(route), 'sha256': sha(route.read_bytes()), 'bytes': route.stat().st_size, 'sections': extents})
        grant['read_paths'].remove(str(member))
        grant['read_paths'].append(str(route))
        grant['reference_transport'] = {'source': str(member), 'admitted_view': str(route), 'sections': ['Control Intake', 'Evaluate The Return', 'Review Flow From The Selected Basis'], 'reason': 'Exact source-view transport within the declared finite acquisition budget.'}
    if name == 'R2':
        grant['issuing_work'] = 'W-42 arithmetic repair; report B-42 if an in-scope finding exists; all other Product carriers and gates remain unchanged.'
    put(root / 'CONTRACT.json', grant)
    prompt = f'Evaluate the hypothetical scenario using the candidate procedure named in {root / "CONTRACT.json"}. Read that contract first, then its exact skill and admitted source routes. Perform the role and scope it binds and return only the specified JSON.\n'
    put(root / 'PROMPT.txt', prompt)
    fixtures['cases'][name] = {'root': str(root), 'skill': skill, 'wall_seconds': wall, 'budget_usd': budget}

e = BASE / 'E1'
frontier = []
for ident, updates in [
    ('FIX-0', {}),
    ('FIX-B', {'boundary_requires_independent_review': True}),
    ('FIX-H', {'repairs': 'H-CAP source-fidelity capture', 'hard_stop': 'H-CAP', 'original_severity': 'S2', 'assigned_priority': 'P5', 'assigned_priority_reason': 'prior Executive scheduled late; this is a scheduling fact'}),
    ('FIX-N', {'reproducer': None}),
    ('FIX-U', {'prior_review_population': ['A', 'B'], 'declared_review_population': ['A', 'B', 'C']}),
]:
    row = {'id': ident, 'candidate': ident + '-after', 'landing': 'completed under its operation grant', 'claim': 'bounded local repair predicate for ' + ident, 'original_severity': 'S3', 'assigned_priority': 'P2', 'source_report': ident + '-report', 'source_finding': ident + '-finding', 'state': 'fixed', 'reproducer': {'before': 'falsified', 'after': 'satisfied', 'same_claim': True}, 'required_suite': {'scope': 'all tests selected for this repair', 'result': 'satisfied'}, 'prior_review_population': ['A', 'B'], 'declared_review_population': ['A', 'B'], 'boundary_requires_independent_review': False, 'hard_stop': None, 'capture': False, 'other_closure_conditions': 'satisfied in the fixture', 'new_review': None}
    row.update(updates)
    if ident == 'FIX-H': row['capture'] = True
    frontier.append(row)
put(e / 'fix_frontier.json', {'standing': 'synthetic exact current evidence; not native Worker runs', 'repairs': frontier, 'requested_decision': 'For each exact repair, state whether its bounded repair claim may close, its verification provenance, any needed evaluation and the effect on landing/closure/release.'})
put(e / 'dependencies.json', {'current_candidate': 'EXPORT-41', 'results': [{'id': 'D-TOTAL', 'state': 'previously satisfied', 'subject_bytes': 'unchanged', 'depends_on': ['EXPORT-41:I-41:gross'], 'claim': 'Archive preview total equals the invoice arithmetic'}, {'id': 'D-DATE', 'state': 'previously satisfied', 'subject_bytes': 'unchanged', 'depends_on': ['EXPORT-41:I-42:invoice_date'], 'claim': 'Archive preview date uses ISO format'}, {'id': 'D-LOGO', 'state': 'satisfied', 'subject_bytes': 'unchanged', 'depends_on': ['logo-v1:approved-color'], 'claim': 'Approved logo color preserved', 'non_influence_evidence': 'Uses only separately fixed logo bytes and color policy; no invoice data, export code, date or arithmetic dependency'}], 'requested_decision': 'Assess continued reliance and the declared producer-to-consumer gate after the current review.'})
put(e / 'triage-advice.json', {'actor': 'earlier bounded triage Worker fixture', 'standing': 'recommendation from grouping metadata, not a decision', 'source': 'FIX-H-report', 'proposal': {'cause_group': 'capture-transform', 'owner': 'capture-writer', 'priority': 'P5', 'severity': 'S4'}, 'original_reviewer_severity': 'S2', 'original_severity_source': 'FIX-H-report', 'evidence_for_new_severity': None})
put(e / 'excluded/capture.txt', 'Fixture-only withheld capture body. No named actor may acquire this file.\n')
put(HERE / 'FIXTURES.json', fixtures)
print(json.dumps({'roots': fixtures['cases'], 'view_bytes': {Path(x['path']).parts[-3]: x['bytes'] for x in fixtures['views']}}, indent=2))
