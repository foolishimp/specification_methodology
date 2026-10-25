import sys,subprocess,hashlib
from pathlib import Path
sys.stdin.buffer.read()
a=sys.argv[1:]
i=a.index("--policy")
a[i:i]=["--policy-sha256",hashlib.sha256(Path(a[i+1]).read_bytes()).hexdigest()]
r=subprocess.run(a,capture_output=True)
sys.stdout.buffer.write(r.stdout)
sys.exit(r.returncode)
