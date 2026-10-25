import sys,hashlib
from pathlib import Path
raw=sys.stdin.buffer.read()
Path(sys.argv[1]).write_text(hashlib.sha256(raw).hexdigest())
