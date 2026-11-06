"""Public initializer witness with real manager and byte-identical copied A1."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

REPO = Path('/Users/jim/src/apps/specification_methodology')
WORK = Path(__file__).absolute().parent
ORIGINAL = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-001')
SCRATCH = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/empty-member-repair-014')
NATIVE = ORIGINAL / 'store/releases/v3.0.5'
PYTHON = ORIGINAL / 'dependencies/graphify/venv/bin/python'

def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def inventory(root):
    return {p.relative_to(root).as_posix(): {'bytes': p.stat().st_size, 'sha256': sha(p)}
            for p in sorted(root.rglob('*')) if p.is_file()}

phase = sys.argv[1]
assert phase in ('before', 'before-registered', 'after')
original = inventory(NATIVE)
method = SCRATCH / 'store/releases/v3.0.5'
product = SCRATCH / 'product'
manager = SCRATCH / 'stdo'
if phase == 'before':
    assert not SCRATCH.exists()
    shutil.copytree(NATIVE, method)
    assert inventory(method) == original
    product.mkdir()
    for old, new in (('stdo_runtime.json', 'Product.json'), ('README.md', 'README.md')):
        shutil.copyfile(ORIGINAL / 'anchors/codex' / old, product / new)
    manager.write_text('#!' + str(PYTHON) + '\nimport subprocess,sys\n'
        + 'raise SystemExit(subprocess.run([' + repr(str(ORIGINAL / 'manager/bin/stdo'))
        + ',"--store",' + repr(str(SCRATCH / 'store')) + ',*sys.argv[1:]]).returncode)\n')
    manager.chmod(0o755)
else:
    assert inventory(method) == original
if phase == 'before-registered':
    # The first copied-store attempt retained a missing-registry refusal. Copy
    # the exact existing relative-path registry; do not fabricate registration.
    shutil.copyfile(ORIGINAL / 'store/registry.json', SCRATCH / 'store/registry.json')
    assert sha(ORIGINAL / 'store/registry.json') == sha(SCRATCH / 'store/registry.json')
out = WORK / phase
out.mkdir(exist_ok=False)
destination = SCRATCH / phase
argv = [str(PYTHON), '-B', str(REPO / 'a_c/build_tenants/graphify/examples/fd-support/prepare_readonly.py'),
        '--out', str(destination), '--profile', 'stdo-3.0.5', '--product-root', str(product),
        '--definition-name', 'Product.json', '--method-installation', str(method), '--stdo', str(manager)]
(out / 'invocation.json').write_text(json.dumps({'argv': argv, 'cwd': str(SCRATCH)}, indent=2) + '\n')
start = time.time_ns()
result = subprocess.run(argv, cwd=SCRATCH, capture_output=True)
(out / 'stdout.txt').write_bytes(result.stdout)
(out / 'stderr.txt').write_bytes(result.stderr)
record = {'schema': 'stdo305.copied-native-initializer/1', 'phase': phase,
          'argv': argv, 'cwd': str(SCRATCH), 'returncode': result.returncode,
          'started_ns': start, 'ended_ns': time.time_ns(),
          'provider': {'path': str(REPO / 'a_c/build_tenants/graphify/code/ac_support_core.py'),
                       'sha256': sha(REPO / 'a_c/build_tenants/graphify/code/ac_support_core.py')},
          'manager': {'path': str(ORIGINAL / 'manager/bin/stdo'), 'sha256': sha(ORIGINAL / 'manager/bin/stdo')},
          'manager_store_launcher': {'path': str(manager), 'sha256': sha(manager)},
          'original_native': str(NATIVE), 'copied_native': str(method), 'before': original,
          'original_after': inventory(NATIVE), 'copied_after': inventory(method),
          'stdout_sha256': sha(out / 'stdout.txt'), 'stderr_sha256': sha(out / 'stderr.txt'),
          'limits': 'Candidate provider against copied complete A1 using actual manager. Not successor installation qualification or an in-place runtime repair.'}
assert original == record['original_after'] == record['copied_after']
(out / 'execution.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({'phase': phase, 'returncode': result.returncode, 'seconds': (record['ended_ns']-start)/1e9,
                  'stderr': result.stderr.decode(), 'native_files_unchanged': len(original)}))
