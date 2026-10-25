"""Selected finite fixture: run one exact CLI request, withhold caller stdout.

This is a real local response boundary, not a simulated model, a tool override,
or an assertion that a timeout rolled an effect back. The recording consumer
retains the child response for subsequent reconciliation; the caller receives
no acknowledgment before this process terminates with code 86.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

p = argparse.ArgumentParser()
p.add_argument("--plan", type=Path, required=True)
p.add_argument("--sha256", required=True)
args = p.parse_args()
raw = args.plan.read_bytes()
if hashlib.sha256(raw).hexdigest() != args.sha256:
    raise SystemExit("Selected fixture plan changed")
plan = json.loads(raw)
for dependency in plan["dependencies"]:
    if hashlib.sha256(Path(dependency["path"]).read_bytes()).hexdigest() != dependency["sha256"]:
        raise SystemExit("Selected fixture dependency changed")
result = subprocess.run(plan["argv"], capture_output=True, timeout=30, env=plan["environment"])
root = Path(plan["record_directory"])
root.mkdir(exist_ok=False)
(root / "child.stdout").write_bytes(result.stdout)
(root / "child.stderr").write_bytes(result.stderr)
(root / "TRANSPORT.json").write_text(json.dumps({
    "schema": "stdo_skills.withheld-ack-observation/1",
    "child_returncode": result.returncode,
    "child_stdout_bytes": len(result.stdout),
    "child_stderr_bytes": len(result.stderr),
    "forwarded_caller_stdout_bytes": 0,
    "boundary": "Child completed; this local transport terminates before forwarding its acknowledgment",
    "caller_transport_returncode": 86,
    "response_record": "child.stdout",
    "semantic_effect": "Read actual child response and target; not inferred from this transport record",
}, indent=2) + "\n")
sys.exit(86)
