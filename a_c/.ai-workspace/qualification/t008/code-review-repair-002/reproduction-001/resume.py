"""Reuse already completed fixture return transport; do not launch it again."""
import json
from pathlib import Path
import reproduce as r

case = r.Case.__new__(r.Case)
case.root = r.ROOT / "fixtures/R1-inherited-new-constraint"
case.sequence = 100
case.version = 3
case.python = Path(r.sys.executable).resolve()
case.policy = case.root / "policy-3.json"
case.policy_sha = r.sha(case.policy)
f = r.Fixture.__new__(r.Fixture)
f.base = case.root
f.workspace = case.root / "workspace"
f.authorities = case.root / "authorities"
f.evidence = case.root / "evidence"
f.policy = json.loads(case.policy.read_bytes())
f.law = f.policy["grants"]["work"]["outcome"]["source"]
f.owner = f.policy["product"]["authority_binding"]["owner_record"]
f.data = f.ref(f.workspace / "inputs/data.json", "workspace", "inputs/data.json")
completed = []
for folder in sorted((case.root / "calls").glob("*-return.capture")):
    response = json.loads((folder / "stdout.bin").read_bytes())
    value = case.ok(response)
    assert value["producer"]["authenticated"] and value["binding_checks"]["format_valid"]
    completed.append({"ref": response["result"]["artifact"], "original": value["original"], "attempt": value["attempt"]})
assert len(completed) == 2
f.subject = completed[0]["original"]["subject"]
f.basis = completed[0]["original"]["basis"]
case.f = f
results = {"R1": r.conjunction(case, completed), "R2": []}
for transport in ("cli", "mcp"):
    for variant in ("exact", "changed-record"):
        results["R2"].append(r.writer(variant, transport))
for variant in ("intact-conflict", "changed-policy", "uncertain-exact", "uncertain-changed", "uncertain-owner-loss", "uncertain-before-owner-changed"):
    results["R2"].append(r.writer(variant))
r.save(r.ROOT / "RESULTS.json", results)
print(json.dumps({"R1": "outer/depth2 inherited exact-P counterexample incorrectly S", "R2_cases": len(results["R2"]), "standing": "Both residuals reproduced on frozen Product; existing two actual scripted return refs reused, no new actor launch."}))
