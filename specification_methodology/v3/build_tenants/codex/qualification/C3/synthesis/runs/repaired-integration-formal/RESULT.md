# Integration review: candidate 9982ab80 against preimage 875a56e3

## Coverage

- **Read in this order:** the Common Requirements, then the FOUNDATIONS core sections (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, derivations), then the consumer diff.
- **Source:** only the changed hunks with about 15 lines of context. I did not see:
  - the omitted bodies of AXIOMATIC_CALCULUS, DESIGN_MODULE_METHOD and TRAVERSAL_OCCURRENCE_PROFILE;
  - SPEC_METHOD (including UP-021 and the `#what-how-and-work-carriers` anchor);
  - TRANSFORMATION_LIBRARY and PREDECESSOR_CLAIMS.
- **Headings:** several section headings fall outside the hunks. I name the nearest visible anchor in those cases.
- **Status:** this is a working source check. It does not accept any member and does not approve the source-port review policy.

## Findings

### 1. The semantic-cut judgment `j_a` is both the output of the conjunction and one of its inputs

**Where:** TRAVERSAL_OCCURRENCE_PROFILE, in two places:
- the `semantic_cut_admission` row of the closed judgment domains table ("core conjunction decides");
- the paragraph after the `j_c / j_e / j_a` block, beginning "Apply core conjunction before mapping the composite result…", just before `### OP-002 Atomic Semantic Admission`.

**Contradiction:**
- The row makes `j_a`'s decision the result of core conjunction.
- The paragraph maps that conjunction into `j_a`'s decision domain (`refused`/`invalid_basis`/`hold`/`admitted`).
- It then says "`satisfied` permits `admitted` only with all three exact admission decisions above". "All three" includes `j_a`.
- It also says "a missing `j_a` remains an absent slot", which makes `j_a` an input slot of the same conjunction.

**Counterexample:** take authentic admitted `j_c` and `j_e` and a valid seven-member cut.
- `j_a` cannot be `admitted` until the conjunction is satisfied.
- The conjunction cannot be satisfied until `j_a` is `admitted`.
- The absent `j_a` slot therefore keeps the conjunction `indeterminate`, so `j_a = hold` permanently.
- Every well-formed cut is held.

OP-002 confirms the intended structure: the seven cut members include the claim judgment and the event judgment, and `j_a` judges the cut.

**Smallest repair:**
- Define `j_a`'s verdict as the core conjunction of the authenticated `j_c`, the authenticated `j_e`, and the cut's declared joins.
- State that the cut is admitted exactly when `j_a` is `admitted`.
- Replace "all three" with "`j_c` and `j_e`".
- Move "a missing `j_a` remains an absent slot" to the downstream consumer that requires an admitted cut.

### 2. An established stale source frontier maps to `hold`, but the conjunction now invoked cannot produce that value

**Where:** TRAVERSAL_OCCURRENCE_PROFILE, `semantic_cut_admission` row ("stale source frontier retains `hold` plus `stale_frontier`"). The unchanged `claim_admission` row has the same issue.

**Contradiction:** core Result conjunction requires the composite to declare each relation as either an admission condition or a material join, and to name that role.
- If staleness is an established failed join, the conjunction is `falsified`, which the new map turns into `refused`.
- If staleness is a failed admission condition, the conjunction is `invalid_basis`.
- Neither role yields `indeterminate`/`hold`.

The profile's own rule allows `hold` only "where decisive evidence is missing", and established staleness is decisive evidence. The new text declares membership and equality as joins but gives frontier currentness no role. The changed DESIGN_MODULE_METHOD `#### Admission contract use` does declare predecessor currentness a join, so the stale case falsifies there. The two admission refinements therefore disagree on the same kind of fact without a declared domain difference.

**Counterexample:** the cut's source frontier is proven superseded. The row says `hold`. The conjunction it cites gives `falsified` → `refused`, or `invalid_basis`. Core precedence also changes the result when another component is `invalid_basis`: a `hold` treatment lets `invalid_basis` win, while a `falsified` treatment wins over it.

**Smallest repair:**
- Declare source-frontier currentness a material join of the cut predicate.
- Map established staleness to `falsified`, giving decision `refused` with cause `stale_frontier`, while keeping the reconstruction re-entry.
- Keep `hold` only for unestablished currentness.
- Apply the same role declaration to `claim_admission`.

### 3. The new `hold` cases on the cut have no declared cause, residual or re-entry (a lost obligation and a recovery gap)

**Where:** TRAVERSAL_OCCURRENCE_PROFILE, the `semantic_cut_admission` row and `### OP-002 Atomic Semantic Admission`.

**Lost obligation:** the preimage turned a missing or non-admitted judgment, a wrong subject or digest, a cross-basis judgment, or a missing member into `refused`. That outcome had a defined stop. The candidate now routes held, absent or unauthenticated judgments to `hold`. The row names a cause and re-entry only for staleness. However:
- the profile states that "the judgment kind defines the applicable stops and residuals; none is inferred from prose";
- AXIOMATIC_CALCULUS requires `hold` always to carry a declared cause.

**Counterexample:** `j_e` is absent. The cut gets `hold` with no cause, no residual and no re-entry. It is also unclear whether a later admitted `j_e` reopens the same unchanged cut or requires a new one. The duplicate rule ("non-identical collision refuses `refuse_duplicate`") makes this ambiguity material.

**Smallest repair:** add to the row's stop/residual/re-entry column:

> missing, held or unauthenticated component judgment retains `hold` plus `unresolved_cause` (naming the slot); re-enter with a new `j_a` over the unchanged cut once the component is admitted, or reconstruct.

### 4. `J:*.verdict` drops `out_of_frame`, which conflicts with the calculus refinement rule and leaves the cut map incomplete

**Where:**
- TRAVERSAL_OCCURRENCE_PROFILE: the new Judgment value-contract table (`J:*.verdict`) and the cut mapping paragraph.
- AXIOMATIC_CALCULUS: the clause before `### AC-008 Explicit Latitude` (presumably AC-007), which says `hold`/`gap`/`refusal` with cause "missing material frame scope or capability" maps to `out_of_frame`.

**Contradiction:** the profile's decision domains include `hold` and `gap`. For an in-domain request, a capability shortfall must therefore map to `out_of_frame` under AXIOMATIC_CALCULUS, but `J:*.verdict` forbids that value. The profile only routes out-of-domain requests to the invocation boundary. In addition, the cut map covers `falsified`, `invalid_basis`, `indeterminate` and `satisfied`, but not `out_of_frame`, even though core conjunction rule 2 can produce it.

**Counterexample:** a `frontier_projection` `gap` whose lineage needs an adopted external kind that the evaluator cannot resolve. The calculus requires `out_of_frame`; the signature cannot record it. Alternatively, an invocation-boundary `out_of_frame` returned for `j_e` turns the cut conjunction `out_of_frame`, and that value has no decision.

**Smallest repair:**
- Admit `out_of_frame` in `J:*.verdict` for in-domain capability or scope shortfalls.
- Keep the out-of-domain sentence.
- Add "`out_of_frame` maps to `hold` with cause `out_of_frame`, retaining that core verdict" to the cut map.

The alternative is for the profile to state, as a guarantee, that in-domain admission ensures evaluator capability, and to accept an invocation-boundary `out_of_frame` as an authenticated contribution.

### 5. Possible second owner: the role of predecessor currentness and grant in admission

**Where:** DESIGN_MODULE_METHOD, `#### Admission contract use`.

**Issue:** the change makes predecessor continuity, predecessor currentness and grant material joins of the admission predicate. That choice decides between `falsified` and `invalid_basis`. The same section says "UP-021 owns the admission decision and standing-test semantics." I cannot see UP-021.

- If UP-021 classifies a stale basis differently (for example as `invalid_basis`, as the preimage text did), two loci decide the same question, contrary to the Single Ownership requirement, item 7.
- If UP-021 is silent, the choice is a legitimate refinement and needs no change.

**Smallest repair:** if UP-021 does state a role, replace the DESIGN sentence with a reference to it. Otherwise no change is needed.

## Checked with no finding at the visible joins

- **AXIOMATIC_CALCULUS:** a prohibition falsifies only the permission or admission predicate, and the unevaluated constraint stays `indeterminate`. This matches the core legal pairs.
- **AXIOMATIC_CALCULUS composition:** the declared-operator delegation and the fallback rule match the core declared-operator and first-nonfailure rules. The clause's AC-016 identity is unverified because the heading is not visible.
- **AC-014 Judgment additions** (required fields, performance extent, no default to `not_requested`) match the core.
- **TRAVERSAL effect mapping:**
  - `no_effect` stopped before dispatch becomes `not_started` only with authenticated evidence, otherwise `unknown`.
  - `partial_effect` maps to `partial`, `reverted` or `unknown`.
  - Lost transport cannot become `no_effect`.

  All three match the core effect law.
- **Field count:** the nineteen-field closure is consistent with the field list in the visible inheritance sentence. The rows for context, owner, scope and basis are not visible.
- **DESIGN `### Cross-view axiom evaluation`:**
  - `not_applicable` now falsifies the applicability predicate and acts as coverage evidence, not as a failed conjunct.
  - Applicable-but-out-of-scope is `out_of_frame`.
  - The preimage obligation that only a supported exclusion removes an axiom is conserved.
  - No consumer outside DESIGN that conjoins the table's raw core verdicts was visible to check.
- **DESIGN build-tenant paragraph:** the reference to SPEC_METHOD aligns with the Build-Tenant Binding requirement ("each candidate's Spec Method states and applies"). The anchor and its content are unverified.
- **DESIGN effect return:** the added `reverted` value aligns with the core.
