"""RC1 coordinates for the pinned existing compiler, integrator and renderers.

No historical entrypoint is run with its original output directory. Historical
account and proof bytes remain inputs; this adapter supplies only RC1 bindings.
"""
import argparse
import copy
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
I5 = HERE.parents[1] / 'iteration-5'
TENANT = HERE.parents[3]
PACKAGE = TENANT / 'successor'
REPO = TENANT.parents[3]
INPUTS = json.loads((HERE / 'INPUTS.json').read_text())
TARGET = 'SPEC_METHOD.construction-assessment-and-delegation'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def exact(commit):
    if len(commit) != 40 or subprocess.check_output(
            ['git', 'rev-parse', commit + '^{commit}'], cwd=REPO, text=True).strip() != commit:
        raise ValueError('Exact full commit required')
    return commit


def frozen(commit, path):
    return subprocess.check_output(['git', 'show', exact(commit) + ':' +
                                    str(path.relative_to(REPO))], cwd=REPO)


def authenticate(commit, path):
    raw = frozen(commit, path)
    if raw != path.read_bytes():
        raise ValueError('Frozen input differs: ' + str(path.relative_to(REPO)))
    return raw


def modules():
    for relative, pin in INPUTS['helpers'].items():
        path = TENANT / relative
        if sha(authenticate(INPUTS['helper_commit'], path)) != pin:
            raise ValueError('Unselected helper: ' + relative)
    sys.path.insert(0, str(I5 / 'tools'))
    context = importlib.import_module('context')
    context.verify_common()
    return context, importlib.import_module('build_interpretation')


def invoke(module, arguments):
    module.HERE = HERE
    module.INPUTS = INPUTS
    saved = sys.argv
    try:
        sys.argv = [str(Path(module.__file__)), *arguments]
        module.main()
    finally:
        sys.argv = saved


def source(args, context, build):
    # Authenticate the complete preimage before any documentary effect.
    build.documentary_inventory(INPUTS['source_repair_commit'])
    raw_source = PACKAGE / 'standards/SPEC_METHOD.md'
    if sha(raw_source.read_bytes()) != INPUTS['repaired_spec_sha256']:
        raise ValueError('Different raw source repair')
    identity = context.library('synthesis/derivation_material.py')
    resource = PACKAGE / identity.RESOURCE
    before = sha(resource.read_bytes())
    material = identity.build(PACKAGE, args.theory_root)
    write(HERE / 'IDENTITY_BUILD.json', {
        'documentary_preimage': INPUTS['source_repair_commit'],
        'generator_sha256': INPUTS['helpers']['qualification/C3/synthesis/derivation_material.py'],
        'resource': identity.RESOURCE, 'before_sha256': before,
        'sha256': sha(resource.read_bytes()), 'historical_members': len(material['members']),
        'standing': 'Constructed with the unchanged helper; cold validation is consolidated at package check.'})
    compression = PACKAGE / 'standards/authority_compressions/spec_method.compressed.md'
    text = compression.read_text()
    old = ('  independent assessment supports promotion, the assessor verifies the exact\n'
           '  live code, authority paths, proof, and installed subject. A constructor\n')
    new = ('  independent assessment supports promotion, the assessor evaluates the exact\n'
           '  live realisation under the selected computational binding, its authority\n'
           '  paths, proof, and installed subject. A constructor\n')
    if text.count(old) != 1:
        raise ValueError('Unexpected Spec compression preimage')
    compression.write_text(text.replace(old, new))
    render = context.library('iteration-3/refresh_current.py')
    comparison = copy.deepcopy(read(I5 / 'COMPRESSION_RECONCILIATION.json'))
    comparison.update(raw_source_commit=INPUTS['source_repair_commit'],
                      prior_record={'commit': INPUTS['helper_commit'],
                                    'path': str((I5 / 'COMPRESSION_RECONCILIATION.json').relative_to(TENANT))},
                      reuse_boundary='Unchanged author comparisons retain their scope and pending independent fidelity standing.')
    for path in sorted((PACKAGE / 'standards/authority_compressions').glob('*.md')):
        pair = render.compression_body(path)
        if pair is None:
            continue
        name = str(path.relative_to(PACKAGE))
        row = comparison['rows'][name]
        owners = render.compression_owners(path, PACKAGE)
        if row['owner_pins'] != owners or row['body_sha256'] != sha(pair[1].encode()):
            previous = copy.deepcopy(row)
            row.update(body_sha256=sha(pair[1].encode()), owner_pins=owners,
                       prior_reconciliation=previous,
                       affected_source_sections='SPEC_METHOD#construction-assessment-and-delegation',
                       standing='RC1 author reconciliation; independent fidelity assessment pending')
            row['comparison'] = (
                'Generic assessment follows the exact live realisation under the selected computational binding. '
                'Exact authority, proof, installed subject, independence and separate acceptance remain.'
                if name.endswith('/spec_method.compressed.md') else
                'Body unchanged. The existing generic live-surface and selected-binding routes remain compatible '
                'with the repaired owner; refresh only its member pin. This is no new independent review.')
    write(HERE / 'COMPRESSION_RECONCILIATION.json', comparison)
    index = copy.deepcopy(read(I5 / 'FRAME_INPUTS.json'))
    index['compression_body_reviews'] = comparison['rows']
    write(HERE / 'FRAME_INPUTS.json', index)
    changes, index = render.render_views(PACKAGE, HERE, INPUTS['common_input'])
    for path, value in changes.items():
        if path.read_text() != value:
            path.write_text(value)
    write(HERE / 'FRAME_INPUTS.json', index)
    protocol = importlib.import_module('account_protocol')
    prior = json.loads(authenticate(INPUTS['prior_account_commit'], I5 / 'DETERMINATIONS.json'))
    row = next(r for r in prior['determinations'] if r['id'] == TARGET)
    before_raw = frozen(prior['subject']['source_commit'], raw_source)
    after_raw = raw_source.read_bytes()
    owner = protocol.source_unit(row['owner']['path'], row['owner']['anchor'], after_raw)
    paragraphs = owner['body'].split(b'\n\n')
    first = paragraphs[1]
    blocks = copy.deepcopy(row['source_clauses'])
    for block in blocks:
        fragment = first if block['id'] == 'c1' else before_raw[block['byte_start']:block['byte_end']]
        if owner['body'].count(fragment) != 1:
            raise ValueError('Ambiguous authored block: ' + block['id'])
        start = owner['byte_start'] + owner['body'].index(fragment)
        block.update(byte_start=start, byte_end=start + len(fragment), sha256=sha(fragment))
    predicate = row['predicate'].replace('exact live code/authority/proof/installed subject',
        'the exact live realisation under its selected computational binding, authority paths, proof and installed subject')
    if predicate == row['predicate']:
        raise ValueError('Unexpected authored predicate preimage')
    argument = copy.deepcopy(row['argument'])
    argument['policy_choices'] = [predicate if item == row['predicate'] else item
                                  for item in argument['policy_choices']]
    inputs = copy.deepcopy(row['inputs'])
    inputs[0]['description'] = 'Actual roles/authorship, selected computational binding, live evidence, accepted decision envelope, operation grant and changed validity conditions.'
    patch = {'schema_version': protocol.PROTOCOL, 'common_input': INPUTS['common_input'],
        'source_preimage': INPUTS['starting_tenant'], 'producer': 'RC1-INTEGRATION',
        'owner_paths': ['standards/SPEC_METHOD.md'], 'new_rows': [],
        'updates': [{'id': TARGET, 'preimage_body_sha256': row['owner']['body_sha256'],
                     'candidate_body_sha256': sha(owner['body']),
                     'semantic_fields': {'predicate': predicate, 'argument': argument,
                                         'inputs': inputs, 'source_clauses': blocks,
                                         'source_excerpt': first.decode()}}]}
    write(HERE / 'ACCOUNT_PATCH.json', patch)
    print(json.dumps({'source_views_ready': True, 'frames': len(index['frames']),
                      'authored_account_updates': 1, 'historical_evidence_rewritten': False}))


def account(args, context, build):
    commit, inventory = build.documentary_inventory(exact(args.source_commit))
    prior_raw = authenticate(INPUTS['prior_account_commit'], I5 / 'DETERMINATIONS.json')
    prior = json.loads(prior_raw)
    patch_raw = authenticate(commit, HERE / 'ACCOUNT_PATCH.json')
    patch = json.loads(patch_raw)
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    old = {p: frozen(prior['subject']['source_commit'], PACKAGE / p) for p in paths}
    current = {p: (PACKAGE / p).read_bytes() for p in paths}
    integrate = importlib.import_module('reconcile_account')
    integrate.INPUTS = INPUTS
    # Two repeated fence blocks in this unchanged section are not unique text
    # matches. Authenticate their preserved local coordinates through the
    # identical complete owner body; retain the integrator's explicit-span check.
    repeated = next(r for r in prior['determinations'] if r['id'] == 'SPEC_METHOD.testing-strategy-taxonomy')
    path = repeated['owner']['path']
    before, old_start, old_end = integrate.body(repeated['owner'], old[path])
    after, new_start, new_end = integrate.body(repeated['owner'], current[path])
    if before != after:
        raise ValueError('Repeated-block owner changed; coordinate preservation is unsupported')
    blocks = copy.deepcopy(repeated['source_clauses'])
    for block in blocks:
        if not old_start <= block['byte_start'] <= block['byte_end'] <= old_end:
            raise ValueError('Repeated block escapes its authenticated owner')
        block['byte_start'] += new_start - old_start
        block['byte_end'] += new_start - old_start
        if sha(current[path][block['byte_start']:block['byte_end']]) != block['sha256']:
            raise ValueError('Repeated block changed at its preserved owner coordinate')
    relocation = {'id': repeated['id'], 'preimage_body_sha256': sha(before),
                  'candidate_body_sha256': sha(after), 'semantic_fields': {'source_clauses': blocks}}
    patch['updates'].append(relocation)
    write(HERE / 'COORDINATE_RELOCATION.json', {'source_commit': commit,
          'prior_source_commit': prior['subject']['source_commit'], 'update': relocation,
          'reason': 'Identical complete owner body authenticates repeated fence blocks c9/c14 at their preserved local coordinates; no semantic change.'})
    result, report = integrate.integrate(prior, old, current, [patch], commit)
    result['source_members'] = inventory
    result['subject'].update(activation='EC-CODEX-RC1-01/RC1-INTEGRATION',
                             source_repair_commit=INPUTS['source_repair_commit'])
    result['standing'] = 'Current RC1 authored construction account; no independent fidelity or acceptance judgment.'
    report.update(common_input=INPUTS['common_input'], prior_account_commit=INPUTS['prior_account_commit'],
                  prior_account_sha256=sha(prior_raw), patch_commit=commit, patch_sha256=sha(patch_raw),
                  coordinate_only_updates=[repeated['id']])
    write(HERE / 'DETERMINATIONS.json', result)
    write(HERE / 'ACCOUNT_INTEGRATION.json', report)
    print(json.dumps({'rows': len(result['determinations']), 'direct_patches': len(report['direct_patches']),
                      'coordinate_updates': len(report['coordinate_updates']), 'source_commit': commit}))


def bind_account(args, build):
    raw = authenticate(exact(args.account_commit), HERE / 'DETERMINATIONS.json')
    account = json.loads(raw)
    commit, inventory = build.documentary_inventory(exact(args.source_commit))
    if account['source_members'] != inventory or account['subject']['source_commit'] != commit:
        raise ValueError('Frozen account documentary membership or subject differs')
    if account['subject']['common_input'] != INPUTS['common_input']:
        raise ValueError('Frozen account common basis differs')
    return account


def consumers(args):
    """Apply only the explicitly admitted closed author patch groups."""
    commit = exact(args.consumer_commit)
    directory = HERE.parent / 'consumer-account'
    account_path = HERE / 'DETERMINATIONS.json'
    account = read(account_path)
    rows = {row['id']: row for row in account['determinations']}
    before = sha(account_path.read_bytes())
    selected, changes, source_cache = [], [], {}

    def source_pin(pin):
        path = (REPO / pin['path']).resolve()
        path.relative_to(PACKAGE.resolve())
        if pin['commit'] != INPUTS['source_repair_commit']:
            raise ValueError('Consumer evidence names a different source commit')
        if path not in source_cache:
            source_cache[path] = authenticate(pin['commit'], path)
        raw = source_cache[path]
        if sha(raw[pin['byte_start']:pin['byte_end']]) != pin['body_sha256']:
            raise ValueError('Consumer evidence source body differs')
        return raw

    def evidence_pins(value):
        if isinstance(value, list):
            for child in value:
                evidence_pins(child)
        elif isinstance(value, dict):
            if {'commit', 'path', 'byte_start', 'byte_end', 'body_sha256'} <= set(value):
                source_pin(value)
            if 'quote_sha256' in value:
                raw = source_pin(value['source'])
                quote = raw[value['quote_byte_start']:value['quote_byte_end']]
                if sha(quote) != value['quote_sha256'] or quote.decode() != value['quote']:
                    raise ValueError('Consumer source quote differs')
            for child in value.values():
                evidence_pins(child)

    for name in args.consumer_patch:
        if name not in {'INVERSE_PROJECTION_PATCH.json', 'RECIPROCAL_CALL_PATCH.json'}:
            raise ValueError('Unselected consumer patch filename')
        raw = authenticate(commit, directory / name)
        patch = json.loads(raw)
        required = patch.get('required_patch')
        if required and not any(Path(p['path']).name == required['filename'] and
                                p['sha256'] == required['sha256'] for p in selected):
            raise ValueError('Consumer patch prerequisite is not selected at its exact digest')
        if (patch['source_commit'] != INPUTS['source_repair_commit'] or
                patch['account_commit'] != INPUTS['prior_account_commit']):
            raise ValueError('Consumer source/account basis differs')
        evidence_pins(patch['updates'])
        for update in patch['updates']:
            identifier, field = update['id'], update['field']
            if identifier == TARGET or field not in {'consumers', 'dependencies'}:
                raise ValueError('Consumer patch escapes its admitted fields or generic owner boundary')
            row = rows[identifier]
            if ((field in row) != update['preimage_present'] or
                    row.get(field, []) != update['preimage']):
                raise ValueError('Consumer patch preimage differs: ' + identifier + '/' + field)
            replacement = update['replacement']
            if (not isinstance(replacement, list) or len(set(replacement)) != len(replacement) or
                    not set(row.get(field, [])) <= set(replacement) or
                    any(target not in rows for target in replacement) or not update['evidence']):
                raise ValueError('Consumer patch loses a positive, names an absent row or lacks evidence')
            row[field] = replacement
            changes.append(copy.deepcopy(update))
        selected.append({'path': str((directory / name).relative_to(TENANT)),
                         'commit': commit, 'sha256': sha(raw)})
    account['coverage']['consumer_completion'] = {
        'producer_commit': commit, 'patch_inputs': selected,
        'updated_rows': sorted({u['id'] for u in changes}),
        'standing': 'Source-supported author completion only; retained positives and unknown absence keep their reported limits.'}
    write(account_path, account)
    write(HERE / 'CONSUMER_INTEGRATION.json', {
        'kind': 'stdo.rc1.consumer-account-integration', 'schema_version': 1,
        'producer_commit': commit, 'patch_inputs': selected,
        'before_account_sha256': before, 'account_sha256': sha(account_path.read_bytes()),
        'updates': changes,
        'semantic_dependency_updates': sorted({u['id'] for u in changes if u['field'] == 'dependencies'}),
        'standing': 'Admitted closed author patch groups applied; no independent fidelity or complete consumer-absence judgment.'})
    print(json.dumps({'consumer_patch_groups': len(selected), 'explicit_field_updates': len(changes)}))


def applicability(args, context, build, account):
    prior_raw = authenticate(INPUTS['helper_commit'], I5 / 'CONSERVATION.json')
    prior = json.loads(prior_raw)
    current, _ = build.semantic_projection(account)
    rows = {r['id']: r for r in current['determinations']}
    reverse = {identifier: set() for identifier in rows}
    for identifier, row in rows.items():
        for edge in build.acquisition_edges(row, set(rows), current['semantic_contracts'], row):
            target = edge['target'].removeprefix(build.NS + 'clause:')
            if target in reverse and edge['acquisition'] in {'required', 'conditional'}:
                reverse[target].add(identifier)
    consumer_report = read(HERE / 'CONSUMER_INTEGRATION.json') if (HERE / 'CONSUMER_INTEGRATION.json').exists() else {}
    seeds = {TARGET, *consumer_report.get('semantic_dependency_updates', [])}
    affected = set(seeds)
    while True:
        expanded = affected | set().union(*(reverse[item] for item in affected))
        if expanded == affected:
            break
        affected = expanded
    parser = context.library('iteration-3/check_conservation.py')
    cache, result = {}, []
    for row in prior['rows']:
        changes, dependents, pins = [], [], []
        routes = list(dict.fromkeys(row.get('successor_loci', [row.get('successor_locus')]) +
                                   row.get('successor_relation', {}).get('replacement_loci', [])))
        for route in filter(None, routes):
            path, _, anchor = route.partition('#')
            if path not in cache:
                cache[path] = (frozen(prior['candidate_source_commit'], PACKAGE / path),
                               frozen(args.source_commit, PACKAGE / path))
            before, after = cache[path]
            old_body = parser.section_body(before.decode(), anchor).encode()
            new_body = parser.section_body(after.decode(), anchor).encode()
            changed = old_body != new_body
            if changed:
                changes.append(route)
            for identifier in affected:
                owner = rows[identifier]['owner']
                if owner['path'] == path:
                    unit = parser.section_body(after.decode(), owner['anchor']).encode()
                    if unit and unit in new_body:
                        dependents.append(identifier)
            pins.append({'route': route, 'prior_body_sha256': sha(old_body),
                         'body_sha256': sha(new_body), 'member_sha256': sha(after), 'bytes': len(new_body)})
        result.append({'id': row['id'], 'prior_disposition': row['disposition'],
                       'prior_acceptance': row['acceptance'], 'loci': pins,
                       'changed_carrying_loci': changes,
                       'affected_declared_account_cone': sorted(set(dependents)),
                       'standing': 'affected_scope_requires_current_independent_assessment'
                                   if changes or dependents else 'prior_scope_retained_no_new_qualification'})
    value = {'kind': 'stdo.rc1.conservation-applicability', 'schema_version': 1,
             'source_commit': args.source_commit, 'account_commit': args.account_commit,
             'prior_record': {'commit': INPUTS['helper_commit'],
                              'path': str((I5 / 'CONSERVATION.json').relative_to(TENANT)),
                              'sha256': sha(prior_raw), 'source_commit': prior['candidate_source_commit']},
             'changed_owner': TARGET, 'changed_semantic_determinations': sorted(seeds),
             'changed_consumer_projection_rows': sorted({u['id'] for u in consumer_report.get('updates', [])
                                                        if u['field'] == 'consumers'}),
             'declared_dependency_cone': sorted(affected), 'rows': result,
             'limits': ['No predecessor disposition or acceptance is changed.',
                        'Unchanged local bytes retain only their prior supported scope; missing independent qualification stays missing.',
                        'Declared required and conditional account edges bound this impact projection. Complete material dependency coverage remains an independent assessment obligation.',
                        'Changed frames, account clauses and source-dependent interpretation require current fidelity assessment; historical actual-use observations are not retagged.']}
    write(HERE / 'CONSERVATION_APPLICABILITY.json', value)
    write(HERE / 'FRONTIER.json', {'kind': 'stdo.rc1.frontier-projection', 'schema_version': 1,
        'source_commit': args.source_commit, 'account_commit': args.account_commit,
        'applicability_sha256': sha((HERE / 'CONSERVATION_APPLICABILITY.json').read_bytes()),
        'rows': [{k: r[k] for k in ('id', 'prior_disposition', 'prior_acceptance', 'standing')} for r in result],
        'standing': 'Historical gaps and reserved decisions remain open; this projection grants no acceptance.'})
    return value


def verify(args, context, build):
    account = bind_account(args, build)
    authenticate(args.source_commit, HERE / 'FRAME_INPUTS.json')
    authenticate(args.source_commit, HERE / 'ACCOUNT_PATCH.json')
    authenticate(args.package_commit, Path(__file__))
    generation_path = HERE / 'interpretation/GENERATION.json'
    generation = json.loads(authenticate(args.package_commit, generation_path))
    for name in ['validation.json', 'DEPENDENCY_VERIFICATION.json', 'QUALIFICATION_EQUIVALENCE.json']:
        authenticate(args.package_commit, HERE / 'interpretation' / name)
    if (generation['document_source_input_commit'] != args.source_commit or
            generation['account_input_commit'] != args.account_commit or
            generation['common_input_commit'] != INPUTS['common_input']):
        raise ValueError('Current native generation receipt has a different frozen subject')
    if (HERE / 'CONSUMER_INTEGRATION.json').exists():
        authenticate(args.package_commit, HERE / 'CONSUMER_INTEGRATION.json')
    current, _ = build.semantic_projection(account)
    if current != read(PACKAGE / 'interpretation/source-account.json'):
        raise ValueError('Packaged account differs from the frozen authored account')
    invoke(importlib.import_module('check_package'), ['--package-commit', exact(args.package_commit)])
    scope = applicability(args, context, build, account)
    target = next(r for r in current['determinations'] if r['id'] == TARGET)
    expected = read(HERE / 'ACCOUNT_PATCH.json')['updates'][0]['semantic_fields']
    if target['predicate'] != expected['predicate'] or 'exact live code/' in target['predicate']:
        raise ValueError('Generic assessment repair lost in semantic projection')
    section = target['owner']
    raw = (PACKAGE / section['path']).read_bytes()
    c1 = next(b for b in target['source_clauses'] if b['id'] == 'c1')
    if raw[c1['byte_start']:c1['byte_end']].decode() != expected['source_excerpt']:
        raise ValueError('Current assessment excerpt lost its exact source block')
    frames = ['WORK_RECOVERY', 'TRIAGE_CARRIER', 'MEMBER_CONSTRUCTION_ASSESSMENT']
    for name in frames:
        text = (PACKAGE / ('standards/frames/' + name + '.md')).read_text()
        if expected['source_excerpt'] not in text:
            raise ValueError('Changed assessment body absent from frame: ' + name)
    baseline_ids = ['STDO_REFERENCE_FRAME_BASELINE.complete-engagement-transition',
                    'STDO_REFERENCE_FRAME_BASELINE.engagement-applicability']
    prior_account = read(I5 / 'DETERMINATIONS.json')
    def consumer_relations(value):
        declared = {(owner, row['id']) for row in value['determinations'] for owner in row.get('dependencies', [])}
        projected = {(row['id'], consumer) for row in value['determinations'] for consumer in row.get('consumers', [])}
        return declared, projected
    old_declared, old_projected = consumer_relations(prior_account)
    declared, projected = consumer_relations(account)
    if old_projected - old_declared != projected - declared:
        raise ValueError('Unmatched prior consumer positives were altered')
    write(HERE / 'CONSUMER_RELATIONS.json', {
        'source_commit': args.source_commit, 'account_commit': args.account_commit,
        'missing_inverse_pairs': sorted(declared - projected),
        'retained_unmatched_positive_pairs': sorted(projected - declared),
        'standing': 'Exact declared-edge projection only. Retained unmatched positives and separate material consumer completeness remain unresolved.'})
    for identifier in baseline_ids:
        old = next(r for r in prior_account['determinations'] if r['id'] == identifier)
        new = next(r for r in account['determinations'] if r['id'] == identifier)
        if (any(old.get(key) != new.get(key) for key in set(old) | set(new) if key != 'consumers')
                or TARGET not in new['dependencies']):
            raise ValueError('Declared baseline consumer changed or lost its owner')
    prefix = str(TENANT.relative_to(REPO)) + '/'
    allowed = ['successor/standards/authority_compressions/', 'successor/standards/frames/',
               'successor/standards/verification_material/', 'successor/interpretation/',
               str(HERE.relative_to(TENANT)) + '/']
    # Other authorised Writers may freeze their closed support between our
    # checkpoints. Audit this Writer's exact commits, not their inherited work.
    checkpoints = sorted({args.source_commit, args.account_commit, args.package_commit})
    changed = set()
    for checkpoint in checkpoints:
        paths = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only',
                                         '-r', checkpoint], cwd=REPO, text=True).splitlines()
        if any(not p.startswith(prefix) or not any(p[len(prefix):].startswith(a) for a in allowed) for p in paths):
            raise ValueError('Writer checkpoint escaped exact RC1 territory: ' + checkpoint)
        changed.update(paths)
    subprocess.run(['git', 'diff', '--exit-code', INPUTS['source_repair_commit'],
                    args.package_commit, '--', str(I5.relative_to(REPO))], cwd=REPO, check=True,
                   stdout=subprocess.PIPE)
    check = read(HERE / 'ARTIFACT_CHECK.json')
    write(HERE / 'CANDIDATE.json', {'kind': 'stdo.rc1.candidate-inventory', 'schema_version': 1,
        'common_input': INPUTS['common_input'], 'document_source_commit': args.source_commit,
        'account_commit': args.account_commit, 'package_commit': args.package_commit,
        'members': check['members'], 'standing': 'Complete construction inventory; qualification and owner decisions remain open.'})
    write(HERE / 'CHANGED_SCOPE.json', {'kind': 'stdo.rc1.changed-scope-check', 'schema_version': 1,
        'source_commit': args.source_commit, 'account_commit': args.account_commit,
        'package_commit': args.package_commit, 'writer_result': 'satisfied',
        'writer_checkpoints': checkpoints, 'changed_paths': sorted(changed), 'historical_paths_preserved': True,
        'determinations': len(current['determinations']), 'members': len(check['members']),
        'native_validation': generation['native_validation'],
        'changed_owner': TARGET, 'baseline_consumers_preserved': baseline_ids,
        'changed_body_frames': frames, 'generic_binding_cases': read(HERE / 'DISCRIMINATORS.json'),
        'conservation_rows': len(scope['rows']),
        'affected_conservation_rows': sum(r['standing'].startswith('affected_') for r in scope['rows']),
        'limits': ['Writer construction check; neither independent assessment nor actual-use qualification.',
                   'Generic binding cases are source-derived logical evaluations, not claims that these real-world subjects were executed.']})
    print(json.dumps({'writer_result': 'satisfied', 'package_members': len(check['members']),
                      'account_rows': len(current['determinations']), 'conservation_rows': len(scope['rows']),
                      'declared_dependency_cone': scope['declared_dependency_cone']}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['source', 'account', 'consumers', 'generate', 'verify'])
    parser.add_argument('--source-commit')
    parser.add_argument('--account-commit')
    parser.add_argument('--package-commit')
    parser.add_argument('--consumer-commit')
    parser.add_argument('--consumer-patch', action='append', default=[])
    parser.add_argument('--coordinates', type=Path)
    parser.add_argument('--theory-root', type=Path)
    args = parser.parse_args()
    if args.coordinates:
        coordinates = read(args.coordinates)
        for field in ['source_commit', 'account_commit', 'package_commit']:
            if getattr(args, field) and getattr(args, field) != coordinates[field]:
                raise ValueError('Conflicting explicit and recorded coordinate: ' + field)
            setattr(args, field, coordinates[field])
    context, build = modules()
    if args.operation == 'source':
        source(args, context, build)
    elif args.operation == 'account':
        account(args, context, build)
    elif args.operation == 'consumers':
        consumers(args)
    elif args.operation == 'generate':
        bind_account(args, build)
        invoke(importlib.import_module('generate_interpretation'),
               ['--source-commit', args.source_commit, '--account-commit', args.account_commit,
                '--theory-root', str(args.theory_root)])
    else:
        verify(args, context, build)


if __name__ == '__main__':
    main()
