"""Candidate public paths against unchanged real native bytes; no host model call."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

REPO = Path(__file__).resolve().parents[6]
EVIDENCE = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / 'stdo_skills/tests'))
from test_install_305 import candidate_package, m
from test_native_routes import anchors, links, local_target


def ref(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    output = EVIDENCE / 'after'; output.mkdir(exist_ok=False)
    scratch = Path(tempfile.mkdtemp(prefix='stdo-post-skills-after-')).resolve()
    package = candidate_package(scratch / 'selected candidate package')
    public = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/public-001')
    config = json.loads((public / 'hosts/codex/.agents/stdo-3.0.5/CONFIG.json').read_bytes())
    method = Path(config['method_root']); native = method / 'plugins/spec'
    guide = native / 'references/GETTING_STARTED.md'
    selected = {method / 'manifest.json', *(p for p in native.rglob('*') if p.is_file())}
    for link in links(guide.read_text()):
        target, _ = local_target(guide, link)
        if target is not None: selected.add(target)
    before = {str(p): ref(p)['sha256'] for p in sorted(selected)}
    cases = []
    for host in ('codex', 'claude'):
        workspace = scratch / (host + ' workspace with spaces'); workspace.mkdir()
        directory = output / host; directory.mkdir()
        base, bundle, receipt_path = m.paths(workspace, host)
        invocations = []
        def run(label, script, command, args):
            argv = [config['python'], '-B', str(script), command, *args]
            started = time.time_ns(); result = subprocess.run(argv, cwd=REPO, capture_output=True); ended = time.time_ns()
            (directory / (label + '.stdout.json')).write_bytes(result.stdout)
            (directory / (label + '.stderr.txt')).write_bytes(result.stderr)
            invocations.append({'operation': label, 'argv': argv, 'returncode': result.returncode,
                                'elapsed_seconds': (ended-started)/1e9,
                                'stdout': ref(directory / (label + '.stdout.json')),
                                'stderr': ref(directory / (label + '.stderr.txt'))})
            assert result.returncode == 0, result.stdout
            return json.loads(result.stdout)
        common = ['--package', str(package), '--host', host, '--workspace', str(workspace),
                  '--definition', config['definition'], '--method-root', str(method),
                  '--ac-root', config['ac_root'], '--stdo', config['stdo'], '--python', config['python']]
        producer = package / 'scripts/manage_skills.py'
        run('plan', producer, 'plan', common); assert not base.exists()
        installed = run('install', producer, 'install', common)
        lifecycle = ['--workspace', str(workspace), '--host', host, '--receipt-sha256', installed['receipt_sha256']]
        run('verify', producer, 'verify', lifecycle)
        run('installed-check-runtime', bundle / 'manage_skills.py', 'check-runtime', ['--configuration', str(bundle / 'CONFIG.json')])
        assert not (bundle / 'native').exists()
        receipt = json.loads(receipt_path.read_bytes()); current = json.loads((bundle / 'CONFIG.json').read_bytes())
        assert receipt['native_workflow'] == current['native_workflow']
        assert current['native_workflow']['root'] == str(native)
        routes = []
        for name in (*m.CORE, *(('stdo-refresh',) if host == 'claude' else ())):
            wrapper = base / 'skills' / name / 'SKILL.md'
            body = wrapper.read_text(); live = re.search(r'\[native workflow\]\(([^)]+)\)', body).group(1)
            target, fragment = local_target(wrapper, live)
            expected = native / ('claude-skills/refresh/SKILL.md' if name == 'stdo-refresh' else 'skills/' + name + '/SKILL.md')
            assert target == expected and fragment == ''
            expected_header = re.sub(r'^name:[^\n]*', 'name: ' + name, target.read_text().split('---', 2)[1], flags=re.M)
            assert body.split('---', 2)[1] == expected_header
            for link in links(body):
                local, _ = local_target(wrapper, link); assert local.is_file(), (wrapper, link)
            (directory / (name + '.wrapper.md')).write_bytes(wrapper.read_bytes())
            routes.append({'wrapper': ref(wrapper), 'canonical_target': ref(target), 'uri': live})
        help_file = native / 'skills/stdo-help/SKILL.md'
        guide_link = next(x for x in links(help_file.read_text()) if 'GETTING_STARTED.md' in x)
        assert local_target(help_file, guide_link)[0] == guide
        guidance = []
        for link in links(guide.read_text()):
            target, fragment = local_target(guide, link)
            if target is None: continue
            assert target.is_file(), (link, target)
            if fragment: assert fragment in anchors(target.read_text()), (link, fragment)
            guidance.append({'link': link, 'canonical_target': ref(target), 'fragment': fragment})
        for path in (receipt_path, bundle / 'CONFIG.json'):
            (directory / path.name).write_bytes(path.read_bytes())
        unrelated = base / 'skills/unrelated/SKILL.md'; unrelated.parent.mkdir(); unrelated.write_text('keep unrelated\n')
        run('remove', producer, 'remove', lifecycle)
        assert unrelated.read_text() == 'keep unrelated\n' and not bundle.exists()
        cases.append({'host': host, 'workspace': str(workspace), 'executions': invocations,
                      'wrapper_routes': routes, 'getting_started_routes': guidance,
                      'dependency': current['native_workflow'], 'removal': 'only receipt-owned files removed; unrelated marker remains'})
    # Remove the actual old-producer installs, retaining their exact old bytes first.
    original = json.loads((EVIDENCE / 'before/RESULT.json').read_bytes()); legacy = []
    for case in original['cases']:
        host = case['host']; workspace = Path(case['workspace']); base, _, receipt_path = m.paths(workspace, host)
        raw = receipt_path.read_bytes(); receipt = json.loads(raw); assert 'native_workflow' not in receipt
        members = {receipt_path.relative_to(base).as_posix(): raw}
        for root in receipt['roots']:
            for name, content in m.tree(base / root).items(): members[root + '/' + name] = content
        archive = output / (host + '-actual-legacy-preimage.zip')
        with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as stream:
            for name, content in sorted(members.items()): stream.writestr(name, content)
        argv = [config['python'], '-B', str(package / 'scripts/manage_skills.py'), 'remove',
                '--workspace', str(workspace), '--host', host, '--receipt-sha256', m.sha(raw)]
        started = time.time_ns(); result = subprocess.run(argv, cwd=REPO, capture_output=True); ended = time.time_ns()
        stdout = output / (host + '-legacy-remove.stdout.json'); stdout.write_bytes(result.stdout)
        stderr = output / (host + '-legacy-remove.stderr.txt'); stderr.write_bytes(result.stderr)
        assert result.returncode == 0, result.stdout
        assert all(not (base / root).exists() for root in receipt['roots']) and not receipt_path.exists()
        legacy.append({'host': host, 'actual_predecessor': case, 'preimage_archive': ref(archive),
                       'members': {name: m.sha(raw) for name, raw in members.items()},
                       'argv': argv, 'returncode': result.returncode, 'elapsed_seconds': (ended-started)/1e9,
                       'stdout': ref(stdout), 'stderr': ref(stderr)})
    after = {str(p): ref(p)['sha256'] for p in sorted(selected)}; assert before == after
    value = {'schema': 'stdo.skills-post-release.public-correction/1', 'status': 'selected_public_paths_passed',
             'candidate_source': ref(REPO / 'stdo_skills/scripts/manage_skills.py'),
             'scratch_candidate_manifest': ref(package / 'release/3.0.5/manifest.json'),
             'published_manifest_unchanged': ref(REPO / 'stdo_skills/release/3.0.5/manifest.json'),
             'cases': cases, 'actual_legacy_removals': legacy,
             'canonical_selected_members_unchanged': before,
             'limits': ['Actual public CLI against unchanged real published native installation and selected manager/runtime.',
                        'Canonical paths containing spaces and canonical-tamper/missing controls use the separate controlled fixture suite.',
                        'No live host/model invocation, global registration, basis adoption, source-package release or old qualification relabelling.']}
    target = output / 'RESULT.json'; target.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    print(json.dumps(ref(target)))


if __name__ == '__main__': main()
