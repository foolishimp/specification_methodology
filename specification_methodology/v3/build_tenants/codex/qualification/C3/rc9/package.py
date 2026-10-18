"""Bind and check the RC9 label change without regenerating method meaning.

Run from any directory with the installed STDO toolchain Python. The existing
package checker is reused with its outputs confined to this RC9 directory.
"""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / 'successor'
REPO = TENANT.parents[3]
INPUTS = json.loads((HERE / 'INPUTS.json').read_text())
PREVIOUS = INPUTS['prior_package_commit']
LABELS = ['README.md', 'plugins/spec/.claude-plugin/plugin.json',
          'plugins/spec/.codex-plugin/plugin.json']
REBIND = ['interpretation/MAPPING.json', 'interpretation/SOURCE_INVENTORY.json']
sys.path.insert(0, str(TENANT / 'qualification/C3/iteration-5/tools'))
import context
import build_interpretation as build


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def frozen(commit, path):
    return context.git_bytes(commit, path.relative_to(REPO))


def write(name, value):
    context.write(HERE / name, value)


def authenticate_helpers():
    for relative, digest in INPUTS['helpers'].items():
        path = TENANT / relative
        if sha(path.read_bytes()) != digest or frozen(INPUTS['helper_commit'], path) != path.read_bytes():
            raise ValueError('Changed packaging helper: ' + relative)
    context.verify_common()


def expected_binding(source_commit):
    commit, members = build.documentary_inventory(source_commit)
    mapping = json.loads(frozen(PREVIOUS, PACKAGE / REBIND[0]))
    mapping['document_source_input_commit'] = commit
    inventory = json.loads(frozen(PREVIOUS, PACKAGE / REBIND[1]))
    inventory['document_source_input_commit'] = commit
    inventory['document_members'] = members
    inventory['interpretation']['mapping_sha256'] = sha(build.json_bytes(mapping))
    return {REBIND[0]: build.json_bytes(mapping), REBIND[1]: build.json_bytes(inventory)}


def compare(source_commit, rebound):
    """Reject any change except the exact labels and derived coordinates."""
    prefix = str(PACKAGE.relative_to(REPO)) + '/'
    tracked = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', PREVIOUS,
                                      '--', str(PACKAGE.relative_to(REPO))], cwd=REPO, text=True).splitlines()
    names = {p[len(prefix):] for p in tracked}
    if names != {m['path'] for m in context.members()}:
        raise ValueError('Package membership changed')
    expected = expected_binding(source_commit) if rebound else {}
    differences = []
    for name in sorted(names):
        old = frozen(PREVIOUS, PACKAGE / name)
        current = (PACKAGE / name).read_bytes()
        wanted = old
        if name in LABELS:
            if old.count(b'3.0.0-rc.5') != 1:
                raise ValueError('Unexpected label preimage: ' + name)
            wanted = old.replace(b'3.0.0-rc.5', b'3.0.0-rc.9')
        elif name in expected:
            wanted = expected[name]
        if current != wanted:
            raise ValueError('Unselected package change: ' + name)
        if current != old:
            differences.append({'path': name, 'before_sha256': sha(old), 'sha256': sha(current)})
    return differences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['bind', 'verify'])
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--package-commit')
    args = parser.parse_args()
    authenticate_helpers()
    if args.operation == 'bind':
        compare(args.source_commit, False)
        for name, raw in expected_binding(args.source_commit).items():
            (PACKAGE / name).write_bytes(raw)
        changes = compare(args.source_commit, True)
        write('BINDING.json', {'source_commit': args.source_commit,
              'prior_package_commit': PREVIOUS, 'changed_members': changes,
              'standing': 'Candidate identity only; reviewed method and semantic interpretation unchanged.'})
        print(json.dumps({'bound': True, 'changed_members': len(changes)}))
        return
    if not args.package_commit:
        parser.error('--package-commit is required for verify')
    changes = compare(args.source_commit, True)
    checker = importlib.import_module('check_package')
    checker.HERE, checker.INPUTS = HERE, INPUTS
    sys.argv = [checker.__file__, '--package-commit', args.package_commit]
    checker.main()
    identity = subprocess.run([sys.executable, '-B', str(PACKAGE / 'interpretation/bindings.py'),
                               '--theory-root', INPUTS['theory_root']],
                              capture_output=True, text=True)
    write('INTERPRETATION_IDENTITY.json', {'exit': identity.returncode,
          'stdout': identity.stdout, 'stderr': identity.stderr,
          'scope': 'Source and theory identity through the unchanged consumer entry.'})
    if identity.returncode:
        raise ValueError('Interpretation identity check failed')
    candidate = {'kind': 'stdo.review-candidate', 'candidate_version': '3.0.0-rc.9',
                 'common_input': INPUTS['common_input'], 'source_commit': args.source_commit,
                 'package_commit': args.package_commit, 'members': context.members(),
                 'standing': 'Frozen for owner evaluation; no acceptance or publication.'}
    write('CANDIDATE.json', candidate)
    write('CHECKS.json', {'passed': True, 'source_commit': args.source_commit,
          'package_commit': args.package_commit, 'changed_members': changes,
          'all_other_package_bytes_unchanged': True,
          'semantic_review_subject': PREVIOUS,
          'review_reuse': 'The standards, frames, semantic account, native program, native map and all deciding content are byte-identical to the reviewed package. Only exact labels and documentary coordinates change.',
          'limits': 'Packaging and identity proof; member decisions, whole-method qualification, selection and release remain open.'})
    print(json.dumps({'candidate_version': '3.0.0-rc.9', 'passed': True, 'changed_members': len(changes)}))


if __name__ == '__main__':
    main()
