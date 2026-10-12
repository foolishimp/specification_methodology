"""Measure one fresh, read-only ordinary-entry acquisition experiment."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("variant", choices=["predecessor", "successor"])
parser.add_argument("--subject", required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parent
base = root.parents[2]
method = (Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
          if args.variant == 'predecessor' else base / 'successor')
task = root / 'task'
out = root / args.variant
out.mkdir(exist_ok=True)
prompt = ('You are a fresh read-only method reader in a controlled acquisition study. '
          'No prior history, advisor, peer or oracle is available. Read the ordinary '
          'stdo-work entry and follow its acquisition routes for the supplied task. '
          'METHOD_ROOT=' + str(method) + '\nTASK_ROOT=' + str(task) + '\n'
          'Start by reading TASK_ROOT/TASK.md. The exact actual construction basis '
          'is already verified by the Host there. The selected documentary package '
          'is the method subject, not an authorization to adopt an unreleased basis. '
          'Read/search within those two roots only; do not edit, run commands, '
          'contact services or assess the other variant. Report the requested '
          'recommendations with source-linked support and limitations. '
          'Acquisition allowance: 200000 rendered UTF-8 tool-result bytes plus this '
          'prompt; 12 turns; 360 seconds; provider-reported maximum USD 0.95. '
          'Read relevant sections rather than assuming an entire corpus is needed.\n')
(out / 'PROMPT.txt').write_text(prompt)
argv = ['claude', '-p', '--safe-mode', '--restricted', '--tools', 'Read,Glob,Grep',
        '--allowedTools', 'Read', 'Glob', 'Grep', '--permission-mode', 'dontAsk',
        '--add-dir', str(method), str(task), '--output-format', 'stream-json',
        '--verbose', '--no-session-persistence', '--model', 'opus', '--effort',
        'medium', '--max-turns', '12', '--max-budget-usd', '0.95']
report = {'variant': args.variant, 'subject_commit': args.subject,
          'method_root': str(method), 'argv': argv, 'prompt_bytes': len(prompt.encode()),
          'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
          'context_allowance_bytes': 200000, 'wall_allowance_seconds': 360,
          'spend_allowance_usd': 0.95, 'role': 'fresh read-only method reader',
          'provider_cwd': '/private/tmp',
          'limits': ['Source-package acquisition after Host basis verification',
                     'No native installation, host skill discovery or actual effects',
                     'Rendered tool-result bytes exclude provider system/internal prompts']}
started = time.monotonic()
try:
    result = subprocess.run(argv, input=prompt.encode(), capture_output=True,
                            cwd=report['provider_cwd'], timeout=360)
    (out / 'TRANSCRIPT.jsonl').write_bytes(result.stdout)
    (out / 'STDERR.txt').write_bytes(result.stderr)
    report['exit_code'] = result.returncode
    messages = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    finals = [m for m in messages if m.get('type') == 'result']
    if finals:
        final = finals[-1]
        for key in ('is_error', 'total_cost_usd', 'usage', 'modelUsage', 'session_id', 'num_turns'):
            if key in final:
                report[key] = final[key]
        (out / 'RESULT.md').write_text(final.get('result', '') + '\n')
        report['provider_subtype'] = final.get('subtype')
    else:
        report['transport_result'] = 'no final result'
    reads, calls, byte_count = [], [], 0
    for message in messages:
        for block in message.get('message', {}).get('content', []):
            if not isinstance(block, dict):
                continue
            if block.get('type') == 'tool_use':
                calls.append({'name': block['name'], 'input': block.get('input', {})})
                if block['name'] == 'Read':
                    reads.append(block.get('input', {}))
            elif block.get('type') == 'tool_result':
                content = block.get('content', '')
                text = (content if isinstance(content, str) else
                        '\n'.join(b.get('text', '') for b in content if isinstance(b, dict)))
                byte_count += len(text.encode())
    report.update(read_requests=reads, tool_calls=calls, rendered_tool_result_bytes=byte_count,
                  context_allowance_observed=byte_count <= 200000)
except subprocess.TimeoutExpired as error:
    (out / 'TRANSCRIPT.jsonl').write_bytes(error.stdout or b'')
    (out / 'STDERR.txt').write_bytes(error.stderr or b'')
    report['transport_result'] = 'timeout'
report['elapsed_seconds'] = round(time.monotonic() - started, 3)
(out / 'MEASUREMENT.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items()
                  if k not in {'argv', 'usage', 'modelUsage', 'tool_calls', 'read_requests'}}))
raise SystemExit(0 if report.get('exit_code') == 0 and not report.get('is_error')
                 and report.get('context_allowance_observed') else 1)
