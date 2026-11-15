#!/usr/bin/env python3
"""Qualify and atomically advance the explicit six-Product RC1 cohort to RC2."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

VERSION = '3.1.0-rc.2'
LINE = '3.1.0'
PREDECESSOR = '3.1.0-rc.1'
NAMES = {'specification_methodology', 'purpose_context', 'stdo_skills',
         'a_c', 'stdo_representation', 'axiom_indexer'}


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def remote_refs(root):
    return {line.split('\t')[1]: line.split('\t')[0]
            for line in git(root, 'ls-remote', 'origin').splitlines()}


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def no_published_successor(remote):
    for namespace in NAMES:
        pattern = re.compile(r'^refs/tags/' + re.escape(namespace) + r'/v3\.1\.0-rc\.(\d+)$')
        if any((match := pattern.match(ref)) and int(match[1]) >= 2 for ref in remote):
            raise ValueError('RC2 or higher already published: ' + namespace)


def predecessor_graph(root, inputs, remote):
    protected = {}
    if {p['namespace'] for p in inputs['products']} != NAMES:
        raise ValueError('Wrong Product population')
    for product in inputs['products']:
        namespace = product['namespace']
        commit = inputs['native_predecessor'] if product['commit_role'] == 'native-A' else inputs['source_predecessor']
        cut = f'refs/tags/{namespace}/v{PREDECESSOR}'
        selector = f'refs/tags/{namespace}/v{LINE}'
        if not remote.get(cut) or remote.get(cut + '^{}') != commit:
            raise ValueError('Predecessor immutable identity differs: ' + namespace)
        protected[cut] = remote[cut]
        protected[cut + '^{}'] = commit
        if not remote.get(selector) or remote.get(selector + '^{}') != commit:
            raise ValueError('Selector is not declared predecessor: ' + namespace)
        for ref in [selector, f'refs/heads/rc/{namespace}/{LINE}', f'refs/heads/release/{namespace}/{LINE}']:
            if not remote.get(ref) or (not ref.startswith('refs/tags/') and remote[ref] != commit):
                raise ValueError('Predecessor mutable identity differs: ' + ref)
            if git(root, 'rev-parse', ref) != remote[ref]:
                raise ValueError('Local mutable ref differs from remote: ' + ref)
    return protected


def tag_object(root, name, commit, message):
    tagger = git(root, 'var', 'GIT_COMMITTER_IDENT')
    body = f'object {commit}\ntype commit\ntag {name}\ntagger {tagger}\n\n{message}'
    return subprocess.check_output(['git', '-C', str(root), 'mktag'],
                                   input=body, text=True).strip()


def check(root, plan, remote):
    if plan['version'] != VERSION or len(plan['refs']) != 25:
        raise ValueError('Wrong version or incomplete ref graph')
    if len({r['destination'] for r in plan['refs']}) != 25:
        raise ValueError('Duplicate destination')
    products = {p['namespace']: p for p in plan['products']}
    if set(products) != NAMES:
        raise ValueError('Wrong Product membership')
    no_published_successor(remote)
    expected_protected = {f'refs/tags/{n}/v{PREDECESSOR}{suffix}'
                          for n in NAMES for suffix in ['', '^{}']}
    if set(plan['protected_predecessor_refs']) != expected_protected:
        raise ValueError('Incomplete predecessor preservation graph')
    for ref, obj in plan['protected_predecessor_refs'].items():
        if remote.get(ref) != obj:
            raise ValueError('Predecessor immutable ref changed: ' + ref)
    expected = {'refs/heads/main'}
    for namespace, product in products.items():
        commit = product['commit']
        if git(root, 'rev-parse', commit + ':' + product['root']) != product['subtree_tree']:
            raise ValueError('Changed Product tree: ' + namespace)
        for kind in ['cut', 'selector', 'rc', 'release']:
            destination = {'cut': f'refs/tags/{namespace}/v{VERSION}',
                           'selector': f'refs/tags/{namespace}/v{LINE}',
                           'rc': f'refs/heads/rc/{namespace}/{LINE}',
                           'release': f'refs/heads/release/{namespace}/{LINE}'}[kind]
            expected.add(destination)
            row = next(r for r in plan['refs'] if r['destination'] == destination)
            if row['commit'] != commit or git(root, 'rev-parse', destination + '^{commit}') != commit:
                raise ValueError('Wrong Product target: ' + destination)
            if destination.startswith('refs/tags/') and git(root, 'cat-file', '-t', destination) != 'tag':
                raise ValueError('Unannotated tag: ' + destination)
            if row['immutable'] != (kind == 'cut'):
                raise ValueError('Wrong mutability: ' + destination)
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
        inputs = json.loads((args.root / f'releases/{VERSION}/COHORT_INPUTS.json').read_text())
        qualification = json.loads(args.qualification.read_text())
        if inputs['version'] != VERSION or qualification['status'] != 'qualified-for-declared-prepublication-claims':
            raise ValueError('Wrong selection or incomplete qualification')
        if qualification['carrier'] != args.carrier or qualification['native'] != args.native:
            raise ValueError('Qualification subjects differ')
        if remote.get('refs/heads/main') != qualification['expected_remote_main']:
            raise ValueError('Remote main changed')
        subprocess.run(['git', '-C', str(args.root), 'merge-base', '--is-ancestor',
                        remote['refs/heads/main'], args.carrier], check=True)
        no_published_successor(remote)
        protected = predecessor_graph(args.root, inputs, remote)
        rows = [{'destination': 'refs/heads/main', 'source': args.carrier,
                 'object': args.carrier, 'commit': args.carrier, 'immutable': False,
                 'expected_remote': remote['refs/heads/main']}]
        products = []
        updates = ['start']
        for product in inputs['products']:
            namespace = product['namespace']
            commit = args.native if product['commit_role'] == 'native-A' else args.carrier
            tree = git(args.root, 'rev-parse', commit + ':' + product['root'])
            products.append({**product, 'commit': commit, 'subtree_tree': tree})
            for tag in [f'{namespace}/v{VERSION}', f'{namespace}/v{LINE}']:
                ref = 'refs/tags/' + tag
                immutable = tag.endswith('-rc.2')
                previous = '' if immutable else remote[ref]
                if ref == f'refs/tags/specification_methodology/v{VERSION}':
                    obj = git(args.root, 'rev-parse', ref)
                    if git(args.root, 'cat-file', '-t', obj) != 'tag' or git(args.root, 'rev-parse', ref + '^{commit}') != args.native:
                        raise ValueError('Native local cut differs')
                    updates.append(f'verify {ref} {obj}')
                else:
                    message = (f'STDO {VERSION} {namespace}\n\nSTDO-Product-Subtree: {product["root"]}\n'
                               f'STDO-Product-Tree: {tree}\nSTDO-Native-Commit: {args.native}\n'
                               'STDO-Cohort-Profile: rc-six-product-v1\n')
                    obj = tag_object(args.root, tag, commit, message)
                    updates.append(f'create {ref} {obj}' if immutable else f'update {ref} {obj} {previous}')
                rows.append({'destination': ref, 'source': ref, 'object': obj, 'commit': commit,
                             'immutable': immutable, 'expected_remote': previous})
            for kind in ['rc', 'release']:
                ref = f'refs/heads/{kind}/{namespace}/{LINE}'
                updates.append(f'update {ref} {commit} {remote[ref]}')
                rows.append({'destination': ref, 'source': ref, 'object': commit,
                             'commit': commit, 'immutable': False, 'expected_remote': remote[ref]})
        updates.extend(['prepare', 'commit'])
        subprocess.run(['git', '-C', str(args.root), 'update-ref', '--stdin'],
                       input='\n'.join(updates) + '\n', text=True, capture_output=True, check=True)
        plan = {'kind': 'stdo.atomic-ref-transaction/1', 'version': VERSION,
                'products': products, 'refs': rows, 'protected_predecessor_refs': protected,
                'qualified_files': qualification['qualified_files'] +
                    [{'path': str(args.qualification.resolve()),
                      'sha256': hashlib.sha256(args.qualification.read_bytes()).hexdigest()}]}
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
        for ref, obj in plan['protected_predecessor_refs'].items():
            if after.get(ref) != obj:
                raise ValueError('Predecessor changed after publication: ' + ref)
        result['remote_readback_valid'] = True
    write(args.result, result)
    print(json.dumps({k: v for k, v in result.items() if k not in ['argv', 'stdout', 'stderr']}))


if __name__ == '__main__':
    main()
