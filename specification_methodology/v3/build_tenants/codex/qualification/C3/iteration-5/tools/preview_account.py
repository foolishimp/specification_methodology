"""Check selected authored patches in a temporary source fixture before freeze.

All unselected owner bytes come from the exact I4 preimage. This writes a scoped
preview receipt only; it never generates current DETERMINATIONS or publication.
"""
import argparse
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile

import build_interpretation as build
from reconcile_account import integrate, validate_patch
from context import HERE, PRIOR, PACKAGE, REPO, INPUTS, git_bytes, sha, write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--patch', action='append', required=True, help='I5-relative source/.../ACCOUNT_PATCH.json')
    parser.add_argument('--output', default='PATCH_PREVIEW.json', help='Filename under I5/interpretation/')
    args = parser.parse_args()
    if Path(args.output).name != args.output:
        raise ValueError('Preview output must be a filename in interpretation/')
    patches, pins = [], []
    for relative in args.patch:
        if Path(relative).is_absolute() or '..' in Path(relative).parts or not relative.startswith('source/'):
            raise ValueError('Expected an I5 source return')
        raw = (HERE / relative).read_bytes()
        patch = json.loads(raw); validate_patch(patch)
        patches.append(patch); pins.append({'path': relative, 'sha256': sha(raw)})
    prior_raw = git_bytes(INPUTS['prior_account_commit'], (PRIOR / 'DETERMINATIONS.json').relative_to(REPO))
    prior = json.loads(prior_raw)
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    paths |= {path for patch in patches for path in patch['owner_paths']}
    prefix = str(PACKAGE.relative_to(REPO)) + '/'
    archive = subprocess.check_output(['git', 'archive', INPUTS['starting_tenant'], prefix], cwd=REPO)
    with tarfile.open(fileobj=io.BytesIO(archive)) as source_archive:
        old = {path: source_archive.extractfile(prefix + path).read() for path in paths}
    source = dict(old)
    for patch in patches:
        for path in patch['owner_paths']:
            source[path] = (PACKAGE / path).read_bytes()
    account, report = integrate(prior, old, source, patches, 'unfrozen-preview-fixture')
    current, _ = build.semantic_projection(account)
    directory = HERE / 'interpretation'; directory.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='patch-preview-', dir=directory) as name:
        root = Path(name)
        for path, raw in source.items():
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_bytes(raw)
        previous = build.PACKAGE
        try:
            build.PACKAGE = root
            build.validate_account(current, package=root)
        finally:
            build.PACKAGE = previous
    result = {'kind': 'stdo.i5.account-preview', 'valid': True,
              'common_input': INPUTS['common_input'], 'source_preimage': INPUTS['starting_tenant'],
              'prior_account_sha256': sha(prior_raw), 'patches': pins,
              'selected_source_sha256': {p: sha(source[p]) for patch in patches for p in patch['owner_paths']},
              'tool_sha256': {p: sha((Path(__file__).parent / p).read_bytes())
                              for p in ['preview_account.py', 'reconcile_account.py', 'account_protocol.py', 'build_interpretation.py', 'context.py']},
              'rows': len(current['determinations']), 'new_rows': report['new_rows'],
              'updated_rows': [p['id'] for p in report['direct_patches']],
              'changed_support_requiring_assessment': report['changed_support_requiring_assessment'],
              'standing': 'Authored protocol, source-pin and reference compatibility only; no semantic fidelity or current publication.'}
    write(directory / args.output, result)
    print(json.dumps({k: result[k] for k in ['valid', 'patches', 'rows', 'new_rows', 'standing']}))


if __name__ == '__main__':
    main()
