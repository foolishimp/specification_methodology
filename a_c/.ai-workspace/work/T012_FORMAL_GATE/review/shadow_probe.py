"""Independent marker-only reproduction against a copied frozen source subject."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

REPO = Path('/Users/jim/src/apps/specification_methodology')
REVIEW = REPO / 'a_c/.ai-workspace/work/T012_FORMAL_GATE/review'
SOURCE = REPO / 'a_c/build_tenants/lean'
FREEZE = REPO / 'a_c/.ai-workspace/work/T012_FORMAL_GATE/lean/SOURCE_FREEZE_001.json'
EXPECTED = '6791eaa26b72e1fe441af9c6b774ed4e3faebaec089845fbd082e01c5ab0adcf'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert sha(FREEZE) == EXPECTED
    frozen = json.loads(FREEZE.read_text())
    out = REVIEW / 'shadow-001'
    out.mkdir(exist_ok=False)
    clone = out / 'checker'
    for name, expected in frozen['source_files'].items():
        original = SOURCE / name
        assert sha(original) == expected, name
        target = clone / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        assert sha(target) == expected, name
    shutil.copyfile(FREEZE, out / 'SOURCE_FREEZE_001.json')
    env = {k: v for k, v in os.environ.items() if k not in ('PYTHONPATH', 'PYTHONHOME')}
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    command = [sys.executable, '-B', str(clone / 'scripts/formal_gate.py'), 'identity']

    def identity(label):
        completed = subprocess.run(command, cwd=out, env=env, capture_output=True,
                                   text=True, timeout=20)
        (out / (label + '.stdout')).write_text(completed.stdout)
        (out / (label + '.stderr')).write_text(completed.stderr)
        assert completed.returncode == 0, (completed.returncode, completed.stderr)
        return json.loads(completed.stdout)

    baseline = identity('before')
    assert baseline == frozen['runtime_identity']
    package = clone / 'scripts/import_fixture'
    package.mkdir()
    package_source = '''"""Review marker: delegate all real behavior to the unchanged flat helper."""
from pathlib import Path
import importlib.util
_marker = Path(__file__).resolve().parents[3] / 'package-executed.txt'
_marker.write_text(str(Path(__file__).resolve()) + '\\n')
_original = Path(__file__).resolve().parents[1] / 'import_fixture.py'
_spec = importlib.util.spec_from_file_location('_review_original_import_fixture', _original)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({name: value for name, value in vars(_module).items() if not name.startswith('__')})
'''
    (package / '__init__.py').write_text(package_source)
    after = identity('after')
    marker = out / 'package-executed.txt'
    unchanged = all(sha(clone / name) == expected
                    for name, expected in frozen['source_files'].items())
    result = {
        'schema': 'a_c.independent-shadow-probe/1',
        'frozen_manifest_sha256': EXPECTED,
        'copied_frozen_members': len(frozen['source_files']),
        'all_original_pins_unchanged': unchanged,
        'before_identity': baseline,
        'after_identity': after,
        'identity_equal': baseline == after,
        'marker_executed': marker.is_file(),
        'marker_content': marker.read_text() if marker.exists() else None,
        'marker_package_sha256': sha(package / '__init__.py'),
        'package_present_in_identity': 'scripts/import_fixture/__init__.py' in after['pins'],
        'command': command,
        'scope': 'Copied public standalone identity CLI only. No proof execution, forged proof, candidate mutation or Graphify execution.',
    }
    (out / 'result.json').write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    assert unchanged and baseline == after and marker.is_file()
    assert not result['package_present_in_identity']
    print(json.dumps({k: v for k, v in result.items() if k not in ('before_identity', 'after_identity')}, indent=2))


if __name__ == '__main__':
    main()
