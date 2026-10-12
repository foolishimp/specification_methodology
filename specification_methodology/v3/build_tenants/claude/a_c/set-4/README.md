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
members. The validation report records 145 resolved sources: every tenant
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
| `axiomatic-program.json` | `bd837f1ab430caa23ec32d957c76e027b232ac3548871cd6c88f78c38d8eebc1` | the authored a_c.text program `urn:stdo-3:claude:program:a-c-text:set-4`; canonical program digest `sha256:10fc52ad07e5730e378dd18ed07819b2d1dd41fd8549a5f67ac7fd4f40fe760c` |
| `logical-constraint-map.json` | `b781bc008efc188988d949b3443ce2e4ed1e884be624c2729c9dffd519b1da98` | deterministic index over the program; intrinsic digest `sha256:5e4c871db46dfec9a2d35efdd30ab72da5fbc4fc6f32a9d3f2ac772280cf9cb3` |
| `validation-report.json` | `3b859b23bdeaed5713589dce4d20b604a06839a859a19e505bba9b8edca87d88` | status `valid`, zero diagnostics; 236 symbols, 330 clauses, 6 residuals; 145 resolved sources |
| `projection-transformation-and-judgment-materialized.json` | `a2beaabab3ed1917d1786d665eafa33083d6cd3b812c9112605c4d6e0e2bb1cd` | frame `transformation-and-judgment`, materialized; projection digest `sha256:325bca71c25e431bc0480dea20c8d402e4cbe43d14e2031b357c728ffb8e30a3` |
| `projection-transformation-and-judgment-reference-only.json` | `cb1e25a955c122359f1f3331cbbe91aeefab09b54707321565b367d38a99d209` | the same frame, reference-only; `sha256:87c236b68a47fabe1052296943aa35f01bbc2ebc6b153056b7285ff7babdceb3` |
| `projection-triage-and-reentry-materialized.json` | `6cc0e3affd153f7c3c022ff3c932a06f40e648d6732edff686d62b77d07027a2` | frame `triage-and-reentry`, materialized; `sha256:c61f5d0d8f3dbe3e898be6ad2d96749151b808494328069eab3c6f6643627253` |
| `projection-triage-and-reentry-reference-only.json` | `8fc3f13527e9f4b9d09a7f988549726da94b4f886f39d00b7323ca611c95fd9f` | the same frame, reference-only; `sha256:7c0d7f7fb39fb49369fe0beb8f027b0895eece256028e63ae3d05d803cdb4d4d` |
| `projection-carrier-and-admission-materialized.json` | `bd1e71191f9e005ced31672debe396bf15afe5244528a948ddde1e1fc88522d9` | frame `carrier-and-admission`, materialized; `sha256:beec3c4b79273b55610d5f2dc1ef77d329257b2f05ef959b7e73663dfca6fd12` |
| `projection-carrier-and-admission-reference-only.json` | `eb64bc39d2a33eb077a87bb3682f29eb0d5e69c2a09eae0fc160eac60b0297a0` | the same frame, reference-only; `sha256:2cf418d7eb62c1b6987aec17e8652b26141ab709e29874ecff3becca9a00698c` |
| `projection-executive-disposition-materialized.json` | `18fad1848de8f5f544309ea497204aeb5ce9b72998a7b06a3a32d0dedcdde285` | frame `executive-disposition`, materialized; `sha256:8fc3703afe1746c5564d0a5fb58c26d4f69d6877675f9e4e8d95a110f68938c7` |
| `projection-executive-disposition-reference-only.json` | `e89acb03e9799650bbc3b427620b2c779910e309e7f3cc2c9c6ec45aa5b55631` | the same frame, reference-only; `sha256:24418167ef7c9f1cf3955836ed22957a36f51d8e997f3ce4ae58d52ffbc80d92` |
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
| `transformation-and-judgment` | 56,993 | `a2beaabab3ed…` | 29,680 | 16, 19, 0 | yes |
| `triage-and-reentry` | 68,182 | `6cc0e3affd15…` | 36,269 | 16, 21, 0 | yes |
| `carrier-and-admission` | 65,847 | `bd1e71191f9e…` | 34,777 | 20, 19, 2 | yes |
| `executive-disposition` | 89,104 | `18fad1848de8…` | 47,183 | 28, 23, 0 | yes |

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
obligation-without-route-is-unjustified and p2-statement. Two residuals are
carried in through the proportionality and principle symbols:
derivation-chain-cost-per-boundary and
independence-arguments-are-one-sentence.

`executive-disposition` (frame ref EXECUTIVE_BASELINE
`#12-complete-engagement-transition`; F-02 task D). 23 clauses:
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
testing-evidence-stays-claim-bound; pulled in by support:
construction-availability-maps-to-core, disposition-consumes-a-core-result,
refinements-map-totally-to-core.

What the size limit kept out: `executive-disposition` does not carry
`result-algebra-has-five-members`, whose closure of nine clauses would add
about 24 KB materialized and put the frame over the limit. The core members
`satisfied`, `falsified`, `indeterminate`, `out_of_frame` and
`invalid_basis` reach the actor through the construction-availability
mapping, the drift-lock failure clause and the work-result clause, not
through the algebra's own definition. The frame also carries no
ACTIVATION §3 or §5 checkpoint law beyond what step 7 restates.

## Departures from the set-3 recipe

- Only the four new frame indexes are projected. The seven set-3 frame
  indexes remain in the program unchanged, but they were not
  re-projected: each would exceed the 100,000-byte limit, since their
  set-3 frames ran 144 to 272 KB. The set-3 recipe projected every index
  in one loop.
- Validation now enforces sorted `source_refs`. Re-anchored rows and the
  new rows have their reference lists sorted, while set-3 rows that were
  already sorted are unchanged.

## Changes between set-3 and set-4

Counts: symbols 209 to 236 (27 added), clauses 269 to 330 (61 added, one
rewritten in place), residuals 6 (one detail rewritten), frame indexes 7 to
11, frame refs 7 to 11. Nothing was retired.

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

There are 27 symbols and 61 clauses, listed by frame above. Each new clause cites the
section it encodes and names its principles in a qualification literal. A
new clause carries a support reference only where its source cites the
supported law: AC-013 cites FOUNDATIONS §4, AC-008 cites FOUNDATIONS §4,
the computed-classification reuse cites ACTIVATION §7, the work-result
mapping cites ACTIVATION §3, step 4 cites ASSURANCE §10, and the boundary
effect and step 7 cite ACTIVATION §3 Disposition. No residual was added.
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
| FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, EVALUATION (changed since `ac3ec5f`: 648 insertions, 114 deletions) | set-3 rows carried; only the ACTIVATION `#output-and-roles` anchors changed | the changes between `ac3ec5f` and `978d324` have not been read against the set-3 rows; their fidelity to the current text is unknown |

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
