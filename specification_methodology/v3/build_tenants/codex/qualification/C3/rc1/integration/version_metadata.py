"""Bind the selected RC1 manifest metadata successor to unchanged semantics."""
import argparse
import copy
import json
from pathlib import Path
import subprocess
import rc1

FIRST_SOURCE = 'ed940de64f787d05c919efd1a2c45c5e1ef31685'
FIRST_ACCOUNT = '1553243d620fc0faf045b17dd98b9ed4ea8cea43'
FIRST_PACKAGE = 'a485db611ab9af8cd6154f96b0e4ca6db6e5e605'
FIRST_CHECK = 'ba547177d7c9f2977fd48fa025618264f913a00a'
GRANT = 'e0fab2931f2962e518ecacdc79e946c5139649c6'
MANIFESTS = ['plugins/spec/.claude-plugin/plugin.json',
             'plugins/spec/.codex-plugin/plugin.json']


def source(args, context, build):
    build.documentary_inventory(FIRST_SOURCE)
    changes = []
    for name in MANIFESTS:
        path = rc1.PACKAGE / name
        before = rc1.authenticate(FIRST_PACKAGE, path)
        value = json.loads(before)
        if value['version'] != '3.0.0' or before.count(b'"version": "3.0.0"') != 1:
            raise ValueError('Different manifest version preimage: ' + name)
        after = before.replace(b'"version": "3.0.0"', b'"version": "3.0.0-rc.1"')
        expected = copy.deepcopy(value)
        expected['version'] = '3.0.0-rc.1'
        if json.loads(after) != expected:
            raise ValueError('Manifest changed beyond version: ' + name)
        path.write_bytes(after)
        changes.append({'path': name, 'before_sha256': rc1.sha(before),
                        'sha256': rc1.sha(after), 'before': '3.0.0', 'after': '3.0.0-rc.1'})
    rc1.write(rc1.HERE / 'VERSION_SELECTION.json', {
        'kind': 'stdo.rc1.candidate-version-selection', 'grant_commit': GRANT,
        'prior_source': FIRST_SOURCE, 'prior_account': FIRST_ACCOUNT,
        'prior_package': FIRST_PACKAGE, 'prior_check_commit': FIRST_CHECK,
        'changes': changes, 'standing': 'Candidate metadata; no publication, selection or acceptance.'})


def account(args, context, build):
    commit, inventory = build.documentary_inventory(rc1.exact(args.source_commit))
    prior_raw = rc1.authenticate(FIRST_ACCOUNT, rc1.HERE / 'DETERMINATIONS.json')
    prior = json.loads(prior_raw)
    paths = {r['owner']['path'] for r in prior['determinations']}
    paths |= {s['path'] for r in prior['determinations'] for s in r.get('supporting_sources', [])}
    if paths.intersection(MANIFESTS):
        raise ValueError('Metadata changes an authored owner or supporting source')
    old_members = {m['path']: m for m in prior['source_members']}
    new_members = {m['path']: m for m in inventory}
    changed = sorted(p for p in old_members.keys() | new_members.keys()
                     if old_members.get(p) != new_members.get(p))
    if changed != sorted(MANIFESTS):
        raise ValueError('Documentary change exceeds selected metadata: ' + repr(changed))
    for path in paths:
        if rc1.frozen(FIRST_SOURCE, rc1.PACKAGE / path) != (rc1.PACKAGE / path).read_bytes():
            raise ValueError('Authored source changed: ' + path)
    result = copy.deepcopy(prior)
    result['subject']['source_commit'] = commit
    result['source_members'] = inventory
    if build.semantic_projection(result) != build.semantic_projection(prior):
        raise ValueError('Metadata rebinding changed the authored meaning')
    rc1.write(rc1.HERE / 'DETERMINATIONS.json', result)
    rc1.write(rc1.HERE / 'VERSION_ACCOUNT.json', {
        'kind': 'stdo.rc1.version-account-rebinding', 'source_commit': commit,
        'prior_source_commit': FIRST_SOURCE, 'prior_account_commit': FIRST_ACCOUNT,
        'prior_account_sha256': rc1.sha(prior_raw), 'changed_members': changed,
        'authenticated_owner_and_support_members': len(paths),
        'determinations_unchanged': True, 'semantic_projection_unchanged': True,
        'standing': 'Documentary membership and current subject rebound. Unchanged authored rows retain their exact valid source provenance and prior evidence limits.'})


def verify(args, context, build):
    account = rc1.bind_account(args, build)
    rc1.authenticate(args.package_commit, Path(__file__))
    selection = json.loads(rc1.authenticate(args.source_commit, rc1.HERE / 'VERSION_SELECTION.json'))
    rc1.authenticate(args.account_commit, rc1.HERE / 'VERSION_ACCOUNT.json')
    prior = json.loads(rc1.frozen(FIRST_ACCOUNT, rc1.HERE / 'DETERMINATIONS.json'))
    if account['determinations'] != prior['determinations'] or build.semantic_projection(account) != build.semantic_projection(prior):
        raise ValueError('Metadata successor changed account meaning or consumer evidence')
    current, _ = build.semantic_projection(account)
    if current != rc1.read(rc1.PACKAGE / 'interpretation/source-account.json'):
        raise ValueError('Generated semantic account differs')
    generation = json.loads(rc1.authenticate(args.package_commit, rc1.HERE / 'interpretation/GENERATION.json'))
    if (generation['document_source_input_commit'] != args.source_commit or
            generation['account_input_commit'] != args.account_commit or generation['native_validation'] != 'passed'):
        raise ValueError('Generation lacks the current exact coordinates or validation')
    for name in ['validation.json', 'DEPENDENCY_VERIFICATION.json', 'QUALIFICATION_EQUIVALENCE.json']:
        rc1.authenticate(args.package_commit, rc1.HERE / 'interpretation' / name)
    members = context.members()
    prefix = str(rc1.PACKAGE.relative_to(rc1.REPO)) + '/'
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', args.package_commit,
                                     '--', str(rc1.PACKAGE.relative_to(rc1.REPO))], cwd=rc1.REPO, text=True).splitlines()
    if {n[len(prefix):] for n in names} != {m['path'] for m in members}:
        raise ValueError('Final package membership differs from freeze')
    changed = []
    for member in members:
        path = rc1.PACKAGE / member['path']
        raw = rc1.authenticate(args.package_commit, path)
        if raw != rc1.frozen(FIRST_PACKAGE, path):
            changed.append(member['path'])
    expected_changes = set(MANIFESTS + ['interpretation/MAPPING.json', 'interpretation/SOURCE_INVENTORY.json'])
    if set(changed) != expected_changes:
        raise ValueError('Metadata successor has unexpected package changes: ' + repr(changed))
    for name in MANIFESTS:
        before = json.loads(rc1.frozen(FIRST_PACKAGE, rc1.PACKAGE / name))
        after = rc1.read(rc1.PACKAGE / name)
        before['version'] = '3.0.0-rc.1'
        if before != after:
            raise ValueError('Manifest changed beyond version: ' + name)
    reuse = {}
    for name in ['CHANGED_SCOPE.json', 'ARTIFACT_CHECK.json', 'IDENTITY_CHECK.json',
                 'CONSERVATION_APPLICABILITY.json', 'FRONTIER.json', 'CONSUMER_RELATIONS.json']:
        raw = rc1.authenticate(FIRST_CHECK, rc1.HERE / name)
        reuse[name] = {'commit': FIRST_CHECK, 'sha256': rc1.sha(raw), 'subject': FIRST_PACKAGE}
    prior_check = rc1.read(rc1.HERE / 'CHANGED_SCOPE.json')
    if prior_check['writer_result'] != 'satisfied':
        raise ValueError('No satisfied construction check to reuse')
    checkpoints = [args.source_commit, args.account_commit, args.package_commit]
    allowed = [str(rc1.HERE.relative_to(rc1.REPO)) + '/', prefix + 'interpretation/']
    exact_paths = {prefix + p for p in MANIFESTS}
    changed_paths = set()
    for checkpoint in checkpoints:
        paths = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', checkpoint], cwd=rc1.REPO, text=True).splitlines()
        if any(p not in exact_paths and not any(p.startswith(a) for a in allowed) for p in paths):
            raise ValueError('Metadata checkpoint escaped granted territory')
        changed_paths.update(paths)
    rc1.write(rc1.HERE / 'CANDIDATE.json', {'kind': 'stdo.rc1.candidate-inventory', 'schema_version': 1,
        'common_input': rc1.INPUTS['common_input'], 'document_source_commit': args.source_commit,
        'account_commit': args.account_commit, 'package_commit': args.package_commit,
        'members': members, 'standing': 'Complete construction inventory; qualification and owner decisions remain open.'})
    rc1.write(rc1.HERE / 'METADATA_CHECK.json', {'kind': 'stdo.rc1.metadata-successor-check',
        'source_commit': args.source_commit, 'account_commit': args.account_commit,
        'package_commit': args.package_commit, 'grant_commit': selection['grant_commit'],
        'writer_result': 'satisfied', 'members': len(members), 'changed_package_members': changed,
        'writer_checkpoints': checkpoints, 'changed_paths': sorted(changed_paths),
        'determinations_unchanged': True, 'semantic_projection_unchanged': True,
        'all_standards_frames_identity_and_executable_interpretation_unchanged': True,
        'native_generation_validation': generation['native_validation'], 'reused_evidence': reuse,
        'reuse_boundary': 'Exact unchanged subjects retain only their earlier supported scope. Native validation binds the successor; no semantic discriminator or cold identity suite repeated. Conservation applicability and all 11 unmatched positives retain their explicit limits.',
        'standing': 'Writer construction check, not independent qualification or acceptance.'})
    print(json.dumps({'writer_result': 'satisfied', 'members': len(members), 'changed_package_members': changed,
                      'semantic_projection_unchanged': True, 'prior_check_commit': FIRST_CHECK}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['source', 'account', 'verify'])
    parser.add_argument('--source-commit')
    parser.add_argument('--account-commit')
    parser.add_argument('--package-commit')
    parser.add_argument('--coordinates', type=Path)
    args = parser.parse_args()
    if args.coordinates:
        coordinates = rc1.read(args.coordinates)
        for field in ['source_commit', 'account_commit', 'package_commit']:
            if getattr(args, field) and getattr(args, field) != coordinates[field]:
                raise ValueError('Conflicting recorded coordinate: ' + field)
            setattr(args, field, coordinates[field])
    context, build = rc1.modules()
    {'source': source, 'account': account, 'verify': verify}[args.operation](args, context, build)


if __name__ == '__main__':
    main()
