"""Measured actual public workflow for the bounded semantic-repair successor."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE
while not (ROOT/'stdo_representation').is_dir():
    ROOT = ROOT.parent
PINS = json.loads((HERE.parent/'provider-generation-final-pins.json').read_text())
CODE = ROOT/PINS['current_source_root']
for path, digest in PINS['files'].items():
    assert hashlib.sha256((CODE/path).read_bytes()).hexdigest() == digest, path
BASE = ROOT/'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
RUN = BASE/'run-coherent-005'
old_project = json.loads((BASE/'run-coherent-004/PROJECT.json').read_text())
assert hashlib.sha256((ROOT/'stdo_representation/stdo_representation.json').read_bytes()).hexdigest() == old_project['definition_sha256']
source = json.loads((BASE/'source-freeze.json').read_text())
assert source['source_identity_sha256'] == '0f4d2d5f77c5a635a553a8517787f1f52bf3e43a1dd150a940360e878ea4f1ba'
assert hashlib.sha256((BASE/'source-freeze.json').read_bytes()).hexdigest() == '640141354a53504999c1c21757689f7a3ecf6cbe77c3f30804f8493a2928dc99'
for row in source['members']+source['native_contracts']:
    for path in [BASE/'source'/row['path'], ROOT/source['source_root']/row['path']]:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256'], str(path)
operation = sys.argv[1]
argv = [sys.executable, '-B', str(CODE/'ac_project.py'), operation]
if operation == 'prepare':
    assert not RUN.exists()
    argv += ['--project', str(ROOT/'stdo_representation'), '--definition', 'stdo_representation.json',
             '--out', str(RUN), '--mode', 'direct', '--chunk-chars', '3000000',
             '--title', 'STDO 3.0.5 exact source model']
    for row in old_project['files']:
        argv += ['--source', row['path']]
else:
    argv += ['--run', str(RUN)]
    if operation in ['task', 'submit']:
        chunks = json.loads((RUN/'generation/chunks.json').read_text())
        assert len(chunks) == 1
        old_chunks = json.loads((BASE/'run-coherent-004/generation/chunks.json').read_text())
        assert chunks == old_chunks, 'Source segmentation changed; return before dependent submission'
        argv += ['--chunk', chunks[0]['id']]
    if operation == 'submit':
        argv += ['--answer', str(HERE/'answer-repaired.json'),
                 '--author', 'STDO Representation Writer: 42 ledger-selected uncertainty-field repairs after independent targeted review; host-session identity is caller-declared']
prefix = HERE/('public-'+operation)
assert not prefix.with_suffix('.receipt.json').exists(), 'Preserve prior attempts; select a successor receipt before retry'
start = time.monotonic()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
result = subprocess.run(argv, capture_output=True)
after = resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix('.stdout.json').write_bytes(result.stdout)
prefix.with_suffix('.stderr.txt').write_bytes(result.stderr)
receipt = {'kind':'stdo305.public-provider-invocation/1', 'argv':argv, 'returncode':result.returncode,
           'elapsed_seconds':time.monotonic()-start, 'user_cpu_seconds':after.ru_utime-before.ru_utime,
           'system_cpu_seconds':after.ru_stime-before.ru_stime, 'max_rss_bytes_macos':after.ru_maxrss,
           'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),
           'stderr_sha256':hashlib.sha256(result.stderr).hexdigest(),
           'machinery_pins':'../provider-generation-final-pins.json',
           'standing':'Actual public API execution; costs describe this subprocess, not LLM context efficiency or independent acceptance'}
prefix.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k != 'argv'},indent=2))
if result.returncode:
    print(result.stderr.decode())
    print(result.stdout.decode()[:4000])
sys.exit(result.returncode)
