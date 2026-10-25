import sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(sys.stdin.buffer.read())
sys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())
sys.stdout.buffer.flush()
