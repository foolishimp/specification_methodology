"""Root-selected final Q12 removal fixture, consuming shipped procedures only."""
import json
from pathlib import Path
import subprocess

from finish_installation import snapshot
from prepare_lifecycle import QUAL, HERE, PYTHON, sha, pin, save


def main():
    lane = 'claude-installation-update-repair-2'
    freeze = HERE/'installations-repair-2/claude'
    captured = QUAL/'results'/lane
    assert sha(captured/'INVENTORY.json') == 'f6cefeb7799e544ab3c1f5d05d0fbbc85a1c833861acd014916b9b3dc639d5d4'
    assert not (freeze/'REMOVAL-CUSTODY.json').exists()
    census = json.loads((captured/'CENSUS.json').read_text())
    assert census['native_process']['returncode'] == 0 and census['native_process']['failure'] is None
    workspace = Path(census['original_workspace'])
    before = snapshot(workspace)
    assert {p: v['sha256'] for p, v in before.items() if v['kind'] == 'file'} == census['workspace']['after']
    assert not any(v['kind'] == 'symlink' for v in before.values())
    codex = HERE/'installations/codex/retained-packages/source-old'
    assert sha(codex/'inventory.json') == '337d274efde96147c8e9a2db3e3b25f7631731fc8486562c9022ad087833aa36'
    calls = []

    def run(argv):
        result = subprocess.run([str(x) for x in argv], capture_output=True, text=True)
        value = {'argv': [str(x) for x in argv], 'returncode': result.returncode,
                 'stdout': result.stdout, 'stderr': result.stderr}
        calls.append(value)
        save(freeze/'removal-operations'/f'{len(calls):02d}.json', value)
        assert result.returncode == 0, value

    target = workspace/'.agents/skills/stdo-work'
    run([PYTHON, '-B', codex/'tests/verify_package.py', codex, '--destination', target])
    run(['/bin/cp', '-R', codex/'skills/stdo-work', target])
    run([PYTHON, '-B', codex/'tests/verify_package.py', codex, '--installed', target])
    both = snapshot(workspace)
    assert all(both.get(path) == row for path, row in before.items())
    assert all(p == '.agents/skills/stdo-work' or p.startswith('.agents/skills/stdo-work/') for p in set(both)-set(before))
    save(freeze/'BOTH-TENANTS-BEFORE-REMOVAL.json', {'workspace': str(workspace), 'entries': both})
    selection = json.loads((QUAL/'selections'/f'{lane}.json').read_text())
    receipt_path = workspace/'.claude/stdo-skills-claude.receipt.json'
    expected_receipt = selection['install_binding']['receipt_sha256']
    assert sha(receipt_path) == expected_receipt
    receipt = json.loads(receipt_path.read_text())
    assert receipt['source_inventory_sha256'] == '33472e5e2b9adf5ba616bd6980d7f84b3c10de168968727919de32378f045704'
    for skill, value in receipt['skills'].items():
        for relative, digest in value['files'].items():
            assert sha(workspace/'.claude/skills'/skill/relative) == digest
    helper = workspace/'.claude/skills/stdo-release-install/scripts/manage_install.py'
    assert sha(helper) == 'c10608336639fcf6ed87443666dab5e7ca79d3cc84df2f7a80b6ef33c603fabe'
    run([PYTHON, '-I', '-B', helper, 'remove', '--workspace', workspace,
         '--receipt-sha256', expected_receipt])
    owned_prefixes = ['.claude/skills/'+name for name in receipt['skills']]
    def owned(path):
        return path == '.claude/stdo-skills-claude.receipt.json' or any(path == p or path.startswith(p+'/') for p in owned_prefixes)
    after = snapshot(workspace)
    assert not any(owned(p) for p in after)
    assert after == {p: v for p, v in both.items() if not owned(p)}
    save(freeze/'REMOVAL-CUSTODY.json', {
        'schema': 'stdo_skills.actual-removal-custody/1',
        'tenant_removed': 'claude', 'candidate_inventory': receipt['source_inventory_sha256'],
        'other_tenant_preserved': 'codex', 'other_inventory': pin(codex/'inventory.json'),
        'root_selection': 'Root consumed repaired Q12 actual result and all eight Bash commands; selected exact other-tenant install and scoped current Claude removal, preserving original LC-01 and S4 count limit. No actor rerun or candidate edit.',
        'captured_native_invocation': pin(captured/'INVENTORY.json'),
        'native_assessment': pin(HERE/'assessments/claude-installation-update-repair-2.json'),
        'driver': pin(Path(__file__)), 'snapshot_driver': pin(HERE/'finish_installation.py'),
        'before_other_install': before, 'before_target_removal': both,
        'receipt_sha256': expected_receipt, 'actual_operations': calls,
        'after_target_removal': after, 'removed_entries': sorted(set(both)-set(after)),
        'standing': 'Only five owned Claude directories and receipt removed by shipped helper. Exact Codex package, both configurations, unrelated skills, greeting and source retained. Host evidence was captured while selected skill bodies existed.',
        'limits': ['Finite cooperative exclusive-access lifecycle witness; no concurrency/crash-atomic or whole-method claim.']})
    print(json.dumps(pin(freeze/'REMOVAL-CUSTODY.json')))


if __name__ == '__main__':
    main()
