"""One finite, read-only candidate-procedure actor with an explicit recorder."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('retained_process_tools', HERE.parents[1] / 'testing/run_probe.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
processes, descendants = prior.processes, prior.descendants


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data if isinstance(data, str) else json.dumps(data, indent=2) + '\n')


def inventory(root):
    return {str(p.relative_to(root)): {'sha256': sha(p), 'bytes': p.stat().st_size} for p in sorted(root.rglob('*')) if p.is_file()}


def events(path):
    values = []
    if path.exists():
        for line in path.read_text(errors='replace').splitlines():
            try: values.append(json.loads(line))
            except json.JSONDecodeError: pass
    return values


def acquired(values):
    total = 0
    for event in values:
        for block in event.get('message', {}).get('content', []) if isinstance(event.get('message', {}).get('content', []), list) else []:
            if isinstance(block, dict) and block.get('type') == 'tool_result':
                content = block.get('content', '')
                total += len((content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)).encode())
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('case', choices=['R1', 'E1', 'R2'])
    name = parser.parse_args().case
    meta = json.loads((HERE / 'CANDIDATE.json').read_text())
    fixture = json.loads((HERE / 'FIXTURES.json').read_text())
    seal = json.loads((HERE / 'FIXTURE_FREEZE.json').read_text())
    candidate = Path(meta['candidate'])
    repo = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
    v3 = repo / 'specification_methodology/v3'
    for row in meta['changed_source']:
        assert sha(repo / row['path']) == row['sha256'], row['path']
    for row in meta['payload']:
        assert sha(candidate / row['path']) == row['sha256']
        assert sha(v3 / 'build_tenants/common' / row['path']) == row['sha256']
    for row in seal['files']:
        assert sha(Path(row['path'])) == row['sha256'], row['path']
    info = fixture['cases'][name]
    root = Path(info['root'])
    if name == 'E1':
        admission = json.loads((HERE / 'E1_RETURN_ADMITTED.json').read_text())
        source = Path(fixture['cases']['R1']['root']) / 'records/R1.json'
        assert sha(source) == admission['sha256'] and admission['usable_closed_result']
        target = root / 'incoming/R1.json'
        assert not target.exists()
        target.parent.mkdir()
        shutil.copyfile(source, target)
    grant = json.loads((root / 'CONTRACT.json').read_text())
    paths = [str(Path(p).resolve(strict=True)) for p in grant['read_paths']]
    distinct = sum(Path(p).stat().st_size for p in paths)
    assert distinct <= grant['limits']['distinct_admitted_text_bytes']
    prompt = (root / 'PROMPT.txt').read_text()
    assert len(prompt.encode()) <= grant['limits']['initial_bytes']
    out = HERE / 'runs' / name
    assert not out.exists(), 'one invocation only'
    out.mkdir(parents=True)
    controls = Path(meta['scratch']) / 'controls' / name
    controls.mkdir(parents=True)
    policy = {'kind': 'stdo.claude-tool-policy', 'schema_version': 1, 'policy_id': 'review-flow-' + name, 'authority_ref': str(root / 'CONTRACT.json') + '#' + sha(root / 'CONTRACT.json'), 'cwd': str(root), 'read_paths': paths, 'bash_commands': [], 'skills': ['spec:' + info['skill']]}
    save(controls / 'policy.json', policy)
    audit = controls / 'audit.jsonl'
    gate = candidate / 'plugins/spec/scripts/claude_tool_gate.py'
    cmd = [meta['python'], str(gate), '--policy', str(controls / 'policy.json'), '--policy-sha256', sha(controls / 'policy.json')]
    settings = {'autoMemoryEnabled': False, 'hooks': {'PreToolUse': [{'matcher': '.*', 'hooks': [{'type': 'command', 'command': meta['python'], 'args': cmd[1:] + ['--audit', str(audit)], 'timeout': 10, 'onFailure': 'block'}]}]}}
    save(controls / 'settings.json', settings)
    save(controls / 'empty-mcp.json', {'mcpServers': {}})
    preflight = []
    for label, tool, body, expected in [('control', 'Read', {'file_path': str(root / 'CONTRACT.json')}, 'allow'), ('subject', 'Read', {'file_path': paths[-1]}, 'allow'), ('excluded', 'Read', {'file_path': str(root / 'excluded/capture.txt')}, 'deny'), ('shell', 'Bash', {'command': 'pwd'}, 'deny'), ('skill', 'Skill', {'skill': 'spec:' + info['skill']}, 'allow')]:
        event = {'hook_event_name': 'PreToolUse', 'cwd': str(root), 'tool_use_id': label, 'tool_name': tool, 'tool_input': body}
        r = subprocess.run(cmd, input=json.dumps(event), cwd=root, capture_output=True, text=True, timeout=10)
        actual = json.loads(r.stdout)['hookSpecificOutput']['permissionDecision']
        preflight.append({'label': label, 'event': event, 'exit': r.returncode, 'actual': actual, 'expected': expected, 'stdout': r.stdout, 'stderr': r.stderr})
        assert r.returncode == 0 and actual == expected
    save(out / 'GATE_PREFLIGHT.json', preflight)
    save(out / 'POLICY.json', policy)
    save(out / 'SETTINGS.json', settings)
    before = inventory(root)
    save(out / 'BEFORE.json', before)
    for p in root.rglob('*'):
        if p.is_file():
            dest = out / 'INPUTS' / p.relative_to(root)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, dest)
    save(out / 'PROMPT.txt', prompt)
    argv = ['/Users/jim/.local/bin/claude', '--print', '--verbose', '--output-format', 'stream-json', '--no-session-persistence', '--permission-mode', 'dontAsk', '--permission-prompts', 'none', '--restricted', '--tools', 'Read,Skill', '--settings', str(controls / 'settings.json'), '--strict-mcp-config', '--mcp-config', str(controls / 'empty-mcp.json'), '--plugin-dir', str(candidate / 'plugins/spec'), '--add-dir', str(candidate / 'plugins/spec'), '--model', meta['model_alias'], '--max-budget-usd', str(info['budget_usd'])]
    save(out / 'INVOCATION.json', {'argv': argv, 'cwd': str(root), 'source_delta_sha256': meta['source_delta_sha256'], 'distinct_admitted_text_bytes': distinct, 'initial_prompt_bytes': len(prompt.encode())})
    start, known, terminated, reason = time.monotonic(), set(), [], None
    with (out / 'STDOUT.jsonl').open('wb') as stdout, (out / 'STDERR.txt').open('wb') as stderr:
        proc = subprocess.Popen(argv, cwd=root, env=dict(os.environ), stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, start_new_session=True)
        proc.stdin.write(prompt.encode())
        proc.stdin.close()
        while proc.poll() is None:
            known |= descendants(proc.pid, processes())
            if time.monotonic() - start > info['wall_seconds']:
                reason = 'wall_time'
            if acquired(events(out / 'STDOUT.jsonl')) > grant['limits']['completed_acquisition_bytes']:
                reason = 'acquisition_bytes'
            if reason:
                os.killpg(proc.pid, signal.SIGTERM)
                try: proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait(timeout=3)
                break
            time.sleep(0.25)
    remaining = {pid for pid in known if pid != proc.pid and pid in processes()}
    for pid in remaining:
        try: os.kill(pid, signal.SIGTERM); terminated.append(pid)
        except ProcessLookupError: pass
    if remaining:
        time.sleep(0.5)
        for pid in remaining & processes().keys():
            try: os.kill(pid, signal.SIGKILL)
            except ProcessLookupError: pass
    trace = events(out / 'STDOUT.jsonl')
    results = [e for e in trace if e.get('type') == 'result']
    result = results[-1] if results else {}
    complete = proc.returncode == 0 and reason is None and result.get('subtype') == 'success' and not result.get('is_error')
    final = result.get('result', '') if complete else ''
    save(out / 'FINAL.txt', final)
    data, transport_error, receipts = None, None, []
    if complete:
        try:
            data = json.loads(final)
            assert set(data) == set(grant['return_json'])
            if name == 'E1': assert isinstance(data['decision_markdown'], str) and data['decision_markdown']
            else:
                assert isinstance(data['review_markdown'], str) and data['review_markdown']
                assert data['bug_report_markdown'] is None or isinstance(data['bug_report_markdown'], str)
            assert len(final.encode()) <= grant.get('return_transport_limit_bytes', 32768)
        except (ValueError, AssertionError) as exc:
            transport_error = str(exc) or 'return shape/size mismatch'
            data = None
    if data is not None:
        targets = [(grant['recorder']['result'], final, 'whole final JSON')]
        if name != 'E1' and data['bug_report_markdown'] is not None:
            targets.append((grant['recorder']['bug_report'], data['bug_report_markdown'], 'bug_report_markdown field'))
        for destination, text, field in targets:
            target = root / destination
            assert not target.exists()
            save(target, text)
            receipts.append({'path': str(target), 'sha256': sha(target), 'bytes': target.stat().st_size, 'producer_field': field, 'recorded_by': 'declared final-result recorder'})
    save(out / 'RECORDING.json', receipts)
    if audit.exists(): shutil.copyfile(audit, out / 'HOOK_AUDIT.jsonl')
    after = inventory(root)
    save(out / 'AFTER.json', after)
    save(out / 'CHANGES.json', {k: {'before': before.get(k), 'after': after.get(k)} for k in sorted(before.keys() | after.keys()) if before.get(k) != after.get(k)})
    models = sorted(set(result.get('modelUsage', {})) | {e['model'] for e in trace if e.get('type') == 'system' and e.get('model')})
    measurement = {'case': name, 'process_completed': complete, 'transport_recorded': data is not None, 'transport_error': transport_error, 'exit': proc.returncode, 'stop_reason': reason, 'elapsed_seconds': round(time.monotonic() - start, 3), 'wall_limit_seconds': info['wall_seconds'], 'configured_budget_usd': info['budget_usd'], 'reported_cost_usd': result.get('total_cost_usd'), 'usage': result.get('usage'), 'models_exposed': models, 'initial_prompt_bytes': len(prompt.encode()), 'distinct_admitted_text_bytes': distinct, 'completed_tool_result_bytes': acquired(trace), 'context_limit_note': 'Acquisition is monitored after complete tool results; managed/system context unmeasured, total active-context fit indeterminate.', 'remaining_known_processes': sorted(known & processes().keys()), 'terminated_descendants': terminated, 'native_qualification': 'candidate-procedure forward test only; synthetic Product premise; source-file/native Skill acquisition reported from actual trace; recorder is external and declared'}
    save(out / 'MEASUREMENT.json', measurement)
    print(json.dumps(measurement, indent=2))


if __name__ == '__main__':
    main()
