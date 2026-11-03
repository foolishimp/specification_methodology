"""Once-only compatibility replay; never rewrites the preceding sealed record."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
REPO = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
OUTPUT = HERE / 'final_checks/RETAINED_REPLAY.json'
assert not OUTPUT.exists(), 'preserve the once-only result'
source = BASE / 'testing/final_replay/ACTUAL_INPUT_REPLAY.json'
original = source.read_bytes()
assert hashlib.sha256(original).hexdigest() == '21f32bd686062d27fc8499895a079cb35fe3a833f42098830bf55a9f63497386'
retained = json.loads(original)
assert len(retained) == 33
reader_source = REPO / 'specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py'
raw = reader_source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'df7730a1f661a8be7a3144feff474f83197987ebfd1cce4063aa9c5504e75c41'
scratch = Path(tempfile.mkdtemp(prefix='stdo304-unicode-retained-', dir='/private/tmp'))
reader = scratch / 'read_basis.py'; reader.write_bytes(raw)
rows = []
for index, previous in enumerate(retained):
    argv = list(previous['original_argv'])
    assert argv[1] == '-B' and argv[2].endswith('/plugins/spec/scripts/read_basis.py')
    assert argv[3] in ('read', 'check') and '--store' in argv
    for flag in ('--definition', '--store'):
        assert Path(argv[argv.index(flag) + 1]).exists(), 'retained route unavailable: ' + flag
    assert Path(argv[argv.index('--stdo') + 1]).is_file()
    argv[2] = str(reader)
    run = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    try: value = json.loads(run.stdout)
    except ValueError: value = None
    same = value == previous['result']
    rows.append({'retained_index': index, 'origin': previous['origin'],
                 'evidence_kind': 'mechanical EF03 reproduction' if previous['origin'] == 'successor3/EF03_REPRO' else 'actual native helper call',
                 'original_argv': previous['original_argv'], 'replay_argv': argv,
                 'exit': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr,
                 'exact_result_object_equal': same,
                 'result_sha256': hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()})
OUTPUT.write_text(json.dumps({'predecessor_record_sha256': hashlib.sha256(original).hexdigest(),
    'reader_sha256': hashlib.sha256(raw).hexdigest(), 'copied_reader': str(reader),
    'actual_native_input_count': 32, 'mechanical_reproduction_count': 1,
    'new_native_model_sessions': 0, 'rows': rows}, indent=2) + '\n')
assert all(r['exit'] == 0 and r['exact_result_object_equal'] and not r['stderr'] for r in rows)
assert hashlib.sha256(source.read_bytes()).hexdigest() == hashlib.sha256(original).hexdigest()
print(json.dumps({'replayed': len(rows), 'identical': sum(r['exact_result_object_equal'] for r in rows),
                  'native_inputs': 32, 'mechanical_reproduction': 1, 'new_model_sessions': 0}))
