"""RC4 coordinates for the existing source, account and package operations.

Only the selected output directory and authenticated inputs change. Historical
helpers and receipts remain immutable. Run each phase against a frozen commit.
"""
import argparse
import importlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[3]
PRIOR = TENANT / 'qualification/C3/rc1/content-repair/integration'
spec = importlib.util.spec_from_file_location('rc4_existing_operations', PRIOR / 'integrate.py')
operations = importlib.util.module_from_spec(spec)
spec.loader.exec_module(operations)
rc1 = operations.rc1
INPUTS = rc1.read(HERE / 'INPUTS.json')
operations.HERE, operations.PRIOR, operations.INPUTS = HERE, PRIOR, INPUTS
rc1.HERE, rc1.INPUTS = HERE, INPUTS


def selected_helpers():
    for relative, pin in INPUTS['operation_helpers'].items():
        raw = rc1.authenticate(INPUTS['helper_commit'], TENANT / relative)
        if rc1.sha(raw) != pin:
            raise ValueError('Unselected operation helper: ' + relative)
    return rc1.modules()


def conservation(args, context):
    operations.conservation(args, context)
    # An author comparison is a semantic statement, separate from refreshed
    # coordinates. Apply only explicit Writer-authored comparison updates.
    changes = json.loads(rc1.authenticate(args.source_commit, HERE / 'CONSERVATION_CHANGES.json'))
    account = rc1.read(HERE / 'CONSERVATION.json')
    rows = {row['id']: row for row in account['rows']}
    for update in changes['updates']:
        if 'author_comparison' not in update:
            continue
        row = rows[update['id']]
        row['author_comparison_history'] = [*row.get('author_comparison_history', []),
                                             row.get('author_comparison', {})]
        comparison = dict(update['author_comparison'])
        comparison['source_commit'] = args.source_commit
        comparison['candidate_assessed_commit'] = args.source_commit
        comparison['successor_sha256'] = row['successor_sha256']
        comparison['candidate_section_sha256'] = row['successor_sha256']
        comparison['standing'] = 'author_comparison_not_independent_acceptance'
        row['author_comparison'] = comparison
    parser = context.library('iteration-3/check_conservation.py')
    account['semantic_sha256'] = parser.semantic_sha(account)
    rc1.write(HERE / 'CONSERVATION.json', account)
    rc1.write(HERE / 'FRONTIER.json', parser.frontier_for(account))


def verify(args, context, build):
    operations.verify(args, context, build)
    # The inherited checker protects earlier phases. RC4 also protects the
    # entire preceding content-repair record, which is now historical input.
    subprocess.run(['git', 'diff', '--exit-code', INPUTS['starting_tenant'],
                    args.package_commit, '--', str(PRIOR.parent.relative_to(rc1.REPO))],
                   cwd=rc1.REPO, check=True, stdout=subprocess.PIPE)
    for relative in ['plugins/spec/.claude-plugin/plugin.json',
                     'plugins/spec/.codex-plugin/plugin.json']:
        manifest = json.loads(rc1.authenticate(args.package_commit, rc1.PACKAGE / relative))
        if manifest['version'] != INPUTS['candidate_version']:
            raise ValueError('Candidate manifest differs: ' + relative)
    inventory = rc1.read(HERE / 'CANDIDATE.json')
    inventory.update(kind='stdo.rc4.review-candidate',
                     candidate_version=INPUTS['candidate_version'],
                     standing='Unaccepted, unpublished review candidate.')
    rc1.write(HERE / 'CANDIDATE.json', inventory)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['source', 'account', 'generate', 'verify'])
    for field in ['source-commit', 'account-commit', 'package-commit']:
        parser.add_argument('--' + field)
    parser.add_argument('--theory-root', type=Path)
    args = parser.parse_args()
    context, build = selected_helpers()
    if args.operation == 'source':
        operations.source(args, context, build)
    elif args.operation == 'account':
        operations.account(args, context, build)
    elif args.operation == 'generate':
        operations.authored_inputs(args.source_commit)
        rc1.bind_account(args, build)
        rc1.invoke(importlib.import_module('generate_interpretation'),
                   ['--source-commit', args.source_commit, '--account-commit', args.account_commit,
                    '--theory-root', str(args.theory_root)])
        conservation(args, context)
    else:
        verify(args, context, build)


if __name__ == '__main__':
    main()
