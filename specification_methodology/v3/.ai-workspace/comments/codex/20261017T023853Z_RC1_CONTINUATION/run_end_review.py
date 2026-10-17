#!/usr/bin/env python3
"""Run the three admitted read-only contexts and retain ordered evidence."""
import concurrent.futures
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

s = json.loads(Path('/tmp/stdo_rc1_current.json').read_text())
out, cwd = Path(s['out']), Path(s['review_scratch'])

def run(name):
    cmd = ['claude', '--restricted', '--print', '--verbose', '--output-format', 'stream-json', '--no-session-persistence', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--tools', 'Read,Glob,Grep', '--allowed-tools', 'Read,Glob,Grep', '--permission-mode', 'dontAsk', '--max-budget-usd', '6']
    started = time.monotonic()
    stamp = datetime.now(timezone.utc).isoformat()
    log, err = out / (name + '_STREAM.jsonl'), out / (name + '_STDERR.txt')
    assert not log.exists()
    prompt = (cwd / (name + '_PROMPT.txt')).read_bytes()
    (out / (name + '_PROMPT.txt')).write_bytes(prompt)
    timed_out = False
    with log.open('wb') as target, err.open('wb') as errors:
        proc = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=target, stderr=errors)
        proc.stdin.write(prompt)
        proc.stdin.close()
        checkpoint = started + 60
        while proc.poll() is None:
            time.sleep(1)
            now = time.monotonic()
            if now >= checkpoint:
                print(json.dumps({'scope': name, 'state': 'running', 'seconds': round(now-started), 'stream_bytes': log.stat().st_size}), flush=True)
                checkpoint = now + 60
            if now-started >= 2700:
                timed_out = True
                proc.terminate()
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
                break
    record = {'scope': name, 'candidate': s['review_package_commit'], 'command': cmd, 'cwd': str(cwd), 'prompt_sha256': hashlib.sha256(prompt).hexdigest(), 'started_at': stamp, 'elapsed_seconds': round(time.monotonic()-started,3), 'exit_code': proc.returncode, 'timed_out': timed_out, 'max_budget_usd': 6}
    messages, requests, acquisition = [], {}, []
    expectations_line = first_subject_line = None
    for lineno, line in enumerate(log.read_text().splitlines(), 1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get('type') == 'system' and event.get('subtype') == 'init':
            record['model'] = event.get('model')
            record['tools'] = event.get('tools')
        if event.get('type') == 'result':
            record['result'] = event
        if event.get('type') != 'assistant':
            continue
        m = event.get('message', {})
        usage = m.get('usage', {})
        request = requests.setdefault(m.get('id', 'unknown-'+str(lineno)), {})
        for key in ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens'):
            request[key] = max(request.get(key, 0), usage.get(key, 0) or 0)
        for content in m.get('content', []):
            if content.get('type') == 'text':
                text = content.get('text', '')
                messages.append(text)
                if expectations_line is None and 'EXPECTATIONS' in text:
                    expectations_line = lineno
            if content.get('type') == 'tool_use':
                args = content.get('input', {})
                acquisition.append({'stream_line': lineno, 'tool': content.get('name'), 'input': args})
                rendered = json.dumps(args)
                if first_subject_line is None and any(x in rendered for x in ('candidate/', 'account-by-owner', 'conservation-by-source', 'evidence/', 'prior-closed-reviews')):
                    first_subject_line = lineno
    model_usage = record.get('result', {}).get('modelUsage', {})
    fields = {'input_tokens': 'inputTokens', 'cache_creation_input_tokens': 'cacheCreationInputTokens', 'cache_read_input_tokens': 'cacheReadInputTokens'}
    totals = {k: sum(u.get(k, 0) for u in requests.values()) for k in fields}
    aggregate = {k: sum(u.get(v, 0) for u in model_usage.values()) for k, v in fields.items()}
    reconciled = bool(model_usage) and totals == aggregate
    peak_input = max((sum(u.values()) for u in requests.values()), default=0)
    all_output = sum(u.get('outputTokens', 0) for u in model_usage.values())
    windows = [u.get('contextWindow') for u in model_usage.values() if u.get('contextWindow')]
    record['context_account'] = {'unique_requests': len(requests), 'request_input_sums': totals, 'provider_input_sums': aggregate, 'reconciled': reconciled, 'maximum_request_input': peak_input, 'aggregate_output_tokens': all_output, 'conservative_peak_token_upper_bound': peak_input + all_output if reconciled else None, 'reported_context_windows': windows, 'basis': 'Includes input, cache creation and cache read; adds the entire call output as a conservative request-output bound. Only observed provider requests are covered.'}
    record['expectations_order'] = {'expectations_stream_line': expectations_line, 'first_detected_subject_acquisition_line': first_subject_line, 'precedes': expectations_line is not None and first_subject_line is not None and expectations_line < first_subject_line, 'limit': 'Path-based detection is supported by retained ordered tool arguments; manual readback still owns the interpretation.'}
    (out / (name + '_REVIEW.md')).write_text('\n\n'.join(messages) + '\n')
    (out / (name + '_EXECUTION.json')).write_text(json.dumps(record, indent=2) + '\n')
    (out / (name + '_ACQUISITION.json')).write_text(json.dumps(acquisition, indent=2) + '\n')
    result = record.get('result', {})
    summary = {'scope': name, 'state': 'returned', 'seconds': record['elapsed_seconds'], 'cost_usd': result.get('total_cost_usd'), 'subtype': result.get('subtype'), 'is_error': result.get('is_error'), 'context_reconciled': reconciled, 'upper_bound_tokens': record['context_account']['conservative_peak_token_upper_bound'], 'expectations_first': record['expectations_order']['precedes']}
    print(json.dumps(summary), flush=True)
    return summary

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    summaries = list(pool.map(run, ('SOURCE', 'DOMAIN', 'REPRESENTATION')))
(out / 'END_REVIEW_EXECUTION.json').write_text(json.dumps(summaries, indent=2) + '\n')
