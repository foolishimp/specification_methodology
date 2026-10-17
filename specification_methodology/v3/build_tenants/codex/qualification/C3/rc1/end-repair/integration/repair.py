"""End-review coordinates over the pinned existing RC1 compiler and renderers."""
import argparse
import collections
import copy
import importlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parents[1] / 'integration'
spec = importlib.util.spec_from_file_location('rc1', PRIOR / 'rc1.py')
rc1 = importlib.util.module_from_spec(spec)
sys.modules['rc1'] = rc1
spec.loader.exec_module(rc1)
INPUTS = rc1.read(HERE / 'INPUTS.json')
if rc1.sha(rc1.authenticate(INPUTS['starting_tenant'], PRIOR / 'rc1.py')) != INPUTS['adapter_sha256']:
    raise ValueError('Unselected existing adapter')
rc1.HERE, rc1.INPUTS = HERE, INPUTS
PACKAGE, TENANT, REPO = rc1.PACKAGE, rc1.TENANT, rc1.REPO
UX = ['UX_METHOD.4a-process-model-without-language-or-framework-mandate',
      'UX_METHOD.12-realization-discretion', 'UX_METHOD.18-canonical-compression']
CALLS = {**{'CARRIER.plugins.spec.skills.' + name + '.SKILL.md':
           'CARRIER.plugins.spec.references.PRODUCT_BASIS.md'
           for name in ['stdo-help', 'stdo-review', 'stdo-status', 'stdo-ticket']},
         'CARRIER.plugins.spec.claude-skills.refresh.SKILL.md': 'CARRIER.plugins.spec.references.REFRESH.md'}


def account(args, context, build):
    source, inventory = build.documentary_inventory(rc1.exact(args.source_commit))
    rc1.authenticate(source, HERE / 'INPUTS.json')
    prior_raw = rc1.frozen(INPUTS['prior_account_commit'], PRIOR / 'DETERMINATIONS.json')
    prior = json.loads(prior_raw)
    patch = json.loads(rc1.authenticate(source, HERE / 'ACCOUNT_PATCH.json'))
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    old = {p: rc1.frozen(INPUTS['prior_source_commit'], PACKAGE / p) for p in paths}
    current = {p: (PACKAGE / p).read_bytes() for p in paths}
    integrator = importlib.import_module('reconcile_account')
    integrator.INPUTS = INPUTS
    result, report = integrator.integrate(prior, old, current, [patch], source)
    inverse = {r['id']: [] for r in result['determinations']}
    for row in result['determinations']:
        for target in row.get('dependencies', []):
            inverse[target].append(row['id'])
    normalized = []
    for row in result['determinations']:
        consumers = sorted(set(inverse[row['id']]))
        if row.get('consumers') != consumers:
            normalized.append({'id': row['id'], 'before': row.get('consumers'), 'after': consumers})
        row['consumers'] = consumers
    observations = json.loads(rc1.frozen(INPUTS['prior_check_commit'], PRIOR / 'CONSUMER_RELATIONS.json'))
    rc1.write(HERE / 'CONSUMER_OBSERVATIONS.json', {
        'historical_commit': INPUTS['prior_check_commit'],
        'historical_path': str((PRIOR / 'CONSUMER_RELATIONS.json').relative_to(TENANT)),
        'retained_unmatched_positive_pairs': observations['retained_unmatched_positive_pairs'],
        'current_inverse_normalization': normalized,
        'standing': 'Historical source-use observations remain unresolved. Removing them from the exact inverse field does not show source absence or complete material consumer coverage.'})
    result['source_members'] = inventory
    result['subject'].update(activation='RC1-INTEGRATION-END-REPAIR', source_commit=source)
    result['standing'] = 'Current end-repair authored account; independent fidelity, coverage and owner decisions remain open.'
    report.update(prior_account_commit=INPUTS['prior_account_commit'], prior_account_sha256=rc1.sha(prior_raw),
                  patch_commit=source, inverse_normalization_rows=len(normalized))
    rc1.write(HERE / 'DETERMINATIONS.json', result)
    rc1.write(HERE / 'ACCOUNT_INTEGRATION.json', report)
    print(json.dumps({'rows': len(result['determinations']), 'authored_updates': len(report['direct_patches']),
                      'inverse_normalization_rows': len(normalized)}))


def conservation(args, context, build):
    prior_raw = rc1.frozen(INPUTS['starting_tenant'], rc1.I5 / 'CONSERVATION.json')
    old = json.loads(prior_raw)
    result = copy.deepcopy(old)
    rows = {r['id']: r for r in result['rows']}
    parser = context.library('iteration-3/check_conservation.py')
    changes = rc1.read(HERE / 'CONSERVATION_CHANGES.json')
    for item in changes['supersessions']:
        row = rows[item['claim']]
        row['prior_disposition'] = row['disposition']
        row.update(disposition='superseded', reason=item['changed_meaning'], successor_loci=item['replacement_loci'])
        row['successor_relation'] = {k: v for k, v in item.items() if k != 'claim'}
        row['successor_relation'].update(predecessor_claim_id=item['claim'],
            standing='proposed_pending_owner_decision', owner_decision=None,
            remaining_condition='Separate owner acceptance and independent semantic assessment remain open.')
        row['semantic_review'] = {'result': 'indeterminate', 'scope': 'End-review author supersession proposal.',
                                  'remaining_obligations': ['Assess the exact changed obligation and all carrying loci; obtain the reserved owner decision.']}
    ticket = rows['TICKET_METHOD.md#execution-contract-admission']
    ticket['successor_relation']['changed_meaning'] += ' ' + changes['ticket_extension']
    ticket['reason'] = ticket['successor_relation']['changed_meaning']
    for identifier in UX:
        row = rows['UX_METHOD.md#' + identifier.removeprefix('UX_METHOD.')]
        row['policy_residual'] = copy.deepcopy(changes['ux_reserved_question'])
        row['acceptance'] = 'preserved_source_pending_compliance_owner_decision_and_fidelity'
    member_pins, locus_pins, sources = {}, {}, {}
    for row in result['rows']:
        routes = list(dict.fromkeys(row.get('successor_loci', [row.get('successor_locus')]) +
                                   row.get('successor_relation', {}).get('replacement_loci', [])))
        row['review_history'] = [*row.get('review_history', []), row.get('current_review', {})]
        for route in filter(None, routes):
            path, _, anchor = route.partition('#')
            if path not in sources:
                sources[path] = rc1.authenticate(args.source_commit, PACKAGE / path)
            raw = sources[path]
            if route not in locus_pins:
                body = parser.section_body(raw.decode(), anchor).encode() if anchor else raw
                member_pins[path] = {'sha256': rc1.sha(raw), 'bytes': len(raw)}
                locus_pins[route] = {'sha256': rc1.sha(body), 'bytes': len(body), 'member_sha256': rc1.sha(raw)}
        if row.get('successor_locus'):
            row['successor_sha256'] = locus_pins[row['successor_locus']]['sha256']
        row['current_review'] = {'source_commit': args.source_commit, 'account_commit': args.account_commit,
            'standing': 'current_affected_readback_pending' if row['id'] in changes['affected_claims'] else 'historical_scope_only_no_new_assessment',
            'reuse': 'Exact current loci are bound. Earlier evidence retains its subject and limits; no owner acceptance or unassessed fidelity is inferred.'}
    result.update(candidate_source_commit=args.source_commit, candidate_account_commit=args.account_commit,
        binding_state='exact_current_source_and_account', pin_state='frozen',
        preimage={'commit': INPUTS['starting_tenant'], 'path': str((rc1.I5 / 'CONSERVATION.json').relative_to(TENANT)),
                  'sha256': rc1.sha(prior_raw), 'candidate_source_commit': old['candidate_source_commit']},
        successor_member_pins=member_pins, successor_locus_pins=locus_pins,
        account_sha256=rc1.sha((HERE / 'DETERMINATIONS.json').read_bytes()), affected_rows=changes['affected_claims'],
        standing='Current authored successor conservation account; supersession proposals and reserved decisions remain unaccepted.')
    proposal_input = {'path': str((HERE / 'CONSERVATION_CHANGES.json').relative_to(TENANT)),
        'sha256': rc1.sha(rc1.authenticate(args.source_commit, HERE / 'CONSERVATION_CHANGES.json')),
        'raw_source_commit': args.source_commit, 'standing': 'Explicit end-review author proposals; no owner acceptance.'}
    result['proposal_inputs'] = [*result['proposal_inputs'], proposal_input]
    result['semantic_sha256'] = parser.semantic_sha(result)
    rc1.write(HERE / 'CONSERVATION.json', result)
    rc1.write(HERE / 'FRONTIER.json', parser.frontier_for(result))
    questions = json.loads(rc1.frozen(INPUTS['starting_tenant'], rc1.I5 / 'REPLACEMENT_QUESTIONS.json'))
    questions.update(source_commit=args.source_commit, account_commit=args.account_commit,
                     inherited_subject={'commit': INPUTS['starting_tenant'], 'path': str((rc1.I5 / 'REPLACEMENT_QUESTIONS.json').relative_to(TENANT))})
    for question in questions['questions']:
        for member in question.get('rows', []):
            if member.get('relation', {}).get('id') == 'I3-R2-R025':
                member['relation'] = copy.deepcopy(ticket['successor_relation'])
                question['end_repair_consequence'] = changes['ticket_extension']
    for item in changes['supersessions']:
        questions['questions'].append({'id': item['id'].replace('-R', '-Q'), 'title': item['claim'],
            'question': item['changed_meaning'], 'decision': {'status': 'pending', 'record': None},
            'rows': [{'claim': item['claim'], 'relation': copy.deepcopy(rows[item['claim']]['successor_relation'])}]})
    questions['reserved_compliance_question'] = changes['ux_reserved_question']
    questions['proposal_inputs'] = [*questions['proposal_inputs'], proposal_input]
    questions['standing'] = 'Current proposal questions; no owner decision inferred from construction or review.'
    rc1.write(HERE / 'REPLACEMENT_QUESTIONS.json', questions)
    return result, questions


def projections(args, build):
    directory = HERE / 'interpretation/projections'
    directory.mkdir(parents=True, exist_ok=True)
    binding = subprocess.run([sys.executable, '-B', str(PACKAGE / 'interpretation/bindings.py'),
                              '--theory-root', str(args.theory_root)], capture_output=True, check=True)
    (directory / 'bindings.json').write_bytes(binding.stdout)
    cases = [('workflow-and-ux-residuals', ['CARRIER.plugins.spec.skills.stdo-help.SKILL.md', *UX],
              'CARRIER.plugins.spec.references.PRODUCT_BASIS.md'),
             ('manual-refresh', ['CARRIER.plugins.spec.claude-skills.refresh.SKILL.md'],
              'CARRIER.plugins.spec.references.REFRESH.md')]
    observations = []
    for name, identifiers, target in cases:
        output = directory / (name + '.json')
        command = [sys.executable, '-B', str(build.TOOL), 'project', '--program', str(PACKAGE / 'interpretation/program.json'),
                   '--map', str(PACKAGE / 'interpretation/map.json'), '--bindings', str(directory / 'bindings.json'),
                   '--mode', 'materialized', '--output', str(output)]
        for identifier in identifiers:
            command += ['--frame-index', build.NS + 'index:' + identifier]
        started = time.monotonic()
        run = subprocess.run(command, capture_output=True, text=True)
        if run.returncode:
            raise ValueError(run.stdout + run.stderr)
        value = rc1.read(output)
        populations = {'clauses': set(), 'residuals': set()}
        def collect(item):
            if isinstance(item, dict):
                for key, child in item.items():
                    if key in populations and isinstance(child, list):
                        populations[key].update(v['uri'] for v in child if isinstance(v, dict) and 'uri' in v)
                    collect(child)
            elif isinstance(item, list):
                for child in item:
                    collect(child)
        collect(value)
        if build.clause_id(target) not in populations['clauses']:
            raise ValueError('Native projection omitted the required procedure: ' + target)
        expected = {build.NS + 'residual:' + i + ':known-compliance-test-ambiguity' for i in UX} if UX[0] in identifiers else set()
        if not expected.issubset(populations['residuals']):
            raise ValueError('Native projection lost a selected source residual')
        observations.append({'case': name, 'selected_indexes': identifiers, 'mode': 'materialized',
            'required_procedure_present': target, 'required_residuals_present': sorted(expected),
            'bytes': output.stat().st_size, 'sha256': rc1.sha(output.read_bytes()),
            'elapsed_seconds': time.monotonic() - started, 'command': command, 'exit_code': run.returncode})
    rc1.write(HERE / 'NATIVE_PROJECTIONS.json', {'package_commit': args.package_commit, 'observations': observations,
        'standing': 'Existing native acquisition and residual retention for these selected routes; no task applicability or execution permission inferred.'})


def verify(args, context, build):
    account = rc1.bind_account(args, build)
    rc1.authenticate(args.source_commit, HERE / 'INPUTS.json')
    for path in [Path(__file__), HERE / 'interpretation/GENERATION.json', HERE / 'CONSERVATION.json', HERE / 'REPLACEMENT_QUESTIONS.json']:
        rc1.authenticate(args.package_commit, path)
    for name in ['validation.json', 'DEPENDENCY_VERIFICATION.json', 'QUALIFICATION_EQUIVALENCE.json']:
        rc1.authenticate(args.package_commit, HERE / 'interpretation' / name)
    generation = rc1.read(HERE / 'interpretation/GENERATION.json')
    if generation['document_source_input_commit'] != args.source_commit or generation['account_input_commit'] != args.account_commit or generation['native_validation'] != 'passed':
        raise ValueError('Generation does not bind the current frozen inputs')
    current, _ = build.semantic_projection(account)
    if current != rc1.read(PACKAGE / 'interpretation/source-account.json'):
        raise ValueError('Packaged account differs from frozen authored account')
    members = context.members()
    prefix = str(PACKAGE.relative_to(REPO)) + '/'
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', args.package_commit, '--', str(PACKAGE.relative_to(REPO))], cwd=REPO, text=True).splitlines()
    if {n[len(prefix):] for n in names} != {m['path'] for m in members}:
        raise ValueError('Frozen package membership differs')
    for member in members:
        rc1.authenticate(args.package_commit, PACKAGE / member['path'])
    entry = json.loads(rc1.authenticate(args.source_commit, HERE.parent / 'entry/RETURN.json'))
    if rc1.sha((HERE.parent / 'entry/RETURN.json').read_bytes()) != INPUTS['entry_return_sha256']:
        raise ValueError('Different closed ENTRY return')
    for change in entry['changes']:
        if rc1.sha((REPO / change['path']).read_bytes()) != change['candidate_sha256']:
            raise ValueError('Closed ENTRY carrier changed')
    for name in ['spec_method.compressed.md', 'stdo_compressed.md']:
        text = (PACKAGE / 'standards/authority_compressions' / name).read_text()
        expected = ['Return evidence, a core verdict', 'and a proposed disposition: `accept` maps to `satisfied`',
                    '`falsified` for a demonstrated defect or `indeterminate` for inadequate',
                    '`re_enter` maps to `falsified` for a defeated candidate',
                    '`invalid_basis` for an unusable governing basis',
                    '`reject` maps to `falsified` for a governing-relation violation',
                    'its separate decision result never overwrites the assessment']
        if any(fragment not in text for fragment in expected):
            raise ValueError('Reason-sensitive owner mapping lost in ' + name)
    check = context.library('synthesis/check_artifacts.py').Check()
    check.links_and_surface(); check.compressions(); check.ownership_signals()
    if check.failures:
        raise ValueError(str(check.failures))
    unchanged = []
    for member in members:
        name = member['path']
        if (name.startswith('standards/') and not name.startswith('standards/authority_compressions/')):
            rc1.authenticate(INPUTS['prior_package_commit'], PACKAGE / name)
            unchanged.append(name)
    prior_identity = rc1.frozen(INPUTS['prior_check_commit'], PRIOR / 'IDENTITY_CHECK.json')
    if not json.loads(prior_identity)['valid']:
        raise ValueError('No successful identity evidence to reuse')
    rows = {r['id']: r for r in account['determinations']}
    inverse = {identifier: set() for identifier in rows}
    for row in rows.values():
        for target in row.get('dependencies', []):
            inverse[target].add(row['id'])
    if any(sorted(inverse[i]) != rows[i]['consumers'] for i in rows):
        raise ValueError('Consumers field is not the exact authored inverse')
    for identifier, target in CALLS.items():
        relations = [r for r in rows[identifier]['dependency_relations'] if r['id'] == target]
        if len(relations) != 1 or relations[0]['kind'] != 'contract_application' or relations[0]['required_when'] != 'within the declared applicability':
            raise ValueError('Selected procedure lacks its typed acquisition contract')
    for identifier in UX:
        row = rows[identifier]
        if len(row['source_residuals']) != 1 or 'UX_METHOD.1a-constitutional-authority-rule' not in row['dependencies']:
            raise ValueError('Known UX ambiguity lost its source-owned fail-closed route')
    mapping = rc1.read(HERE / 'CONSERVATION.json')
    if len(mapping['rows']) != 691 or len({r['id'] for r in mapping['rows']}) != 691:
        raise ValueError('Conservation population differs')
    counts = dict(collections.Counter(r['disposition'] for r in mapping['rows']))
    if counts != {'conserved': 606, 'superseded': 84, 'not applicable': 1}:
        raise ValueError('Conservation disposition counts differ from the three selected proposals')
    proposals = {r['successor_relation']['id'] for r in mapping['rows'] if r['disposition'] == 'superseded'}
    questions = rc1.read(HERE / 'REPLACEMENT_QUESTIONS.json')
    questioned = {r['relation']['id'] for q in questions['questions'] for r in q.get('rows', [])}
    if proposals != questioned:
        raise ValueError('Conservation proposal/question membership differs')
    for r in mapping['rows']:
        if r['disposition'] == 'superseded' and (r['successor_relation']['owner_decision'] is not None or r['successor_relation']['standing'] != 'proposed_pending_owner_decision'):
            raise ValueError('Proposal acquired unsupported acceptance')
    allowed = [str(HERE.relative_to(REPO)) + '/', str((HERE.parent / 'entry').relative_to(REPO)) + '/',
               prefix + 'interpretation/', prefix + 'standards/authority_compressions/',
               prefix + 'standards/frames/', prefix + 'standards/verification_material/']
    exact_paths = {prefix + 'README.md', *(c['path'] for c in entry['changes'])}
    changed_paths = set()
    for checkpoint in {args.source_commit, args.account_commit, args.package_commit}:
        paths = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', checkpoint], cwd=REPO, text=True).splitlines()
        if any(p not in exact_paths and not any(p.startswith(a) for a in allowed) for p in paths):
            raise ValueError('Checkpoint escaped exact granted territory')
        changed_paths.update(paths)
    subprocess.run(['git', 'diff', '--exit-code', INPUTS['starting_tenant'], args.package_commit, '--',
                    str(rc1.I5.relative_to(REPO)), str(PRIOR.relative_to(REPO))], cwd=REPO, check=True, stdout=subprocess.PIPE)
    projections(args, build)
    rc1.write(HERE / 'CANDIDATE.json', {'kind': 'stdo.rc1.end-repair-candidate', 'common_input': INPUTS['common_input'],
        'source_commit': args.source_commit, 'account_commit': args.account_commit,
        'package_commit': args.package_commit, 'members': members})
    rc1.write(HERE / 'CHANGED_SCOPE.json', {'kind': 'stdo.rc1.end-repair-check', 'writer_result': 'satisfied',
        'source_commit': args.source_commit, 'account_commit': args.account_commit, 'package_commit': args.package_commit,
        'members': len(members), 'account_rows': len(rows), 'conservation_counts': counts, 'proposal_count': len(proposals),
        'exact_inverse': True, 'historical_unmatched_observations': 11, 'native_projection_cases': 2,
        'changed_paths': sorted(changed_paths), 'historical_I5_and_RC1_preserved': True,
        'unchanged_raw_standards_frames_identity': unchanged, 'reused_identity_receipt_sha256': rc1.sha(prior_identity),
        'artifact_checks': check.counts, 'limits': ['Writer checks, not independent fidelity or actual-use qualification.',
            'Conservation proposals, the separate UX compliance decision and material consumer coverage remain open.']})
    print(json.dumps({'writer_result': 'satisfied', 'members': len(members), 'counts': counts, 'native_projections': 2}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['account', 'generate', 'verify'])
    for field in ['source-commit', 'account-commit', 'package-commit']:
        parser.add_argument('--' + field)
    parser.add_argument('--coordinates', type=Path)
    parser.add_argument('--theory-root', type=Path)
    args = parser.parse_args()
    if args.coordinates:
        for key, value in rc1.read(args.coordinates).items():
            if key in {'source_commit', 'account_commit', 'package_commit'}:
                setattr(args, key, value)
    context, build = rc1.modules()
    if args.operation == 'account':
        account(args, context, build)
    elif args.operation == 'generate':
        rc1.bind_account(args, build)
        rc1.invoke(importlib.import_module('generate_interpretation'),
                   ['--source-commit', args.source_commit, '--account-commit', args.account_commit,
                    '--theory-root', str(args.theory_root)])
        conservation(args, context, build)
    else:
        verify(args, context, build)


if __name__ == '__main__':
    main()
