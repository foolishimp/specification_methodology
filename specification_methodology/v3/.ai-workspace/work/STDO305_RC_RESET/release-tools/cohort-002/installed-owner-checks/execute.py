import hashlib, json, os, subprocess, time
from pathlib import Path
R = Path.cwd()
O = Path(__file__).resolve().parent
sha = lambda b: hashlib.sha256(b).hexdigest()
def ref(p):
    b = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'bytes': len(b), 'sha256': sha(b)}
def save(p, x):
    with p.open('x') as out:
        json.dump(x, out, indent=2, sort_keys=True)
        out.write('\n')
    return ref(p)
plan = json.loads((O / 'PLAN.json').read_bytes())
receipts = []
for command in plan['commands']:
    outdir = Path(command['output_directory'])
    assert not outdir.exists()
    assert ref(R / command['producer']['path']) == command['producer']
    python = command['python']
    assert Path(python['invocation']).resolve() == Path(python['executable_realpath'])
    assert sha(Path(python['executable_realpath']).read_bytes()) == python['sha256']
    outdir.mkdir()
    env = dict(os.environ, **command['environment']['set'])
    for name in command['environment']['unset']:
        env.pop(name, None)
    start = time.time_ns()
    print('START', command['id'], flush=True)
    with (outdir / 'stdout.txt').open('xb') as stdout, (outdir / 'stderr.txt').open('xb') as stderr:
        run = subprocess.run(command['argv'], cwd=R, env=env, stdout=stdout, stderr=stderr, timeout=300)
    end = time.time_ns()
    raw = (outdir / 'stdout.txt').read_bytes()
    if run.returncode == 0:
        (outdir / 'result.json').write_bytes(raw)
    outputs = [ref(p) for p in sorted(outdir.iterdir())]
    record = {'schema': 'stdo.execution-observation/1', 'selected_plan': ref(O / 'PLAN.json'), 'producer': command['producer'],
        'execution': {'argv': command['argv'], 'cwd': str(R), 'returncode': run.returncode, 'started_ns': start, 'ended_ns': end,
            'elapsed_seconds': (end-start)/1e9, 'environment': {'python': python, 'additions': command['environment']['set'], 'unset': command['environment']['unset']},
            'inputs': [], 'outputs': outputs, 'stdout': ref(outdir / 'stdout.txt'), 'stderr': ref(outdir / 'stderr.txt')}}
    if run.returncode == 0:
        record['result'] = ref(outdir / 'result.json')
    receipts.append(save(outdir / 'execution.json', record))
    assert run.returncode == 0, (command['id'], (outdir / 'stderr.txt').read_text())
    result = json.loads(raw)
    assert all(result[key] == value for key, value in command['expected'].items() if key != 'returncode')
    print('DONE', command['id'], record['execution']['elapsed_seconds'], flush=True)
print('COMPLETE', save(O / 'COMPLETION.json', {'status': 'passed', 'plan': ref(O / 'PLAN.json'), 'receipts': receipts})['sha256'], flush=True)
