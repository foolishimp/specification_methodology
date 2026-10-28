"""Independent bounded repair controls. No compiler/toolchain is copied or run."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from unittest.mock import patch

REPO = Path('/Users/jim/src/apps/specification_methodology')
WORK = REPO / 'a_c/.ai-workspace/work/T012_FORMAL_GATE'
REVIEW = WORK / 'review'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def main():
    freeze_path = WORK / 'lean/SOURCE_FREEZE_002.json'
    graph_path = WORK / 'graphify/namespace-repair-001/SOURCE_MANIFEST.json'
    assert sha(freeze_path) == 'a3dda842076022394543ff45e5e0c27764e2a30f22ede67b91be82f4a1c0879a'
    assert sha(graph_path) == 'd660e97cb07c773fe5d553b171f9eb705b586e395a9a031a3e4a295b639e1ed4'
    freeze = json.loads(freeze_path.read_text())
    graph = json.loads(graph_path.read_text())
    out = REVIEW / 'repaired-controls-001'
    out.mkdir(exist_ok=False)
    clone = out / 'checker'
    for name, digest in freeze['source_files'].items():
        original = REPO / 'a_c/build_tenants/lean' / name
        assert sha(original) == digest, name
        target = clone / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
    graph_dir = out / 'graphify-code'
    graph_dir.mkdir()
    copied_graph = {}
    for name in ('ac_formal_gate.py', 'ac_generate.py', 'ac_support_core.py',
                 'ac_support_effects.py', 'ac_graph.py', 'ac_support_composition.py'):
        relative = 'a_c/build_tenants/graphify/code/' + name
        original = REPO / relative
        if relative in graph['files']:
            assert sha(original) == graph['files'][relative], name
        copied_graph[relative] = sha(original)
        shutil.copyfile(original, graph_dir / name)
    shutil.copyfile(freeze_path, out / 'LEAN_SOURCE_FREEZE.json')
    shutil.copyfile(graph_path, out / 'GRAPHIFY_SOURCE_MANIFEST.json')
    env = {k: v for k, v in os.environ.items() if k not in ('PYTHONPATH', 'PYTHONHOME')}
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    python = Path(sys.executable).resolve()
    command = [str(python), '-I', '-S', '-B', str(clone / 'scripts/formal_gate.py')]
    rows = []

    def run(label, arguments, expected):
        completed = subprocess.run(command + arguments, cwd=out, env=env,
                                   capture_output=True, text=True, timeout=15)
        (out / (label + '.stdout')).write_text(completed.stdout)
        (out / (label + '.stderr')).write_text(completed.stderr)
        assert completed.returncode == expected, (label, completed.stderr, completed.stdout)
        return json.loads(completed.stdout)

    identity = run('identity', ['identity'], 0)
    assert identity == freeze['runtime_identity']
    spec = importlib.util.spec_from_file_location('review_exact_parent', graph_dir / 'ac_formal_gate.py')
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    config = parent.select_checker(clone, python, timeout_seconds=15)
    assert config['runtime_identity'] == identity
    write(out / 'checker-config.json', config)
    rows.append({'case': 'public-isolated-identity-and-parent-selection', 'status': 'passed'})

    marker = out / 'unselected-helper-executed'
    package = clone / 'scripts/import_fixture'
    package.mkdir()
    (package / '__init__.py').write_text('from pathlib import Path\nPath(' + repr(str(marker)) + ').write_text("executed")\n')
    refused = run('helper-package', ['identity'], 2)
    assert refused['status'] == 'refused' and not marker.exists()
    rows.append({'case': 'checker-package-shadow', 'status': refused['status'], 'marker_executed': marker.exists()})
    for label, action in [('selected-parent-currentness', lambda: parent.current(config)),
                          ('parent-initial-selection', lambda: parent.select_checker(clone, python))]:
        with patch.object(parent.subprocess, 'Popen', side_effect=AssertionError('child invocation occurred')):
            try:
                action()
            except parent.GateError as error:
                assert error.status == 'refused' and 'namespace' in str(error)
                rows.append({'case': label, 'status': error.status, 'reason': str(error), 'child_started': False})
            else:
                raise AssertionError(label + ' admitted unselected package')
    shutil.copyfile(package / '__init__.py', out / 'rejected-package-source.txt')
    shutil.rmtree(package)

    model = json.loads((clone / 'fixtures/stdo-3.0.2/MODEL.json').read_text())
    model['signature'] = None
    model_path = out / 'signature-null.json'
    write(model_path, model)
    request = {'schema': 'a_c.formal-gate.request/1',
               'input': {'format': 'model', 'path': str(model_path), 'raw_sha256': sha(model_path)},
               'selections': [], 'supplied_views': None, 'context_binding': None}
    request_path = out / 'null-request.json'
    write(request_path, request)
    result = run('null-cli', ['verify', '--request', str(request_path), '--output', str(out / 'null-cli-evidence')], 2)
    assert result['status'] == 'refused'
    assert json.loads((out / 'null-cli-evidence/result.json').read_text()) == result
    assert result['evidence']['manifest_sha256'] == sha(out / 'null-cli-evidence/manifest.json')
    rows.append({'case': 'malformed-signature-public-cli', 'status': 'refused', 'normal_receipt_retained': True})

    sys.path.insert(0, str(clone / 'scripts'))
    import formal_gate as gate
    with patch.object(gate.support, 'check', side_effect=AssertionError('proof support reached')):
        result = gate.verify(request, out / 'null-api-evidence')
    assert result['status'] == 'refused'
    assert json.loads((out / 'null-api-evidence/result.json').read_text()) == result
    rows.append({'case': 'malformed-signature-api', 'status': 'refused', 'normal_receipt_retained': True})
    scope = ' '.join(result['limits'])
    assert 'supplied or carrier-recovered model JSON' in scope
    assert 'prose/corpus-to-model F_P fidelity remains opaque and unproved' in scope

    old_bundle = out / 'old-successful-bundle'
    shutil.copytree(WORK / 'runtime/qualification-002/new-model-only', old_bundle)
    old_result = json.loads((old_bundle / 'result.json').read_text())
    assert old_result['status'] == 'verified'
    stale = run('old-successful-bundle', ['check-evidence', '--bundle', str(old_bundle),
                                        '--output', str(out / 'stale-replay')], 2)
    assert stale['status'] == 'refused' and 'pins are stale' in stale['reason']
    assert not (out / 'stale-replay').exists()
    rows.append({'case': 'old-success-not-current-evidence', 'status': 'refused', 'reason': stale['reason'], 'proof_started': False})

    bridge_marker = out / 'unselected-bridge-executed'
    bridge_package = graph_dir / 'ac_formal_gate'
    bridge_package.mkdir()
    (bridge_package / '__init__.py').write_text('from pathlib import Path\nPath(' + repr(str(bridge_marker)) + ').write_text("executed")\nraise RuntimeError("unselected bridge")\n')
    probe = '''import hashlib,json
from pathlib import Path
import ac_generate as generation
import ac_support_core as core
import ac_support_effects as effects
source = Path.cwd() / 'ac_formal_gate.py'
expected = hashlib.sha256(source.read_bytes()).hexdigest()
assert effects.formal is core.ac_formal_gate
config = json.loads((Path.cwd().parent / 'checker-config.json').read_text())
for module in (generation.ac_formal_gate, core.ac_formal_gate):
    assert Path(module.__file__) == source
    assert module.__a_c_loaded_sha256__ == expected
    module.validate_config(config)
source.write_bytes(source.read_bytes() + b'\\n# review-only changed current bytes after load\\n')
config['adapter_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
for module in (generation.ac_formal_gate, core.ac_formal_gate):
    try: module.validate_config(config)
    except module.GateError as exc: assert exc.status == 'refused'
    else: raise AssertionError('loaded source identity substituted')
print(json.dumps({'exact_bridge_loaded':True,'loaded_source_drift_refused':True}))
'''
    (out / 'bridge_probe.txt').write_text(probe)
    before_bridge = (graph_dir / 'ac_formal_gate.py').read_bytes()
    completed = subprocess.run([str(python), '-S', '-B', '-c', probe], cwd=graph_dir,
                               env=env, capture_output=True, text=True, timeout=15)
    (out / 'bridge.stdout').write_text(completed.stdout)
    (out / 'bridge.stderr').write_text(completed.stderr)
    assert completed.returncode == 0, (completed.stdout, completed.stderr)
    assert not bridge_marker.exists()
    (graph_dir / 'ac_formal_gate.py').write_bytes(before_bridge)
    rows.append({'case': 'exact-generation-core-effects-bridge', 'status': 'passed',
                 'package_executed': False, 'loaded_source_drift_refused': True})
    assert all(sha(clone / name) == digest for name, digest in freeze['source_files'].items())
    result = {'schema': 'a_c.independent-repaired-startup-controls/1',
              'authorization': 'Executive released small own-copy startup/malformed/receipt refusal controls; no Lean or kernel execution',
              'lean_freeze_sha256': sha(freeze_path), 'graphify_freeze_sha256': sha(graph_path),
              'runtime_identity': identity['sha256'], 'cases': rows,
              'graphify_source_copies': copied_graph, 'toolchain_copied': False,
              'compiler_or_kernel_execution': False, 'all_44_lean_source_pins_unchanged': True}
    write(out / 'result.json', result)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
