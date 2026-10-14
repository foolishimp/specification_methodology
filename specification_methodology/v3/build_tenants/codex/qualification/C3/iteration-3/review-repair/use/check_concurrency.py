"""Exercise real competing reader processes against a shared byte envelope."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
READER = HERE / 'trials.py'
WORKER = '''
import importlib.util, pathlib, sys, time
spec = importlib.util.spec_from_file_location('reader', sys.argv[1])
reader = importlib.util.module_from_spec(spec); spec.loader.exec_module(reader)
root = pathlib.Path(sys.argv[2])
original = pathlib.Path.read_bytes
def slow_read(path):
    if path.name == 'material.txt':
        time.sleep(0.3)
    return original(path)
pathlib.Path.read_bytes = slow_read
(root / ('ready-' + sys.argv[4])).touch()
while not (root / 'start').exists(): time.sleep(0.005)
try:
    getattr(reader, sys.argv[3])(root, 'frame', None, None, None)
except ValueError as error:
    print(str(error), file=sys.stderr)
    raise SystemExit(7)
'''


def run_case(folder, operation):
    root = folder / operation
    root.mkdir()
    data = b'x' * 512
    (root / 'material.txt').write_bytes(data)
    manifest = {'routes': {'frame': {'file': 'material.txt', 'bytes': len(data),
                'sha256': hashlib.sha256(data).hexdigest()}},
                'started_monotonic': None, 'started_utc': None,
                'maximum_acquired_bytes': 768, 'wall_seconds': 600}
    (root / 'manifest.json').write_text(json.dumps(manifest))
    workers = [subprocess.Popen([sys.executable, '-B', '-c', WORKER,
               str(READER), str(root), operation, str(n)],
               stdout=subprocess.PIPE, stderr=subprocess.PIPE) for n in range(2)]
    deadline = time.monotonic() + 10
    try:
        while len(list(root.glob('ready-*'))) != 2:
            if time.monotonic() > deadline:
                raise RuntimeError('Reader controls failed to reach the start barrier')
            time.sleep(0.005)
        (root / 'start').touch()
        outputs = [p.communicate(timeout=10) for p in workers]
    finally:
        for worker in workers:
            if worker.poll() is None:
                worker.kill()
                worker.communicate()
    rows = [json.loads(line) for line in (root / 'acquisition.jsonl').read_text().splitlines()]
    total = 0
    consistent = True
    for row in rows:
        total += row['emitted_bytes']
        consistent = consistent and row['cumulative_bytes'] == total
    return {'operation': operation, 'exit_codes': sorted(p.returncode for p in workers),
            'emitted_stdout_bytes': sum(len(output[0]) for output in outputs),
            'event_sum_bytes': total, 'maximum_bytes': 768,
            'cumulative_rows_consistent': consistent,
            'refusals': [output[1].decode().strip() for output in outputs if output[1]]}


with tempfile.TemporaryDirectory(prefix='stdo-i3-reader-concurrency-') as folder:
    # Calling the internal transaction without its lock reproduces the old
    # interleaving. The public entry must refuse the second competing read.
    old = run_case(Path(folder), 'acquire_locked')
    fixed = run_case(Path(folder), 'acquire')
checks = {
    'unlocked_counterexample_exceeds_shared_envelope': old['exit_codes'] == [0, 0]
        and old['event_sum_bytes'] == 1024 and not old['cumulative_rows_consistent'],
    'locked_entry_admits_only_one_competing_read': fixed['exit_codes'] == [0, 7]
        and fixed['event_sum_bytes'] == fixed['emitted_stdout_bytes'] == 512,
    'locked_entry_retains_exact_cumulative_count': fixed['cumulative_rows_consistent'],
    'refusal_names_shared_allowance': fixed['refusals'] == ['Admitted acquisition allowance exceeded; return current result'],
}
report = {'valid': all(checks.values()), 'checks': checks, 'unlocked_control': old,
          'fixed_control': fixed, 'reader_sha256': hashlib.sha256(READER.read_bytes()).hexdigest(),
          'scope': 'POSIX local reader processes; not host/model context or prior-attempt requalification.'}
(HERE / 'CONCURRENCY_CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
if not report['valid']:
    raise SystemExit(1)
