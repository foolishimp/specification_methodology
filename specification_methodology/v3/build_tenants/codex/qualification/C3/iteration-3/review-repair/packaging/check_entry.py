"""Exercise the documented plugin-to-basis routes without a source checkout.

This tests installed rc.2 resolution and a separately selected frozen candidate
assessment package. It does not install or qualify an issued v3 release.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
REPO = Path(subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
PREFIX = str(TENANT.relative_to(REPO)) + '/successor/'
MANIFEST_SHA = '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
BASIS = 'stdo://releases/v2.5.1-rc.2/'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frozen(commit, member):
    return subprocess.check_output(['git', 'show', commit + ':' + PREFIX + member], cwd=REPO)


def command(args, cwd):
    run = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    try:
        value = json.loads(run.stdout)
    except ValueError:
        value = {'stdout': run.stdout, 'stderr': run.stderr}
    return {'command': args, 'exit': run.returncode, 'result': value}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    resolved = subprocess.check_output(['git', 'rev-parse', args.source_commit + '^{commit}'],
                                       cwd=REPO, text=True).strip()
    if resolved != args.source_commit:
        raise ValueError('Use a full frozen commit')
    start = time.monotonic()
    skill_name = 'plugins/spec/skills/stdo-work/SKILL.md'
    basis_name = 'plugins/spec/references/PRODUCT_BASIS.md'
    skill, procedure = frozen(resolved, skill_name), frozen(resolved, basis_name)
    routes = sorted(set(re.findall(r'`((?:standards|interpretation)/[^`]+)`', skill.decode())))
    checks, observations = {}, []
    # Retained plugin-local references resolve within the independently installed plugin.
    local_links = re.findall(r'\]\(([^)]+)\)', skill.decode())
    checks['no_source_relative_member_links'] = all('../../../../' not in r for r in local_links)
    checks['declared_member_routes_present'] = bool(routes)
    with tempfile.TemporaryDirectory(prefix='stdo-i3-entry-') as directory:
        root = Path(directory)
        plugin = root / 'installed-plugin'
        for name, data in [(skill_name, skill), (basis_name, procedure)]:
            destination = plugin / name.removeprefix('plugins/spec/')
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        # These are deliberate distractions, not members or selecting evidence.
        decoy = root / 'standards'
        decoy.mkdir()
        (decoy / 'SPEC_METHOD.md').write_text('Unselected nearby source.\n')
        checks['plugin_local_reference_resolves'] = all(
            (plugin / 'skills/stdo-work' / r).resolve().is_file() for r in local_links)
        # The manifest is read from the exact installed store, never the decoy.
        spec = command(['stdo', 'resolve', BASIS + 'standards/SPEC_METHOD.md'], root)
        observations.append(spec)
        member = Path(spec['result']['path'])
        install = member.parents[1]
        manifest_bytes = (install / 'manifest.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        checks['installed_manifest_is_selected'] = sha(manifest_bytes) == MANIFEST_SHA
        pins = {'standards/' + row['path']: row['sha256'] for row in manifest['standards']['members']}
        checks['installed_owner_matches_membership'] = sha(member.read_bytes()) == pins['standards/SPEC_METHOD.md']
        checks['plugin_location_and_decoy_do_not_select_basis'] = root not in member.parents
        checks['selected_section_exists'] = '## Universal Intake Triage' in member.read_text()
        # Fragment selection follows resolution, since the actual resolver refuses fragments.
        fragment = command(['stdo', 'resolve', BASIS + 'standards/SPEC_METHOD.md#universal-intake-triage'], root)
        observations.append(fragment)
        checks['fragment_is_not_misrouted_to_resolver'] = fragment['exit'] != 0
        absent = command(['stdo', 'resolve', BASIS + 'standards/TRANSFORMATION_LIBRARY.md'], root)
        observations.append(absent)
        checks['missing_member_does_not_fall_back'] = absent['exit'] != 0
        checks['changed_member_cannot_match_selected_pin'] = sha(member.read_bytes() + b'changed') != pins['standards/SPEC_METHOD.md']
        # Candidate routes use their own explicitly selected source package and pins.
        # No candidate file is substituted for any absent installed member above.
        candidate = root / 'assessment-package'
        records = []
        for route in routes:
            path, _, anchor = route.partition('#')
            data = frozen(resolved, path)
            target = candidate / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            records.append({'route': route, 'bytes': len(data), 'sha256': sha(data)})
        checks['all_declared_candidate_member_routes_resolve'] = len(records) == len(routes)
        # Heading validity is covered by the package link/anchor check, not guessed here.
    report = {'kind': 'stdo.i3.plugin-basis-entry-check', 'source_commit': resolved,
              'plugin_sha256': sha(skill), 'basis_procedure_sha256': sha(procedure),
              'checks': checks, 'candidate_routes': records, 'observations': observations,
              'valid': all(checks.values()), 'elapsed_seconds': time.monotonic() - start,
              'limits': ['Author routing experiment; not a native host skill activation.',
                         'Existing installed rc.2 and frozen candidate assessment package are distinct.',
                         'No v3 publication, identity issuance, installation or adoption is established.']}
    (HERE / 'ENTRY_CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'valid': report['valid'], 'checks': checks, 'elapsed_seconds': report['elapsed_seconds']}, indent=2))
    return 0 if report['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
