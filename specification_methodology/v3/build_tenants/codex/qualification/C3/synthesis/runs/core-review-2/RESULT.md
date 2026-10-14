# Independent review: revised Codex core (FOUNDATIONS.md, TRANSFORMATION_LIBRARY.md)

I checked the source against README common requirements first, then the text. The scope is the two members shown. I made no release-acceptance inference and no port-fidelity review. Where a determination may live in an unseen member (RF-*, UP-*, AC-*, Baseline), I mark it as unverified rather than as a defect.

## Material defects

### M1. The performance coordinate has no defined boundary, so equal facts get different encodings and different conjunction verdicts
**Requirement:** Single Result Algebra 3 (not performed ≠ undecidable), 6 (one composition).

`FOUNDATIONS.md#result-algebra` says performance "concerns the named predicate". Yet `not_performed` means "the named evaluation did not run". `performed` covers "scope or basis diagnosis", but "a failed admission check can be performed while downstream work is not performed." Three boundaries are left undefined: diagnosis vs judgment, started vs concluded, and operation vs evaluation.

- **Counterexample A (basis failure).** An admission check finds that subject S's digest ≠ bound B, so evaluation of P never launches. Two legal encodings follow:
  - (i) P = `performed/invalid_basis`. The conjunction is `invalid_basis` (rule 2), which leads to re-entry on the basis.
  - (ii) admission predicate = `performed/falsified`, and P = `not_performed/indeterminate`. The conjunction is `falsified` (rule 1), which invites rejection of a candidate whose only defect is a stale evaluation basis.
- **Counterexample B (aborted run).** A test runner is OOM-killed at 40% with no failures seen. `not_performed` is false because it started. `performed/indeterminate` merges "aborted, retry may decide" with "concluded, evidence cannot decide", which is the distinction item 3 protects.

**Minimal correction:** Define the coordinate over conclusion of the named predicate's evaluation procedure:
- `performed`: the procedure reached its declared conclusion, including a scope or basis diagnosis.
- `not_performed`: evidence establishes that it reached no conclusion. This covers never started, or a known abort, with the abort retained as evidence.
- `unconfirmed`: whether it concluded is not established.

Add: "A failed basis or scope precondition is reported on each dependent required predicate as `invalid_basis`/`out_of_frame` with performance `performed`, citing the precondition result. That precondition result is evidence, not an additional required predicate, unless the governing plan declares it one."

### M2. An authenticated join failure does not falsify the conjunction
**Requirement:** Single Result Algebra 3, 6, and the Foundations derivation row "a failed required predicate defeats conjunction".

`#result-conjunction` evaluates "all required predicates and their material joins", but rule 1 fires only on falsification of a "required predicate". A disproved join falls into rule 3 ("unproved material join") and yields `indeterminate`.

- **Counterexample:** Modules M1 and M2 each satisfy their contracts, and an authenticated integration check of their interface join fails. The aggregate is `indeterminate`, not `falsified`. A known failure is graded as missing evidence, which contradicts "Local success cannot erase a failed … material relation" (`#typed-composition-and-conservation`).

**Minimal correction:** In rule 1, change "of a required predicate" to "of a required predicate or material join". In rule 3, change "unproved" to "undecided".

### M3. Result composition beyond conjunction is not defined once, and standing protections lapse there
**Requirement:** Single Result Algebra 6, and 3 as applied to composites.

The text says three things:
- Disjunction and selection "evaluate [their] own predicate".
- Sequential results evaluate "the declared outer predicate using its preservation argument".
- Only all-stage pipelines reduce to conjunction.

So any recovery path, fallback or selection combines results by a per-instance rule. The core's guards ("satisfied requires … authentically satisfied", authentication, coverage) are stated only for conjunction. The refinement guards cover single-outcome mapping, not operators.

- **Counterexample:** The outer predicate is "primary deploy OK or fallback OK". Primary is `performed/falsified`, and the fallback's acknowledgment is lost, so it is `unconfirmed/indeterminate`. A domain "first non-failure" rule returns `satisfied`, and no core clause forbids it.

**Minimal correction:** Generalise `#result-conjunction` into one operator rule, with conjunction as its instance:

> "A declared operator states truth and falsity conditions over its required leaves and joins. The aggregate is `satisfied` only when the truth condition is met by authenticated satisfied leaves and established joins and coverage. It is `falsified` only when the falsity condition is met by authenticated falsifications. Otherwise the invalid_basis → out_of_frame → indeterminate precedence applies to the leaves that could change the outcome. Authentication, retention and the effect join are unchanged."

Under this rule, disjunction is the dual case. Sequential composition then reads: "evaluates the declared outer predicate under this rule."

### M4. A fully observed begun-and-reverted effect has no truthful value
**Requirement:** README Bounded Transitions 5 ("unknown effects are resolved sufficiently"), and truthful state.

The defined values do not cover this case:
- `not_started` requires that the effect "did not begin".
- `partial` requires an observed completed part.
- `completed` is false.

- **Counterexample:** A transaction begins, an authenticated rollback is confirmed, and nothing persists. The only admissible value is `unknown`. Under `#workspace-and-context` this demands reconciliation, but no observation can ever move it out of `unknown`. The record cannot express a resolved state.

**Minimal correction:** State that effect values describe the selected effect at the declared observation boundary. Extend `not_started` to "did not begin, or every begun part is evidenced as reverted within that boundary, with the reversal retained as evidence". Extend `partial` to "observed completed part and observed unexecuted or reverted remainder". Effects that cannot be reverted, such as sent messages, must lie inside the declared boundary.

### M5. The Library narrows Acquire's failure result to `indeterminate`, contradicting its own Acquire section and the core
**Requirement:** Single Ownership 7 and Single Result Algebra 6.

`TRANSFORMATION_LIBRARY.md#foundational-contract` says Acquire "returns support adequate … or an indeterminate result". `#acquire` says "the applicable core result".

- **Counterexample:** The bound source digest cannot be resolved. The foundational contract yields `indeterminate`, while the core meaning yields `invalid_basis`. The conjunction precedence then differs (rule 2 vs rule 3), so two loci give two answers.

**Minimal correction:** Change the clause to "or the applicable non-satisfied core result (`indeterminate`, `out_of_frame` or `invalid_basis`) with the unresolved support".

### M6. Configuration preservation is narrower than README Bounded Transitions 4
README 4 requires: "the permitted allocation and reconfiguration preserve material dependencies, outstanding obligations, effects, admitted authority and required independence."

`FOUNDATIONS.md#configuration` covers only "an adaptive reassignment", and preserves "effect uncertainty", not effects.

- **Counterexample:** A fixed configuration is re-planned between activations. A completed charge that was observed only in the prior actor's frame is not required to survive. The new actor sees no uncertainty and repeats the charge.

**Minimal correction:** Replace the sentence with "Every allocation and reconfiguration, fixed or adaptive, preserves material dependencies, outstanding obligations, observed and uncertain effects, admitted authority and required independence."

### M7. Foundations gates sequential composition on a Library contract that the Library disclaims
**Requirement:** Single Ownership 1 and 3.

`#result-conjunction` says "Sequential operations compose only under the library's typed composition contract." `TRANSFORMATION_LIBRARY.md#composition-law` assigns design composition to UP-016/UP-017 and calculus composition to AC-016. It also says it "establishes neither a new composition obligation". An actor following the gate therefore reaches no owner.

**Minimal correction:** Change the clause to "compose only under their applicable owner: UP-016/UP-017 for design composition, AC-016 within a_c". Foundations keeps only the result side, as revised by M3.

## Minor defects

1. **Refined value domain** (`#result-algebra`, reason-sensitive map vs SRA 2 "exactly one core value"). Declare the refined value as the pair (outcome, reason) over a declared reason domain. Make "reason missing" an explicit refined value mapping to `indeterminate`, with performance as known. This replaces "inadmissible for its slot", which reads as outside the core.
2. **Absence in a projection** (README BT 5, "an absent sparse file is not evidence of absence"). The core states this only for effects ("empty local log"). If no unseen member owns it, add to `#workspace-and-context`: "Absence from a partial projection, sparse checkout or empty local record is not evidence of absence in the bound subject; observe the authoritative source at the bound basis or return `indeterminate`."
3. **Duplicate misfit determination.** Library `#acquire` restates the capacity-misfit response list that Foundations owns in `#finite-capacity-and-total-handling`, with different wording ("refinement or reassignment"). It also cites the wrong section (Workspace and context). Replace the list with a reference.
4. **Owner kind collision.** README defines owner as a textual locus. Foundations says "the context and owner declared above own F1–F6", where that owner is the Product authority, and gives the import source owner as a file. State that the section is the owning locus and that the Product authority is the context's semantic authority.
5. **Two encodings of an unrun stage.** "Records a downstream evaluation as `not_performed`" conflicts with "absent coverage slot … not a fabricated child result". Pick one form, for example: "an absent slot carrying `not_performed`, or `unconfirmed` when the run is not established".

## Bounded no-new-defect results (within these two members)

- **Legal verdict/performance pairs:** satisfied and falsified require `performed`, which is sound apart from M1.
- **No standing raise through refinement:** failure, undecidability, non-performance and unknown effects all stay distinct.
- **Candidate stages:** availability, fitness and acceptance stay separate, and the decision-result predicate is separate from recording.
- **Stop reporting:** sound.
- **Effect join:** it is the join on the lattice NR < {C, NS} < P < U, so it is associative and commutative. The verdict combination is max on falsified > invalid_basis > out_of_frame > indeterminate > satisfied, so it is associative. The regrouping premises, a fixed interpretable basis with no hidden intermediate basis failure, are sufficient. Reordering correctly needs a separate effect-independence law.
- **Unknown effects:** retry is gated on established idempotence, and transport dispatch or a lost acknowledgment is treated as `unknown`.
- **Observation freshness and basis:** contrary evidence reopens claims without rebinding the basis or granting authority, and resumption from workspace needs no universal replay.
- **Authority:** imports are reference-only, and no grant is minted from evidence, capability, names or frame selection.
- **Categorical claims:** A, I and C_H are correctly held as hypotheses pending objects, arrows and laws. Conformance, equivalence and functoriality stay distinct.

## Not verifiable here

- The refinement maps for WorkerResult, AC-007/AC-013 and RF-012.
- Frame carriage of the algebra (SRA 7).
- Build-tenant item 2 (actor ≠ adjudication), which README assigns to Spec Method.
- The RF-014 and UP-020 contents these members rely on.
