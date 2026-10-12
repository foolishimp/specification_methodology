"""Apply the independently reviewed, owner-selected internal RC1 configuration."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
PROPOSALS = OUT / "companion/configuration-proposals"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


require(sha(PROPOSALS / "manifest.json") == "47e18c4734566d256b6fe56e4b4791fdac4c164082067ae041be2283fe136f06", "proposal manifest drift")
require(sha(PROPOSALS / "selection-subject.json") == "98160834808028043b0a7582ef5eb1efeb135c0105a731c4107868c610fdc1c5", "selected subject drift")
manifest = json.loads((PROPOSALS / "manifest.json").read_text())
selection = json.loads((PROPOSALS / "selection-subject.json").read_text())
source_basis = ROOT / "specification_methodology/stdo_default.json"
source_before = sha(source_basis)
require(json.loads(source_basis.read_text())["constitution"]["stdo"]["basis"]["uri"] == "stdo://releases/v2.5.0-rc.4/", "source authoring basis changed")
review = OUT / "independent-configuration-review.md"
require(review.is_file(), "independent configuration review absent")
operations = []
for row in manifest["proposals"]:
    project = ROOT / row["project"]
    live_frame = project / "specification/REFERENCE_FRAME_BASIS.md"
    live_definition = project / Path(row["definition_proposal"]).name
    decision = ROOT / row["proposed_decision_path"]
    require(not decision.exists(), "successor decision already exists")
    for key, live in (("frame", live_frame), ("definition", live_definition)):
        require(sha(live) == row["live_" + key + "_sha256"], "live configuration preimage changed")
        require(sha(ROOT / row[key + "_proposal"]) == row[key + "_sha256"], "reviewed proposal changed")
    prior_path = project / ".ai-workspace/decisions/20260915_rc7_frame_basis_acceptance.json"
    prior = json.loads(prior_path.read_text())
    value = dict(prior)
    value.update(
        subject_uri=row["frame_uri"], subject_sha256="sha256:" + row["frame_sha256"],
        definition_sha256="sha256:" + row["definition_sha256"],
        method_basis_uri="stdo://releases/v2.5.1-rc.1/standards/REFERENCE_FRAME_METHOD.md",
        actor_identity="urn:openai:codex:root:bounded-local-preparation",
        authority_mode="current-direct-owner-granted-bounded-rc1-preparation-configuration",
        decided_at=datetime.now(timezone.utc).isoformat(),
        grant_text="we can prepare 2.5.1 RC1 without any dependency",
        scope="Bind only this exact internal RC1 construction/qualification configuration and continuing-source Definition after independent conservation assessment. Preserve STDO source RC4 and external consumer pins.",
        source_stdo={"uri": selection["source_stdo"]["uri"],
                     "manifest_sha256": selection["source_stdo"]["installed_manifest_sha256"],
                     "source_ref": selection["source_stdo"]["release"]["qualified_ref"],
                     "freeze": selection["source_stdo"]["release"]},
        selected_subject={"path": "../" + str((PROPOSALS / "selection-subject.json").relative_to(ROOT)),
                          "sha256": sha(PROPOSALS / "selection-subject.json")},
        supersession_record={"prior_subject_sha256": prior["subject_sha256"],
                             "prior_decision": "./.ai-workspace/decisions/20260915_rc7_frame_basis_acceptance.json",
                             "prior_decision_sha256": "sha256:" + sha(prior_path),
                             "disposition": "Prior RC7 decision remains historical; its grant is not reused or expanded."},
        evidence_refs=[{"path": "../" + str(review.relative_to(ROOT)), "sha256": sha(review)}],
        release_relation="Internal configuration acceptance does not close native qualification or accept an immutable Product. Publication and external adoption are unselected; ABI/T-288 supplies no dependency."
    )
    value["exclusions"] = sorted(set(prior["exclusions"] + ["publication", "ABI/T-288 delivery or closure"]))
    operations.append((row, live_frame, live_definition, decision, value))

# Every precondition is checked before the first effect.
for row, live_frame, live_definition, decision, value in operations:
    put(decision, value)
    live_frame.write_bytes((ROOT / row["frame_proposal"]).read_bytes())
    live_definition.write_bytes((ROOT / row["definition_proposal"]).read_bytes())
    require(sha(live_frame) == row["frame_sha256"] and sha(live_definition) == row["definition_sha256"], "promotion byte mismatch")
require(sha(source_basis) == source_before, "source authoring basis changed")
put(OUT / "internal-configuration.json", {
    "status": "accepted_and_applied", "scope": "internal local RC1 preparation only",
    "independent_review_sha256": sha(review), "source_authoring_basis_sha256": source_before,
    "objects": [{"project": row["project"], "frame_sha256": sha(frame),
                 "definition_sha256": sha(definition), "decision": str(decision.relative_to(ROOT)),
                 "decision_sha256": sha(decision)} for row, frame, definition, decision, value in operations],
    "publication": "unselected", "external_adoption": "unselected", "abi_dependency": False
})
print("Exact internal companion configuration applied; STDO source authoring basis preserved.")

