import json,os,sys,time
from pathlib import Path
data=sys.stdin.buffer.read()
Path(sys.argv[1]).write_bytes(data)
Path(sys.argv[2]).write_text(json.dumps({k:os.environ.get(k) for k in ('HOME','home','CODEX_HOME','AC_TEST_SETTING')}))
sys.stdout.buffer.write(b'{"thread_id":"fixture","type":"thread.started"}\n{"item":{"text":"Earlier commentary is not the final answer","type":"agent_message"},"type":"item.completed"}\n{"item":{"text":" \\n{\\"schema\\":\\"a_c.fd-support.closed-return/1\\",\\"opaque\\":\\"unchanged\\", \\"n\\":1}\\t","type":"agent_message"},"type":"item.completed"}\n{"fixture_ratio":0.25,"type":"turn.completed","usage":{"cached_input_tokens":20,"input_tokens":100,"output_tokens":30}}\n');sys.stdout.buffer.flush()
sys.stderr.buffer.write(b'fixture stderr\n');sys.stderr.buffer.flush()
time.sleep(0)
raise SystemExit(0)
