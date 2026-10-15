"""Record bounded source acquisition for I4-PROFILE-SOURCE; no source mutation."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "ACQUISITION.json"
parser = argparse.ArgumentParser()
parser.add_argument("coordinate")
parser.add_argument("ranges", help="one or more inclusive line ranges, e.g. 10:30,40:50")
args = parser.parse_args()
if ":" in args.coordinate and not args.coordinate.startswith("/"):
    raw = subprocess.check_output(["git", "show", args.coordinate])
else:
    raw = Path(args.coordinate).read_bytes()
lines = raw.decode().splitlines(keepends=True)
selected = []
for interval in args.ranges.split(","):
    first, last = map(int, interval.split(":"))
    selected.extend(lines[first - 1:last])
body = "".join(selected)
ledger = json.loads(LEDGER.read_text())
amount = len(body.encode())
used = ledger["initial_conservative_charge_bytes"] + sum(x["bytes"] for x in ledger["acquisitions"])
if used + amount > ledger["limit_bytes"]:
    raise SystemExit(f"Acquisition would exceed limit: {used} + {amount}")
ledger["acquisitions"].append({"coordinate": args.coordinate, "lines": args.ranges,
                              "bytes": amount, "source_sha256": hashlib.sha256(raw).hexdigest(),
                              "selected_sha256": hashlib.sha256(body.encode()).hexdigest()})
LEDGER.write_text(json.dumps(ledger, indent=2) + "\n")
print(body, end="")
print(f"\nACQUISITION_BYTES={amount}; CUMULATIVE_CHARGED_BYTES={used + amount}")
