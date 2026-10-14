"""Check exact tool identity, current sources and selected a_c mechanics.

Mechanics do not execute the program's semantic predicates. The retained finite
model checks only its already-declared small domains and is separately reported.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from refresh_current import HERE, TENANT, PACKAGE, read

ROOT = HERE / "a_c"
INSTALL = TENANT / "a_c/install/axiom_indexer-v2.5.1-rc.2"
TOOL = INSTALL / "build_tenants/core/code/ac.py"
NS = "urn:codex-stdo3:iteration-3:"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def invoke(args, expected=0):
    result = subprocess.run([sys.executable, "-B", str(TOOL), *map(str, args)], capture_output=True, text=True)
    if result.returncode != expected:
        raise RuntimeError(result.stdout + result.stderr)
    return result


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


started = time.monotonic()
receipt = read(TENANT / "a_c/INSTALL_RECEIPT.json")
for member in receipt["members"]:
    p = INSTALL / member["path"]
    assert p.is_symlink() == (member["type"] == "symlink"), member["path"]
    data = os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
    assert sha(data) == member["sha256"], member["path"]
    assert data == subprocess.check_output(["git", "show", "9a9c479776ffd974fbcafcf48341980918209aef:axiom_indexer/" + member["path"]], cwd=TENANT)
assert sha(TOOL.read_bytes()) == "5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8"
inventory = read(HERE / "CANDIDATE.json")
assert inventory["candidate_body_input_commit"], "Freeze source before qualification"
for member in inventory["members"]:
    assert sha((PACKAGE / member["path"]).read_bytes()) == member["sha256"], member["path"]

invoke(["validate", "--program", ROOT / "program.json", "--bindings", ROOT / "bindings.json",
        "--output", ROOT / "validation.json", "--emit-map", ROOT / "map.json"])
base = ["project", "--program", ROOT / "program.json", "--map", ROOT / "map.json", "--bindings", ROOT / "bindings.json",
        "--frame-index", NS + "index:constraint-application"]
projections = []
for mode in ("reference-only", "materialized"):
    dest = ROOT / ("projection-" + mode + ".json")
    invoke(base + ["--mode", mode, "--output", dest])
    projections.append(read(dest))
for key in ("closure", "clause_relations", "residual_routes", "source_routes"):
    assert projections[0][key] == projections[1][key], key
program = read(ROOT / "program.json")
roots = next(f["clause_refs"] for f in program["frame_indexes"] if f["uri"].endswith(":constraint-application"))
assert set(roots) < set(projections[0]["closure"]["clauses"])
# The shared-law frame is not a domain decision frame. Its selected residual
# states the missing domain binding instead of dragging every family's clauses
# into the acquisition solely through residual subject links.
closure = projections[0]["closure"]["clauses"]
assert not any(":clause:consumer-" in uri for uri in closure)
assert len(closure) < len(program["clauses"])

mutant = json.loads(json.dumps(program))
mutant["clauses"][0]["statement"] += " Altered after map generation."
write("program-map-drift-mutant.json", mutant)
negative = subprocess.run([sys.executable, "-B", str(TOOL), "project", "--program", str(ROOT / "program-map-drift-mutant.json"),
    "--map", str(ROOT / "map.json"), "--bindings", str(ROOT / "bindings.json"), "--mode", "reference-only",
    "--frame-index", NS + "index:constraint-application"], capture_output=True, text=True)
diagnostic = json.loads(negative.stdout)
assert negative.returncode != 0 and any(d["code"] == "map_mismatch" for d in diagnostic["diagnostics"])
write("MAP_DRIFT_REFUSAL.json", diagnostic)

sections = [{"label": "Source scope and interpretation limits", "text": (ROOT / "SOURCE.md").read_text()},
            {"label": "Current constraint closure", "text": json.dumps(projections[1], indent=2)}]
write("sections.json", sections)
invoke(["join", "--input", ROOT / "sections.json", "--output", ROOT / "JOINED.txt"])
assert (ROOT / "JOINED.txt").read_text() == "\n\n".join(s["label"] + "\n" + s["text"] for s in sections)
report = {"valid": True, "source_commit": inventory["candidate_body_input_commit"],
          "tool_members_verified": len(receipt["members"]), "tool_sha256": sha(TOOL.read_bytes()),
          "clauses": len(program["clauses"]), "symbols": len(program["symbols"]), "indexes": len(program["frame_indexes"]),
          "residuals": len(program["residuals"]), "closure_clauses": len(closure),
          "shared_frame_excludes_domain_consumers": True,
          "projection_parity": True, "map_drift_refused": True, "exact_join": True,
          "elapsed_seconds": time.monotonic() - started,
          "limits": ["Selected textual interpretation; source fidelity needs independent evidence.",
                     "No general semantic admission engine, whole-method proof or release acceptance."]}
write("MECHANICAL_RESULT.json", report)
print(json.dumps(report))
