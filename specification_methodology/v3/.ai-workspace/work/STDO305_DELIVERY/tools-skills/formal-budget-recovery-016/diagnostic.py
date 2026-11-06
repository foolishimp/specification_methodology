"""One operator-authorized compiler diagnostic; no full-model proof verdict."""
from pathlib import Path
import hashlib
import json
import resource
import shutil
import subprocess
import sys
import time

REPO = Path('/Users/jim/src/apps/specification_methodology')
PORTABLE = Path(__file__).absolute().parent
BASE = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/local-002')
LEAN = BASE / 'runtime/a_c/build_tenants/lean'
OUTPUT = BASE / 'diagnostics/gatedata-016'
INPUT = BASE / 'formal/current-full-002/GateData.lean'
EXPECTED = '5c98ff5174d5eb2c0f490d287456b14358091951f0929f811df9ed2c10071553'


def pin(path):
    path = Path(path).absolute()
    with path.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    return {'path': str(path), 'sha256': digest, 'bytes': path.stat().st_size}


def write(path, value):
    with path.open('xb') as stream:
        stream.write((json.dumps(value, indent=2, sort_keys=True) + '\n').encode())


def main():
    assert not OUTPUT.exists() and not any(x.is_symlink() for x in (OUTPUT, *OUTPUT.parents))
    assert pin(INPUT)['sha256'] == EXPECTED and INPUT.stat().st_size == 11470670
    sys.path.insert(0, str(LEAN / 'scripts'))
    import formal_support as support
    import runtime_process
    assert Path(support.__file__).absolute() == LEAN / 'scripts/formal_support.py'
    assert Path(runtime_process.__file__).absolute() == LEAN / 'scripts/runtime_process.py'
    identity = json.loads((REPO / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY/tools-skills/installed-qualification-015/formal/runtime-identity.json').read_bytes())
    assert pin(Path(support.__file__))['sha256'] == identity['pins']['scripts/formal_support.py']
    assert pin(Path(runtime_process.__file__))['sha256'] == identity['pins']['scripts/runtime_process.py']
    prefix, env, lock = support.proof_environment(OUTPUT)
    OUTPUT.mkdir(parents=True)
    shutil.copyfile(INPUT, OUTPUT / 'GateData.lean')
    assert pin(OUTPUT / 'GateData.lean')['sha256'] == EXPECTED
    argv = [str(prefix / 'bin/lean'), '-j', '1', '-M', '4096', '-R', str(OUTPUT),
            '-o', str(OUTPUT / 'GateData.olean'), str(OUTPUT / 'GateData.lean')]
    selected_env = {name: env[name] for name in ('PATH', 'LEAN_PATH', 'MATHLIB_CACHE_DIR', 'MATHLIB_NO_CACHE_ON_UPDATE')}
    invocation = {'schema': 'stdo305.compiler-diagnostic-invocation/1', 'argv': argv, 'cwd': str(LEAN),
        'timeout_seconds': 600, 'input': pin(INPUT), 'copied_input': pin(OUTPUT / 'GateData.lean'),
        'compiler': pin(prefix / 'bin/lean'), 'helpers': [pin(Path(support.__file__)), pin(Path(runtime_process.__file__))],
        'support_profile': pin(LEAN / 'profiles/proof-support-v1.json'), 'runtime_identity': identity['sha256'],
        'selected_environment': selected_env,
        'environment_rule': 'Exact formal_support.proof_environment(OUTPUT) result supplied unchanged; inherited authentication/unrelated environment values are neither inspected nor recorded. The helper excludes Lean/Lake/loader/Python overrides and supplies these selected paths.',
        'process_rule': 'Pinned runtime_process.run private process group and timeout cleanup; child stderr merged into retained stdout exactly as helper specifies.',
        'authority': 'Root authorized one isolated exact GateData compiler diagnostic at600s/-j1/-M4096; no full-model proof or release verdict.',
        'output': str(OUTPUT), 'standing': 'Recorded before the single diagnostic invocation.'}
    write(PORTABLE / 'INVOCATION.json', invocation)
    log = OUTPUT / 'compiler.stdout-stderr.log'
    started = time.time_ns(); before = resource.getrusage(resource.RUSAGE_CHILDREN)
    code = None; failure = None
    with log.open('xb') as stream:
        try:
            completed = runtime_process.run(argv, cwd=LEAN, env=env, stdout=stream, timeout=600)
            code = completed.returncode
        except (subprocess.TimeoutExpired, runtime_process.CleanupUnresolved, InterruptedError) as error:
            failure = {'type': type(error).__name__, 'message': str(error)}
    ended = time.time_ns(); after = resource.getrusage(resource.RUSAGE_CHILDREN)
    files = [pin(path) for path in sorted(OUTPUT.iterdir()) if path.is_file()]
    shutil.copyfile(log, PORTABLE / log.name)
    result = {'schema': 'stdo305.compiler-diagnostic-result/1', 'invocation': pin(PORTABLE / 'INVOCATION.json'),
        'returncode': code, 'failure': failure, 'started_ns': started, 'ended_ns': ended,
        'elapsed_seconds': (ended-started)/1e9, 'user_seconds': after.ru_utime-before.ru_utime,
        'system_seconds': after.ru_stime-before.ru_stime, 'child_maxrss_native_units': after.ru_maxrss,
        'outputs': files, 'exact_original_input_unchanged': pin(INPUT)['sha256'] == EXPECTED,
        'standing': 'One exact GateData compilation only. Successful exit does not establish whole model, selected views, theorem audit, kernel replay, installed qualification or release.'}
    write(PORTABLE / 'RESULT.json', result)
    print(json.dumps(result))
    raise SystemExit(0 if code == 0 and failure is None else 2)


if __name__ == '__main__':
    main()
