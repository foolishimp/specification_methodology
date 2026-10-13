# Integration review: candidate 875a56e3 against preimage 5b4aebb

## Coverage

I read COMMON first, then the CORE excerpt (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations), then the two consumer diffs.

I only saw the changed hunks with about 15 lines of context each. These bodies were not available, so I could not check them:

- RF-001 to RF-006 (RF-002 to RF-004 matter most);
- the `activate` signature;
- Event-Driven Executive Attention;
- TRANSFORMATION_LIBRARY, SPEC_METHOD UP-020, DESIGN_MODULE_METHOD and TICKET_METHOD;
- PREDECESSOR_CLAIMS rows;
- F1 to F6.

Findings that depend on omitted text are marked **conditional**. This is a source check, not acceptance.

---

## 1. Activation refusal attaches work-predicate verdicts to the admission predicate

**Where:** REFERENCE_FRAME_METHOD.md, RF-012 Closed Results, paragraph 2. It joins with the baseline's Work result section and Complete Engagement Transition step 2.

**Defect:** RF-012 records a refused activation "with the failed admission predicate". It then maps a missing capability to `out_of_frame` and an unusable basis to `invalid_basis`. The core rules say otherwise:

- The admission check concluded and established its own predicate false. In the core algebra that is `performed`, `falsified`.
- "A concluding basis/scope diagnosis on P reports invalid_basis/out_of_frame on P … a different admission predicate is not silently substituted for P."

**Counterexample:** The Executive activates a Worker for P ("candidate C preserves the Product definition") with an actor that lacks the capability.

- RF-012 produces an admission result marked `out_of_frame`, and the P slot stays empty with `not_performed`.
- Core conjunction rule 3 then gives P `indeterminate` (missing evaluation), not rule 2's `out_of_frame`.
- The scope diagnosis is lost at the conjunction, and Reconfigure only fires after a "repeated indeterminate".

The other reading, where the verdict applies to P, also fails. There "an established admission prohibition → falsified" puts a `falsified`/`not_performed` result on P without any authenticated counterexample to P.

**Cause mismatch:** The baseline names five activation-refusal causes: capability, authority, stale-basis, ambiguous-basis and topology. RF-012 maps four cases. Authority and ambiguous-basis have no single target, so a consumer has to guess, which the core forbids.

**Smallest repair:** Rewrite RF-012 paragraph 2 to say:

- A refused activation is a `performed` result on the admission predicate "F may be activated for actor K on S at B".
- That result is `falsified`, with its cause, when admission is established to fail. It is `indeterminate` when admission evidence is unresolved.
- Each named refusal cause maps to exactly one of these values. Where ambiguous-basis falls is a domain choice, but it must be fixed.
- Where the plan requires P, an established capability or basis diagnosis is also reported on P as `out_of_frame` or `invalid_basis`, with `not_performed`. Otherwise P stays an absent slot with `not_performed`.
- Neither result is a Worker result. This keeps baseline step 2's "must not manufacture a Worker result" consistent.

## 2. A frame-local conflict rule competes with core conjunction and can downgrade a falsification

**Where:**

- RF Using Frames In Conjunction → Result Conjunction. The binding list still includes "how conflict and indeterminacy are handled".
- The signature block before Engagement: `conjoin(...) -> decision | conflict | indeterminate`, plus the new rule that "the frame binds any finer case mapping".

**Defect:** COMMON Single Result Algebra item 6 says conjunction is defined once, over the core. Here each frame can map `conflict` on its own terms.

**Counterexample:**

1. On mandatory P, frame A is authenticated `satisfied` and frame B is authenticated `falsified`.
2. Core rule 1 makes the conjunction `falsified`.
3. A frame binding that follows the predecessor text ("conflicted … mandatory results remain unresolved") maps `conflict` to `indeterminate`.
4. The Executive then treats the result as retainable uncertainty. The loop's stop condition lets authority retain it as a residual, and the rule "a falsified mandatory claim cannot be waived by lowering priority" never fires.

This gives a failure greater standing, contrary to core item 3 and "No refinement turns failure … into greater standing".

**Smallest repair:**

- In Result Conjunction, change that bullet to: "how conflicting or indeterminate contributions are routed for re-evaluation; the verdict is the core conjunction result."
- In the signature paragraph, state that `conjoin`'s verdict is the core conjunction, and that `conflict` annotates retained contradictory authenticated contributions rather than being a separately mapped outcome.

## 3. Missing-cause case not mapped, so the map is not total

**Where:**

- Baseline Work result: "a generic re-entry request without it is insufficient" and "total over these declared cases".
- RF-012: "An unclassified finer outcome is not silently treated as satisfaction."

**Defect:** The core requires the reason domain to include an explicit missing-reason case. A missing required reason maps to `indeterminate`, is inadmissible as deciding support, and keeps its raw outcome. RF-012's restatement only rules out `satisfied`, so it still permits `falsified`, `out_of_frame` or `invalid_basis`.

This also loses the predecessor's "total and exclusive" claim (Closure item 4 dropped "exclusively").

**Counterexample:** A Worker returns `re_entry_requested` with no cause.

- The baseline gives no verdict.
- RF-012 allows the predecessor mapping to `out_of_frame` or `invalid_basis`.
- The Executive reconfigures, or refuses consumption, as though a scope or basis diagnosis had been established.

**Smallest repair:**

- Add a row to the Work result table: "`incomplete` or `re_entry_requested`, cause missing → `indeterminate`; raw outcome retained; inadmissible as deciding support."
- Replace RF-012's sentence with: "An outcome lacking its required cause follows the core missing-reason rule."

## 4. Authorisation substitutes for established idempotence on retry

**Where:** RF Engagement → Select And Activate, the new paragraph ending "…or an authorised recovery contract permits another action."

**Defect:** The core (Workspace and context) allows a retry with uncertain effects only after enough observation or reconciliation to decide the next dependent action, or where idempotence is established for that subject and effect. "Otherwise select another permitted action or return the unresolved result." A grant alone is not enough.

**Counterexample:** A non-idempotent external send loses its acknowledgement, so the effect is `unknown`. A recovery contract authorises a resend. The RF text lifts the hold and the effect is duplicated.

**Smallest repair:** Change the ending to: "…until observation or reconciliation suffices to decide the next dependent action, or idempotence is established for that subject and effect; otherwise select another permitted action or return the unresolved result."

## 5. The Worker result has no single bound predicate

**Where:** Baseline Work result table, "Predicate and evidence condition" column.

**Defect:** Each row decides a different claim:

- `candidate_ready` decides availability;
- `refused` decides the "requested construction claim";
- `incomplete` decides the "declared construction claim";
- `postcondition_defeated` decides "that exact claim", with a deadline.

The core needs one predicate per result and per plan slot.

**Counterexample:**

1. A Worker misses a deadline and returns `incomplete`/`postcondition_defeated`, which maps to `falsified`.
2. If the predicate is plain availability, a missed deadline is not a counterexample to it.
3. A reactivated Worker then returns `candidate_ready`, `satisfied`, on the same slot.
4. Either the two results contradict each other, or they are about different predicates. In the second case the baseline's own rule ("cannot conjoin different predicates") leaves the slot with no comparable result.

**Smallest repair:**

- State the Worker predicate once, for example: "the requested candidate and its transition evidence are available on the activated basis within the admitted grant's declared bounds."
- Phrase every row against that predicate.
- Include the bounds clause only if `postcondition_defeated` is kept.

## 6. Competing acquisition owners (conditional on omitted bodies)

**Where:** RF Position.

- "RF-002 through RF-004 decide that acquisition." The core's Workspace and context section already decides acquisition ("Acquisition binds the current task, subject…").
- "The transformation library binds acquisition, evaluation and result consumption." This replaces the predecessor clause saying the library's correspondences are explanatory and that the RF functions keep their applicability, result algebras and owner boundaries. That retention obligation is now lost.

This conflicts with COMMON Single Ownership items 3 and 7.

**Smallest repair:**

- Change the first sentence to "RF-002 through RF-004 refine the core acquisition rule for frame activation."
- Restore: "The library's responsibilities are explanatory correspondences; the core and the method functions below retain applicability, results and owner boundaries."

## 7. The Executive's fit path has no stop

**Where:** Baseline Executive Attention, Evaluation, And Action, the paragraph after the loop: "If that decision does not fit, it refines … or obtains another bounded evaluation."

**Defect:** COMMON Bounded Transitions item 2 and the core's total control contract both require "return the applicable stop" as an alternative. Without it, a decision that cannot be refined has no lawful response.

**Smallest repair:** Append "or returns the applicable stop retaining the unresolved obligation."

## Conditional: liveness of unreturned Worker activations

The predecessor said "every coordinated Worker activation terminates in one closed work result". Step 3 now covers only completed activations; interruption becomes "observed as unreturned work".

Unless Event-Driven Executive Attention (omitted) re-enters on non-return, through an observation or bound, a lost Worker produces no event and the loop awaits indefinitely. Check that section. Also check that PREDECESSOR_CLAIMS records dispositions for:

- this replaced claim;
- "complete Product view";
- "conflicted remains unresolved";
- the library's explanatory status.

## Checked without defect at the visible joins

- The Reviewer projection is total over the core verdicts.
- `candidate_ready` is limited to availability, which matches core item 5.
- Unconfirmed or absent returns stay absent slots with `unconfirmed`, and no effect is inferred from a missing return.
- The RF-009 and baseline configuration text matches core Configuration.
- The RF reuse rewrite conserves the predecessor's content through the core reuse rule.
