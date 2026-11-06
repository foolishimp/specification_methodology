"""Retain actual public case-alias observations in disposable private custody."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time

REPO = Path(__file__).resolve().parents[7]
WORK = Path(__file__).resolve().parent
CODE = REPO / 'a_c/build_tenants/graphify/code'
ROUTER = REPO / 'a_c/scripts/ac.py'


def sha(raw): return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def tree(root):
    result = {}
    for path in sorted(root.rglob('*')):
        name = path.relative_to(root).as_posix()
        if path.is_symlink(): result[name] = {'kind': 'symlink', 'target': str(path.readlink())}
        elif path.is_file(): result[name] = {'kind': 'file', 'sha256': sha(path.read_bytes())}
        elif path.is_dir(): result[name] = {'kind': 'directory'}
    return result


def upstream():
    private = Path(tempfile.mkdtemp(prefix='stdo305-upstream-case-')).resolve()
    original = Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo305-runtime-logged-zy3qk0do/graphify/RUNTIME.json')
    runtime = json.loads(original.read_text())
    protected = private / 'protected'
    shutil.copytree(runtime['upstream'], protected, symlinks=True)
    runtime['upstream'] = str(protected)
    runtime_path = private / 'runtime.json'; save(runtime_path, runtime)
    fixtures = WORK.parent / 'upstream-owner-tests'
    alias = private / 'PROTECTED'
    argv = [runtime['python'], '-B', str(ROUTER), 'upstream',
            '--model', str(REPO / 'a_c/build_tenants/graphify/test_env/fixtures/toy_model.json'),
            '--carrier', str(fixtures / 'carrier.json'), '--selections', str(fixtures / 'selections.json'),
            '--upstream', str(protected), '--runtime', str(runtime_path), '--output', str(alias / 'review-output')]
    return private, protected, alias, argv, {'runtime_receipt_is_controlled_relocation_of': str(original)}


def native():
    sys.path.insert(0, str(CODE.parent / 'test_env'))
    import test_ac_support_native305 as test
    fixture = test.Native305PublicTests('test_current_discovery_and_result_parent')
    fixture.setUp()
    # Preserve this independently constructed disposable tree, including failure.
    fixture.temp._finalizer.detach()
    private = fixture.root; protected = fixture.installation
    alias = protected.with_name('METHOD')
    selected = alias / 'runtime-evidence'
    fixture.f.policy['evidence_root'] = str(selected)
    fixture.f.policy['product']['authority_binding']['result_surface']['root'] = str(selected)
    fixture._select_policy()
    request = private / 'case-request.json'
    save(request, {'schema': test.c.REQUEST, 'id': 'actual-case-alias', 'operation': 'tools.describe', 'arguments': {}})
    argv = [str(fixture.python), '-B', str(ROUTER), 'support', '--policy', str(fixture.policy_path),
            '--policy-sha256', fixture.policy_sha, '--principal', 'executive', 'call', '--request', str(request)]
    return private, protected, alias, argv, {'policy_sha256': fixture.policy_sha, 'synthetic_installed_cut': True}


def main(subject, label):
    evidence = WORK / (subject + '-' + label); evidence.mkdir(exist_ok=False)
    private, protected, alias, argv, extra = {'upstream': upstream, 'native': native}[subject]()
    assert alias.exists() and alias.samefile(protected), 'This control requires a real filesystem case alias'
    assert alias.resolve() != protected.resolve(), 'The control must challenge resolved lexical containment'
    before = tree(protected)
    start = time.time_ns(); result = subprocess.run(argv, cwd=REPO, capture_output=True, timeout=60); end = time.time_ns()
    after = tree(protected)
    (evidence / 'stdout.json').write_bytes(result.stdout); (evidence / 'stderr.log').write_bytes(result.stderr)
    save(evidence / 'before-tree.json', before); save(evidence / 'after-tree.json', after)
    names = ('ac_upstream.py', 'ac_generate.py', 'ac_graph.py') if subject == 'upstream' else ('ac_support.py', 'ac_support_core.py', 'ac_support_effects.py', 'ac_support_composition.py', 'ac_formal_gate.py', 'ac_graph.py')
    producers = [ROUTER, *(CODE / name for name in names)]
    if (CODE / 'ac_fs_boundary.py').exists(): producers.append(CODE / 'ac_fs_boundary.py')
    record = {'schema': 'stdo305.case-containment-execution/1', 'subject': subject, 'label': label,
              'producers': {str(p.relative_to(REPO)): sha(p.read_bytes()) for p in producers},
              'argv': argv, 'cwd': str(REPO), 'exit_code': result.returncode, 'started_ns': start, 'ended_ns': end,
              'private_custody_root': str(private), 'protected': str(protected), 'alias': str(alias),
              'alias_samefile': alias.samefile(protected), 'resolved_spellings_differ': alias.resolve() != protected.resolve(),
              'before_tree_sha256': sha((evidence / 'before-tree.json').read_bytes()),
              'after_tree_sha256': sha((evidence / 'after-tree.json').read_bytes()),
              'added': sorted(set(after) - set(before)), 'removed': sorted(set(before) - set(after)),
              'changed': sorted(k for k in before.keys() & after.keys() if before[k] != after[k]),
              'stdout_sha256': sha(result.stdout), 'stderr_sha256': sha(result.stderr), **extra}
    save(evidence / 'execution.json', record)
    returned = json.loads(result.stdout)
    print(json.dumps({'subject': subject, 'phase': label, 'exit_code': result.returncode,
                      'status': returned.get('status'), 'reason': returned.get('reason', returned.get('refusal')),
                      'added': record['added'], 'removed': record['removed'], 'changed': record['changed'],
                      'private_custody': str(private)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('subject', choices=['upstream', 'native']); parser.add_argument('label')
    args = parser.parse_args(); main(args.subject, args.label)
