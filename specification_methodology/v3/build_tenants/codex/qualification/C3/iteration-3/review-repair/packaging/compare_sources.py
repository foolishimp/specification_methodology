"""Measure fixed deciding-source coordinates in both admitted baselines."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
PREFIX = str(TENANT.relative_to(REPO)) + '/successor/'
OLD = '3ad1fca31dc93ba0847bbbbf308312a554daa1f6'
MANIFEST = '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782'
LOCATORS = {
    'intake': ('SPEC_METHOD.md', 'universal-intake-triage'),
    'computed-treatment': ('SPEC_METHOD.md', 'computed-classification-and-treatment'),
    'complete-transition': ('SPEC_METHOD.md', 'complete-enclosing-relation-admission-stdo-up-021'),
    'work-admission': ('TICKET_METHOD.md', 'execution-contract-admission'),
    'work-closure': ('TICKET_METHOD.md', 'condition-based-closure-and-reuse'),
    'release-qualification': ('RELEASE_METHOD.md', 'exact-cut-qualification'),
}


def sha(value):
    return hashlib.sha256(value).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    if subprocess.check_output(['git', 'rev-parse', args.source_commit + '^{commit}'], cwd=REPO, text=True).strip() != args.source_commit:
        raise ValueError('Require full immutable source commit')
    install = Path.home() / 'Library/Application Support/STDO/releases/v2.5.1-rc.2'
    if sha((install / 'manifest.json').read_bytes()) != MANIFEST:
        raise ValueError('Installed comparison manifest drift')
    pins = {r['path']: r['sha256'] for r in json.loads((install / 'manifest.json').read_text())['standards']['members']}
    reader = HERE.parents[1] / 'use-r2/harness/acquire.py'
    spec = importlib.util.spec_from_file_location('comparison_section_parser', reader)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    rows = []
    for case, (name, anchor) in LOCATORS.items():
        row = {'case': case, 'locator': 'standards/' + name + '#' + anchor, 'subjects': {}}
        for subject, commit in [('rc2', None), ('previous_candidate', OLD), ('repaired_candidate', args.source_commit)]:
            if commit:
                data = subprocess.check_output(['git', 'show', commit + ':' + PREFIX + 'standards/' + name], cwd=REPO)
            else:
                data = (install / 'standards' / name).read_bytes()
                if sha(data) != pins[name]:
                    raise ValueError('Installed comparison member drift: ' + name)
            text, first, last = module.section(data.decode(), anchor)
            row['subjects'][subject] = {'member_sha256': sha(data), 'section_sha256': sha(text.encode()),
                                       'section_bytes': len(text.encode()), 'first_line': first, 'last_line': last}
        rows.append(row)
    report = {'kind': 'stdo.i3.fixed-subject-source-comparison', 'current_commit': args.source_commit,
              'previous_commit': OLD, 'installed_basis': 'stdo://releases/v2.5.1-rc.2/',
              'manifest_sha256': MANIFEST, 'rows': rows,
              'scope': 'Named consumer fragments only; shared/conditional dependency acquisition, semantic equivalence and actor performance require their own evidence.',
              'claims': ['Source bytes are not interpretation effort.', 'No whole-method efficiency or practical superiority conclusion.']}
    (HERE / 'SOURCE_COMPARISON.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps([{'case': x['case'], 'bytes': {k: v['section_bytes'] for k, v in x['subjects'].items()}} for x in rows], indent=2))


if __name__ == '__main__':
    main()
