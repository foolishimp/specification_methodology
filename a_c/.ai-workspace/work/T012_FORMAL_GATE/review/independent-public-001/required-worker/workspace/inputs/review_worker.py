import hashlib,json,sys
from pathlib import Path
data=sys.stdin.buffer.read()
Path(sys.argv[1]).write_bytes(data)
print(json.dumps({"stdin_sha256":hashlib.sha256(data).hexdigest(),"stdin_bytes":len(data)}))
