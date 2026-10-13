# Independent review: does the introduced explanation conserve owner standing without a rival universal signature or hierarchy?

**Overall result: `falsified`.** Several literal counterexamples below defeat the predicate, which requires every listed relation to hold together. Parts of the candidate are conserved. Members and claims whose source was not supplied are marked `out_of_frame`.

This is a review result only. It is not an `accept`, `local_repair`, `re_enter` or `reject` disposition, which belongs to the decision owner.

## Basis and limits

- **Subject:** commit `804b396878d1cc04c776f136ef82dfdafb544771`, as resolved by the Host Writer. I used only the bytes in your message and called no tools, including the advisor.
- **Hashes:** I cannot reacquire or recompute any SHA-256. Every digest is taken as host-asserted.
- **Excerpts only:** the inserted introductions for SPEC, AXIOMATIC_CALCULUS (`a_c`), REFERENCE_FRAME (RF), ODD, WORLD_MODEL and UX came without full-member digests or placement. Whether the rest of each member is byte-unchanged, and where each introduction sits, is unverified.
- **Partial sources:** the DESIGN_MODULE_METHOD and STDO_REFERENCE_FRAME_BASELINE text was supplied only as excerpts.
- **Source not supplied:** TICKET, RELEASE, IDENTITY, GLOSSARY, WORLD_MODEL, UX, TRAVERSAL and `frames/*`.

## Findings that falsify the predicate

Each finding is labelled with what it breaks: an **owning obligation** (a rule owned by a source member), a **correspondence defect** (a non-deciding mapping that does not hold), or an **unsupported wider claim**.

### F1. README demotes method members below their source standing (owning obligation)
- **Candidate text (README):** "constitutional method surfaces include Spec, Frame, ODD, Identity and World Model … Design, Ticket, Release, Posting and Writing are companion governance/operating surfaces; UX owns its adopted realization process".
- **Source:** ODD §4 says "Only `*_METHOD.md` documents are constitutional method surfaces. `*_GUIDE.md` documents refine application." SPEC's STDO Method Identity names Ticketing (`TICKET_METHOD.md`) and Design (`DESIGN_MODULE_METHOD.md`) as two of the four STDO pillars.
- **Counterexample:** `TICKET_METHOD.md`, `DESIGN_MODULE_METHOD.md`, `RELEASE_METHOD.md` and `UX_METHOD.md` are `*_METHOD.md` members. They are reclassified below "constitutional" and put in the same class as the `*_GUIDE.md` members (Posting, Writing).
- **Residual:** a self-declared standing inside the unsupplied Ticket or Release member is `out_of_frame`.

### F2. README ownership table misattributes owners (owning obligation)
- **"Context … | Reference Frame Method":** SPEC owns `urn:stdo:bounded-context:semantic-resolution`. RF owns only "frame declaration, activation, evaluation, basis, relation, result, coverage, revision, and qualification concepts". → `falsified`
- **"Exact cuts, conservation, publication and adoption | Release Method":** SPEC's product-definition-routing context owns the Installed Release Basis, Adoption Plan, `adopt --dry-run` and mutating `adopt`. SPEC sends only "release criteria, immutable RC publication, selector advancement" and selector alias semantics to RELEASE. → `falsified` against the supplied SPEC; the RELEASE member itself was not supplied.
- **"Constitutional WHAT … | Spec Method" and "Structural HOW | Design Module Method":** SPEC says "the surfaces bound by `what` define `WHAT`" and "design and realization surfaces define `HOW`", and each Product owns those surfaces. The column header "Owning or locating" makes this row `indeterminate` rather than falsified.

### F3. README collapses Product identity into the definition line (owning obligation)
- **Candidate text (README):** "The Methodology Product retains its identity across releases."
- **Source (SPEC):** "The definition identity may remain stable while that source line authors successive Product releases. Every immutable Product or release produced from the line retains its own Product- and Release-Method identity." The `Product` conformance row says the released Product and the Product Definition "remain distinct".
- **Residual:** IDENTITY_METHOD was not supplied.

### F4. "Composition law" is a rival universal composition rule (owning obligation, plus a wider claim)
- **Candidate text (TRANSFORMATION_LIBRARY):** "S after T is admitted only when carried meaning, identity, basis, lifecycle, effects and authority match or have a lawful explicit translation."
- **Counterexample 1:** two participants whose bases are joined by an explicitly owned composite basis are lawful under AC-006 and SPEC rule `STDO-UP-021` ("design-declared coherent composite basis"). A composite basis is neither a match nor a translation, so the library would refuse them.
- **Counterexample 2:** under AC-016, `F_D[w] compose F_P[v]` is lawful when types and preconditions fit. The two traversals keep different authorities, which AC-016 says composition "retains". The library's "authority match or … translation" would refuse this.
- **Standing contradiction:** the same section says "This states a bounded composition obligation", and no owner is cited for the associative-regrouping condition. The member's opening calls itself "non-deciding", and FOUNDATIONS says these accounts "introduce no duties".

### F5. The library's Evaluate family contradicts the owner functions mapped onto it (correspondence defect)
- **Candidate text (Library, Evaluate), unscoped:** "A judgment supplies no repair, acceptance or next-action authority."
- **Counterexample (calculus):** in `a_c`, `J_X = Accept_X(M_X) -> accepted` is an acceptance judgment, and AC-014 makes "Promotion … an explicit relation between the unchanged subject and its admission or acceptance judgment".
- **Counterexample (ODD):** the ODD introduction places `evaluate_next` (whose output includes `selected_action`) and `evaluate_action` (which decides repair and re-enter) under Evaluate. ODD §11.5D gives exactly those functions next-action and closure-decision authority.
- **Mitigation:** owner authority survives through "No name or partial output in this account replaces that table". The correspondence is still incoherent.

### F6. Library family terms have no declared bounded context (owning obligation)
- FOUNDATIONS declares `urn:stdo:bounded-context:foundations`, but its scope is "the whole member's" terms, meaning FOUNDATIONS.md only.
- Bind, Acquire, Transform, Evaluate, Conjoin and Dispose are used across six members. "Evaluate" and "Conjoin" are equal-spelled with RF's `evaluate` and `conjoin`.
- SPEC: "Equal spelling … does not establish equal meaning." Zero applicable concepts is unresolved meaning. The `a_c` introduction disambiguates against AC-013; the RF and ODD introductions rely on nominal correspondence.
- Whether this fails closed depends on whether the occurrences sit at a material boundary. F4's "admitted only when" makes at least one of them material.

### F7. SPEC introduction asserts a premise relation over the chain (unsupported wider claim)
- **Candidate text:** "A selected purpose, interpreted subject, governing specification, sufficient evidence and actual owner grants supply the premises of the constitutional chain below."
- **Conflict:** FOUNDATIONS disclaims any "normative hierarchy, derivation provenance or constitutional specialization relation" and any "replacement derivation basis". SPEC's chain gets its authority directionally from Goals.
- **Secondary ambiguity:** "the general method and conditionally applicable realization profiles". If ODD is meant as one of these "profiles", that conflicts with ODD §2: "constitutional law for graph-native traversal governance".

### F8. "Selected" collapses availability, adoption and activation (owning obligation)
- **Candidate text:**
  - FOUNDATIONS: "Where the construction engagement profile is selected, the Baseline owns …"
  - Library: "A selected Baseline WorkerResult instance"
  - ODD introduction: "Selection of this method activates its declared ODD obligations"
- **Source:**
  - SPEC: "Profile availability, Product adoption, and execution-scoped activation are three distinct relations."
  - Baseline: "Inclusion in an exact released standards cut … makes this profile available; it does not adopt it."
  - `STDO-SURFACE-001`: no "selectable partial constitution".
- **Counterexample:** a Product whose selected cut contains the Baseline but which has adopted no Project Reference-Frame Basis. Read literally, "selected" lets the Baseline govern there.

### F9. Projected instructions lose conditions or lawful alternatives (owning obligation, `STDO-SURFACE-001`)
SPEC: "A projected prohibition cannot lose its condition or lawful alternative" and "cannot require a stricter or weaker relation by compression".

| Candidate text | Owner condition dropped |
|---|---|
| FOUNDATIONS: "Before acting, establish sufficient material context and capability." | SPEC Computed Classification lets a bounded grant take "the cheapest useful discriminator, including obtaining the first candidate", and "Unknown treatment withholds dependent reliance … not unrelated authorized work." |
| Library: "When reconstructability matters, destroy or exclude the incidental process state" | `STDO-UP-020` applies this only to a durable or reconstructable authority claim, and only where losing incidental process state is a material counterexample. A Reconstruction Litmus derivation such as Requirements→Design would trigger the library's broader wording. |
| Library: "Reassess only materially affected premises" | SPEC requires recomputing "the wider frontier where independence is unproved". |
| FOUNDATIONS: "An obligation with no requiring purpose or invariant must be justified or removed by its owner." | `STDO-UP-014` covers method obligations. `a_c` constraints have no purpose dependency ("not dependencies of every calculus definition"). |
| Library: "Combine only compatible, authenticated results" | RF `conjoin` must consume conflicting results and return `conflict`. This is `indeterminate` because "compatible" is undefined. |

### F10. Unresolved transitional reference (low)
- **Candidate text (FOUNDATIONS):** "This candidate's design tests a proposed additional family …"
- The referent is not in the member set, so it resolves to nothing. It is also candidate-process wording in a would-be live member, against SPEC's Specification Surface Rule (present tense, no transitional law).

### F11. ODD introduction widens ODD's dependencies (low, `indeterminate`)
- **Candidate text:** "Its constitutional composition uses … Reference Frame Method, Ticket Method and Release Method."
- ODD §3 states its own composition. ODD §15 keeps release as "a separate process surface".

## Conserved items (`satisfied` on the supplied bytes)
- **Calculus independence:** FOUNDATIONS says the engagement bindings are "not dependencies of every calculus definition". The `a_c` introduction "adds no fields, dependencies or obligations" and keeps AC-013 primary.
- **Symbols:** `U_foundation`, `Sigma_contract`, `C_H` and the others are context-qualified and stated not to define same-spelled symbols elsewhere.
- **ODD function table:** the `synthesize_model`, `eval_gap`, `evaluate_action` and `evaluate_next` outputs match §11.5D, including the `post_reprice` no-action case. The Transform row grants no event or ledger mutation, consistent with A5. The Dispose row keeps the A4a separation, A11 disposition versus selection, and ABG admission of ConstructionIntent.
- **Result algebras:** WorkerResult variants, AC-013 `M_b_prime*/hold/gap/refusal` and the RF-012 base with compatible extensions are shown as instance-owned, "not a common mandatory enum".
- **Construction dispositions:** the conditions for the four `STDO-UP-020` dispositions are restated faithfully. Treating the assessor's disposition as evidence is supported by "Transition evidence is a read model and does not become … admission authority."
- **Other conserved points:**
  - `STDO-UP-013`: salvage stays consumer-owned.
  - `STDO-UP-014`: no universal quota.
  - Baseline: severity is not priority.
  - README: in ODD, the next work decision stays with `evaluate_next`.
  - Compressions are non-deciding.
  - RF-014: capacity misfit is handled by human configuration authority.

## `out_of_frame` or `indeterminate`
- **WORLD_MODEL and UX introductions:** the owner text was not supplied. The only checkable UX claim, that escrow is not closure, matches SPEC's Sprint Execution Boundary.
- **Members not supplied:**
  - `frames/*` content: the risk is RF anti-pattern 2, where a view is called a frame without an evaluation relation, alongside the `Frame` nominal-match case.
  - TRAVERSAL, TICKET and RELEASE classifications.
  - DESIGN_MODULE §8 totality and rules `STDO-UP-016`, `STDO-UP-019` and `STDO-UP-023`.
- **Bounded-context ownership:** whether a non-deciding member may own a bounded context through "STDO Specification Methodology Product authority" is left as residual judgment for the owner.
- **Calculus layering:** whether calling Library correspondences "instances" sets up a type/instance relation the disclaimers deny is left as residual.

## Re-entry pressure
- **README source-standing and owner table (F1–F3):** goes back to the README's owner, measured against SPEC, ODD §4 and IDENTITY.
- **Library and introduction findings (F4–F9):** local wording repairs inside the explanatory members appear sufficient. None of the governing owner contracts appears to need to change.

The decision owner keeps the disposition.
