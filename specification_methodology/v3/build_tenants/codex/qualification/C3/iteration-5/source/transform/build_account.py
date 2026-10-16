"""Authored consumer delta and exact source binding; no fidelity verdict."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
I5 = HERE.parents[1]
TENANT = I5.parents[2]
PACKAGE = TENANT / "successor"
sys.path.insert(0, str(I5 / "tools"))
from account_protocol import heading_units, make_owner

PREIMAGE = "11163991fd8525c98bdd94a36c71a2cfeb15a403"
COMMON = "4c340f7adec9f3c893e3e267b23e4cadeb357854"
PINS = {
    "standards/TRANSFORMATION_LIBRARY.md": "5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10",
    "standards/STDO_REFERENCE_FRAME_BASELINE.md": "c586746143bc060ed1e96efe520972aa4daee46d158415cf94d5cdcbc8b94067",
}
sha = lambda raw: hashlib.sha256(raw).hexdigest()
CURRENT = {path: (PACKAGE / path).read_bytes() for path in PINS}
BEFORE = {path: subprocess.check_output(["git", "show", PREIMAGE + ":specification_methodology/v3/build_tenants/codex/successor/" + path]) for path in PINS}
for path, expected in PINS.items():
    assert sha(CURRENT[path]) == expected, "Re-enter authorship if a frozen consumer changes"
assert sha((PACKAGE / "standards/FOUNDATIONS.md").read_bytes()) == "a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336"
OLD = {r["id"]: r for r in json.loads((I5.parent / "iteration-4/DETERMINATIONS.json").read_text())["determinations"]}
CORE_PATCH = json.loads((I5 / "source/core/ACCOUNT_PATCH.json").read_text())
KNOWN = set(OLD) | {r["id"] for r in CORE_PATCH["new_rows"]}


def unit(path, anchor, old=False):
    return heading_units(BEFORE[path] if old else CURRENT[path])[anchor]


def paragraph(path, anchor, prefix):
    selected = unit(path, anchor)
    matches = [m for m in re.finditer(rb"\S[^\n]*(?:\n(?!\n)[^\n]*)*", selected["body"])
               if m.group().decode().startswith(prefix)]
    assert len(matches) == 1, (anchor, prefix, len(matches))
    match = matches[0]
    return selected["byte_start"] + match.start(), selected["byte_start"] + match.end()


def dependency(row, identifier, binding, when):
    if identifier not in row["dependencies"]:
        row["dependencies"].append(identifier)
    row.setdefault("dependency_relations", []).append({"id": identifier, "kind": "conditional_contract_application", "binding": binding, "required_when": when})


def resolve(row, pointer):
    value = row
    for part in pointer.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def annotation(row, block, pointers):
    for pointer in pointers:
        resolve(row, pointer)
    return {"source_clause_id": row["id"] + "#" + block["id"], "source_block_id": block["id"],
            "source_block_sha256": block["sha256"], "source_byte_start": block["byte_start"], "source_byte_end": block["byte_end"],
            "source_roles": block["roles"], "represented_at": [{"role": "O", "pointer": pointer} for pointer in pointers],
            "standing": "author_source_to_representation_mapping_not_fidelity_verdict"}


def bind_delta(row, replacements, additions):
    """Keep exact old spans; author each changed body/paragraph and new block."""
    path, anchor = row["owner"]["path"], row["owner"]["anchor"]
    current, old = CURRENT[path], BEFORE[path]
    selected = unit(path, anchor)
    prior = OLD[row["id"]]
    updated = []
    role_index = {role["source_block_id"]: copy.deepcopy(role) for role in prior.get("source_clause_roles", [])}
    for original in prior["source_clauses"]:
        block = copy.deepcopy(original)
        identifier = block["id"]
        original_bytes = old[block["byte_start"]:block["byte_end"]]
        assert sha(original_bytes) == block["sha256"]
        if identifier == "body":
            # The existing explicit source-owned body changes with its owner.
            # Its former granularity is preserved, not guessed from a digest.
            assert original_bytes == unit(path, anchor, old=True)["body"]
            start, end = selected["byte_start"], selected["byte_end"]
        elif identifier in replacements:
            prefix, _ = replacements[identifier]
            start, end = paragraph(path, anchor, prefix)
        else:
            positions = [match.start() for match in re.finditer(re.escape(original_bytes), selected["body"])]
            assert len(positions) == 1, (row["id"], identifier, "unchanged block must resolve uniquely")
            start = selected["byte_start"] + positions[0]
            end = start + len(original_bytes)
        block.update(byte_start=start, byte_end=end, sha256=sha(current[start:end]))
        updated.append(block)
        if identifier in role_index:
            role_index[identifier].update(source_clause_id=row["id"] + "#" + identifier, source_block_sha256=block["sha256"], source_byte_start=start, source_byte_end=end)
        if identifier in replacements:
            role_index[identifier] = annotation(row, block, replacements[identifier][1])
    for number, (prefix, pointers, source_roles) in enumerate(additions, 1):
        start, end = paragraph(path, anchor, prefix)
        block = {"id": "i5c" + str(number), "sha256": sha(current[start:end]), "byte_start": start, "byte_end": end, "roles": source_roles}
        updated.append(block)
        role_index[block["id"]] = annotation(row, block, pointers)
    row["source_clauses"] = updated
    row["source_clause_ids"] = [row["id"] + "#" + block["id"] for block in updated]
    # Existing rows without a detailed role map remain bounded legacy bindings;
    # the new/changed contributions have explicit authored roles. No omitted old
    # semantic assessment is silently promoted to complete by this delta.
    row["source_clause_roles"] = list(role_index.values())
    for role in row["source_clause_roles"]:
        for target in role["represented_at"]:
            resolve(row, target["pointer"])


UPDATES = []


def edit(identifier):
    row = copy.deepcopy(OLD[identifier])
    row["owner"] = make_owner(row["owner"]["path"], row["owner"]["anchor"], CURRENT[row["owner"]["path"]])
    return row


def append(row, text):
    row["obligations"].append(text)
    return "/obligations/" + str(len(row["obligations"]) - 1)


def finish(row, replacements=None, additions=None):
    bind_delta(row, replacements or {}, additions or [])
    before = OLD[row["id"]]
    fields = {k: v for k, v in row.items() if k not in {"id", "owner"} and before.get(k) != v}
    UPDATES.append({"id": row["id"], "preimage_body_sha256": before["owner"]["body_sha256"],
                    "candidate_body_sha256": row["owner"]["body_sha256"], "semantic_fields": fields})


row = edit("TRANSFORMATION_LIBRARY.contract-application")
row["obligations"][0]["conditions"]["Preservation"] = "Establish material input/output/cross-boundary relations under declared compatibility or translation, applying Foundations Preservation obligations to the claimed step/composition. Retain identity, meaning, lifecycle, producer/evidence coordinates, constraints, authority and effects. Lawful differences require the admitted instance relation; neither universal equality nor invented translation decides compatibility."
row["obligations"][0]["conditions"]["Currentness"] = "Acquire observations/concurrency/uncertain effects under Workspace and context, and apply Change impact and evidence retention to existing evidence. Supported changed dependencies reopen affected determination; unsupported currentness stays unresolved. Supported unchanged premises permit reuse without rechecking fixed graphs or every unchanged relation on every event."
dependency(row, "FOUNDATIONS.preservation-obligations", "Bind support for the instance's claimed step or composition.", "a preservation relation is material to application")
dependency(row, "FOUNDATIONS.change-impact-and-evidence-retention", "Establish applicability of existing evidence.", "application relies on retained evidence")
finish(row, {"c3": ("1. **Binding.**", ["/obligations/0"])})

row = edit("TRANSFORMATION_LIBRARY.evaluate")
pointer = append(row, "Apply Assertions and observations to the source obligation, interpreted required predicate, actual assertion and observation/checker basis. Establish the implication used for broader reliance, support actual acquisition, and preserve assertion derivation separately from execution provenance. Keep the original predicate and distinguish unresolved fidelity, unavailable observation and non-performance; source/execution authentication alone supplies no missing justification.")
dependency(row, "FOUNDATIONS.assertions-and-observations", "Bind assertion strength, checker and actual observation support.", "an evaluation conclusion is relied on")
dependency(row, "FOUNDATIONS.parallel-assurance-and-provenance", "Retain justified assertion and actual execution provenance.", "an evaluation conclusion is relied on")
finish(row, additions=[("Bind [Assertions and observations]", [pointer], ["obligation", "scope", "result"])])

row = edit("TRANSFORMATION_LIBRARY.conjoin")
pointer = append(row, "For mutual assurance from compared or repeated evidence, apply Parallel assurance and provenance to shared causes/dependencies and Risk and assurance selection to quantitative confidence. Preserve the existing logical conjunction; multiple predicates from one execution are not independent observations.")
dependency(row, "FOUNDATIONS.parallel-assurance-and-provenance", "Account for material shared causes in compared/repeated evidence.", "results supply mutual assurance")
dependency(row, "FOUNDATIONS.risk-and-assurance-selection", "Support any claimed quantitative confidence.", "a quantitative confidence claim is made")
finish(row, additions=[("When comparison or repeated evidence", [pointer], ["obligation", "scope"])])

row = edit("TRANSFORMATION_LIBRARY.composition-law")
pointer = append(row, "Apply Preservation obligations to boundary properties, assumptions, transitions and the outer outcome. Bind initial/step/join/final support for this composition and separately support actual execution, branches, concurrency and external effects. Retain supported locals when outer support is unresolved; refinements/approximations use the same owner's preservation and complete-composition adequacy.")
dependency(row, "FOUNDATIONS.preservation-obligations", "Bind the actual composite's preservation premises and execution conformance.", "a step or outer composition claim is made")
finish(row, additions=[("Apply [Preservation obligations]", [pointer], ["obligation", "scope", "latitude"])])

row = edit("TRANSFORMATION_LIBRARY.recovery-law")
row["obligations"][2] = "Select assurance from applicable retained evidence and required reassessment. A selected proof must falsify the affected relation and meet required independence; apply UP-014 inside Risk and assurance selection, accounting for acquisition, impact-analysis and assessment costs. For private-state-independent continuity, exclude that state and compare reconstruction with current reality; a same-context exercise does not establish it."
pointer = append(row, "Apply Change impact and evidence retention to observed change, assertion justification and material execution/validity dependencies. Establish historical evidence applicability while retaining its old subject; keep unknown impact, new cases, gates, failures and uncovered obligations. Selection itself produces no new execution result.")
dependency(row, "FOUNDATIONS.change-impact-and-evidence-retention", "Bind change impact and retained historical support before reuse.", "recovery relies on earlier evidence or observed changed support")
dependency(row, "FOUNDATIONS.risk-and-assurance-selection", "Constrain recovery proof and total-cost selection by required assurance.", "recovery assurance is selected")
finish(row, {"c3": ("Select assurance for the affected relation", ["/obligations/2"])}, [("Bind [Change impact and evidence retention]", [pointer], ["obligation", "scope", "result"])])

row = edit("STDO_REFERENCE_FRAME_BASELINE.derived-product-testing-frame-set")
pointer = append(row, "Apply Construction assurance to each selected testing claim, binding the requirement/refinement source, asserted predicate, observation basis and required assurance. Existing adoption, ordinary-path and exact-subject conditions remain; no new archetype or mandatory actor follows.")
dependency(row, "FOUNDATIONS.construction-assurance", "Apply the common assurance owner to each declared testing claim.", "the testing frame is adopted and selected")
finish(row, additions=[("Apply [Construction assurance]", [pointer], ["obligation", "scope", "latitude"])])

row = edit("STDO_REFERENCE_FRAME_BASELINE.combinatorial-coverage-and-testing-value-index")
row["obligations"][1] += " Interaction coverage is not a probability or statistical-independence claim."
pointer = append(row, "Admitted work authority selects testing assurance under Risk and assurance selection, binding failure consequences, coverage, uncertainty and action/acceptance conditions. Cost includes acquisition, impact analysis, execution and assessment with estimates distinct from measurements. Numeric confidence uses supported probability/dependence/calibration, not this index or test count.")
dependency(row, "FOUNDATIONS.risk-and-assurance-selection", "Select testing assurance and support any numeric confidence within its risk model.", "testing strategy or numeric confidence is selected")
finish(row, {"c6": ("At integration, end-to-end, and user-acceptance altitude", ["/obligations/1"])}, [("The admitted work authority selects the needed testing assurance", [pointer], ["obligation", "scope"])])

row = edit("STDO_REFERENCE_FRAME_BASELINE.testing-evidence-composition")
pointer = append(row, "For mutual assurance, apply Parallel assurance and provenance to each justified requirement/refinement assertion path and actual execution. Retain shared fixtures, tools, observations, interpretations and received contributions; overlapping claims from one run are not independent observations. Keep existing logical conjunction, failures, missing claims and required assessment authorship.")
dependency(row, "FOUNDATIONS.parallel-assurance-and-provenance", "Account for provenance and shared failure causes without changing conjunction.", "testing results supply mutual assurance")
finish(row, additions=[("Apply [Parallel assurance and provenance]", [pointer], ["obligation", "scope"])])

row = edit("STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation")
p1 = append(row, "Apply Assertions and observations to the oracle and actual subject: state target predicate, scope and justified relation to the requirement/refinement. A narrower assertion supports only its actual conclusion; choose the required acceptable relation without assuming equal valid outputs. Support real observation/checker conformance and material discriminations; retain missing support and the original core predicate instead of promoting a reported pass/failure.")
p2 = append(row, "Retain assertion and execution provenance separately in existing source/test/evidence bindings through Parallel assurance and provenance. A common derivation may serve a declared family; implementation-derived checks retain local/regression use but do not meet this profile's independent upstream-oracle condition by repeating implementation answers.")
dependency(row, "FOUNDATIONS.assertions-and-observations", "Justify the oracle's source relation and actual acquired observation.", "an assertion result supports this claim")
dependency(row, "FOUNDATIONS.parallel-assurance-and-provenance", "Keep expected-predicate derivation and actual execution provenance distinct.", "assertion/execution evidence is relied on")
finish(row, additions=[("Apply [Assertions and observations]", [p1], ["obligation", "scope", "result"]), ("The existing source, test and evidence bindings", [p2], ["obligation", "latitude"])])

row = edit("STDO_REFERENCE_FRAME_BASELINE.counterexample-localization")
pointer = append(row, "Before using an observed test failure against a broader obligation, establish that relation through Evaluate; otherwise retain the actual bounded result and unresolved assertion/observation support. Diagnostic work keeps Spec's owner and a test label supplies no cause, repair class or authority.")
dependency(row, "TRANSFORMATION_LIBRARY.evaluate", "Establish whether the observed test failure defeats the broader claimed obligation.", "test failure is used as a counterexample to that broader obligation")
finish(row, additions=[("Before using an observed test failure", [pointer], ["obligation", "scope", "result"])])

anchor = "testing-reassessment-and-evidence-reuse"
identifier = "STDO_REFERENCE_FRAME_BASELINE." + anchor
path = "standards/STDO_REFERENCE_FRAME_BASELINE.md"
new = {"id": identifier, "family": "Testing Reassessment And Evidence Reuse", "owner": make_owner(path, anchor, CURRENT[path]),
       "coverage_standing": "bounded_author_binding", "representation_kind": "consumer_binding", "family_ref": path,
       "unit_kind": OLD["TRANSFORMATION_LIBRARY.evaluate"]["unit_kind"], "interpretation_standing": "bounded_semantic_binding",
       "predicate": "The adopted testing assessment covers affected/new obligations and gates while retaining only evidence applicable to the new subject and basis.",
       "applicability": "An adopted Baseline testing claim undergoes a material subject/basis/dependency change, reassessment, recovery or evidence reuse.",
       "obligations": [
           "Apply Change impact and evidence retention to the selected claim/change; distinguish assertion-source justification from implementation, fixture/data, instrument, tool, environment and other validity dependencies. Use conservative impact/exclusion conditions; unknown influence cannot drop work, new uncovered obligations require assessment and mandatory gates remain.",
           "Keep old execution subjects and establish the new applicability relation. Add actual reassessment while preserving failed, indeterminate and unperformed conditions. Selection supplies no execution evidence; changed requirements revise expectations through owners, and implementation/environment corrections revisit affected execution/integration under applicable obligations.",
           "Select assessment strategy within required assurance/risk and total selection/execution costs. Retain residual combinations and counterexamples in the existing account; broader testing remains available where impact/policy requires it."],
       "permissions_exceptions": ["Supported unaffected evidence need not be re-executed solely because another dependency changed. No fixed full-suite cadence or independent test ledger is added."],
       "dependencies": [], "dependency_relations": [], "inputs": [
           {"description": "Selected testing claim, exact old/new subject and basis, actual change and material assertion/execution/validity dependencies.", "required_when": "Assessing changed applicability or selecting reassessment.", "standing": "required_at_instance_not_missing_source"},
           {"description": "Original execution evidence, failures and unresolved coverage, with support for retained applicability and actual new assessment.", "required_when": "Relying on retained or reassessed evidence.", "standing": "required_at_instance_not_missing_source"},
           {"description": "Required assurance, risk policy, mandatory gates and relevant selection/execution costs.", "required_when": "Selecting the reassessment strategy.", "standing": "required_at_instance_not_missing_source"}],
       "consumers": ["STDO_REFERENCE_FRAME_BASELINE.derived-product-testing-frame-set", "STDO_REFERENCE_FRAME_BASELINE.testing-evidence-composition", "STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation"],
       "scope_refs": ["STDO_REFERENCE_FRAME_BASELINE.status-and-authority-boundary"], "source_references": [],
       "result_mapping": copy.deepcopy(OLD["STDO_REFERENCE_FRAME_BASELINE.testing-evidence-composition"]["result_mapping"]),
       "argument": {"premises": [{"id": value, "kind": "foundational_premise", "owner": "FOUNDATIONS.foundational-commitments"} for value in ["F2", "F3", "F4", "F5", "F6"]],
                    "conditional_consequence": "On this adopted testing claim, changed validity dependencies require affected reassessment without erasing independently applicable evidence, known failures or required coverage.",
                    "policy_choices": ["The adopting Product and existing mandate choose testing scope, gates, risk policy and strategy; Foundations owns the shared impact and retention relation."],
                    "source_refs": [identifier, "FOUNDATIONS.change-impact-and-evidence-retention", "FOUNDATIONS.risk-and-assurance-selection"],
                    "clause_arguments": [], "source_family_arguments": [], "standing": "authored_conditional_argument_not_independent_entailment_proof"},
       "source_clauses": [], "source_clause_ids": [], "source_clause_roles": []}
new["result_mapping"]["predicate_binding"] = new["predicate"]
new["result_mapping"].update(evaluation_contract_ref="core.shared_contracts.core_evaluation", owner_refs=["FOUNDATIONS.result-algebra", "FOUNDATIONS.result-conjunction"])
for ident, binding in [
    ("FOUNDATIONS.change-impact-and-evidence-retention", "Apply the single dependency, impact, exclusion and retention owner."),
    ("FOUNDATIONS.risk-and-assurance-selection", "Preserve required assurance and risk while selecting cost-effective assessment."),
    ("STDO_REFERENCE_FRAME_BASELINE.status-and-authority-boundary", "Preserve optional profile adoption and existing authority."),
    ("STDO_REFERENCE_FRAME_BASELINE.derived-product-testing-frame-set", "Bind the actual testing claim, subject, population and required evidence."),
    ("FOUNDATIONS.result-algebra", "Preserve original verdict, performance and effect distinctions.")]:
    dependency(new, ident, binding, "within the declared adopted testing applicability")
for number, prefix in enumerate(["Apply [Change impact and evidence retention]", "Retain each old execution's subject", "Choose the assessment strategy"], 1):
    start, end = paragraph(path, anchor, prefix)
    block = {"id": "c" + str(number), "byte_start": start, "byte_end": end, "sha256": sha(CURRENT[path][start:end]), "roles": ["obligation", "scope"] + (["latitude"] if number == 3 else [])}
    new["source_clauses"].append(block)
    role = annotation(new, block, ["/obligations/" + str(number - 1)])
    if number == 3:
        role["represented_at"].append({"role": "P", "pointer": "/permissions_exceptions/0"})
        resolve(new, "/permissions_exceptions/0")
    new["source_clause_roles"].append(role)
new["source_clause_ids"] = [item["source_clause_id"] for item in new["source_clause_roles"]]
NEW = [new]
KNOWN.add(identifier)

PATCH = {"schema_version": "stdo.i5.authored-account-patch/v1", "common_input": COMMON,
         "source_preimage": PREIMAGE, "producer": "I5-WRITE-TRANSFORM", "owner_paths": list(PINS),
         "updates": UPDATES, "new_rows": NEW}
assert len(UPDATES) == 10 and len(NEW) == 1
for update in UPDATES:
    prior = OLD[update["id"]]
    assert sha(unit(prior["owner"]["path"], prior["owner"]["anchor"], old=True)["body"]) == update["preimage_body_sha256"]
    rebuilt = copy.deepcopy(prior); rebuilt.update(update["semantic_fields"])
    introduced = set(rebuilt.get("dependencies", []) + rebuilt.get("consumers", [])) - set(prior.get("dependencies", []) + prior.get("consumers", []))
    assert introduced <= KNOWN, (update["id"], introduced - KNOWN)
for row in NEW:
    assert row["id"] not in OLD
    assert set(row["dependencies"] + row["consumers"] + row["scope_refs"]) <= KNOWN
for path in PINS:
    before, current = heading_units(BEFORE[path]), heading_units(CURRENT[path])
    changed = {anchor for anchor in before if before[anchor]["body"] != current[anchor]["body"]}
    authored = {OLD[u["id"]]["owner"]["anchor"] for u in UPDATES if OLD[u["id"]]["owner"]["path"] == path}
    assert changed == authored, (path, changed, authored)
    assert set(current) - set(before) == {r["owner"]["anchor"] for r in NEW if r["owner"]["path"] == path}
destination = HERE / "ACCOUNT_PATCH.json"
destination.write_text(json.dumps(PATCH, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"patch": str(destination.relative_to(TENANT)), "sha256": sha(destination.read_bytes()), "updates": len(UPDATES), "new_rows": len(NEW), "source_pins": PINS}, indent=2))
