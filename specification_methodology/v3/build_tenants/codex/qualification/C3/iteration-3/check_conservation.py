"""Check the current authored conservation map; coordinates are not semantic proof.

Only the optional report output is written. Negative controls mutate in-memory
copies. Section claims end at the next heading of ANY level, as the common
inventory requires; frame excerpt subtree extraction is a different operation.
"""
import argparse
import copy
from functools import lru_cache
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / "successor"
REPO = TENANT.parents[3]
COMMON_INPUT = "355aa8655cca9c6ba6cf5c414f9bea3032ae89fd"
PREIMAGE = "1ea382a283247fe1658e9d75d9570dd2682cf13d"
PRIOR = "3ad1fca31dc93ba0847bbbbf308312a554daa1f6"
BUILDER_SHA = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
INSTALLED = Path.home() / "Library/Application Support/STDO/releases/v2.5.1-rc.2"
COMMON_PATH = "specification_methodology/v3/specification/requirements/PREDECESSOR_CLAIMS.md"
OLD_MAP_PATH = "specification_methodology/v3/build_tenants/codex/qualification/C3/CONSERVATION.json"
spec = importlib.util.spec_from_file_location("conservation_coordinates", HERE.parent / "synthesis/check_artifacts.py")
coordinates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coordinates)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()


@lru_cache(maxsize=2048)
def git_bytes(commit, path):
    return subprocess.check_output(["git", "show", commit + ":" + path], cwd=REPO)


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key: " + key)
        result[key] = value
    return result


def read(path):
    return json.loads(path.read_text(), object_pairs_hook=strict_pairs)


@lru_cache(maxsize=128)
def heading_rows(text):
    return coordinates.headings(text)


@lru_cache(maxsize=128)
def anchor_names(text):
    return {h["anchor"] for h in heading_rows(text)} | set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))


@lru_cache(maxsize=2048)
def section_body(text, anchor):
    """Return one inventory section, excluding all child/sibling sections."""
    if not anchor:
        return text
    anchor = anchor.lstrip("#")
    headings = heading_rows(text)
    positions = [i for i, h in enumerate(headings) if h["anchor"] == anchor]
    if not positions:
        # An explicit alias immediately before a heading names that heading.
        # It does not select the preceding inventory row or a whole subtree.
        aliases = list(re.finditer(r'<a\s+(?:id|name)=["\']' + re.escape(anchor) + r'["\'][^>]*></a>', text))
        if len(aliases) == 1:
            alias = aliases[0]
            positions = [i for i, h in enumerate(headings)
                         if h["offset"] >= alias.end() and not text[alias.end():h["offset"]].strip()]
    if len(positions) != 1:
        raise ValueError("missing or ambiguous section: " + anchor)
    i = positions[0]
    end = headings[i + 1]["offset"] if i + 1 < len(headings) else len(text)
    return text[headings[i]["offset"]:end]


def semantic_payload(mapping):
    value = copy.deepcopy(mapping)
    for key in ("candidate_source_commit", "pin_state", "successor_member_pins", "successor_locus_pins", "semantic_sha256"):
        value.pop(key, None)
    for row in value["rows"]:
        row.pop("successor_sha256", None)
    return value


def semantic_sha(mapping):
    return sha(canonical(semantic_payload(mapping)))


def frontier_for(mapping):
    return {"kind": "stdo.current-author-frontier", "input_commit": mapping["input_commit"],
            "candidate_source_commit": mapping["candidate_source_commit"], "pin_state": mapping["pin_state"],
            "semantic_sha256": mapping["semantic_sha256"], "row_count": len(mapping["rows"]),
            "standing": "Exact projection of current authored rows; proposals and unresolved proof are not acceptance.",
            "rows": copy.deepcopy(mapping["rows"])}


def historical_changes():
    before = json.loads(git_bytes("a746559", OLD_MAP_PATH))
    after = json.loads(git_bytes(PRIOR, OLD_MAP_PATH))
    old = {r["id"]: r for r in before["rows"]}
    return [{"id": r["id"], "before": old[r["id"]]["disposition"], "after": r["disposition"]}
            for r in after["rows"] if old[r["id"]]["disposition"] != r["disposition"]]


def validate(mapping, frontier, ports, require_frozen=False):
    failures = []

    def fail(code, detail):
        failures.append({"code": code, "detail": detail})

    expected = coordinates.common_rows(git_bytes(COMMON_INPUT, COMMON_PATH).decode())
    preimage = json.loads(git_bytes(PREIMAGE, str((HERE / "CONSERVATION.json").relative_to(REPO))))
    rows = mapping.get("rows", [])
    ids = [r.get("id") for r in rows]
    if len(ids) != 691 or len(set(ids)) != 691 or set(ids) != set(expected):
        fail("row_identity", "Expected exactly the selected 691 unique stable predecessor IDs")
    if ids != [r["id"] for r in preimage["rows"]]:
        fail("row_order", "Stable predecessor row order changed")
    for field in ("historical_qualification", "round_1", "historical_author_map_input_commit"):
        if mapping.get(field) != preimage.get(field):
            fail("historical_fact", field)
    if mapping.get("input_commit") != COMMON_INPUT or mapping.get("builder_manifest_sha256") != BUILDER_SHA:
        fail("basis", "Wrong selected common input or installed builder")
    if mapping.get("semantic_sha256") != semantic_sha(mapping):
        fail("semantic_digest", "Authored semantic payload changed without its explicit integrity digest")
    if mapping.get("port_account_semantic_sha256") != sha(canonical(ports)):
        fail("port_integrity", "Current port account differs from the authored map binding")
    if frontier != frontier_for(mapping):
        fail("frontier", "FRONTIER is not the exact current-map projection")
    if mapping.get("history_correction", {}).get("changes") != historical_changes():
        fail("history", "Current correction does not retain the 34 actual historical changes")
    original_draft = HERE / "DISPOSITION_REVISIONS.json"
    if sha(original_draft.read_bytes()) != mapping.get("draft_integration", {}).get("input_sha256"):
        fail("draft_input", "Preserved draft revisions differ from the evaluated input")
    draft_ids = set(read(original_draft)["rows"])
    proposals = read(original_draft)["rows"]
    integration = mapping.get("draft_integration", {}).get("rows", [])
    if len(integration) != 47 or {x.get("id") for x in integration} != draft_ids:
        fail("draft_coverage", "The exact 47 draft proposals are not each accounted once")
    by_id = {r.get("id"): r for r in rows}
    for decision in integration:
        row = by_id.get(decision.get("id"), {})
        if decision.get("current_disposition") != row.get("disposition") or not decision.get("assessment"):
            fail("draft_decision", str(decision.get("id")))
        if decision.get("prior_recorded_disposition") != proposals.get(decision.get("id"), {}).get("prior_disposition"):
            fail("draft_history", str(decision.get("id")))

    files = {}
    locus_pins = {}

    def inspect(locus):
        if not isinstance(locus, str):
            raise ValueError("locus must be a string")
        if locus in locus_pins:
            return locus_pins[locus]
        name, _, anchor = locus.partition("#")
        path = coordinates.confined(PACKAGE, name)
        if not name or not path.is_file():
            raise ValueError("missing successor file: " + name)
        if name not in files:
            data = path.read_bytes()
            text = data.decode() if anchor or path.suffix == ".md" else None
            files[name] = {"sha256": sha(data), "bytes": len(data), "text": text}
        entry = files[name]
        if anchor and anchor not in anchor_names(entry["text"]):
            raise ValueError("missing successor anchor: " + locus)
        body = section_body(entry["text"], anchor).encode() if anchor else path.read_bytes()
        pin = {"file_sha256": entry["sha256"], "section_sha256": sha(body), "section_bytes": len(body)}
        locus_pins[locus] = pin
        return pin

    bindings = mapping.get("consumer_bindings", {})
    for key, binding in bindings.items():
        for locus in binding.get("loci", []):
            try:
                inspect(locus)
            except (ValueError, OSError, UnicodeError) as error:
                fail("binding_locus", key + ": " + str(error))
    relation_ids = []
    old_rows = {r["id"]: r for r in preimage["rows"]}
    for row in rows:
        identity = row.get("id")
        if row.get("source_member") != expected.get(identity):
            fail("source_member", str(identity))
        for field in ("source_anchor", "source_selection"):
            if row.get(field) != old_rows.get(identity, {}).get(field):
                fail("source_fact", str(identity) + ": " + field)
        disposition = row.get("disposition")
        if disposition not in {"conserved", "superseded", "not applicable", "intentionally removed", "unresolved"}:
            fail("disposition", str(identity))
        if row.get("disposition_standing") not in {"author_proposal", "unresolved", "accepted"}:
            fail("standing", str(identity))
        if row.get("disposition_standing") == "accepted" and not row.get("owner_decision"):
            fail("acceptance", str(identity) + ": no exact owner decision")
        if disposition == "intentionally removed" and not row.get("owner_decision"):
            fail("removal", str(identity) + ": no owner decision")
        if disposition in {"not applicable", "unresolved"} and not row.get("reason"):
            fail("reason", str(identity))
        loci = row.get("successor_loci", [])
        if len(loci) != len(set(loci)):
            fail("duplicate_locus", str(identity))
        if disposition in {"conserved", "superseded"} and (not loci or row.get("successor_locus") not in loci):
            fail("carrying_loci", str(identity))
        for binding_id in row.get("consumer_binding_refs", []):
            if binding_id not in bindings:
                fail("binding_ref", str(identity) + ": " + binding_id)
            elif not set(bindings[binding_id]["loci"]).issubset(loci):
                fail("binding_carry", str(identity) + ": required declared binding routes omitted")
        for locus in loci:
            try:
                inspect(locus)
            except (ValueError, OSError, UnicodeError) as error:
                fail("carrying_locus", str(identity) + ": " + str(error))
        relation = row.get("successor_relation")
        if disposition == "superseded":
            if not isinstance(relation, dict) or not relation.get("id") or not relation.get("changed_meaning"):
                fail("replacement_relation", str(identity))
            else:
                relation_ids.append(relation["id"])
                if relation.get("predecessor_claim_id") != identity or not relation.get("replacement_loci") or not set(relation["replacement_loci"]).issubset(loci):
                    fail("replacement_binding", str(identity))
                if relation.get("standing") != "proposed_pending_owner_decision" and not relation.get("owner_decision"):
                    fail("replacement_authority", str(identity))
        if not row.get("semantic_review", {}).get("remaining_obligations"):
            fail("review_scope", str(identity) + ": author map must retain its unresolved review boundary")
        comparison = row.get("author_comparison")
        if identity in draft_ids or comparison:
            if not comparison or not comparison.get("meaning_assessment"):
                fail("author_comparison", str(identity))
            else:
                try:
                    current = inspect(comparison["candidate_locus"])
                    predecessor = section_body((INSTALLED / row["source_member"]).read_text(), row["source_anchor"]).encode()
                    if current["section_sha256"] != comparison["candidate_section_sha256"] or sha(predecessor) != comparison["predecessor_section_sha256"]:
                        fail("comparison_drift", str(identity))
                    assessed_commit = comparison.get("candidate_assessed_commit", "")
                    if not isinstance(assessed_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", assessed_commit):
                        fail("comparison_subject", str(identity) + ": missing immutable comparison subject")
                    else:
                        name, _, anchor = comparison["candidate_locus"].partition("#")
                        frozen_text = git_bytes(assessed_commit, str((PACKAGE / name).relative_to(REPO))).decode()
                        if sha(section_body(frozen_text, anchor).encode()) != comparison["candidate_section_sha256"]:
                            fail("comparison_subject", str(identity) + ": assessed commit differs from recorded body")
                except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
                    fail("author_comparison", str(identity) + ": " + str(error))
    if len(relation_ids) != len(set(relation_ids)):
        fail("relation_identity", "Replacement relation IDs must be unique")
    source_pins = mapping.get("source_member_pins", {})
    if set(source_pins) != set(expected.values()):
        fail("source_inventory", "Incomplete predecessor member pins")
    for name, pin in source_pins.items():
        data = (INSTALLED / name).read_bytes()
        if pin.get("sha256") != sha(data) or pin.get("bytes") != len(data):
            fail("source_pin", name)
    if sha((INSTALLED / "manifest.json").read_bytes()) != BUILDER_SHA:
        fail("builder_pin", "Installed manifest changed")
    if len(ports.get("contributions", [])) != 5:
        fail("port_count", "Only the five already-named contributions are selected")
    if {p.get("id") for p in ports.get("contributions", [])} != {"I3-R2-P%02d" % i for i in range(1, 6)}:
        fail("port_identity", "The five named contribution identities must be complete and unique")
    for port in ports.get("contributions", []):
        if port.get("source_commit") != "31f28f90c4a9b15243d84630fc4799024a9cd7ac":
            fail("port_source", port.get("id"))
        try:
            inspect(port.get("receiving_owner_locus"))
        except (ValueError, OSError, UnicodeError) as error:
            fail("port_owner", str(error))
        if not port.get("affected_predecessor_ids") or not set(port["affected_predecessor_ids"]).issubset(set(ids)):
            fail("port_frontier", port.get("id"))
        expected_relations = [by_id[i]["successor_relation"]["id"] for i in port.get("affected_predecessor_ids", [])
                              if i in by_id and by_id[i].get("successor_relation")]
        if port.get("current_relation_ids") != expected_relations:
            fail("port_relation", port.get("id"))
        if port.get("source_comparison", {}).get("result") != "indeterminate":
            fail("port_standing", "No fresh source comparison was selected for " + str(port.get("id")))
    frozen = mapping.get("pin_state") == "frozen_source_verified"
    if require_frozen and not frozen:
        fail("source_freeze", "Conservation pins await the exact complete frozen package")
    if frozen:
        commit = mapping.get("candidate_source_commit")
        if not commit:
            fail("source_freeze", "Missing frozen candidate commit")
        expected_pins = {k: {"sha256": v["sha256"], "bytes": v["bytes"]} for k, v in files.items()}
        if mapping.get("successor_member_pins") != expected_pins or mapping.get("successor_locus_pins") != locus_pins:
            fail("successor_pins", "Current source differs from finalized complete carrying pins")
        for row in rows:
            primary = row.get("successor_locus")
            if primary and row.get("successor_sha256") != files.get(primary.split("#")[0], {}).get("sha256"):
                fail("primary_pin", row["id"])
        if commit:
            for name, entry in files.items():
                try:
                    frozen_data = git_bytes(commit, str((PACKAGE / name).relative_to(REPO)))
                    if sha(frozen_data) != entry["sha256"]:
                        fail("frozen_bytes", name)
                except subprocess.CalledProcessError:
                    fail("frozen_bytes", "Missing from frozen source: " + name)
    elif mapping.get("candidate_source_commit") is not None or mapping.get("successor_member_pins") or mapping.get("successor_locus_pins"):
        fail("pending_pins", "Pending draft must not carry operative frozen pins")
    return {"valid": not failures, "draft_valid": not any(f["code"] != "source_freeze" for f in failures),
            "failures": failures, "row_count": len(rows),
            "dispositions": {d: sum(r.get("disposition") == d for r in rows) for d in sorted({r.get("disposition") for r in rows})},
            "draft_relations_accounted": len(integration), "historical_changes": len(mapping.get("history_correction", {}).get("changes", [])),
            "carrying_loci": len(locus_pins), "source_members": len(source_pins), "frozen": frozen,
            "semantic_conservation": "indeterminate", "owner_acceptance": "not_established",
            "observed_member_pins": {k: {"sha256": v["sha256"], "bytes": v["bytes"]} for k, v in files.items()},
            "observed_locus_pins": locus_pins}


def negative_controls(mapping, ports):
    controls = []

    def run(name, mutate, expected_code):
        candidate = copy.deepcopy(mapping)
        mutate(candidate)
        candidate["semantic_sha256"] = semantic_sha(candidate)
        report = validate(candidate, frontier_for(candidate), ports)
        codes = {f["code"] for f in report["failures"]}
        controls.append({"name": name, "expected_code": expected_code, "detected": expected_code in codes})

    run("duplicate stable row ID", lambda m: m["rows"].__setitem__(1, copy.deepcopy(m["rows"][0])), "row_identity")
    run("missing secondary carrying anchor", lambda m: m["rows"][0]["successor_loci"].append("standards/FOUNDATIONS.md#absent-conservation-control"), "carrying_locus")
    run("supersession without its relation", lambda m: next(r for r in m["rows"] if r["disposition"] == "superseded").pop("successor_relation"), "replacement_relation")
    run("author proposal promoted without owner decision", lambda m: m["rows"][0].update(disposition_standing="accepted"), "acceptance")
    run("historical disposition change omitted", lambda m: m["history_correction"]["changes"].pop(), "history")
    run("unknown shared binding", lambda m: m["rows"][0]["consumer_binding_refs"].append("absent-binding-control"), "binding_ref")
    run("assessed row body digest changed", lambda m: next(r for r in m["rows"] if r.get("author_comparison"))["author_comparison"].update(candidate_section_sha256="0" * 64), "comparison_drift")
    run("historical fact rewritten", lambda m: m["historical_qualification"]["fields"]["synthesis"].update(meaning="dispositions all conserved"), "historical_fact")
    bad_frontier = frontier_for(mapping)
    bad_frontier["rows"][0]["disposition"] = "unresolved"
    controls.append({"name": "frontier semantic drift with unchanged IDs", "expected_code": "frontier",
                     "detected": any(f["code"] == "frontier" for f in validate(mapping, bad_frontier, ports)["failures"])})
    controls.append({"name": "section claim excludes descendant heading", "expected_code": "section_granularity",
                     "detected": section_body("# Parent\nA\n## Child\nB\n", "parent") == "# Parent\nA\n"})
    return controls


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-frozen", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    mapping, frontier, ports = [read(HERE / n) for n in ("CONSERVATION.json", "FRONTIER.json", "PORT_ACCOUNT.json")]
    report = validate(mapping, frontier, ports, args.require_frozen)
    report.pop("observed_member_pins")
    report.pop("observed_locus_pins")
    report["kind"] = "stdo.conservation-mechanical-check"
    report["map_sha256"] = sha((HERE / "CONSERVATION.json").read_bytes())
    report["semantic_sha256"] = mapping["semantic_sha256"]
    report["port_account_sha256"] = sha((HERE / "PORT_ACCOUNT.json").read_bytes())
    report["negative_controls"] = negative_controls(mapping, ports) if args.self_test else []
    report["valid"] &= all(c["detected"] for c in report["negative_controls"])
    report["draft_valid"] &= all(c["detected"] for c in report["negative_controls"])
    report["elapsed_seconds"] = round(time.monotonic() - started, 3)
    report["limits"] = ["Coordinate, shape and preservation checks do not prove semantic conservation.",
                        "Pending owner decisions and independent row/source/port assessments remain open.",
                        "Draft validity permits pending frozen pins; --require-frozen checks current-source binding separately."]
    if not args.no_write:
        (HERE / "CONSERVATION_CHECK.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
