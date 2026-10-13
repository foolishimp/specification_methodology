# Source-first semantic comparison: Codex v3 at f58750f vs STDO 2.5.1 RC2

**Basis and limits.** I compared only the predecessor and candidate texts you pasted. I read the source before the candidate in each case. I used no tools, did not access peers, and did not use author summaries as evidence. Without a tool I could not do a byte diff, so "no body delta" below means a clause-by-clause read found no difference, not a mechanical guarantee. SPEC_METHOD, REFERENCE_FRAME_METHOD, the Reference Frame Baseline, DESIGN_MODULE_METHOD, ODD, WORLD_MODEL, UX, Identity, the calculus, the traversal profile and the compression/template READMEs were not supplied. Any finding that depends on them is marked as a limit, not decided. Whole-release and toolchain efficacy are outside this claim.

## Results

| Member | Result |
|---|---|
| README.md | **falsified** (narrow) |
| TICKET_METHOD.md | **falsified** (narrow; preamble only) |
| RELEASE_METHOD.md | **satisfied** |
| GLOSSARY_GUIDE.md | **satisfied** (with an anchor-resolution limit) |
| POSTING_GUIDE.md | **satisfied** |
| WRITING_GUIDE.md | **satisfied** as a member; its retained law is breached by the new introductions (F5) |
| FOUNDATIONS.md (new) | **indeterminate** for the "explains owners, overrides no member duty" predicate |
| TRANSFORMATION_LIBRARY.md (new) | **indeterminate** for the same predicate |

## Findings

**F1 — README: lost exact-install determination.**
- **Source:** predecessor README, final paragraph: "resolves logical release URIs without putting machine-local paths in Product Definitions"; local copies "are not the default."
- **Candidate:** "Distribution and entry", paragraph 2. It keeps the shared store, logical URIs, the explicit-bind-and-verify condition, the exact-basis tuple and selector non-replacement. It drops the machine-local-path exclusion.
- **Lost determination:** Product Definitions carry no machine-local paths.
- **Repair:** restore that clause in this paragraph only. The same law may also live in SPEC_METHOD's shared-installed-release-basis section, but I can't check that here, so the README restatement must carry it itself.

**F2 — README: optionality reclassification has no source basis.**
- **Source:** the predecessor README lists ODD_METHOD and WORLD_MODEL_METHOD as "constitutional method surfaces" and STDO_REFERENCE_FRAME_BASELINE as a "derived application profile". It marks only the Traversal Occurrence Profile as optional ("adoption remains optional").
- **Candidate:** the "Method owners" table labels ODD, World Model, UX and the Baseline "Optional". It labels Ticket "Selected durable work-carrier profile".
- **Assessment:** this is an applicability determination, not a discovery reorganization. If the owning members themselves state conditional applicability, the labels are lawful summaries, but those members were not supplied. UX_METHOD does not appear in the predecessor README list at all.
- **Repair:** take each row's standing word from its owning member clause, or remove the word.

**F3 — README: minor discovery losses.** These are below the falsifying threshold on their own.
- "subordinate executable … tooling" is narrowed to "plugin interaction assets".
- Schemas lose "normative", "layout-neutral" and the `schemas/` locator.
- Templates lose "single per-product", the project specification templates and the agent bootstrap templates.
- The link `../frames/WORK_RECOVERY.md` points outside a tree that claims to be "the complete documentary realization". In an installed cut that is a membership and dangling-reference risk.
- **Repair:** restore the qualifiers. Either bring the frames reference inside the member set or mark it as a non-member pointer.

**F4 — TICKET_METHOD: introduced applicability qualifier.**
- **Source:** "Default Layout" says the applicable Product Definition resolves `TICKET_METHOD.md` "from its exact shared installed STDO basis. Their absence from the project tree is not absence from the governing method." The predecessor README lists Ticket among the companion governance and operating surfaces, not as optional.
- **Candidate:** the preamble calls it "This optional work-carrier profile". The retained body still contains the Default Layout clause, so the member now contradicts itself.
- **Risk:** if the member is optional, deselecting it could remove the run-scoped execution-contract duty and the UP-006, UP-007 and UP-009 duties.
- **Body:** no other delta found. All sections from Core Model through Future Extensions are preserved.
- **Repair:** the preamble word "optional" and README row F2. What *is* optional or rebindable is the carriers (layout and the ticket/sprint selection), which the body already says. The preamble's "refines Bind, Transform and Dispose" also leaves out the Evaluate-like UP-007 review and the closure content. That is not binding, but it is a mis-mapping.

**F5 — Introductions breach the retained WRITING_GUIDE and RELEASE_METHOD law.**
- **Source:**
  - WRITING_GUIDE, "Specification Artifact Practice": "state the current live truth, not a narrated transition".
  - WRITING_GUIDE, "Current-Surface Writing": version labels only for immutable release facts.
  - RELEASE_METHOD, "Release-Scoped Assets": version identity "belong[s] in release-scoped carriers".
- **Candidate:**
  - FOUNDATIONS opening ("draft v3 text") and final paragraph ("accepted Codex C1 argument", "The successor member map").
  - RELEASE preamble ("not selection of a v3 release cut").
  - README ("This tenant tree is a candidate", "predecessor routes are provenance").
- **Also:** "accepted Codex C1 argument" asserts acceptance from inside the member it supports. That is unsupported standing, and "successor member map" is an unresolved reference.
- **Repair:** move construction and provenance statements to release-scoped or qualification carriers.

**F6 — FOUNDATIONS / LIBRARY: normative rules without named owners.**
- **Examples:**
  - "Never replace a difficult required relation…"
  - "prohibited retry practice"
  - "an omitted planned judgment is an admission defect"
  - "Discarding retained work requires an owning decision…"
  - "For an UP-020 assessment retain the assessor-disposition field…"
- **Problem:** your criterion is that introductions explain owners. None of these cite an owning member clause. They are probably SPEC_METHOD (UP-013, UP-020, churn) restatements, which I could not check.
- **Repair:** cite the owning clause for each rule, or state that the passage is a non-deciding summary.

**F7 — LIBRARY Dispose vocabulary vs member dispositions.**
- **Library Dispose:** {accept, local_repair, re_enter, reject}.
- **Member dispositions:**
  - Ticket sprint close: {accepted, local_paydown, design_reframe, requirement_reprice, product_reprice, remove}.
  - Ticket repricing: {retained, superseded, deferred, withdrawn}.
  - Release UP-015: {conserved, superseded, intentionally removed, not applicable}.
- **Writer closure:** Ticket's Condition-Based Closure lets an authorized Writer record closure without extra review or appointment. The library frames Dispose as a decision-owner selection.
- **Assessment:** the "not compulsory stages / no authority from the library" disclaimers prevent an outright override, but how the member sets map onto Dispose is undeclared.
- **Repair:** a mapping sentence stating that member disposition sets govern.

**F8 — FOUNDATIONS symbol collision.**
- **Collision:** the unqualified "object O", "Sigma" and "kappa" collide with the indexed `O` pillar symbol (method-identity), Ticket's "reserved choice O", and `Sigma_occurrence`.
- **Rule:** Bounded-context semantic resolution (cited by Ticket and Glossary) requires a material term to resolve to exactly one meaning.
- **Repair:** rename or bind these symbols in FOUNDATIONS. The Glossary needs no change.

**RELEASE / GLOSSARY / POSTING / WRITING.**
- No body delta found.
- The preambles add standing descriptions only and override no duty.
- Release's normative namespace allocation is not caught by "examples are examples".

## Lost determinations and introduced duties

- **Lost:** the machine-local-path exclusion (F1). Possibly the constitutional standing of ODD, World Model and the Baseline (F2, pending their owning members).
- **Introduced:** Ticket's optional standing (F4); the unowned library and foundation rules (F6); construction-state text in live members (F5).

## Residual limits

- No mechanical diff was possible.
- Glossary anchors have not been checked against the successor SPEC_METHOD, ODD and other unsupplied members. Under the Index Contract, a row that does not resolve is invalid.
- F2 and F6 cannot be settled without the unsupplied owning members.
- This report records findings only. It does not accept or dispose of them; that belongs to the decision owner.
