# Task contract: route consistency of FOUNDATIONS §3

Identity: urn:stdo-3:claude:contract:T-05:s3-routes. Owner: the T-05 case
owner (the Claude tenant author). This is the outer contract of the
construction that was interrupted; the resuming actor completes it. It is
fixture material, not a standard.

## Claim

- Subject: FOUNDATIONS §3 Commitments, the section
  `standards/FOUNDATIONS.md#3-commitments` of FOUNDATIONS at SHA-256
  `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22`;
  section bytes SHA-256
  `d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf`.
- Property: every rc.2 route cited in the section is consistent under the
  contract in `qualification/instruments/ROUTE_CARD.md` (SHA-256
  `068e5b360208029540a60f2f2abdc7ba59ac1a958e62f6418dad8622570b07b6`).
- Basis: the section, the card, and the installed rc.2 cut
  `stdo://releases/v2.5.1-rc.2/` (manifest
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`).
- Witness relation: one authenticated step-actor judgment per route,
  produced through `qualification/instruments/bounded_step.py` at cap
  24,000 bytes.
- Falsifier: any covered route judged falsified.

## Required obligations R

The 23 routes R01–R23 of the table in
[../T-03-04/OUTER_CONTRACT.md](../T-03-04/OUTER_CONTRACT.md), which binds
the same route set over a variant of this section; here the routes are
over the section proper.

## Admitted coverage C

As in that contract, with the tenant block being this section: a judgment
counts when its step's `measured` entry carries the section's SHA-256 and
the card's SHA-256, its `actor_ended` entry logs an `output_sha256` equal
to the current digest of `steps/<step>.out.md`, and the file carries the
route's `ROUTE` line. A step with `actor_started` and no `actor_ended` has
produced no admissible judgment: its external effect (an API call that
may have completed and been billed) is unknown until reconciled.

## Composite rule

The declared conjunction over R: satisfied only when every route is
covered and every covered judgment is satisfied; otherwise falsified if
any covered judgment is falsified; else invalid_basis if any; else
out_of_frame if any covered judgment is out_of_frame or any route is
uncovered and the step cannot produce coverage within its grant; else
indeterminate. The record carries every covered judgment line unchanged,
R minus C with reasons, and the reconciliation of every uncertain step.
