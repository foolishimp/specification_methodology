#!/usr/bin/env python3
"""Read-only bounded frame/package/link checks for the four-reference trace repair."""
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
for relative, expected in json.loads((here / "TOOL_PINS.json").read_text()).items():
    if digest((checkout / relative).read_bytes()) != expected:
        raise SystemExit("Tool digest mismatch: " + relative)

def run(arguments, parse=False):
    result = subprocess.run(arguments, cwd=checkout, text=True, capture_output=True)
    if result.returncode:
        raise SystemExit(result.stdout + result.stderr)
    return json.loads(result.stdout) if parse else result.stdout

frames = v3 / ".ai-workspace/common-build/frame-tools/generate_frames.py"
run([sys.executable, "-I", str(frames), "--root", str(native), "--check"])
inventory = here / "NATIVE_INVENTORY.json"
expected_inventory = "bf45dfbe466f0440c958c4be3415257b319bb8c6d0b0a06cf7c2a18f168e44a6"
if digest(inventory.read_bytes()) != expected_inventory:
    raise SystemExit("Native inventory changed")
package = v3 / ".ai-workspace/common-build/tools/package_tools.py"
report = run([sys.executable, "-I", str(package), "check", "--root", str(native),
              "--inventory", str(inventory), "--inventory-sha256", expected_inventory], True)
run(["git", "diff", "--check", "--", str(native)])
print(json.dumps({"frame_reproduction": "passed",
                  "tool_authentication": "passed before subprocess execution",
                  "package_valid": report["valid"], "package_failures": report["failures"],
                  "local_references": report["checked_local_reference_count"],
                  "inventory_sha256": expected_inventory,
                  "frame_bytes_max": max(p.stat().st_size for p in (native / "standards/frames").glob("*.md")),
                  "executable_examples": "unchanged bytes; repair-1 finite evidence retained, not rerun",
                  "standing": "bounded author checks; no new independent semantic acceptance"}, indent=2))
