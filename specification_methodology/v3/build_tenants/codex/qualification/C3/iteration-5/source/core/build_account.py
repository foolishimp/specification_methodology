"""Author the bounded core contribution; source pins do not assess fidelity."""
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
OWNER = "standards/FOUNDATIONS.md"
REPO_PATH = "specification_methodology/v3/build_tenants/codex/successor/" + OWNER
SOURCE = (PACKAGE / OWNER).read_bytes()
BEFORE = subprocess.check_output(["git", "show", PREIMAGE + ":" + REPO_PATH])
PIN = "a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336"
sha = lambda value: hashlib.sha256(value).hexdigest()
assert sha(SOURCE) == PIN, "Re-enter authoring if the frozen core subject changes"
old_units, units = heading_units(BEFORE), heading_units(SOURCE)
BASE = json.loads((I5.parent / "iteration-4" / "DETERMINATIONS.json").read_text())
OLD = {row["id"]: row for row in BASE["determinations"]}
CORE_RESULT = copy.deepcopy(OLD["FOUNDATIONS.bounded-construction"]["result_mapping"])


def fid(anchor):
    return "FOUNDATIONS." + anchor


def source_families():
    result = []
    scope = "Only when assessing this family argument, its applicability, consequence, conservation, coverage or fidelity against this consumer. This is not an unconditional operational dependency."
    unit = units["core-contract-derivations"]
    for number, line in enumerate(SOURCE.splitlines(keepends=True), 1):
        if not unit["start_line"] <= number <= unit["end_line"]:
            continue
        text = line.decode().strip()
        if not text.startswith("| ") or text.startswith("| Deciding"):
            continue
        cells = [cell.strip() for cell in text.split("|")[1:-1]]
        if len(cells) != 4:
            raise ValueError("Unexpected argument-table arity")
        result.append({
            "family": cells[0], "declared_consumer_scope": cells[0],
            "premises": sorted(set(re.findall(r"F[1-6]", cells[1]))),
            "premise_and_pillar_argument": cells[1],
            "conditional_consequence": cells[2], "additional_policy_and_owner": cells[3],
            "source_row": {"path": OWNER, "anchor": "core-contract-derivations", "line": number,
                           "sha256": sha(line), "hash_boundary": "Exact Markdown row including terminal newline."},
            "source_refs": [{"path": OWNER, "anchor": "core-contract-derivations", "role": "provenance", "required_when": scope}],
            "required_when": scope,
        })
    assert len(result) == 18
    return result


FAMILIES = source_families()


def family_for(anchor):
    return [copy.deepcopy(item) for item in FAMILIES if "(#" + anchor + ")" in item["family"]]


def paragraph_blocks(anchor):
    unit = units[anchor]
    # Explicitly selected authored granularity: each immediate-section prose,
    # formula or table block. This does not discover obligations or their roles.
    matches = list(re.finditer(rb"\S[^\n]*(?:\n(?!\n)[^\n]*)*", unit["body"]))
    assert matches and matches[0].group().startswith(b"#")
    return [(unit["byte_start"] + m.start(), unit["byte_start"] + m.end()) for m in matches[1:]]


def resolve(value, pointer):
    for part in pointer.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def bind_blocks(row, plan):
    """The caller authors the exact role and semantic pointer for every block."""
    anchor = row["owner"]["anchor"]
    blocks = paragraph_blocks(anchor)
    assert len(blocks) == len(plan), (anchor, len(blocks), len(plan))
    clauses, roles = [], []
    for number, ((start, end), (source_roles, targets)) in enumerate(zip(blocks, plan), 1):
        block_id = "c" + str(number)
        block = {"id": block_id, "sha256": sha(SOURCE[start:end]), "byte_start": start, "byte_end": end, "roles": source_roles}
        clauses.append(block)
        represented = [{"role": role, "pointer": pointer} for role, pointer in targets]
        for item in represented:
            resolve(row, item["pointer"])
        roles.append({"source_clause_id": row["id"] + "#" + block_id, "source_block_id": block_id,
                      "source_block_sha256": block["sha256"], "source_byte_start": start, "source_byte_end": end,
                      "source_roles": source_roles, "represented_at": represented,
                      "standing": "author_source_to_representation_mapping_not_fidelity_verdict"})
    row["source_clauses"] = clauses
    row["source_clause_ids"] = [item["source_clause_id"] for item in roles]
    row["source_clause_roles"] = roles


def O(number):
    return ("O", "/obligations/" + str(number))


def P(number):
    return ("P", "/permissions_exceptions/" + str(number))


def D(number):
    return ("D", "/definition/clauses/" + str(number))


def add_dependency(row, identifier, binding, required_when="within the declared applicability"):
    if identifier not in row.setdefault("dependencies", []):
        row["dependencies"].append(identifier)
    relation = {"id": identifier, "kind": "contract_application", "binding": binding, "required_when": required_when}
    row.setdefault("dependency_relations", []).append(relation)


def argument(anchor, premises, consequence, choices):
    return {"premises": [{"id": p, "kind": "foundational_premise", "owner": fid("foundational-commitments")} for p in premises],
            "conditional_consequence": consequence, "policy_choices": choices,
            "source_refs": [fid(anchor), fid("foundational-commitments")],
            "clause_arguments": [], "standing": "authored_conditional_argument_not_independent_entailment_proof",
            "source_family_arguments": family_for(anchor)}


def new_row(anchor, predicate, applicability, obligations, permissions, definitions,
            premises, consequence, choices, consumers, dependencies, kind="constraint"):
    row = {"id": fid(anchor), "family": units[anchor]["heading"], "owner": make_owner(OWNER, anchor, SOURCE),
           "coverage_standing": "bounded_author_binding", "predicate": predicate, "applicability": applicability,
           "obligations": obligations, "permissions_exceptions": permissions,
           "dependencies": [], "dependency_relations": [], "inputs": [], "consumers": consumers,
           "result_mapping": copy.deepcopy(CORE_RESULT),
           "argument": argument(anchor, premises, consequence, choices),
           "unit_kind": OLD[fid("bounded-construction")]["unit_kind"],
           "scope_refs": [fid("premises-and-standing")], "interpretation_standing": "bounded_semantic_binding",
           "source_references": [], "representation_kind": kind, "family_ref": OWNER,
           "definition": {"kind": "supporting_definitions", "structures": {}, "clauses": definitions}}
    for identifier, binding, when in dependencies:
        add_dependency(row, identifier, binding, when)
    add_dependency(row, fid("premises-and-standing"), "Selected methodology scope and source-owned authority.")
    add_dependency(row, fid("foundational-commitments"), "Only the named premise subset supports the conditional argument.")
    add_dependency(row, fid("result-algebra"), "Preserve verdict, evaluation performance, original domain outcome and material effects.")
    return row


NEW = []
row = new_row("construction-assurance",
    "Dependent reliance binds the applicable preservation, assertion, observation, dependence, risk and evidence-validity relationships on its exact claim.",
    "A consumer relies on construction or assurance evidence for its selected obligation.",
    ["Bind the source obligation, interpreted predicate, exact subject, governing basis, assumptions and admissible evidence.",
     "Apply preservation at material construction joins; assertion and observation justification at evaluation; dependence and risk at evidence selection; applicability at change or reuse.",
     "Return conclusions through the core result record and combine required predicates through the core conjunction."],
    ["The consumer supplies domain policy and required assurance. No additional stage, role, record or authority is introduced."],
    [], ["F1", "F2", "F4", "F6"],
    "A reported pass, formula or combined result supports only the claim established by the applicable assurance relations.",
    ["Domain policy selects required assurance and admissible evidence within existing authority."],
    ["TRANSFORMATION_LIBRARY.evaluate", "TRANSFORMATION_LIBRARY.conjoin", "STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation", "TICKET_METHOD.condition-based-closure-and-reuse"],
    [(fid(a), binding, when) for a, binding, when in [
        ("preservation-obligations", "Bind preservation premises and joins.", "a construction or composition claim is relied on"),
        ("assertions-and-observations", "Justify the assertion and observation basis.", "an evaluation conclusion is relied on"),
        ("parallel-assurance-and-provenance", "Retain assertion/execution provenance and shared causes.", "construction or assurance paths are compared"),
        ("risk-and-assurance-selection", "Select required assurance within governing risk and resource limits.", "assurance work or quantitative confidence is selected"),
        ("change-impact-and-evidence-retention", "Establish affected claims and retained applicability.", "a change, recovery or evidence reuse occurs"),
        ("result-conjunction", "Retain required predicates and material joins.", "required results are combined")]], "consumer_binding")
bind_blocks(row, [(["obligation", "scope", "latitude"], [O(0), O(1), O(2), P(0)])]); NEW.append(row)

row = new_row("preservation-obligations",
    "The claimed preservation step or end-to-end construction has its applicable initial, transition, join and outcome implications established on the declared domain.",
    "Preservation, refinement, invariant or end-to-end claims over selected state or trace transformations, including material effects and approximations.",
    ["Bind A, Z, governing assumptions, state/trace domains, transition relations and boundary properties; include material effect and trace conditions in the outcome.",
     "Establish P_i(x) and F_i(x,x') implies P_(i+1)(x') for every admitted pair claimed by the step.",
     "For an end-to-end claim establish the initial condition, each applicable step, compatible preconditions/postconditions and the final implication to Z. Acquire missing join conditions. An invariant requires its initial case and every admitted preservation step; it proves neither progress nor termination.",
     "Cover material outcomes, effects and assumptions. A successful-completion relation gives no refusal/failure/interruption/unknown-effect claim. Actual execution conformance is separate; branches, concurrency and external effects need their applicable composition law.",
     "Exact transformations preserve declared meaning. Approximation requires its adequacy relation and an established complete-composition bound, not merely local tolerances. Identify cross-account maps and preservation.",
     "Keep stated formulas, discharged arguments, mechanical checks, finite models, sampled tests and observed execution at their distinct scope; retain unresolved universal claims."],
    ["Supported local claims remain usable while an unsupported outer claim remains unresolved.",
     "An unavailable universal proof stops dependent work requiring it; otherwise admitted bounded construction can continue."],
    [{"X_i": "Declared state or trace domain at boundary i.", "F_i": "Declared relation contained in X_i x X_(i+1).", "P_i": "Boundary property to retain or establish.", "Gamma": "Governing assumptions."}],
    ["F2", "F4"], "A locally supported step cannot establish an unsupported join, arrival, concurrency or execution-conformance claim.",
    ["The composite owner selects properties and admitted loss; the execution binding supports actual conformance. Stronger mathematical claims need their own premises."],
    ["TRANSFORMATION_LIBRARY.composition-law", "FOUNDATIONS.typed-composition-and-conservation", "FOUNDATIONS.orthogonal-descriptions"],
    [(fid("bounded-construction"), "Bind current A, selected Z and distinct progress/completion claims.", "within the declared applicability"),
     (fid("orthogonal-descriptions"), "Apply the categorical demonstration for cross-account categorical claims.", "a categorical claim is made")])
bind_blocks(row, [(["scope", "obligation", "definition"], [O(0), D(0)]), (["obligation"], [O(1)]),
    (["obligation", "latitude"], [O(2), P(0)]), (["obligation", "scope"], [O(3)]),
    (["obligation", "latitude", "scope"], [O(4), O(5), P(1)])]); NEW.append(row)

row = new_row("assertions-and-observations",
    "The claimed assertion conclusion faithfully relates to its source obligation and is supported by the admitted checker and actual observation basis on its declared domain.",
    "Interpreting an obligation, selecting an assertion, or relying on checker soundness, completeness, observation sufficiency or reported test results.",
    ["Interpret the owning obligation on declared assumptions and cases including material inputs, behaviour and environment, preserving conditions, exceptions and alternatives. Text identity alone proves no interpretation fidelity.",
     "State whether the assertion targets the full obligation or a narrower condition, and justify the implication relied on. A necessary-condition pass cannot establish the full obligation; a sufficient conjunction needs coverage and compatibility.",
     "An equality oracle is justified only where the obligation requires equal outputs; different outputs may satisfy the same acceptable relation.",
     "For every admitted case, a satisfied checker verdict implies the asserted predicate and a falsified verdict implies its negation, wherever those soundness directions are claimed. Retain unresolved support.",
     "Universal soundness covers every admitted conclusion, not a favourable selected run. Actual checker and observation acquisition need conformance support; a selected model or ideal observation map does not supply it.",
     "A reported pass or failure remains observation until oracle and observation justification support the claimed conclusion. Preserve original predicate, actual performance, uncertain effects and independently admissible counterevidence through the core.",
     "A checker that always decides correctly from pi alone requires equal observations to imply equal predicate truth. A collision requires distinguishing evidence, justified narrower scope or indeterminate on that attempted decision."],
    ["Human/probabilistic checkers may admit both a sound satisfied result and indeterminate. Deterministic checking is a scoped special case; the relation supplies no probability distribution.",
     "In a classical set model observation sufficiency permits a predicate on pi's image, but supplies no executable procedure or cost bound."],
    [{"Q_r": "interpret(r, Gamma, Omega), the required predicate preserving the obligation's scope.", "q_t": "Assertion target predicate."},
     {"necessary": "Q_r implies q_t", "sufficient": "q_t implies Q_r", "sufficient_conjunction": "(q_1 and ... and q_n) implies Q_r"},
     {"pi": "Omega -> O, available-observation model", "T": "Admitted evaluation relation contained in O x R", "R": "Existing core result records", "sat_fal": "Abbreviations for core verdicts on q_t, not execution states."},
     {"sound_satisfaction": "For every s: (pi(s),sat) in T implies q_t(s)", "sound_falsification": "For every s: (pi(s),fal) in T implies not q_t(s)"},
     {"observation_sufficiency": "For all s,s' in Omega: pi(s)=pi(s') implies q_t(s)=q_t(s')"}],
    ["F1", "F2", "F3", "F6"], "Insufficient assertion strength or observations cannot support the broader required conclusion; favourable runs do not prove universal soundness.",
    ["The source owner selects required meaning. The evaluation binding selects justified scope and instrumentation; probability and computational feasibility need further models."],
    ["TRANSFORMATION_LIBRARY.evaluate", "STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation", "FOUNDATIONS.judgment-and-authority"],
    [(fid("interpretation-and-representation"), "Retain source-to-predicate meaning.", "within the declared applicability")])
bind_blocks(row, [(["obligation", "scope", "definition"], [O(0), D(0)]), (["obligation"], [O(1)]),
    (["definition"], [D(1)]), (["obligation", "latitude"], [O(1), O(2)]),
    (["definition", "result"], [D(2)]), (["obligation", "definition"], [O(3), D(3)]),
    (["obligation", "latitude"], [O(3), O(4), P(0)]), (["obligation", "result"], [O(5)]),
    (["obligation"], [O(6)]), (["definition", "obligation"], [O(6), D(4)]),
    (["obligation", "latitude"], [O(5), O(6), P(1)])]); NEW.append(row)

row = new_row("parallel-assurance-and-provenance",
    "Comparison and reliance on assertion/construction paths preserve their source justification, execution provenance, shared failure causes and applicable independence conditions.",
    "Construction and assertion paths share an obligation, or evidence from different constructions, checks, actors or received contributions is compared or combined.",
    ["Justify each path's actual source and scope: requirement and refinement assertions assess their own applicable conditions; neither automatically covers the other.",
     "Preserve assertion provenance (obligation, interpretation, assumptions, derivation, shared dependencies) separately from execution provenance (actual checker, exact subject, environment, inputs, observations, result). Logs alone cannot justify the expected predicate.",
     "An implementation-derived assertion provides no independent upstream fidelity merely by repeating the implementation. Claims that a shorter path saves cost require evidence for that path and establish no automatic correctness, coverage or independence.",
     "Agreement permits shared error; disagreement requires diagnosis without identifying the faulty party. Account for shared specifications, interpretations, tools, fixtures, observations, copied contributions and other failure causes. Actor/family/codebase differences and repeated observations do not establish statistical independence.",
     "Validate a common model against its purpose and material external observations through their owners. Agreement inside the model cannot do so; preserve counterexamples and route correction through bounded construction and its authority."],
    ["Implementation-derived checks remain useful for regression or an explicitly scoped local property.",
     "One shared derivation may cover a declared family in existing bindings and evidence, without a per-test document. Required authorship independence remains separately applicable."],
    [{"assertion_provenance": ["owning obligation", "interpretation", "assumptions", "derivation", "shared dependencies"], "execution_provenance": ["actual checker", "exact subject", "environment", "inputs", "observations", "result"]}],
    ["F2", "F3", "F6"], "Execution identity and agreement cannot replace the independent justification or dependence account of a broader claim.",
    ["Domain contracts choose acceptable derivations and required authorship independence; statistical independence and model validation need their declared models and owners."],
    ["STDO_REFERENCE_FRAME_BASELINE.assurance-subject-acquisition-and-evaluation", "FOUNDATIONS.configuration"],
    [(fid("assertions-and-observations"), "Justify the compared predicates and observations.", "within the declared applicability"),
     (fid("bounded-construction"), "Diagnose discrepancy and route authorised correction.", "comparison exposes a discrepancy"),
     (fid("risk-and-assurance-selection"), "Dependence constrains quantitative or qualitative assurance selection.", "evidence is used for assurance selection")])
bind_blocks(row, [(["obligation", "scope"], [O(0)]), (["obligation", "definition", "latitude"], [O(1), D(0), P(1)]),
    (["obligation", "latitude"], [O(2), P(0)]), (["obligation", "scope"], [O(3), P(1)]),
    (["obligation"], [O(4)])]); NEW.append(row)

row = new_row("risk-and-assurance-selection",
    "The selected assurance and any quantified conclusion meet the governing obligations, consequence/risk policy, dependence model, calibration scope and resource limits.",
    "An admitted actor selects assurance, or claims a posterior violation probability, joint miss probability, detection probability or other quantitative confidence.",
    ["Admitted work authority selects assurance against obligations, material failure consequences, coverage, uncertainty, resources and action/acceptance conditions. More checks strengthen only applicable dependence-qualified evidence; required safety, authority and acceptance conditions remain.",
     "Quantified assurance states the population or uncertainty, prior information, likelihoods, shared causes and calibration limits. Bayes' rule requires a nonzero denominator and defined used conditionals, and supplies no missing priors or likelihoods.",
     "Agreement/disagreement likelihoods in both faulty and non-faulty conditions matter; numerical conclusions retain model/evidence limits, and agreement need not increase confidence when shared causes or new information change the model.",
     "Factor joint misses with the exact conditional chain only on defined conditioning events. Handle zero-probability prefixes without inventing conditional values; replacing conditional factors by marginals requires relevant conditional independence.",
     "One minus the joint miss probability is detection probability under those conditions, not whole-product correctness. Calibrate sampled/injected cases only to their justified operational relationship.",
     "Keep unsupported numerical confidence unresolved. Assurance/risk policy constrains cost selection rather than being waived by a cheaper plan."],
    ["Qualitative evidence remains usable within governing policy and stated limits; no universal probability threshold or per-test numeric estimate is required."],
    [{"V": "Specified violation event", "E": "Specified evidence event", "Gamma": "Declared conditioning assumptions", "posterior": "P(V|E,Gamma)=P(E|V,Gamma)P(V|Gamma)/(P(E|V,Gamma)P(V|Gamma)+P(E|not V,Gamma)P(not V|Gamma))"},
     {"M_i": "Check i misses V under specified conditions", "joint_miss": "P(M_1 and ... and M_n|V,Gamma)=product_i P(M_i|V,Gamma,M_1,...,M_(i-1))"}],
    ["F1", "F2", "F5", "F6"], "Resource-aware evidence selection preserves required assurance; quantitative confidence is only as strong as its explicit probability and dependence model.",
    ["Work authority selects assurance within policy; a declared probability model supplies the additional mathematical premises for probability identities, not F1-F6 alone."],
    ["SPEC_METHOD.proportional-method-and-delivery-stdo-up-014", "STDO_REFERENCE_FRAME_BASELINE.combinatorial-coverage-and-testing-value-index", "FOUNDATIONS.bounded-construction"],
    [(fid("parallel-assurance-and-provenance"), "Preserve shared causes and distinct assertion/execution provenance.", "evidence is combined or compared")])
bind_blocks(row, [(["obligation", "scope"], [O(0)]), (["obligation", "scope"], [O(1)]),
    (["definition"], [D(0)]), (["obligation", "scope"], [O(1), O(2)]),
    (["definition"], [D(1)]), (["definition"], [D(1)]),
    (["obligation", "scope"], [O(3), O(4)]), (["obligation", "latitude"], [O(4), O(5), P(0)])]); NEW.append(row)

row = new_row("change-impact-and-evidence-retention",
    "Reassessment covers the material change, affected dependencies, new obligations and gates, while retained evidence has established applicability to the new subject and basis.",
    "Change, recovery, reuse or closure relies on existing evidence, including newly discovered invalid assumptions and changes to requirements, refinements, execution environments or selection models.",
    ["Distinguish assertion-justification dependencies from evidence-validity dependencies including implementation, libraries, data, instruments, environments and assumptions; requirement-to-test linkage alone is incomplete.",
     "Bind a conservative impact closure and the transitive dependencies material to assertion, execution and reliance. Exclusion requires supported coverage and a reason the change cannot invalidate the claim; an absent edge proves no non-influence.",
     "Unknown impact widens assessment or leaves dependent assurance unresolved. New obligations and uncovered cases create work; mandatory gates apply. Selection alone supplies no execution evidence.",
     "Form the new account from applicable retained records and actual reassessment, including new obligations and mandatory gates.",
     "Retention supports unchanged claim/scope, justified assertion/observation bases, required independence and dependencies unchanged or covered by established preservation. Keep original subjects and an explicit new applicability relation; changed hashes prove neither invalidity nor equivalence.",
     "Reopen affected reliance while preserving historical observations, failures, unresolved coverage and citations until supported repair, reassessment or authorised obligation change disposes them.",
     "Reassess changed requirements and dependent expectations through change authority; changed refinements revisit both links; changed realization revisits affected implementation/integration under applicable obligations. Use semantic dependencies, not file boundaries.",
     "Account completeness differs from fresh execution of every check. Include impact/acquisition/execution/assessment cost, separating estimates from measurements. Required assurance, risk and gates constrain optimisation; cheap selection cannot omit required coverage.",
     "Broader testing can be justified by broad/unknown impact, changed selection models, release rules or missed dependencies. Failures enter diagnosis and authorised response; evidence acquisition may precede justified repair."],
    ["Use any adequate dependency representation; no exhaustive graph database or separate ledger is required.",
     "Recovery preserves valid work and need not rerun every check. Role, conversation, component or resumption boundaries alone do not invalidate evidence.",
     "Full-suite execution remains available and may have gaps; no universal cadence or exemption from mandatory gates follows."],
    [{"Delta": "Material fact/dependency change, including discovery of invalid assumptions.", "I(Delta)": "Conservative changed-fact and affected-dependent coverage.", "D*(t)": "Transitive dependencies material to assertion, execution and evidence reliance.", "S_Delta": "{t: D*(t) intersects I(Delta)}"},
     {"E_new": "retain_applicable(E_old,new_subject,new_basis) union E_reassessed", "E_reassessed": "Actual reassessment, new obligation assessment and applicable mandatory gates."}],
    ["F2", "F3", "F4", "F6"], "A new subject can use justified retained evidence together with actual reassessment, while unknown influence and uncovered obligations cannot be hidden by selection.",
    ["Owners select obligations/gates and provide preservation relations; the tenant chooses an adequate impact representation and strategy within required assurance."],
    ["TRANSFORMATION_LIBRARY.recovery-law", "SPEC_METHOD.universal-intake-triage", "TICKET_METHOD.condition-based-closure-and-reuse", "FOUNDATIONS.workspace-and-context"],
    [(fid("preservation-obligations"), "Establish any preservation relation used to retain changed dependencies.", "retention relies on preserved changed support"),
     (fid("assertions-and-observations"), "Keep assertion and observation justification applicable.", "evidence is retained"),
     (fid("parallel-assurance-and-provenance"), "Preserve actual provenance and required independence.", "evidence is retained or combined"),
     (fid("risk-and-assurance-selection"), "Required assurance/risk constrains selection and cost.", "reassessment strategy is selected"),
     (fid("bounded-construction"), "Diagnose failures and choose an authorised response.", "a failure or discrepancy is exposed")])
bind_blocks(row, [(["obligation", "scope"], [O(0)]), (["definition", "scope"], [D(0)]),
    (["definition"], [D(0)]), (["obligation", "latitude"], [O(1), O(2), P(0)]),
    (["obligation", "definition"], [O(3), D(1)]), (["definition"], [D(1)]),
    (["obligation", "scope"], [O(4), O(5)]), (["obligation", "latitude"], [O(6), P(1)]),
    (["obligation", "latitude"], [O(7), O(8), P(2)])]); NEW.append(row)

# Existing semantic determinations retain their established fields except the
# explicitly authored replacements below. Source blocks are rebound paragraph
# by paragraph, with the new role-to-meaning relation stated at every block.
UPDATES = []


def changed(anchor):
    row = copy.deepcopy(OLD[fid(anchor)])
    row["owner"] = make_owner(OWNER, anchor, SOURCE)
    # These argument table rows are unchanged or explicitly extended here.
    if isinstance(row.get("argument"), dict):
        authored_families = family_for(anchor)
        if authored_families:
            row["argument"]["source_family_arguments"] = authored_families
    return row


def finish(row, plan):
    bind_blocks(row, plan)
    before = OLD[row["id"]]
    # Coordinate-only rebinding of retained argument rows: exact line bytes,
    # never a new interpretation or a guessed nearest source location.
    line_index = {}
    for line_number, line in enumerate(SOURCE.splitlines(keepends=True), 1):
        line_index.setdefault(sha(line), []).append(line_number)
    def relocate_arguments(value):
        if isinstance(value, dict):
            source_row = value.get("source_row")
            if isinstance(source_row, dict) and source_row.get("path") == OWNER:
                positions = line_index.get(source_row["sha256"], [])
                assert len(positions) == 1, source_row
                source_row["line"] = positions[0]
            for child in value.values():
                relocate_arguments(child)
        elif isinstance(value, list):
            for child in value:
                relocate_arguments(child)
    relocate_arguments(row)
    fields = {key: value for key, value in row.items() if key not in {"id", "owner"} and before.get(key) != value}
    UPDATES.append({"id": row["id"], "preimage_body_sha256": sha(old_units[row["owner"]["anchor"]]["body"]),
                    "candidate_body_sha256": row["owner"]["body_sha256"], "semantic_fields": fields})


row = changed("stdo-foundations")
row["predicate"] = "Domain methods apply the shared result, current-state, bounded-work and construction-assurance owners while supplying their own predicates, types, policies and grants."
row["obligations"].append("Use the Transformation Library's contract operations while Foundations owns shared construction assurance; domain specialization supplies no parallel law or actual authority.")
add_dependency(row, fid("construction-assurance"), "Use the single assurance owner for dependent construction/evidence reliance.")
finish(row, [(["argument", "scope"], [O(0)]), (["obligation", "scope", "latitude"], [O(1), P(0)])])

row = changed("identity-state-and-evidence")
row["obligations"].append("Acquire current subject support under Workspace and context, and decide reuse through Change impact and evidence retention; identity or digest alone supplies no applicability or acceptance.")
add_dependency(row, fid("change-impact-and-evidence-retention"), "Evaluate retention applicability on the currently acquired subject.", "evidence is reused")
finish(row, [(["scope", "latitude"], [O(0), P(0)]), (["obligation", "scope"], [O(0), O(1)])])

row = changed("typed-composition-and-conservation")
row["obligations"].append("Use Preservation obligations for step/end-to-end preservation support, Contract application for binding the selected instance's material contract, and Design's bounded-frame conservation for its additional declaration obligations.")
add_dependency(row, fid("preservation-obligations"), "Supply preservation support for steps and end-to-end joins.", "a preservation or composition claim is made")
finish(row, [(["obligation", "scope"], [O(0)]), (["obligation", "latitude", "scope"], [O(1), P(0)])])

row = changed("judgment-and-authority")
row["obligations"].append("Before relying on a reported pass/failure for a broader claim, bind Construction assurance's assertion, observation and evidence-combination relations. A supported judgment supplies no operation/decision mandate.")
add_dependency(row, fid("construction-assurance"), "Justify what the evidence establishes before dependent reliance.", "a reported assertion or evidence combination is relied on")
finish(row, [(["obligation", "scope", "result"], [O(0), P(0)]), (["obligation", "scope"], [O(1)]), (["obligation", "scope"], [O(2)])])

row = changed("orthogonal-descriptions")
row["obligations"][1] = "Each refinement applies Preservation obligations to declared meaning and admitted approximation. Use laws valid on the subject; without additional laws only universally valid steps are licensed. Represent method laws, records and maps in a_c with premises, consequences and choices distinct; calculus, interpretation and carriers retain separate identities."
add_dependency(row, fid("preservation-obligations"), "Preservation and approximation support have one owner.", "a refinement or approximation claim is made")
finish(row, [(["definition", "scope"], [D(0)]), (["definition", "obligation"], [D(1), O(0), O(3)]),
    (["obligation", "definition", "argument"], [O(1), O(2), D(2)]), (["definition", "scope", "latitude"], [D(3), P(0)])])

row = changed("workspace-and-context")
row["obligations"][3] = "Apply Change impact and evidence retention to the acquired current subject, governing basis and material changes. Its applicability relation preserves valid progress/history while reopening affected reliance; a green label is no validity argument. Production and invalidation of support remain recoverable, and private context/resumption alone establishes neither applicability nor invalidation."
row["permissions_exceptions"][2] = "A private-context or resumption boundary alone establishes neither evidence applicability nor invalidation; use the owning retention relation."
add_dependency(row, fid("change-impact-and-evidence-retention"), "Decide retained applicability and reassessment using the single assurance owner.", "reuse, resumption or changed material support is present")
finish(row, [(["definition", "obligation", "scope"], [D(0), O(0)]), (["obligation", "scope"], [O(1)]),
    (["obligation", "scope"], [O(5)]), (["obligation", "latitude"], [O(2), P(0)]),
    (["definition", "latitude"], [D(1), P(1)]), (["obligation", "latitude"], [O(3), P(2)]),
    (["obligation", "latitude"], [O(4), P(3)])])

row = changed("bounded-construction")
row["predicate"] = "Construction selects and carries out supported lawful work toward Z with compatible preservation, justified feedback/diagnosis, resource and assurance tradeoffs, truthful control and evidence-bounded completion."
row["applicability"] = "Purposeful construction from bound current A toward selected outcome constraints Z, including strategy, bug/change diagnosis, decomposition, repeated control, recovery and delivery claims."
row["definition"]["clauses"][0]["A"] = "The current material state bound for construction; its acquired account can be incomplete or stale and includes workspace state, external observations, justified knowledge and unknowns."
row["definition"]["clauses"].extend([
    {"required_conditions": "The governing specification models what must hold.", "observations": "What holds in bound reality.", "predictive_model": "How an intervention may affect reality; accuracy is separate from required-outcome satisfaction."},
    {"feedback": ["observe", "compare with requirements", "diagnose", "select authorised response", "act", "observe again"], "homeostasis": "Correction toward required conditions without guaranteed convergence or adequacy."},
    {"bug": "Category of feature/change work using the same intake and delivery mechanism.", "severity": "Consequence", "priority": "Response order under outcome, dependencies, resources and authority."}])
row["obligations"] = [
    "Bind current A and its fallible acquired account, required Z and permitted transitions. Intent/Product/Specification refine Z under authority; lawful calculi do not choose Z or prove it satisfied. Refine into supported transitions where one adequate activation does not fit.",
    "Distinguish required conditions, observations and causal/predictive models. Prediction accuracy proves no required outcome and prediction error alone proves no failure; a path may need discovery through bounded construction/evaluation.",
    "Finite capacity motivates bounded acquisition, while purpose, identity, compatibility and assurance are additional premises. Decomposition preserves material outer obligations/joins; local success requires coverage and preservation to establish the outer outcome.",
    "Strategy selects admissible construction/assurance within Z and the resource envelope. Account for material resources, feedback, uncertainty, integration and rework, including planning/checking/coordination costs. Measures state units/boundaries/composition; separate estimates, assumptions and observations. Owning criteria decide incomparable tradeoffs and the existing design/work record states rationale.",
    "Feedback diagnoses realization, requirement/design, predictive-model or observation defects, preserves unresolved alternatives and may first acquire evidence. Route supported repair to its owner, retaining counterexamples and unaffected work; changing the model proves neither repair nor the former Z.",
    "Bugs use the same feature/change process. Labels supply no cause, repair class or grant; Spec binds lawful Product re-entry. Bug lists project existing work state; keep severity, priority, semantic result and authorized disposition distinct.",
    "Total control truthfully handles unavailable input, unknown conditions, failed preconditions, partial effects, exhausted capability/authority and revoked authority through the core under the actual grant. Deterministic, probabilistic and human outcomes retain their selected models.",
    "Distinguish preservation, progress, termination and satisfaction. Induction/termination claims need premises/arguments; continuing work needs supported purpose. Discovery/counts/activity do not establish delivery. Completion requires current evidence/acceptance; changed Z, exhaustion and retry establish neither former completion nor impossibility. Repeat a failed relation only after supported causal change; reacquire changed support and uncertain effects before dependent action."]
row["permissions_exceptions"] = [
    "Repair, re-entry, refusal, yield or termination may be available within the grant; total handling guarantees neither a solution nor external termination.",
    "No universal termination proof is required to begin admitted bounded work; uncertainty reduction or testing a bounded hypothesis may justify continuation.",
    "No exhaustive optimisation, scalar cost, numerical quota, preferred strategy, role sequence, independent ledger or orchestration runtime is imposed. Ongoing maintenance may continue under its mandate, while delivery needs a completion condition."]
row["argument"] = argument("bounded-construction", ["F1", "F2", "F3", "F4", "F5", "F6"],
    "Destination, observed reality, interpreted models, compatible joins and finite resources constrain supported strategy and feedback; lawful local activity cannot establish unsupported progress or completion.",
    ["Purpose authority selects Z; admitted work authority chooses strategy and response within assurance/resource policy; domain owners bind models, execution and additional controls."])
for a, binding, when in [
    ("preservation-obligations", "Support applicable step and end-to-end preservation claims.", "local steps are used for an outer claim"),
    ("risk-and-assurance-selection", "Required assurance and risk constrain strategy.", "construction or checking strategy is selected"),
    ("change-impact-and-evidence-retention", "Reopen affected support and retain justified evidence.", "observations or dependencies change")]: add_dependency(row, fid(a), binding, when)
finish(row, [(["definition", "obligation", "scope"], [D(0), O(0)]), (["definition", "obligation"], [D(2), O(1)]),
    (["argument", "obligation"], [O(2)]), (["obligation", "latitude"], [O(3), P(2)]),
    (["definition", "obligation", "latitude"], [D(3), O(4)]), (["definition", "obligation"], [D(4), O(5)]),
    (["obligation", "latitude", "result"], [O(6), P(0)]), (["definition", "obligation", "latitude"], [D(1), O(7), P(1), P(2)])])

row = changed("core-contract-derivations")
row["applicability"] = "Conditional arguments for the shared deciding families in the selected methodology domain."
row["definition"]["meaning"] = "Eighteen source-bound conditional family arguments bind actual consumers, applicable premises/pillars, conditional consequences and additional owner choices; the linked bodies own the decisions."
row["definition"]["source_family_arguments"] = copy.deepcopy(FAMILIES)
row["dependency_relations"] = [{"id": fid("foundational-commitments"), "kind": "adopted_premise", "binding": "F1-F6 supply only the combinations and instance conditions explicitly named in each argument."}]
if isinstance(row.get("argument"), dict): row["argument"]["source_family_arguments"] = copy.deepcopy(FAMILIES)
finish(row, [(["definition", "scope"], [("D", "/definition/meaning")]),
    (["argument", "definition"], [("D", "/definition/source_family_arguments")]),
    (["scope", "latitude"], [("D", "/definition/meaning")])])

PATCH = {"schema_version": "stdo.i5.authored-account-patch/v1", "common_input": COMMON,
         "source_preimage": PREIMAGE, "producer": "I5-WRITE-CORE", "owner_paths": [OWNER],
         "updates": UPDATES, "new_rows": NEW}

# These checks authenticate the authored contribution; they are not a semantic
# proof of the prose, its a_c interpretation or consumer behaviour.
all_ids = set(OLD) | {row["id"] for row in NEW}
assert len(NEW) == 6 and len(UPDATES) == 8
for row in NEW:
    assert row["id"] not in OLD
    assert all(identifier in all_ids for identifier in row["dependencies"] + row["consumers"]), row["id"]
for update in UPDATES:
    anchor = update["id"].split(".", 1)[1]
    assert update["preimage_body_sha256"] == OLD[update["id"]]["owner"]["body_sha256"], update["id"]
    assert update["candidate_body_sha256"] == sha(units[anchor]["body"])
    reconstructed = copy.deepcopy(OLD[update["id"]])
    reconstructed.update(update["semantic_fields"])
    newly_referenced = set(reconstructed.get("dependencies", []) + reconstructed.get("consumers", [])) - set(OLD[update["id"]].get("dependencies", []) + OLD[update["id"]].get("consumers", []))
    assert newly_referenced <= all_ids, (update["id"], newly_referenced - all_ids)
for anchor in ["result-algebra", "result-conjunction"]:
    assert old_units[anchor]["body"] == units[anchor]["body"]
expected_changed = {update["id"].split(".", 1)[1] for update in UPDATES}
actual_changed = {anchor for anchor in old_units if old_units[anchor]["body"] != units[anchor]["body"]}
assert expected_changed == actual_changed, (expected_changed, actual_changed)
assert set(units) - set(old_units) == {row["owner"]["anchor"] for row in NEW}
destination = HERE / "ACCOUNT_PATCH.json"
destination.write_text(json.dumps(PATCH, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"patch": str(destination.relative_to(TENANT)), "sha256": sha(destination.read_bytes()),
                  "source_sha256": PIN, "existing_updates": len(UPDATES), "new_rows": len(NEW),
                  "source_blocks": sum(len(row["source_clauses"]) for row in NEW) + sum(len(u["semantic_fields"]["source_clauses"]) for u in UPDATES),
                  "result_sections_unchanged": True}, indent=2))
