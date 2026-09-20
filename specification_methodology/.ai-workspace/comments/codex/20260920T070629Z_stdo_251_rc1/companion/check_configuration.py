"""Check exact proposed configuration shape and bounded conservation only."""
from pathlib import Path
import copy
import hashlib
import json
from jsonschema import Draft202012Validator, FormatChecker

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1")
DEST = OUT / "configuration-proposals"
PRE = OUT / "preimages"
OLD = "stdo://releases/v2.5.0-rc.7/"
NEW = "stdo://releases/v2.5.1-rc.1/"


def sha(path):
    return hashlib.sha256(str(path.readlink()).encode() if path.is_symlink() else path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inverse(value):
    if isinstance(value, str):
        return value.replace(NEW, OLD)
    if isinstance(value, list):
        return [inverse(v) for v in value]
    if isinstance(value, dict):
        return {k: inverse(v) for k, v in value.items()}
    return value


def main():
    schema = load(INSTALL / "standards/schemas/product-definition.schema.json")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    manifest = load(DEST / "manifest.json")
    require(sha(DEST / "selection-subject.json") == manifest["selection_subject_sha256"], "Selection changed")
    subject = load(DEST / "selection-subject.json")
    for row in subject["owning_sources"] + subject["release_notes"] + subject["closed_independent_assessments"] + [subject["matched_cohort"]]:
        require(sha(ROOT / row["path"]) == row["sha256"], "Selected source changed: " + row["path"])
    proposal_results = []
    for row in manifest["proposals"]:
        child = row["project"]
        candidate_path = ROOT / row["definition_proposal"]
        frame_path = ROOT / row["frame_proposal"]
        name = candidate_path.name
        old = load(PRE / child / name)
        candidate = load(candidate_path)
        errors = sorted((e.json_path + ": " + e.message for e in validator.iter_errors(candidate)))
        require(not errors, "Proposal schema errors: " + str(errors))
        restored = inverse(copy.deepcopy(candidate))
        restored["constitution"]["stdo"]["selector"] = old["constitution"]["stdo"]["selector"]
        restored["constitution"]["stdo"]["basis"]["manifest_sha256"] = old["constitution"]["stdo"]["basis"]["manifest_sha256"]
        restored["reference_frame_bases"][0]["authority"] = old["reference_frame_bases"][0]["authority"]
        require(restored == old, "Unexpected Definition semantic/shape change: " + child)
        require(sha(candidate_path) == row["definition_sha256"] and sha(frame_path) == row["frame_sha256"], "Proposal drift")
        require(sha(ROOT / child / name) == row["live_definition_sha256"], "Live Definition changed")
        require(sha(ROOT / child / "specification/REFERENCE_FRAME_BASIS.md") == row["live_frame_sha256"], "Live frame changed")
        require(not (ROOT / row["proposed_decision_path"]).exists(), "Unexpected decision promotion")
        old_frame = (PRE / child / "specification/REFERENCE_FRAME_BASIS.md").read_text()
        new_frame = frame_path.read_text()
        old_actors = [line for line in old_frame.splitlines() if line.startswith("| `K-")]
        new_actors = [line for line in new_frame.splitlines() if line.startswith("| `K-")]
        require(old_actors == new_actors, "Actor/independence contract changed")
        old_names = [line for line in old_frame.splitlines() if line.startswith("### F-")]
        new_names = [line for line in new_frame.splitlines() if line.startswith("### F-")]
        require(old_names == new_names, "Frame identity set changed")
        proposal_results.append({"project": child, "schema_errors": errors,
            "inverse_definition_basis_and_decision_change_equals_predecessor": True,
            "actor_envelopes_byte_conserved": True, "frame_identity_set_conserved": True,
            "live_definition_and_frame_preserved": True, "decision_absent": True,
            "frame_sha256": sha(frame_path), "definition_sha256": sha(candidate_path)})
    for child, inventory in (("axiom_indexer", subject["axiom_product"]),
                             ("stdo_representation", subject["representation_product"])):
        for row in inventory["members"]:
            require(sha(ROOT / child / row["path"]) == row["sha256"], "Frozen member drift: " + row["path"])
    record = {"kind": "stdo.rc1-configuration-conservation-check", "schema_version": 1,
              "status": "valid", "proposal_manifest_sha256": sha(DEST / "manifest.json"),
              "selection_subject_sha256": sha(DEST / "selection-subject.json"),
              "schema_uri": NEW + "standards/schemas/product-definition.schema.json",
              "schema_sha256": sha(INSTALL / "standards/schemas/product-definition.schema.json"),
              "proposals": proposal_results, "all_7_axiom_and_9_representation_members_unchanged": True,
              "selected_owning_sources_release_notes_and_cohort_unchanged": True,
              "claim": "Schema, exact identity and bounded conservation only. Independent configuration judgment and its authorized decision remain external."}
    (OUT / "configuration-check.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
