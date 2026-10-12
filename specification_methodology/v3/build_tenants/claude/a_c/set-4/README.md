# a_c interpretation of the thirteen-member set (Claude tenant, set-4)

Status: the successor of [set-3/](../set-3/README.md), derived over the
standards at commit `978d324` on `tenant/claude/c3-v3-evA` by the W13
Writer activation. It is a partial encoding. It adds what the four F-02 task
frames need from AXIOMATIC_CALCULUS, SPEC_METHOD (restated), TICKETS,
EXECUTIVE_BASELINE and ASSURANCE, re-anchors the set-3 rows whose anchors
the restatements moved, and encodes nothing of PRODUCT_DEFINITION. The program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer subject. Four frames are projected, each under the Executive's
100,000-byte limit. No author-independent fidelity judgment of this program
exists, nothing here is accepted, and set-3/ is frozen history that this
derivation did not edit.

## Frozen subject

The thirteen files under `standards/` at `978d324`, identified by digest.
`git status --porcelain -- standards/` was empty at derivation time.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `29531acfaa5d2ac76568ce892d2fca002cf90acc358c68190f95a359230e6b66` |
| `standards/REFERENCE_FRAME.md` | `a3d0bfaa2afbaaafa04d3fae59fb84e71dfdb730b1bdbcf29663b71e4072454c` |
| `standards/ACTIVATION.md` | `657a135ec6c6b5563e1bb7de492440ab1475f3ddbcd13779c20b123fdfa810ef` |
| `standards/AXIOMATIC_CALCULUS.md` | `d1c78a63010c6478e82384f44e6ecc4a18d0ce0f3937226f9c290f3472d54f75` |
| `standards/EVALUATION.md` | `c8e55de7549f59df40468a8e2dd10c87498029448fd439344d3ca26132919e24` |
| `standards/SPEC_METHOD.md` | `5baf6cfc0cc1afcbaffd184cc64d2cbf6d23f567d9cebaef5efb71f491aefad1` |
| `standards/PRODUCT_DEFINITION.md` | `32fa515047fec42da5fca3f0c2db15259de71804614ff0d170bc988f59e97cb7` |
| `standards/ASSURANCE.md` | `a641394a4163579f23cfb5060b82b3daa5d7e6da86b295f5019116849ed1154c` |
| `standards/TICKETS.md` | `648083c9c6dcdbf7a5797d50f891f960abe32e84649ff3bb4332f821a7d74893` |
| `standards/CONFORMANCE.md` | `be1b88f98e24f3d9c655948191f5cd87d28e7941f0a4bb8028010004eef1dd05` |
| `standards/PROFILES.md` | `3cf9498adb4e26416ad9bb613fac7dc490ba37c1170ce60208b86fdae8bc22d0` |
| `standards/EXECUTIVE_BASELINE.md` | `b0bae9ebd7b10f225799a9370106c7934a6d40732fd0348271628903f8af7426` |
| `standards/README.md` | `e01a658559659d4eb33e4f7fb2d93b862f6b6a4df5e52a895928dc378818a071` |
<!-- /subject -->

CONFORMANCE.md and PROFILES.md are byte-identical to set-3's subject.
FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, EVALUATION, SPEC_METHOD and
README changed between `ac3ec5f` and `978d324`, and the other five are new
members. The validation report records 146 resolved sources: every tenant
source carries one of the digests above, and the one rc.2 source is the
calculus.

## Mechanical subject

The mechanical subject is the same as set-3's: tag `refs/tags/axiom_indexer/v2.5.1-rc.2` (tag object
`9bff233c…`, commit `9a9c4797…`). For this run
`build_tenants/core/code/ac.py` was read from that tag with `git show`. Its
SHA-256, `5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`,
was compared with the release record `axiom_indexer/releases/v2.5.1.md` at
the same tag and matched. The executable was invoked from a scratch copy with
`python3 -I`. No Axiom Indexer Install was selected. Every mechanical result
is candidate evidence bound to the byte-verified tagged subject.

`calculus_ref` stays `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`,
as in set-3. The tenant's AXIOMATIC_CALCULUS member is now part of the
encoded subject: its clauses are encoded as program content under the
`stdo-3://` basis. The program is still written in, and validated against,
the rc.2 calculus. Moving `calculus_ref` to the tenant member would change
the recipe, and that decision is not this Writer's to make.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `8c7984e8fcad67480f232f85ac8823e97266ecc1069f9cebefa0ffec9a18b74b` | the authored a_c.text program `urn:stdo-3:claude:program:a-c-text:set-4`; canonical program digest `sha256:16f840cb501b0df497d7a7747142e756108d031e6c0db2fbd8d3f69003325025` |
| `logical-constraint-map.json` | `3f77d7f745786317ec5f07910b8408c8aa21488b31a7316428564cec8f163bcf` | deterministic index over the program; intrinsic digest `sha256:7e14668bb7e08c8349bbb7cde96faa0df15616b57ae3776c7b6642488c8802a9` |
| `validation-report.json` | `7b86542f8f9ffc01d04ae7ebf0778e766dfbf7a4990286f468216a8c0e984a7b` | status `valid`, zero diagnostics; 236 symbols, 331 clauses, 7 residuals; 146 resolved sources |
| `projection-transformation-and-judgment-materialized.json` | `839dff0bba028508132270a61e8fad73f18e7824b01294fe85fdd3b945455ea6` | frame `transformation-and-judgment`, materialized; projection digest `sha256:5100f10c416b2bfcb6d8f4fa4bde805bf28c215b73b53e4227f2a26ba20522e3` |
| `projection-transformation-and-judgment-reference-only.json` | `d3183da29112cf8e6160a26f0e0ba1c8bfa638c6b18448dc6055224e26eb9f50` | the same frame, reference-only; `sha256:fb1a340ece545701cda9b9285e119c1e2a31cdf5ff99d8b632672a2a2f43a126` |
| `projection-triage-and-reentry-materialized.json` | `90336a8f9e269dc70bb128e41605b51141d6d438cf45b740f433d10c06685ac1` | frame `triage-and-reentry`, materialized; `sha256:eec09cd9ab699669c892dfd72cc3e4bd6ceb52c3d86999fef8fe0a65d4ced273` |
| `projection-triage-and-reentry-reference-only.json` | `f9727fab7201604bd687296793d804120d606270f17c85bc35749ae4c8e01b3d` | the same frame, reference-only; `sha256:0cadb9d57d68c15c02d756b151b0d53d16e126be5bb0b9613c7e0da5398d1313` |
| `projection-carrier-and-admission-materialized.json` | `5ee0fb61ab65aa130d5950bdb974cfbff37f852f53de322e3bf9227c16fec163` | frame `carrier-and-admission`, materialized; `sha256:7d7f47cc72dbf4ee2d9396949ee9d2ce677050d0f14792dbc0c402d49b3f7133` |
| `projection-carrier-and-admission-reference-only.json` | `cc4867e0f2820bd1fc58131d1cb0583f4df2b07dc07809c8ae4aec27c770d433` | the same frame, reference-only; `sha256:55d2e04edd633adb48ccdc01915291d6e428bd914ff5a30595f1019048b701c2` |
| `projection-executive-disposition-materialized.json` | `b9b2f361b40ecbff80e59ac43755a9647acc0b4646759e8dfa5e3ddd6c562c75` | frame `executive-disposition`, materialized; `sha256:2ce52d38ea8417b402ffedd7cb58a0556c54e7dc402f353bd9ed66d876f1296f` |
| `projection-executive-disposition-reference-only.json` | `1c8bb57f4383b5d005b239655464201628b89c295ae517e9327129615cafb7a3` | the same frame, reference-only; `sha256:d5d2d0ff1cd1a5ac4c4d2a901d64b545cf4a83a6150dc55bbe9a932e4c3448ca` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | byte-identical to set-3's |
<!-- /artifacts -->

## Frames

Each frame was projected from one new frame index and measured with
`wc -c` after projection, before any actor read it. The limit is 100,000
bytes materialized. All four frames are under it, and the limit was met by
selecting clauses, not by truncating them. Each frame's clause list is the
projection's `closure.clauses`: the index roots plus the clauses that their
support references pull in transitively.

| Frame | Materialized bytes | SHA-256 (materialized file) | Reference-only bytes | Closure (symbols, clauses, residuals) | Under limit |
|---|---|---|---|---|---|
| `transformation-and-judgment` | 56,993 | `839dff0bba02…` | 29,680 | 16, 19, 0 | yes |
| `triage-and-reentry` | 68,182 | `90336a8f9e26…` | 36,269 | 16, 21, 0 | yes |
| `carrier-and-admission` | 67,504 | `5ee0fb61ab65…` | 35,467 | 20, 19, 3 | yes |
| `executive-disposition` | 93,412 | `b9b2f361b40e…` | 49,451 | 28, 24, 0 | yes |

`transformation-and-judgment` (frame ref AXIOMATIC_CALCULUS
`#ac-013-transformation`; F-02 task A). 19 clauses:
ac-005-copying-transfers-no-authority,
ac-008-difference-only-through-latitude-or-transformation,
ac-009-absence-from-projection-is-not-resolution,
ac-013-application-proposes-and-never-self-admits,
ac-013-closed-local-record-delta,
ac-013-coordinates-equal-or-restrict-the-traversal,
ac-013-external-resolution-delta-and-witnesses,
ac-013-model-identities-are-exact,
ac-013-preservation-relation-is-exact-typed-equality,
ac-013-preserved-identity-is-proven-equal,
ac-013-residuals-survive-unless-disposed,
ac-013-same-basis-or-separately-identified-migration,
ac-013-transformation-record-fields,
ac-014-judgment-never-transforms-its-subject, ac-014-judgment-record-fields,
latitude-record-is-explicit-and-bounded, residual-record-cannot-be-erased;
pulled in by support: latitude-must-be-declared,
transformation-records-accounting (FOUNDATIONS §4).

`triage-and-reentry` (frame ref SPEC_METHOD `#universal-intake-triage`;
F-02 task B). 21 clauses: universal-intake-has-one-front-door,
intake-triage-makes-six-determinations,
triage-triangulates-across-applicable-frames,
below-goals-re-entry-asserts-no-upstream-change,
c-j-o-annotations-separate-determinations,
computed-classification-identifies-its-production,
computed-result-exposes-four-things-in-order,
nonconformance-does-not-itself-change-the-contract,
unknown-treatment-withholds-dependent-reliance,
computed-classification-is-reused-after-applicability-check,
upward-check-consumes-the-computed-classification,
realization-refactor-requires-sufficient-governing-layers,
upward-walk-stops-at-first-missing-layer,
ticket-records-change-class-orthogonal-to-type-and-category,
triage-metadata-minimum-fields; the set-3 rows
substantive-change-starts-with-triage, change-classes-and-re-entry-points
(rewritten) and changed-relation-accepted-only-at-owner; pulled in by
support: changed-inputs-invalidate-before-reliance,
counterevidence-invalidates-dependents and authority-is-never-minted.

`carrier-and-admission` (frame ref TICKETS `#carrier-selection`; F-02 task
C). 19 clauses: execution-contract-is-the-run-scoped-admitted-surface,
execution-contract-loop-admits-before-execution,
carrier-selection-takes-the-first-matching-row,
ticket-shaped-creates-no-ticket,
absence-of-a-ticket-neither-requires-nor-authorises-one,
carrier-assertion-is-not-admission-evidence,
surviving-obligation-is-carried-when-admission-fails,
carrier-is-an-admission-candidate-never-truth,
admission-never-admits-a-growth-basis; the set-3 ACTIVATION §1 admission
rows drafting-and-admission-are-distinct,
drafting-actor-never-infers-admission,
execution-begins-only-after-admission,
admitted-result-identifies-mechanism-contract-decision-and-evidence and
admitted-contract-names-a-durable-result-surface; the set-3 SPEC_METHOD
carriers row carrier-is-selected-by-proportionality; pulled in by support:
proportionality-definition, no-universal-quota-follows,
obligation-without-route-is-unjustified and p2-statement. Three residuals
are carried in by the affected-subject rule. The set-4 conflict residual
contract-state-set-closed-or-minimum comes in through `contract-state` and
`execution-contract`. derivation-chain-cost-per-boundary and
independence-arguments-are-one-sentence come in through the proportionality
and principle symbols.

`executive-disposition` (frame ref EXECUTIVE_BASELINE
`#12-complete-engagement-transition`; F-02 task D). 24 clauses:
technical-triage-records-supportable-finding-fields,
severity-priority-result-and-boundary-effect-are-four-values,
boundary-effect-precedes-exactly-one-disposition,
work-result-variants-map-totally-to-core,
work-result-references-existing-classification,
exact-candidate-is-a-stabilised-subject-identity, executive-mutates-nothing,
five-drift-locks-before-activation-and-disposition,
failed-drift-lock-maps-to-its-result,
step-4-non-candidate-variants-are-not-progress,
step-4-candidate-ready-decides-independent-assessment,
step-5a-self-review-stays-worker-evidence,
step-5b-reviewer-activation-contents,
step-6-reviewer-returns-one-closed-evaluation-to-the-executive,
step-7-executive-disposes-exactly-once-and-checkpoints,
step-7-severity-neither-selects-priority-nor-blocks,
promotion-constraint-projection,
testing-frame-authority-is-bounded-by-the-claim,
product-testing-frame-set-assigns-claims-not-authority,
testing-evidence-stays-claim-bound,
dispositions-are-selected-by-their-conditions (ACTIVATION §3
Disposition); pulled in by support:
construction-availability-maps-to-core, disposition-consumes-a-core-result,
refinements-map-totally-to-core.

What the size limit kept out: `executive-disposition` does not carry
`result-algebra-has-five-members`. It closes over nine clauses, and with it
added to the index a scratch projection measured 118,120 bytes
materialized, over the limit. The core members
`satisfied`, `falsified`, `indeterminate`, `out_of_frame` and
`invalid_basis` reach the actor through the construction-availability
mapping, the drift-lock failure clause and the work-result clause, not
through the algebra's own definition. The frame carries the ACTIVATION §3
Disposition conditions but no ACTIVATION §5 checkpoint law beyond what
step 7 restates.

## Departures from the set-3 recipe

- Only the four new frame indexes are projected. The seven set-3 frame
  indexes remain in the program unchanged, but they were not
  re-projected: each would exceed the 100,000-byte limit, since their
  set-3 frames ran 144 to 272 KB. The set-3 recipe projected every index
  in one loop.
- The re-anchored rows and the new rows have sorted `source_refs` and
  `re_entry_refs`, because the pinned validator requires that order. set-3
  rows that were already sorted are unchanged.

## Changes between set-3 and set-4

Counts: symbols 209 to 236 (27 added), clauses 269 to 331 (62 added, one
rewritten in place), residuals 6 to 7 (one added, one detail rewritten),
frame indexes 7 to 11, frame refs 7 to 11. Nothing was retired.

### Re-anchored (stale anchors from the restatements)

Validating set-3's program unchanged against `978d324` gave 44
`unresolved_fragment` diagnostics over 41 records (22 clauses, 18 symbols,
one residual). Each moved anchor now points at the heading that holds the
restated text, located by grep. Only the anchors changed; the wording of
these rows was not re-derived against the restated text.

| Old anchor | New anchor(s) | Rows |
|---|---|---|
| ACTIVATION `#output-and-roles` | `#output` | candidate, stop-state, step-output-is-candidate-plus-facts, internal-path-is-not-governed |
| ACTIVATION `#output-and-roles` | `#roles-and-delegation` | assessor, constructor, decision-owner, direct-entry-unless-coordination-needed, one-actor-may-hold-several-roles, roles-are-relations-not-actor-kinds |
| SPEC_METHOD `#1-the-chain` | `#constitutional-chain` | constitutional-chain, work-wave, read-models-never-outrank-specification |
| SPEC_METHOD `#1-the-chain` | `#2-the-chain`, `#reconstruction-litmus` | layer |
| SPEC_METHOD `#1-the-chain` | `#reconstruction-litmus` | layer-sufficiency-is-derivability |
| SPEC_METHOD `#1-the-chain` | `#5-ambiguity-governance-and-lifecycle` | major-ambiguity, chain-layers-narrow-ambiguity, major-ambiguity-is-recorded-with-disposition |
| SPEC_METHOD `#2-one-what-independent-hows` | `#constitutional-chain` | shared-what, tenant-how, conforming-tenants-may-differ, what-bindings-locate-shared-what |
| SPEC_METHOD `#2-one-what-independent-hows` | `#11-governance-of-tenants-in-this-source-project` | tenant-never-patches-what-or-peer |
| SPEC_METHOD `#4-change-classes-and-re-entry` | `#universal-intake-triage` | triage |
| SPEC_METHOD `#4-change-classes-and-re-entry` | `#change-classes` | change-class, change-classes-and-re-entry-points, changed-relation-accepted-only-at-owner |
| SPEC_METHOD `#4-change-classes-and-re-entry` | `#4-change-management`, `#change-classes` | substantive-change-starts-with-triage |
| SPEC_METHOD `#4-change-classes-and-re-entry` | `#carriers` | carrier, carrier-is-selected-by-proportionality |
| SPEC_METHOD `#4-change-classes-and-re-entry` | `#core-interface-migration` | migration, shared-contract-change-is-migration |
| SPEC_METHOD `#5-activation-checkpoint-and-continuation` | `#8-bounded-execution-in-this-method` | steel-thread, baseline-roles-are-relations, delivery-widens-from-smallest-real-path |
| SPEC_METHOD `#5-activation-checkpoint-and-continuation` | `#8-bounded-execution-in-this-method`, ACTIVATION `#5-work-state-and-restart` | checkpoint, acceptance-binds-one-checkpoint |
| SPEC_METHOD `#5-activation-checkpoint-and-continuation` | `#8-bounded-execution-in-this-method`, ACTIVATION `#roles-and-delegation` | executive-relation, return-goes-to-declared-consumer |
| SPEC_METHOD `#7-governance-of-tenants-in-this-source-project` | `#11-governance-of-tenants-in-this-source-project` | tenant-how, tenant-governance-imported-by-reference, residual product-definition-import-outside-basis (source and re-entry) |
| SPEC_METHOD `#8-source-dispositions` | `#12-source-dispositions` | baseline-roles-are-relations |

Two rows are weakly grounded. The constitutional-chain sentences of
`read-models-never-outrank-specification` are in `#constitutional-chain`,
but its final sentence ("Read models, commentary and generated views never
outrank live specification") was not located in the restated SPEC_METHOD.
For `tenant-never-patches-what-or-peer`, §11 states only the peer-tenant
prohibition. Both rows are unreferenced by any of the four new frames.

### Rewritten in place

- `clause:change-classes-and-re-entry-points` (SPEC_METHOD `#change-classes`):
  its qualification literal is now the restated table, giving each class
  with its "Re-enters at" and "Flows through" columns, and its statement
  names the flow.
- `residual:product-definition-import-outside-basis`: "SPEC_METHOD section
  7" now reads "section 11". The residual still holds, because SPEC_METHOD §11 still
  imports the stdo_3 project's PRODUCT.md Development Isolation, which is
  outside the basis. It is unrelated to the PRODUCT_DEFINITION member.

### Added

There are 27 symbols and 62 clauses, listed by frame above. Each new clause cites the
section it encodes and names its principles in a qualification literal. A
new clause carries a support reference only where its source cites the
supported law: AC-013 cites FOUNDATIONS §4, AC-008 cites FOUNDATIONS §4,
the computed-classification reuse cites ACTIVATION §7, the work-result
mapping cites ACTIVATION §3, step 4 cites ASSURANCE §10, and the boundary
effect, step 7 and the Disposition conditions cite ACTIVATION §3. One
residual was added: `residual:contract-state-set-closed-or-minimum`
(kind `conflict`). ACTIVATION §1 Admission states a closed set of four
contract states, and TICKETS §5 states those four as a minimum. The W9b
return routed this conflict to the Executive.
Four frame refs were added: AXIOMATIC_CALCULUS `#ac-013-transformation`,
SPEC_METHOD `#universal-intake-triage`, TICKETS `#carrier-selection` and
EXECUTIVE_BASELINE `#12-complete-engagement-transition`.

## What is and is not encoded

| Member | Encoded in set-4 | Not encoded |
|---|---|---|
| AXIOMATIC_CALCULUS (new) | §3 Latitude and Residual records; AC-005, AC-008, AC-009, AC-013, AC-014 | §1, §2 signature, §3 semantic object, typed relation and constraint, AC-001 to AC-004, AC-006, AC-007, AC-010 to AC-012, §5 and AC-015/016, §6 and AC-017 to AC-019, §7 and AC-020, §8 to §11 |
| SPEC_METHOD (restated) | §4 universal intake triage, change classes (one rewrite, one addition), computed classification and treatment; 15 set-3 rows re-anchored, wording not re-derived | all other restated text: §1, §2 and §3 beyond the re-anchored rows, §4 consistency gate, sprint execution boundary and procedures, §5 to §7, §8 beyond the re-anchored rows, §9 to §12 |
| PRODUCT_DEFINITION (new) | nothing | §1 to §13 |
| ASSURANCE (new) | §7 Terms (testing frame, authoritative Product path), §7 The set, §10 | §1 to §6, §7 user-acceptance, end-to-end, integration and unit frame declarations, §8, §9, §11 to §14 |
| TICKETS (new) | §1 Execution contracts; §4 Change class, Upward propagation check, Triage metadata; §5 Carrier selection, Execution contract admission | §1 goals, records, sprints, comments, milestones; §2; §3; §4 other rules; §5 evaluation criteria and term binding; §6 to §10 |
| EXECUTIVE_BASELINE (new) | §5 technical triage, severity, priority and boundary effect, work result, exact candidate; §6 no mutation, drift locks; §12 steps 4, 5A, 5B, 6 and 7 and the promotion constraint projection | §1 to §4; §5 other terms; §6 duties, attention cycle, event-driven attention, product-chain basis; §7 to §11; §12 steps 1 to 3; §13 to §23 |
| ACTIVATION (changed since `ac3ec5f`) | §3 Disposition (one clause added); set-3 rows carried, `#output-and-roles` anchors moved. The diff hunks were mapped: §1 Admission has no hunk, so its five set-3 rows face unchanged text; §3 gained cross-references, the three-way out_of_frame wording and the new Disposition subsection, which is consistent with the set-3 refinement rows | §1 intake and roles changes, §4 Complete enclosing-relation admission and Standing structural qualification, the §5 checkpoint, progress and falsifier text, the §6 proportionality text and §7 Transition evidence; none of these is compared with the set-3 rows |
| FOUNDATIONS, REFERENCE_FRAME, EVALUATION (changed since `ac3ec5f`) | set-3 rows carried unchanged | the changes between `ac3ec5f` and `978d324` have not been read against the set-3 rows; their fidelity to the current text is unknown |

As in set-3, the source-dispositions tables of every member are not
encoded.

## What validation proves

Validation proves structure, URI resolution, reference closure, the
grounding of every anchor in a heading of the resolved file, and the
canonical digest. It does not prove that the clauses are faithful to the
documents, complete or uniquely interpreted; that judgment is
author-independent and source-first, and none has been made. The program
increment, the frames and the F-02 fixture under
[qualification/cases/F-02/](../../qualification/cases/F-02/CASE.md) were
all authored by the same actor.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in transformation-and-judgment triage-and-reentry carrier-and-admission executive-disposition; do
  for M in materialized reference-only; do
    python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
      --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
      --mode $M --output projection-$FI-$M.json
  done
done
```

The derivation from set-3's program was performed by a scratch script that
is not committed, as with set-2 and set-3. That script did the
re-anchoring table, the two rewrites, the additions and the four frame
indexes above. The program is the artefact, and this file records every
class of change.
