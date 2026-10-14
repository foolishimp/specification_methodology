"""Check exact interpretation coordinates and selected native mechanics.

This author check proves neither semantic fidelity nor complete material coverage.
Each invocation retains its own evidence directory, including failed controls.
"""
import argparse
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

import build_interpretation as build

HERE = build.HERE
PACKAGE = build.PACKAGE
OUTPUT = build.OUTPUT
EVIDENCE = None


def require(condition, message):
    if not condition:
        raise ValueError(message)


def write(name, value):
    (EVIDENCE / name).write_bytes(build.json_bytes(value))


def invoke(args, expected=0):
    result = subprocess.run([sys.executable, '-B', str(build.TOOL), *map(str, args)], capture_output=True, text=True)
    require(result.returncode == expected, result.stdout + result.stderr)
    return result


def package_inventory(document_commit):
    inventory = build.read(HERE / 'CANDIDATE.json')
    require(inventory.get('document_source_input_commit') == document_commit, 'Complete-package inventory binds another documentary subject')
    require(inventory.get('source_input_commit') == build.COMMON_INPUT, 'Complete-package common input differs')
    commit = inventory.get('inventory_input_commit')
    require(isinstance(commit, str) and len(commit) == 40, 'Freeze the complete package before final interpretation checks')
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=PACKAGE, text=True).strip())
    expected = {r['path']: r for r in inventory['members']}
    actual = {str(p.relative_to(PACKAGE)): p for p in PACKAGE.rglob('*') if p.is_file()}
    require(len(expected) == len(inventory['members']) and set(expected) == set(actual), 'Complete-package inventory membership differs')
    for name, row in expected.items():
        data = actual[name].read_bytes()
        require(not actual[name].is_symlink() and build.sha(data) == row['sha256'] and len(data) == row['bytes'], 'Complete-package member drift: ' + name)
        frozen = subprocess.check_output(['git', 'show', commit + ':' + str(actual[name].relative_to(repo))], cwd=repo)
        require(data == frozen, 'Complete-package freeze differs: ' + name)
    return commit


def assert_compilation(current, program, mapping):
    expected, rows, frames = build.build_program(current)
    require(program == expected, 'Program differs from the current semantic account')
    require(mapping['rows'] == rows, 'Source mapping omits or changes an accounted determination')
    require(mapping['optional_family_indexes'] == build.family_mappings(current), 'Optional group mapping differs')
    require((OUTPUT / 'FRAMES.md').read_text() == frames, 'Acquisition-frame routes differ from the account')
    require((OUTPUT / 'SIGNATURE.md').read_text() == build.SIGNATURE, 'Interpretation vocabulary differs from selected compiler')
    require((OUTPUT / 'bindings.py').read_text() == build.BINDINGS_SCRIPT, 'Relocatable binding procedure differs from selected compiler')
    require((OUTPUT / 'README.md').read_text() == build.README, 'Interpretation entry differs from selected compiler')
    return rows


def projection(program, logical_map, bindings, index, mode, destination):
    invoke(['project', '--program', program, '--map', logical_map, '--bindings', bindings,
            '--frame-index', index, '--mode', mode, '--output', destination])
    return build.read(destination)


def refusal(args, diagnostic):
    result = subprocess.run([sys.executable, '-B', str(build.TOOL), *map(str, args)], capture_output=True, text=True)
    report = json.loads(result.stdout)
    require(result.returncode != 0 and any(row['code'] == diagnostic for row in report['diagnostics']),
            'Expected native refusal ' + diagnostic + ': ' + result.stdout + result.stderr)
    return report


def rejected(call, label, controls):
    try:
        call()
    except ValueError as error:
        controls.append({'case': label, 'result': str(error)})
    else:
        raise ValueError(label + ' escaped its guard')


def main():
    global EVIDENCE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frame-index', action='append', required=True, help='Explicit index URI; repeat for separate mode comparisons')
    parser.add_argument('--theory-root', type=Path, default=Path.home() / 'Library/Application Support/STDO/releases/v2.5.1-rc.2')
    parser.add_argument('--document-only', action='store_true', help='Exclude complete-package qualification before its freeze')
    args = parser.parse_args()
    started = time.monotonic()
    label = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    EVIDENCE = HERE / 'a_c/current/checks' / label
    EVIDENCE.mkdir(parents=True, exist_ok=False)
    write('ACTIVATION.json', {'document_only': args.document_only, 'selected_indexes': args.frame_index,
                              'started_utc': label, 'checker_sha256': build.sha(Path(__file__).read_bytes())})
    dependencies = build.verify_dependencies(args.theory_root)
    source = build.read(OUTPUT / 'SOURCE_INVENTORY.json')
    require(source['encoding_theory'] == {'release_uri': build.THEORY_URI, 'manifest_sha256': build.MANIFEST_SHA,
        'member': 'standards/AXIOMATIC_CALCULUS.md', 'member_sha256': build.THEORY_SHA}, 'Encoding theory differs')
    document_commit, members = build.documentary_inventory(source['document_source_input_commit'])
    require(source['document_members'] == members, 'Documentary inventory differs from frozen source')
    complete_commit = None if args.document_only else package_inventory(document_commit)
    account = build.read(build.ACCOUNT)
    current, exclusions = build.semantic_projection(account)
    build.validate_account(current)
    require(build.read(OUTPUT / 'source-account.json') == current, 'Packaged semantic projection differs from the current source account')
    require(source['interpretation']['semantic_account_sha256'] == build.sha((OUTPUT / 'source-account.json').read_bytes()), 'Semantic account digest differs')
    generation = build.read(HERE / 'a_c/current/GENERATION.json')
    require(generation['account_input_sha256'] == build.sha(build.ACCOUNT.read_bytes()), 'Generation names another source account')
    require(generation['excluded_construction_metadata'] == exclusions, 'Metadata separation differs from generation')
    program = build.read(OUTPUT / 'program.json')
    require(source['interpretation']['program_file_sha256'] == build.sha((OUTPUT / 'program.json').read_bytes()), 'Program identity differs')
    require(source['interpretation']['vocabulary_sha256'] == build.sha((OUTPUT / 'SIGNATURE.md').read_bytes()), 'Vocabulary identity differs')
    mapping = build.read(OUTPUT / 'MAPPING.json')
    require(mapping['document_source_input_commit'] == document_commit, 'Source mapping binds another subject')
    rows = assert_compilation(current, program, mapping)
    require(len(set(args.frame_index)) == len(args.frame_index), 'Duplicate selected index')
    require(set(args.frame_index) <= {f['uri'] for f in program['frame_indexes']}, 'Selected index is absent')
    before = {str(p.relative_to(PACKAGE)): build.sha(p.read_bytes()) for p in PACKAGE.rglob('*') if p.is_file()}
    result = subprocess.run([sys.executable, '-B', str(OUTPUT / 'bindings.py'), '--theory-root', str(args.theory_root)], capture_output=True, text=True)
    require(result.returncode == 0, result.stdout + result.stderr)
    binding_path = EVIDENCE / 'bindings.json'
    binding_path.write_text(result.stdout)
    invoke(['validate', '--program', OUTPUT / 'program.json', '--bindings', binding_path,
            '--output', EVIDENCE / 'validation.json', '--emit-map', EVIDENCE / 'map-reproduced.json'])
    require(build.read(EVIDENCE / 'map-reproduced.json') == build.read(OUTPUT / 'map.json'), 'Packaged logical map is stale')
    projections = []
    parity = ('closure', 'clause_relations', 'residual_routes', 'source_routes')
    for index in args.frame_index:
        name = build.slug(index.removeprefix(build.NS + 'index:'))
        files = [name + '-' + mode + '.json' for mode in ('reference-only', 'materialized')]
        views = [projection(OUTPUT / 'program.json', OUTPUT / 'map.json', binding_path, index, mode, EVIDENCE / file)
                 for mode, file in zip(('reference-only', 'materialized'), files)]
        require(all(views[0][key] == views[1][key] for key in parity), 'Projection modes disagree')
        projections.append({'index': index, 'clauses': len(views[0]['closure']['clauses']),
            'residuals': len(views[0]['closure']['residuals']), 'files': files,
            'bytes': {name: (EVIDENCE / name).stat().st_size for name in files},
            'scope': 'Explicit authored closure; no predicate evaluation or task-use acceptance'})
    controls = []
    damaged = copy.deepcopy(program)
    damaged['clauses'][0]['statement'] += ' Unsupported alteration.'
    write('program-map-drift-mutant.json', damaged)
    report = refusal(['project', '--program', EVIDENCE / 'program-map-drift-mutant.json', '--map', OUTPUT / 'map.json',
        '--bindings', binding_path, '--frame-index', args.frame_index[0], '--mode', 'reference-only'], 'map_mismatch')
    write('MAP_DRIFT_REFUSAL.json', report)
    controls.append({'case': 'Changed program with retained map', 'result': 'map_mismatch'})
    damaged_mapping = copy.deepcopy(mapping)
    damaged_mapping['rows'].pop()
    rejected(lambda: assert_compilation(current, program, damaged_mapping), 'Omitted source mapping', controls)
    damaged_current = copy.deepcopy(current)
    damaged_current['determinations'][0]['dependencies'].append('absent-owner-determination')
    rejected(lambda: build.validate_account(damaged_current), 'Unresolved determination dependency', controls)
    damaged_current = copy.deepcopy(current)
    target = next(r for r in damaged_current['determinations'] if r['representation_kind'] != 'non_deciding_locator')
    target['result_mapping'] = {'contract_ref': 'absent.shared.semantic.contract'}
    rejected(lambda: build.validate_account(damaged_current), 'Unresolved shared semantic contract', controls)
    # Native dangling refs are also rejected, independently of this adapter.
    damaged = copy.deepcopy(program)
    damaged['clauses'][0]['arguments'].append({'role': build.VOCAB + 'semantic-reference', 'ref': build.NS + 'contract:absent'})
    write('unresolved-native-reference-mutant.json', damaged)
    result = subprocess.run([sys.executable, '-B', str(build.TOOL), 'validate', '--program', str(EVIDENCE / 'unresolved-native-reference-mutant.json'), '--bindings', str(binding_path)], capture_output=True, text=True)
    require(result.returncode != 0, 'Native checker accepted unresolved semantic reference')
    native_report = json.loads(result.stdout)
    require(any(r['code'] == 'dangling_ref' for r in native_report['diagnostics']), 'Native control did not reach its intended reference guard')
    write('NATIVE_REFERENCE_REFUSAL.json', native_report)
    controls.append({'case': 'Native unresolved semantic reference', 'result': [r['code'] for r in native_report['diagnostics']]})
    # Definitions do not become constraints; required future inputs do not
    # create unconditional unknown outcomes or missing-source residuals.
    by_clause = {c['uri']: c for c in program['clauses']}
    null_definitions = [r for r in current['determinations'] if r.get('predicate') is None and r['representation_kind'] in {'definition_data', 'consumer_binding', 'non_deciding_locator'}]
    require(all(by_clause[build.clause_id(r['id'])]['clause_type'] == 'relation' for r in null_definitions), 'Null definition became a constraint')
    require(not program['residuals'] and not any(c['operator'].endswith('acquire-source') for c in program['clauses']), 'Construction or task unknowns were manufactured')
    controls.append({'case': 'Definition/locator and future-input distinction', 'result': {'null_relations': len(null_definitions), 'manufactured_residuals': 0}})
    # Exact source-block corruption is detected before relying on source routes.
    damaged_current = copy.deepcopy(current)
    block_row = next(r for r in damaged_current['determinations'] if r.get('source_clauses'))
    block_row['source_clauses'][0]['sha256'] = '0' * 64
    rejected(lambda: build.validate_account(damaged_current), 'Source block digest drift', controls)
    with tempfile.TemporaryDirectory(prefix='relocated-', dir=EVIDENCE) as temporary:
        cold = Path(temporary) / 'successor'
        shutil.copytree(PACKAGE, cold)
        result = subprocess.run([sys.executable, '-B', str(cold / 'interpretation/bindings.py'), '--theory-root', str(args.theory_root)], capture_output=True, text=True)
        require(result.returncode == 0, result.stdout + result.stderr)
        cold_binding = Path(temporary) / 'bindings.json'
        cold_binding.write_text(result.stdout)
        cold_view = projection(cold / 'interpretation/program.json', cold / 'interpretation/map.json', cold_binding,
                               args.frame_index[0], 'reference-only', Path(temporary) / 'projection.json')
        warm_view = build.read(EVIDENCE / projections[0]['files'][0])
        require(all(cold_view[key] == warm_view[key] for key in parity), 'Relocation changed logical acquisition')
        controls.append({'case': 'Relocated unchanged package with verified encoding theory', 'result': 'same selected closure and routes'})
        owner = cold / current['determinations'][0]['owner']['path']
        owner.write_bytes(owner.read_bytes() + b'\nChanged source observation.\n')
        result = subprocess.run([sys.executable, '-B', str(cold / 'interpretation/bindings.py'), '--theory-root', str(args.theory_root)], capture_output=True, text=True)
        require(result.returncode != 0 and 'Documentary subject drift' in result.stderr + result.stdout, 'Changed documentary source accepted by bindings')
        controls.append({'case': 'Relocated source owner altered', 'result': 'source drift refused before binding'})
        source_report = refusal(['project', '--program', cold / 'interpretation/program.json', '--map', cold / 'interpretation/map.json',
            '--bindings', cold_binding, '--frame-index', args.frame_index[0], '--mode', 'reference-only'], 'map_mismatch')
        write('SOURCE_DRIFT_REFUSAL.json', source_report)
        controls.append({'case': 'Source drift bypassing binding preflight', 'result': 'native map_mismatch'})
    after = {str(p.relative_to(PACKAGE)): build.sha(p.read_bytes()) for p in PACKAGE.rglob('*') if p.is_file()}
    require(before == after, 'Package changed during qualification; discard this result')
    report = {'kind': 'codex-current-interpretation-mechanics', 'valid': True,
        'document_source_input_commit': document_commit, 'complete_package_input_commit': complete_commit,
        'scope': 'documentary construction check' if args.document_only else 'frozen complete-package mechanical check',
        'common_input_commit': build.COMMON_INPUT, 'dependency_verification': dependencies,
        'account_input_commit': generation['account_input_commit'], 'account_sha256': generation['account_input_sha256'], 'semantic_account_sha256': build.sha((OUTPUT / 'source-account.json').read_bytes()),
        'program_sha256': build.sha((OUTPUT / 'program.json').read_bytes()), 'map_sha256': build.sha((OUTPUT / 'map.json').read_bytes()),
        'checker_sha256': build.sha(Path(__file__).read_bytes()), 'generator_sha256': build.sha(Path(build.__file__).read_bytes()),
        'represented_units': len(rows), 'shared_contracts': len(current['semantic_contracts']),
        'representation_kinds': dict(build.Counter(r['representation_kind'] for r in current['determinations'])),
        'selected_projections': projections, 'controls': controls,
        'elapsed_seconds': time.monotonic() - started, 'package_unchanged': True,
        'package_interpretation_bytes': sum(p.stat().st_size for p in OUTPUT.iterdir() if p.is_file()),
        'retained_evidence_directory': str(EVIDENCE.relative_to(HERE)),
        'limits': ['Mechanical account/compiler consistency does not prove source completeness or fidelity.',
            'Authored predicate logic requires independent source-first semantic assessment.',
            'Relocation uses separately verified RC2 encoding theory; no new release policy is selected.',
            'No finite-model test is counted as execution of these clauses.',
            'No fresh actor task use, semantic acceptance, issued identity or release qualification.']}
    write('MECHANICAL_RESULT.json', report)
    (HERE / 'a_c/current/MECHANICAL_RESULT.json').write_bytes(build.json_bytes(report))
    print(json.dumps({'valid': True, 'source': document_commit, 'complete_package': complete_commit,
        'determinations': len(rows), 'projections': len(projections), 'controls': len(controls),
        'elapsed_seconds': report['elapsed_seconds'], 'evidence': report['retained_evidence_directory']}))


if __name__ == '__main__':
    main()
