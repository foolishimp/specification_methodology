import json,os,sys,time
from pathlib import Path
data=sys.stdin.buffer.read()
Path(sys.argv[1]).write_bytes(data)
Path(sys.argv[2]).write_text(json.dumps({k:os.environ.get(k) for k in ('HOME','home','CODEX_HOME','AC_TEST_SETTING')}))
sys.stdout.buffer.write(b'{"is_error":false,"result":"{\\"schema\\":\\"a_c.fd-support.closed-return/1\\",\\"n\\":1e0}","subtype":"success","type":"result"}');sys.stdout.buffer.flush()
sys.stderr.buffer.write(b'fixture stderr\n');sys.stderr.buffer.flush()
time.sleep(0)
raise SystemExit(0)
