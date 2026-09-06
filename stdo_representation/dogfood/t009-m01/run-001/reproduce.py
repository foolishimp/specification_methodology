"""Replay T009 M01's bounded RC4 baseline; this is evidence, not Product code."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STDO_STORE = Path('/Users/jim/Library/Application Support/STDO')
AXIOM_REF = 'refs/tags/axiom_indexer/v2.5.0-rc.4'
REP_REF = 'refs/tags/stdo_representation/v2.5.0-rc.4'
PREFIX = 'stdo://releases/v2.5.0-rc.4/standards/'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save(name: str, value: object) -> None:
    (HERE / name).write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def call(args: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def inventory(root: Path) -> tuple[str, list[dict[str, str]]]:
    rows = []
    record = (root / 'releases/v2.5.0.md').read_text()
    for kind, rel, expected in re.findall(
        r'^\| (file|symlink) \| `([^`]+)`(?: -> `[^`]+`)? \| `([0-9a-f]{64})` \|$',
        record, re.M,
    ):
        path = root / rel
        raw = os.readlink(path).encode() if kind == 'symlink' else path.read_bytes()
        actual = digest(raw)
        if actual != expected:
            raise ValueError(f'member mismatch: {rel}')
        rows.append({'path': rel, 'kind': kind, 'sha256': actual})
    rows.sort(key=lambda row: row['path'])
    data = ''.join(f"{r['sha256']}  {r['kind']}  {r['path']}\n" for r in rows)
    return digest(data.encode()), rows


def main() -> None:
    result = {'actor': '/root/t030_m01_review', 'role': 'Writer/Worker',
              'claim': 'T009 M01 actual RC4 mechanics and source-route baseline',
              'start_checkpoint': 'e8a19fbcf60926818172a9eefd48f4fcafea157f',
              'python': sys.version, 'head_at_execution': git('rev-parse', 'HEAD')}
    statuses = {}
    for child, definition in [('stdo_representation', 'stdo_representation.json'),
                              ('axiom_indexer', 'stdo_default.json')]:
        proc = call(['stdo', 'status', '--definition', f'{child}/{definition}', '--verify'])
        status = json.loads(proc.stdout)
        save(f'{child}-status.json', status)
        if proc.returncode or not status['valid'] or status['failures']:
            raise ValueError(f'invalid basis: {child}')
        statuses[child] = {key: status[key] for key in
                           ('definition_id', 'basis', 'manifest_sha256', 'valid', 'failures')}
    result['product_status'] = statuses
    result['refs'] = {ref: {'type': git('cat-file', '-t', ref),
                            'tag_object': git('rev-parse', ref),
                            'commit': git('rev-parse', ref + '^{}')}
                      for ref in (AXIOM_REF, REP_REF)}
    expected_tags = {AXIOM_REF: '4750e09639c118f1097d4ea046fe23d26713f96b',
                     REP_REF: 'd85d25482f9d9132147bea189b0fe0aca1929dff'}
    if any(r['type'] != 'tag' or r['tag_object'] != expected_tags[ref] or
           r['commit'] != 'a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2'
           for ref, r in result['refs'].items()):
        raise ValueError('immutable dependency ref mismatch')

    with tempfile.TemporaryDirectory(prefix='t009-m01-') as temp:
        work = Path(temp)
        archive = subprocess.check_output(['git', 'archive', '--format=tar', AXIOM_REF], cwd=ROOT)
        with tarfile.open(fileobj=io.BytesIO(archive)) as source:
            source.extractall(work)
        result['skill_archive_path_probe'] = {
            'documented_executable_exists': (work / 'build_tenants/core/code/ac.py').is_file(),
            'declared_project_subtree_executable_exists': (work / 'axiom_indexer/build_tenants/core/code/ac.py').is_file(),
            'archive_from': AXIOM_REF,
            'disposition': 'Representation M03 routing repair; use exact declared Axiom subtree for this baseline',
        }
        axiom = work / 'axiom_indexer'
        rep = work / 'stdo_representation'
        executable = axiom / 'build_tenants/core/code/ac.py'
        inv, rows = inventory(axiom)
        if inv != '7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6':
            raise ValueError('Axiom inventory mismatch')
        result['axiom_inventory'] = {'sha256': inv, 'members': rows}
        inv, rows = inventory(rep)
        if inv != '32dd04f5644a05c04c844a28d1978d1c1ffdd5e7f20473b7d7f8626e1e07e830':
            raise ValueError('Representation inventory mismatch')
        result['representation_inventory'] = {'sha256': inv, 'members': rows}
        result['frame_basis_distinction'] = {
            'released_construction': digest((rep / 'specification/REFERENCE_FRAME_BASIS.md').read_bytes()),
            'current_source': digest((ROOT / 'stdo_representation/specification/REFERENCE_FRAME_BASIS.md').read_bytes()),
            'source_skill_at_start_matches_release': (rep / 'skills/stdo-representation/SKILL.md').read_bytes() ==
                subprocess.check_output(['git', 'show', result['start_checkpoint'] +
                    ':stdo_representation/skills/stdo-representation/SKILL.md'], cwd=ROOT),
        }
        source_dir = rep / 'build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4'
        program_path = source_dir / 'axiomatic-program.json'
        program_before = program_path.read_bytes()
        program = json.loads(program_before)
        bindings = {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
                    'bindings': [{'uri_prefix': PREFIX, 'path': str(STDO_STORE / 'releases/v2.5.0-rc.4/standards')}]}
        binding_path = work / 'bindings.json'
        binding_path.write_text(json.dumps(bindings))
        base_map = source_dir / 'logical-constraint-map.json'
        generated = work / 'map.json'
        proc = call([sys.executable, str(executable), 'validate', '--program', str(program_path),
                     '--bindings', str(binding_path), '--output', str(HERE / 'validation-report.json'),
                     '--emit-map', str(generated)])
        report = json.loads((HERE / 'validation-report.json').read_text())
        result['reproduction'] = {'exit': proc.returncode, 'status': report['status'],
            'program_unchanged': program_path.read_bytes() == program_before,
            'map_byte_equal': generated.read_bytes() == base_map.read_bytes(),
            'map_file_sha256': digest(generated.read_bytes()),
            'map_intrinsic_sha256': json.loads(generated.read_text())['map_sha256']}
        if proc.returncode or not result['reproduction']['program_unchanged'] or not result['reproduction']['map_byte_equal']:
            raise ValueError('RC4 reproduction failed')
        tests = []
        for flags, name in [([], 'normal'), (['-O'], 'optimized')]:
            proc = call([sys.executable, *flags, '-m', 'unittest', 'discover', '-s',
                         str(axiom / 'build_tenants/core/code'), '-p', 'test_*.py', '-v'])
            (HERE / f'tests-{name}.txt').write_text(proc.stdout + proc.stderr)
            tests.append({'mode': name, 'exit': proc.returncode,
                          'test_file_sha256': digest((axiom / 'build_tenants/core/code/test_ac.py').read_bytes())})
            if proc.returncode:
                raise ValueError(f'{name} mechanical tests failed')
        result['existing_tests'] = tests
        variants = {}
        p = copy.deepcopy(program); p['symbols'].append(copy.deepcopy(p['symbols'][0])); variants['duplicate_identity'] = (p, bindings)
        p = copy.deepcopy(program); p['clauses'][0]['arguments'][0]['ref'] = 'urn:t009:missing'; p['clauses'][0]['arguments'][0].pop('literal', None); variants['dangling_ref'] = (p, bindings)
        p = copy.deepcopy(program); p['symbols'][0]['source_refs'] = [PREFIX + 'SPEC_METHOD.md#t009-missing']; variants['unresolved_fragment'] = (p, bindings)
        p = copy.deepcopy(program); p['symbols'][0]['source_refs'] = []; variants['ungrounded'] = (p, bindings)
        p = copy.deepcopy(program); p['residuals'][0]['re_entry_refs'] = [PREFIX + 'SPEC_METHOD.md#t009-missing']; variants['broken_residual'] = (p, bindings)
        p = copy.deepcopy(program); p['symbols'][0]['source_refs'] = [PREFIX + '../outside.md']; variants['escaped_binding'] = (p, bindings)
        b = copy.deepcopy(bindings); b['bindings'].append(copy.deepcopy(b['bindings'][0])); variants['duplicate_binding'] = (program, b)
        b = copy.deepcopy(bindings); b['bindings'][0]['uri_prefix'] = 'stdo://releases/missing/'; variants['unresolved_binding'] = (program, b)
        refusals = []
        for name, (p, b) in variants.items():
            pp, bp = work / 'negative-program.json', work / 'negative-bindings.json'
            pp.write_text(json.dumps(p)); bp.write_text(json.dumps(b)); generated.write_text('stale map')
            proc = call([sys.executable, str(executable), 'validate', '--program', str(pp),
                         '--bindings', str(bp), '--emit-map', str(generated)])
            value = json.loads(proc.stdout)
            row = {'case': name, 'exit': proc.returncode, 'report': value,
                   'stale_map_removed': not generated.exists()}
            refusals.append(row)
            if proc.returncode == 0 or not row['stale_map_removed']:
                raise ValueError(f'refusal failed: {name}')
        save('refusals.json', refusals)
        result['refusals'] = [{'case': r['case'], 'exit': r['exit'],
                              'codes': sorted({d['code'] for d in r['report']['diagnostics']}),
                              'stale_map_removed': r['stale_map_removed']} for r in refusals]
        sections = HERE / 'sections.json'
        if sections.exists():
            proc = call([sys.executable, str(executable), 'join', '--input', str(sections),
                         '--output', str(HERE / 'request.txt')])
            expected = '\n\n'.join(row['label'] + '\n' + row['text'] for row in json.loads(sections.read_text())).encode()
            actual = (HERE / 'request.txt').read_bytes()
            result['actual_task_join'] = {'exit': proc.returncode, 'exact_bytes': actual == expected,
                                          'sha256': digest(actual)}
            if proc.returncode or actual != expected:
                raise ValueError('actual-task join failed')
    result['result'] = 'mechanics_sufficient_for_selected_M01_dependencies'
    save('baseline.json', result)
    print(json.dumps({key: result[key] for key in ('skill_archive_path_probe', 'frame_basis_distinction',
          'reproduction', 'existing_tests', 'refusals', 'actual_task_join', 'result')}, indent=2))


if __name__ == '__main__':
    main()
