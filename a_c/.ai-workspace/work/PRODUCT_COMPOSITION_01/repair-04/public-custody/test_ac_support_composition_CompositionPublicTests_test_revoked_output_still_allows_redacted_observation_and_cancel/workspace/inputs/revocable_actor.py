import sys,time
from pathlib import Path
sys.stdin.buffer.read()
Path(sys.argv[1]).write_text("launched")
print("DONOR-PRIVATE-ALGORITHM",flush=True)
time.sleep(30)
