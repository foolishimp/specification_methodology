"""Actual public installer reproduction on the unchanged published native root."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import tempfile
import time
from urllib.parse import unquote, urljoin, urlsplit

REPO = Path(__file__).resolve().parents[6]
EVIDENCE = Path(__file__).resolve().parent / 'before'
PUBLIC = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5/public-001')


def ref(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    EVIDENCE.mkdir(exist_ok=False)
    scratch = Path(tempfile.mkdtemp(prefix='stdo-post-skills-before-')).resolve()
    config = json.loads((PUBLIC / 'hosts/codex/.agents/stdo-3.0.5/CONFIG.json').read_bytes())
    native = Path(config['method_root']) / 'plugins/spec'
    native_before = {p.relative_to(native).as_posix(): ref(p)['sha256'] for p in native.rglob('*') if p.is_file()}
    rows = []
    for host in ('codex', 'claude'):
        workspace = scratch / (host + ' workspace'); workspace.mkdir()
        records = EVIDENCE / host; records.mkdir()
        base = workspace / ('.agents' if host == 'codex' else '.claude')
        common = ['--package', str(REPO / 'stdo_skills'), '--host', host,
                  '--workspace', str(workspace), '--definition', config['definition'],
                  '--method-root', config['method_root'], '--ac-root', config['ac_root'],
                  '--stdo', config['stdo'], '--python', config['python']]
        executions = []
        def run(command, arguments):
            argv = [config['python'], '-B', str(REPO / 'stdo_skills/scripts/manage_skills.py'), command, *arguments]
            started = time.time_ns(); result = subprocess.run(argv, capture_output=True, cwd=REPO); ended = time.time_ns()
            (records / (command + '.stdout.json')).write_bytes(result.stdout)
            (records / (command + '.stderr.txt')).write_bytes(result.stderr)
            executions.append({'argv': argv, 'returncode': result.returncode,
                               'elapsed_seconds': (ended-started)/1e9,
                               'stdout': ref(records / (command + '.stdout.json')),
                               'stderr': ref(records / (command + '.stderr.txt'))})
            assert result.returncode == 0, result.stdout
            return json.loads(result.stdout)
        run('plan', common); assert not base.exists()
        installed = run('install', common)
        run('verify', ['--workspace', str(workspace), '--host', host,
                       '--receipt-sha256', installed['receipt_sha256']])
        wrapper = base / 'skills/stdo-help/SKILL.md'
        live = re.search(r'\[native workflow\]\(([^)]+)\)', wrapper.read_text()).group(1)
        workflow = Path(unquote(urlsplit(urljoin(wrapper.as_uri(), live)).path))
        guide_link = re.search(r'\]\(([^)]+GETTING_STARTED\.md)\)', workflow.read_text()).group(1)
        guide = Path(unquote(urlsplit(urljoin(workflow.as_uri(), guide_link)).path))
        broken = []
        for target in re.findall(r'\]\(([^)]+)\)', guide.read_text()):
            parsed = urlsplit(urljoin(guide.as_uri(), target))
            if parsed.scheme == 'file' and not Path(unquote(parsed.path)).exists():
                canonical = urlsplit(urljoin((native / 'references/GETTING_STARTED.md').as_uri(), target))
                broken.append({'link': target, 'relocated_target': unquote(parsed.path),
                               'canonical_target': unquote(canonical.path),
                               'canonical_exists': Path(unquote(canonical.path)).is_file()})
        assert len(broken) == 9 and all(x['canonical_exists'] for x in broken)
        row = {'host': host, 'workspace': str(workspace), 'executions': executions,
               'wrapper': ref(wrapper), 'live_workflow': ref(workflow), 'relocated_guide': ref(guide),
               'missing_targets_despite_verify_success': broken}
        if host == 'claude':
            refresh = base / 'skills/stdo-refresh/SKILL.md'
            source = native / 'claude-skills/refresh/SKILL.md'
            assert 'disable-model-invocation: true' in source.read_text()
            assert 'disable-model-invocation:' not in refresh.read_text()
            assert 'argument-hint:' not in refresh.read_text()
            (records / 'refresh.wrapper.md').write_bytes(refresh.read_bytes())
            (records / 'refresh.native.md').write_bytes(source.read_bytes())
            row['refresh'] = {'source': ref(source), 'wrapper': ref(refresh),
                              'lost_fields': ['argument-hint', 'disable-model-invocation'],
                              'claim': 'Actual deterministic wrapper metadata loss; no spontaneous model-invocation trial.'}
        rows.append(row)
    native_after = {p.relative_to(native).as_posix(): ref(p)['sha256'] for p in native.rglob('*') if p.is_file()}
    assert native_before == native_after
    result = {'schema': 'stdo.skills-post-release.reproduction/1', 'status': 'both_findings_reproduced',
              'source': ref(REPO / 'stdo_skills/scripts/manage_skills.py'),
              'native_manifest': ref(Path(config['method_root']) / 'manifest.json'),
              'cases': rows, 'native_plugin_unchanged': native_before,
              'limits': 'Actual public plan/install/verify using the selected real manager/native install; no LLM invocation, native mutation, global registration or adoption.'}
    target = EVIDENCE / 'RESULT.json'; target.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(ref(target)))


if __name__ == '__main__':
    main()
