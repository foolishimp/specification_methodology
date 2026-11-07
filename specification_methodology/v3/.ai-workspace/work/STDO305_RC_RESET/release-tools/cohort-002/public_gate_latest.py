"""Prescribed final public gate and conditional same-ID normal Latest update."""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
R = Path.cwd(); C = Path(__file__).resolve().parent
O = C.parent.parent / 'public-qualification-001'
E = O / 'publication-closure'
E.mkdir(exist_ok=True)
PY = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes(); return {'path': str(p.relative_to(R)), 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}
def save(p, value):
    with p.open('x') as f: json.dump(value, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
assert os.path.samefile(sys.executable, PY)
assert hashlib.sha256(Path(PY).read_bytes()).hexdigest() == 'a708f6e9f4803b806b29146c4e0feecfd9bf2d9eb60f3e15b850cd7cb56f200b'
manifest = load(R / 'stack_release.json')
receipt = load(O / 'PUBLIC_READBACK.json')
carrier = receipt['carrier']; release_id = receipt['release_id']
assert load(C / 'publication-execution/PUBLISHED_PASSED.json')['carrier'] == carrier
def run(name, argv, stdin=None):
    p = E / name; p.mkdir(exist_ok=False)
    save(p / 'invocation.json', {'argv': argv, 'cwd': str(R)})
    if stdin is not None: (p / 'stdin.json').write_bytes(stdin)
    start = time.time_ns(); print('START', name, flush=True)
    with (p / 'stdout.txt').open('xb') as out, (p / 'stderr.txt').open('xb') as err:
        result = subprocess.run(argv, cwd=R, input=stdin, stdout=out, stderr=err)
    record = save(p / 'execution.json', {'argv': argv, 'returncode': result.returncode, 'elapsed_seconds': (time.time_ns()-start)/1e9,
        'stdout': ref(p / 'stdout.txt'), 'stderr': ref(p / 'stderr.txt'), 'stdin': ref(p / 'stdin.json') if stdin is not None else None})
    print('DONE', name, result.returncode, flush=True)
    assert result.returncode == 0, (name, (p / 'stderr.txt').read_text()[-3000:])
    return (p / 'stdout.txt').read_bytes(), record
if sys.argv[1] == 'public':
    argv = [PY, '-B', str(R / 'scripts/check_stack_release.py'), '--phase', 'public', '--revision', carrier,
        '--public-receipt', str((O / 'PUBLIC_READBACK.json').relative_to(R)), '--public-receipt-sha256', ref(O / 'PUBLIC_READBACK.json')['sha256']]
    raw, execution = run('public-gate', argv)
    result = json.loads(raw)
    assert result['status'] == 'valid' and result['phase'] == 'public' and result['failures'] == []
    print('PUBLIC_GATE_PASSED', save(O / 'PUBLIC_GATE_PASSED.json', {'status': 'passed', 'carrier': carrier, 'receipt': ref(O / 'PUBLIC_READBACK.json'), 'execution': execution, 'result': ref(E / 'public-gate/stdout.txt')})['sha256'], flush=True)
elif sys.argv[1] == 'latest':
    assert load(O / 'PUBLIC_GATE_PASSED.json')['carrier'] == carrier
    expected = {a['name']: ('sha256:' + a['sha256'], a['bytes']) for a in manifest['publication']['assets']}
    expected[manifest['publication']['external_manifest_asset']['name']] = ('sha256:' + ref(R / 'stack_release.json')['sha256'], (R / 'stack_release.json').stat().st_size)
    def acquire(name, url):
        request = urllib.request.Request(url, headers={'User-Agent': 'STDO-RC-release-readback', 'Accept': 'application/vnd.github+json'})
        with urllib.request.urlopen(request, timeout=45) as response:
            raw = response.read(1024*1024); status = response.status; final = response.url
        assert status == 200
        path = E / (name + '.json'); path.write_bytes(raw)
        save(E / (name + '-transport.json'), {'url': url, 'final_url': final, 'status': status, 'unauthenticated': True, 'tls_verification': True, 'body': ref(path)})
        value = json.loads(raw)
        assert value['id'] == release_id and value['tag_name'] == 'specification_methodology/v3.0.5-rc.1'
        assert value['draft'] is False and value['prerelease'] is False and len(value['assets']) == 5
        assert {a['name']: (a['digest'], a['size']) for a in value['assets']} == expected
        return ref(path)
    before = acquire('release-before-latest', f'https://api.github.com/repos/foolishimp/specification_methodology/releases/{release_id}')
    raw, remote_receipt = run('remote-before-latest', ['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', 'ls-remote', '--heads', '--tags', manifest['publication']['repository_url']])
    remote = {line.split('\t')[1]: line.split('\t')[0] for line in raw.decode().splitlines()}
    selected = load(C / 'manifest-reconciliation-002/RESULT.json')['selected']
    assert all(remote.get(name) == oid for name, oid in selected.items())
    patch = b'{"make_latest":"true"}\n'
    raw, mutation = run('same-release-latest', ['gh', 'api', '--method', 'PATCH', f'repos/foolishimp/specification_methodology/releases/{release_id}', '--input', '-'], patch)
    changed = json.loads(raw); assert changed['id'] == release_id and changed['draft'] is False and changed['prerelease'] is False
    after = acquire('anonymous-latest', 'https://api.github.com/repos/foolishimp/specification_methodology/releases/latest')
    print('LATEST_CONFIRMED', save(O / 'LATEST_CONFIRMED.json', {'status': 'confirmed_latest', 'carrier': carrier, 'release_id': release_id, 'before': before, 'mutation': mutation, 'anonymous_latest': after, 'assets_unchanged': expected, 'remote_readback': remote_receipt})['sha256'], flush=True)
else: raise ValueError('unknown phase')
