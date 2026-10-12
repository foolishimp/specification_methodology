# TASK D: dispose a Worker result and a Reviewer result as Executive

## Subject

Product `shopfront`: an online shop. You act as the Executive, Omar, in
the coordinated branch. The facts below are the whole subject; the record
is invented for this task and is evidence about no real product.

Mandate: release `1.2` (owner Jules, product owner) delivers guest checkout
with card payment. Saved-address autofill is not part of the 1.2 mandate;
it ships behind the flag `autofill_v2`, which is off in the release
configuration.

Product-owned project reference-frame basis (owner Jules):

- severity scale: critical, high, medium, low;
- priority scale: P0 (act now) to P3 (backlog);
- decision cutoff: a finding blocks the current promotion boundary only if
  its severity is critical on a path in the release mandate, or it
  violates a hard stop; findings of severity high or lower on paths outside
  the release mandate do not block and are recorded as residuals with an
  owner;
- hard stop: a card number persisted anywhere outside the payment provider.

Omar's grant: dispositions `accept`, `local_repair`, `re_enter` and
`reject` over 1.2 release candidates. The admitted work contract `EC-77`
requires independent review of any change on the payment path.

Basis at activation: build `b-77` (commit `4be19f02`), configuration
`checkout.yaml` revision r41.

Worker result `WR-31` (Worker Ada, 2026-10-11T17:00Z): `candidate_ready`;
candidate commit `4be19f02`, build `b-77`; transition evidence: user
acceptance `UA-5` (guest checkout outcome) green, end to end `E2E-3`
(checkout path from cart to confirmation) green, integration `INT-8`
(payment-provider seam) green and the unit suite green, all on `b-77` with
r41. Self-review attached.

Reviewer result `RR-9` (Reviewer Hana, independent of Ada, 2026-10-12T08:00Z):
claim "guest checkout on `b-77` with r41 meets requirements R-C1 to R-C6,
including the address step"; population: the 1.2 guest checkout flows,
with `autofill_v2` both on and off; core result `falsified`; one finding:

- F-1: with `autofill_v2` on, a second guest in the same browser session
  sees the previous guest's address prefilled, against R-C4 ("a guest's
  data is never shown to another guest"); severity high; causal
  assessment: a session-storage key is not cleared on order completion,
  confidence medium; blast radius: guests sharing one browser while
  `autofill_v2` is on; workaround: keep `autofill_v2` off; repair
  complexity low, regression risk low; residual uncertainty: whether other
  session keys persist, reducible by a storage-dump test.

`RR-9` names as its invalidation conditions any change to `b-77` or to
`checkout.yaml`.

Change after the review: at 2026-10-12T09:30Z the operations lead Priya,
under her configuration authority, advanced `checkout.yaml` to r42, which
lowers the payment-provider timeout from 10 s to 4 s. Nothing else
changed. The current time is 2026-10-12T10:00Z.

## Instruction

1. Under a heading `Drift locks`, give each of the five locks as holds,
   fails or cannot be determined, with the fact that decides it, and for
   each failed lock the result it yields.
2. Under a heading `Work result`, give your evaluation of `WR-31` at step 4.
3. Under a heading `Finding F-1`, give its severity, priority, frame result
   and current-boundary effect, saying who sets each; assign the priority
   yourself with a one-sentence reason.
4. Under a heading `Disposition`, apply exactly one disposition, or say why
   none can be applied now, and name the next action you take within your
   grant.
5. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
