# RETURN (draft, in progress) — FOUNDATIONS §3 route check

Run: s3-routes, cap 24,000 bytes per step, instrument bounded_step.py with
ROUTE_CARD.md. Started 2026-10-11T14:50:12Z.

## Intake

- Outcome served: the task contract `TASK_CONTRACT.md` (route consistency
  of FOUNDATIONS §3, 23 routes).
- Affected set: the 23 routes R01–R23 over the section
  `standards/FOUNDATIONS.md#3-commitments`.
- Basis: FOUNDATIONS `2f15c6c1…38a22`; section bytes `d654d395…feaf`;
  card `068e5b36…07b6`; rc.2 manifest `3d860ff4…2782`.
- Grant: measure and start step actors through the instrument; write this
  record. Nothing else changes.
- Re-entry: any falsified route re-enters at the FOUNDATIONS author.

## Closure and partition

Single step over the whole section with all 23 routes would exceed the
cap (not measured; partitioned by paragraph from the start). Partition:
P1 (R01–R04), P2 (R05–R06), P3 (R07–R08), P4a (R09–R10), P4b (R11–R15),
P5 (R16–R19), P6 (R20–R23).

## Steps

| Step | Routes | Measured | Fit | Status |
|---|---|---|---|---|
| P1 | R01–R04 | 10,946 | fits | done, 4 satisfied |
| P2 | R05–R06 | 13,744 | fits | done, 2 satisfied |
| P3 | R07–R08 | 15,217 | fits | done, 2 satisfied |
| P4a | R09–R10 | 9,813 | fits | done, 2 satisfied |
| P4b | R11–R15 | 25,147 | over cap | refused; split |
| P4b-1 | R11–R13 | 15,953 | fits | done, 3 satisfied |
| P4b-2 | R14–R15 | 17,737 | fits | done, 2 satisfied |
| P5 | R16–R19 | — | — | next |
| P6 | R20–R23 | — | — | next |

Composite so far: satisfied, 15 of 23 routes; no failures.

## Remaining

Run P5 and P6, then compute the composite and write the handoff.
