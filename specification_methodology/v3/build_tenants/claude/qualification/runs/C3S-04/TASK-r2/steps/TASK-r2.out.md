## Drift locks

| Lock | Status | Deciding fact |
|---|---|---|
| Outcome | Holds | The task states no change to the 1.2 mandate (guest checkout with card payment), the Product outcome, the boundary or the triage policy. The only change is the r42 configuration edit. |
| Basis | **Fails** | `WR-31` and `RR-9` are bound to build `b-77` with `checkout.yaml` r41. The configuration coordinate is now r42, so it is no longer exact and current. `RR-9` also names any change to `checkout.yaml` as an invalidation condition. |
| Product-role | Cannot be determined | The task gives no facts about Source Project, Product, Install or Development Product identities or their bindings. I can't confirm or deny this lock. |
| Authority | Holds | Priya changed the configuration under her own configuration authority. The task gives no change to Omar's grant, Jules's ownership, the `EC-77` requirement or the review and acceptance owners. |
| Coverage-and-return | **Fails** | `EC-77` requires independent review of payment-path changes. The only closed review (`RR-9`) is invalidated by its own condition. The r42 change touches the payment-provider timeout, and the card-payment step is part of this candidate. The user-acceptance, end-to-end and integration results were produced on r41. So a material evaluation has no closed result on the current basis. |

- **Basis lock, result yielded:** a stale basis is `invalid_basis`. `RR-9` and the r41-bound evidence of `WR-31` cannot be relied on for r42 until their applicability is re-established.
- **Coverage lock, result yielded:** the method gives this lock no named core value. Its effect is a planned assessment with no applicable closed result, which is a gap. Any conjunction over these results is therefore never `satisfied`. Per the conjunction rule, if the mandatory results were all `satisfied` it would report `indeterminate`, with the gap recorded as "not performed on r42". Here the mandatory review is already `falsified` on r41, so the declared rule for the non-satisfied value is what the mandate would still have to supply.
- **Not determined:** whether the r42 timeout actually changes any outcome. I haven't inferred that either way.

## Work result

- `WR-31` is `candidate_ready`, which maps to `satisfied` for the predicate "a candidate is available". It shows only that an exact candidate (`4be19f02`, `b-77`) and its transition evidence exist. It is not an assessment and not acceptance.
- The subject is exact. The evidence is not current. `UA-5`, `E2E-3`, `INT-8` and the unit suite were all run with r41. `INT-8` (the payment-provider seam) and `E2E-3` (cart to confirmation) are the most exposed to a timeout change.
- I can't treat those results as covering r42, and green aggregate status can't stand in for them. Whether the unit suite is unaffected by the configuration is not stated.
- Independent review is required: `EC-77` applies because the commit changes the payment path.
- Ada's self-review stays Worker evidence and can't count as that review.
- `RR-9` is the review, but it is invalidated on r42 (see Drift locks).
- `WR-31` as a work result stands, but it is not a basis for `accept` now.

## Finding F-1

- **Severity: high.** Hana (Reviewer) sets it. It is evaluation evidence.
- **Priority: P2.** I (Omar, Executive) assign it. Reason: the flag is off in the release configuration, so 1.2 users are not exposed. The repair is low in complexity and regression risk, and it must land before anyone turns `autofill_v2` on.
- **Frame result: `falsified`.** Hana sets it, for the claim "meets R-C1 to R-C6 including the address step" on r41 with the flag both on and off. The counterexample is R-C4 with the flag on. This result is invalidated by `RR-9`'s own condition, so I keep it as the original ruling and don't rely on it for r42.
  - Whether F-1 survives is a separate question. The finding concerns session storage on the address path and looks independent of the payment timeout, but the facts don't demonstrate that. I treat it as unestablished for r42 until the review is re-run or the Reviewer confirms it.
- **Current-boundary effect: no block (provisional).** I set it, using Jules's cutoff, on the finding as it stood at r41.
  - Severity is high, not critical, and the path (saved-address autofill under `autofill_v2`) is outside the 1.2 mandate. The cutoff does not make that finding blocking, and it is recorded as a residual with an owner.
  - The residual's owner is not named in the facts. Jules assigns it.
  - Not excluded: whether other session keys persist. If a card number were persisted outside the payment provider, that would be a hard stop, which priority cannot waive. Nothing in the facts says one is, but the storage-dump test would settle it. I keep this open and explicit.

## Disposition

**No disposition can be applied now.**
- The basis lock failed, and the drift locks must hold before disposition. The coverage lock also failed.
- `accept` needs the candidate to close its cone with the required independent review. There is no applicable closed review on r42.
- `local_repair` and `reject` would rest on `RR-9`, which cannot be consumed as-is.
- `re_enter` doesn't fit. Its condition is a change to the outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design. A configuration revision on its own is none of these. Whether r42 is intended for release is Priya's call as configuration authority, not mine.

**Next action:** I activate an independent Reviewer against the exact candidate `4be19f02` / `b-77` with `checkout.yaml` r42. The claim is the 1.2 guest-checkout requirements. It must cover the card-payment step with the 4 s timeout and retry handling, plus the address step with `autofill_v2` on and off. It includes a storage-dump test for the open F-1 and hard-stop question. In the same step I also:
- ask Ada's Worker lane for no change: I mutate nothing and issue no repair;
- ask for the r42 re-run of `UA-5`, `E2E-3`, `INT-8` and the unit suite as part of the Worker's transition evidence, if current authority already permits reactivating that work;
- keep F-1 open as a residual awaiting an owner from Jules.

I then redo the drift locks and dispose from the new results. Whether a Reviewer activation falls within Omar's stated grant is an open point: the grant lists only the four dispositions. I rely on the Executive's activation duty and on `EC-77`.

## No method source

- The core value for a failed coverage-and-return lock. The method says only that an unresolved conflict or gap prevents a `satisfied` conjunction.
- The Product-owned declared conjunction rule: which non-satisfied value to report, and which results are mandatory.
- The owner of an accepted residual (the cutoff says "with an owner"). The task doesn't name one.
- Whether Omar's grant, which lists dispositions only, covers activating the Reviewer.
- Facts for the Product-role lock (identities and Install bindings).
- Whether a configuration change alone is a "material change" to F-1's independent surviving claim. The method requires "demonstrably independent surviving results" but gives no test.
- The meaning of P2 on the priority scale beyond "P0 act now, P3 backlog".
