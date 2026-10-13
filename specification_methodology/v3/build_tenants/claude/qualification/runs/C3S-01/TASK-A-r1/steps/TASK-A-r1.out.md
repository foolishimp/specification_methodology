# Part 1: Frame declaration

```markdown
# Frame: F-E1-ledger-export-trailer-count (revision r1)

## Evaluation Family
Predicate for E1: on build `b-120`, the trailer count equals the source table's row count at export time (requirement R-3).
Closed result algebra: the five core values (`satisfied`, `falsified`, `indeterminate`, `out_of_frame`, `invalid_basis`), with no refinement.
E2 and E3 are separate evaluations. They are not part of this family and are not decided here.

## Subject And Basis
- Workspace: `W-ledger-export`, service `ledger-export`, file `exporter.py`.
- Source commit `c0ffee12`, with `exporter.py` SHA-256 `5f1a…9c2e`. Only the abbreviated hash is given, so the full hash is missing.
- Build `b-120` is the evaluated build (commit `c0ffee12`). Build `b-118` (commit `b7a1d3e0`) is a different build.
- Configuration: `export.yaml` revision 14.
- Database: production table `ledger_rows`, read from a read replica since 2026-10-09 (lag up to 30 s).
- Time of claim: 2026-10-11T16:00Z.
- Missing: the diff between `b7a1d3e0` and `c0ffee12`, and the replica identity and its isolation or snapshot settings.

## Material Manifold
- R-3, the trailer line, the exported row count and the source row count.
- D-3: read transaction, then streaming of rows, then a separate `SELECT COUNT(*)`, then the trailer write.
- The data source (primary versus replica) and replica lag, which determine which table state the count is taken from.
- Relations between build, commit and configuration, and between evidence and build.
- Missing: the transaction isolation level, which source the count query hits, and whether rows are written and counted from the same snapshot.

## Coordinates And Equality
- Build, commit, file hash, configuration revision and time coordinate are each compared by exact identity.
- Equal service name, file name or "the tests pass" does not equate `b-118` with `b-120`.
- Missing: a declared equality law for "row count at export time", that is, which clock and which database state the time refers to.

## Invariants
- R-3 as worded.
- Results bind exact subject and basis (RF-005).
- No result is raised in standing by refinement.
- Frame selection grants no authority.

## Authorities
- Semantic: Mara, who owns the meaning of R-3.
- Release decision: Mara.
- Changes to `exporter.py` and `export.yaml`: Deon (operation authority, not material here because E1 is read-only and the frame declares no operation authority).
- Database configuration: Priya.
- Frame-set authority: not stated.
- Evaluation authority: no role is named in the subject for performing E1.

## Evidence
Admissible, by provenance and subject:
- V1: CI run 4471 on `b-118`, 2026-10-08. It binds a different build and a 25-row fixture, with no replica.
- V2: OPS-391, an export on 2026-10-10. The build is not stated, and no source count was recorded.
- V3: CHG-2026-1009, replica move and lag.

Evidence about `b-120`'s own behavior is missing.

## Capability Envelope
Missing. The subject names no actor, tools, access or independence conditions. Read-only inspection of the listed evidence is assumed.

## Boundary And Exclusions
- Excluded: whether the product should ship, and any change to `exporter.py` or the database.
- Prohibited: treating V1's `b-118` results as `b-120` results without a declared relation, and treating the trailer value as the true count without a recorded source count.
- Out of frame: the exact meaning of "at export time" under replica lag, because it is not defined in R-3.

## Optional Frame Relations
Consumer: claim K (Mara). E2 and E3 are complementary evaluations. No result from them is consumed here.

## Invalidation And Recharting
- A new build or commit.
- A configuration revision change from 14.
- A change in the replica, its lag or the isolation level.
- A change to the meaning of R-3.
- New evidence on `b-120`.
- Any topology change (source primary versus replica).

## Qualification
- Representative cases, counterexamples and qualification evidence: none on file.
- Known residuals: those listed in the sections above.
```

# Part 2: Activation and evaluation result

Activation outcome for the predicate "the frame is activated for E1, subject, basis and actor": `activated_frame` (`satisfied`). The subject and basis are exact (commit `c0ffee12`, `b-120`, `export.yaml` rev 14, claim time).

Two things are not stated, and I do not invent them. The evaluation authority and the actor envelope are missing. The evaluation is read-only, so no operation authority is needed. This activation therefore holds only if the assigning authority admits the evaluator.

```markdown
# Frame Evaluation Result

- frame identity and revision: F-E1-ledger-export-trailer-count, r1
- activation identity: ACT-E1-b-120-c0ffee12-cfg14-2026-10-11T16:00Z (my label; the subject names none)
- evaluation: E1, predicate "on `b-120`, the trailer count equals the source table's row count at export time"
- subject and basis: build `b-120`, commit `c0ffee12`, `exporter.py` SHA-256 `5f1a…9c2e`, `export.yaml` rev 14, production table `ledger_rows` read via replica (lag ≤ 30 s), time 2026-10-11T16:00Z
- actor and capability envelope: not stated in the subject
- semantic, evaluation, operation where material, and decision authority: semantic = Mara; evaluation = not stated; operation = none (read-only); decision = Mara (release decision)
- admissible evidence: V1, V2, V3 as limited in the frame's Evidence section; none is evidence about `b-120`'s production behavior
- result: indeterminate
- inference relation: V1 passes on `b-118` (commit `b7a1d3e0`) against a 25-row fixture. It does not bind `b-120`, the production table or the replica, so it does not decide E1. V2 shows only that a trailer of 1,204,311 existed on 2026-10-10. The build is not stated and no source count was recorded, so equality cannot be tested. V3 shows a replica lag of up to 30 s, which makes "source row count at export time" depend on which state is meant. D-3 is design intent, not observation of `b-120`. No counterexample is on file, so the result is not `falsified`. Nothing on file establishes the predicate on this basis, so it is not `satisfied`. The evidence available cannot decide, so the result is `indeterminate`. Evidence that would decide: a recorded run of `b-120` on the production table (or a faithful replica) with the trailer and a source count taken at the same defined moment, plus the isolation or snapshot setting.
- residual uncertainty: the diff from `b7a1d3e0` to `c0ffee12` is unknown; the build behind V2 is unknown; the replica isolation or snapshot behavior and the source of the count query are unknown; whether rows and count share one snapshot is unknown; the actor and evaluation authority are unstated
- out_of_frame residual (missing relation or capability, owner, reconfiguration pressure): `out_of_frame` also has a lawful ground here. "Row count at export time" is undefined under replica lag (owner: Mara, semantic authority; replica configuration: Priya). It is a term the frame leaves undefined, hence an undeclared material relation. I return `indeterminate` on the evidence ground. If Mara defines the term, the frame would be revised (reconfiguration pressure).
- invalidation conditions: those in the frame's Invalidation And Recharting section
- consuming decision or conjunction: claim K (Mara's release decision). No conjunction rule has been declared, and E2 and E3 have no results here.
```

# Claim K

My result is `indeterminate` for E1 only. It does not establish that R-3 is satisfied on `b-120`, and it does not falsify it. It says nothing about "ready to ship", which is a separate acceptance predicate, and E2 and E3 have no results here. Mara disposes claim K (she owns R-3's meaning and the release decision); my result is evidence for her and is not a disposition.

# No method source

- The `activate` refusal causes do not say whether an unstated evaluation authority or actor envelope should refuse activation or leave it standing with a recorded residual. I recorded it as a residual.
- The METHOD block gives no rule for choosing between `indeterminate` and `out_of_frame` when both have a lawful ground. It requires only that the result name the value and the ground. The choice of `indeterminate` is mine.
- The METHOD block gives no format for the activation identity, and it does not say what counts as a decisive test for E1. The decisive evidence I named comes from the task's facts.
- The METHOD block does not say how to judge whether `b-118` evidence transfers to `b-120`. I treated it as not applicable because no relation is declared.
