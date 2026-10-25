"""Retain source preimages and immutable guards before the factual Writer edits."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import time

D = Path(__file__).resolve().parent
P = D.parents[3]
R = P.parent
I = P / ".ai-workspace/qualification/t008/interfaces/integration-004"


def h(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def save(name, value):
    with (D / name).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


admission = json.loads((D / "WRITER.admission.json").read_bytes())
assert h(I / "SOURCE_MANIFEST.json") == admission["preimage_source_manifest"]["sha256"]
source = {row["path"]: row for row in json.loads((I / "SOURCE_MANIFEST.json").read_bytes())["sources"]}
assert h(I / "CLOSED_RETURN.json") == "b895994e7c43e6c8da750828fe0899edf221988721430d0fb8a748d5d08a1175"
review = P / ".ai-workspace/comments/codex/t008-platform-code-review-003"
assert h(review / "REVIEW.md") == "e4d97b80b9973cabfba5019bc93226836733461adfb03143f38f1dd2fc2bbc7c"
assert h(review / "CLOSED_RETURN.json") == "a972ca4ccb1fbdad4f837329395507e6dd4ab310d4cfead2f6fc211164c95bbb"
before = []
allowed = {"a_c/" + path for path in admission["existing_paths"]}
for relative in admission["existing_paths"]:
    path = P / relative
    row = source["a_c/" + relative]
    assert path.is_file() and not path.is_symlink() and h(path) == row["sha256"] and path.stat().st_size == row["bytes"], relative
    target = D / "before" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    target.chmod(0o444)
    before.append({"path": relative, "sha256": h(path), "bytes": path.stat().st_size,
        "snapshot": str(target.relative_to(D)), "integration004_snapshot": row["snapshot"]})
assert len(before) == 11
save("SOURCE_BEFORE.json", {"source_manifest": admission["preimage_source_manifest"], "sources": before,
    "captured_ns": time.time_ns(), "all_11_exact_regular_preimages": True})
old_guards = json.loads((I / "GUARDS_BEFORE.json").read_bytes())["files"]
guards = {}
for row in old_guards:
    if row["path"] in allowed:
        continue
    path = R / row["path"]
    if row["kind"] == "symlink":
        assert path.is_symlink() and os.readlink(path) == row["target"], row["path"]
    else:
        assert path.is_file() and not path.is_symlink() and h(path) == row["sha256"] and path.stat().st_size == row["bytes"], row["path"]
    guards[row["path"]] = row
for root in [I, review]:
    for path in sorted(root.rglob("*")):
        key = str(path.relative_to(R))
        if path.is_symlink():
            guards[key] = {"path": key, "kind": "symlink", "target": os.readlink(path), "target_not_followed": True}
        elif path.is_file():
            guards[key] = {"path": key, "kind": "regular", "sha256": h(path), "bytes": path.stat().st_size}
save("GUARDS_BEFORE.json", {"files": [guards[key] for key in sorted(guards)],
    "authorized_existing_paths_excluded_only": sorted(allowed),
    "scope": "Immutable code/tests/helpers/profile/PD/INTENT/owner maps/method/original Graphify/studies and prior proof/review/live histories; symlink targets not followed; raw streams hashed opaquely only"})
ticket = (D / "before/.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md").read_bytes()
lines = ticket.splitlines(keepends=True)
binding = b"".join(lines[784:860])
assert len(lines) >= 860
with (D / "before/binding002.original-lines785-860.txt").open("xb") as stream:
    stream.write(binding)
save("TICKET_CUSTODY.before.json", {"full_before_sha256": hashlib.sha256(ticket).hexdigest(), "bytes": len(ticket),
    "original_prefix_52350_sha256": hashlib.sha256(ticket[:52350]).hexdigest(),
    "binding002_original_lines": [785, 860], "binding002_original_bytes_sha256": hashlib.sha256(binding).hexdigest(),
    "prefix_claim": "The full before snapshot retains the original prefix. After the two permitted navigation-line edits, that prefix is not claimed byte-exact current.",
    "binding_standing": "HISTORICAL/stale; no repin, renewal or binding003"})
save("PRE_EFFECT_CHECKS.json", {"contract_sha256": h(D / "WRITER.contract.txt"),
    "Root_reported_admission_sha256": h(D / "WRITER.admission.json"), "exact_11_preimages_retained": True,
    "immutable_guard_members": len(guards), "actual_provider_calls": 0, "tests_or_runtime_operations": 0,
    "new_work": "Factual Markdown edits and structural custody/link/permitted-diff checks only"})
print(json.dumps({"preimages": len(before), "guard_members": len(guards), "source_before_sha256": h(D / "SOURCE_BEFORE.json")}))
