#!/usr/bin/env python3
"""Resolve exact external Products and forward public operations; owns no index engine."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def member(root, relative):
    p = Path(relative)
    if p.is_absolute() or not p.parts or any(x in ('', '.', '..') for x in relative.split('/')):
        raise ValueError('Unsafe dependency member path')
    target = root / p
    if target.is_symlink() or any(x.is_symlink() for x in target.parents if x != root.parent):
        raise ValueError('Dependency member or ancestor is a symlink')
    if not target.is_file():
        raise ValueError('Dependency member is missing: ' + relative)
    return target


def component(configuration, name, configuration_path):
    spec = configuration.get('components', {}).get(name)
    if spec is None:
        raise ValueError('Component not selected: ' + name)
    root = Path(spec['root'])
    if not root.is_absolute():
        root = configuration_path.parent / root
    root = root.resolve(strict=True)
    manifest_path = member(root, spec['manifest'])
    raw = manifest_path.read_bytes()
    if sha(raw) != spec['manifest_sha256']:
        raise ValueError('Selected component manifest changed: ' + name)
    manifest = json.loads(raw)
    if manifest['product_definition_id'] != spec['product_definition_id']:
        raise ValueError('Selected component Product differs: ' + name)
    seen = set()
    for row in manifest['files']:
        if row['path'] in seen:
            raise ValueError('Duplicate dependency member')
        seen.add(row['path'])
        data = member(root, row['path']).read_bytes()
        if sha(data) != row['sha256'] or len(data) != row['bytes']:
            raise ValueError('Selected component member changed: ' + row['path'])
    if manifest['entrypoint'] not in seen:
        raise ValueError('Public entrypoint is outside the selected manifest')
    return root, manifest


def configuration(path=None):
    if path is None:
        binding = Path(__file__).resolve().parents[1] / 'BINDING.json'
        path = binding.parent / read_json(binding)['configuration']
    path = Path(path).resolve(strict=True)
    value = read_json(path)
    if value.get('kind') not in {'stdo-skills.source-dependencies/1', 'stdo-skills.development-runtime/1', 'stdo-skills.release-runtime/1'}:
        raise ValueError('Unsupported Skills dependency configuration')
    return path, value


def python(value):
    selected = value.get('python')
    if selected is None:
        return sys.executable
    path = Path(selected['invocation'])
    if not path.is_file() or not os.access(path, os.X_OK) or sha(path.resolve().read_bytes()) != selected['sha256']:
        raise ValueError('Selected Python changed')
    return str(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--configuration', type=Path)
    parser.add_argument('operation', choices=['describe', 'context', 'visual'])
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    try:
        path, value = configuration(args.configuration)
        name = 'visual' if args.operation == 'visual' else 'purpose_context'
        root, manifest = component(value, name, path)
        interpreter = python(value)
        if args.operation == 'describe':
            result = {'status': 'verified', 'product_definition_id': manifest['product_definition_id'],
                      'root': str(root), 'manifest_sha256': value['components'][name]['manifest_sha256'],
                      'cli': str(root / manifest['entrypoint']), 'skill': str(root / manifest['skill']),
                      'catalog': str(root / manifest['catalog']), 'python': interpreter,
                      'visual_selected': value.get('components', {}).get('visual') is not None,
                      'limit': 'Dependency identity only; no semantic coverage or host qualification.'}
            print(json.dumps(result, indent=2))
            return 0
        arguments = args.arguments[1:] if args.arguments[:1] == ['--'] else args.arguments
        return subprocess.run([interpreter, '-B', str(root / manifest['entrypoint']), *arguments]).returncode
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'refused', 'reason': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
