# Integration review: candidate `9982ab80` against own preimage `875a56e3`

## Coverage

I read COMMON, then the provided CORE sections (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations), then the four hunks. I saw only the changed lines and about 15 lines of context around each.

I did not see:

- `SPEC_METHOD.md#bounded-context-semantic-resolution`;
- the successor `RELEASE_METHOD.md` UP-015 text;
- the F1–F6 statements;
- the frame catalogue and route bodies or their digests;
- `PREDECESSOR_CLAIMS` rows;
- the heading of the `stdo-work` section that was changed;
- whether any cited anchor resolves.

Findings that depend on omitted bodies are marked conditional.

## Findings

### 1. `GLOSSARY_GUIDE.md` › Acquisition use: the route-result map overlaps (established)

The map assigns "partial acquisition" to `indeterminate`. That clause is about how much was acquired. The other clauses are about the outcome. The same case can therefore match two values. CORE requires a total, reason-sensitive map, and COMMON item 2 says each refined value maps to exactly one core value.

**Counterexample A.** Under bounded acquisition (CORE Workspace and context), an actor acquires only `SPEC_METHOD.md` from the frozen cut. The row's anchor `#stdo-method-identity` resolves there.
- "Resolution in the selected complete basis" gives `satisfied`.
- "Partial acquisition" gives `indeterminate`.
- If the indeterminate clause takes precedence, no bounded acquisition can ever reach `satisfied`. Full-corpus loading would become the price of a green route, which contradicts the CORE exclusion of irrelevant material.

**Counterexample B.** The target file is acquired whole from the cut and the anchor is absent from it.
- "Established invalid" gives `falsified`.
- "Partial acquisition" gives `indeterminate`.

**Smallest repair:** change "partial acquisition or unresolved ambiguity is indeterminate" to "partial acquisition that neither resolves nor establishes invalidity, or unresolved ambiguity, is indeterminate".

### 2. `GLOSSARY_GUIDE.md` › Acquisition use: "unresolved ambiguity is indeterminate" (conditional on SPEC_METHOD)

The new sentence makes the actor apply bounded-context semantic resolution first. It then fixes any ambiguity that remains at `indeterminate`. Two different outcomes fall under that wording:

- **Not yet decided.** Semantic resolution has not decided the occurrence. `indeterminate` is correct here.
- **Concluded.** Semantic resolution has finished and established that no unique owner applies. That is admissible evidence against "the occurrence's route resolves", so CORE's definitions make it `falsified`. If SPEC_METHOD gives a basis or scope reason instead, it would be `invalid_basis` or `out_of_frame`.

Reporting the concluded case as `indeterminate` changes the joins that consume it. Under conjunction precedence (falsified, then invalid_basis, then out_of_frame, then indeterminate), a hidden falsification can let `invalid_basis` or `out_of_frame` become the aggregate verdict. It also takes the domain meaning away from SPEC_METHOD, its owner (CORE: "Domain meaning stays with its domain owner").

**Smallest repair:** change "unresolved ambiguity" to "ambiguity that bounded-context semantic resolution leaves undecided", and add: "an ambiguity outcome it concludes maps by its reason under the core rule."

### 3. `WRITING_GUIDE.md` › Current-Surface Writing: deletion license left unqualified (established, from visible context)

The change correctly limits the question-list "rewrite or delete" to the owning authority and the recorded UP-015 disposition. Fifteen lines later, Current-Surface Writing still independently permits "delete it / supersede it / move it to commentary" for anything the writer judges "no longer live", with no such limit.

**Counterexample.** A writer judges a conserved predecessor determination stale and moves it to a post. That causes two problems:

- The claim stops being stated in the successor's own text, which breaks the Standalone Successor Requirement. POSTING_GUIDE says posts are not constitutional truth.
- No product-owner decision or accepted successor relation has been recorded, which is what UP-015 requires for `intentionally removed` or `superseded`.

Two loci now decide the same question ("may this text leave the active surface?") under different conditions. That violates Single Ownership item 7.

**Smallest repair:** change "If something is no longer live:" to "If something is no longer live, within the owning authority and any recorded UP-015 disposition:". Alternatively, make it refer to the new sentence.

### 4. `stdo-work/SKILL.md` › acquisition paragraph (heading outside context): partial copy of the core record (low)

"Carry the complete core result record, including …" lists the record's fields but differs from its owner in two ways:

- It omits the **verdict**. The preimage carried it as "core result".
- It writes "unresolved coverage" where CORE says "unresolved obligations". That narrows the field: a stop's outstanding obligations are not coverage facts.

"Complete" arguably still governs. Even so, a copy that differs from its owner is a conformance defect under Single Ownership item 4.

**Smallest repair:** add "verdict" to the list and replace "unresolved coverage" with "unresolved obligations". Alternatively, delete the list and keep "Carry the complete core result record."

## Checked, no defect found

- **SKILL, "bound subject and basis … selected snapshot".** This matches COMMON Bounded Transitions item 5 and CORE acquisition. The recovery case that needs *current* effect state is still routed through the unchanged work/recovery route, which projects current-state clauses.
- **GLOSSARY, "packaging choice" changed to "this guide's glossary convention".** This corrects the tier: guides own glossary conventions, and packaging owns no determination.
- **GLOSSARY, removal of "A stale or ambiguous route leaves the term unresolved".** A stale route is now covered by resolution in the selected basis (falsified when established invalid). Term-level non-acceptance is kept by "None reports semantic acceptance". This is own-candidate text, not a predecessor claim.
- **POSTING_GUIDE, Boundary.** "Concise sufficient reference" matches CORE's condition that a reference preserve meaning and availability. "Commentary cannot supply an absent decision" is kept.
- **WRITING_GUIDE, added sentence.** It is consistent with UP-015 and the Standalone Successor Requirement. Whether the successor `RELEASE_METHOD` anchor restates UP-015 is not verified.

## Result of this check

| Coordinate | Value |
|---|---|
| Predicate | The four changed joins conform to COMMON and the CORE result and workspace contracts, on the provided hunks |
| Verdict | `falsified`, by findings 1 and 3. Finding 2 is `indeterminate` until SPEC_METHOD's resolution outcomes are acquired. |
| Performance | `performed`, with partial extent (hunks plus context only) |
| Effects | `not_requested` |
| Standing | This is not member acceptance, and not an evaluation of the source-port review policy |
