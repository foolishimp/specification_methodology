"""Current coordinates over existing RC1 account, renderer and compiler owners.

Historical entrypoints and evidence are read-only. The parent freezes each
returned phase before the next operation is admitted.
"""
import argparse
import collections
import copy
import importlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
PRIOR = HERE.parents[1] / 'end-repair/integration'
ADAPTER = HERE.parents[1] / 'integration/rc1.py'
spec = importlib.util.spec_from_file_location('rc1_content_support', ADAPTER)
rc1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc1)
INPUTS = rc1.read(HERE / 'INPUTS.json')
rc1.HERE, rc1.INPUTS = HERE, INPUTS
PACKAGE, REPO = rc1.PACKAGE, rc1.REPO


def authored_inputs(commit):
    for name in ['INPUTS.json', 'integrate.py']:
        rc1.authenticate(commit, HERE / name)
    if rc1.sha(rc1.authenticate(INPUTS['helper_commit'], ADAPTER)) != INPUTS['adapter_sha256']:
        raise ValueError('Existing RC1 adapter differs from selected input')
    if len(INPUTS['source_returns']) != 2:
        raise ValueError('Both closed source returns must be selected before generation')
    for returned in INPUTS['source_returns']:
        path = TENANT / returned['path']
        if rc1.sha(rc1.authenticate(commit, path)) != returned['sha256']:
            raise ValueError('Closed source return changed: ' + returned['path'])
    for member in INPUTS['source_members']:
        if rc1.sha(rc1.authenticate(commit, PACKAGE / member['path'])) != member['sha256']:
            raise ValueError('Closed source member changed: ' + member['path'])


def prepare_compressions(decisions):
    """Check every authored replacement before any documentary write."""
    prepared = {}
    for decision in decisions['rows']:
        path = PACKAGE / decision['path']
        value = path.read_text()
        for replacement in decision.get('replacements', []):
            if value.count(replacement['before']) != 1:
                raise ValueError('Compression authored preimage is absent or ambiguous: ' + decision['path'])
            value = value.replace(replacement['before'], replacement['after'])
        prepared[path] = value
    return prepared


def source(args, context, build):
    authored_inputs(args.source_commit)
    build.documentary_inventory(rc1.exact(args.source_commit))
    build.verify_dependencies(args.theory_root)
    render = context.library('iteration-3/refresh_current.py')
    comparison = rc1.read(HERE / 'COMPRESSION_RECONCILIATION.json')
    if comparison['common_input'] != INPUTS['common_input']:
        raise ValueError('Compression account uses another common input')
    decisions = json.loads(rc1.authenticate(args.source_commit, HERE / 'COMPRESSION_DECISIONS.json'))
    prepared = prepare_compressions(decisions)
    for decision in decisions['rows']:
        path = PACKAGE / decision['path']
        value = prepared[path]
        if value != path.read_text():
            path.write_text(value)
        row = comparison['rows'][decision['path']]
        previous = copy.deepcopy(row)
        row.update(body_sha256=rc1.sha(render.compression_body(path)[1].encode()),
                   owner_pins=render.compression_owners(path, PACKAGE),
                   comparison=decision['comparison'],
                   affected_source_sections=decision['affected_source_sections'],
                   prior_reconciliation=previous,
                   standing='Content-repair author comparison of changed conditions; independent affected readback pending.')
    comparison.update(raw_source_commit=args.source_commit,
                      standing='Current changed-condition author comparisons; complete compression qualification remains deferred.')
    rc1.write(HERE / 'COMPRESSION_RECONCILIATION.json', comparison)
    index = rc1.read(HERE / 'FRAME_INPUTS.json')
    index['compression_body_reviews'] = comparison['rows']
    rc1.write(HERE / 'FRAME_INPUTS.json', index)
    changes, index = render.render_views(PACKAGE, HERE, INPUTS['common_input'])
    changed = []
    for path, value in changes.items():
        if path.read_text() != value:
            changed.append(str(path.relative_to(PACKAGE)))
            path.write_text(value)
    rc1.write(HERE / 'FRAME_INPUTS.json', index)
    identity = context.library('synthesis/derivation_material.py')
    resource = PACKAGE / identity.RESOURCE
    before = rc1.sha(resource.read_bytes())
    material = identity.build(PACKAGE, args.theory_root)
    rc1.write(HERE / 'IDENTITY_BUILD.json', {
        'documentary_preimage': args.source_commit, 'resource': identity.RESOURCE,
        'generator_sha256': INPUTS['libraries']['synthesis/derivation_material.py'],
        'before_sha256': before, 'sha256': rc1.sha(resource.read_bytes()),
        'historical_members': len(material['members']),
        'standing': 'Current documentary derivation; cold identity check awaits the frozen package.'})
    rc1.write(HERE / 'SOURCE_BUILD.json', {
        'authored_input_commit': args.source_commit, 'changed_views': changed,
        'identity_resource': identity.RESOURCE,
        'standing': 'Documentary output awaits parent source freeze; no qualification or acceptance.'})
    print(json.dumps({'phase': 'source', 'changed_views': len(changed)}))


def account(args, context, build):
    authored_inputs(args.source_commit)
    source_commit, inventory = build.documentary_inventory(rc1.exact(args.source_commit))
    prior_path = TENANT / INPUTS['prior_account_path']
    prior_raw = rc1.frozen(INPUTS['prior_account_commit'], prior_path)
    prior = json.loads(prior_raw)
    patches = [json.loads(rc1.authenticate(source_commit, TENANT / path))
               for path in INPUTS['account_patches']]
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    for patch in patches:
        paths.update(patch['owner_paths'])
    old = {path: rc1.frozen(INPUTS['prior_source_commit'], PACKAGE / path) for path in paths}
    current = {path: rc1.authenticate(source_commit, PACKAGE / path) for path in paths}
    integrator = importlib.import_module('reconcile_account')
    integrator.INPUTS = INPUTS
    result, report = integrator.integrate(prior, old, current, patches, source_commit)
    inverse = {r['id']: [] for r in result['determinations']}
    for row in result['determinations']:
        for target in row.get('dependencies', []):
            inverse[target].append(row['id'])
    for row in result['determinations']:
        row['consumers'] = sorted(set(inverse[row['id']]))
    result['source_members'] = inventory
    result['subject']['activation'] = INPUTS['activation']
    result['standing'] = 'Current authored content-repair account; source fidelity, complete coverage and owner decisions remain open.'
    report.update(prior_account_commit=INPUTS['prior_account_commit'],
                  prior_account_path=INPUTS['prior_account_path'],
                  prior_account_sha256=rc1.sha(prior_raw), exact_inverse=True)
    rc1.write(HERE / 'DETERMINATIONS.json', result)
    rc1.write(HERE / 'ACCOUNT_INTEGRATION.json', report)
    observations = json.loads(rc1.frozen(INPUTS['prior_account_commit'], PRIOR / 'CONSUMER_OBSERVATIONS.json'))
    observations['inherited_record'] = {
        'commit': INPUTS['prior_account_commit'],
        'path': str((PRIOR / 'CONSUMER_OBSERVATIONS.json').relative_to(TENANT))}
    observations['standing'] = 'Historical unmatched source-use observations retain unresolved meaning; current consumers are the exact authored dependency inverse.'
    rc1.write(HERE / 'CONSUMER_OBSERVATIONS.json', observations)
    print(json.dumps({'phase': 'account', 'rows': len(result['determinations']),
                      'authored_updates': len(report['direct_patches'])}))


def conservation(args, context):
    parser = context.library('iteration-3/check_conservation.py')
    prior_raw = rc1.frozen(INPUTS['prior_account_commit'], PRIOR / 'CONSERVATION.json')
    result = json.loads(prior_raw)
    questions = json.loads(rc1.frozen(INPUTS['prior_account_commit'], PRIOR / 'REPLACEMENT_QUESTIONS.json'))
    changes = json.loads(rc1.authenticate(args.source_commit, HERE / 'CONSERVATION_CHANGES.json'))
    rows = {r['id']: r for r in result['rows']}
    affected = set()
    for update in changes['updates']:
        row = rows[update['id']]
        if row['disposition'] != update['expected_disposition']:
            raise ValueError('Conservation preimage differs: ' + row['id'])
        row['content_repair_preimage'] = copy.deepcopy(row)
        for key in ['disposition', 'reason', 'successor_loci', 'successor_relation']:
            if key in update:
                row[key] = copy.deepcopy(update[key])
        affected.add(row['id'])
        if row['disposition'] == 'superseded':
            relation = row['successor_relation']
            if relation['standing'] != 'proposed_pending_owner_decision' or relation['owner_decision'] is not None:
                raise ValueError('Authored replacement acquired acceptance')
            found = False
            for question in questions['questions']:
                for member in question.get('rows', []):
                    if member.get('relation', {}).get('id') == relation['id']:
                        member['relation'] = copy.deepcopy(relation)
                        found = True
            if not found:
                questions['questions'].append({
                    'id': update['question_id'], 'title': row['id'],
                    'question': relation['changed_meaning'],
                    'decision': {'status': 'pending', 'record': None},
                    'rows': [{'claim': row['id'], 'relation': copy.deepcopy(relation)}]})
    old_pins = result['successor_locus_pins']
    member_pins, locus_pins, sources = {}, {}, {}
    for row in result['rows']:
        routes = list(dict.fromkeys(row.get('successor_loci', [row.get('successor_locus')]) +
                                   row.get('successor_relation', {}).get('replacement_loci', [])))
        for route in filter(None, routes):
            path, _, anchor = route.partition('#')
            if path not in sources:
                sources[path] = rc1.authenticate(args.source_commit, PACKAGE / path)
            raw = sources[path]
            body = parser.section_body(raw.decode(), anchor).encode() if anchor else raw
            member_pins[path] = {'sha256': rc1.sha(raw), 'bytes': len(raw)}
            locus_pins[route] = {'sha256': rc1.sha(body), 'bytes': len(body), 'member_sha256': rc1.sha(raw)}
            if route not in old_pins or old_pins[route]['sha256'] != rc1.sha(body):
                affected.add(row['id'])
        if row.get('successor_locus'):
            row['successor_sha256'] = locus_pins[row['successor_locus']]['sha256']
        row['review_history'] = [*row.get('review_history', []), row.get('current_review', {})]
        row['current_review'] = {
            'source_commit': args.source_commit, 'account_commit': args.account_commit,
            'standing': 'current_affected_readback_pending' if row['id'] in affected else 'historical_scope_only_no_new_assessment',
            'reuse': 'Current coordinates do not confer a new semantic judgment or owner decision.'}
        if row['id'] in affected:
            row['semantic_review_history'] = [*row.get('semantic_review_history', []), row.get('semantic_review', {})]
            row['semantic_review'] = {'result': 'indeterminate', 'scope': 'Content-repair affected source; independent readback and reserved owner decisions remain open.'}
    result.update(candidate_source_commit=args.source_commit, candidate_account_commit=args.account_commit,
        preimage={'commit': INPUTS['prior_account_commit'], 'path': str((PRIOR / 'CONSERVATION.json').relative_to(TENANT)), 'sha256': rc1.sha(prior_raw)},
        successor_member_pins=member_pins, successor_locus_pins=locus_pins,
        account_sha256=rc1.sha((HERE / 'DETERMINATIONS.json').read_bytes()),
        affected_rows=sorted(affected), binding_state='exact_current_source_and_account', pin_state='frozen',
        standing='Current authored conservation account; semantic judgments and replacement decisions retain their explicit scope.')
    result['semantic_sha256'] = parser.semantic_sha(result)
    questions.update(source_commit=args.source_commit, account_commit=args.account_commit,
                     standing='Current proposed replacement questions; no owner acceptance or removal of historical questions.')
    rc1.write(HERE / 'CONSERVATION.json', result)
    rc1.write(HERE / 'REPLACEMENT_QUESTIONS.json', questions)
    rc1.write(HERE / 'FRONTIER.json', parser.frontier_for(result))


def projections(args, build):
    cases = json.loads(rc1.authenticate(args.source_commit, HERE / 'PROJECTION_CASES.json'))
    results = []
    with tempfile.TemporaryDirectory(prefix='stdo-content-repair-project-') as temporary:
        directory = Path(temporary)
        bindings = directory / 'bindings.json'
        binding = subprocess.run([sys.executable, '-B', str(PACKAGE / 'interpretation/bindings.py'),
                                  '--theory-root', str(args.theory_root)], capture_output=True, check=True)
        bindings.write_bytes(binding.stdout)
        for case in cases['cases']:
            output = directory / (case['id'] + '.json')
            command = [sys.executable, '-B', str(build.TOOL), 'project',
                       '--program', str(PACKAGE / 'interpretation/program.json'),
                       '--map', str(PACKAGE / 'interpretation/map.json'),
                       '--bindings', str(bindings), '--mode', 'materialized', '--output', str(output)]
            for identifier in case['indexes']:
                command += ['--frame-index', build.NS + 'index:' + identifier]
            subprocess.run(command, check=True, capture_output=True)
            value = rc1.read(output)
            clauses = set()
            def collect(item):
                if isinstance(item, dict):
                    for key, child in item.items():
                        if key == 'clauses' and isinstance(child, list):
                            clauses.update(v['uri'] for v in child if isinstance(v, dict) and 'uri' in v)
                        collect(child)
                elif isinstance(item, list):
                    for child in item:
                        collect(child)
            collect(value)
            expected = {build.clause_id(identifier) for identifier in case['required_clauses']}
            if not expected.issubset(clauses):
                raise ValueError('Native route omitted selected owned clauses: ' + case['id'])
            results.append({'case': case['id'], 'indexes': case['indexes'], 'mode': 'materialized',
                'required_clauses_present': sorted(expected), 'clause_count': len(clauses),
                'output_bytes': output.stat().st_size, 'output_sha256': rc1.sha(output.read_bytes()),
                'standing': 'Mechanical native route availability; applicability and semantic fidelity remain separate.'})
    rc1.write(HERE / 'NATIVE_PROJECTIONS.json', {'package_commit': args.package_commit,
        'cases': results, 'replay': 'Use the frozen package program/map and bindings.py with PROJECTION_CASES.json indexes; output may remain in scratch.',
        'standing': 'Two changed-route projections; no fresh actor actual-use or whole-interpretation qualification.'})


def verify(args, context, build):
    authored_inputs(args.source_commit)
    account = rc1.bind_account(args, build)
    current, _ = build.semantic_projection(account)
    if current != rc1.read(PACKAGE / 'interpretation/source-account.json'):
        raise ValueError('Packaged semantic account differs')
    generation = rc1.read(HERE / 'interpretation/GENERATION.json')
    if (generation['document_source_input_commit'], generation['account_input_commit'], generation['native_validation']) != (args.source_commit, args.account_commit, 'passed'):
        raise ValueError('Generation coordinates differ')
    rc1.invoke(importlib.import_module('check_package'), ['--package-commit', args.package_commit])
    rows = {r['id']: r for r in account['determinations']}
    inverse = {identifier: set() for identifier in rows}
    for row in rows.values():
        for target in row.get('dependencies', []):
            inverse[target].add(row['id'])
    if any(sorted(inverse[i]) != rows[i]['consumers'] for i in rows):
        raise ValueError('Authored dependency inverse differs')
    mapping = rc1.read(HERE / 'CONSERVATION.json')
    questions = rc1.read(HERE / 'REPLACEMENT_QUESTIONS.json')
    if len(mapping['rows']) != 691 or len({r['id'] for r in mapping['rows']}) != 691:
        raise ValueError('Predecessor population changed')
    proposals = {r['successor_relation']['id'] for r in mapping['rows'] if r['disposition'] == 'superseded'}
    questioned = {r['relation']['id'] for q in questions['questions'] for r in q.get('rows', [])}
    if proposals != questioned:
        raise ValueError('Proposal/question membership differs')
    for relative in ['iteration-5', 'rc1/integration', 'rc1/end-repair', 'rc1/release-preparation']:
        path = TENANT / 'qualification/C3' / relative
        subprocess.run(['git', 'diff', '--exit-code', INPUTS['starting_tenant'], args.package_commit, '--',
                        str(path.relative_to(REPO))], cwd=REPO, check=True, stdout=subprocess.PIPE)
    projections(args, build)
    inventory = context.members()
    rc1.write(HERE / 'CANDIDATE.json', {'kind': 'stdo.rc1.content-repair-candidate',
        'common_input': INPUTS['common_input'], 'source_commit': args.source_commit,
        'account_commit': args.account_commit, 'package_commit': args.package_commit, 'members': inventory})
    result = {'writer_result': 'satisfied', 'source_commit': args.source_commit,
        'account_commit': args.account_commit, 'package_commit': args.package_commit,
        'members': len(inventory), 'account_rows': len(rows), 'exact_inverse': True,
        'conservation_counts': dict(collections.Counter(r['disposition'] for r in mapping['rows'])),
        'historical_evidence_preserved': True,
        'limits': ['Mechanical package/account checks; independent affected readback remains separate.',
                   'Complete interpretation fidelity, compression efficiency and actual-use qualification remain deferred.',
                   'Replacement, member acceptance, release and adoption decisions remain with their owners.']}
    rc1.write(HERE / 'CHANGED_SCOPE.json', result)
    print(json.dumps(result))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['source', 'account', 'generate', 'verify'])
    for field in ['source-commit', 'account-commit', 'package-commit']:
        parser.add_argument('--' + field)
    parser.add_argument('--theory-root', type=Path)
    args = parser.parse_args()
    context, build = rc1.modules()
    if args.operation == 'source':
        source(args, context, build)
    elif args.operation == 'account':
        account(args, context, build)
    elif args.operation == 'generate':
        authored_inputs(args.source_commit)
        rc1.bind_account(args, build)
        rc1.invoke(importlib.import_module('generate_interpretation'),
                   ['--source-commit', args.source_commit, '--account-commit', args.account_commit,
                    '--theory-root', str(args.theory_root)])
        conservation(args, context)
    else:
        verify(args, context, build)


if __name__ == '__main__':
    main()
