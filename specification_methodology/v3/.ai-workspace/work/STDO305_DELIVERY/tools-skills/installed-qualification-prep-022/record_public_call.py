"""Record one real call using a prepared installed policy; no shell or test shim."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import time


def pin(path):
    path = Path(path).absolute()
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path, required=True)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timeout-seconds', type=int, default=60)
    args = parser.parse_args()
    selected = json.loads(args.case.read_text())
    for item in (selected['configuration'], selected['policy'], selected['provider']):
        if pin(item['path']) != item:
            raise ValueError('Prepared source changed: ' + item['path'])
    config = json.loads(Path(selected['configuration']['path']).read_text())
    request = json.loads(args.request.read_text())
    if request.get('schema') != 'a_c.fd-support.request/1':
        raise ValueError('Expected an actual public support request')
    output = args.output.absolute()
    output.mkdir(parents=True, exist_ok=False)
    argv = [config['python'], '-B', selected['provider']['path'], '--policy', selected['policy']['path'],
            '--policy-sha256', selected['policy']['sha256'], '--principal', 'executive',
            'call', '--request', str(args.request.absolute())]
    started = time.time_ns()
    timed_out = False
    try:
        run = subprocess.run(argv, cwd=selected['cwd'], capture_output=True, timeout=args.timeout_seconds,
                             env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
        stdout, stderr, returncode = run.stdout, run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        stdout, stderr, returncode = error.stdout or b'', error.stderr or b'', None
        timed_out = True
    (output / 'stdout.json').write_bytes(stdout)
    (output / 'stderr.log').write_bytes(stderr)
    receipt = {'schema': 'stdo305.public-installed-operation/1', 'argv': argv, 'cwd': selected['cwd'],
               'request': pin(args.request), 'configuration': selected['configuration'], 'policy': selected['policy'],
               'producer': selected['provider'], 'returncode': returncode, 'timed_out': timed_out,
               'timeout_seconds': args.timeout_seconds,
               'recovery': 'On timeout retain output and reconcile descendant/effect state before any retry.',
               'started_ns': started, 'ended_ns': time.time_ns(),
               'stdout': pin(output / 'stdout.json'), 'stderr': pin(output / 'stderr.log')}
    (output / 'execution.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(stdout.decode(errors='replace'), end='')
    raise SystemExit(124 if timed_out else returncode)


if __name__ == '__main__': main()
