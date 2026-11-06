"""Record selected installed commands and preserve exact portable observations."""
from pathlib import Path
import hashlib
import json
import os
import resource
import shutil
import subprocess
import time

REPO = Path('/Users/jim/src/apps/specification_methodology')
WORKSPACE = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-003')
PORTABLE = Path(__file__).absolute().parent

def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()

def ref(path, *, canonical=None, archived=False):
    path = Path(path).absolute()
    assert path.is_file() and not path.is_symlink(), str(path)
    if canonical is not None:
        retained = REPO / canonical
        assert sha(retained) == sha(path), (path, retained)
    elif path.is_relative_to(REPO):
        retained = path
    else:
        retained = PORTABLE / 'observed' / path.relative_to(WORKSPACE)
        if not archived or path.name in ('manifest.json', 'result.json'):
            retained.parent.mkdir(parents=True, exist_ok=True)
            if retained.exists():
                assert sha(retained) == sha(path), ('changed retained observation', retained)
            else:
                shutil.copyfile(path, retained)
                assert not os.path.samefile(path, retained)
    return {'path': retained.relative_to(REPO).as_posix(), 'sha256': sha(path), 'bytes': path.stat().st_size}

def run(name, argv, producer, *, inputs=(), output_files=(), output_tree=None,
        archived_tree=False, stdin=None, decode='json', cwd=WORKSPACE, env_add=None):
    """No automatic retry. Caller supplies actual paths and the prescribed argv."""
    argv = [str(x) for x in argv]
    directory = PORTABLE / 'executions' / name
    directory.mkdir(parents=True, exist_ok=False)
    actual_producer = Path(argv[next(i for i, x in enumerate(argv) if x.endswith('.py'))])
    producer_ref = ref(actual_producer, canonical=producer)
    selected_inputs = []
    observed_inputs = []
    for item in inputs:
        path, canonical = item if isinstance(item, tuple) else (item, None)
        selected = ref(path, canonical=canonical)
        selected_inputs.append(selected)
        observed_inputs.append({'actual_path': str(Path(path).absolute()), 'retained': selected})
    invocation = Path(argv[0]).absolute()
    physical = invocation.resolve(strict=True)
    py_version = subprocess.check_output([str(invocation), '-I', '-S', '-c', 'import platform; print(platform.python_version())'], text=True).strip()
    python = {'invocation': str(invocation), 'executable_realpath': str(physical), 'sha256': sha(physical), 'version': py_version}
    selected_stdin = ref(stdin) if stdin is not None else None
    before = {'schema': 'stdo.execution-invocation/1', 'argv': argv, 'cwd': str(cwd),
              'producer': producer_ref, 'python': python, 'inputs': observed_inputs,
              'stdin': selected_stdin, 'environment_additions': env_add or {},
              'recovery': 'Retain failed/partial outputs and reconcile before any further invocation.'}
    (directory / 'invocation.json').write_bytes(encoded(before))
    stdout = directory / 'stdout.txt'; stderr = directory / 'stderr.txt'
    started = time.time_ns(); usage_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    print(json.dumps({'phase': name, 'status': 'started', 'argv': argv}), flush=True)
    with stdout.open('wb') as out, stderr.open('wb') as err:
        process = subprocess.run(argv, cwd=cwd, stdout=out, stderr=err,
                                 input=Path(stdin).read_bytes() if stdin is not None else None,
                                 env=os.environ | (env_add or {}))
    ended = time.time_ns(); usage_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    outputs = [ref(stdout), ref(stderr)]
    for path in output_files:
        if Path(path).is_file(): outputs.append(ref(path))
    if output_tree is not None and Path(output_tree).is_dir():
        for path in sorted(Path(output_tree).rglob('*')):
            if path.is_file() and path.name != 'local-origin.json':
                outputs.append(ref(path, archived=archived_tree))
    result = None
    if decode is not None:
        raw = stdout.read_bytes()
        try:
            if decode == 'json': result = json.loads(raw)
            elif decode == 'jsonl': result = [json.loads(line) for line in raw.splitlines()]
            elif decode == 'last-json': result = json.loads(raw[raw.rfind(b'\n{') + 1:])
            else: raise ValueError('Unknown decode mode')
        except (ValueError, UnicodeError):
            result = None
    result_path = directory / 'result.json'
    if result is not None:
        result_path.write_bytes(encoded(result)); outputs.append(ref(result_path))
    record = {'schema': 'stdo.execution-observation/1', 'producer': producer_ref,
              'result': ref(result_path) if result is not None else ref(stdout),
              'observed_input_paths': observed_inputs,
              'execution': {'argv': argv, 'cwd': str(cwd), 'returncode': process.returncode,
                'started_ns': started, 'ended_ns': ended, 'elapsed_seconds': (ended-started)/1e9,
                'user_seconds': usage_after.ru_utime-usage_before.ru_utime,
                'system_seconds': usage_after.ru_stime-usage_before.ru_stime,
                'child_maxrss_native_units': usage_after.ru_maxrss,
                'environment': {'python': python, 'additions': env_add or {}},
                'inputs': selected_inputs, 'outputs': outputs, 'stdout': ref(stdout), 'stderr': ref(stderr)}}
    if stdin is not None: record['execution']['stdin'] = selected_stdin
    (directory / 'execution.json').write_bytes(encoded(record))
    assert ref(actual_producer, canonical=producer) == producer_ref
    print(json.dumps({'phase': name, 'returncode': process.returncode,
                      'seconds': record['execution']['elapsed_seconds'], 'record': str(directory/'execution.json')}), flush=True)
    return record, result
