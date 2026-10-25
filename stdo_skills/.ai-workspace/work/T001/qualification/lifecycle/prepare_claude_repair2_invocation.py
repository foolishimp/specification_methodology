"""Prepare one selected affected Q12 host successor; no actor dispatch.

Uses the shipped unchanged bundle helper for an actual old-to-repaired package
update. Earlier negative installer controls remain reusable evidence, rather
than being rerun. Root must supply and select the exact repaired inventory.
"""
import argparse
import json
from pathlib import Path
import shutil

from prepare_lifecycle import QUAL, HERE, PRODUCT, PYTHON, common, pin, save, sha, inventory
from prepare_installation import run


def prepare(base, selected_inventory):
    lane = 'installation-update-repair-2'
    workspace = base/'claude/workspace'
    control = base/'claude/control'
    freeze = HERE/'installations-repair-2/claude'
    package = PRODUCT/'build_tenants/claude'
    assert sha(package/'INVENTORY.md') == selected_inventory
    helper_rel = 'skills/stdo-release-install/scripts/manage_install.py'
    assert sha(package/helper_rel) == 'c10608336639fcf6ed87443666dab5e7ca79d3cc84df2f7a80b6ef33c603fabe'
    old_source = HERE/'installations/claude/retained-packages/source-old'
    assert sha(old_source/'INVENTORY.md') == '42d246cbe2fcf1414b0fd7ed094be74d6f2607595525555caa52618d8999f79a'
    # Equivalent ordinary task and permissions; no prior answer or oracle.
    prior = json.loads((HERE/'installations/claude/fixture.json').read_text())
    prior_workspace = Path(prior['workspace'])
    common(workspace, 'installed-update',
           (prior_workspace/'specification/REQUIREMENT.md').read_text(),
           (prior_workspace/'design/DESIGN.md').read_text(),
           (prior_workspace/'TASK.md').read_text(), ['outputs/greeting.txt'])
    save(workspace/'inputs/name.txt', 'Ada\n')
    save(workspace/'outputs/greeting.txt', 'Hello, Grace.\n')
    for rel in ['.agents/skills/unrelated-tool/SKILL.md',
                '.claude/skills/unrelated-tool/SKILL.md',
                '.codex/config.toml', '.claude/settings.json']:
        save(workspace/rel, (prior_workspace/rel).read_bytes())
    before = inventory(workspace)
    old = control/'source-old'
    new = control/'source-repair-2'
    shutil.copytree(old_source, old)
    shutil.copytree(package, new)
    retained = freeze/'retained-package'
    shutil.copytree(new, retained)
    assert inventory(new) == inventory(retained)
    save(freeze/'PACKAGE-CUSTODY.json', {
        'schema': 'stdo_skills.fixture-package-custody/1',
        'original_package': pin(new/'INVENTORY.md'),
        'retained_package': str(retained.relative_to(QUAL)),
        'files': inventory(retained),
    })
    records = []
    first = run([PYTHON, '-I', '-B', old/helper_rel, 'install', '--package', old,
                 '--workspace', workspace], records)
    old_receipt = json.loads(first.stdout)['receipt_sha256']
    initial = inventory(workspace)
    updated = run([PYTHON, '-I', '-B', new/helper_rel, 'update', '--package', new,
                   '--workspace', workspace, '--receipt-sha256', old_receipt], records)
    new_receipt = json.loads(updated.stdout)['receipt_sha256']
    for row in before:
        assert sha(workspace/row['path']) == row['sha256']
    custody = {
        'schema': 'stdo_skills.actual-installation-lifecycle/1', 'tenant': 'claude',
        'workspace': str(workspace), 'old_inventory': pin(old/'INVENTORY.md'),
        'new_inventory': pin(new/'INVENTORY.md'),
        'compatibility': 'Explicitly selected full-bundle successor with the same roster, method pin, installer and receipt schema; source identities are retained.',
        'initial': initial, 'records': records, 'post_update': inventory(workspace),
        'preserved_original_files': before,
        'unchanged_installer_controls': pin(HERE/'installations/claude/UPDATE-CUSTODY.json'),
        'removal': 'Not selected in this affected native invocation; prior unchanged physical removal evidence remains separate.',
    }
    save(freeze/'UPDATE-CUSTODY.json', custody)
    save(control/'ordinary-prompt.base.txt',
         'Please correct outputs/greeting.txt for inputs/name.txt under the existing requirement and design, using the current installed skill. Preserve unrelated files and both host configurations. I authorize the bounded task in TASK.md.\n')
    stable = [str(p.relative_to(workspace)) for p in sorted(workspace.rglob('*'))
              if p.is_file() and str(p.relative_to(workspace)) not in
              ['outputs/greeting.txt', '.claude/stdo-skills-claude.receipt.json']
              and not str(p.relative_to(workspace)).startswith(('.agents/skills/', '.claude/skills/'))]
    save(freeze/'INPUTS.json', {'schema': 'stdo_skills.fixture-inputs/1',
                              'workspace': str(workspace), 'files': inventory(workspace)})
    save(freeze/'fixture.json', {'schema': 'stdo_skills.qualification-fixture/1',
         'tenant': 'claude', 'lane': lane, 'workspace': str(workspace), 'control': str(control),
         'artifact_paths': ['outputs/greeting.txt'], 'stable_input_paths': stable,
         'input_manifest': pin(freeze/'INPUTS.json')})
    selected = json.loads((QUAL/'selections/claude-installation-update.json').read_text())
    selected.update(lane=lane, candidate_record=pin(new/'INVENTORY.md'),
                    tenant_root=str(new), package_root=str(new/'skills'),
                    install_documentation=pin(new/'INSTALL.md'),
                    package_files=[{'path': str(p.relative_to(new/'skills')), 'sha256': sha(p)}
                                   for p in sorted((new/'skills').rglob('*')) if p.is_file()],
                    fixture_record=pin(freeze/'fixture.json'), timeout_ms=600000,
                    install_binding={'kind': 'claude-bundle-installer/1',
                       'action': 'verified-existing', 'helper': pin(new/helper_rel),
                       'receipt_sha256': new_receipt, 'custody': pin(freeze/'UPDATE-CUSTODY.json')},
                    install_checks={'before': [], 'after': []})
    path = QUAL/'selections'/('claude-'+lane+'.json')
    save(path, selected)
    print(json.dumps({'selection': pin(path), 'custody': pin(freeze/'UPDATE-CUSTODY.json'),
                      'fixture': pin(freeze/'fixture.json')}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--inventory-sha256', required=True)
    args = parser.parse_args()
    prepare(args.base.resolve(), args.inventory_sha256)
