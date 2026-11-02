"""Bounded successor actors; no oracle or inferred final result is supplied."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('prior_runner_utilities', HERE.parent / 'run_probe.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
sha, save, inventory, processes, descendants = prior.sha, prior.save, prior.inventory, prior.processes, prior.descendants


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('case', choices=['issuer', 'receiver'])
    args = parser.parse_args()
    case = args.case
    out = HERE / 'runs' / case
    if out.exists(): raise SystemExit('one invocation only; preserve prior evidence')
    meta = json.loads((HERE / 'FIXTURES.json').read_text())
    freeze = json.loads((HERE / 'SOURCE_FREEZE.json').read_text())
    repo = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
    for row in freeze['payload'] + freeze['support']:
        assert sha((repo / row['path']).read_bytes()) == row['sha256'], row['path']
    candidate = Path(meta['candidate'])
    for row in freeze['payload']:
        relative = Path(row['path']).relative_to(freeze['candidate_root'])
        assert sha((candidate / relative).read_bytes()) == row['sha256'], str(relative)
    for path, pin in json.loads((HERE / 'RUNTIME_PINS.json').read_text()).items():
        assert sha(Path(path).read_bytes()) == pin['sha256'], path
    project = {'direct': 'direct', 'issuer': 'coordinated', 'receiver': 'coordinated', 'negative': 'review'}[case]
    root = Path(meta['projects'][project])
    if case == 'receiver':
        receipt = json.loads((HERE / 'runs/issuer/RELAY_RECEIPT.json').read_text())
        prior_measure = json.loads((HERE / 'runs/issuer/MEASUREMENT.json').read_text())
        assert receipt and prior_measure['completed'] and not prior_measure['timeout'], 'no completed issuer packet'
        assert sha((root / 'incoming/issuer-return.md').read_bytes()) == receipt[-1]['sha256']
    out.mkdir(parents=True)
    prompt_name = {'direct': 'PROMPT.txt', 'issuer': 'PROMPT-ISSUER.txt', 'receiver': 'PROMPT-RECEIVER.txt', 'negative': 'PROMPT-NEGATIVE.txt'}[case]
    prompt = (root / prompt_name).read_text()
    wall_limit = {'direct': 240, 'issuer': 300, 'receiver': 240, 'negative': 180}[case]
    before = inventory(root)
    save(out / 'BEFORE.json', before)
    save(out / 'PROMPT.txt', prompt)
    for name in before:
        target = out / 'INPUTS' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / name, target)
    if case == 'direct':
        host = 'codex'
        argv = ['/Users/jim/bin/codex', '--no-daemon', '--disable', 'memories', 'exec', '--ephemeral', '--json', '--skip-git-repo-check', '--sandbox', 'workspace-write', '-C', str(root), '-']
    else:
        host = 'claude'
        policy = meta['policies'][case]
        save(out / 'POLICY.json', Path(policy['policy']).read_text())
        save(out / 'SETTINGS.json', Path(policy['settings']).read_text())
        # Actual shipped CLI probe before actor work; tests supported calls and concrete negative guards.
        p = json.loads(Path(policy['policy']).read_text())
        gate = candidate / 'plugins/spec/scripts/claude_tool_gate.py'
        command = [meta['python'], str(gate), '--policy', policy['policy'], '--policy-sha256', policy['policy_sha256']]
        events = [
            ('listed-control', {'tool_name': 'Read', 'tool_input': {'file_path': str(root / ('inbox/bad-packet.md' if case == 'negative' else 'contracts/' + ('issuer' if case == 'issuer' else 'worker') + '.json'))}}, 'allow'),
            ('unlisted-output', {'tool_name': 'Read', 'tool_input': {'file_path': str(root / 'excluded-outputs/private.txt')}}, 'deny'),
            ('listed-command', {'tool_name': 'Bash', 'tool_input': {'command': p['bash_commands'][0]}}, 'allow'),
            ('parent-listing', {'tool_name': 'Bash', 'tool_input': {'command': 'ls ..'}}, 'deny'),
            ('command-suffix', {'tool_name': 'Bash', 'tool_input': {'command': p['bash_commands'][0] + ' && ls ..'}}, 'deny'),
            ('selected-skill', {'tool_name': 'Skill', 'tool_input': {'skill': p['skills'][0]}}, 'allow'),
        ]
        checks = []
        for label, body, expected in events:
            event = {'hook_event_name': 'PreToolUse', 'cwd': str(root), 'tool_use_id': 'synthetic-' + label, **body}
            result = subprocess.run(command, input=json.dumps(event), cwd=root, capture_output=True, text=True, timeout=15)
            value = json.loads(result.stdout)
            actual = value['hookSpecificOutput']['permissionDecision']
            checks.append({'case': label, 'input': event, 'expected': expected, 'actual': actual, 'exit': result.returncode, 'output': value})
            assert result.returncode == 0 and actual == expected, label
        save(out / 'GATE_PREFLIGHT.json', checks)
        argv = ['/Users/jim/.local/bin/claude', '--print', '--verbose', '--output-format', 'stream-json', '--no-session-persistence', '--permission-mode', 'dontAsk', '--permission-prompts', 'none', '--restricted', '--tools', 'Read,Skill,Bash', '--settings', policy['settings'], '--strict-mcp-config', '--mcp-config', str(Path(meta['controls']) / 'empty-mcp.json'), '--plugin-dir', str(candidate / 'plugins/spec'), '--add-dir', str(candidate / 'plugins/spec'), '--model', 'claude-fable-5-1']
    start = time.monotonic()
    known, terminated, timed_out = set(), [], False
    with (out / 'STDOUT.jsonl').open('wb') as stdout, (out / 'STDERR.txt').open('wb') as stderr:
        proc = subprocess.Popen(argv, cwd=root, env=dict(os.environ), stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, start_new_session=True)
        proc.stdin.write(prompt.encode()); proc.stdin.close()
        while proc.poll() is None:
            known |= descendants(proc.pid, processes())
            if time.monotonic() - start >= wall_limit:
                timed_out = True
                os.killpg(proc.pid, signal.SIGTERM)
                try: proc.wait(timeout=3)
                except subprocess.TimeoutExpired: os.killpg(proc.pid, signal.SIGKILL); proc.wait(timeout=3)
                break
            time.sleep(0.5)
        leftovers = {pid for pid in known if pid != proc.pid and pid in processes()}
        for pid in leftovers:
            try: os.kill(pid, signal.SIGTERM); terminated.append(pid)
            except ProcessLookupError: pass
        if leftovers:
            time.sleep(0.5)
            for pid in leftovers & processes().keys():
                try: os.kill(pid, signal.SIGKILL)
                except ProcessLookupError: pass
    events = []
    for line in (out / 'STDOUT.jsonl').read_text(errors='replace').splitlines():
        try: events.append(json.loads(line))
        except json.JSONDecodeError: pass
    completed = not timed_out and proc.returncode == 0 and (any(e.get('type') == 'turn.completed' for e in events) if host == 'codex' else any(e.get('type') == 'result' and e.get('subtype') == 'success' and not e.get('is_error') for e in events))
    messages, models, usage, cost = [], set(), None, None
    for event in events:
        if event.get('type') == 'item.completed' and event.get('item', {}).get('type') == 'agent_message': messages.append(event['item'].get('text', ''))
        if event.get('type') == 'result':
            messages.append(event.get('result', '')); usage = event.get('usage'); cost = event.get('total_cost_usd'); models.update(event.get('modelUsage', {}))
        if event.get('type') == 'system' and event.get('model'): models.add(event['model'])
        if event.get('type') == 'turn.completed': usage = event.get('usage')
    final = messages[-1] if messages and completed else ''
    save(out / 'LAST_AGENT_MESSAGE.md', (messages[-1] if messages else '') + '\n')
    save(out / 'FINAL.md', final + '\n')
    relays = {'direct': ['records/direct-result.md'], 'issuer': ['records/issuer-result.md', 'incoming/issuer-return.md'], 'receiver': ['records/worker-result.md'], 'negative': ['records/bad-review-result.md']}[case]
    receipts = []
    if final:
        for name in relays:
            target = root / name
            actor_recorded = target.exists()
            if not actor_recorded: save(target, final + '\n')
            elif name.startswith('incoming/'): raise SystemExit('incoming packet already exists')
            receipts.append({'path': name, 'recorded_by': 'actor' if actor_recorded else 'final-return relay', 'sha256': sha(target.read_bytes())})
    save(out / 'RELAY_RECEIPT.json', receipts)
    after = inventory(root)
    save(out / 'AFTER.json', after)
    changes = {k: {'before': before.get(k), 'after': after.get(k)} for k in sorted(before.keys() | after.keys()) if before.get(k) != after.get(k)}
    save(out / 'CHANGES.json', changes)
    if host == 'claude' and Path(meta['policies'][case]['audit']).exists(): shutil.copyfile(meta['policies'][case]['audit'], out / 'HOOK_AUDIT.jsonl')
    measurement = {'case': case, 'host': host, 'argv': argv, 'cwd': str(root), 'source_freeze_sha256': meta['source_freeze_sha256'], 'prompt_bytes': len(prompt.encode()), 'prompt_sha256': sha(prompt.encode()), 'wall_limit_seconds': wall_limit, 'elapsed_seconds': round(time.monotonic() - start, 3), 'exit_code': proc.returncode, 'timeout': timed_out, 'completed': completed, 'known_process_ids': sorted(known), 'terminated_descendants': terminated, 'remaining_known_processes': sorted(known & processes().keys()), 'models_exposed': sorted(models), 'reported_cost_usd': cost, 'usage': usage, 'host_instructions': 'fresh process with fixture AGENTS/CLAUDE; no resumed conversation; managed/system inherited context unmeasured; selected per-run controls retained', 'discovery': 'Claude --plugin-dir native plugin; Codex native local .agents/skills alias', 'standing': 'raw bounded observation requiring semantic interpretation'}
    save(out / 'MEASUREMENT.json', measurement)
    print(json.dumps({k: measurement[k] for k in ['case', 'host', 'elapsed_seconds', 'timeout', 'completed', 'models_exposed', 'remaining_known_processes']}, indent=2))
    print(json.dumps({'changed_paths': list(changes), 'final_bytes': len(final.encode())}, indent=2))


if __name__ == '__main__': main()
