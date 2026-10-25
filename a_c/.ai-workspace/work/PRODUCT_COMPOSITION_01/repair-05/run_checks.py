"""One frozen successor campaign; retain command exits and exact source custody."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
FREEZE = HERE.parent / 'source-freeze-05.json'
pins = json.loads(FREEZE.read_text())['files']


def verify_sources():
    for name, expected in pins.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name


commands = [
    ('predecessor', ['python3', '-B', str(HERE / 'replay_predecessor.py')]),
    ('targeted', ['python3', '-B', '-m', 'unittest', 'discover', '-s',
                 'a_c/build_tenants/graphify/test_env', '-p', 'test_ac_support_composition.py', '-v']),
    ('support-suite', ['python3', '-B', '-m', 'unittest', 'discover', '-s',
                      'a_c/build_tenants/graphify/test_env', '-p', 'test_ac_support*.py', '-v']),
    ('typing', ['a_c/.venv/bin/python', '-m', 'mypy', '--strict',
                *['a_c/build_tenants/graphify/code/' + file for file in
                  ('ac_support.py', 'ac_support_core.py', 'ac_support_effects.py', 'ac_support_composition.py')]]),
    ('whitespace', ['git', 'diff', '--check', '--', *pins]),
]
records = []
for name, argv in commands:
    verify_sources()
    env = dict(os.environ)
    if name == 'targeted':
        env['AC_SUPPORT_EFFECTS_PROOF_ROOT'] = str(HERE / 'public-custody')
    started = time.time_ns()
    path = HERE / (name + '.log')
    with path.open('xb') as output:
        run = subprocess.run(argv, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT, env=env, timeout=600)
    record = {'name': name, 'argv': argv, 'exit': run.returncode,
              'started_ns': started, 'ended_ns': time.time_ns(),
              'source_freeze': '../source-freeze-05.json',
              'source_freeze_sha256': hashlib.sha256(FREEZE.read_bytes()).hexdigest(),
              'log': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    records.append(record)
    (HERE / 'checks.json').write_text(json.dumps(records, indent=2) + '\n')
    print(name, run.returncode, flush=True)
    verify_sources()
    if run.returncode:
        raise SystemExit(run.returncode)

(HERE / 'FINAL_CHECKS.json').write_text(json.dumps({
    'schema': 'a_c.composition.final-checks/1',
    'source_freeze': '../source-freeze-05.json',
    'source_freeze_sha256': hashlib.sha256(FREEZE.read_bytes()).hexdigest(),
    'files_verified_before_and_after_every_check': pins,
    'all_commands_passed': True,
    'standing': 'bounded controlled-process evidence; independent review and acceptance separate'
}, indent=2) + '\n')
