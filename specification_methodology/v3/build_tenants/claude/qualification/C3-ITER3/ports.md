# Named Port Accounting, Iteration 3

Activation I3-4c under `EC-CLAUDE-I3-01`, run by the Executive in the main
session. It accounts for the six named ports of
[CROSS_SYNTHESIS](../../design/CROSS_SYNTHESIS.md#port-list). The exact
source of each port is the Codex path and lines recorded there, read at
commit `31f28f90c4a9b15243d84630fc4799024a9cd7ac`. No peer source was
opened for this accounting: the contract selects no new peer inspection,
and comparison of the ported text with the peer source waits for the
product owner's ported-part review policy. Every statement below is
about this candidate's own files.

A port is a named contribution, not a predecessor claim. It has no
disposition of its own under RELEASE §9. It enters the frontier only as
part of the restatement of the member that receives it, so the rows of
that member's cone carry it.

| # | Part | Receiving owner, checked to exist at the current commit | Frontier cone | Frontier rows that carry it | State in this iteration |
|---|---|---|---|---|---|
| 1 | Specialization table with premise standing | FOUNDATIONS §3 `Foundation to law` (format, standing, family index, Pillar column added in step 1) | FOUNDATIONS | the FOUNDATIONS rows for the commitments and the foundation-to-law relation; every member's `Position` row that says its family table is new | extended: the Pillar column (step 1) and real arguments in every family table (step 2). The format stays one owner |
| 2 | Premise standing discipline | FOUNDATIONS §3 Commitments (the standing column) | FOUNDATIONS | as part 1 | unchanged |
| 3 | Reference-only import declarations | REFERENCE_FRAME §1 `Imports into this context`, under the import rule of FOUNDATIONS §2 Imports between members | REFERENCE_FRAME | row 295 (RF `#position`: "the context also holds the concepts other members define, by reference-only import") | unchanged; PRODUCT_DEFINITION §5 reads its relation kinds in the owner's terms (R21) |
| 4 | Equivalence ladder | EVALUATION §6 Conformance of realisations, `Equivalence ladder` | EVALUATION | the EVALUATION rows of the reference-frame and design conformance claims (EVALUATION §6 source dispositions) | F7 table rewritten with derivations (I3-3j); ladder text unchanged |
| 5 | Verbatim digest-bound frames and direct acquisition of deciding owners | ACTIVATION §2 `Acquisition`; the frame generator `qualification/instruments/generate_frames.py` | ACTIVATION (acquisition rule only); the generator and frames are instruments and derived surfaces, in no cone | the ACTIVATION rows that dispose the rc.2 acquisition and staleness rows | extended: Acquisition now names a constraint surface of a current `a_c` interpretation as a derived surface (I3-2r, pillar 10); frames are regenerated at the freeze |
| 6 | Finite check with mutant counterexamples | `qualification/instruments/finite_oracle/`, an instrument | none | none | re-reviewed and re-declared against the changed sections; `--check` exits 0 (I3-3i) |

## Conflicts between records

- CROSS_SYNTHESIS says part 3 replaced REFERENCE_FRAME §1's "Statement of
  ownership" paragraph. The rule it follows is now owned by FOUNDATIONS §2
  Imports between members, and REFERENCE_FRAME §1 applies it. The two
  records agree; CROSS_SYNTHESIS predates the FOUNDATIONS owner and does
  not name it.
- CROSS_SYNTHESIS lists five parts with a frontier cone and none for part
  6. The frontier holds no row naming a port. This agrees: a port is
  carried by the receiving member's rows, not by a row of its own.
- No port has two owners, and no port is carried by two cones.

## What this accounting does not establish

It does not establish that the ported text is faithful to its Codex
source, that the port is needed, or that the receiving owner's text is
correct. Those need the ported-part review the product owner has not yet
selected, and a cross-family review.
