"""Project frozen historical claims onto the current common candidate.

Run from any directory: python3 build_records.py [--check]
Writes only beside this script. --check verifies the persisted projection.
Historical review is retained as evidence awaiting current applicability;
this program does not determine semantic conservation or acceptance.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
CANDIDATE = HERE.parents[2] / "build_tenants/common"
SEED = "3a2097137c3588ba44b98e3ea801ac7f2be1daf0"
SEED_ROOT = "specification_methodology/v3/build_tenants/claude/"
VALUES = {"conserved", "superseded", "intentionally_removed", "not_applicable", "unresolved"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(data: str | bytes) -> Any:
    return json.loads(data, object_pairs_hook=unique_object)


def read_json(name: str) -> Any:
    return parse_json((HERE / name).read_bytes())


def require(condition: bool, detail: str) -> None:
    if not condition:
        raise ValueError(detail)


def source_ref(file: str, pointer: str = "", line: int | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"file": "sources/" + file}
    if pointer:
        result["json_pointer"] = pointer
    if line is not None:
        result["line"] = line
    return result


def parse_inventory(text: str) -> tuple[dict[str, Any], dict[str, Any], dict[str, str]]:
    """Parse known table shapes while retaining embedded pipes in disposition prose."""
    body: dict[str, Any] = {}
    nonbody: dict[str, Any] = {}
    member_hashes = {}
    heading = ""
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            heading = line[3:].strip()
        if not line.startswith("|"):
            continue
        cells = [part.strip() for part in re.split(r"(?<!\\)\|", line)[1:-1]]
        if heading == "Members" and len(cells) == 4 and re.fullmatch(r"`[a-f0-9]{64}`", cells[-1]):
            member_hashes[cells[0].strip("`")] = cells[-1].strip("`")
        if heading.endswith(".md") and len(cells) >= 6 and cells[1].startswith("`#"):
            anchor = cells[1].strip("`")
            rid = heading + anchor
            require(rid not in body, "duplicate body inventory ID " + rid)
            body[rid] = {
                "id": rid, "member": heading, "anchor": anchor,
                "title": cells[0], "identifiers": cells[2], "bytes_text": cells[3],
                "disposition_note": " | ".join(cells[4:-1]), "locus_text": cells[-1],
                "source_line": number, "raw_line": line,
            }
        elif len(cells) == 5 and cells[0].startswith("`") and re.fullmatch(r"`[a-f0-9]{64}`", cells[2]):
            rid = cells[0].strip("`")
            require(rid not in nonbody, "duplicate nonbody inventory ID " + rid)
            nonbody[rid] = {
                "id": rid, "kind": cells[1], "predecessor_member_sha256": cells[2].strip("`"),
                "disposition_note": cells[3], "locus_text": cells[4],
                "source_line": number, "raw_line": line,
            }
    return body, nonbody, member_hashes


def disposition(note: str) -> str:
    for text, value in [("not applicable", "not_applicable"), ("intentionally removed", "intentionally_removed"),
                        ("conserved", "conserved"), ("superseded", "superseded"), ("unresolved", "unresolved")]:
        if note.lower().startswith(text):
            return value
    raise ValueError("unknown disposition note: " + note[:80])


def normalize_body(row: dict[str, Any]) -> tuple[str, bool]:
    value = row["disposition"]
    if value == "not":
        require(disposition(row["disposition_note"]) == "not_applicable", "truncated not has no bounded non-applicability reason")
        require(len(row["disposition_note"].strip()) > len("not applicable:"), "empty non-applicability reason")
        return "not_applicable", True
    require(value in VALUES, "unknown body disposition " + str(value))
    return value, False


def refs(text: str) -> list[str]:
    return [item for item in re.findall(r"`([^`]+)`", text)
            if re.match(r"(?:standards/|plugins/|release/|schemas/|templates/)?[^ ]+\.(?:md|json|yaml)(?:#.*)?$", item)
            or item == "LICENSE"]


def candidate_locus(locus: str, rules: dict[str, Any]) -> str:
    locus = rules["locus_adaptations"].get(locus, locus)
    path, marker, anchor = locus.partition("#")
    if not path.startswith(("standards/", "plugins/", "release/")) and path != "LICENSE":
        path = "standards/" + path
    require(not Path(path).is_absolute() and ".." not in Path(path).parts, "nonlocal candidate locus " + locus)
    return path + (marker + anchor if marker else "")


def heading_sections(text: str) -> dict[str, dict[str, Any]]:
    lines = text.splitlines(keepends=True)
    headings = []
    seen: dict[str, int] = {}
    fence = None
    for index, line in enumerate(lines):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match[1][0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        match = None if fence else re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w\- ]", "", match[2].strip().lower().replace("`", "")).replace(" ", "-")
            n = seen.get(slug, 0)
            seen[slug] = n + 1
            headings.append((index, len(match[1]), slug if not n else slug + "-" + str(n)))
    result = {}
    for pos, (start, level, anchor) in enumerate(headings):
        direct_end = headings[pos + 1][0] if pos + 1 < len(headings) else len(lines)
        full_end = next((i for i, lvl, _ in headings[pos + 1:] if lvl <= level), len(lines))
        result[anchor] = {
            "line_start": start + 1, "direct_end": direct_end, "with_children_end": full_end,
            "direct_sha256": digest("".join(lines[start:direct_end]).encode()),
            "with_children_sha256": digest("".join(lines[start:full_end]).encode()),
        }
    return result


class Projection:
    def __init__(self) -> None:
        self.current: dict[str, bytes | None] = {}
        self.seed: dict[str, bytes | None] = {}
        self.sections: dict[tuple[str, str], dict[str, Any]] = {}

    def bytes(self, path: str, current: bool) -> bytes | None:
        cache = self.current if current else self.seed
        if path not in cache:
            if current:
                target = CANDIDATE / path
                cache[path] = target.read_bytes() if target.is_file() else None
            else:
                found = subprocess.run(["git", "-C", str(REPO), "show", SEED + ":" + SEED_ROOT + path], capture_output=True)
                cache[path] = found.stdout if found.returncode == 0 else None
        return cache[path]

    def resolve(self, locus: str, original: str) -> dict[str, Any]:
        path, _, anchor = locus.partition("#")
        data = self.bytes(path, True)
        result: dict[str, Any] = {"locus": locus, "seed_locus": original, "evidence_scope": "text identity and address resolution only"}
        if data is None:
            return result | {"status": "missing_candidate_member"}
        result["member_sha256"] = digest(data)
        if anchor:
            section = heading_sections(data.decode()).get(anchor)
            if section is None:
                return result | {"status": "missing_candidate_anchor"}
            result["section"] = section
        result["status"] = "resolved"
        seed_path, _, seed_anchor = candidate_locus(original, {"locus_adaptations": {}}).partition("#")
        seed_data = self.bytes(seed_path, False)
        if seed_data is not None:
            result["seed_member_sha256"] = digest(seed_data)
            seed_section = heading_sections(seed_data.decode()).get(seed_anchor) if seed_anchor else None
            if seed_section:
                result["seed_section"] = seed_section
            if anchor and seed_section:
                equal = result["section"]["with_children_sha256"] == seed_section["with_children_sha256"]
            elif not anchor and not seed_anchor:
                equal = data == seed_data
            else:
                equal = None
            result["text_relation"] = "unchanged" if equal else "changed" if equal is False else "not_comparable"
        else:
            result["text_relation"] = "seed_member_unavailable"
        result["semantic_conservation"] = "not_determined_by_identity_check"
        return result

    def confirm_stable(self) -> None:
        for path, data in self.current.items():
            target = CANDIDATE / path
            now = target.read_bytes() if target.is_file() else None
            require(now == data, "candidate changed during projection: " + path)


def freeze_sources() -> dict[str, Any]:
    manifest = read_json("SOURCES.json")
    for entry in manifest["sources"]:
        data = (HERE / entry["file"]).read_bytes()
        require(len(data) == entry["bytes"] and digest(data) == entry["sha256"], "frozen source digest mismatch: " + entry["file"])
        exact = subprocess.check_output(["git", "-C", str(REPO), "show", entry["git_commit"] + ":" + entry["git_path"]])
        require(data == exact, "frozen source differs from declared Git object: " + entry["file"])
    return manifest


def recover_predecessor(rows: list[dict[str, Any]]) -> dict[str, Any]:
    source = read_json("PREDECESSOR_SOURCE.json")
    raw = (HERE / source["manifest_file"]).read_bytes()
    require(digest(raw) == source["manifest_sha256"] == "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782", "predecessor manifest does not match selected exact basis")
    manifest = parse_json(raw)
    authenticated = {item["path"]: item["sha256"] for item in manifest["standards"]["members"]}
    members = {}
    for entry in source["members"]:
        data = (HERE / entry["file"]).read_bytes()
        require(digest(data) == entry["sha256"] == authenticated[entry["member"]], "predecessor member digest mismatch")
        members[entry["member"]] = data
    results = []
    for row in rows:
        if row["predecessor_sha256"] is not None:
            continue
        member = row["source_member"]
        text = members[member].decode()
        lines = text.splitlines(keepends=True)
        sections = heading_sections(text)
        wanted = row["source_anchor"].lstrip("#")
        direct = [name for name in sections if re.sub("-+", "-", name) == re.sub("-+", "-", wanted)]
        entry: dict[str, Any] = {"id": row["id"], "original_predecessor_sha256": None, "source_member": member, "source_member_sha256": digest(members[member]), "source_release_uri": "stdo://releases/v2.5.1-rc.2/", "manifest_sha256": source["manifest_sha256"], "source_file": "sources/predecessor/" + member, "source_field_rewritten": False}
        if len(direct) == 1:
            anchor = direct[0]
            section = sections[anchor]
            # Match the original frontier parser: text after the heading,
            # through the next heading of any level, preserving all bytes.
            content = "".join(lines[section["line_start"]:section["direct_end"]]).encode()
            entry.update(status="recovered_exact_heading_content", resolved_anchor="#" + anchor, claim_sha256=digest(content), line_start=section["line_start"] + 1, line_end=section["direct_end"], byte_start=len("".join(lines[:section["line_start"]]).encode()), bytes=len(content), resolution_rule="unique heading match after collapsing repeated hyphens; original parser content excludes heading", original_omission_cause="inventory anchor omits a hyphen produced by the em dash in the exact heading")
        else:
            parents = [name for name in sections if wanted.startswith(name + "-")]
            parent = max(parents, key=len) if parents else None
            entry.update(status="unresolved_exact_clause_extent", claim_sha256=None, reason="The source ID is a clause-split synthetic anchor, not a heading. The frozen record does not define an exact byte span for the clause; hashing its containing section would change the claim scope.")
            if parent:
                section = sections[parent]
                content = "".join(lines[section["line_start"]:section["direct_end"]]).encode()
                entry["authenticated_containing_section"] = {"anchor": "#" + parent, "content_sha256": digest(content), "line_start": section["line_start"] + 1, "line_end": section["direct_end"], "scope": "containing-section context only; not substituted for the clause digest"}
        results.append(entry)
    return {"kind": "stdo.common.predecessor-digest-recovery", "source_freeze_sha256": digest((HERE / "PREDECESSOR_SOURCE.json").read_bytes()), "hash_scope_source": source_ref("source_frontier_review.py", line=19), "original_fields_preserved": True, "rows": results, "counts": dict(Counter(item["status"] for item in results))}


def source_questions() -> list[dict[str, Any]]:
    result = []
    for number, line in enumerate((HERE / "sources/claude_decisions.md").read_text().splitlines(), 1):
        match = re.match(r"(?:\| |- )(Q\d+)\b", line)
        if not match:
            continue
        qid = match[1]
        scope = "requires_current_subject_readback; no source decision transferred"
        if qid in {"Q8", "Q11"}:
            scope = "interpretation/compression delivery deferred by construction scope; historical question retained"
        elif qid == "Q15":
            scope = "interpretation fidelity deferred; covering nonauthor conservation review still required"
        elif qid == "Q16":
            scope = "historical release-cut question; current release selection remains a separate owner decision"
        result.append({"id": qid, "source": source_ref("claude_decisions.md", line=number), "quoted_source": line, "standing": "historical question; not acceptance", "current_scope": scope})
    require({item["id"] for item in result} == {"Q" + str(n) for n in range(1, 20)}, "source question coverage differs")
    return result


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    manifest = freeze_sources()
    rules = read_json("RULES.json")
    shared, shared_non, member_hashes = parse_inventory((HERE / "sources/shared_predecessor_claims.md").read_text())
    frontier, frontier_non, _ = parse_inventory((HERE / "sources/claude_frontier.md").read_text())
    seed_review = read_json("sources/claude_review.json")
    seed_rows = seed_review["rows"]
    predecessor_recovery = recover_predecessor(seed_rows)
    recovery_by_id = {item["id"]: index for index, item in enumerate(predecessor_recovery["rows"])}
    require(len({row["id"] for row in seed_rows}) == len(seed_rows), "duplicate REVIEW ID")
    ids = {row["id"] for row in seed_rows}
    require(set(shared).issubset(ids), "shared body claim missing from REVIEW")
    require(ids == set(frontier), "prose and machine body ID sets differ")
    require(set(shared_non) == set(frontier_non), "shared and tenant nonbody ID sets differ")
    differences = read_json("sources/differing_dispositions.json")
    require(ids - set(shared) == set(differences["only_claude"]), "child identity set differs from frozen packet inventory")
    packet = sorted(differences["differ"], key=lambda item: (item["claude"], item["codex"], item["id"]))
    packet_numbers = {item["id"]: n for n, item in enumerate(packet, 1)}
    assessments: dict[str, list[dict[str, Any]]] = {}
    for n, assessment in enumerate(read_json("sources/claude_review_assessments.json")["assessments"]):
        require(assessment["id"] in ids, "assessment for unknown body claim")
        assessments.setdefault(assessment["id"], []).append({"source": source_ref("claude_review_assessments.json", f"/assessments/{n}"), "historical_result": assessment["semantic_review"], "current_applicability": "not_established"})
    projection = Projection()
    repairs = []
    rows = []
    for index, source in enumerate(seed_rows):
        rid = source["id"]
        normalized, repaired = normalize_body(source)
        prose = frontier[rid]
        require(disposition(prose["disposition_note"]) == normalized, "prose/machine disposition disagreement: " + rid)
        if repaired:
            repairs.append({"id": rid, "from": "not", "to": "not_applicable", "bounded_reason": source["disposition_note"], "source": source_ref("claude_review.json", f"/rows/{index}"), "prose_source": source_ref("claude_frontier.md", line=prose["source_line"])})
        original_loci = [locus["locus"] for locus in source["successor_loci"]]
        prose_loci = refs(prose["locus_text"])
        recovered = [locus for locus in prose_loci if locus not in original_loci]
        if recovered:
            repairs.append({"id": rid, "kind": "successor_routes_recovered_from_prose", "loci": recovered, "source": source_ref("claude_frontier.md", line=prose["source_line"]), "quoted_frozen_row": prose["raw_line"], "route_semantics": {"FOUNDATIONS.md#results": "the core result algebra and its conjunction", "ASSURANCE.md#7-product-testing-frame-set": "the testing-frame mappings consumed by the executive profile"}, "disposition_before": source["disposition"], "disposition_after": normalized, "acceptance": "pending; unchanged", "meaning_or_acceptance_changed": False})
        original_loci += recovered
        current_loci = [projection.resolve(candidate_locus(locus, rules), locus) for locus in dict.fromkeys(original_loci)]
        n = packet_numbers.get(rid)
        loans = [loan for loan, numbers in rules["meaning_change_loans"].items() if n in numbers]
        disputed = n in rules["disputed_conserved_rows"]
        standalone = rid in rules["standalone_adaptation_rows"]
        proposal = "superseded" if loans else "unresolved" if disputed or standalone else normalized
        decisions = [{"id": "COMMON-ACCEPT:" + rid, "owner": "product_owner", "status": "pending_exact_subject_acceptance"}]
        if rid in rules["question_ids_by_claim"]:
            decisions.append({"id": rules["question_ids_by_claim"][rid], "owner": "product_owner", "status": "pending_source_replacement_decision", "source": source_ref("claude_decisions.md")})
        if disputed:
            decisions.append({"id": f"CONFIRM-ROW-{n:02d}", "owner": "covering_reviewer_then_product_owner", "status": "pending_row_specific_meaning_confirmation", "source": source_ref("loan_result.md")})
        if str(n) in rules["owner_keep_or_withdraw_rows"]:
            decisions.append({"id": f"KEEP-OR-WITHDRAW-{n:02d}", "question": rules["owner_keep_or_withdraw_rows"][str(n)], "owner": "product_owner", "status": "pending; no withdrawal performed"})
        if n in rules["a1_reach_pending_rows"]:
            decisions.append({"id": "A1-REACH", "owner": "product_owner", "status": "pending; proposed extension is not assumed adopted"})
        if n in rules["p1_class_pending_rows"]:
            decisions.append({"id": "P1-CLASS", "owner": "covering_reviewer", "status": "pending_classification"})
        for loan in loans:
            decisions.append({"id": loan, "owner": "product_owner", "status": "pending_exact_replacement_acceptance", "source": source_ref("loan_register.md")})
        if standalone:
            decisions.append({"id": "STANDALONE:" + rid, "owner": "covering_reviewer_then_product_owner", "status": "pending_meaning_readback_under_owner_standalone_direction"})
        if rid in {"UX_METHOD.md#4a-process-model-without-language-or-framework-mandate", "UX_METHOD.md#12-realization-discretion"}:
            decisions.append({"id": "Q10", "owner": "product_owner", "status": "pending_compliance_test_choice; existing_fail_closed_application_retained", "source": source_ref("claude_decisions.md")})
        rows.append({
            "id": rid, "kind": "body", "source_member": source["source_member"], "source_anchor": source["source_anchor"],
            "inventory_class": "shared_body" if rid in shared else "tenant_child", "identifiers": source["identifiers"],
            "source": source_ref("claude_review.json", f"/rows/{index}"), "source_record_sha256": digest(canonical(source)),
            "shared_source": source_ref("shared_predecessor_claims.md", line=shared[rid]["source_line"]) if rid in shared else None,
            "source_member_sha256": member_hashes[source["source_member"]], "source_claim_sha256": source["predecessor_sha256"],
            "source_claim_digest_status": "resolved_in_seed_record" if source["predecessor_sha256"] else "unresolved_in_seed_record; not_repaired_by_this_projection",
            "new_predecessor_evidence": {"file": "CLAIM_DIGEST_RECOVERY.json", "json_pointer": f"/rows/{recovery_by_id[rid]}", "scope": "new evidence, not a rewrite of the original field"} if rid in recovery_by_id else None,
            "seed_disposition": {"raw": source["disposition"], "normalized": normalized, "note": source["disposition_note"], "standing": source["disposition_standing"], "acceptance": source["acceptance"]},
            "successor_relation": {"proposed_disposition": proposal, "standing": "author_proposal", "effective_disposition": "unresolved", "acceptance": "pending", "changed_meaning": {"loans": loans, "disputed_seed_conservation": disputed, "standalone_adaptation": standalone, "row_specific_confirmation": "pending"}, "receiving_loci": current_loci, "dependencies": {"seed_required_loci": original_loci, "material_relation_scope": "owning locus plus all supplied bindings", "completeness": "requires_covering_semantic_review"}, "pending_decisions": decisions, "residuals": ["Current nonauthor semantic review and applicability of historical evidence remain open."]},
            "evidence": [{"source": source_ref("claude_review.json", f"/rows/{index}/semantic_review"), "historical_result": source["semantic_review"], "current_applicability": "not_established"}] + assessments.get(rid, []),
            "loan_comparison_row": n, "delivery_scope": "in_scope",
        })
    for rid, source in shared_non.items():
        seed = frontier_non[rid]
        normalized = disposition(seed["disposition_note"])
        compression = source["kind"] == "compression"
        original_loci = refs(seed["locus_text"])
        original_loci = list(dict.fromkeys(original_loci))
        note_routes = list(dict.fromkeys(refs(seed["disposition_note"])))
        # Narrative notes quote both predecessor paths and receiving owners. They
        # remain historical evidence until a row-specific relation selects them.
        # A bounded non-applicability reason requires no replacement locus.
        resolved = [] if normalized == "not_applicable" else [projection.resolve(candidate_locus(locus, rules), locus) for locus in original_loci]
        decisions = [{"id": "COMMON-NONBODY:" + rid, "owner": "product_owner", "status": "pending_current_scope_and_disposition", "source": source_ref("claude_frontier.md", line=seed["source_line"])}]
        if compression:
            decisions.append({"id": "Q8", "owner": "product_owner", "status": "delivery_deferred; semantic_disposition_unresolved"})
        rows.append({
            "id": rid, "kind": source["kind"], "inventory_class": "shared_nonbody", "source": source_ref("shared_predecessor_claims.md", line=source["source_line"]), "seed_source": source_ref("claude_frontier.md", line=seed["source_line"]),
            "source_member_sha256": source["predecessor_member_sha256"], "source_raw_line": source["raw_line"],
            "seed_disposition": {"raw": seed["disposition_note"], "normalized": normalized, "note": seed["disposition_note"], "standing": "historical_author_proposal", "acceptance": "not_transferred"},
            "successor_relation": {"proposed_disposition": "unresolved" if compression else normalized, "standing": "author_proposal", "effective_disposition": "unresolved", "acceptance": "pending", "changed_meaning": {"classification": "not_determined_by_member_inventory"}, "receiving_loci": resolved, "dependencies": {"seed_locus_column": original_loci, "historical_note_routes": note_routes, "historical_route_standing": "context only; not selected as current receiving dependencies", "completeness": "requires_covering_semantic_review"}, "pending_decisions": decisions, "residuals": ["Delivery deferral does not decide semantic non-applicability."] if compression else ["Current nonauthor comparison required for changed members."]},
            "evidence": [{"source": source_ref("claude_frontier.md", line=seed["source_line"]), "current_applicability": "not_established"}],
            "delivery_scope": "deferred" if compression else "historical_release_only" if source["kind"] == "release note" else "in_scope",
        })
    projection.confirm_stable()
    inputs = [{"path": path, "sha256": digest(data) if data is not None else None} for path, data in sorted(projection.current.items())]
    result = {"kind": "stdo.common.conservation-projection", "schema_version": 1, "standing": "construction_record_only; no acceptance", "source_freeze_sha256": digest((HERE / "SOURCES.json").read_bytes()), "predecessor_evidence_freeze_sha256": digest((HERE / "PREDECESSOR_SOURCE.json").read_bytes()), "transform_rules_sha256": digest((HERE / "RULES.json").read_bytes()), "generator_sha256": digest(Path(__file__).read_bytes()), "candidate_basis": {"kind": "worktree_member_projection", "files": inputs, "sha256": digest(canonical(inputs)), "not_a_release_or_qualification": True}, "source_question_register": source_questions(), "rows": rows, "repairs": repairs}
    require(len(rows) == rules["expected"]["all_rows"], "unexpected total source coverage")
    validate(result, rules, shared, shared_non, ids)
    unresolved_loci = [{"id": row["id"], **locus} for row in rows for locus in row["successor_relation"]["receiving_loci"] if locus["status"] != "resolved"]
    proof = {"kind": "stdo.common.conservation-mechanical-validation", "result": "mechanical_properties_pass", "counts": {"body": len(seed_rows), "shared_body": len(shared), "tenant_children": len(ids - set(shared)), "nonbody": len(shared_non), "nonbody_kinds": dict(Counter(row["kind"] for row in rows if row["kind"] != "body")), "truncated_not_repairs": sum(item.get("from") == "not" for item in repairs), "route_recovery_repairs": sum(item.get("kind") == "successor_routes_recovered_from_prose" for item in repairs), "disputed_rows_pending": len(rules["disputed_conserved_rows"]), "source_claim_digests_unresolved": sum(row["source_claim_sha256"] is None for row in rows if row["kind"] == "body"), "unresolved_candidate_loci": len(unresolved_loci)}, "unresolved_candidate_loci": unresolved_loci, "semantic_qualification": "not_assessed; unresolved dispositions and pending decisions retained", "sources_verified": len(manifest["sources"]), "controls": controls(result, rules, shared, shared_non, ids)}
    proof["controls_pass"] = all(item["result"] == "pass" for item in proof["controls"])
    proof["counts"]["predecessor_digest_recovery"] = predecessor_recovery["counts"]
    require(proof["controls_pass"], "targeted control failed")
    packet_index = {"kind": "stdo.loan-comparison-row-index", "source": source_ref("differing_dispositions.json", "/differ"), "order_source": source_ref("build_loan_packets.py"), "order": rules["loan_packet_order"], "rows": [{"number": n, "id": item["id"], "claude": item["claude"], "codex": item["codex"]} for n, item in enumerate(packet, 1)]}
    return result, proof, packet_index, predecessor_recovery


def validate(result: dict[str, Any], rules: dict[str, Any], shared: dict[str, Any], nonbody: dict[str, Any], body_ids: set[str]) -> None:
    rows = result["rows"]
    require(len({row["id"] for row in rows}) == len(rows), "duplicate projected ID")
    require({row["id"] for row in rows} == body_ids | set(nonbody), "omitted or unexpected projected ID")
    require(Counter(row["kind"] for row in rows if row["kind"] != "body") == rules["expected"]["nonbody_kinds"], "nonbody kind coverage differs")
    require(sum(row["inventory_class"] == "shared_body" for row in rows) == len(shared), "shared body coverage differs")
    require(sum(row["inventory_class"] == "tenant_child" for row in rows) == rules["expected"]["body_child_rows"], "child coverage differs")
    require(sum(item.get("from") == "not" for item in result["repairs"]) == rules["expected"]["truncated_not_repairs"], "missing truncated-not repair")
    for row in rows:
        relation = row["successor_relation"]
        require(relation["proposed_disposition"] in VALUES, "unknown proposed disposition")
        require(relation["effective_disposition"] == "unresolved" and relation["acceptance"] == "pending", "acceptance or effective conservation invented")
        require(relation.get("dependencies") and relation.get("pending_decisions") and row.get("evidence"), "relation lost dependency, evidence or pending decision")
        if row["seed_disposition"]["normalized"] == "not_applicable":
            require(disposition(row["seed_disposition"]["note"]) == "not_applicable" and len(row["seed_disposition"]["note"].strip()) > 16, "non-applicability reason missing")
        if row["kind"] == "compression":
            require(row["delivery_scope"] == "deferred" and relation["proposed_disposition"] == "unresolved", "deferred compression relabeled or brought into scope")
        n = row.get("loan_comparison_row")
        if n in rules["disputed_conserved_rows"]:
            require(relation["proposed_disposition"] == "unresolved" and any(d["id"] == f"CONFIRM-ROW-{n:02d}" for d in relation["pending_decisions"]), "disputed row silently settled")
        if any(n in ns for ns in rules["meaning_change_loans"].values()):
            require(relation["proposed_disposition"] == "superseded", "proposed meaning change marked conserved")
        if str(n) in rules["owner_keep_or_withdraw_rows"]:
            require(any(d["id"] == f"KEEP-OR-WITHDRAW-{n:02d}" for d in relation["pending_decisions"]), "Q2/Q6 owner choice lost")
        for locus in relation["receiving_loci"]:
            require(candidate_locus(locus["locus"], {"locus_adaptations": {}}) == locus["locus"], "receiving locus is not package-local")
        for evidence in row["evidence"]:
            require(evidence["current_applicability"] == "not_established", "historical review applicability invented")


def controls(result: dict[str, Any], rules: dict[str, Any], shared: dict[str, Any], nonbody: dict[str, Any], body_ids: set[str]) -> list[dict[str, str]]:
    outcomes = [{"name": "positive_complete_projection", "result": "pass", "observed": "all identity, scope, reason and pending-decision invariants accepted"}]

    def rejected(name: str, operation: Any) -> None:
        try:
            operation()
        except (ValueError, KeyError, TypeError) as error:
            outcomes.append({"name": name, "result": "pass", "observed": str(error)})
        else:
            outcomes.append({"name": name, "result": "FAIL", "observed": "invalid subject accepted"})

    def mutated(name: str, change: Any) -> None:
        sample = deepcopy(result)
        change(sample)
        rejected(name, lambda: validate(sample, rules, shared, nonbody, body_ids))

    def select(sample: dict[str, Any], predicate: Any) -> dict[str, Any]:
        return next(row for row in sample["rows"] if predicate(row))

    mutated("omitted_shared_body_row", lambda s: s["rows"].remove(select(s, lambda r: r["inventory_class"] == "shared_body")))
    mutated("omitted_nonbody_row", lambda s: s["rows"].remove(select(s, lambda r: r["kind"] == "template")))
    mutated("duplicate_ID", lambda s: s["rows"].append(deepcopy(s["rows"][0])))
    mutated("compression_marked_not_applicable", lambda s: select(s, lambda r: r["kind"] == "compression")["successor_relation"].update(proposed_disposition="not_applicable"))
    mutated("compression_silently_in_scope", lambda s: select(s, lambda r: r["kind"] == "compression").update(delivery_scope="in_scope"))
    mutated("invented_acceptance", lambda s: s["rows"][0]["successor_relation"].update(acceptance="accepted", effective_disposition="conserved"))
    mutated("disputed_row_marked_conserved", lambda s: select(s, lambda r: r.get("loan_comparison_row") in rules["disputed_conserved_rows"])["successor_relation"].update(proposed_disposition="conserved"))
    mutated("loan_meaning_change_marked_conserved", lambda s: select(s, lambda r: r.get("loan_comparison_row") == 67)["successor_relation"].update(proposed_disposition="conserved"))
    mutated("not_applicable_reason_erased", lambda s: select(s, lambda r: r["seed_disposition"]["normalized"] == "not_applicable")["seed_disposition"].update(note=""))
    mutated("missing_dependency", lambda s: s["rows"][0]["successor_relation"].pop("dependencies"))
    mutated("missing_Q2_Q6_owner_choice", lambda s: select(s, lambda r: r.get("loan_comparison_row") == 93)["successor_relation"].update(pending_decisions=[]))
    mutated("historical_review_promoted_to_current", lambda s: s["rows"][0]["evidence"][0].update(current_applicability="established"))
    mutated("locus_escapes_candidate", lambda s: s["rows"][0]["successor_relation"]["receiving_loci"][0].update(locus="../../old/OWNER.md#rule"))
    rejected("duplicate_JSON_key", lambda: parse_json('{"rows":[],"rows":[]}'))
    rejected("malformed_not_without_reason", lambda: normalize_body({"disposition": "not", "disposition_note": "not an applicable record"}))
    return outcomes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare the persisted projection with current frozen sources and candidate bytes")
    args = parser.parse_args()
    projection, proof, packet, predecessor = build()
    outputs = {"CONSERVATION.json": projection, "VALIDATION.json": proof, "LOAN_ROW_INDEX.json": packet, "CLAIM_DIGEST_RECOVERY.json": predecessor}
    for name, value in outputs.items():
        target = HERE / name
        if args.check:
            require(read_json(name) == value, "stale or altered projection: " + name)
        else:
            data = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
            temporary = target.with_suffix(target.suffix + ".tmp")
            temporary.write_text(data)
            temporary.replace(target)
    print(json.dumps({"mode": "check" if args.check else "build", "rows": len(projection["rows"]), "controls_pass": proof["controls_pass"], **proof["counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()
