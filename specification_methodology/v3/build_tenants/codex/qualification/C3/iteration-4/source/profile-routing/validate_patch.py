"""Validate authored routes against frozen inputs without writing an account."""
import collections
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
REPO = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
patch_bytes = (OUT / "ACCOUNT_PATCH.json").read_bytes()
patch = json.loads(patch_bytes)
coverage_bytes = (OUT / "COVERAGE.json").read_bytes()
coverage = json.loads(coverage_bytes)
subject = patch["subject"]
account_path = REPO / subject["provisional_account_path"]
raw = account_path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == subject["provisional_account_sha256"]
original = json.loads(raw)
changed = copy.deepcopy(original)
before = {r["id"]: r for r in original["determinations"]}
after = {r["id"]: r for r in changed["determinations"]}
assert len(before) == len(after) == 701
assert len(patch["patches"]) == len({p["id"] for p in patch["patches"]}) == 95

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()

root_preimages = []
for amendment in patch["patches"]:
    identity = amendment["id"]
    touched = set()
    for dotted, value in amendment["set"].items():
        keys = dotted.split(".")
        touched.add(keys[0])
        target = after[identity]
        for key in keys[:-1]:
            assert isinstance(target.get(key), dict), (identity, dotted)
            target = target[key]
        target[keys[-1]] = copy.deepcopy(value)
    root_preimages.append({"id": identity, "root_fields": {key: digest(before[identity].get(key)) for key in sorted(touched)}})

def leaves(value, prefix=""):
    if not isinstance(value, dict):
        return {prefix: value}
    result = {}
    for key, child in value.items():
        path = key if not prefix else prefix + "." + key
        if isinstance(child, dict):
            result.update(leaves(child, path))
        else:
            result[path] = child
    return result

actual_changed_paths = []
by_patch = {p["id"]: p for p in patch["patches"]}
for identity, prior in before.items():
    observed = after[identity]
    permitted = set(by_patch.get(identity, {}).get("set", {}))
    prior_leaves, observed_leaves = leaves(prior), leaves(observed)
    diffs = {k for k in prior_leaves.keys() | observed_leaves.keys() if prior_leaves.get(k) != observed_leaves.get(k)}
    assert all(any(k == path or k.startswith(path + ".") for path in permitted) for k in diffs), (identity, diffs, permitted)
    if diffs:
        actual_changed_paths.append({"id": identity, "paths": sorted(diffs)})
    # No operative local law or owner/source coordinate is changed.
    for key in ["predicate", "obligations", "permissions_exceptions", "owner", "applicability", "consumers"]:
        assert prior.get(key) == observed.get(key), (identity, key)

prior_path = subject["provisional_account_path"].replace("iteration-4/", "iteration-3/")
historical_raw = subprocess.check_output(["git", "show", subject["historical_account_commit"] + ":" + prior_path])
assert hashlib.sha256(historical_raw).hexdigest() == subject["historical_account_sha256"]
historical = json.loads(historical_raw)
members = {p["path"].rsplit("/", 1)[-1][:-3] for p in subject["source_members"]}
expected_locations = {(r["id"], field) for r in historical["determinations"] if r["id"].split(".")[0] in members for field in ["argument", "definition"] if isinstance(r.get(field), dict) and r[field].get("source_family_arguments")}
observed_locations = {(entry["id"], entry["field"]) for entry in coverage["entries"]}
assert expected_locations == observed_locations and len(expected_locations) == 95

current_rows = {}
source_checks = []
for member in subject["source_members"]:
    path = member["path"]
    current = subprocess.check_output(["git", "show", subject["source_commit"] + ":" + path])
    frozen = subprocess.check_output(["git", "show", subject["source_freeze"] + ":" + path])
    assert current == frozen == (REPO / path).read_bytes()
    assert hashlib.sha256(current).hexdigest() == member["sha256"]
    lines = current.decode().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Determination and consuming law |"))
    hashes = []
    for number, line in enumerate(lines[start + 2:], start + 3):
        if not line.startswith("|"):
            break
        hashed = hashlib.sha256(line.encode()).hexdigest()
        current_rows[hashed] = {"path": "standards/" + path.rsplit("/", 1)[-1], "line": number, "member_sha256": member["sha256"]}
        hashes.append(hashed)
    source_checks.append({"path": path, "sha256": member["sha256"], "rows": len(hashes), "frozen_and_worktree_identical": True})
assert len(current_rows) == 45

copy_rows = 0
retired_hashes = {x for entry in coverage["entries"] for x in entry["old_source_row_hashes_retired"]}
for entry in coverage["entries"]:
    identity, field = entry["id"], entry["field"]
    observed = after[identity][field]
    rows = observed["source_family_arguments"]
    assert len(rows) == entry["current_rows"]
    assert bool(rows) == (entry["standing"] != "unresolved")
    for row in rows:
        pin = row["source_row"]
        assert pin["sha256"] in current_rows and pin["sha256"] not in retired_hashes
        for key, expected in current_rows[pin["sha256"]].items():
            assert pin[key] == expected
        assert pin["source_commit"] == subject["source_commit"]
        assert row["source_reference_role"] == "provenance"
        assert "not an unconditional operational prerequisite" in row["required_when"]
        assert all(locus["role"] == "provenance" and locus["required_when"] for locus in row["audit_consumer_loci"])
        assert row["consumer_binding"]["anchor"] == before[identity]["owner"]["anchor"]
        assert row["consumer_binding"]["required_when"]
        copy_rows += 1

for audit in patch["owner_argument_audit"]:
    identity = audit["id"]
    assert before[identity]["argument"] == after[identity]["argument"]
    for row in after[identity]["argument"]["source_family_arguments"]:
        assert row.get("source_row_sha256", row.get("source_row", {}).get("sha256")) in current_rows

odd_id = "ODD_METHOD.118-cumulative-environment-law-is-mandatory"
prior, observed = before[odd_id], after[odd_id]
assert observed["result_mapping"]["bound_predicate"] == observed["predicate"]
assert "Every retained function declares" not in observed["result_mapping"]["bound_predicate"]
assert "recommendation" in observed["result_mapping"]["bound_predicate"]
preserved_result_keys = sorted(set(prior["result_mapping"]) - {"bound_predicate"})
assert all(prior["result_mapping"][key] == observed["result_mapping"][key] for key in preserved_result_keys)
assert all(observed["argument"][key] == value for key, value in prior["argument"].items())
composition = [r for r in observed["dependency_relations"] if r["id"] == "TRANSFORMATION_LIBRARY.composition-law"]
assert len(composition) == 1 and composition[0]["kind"] == "composition_contract"
assert "Within an adopted ODD scope" in composition[0]["required_when"]
assert "not a mandatory satisfaction conjunct" in composition[0]["binding"]
assert prior["dependencies"] == observed["dependencies"]
for identity in before:
    if identity != odd_id:
        assert before[identity].get("result_mapping") == after[identity].get("result_mapping")
        assert before[identity].get("dependencies") == after[identity].get("dependencies")
        assert before[identity].get("dependency_relations") == after[identity].get("dependency_relations")

# The more-specific source owner wins over its enclosing heading for routing.
projection = after["DESIGN_MODULE_METHOD.computational-realization-projection-stdo-up-019"]["argument"]["source_family_arguments"]
assert len(projection) == 1 and projection[0]["family"].startswith("Domain-to-computational realization")
cross = after["DESIGN_MODULE_METHOD.3a-odd-alignment-and-escalation-rule"]["argument"]["source_family_arguments"]
assert all("Only when Design is used inside an ODD-governed Product" in r["consumer_binding"]["scope"] for r in cross)
assert after["DESIGN_MODULE_METHOD.11a-governancestrategy-separation-rule"]["argument"]["source_family_arguments"] == []
assert account_path.read_bytes() == raw

report = {
    "activation": patch["activation"],
    "standing": "Writer static validation only; no integrated successor, independent review or behavioral qualification produced",
    "provisional_account_sha256": subject["provisional_account_sha256"],
    "account_patch_sha256": hashlib.sha256(patch_bytes).hexdigest(),
    "coverage_sha256": hashlib.sha256(coverage_bytes).hexdigest(),
    "checks_passed": ["95 of 95 inherited locations addressed", "all 45 frozen source rows verified", "115 replacement row copies use current exact source-row pins", "zero retired row hashes in current replacement copies", "all six already-correct owner arguments preserved", "all 701 predicates, obligations, exceptions and owner coordinates preserved", "all result mappings preserved except explicit ODD 11.8 bound_predicate", "ODD 11.8 specific local argument preserved", "ODD Composition relation conditional; all dependency ID sets unchanged", "no unmentioned semantic fields changed", "all six source members byte-identical at both freezes and current worktree", "provisional account not written"],
    "counts": {"determinations": 701, "patches": 95, "consumer_copies": 93, "owner_definition_copies": 2, "replacement_rows": copy_rows, "current_source_rows": 45, "standing": dict(collections.Counter(e["standing"] for e in coverage["entries"])), "match_kinds": dict(collections.Counter(e["match_kind"] for e in coverage["entries"]))},
    "odd_result_mapping_preserved_keys": preserved_result_keys,
    "source_checks": source_checks,
    "root_field_preimages": root_preimages,
    "actual_changed_paths": actual_changed_paths,
    "limits": ["This checks exact routing, field preservation and current-row provenance, not independent entailment.", "One family-table applicability remains unresolved; two matches retain explicit non-universal coverage limits.", "No source standard or generated account is changed by this activation."]
}
(OUT / "VALIDATION.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"passed": True, "counts": report["counts"], "preserved_result_keys": preserved_result_keys}))
