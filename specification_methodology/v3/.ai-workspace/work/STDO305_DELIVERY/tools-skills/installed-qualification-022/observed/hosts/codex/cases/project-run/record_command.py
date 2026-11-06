"""Retain a qualification command's exact argv and output under cases only."""
import json
from pathlib import Path
import subprocess
import sys

destination = Path(sys.argv[1]).resolve()
case_root = Path(__file__).resolve().parents[1]
if not destination.is_relative_to(case_root):
    raise SystemExit("output must remain under cases")
destination.mkdir(parents=True, exist_ok=False)
argv = sys.argv[2:]
(destination / "argv.json").write_text(json.dumps(argv, indent=2) + "\n")
result = subprocess.run(argv, capture_output=True)
(destination / "stdout.txt").write_bytes(result.stdout)
(destination / "stderr.txt").write_bytes(result.stderr)
(destination / "result.json").write_text(json.dumps({"returncode": result.returncode}) + "\n")
print(json.dumps({"output": str(destination), "returncode": result.returncode}))
raise SystemExit(result.returncode)
