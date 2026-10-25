import sys,hashlib
from pathlib import Path
raw=sys.stdin.buffer.read()
value=hashlib.sha256(raw).hexdigest()
Path(sys.argv[1]).write_text(value)
print(value)
