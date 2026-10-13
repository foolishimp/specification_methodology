# Assessment: core interpretation fidelity of `core-and-material-families`

**Basis.** I used only the supplied text: SOURCE.md frames, the seven FOUNDATIONS sections, SIGNATURE.md, and the program value. I could not check digests, the frozen commit, SOURCE_INVENTORY.json, or the rc.2 calculus semantics.

**Overall result.** Most of the core clauses follow their source closely. The claim "the program faithfully interprets the selected core" is still **falsified** at the clauses listed under A. Section B lists rules the source states that are missing from the program, and none of those gaps is declared as a residual. Every family-relationship claim is **indeterminate** on the supplied evidence (section D).

This review is one assessment. It does not provide acceptance, release qualification, or independent-review standing under any grant.

---

## A. Demonstrated divergences (clause narrows, alters or relocates source law)

**A1. `total-control`: the guard narrows a totality law.**
- Source (Bounded construction): a total control contract "supplies a response for **every admitted control state**, including unavailable input, unknown world conditions, failed preconditions, partial effects, exhausted capability and revoked or exhausted authority."
- Clause guard: "an admitted control state includes unknown world conditions or partial work."
- Counterexample: an activation whose grant is revoked mid-task, with no unknown world condition and no partial work. The source requires a defined response. The clause's guard never fires, so it imposes nothing.

**A2. `refinement`: drops totality, the explicit missing-reason case, and the no-upgrade law.**
- Source: the refined value includes "an explicit missing-reason case". The map is "**total**, reason-sensitive". A missing reason "maps the claimed predicate to indeterminate… retain its raw outcome and unresolved authentication". Also: "**No refinement turns failure, undecidability, non-performance or unknown effect completion into greater standing**", "Unconfirmed evaluation performance stays unconfirmed", and "Domain meaning stays with its domain owner."
- The clause says only that a missing reason "is not deciding support". It names no indeterminate mapping, no raw-outcome retention, no totality, and no monotonicity.
- Counterexample: a domain maps `refused` (reason missing, performance `unconfirmed`) to performance `not_performed`, verdict `indeterminate`. That satisfies every stated part of the clause, yet the source forbids it: unconfirmed must stay unconfirmed. The clause restricts only effect upgrades, not performance or verdict upgrades.

**A3. `nonperformance` / `performance-compatibility`: performance becomes a fact rather than an evidenced claim.**
- Source: `performed` means "**Evidence establishes** that the evaluation was undertaken". `unconfirmed` means "Whether the evaluation was undertaken is not established."
- Clauses: "actual undertaking is performed…" and "actual undertaken evaluation permits all five verdicts".
- Counterexample: an evaluation ran, but its activation record was lost. The source gives `unconfirmed`, which bars `satisfied`. Read literally, the clause gives `performed`, which permits `satisfied`. `consumer-release` inherits the same wording ("require actual evaluation").

**A4. Reconfiguration preservation and optimality appear only under the Executive guard.**
- Source (Configuration) states these generally: "Every allocation and reconfiguration, fixed or adaptive, preserves material dependencies, outstanding obligations, observed and uncertain effects, admitted authority and required independence." The optimality-evidence rule is also general.
- In the program they appear only in `coordinator`'s qualification, whose guard is "a task-based Executive arrangement is selected". `allocation` does not carry them.
- Counterexample: an adaptive peer reallocation that drops an outstanding obligation violates no clause.

**A5. `coordinator` turns profile procedure into core method law, citing the wrong owner.**
- Its statement, "maintain longer-term outcome… request additional bounded evaluation before unsupported decisions", and its qualification ("work outside current attention stays in workspace") do not appear in FOUNDATIONS#configuration.
- That section says the Executive arrangement's "procedure and grants belong to that profile" (STDO_REFERENCE_FRAME_BASELINE), which `coordinator` does not cite. The clause still has standing "method law".
- Result: unresolved from the cited source, and the standing is overstated.

**A6. `decision-stop`: drops the stop verdict rule, the stop reason, and the decision authority.**
- Source: a stop retains "its **reason**". Its verdict is "indeterminate… falsified… or the established scope/basis diagnosis". `satisfied` is not among them. The decision predicate includes "**by its bound authority**".
- The clause keeps the predicate, effects and obligations. It omits the reason and the verdict mapping, so a stop could report `satisfied` without completion. Its statement also drops the bound-authority element of the decision predicate. It takes `premise-authority` as a premise but does not state the binding.

**A7. `allocation`: omits the grant ceiling and the separation of dependency kinds.**
- Source: a configuration "assigns effects **only within grants the allocator holds and may delegate**", its record explains "resource limits and failure assumptions", and "Functional decomposition, communication, authority and evaluation dependency are distinct."
- The clause says "permitted effects", which does not tie them to the allocator's own delegable grants. The other two points are absent.

---

## B. Source rules with no carrying clause (omissions not declared as residuals)

| Source rule | Where it should land | Note |
|---|---|---|
| "The aggregate evaluation has performance `performed` when its combining rule is applied; this does not change component performance" | `conjunction-*`, `logical-operator` | No clause gives aggregate performance. This is a retained-coordinate gap. |
| "Absence from a partial projection, sparse checkout or empty local record is not evidence of absence… acquire… or retain indeterminacy"; "A rule packet without its current subject is insufficient"; "A summary without supported freshness cannot override its owner" | `acquisition` | Sparse absence appears only in `consumer-identity`. Core acquisition omits all three rules. |
| "An empty local log or discarded context does not establish no effect" | `effect-observation` | Absent. |
| Effect boundary includes "**any observed departure**" from the supported operating model | `effect-observation` | The clause covers only "possibly affected" parts. Counterexample: the model says a job writes only table A, but an observation shows it wrote table B. The source requires B in the boundary. |
| `reverted` requires "**every** begun part… reversed" | `effect-observation` | Clause: "known rollback is reverted only within its evidenced boundary". This is weaker: one reverted part plus one completed part could be read as `reverted` when the source gives `partial`. |
| Normalize parts "including one owned by an absent evaluation slot"; "The combining operation's own lack of mutation cannot label an effectful composite not_requested" | `effect-join` | Both absent. The join summary is also non-exhaustive: it omits all-`not_requested` → `not_requested`, any `partial` input → `partial`, and the "every remaining fully observed mixture gives partial" catch-all. It relies on the source to be total. |
| "A new result over a different predicate does not overwrite the earlier result" | `result-binding` / `refinement` | Absent. |
| A precondition is evidence for its dependent evaluation unless the plan requires it separately; "a different admission predicate is not silently substituted for P" | core results | Appears only in `consumer-reference-frame`, not in core. |
| Context loss "creates no **authority** or idempotence guarantee" (SOURCE.md Recovery) | `context-reset` | `context-reset` does not take `premise-authority`. `safe-reentry` covers idempotence for partial progress, not context loss. |
| Sequential composition routes to UP-016/017 (DESIGN_MODULE_METHOD#transformation-admission-completeness-stdo-up-016); "retained component sets combine by union"; an unestablished outer interpretation returns unresolved or invalid_basis | `composition-order` | `consumer-design` cites other Design anchors. The UP-016 route is not carried. |
| "Changing Z follows its owner"; Intent, Product and Specification refine Z under their owning authority | `progress-stop` | Only "changed destination is not old completion" is carried. |

**Lower-severity weakening:**
- `workspace-truth` drops "**admissible**" contrary evidence.
- `safe-reentry`'s guard "could duplicate" is narrower than the source's "repeating an operation with uncertain effects".
- `result-binding` drops "citations" and the reference "availability" condition. Its qualifier "material" weakens the source's unconditional "Every result projection preserves these coordinates and the original predicate".
- `freshness` omits "An observation binds its source and observation time or version."
- `outer-preservation` names identity as an extra premise in its qualification, but `premise-identity` is not among its premises.
- `reuse` requires "independent authorship" without `independence` as a premise.
- The F1–F6 premise clauses drop their "distinction retained" column:
  - F1: value choices come from the purpose owner.
  - F2: unsupported interpretation stays unresolved.
  - F4: shared machinery does not merge owners, findings or authority.
  - F6: an available tool is not permission.
- `acquisition`'s qualification "no omission to meet capacity" can be derived from Bounded construction ("Decomposition preserves all material outer obligations"). That section is not cited.

---

## C. Structural and vocabulary findings

1. **Anchors unresolved from the supplied source:**
   - `FOUNDATIONS.md#judgment-and-authority` (symbol `grant`)
   - `FOUNDATIONS.md#identity-state-and-evidence` (symbol `identity`)
   - `SOURCE.md#finite-oracle` (residual `semantic-proof`)

   None of these sections was supplied. F3 and F6 in #foundational-commitments are the supplied loci. Also, "the Product authority declared above" in Foundational commitments refers to text that was not supplied.
2. **Operator misuse.** The six `family-*` clauses use `#refines`. SIGNATURE defines Refines as a source-owned domain's reason-sensitive outcome refinement. A library responsibility *consuming* the shared contract is not that relation.
3. **Standing literal outside the vocabulary.** "domain specialization with source-owned policy" is not one of SIGNATURE's three standings (premise / source-owned method law / additional domain policy).
4. **Index gaps.**
   - The material-families frame names "the six library responsibilities", but its index omits all six `family-*` clauses.
   - 21 of the 53 clauses are reachable only as premises, with no frame index entry. These include `result-binding`, `verdict-domain`, `nonperformance`, `effect-observation`, `conjunction-failure`, `authentication`, `acquisition`, `freshness` and `workspace-truth`.
   - Whether the indexer requires direct indexing is outside what was supplied.
5. **Residual accounting.** The gaps in A and B are core law, not "fine policy". The frame `scope` strings say only fine policy and acceptance remain, which overstates core coverage.
6. **Version pairing.** The program pins `calculus_ref` to `releases/v2.5.1-rc.2/…/AXIOMATIC_CALCULUS.md`. `consumer-axiomatic-calculus` interprets the *successor* AXIOMATIC_CALCULUS. Whether the encoding calculus and the interpreted family agree is unresolved.
7. **Editorial (SOURCE.md).** "The archived … directories contain … **and supplies** … **It** is excluded" has number disagreement. Spelling is mixed: specialization/specialisation, authorised/authorized.

---

## D. Family claims: unresolved

None of the owning sources were supplied:
- TRANSFORMATION_LIBRARY
- AXIOMATIC_CALCULUS AC-007 and AC-016
- DESIGN_MODULE_METHOD
- STDO_REFERENCE_FRAME_BASELINE
- IDENTITY, ODD, REFERENCE_FRAME, RELEASE, SPEC, TICKET, TRAVERSAL, UX and WORLD_MODEL methods

So all 12 `consumer-*` statements and all 6 `family-*` statements are **indeterminate** as source-fidelity claims. Foundational commitments adds that "a family without that argument remains an unsupported specialisation". Whether each family states its premises, consequences and choices is likewise unresolved.

No consumer statement contradicts the core on its face. Three need a targeted source check because they depend on a specific role or label choice:
- **`consumer-design`**: are predecessor currentness and the admitter grant declared as *material joins* or as *admission conditions*? Under the core, the first gives `falsified` on failure. The second prevents interpretation.
- **`consumer-traversal`**: `out_of_scope` maps to `falsified` only if `event_scope_compatible` is the bound predicate and not a substituted admission check. The j_a output dependency is, per SOURCE.md, recorded but not implemented.
- **`consumer-release`**: "actual evaluation" carries the A3 wording issue.

---

## E. Scope limits of this assessment

- This was a text-only review. I did not run the Axiom Indexer or any finite oracle.
- Digests, the frozen commit, and the archived-directory exclusion were not verified.
- Structural validity and finite checks establish neither semantic fidelity nor corpus acceptance. My findings do not establish them either.
- Whole-candidate acceptance, release qualification, and independent-review standing remain with their bound owners.

**Suggested re-entry order:**
1. A1–A3: totality, the no-upgrade law, and evidenced performance.
2. A4/A5: move general configuration law into `allocation`, and route `coordinator` to its profile owner.
3. Add the aggregate-performance and acquisition-absence rules from B.
4. Then either add the remaining B items or declare them as core residuals, so the frame scope strings are accurate.
