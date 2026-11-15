from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import uuid

BASE = Path(__file__).resolve().parent
stage = (BASE / sys.argv[1]).resolve()
assert stage.is_relative_to(BASE)
packet = stage / 'PACKET.md'
assert packet.is_file()
assert not (stage / 'INVOCATION.json').exists(), 'Preserve the original invocation; select a new stage directory.'
source_first = stage.name.startswith('source-first')
system = ('You are an independent source-first assessment actor. Derive obligations and finite falsifiers only from the supplied governing sources before any candidate exposure. Return your own source-grounded expectations, source gaps and limits. Do not construct, repair or judge any unseen candidate. Do not use tools.' if source_first else
          'You are an independent assessment actor. Assess only the declared frozen subject against the supplied governing sources and previously fixed source-first expectations. Distinguish source meaning, operator-computed observations, author claims and your own judgment. You may not construct or repair the candidate, change scope or authorize publication. Do not use tools. Return exact-subject conclusions, findings, counterexamples, source/evidence gaps and explicit limits.')
session = str(uuid.uuid4())
command = ['/Users/jim/.local/bin/claude', '--print', '--safe-mode', '--tools', '', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--permission-mode', 'dontAsk', '--no-session-persistence', '--session-id', session, '--model', 'opus', '--effort', 'high', '--output-format', 'stream-json', '--verbose', '--system-prompt', system]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

record = {'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'argv': command, 'cwd': str(stage), 'stdin': 'PACKET.md', 'stdin_sha256': sha(packet),
          'stdin_bytes': packet.stat().st_size, 'requested_model': 'opus', 'requested_session_id': session,
          'requested_tools': [], 'supplied_context': 'source-only expectations' if source_first else 'declared frozen subject and fixed source expectations',
          'host_limitations': 'ordinary Claude CLI; requested safe/tool-disabled session is not an enforced clean-room guarantee',
          'context_capacity': 'packet bytes measured; no numerical actor capacity selected; hidden host/system context not measured'}
(stage / 'INVOCATION.json').write_text(json.dumps(record, indent=2) + '\n')
(stage / 'SESSION_ID').write_text(session + '\n')
version = subprocess.run(['/Users/jim/.local/bin/claude', '--version'], capture_output=True, text=True)
(stage / 'CLI_VERSION.txt').write_text(version.stdout + version.stderr)
with packet.open('rb') as source, (stage / 'claude.stdout.jsonl').open('wb') as stdout, (stage / 'claude.stderr.txt').open('wb') as stderr:
    try:
        result = subprocess.run(command, stdin=source, stdout=stdout, stderr=stderr, cwd=stage, timeout=1200)
        record['exit_code'] = result.returncode
    except subprocess.TimeoutExpired:
        record['exit_code'] = None
        record['timeout_seconds'] = 1200
record['finished_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
record['stdout_sha256'] = sha(stage / 'claude.stdout.jsonl')
record['stderr_sha256'] = sha(stage / 'claude.stderr.txt')
(stage / 'INVOCATION.json').write_text(json.dumps(record, indent=2) + '\n')
parts, uses, result, init = [], [], None, None
for line in (stage / 'claude.stdout.jsonl').read_text().splitlines():
    try:
        obj = json.loads(line)
    except ValueError:
        continue
    if obj.get('type') == 'system' and obj.get('subtype') == 'init':
        init = obj
    if obj.get('type') == 'assistant':
        for item in obj.get('message', {}).get('content', []):
            if item.get('type') == 'text':
                parts.append(item['text'])
            if item.get('type') == 'tool_use':
                uses.append(item)
    if obj.get('type') == 'result':
        result = obj
report = stage / ('EXPECTATIONS.md' if source_first else 'ASSESSMENT.md')
report.write_text('\n\n'.join(parts) + '\n')
execution = {'init': init, 'result': result, 'observed_tool_uses': uses,
             'invocation': record, 'report': report.name, 'report_sha256': sha(report)}
(stage / 'EXECUTION.json').write_text(json.dumps(execution, indent=2) + '\n')
print(json.dumps({'exit_code': record['exit_code'], 'report': str(report), 'report_bytes': report.stat().st_size,
                  'result_subtype': result.get('subtype') if result else None, 'tools_used': len(uses),
                  'actual_model': init.get('model') if init else None}))
