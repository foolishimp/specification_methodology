"""Execute one selected phase of the admitted RC reset transaction, with receipts."""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
R = Path.cwd()
O = Path(__file__).resolve().parent
P = O / 'publication'
E = O / 'publication-execution'
GIT = ['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false']
sha = lambda b: hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes(); return {'path': p.relative_to(R).as_posix(), 'sha256': sha(b), 'bytes': len(b)}
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(value, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
def git(*args): return subprocess.check_output([*GIT, *args], cwd=R).decode().strip()
def run(name, argv, *, stdin=None, expected=0, extra_env=None):
    directory = E / name; directory.mkdir(parents=True, exist_ok=False)
    if stdin is not None: (directory / 'stdin.txt').write_bytes(stdin)
    save(directory / 'invocation.json', {'argv': argv, 'cwd': str(R), 'stdin': ref(directory / 'stdin.txt') if stdin is not None else None,
        'extra_environment': extra_env or {}, 'started_ns': time.time_ns()})
    stdout, stderr = directory / 'stdout.txt', directory / 'stderr.txt'
    start = time.time_ns(); print('START', name, flush=True)
    with stdout.open('xb') as out, stderr.open('xb') as err:
        process = subprocess.run(argv, cwd=R, env=dict(os.environ, **(extra_env or {})), input=stdin, stdout=out, stderr=err)
    receipt = save(directory / 'execution.json', {'argv': argv, 'cwd': str(R), 'returncode': process.returncode,
        'elapsed_seconds': (time.time_ns() - start) / 1e9, 'stdout': ref(stdout), 'stderr': ref(stderr),
        'stdin': ref(directory / 'stdin.txt') if stdin is not None else None})
    print('DONE', name, process.returncode, receipt['sha256'], flush=True)
    assert process.returncode == expected, (name, process.returncode, stderr.read_text()[-4000:])
    return stdout.read_bytes()
forms = load(P / 'OPERATION_TEMPLATES.json')
assert ref(P / 'OPERATION_TEMPLATES.json')['sha256'] == '4b75d9fa1ce3dcd5f8026764f9b6fcd3f0cec7d7fbe66720f8d9485adcd5551a'
carrier = load(O / 'manifest-reconciliation-001/RESULT.json')['commit']
assert git('rev-parse', 'HEAD') == carrier
manifest_raw = subprocess.check_output([*GIT, 'show', carrier + ':stack_release.json'], cwd=R)
manifest = json.loads(manifest_raw)
assert manifest['cohort']['status'] == 'candidate' and manifest['cohort']['cut'] == 'v3.0.5-rc.1'
handoff = load(R / forms['native_handoff']['path'])
assert git('rev-parse', handoff['native_tag']) == handoff['native_tag_object']
assert os.statvfs(R).f_bavail * os.statvfs(R).f_frsize >= 2 * 1024**3
commands = {c['id']: c for c in forms['commands']}
def remote(name):
    raw = run(name, [*GIT, 'ls-remote', '--heads', '--tags', manifest['publication']['repository_url']])
    return {line.split('\t')[1]: line.split('\t')[0] for line in raw.decode().splitlines()}
def preimages(observed):
    assert all(observed.get(k) == v for k, v in forms['expected_remote'].items()), 'Remote reset preimage drift'
    assert all(observed.get(k) == v for k, v in forms['preserved_immutable_refs'].items()), 'Historical ref drift'
phase = sys.argv[1]
if phase == 'tags':
    preimages(remote('001-remote-before-local-refs'))
    for row in forms['selector_annotations'].values(): assert git('rev-parse', row['ref']) == row['expected_old_object']
    for name in [r['ref'] for r in forms['cut_annotations'].values()] + list(forms['archive_refs']):
        assert subprocess.run([*GIT, 'show-ref', '--verify', '--quiet', name], cwd=R).returncode == 1, name
    tagger = git('var', 'GIT_COMMITTER_IDENT')
    created = {}
    for category in ('cut_annotations', 'selector_annotations'):
        for product, row in forms[category].items():
            target = carrier if row['target'] == 'FINAL_CARRIER_COMMIT' else row['target']
            tag = row['ref'].removeprefix('refs/tags/')
            body = '\n'.join([f'object {target}', 'type commit', f'tag {tag}', f'tagger {tagger}', '', *row['annotation_lines'], ''])
            oid = run('tag-' + category + '-' + product, commands['annotated-tag-objects']['argv'], stdin=body.encode()).decode().strip()
            assert len(oid) == 40 and git('cat-file', '-t', oid) == 'tag'
            created[row['ref']] = oid
    lines = ['start']
    for row in forms['cut_annotations'].values(): lines.append('create ' + row['ref'] + ' ' + created[row['ref']])
    for name, oid in forms['archive_refs'].items(): lines.append('create ' + name + ' ' + oid)
    for row in forms['selector_annotations'].values(): lines.append('update ' + row['ref'] + ' ' + created[row['ref']] + ' ' + row['expected_old_object'])
    lines += ['prepare', 'commit', '']
    run('002-local-atomic-refs', commands['local-atomic-reset-refs']['argv'], stdin='\n'.join(lines).encode())
    selected = {**created, **forms['archive_refs'], handoff['native_tag']: handoff['native_tag_object'], 'refs/heads/main': carrier}
    assert len(selected) == 16 and all(git('rev-parse', name) == oid for name, oid in selected.items())
    save(E / 'LOCAL_REFS.json', {'status': 'established', 'carrier': carrier, 'selected': selected, 'preserved_native': handoff['native_tag_object']})
elif phase in ('refs', 'published'):
    argv = [carrier if a == 'FINAL_CARRIER_COMMIT' else a for a in commands[phase]['argv']]
    raw = run('014-refs-successor' if phase == 'refs' else '010-published', argv)
    result = json.loads(raw); assert result['status'] == 'valid' and result['phase'] == phase and not result['failures']
    save(E / (phase.upper() + '_PASSED.json'), {'status': 'passed', 'phase': phase, 'carrier': carrier,
        'result': ref(E / ('014-refs-successor' if phase == 'refs' else '010-published') / 'stdout.txt'),
        'coverage': 'ready/content predicates executed within refs(D)' if phase == 'refs' else 'Prescribed published(D) predicates; public qualification remains separate.'})
elif phase == 'push':
    assert load(E / 'REFS_PASSED.json')['carrier'] == carrier
    result = load(E / '014-refs-successor/stdout.txt')
    argv = result['push_argv']
    assert argv[:3] == ['git', 'push', '--atomic']
    selected = load(E / 'LOCAL_REFS.json')['selected']
    assert set(argv[-16:]) == {oid + ':' + name for name, oid in selected.items()}
    assert set(a for a in argv if a.startswith('--force-with-lease=')) == {'--force-with-lease=' + name + ':' + (old or '') for name, old in forms['expected_remote'].items()}
    preimages(remote('004-remote-before-push'))
    run('005-atomic-push', argv, extra_env=commands['atomic-push']['environment'])
    observed = remote('006-remote-after-push')
    assert all(observed.get(name) == oid for name, oid in selected.items())
    assert all(observed.get(name) == oid for name, oid in forms['preserved_immutable_refs'].items())
    save(E / 'PUSH_PASSED.json', {'status': 'pushed', 'carrier': carrier, 'selected': selected, 'qualified_push_sha256': result['qualified_push_sha256']})
elif phase == 'release':
    assert load(E / 'PUSH_PASSED.json')['carrier'] == carrier
    original = load(R / load(O.parent / 'PREIMAGES.json')['release']['path'])
    before = json.loads(run('007-old-release-before', ['gh', 'api', 'repos/foolishimp/specification_methodology/releases/437012396']))
    def asset_ids(value): return sorted((a['id'], a['name'], a['size'], a['digest']) for a in value['assets'])
    assert before['id'] == original['id'] == 437012396 and before['tag_name'] == original['tag_name'] and asset_ids(before) == asset_ids(original)
    assert before['draft'] is False and before['prerelease'] is False
    run('008-archive-old-release', commands['archive-previous-release']['argv'])
    after = json.loads(run('009-old-release-after', ['gh', 'api', 'repos/foolishimp/specification_methodology/releases/437012396']))
    patch = load(P / 'archive-previous-release.json')
    assert after['id'] == before['id'] and after['tag_name'] == patch['tag_name'] and asset_ids(after) == asset_ids(before)
    absent = run('011-new-release-absence', commands['new-release-absence']['argv'], expected=1)
    assert json.loads(absent).get('status') == '404', absent
    assets = P / 'assets'; assets.mkdir(exist_ok=False)
    asset = assets / forms['external_manifest_asset']['name']; asset.write_bytes(manifest_raw)
    for row in forms['assets']:
        assert ref(R / row['path']) == {k: row[k] for k in ('path', 'sha256', 'bytes')}
    run('012-create-normal-release', commands['release-create']['argv'])
    actual = json.loads(run('013-new-release-readback', commands['new-release-absence']['argv']))
    expected = {r['name']: ('sha256:' + r['sha256'], r['bytes']) for r in forms['assets']}
    expected[asset.name] = ('sha256:' + sha(manifest_raw), len(manifest_raw))
    assert actual['tag_name'] == 'specification_methodology/v3.0.5-rc.1' and actual['draft'] is False and actual['prerelease'] is False
    assert len(actual['assets']) == 5 and {a['name']: (a['digest'], a['size']) for a in actual['assets']} == expected
    save(E / 'RELEASE_PUBLISHED.json', {'status': 'normal_release_published_latest_pending', 'carrier': carrier, 'release_id': actual['id'],
        'release': ref(E / '013-new-release-readback/stdout.txt'), 'external_manifest': ref(asset), 'assets': expected,
        'next': 'Fresh anonymous published recipe acquisition/install and public qualification; prescribed published gate may overlap under the selected resource bound.'})
else: raise ValueError('Unknown selected phase: ' + phase)
