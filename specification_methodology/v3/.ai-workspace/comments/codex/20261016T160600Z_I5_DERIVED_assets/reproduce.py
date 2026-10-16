#!/usr/bin/env python3
"""Read exact Git inputs into an isolated tree and reproduce the I5 carrier checks.

This script never writes a candidate or Git state. Review evidence is written
beside this script. Frozen author conclusions are not inputs. The optional
publication commit must be an explicit frozen output supplied for this review.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import time

sys.dont_write_bytecode = True
ASSETS = Path(__file__).resolve().parent
REPO = Path('/Users/jim/src/apps/specification_methodology-codex')
BASE = 'specification_methodology/v3/build_tenants/codex/'
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
DOC = '1e4bed65fe2216b288903ea553391c45ff90e9c1'
TOOLS = 'fd450061c39a5fbb10625c99b64a52b518d1d00e'
ACCOUNT = '57f711d964cd4eac8ed8523460cecc68bcaa63fb'
PRIOR = '62318d3b0be35985a0397aa39daee0ec8836eabc'
PYTHON = '/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python'
THEORY = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def raw(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=REPO)


def names(commit, prefix):
    return subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit, '--', prefix], cwd=REPO, text=True).splitlines()


def write(name, value):
    (ASSETS / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--publication-commit')
    parser.add_argument('--reuse-root', type=Path,
                        help='Reuse only an already verified isolated tree and exact prior publication comparison')
    parser.add_argument('--skip-native-sweep', action='store_true',
                        help='Do not repeat the redundant eighteen-projection author sweep')
    args = parser.parse_args()
    started = time.monotonic()
    root = args.reuse_root or Path(tempfile.mkdtemp(prefix='I5_DERIVED_review_', dir='/tmp'))
    retained_inputs = {}
    retained_generation = None
    if args.reuse_root:
        previous = json.loads((ASSETS / 'FROZEN_INPUTS.json').read_text())
        retained_inputs = {(r['commit'], r['path']): r for r in previous['entries']}
        publication = json.loads((ASSETS / 'PUBLICATION_REPRODUCTION.json').read_text())
        if not publication['all_equal'] or Path(publication['temporary_root']) != root:
            raise ValueError('The reused tree lacks its exact publication comparison')
        for row in publication['members']:
            if sha((root / row['path']).read_bytes()) != row['reproduced_sha256']:
                raise ValueError('Previously reproduced publication drift')
        retained_generation = next(r for r in json.loads((ASSETS / 'COMMANDS.json').read_text()) if r['name'] == 'generate')
        if retained_generation['exit_code'] != 0:
            raise ValueError('Generation has no successful retained observation')
    entries = []

    def extract(commit, path):
        if (commit, path) in retained_inputs:
            prior = retained_inputs[commit, path]
            out = root / path
            data = os.readlink(out).encode() if out.is_symlink() else out.read_bytes()
            if sha(data) != prior['sha256']:
                raise ValueError('Retained frozen input drift: ' + path)
            entries.append(prior)
            return
        data = raw(commit, path)
        out = root / path
        out.parent.mkdir(parents=True, exist_ok=True)
        mode = '100644'
        if '/a_c/install/' in path:
            mode = subprocess.check_output(['git', 'ls-tree', commit, '--', path], cwd=REPO, text=True).split()[0]
        if mode == '120000':
            out.symlink_to(data.decode())
        else:
            out.write_bytes(data)
        entries.append({'commit': commit, 'path': path, 'bytes': len(data), 'sha256': sha(data)})

    for path in names(DOC, BASE + 'successor/'):
        if not path.startswith(BASE + 'successor/interpretation/'):
            extract(DOC, path)
    for path in names(TOOLS, BASE + 'qualification/C3/iteration-5/tools/'):
        extract(TOOLS, path)
    extract(TOOLS, BASE + 'qualification/C3/iteration-5/INPUTS.json')
    inputs = json.loads(raw(TOOLS, BASE + 'qualification/C3/iteration-5/INPUTS.json'))
    for relative in inputs['libraries']:
        extract(TOOLS, BASE + 'qualification/C3/' + relative)
    for path in names(TOOLS, BASE + 'a_c/install/'):
        extract(TOOLS, path)
    extract(TOOLS, BASE + 'a_c/INSTALL_RECEIPT.json')
    for name in ('DETERMINATIONS.json', 'ACCOUNT_INTEGRATION.json'):
        extract(ACCOUNT, BASE + 'qualification/C3/iteration-5/' + name)
    for name in ('FRAME_INPUTS.json', 'COMPRESSION_RECONCILIATION.json', 'FRAME_ADDITIONS.json'):
        extract(DOC, BASE + 'qualification/C3/iteration-5/' + name)
    extract(DOC, BASE + 'qualification/C3/iteration-5/tools/measure_reduction.py')
    extract(DOC, BASE + 'qualification/C3/iteration-5/REDUCTION_PROTOCOL.md')
    for path in names(COMMON, 'specification_methodology/v3/specification/'):
        extract(COMMON, path)
    extract(PRIOR, BASE + 'qualification/C3/iteration-4/FRAME_INPUTS.json')
    extract(PRIOR, BASE + 'qualification/C3/iteration-4/INPUTS.json')
    extract(PRIOR, BASE + 'qualification/C3/iteration-4/DETERMINATIONS.json')
    extract(PRIOR, BASE + 'qualification/C3/iteration-4/ACCOUNT_INTEGRATION.json')
    # The pinned renderer loads its historical parser from this explicit path.
    for relative in ['synthesis/check_artifacts.py', 'synthesis/derivation_material.py']:
        if not (root / BASE / 'qualification/C3' / relative).exists():
            extract(TOOLS, BASE + 'qualification/C3/' + relative)

    write('FROZEN_INPUTS.json', {'entries': entries, 'processed_bytes': sum(e['bytes'] for e in entries),
          'boundary': 'Mechanically extracted files; not all bodies were presented to the Reviewer.'})

    tenant = root / BASE
    package = tenant / 'successor'
    here = tenant / 'qualification/C3/iteration-5'
    tool_dir = here / 'tools'
    (package / 'interpretation').mkdir(exist_ok=True)
    env = dict(os.environ)
    env.update(GIT_DIR=subprocess.check_output(['git', 'rev-parse', '--absolute-git-dir'], cwd=REPO, text=True).strip(), GIT_WORK_TREE=str(root), PYTHONDONTWRITEBYTECODE='1')
    commands = [retained_generation] if retained_generation else []

    def run(name, command):
        begin = time.monotonic()
        result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
        observation = {'name': name, 'command': command, 'exit_code': result.returncode,
                       'stdout': result.stdout, 'stderr': result.stderr,
                       'elapsed_seconds': time.monotonic() - begin}
        commands.append(observation)
        write('COMMANDS.json', commands)
        if result.returncode:
            raise RuntimeError(name + ': ' + result.stderr + result.stdout)
        return result

    # The exact generator does all documentary and dependency verification.
    if not args.reuse_root:
        run('generate', [PYTHON, '-B', str(tool_dir / 'generate_interpretation.py'),
                        '--source-commit', DOC, '--account-commit', ACCOUNT,
                        '--theory-root', THEORY])
    for name in ('GENERATION.json', 'QUALIFICATION_EQUIVALENCE.json', 'DEPENDENCY_VERIFICATION.json', 'validation.json'):
        value = json.loads((here / 'interpretation' / name).read_text())
        write('REPRODUCED_' + name, value)
    if not args.skip_native_sweep:
        run('native_check', [PYTHON, '-B', str(tool_dir / 'check_interpretation.py'), '--theory-root', THEORY])
        write('REPRODUCED_NATIVE_CHECK.json', json.loads((here / 'interpretation/NATIVE_CHECK.json').read_text()))

    # Independently selected controls use a real generated qualification.
    sys.path.insert(0, str(tool_dir))
    spec = importlib.util.spec_from_file_location('reviewed_build', tool_dir / 'build_interpretation.py')
    build = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(build)
    program = json.loads((package / 'interpretation/program.json').read_text())
    semantic = json.loads((package / 'interpretation/source-account.json').read_text())
    controls = []
    for clause in program['clauses']:
        scopes = {}
        selected = None
        for arg in clause['arguments']:
            role = arg['role'].removeprefix(build.VOCAB)
            if role == 'semantic-record':
                scopes['semantic-record'] = json.loads(arg['literal'])
            elif role == 'inlined-contract':
                val = json.loads(arg['literal']); scopes[val['identity']] = val['definition']
            elif role == 'acquisition-route':
                val = json.loads(arg['literal'])
                if 'qualification_ref' in val:
                    selected = val
                    break
        if selected:
            break
    assert selected is not None
    selected_identity = {'clause': clause['uri'], 'scope': selected['scope'], 'pointer': selected['pointer'], 'qualification_ref': selected['qualification_ref']}
    expected = build.resolve_pointer(scopes[selected['scope']], selected['qualification_ref']['pointer'])
    assert build.expand_qualification(selected, scopes) == expected
    controls.append({'case': 'positive exact object expansion', 'observed': 'equal', 'expected': 'equal'})

    def refusal(name, record_change=None, scope_change=None):
        record, bases = copy.deepcopy(selected), copy.deepcopy(scopes)
        if record_change:
            record_change(record)
        if scope_change:
            scope_change(bases)
        try:
            build.expand_qualification(record, bases)
        except (ValueError, KeyError, TypeError) as error:
            controls.append({'case': name, 'observed': 'refused', 'expected': 'refused', 'reason': str(error)})
        else:
            controls.append({'case': name, 'observed': 'accepted', 'expected': 'refused'})

    refusal('missing reference scope', scope_change=lambda b: b.clear())
    refusal('cross-scope substitution', record_change=lambda r: r['qualification_ref'].update(scope='foreign-scope'))
    refusal('missing pointer target', record_change=lambda r: r['qualification_ref'].update(pointer='/missing'))
    refusal('invalid RFC 6901 escape', record_change=lambda r: r['qualification_ref'].update(pointer='/~2'))
    refusal('reference digest drift', record_change=lambda r: r['qualification_ref'].update(sha256='0' * 64))
    refusal('required condition changed', record_change=lambda r: r.update(required_when='unconditional permission'))
    refusal('required condition missing', record_change=lambda r: r.pop('required_when'))
    refusal('ambiguous inline and referenced qualification', record_change=lambda r: r.update(qualification=expected))
    refusal('unclassified reference field', record_change=lambda r: r['qualification_ref'].update(unexpected=True))
    def alter_material_clause(bases):
        build.resolve_pointer(bases[selected['scope']], selected['qualification_ref']['pointer'])['review_probe_material_condition'] = 'changed'
    refusal('material qualification object changed', scope_change=alter_material_clause)
    literal_null = {'qualification': None}
    controls.append({'case': 'permitted literal null qualification', 'observed': build.expand_qualification(literal_null, {}) is None, 'expected': True})
    assert all(c['observed'] == c['expected'] for c in controls)
    write('INDEPENDENT_QUALIFICATION_PROBES.json', {'source': TOOLS, 'selection': selected_identity, 'controls': controls,
          'limits': 'Local transformation/refusal observations only; no actor-use, semantic acceptance or universal adversarial completeness.'})

    partial_path = ASSETS / 'PARTIAL_NATIVE_SWEEP.json'
    if args.skip_native_sweep and partial_path.exists():
        partial = json.loads(partial_path.read_text())
        checked = []
        archive = ASSETS / 'PARTIAL_NATIVE_OUTPUTS.tar.gz'
        if sha(archive.read_bytes()) != partial['archive_sha256']:
            raise ValueError('Retained native archive drift')
        for row in partial['observations']:
            if row['native_pass_credit'] and row['name'].endswith('-materialized.json'):
                with tarfile.open(archive, 'r:gz') as stored:
                    data = stored.extractfile(row['name']).read()
                if sha(data) != row['sha256']:
                    raise ValueError('Retained native output drift')
                value = json.loads(data)
                counts = build.validate_occurrences({'clauses': value['clauses']}, semantic['semantic_contracts'])
                checked.append({'case': row['name'], 'sha256': row['sha256'], 'checked_occurrences': counts})
        write('RETAINED_NATIVE_OCCURRENCE_CHECK.json', {'cases': checked,
              'scope': 'Occurrence and qualification resolution on completed native outputs only. Remaining projections have no credit.'})

    # Re-render all task views from frozen route inputs, comparing every byte.
    before = {str(p.relative_to(package)): sha(p.read_bytes()) for p in (package / 'standards/frames').glob('*.md')}
    run('views', [PYTHON, '-B', str(tool_dir / 'prepare_views.py'),
                  '--reconciliation', str(here / 'COMPRESSION_RECONCILIATION.json'),
                  '--routes', str(here / 'FRAME_ADDITIONS.json')])
    after = {str(p.relative_to(package)): sha(p.read_bytes()) for p in (package / 'standards/frames').glob('*.md')}
    write('VIEW_REPRODUCTION.json', {'before': before, 'after': after, 'equal': before == after,
          'limits': 'Exact renderer reproduction does not establish route sufficiency for any actual task.'})
    assert before == after

    run('source_route_costs', [PYTHON, '-B', str(tool_dir / 'measure_reduction.py'),
                              '--source-commit', DOC, '--theory-root', THEORY])
    measured = (here / 'REDUCTION_MEASUREMENTS.json').read_bytes()
    frozen_measurement = raw('1529a725ad5498c43ca651133b1409bcf5a10617', BASE + 'qualification/C3/iteration-5/REDUCTION_MEASUREMENTS.json')
    write('REPRODUCED_REDUCTION_MEASUREMENTS.json', json.loads(measured))
    write('REDUCTION_REPRODUCTION.json', {'published_commit': '1529a725ad5498c43ca651133b1409bcf5a10617',
          'published_sha256': sha(frozen_measurement), 'reproduced_sha256': sha(measured), 'equal': measured == frozen_measurement})
    assert measured == frozen_measurement

    if args.publication_commit:
        comparison = []
        for path in names(args.publication_commit, BASE + 'successor/interpretation/'):
            expected_data = raw(args.publication_commit, path)
            actual = (root / path).read_bytes()
            comparison.append({'path': path, 'published_sha256': sha(expected_data), 'reproduced_sha256': sha(actual), 'equal': actual == expected_data,
                               'published_bytes': len(expected_data), 'reproduced_bytes': len(actual)})
        equal = bool(comparison) and all(r['equal'] for r in comparison)
        write('PUBLICATION_REPRODUCTION.json', {'temporary_root': str(root), 'documentary_commit': DOC,
              'account_commit': ACCOUNT, 'publication_commit': args.publication_commit,
              'members': comparison, 'all_equal': equal})
        if not equal:
            raise ValueError('The reproduced publication differs from its frozen comparison subject')
    write('FROZEN_INPUTS.json', {'entries': entries, 'processed_bytes': sum(e['bytes'] for e in entries),
          'boundary': 'Mechanically extracted files; not all bodies were presented to the Reviewer.'})
    write('REPRODUCTION.json', {'temporary_root': str(root), 'documentary_commit': DOC, 'tooling_commit': TOOLS,
          'account_commit': ACCOUNT, 'publication_commit': args.publication_commit,
          'elapsed_seconds': time.monotonic() - started, 'independent_controls': len(controls),
          'result': 'satisfied', 'native_cost': None, 'active_context': None,
          'native_sweep_repeated': not args.skip_native_sweep,
          'retained_generation_used': bool(args.reuse_root)})
    print(json.dumps({'temporary_root': str(root), 'independent_controls': len(controls), 'elapsed_seconds': time.monotonic() - started}))


if __name__ == '__main__':
    main()
