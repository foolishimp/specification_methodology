"""Serialize the bounded Writer-authored RC1 semantic interpretation.

Statements and dependencies below are authored source judgments, not extracted
or inferred by this script. The frozen source-inventory handoff is checked
before serialization; independent fidelity assessment remains required.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json

OUT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[6]
P = "stdo://releases/v2.5.1-rc.1/standards/"
C = "urn:stdo-representation:a-c-text:clause:"
S = "urn:stdo-representation:a-c-text:symbol:"
R = "urn:stdo-representation:a-c-text:residual:"
V = "urn:stdo-representation:vocabulary:"
I = "urn:stdo-representation:frame-index:"
B = "STDO_REFERENCE_FRAME_BASELINE.md"
SPEC = "SPEC_METHOD.md"
DMM = "DESIGN_MODULE_METHOD.md"
TICKET = "TICKET_METHOD.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-sha256", required=True)
    args = parser.parse_args()
    inventory = json.loads((OUT.parent / "source-inventory.json").read_text())
    changes = {}
    for row in inventory["standards"]:
        path = ROOT / "specification_methodology/specification/standards" / row["path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError("Source changed after the reviewed inventory: " + row["path"])
        if row["disposition"] == "changed":
            changes[row["path"]] = {"before_sha256": row["predecessor_sha256"],
                                    "after_sha256": row["sha256"]}
    pre = OUT / "preimages/stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7/axiomatic-program.json"
    program = json.loads(pre.read_text().replace("stdo://releases/v2.5.0-rc.7/", "stdo://releases/v2.5.1-rc.1/"))
    existing = {r["uri"]: r for r in program["clauses"]}
    additions = []
    replacements = {}

    def clause(name, statement, subjects, sources, links=()):
        row = {"uri": C + name, "clause_type": "constraint", "operator": V + "operator:requires",
               "arguments": [{"role": V + "role:subject", "ref": S + s} for s in subjects] +
                            [{"role": V + "role:requirement", "literal": statement}] +
                            [{"role": V + "role:" + role, "ref": C + target} for role, target in links],
               "statement": statement, "source_refs": sorted(P + source for source in sources)}
        additions.append(row)
        return name

    def amend(name, suffix=None, sources=(), links=()):
        row = replacements.setdefault(C + name, copy.deepcopy(existing[C + name]))
        if suffix:
            old = row["statement"]
            row["statement"] = old + " " + suffix
            for arg in row["arguments"]:
                if arg.get("literal") == old:
                    arg["literal"] = row["statement"]
        row["source_refs"] = sorted(set(row["source_refs"]) | {P + s for s in sources})
        row["arguments"].extend({"role": V + "role:" + role, "ref": C + target} for role, target in links)

    validity = clause("enclosing-admission-reuses-valid-established-facts",
        "Each admission owner remains independently responsible for deriving and validating its complete enclosing relation. It may consume established facts whose exact subject, basis, scope, provenance and validity remain applicable, with recoverable production and invalidation. A function, component, role, conversation or status boundary alone requires no repeated derivation. Unsupported assertions of prior success establish nothing. Material mutation, rollback, changed authority or basis, expired validity and actual trust crossings require applicable validation before reliance or effect. Reuse transfers no admission responsibility, omits no participant and supplies no separately required independent judgment. All participants and joins remain bound to one admission-valid basis or declared coherent composite basis through one all-or-none semantic commit; if support can advance, revalidate or use a design-declared concurrency mechanism.",
        ["computed-classification", "closed-frame-result"],
        [SPEC + "#complete-enclosing-relation-admission-stdo-up-021"],
        [("support", "computed-facts-judgments-and-rulings-retain-owners"),
         ("support", "closed-result-reuse-preserves-required-independence")])
    read_scope = clause("worker-read-scope-follows-complete-causal-cone",
        "Within its declared access grant, a Worker inspects the complete causal cone, including material producers, consumers and governing owners even when they lie outside its write territory. Narrow mutation scope cannot justify omitted causal context. A required repair beyond that territory returns to its owner; inspection and understanding confer no cross-boundary effect authority.",
        ["worker", "execution-contract"], [B + "#derived-worker-frame", SPEC + "#bounded-causal-construction"])
    workload = clause("computational-path-operational-assumptions",
        "For material algorithmic work, the computational realization projection binds supported input dimensions, workload, growth and operational assumptions for the selected outcome. Product authority owns any acceptance limits before qualification. Challenge representative supported paths and material growth, observing work directly where elapsed time cannot locate it and without repeating work merely to count it. Separate material startup, framework, external computation, transport and assurance costs. Existing design and proof carriers suffice; no universal quota, complexity requirement or extra accounting system follows. Different domain names establish no distinct computational responsibility, and similarity alone proves no semantic equivalence.",
        ["design", "work-outcome"], [DMM + "#computational-realization-projection-stdo-up-019"],
        [("support", validity)])
    method = clause("method-work-serves-decision-or-assurance-need",
        "Method execution obeys the same proportionality relation as Product construction: repeated source acquisition, context assembly, hashing, activation preparation, status recording, review and evidence generation serve an identified change, decision or assurance need. Repetition alone establishes neither validity nor independence. Reuse current applicable evidence, and qualify material method overhead under the Product-owned computational workload and operational assumptions. No universal resource quota or separate accounting carrier is introduced.",
        ["work-outcome", "computed-classification"], [SPEC + "#proportional-method-and-delivery-stdo-up-014"],
        [("condition", validity), ("support", workload)])
    threat = clause("findings-and-tests-require-supported-operating-model",
        "A finding or acceptance predicate binds a violated obligation, supported input or state, governing operating/threat model and credible causal path. An excluded threat alone authorizes neither a predicate nor retained defensive work; existing tests and hypothetical hostility supply no standing. Exclusion itself requires the governing owner, not a helper's inability to construct a case, and internal location alone establishes no trust. Preserve supported malformed-input, mutable-state, authority, freshness and effect checks. Audit affected predicates when replacing the responsibility; retire unsupported expectations without inventing a replacement guard. Live authority conflicts or a proposed wider model re-enter their actual owner rather than receiving a test-only waiver.",
        ["reference-frame", "design"], [SPEC + "#standing-structural-qualification", B + "#derived-reviewer-frame", TICKET + "#test-case-authority"])
    retention = clause("superseded-retention-bears-its-own-burden",
        "Retire superseded production responsibility unless retention identifies a distinct current supported obligation, owner, purpose, execution scope and material cost. Temporary compatibility or comparison has an expiry or removal trigger; existing tests, an oracle label or nominal demotion cannot justify duplicate production work. A required cold reconstruction route or independent test oracle may serve an enduring distinct obligation without an invented expiry. Identify the surviving owner where an obligation remains; no replacement guard is required where no governing obligation exists. Retirement in a closed affected cone need not await unrelated whole-Product closure. Commonization closes when the selected path consumes the accepted relation and superseded work is retired or justifiably retained; shared names, fewer lines or an unused helper prove no contraction.",
        ["design", "work-outcome"], [SPEC + "#closure-criterion", SPEC + "#live-surface-immutability", DMM + "#11c-recurrence-extraction-rule", DMM + "#transformation-admission-completeness-stdo-up-016"],
        [("condition", threat)])
    checkpoint = clause("bounded-grant-preserves-status-and-checkpoint-continuity",
        "One bounded operation grant may cover its declared construction, status and checkpoint sequence. Record actual role transitions in the existing carrier; a status change alone needs no fresh grant or rehash of an unchanged subject. Resolve changed operation, subject, territory, authority or validity conditions before the affected effect, and preserve Executive mutation restrictions. A preservation checkpoint may retain unfinished or unaccepted work under its exact grant with predecessor, included territory, concurrent-writer disposition and durable evidence location; it supplies no acceptance, promotion or publication. A restart explains why retained repair is insufficient, which obligations and evidence survive and which causal assumptions change. Reconstructability supplies no restart authority.",
        ["execution-contract", "work-outcome"], [SPEC + "#construction-assessment-and-delegation", SPEC + "#checkpoint-continuation-progress-and-churn", SPEC + "#reconstruction-litmus"],
        [("condition", validity), ("support", "executive-mutation-needs-prior-writer-transition")])

    interface = "interface-integration-distinguishes-four-claims"
    contract = clause("interface-contract-exposes-domains-and-owned-facts",
        "At each material interface, bind input domain, producer guarantees, consumer preconditions, permitted effects, refusals and observable exit. A direct successful handoff meets consumer preconditions; candidate output, later admission and semantic assessment remain distinct when that is the declared contract. Refusal of an inadmissible candidate does not alone falsify an adequate candidate interface. Supply material actor obligations and domains in the actual context or through an exact lawfully accessible locator, including material LLM role, instructions, tools and transport/model configuration. Generic governance access cannot replace the Product contract or license hidden-validator inference. Deterministic owners expose their owned facts through reuse or equivalent projections; semantic judgment and reserved owner admission remain separately owned.",
        ["work-outcome", "reference-frame"], [B + "#interface-integration-obligations"],
        [("support", validity), ("support", "computed-facts-judgments-and-rulings-retain-owners")])
    domains = clause("interface-boundaries-preserve-domain-and-temporal-meaning",
        "Across serialization, parsing, normalization and adaptation, preserve domain, units, identity, cardinality, order, empty/null/default meaning and lifecycle validity. A lawful translation binds source/target coordinates, preserved meaning, accepted loss, provenance, owner and refusal. Distinguish proposed, admitted, assessed and completed states, active input from history, and current validity from available bytes. Equal wire shape or output proves neither translation nor equal meaning, provenance or authority.",
        ["identity", "public-serialization", "work-outcome"], [B + "#derived-end-to-end-interface-integration-frame", B + "#interface-integration-obligations"])
    actual = clause("interface-path-binds-actual-subject-and-effect-owners",
        "A realized interface claim acquires both selected participants and their exchanges, the exact runnable artifact/install, supported callable entry-to-outcome path, configuration, relevant current mutable workspace and actual state/effect/observation boundaries. Bind current observations separately from immutable authority, history and prior candidates. Refresh affected evidence after changed support while preserving unaffected valid work; actor change alone invalidates nothing. Matching output via hidden fallback, state injection, repaired response, private entry or undeclared retry cannot prove the ordinary path. A pure function acquires no event lifecycle from this evaluation.",
        ["install", "observed-effect-state", "work-outcome"], [B + "#interface-integration-claim-boundaries", B + "#interface-integration-obligations"],
        [("condition", validity), ("support", domains)])
    diagnostic = clause("interface-causal-diagnostics-retain-frontier-and-uncertainty",
        "Preserve the supported originating causal frontier through wrappers and projections: material seam, bounded field/path, expected domain or basis, observed mismatch and evidence locator where available, together with downstream symptoms, successful work and declared continuation or block. Clock or log order alone identifies no cause. Preserve joint causes, alternative frontiers and indeterminacy instead of inventing a unique cause; honor Product redaction and name required diagnostic gaps. Return the smallest supported owner/re-entry without granting repair or retry.",
        ["observed-effect-state", "reference-frame"], [B + "#counterexample-localization", B + "#interface-integration-obligations"])
    usability = clause("interface-usability-requires-ordinary-context-evidence",
        "User usability requires the ordinary human, LLM or software caller to obtain the selected outcome through its declared context, access and supported surface. Internal success and private-validator-aware fixtures prove no such claim. LLM usability uses clean-room UAT with ordinary context/tools and expected outcomes fixed before response inspection, covering the sunny and material ambiguity/negative cases. Disclose substitutes: replayed/fabricated responses prove only their narrower relation. Preserve failures, unedited responses and actual attempts; no silent retry until green. Live claims require live evidence under existing UAT law, while design-only work acquires no universal live-provider prerequisite. Mechanical, semantic and native-user evidence qualify their own claims.",
        ["work-outcome", "reference-frame"], [B + "#interface-integration-claim-boundaries", B + "#interface-integration-obligations", SPEC + "#assurance-boundary-congruence-and-method-qualification-stdo-up-022"],
        [("condition", contract), ("support", "profile-qualification-separates-mechanical-and-semantic-evidence")])
    clause(interface,
        "For one exact outcome and independently stated oracle, select the applicable interface claims and state why others are unselected: contract sufficiency from declared interfaces and available participant context; boundary congruence from actual participants and exchanges; path realization from the authoritative runnable entry-to-outcome path; and user usability from ordinary caller evidence. Design may establish a bounded contract claim while implementation and user facts remain unresolved or unclaimed. Unknown material support leaves its dependent claim unresolved. Full end-to-end usability requires all four distinct results joined on the same basis or a lawful translation. Transport, parse, admission, semantic satisfaction, completion and user success are not interchangeable. The composite refines existing specialist/testing frames without a new family, role, universal gate, ledger or automatic extra actor. Return exact claim dispositions, evidence, exercised path, substitutions, retained work, causal findings, residuals and invalidators to the declared consumer; no acceptance or next-operation grant follows.",
        ["reference-frame", "work-outcome", "closed-frame-result"], [B + "#derived-end-to-end-interface-integration-frame", B + "#interface-integration-claim-boundaries", B + "#interface-integration-obligations", B + "#interface-integration-qualification"],
        [("condition", "required-frame-conjunction-retains-every-constraint"), ("support", contract),
         ("support", domains), ("support", actual), ("support", diagnostic), ("support", usability)])
    computational = clause("computational-whole-path-evaluation",
        "For material computational composition or recurrence, compose the selected interface claims with existing Operator, Owner, Reuse/Foundation and Proof frames to evaluate one complete producer-to-consumer path. Bind fact establishment, each consumer, applicable basis and invalidators, effect boundaries, retained alternatives and accumulated work, including material method/assurance work. Evaluate equivalent computation across different domain names without inferring semantic equivalence, and preserve distinct supported scope, freshness and effect checks. Return one identifiable complete-path result and its evidence; local successes cannot substitute. Design evidence establishes only design, and actual-work claims require observations on the selected path under its declared workload and operational assumptions. Reuse unchanged valid results and reassess affected support after material path, basis or workload changes. This is bounded composition, not a permanent actor, per-helper review or new accounting ledger.",
        ["reference-frame", "design", "work-outcome"], [B + "#computational-whole-path-evaluation", DMM + "#computational-realization-projection-stdo-up-019", DMM + "#11c-recurrence-extraction-rule"],
        [("condition", interface), ("support", validity), ("support", read_scope),
         ("support", workload), ("support", method), ("support", retention)])

    amend("computed-result-reuse-invalidates-affected-dependencies", links=[("support", validity)])
    amend("selected-design-reconstruction-reuses-current-coverage",
          "Reconstructability requires a correct reconstruction route, not execution at every use; it grants no restart authority and cannot excuse stale success.",
          [SPEC + "#reconstruction-litmus"], [("support", validity)])
    amend("compression-assets-are-read-models",
          "Within their scope, derived instructions preserve applicability, obligations, permissions, exclusions, decision owners and invalidators. A projected prohibition retains its condition and lawful alternative; correct digests cannot justify stricter or weaker meaning. References must resolve within the actor's access or the required meaning must be supplied directly.",
          [SPEC + "#one-constitutional-surface-and-version-boundary-stdo-surface-001"])
    amend("profile-qualification-separates-mechanical-and-semantic-evidence",
          "Changed derived guidance is qualified against source-derived expected permissions, exclusions and invalidators. Native-use claims require an ordinary actor through its declared entry/context; mechanical and operational claims require executable observations, including applicable workload assumptions. Semantic agreement substitutes for neither.",
          [SPEC + "#assurance-boundary-congruence-and-method-qualification-stdo-up-022"], [("support", workload)])
    amend("recorded-judgment-binds-semantic-question-and-reviser",
          "Repricing dispositions each affected obligation as retained, superseded, deferred or withdrawn in that same carrier, with owner and evidence. Preserve surviving work and changed dependencies without a parallel ledger of unaffected history. Present the short consequence delta while retaining the original ruling; a general continue instruction accepts no undisclosed architecture or scope change.")
    amend("sufficient-writer-entry-is-direct", links=[("support", checkpoint), ("support", read_scope)])
    amend("reviewer-result-triage-is-total", sources=[B + "#derived-reviewer-frame"], links=[("support", threat)])
    amend("compressed-spec-preserves-authority-flow", links=[("support", "compression-assets-are-read-models"), ("support", validity), ("support", retention), ("support", method)])
    amend("compressed-design-requires-decision-closure", links=[("support", workload), ("support", retention)])
    amend("compressed-ticket-preserves-carrier-binding", links=[("support", "recorded-judgment-binds-semantic-question-and-reviser"), ("support", threat)])
    amend("aggregate-compression-reenters-source", links=[("support", "compression-assets-are-read-models")])
    amend("bootstrap-resolves-exact-basis", links=[("support", "compression-assets-are-read-models"), ("support", checkpoint), ("support", read_scope)])

    frame = P + B + "#derived-end-to-end-interface-integration-frame"
    indexes = []
    for name, root, scope, refs in [
        ("end-to-end-interface-integration", interface,
         "Evaluate explicitly selected contract sufficiency, boundary congruence, actual path realization and ordinary-user usability for one outcome. Their evidence and applicability remain separate; full end-to-end usability needs all four. The index grants no activation, construction, acceptance, retry or new universal assurance prerequisite.",
         ["#derived-end-to-end-interface-integration-frame", "#interface-integration-claim-boundaries", "#interface-integration-obligations", "#interface-integration-qualification"]),
        ("computational-whole-path-evaluation", computational,
         "Evaluate one material computational composition or recurrence path through existing interface, Operator, Owner, Reuse/Foundation and Proof relations. Expose fact reuse/invalidation, supported distinct checks, justified retention and Product-owned workload/cost observations. Select applicable claims; a design result establishes no runtime work or usability, and this index supplies no new actor, quota or effect grant.",
         ["#derived-end-to-end-interface-integration-frame", "#computational-whole-path-evaluation"])]:
        indexes.append({"uri": I + name, "frame_ref": frame, "scope": scope,
                        "clause_refs": [C + root],
                        "residual_refs": sorted([R + "frame-adoption-not-claimed", R + "task-frame-obligations-require-owned-applicability", R + "interface-and-workload-observations-remain-owner-supplied"]),
                        "source_refs": sorted(P + B + ref for ref in refs)})
    residual = {"uri": R + "interface-and-workload-observations-remain-owner-supplied", "kind": "unresolved",
                "subject_refs": sorted([S + "closed-frame-result", S + "observed-effect-state", S + "reference-frame", S + "work-outcome"]),
                "detail": "No task-specific interface contract, supported operating/threat model, actor context, runnable path, current mutable observation, workload limit, retention obligation or work measurement is supplied by this program. Their actual owners provide them. Unavailable facts remain unknown; design correspondence, view closure and a fixture that knows private rules establish neither live behavior nor ordinary usability. Existing grants and required independent evaluations retain their own boundaries.",
                "re_entry_refs": sorted([P + B + "#interface-integration-obligations", P + B + "#computational-whole-path-evaluation", P + DMM + "#computational-realization-projection-stdo-up-019"]),
                "source_refs": sorted([P + B + "#derived-end-to-end-interface-integration-frame", P + DMM + "#computational-realization-projection-stdo-up-019"])}
    old_residual = copy.deepcopy(next(r for r in program["residuals"] if r["uri"] == R + "successor-construction-and-qualification-not-yet-joined"))
    old_residual["detail"] = "This program binds the exact complete STDO 2.5.1 RC1 source and conserved generic Axiom mechanics. It represents T031 interface integration and the bounded shared validity, complete-path, operational, applicability, fidelity, retention and continuity amendments. Mechanical validation/projections supply neither independent semantic comparison nor native-use qualification. Matched child construction, exact configuration decisions, native observations, release disposition and any later publication/adoption retain separate owning evidence and authority. Product presence is not acceptance."
    assessments = {
        SPEC: "R1 validity/admission and reconstruction; R3 method overhead; R4 supported threat applicability; R5 guidance fidelity; R6 retention burden; R7 grants/checkpoints; R8 retained repair. New owning constraints and four affected existing statements carry these relations.",
        DMM: "Material computational path, operational assumptions and recurrence closure are authored as workload and whole-path clauses consuming the singular SPEC validity/retention owners.",
        B: "Preserve existing frame identities and roles; add the accepted T031 composite and its R2 computational refinement, Worker causal read scope and Reviewer supported-model applicability. Two explicit indexes expose these existing source contracts.",
        TICKET: "Affected repricing obligations and consequence deltas extend existing J/O continuity; supported acceptance predicates use the shared applicability constraint. Existing carriers and authority remain.",
        "authority_compressions/design_module_method.compressed.md": "The existing design compression clause retains its old claim and gains explicit workload/retention supporting dependencies corresponding to the changed digest-bound projection.",
        "authority_compressions/spec_method.compressed.md": "The existing authority-flow clause retains its claim and links scoped fidelity, validity, retention and material method work; exact raw owners retain meaning.",
        "authority_compressions/stdo_bootstrap.md": "Keep original discovery/authority statement; add the material shared fidelity, bounded grant and causal-read support projected by the new bootstrap. No caller adoption is inferred.",
        "authority_compressions/stdo_compressed.md": "Existing aggregate re-entry remains; explicit scoped-fidelity support and new source-owned interface/path relations cover affected meaning, without promoting compression into source authority.",
        "authority_compressions/ticket_method.compressed.md": "Keep carrier-binding statement; link current obligation-continuity and supported-test applicability constraints. No new ledger or admission source."
    }
    if set(assessments) != set(changes):
        raise ValueError("The reviewed nine-member source delta changed")
    delta = {"kind": "stdo-representation.authored-semantic-delta", "schema_version": 1,
             "installed_manifest_sha256": args.manifest_sha256, "source_changes": changes,
             "source_assessments": assessments,
             "replace_clauses": sorted(replacements.values(), key=lambda r: r["uri"]),
             "add_clauses": sorted(additions, key=lambda r: r["uri"]),
             "replace_residuals": [old_residual], "add_residuals": [residual],
             "add_frame_refs": [frame], "add_frame_indexes": sorted(indexes, key=lambda r: r["uri"]),
             "combined_projection_selections": {
                 "combined-worker-reviewer": [I + "t009:complete-update-worker", I + "t009:complete-update-reviewer"],
                 "combined-interface-computational": [I + "end-to-end-interface-integration", I + "computational-whole-path-evaluation"]},
             "claim": "Writer-authored candidate interpretation of the frozen nine-member source delta; independent source-fidelity disposition remains external. No Axiom semantic mechanics are added."}
    path = OUT / "semantic-delta.json"
    path.write_text(json.dumps(delta, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "added_clauses": len(additions), "changed_clauses": len(replacements), "added_indexes": len(indexes)}))


if __name__ == "__main__":
    main()
