"""Bind independently stated expectations to reviewed frozen source bytes."""
from pathlib import Path
import json

from prepare_native import HERE, sha, write

SOURCE = Path("/Users/jim/src/apps/specification_methodology/specification_methodology")
INSTALLED = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
FREEZE = HERE.parent / "source/candidate-subject.json"
SPANS = {
    "SPEC_METHOD.md": [
        {"cases": ["A", "C"], "lines": [1465, 1472], "relation": "Proportional method work"},
        {"cases": ["C"], "lines": [1560, 1575], "relation": "Writer entry and bounded sequence"},
        {"cases": ["C"], "lines": [1617, 1636], "relation": "Preservation, restart and progress"},
        {"cases": ["A"], "lines": [1652, 1715], "relation": "Complete admission, validity-preserving reuse and supported threat"},
        {"cases": ["A"], "lines": [1981, 2008], "relation": "Retention burden and replacement closure"},
        {"cases": ["A", "B", "C"], "lines": [2121, 2128], "relation": "Ordinary-use semantic fidelity and separate mechanical observations"},
        {"cases": ["A", "C"], "lines": [2419, 2427], "relation": "Reconstruction sufficiency and reuse"}],
    "DESIGN_MODULE_METHOD.md": [
        {"cases": ["A"], "lines": [1532, 1579], "relation": "Complete computational path, owned workload and equivalence"}],
    "TICKET_METHOD.md": [
        {"cases": ["C"], "lines": [777, 817], "relation": "Judgment, ruling and obligation continuity"},
        {"cases": ["C"], "lines": [869, 890], "relation": "Condition-based closure"},
        {"cases": ["A"], "lines": [892, 913], "relation": "Test predicates need governing support"}],
    "STDO_REFERENCE_FRAME_BASELINE.md": [
        {"cases": ["A"], "lines": [645, 700], "relation": "Read/write scope and Reviewer applicability"},
        {"cases": ["B"], "lines": [1107, 1225], "relation": "T031 exact interface claims, context, cause and user evidence"},
        {"cases": ["A"], "lines": [1227, 1245], "relation": "Computational whole-path refinement"}],
}


def main():
    if (HERE / "oracle-binding.json").exists():
        raise SystemExit("Refuse overwriting oracle binding")
    freeze = json.loads(FREEZE.read_text())
    expected = {row["path"]: row["sha256"] for row in freeze["members"]}
    members = []
    for name, spans in SPANS.items():
        source = SOURCE / "specification/standards" / name
        installed = INSTALLED / "standards" / name
        digest = expected["specification/standards/" + name]
        if sha(source) != digest or sha(installed) != digest:
            raise SystemExit("Source/install drift: " + name)
        lines = source.read_text().splitlines()
        for span in spans:
            first, last = span["lines"]
            if not 1 <= first <= last <= len(lines):
                raise SystemExit("Invalid owning span")
        members.append({"path": "standards/" + name, "sha256": digest, "relations": spans})
    write(HERE / "oracle-binding.json", {"status": "bound", "source_manifest_sha256": sha(INSTALLED / "manifest.json"),
        "source_freeze_sha256": sha(FREEZE), "source_member_set_sha256": freeze["member_set_sha256"],
        "oracle_sha256": sha(HERE / "oracle.md"), "source_members": members,
        "claim": "Expected lawful decisions for the bounded native packet, source-derived before any exposure; not source or Product acceptance"})
    print(json.dumps({"source_members": len(members), "oracle_bound": True, "provider_calls": 0}))


if __name__ == "__main__":
    main()
