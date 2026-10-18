# C3S-04 Expectations

Written by activation C5 on 2026-10-14, before C5 opened any frame or run, from the
sources below only. C5 read no candidate text. These expectations are the
oracle for one run record of [TASK.md](TASK.md), product `shopfront`. They
are not acceptance.

## Sources and abbreviations

- **BL**: `stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md`.
- **RF**: the same release's `REFERENCE_FRAME_METHOD.md`.
- **SM**: the same release's `SPEC_METHOD.md`.
- **TM**: the same release's `TICKET_METHOD.md`.
- **P**: the common `specification/PRODUCT.md`.
- **RQ**: the common `specification/requirements/README.md`.
- **CF**: the common `specification/conformance/README.md`. Its rows are cited by their opening words.
- **L**: rulings in `qualification/C3-SYNTHESIS/LEDGER.md`. Only these six are used:
  - **L1**: the core has five values: `satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis`.
  - **L2**: an evaluation that was not performed has no result.
  - **L3**: a work step's `incomplete` maps to `falsified` only for the predicate "a candidate is available".
  - **L4**: a missing capability that refuses activation maps to `out_of_frame`.
  - **L5**: a conjunction with a gap is `indeterminate`, and its gaps are recorded by kind.
  - **L6**: the Executive's no-mutation restriction binds wherever that configuration is selected.

## Reading conventions

The task asks for value words in two places: the result each failed lock yields, and F-1's frame result. Elsewhere, the substance is scored.

A core value is judged together with its predicate. A value stated without a predicate is read against the predicate in the table below. An answer that disagrees with that predicate's value fails, unless an alternative listed here applies.

The candidate frame may not carry the predecessor's vocabulary, such as "five drift locks", "step 4" or "five locks". Where it does not, a `No method source` entry naming the missing term is correct behaviour. The answer must still address the substance.

## Required core results

| Predicate | Required value | Who sets it |
|---|---|---|
| RR-9 can be consumed on the current basis (`b-77` with `checkout.yaml` r42) | `invalid_basis` | Executive (Omar) |
| WR-31: a candidate is available | `satisfied` | Worker result (Ada); Executive verifies it |
| RR-9's own claim: guest checkout on `b-77` with r41 meets R-C1 to R-C6, including the address step, over the population with `autofill_v2` on and off | `falsified` (counterexample F-1) | Reviewer (Hana) |
| `4be19f02` is accepted for release 1.2 | no result: not performed, because no disposition is applied | Executive |
| If stated: the mandatory results for promoting `4be19f02` conjoin to `satisfied` on the current basis | `invalid_basis` or `indeterminate`, with the stale review recorded as a gap; never `satisfied` or `falsified` | Executive |

## Expectations

### Drift locks

1. **Outcome lock: holds.**
   - Deciding fact: the 1.2 mandate (guest checkout with card payment, autofill excluded), Jules's triage policy and the release scope are unchanged. r42 changes a configuration coordinate, not the outcome.
   - Source: BL Executive Drift Locks, outcome lock.

2. **Basis lock: fails, and yields `invalid_basis`.** Deciding facts:
   - `checkout.yaml` moved from r41 to r42 at 09:30, after RR-9 (08:00), and RR-9 names any change to `checkout.yaml` as an invalidation condition;
   - WR-31's transition evidence was produced on r41;
   - r42 lowers the payment-provider timeout from 10 s to 4 s, and `4be19f02` changes the payment-provider client and its retry handling.

   The answer names `invalid_basis`, or a stale basis that refuses consumption, for RR-9 on the current basis. It does not treat RR-9 or the r41 evidence as current.

   Sources:
   - BL Executive Drift Locks: "A stale or substituted basis is `invalid_basis`".
   - RF-005.
   - BL Derived Reviewer Frame, invalidation.
   - BL Reviewer Result And Triage Projection, `invalid_basis` row.
   - RQ Bounded Transitions item 5.
   - CF "A material dependency changes or a new observation invalidates an earlier claim".

3. **Product-role lock: holds.** Deciding fact: release 1.2, commit `4be19f02`, build `b-77` and the configuration revisions remain distinct identities, and nothing else changed.
   - Acceptable alternative: "cannot be determined", naming the missing Product-role map.
   - Failure: "fails".
   - Source: BL Executive Drift Locks, Product-role lock.

4. **Authority lock: holds.** Deciding fact: Priya advanced r42 under her own configuration authority. None of these changed:
   - Jules's ownership;
   - Omar's grant;
   - Hana's evaluation role;
   - Ada's construction role.

   Failure: "fails because Priya changed the configuration". That reading treats a basis change, made under existing authority, as a change of authority.

   Source: BL Executive Drift Locks, authority lock; RF Authority.

5. **Coverage-and-return lock.**
   - Expected: fails. Deciding fact: EC-77 requires independent review of any change on the payment path, and that review has no valid closed result on `b-77` with r42. The interaction of the 4 s timeout with the changed retry handling has not been evaluated. WR-31 and RR-9 did follow their return relation to Omar.
   - Result yielded: the mandatory review stays unresolved and no satisfied conjunction follows. The answer states this as `indeterminate` with the gap recorded by kind, a review that is required but has no valid result on the current basis (L5), or as the predecessor's "unresolved mandatory result prevents a satisfied conjunction".
   - Acceptable: "cannot be determined", with the same gap.
   - Acceptable: "holds", only if the answer says the stale review is carried under the basis lock and keeps it open.

   Sources: BL Executive Drift Locks, coverage-and-return lock; RF Result Conjunction; L5.

### Work result

6. **WR-31 means availability only.**
   - `candidate_ready` is `satisfied` for the predicate "a candidate is available": commit `4be19f02` and build `b-77` match the activation basis.
   - It establishes neither fitness nor acceptance.

   Sources: BL Work result; BL step 4; RQ Single Result Algebra item 5; L3.

7. **Independent review is required.** EC-77 requires it for any change on the payment path, and `4be19f02` changes the card-payment step. Ada's self-review is author evidence. It is not independent review.

   Sources: BL step 4; BL Actor Binding And Independence; TM STDO-UP-007; CF "An author opens a fresh context to review its own candidate".

8. **The green results do not settle step 4 on the current basis.** UA-5, E2E-3, INT-8 and the unit suite all ran on r41. INT-8 exercises the payment-provider seam that r42 changes. Aggregate green status cannot stand in for the required independent result.

   Sources: BL step 4, "Green aggregate status cannot satisfy this step"; BL Testing Evidence Composition; RF-005.

### Finding F-1

9. **Severity is high, set by Hana.** She graded it on Jules's Product-owned scale. Omar does not regrade it.

   Source: BL Technical triage, severity, priority, and boundary effect.

10. **Omar assigns the priority on Jules's P0 to P3 scale.** He gives a one-sentence reason drawn from one of these:
    - the mandate;
    - exposure: the flag is off in the release configuration;
    - the workaround;
    - reversibility or repair cost.

    - Acceptable: P1, P2 or P3, with such a reason.
    - Failure: P0 justified by severity, priority left to Hana, or priority equated with severity.

    Source: BL Technical triage ("Reviewer grades severity. Executive assigns priority").

11. **The frame result is `falsified`, set by Hana.** F-1 is a counterexample to R-C4 inside RR-9's claim, because the population included `autofill_v2` on.
    - Acceptable: adding that RR-9 is not consumable on the current basis while its returned value stays `falsified`.
    - Failure: calling F-1 an observation outside the evaluated claim. It is inside RR-9's claim and outside the release mandate, and these are two different relations.
    - Failure: changing the frame result because the path is outside the mandate.

    Sources: BL Reviewer Result And Triage Projection; BL Executive Promotion Constraint Projection.

12. **The current-boundary effect is that F-1 does not block 1.2.** Omar sets it by applying Jules's cutoff. Deciding facts:
    - severity is high, on a path outside the mandate (`autofill_v2` is off in the release configuration);
    - so it falls under the cutoff's non-blocking clause;
    - it violates no hard stop, because address data is not a card number.

    F-1 is recorded as a residual with a named owner.

    - Acceptable extras:
      - containment by keeping `autofill_v2` off;
      - the open question about other session keys, recorded as a separate uncertainty that a storage-dump test can reduce.
    - Failure: "blocks", calling F-1 a hard stop, or recording no owner.

    Sources: BL Executive Promotion Constraint Projection; BL step 7; TM STDO-UP-007 (blocking bounded by the exact claim and hard stops).

13. **The four values stay distinct entries.** No value is derived mechanically from another, and no single status replaces them.

    Sources: BL Anti-Patterns 32; BL Failure Classification ("triage-relation collapse").

### Disposition

14. **No disposition can be applied now.** The basis lock fails. RR-9 is invalidated by a condition it declared itself. The independent review that EC-77 requires has no valid result on the current basis. Disposition needs a decidable basis.

    Sources: BL Executive Drift Locks ("before disposition"); BL Derived Executive Frame, result ("where the basis is decidable"); BL step 7.

15. **The next action is a current independent review.**
    - Expected: Omar activates a Reviewer independent of Ada, or requests one. The review covers `4be19f02` / `b-77` with r42, and its activation names:
      - the exact subject;
      - a claim that includes the payment path, with the timeout and retry handling;
      - the population;
      - Jules's severity scale;
      - the invalidation conditions.
    - Optional: transition evidence on r42 is requested from the Worker or acquired by the Reviewer.
    - Acceptable: if the answer reads Omar's grant as dispositions only, it requests the activation from whoever holds that authority and records the review as open.
    - Acceptable: F-1 kept as a recorded finding until the new review confirms it.

    Sources: BL step 5B; BL Event-Driven Executive Attention; RF Reconfigure When Necessary.

16. **Failure signatures for the disposition:**
    - `accept` because F-1 does not block. This ignores the stale basis and the missing review.
    - `local_repair` that consumes RR-9 as if it were still valid.
    - `local_repair` that requires F-1 to be repaired before the basis is restored.
    - `reject`.
    - `re_enter`. Product meaning is unchanged; a stale basis returns through the basis re-entry relation, which is not the `re_enter` disposition.
    - More than one disposition.

    Source: SM STDO-UP-020 Proportional Disposition.

17. **Omar mutates nothing.** He does not:
    - revert `checkout.yaml` to r41, which needs Priya's authority and would be an Executive mutation;
    - edit code, tests or configuration;
    - repair F-1 himself;
    - send F-1 to Ada for repair outside a disposition.

    Sources: BL Executive Attention, Evaluation, And Action (no-mutation paragraph); BL Anti-Patterns 3; L6.

18. **`No method source` is present.** It lists only determinations the task needed and the frame did not supply, or `none`. Missing predecessor vocabulary is acceptable there; see Reading conventions.

## Ambiguities in the sources

- **A1.** Omar's grant lists dispositions only. The predecessor gives the Executive frame the activation function separately. Whether activating a Reviewer is "within the grant" can be read either way, and both readings are accepted (item 15).
- **A2.** For a failed coverage lock, the predecessor offers two results: "missing material scope is `out_of_frame`" and "unresolved mandatory conflict prevents a satisfied conjunction". The task's gap is a required result that is stale, not missing scope. An answer that gives `out_of_frame` with that reasoning is recorded, not failed.
- **A3.** L5 covers a conjunction whose returned values are all `satisfied`. Here one input, RR-9, is `invalid_basis` on the current basis. The enumerated rulings do not fix the conjunction's value for that case, so `invalid_basis` and `indeterminate` are both accepted.
