#!/usr/bin/env python3
"""Install one STDO Skills 3.0.5 host binding beside one exact native owner."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys

VERSION = '3.0.5'
CORE = ('stdo-work', 'stdo-review', 'stdo-ticket', 'stdo-status', 'stdo-help')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()


def read(path):
    path = Path(path)
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError('Symlink path is unsupported: ' + str(parent))
    if not stat.S_ISREG(path.stat().st_mode):
        raise ValueError('Expected a regular file: ' + str(path))
    return path.read_bytes()


def tree(root):
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('Expected a real directory: ' + str(root))
    result = {}
    directories = set()
    for current, dirs, files in os.walk(root, followlinks=False):
        directories.update((Path(current) / name).relative_to(root).as_posix() for name in dirs)
        for name in dirs:
            if (Path(current) / name).is_symlink():
                raise ValueError('Symlink directory is unsupported')
        for name in files:
            path = Path(current) / name
            result[path.relative_to(root).as_posix()] = read(path)
    expected_dirs = {parent.as_posix() for name in result for parent in Path(name).parents if str(parent) != "."}
    if directories != expected_dirs:
        raise ValueError("Uninventoried empty directory in selected tree")
    return result


def validate_package(package):
    package = Path(package).absolute()
    raw = read(package / 'release/3.0.5/manifest.json')
    manifest = json.loads(raw)
    if manifest.get('version') != VERSION or manifest.get('kind') != 'stdo-skills.package/1':
        raise ValueError('Unsupported Skills package')
    declared = {row['path'] for row in manifest['files']}
    if len(declared) != len(manifest['files']):
        raise ValueError('Duplicate package member')
    for host in ('codex', 'claude'):
        prefix = 'build_tenants/' + host + '/current'
        actual = {prefix + '/' + name for name in tree(package / prefix)}
        if actual != {name for name in declared if name.startswith(prefix + '/')}:
            raise ValueError('Host package population differs from its inventory')
    for row in manifest['files']:
        path = row['path']
        if Path(path).is_absolute() or any(p in ('', '.', '..') for p in path.split('/')):
            raise ValueError('Unsafe package path')
        value = read(package / path)
        if sha(value) != row['sha256'] or len(value) != row['bytes']:
            raise ValueError('Skills package member differs: ' + path)
    return manifest, sha(raw)


def verified_method(definition, method_root, stdo):
    definition = Path(definition).absolute(); method_root = Path(method_root).absolute()
    selected = json.loads(read(definition))['constitution']['stdo']['basis']
    if selected['uri'] != 'stdo://releases/v3.0.5/':
        raise ValueError('Host installation requires the exact selected 3.0.5 Product basis')
    run = subprocess.run([stdo, 'status', '--definition', str(definition), '--verify'], capture_output=True, text=True, timeout=60)
    if run.returncode:
        raise ValueError('Method verification failed: ' + (run.stderr or run.stdout))
    observed = json.loads(run.stdout)
    if observed.get('basis') != selected['uri'] or observed.get('manifest_sha256') != selected['manifest_sha256'] or observed.get('installed') is not True or observed.get('valid') is not True or observed.get('failures'):
        raise ValueError('Manager did not verify the exact selected Product basis')
    if Path(observed.get('path', '')).resolve() != method_root.resolve() or Path(observed.get('definition', '')).resolve() != definition.resolve():
        raise ValueError('Manager verified a different method installation or Product')
    manifest_raw = read(method_root / 'manifest.json')
    manifest = json.loads(manifest_raw)
    if sha(manifest_raw) != selected['manifest_sha256'] or manifest['release']['cut'] != 'v3.0.5':
        raise ValueError('Selected method root differs from the verified Product basis')
    plugin = manifest['auxiliary']['plugin']; native = method_root / plugin['installed_root']
    files = tree(native)
    expected = {row['path']: row['sha256'] for row in plugin['members']}
    if len(expected) != plugin['member_count'] or set(files) != set(expected) or any(sha(raw) != expected[name] for name, raw in files.items()):
        raise ValueError('Native skill population or bytes differ from verified installation')
    return selected, files, observed


def runtime_pins(ac_root):
    ac_root = Path(ac_root).absolute()
    if read(ac_root / 'VERSION').decode().strip() != VERSION:
        raise ValueError('Selected a_c source package is not 3.0.5')
    selected = [ac_root / 'VERSION']
    for directory, suffix in [('scripts', '.py'), ('build_tenants/graphify/code', ''), ('build_tenants/lean/scripts', '.py'), ('build_tenants/lean/AC', '.lean'), ('build_tenants/lean/profiles', '.json')]:
        selected.extend(p for p in (ac_root / directory).rglob('*' + suffix) if p.is_file() and '__pycache__' not in p.parts)
    selected.extend([ac_root / 'build_tenants/graphify/design/fd-method-stdo-3.0.5.json', ac_root / 'build_tenants/lean/toolchain-lock.json', ac_root / 'build_tenants/lean/lake-manifest.json'])
    return {p.relative_to(ac_root).as_posix(): sha(read(p)) for p in sorted(set(selected))}


def python_selection(invocation):
    # A venv symlink's invocation directory determines sys.prefix and packages.
    # Keep that spelling; physical identity is a separate currentness check.
    invocation = Path(invocation).absolute()
    if not invocation.is_file() or not os.access(invocation, os.X_OK):
        raise ValueError('Selected Python invocation is not executable')
    physical = invocation.resolve(strict=True)
    return {'invocation': str(invocation), 'physical_path': str(physical), 'sha256': sha(read(physical))}


def manager_selection(invocation, launcher=None):
    invocation = Path(shutil.which(str(invocation)) or invocation).absolute()
    if not invocation.is_file() or not os.access(invocation, os.X_OK):
        raise ValueError('Selected manager invocation is not executable')
    physical = invocation.resolve(strict=True)
    identity = {'invocation': str(invocation), 'physical_path': str(physical),
                'sha256': sha(read(physical)), 'runtime_launcher': launcher}
    if launcher is not None:
        expected = {'path', 'sha256', 'manager', 'manager_sha256', 'store', 'manifest', 'manifest_sha256'}
        if not isinstance(launcher, dict) or set(launcher) != expected:
            raise ValueError('Malformed selected manager launcher identity')
        if any(not isinstance(launcher[key], str) or not Path(launcher[key]).is_absolute()
               for key in ('path', 'manager', 'store', 'manifest')):
            raise ValueError('Selected manager launcher paths must be absolute')
        if launcher['path'] != str(invocation) or sha(read(invocation)) != launcher['sha256']:
            raise ValueError('Selected manager launcher changed')
        if sha(read(launcher['manager'])) != launcher['manager_sha256']:
            raise ValueError('Selected underlying manager changed')
        store = Path(launcher['store'])
        if not store.is_dir() or store.resolve(strict=True) != store:
            raise ValueError('Selected manager store changed')
        if Path(launcher['manifest']) != store / 'releases' / ('v' + VERSION) / 'manifest.json':
            raise ValueError('Selected launcher manifest does not belong to its store')
        if sha(read(launcher['manifest'])) != launcher['manifest_sha256']:
            raise ValueError('Selected manager store manifest changed')
    return identity


def paths(workspace, host):
    base = Path(workspace).absolute() / ('.agents' if host == 'codex' else '.claude')
    return base, base / ('stdo-' + VERSION), base / ('stdo-skills-' + VERSION + '.receipt.json')


def prepared(package, workspace, host, definition, method_root, ac_root, stdo, python):
    manifest, package_sha = validate_package(package)
    selected_manager = manager_selection(stdo)
    basis, native, observed = verified_method(definition, method_root, selected_manager['invocation'])
    manager = manager_selection(selected_manager['invocation'], observed.get('runtime_launcher'))
    if {**manager, 'runtime_launcher': None} != selected_manager:
        raise ValueError('Selected manager changed during installation verification')
    pins = runtime_pins(ac_root)
    base, bundle, receipt = paths(workspace, host)
    files = {('stdo-' + VERSION + '/native/' + path): raw for path, raw in native.items()}
    interpreter = python_selection(python)
    configuration = {'kind': 'stdo-skills.runtime/1', 'version': VERSION, 'host': host, 'basis': basis,
                     'method_selection_scope': 'runtime-installation-anchor-only',
                     'operation_basis_rule': 'resolve the nominated Product Definition; no adoption or override',
                     'definition': str(Path(definition).absolute()), 'method_root': str(Path(method_root).absolute()),
                     'ac_root': str(Path(ac_root).absolute()), 'python': interpreter['invocation'], 'python_identity': interpreter, 'provider_pins': pins,
                     'stdo': manager['invocation'], 'manager_identity': manager, 'manager_verification': observed}
    files['stdo-' + VERSION + '/CONFIG.json'] = encode(configuration)
    files['stdo-' + VERSION + '/manage_skills.py'] = read(Path(__file__))
    extension = Path(package) / 'build_tenants' / host / 'current/skills/stdo-project'
    for path, raw in tree(extension).items():
        files['skills/stdo-project/' + path] = raw
    for name in (*CORE, *(('stdo-refresh',) if host == 'claude' else ())):
        native_path = 'claude-skills/refresh/SKILL.md' if name == 'stdo-refresh' else 'skills/' + name + '/SKILL.md'
        body = native[native_path].decode()
        desc = re.search(r'^description:\s*(.+)$', body, re.M).group(1)
        wrapper = f'---\nname: {name}\ndescription: {desc}\n---\n\nRead and apply the exact [native workflow](../../stdo-{VERSION}/native/{native_path}). This host binding owns no alternate workflow or authority. Keep that file\'s relative references in its native package. Read [host runtime](../../stdo-{VERSION}/CONFIG.json) only when its public provider is needed.\n'
        files['skills/' + name + '/SKILL.md'] = wrapper.encode()
    roots = ['stdo-' + VERSION] + sorted({'/'.join(path.split('/')[:2]) for path in files if path.startswith('skills/')})
    return base, receipt, files, roots, package_sha


def current(workspace, host, expected):
    base, bundle, receipt_path = paths(workspace, host)
    raw = read(receipt_path)
    if sha(raw) != expected:
        raise ValueError('Ownership receipt differs from the caller-selected installation')
    receipt = json.loads(raw)
    if receipt['version'] != VERSION or receipt['host'] != host:
        raise ValueError('Ownership receipt selects a different host or version')
    allowed = {'stdo-' + VERSION, 'skills/stdo-project', *('skills/' + name for name in CORE)}
    if host == 'claude':
        allowed.add('skills/stdo-refresh')
    if set(receipt['roots']) != allowed or len(receipt['roots']) != len(allowed):
        raise ValueError('Receipt owned roots differ from this exact host bundle')
    actual = {}
    for directory in receipt['roots']:
        for name, value in tree(base / directory).items():
            actual[directory + '/' + name] = sha(value)
    if actual != receipt['files']:
        raise ValueError('Owned installation changed; preserve it and reconcile before update/removal')
    return base, receipt_path, receipt


def install(args):
    base, receipt_path, files, roots, package_sha = prepared(args.package, args.workspace, args.host, args.definition, args.method_root, args.ac_root, args.stdo, args.python)
    for destination in [receipt_path, *(base / name for name in roots)]:
        if destination.exists() or destination.is_symlink():
            raise ValueError('Installation destination already exists: ' + str(destination))
        for parent in destination.parents:
            if parent.is_symlink():
                raise ValueError('Installation ancestor is a symlink')
    if args.command == 'plan':
        return {'status': 'planned', 'host': args.host, 'files': len(files), 'roots': roots, 'package_sha256': package_sha}
    for name, raw in files.items():
        target = base / name; target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as out:
            out.write(raw)
    receipt = {'kind': 'stdo-skills.installation/1', 'version': VERSION, 'host': args.host, 'package_sha256': package_sha,
               'roots': roots, 'files': {name: sha(raw) for name, raw in files.items()}}
    raw = encode(receipt)
    with receipt_path.open('xb') as out:
        out.write(raw)
    return {'status': 'installed', 'host': args.host, 'receipt': str(receipt_path), 'receipt_sha256': sha(raw), 'files': len(files)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('plan', 'install'):
        p = sub.add_parser(name)
        for field in ('package', 'workspace', 'definition', 'method-root', 'ac-root'):
            p.add_argument('--' + field, type=Path, required=True)
        p.add_argument('--host', choices=('codex', 'claude'), required=True)
        p.add_argument('--stdo', default=shutil.which('stdo')); p.add_argument('--python', default=sys.executable)
    for name in ('verify', 'remove'):
        p = sub.add_parser(name); p.add_argument('--workspace', type=Path, required=True)
        p.add_argument('--host', choices=('codex', 'claude'), required=True); p.add_argument('--receipt-sha256', required=True)
    p = sub.add_parser('check-runtime'); p.add_argument('--configuration', type=Path, required=True)
    args = parser.parse_args()
    if args.command in ('plan', 'install'):
        result = install(args)
    elif args.command == 'check-runtime':
        config = json.loads(read(args.configuration))
        if config.get('method_selection_scope') != 'runtime-installation-anchor-only':
            raise ValueError('Runtime method selection scope is missing or unsupported')
        if python_selection(config['python']) != config.get('python_identity'):
            raise ValueError('Selected Python executable changed')
        actual = runtime_pins(config['ac_root'])
        if actual != config['provider_pins']:
            raise ValueError('Selected a_c provider changed; explicitly select a current installation')
        selected_manager = config['manager_identity']
        if manager_selection(config['stdo'], selected_manager['runtime_launcher']) != selected_manager:
            raise ValueError('Selected manager executable changed')
        basis, _, observed = verified_method(config['definition'], config['method_root'], config['stdo'])
        if manager_selection(config['stdo'], observed.get('runtime_launcher')) != selected_manager:
            raise ValueError('Fresh manager verification changed the selected launcher/store identity')
        if basis != config['basis']:
            raise ValueError('Selected method basis changed')
        result = {'status': 'verified', 'configuration': config}
    else:
        base, receipt_path, receipt = current(args.workspace, args.host, args.receipt_sha256)
        if args.command == 'remove':
            for directory in receipt['roots']:
                shutil.rmtree(base / directory)
            receipt_path.unlink()
        result = {'status': 'removed' if args.command == 'remove' else 'verified', 'host': args.host, 'files': len(receipt['files'])}
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(json.dumps({'status': 'refused_or_incomplete', 'error': str(error), 'recovery': 'Retain current files/receipt; reconcile partial effects before retry.'}))
        raise SystemExit(2)
