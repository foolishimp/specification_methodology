#!/usr/bin/env python3
"""Read-only reproduction of the bounded source checks, with tool authentication."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


here = Path(__file__).resolve().parent
v3 = here.parents[4]
checkout = v3.parents[1]
native = v3 / "build_tenants/common"
digest = lambda data: hashlib.sha256(data).hexdigest()
pins = json.loads((here / "TOOL_PINS.json").read_text())
for relative, expected in pins.items():
    actual = digest((checkout / relative).read_bytes())
    if actual != expected:
        raise SystemExit("Tool digest mismatch: " + relative)


def run(arguments, parse=False):
    result = subprocess.run(arguments, cwd=checkout, text=True, capture_output=True)
    if result.returncode:
        raise SystemExit(result.stdout + result.stderr)
    return json.loads(result.stdout) if parse else result.stdout


finite = run([sys.executable, "-I", str(native / "standards/examples/deterministic_contracts.py")], True)
frames = v3 / ".ai-workspace/common-build/frame-tools/generate_frames.py"
run([sys.executable, "-I", str(frames), "--root", str(native), "--check"])
inventory = here / "NATIVE_INVENTORY.json"
expected_inventory = "0277fc407eb6f14deda3398a2cc245a89a22b3e79473e347ca48265a3b123737"
if digest(inventory.read_bytes()) != expected_inventory:
    raise SystemExit("Native inventory changed")
package = v3 / ".ai-workspace/common-build/tools/package_tools.py"
report = run([sys.executable, "-I", str(package), "check", "--root", str(native),
              "--inventory", str(inventory), "--inventory-sha256", expected_inventory], True)
run(["git", "diff", "--check"])
print(json.dumps({"finite": finite, "frame_reproduction": "passed",
                  "tool_authentication": "passed before subprocess execution",
                  "package_valid": report["valid"],
                  "package_failures": report["failures"],
                  "local_references": report["checked_local_reference_count"],
                  "inventory_sha256": expected_inventory,
                  "standing": "bounded author checks; no independent semantic acceptance"}, indent=2))
