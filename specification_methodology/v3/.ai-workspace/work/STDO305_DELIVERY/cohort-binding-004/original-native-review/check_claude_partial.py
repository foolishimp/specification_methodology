from pathlib import Path
import hashlib, json, time, itertools

R = Path('/Users/jim/src/apps/specification_methodology')
D = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills'
Q = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-004')
C = Q / 'hosts/claude/cases'
E = D / 'installed-qualification-022/executions/claude-native-session'
O = Path(__file__).parent
seen = {}
def sha(b): return hashlib.sha256(b).hexdigest()
def raw(p):
    p = Path(p)
    b = p.read_bytes()
    seen[str(p)] = {'path': str(p), 'bytes': len(b), 'sha256': sha(b)}
    return b
def read(p): return json.loads(raw(p))
def ref(z):
    p = Path(z['path'])
    if not p.is_absolute(): p = R / p
    b = raw(p)
    assert sha(b) == z['sha256'], p
    assert len(b) == z.get('bytes', len(b)), p
    return p
def refs(z):
    if isinstance(z, dict):
        if set(('path', 'sha256')) <= z.keys(): ref(z)
        else:
            for v in z.values(): refs(v)
    elif isinstance(z, list):
        for v in z: refs(v)

started = time.time_ns()
frontier = read(E / 'FAILED_FRONTIER.json')
assert sha(raw(E / 'FAILED_FRONTIER.json')) == 'b6a3f255e2ed9b5b2177d544ac81a319687a6e8cf0a43759bbcb733ba8e18c63'
proposal = read(E / 'PROPOSED_REPORT_ONLY.json')
assert sha(raw(E / 'PROPOSED_REPORT_ONLY.json')) == 'eee73d1a3ba2b6c8a1246a600ccb8beff6c1de575151f17a20f3420d8d1cd911'
# Small exact evidence references only. No support-tree or native payload inventory scan.
refs(frontier)
refs(proposal)
process = read(E / 'result.json')
invocation = read(E / 'invocation.json')
refs(invocation['inputs'])
assert process['timed_out'] and process['returncode'] == 143
assert process['elapsed_seconds'] == 900.59747
assert not process['remaining_known_groups'] and not process['unresolved_cleanup']
assert process['cleanup_actions'] == [{'group': 92472, 'sent': True, 'signal': 'SIGTERM'}]
assert invocation['wall_timeout_seconds'] == 900
assert invocation['requested_model'] == 'opus' and invocation['requested_effort'] == 'xhigh'
assert invocation['environment_additions']['STDO_STORE'].endswith('deliberately-unselected-store')
assert not (C / 'HOST_RETURN.md').exists()
rows = [json.loads(s) for s in raw(C / 'native-session.stdout.jsonl').decode().splitlines()]
assert sha(raw(C / 'native-session.stdout.jsonl')) == '49074ac94d961f8c8ceffd63b0650577c6a6380b7b5543060f4610f1fcc617a5'
assert not any(z.get('type') == 'result' for z in rows)
assert rows[0]['model'] == 'claude-opus-5-5'
calls = [(i, x) for i, z in enumerate(rows) for x in z.get('message', {}).get('content', []) if x.get('type') == 'tool_use']
assert calls[0][1]['name'] == 'Read'
assert calls[0][1]['input']['file_path'] == str(C / 'WORKER_INTAKE.json')

selected = read(C / 'SELECTION.json')
intake = read(C / 'REVIEW_INTAKE.json')
review = read(C / 'REVIEW_RETURN.json')
assert all(k in review for k in intake['required_return_fields']) and len(intake['required_return_fields']) == 15
ref(intake['candidate']); ref(intake['product'])
assert review['verdict']['core_value'] == 'falsified'
assert review['triage']['findings'][0]['severity'] == 1
candidate = raw(C / 'review/candidate.py')
ns = {}; exec(compile(candidate, '<frozen-admission-candidate>', 'exec'), ns)
counterexamples = []
for v in itertools.product([False, True], repeat=3):
    if bool(ns['admitted'](*v)) and not all(v): counterexamples.append(list(v))
assert counterexamples == [[False, True, True], [True, False, True]]
assert 'only if an established downstream guard' in review['triage']['findings'][0]['severity_rationale']
assert 'rests on the absence' in review['uncertainty']['severity']
native_severity = raw(Q / 'store/releases/v3.0.5/standards/EXECUTIVE_BASELINE.md').decode()
assert '| 2 | Major failure of essential behaviour, with substantial affected users, paths or dependencies and no adequate ordinary containment.' in native_severity
assert review['independence']['context_isolation'].startswith('not established')

project = read(C / 'project-run/calls/06-status.stdout')
assert project['status'] == 'built' and project['pending'] == []
assert project['method']['manifest_sha256'] == '9304727d370ae58a0b955d1f831ee15e8dddeb2ca3e8886454233a8422846142'
assert project['result']['formal_gate']['status'] == 'not_performed'
for stem in ['01-prepare', '02-task', '03-submit', '04-task-after-submit', '05-build', '06-status']:
    assert raw(C / f'project-run/calls/{stem}.rc').strip() == b'0'
    argv = raw(C / f'project-run/calls/{stem}.argv').decode().splitlines()
    assert argv[0] == str(Q / 'dependencies/graphify/venv/bin/python')
    if stem == '01-prepare': assert argv[argv.index('--stdo') + 1] == str(Q / 'anchors/claude/stdo')
    raw(C / f'project-run/calls/{stem}.stdout')
for relative, digest in project['result']['files'].items():
    assert sha(raw(C / 'project-run/run' / relative)) == digest
source_manifest = read(C / 'project-run/run/source-manifest.json')
for z in source_manifest['files']:
    assert sha(raw(C / 'project' / z['path'])) == z['sha256']
assert source_manifest['definition_sha256'] == sha(raw(C / 'project/Product.json'))
answer = read(next((C / 'answers').glob('*.json')))
constraints = {z['key']: z for z in answer['constraints']}
assert 'all three of' in constraints['delivery_requires_all_prerequisites']['statement']
assert 'must be reconciled before a new attempt' in constraints['reconcile_uncertain_effect_before_new_attempt']['statement']
assert any(z['key'] == 'host_permission_setting_unresolved' for z in answer['residuals'])
inspection = read(C / 'project-run/formal-inspection/stdout.json')
assert inspection['status'] == 'consistent'
assert inspection['evidence']['result_sha256'] == 'd1386aab366b74939315168c724a8c7709651b8c66efebb64c32daffb159d3bc'
assert raw(C / 'project-run/formal-inspection/rc').strip() == b'0'
assert raw(C / 'project-run/formal-inspection/argv.txt').decode().splitlines() == selected['formal_inspection_argv']
view_summary = read(C / 'project-run/formal-inspection/native-work-view-summary.json')
assert view_summary['included_count'] == 21
assert view_summary['host_residual']['id'] == selected['required_host_residual']
assert len(view_summary['required_relations']) == 3

responses = {}
for case in ['missing-issuer', 'missing-recipient', 'uncertain']:
    case_ref = read(C / case / 'CASE.json')
    for k in ('configuration', 'policy', 'provider'): ref(case_ref[k])
    for folder in sorted((C / case / 'calls').iterdir()):
        e = read(folder / 'execution.json')
        for k in ('configuration', 'policy', 'producer', 'request', 'stdout', 'stderr'): ref(e[k])
        assert not e['timed_out']
        assert e['argv'][0] == str(Q / 'dependencies/graphify/venv/bin/python')
        responses[f'{case}/{folder.name}'] = read(folder / 'stdout.json')
    read(C / case / 'observations/RESULT.json')
    if case != 'uncertain':
        assert not list((C / case / 'workspace/outputs').iterdir())
        assert not list((C / case / 'evidence/events').glob('*.json'))
        assert not list((C / case / 'evidence/requests').glob('*.attempt.json'))
        assert not list((C / case / 'evidence/attempts').glob('*'))
issuer = responses['missing-issuer/001-dispatch.start-issuer-denied']
assert issuer['status'] == 'refused' and issuer['refusal']['code'] == 'authority_missing'
assembled = responses['missing-recipient/001-context.assemble']
pf = responses['missing-recipient/002-contract.preflight']
assert pf['status'] == 'ok' and pf['result']['value']['decision'] == 'rejected'
assert pf['result']['value']['context'] == assembled['result']['artifact']
dispatch = responses['missing-recipient/003-dispatch.start']
assert dispatch['refusal']['code'] == 'authority_missing'
assert pf['result']['artifact'] in dispatch['refusal']['gaps']
assert read(C / 'missing-recipient/requests/003-dispatch.start.request.json')['arguments']['preflight'] == pf['result']['artifact']
retry = responses['uncertain/003-dispatch.start-selected-retry-probe']
assert retry['status'] == 'error' and retry['refusal']['code'] == 'effect_unreconciled'
before = responses['uncertain/002-dispatch.observe']['result']['value']
after = responses['uncertain/004-dispatch.observe-after-probe']['result']['value']
assert before == after and before['effect']['value'] == 'completion_unknown'
assert before['process_end']['returncode'] == 0 and not before['effect']['end_established']
assert raw(C / 'uncertain/workspace/outputs/count') == b'1'
assert len(before['events']) == 8 and before['cursor'] == 8
retry_calls = [(i, x) for i, x in calls if x['name'] == 'Bash' and 'record_public_call.py' in x['input']['command'] and '--request' in x['input']['command'] and '/retry-request.json' in x['input']['command']]
assert len(retry_calls) == 1

def command(i):
    return next(x['input']['command'] for n, x in calls if n == i and x['name'] == 'Bash')
assert 'find cases -maxdepth 3' in command(14)
assert 'mkdir -p ../cases/review-observations' in command(678)
assert '> /tmp/claude-review-verify.$$' in command(678)
assert 'rmdir review-observations' in command(678)
assert 'cat -n REQUIREMENT.md' in command(702)
assert '--store $STORE' in command(725)
assert '--store' not in command(757)
assert 'candidate.py' in command(788)
assert '-m json.tool REVIEW_INTAKE.json' in command(645)
assert 645 < 702 < 788
assert not (C / 'review-observations').exists()

for p in [R / 'stdo_skills/specification/RELEASE_3_0_5.md', R / 'stdo_skills/specification/requirements/README.md', D / 'installed-qualification-prep-017/CASE_CONTRACTS.json', D / 'installed-qualification-prep-022/NATIVE_HOST_BOUND.json']:
    raw(p)
for path, z in seen.items():
    assert sha(Path(path).read_bytes()) == z['sha256'], ('changed during review', path)

report = {
    'schema': 'stdo305.independent-claude-interrupted-host-review/1',
    'assessor': '/root/stdo305_integration_review',
    'authors': ['/root/stdo305_tools_skills', '/root/stdo305_release_tools', '/root/stdo305_representation'],
    'started_ns': started, 'ended_ns': time.time_ns(),
    'native': 'd1f13c53ab733a73993615498f66251041a74073',
    'frontier': seen[str(E / 'FAILED_FRONTIER.json')],
    'proposal': seen[str(E / 'PROPOSED_REPORT_ONLY.json')],
    'conclusion': 'Original Claude session incomplete. Valid completed case evidence retained. Report-only recovery is permitted in principle, but the proposed Worker-only return cannot by itself close the unsupported part of the Reviewer severity derivation.',
    'release_source_findings': [],
    'process': {'returncode': 143, 'timed_out': True, 'elapsed_seconds': 900.59747, 'known_groups_absent': process['known_groups'], 'cleanup': process['cleanup_actions'], 'limit': 'Known observed groups only; unobserved/reparented descendant settlement is not established.'},
    'review_probe_notes': 'Three scratch-only assertions were corrected after reading the actual retained formats: refusal gap is an artifact object, the single retry uses a case-local shell variable, and intake was read by Bash/json.tool rather than Read. No Product source, trial evidence or expected case predicate changed; final assertions cover the actual forms.',
    'established': {
        'project': 'Actual public prepare/task/submit/build/status, terminal task with no pending work, exact nominated A4 basis, selected venv and fixed-store launcher. All published proposal file hashes match. Sampled author constraints retain all three prerequisites, unresolved effect and host residual. This is not exhaustive semantic acceptance.',
        'formal': 'Actor actually ran owner inspect-evidence during the session: project-run/formal-inspection, not merely the earlier prepared proof-inspection. Current installed full result consistent, no new host proof; current21 summary preserves the three nested relations and required host residual.',
        'controls': 'Distinct issuer policy refuses dispatch; recipient context is assembled but preflight rejected and its returned rejected receipt is refused by dispatch. No recipient output/attempt/event. One uncertain retry is held(effect)/effect_unreconciled; original count1 and identical eight-event observations. No policy repair or fabricated reconciliation.',
        'review': 'Reviewer intake then requirement then operator candidate; independent in-memory check reproduces both one-grant counterexamples. All15 required fields, same-process prior context disclosed, no candidate authorship/priority/disposition.',
        'model': 'Requested opus/xhigh; actual native init and assistant metadata expose claude-opus-5-5. Exact effective effort is not exposed.'
    },
    'remaining_required': [
        'HOST_RETURN.md and final CLI result are absent. The original session must remain incomplete.',
        'Actor explanation of each of the five checked proof obligations is not present as a completed return; the successful inspector and current21 summary are retained inputs for it.',
        'REVIEW_RETURN.json:78 misstates the S2 anchor as requiring a downstream recheck; :113 explicitly bases S1 on absent established containment. Selected EXECUTIVE_BASELINE.md:479 instead permits S2 with no adequate ordinary containment. Correct the rationale without demanding a particular number. S1 may be defensible for essential authority failure within the selected unit; unknown downstream reach alone is not evidence of maximal impact.'
    ],
    'operational_limits': [
        'WORKER_INTAKE read first. Raw event14 lists all case filenames before Reviewer intake; no candidate bytes were acquired then. Full Receive-order/acquisition-frontier compliance is not established.',
        'Raw event678 created/removed an empty review-observations directory and /tmp/claude-review-verify.<pid>, despite Reviewer permission for only REVIEW_RETURN/HOST_RETURN writes. Actual bounded grant deviation remains; no general strict write-territory compliance claim. The script output supports removal, but no universal filesystem audit is claimed.',
        'Redundant --store in compact native example was refused by the selected fixed-store launcher. Host inspected the launcher and removed only the redundant option. Same manager/store and Product basis remained; wrong ambient store did not redirect.',
        'The author reported a fixed generation prompt calculus-basis string 2.5.1-rc.2 alongside an exact Product binding 3.0.5. This bounded review records that exposure; actual Product basis stayed A4 and no new basis adoption is inferred.',
        'Same-process Worker/Reviewer context, no clean-room or cross-family guarantee; selected semantic examples do not qualify general instruction adherence.',
        'No new source defect inferred from timeout or actor behavior. No source edits, compiler, support scan, model session, browser or Git effects by this Reviewer.'
    ],
    'supported_recovery': {
        'basis': 'SK-08 preserves valid evidence after interruption; SK-09 leaves incomplete work visible. Current release contract selects completed fresh cases, not one uninterrupted successful process. NATIVE_HOST_BOUND returns failures to Root and forbids automatic retry.',
        'requires_root_assignment': True,
        'conditions': [
            'New explicit bounded activation references the original invocation/process/timeout and this exact frontier; original raw stream, return, refusals and case evidence remain immutable.',
            'Operator revalidates the selected small input/CONFIG/manifest/runtime/receipt identities and observes no surviving known group; this is not reconciliation of the separately uncertain application effect.',
            'No project, dispatch, retry, reconciliation, proof or support rerun. Only exact named input reads and new named report outputs; fresh finite supervision and actual model metadata recorded.',
            'A distinct Reviewer addendum must correct/reaffirm the severity derivation against the selected source, leaving the original report/grade intact. No forced S3 or any forced grade. A Worker reporting grant cannot silently regrade.',
            'Complete HOST_RETURN explains all five structural claims, original timeout and correction history, completed versus missing predicates, actual effect counts, source/host residuals and separate requested/observed model identity.',
            'Any successor is reporting/review completion through recovery; original 900-second trial remains incomplete and cost includes both invocations. Perfect Receive ordering and strict original write-boundary compliance remain unqualified.'
        ],
        'proposal_as_written': 'PROPOSED_REPORT_ONLY allows only HOST_RETURN and explicitly forbids regrading/review revision. It is sufficient for reporting, not for the remaining supported-severity obligation unless that obligation receives a separate explicit Reviewer activation/addendum.',
        'whole_new_session_required': False
    },
    'files_before_after': list(seen.values())
}
p = O / 'CLAUDE_PARTIAL_REVIEW.json'
p.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
print(json.dumps({'path': str(p), 'sha256': sha(p.read_bytes()), 'checked_selected_refs': len(seen), 'source_findings': [], 'standing': 'original session incomplete; bounded recovery recommended with explicit Reviewer addendum'}, indent=2))
