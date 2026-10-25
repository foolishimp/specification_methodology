"""Complete the separately selected post-close Q12 preservation/removal fixture.

Consumes shipped installers/verifiers and their documented scoped recipes. This
driver is not a package installer and must not run before Root reviews the closed
native invocation. It never dispatches a host or changes an actual candidate.
"""
import argparse
import json
import os
from pathlib import Path
import stat
import subprocess

from prepare_lifecycle import QUAL, HERE, PYTHON, sha, pin, save


def snapshot(root):
    result = {}
    for path in sorted(root.rglob('*')):
        info = path.lstat()
        item = {'mode': stat.S_IMODE(info.st_mode)}
        if stat.S_ISREG(info.st_mode):
            item.update(kind='file', sha256=sha(path), bytes=info.st_size)
        elif stat.S_ISDIR(info.st_mode):
            item['kind'] = 'directory'
        elif stat.S_ISLNK(info.st_mode):
            item.update(kind='symlink', target=os.readlink(path))
        else:
            raise ValueError('Unexpected special file: ' + str(path))
        result[str(path.relative_to(root))] = item
    return result


def complete(tenant, expected_capture, root_close_reference):
    freeze = HERE/'installations'/tenant
    destination = freeze/'REMOVAL-CUSTODY.json'
    if destination.exists():
        raise ValueError('Removal custody already exists; do not repeat effects')
    name = tenant+'-installation-update'
    captured = QUAL/'results'/name
    assert sha(captured/'INVENTORY.json') == expected_capture
    census = json.loads((captured/'CENSUS.json').read_text())
    assert census['native_process']['returncode'] == 0
    assert census['native_process']['failure'] is None
    assert census['native_process']['stdout_eof'] and census['native_process']['stderr_eof']
    workspace = Path(census['original_workspace'])
    current = snapshot(workspace)
    assert not any(row['kind'] == 'symlink' for row in current.values())
    assert {k: v['sha256'] for k, v in current.items() if v['kind'] == 'file'} == census['workspace']['after']
    assert (workspace/'outputs/greeting.txt').read_bytes() == b'Hello, Ada.\n'
    selected = freeze/'retained-packages/source-compatible-update'
    other = 'claude' if tenant == 'codex' else 'codex'
    preserved_package = HERE/'installations'/other/'retained-packages/source-old'
    invname = 'INVENTORY.md' if other == 'claude' else 'inventory.json'
    expected = ('42d246cbe2fcf1414b0fd7ed094be74d6f2607595525555caa52618d8999f79a'
                if other == 'claude' else '337d274efde96147c8e9a2db3e3b25f7631731fc8486562c9022ad087833aa36')
    assert sha(preserved_package/invname) == expected
    records = []

    def run(argv):
        proc = subprocess.run([str(x) for x in argv], capture_output=True, text=True)
        record = {'argv': [str(x) for x in argv], 'returncode': proc.returncode,
                  'stdout': proc.stdout, 'stderr': proc.stderr}
        records.append(record)
        # Retain each physical result before checking it; a partial failure is not
        # erased, and this driver never retries or rolls back a failed operation.
        save(freeze/'removal-operations'/f'{len(records):02d}.json', record)
        if proc.returncode != 0:
            raise ValueError('Shipped lifecycle operation failed; inspect retained operation and actual tree')
        return proc

    if other == 'claude':
        helper = preserved_package/'skills/stdo-release-install/scripts/manage_install.py'
        run([PYTHON, '-I', '-B', helper, 'install', '--package', preserved_package, '--workspace', workspace])
        other_prefixes = ['.claude/skills/'+p.name for p in (preserved_package/'skills').iterdir()]
        other_receipt = '.claude/stdo-skills-claude.receipt.json'
    else:
        verifier = preserved_package/'tests/verify_package.py'
        other_destination = workspace/'.agents/skills/stdo-work'
        run([PYTHON, '-B', verifier, preserved_package, '--destination', other_destination])
        run(['/bin/cp', '-R', preserved_package/'skills/stdo-work', other_destination])
        run([PYTHON, '-B', verifier, preserved_package, '--installed', other_destination])
        other_prefixes, other_receipt = ['.agents/skills/stdo-work'], None
    both = snapshot(workspace)
    assert all(both.get(path) == row for path, row in current.items())
    added = set(both)-set(current)
    assert all(path == other_receipt or any(path == prefix or path.startswith(prefix+'/') for prefix in other_prefixes) for path in added)
    save(freeze/'BOTH-TENANTS-BEFORE-REMOVAL.json', {'workspace': str(workspace), 'entries': both})

    if tenant == 'codex':
        unit = workspace/'.agents/skills/stdo-work'
        run([PYTHON, '-B', selected/'tests/verify_package.py', selected, '--installed', unit])
        owned_prefixes, owned_receipt = ['.agents/skills/stdo-work'], None
        run(['/bin/rm', '-r', unit])
    else:
        receipt = '.claude/stdo-skills-claude.receipt.json'
        selection = json.loads((QUAL/'selections'/f'{name}.json').read_text())
        receipt_sha = selection['install_binding']['receipt_sha256']
        assert sha(workspace/receipt) == receipt_sha
        owned_prefixes = ['.claude/skills/'+p.name for p in (selected/'skills').iterdir()]
        owned_receipt = receipt
        helper = workspace/'.claude/skills/stdo-release-install/scripts/manage_install.py'
        assert sha(helper) == 'c10608336639fcf6ed87443666dab5e7ca79d3cc84df2f7a80b6ef33c603fabe'
        run([PYTHON, '-I', '-B', helper, 'remove', '--workspace', workspace, '--receipt-sha256', receipt_sha])
    after = snapshot(workspace)
    def owned(path):
        return path == owned_receipt or any(path == prefix or path.startswith(prefix+'/') for prefix in owned_prefixes)
    assert not any(owned(path) for path in after)
    assert after == {path: row for path, row in both.items() if not owned(path)}
    save(destination, {
        'schema': 'stdo_skills.actual-removal-custody/1', 'tenant_removed': tenant,
        'other_tenant_preserved': other, 'root_close_reference': root_close_reference,
        'fixture_driver': pin(Path(__file__)),
        'captured_native_invocation': pin(captured/'INVENTORY.json'),
        'target_update_custody': pin(freeze/'UPDATE-CUSTODY.json'),
        'target_package_custody': pin(freeze/'PACKAGE-CUSTODY.json'),
        'preserved_package_custody': pin(HERE/'installations'/other/'PACKAGE-CUSTODY.json'),
        'before_other_tenant_install': current, 'before_target_removal': both,
        'actual_operations': records, 'after_target_removal': after,
        'removed_entries': sorted(set(both)-set(after)),
        'standing': 'Actual scoped removal after captured host invocation; exact other selected tenant, both host configurations, unrelated skills, outputs and source preserved. No invocation of the removed skill body is claimed.',
        'limits': ['One finite lifecycle fixture under exclusive cooperative access, not a concurrent/crash-atomic or OS-isolation guarantee.',
                   'The compatible update is a controlled metadata-only derivative, not a Product release.']})
    print(json.dumps(pin(destination)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tenant', choices=['codex', 'claude'], required=True)
    parser.add_argument('--invocation-inventory-sha256', required=True)
    parser.add_argument('--root-close-reference', required=True)
    args = parser.parse_args()
    complete(args.tenant, args.invocation_inventory_sha256, args.root_close_reference)
