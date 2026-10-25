import json,os,sys,time
from pathlib import Path
data=sys.stdin.buffer.read()
Path(sys.argv[1]).write_bytes(data)
Path(sys.argv[2]).write_text(json.dumps({k:os.environ.get(k) for k in ('HOME','home','CODEX_HOME','AC_TEST_SETTING')}))
sys.stdout.buffer.write(b'{"is_error":false,"modelUsage":{"fixture":{"costUSD":0.0123}},"result":" \\n{\\"schema\\":\\"a_c.fd-support.closed-return/1\\",\\"opaque\\":\\"unchanged\\", \\"n\\":1}\\t","subtype":"success","total_cost_usd":0.0123,"type":"result","usage":{"input_tokens":17}}');sys.stdout.buffer.flush()
sys.stderr.buffer.write(b'fixture stderr\n');sys.stderr.buffer.flush()
time.sleep(0)
raise SystemExit(0)
