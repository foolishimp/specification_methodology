# Human Decision: Authorize STDO 2.5.0 RC2 Publication

## Authority And Instruction

- authority: direct human Product authority;
- received: 2026-09-01 through the active working session;
- instruction: release STDO 2.5.0 RC2 when the authorized tuning and
  qualification are complete;
- scope: Specification Methodology STDO `2.5.0` RC2 publication only; and
- recorder: Codex.

## Conditional Grant

The instruction authorizes publication only when all of the following are true:

1. the exact 52-member standards subject and protected inputs reproduce the
   current release record;
2. T-022 closes on an exact semantic Reviewer result;
3. one independent whole-cut review returns no P0, P1, or P2 blocker;
4. the qualified RC tag, selector, RC branch, release branch, and carrier commit
   can be pushed atomically without moving any historical RC1 ref; and
5. remote reacquisition verifies the tag object, peel, trees, inventory, and
   installed manifest.

The qualifying standards aggregate selected by this grant is:

`a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7`.

Closure-only comments, tickets, and release bookkeeping may advance the carrier
commit without changing that Product subject. Any change to a standards member,
protected input, release record, or qualified toolchain byte invalidates this
grant for RC2 and requires fresh qualification.

## Boundary

This decision authorizes the publication operation. It does not accept RC2 as
the final STDO Product, adopt it for a consumer, or authorize an STDO
Representation release. Those remain separate decisions over their own exact
subjects.
