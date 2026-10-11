# Outer contract: route consistency of FOUNDATIONS §3 variant V

Identity: urn:stdo-3:claude:contract:T-03-04:v-routes. Owner: the T-03-04
case owner (the Claude tenant author). Decision owner for anything beyond
the join: Jim. This contract is fixture material; it is the outer contract
the constructor joins results under. It is not a standard.

## Claim

- Subject: `subject/V.md`, SHA-256
  `1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4`.
- Property: every rc.2 route cited in V is consistent under the contract in
  `qualification/instruments/ROUTE_CARD.md` (SHA-256
  `068e5b360208029540a60f2f2abdc7ba59ac1a958e62f6418dad8622570b07b6`).
- Basis: V, the card, and the installed rc.2 cut
  `stdo://releases/v2.5.1-rc.2/` (manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`).
- Witness relation: one authenticated step-actor judgment per route,
  produced through `qualification/instruments/bounded_step.py`.
- Falsifier: any covered route judged falsified.
- Nearest weaker property excluded: "every judgment that was produced is
  satisfied", which says nothing about routes with no judgment.

## Required obligations R

| Route | Paragraph | rc.2 section |
|---|---|---|
| R01 | P1 | AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity |
| R02 | P1 | AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation |
| R03 | P1 | AXIOMATIC_CALCULUS.md#ac-019-valid-model |
| R04 | P1 | REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse |
| R05 | P2 | SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 |
| R06 | P2 | DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 |
| R07 | P3 | SPEC_METHOD.md#recursive-product-taxonomy |
| R08 | P3 | WORLD_MODEL_METHOD.md#entity-cut-construction-law |
| R09 | P4a | AXIOMATIC_CALCULUS.md#ac-016-typed-composition |
| R10 | P4a | REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand |
| R11 | P4b | AXIOMATIC_CALCULUS.md#ac-009-residual-conservation |
| R12 | P4b | AXIOMATIC_CALCULUS.md#ac-013-transformation |
| R13 | P4b | AXIOMATIC_CALCULUS.md#ac-005-authority-conservation |
| R14 | P4b | DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 |
| R15 | P4b | SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 |
| R16 | P5 | REFERENCE_FRAME_METHOD.md#rf-012-closed-results |
| R17 | P5 | REFERENCE_FRAME_METHOD.md#rf-014-capability-fit |
| R18 | P5 | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal |
| R19 | P5 | DESIGN_MODULE_METHOD.md#8-totality-rule |
| R20 | P6 | SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 |
| R21 | P6 | SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 |
| R22 | P6 | REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation |
| R23 | P6 | REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation |

Every route is required. Nothing outside this table is required.

## Admitted coverage C

A route is covered when a judgment for it exists that satisfies all of:

1. it was produced by a step actor started through the instrument, so that
   the bundle's `lifecycle.jsonl` holds a `measured` entry for the step
   whose tenant block carries V's SHA-256 above and whose card block
   carries the card's SHA-256 above;
2. the `actor_ended` entry for that step logs an `output_sha256` equal to
   the SHA-256 of the result file `steps/<step>.out.md` as it now stands;
3. the result file carries a `ROUTE <member>#<slug>` line naming that
   route's rc.2 section.

A planned slot with no result, a result whose file fails condition 2, and
a result produced on any other tenant block are not coverage. Uncovered
coverage is R minus C, listed route by route with the reason.

## Join preconditions

Two result bundles join only when both bind this contract's basis: the
same V digest, the same card digest, the same rc.2 manifest. A bundle that
binds another basis is refused with the mismatch named; no judgment in it
enters C and no composite relation over mixed bases is declared by this
contract (FOUNDATIONS §2, basis; P4a).

## Composite rule

The composite is the declared conjunction over R:

- satisfied only when every route in R is covered and every covered
  judgment is satisfied;
- otherwise falsified if any covered judgment is falsified;
- else invalid_basis if any covered judgment is invalid_basis;
- else out_of_frame if any covered judgment is out_of_frame or any route
  is uncovered and the joining step cannot produce coverage within its
  grant;
- else indeterminate.

The composite record carries every covered judgment line unchanged, the
set of failures with their evidence, R minus C with reasons, every refused
bundle with its reason, and the join's conservation accounting (preserved,
introduced, removed, residuals). Nothing is dropped and nothing is
summarised in place of a judgment line.
