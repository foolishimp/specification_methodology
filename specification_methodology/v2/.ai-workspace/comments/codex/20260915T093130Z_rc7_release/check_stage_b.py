"""Bounded RC7 replay using existing Axiom and skill checks; no semantic verdict."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
ART = ROOT / 'stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7'
AC = ROOT / 'axiom_indexer/build_tenants/core/code/ac.py'
PY = sys.executable

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')

def main():
    results = []
    inputs = {str(p.relative_to(ROOT)): sha(p) for p in ART.iterdir() if p.is_file()}
    with tempfile.TemporaryDirectory(prefix='mechanical-temp.', dir=OUT) as tmp:
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', TMPDIR=tmp)
        def run(label, argv, cwd=ROOT):
            result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
            (OUT / (label + '.stdout.txt')).write_text(result.stdout)
            (OUT / (label + '.stderr.txt')).write_text(result.stderr)
            results.append({'label': label, 'argv': list(map(str, argv)), 'cwd': str(cwd), 'exit_code': result.returncode})
            put(OUT / 'stage-b-mechanical-checks.json', {'commands': results, 'semantic_acceptance': False})
            if result.returncode:
                raise RuntimeError(label + ': ' + result.stderr + result.stdout)
        for runtime, interpreter in [('python312', '/private/tmp/stdo-rc5-installed-manager-20260906/bin/python'), ('python313', PY)]:
            for mode, flags in [('normal', []), ('optimized', ['-O'])]:
                run('axiom-tests-' + runtime + '-' + mode, [interpreter, '-B', *flags, '-m', 'unittest', 'discover', '-s', 'build_tenants/core/code', '-p', 'test_*.py', '-v'], ROOT / 'axiom_indexer')
            run('direct-regression-' + runtime, [interpreter, '-B', str(OUT / 'runtime_discriminator.py'), '--repaired'])
        run('skill-structure', ['/private/tmp/stdo-rc5-installed-manager-20260906/bin/python', '-B', '/Users/jim/.codex/skills/.system/skill-creator/scripts/quick_validate.py', str(ROOT / 'stdo_representation/skills/stdo-representation')])
        run('cohort-content', [PY, '-B', str(ROOT / 'scripts/check_stack_release.py'), '--phase', 'content'])
        common = ['--program', str(ART / 'axiomatic-program.json'), '--bindings', str(OUT / 'representation-rc7-bindings.json')]
        report, output_map = Path(tmp) / 'report.json', Path(tmp) / 'map.json'
        run('index-replay', [PY, '-B', str(AC), 'validate', *common, '--output', str(report), '--emit-map', str(output_map)])
        assert report.read_bytes() == (ART / 'validation-report.json').read_bytes()
        assert output_map.read_bytes() == (ART / 'logical-constraint-map.json').read_bytes()
        selections = {'executive': ['urn:stdo-representation:frame-index:executive-event-driven-attention'],
            'steel': ['urn:stdo-representation:frame-index:executive-steel-thread-delivery'],
            'worker': ['urn:stdo-representation:frame-index:t009:complete-update-worker'],
            'reviewer': ['urn:stdo-representation:frame-index:t009:complete-update-reviewer']}
        selections['combined'] = selections['worker'] + selections['reviewer']
        for name, indexes in selections.items():
            views = []
            for mode in ('reference-only', 'materialized'):
                output = Path(tmp) / (name + '-' + mode + '.json')
                run('projection-replay-' + name + '-' + mode, [PY, '-B', str(AC), 'project', *common,
                    '--map', str(output_map), *[x for i in indexes for x in ('--frame-index', i)], '--mode', mode, '--output', str(output)])
                assert output.read_bytes() == (OUT / 'representation-projections' / output.name).read_bytes()
                views.append(json.loads(output.read_text()))
            for field in ('closure', 'clause_relations', 'residual_routes', 'source_routes', 'frame_refs', 'frame_indexes'):
                assert views[0][field] == views[1][field], (name, field)
        run('diff-check', ['git', 'diff', '--check'])
    assert inputs == {str(p.relative_to(ROOT)): sha(p) for p in ART.iterdir() if p.is_file()}
    put(OUT / 'stage-b-mechanical-checks.json', {'status': 'satisfied', 'commands': results,
        'input_sha256': inputs, 'input_preservation': True, 'report_and_map_byte_reproduction': True,
        'projection_byte_reproductions': 10, 'same_closure_both_modes': True,
        'semantic_acceptance': False, 'native_qualification': False})
    print(json.dumps({'status': 'satisfied', 'commands': len(results), 'projection_reproductions': 10}))

if __name__ == '__main__':
    main()
