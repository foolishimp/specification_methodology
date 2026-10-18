Historical: this set binds earlier member bytes and is not current; the current interpretation is [../i3/](../i3/README.md).

# T2 a_c Interpretation (Claude tenant)

Status: the T2 document increment is frozen and encoded; the program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject; two frames are projected. No author-independent fidelity
judgment of this version exists. Lineage: the T1.2 program
([t1/](../t1/README.md), canonical `c3f482ab…8d49`) is contained unchanged
in clause content except where the T2 text repaired CALCULUS §4–7; the T1.2
rows are carried, the T2 rows added. Actual-use evidence is the T-03-04
case, recorded in
[qualification/cases/T-03-04/](../../qualification/cases/T-03-04/CASE.md).
Nothing here is the released STDO Representation, and nothing here is
accepted.

## Frozen subject

T2 on `tenant/claude/c3`, identified by digest. The increment adds
CALCULUS §4–7 and SPEC_METHOD §1–7 to the T1.2 scope (FOUNDATIONS,
CALCULUS §1–3, EVALUATION §1–4). FOUNDATIONS and EVALUATION are byte
identical to T1.2; CALCULUS §1–3 is byte identical to T1.2 (8,056 bytes up
to the §4 heading); SPEC_METHOD is wholly new to the encoding.

| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` |
| `standards/SPEC_METHOD.md` | `c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4` |

The validation report's resolved sources carry exactly these digests.

Changes to CALCULUS §4–7 and SPEC_METHOD before this freeze, each traced
to the author's pre-freeze route check (29 routes judged by fresh step
actors through `qualification/instruments/bounded_step.py` with
`ROUTE_CARD.md`; first pass 19 satisfied, 3 out_of_frame, 2 indeterminate
and five wording residuals; second pass 28 satisfied, 1 indeterminate;
third pass on §4 all satisfied; logs retained in the author's scratch
space, not in the repository): UP-021 restated as the complete transition
within its enclosing relation; graph functions attributed to ODD without
the tenant's "graph profile" term; CALCULUS §5 names resumption (re-entry
over current work state) and restart (reconstruction from less) as rc.2
does, and marks the generic work-state object, reconciliation of uncertain
effects and non-idempotence as new; the allowance rule in §6 marked new;
§7 attributes the basis invalidator to judgment continuity; SPEC_METHOD §3
carries UP-013's "by itself" and the assurance carve-out; §4 cites
Universal Intake Triage, conserves the TICKET core model's carrier
selection by lifetime and reframes only its default; §5 attributes the
non-widening rule to UP-020, conserves the baseline role labels by
reference and reframes Steel-Thread Delivery as a heuristic; §6 carries
UP-015's two qualifiers, cites RELEASE_METHOD's release identities, phases,
naming and cohorts, and restates AC-020 in its own terms. The author's
check is construction output under EVALUATION §3, not assessment.

## Mechanical subject

As in [t1/](../t1/README.md): the pinned tag `refs/tags/axiom_indexer/v2.5.1-rc.2`
(commit `9a9c4797…`), its seven Product members byte-verified against the
release record, executable copied to scratch for invocation; no Axiom
Indexer Install selected. Jim owns selection and acceptance of this
dependency's use within STDO 3; until then every mechanical result below
is candidate evidence bound to the byte-verified tagged subject.

## Artifacts

| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `bbc624e20bf3e16978de8a68619edc4b4f4287528af37cc33ea0d542ee1f5524` | the authored a_c.text program; canonical program digest `sha256:13338baadf3129c72da0353983d9a2f862b8777b77b68f4c8edc35dab8c57f8b` |
| `logical-constraint-map.json` | `f5f774d16550a3ab347df803bf45af6b1d51c125b33382a4a6853f30725ba20e` | deterministic index over the program; intrinsic digest `sha256:0ef98f4f6156274cc70f40c12b15e7c2d4a84a78a7ab146725c5864d9714aeda` |
| `validation-report.json` | `e718e22104a09fce57f49bca5b230b577645e99341a9fd16ff871121f88ea7bb` | zero diagnostics; 108 symbols, 135 clauses, 6 residuals; 36 resolved sources |
| `projection-bounded-activation-materialized.json` | `5d26de0492bd487fa1861277d713f556bbae98a24c5777dd57d36a49f8190008` | the T-01 frame over this program: 42 symbols, 35 clauses, 4 residuals in closure; projection digest `sha256:97f8ede0…f7af` |
| `projection-bounded-activation-reference-only.json` | `6059248c5e99625675c21336f28faff45515331598f6cd53bcd2de5f0b4eca5d` | the same frame, reference-only |
| `projection-composition-conservation-materialized.json` | `3a0a1cdb91184f12f1f0da31537da0f193aabbe40d267aa966d6e54179bcc231` | the T-03-04 frame: 51 symbols, 46 clauses, 2 residuals in closure; projection digest `sha256:d9b87c21…3653` |
| `projection-composition-conservation-reference-only.json` | `bb5cfd36f4c45b5eefc6f0a873281d8067b728e968002ee988c532c7693455c4` | the same frame, reference-only |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | invocation-local, as in t1 |

Program identity `urn:stdo-3:claude:program:a-c-text:t2`; source basis
`stdo-3://build_tenants/claude/standards/`; calculus
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; frame refs
CALCULUS §2 and CALCULUS §4.

## Source-to-model dispositions

Vocabulary unchanged from T1.2 (seven kinds, six operators, nine roles).

Added as symbols (33): CALCULUS §4 outer contract, refinement, the named
dispositions, condition class, hard stop, seam; §5 work state, resumption,
preservation checkpoint, restart, progress, churn; §6 proportionality,
cost category; §7 closed result, invalidator, applicability check;
SPEC_METHOD chain, layer, major ambiguity, shared WHAT, tenant HOW, work
wave, change class, triage, migration, carrier, executive relation,
checkpoint, steel thread, product role, successor, predecessor claim
disposition.

Added as clauses (49): CALCULUS §4 (ten: dispositions named in advance,
no omniscience, ambiguity handling, hard stops, faithful refinement,
premises not conclusions, coupled relations fit together, seam far side,
one-commit admission, generalisation of graph functions); §5 (five: work
state tuple, resumption, non-idempotence, restart must be argued,
progress against churn); §6 (six: proportionality, method execution
proportionate, spend reported with source, cost categories, report volume,
no universal quota); §7 (three); SPEC_METHOD §1 (four), §2 (three), §3
(four), §4 (five, including the class-to-re-entry mapping), §5 (four), §6
(four), §7 (one). Standings that the documents mark as reframed or new are
carried in clause qualifications (steel thread reframed; resumption,
non-idempotence, the allowance rule and the work-state object new;
carrier default reframed).

Frame index `composition-conservation` (CALCULUS §4 with FOUNDATIONS §4):
29 clauses selected for the T-03-04 case, one residual.

Not encoded: the source-dispositions tables (rc.2 outside the basis);
EVALUATION §5–8, CONFORMANCE and PROFILES (residual
`t2-boundary-forward-references`); the Product Definition imported by
SPEC_METHOD §7 (residual `product-definition-import-outside-basis`).

Residuals (six): the two above plus the four carried from T1.2 (fit test
on attention, time and capability; independence arguments of one
sentence; formal fragment carried not constructed; rc.2 routes outside the
program basis).

## What validation proves

Structure, URI resolution, reference closure, grounding and the canonical
digest. It does not prove that the clauses are faithful to the documents,
complete, or uniquely interpreted. That judgment is author-independent and
source-first; none has been made of this version.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in bounded-activation composition-conservation; do
  python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
    --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
    --mode materialized --output projection-$FI-materialized.json
done
```
