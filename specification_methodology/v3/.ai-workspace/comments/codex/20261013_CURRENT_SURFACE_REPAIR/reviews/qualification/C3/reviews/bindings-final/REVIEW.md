# Reviewer evaluation: subject `427a0deb39b7cd8e298b3b2ebc126c052f056d8a`

## Activation and basis

- **Role:** author-independent, source-first Reviewer. I have no repair, priority or disposition authority. Results go to the decision owner.
- **Subject:** the frozen candidate excerpts quoted in the request, bound to commit `427a0deb…`.
- **Owners:** the immutable owner excerpts at their stated SHA256 values.
- **What was evaluated:** only the quoted owner excerpts and the candidate's introductions and bindings. These were not in the population: Spec constitutional chain, STDO-UP-007, STDO-UP-019, STDO-UP-021 and STDO-UP-022; the ODD Method outside §11.5D; candidate member bodies; and the Ticket and Release Method bodies.
- **Basis residual:** I used no tools, so I did not check the quoted bytes against the subject commit or the stated digests. Every result below is conditional on the quoted text being exact.
- **Conjunction:** no conjunction rule or Product-selected severity scale was supplied. I give no combined result. Severity below is qualitative.

---

## C1. Foundation context: `satisfied`

**Evidence.** FOUNDATIONS declares everything the Spec Method's bounded-context law requires ("exists only when an owning authority declares its stable identity, owner, selected basis, and governed semantic scope"):
- **Identity:** `urn:stdo:bounded-context:foundations`.
- **Owner:** "the STDO Specification Methodology Product authority".
- **Basis:** "this member's definitions at the exact member digest together with the cited source-owned clauses, bound under the activation's governing cut".
- **Scope:** "the whole member's explanatory terms, symbols and explicitly scoped hypotheses, including the account in Orthogonal descriptions".
- **Identity rules:** stable across location; a new digest changes content and may change applicability.
- **Symbol clash:** it explicitly says its symbols do not define same-spelled symbols in the calculus and other contexts (`I`, `A`, and `U` versus ODD's `U`).

Deferring the basis to the activation's cut follows the owner's own precedent ("under the selected complete STDO basis").

**Residuals**
- **R1.1** The owner is named in prose, not as an authority identity. The Identity Method requires authority, kind and value, and STDO-UP-004 requires owner, kind, subject, scope and basis. It cannot be resolved from this population.
- **R1.2** The basis selects only "definitions", but the scope covers "terms, symbols and … hypotheses". Scoped terms that are not definitions have no stated basis content.
- **R1.3** Putting "the cited source-owned clauses" in the basis is not a Semantic Import. The owner requires an import carrier with source and target concepts, direction, what is preserved or lost, owners, bases and lifecycle. Foundations uses owner-specific terms with no such carrier: "Reviewer" (owned by the optional Baseline), "decision owner", RF-014 roles. If a consumer relies on these at a material boundary, the owner's rule makes them unresolved, and the result would become `falsified`.
- **R1.4** "Permitted representation changes" does not say who permits them.

---

## C2. Explanatory direction versus formal derivation: `falsified`

**F2.1 (counterexample).** FOUNDATIONS states that the explanatory direction "abstracts recurring relations from the detailed owners … It creates no normative hierarchy, derivation provenance or constitutional specialization relation." But "Premises and standing" then says:

> "The method's obligations follow from these premises together … Finite capacity alone does not prove all those obligations."

This claims that the method's obligations are entailed by the Foundations premises. That runs opposite to the declared direction (owners → abstraction) and treats the passage as a proof ("does not prove all").

- **Conflict with the calculus:** the calculus owner fixes its derivation provenance as specific Spec, Frame and Identity clause families, recorded in `AxiomaticCalculusBasis.derivation_basis.principle_refs`, and says "the derivation direction is one-way." "The method's obligations" includes the calculus's, so Foundations asserts a derivation source missing from that one-way record.
- **Conflict with Foundations' own rule:** a universal claim must state a "defined domain, adequacy relation and argument"; otherwise it "remain[s] hypotheses". The entailment claim states none of these and is not labelled a hypothesis.

**Triage for F2.1**
- **Affected claim:** that Foundations has explanatory, non-deriving standing.
- **Severity:** moderate. Read literally, it gives Foundations derivation standing over every owner.
- **Cause and confidence:** a modal ("follow from … prove") inside a section that otherwise only explains; medium-high confidence.
- **Blast radius:** every member whose introduction cites Foundations.
- **Workaround:** none in the text. The disclaimer sentence contradicts the claim rather than limiting it.
- **Repair complexity:** low, one sentence. Regression risk: low.

**Residuals**
- **R2.1** Traversal says it "refines Foundations", World Model says its terms "refine the shared foundation", and Spec says "Bind is refined here". None declares what kind of relation this is. The Frame Method says relations "apply only where explicitly declared". The Spec Method says calling something a specialization without the coordinates "establishes nothing". So two readings stay open: refinement as the converse of the abstraction, or downward refinement.
- **R2.2** Orthogonal descriptions contains orders with no owner: "Keep three accounts distinct", "must be supplied before using them as proof". These are new normative content, not abstractions of an owner. The scope covers "hypotheses", not orders.

---

## C3. Existing configuration grants: `satisfied`

**Evidence**
- Foundations: "The existing human or delegated configuration authority selects refinement, another actor, sequencing or lawful compression under RF-014 … capacity supplies no configuration grant." The actor "acts on an already authorized response, requests the owning decision, or stops".
- RF-014 says "human authority may select…" and "may not silently omit material relations". STDO-UP-004 allows human authority "through an explicitly admitted bounded proxy".
- The library's Bind says "A name, path, cached result or available tool is no grant". README says plugins "mint no authority". ODD says "availability supplies no … grant". These match RF-006 and STDO-UP-020 direct entry ("not self-acceptance at a boundary owned elsewhere").

**Residuals**
- **R3.1** "Delegated configuration authority" does not require the STDO-UP-004 proxy-grant details (grantor, subject, scope, permitted and excluded decisions, validity, revocation). "Existing" limits it but does not supply them.
- **R3.2** The Baseline's candidate Canonical Compression says adoption is "admitted by the existing project authority … A local axioms file may carry the decision". The owner's status boundary requires "a separately accepted Product-owned Project Reference-Frame Basis". The compression is weaker than that duty and does not restate it. If "project authority" is read as broader than the Product, this becomes a counterexample.
- **R3.3** The Baseline sends coordinated activation misfit as `activation_refusal` directly to Executive, with "no Worker evaluation". Foundations says "reports the misfit" / "stops with an explicit unresolved result" and names no consumer. It could be misread as a WorkerResult `incomplete`.

---

## C4. Parameterized Transform / Evaluate / Dispose: `satisfied`

**Evidence**
- **Transform:** "Return the instance-owned outcome". It names the Baseline WorkerResult variants and AC-013 `M_b_prime*/hold/gap/refusal` exactly as the owners state them, and says these are "not a common mandatory enum".
- **Evaluate:**
  - The reference-frame results match RF-012.
  - It states: "Other judgment domains retain their admitted result algebras."
  - Independence applies only "where required".
  - The STDO-UP-020 assessor disposition is kept as a field next to the predicate result. This matches "Assessment returns one of these semantic dispositions" and the Baseline rule that the Reviewer returns to Executive and Executive disposes.
- **Dispose:**
  - For STDO-UP-020 it uses `accept/local_repair/re_enter/reject`, and its four conditions restate the owner's table.
  - "Accept binds an exact checkpoint; it does not imply release." Writer recording matches STDO-UP-020 ("condition-based result recording").
  - Ticket, Release, UX six-class and ODD yield keep their own owners and result domains.
- **Conjoin:** missing slots are "not … falsification", which matches the Frame Method ("remain unresolved … aggregate green status cannot replace them").

**Residuals**
- **R4.1** STDO-UP-020 calls the assessor's output a "semantic disposition". The library calls it an "evidence classification". The values and conditions are kept, but the standing label changed. No owner clause says the authority owner may act against an assessor's `reject`, and the candidate does not say either way.
- **R4.2** Two orders have no owner in the evaluated population: "Preserve the original producer, material inputs and observed effects" and "Observe uncertain external effects before repeating them" (see A5.1).
- **R4.3** Dispose names only "yield" as a domain-specific ODD value. ODD's `repair` and `re-enter` look like STDO-UP-020's `local_repair` and `re_enter`. "Other instances retain their own result domains" covers this, but a disambiguation is not stated.

---

## C5. Source-owned restart and consumer discard: `satisfied`

**Evidence**
- **Restart:** "A proposed construction restart identifies why repair is insufficient, what survives and which causal assumptions change under UP-020. This is distinct from process resumption." This matches STDO-UP-020.
- **Discard:** "Deletion, archival, quarantine and salvage mechanics remain consumer-owned under UP-013; this summary imposes no additional discard law." This matches STDO-UP-013.
- **Churn:** "Rejected or superseded construction is churn" matches. Restricting the retry prohibition to "unchanged failed relation" matches STDO-UP-020.
- **Recovery source:** "Reconstruct … from their declared owners, not private memory" matches STDO-UP-020 intake ("without … prior-worker memory").

**Residuals**
- **R5.1** "What survives" shortens the owner's "which obligations and evidence survive". The owner's "reconstructability alone does not select reconstruction" is left out of the library. Foundations' "does not select" wording covers only resumption.
- **R5.2** The STDO-UP-013 salvage limit (re-adopted semantics only; no inherited authority, dependencies or completion claim) is not projected. The library says it imposes no extra law, so this is a gap, not a contradiction.

**Adjacent observation A5.1 (`indeterminate` pressure; triage `not_applicable` to this claim).** Foundations says "An uncertain effect must be observed, reconciled or returned unresolved before any repetition…" and places it "under agentic construction law". The STDO-UP-020 excerpt has no such duty. This is either an unowned duty attributed to STDO-UP-020 or a duty owned somewhere outside the population. Return to the owner of STDO-UP-020 or of the effect relation.

---

## C6. Conditional material cost: `satisfied`

**Evidence**
- The library says cost measures are chosen "material to that claim … illustrative … not an all-fields obligation, universal quota or separate accounting carrier". The owner says "No universal resource quota or separate accounting carrier follows".
- "Raw counts alone cannot establish it" matches "not raw line count, artifact count, or context-window size".
- Foundations' "No universal numeric budget, resource ledger or measurement gate" stays within "universal".

**Residual R6.1.** The owner's condition is "Where this work materially affects the supported outcome, qualify its operational assumptions under … STDO-UP-019". The library's condition is narrower ("for a computational or handoff cost claim") and never names STDO-UP-019. A consumer using only the library would miss the qualification route the owner requires. This is a gap rather than a contradiction, because the library excludes nothing. STDO-UP-019 itself was not in the population.

---

## C7. Deciding authority and source standing: `falsified`

**F7.1 (counterexample).**
- Foundations "Interpretation and representation" says, about interpretation in general: "The calculus fidelity law (AC-017) owns the interpretation obligation."
- "Judgment and authority" says AC-014 (with RF-006) "own these distinctions" — the distinctions between definitions, observations, judgments and accepted claims, and "A Reviewer judges; a decision owner accepts…".

The calculus owner limits itself: it makes "no claim of universal applicability"; its laws are the normative authority "for the meaning of `a_c`" in `urn:stdo:bounded-context:axiomatic-calculus`; outside uses are "external to the calculus"; and it is not "an authority registry". AC-017 and AC-014 govern only `a_c` interpretations and judgments. Citing them as owners of general obligations widens their reach, which RF-006 and AC-005 forbid (copying or interpreting a record "does not transfer authority"). It is also a cross-context use with no declared relation.

AC-014 does not own "Reviewer" or "decision owner" at all. Those come from the Baseline and STDO-UP-020/007. In ODD scope the next action is chosen by `evaluate_next`, not by a "decision owner".

**Triage for F7.1**
- **Severity:** moderate.
- **Cause and confidence:** wrong owner citation; medium-high confidence. Reading it as scoped to `a_c` remains possible, but the text gives no scope.
- **Blast radius:** every reader who uses Foundations to find owners.
- **Repair complexity:** low. Regression risk: low.

**F7.2 (counterexample).** README opens: "These standards are the deciding documentary surfaces." Its own table includes GLOSSARY_GUIDE, which the Spec Method owner calls "a non-deciding locator index … defines neither". README's later line ("the Glossary is a non-deciding locator") agrees with the owner, but the blanket sentence still literally contradicts it.

**Triage for F7.2**
- **Severity:** low.
- **Workaround:** the specific clause in the same README.
- **Repair complexity:** trivial.

**F7.3 (finding, ambiguous standing).** The ODD, UX and World Model bindings each call themselves a "constitutional method surface" or authority, then call themselves "the profile" in the same binding. The only declared "profile" in the population is the Baseline: "an optional derived … profile … no independent ownership". The UX owner §1A makes UX "the sole UX realization authority". No definition separates the two meanings of "profile", so there are two readings of standing, and the Spec Method says to fail closed.
- **Severity:** low-moderate. Confidence: medium.

**Residuals**
- **R7.1** README's standing classes ("constitutional method surfaces include Spec, Frame, ODD, Identity and World Model"; "Design, Ticket, Release … companion governance/operating surfaces") are presented as "retained", but no owner in the population declares that classification for Frame, Identity or Design.
- **R7.2** RELEASE's "owns release contracts for … and Evaluate, Conjoin and Dispose from the transformation library" can be read as Release owning the shared families.
- **R7.3** IDENTITY's candidate lists "elevation, transfer, supersession or retirement". STDO-UP-004 also requires explicit decisions for split, merge, proxy grant and revocation. Its "where their owning contract requires them" phrasing understates STDO-UP-004's unconditional requirement that an authority identity preserve its governing basis.

---

## C8. ODD `synthesize_model` / `eval_gap` / `evaluate_action` / `evaluate_next` / admission paths: `falsified`

The cone label in this activation says `evaluate_gap`. The owner's function identity is `eval_gap`, and the owner requires every design or proof to name exactly `synthesize_model`, `eval_gap`, `evaluate_next` or `evaluate_action`. I evaluated against the owner.

**F8.1 (counterexample).** The candidate ODD Evaluate row does not match the owner's function table:

| Candidate wording | Owner (§11.5D) | Problem |
|---|---|---|
| `evaluate_gap` | `eval_gap` | No declared identity or relation for this name; unresolved meaning under the Spec Method |
| `synthesize_model produces CurrentModelProjection` | output is `ProductAssetModel`, "Product-owned model truth … not runtime fact" | Undeclared carrier; "Projection" moves it toward the RuntimeProjection / ABG projection-truth standing |
| `evaluate_gap supplies GapProjection` | `ObservationSnapshot + GapPressureRow` | Undeclared carrier; collides in name with the A12 gaps view and A16 non-authoritative read models |
| `evaluate_action … returns EdgeClosureDecision` | `EdgeFulfillmentLedger + EdgeClosureDecision` | Drops the ledger fold that A6/A7 require |
| `evaluate_next selects NextActionProjection` | `PriorityProjection + NextActionProjection + selected_action`; typed no-action for unresolved `post_reprice` | Partial output; in the owner, the projection selects the action, not the reverse |

A0 requires one surface, A4a forbids rival names for authority, and A16 says method wording cannot weaken the loop. Undeclared carrier names in the method's own binding table fail closed under the Spec Method.

**Triage for F8.1**
- **Severity:** high within ODD scope. A16 makes these axioms the controlling acceptance constraints, and the binding is the members' entry map.
- **Confidence:** high.
- **Blast radius:** every ODD design, ticket or proof that names functions or carriers from the binding.
- **Workaround:** §11.5D text, which the binding says still governs. But the binding itself uses the names that conflict with it.
- **Repair complexity:** low. Regression risk: low.

**F8.2 (finding).** The Dispose row says "Closure truth remains under F_D/ABG/product admission: evaluate_action returns EdgeClosureDecision; evaluate_next selects …". The colon puts `evaluate_next` under closure truth. The owner separates them: `evaluate_next` "does not … evaluate the result of an action" (A4a, A7).
- **Severity:** low-moderate. Confidence: medium.

**Admission paths.** The candidate's "produces required evidence for owning native admission", "Admission of a ConstructionIntent is its separate owning step" and "grants no runtime-event or ledger mutation" are consistent with the owner's `admit_construction_intent`, `admit_evidence(invoke(I))` and A5. The step's owner (ABG admission and traversal authority) is not named.

**Residuals**
- **R8.1** `TargetObligationBinding`, the requirement that `U` stay reachable through the binding and the ConstructionIntent (A13a and the constitutional equation), `NextActionBasis` and the `post_reprice` typed no-action are not projected. They are left to §11.5D, so this is a gap, not a contradiction.
- **R8.2** "Zoom-stable closure" (Conjoin row) is not declared in the population.
- **R8.3** Foundations' unscoped "Logs supply observability and audit, and may support reconstruction" understates ODD's RuntimeEventLog as "ABG runtime truth" and the ledger as governed attention (A1a/A1b). "Not a generic law" scopes only the reload sentence.

---

## Summary of results

| Cone | Result |
|---|---|
| C1 Foundation context | `satisfied` |
| C2 Explanatory vs. derivation | `falsified` (F2.1) |
| C3 Configuration grants | `satisfied` |
| C4 Parameterized T/E/D | `satisfied` |
| C5 Restart / discard | `satisfied` (plus adjacent A5.1, `indeterminate` pressure) |
| C6 Conditional material cost | `satisfied` |
| C7 Authority / source standing | `falsified` (F7.1, F7.2; finding F7.3) |
| C8 ODD function and admission paths | `falsified` (F8.1; finding F8.2) |

**Invalidation conditions**
- A mismatch between the quoted text and the bytes at `427a0deb…` or the stated owner digests.
- Owner text outside the evaluated population that declares the missing relations: STDO-UP-019, the effect-repetition duty, a definition of "profile", or a declared `evaluate_gap`/`eval_gap` relation.
- Any change to the candidate.

These results go back to the decision owner. Re-entry pressure: Foundations and README to the Methodology Product authority; the ODD binding to the ODD Method owner.
