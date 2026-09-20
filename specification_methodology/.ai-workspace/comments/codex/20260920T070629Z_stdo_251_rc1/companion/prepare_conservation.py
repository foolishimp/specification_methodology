"""Freeze the admitted companion preimage without Git or Product effects.

This preparation helper records exact bytes. It neither ratifies meaning nor
supplies a future release, configuration or publication decision.
"""
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
PREVIOUS = "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7"


def sha(content):
    return hashlib.sha256(content).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def member_bytes(path):
    return str(path.readlink()).encode() if path.is_symlink() else path.read_bytes()


def main():
    destination = OUT / "preimage.json"
    require(not destination.exists(), "Preserve the existing preimage record")
    cohort_path = ROOT / "stack_release.json"
    cohort = json.loads(cohort_path.read_text())
    axiom = cohort["products"]["axiom_indexer"]["subject"]
    require(axiom["member_count"] == len(axiom["members"]) == 7,
            "Expected the complete seven-member generic Axiom Product")
    for row in axiom["members"]:
        path = ROOT / "axiom_indexer" / row["path"]
        require(sha(member_bytes(path)) == row["sha256"],
                "Axiom member differs from the selected cohort: " + row["path"])
    paths = ["stack_release.json"]
    for child, definition in (("axiom_indexer", "stdo_default.json"),
                              ("stdo_representation", "stdo_representation.json")):
        paths.extend(f"{child}/{p}" for p in [
            "README.md", "QUICKSTART.md", "specification/GOALS.md",
            "specification/PRODUCT.md", "specification/REFERENCE_FRAME_BASIS.md",
            definition, ".ai-workspace/decisions/20260915_rc7_frame_basis_acceptance.json"])
    paths.extend("stdo_representation/" + p for p in [
        "build_tenants/axiom_indexer/README.md",
        "build_tenants/axiom_indexer/FRAME_INDEX_PROJECTIONS.md",
        "skills/stdo-representation/SKILL.md",
        "skills/stdo-representation/references/frame-index-use.md",
        "specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
        *[f"{PREVIOUS}/{name}.json" for name in [
            "axiomatic-program", "logical-constraint-map", "source-corpus", "validation-report"]]])
    rows = []
    for relative in sorted(paths):
        source = ROOT / relative
        if not source.exists():
            require(relative.endswith("/QUICKSTART.md"), "Unexpected missing preimage: " + relative)
            rows.append({"path": relative, "absent": True})
            continue
        content = source.read_bytes()
        copy = OUT / "preimages" / relative
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_bytes(content)
        rows.append({"path": relative, "sha256": sha(content), "bytes": len(content),
                     "preimage": str(copy.relative_to(OUT))})
    record = {
        "kind": "stdo.rc1-companion-preimage", "schema_version": 1,
        "basis": "v2.5.0-rc.7", "candidate_version": "2.5.1-rc.1",
        "axiom_product": axiom,
        "axiom_disposition": "All seven members must remain byte-identical, including symlink targets.",
        "files": rows,
        "configuration_disposition": "Live child Definitions and accepted frame declarations remain unchanged until separately assessed successor proposals and a recorded exact configuration decision.",
        "claim": "Preimage and conservation subject only; no semantic or Product acceptance."
    }
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"record": str(destination.relative_to(ROOT)),
                      "sha256": sha(destination.read_bytes()), "files": len(rows),
                      "axiom_members_verified": len(axiom["members"])}))


if __name__ == "__main__":
    main()
