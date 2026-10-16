"""Read and meter selected frozen headings for the routing activation."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

out = Path(__file__).resolve().parent
coordinate, *headings = sys.argv[1:]
raw = subprocess.check_output(["git", "show", coordinate])
text = raw.decode()
matches = list(re.finditer(r"^#{1,6} .+$", text, re.M))
selected = []
for index, match in enumerate(matches):
    if match.group() in headings:
        selected.append(text[match.start():matches[index + 1].start() if index + 1 < len(matches) else len(text)])
if len(selected) != len(headings):
    raise SystemExit("One or more exact headings did not resolve")
body = "\n".join(selected)
ledger_path = out / "ACQUISITION.json"
ledger = json.loads(ledger_path.read_text())
used = ledger["initial_conservative_charge_bytes"] + sum(x["bytes"] for x in ledger["acquisitions"])
amount = len(body.encode())
assert used + amount <= ledger["limit_bytes"]
ledger["acquisitions"].append({"coordinate": coordinate, "headings": headings, "bytes": amount,
                               "source_sha256": hashlib.sha256(raw).hexdigest(),
                               "selected_sha256": hashlib.sha256(body.encode()).hexdigest()})
ledger_path.write_text(json.dumps(ledger, indent=2) + "\n")
print(body)
print("CHARGED_BYTES", used + amount)
