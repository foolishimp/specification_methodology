"""I5 tool checks on frozen I4 inputs and deliberately damaged small accounts.

This does not generate the current I5 account or publication. It retains exact
fixture/source identities and distinguishes serialization equivalence from
source fidelity. All transient files remain in the I5 interpretation territory.
"""
import argparse
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import build_interpretation as build
from account_protocol import PROTOCOL, make_owner, source_block, source_unit
from reconcile_account import integrate
from context import HERE, PACKAGE, REPO, INPUTS, encoded, git_bytes, sha, write


def integration_cases():
    path = 'standards/FIXTURE.md'
    old = b'# Fixture\n\n## Rule\n\nKeep the declared condition.\n'
    new = b'# Fixture\n\n## Rule\n\nKeep the changed condition.\n\n## Added rule\n\nObserve the required input.\n'

    def row(identifier, anchor, raw):
        return {'id': identifier, 'family': 'fixture', 'representation_kind': 'constraint',
                'owner': make_owner(path, anchor, raw), 'predicate': 'Source-bound fixture predicate',
                'applicability': 'Only this deliberately small integration fixture',
                'obligations': ['The exact source condition'], 'permissions_exceptions': [],
                'dependencies': [], 'dependency_relations': [], 'inputs': [],
                'argument': {'premises': [], 'source_refs': []},
                'result_mapping': {'kind': 'fixture-only'}, 'source_clauses': [source_block(path, anchor, raw=raw)]}

    original = row('FIXTURE.rule', 'rule', old)
    prior = {'schema_version': 'stdo.determinations.v1.4', 'determinations': [original],
             'source_members': [{'path': path}], 'coverage': {'standing': 'fixture'},
             'semantic_contracts': {}, 'subject': {'source_commit': 'fixture-original'}}
    patch = {'schema_version': PROTOCOL, 'common_input': INPUTS['common_input'],
             'source_preimage': INPUTS['starting_tenant'], 'producer': 'fixture-author',
             'owner_paths': [path], 'updates': [{'id': original['id'],
                'preimage_body_sha256': original['owner']['body_sha256'],
                'candidate_body_sha256': sha(source_unit(path, 'rule', new)['body']),
                'semantic_fields': {'predicate': 'Explicitly changed source-bound predicate',
                                    'source_clauses': [source_block(path, 'rule', raw=new)]}}],
             'new_rows': [row('FIXTURE.added-rule', 'added-rule', new)]}
    current, report = integrate(prior, {path: old}, {path: new}, [patch], 'fixture-current')
    if len(current['determinations']) != 2 or report['new_rows'] != ['FIXTURE.added-rule']:
        raise ValueError('Explicit new-row integration did not retain both rows')
    cases = [{'case': 'authored changed section and explicit new row', 'result': 'passed'}]

    def refuse(name, action):
        try:
            action()
        except (ValueError, KeyError) as error:
            cases.append({'case': name, 'result': 'refused', 'reason': str(error)})
        else:
            raise ValueError('Unsafe account alteration escaped: ' + name)

    refuse('changed source without an authored patch', lambda: integrate(prior, {path: old}, {path: new}, [], 'fixture'))
    changed = copy.deepcopy(patch); changed['new_rows'] = []
    refuse('new heading without an authored new determination', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    refuse('two producers patch one owner', lambda: integrate(prior, {path: old}, {path: new}, [patch, patch], 'fixture'))
    changed = copy.deepcopy(patch); changed['updates'][0]['candidate_body_sha256'] = '0' * 64
    refuse('stale current source pin', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['updates'][0]['preimage_body_sha256'] = '0' * 64
    refuse('stale source preimage', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['updates'][0]['semantic_fields'].pop('source_clauses')
    refuse('changed source block silently coarsened or relabelled', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['owner_paths'] = ['standards/OTHER.md']
    refuse('patch outside producer owner territory', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['new_rows'][0]['id'] = original['id']
    refuse('new row collides with the preserved I4 identity', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['updates'][0]['semantic_fields']['unclassified_permission'] = True
    refuse('unclassified field silently discarded', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    changed = copy.deepcopy(patch); changed['common_input'] = '0' * 40
    refuse('another common basis', lambda: integrate(prior, {path: old}, {path: new}, [changed], 'fixture'))
    return cases


def byte_sizes(value):
    return {'pretty_json_utf8_bytes': len(encoded(value)),
            'compact_utf8_bytes': len(json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode())}


def frozen_fixture(root, commit):
    prefix = str(PACKAGE.relative_to(REPO)) + '/'
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit, '--', prefix], cwd=REPO, text=True).splitlines()
    for name in names:
        relative = name[len(prefix):]
        if relative.startswith('interpretation/'):
            continue
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(git_bytes(commit, name))


def qualification_cases(root, theory):
    frozen = INPUTS['prior_account_commit']
    account_raw = git_bytes(frozen, (PACKAGE / 'interpretation/source-account.json').relative_to(REPO))
    original_raw = git_bytes(frozen, (PACKAGE / 'interpretation/program.json').relative_to(REPO))
    account = json.loads(account_raw)
    frozen_fixture(root, frozen)
    former = build.PACKAGE
    try:
        build.PACKAGE = root
        build.validate_account(account, package=root)
        compact, _, frames = build.build_program(account)
        expanded, _, _ = build.build_program(account, compact_qualifications=False)
    finally:
        build.PACKAGE = former
    equivalence = build.qualification_equivalence(compact, expanded)
    if expanded != json.loads(original_raw):
        raise ValueError('Expanded fixture is not the original frozen I4 program')
    controls = []
    alterations = [
        ('missing qualification source pointer', lambda r: r['qualification_ref'].update(pointer='/not-present')),
        ('stale qualification digest', lambda r: r['qualification_ref'].update(sha256='0' * 64)),
        ('condition changed into permission', lambda r: r.update(required_when='Always permitted')),
        ('qualification base changed', lambda r: r['qualification_ref'].update(scope='unregistered-scope')),
        ('conditional acquisition changed to required', lambda r: r.update(acquisition='required')),
        ('route qualification dropped', lambda r: r.pop('qualification_ref')),
    ]
    for name, alter in alterations:
        damaged = copy.deepcopy(compact)
        arg = next(a for c in damaged['clauses'] for a in c['arguments']
                   if a['role'] == build.VOCAB + 'acquisition-route'
                   and 'qualification_ref' in json.loads(a['literal']))
        value = json.loads(arg['literal']); alter(value); arg['literal'] = build.text(value)
        try:
            build.qualification_equivalence(damaged, expanded)
        except (ValueError, KeyError) as error:
            controls.append({'case': name, 'result': 'refused', 'reason': str(error)})
        else:
            raise ValueError('Unsafe qualification alteration escaped: ' + name)
    interpretation = root / 'interpretation'; interpretation.mkdir()
    (interpretation / 'SIGNATURE.md').write_text(build.SIGNATURE)
    (interpretation / 'FRAMES.md').write_text(frames)
    binding = root.parent / 'bindings.json'
    write(binding, {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
                    'bindings': [{'uri_prefix': build.URI, 'path': str(root)},
                                 {'uri_prefix': build.THEORY_URI, 'path': str(theory.resolve())}]})
    metrics = {}
    maps = {}
    for name, program in [('expanded', expanded), ('referenced', compact)]:
        program_path = root.parent / (name + '-program.json')
        map_path = root.parent / (name + '-map.json')
        write(program_path, program)
        command = [sys.executable, '-B', str(build.TOOL), 'validate', '--program', str(program_path),
                   '--bindings', str(binding), '--output', str(root.parent / (name + '-validation.json')),
                   '--emit-map', str(map_path)]
        run = subprocess.run(command, capture_output=True, text=True)
        if run.returncode:
            raise ValueError('Native fixture validation failed: ' + run.stdout + run.stderr)
        mapped = json.loads(map_path.read_text())
        if mapped['clauses'] != program['clauses']:
            raise ValueError('Pinned native map ceased carrying its exact program clauses')
        maps[name] = mapped
        metrics[name] = {'program': byte_sizes(program), 'map': byte_sizes(mapped),
                         'actual_program_file_bytes': program_path.stat().st_size,
                         'actual_native_map_file_bytes': map_path.stat().st_size,
                         'clause_array': byte_sizes(program['clauses']),
                         'native_validation': 'passed', 'native_map_clause_copy': True}
    # Exercise one actual materialized projection, including its carried scopes.
    projected = root.parent / 'projection.json'
    run = subprocess.run([sys.executable, '-B', str(build.TOOL), 'project',
                          '--program', str(root.parent / 'referenced-program.json'),
                          '--map', str(root.parent / 'referenced-map.json'), '--bindings', str(binding),
                          '--frame-index', build.NS + 'index:TRANSFORMATION_LIBRARY.workrecovery-specialization',
                          '--mode', 'materialized', '--output', str(projected)], capture_output=True, text=True)
    if run.returncode:
        raise ValueError('Native materialized acquisition failed: ' + run.stdout + run.stderr)
    view = json.loads(projected.read_text())
    occurrences = build.validate_occurrences({'clauses': view['clauses']}, account['semantic_contracts'])
    return {'frozen_I4_commit': frozen, 'source_account_sha256': sha(account_raw),
            'original_program_sha256': sha(original_raw), 'expanded_matches_original_program': True,
            'equivalence': equivalence, 'negative_controls': controls, 'same_semantic_input_costs': metrics,
            'native_acquisition': {'selector': 'TRANSFORMATION_LIBRARY.workrecovery-specialization',
                                   'bytes': projected.stat().st_size, 'occurrences': occurrences},
            'limits': ['Identical frozen I4 semantic input; costs isolate the selected representation change.',
                       'Serialized and compact JSON sizes are not process memory, retained context or task efficiency.',
                       'Native structure and exact expansion do not establish source fidelity or I5 coverage.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--theory-root', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    tool_pins = {p.name: sha(p.read_bytes()) for p in sorted(Path(__file__).parent.glob('*.py'))
                 if p.name not in {'carry_conservation.py', 'measure_reduction.py'}}
    directory = HERE / 'interpretation'; directory.mkdir(exist_ok=True)
    dependencies = build.verify_dependencies(args.theory_root)
    integration = integration_cases()
    with tempfile.TemporaryDirectory(prefix='tool-fixture-', dir=directory) as work:
        root = Path(work) / 'package'; root.mkdir()
        qualification = qualification_cases(root, args.theory_root)
    for name, digest in tool_pins.items():
        if sha((Path(__file__).parent / name).read_bytes()) != digest:
            raise ValueError('Tool source changed during its check: ' + name)
    result = {'kind': 'stdo.i5.tooling-check', 'valid': True, 'common_input': INPUTS['common_input'],
              'inputs_sha256': sha((HERE / 'INPUTS.json').read_bytes()), 'dependency_verification': dependencies,
              'tool_sha256': tool_pins,
              'integration_cases': integration, 'qualification': qualification,
              'elapsed_seconds': time.monotonic() - started,
              'current_I5_generation': 'not performed; frozen core and consumer returns required'}
    write(directory / 'TOOLING_CHECK.json', result)
    print(json.dumps({'valid': True, 'integration_cases': len(integration),
                      'qualification_controls': len(qualification['negative_controls']),
                      'elapsed_seconds': result['elapsed_seconds'],
                      'same_input_costs': qualification['same_semantic_input_costs']}))


if __name__ == '__main__':
    main()
