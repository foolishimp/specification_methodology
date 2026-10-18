"""Re-execute the retained cold identity verifier on the current package.

The verifier operates on a temporary publication fixture. It supplies no
native installed-v3 admission or release acceptance evidence.
"""
import hashlib
import json
import time
from refresh_current import HERE, PREVIOUS, PACKAGE, load_module, read


started = time.monotonic()
owner = PREVIOUS / "synthesis/derivation_material.py"
helper = load_module("iteration3_derivation", owner)
inventory = read(HERE / "CANDIDATE.json")
assert inventory["candidate_body_input_commit"]
for member in inventory["members"]:
    assert hashlib.sha256((PACKAGE / member["path"]).read_bytes()).hexdigest() == member["sha256"]
report = helper.test(PACKAGE)
report.update({
    "source_commit": inventory["candidate_body_input_commit"],
    "verifier_sha256": hashlib.sha256(owner.read_bytes()).hexdigest(),
    "elapsed_seconds": time.monotonic() - started,
})
(HERE / "IDENTITY_CHECK.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"valid": report["valid"], "negative_controls": len(report["negative_controls"]),
                  "source_commit": report["source_commit"], "elapsed_seconds": report["elapsed_seconds"]}))
