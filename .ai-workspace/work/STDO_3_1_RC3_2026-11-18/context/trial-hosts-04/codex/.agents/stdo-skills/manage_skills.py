#!/usr/bin/env python3
"""Install an exact Skills package over its independently selected Products."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

CORE = ('stdo-work', 'stdo-review', 'stdo-ticket', 'stdo-status', 'stdo-help')
BUNDLE = 'stdo-skills-dev'
RECEIPT = 'stdo-skills-dev.receipt.json'
RELEASE_BUNDLE = 'stdo-skills'
RELEASE_RECEIPT = 'stdo-skills.receipt.json'
ROOT = Path(__file__).resolve().parents[1]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def read(path):
    path = Path(path)
    if any(p.is_symlink() for p in (path, *path.parents)) or not path.is_file():
        raise ValueError('Expected regular file without symlink ancestors: ' + str(path))
    return path.read_bytes()


def tree(root):
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('Expected real source directory: ' + str(root))
    result = {}
    for current, dirs, files in os.walk(root, followlinks=False):
        for name in dirs:
            if (Path(current) / name).is_symlink():
                raise ValueError('Symlink directory in owned tree')
        for name in files:
            p = Path(current) / name
            result[p.relative_to(root).as_posix()] = read(p)
    return result


def provider(package):
    path = Path(package) / 'skills/stdo-context/scripts/provider.py'
    spec = importlib.util.spec_from_file_location('skills_product_binding', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_package(package):
    package = Path(package).resolve(strict=True)
    raw = read(package / 'INVENTORY.json'); manifest = json.loads(raw)
    if manifest.get('kind') not in {'stdo-skills.development-package/1', 'stdo-skills.release-package/1'}:
        raise ValueError('Expected an explicitly inventoried Skills package')
    if manifest.get('product_definition_id') != 'urn:stdo:product-definition:stdo-skills':
        raise ValueError('Package Product identity differs')
    if manifest['kind'] == 'stdo-skills.release-package/1':
        release_identity(manifest['release'])
    declared = {x['path']: x for x in manifest['files']}
    if len(declared) != len(manifest['files']):
        raise ValueError('Duplicate package member')
    actual = tree(package); actual.pop('INVENTORY.json')
    if set(actual) != set(declared):
        raise ValueError('Package population differs from its exact inventory')
    for name, data in actual.items():
        if sha(data) != declared[name]['sha256'] or len(data) != declared[name]['bytes']:
            raise ValueError('Package member changed: ' + name)
    required = {'scripts/manage_skills.py', 'skills/stdo-context/SKILL.md',
                'skills/stdo-context/BINDING.json', 'skills/stdo-context/scripts/provider.py',
                'specification/composition/DEPENDENCIES.json'}
    if not required <= set(actual):
        raise ValueError('Incomplete Skills adapter package')
    return package, manifest, sha(raw)


def release_identity(value):
    version = value['version']; method = value['native_method']
    if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-rc\.\d+)?', version):
        raise ValueError('Invalid exact Skills release version')
    if method['uri'] != 'stdo://releases/v' + version + '/' or not re.fullmatch(r'[0-9a-f]{64}', method['manifest_sha256']):
        raise ValueError('Release package native binding differs')
    return value


def executable(path):
    path = Path(shutil.which(str(path)) or path).absolute()
    if not path.is_file() or not os.access(path, os.X_OK):
        raise ValueError('Selected executable unavailable: ' + str(path))
    return {'invocation': str(path), 'sha256': sha(path.resolve(strict=True).read_bytes())}


def native_method(definition, method_root, stdo):
    definition = Path(definition).resolve(strict=True); root = Path(method_root).resolve(strict=True)
    selected = json.loads(read(definition))['constitution']['stdo']['basis']
    manager = executable(stdo)
    call = subprocess.run([manager['invocation'], 'status', '--definition', str(definition), '--verify'], capture_output=True, text=True, timeout=60)
    if call.returncode:
        raise ValueError('Selected method verification failed: ' + (call.stderr or call.stdout))
    observed = json.loads(call.stdout)
    if observed.get('basis') != selected['uri'] or observed.get('manifest_sha256') != selected['manifest_sha256'] or observed.get('valid') is not True or observed.get('installed') is not True or observed.get('failures'):
        raise ValueError('Manager did not verify the selected exact method')
    if Path(observed.get('path', '')).resolve() != root or Path(observed.get('definition', '')).resolve() != definition:
        raise ValueError('Manager returned another installation or Product')
    raw = read(root / 'manifest.json')
    if sha(raw) != selected['manifest_sha256']:
        raise ValueError('Native method manifest differs')
    manifest = json.loads(raw); plugin = manifest['auxiliary']['plugin']
    relative = plugin['installed_root']
    if Path(relative).is_absolute() or any(x in ('', '.', '..') for x in relative.split('/')):
        raise ValueError('Unsafe native plugin location')
    native = root / relative; files = tree(native)
    declared = {x['path']: x['sha256'] for x in plugin['members']}
    if len(declared) != plugin['member_count'] or set(files) != set(declared) or any(sha(v) != declared[k] for k, v in files.items()):
        raise ValueError('Native plugin population or content differs')
    launcher = observed.get('runtime_launcher')
    if launcher:
        for field, digest in [('manager', 'manager_sha256'), ('manifest', 'manifest_sha256')]:
            if sha(Path(launcher[field]).read_bytes()) != launcher[digest]:
                raise ValueError('Selected manager/store dependency changed')
    return {'basis': selected, 'definition': str(definition), 'definition_sha256': sha(read(definition)),
            'method_root': str(root), 'native_root': str(native), 'manager': manager,
            'runtime_launcher': launcher}, files


def native_header(raw, name):
    match = re.match(r'\A---\r?\n.*?\r?\n---(?:\r?\n|\Z)', raw.decode(), re.S)
    if not match:
        raise ValueError('Native skill lacks frontmatter')
    header = match.group(0)
    if any(len(re.findall(r'^' + key + r':', header, re.M)) != 1 for key in ['name', 'description']):
        raise ValueError('Ambiguous native skill metadata')
    header = re.sub(r'^name:[^\r\n]*', 'name: ' + name, header, count=1, flags=re.M)
    return header + ('' if header.endswith('\n') else '\n')


def prepared(args):
    package, manifest, package_sha = validate_package(args.package)
    if read(package / 'scripts/manage_skills.py') != Path(__file__).read_bytes():
        raise ValueError('Invoke the selected package installer')
    dependency = json.loads(read(package / 'specification/composition/DEPENDENCIES.json'))
    components = {}
    for name, selected_root in [('purpose_context', args.purpose_context), ('visual', args.visual_root)]:
        if selected_root is None:
            continue
        spec = dependency['components'].get(name)
        if spec is None:
            raise ValueError('Component is not declared by this package: ' + name)
        components[name] = {**spec, 'root': str(Path(selected_root).resolve(strict=True))}
    release = manifest.get('release') if manifest['kind'] == 'stdo-skills.release-package/1' else None
    bundle = RELEASE_BUNDLE if release else BUNDLE
    configuration = {'kind': 'stdo-skills.release-runtime/1' if release else 'stdo-skills.development-runtime/1', 'components': components,
                     'python': executable(args.python), 'host': args.host,
                     'standing': 'Exact installed binding; publication, semantic coverage and host behavior are separate evidence.' if release else 'development installation; no release or automatic host qualification'}
    if release:
        configuration['release'] = release
    binding = provider(package)
    for name in components:
        binding.component(configuration, name, package / 'INVENTORY.json')
    method, native = native_method(args.definition, args.method_root, args.stdo)
    if release and method['basis'] != release['native_method']:
        raise ValueError('Selected Product native basis differs from release package')
    configuration['native_method'] = method
    files = {bundle + '/CONFIG.json': encode(configuration), bundle + '/manage_skills.py': read(package / 'scripts/manage_skills.py')}
    for guide in ['GETTING_STARTED.md', 'RELEASE.md', 'scripts/INSTALLATION.md']:
        files[bundle + '/' + guide] = read(package / guide)
    for name, raw in tree(package / 'skills/stdo-context').items():
        files['skills/stdo-context/' + name] = raw
    files['skills/stdo-context/BINDING.json'] = encode({'configuration': '../../' + bundle + '/CONFIG.json'})
    if args.visual_root:
        for name, raw in tree(package / 'build_tenants' / args.host / 'current/skills/stdo-project').items():
            files['skills/stdo-project/' + name] = raw
    for name in (*CORE, *(('stdo-refresh',) if args.host == 'claude' else ())):
        relative = 'claude-skills/refresh/SKILL.md' if name == 'stdo-refresh' else 'skills/' + name + '/SKILL.md'
        header = native_header(native[relative], name)
        target = (Path(method['native_root']) / relative).as_uri()
        body = '\nFollow the exact [native workflow](' + target + ') and its canonical relative references. It owns intake, grants, assessment, handoff and recovery; this host binding creates no alternate lifecycle.\n'
        body += '\nFor relevant task constraints, code builds, review context, continuation or context refresh, use [Purpose Context](../stdo-context/SKILL.md) and its reusable purpose indexes after native control intake. At SDLC work, QA, finding-triage, repair or acceptance/release decisions, select its declared workflow purpose and adopted default with the actual decision facts; retain the bound outcome, scope, subject and basis. Required source-first review derives expectations before candidate-derived index judgments. Source/method/purpose mismatch and unknown facts remain explicit. Ordinary unrelated work need not construct context.\n'
        body += '\nFor this exact Skills package installation and purpose selection, use [Getting Started](../../' + bundle + '/GETTING_STARTED.md). Frozen native setup instructions retain their original release scope; the current guide locates the independently selected Products.\n'
        body += '\nFor ticketed work or resumption, bind the current ticket or sufficient admitted carrier and actual source/evidence under the selected native TICKETS and ACTIVATION laws. Construct only the next decision context, preserve its declared acquisition bounds, and reconcile invalidated support or unknown effects before dependent work. Record facts/results through the permitted native return route; only the granted Writer updates work state. Private context, a summary or an index is no rival authority and resets no completed work.\n'
        if args.visual_root:
            body += '\nFor visual documentation or code/test-source exploration, use the separately selected [visual project skill](../stdo-project/SKILL.md).\n'
        files['skills/' + name + '/SKILL.md'] = (header + body).encode()
    return configuration, files, package_sha


def paths(workspace, host, released=False):
    base = Path(workspace).absolute() / ('.agents' if host == 'codex' else '.claude')
    return base, base / (RELEASE_RECEIPT if released else RECEIPT)


def install(args):
    configuration, files, package_sha = prepared(args)
    released = configuration['kind'] == 'stdo-skills.release-runtime/1'
    bundle = RELEASE_BUNDLE if released else BUNDLE
    base, receipt = paths(args.workspace, args.host, released)
    roots = [bundle] + sorted({'/'.join(x.split('/')[:2]) for x in files if x.startswith('skills/')})
    for target in [receipt, *(base / x for x in roots)]:
        if target.exists() or target.is_symlink() or any(p.is_symlink() for p in target.parents):
            raise ValueError('Installation destination collision or symlink: ' + str(target))
    if args.command == 'plan':
        return {'status': 'planned', 'roots': roots, 'package_sha256': package_sha, 'components': sorted(configuration['components'])}
    for name, raw in files.items():
        target = base / name; target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as out:
            out.write(raw)
    record = {'kind': 'stdo-skills.release-installation/1' if released else 'stdo-skills.development-installation/1', 'host': args.host, 'package_sha256': package_sha,
              'roots': roots, 'files': {k: sha(v) for k, v in files.items()}}
    if released:
        record['release'] = configuration['release']
    with receipt.open('xb') as out:
        out.write(encode(record))
    return {'status': 'installed', 'receipt': str(receipt), 'receipt_sha256': sha(receipt.read_bytes()), 'components': sorted(configuration['components'])}


def owned(args):
    base, _ = paths(args.workspace, args.host)
    matches = [p for p in (base / RECEIPT, base / RELEASE_RECEIPT) if p.is_file() and sha(read(p)) == args.receipt_sha256]
    if len(matches) != 1:
        raise ValueError('Receipt identity differs')
    path = matches[0]; raw = read(path)
    receipt = json.loads(raw)
    released = receipt.get('kind') == 'stdo-skills.release-installation/1'
    if receipt.get('kind') not in {'stdo-skills.development-installation/1', 'stdo-skills.release-installation/1'} or receipt.get('host') != args.host:
        raise ValueError('Not this Skills installation')
    if path.name != (RELEASE_RECEIPT if released else RECEIPT):
        raise ValueError('Receipt path and installation kind differ')
    if released:
        release_identity(receipt['release'])
    bundle = RELEASE_BUNDLE if released else BUNDLE
    required = {bundle, 'skills/stdo-context', *('skills/' + n for n in CORE)}
    if args.host == 'claude':
        required.add('skills/stdo-refresh')
    roots = set(receipt['roots'])
    if roots not in (required, required | {'skills/stdo-project'}) or len(roots) != len(receipt['roots']):
        raise ValueError('Receipt contains unsupported ownership roots')
    actual = {root + '/' + n: sha(v) for root in receipt['roots'] for n, v in tree(base / root).items()}
    if actual != receipt['files']:
        raise ValueError('Owned files changed; preserve and reconcile before removal')
    return base, path, receipt


def verify_configuration(path):
    value = json.loads(read(path)); method = value['native_method']
    if executable(method['manager']['invocation']) != method['manager'] or sha(read(method['definition'])) != method['definition_sha256']:
        raise ValueError('Selected native manager or Product changed')
    observed, _ = native_method(method['definition'], method['method_root'], method['manager']['invocation'])
    if observed != method:
        raise ValueError('Native method/store binding changed')
    if value.get('kind') == 'stdo-skills.release-runtime/1' and release_identity(value['release'])['native_method'] != method['basis']:
        raise ValueError('Runtime release native binding differs')
    base = path.parent.parent
    module = provider(base)
    module.python(value)
    for name in value['components']:
        module.component(value, name, path)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__); sub = parser.add_subparsers(dest='command', required=True)
    for name in ['plan', 'install']:
        p = sub.add_parser(name)
        for field in ['package', 'workspace', 'definition', 'method-root', 'purpose-context']:
            p.add_argument('--' + field, type=Path, required=True)
        p.add_argument('--visual-root', type=Path);p.add_argument('--host', choices=['codex', 'claude'], required=True)
        p.add_argument('--stdo', default=shutil.which('stdo'));p.add_argument('--python', default=sys.executable)
    for name in ['verify', 'remove']:
        p = sub.add_parser(name);p.add_argument('--workspace', type=Path, required=True)
        p.add_argument('--host', choices=['codex', 'claude'], required=True);p.add_argument('--receipt-sha256', required=True)
    p=sub.add_parser('check-runtime');p.add_argument('--configuration', type=Path, required=True)
    args=parser.parse_args()
    try:
        if args.command in ['plan','install']:
            result=install(args)
        elif args.command=='check-runtime':
            result={'status':'verified','configuration':verify_configuration(args.configuration)}
        else:
            base,path,receipt=owned(args)
            if args.command=='verify':
                bundle = RELEASE_BUNDLE if receipt['kind'] == 'stdo-skills.release-installation/1' else BUNDLE
                configuration = verify_configuration(base/bundle/'CONFIG.json')
                if receipt.get('release') != configuration.get('release'):
                    raise ValueError('Receipt and runtime release identities differ')
            else:
                for root in receipt['roots']:shutil.rmtree(base/root)
                path.unlink()
            result={'status':'verified' if args.command=='verify' else 'removed','owned_roots':receipt['roots']}
        print(json.dumps(result,indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError,subprocess.TimeoutExpired) as exc:
        print(json.dumps({'status':'refused_or_incomplete','error':str(exc),'recovery':'Preserve partial effects and exact receipt; reconcile before retry.'}),file=sys.stderr);return 2


if __name__=='__main__':raise SystemExit(main())
