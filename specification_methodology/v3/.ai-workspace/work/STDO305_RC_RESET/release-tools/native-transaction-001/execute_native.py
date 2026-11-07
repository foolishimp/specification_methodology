"""Execute only the bound local RC native operations after the exact C2 checkpoint."""
import hashlib, json, os, re, stat, subprocess, time, zipfile
from pathlib import Path, PurePosixPath

R = Path.cwd()
O = Path(__file__).resolve().parent
W = O.parent
Q = W.parent
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def load(p):
    return json.loads(p.read_bytes())

def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix() if p.is_relative_to(R) else str(p), 'sha256': sha(raw), 'bytes': len(raw)}

def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as out:
        json.dump(value, out, indent=2, sort_keys=True)
        out.write('\n')
    return ref(p)

def git(*args):
    return subprocess.check_output(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '--no-optional-locks', *args], cwd=R)

def ordinary_ancestors(p):
    assert p.is_absolute() and '..' not in p.parts
    for parent in (p, *p.parents):
        assert not parent.is_symlink(), parent
        if parent.exists():
            assert parent.is_dir(), parent

ops = load(O / 'OPERATIONS.json')
assert ref(O / 'OPERATIONS.json')['sha256'] == '0270020d63f6d890c02871e9055df6e67fce9f9c21223beb139d4c8e24c708eb'
checkpoint = load(O / 'RESULT.json')
assert checkpoint['status'] == 'committed'
C = checkpoint['commit']
assert git('rev-parse', 'HEAD').decode().strip() == C
assert git('show', '-s', '--format=%P', C).decode().strip() == ops['source_checkpoint_preimage']
assert git('rev-parse', C + ':specification_methodology/v3/build_tenants/common').decode().strip() == ops['expected_package_tree']
assert not git('diff', '--cached', '--name-only')
assert os.statvfs(R).f_bavail * os.statvfs(R).f_frsize >= 2 * 1024**3
X, N = Path(ops['external_root']), Path(ops['native_run'])
ordinary_ancestors(X)
assert not X.exists() and not N.exists() and not (O / 'native-index').exists()
assert not (O / 'native-execution').exists()
E = O / 'native-execution'
E.mkdir()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PIP_DISABLE_PIP_VERSION_CHECK='1')
for name in ('PYTHONPATH', 'PYTHONHOME', 'STDO_STORE'):
    env.pop(name, None)
dynamic = {'${C}': C}
receipts = {}
native_tag = 'refs/tags/specification_methodology/v3.0.5-rc.1'
preimages = load(W / 'PREIMAGES.json')
initial_local = git('show-ref').decode()
assert native_tag not in dict(line.split(' ', 1)[::-1] for line in initial_local.splitlines())
(E / 'local-refs-before.txt').write_text(initial_local)
manager_build = load(W / 'manager-001/BUILD.json')
manager_facts = None
current = None

try:
    for command in ops['commands']:
        current = command['id']
        print('START', current, flush=True)
        started = time.time_ns()
        if current == 'manager-runtime-extract':
            archive = R / command['archive']['path']
            assert ref(archive) == command['archive']
            destination = Path(command['destination'])
            assert not destination.exists()
            with zipfile.ZipFile(archive) as zipped:
                names = zipped.namelist()
                assert len(names) == len(set(names)) == 25
                contents = {}
                for entry in zipped.infolist():
                    p = PurePosixPath(entry.filename)
                    assert str(p) == entry.filename and not p.is_absolute() and all(x not in ('', '.', '..') for x in p.parts)
                    assert not entry.is_dir() and stat.S_IFMT(entry.external_attr >> 16) in (0, stat.S_IFREG)
                    contents[entry.filename] = zipped.read(entry)
            wheels = json.loads(contents['WHEELS.json'])
            assert wheels['version'] == '3.0.5-rc.1' and wheels['python_distribution_version'] == '3.0.5rc1'
            assert len(wheels['members']) == 21
            for row in wheels['members']:
                assert sha(contents[row['path']]) == row['sha256'] and len(contents[row['path']]) == row['bytes']
            destination.mkdir(parents=True)
            for name, raw in contents.items():
                target = destination / name
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open('xb') as out:
                    out.write(raw)
                target.chmod(0o644)
            receipts[current] = save(E / (current + '.json'), {'kind': 'stdo.selected-runtime-extraction/1', 'status': 'extracted',
                'archive': command['archive'], 'destination': str(destination), 'files': [ref(destination / name) for name in sorted(contents)],
                'elapsed_seconds': (time.time_ns() - started) / 1e9})
        else:
            argv = [dynamic.get(value, value) for value in command['argv']]
            invocation = list(argv)
            if argv[0] == 'git':
                argv = ['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', *argv[1:]]
            selected_env = dict(env, **command.get('environment', {}))
            stdin = None
            if current == 'native-annotated-tag-object':
                message = (N / 'tag-message.txt').read_bytes()
                for text in ('Frozen-Source-Commit: ' + C, 'Frozen-Source-Tree: ' + ops['expected_package_tree'], 'Predecessor-Native-Commit: ' + ops['native_parent']):
                    assert text.encode() in message.splitlines()
                assert b'STDO-Release-Profile: stable-v1' not in message
                stdin = ('object ' + dynamic['${A}'] + '\ntype commit\ntag specification_methodology/v3.0.5-rc.1\ntagger ' + dynamic['${committer_ident}'] + '\n\n').encode() + message
                with Path(command['stdin_path']).open('xb') as out:
                    out.write(stdin)
            elif 'stdin_path' in command:
                stdin = Path(command['stdin_path']).read_bytes()
            if current == 'native-RC-tag-create-only':
                remote_raw = git('ls-remote', 'https://github.com/foolishimp/specification_methodology.git')
                (E / 'remote-before-native-tag.txt').write_bytes(remote_raw)
                remote = dict(line.split('\t')[::-1] for line in remote_raw.decode().splitlines())
                assert native_tag not in remote and native_tag + '^{}' not in remote
                assert remote['refs/heads/main'] == preimages['head']
                for row in preimages['tag_objects']:
                    assert remote[row['ref']] == row['object']
                    assert git('rev-parse', row['ref']).decode().strip() == row['object']
                assert subprocess.run(['git', '--no-optional-locks', 'show-ref', '--verify', '--quiet', native_tag], cwd=R).returncode == 1
            stdout = Path(command.get('stdout_path', str(E / (current + '.stdout'))))
            stderr = E / (current + '.stderr')
            stdout.parent.mkdir(parents=True, exist_ok=True)
            with stdout.open('xb') as out, stderr.open('xb') as err:
                process = subprocess.run(argv, input=stdin, cwd=R, env=selected_env, stdout=out, stderr=err)
            record = {'kind': 'stdo.native-transaction-execution/1', 'operation': current, 'argv': invocation, 'executed_argv': argv,
                'cwd': str(R), 'environment_selection': {name: selected_env[name] for name in ('PYTHONDONTWRITEBYTECODE', 'PIP_DISABLE_PIP_VERSION_CHECK', 'GIT_INDEX_FILE') if name in selected_env},
                'returncode': process.returncode, 'elapsed_seconds': (time.time_ns() - started) / 1e9,
                'stdout': ref(stdout), 'stderr': ref(stderr)}
            if stdin is not None:
                record['stdin'] = {'sha256': sha(stdin), 'bytes': len(stdin), 'path': command['stdin_path']}
            if invocation[0] != 'git':
                executable = Path(invocation[0])
                record['executable'] = {'invocation': str(executable), 'physical_path': str(executable.resolve()), 'sha256': sha(executable.read_bytes())}
            receipts[current] = save(E / (current + '.json'), record)
            assert process.returncode == 0, (current, process.returncode, stderr.read_text())
            output = stdout.read_text().strip()
            if current == 'external-manager-identities':
                identity = json.loads(output)
                assert identity['manager_version'] == '3.0.5rc1' and identity['python'].startswith('3.13.7 ')
                normalize = lambda name: re.sub(r'[-_.]+', '-', name).lower()
                actual = {normalize(row['name']): row['version'] for row in identity['dependencies']}
                expected = {normalize(row['name']): row['version'] for row in wheels['members']}
                assert actual == expected
            elif current == 'external-manager-source-match':
                matched = json.loads(output)
                assert matched['wheel_sha256'] == manager_build['wheel']['sha256'] and len(matched['members']) == 13
                physical = (X / 'manager/bin/python').resolve()
                assert sha(physical.read_bytes()) == 'a708f6e9f4803b806b29146c4e0feecfd9bf2d9eb60f3e15b850cd7cb56f200b'
                manager_facts = {'kind': 'stdo.external-manager-qualification/1', 'version': '3.0.5rc1', 'release_version': '3.0.5-rc.1',
                    'workspace': str(X), 'manager': ref(X / 'manager/bin/stdo'), 'source_member_count': 13,
                    'dependencies_exact': True, 'selected_distribution_population': actual,
                    'dependency_selection': ref(X / 'manager-runtime/WHEELS.json'), 'identities': ref(E / 'external-manager-identities.stdout'), 'source_match': ref(stdout),
                    'python': {'invocation': str(X / 'manager/bin/python'), 'executable_realpath': str(physical), 'sha256': sha(physical.read_bytes()), 'version': '3.13.7'}}
                save(E / 'MANAGER.json', manager_facts)
                print('MANAGER_VERIFIED 3.0.5rc1 21 distributions 13 source files', flush=True)
            elif current == 'native-prepare':
                source = load(N / 'source.json')
                assert source['source_candidate']['package_tree'] == ops['expected_package_tree'] and source['file_count'] == 173
                dynamic['${source_sha256}'] = ref(N / 'source.json')['sha256']
            elif current == 'native-tree':
                assert output == ops['expected_native_tree']
                dynamic['${native_tree}'] = output
            elif current == 'native-commit-A':
                assert re.fullmatch('[a-f0-9]{40}', output)
                assert git('show', '-s', '--format=%P', output).decode().strip() == ops['native_parent']
                dynamic['${A}'] = output
                print('NATIVE_COMMIT', output, flush=True)
            elif current == 'native-tagger-identity':
                assert '\n' not in output
                dynamic['${committer_ident}'] = output
            elif current == 'native-annotated-tag-object':
                assert output == hashlib.sha1(b'tag ' + str(len(stdin)).encode() + b'\0' + stdin).hexdigest()
                dynamic['${tag_object}'] = output
            elif current == 'native-attest':
                dynamic['${native_sha256}'] = ref(N / 'native.json')['sha256']
            elif current == 'native-seal':
                dynamic['${manifest_sha256}'] = ref(N / 'stdo-v3.0.5-rc.1-manifest.json')['sha256']
                dynamic['${selection_sha256}'] = ref(N / 'SOURCE_SELECTION.json')['sha256']
            elif current == 'initial-local-verify':
                verified = json.loads(output)
                assert verified['valid'] is True and verified['failures'] == [] and verified['cut'] == 'v3.0.5-rc.1'
                assert verified['manifest_sha256'] == dynamic['${manifest_sha256}']
        print('DONE', current, round((time.time_ns() - started) / 1e9, 3), flush=True)

    native = load(N / 'native.json')['native']
    native_root = X / 'store/releases/v3.0.5-rc.1'
    selection = load(N / 'SOURCE_SELECTION.json')
    assert load(N / 'installed-local.json')['files'] == 174
    handoff = {'kind': 'stdo.local-native-qualification-handoff/1', 'version': '3.0.5-rc.1', 'source_checkpoint': C,
        'source_package_tree': ops['expected_package_tree'], 'native_commit': dynamic['${A}'], 'native_root_tree': ops['expected_native_tree'],
        'native_tag': native_tag, 'native_tag_object': dynamic['${tag_object}'], 'native_manifest': ref(N / 'stdo-v3.0.5-rc.1-manifest.json'),
        'native_root': str(native_root), 'source_selection': ref(N / 'SOURCE_SELECTION.json'), 'store': str(X / 'store'), 'workspace': str(X),
        'manager': manager_facts, 'transport_mode': 'local_prepublication',
        'acquisition': {'mode': 'local_prepublication', 'repository': str(R), 'ref': native_tag, 'commit': dynamic['${A}'], 'manifest_sha256': dynamic['${manifest_sha256}']},
        'install': receipts['initial-local-install'], 'verify': receipts['initial-local-verify'], 'installed_byte_attestation': ref(N / 'installed-local.json'),
        'construction_proof': ref(Q / 'tools-skills/construction-proof-001/CURRENT_FORMAL.json'),
        'current_graphify': ref(Q / 'tools-skills/current-graphify-001/CURRENT_GRAPHIFY.json'),
        'routes': {name: str(native_root / path) for name, path in {'documentation': 'standards/documentation', 'proof_reader': 'standards/documentation/proofs',
            'proof_materializer': 'standards/documentation/proofs/materialize.py', 'tooling': 'standards/tooling', 'tooling_materializer': 'standards/tooling/materialize.py',
            'tooling_runtime': 'standards/tooling/runtime.py', 'tooling_setup': 'standards/tooling/setup.py', 'native_plugin': 'plugins/spec'}.items()},
        'limits': 'Exact fresh local manager/native install and 174-file attestation only. Fixed installed interfaces, actual installed proof, independent browser, final cohort/public qualification pending. Historical actor/Context trials retain original subjects and limits; no rerun or adoption claim.'}
    output_ref = save(O / 'HANDOFF.json', handoff)
    save(E / 'COMPLETE.json', {'status': 'passed', 'operations': ref(O / 'OPERATIONS.json'), 'receipts': receipts, 'handoff': output_ref})
    print('HANDOFF', output_ref['sha256'], dynamic['${A}'], dynamic['${manifest_sha256}'], flush=True)
except BaseException as exc:
    save(E / 'STOPPED.json', {'status': 'stopped', 'operation': current, 'exception_type': type(exc).__name__, 'detail': str(exc), 'completed_receipts': receipts, 'dynamic_bindings': dynamic})
    raise
