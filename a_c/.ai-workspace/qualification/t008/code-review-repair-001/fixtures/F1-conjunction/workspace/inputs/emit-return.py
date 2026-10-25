import sys
from pathlib import Path
sys.stdin.buffer.read()
sys.stdout.buffer.write(Path(sys.argv[1]).read_bytes())
sys.stdout.buffer.flush()
