#!/usr/bin/env python3
"""Prepare, check and atomically publish the explicit six-Product ref graph."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def remote_refs(root):
    return {line.split('\t')[1]: line.split('\t')[0]
            for line in git(root, 'ls-remote', 'origin').splitlines()}


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def check(root, plan, remote):
    if plan['version'] != '3.1.0-rc.1' or len(plan['refs']) != 25:
        raise ValueError('Wrong version or incomplete ref graph')
    if len({r['destination'] for r in plan['refs']}) != 25:
        raise ValueError('Duplicate destination')
    products = {p['namespace']: p for p in plan['products']}
    if set(products) != {'specification_methodology', 'purpose_context', 'stdo_skills',
                         'a_c', 'stdo_representation', 'axiom_indexer'}:
        raise ValueError('Wrong Product membership')
    expected = {'refs/heads/main'}
    for namespace, product in products.items():
        commit = product['commit']
        if git(root, 'rev-parse', commit + ':' + product['root']) != product['subtree_tree']:
            raise ValueError('Changed Product tree: ' + namespace)
        for kind in ['cut', 'selector', 'rc', 'release']:
            destination = {'cut': f'refs/tags/{namespace}/v3.1.0-rc.1',
                           'selector': f'refs/tags/{namespace}/v3.1.0',
                           'rc': f'refs/heads/rc/{namespace}/3.1.0',
                           'release': f'refs/heads/release/{namespace}/3.1.0'}[kind]
            expected.add(destination)
            row = next(r for r in plan['refs'] if r['destination'] == destination)
            if row['commit'] != commit or git(root, 'rev-parse', destination + '^{commit}') != commit:
                raise ValueError('Wrong Product target: ' + destination)
            if destination.startswith('refs/tags/') and git(root, 'cat-file', '-t', destination) != 'tag':
                raise ValueError('Unannotated tag: ' + destination)
    if expected != {r['destination'] for r in plan['refs']}:
        raise ValueError('Unexpected ref')
    for row in plan['refs']:
        if git(root, 'rev-parse', row['source']) != row['object']:
            raise ValueError('Changed local object: ' + row['destination'])
        if remote.get(row['destination'], '') != row['expected_remote']:
            raise ValueError('Changed remote object: ' + row['destination'])
        if row['immutable'] and row['expected_remote']:
            raise ValueError('Immutable tag already exists remotely')
    for item in plan['qualified_files']:
        if hashlib.sha256(Path(item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('Changed qualification input: ' + item['path'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'check', 'publish'])
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--carrier')
    parser.add_argument('--native')
    parser.add_argument('--qualification', type=Path)
    parser.add_argument('--result', type=Path, required=True)
    args = parser.parse_args()
    remote = remote_refs(args.root)
    if args.mode == 'prepare':
        if args.plan.exists():
            raise FileExistsError(args.plan)
        inputs = json.loads((args.root / 'releases/3.1.0-rc.1/COHORT_INPUTS.json').read_text())
        qualification = json.loads(args.qualification.read_text())
        if qualification['status'] != 'qualified-for-declared-prepublication-claims':
            raise ValueError('Prepublication qualification is incomplete')
        if qualification['carrier'] != args.carrier or qualification['native'] != args.native:
            raise ValueError('Qualification subjects differ')
        if remote.get('refs/heads/main') != qualification['expected_remote_main']:
            raise ValueError('Remote main changed')
        subprocess.run(['git', '-C', str(args.root), 'merge-base', '--is-ancestor',
                        remote['refs/heads/main'], args.carrier], check=True)
        selected = [f'refs/{prefix}/{p["namespace"]}/{suffix}'
                    for p in inputs['products']
                    for prefix, suffix in [('tags', 'v3.1.0-rc.1'), ('tags', 'v3.1.0')]]
        selected += [f'refs/heads/{kind}/{p["namespace"]}/3.1.0'
                     for p in inputs['products'] for kind in ['rc', 'release']]
        if any(ref in remote for ref in selected):
            raise ValueError('A selected new release ref already exists remotely')
        rows = [{'destination': 'refs/heads/main', 'source': args.carrier,
                 'object': args.carrier, 'commit': args.carrier, 'immutable': False,
                 'expected_remote': remote['refs/heads/main']}]
        products = []
        for product in inputs['products']:
            namespace = product['namespace']
            commit = args.native if product['commit_role'] == 'native-A' else args.carrier
            tree = git(args.root, 'rev-parse', commit + ':' + product['root'])
            products.append({**product, 'commit': commit, 'subtree_tree': tree})
            for tag in [f'{namespace}/v3.1.0-rc.1', f'{namespace}/v3.1.0']:
                ref = 'refs/tags/' + tag
                if ref != 'refs/tags/specification_methodology/v3.1.0-rc.1':
                    message = f'STDO 3.1.0-rc.1 {namespace}\n\nSTDO-Product-Subtree: {product["root"]}\nSTDO-Product-Tree: {tree}\nSTDO-Native-Commit: {args.native}\nSTDO-Cohort-Profile: rc-six-product-v1\n'
                    subprocess.run(['git', '-C', str(args.root), 'tag', '-a', tag, commit,
                                    '-F', '-'], input=message, text=True, check=True)
                rows.append({'destination': ref, 'source': ref,
                             'object': git(args.root, 'rev-parse', ref), 'commit': commit,
                             'immutable': tag.endswith('-rc.1'), 'expected_remote': ''})
            for kind in ['rc', 'release']:
                ref = f'refs/heads/{kind}/{namespace}/3.1.0'
                subprocess.run(['git', '-C', str(args.root), 'update-ref', ref, commit,
                                '0' * 40], check=True)
                rows.append({'destination': ref, 'source': ref, 'object': commit,
                             'commit': commit, 'immutable': False, 'expected_remote': ''})
        plan = {'kind': 'stdo.atomic-ref-transaction/1', 'version': '3.1.0-rc.1',
                'products': products, 'refs': rows, 'qualified_files': qualification['qualified_files'] +
                    [{'path': str(args.qualification.resolve()), 'sha256': hashlib.sha256(args.qualification.read_bytes()).hexdigest()}]}
        write(args.plan, plan)
    else:
        plan = json.loads(args.plan.read_text())
    check(args.root, plan, remote)
    result = {'mode': args.mode, 'local_graph_valid': True, 'remote_expectations_match': True,
              'plan_sha256': hashlib.sha256(args.plan.read_bytes()).hexdigest(), 'refs': len(plan['refs'])}
    if args.mode == 'publish':
        argv = ['git', '-C', str(args.root), 'push', '--atomic']
        argv += [f'--force-with-lease={r["destination"]}:{r["expected_remote"]}' for r in plan['refs']]
        argv += ['origin'] + [r['source'] + ':' + r['destination'] for r in plan['refs']]
        proc = subprocess.run(argv, capture_output=True, text=True)
        result.update({'argv': argv, 'exit': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr})
        write(args.result, result)
        if proc.returncode:
            raise SystemExit(proc.returncode)
        after = remote_refs(args.root)
        for row in plan['refs']:
            if after.get(row['destination']) != row['object']:
                raise ValueError('Remote readback mismatch: ' + row['destination'])
            if row['destination'].startswith('refs/tags/') and after.get(row['destination'] + '^{}') != row['commit']:
                raise ValueError('Remote peel mismatch: ' + row['destination'])
        result['remote_readback_valid'] = True
    write(args.result, result)
    print(json.dumps({key: value for key, value in result.items() if key not in ['argv', 'stdout', 'stderr']}))


if __name__ == '__main__':
    main()
