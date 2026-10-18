"""Prepare exact equal-condition source fixtures; refuse an existing trial arm."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
USE = HERE.parent
TENANT = USE.parents[3]
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
PREFIX = 'specification_methodology/v3/build_tenants/codex/successor/'
PREVIOUS = '3ad1fca31dc93ba0847bbbbf308312a554daa1f6'
MANIFEST = '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
TASK_SHA = 'd6f7bcba133228ae74c3b54f0055696da191fb697b5151070049566c3baaa559'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=REPO)


def git_members(commit):
    resolved = subprocess.check_output(['git', 'rev-parse', commit + '^{commit}'], cwd=REPO, text=True).strip()
    if resolved != commit:
        raise ValueError('Require full immutable source commit')
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit, '--', PREFIX], cwd=REPO, text=True).splitlines()
    if not names:
        raise ValueError('No package members at selected source')
    return {p[len(PREFIX):]: git_bytes(commit, p) for p in names}


def installed_members(root):
    data = (root / 'manifest.json').read_bytes()
    if sha(data) != MANIFEST:
        raise ValueError('Installed manifest differs')
    manifest = json.loads(data)
    rows = [{'path': 'standards/' + p['path'], 'sha256': p['sha256']} for p in manifest['standards']['members']]
    rows += [{'path': 'plugins/spec/' + p['path'], 'sha256': p['sha256']} for p in manifest['auxiliary']['plugin']['members']]
    rows.append(manifest['auxiliary']['license'])
    release_note = manifest['auxiliary']['release_note']
    rows.append({'path': release_note['installed_path'], 'sha256': release_note['sha256']})
    result = {}
    for member in rows:
        value = (root / member['path']).read_bytes()
        if sha(value) != member['sha256']:
            raise ValueError('Installed source differs: ' + member['path'])
        result[member['path']] = value
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new-commit', required=True)
    args = parser.parse_args()
    packet = (USE / 'oracle/attempt-02/ACTOR_TASKS.json').read_bytes()
    if sha(packet) != TASK_SHA:
        raise ValueError('Oracle actor packet differs')
    inputs = {
        'A': ({'kind': 'installed', 'basis': 'stdo://releases/v2.5.1-rc.2/', 'manifest_sha256': MANIFEST}, installed_members(Path.home() / 'Library/Application Support/STDO/releases/v2.5.1-rc.2')),
        'B': ({'kind': 'frozen_source', 'commit': PREVIOUS, 'prefix': PREFIX}, git_members(PREVIOUS)),
        'C': ({'kind': 'frozen_source', 'commit': args.new_commit, 'prefix': PREFIX}, git_members(args.new_commit)),
    }
    if any((USE / 'arms' / arm).exists() for arm in inputs):
        raise ValueError('Existing trial arm: preserve it; select a successor run before retry')
    root = Path(tempfile.mkdtemp(prefix='stdo-i3-use-')).resolve()
    boundary = ('The installed rc.2 process governs this assessment. Apply the selected frozen method subject to the identical synthetic work via its ordinary source entry. '
                'Read-only verified subject acquisition is supplied here. A source candidate is not an installed operative v3 release; do not substitute it as the builder or claim native-host installation. '
                'All effect permissions in task fixtures concern simulated decisions only. Actual writes are limited to this arm result territory and automatic acquisition logs. '
                'The construction task is a bounded matched exercise, not the separately reserved categorical steel-thread qualification.')
    for arm, (identity, members) in inputs.items():
        target = root / arm
        for name, data in members.items():
            path = target / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            path.chmod(0o444)
        out = USE / 'arms' / arm
        (out / 'result').mkdir(parents=True)
        (out / 'ACTOR_TASKS.json').write_bytes(packet)
        prompt = (HERE / 'ACTOR_PROMPT.md').read_text().replace('{{ARM}}', arm).replace('{{READER}}', str(HERE / 'acquire.py')).replace('{{RESULT}}', str(out / 'result'))
        (out / 'ACTOR_PROMPT.md').write_text(prompt)
        activation = {'activation': 'I3-R2-MATCHED-USE-01', 'arm': arm, 'prepared_utc': datetime.now(timezone.utc).isoformat(),
                      'source': {'identity': identity, 'materialized_root': str(target), 'members': [{'path': p, 'sha256': sha(b), 'bytes': len(b)} for p,b in sorted(members.items())]},
                      'ordinary_entry': 'plugins/spec/skills/stdo-work/SKILL.md', 'task_sha256': TASK_SHA, 'assessment_boundary': boundary,
                      'limits': {'pass': 'one initial six-task pass; no untriaged retry', 'external_paid_calls': 'not selected', 'retained_context_or_platform_budget': 'uninstrumented; do not infer fit', 'within_arm_context': 'one fresh actor, reused across tasks'},
                      'reader': str(HERE / 'acquire.py')}
        activation['actor_prompt_sha256'] = sha(prompt.encode())
        activation['actor_prompt_boundary'] = 'The explicit trial task message; inherited platform instructions and host context are not measured.'
        (out / 'ACTIVATION.json').write_text(json.dumps(activation, indent=2) + '\n')
    print(json.dumps({'arms': ['A','B','C'], 'source_root': str(root), 'new_commit': args.new_commit, 'task_sha256': TASK_SHA}, indent=2))


if __name__ == '__main__':
    main()
