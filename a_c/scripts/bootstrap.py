#!/usr/bin/env python3
"""Explicit isolated setup for a_c 3.0.5-rc.1; never changes global environments."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
GRAPHIFY_COMMIT = 'fe085cedddde3a18554f8749b230bfe47f3dcce7'
GRAPHIFY_REPOSITORY = 'https://github.com/Graphify-Labs/graphify.git'


class ExecutionLog:
    """Retain each actual setup command and its byte-exact output."""
    def __init__(self, root):
        self.root = Path(root); self.root.mkdir(parents=True, exist_ok=False)
        self.steps = []

    def run(self, argv, **kwargs):
        argv = [str(x) for x in argv]; index = str(len(self.steps) + 1).zfill(3)
        started = time.time_ns()
        result = subprocess.run(argv, capture_output=True, **kwargs)
        row = {'argv': argv, 'cwd': str(Path(kwargs.get('cwd', Path.cwd())).absolute()),
               'started_ns': started, 'ended_ns': time.time_ns(), 'exit_code': result.returncode}
        for name, raw in (('stdout', result.stdout), ('stderr', result.stderr)):
            path = self.root / (index + '.' + name + '.log'); path.write_bytes(raw)
            row[name] = {'path': path.name, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
            stream = sys.stdout.buffer if name == 'stdout' else sys.stderr.buffer
            stream.write(raw); stream.flush()
        self.steps.append(row)
        (self.root / 'execution.json').write_text(json.dumps({'schema': 'a_c.bootstrap.execution/1', 'python': sys.version, 'steps': self.steps}, indent=2) + '\n')
        result.check_returncode()
        return result


def graphify(destination):
    destination = destination.absolute()
    if any(p.is_symlink() for p in (destination, *destination.parents)):
        raise ValueError('Graphify runtime destination may not traverse symlinks')
    if destination.exists() or destination.is_symlink():
        raise ValueError('Graphify runtime destination must be absent; retain partial setup before retry')
    destination.mkdir(parents=True)
    log = ExecutionLog(destination / 'bootstrap-evidence')
    python_root = destination / 'venv'
    log.run([sys.executable, '-m', 'venv', python_root])
    python = python_root / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    upstream = destination / 'graphify'
    log.run(['git', 'init', upstream])
    log.run(['git', '-C', upstream, 'remote', 'add', 'origin', GRAPHIFY_REPOSITORY])
    log.run(['git', '-C', upstream, 'fetch', '--depth', '1', 'origin', GRAPHIFY_COMMIT])
    log.run(['git', '-C', upstream, 'checkout', '--detach', GRAPHIFY_COMMIT])
    observed = log.run(['git', '-C', upstream, 'rev-parse', 'HEAD']).stdout.decode().strip()
    if observed != GRAPHIFY_COMMIT:
        raise ValueError('Upstream checkout differs from exact pin')
    tenant = ROOT / 'build_tenants/graphify'
    for requirements in ('test_env/requirements-qualification.txt', 'code/generation/requirements.txt', 'code/code-requirements.txt'):
        log.run([python, '-m', 'pip', 'install', '-r', tenant / requirements])
    packages = log.run([python, '-m', 'pip', 'freeze', '--all']).stdout
    package_file = destination / 'bootstrap-evidence/packages.txt'; package_file.write_bytes(packages)
    log.run(['git', '-C', upstream, 'diff', '--exit-code', 'HEAD'])
    result = {'version': '3.0.5-rc.1', 'status': 'installed', 'python': str(python), 'upstream': str(upstream), 'upstream_commit': observed,
              'bootstrap_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'execution': str(log.root / 'execution.json'), 'packages_sha256': hashlib.sha256(packages).hexdigest(),
              'requirements': {name: hashlib.sha256((tenant / name).read_bytes()).hexdigest() for name in ('test_env/requirements-qualification.txt', 'code/generation/requirements.txt', 'code/code-requirements.txt')}}
    (destination / 'RUNTIME.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def lean(establish_support):
    tenant = ROOT / 'build_tenants/lean'
    log = ExecutionLog(tenant / '.bootstrap' / ('setup-' + uuid.uuid4().hex))
    log.run([sys.executable, '-B', tenant / 'scripts/bootstrap.py'])
    if establish_support:
        support = tenant / 'profiles/proof-support-v1.json'
        if support.exists():
            raw = support.read_bytes()
            retained = tenant / '.bootstrap' / ('proof-support-' + hashlib.sha256(raw).hexdigest() + '.json')
            retained.parent.mkdir(exist_ok=True)
            if retained.exists() and retained.read_bytes() != raw:
                raise ValueError('Conflicting retained support manifest')
            if not retained.exists():
                retained.write_bytes(raw)
            support.unlink()
        # This is an explicit fresh local support establishment, not proof reuse.
        log.run([sys.executable, '-B', tenant / 'scripts/formal_support.py', '--output', support])
    return {'version': '3.0.5-rc.1', 'status': 'installed', 'lean_root': str(tenant),
            'execution': str(log.root / 'execution.json'),
            'toolchain_lock_sha256': hashlib.sha256((tenant / 'toolchain-lock.json').read_bytes()).hexdigest(),
            'proof_support': 'freshly_established' if establish_support else 'not_reestablished',
            'next': 'Select the exact checker with ac.py formal-select after support establishment.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check')
    graph = sub.add_parser('graphify'); graph.add_argument('--destination', type=Path, required=True)
    formal = sub.add_parser('lean'); formal.add_argument('--establish-support', action='store_true')
    args = parser.parse_args()
    if args.command == 'check':
        result = {'version': '3.0.5-rc.1', 'python': sys.version, 'base_tools': 'available',
                  'optional_setup': {'graphify': 'graphify --destination NEW_DIR', 'lean': 'lean --establish-support'},
                  'executables': {name: shutil.which(name) for name in ('stdo', 'git', 'curl', 'tar', 'zstd')}}
    elif args.command == 'graphify':
        result = graphify(args.destination)
    else:
        result = lean(args.establish_support)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(json.dumps({'status': 'incomplete', 'error': str(error), 'recovery': 'Preserve partial runtime and reconcile before retry.'}))
        raise SystemExit(2)
