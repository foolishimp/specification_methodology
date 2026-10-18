#!/usr/bin/env python3
"""Author account deltas and reproduce bounded delivery-source checks.

Writes only this activation's return directory. It does not modify the current
determination account, interpretation, frames, source standards or Git state.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / ".git").exists())
TENANT = Path("specification_methodology/v3/build_tenants/codex")
PREIMAGE = "199c6d29bc02590a8b7f252043fc43223c09808d"
DONOR = "2beed8d9a043cfa572bd240793e5020134300410"
COMMON = "3c4c503d291e7cb19ba21333ba6caf6167be77c9"
ACCOUNT = TENANT / "qualification/C3/iteration-3/DETERMINATIONS.json"
FILES = ["SPEC_METHOD.md", "TICKET_METHOD.md", "RELEASE_METHOD.md", "IDENTITY_METHOD.md"]
EXPECTED = {
    "SPEC_METHOD.md": {"method-families", "universal-intake-triage", "agentic-construction-execution-stdo-up-020"},
    "TICKET_METHOD.md": {"carrier-families", "work-carrier-to-execution-rule", "condition-based-closure-and-reuse"},
    "RELEASE_METHOD.md": {"release-publication-context", "exact-cut-qualification"},
    "IDENTITY_METHOD.md": {"governing-relations"},
}
TABLES = {
    "SPEC_METHOD.md": "method-families",
    "TICKET_METHOD.md": "carrier-families",
    "RELEASE_METHOD.md": "release-publication-context",
    "IDENTITY_METHOD.md": "governing-relations",
}
CONTAINER_CONSUMERS = {
    "IDENTITY_METHOD.authority-split": ["IDENTITY_METHOD.engine-owned-identity", "IDENTITY_METHOD.domain-owned-identity"],
    "IDENTITY_METHOD.default-formats-and-overrides": ["IDENTITY_METHOD.defaults-from-a-bound-abg-realization", "IDENTITY_METHOD.derived-domain-overrides", "IDENTITY_METHOD.override-publication-surface"],
}
LOCAL_ARGUMENTS = {
    "SPEC_METHOD.universal-intake-triage": {
        "premises": ["F1", "F2", "F3", "F6"],
        "conditional_consequence": "A selected Product outcome, interpreted governing layers, current subject and separately owned mutation authority make intake a diagnosis of the actual relation needing correction. A report label or the location that exposes failure cannot determine its cause or grant its repair; evidence unable to distinguish implementation failure from missing requirement meaning leaves that distinction unresolved.",
        "policy_choices": ["Spec chooses the single intake route, six change classes and lower-re-entry assertion of no upstream change. Computed Classification And Treatment owns candidate-versus-governing-relation correction; the affected owner decides the change."],
    },
    "SPEC_METHOD.agentic-construction-execution-stdo-up-020": {
        "premises": ["F1", "F2", "F3", "F4", "F5", "F6"],
        "conditional_consequence": "Given a selected outcome, delegated affected cone, concrete execution binding and separate assessment/decision authority, candidate availability, cone preservation and disposition remain different predicates. Continuation retains useful work and observes current state and unresolved effects; composed bounded steps preserve affected outer relations and no construction or assessment creates acceptance authority.",
        "policy_choices": ["UP-020 chooses cone, proxy, checkpoint and remedy policies. Governing owners select outcome, delegation and required independent assessment. Human, machine and mixed bindings retain the same obligations; optional profiles add duties only where adopted and topology/internal search remain permitted variation."],
    },
    "TICKET_METHOD.work-carrier-to-execution-rule": {
        "premises": ["F2", "F3", "F5", "F6"],
        "conditional_consequence": "With an obligation surviving the local carrier boundary, persistent identity/state and finite actor context require the needed state to remain outside private memory. That lifetime argument does not select a ticket or grant its creation. Admission instead concerns whether the exact interpreted contract is covered by current upstream work authority; creating a carrier cannot supply that grant.",
        "policy_choices": ["Ticket chooses the ordered ticket/sprint/run lifetime table, deterministic admission or exact human override, durable result surface and recorded judgment/ruling continuity. An obligation without ticket-state authority remains on the already permitted result surface."],
    },
    "TICKET_METHOD.condition-based-closure-and-reuse": {
        "premises": ["F1", "F2", "F3", "F4", "F6"],
        "conditional_consequence": "Closure is about the declared work outcome and each applicable obligation, including the actual required owner decision. Conjunction preserves those predicates, so a completed review or a lawful rejection cannot satisfy an absent acceptance condition. Support tied to the exact subject remains reusable while applicable; changing actors alone does not invalidate it.",
        "policy_choices": ["The admitted contract and governing law select required completion, non-closure, review and acceptance conditions. Ticket permits a granted Writer to record a satisfied bounded result when no applicable independent-review or reserved-acceptance condition remains."],
    },
    "RELEASE_METHOD.exact-cut-qualification": {
        "premises": ["F1", "F2", "F3", "F4", "F6"],
        "conditional_consequence": "For a declared cut, claim set and observation boundaries, evidence answers the claim and subject actually observed. Source, package and installed-use successes can answer different predicates. Conjunction retains all required items and uncovered scope, and qualification does not supply acceptance authority.",
        "policy_choices": ["Release chooses exact-cut review, required operator checks and human acceptance. Product authority declares claims, external dependencies and lawful narrowing. Supported alternative realizations are assessed against those same claim conditions."],
    },
}


def git_bytes(path, ref=PREIMAGE):
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def digest(body):
    return hashlib.sha256(body).hexdigest()


def slug(text):
    text = re.sub(r"[`*_]", "", text).lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return re.sub(r" +", "-", text)


def sections(text):
    lines = text.splitlines(keepends=True)
    starts = []
    counts = {}
    in_fence = False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        match = re.match(r"^(#{1,6}) (.+?)\s*$", line)
        if match:
            base = slug(match[2]); ordinal = counts.get(base, 0); counts[base] = ordinal + 1
            anchor = base if not ordinal else f"{base}-{ordinal}"
            starts.append((anchor, match[2], i))
    result = {}
    for index, (anchor, title, start) in enumerate(starts):
        end = starts[index + 1][2] if index + 1 < len(starts) else len(lines)
        body = "".join(lines[start:end])
        result[anchor] = {"heading": title, "start_line": start + 1, "end_line": end, "body": body}
    return result


def premises(text):
    found = set()
    for a, b in re.findall(r"F([1-6])[–-]F([1-6])", text):
        found.update(f"F{i}" for i in range(int(a), int(b) + 1))
    found.update(re.findall(r"\bF[1-6]\b", text))
    return sorted(found)


def table_rows(name, section):
    result = []
    for line in section["body"].splitlines():
        if not line.startswith("| ["):
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        assert len(cells) == 4, (name, cells)
        consumer, premise, consequence, policy = cells
        source_refs = [name.removesuffix(".md") + "." + a for a in re.findall(r"\]\(#([^)]+)\)", consumer)]
        refs = [ref for scope in source_refs for ref in CONTAINER_CONSUMERS.get(scope, [scope])]
        result.append({
            "family": re.match(r"\| \[([^]]+)", line)[1],
            "declared_consumer_scope": consumer,
            "consumer_refs": refs,
            "consumer_heading_refs": source_refs,
            "premises": premises(premise),
            "premises_and_pillar_contribution": premise,
            "conditional_consequence": consequence,
            "additional_policy_and_owner": policy,
            "source_refs": [name.removesuffix(".md") + "." + TABLES[name]],
            "source_row": {"path": "standards/" + name, "anchor": TABLES[name], "sha256": digest((line + "\n").encode())},
        })
    return result


def account_row(row):
    """Consumer inventories are provenance, not universal acquisition edges."""
    result = {k: v for k, v in row.items() if k not in {"consumer_refs", "consumer_heading_refs"}}
    result["source_refs"] = sorted(set(row["source_refs"] + row["consumer_refs"]))
    result["acquisition_scope"] = "Consumer routes in source_refs are provenance for reviewing this row; applying one consumer does not require acquiring every listed consumer. The row is selected when the task evaluates its family argument or applicability. Existing required premise and operation dependencies remain in force."
    return result


def main():
    account_bytes = git_bytes(ACCOUNT)
    account = json.loads(account_bytes)
    units = {row["id"]: row for row in account["determinations"]}
    source = {}
    original = {}
    changes = []
    preserved = 0
    pins = []
    families = {}
    for name in FILES:
        path = TENANT / "successor/standards" / name
        old = git_bytes(path); new = (ROOT / path).read_bytes()
        before = sections(old.decode()); after = sections(new.decode())
        assert [(a, v["heading"]) for a, v in before.items()] == [(a, v["heading"]) for a, v in after.items()], name
        changed = {a for a in before if before[a]["body"] != after[a]["body"]}
        assert changed == EXPECTED[name], (name, changed)
        preserved += len(before) - len(changed)
        source[name] = after
        original[name] = before
        families[name] = table_rows(name, after[TABLES[name]])
        assert len(families[name]) == {"SPEC_METHOD.md": 8, "TICKET_METHOD.md": 8, "RELEASE_METHOD.md": 7, "IDENTITY_METHOD.md": 7}[name]
        pins.append({"path": str(path), "preimage_sha256": digest(old), "sha256": digest(new), "preimage_bytes": len(old), "bytes": len(new)})
        for anchor in sorted(changed):
            unit_id = name.removesuffix(".md") + "." + anchor
            assert unit_id in units, unit_id
            changes.append({"id": unit_id, "path": str(path), "heading": after[anchor]["heading"], "anchor": anchor,
                            "change_kind": "argument_and_consumer_explanation", "new_decision_scope": False,
                            "predicate_or_result_change": False, "preimage_body_sha256": digest(before[anchor]["body"].encode()),
                            "body_sha256": digest(after[anchor]["body"].encode())})
    unchanged_decision_tails = []
    for name, anchor, marker in [
        ("SPEC_METHOD.md", "universal-intake-triage", "Select the smallest sufficient applicable configuration"),
        ("SPEC_METHOD.md", "agentic-construction-execution-stdo-up-020", "When construction is delegated to a probabilistic or agentic worker"),
        ("TICKET_METHOD.md", "work-carrier-to-execution-rule", "Every execution governed by this method"),
        ("TICKET_METHOD.md", "condition-based-closure-and-reuse", "Apply [Contract application]"),
        ("RELEASE_METHOD.md", "exact-cut-qualification", "Qualification binds:"),
    ]:
        old_tail = original[name][anchor]["body"].split(marker, 1)[1]
        new_tail = source[name][anchor]["body"].split(marker, 1)[1]
        assert old_tail == new_tail, (name, anchor, "decision tail changed")
        unchanged_decision_tails.append({"source": name + "#" + anchor, "from": marker, "sha256": digest(new_tail.encode()), "bytes": len(new_tail.encode())})
    assert original["SPEC_METHOD.md"]["universal-intake-triage"]["body"].split("Intake applies [Contract application]", 1)[0] == source["SPEC_METHOD.md"]["universal-intake-triage"]["body"].split("The intake judgment concerns", 1)[0]
    link_checks = []
    for name, blocks in source.items():
        for anchor in EXPECTED[name]:
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", blocks[anchor]["body"]):
                if "://" in target:
                    continue
                path_part, _, fragment = target.partition("#")
                if path_part and not path_part.endswith(".md"):
                    continue
                dep = path_part or name
                if dep not in source:
                    dep_text = git_bytes(TENANT / "successor/standards" / dep).decode()
                    dep_sections = sections(dep_text)
                else:
                    dep_sections = source[dep]
                assert not fragment or fragment in dep_sections, (name, anchor, target)
                link_checks.append({"source": name + "#" + anchor, "target": target})
    patches = []
    for changed in changes:
        unit_id = changed["id"]; unit = units[unit_id]
        name = Path(changed["path"]).name; anchor = changed["anchor"]
        local_rows = [row for row in families[name] if unit_id in row["consumer_refs"]]
        fields = {}
        if anchor == TABLES[name]:
            argument = {
                "premises": sorted({p for row in families[name] for p in row["premises"]}),
                "conditional_consequence": "The source states distinct conditional consequences for each named consumer from its explicit foundational and instance premises. Pillar contributions supply those relations; the separately owned policies are not inferred from finite capacity.",
                "policy_choices": [row["additional_policy_and_owner"] for row in families[name]],
                "source_refs": [unit_id, "FOUNDATIONS.foundational-commitments"],
                "source_table_scope": "Each row applies only to its named consumer scope. Local source-specific arguments and each owner's conditions, exceptions and modal force remain operative.",
                "standing": "authored_conditional_argument_not_independent_proof",
            }
            if unit["representation_kind"] == "definition_data":
                definition = dict(unit.get("definition") or {})
                definition["source_family_arguments"] = [account_row(row) for row in families[name]]
                fields["definition"] = definition
            else:
                argument["source_family_arguments"] = [account_row(row) for row in families[name]]
                argument["conditional_consequence"] = "Subjects with different owners or kinds and persistent lifecycles must remain distinguishable through representation, transport and owning transitions. Current identity does not prove current content or authority. The scoped minimum is local identity policy; the attached rows state the additional arguments at each actual consumer."
            fields["argument"] = argument
        else:
            argument = dict(LOCAL_ARGUMENTS[unit_id])
            argument.update({"source_refs": [unit_id, name.removesuffix(".md") + "." + TABLES[name], "FOUNDATIONS.foundational-commitments"],
                             "standing": "authored_conditional_argument_not_independent_proof",
                             "source_family_arguments": [account_row(row) for row in local_rows]})
            fields["argument"] = argument
        patches.append({
            **changed,
            "existing_representation_kind": unit["representation_kind"],
            "semantic_fields": fields,
            "preserve_existing_fields": ["predicate", "obligations", "permissions_exceptions", "result_mapping", "representation_kind", "applicability", "dependencies", "dependency_relations"],
            "acquisition_binding": {
                "argument_table_required_when": "The selected task evaluates this family argument or the applicability of one of its rows; ordinary use of a consumer does not require all family-table consumers.",
                "consumer_lists": "All added consumer IDs occur in source_refs as review provenance, not new required-acquisition edges. No consumers field is added or widened.",
                "premises": "Preserve genuine existing foundation, contract and operation dependencies. Evaluating the added conditional argument requires its selected F1-F6 premises and instance assumptions, not every operation named as an example of their use.",
            },
            "source_pin_action": "Refresh body/range and scoped source-block pins from the final source freeze; do not copy old ranges onto changed text.",
            "binding_standing": "authored_complete_for_changed_heading; integration_and_independent_fidelity_pending",
        })
    def check_provenance(value):
        if isinstance(value, dict):
            assert "consumer_refs" not in value
            assert "consumer_heading_refs" not in value
            for child in value.values():
                check_provenance(child)
        elif isinstance(value, list):
            for child in value:
                check_provenance(child)
    for patch in patches:
        assert "consumers" not in patch["semantic_fields"]
        check_provenance(patch["semantic_fields"])
    challenges = json.loads((HERE / "CHALLENGE_CASES.json").read_text())
    for case in challenges["cases"]:
        assert all(ref in units for ref in case["sources"]), case["id"]
    refs = sorted({ref for rows in families.values() for row in rows for ref in row["consumer_refs"]})
    missing = [ref for ref in refs if ref not in units]
    assert not missing, missing
    changed_ids = {r["id"] for r in changes}
    dependents = []
    for unit_id, unit in units.items():
        if unit_id in changed_ids:
            continue
        mapped = [row for rows in families.values() for row in rows if unit_id in row["consumer_refs"]]
        prior = unit.get("argument", {}).get("source_family_arguments", [])
        affected_old = [r for r in prior if any(ref in [n.removesuffix(".md") + "." + a for n, a in TABLES.items()] for ref in r.get("source_refs", []))]
        if mapped or affected_old:
            dependents.append({"id": unit_id, "new_direct_family_arguments": [account_row(row) for row in mapped],
                               "old_family_argument_count": len(affected_old),
                               "action": "Refresh only the scoped family argument references; preserve the unit's predicate, result mapping and more specific local argument. An empty direct list requires owner/subsection applicability assessment, not silent deletion.",
                               "standing": "dependent_integration_required"})
    patch = {
        "kind": "stdo.delivery-source-authored-account-patch", "schema_version": 1,
        "activation": "I4-DELIVERY-SOURCE", "source_preimage": PREIMAGE, "common_input": COMMON, "donor": DONOR,
        "account_preimage": {"commit": PREIMAGE, "path": str(ACCOUNT), "sha256": digest(account_bytes)},
        "standing": "author_input_not_independent_fidelity_evidence",
        "source_pins": pins, "patches": patches, "dependent_argument_refresh": dependents,
        "integration_limits": [
            "No current account, compiler, generated interpretation, frame, compression or conservation artifact is modified.",
            "The four-family tables contain 30 authored arguments. Do not collapse them back to coarse inventory descriptions.",
            "The source-table definitions remain data and the existing consumer/constraint kinds remain unchanged; no new Boolean predicate is introduced.",
            "Block roles, new argument/table source blocks, scoped pointers, dependencies and pins need the integrating account Writer's refresh against the final source freeze.",
            "Consumer inventories are provenance source_refs, not unconditional acquisition edges. Preserve the existing required_when and provenance-aware I3 behavior; do not change compiler defaults to compensate for the account.",
            "Other source owners are concurrently changing; any affected foundation or library relation needs joined-source review after freeze.",
        ],
    }
    (HERE / "ACCOUNT_PATCH.json").write_text(json.dumps(patch, ensure_ascii=False, indent=2) + "\n")
    whitespace = subprocess.run(["git", "diff", "--check", "--", *[str(TENANT / "successor/standards" / n) for n in FILES]], cwd=ROOT, text=True, capture_output=True)
    assert whitespace.returncode == 0, whitespace.stdout + whitespace.stderr
    check = {
        "activation": "I4-DELIVERY-SOURCE", "source_preimage": PREIMAGE,
        "source_pins": pins, "changed_sections": changes,
        "headings_and_order_unchanged": True, "unchanged_section_count": preserved,
        "all_other_sections_byte_identical": True,
        "decision_tails_within_changed_sections_byte_identical": unchanged_decision_tails,
        "family_argument_rows": {n: len(rows) for n, rows in families.items()},
        "changed_section_links_checked": len(link_checks), "missing_links": [],
        "consumer_refs_resolve_in_frozen_account": len(refs),
        "new_consumer_lists_are_provenance_only": True,
        "author_challenge_cases_source_bound": len(challenges["cases"]),
        "changed_heading_account_patches": len(patches), "dependent_argument_units": len(dependents),
        "scoped_git_diff_check": "passed",
        "limits": "These are author structural and preservation checks. They do not prove source entailment, whole-source conservation, interpretation fidelity, reduction, actual-use fit or acceptance.",
    }
    (HERE / "CHECKS.json").write_text(json.dumps(check, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"changed_sections": len(changes), "unchanged_sections": preserved, "family_rows": sum(len(r) for r in families.values()), "links_checked": len(link_checks), "consumer_refs": len(refs), "account_patches": len(patches), "dependent_units": len(dependents), "whitespace": "passed"}))


if __name__ == "__main__":
    main()
