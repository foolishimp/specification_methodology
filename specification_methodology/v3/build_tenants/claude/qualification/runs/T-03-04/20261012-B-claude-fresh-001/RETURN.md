# RETURN: T-03-04 run B, 20261012-B-claude-fresh-001

Constructor: a fresh context of the Claude family (harness model id
`claude-fable-5-1`), activated as a bounded step under CALCULUS §1–4.
Start (`date -u`): `Sun 11 Oct 2026 14:48:55 UTC`. End: last line of this
file. Wall allowance: 45 minutes. Run directory:
`qualification/runs/T-03-04/20261012-B-claude-fresh-001/`. This is the only
file the constructor wrote; `lifecycle.jsonl` and `steps/` beside it were
written by the instrument.

Paths below are relative to
`/Users/jim/src/apps/specification_methodology-claude/stdo_3/build_tenants/claude/`
unless absolute. "Log event" means a line of a named `lifecycle.jsonl`,
identified by its `ts` and `event`.

## 1. Intake (CALCULUS §1)

Outcome served: the shared task of CASE.md (digest below): join bundles R_A
and R_B under OUTER_CONTRACT.md, report the composite under the contract's
composite rule, dispose R_C, record the join's conservation accounting,
triage the detected failure under SPEC_METHOD §4, return a handoff. Run B:
coverage may be produced for uncovered routes as new steps on basis V, and
R minus C recomputed.

Affected relation set: the 23 routes of the contract's table R; the admitted
coverage relation C (three conditions); the join preconditions (same V
digest, same card digest, same rc.2 manifest); the composite rule; FOUNDATIONS
§4 conservation accounting; SPEC_METHOD §4 triage fields. Invariants: no
judgment is reported satisfied unless covered and authenticated; every
covered judgment line is carried unchanged; a known failure and an uncovered
obligation survive every join; nothing in V or any bundle is edited.

Basis, by identity and SHA-256 as computed by this constructor at intake
(`shasum -a 256`):

| Input | SHA-256 | Bytes |
|---|---|---|
| `qualification/cases/T-03-04/CASE.md` | `67406c320242474110afdb94d5267a1fe633103ac6058a5d9825d2c50d1d29f3` | 10379 |
| `qualification/cases/T-03-04/OUTER_CONTRACT.md` | `a24dc63f4ae207b148d668b54def34fcc010c340f650bb6ed515c900bc96170c` | 4884 |
| `qualification/cases/T-03-04/subject/V.md` | `1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4` (equals the contract's declared subject digest) | 6104 |
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` (equals CASE.md's table) | 15218 |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` (equals CASE.md's table) | 15850 |
| `standards/SPEC_METHOD.md` | `c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4` (CASE.md defers to the T2 record, which is outside this grant; recorded as read) | 11522 |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` (equals CASE.md's table) | 8042 |
| `a_c/t2/projection-composition-conservation-materialized.json` | `3a0a1cdb91184f12f1f0da31537da0f193aabbe40d267aa966d6e54179bcc231` (optional aid; first 1200 bytes read, not relied on) | 120805 |
| `qualification/instruments/bounded_step.py` | `aebcc671611d30b02a54b4eba3f1d72750562020e885efa8917fa85838e95938` | 10593 |
| `qualification/instruments/ROUTE_CARD.md` | `068e5b360208029540a60f2f2abdc7ba59ac1a958e62f6418dad8622570b07b6` (equals the contract's declared card digest) | 2540 |
| `results/R_A/MANIFEST.md` / `lifecycle.jsonl` | `10f91b83ff5968b902e8297621eac71b488a7381fc1204a146115ca1b8827d1f` / `bbf1e3cd2fa329e468525f792a5ad618ae3083c0fa1981ef13807dfd40bdc341` | |
| `results/R_B/MANIFEST.md` / `lifecycle.jsonl` | `944360e40bb0352a763b67a3957122a072c5ecc35ded669ad2c0aa004fc7c695` / `9a4deff9b0fc068156cb17130a67315c51ede27571d07d293b487ad8aaa6f225` | |
| `results/R_C/MANIFEST.md` / `lifecycle.jsonl` | `07b7d0fdc22b35cf7d4d5d1aa176445664928120d1f6f66a037f610a12d4b069` / `65f3fd3d3a48e53a8a4cbefdd20205cef609dd3edb0528b05b5319e9b97e99d6` | |
| three bundles, all files under `results/` | per-file digests in §2 | 212352 total |

The rc.2 cut `stdo://releases/v2.5.1-rc.2/` (manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` per the
contract) is part of the basis but outside this constructor's read grant; the
instrument reads it for step actors and logs each section's SHA-256.

Grant: read every file named above and compute digests; start at most four
step actors through `bounded_step.py` at cap 40000 with ROUTE_CARD.md, V as
the tenant block and rc.2 sections as blocks, into this run directory; write
exactly this file. Reserved to others: any repair of V or a bundle (not
granted); any reading of rc.2 text, earlier runs, received material,
reviews, design, `a_c/t1` or git history (not granted); disposition of the
triaged failure (Jim, per the contract's decision-owner line); independent
assessment of this record (an assessor other than the author).

Re-entry conditions named in advance (CALCULUS §4): a bundle binding another
basis is refused, not joined; a step context over cap is refused by the
instrument and refined, never trimmed; an actor failure consumes one start and
is retried only within the remaining allowance; a non-satisfied step judgment
is carried as its member, never coerced; anything needing a change to V, a
bundle, the contract or the card re-enters its owner and is not done here.

Allowance and measurement: four actor starts (two used, two unused); wall 45
minutes by `date -u`; per-actor spend as the instrument logs it
(`context_tokens`, `output_tokens`, `total_cost_usd` at list, `model_ids`,
`total_bytes`); the coordinator's own spend is an unverified harness counter
(§8).

## 2. Join: per-bundle precondition checks

Join preconditions (OUTER_CONTRACT.md "Join preconditions"): same V digest,
same card digest, same rc.2 manifest. Checked against every `measured`
event's `components` list in each bundle's `lifecycle.jsonl`.

| Bundle | Steps (measured events, `ts`) | Tenant block SHA-256 in every measured event | Card SHA-256 in every measured event | rc.2 binding | Result |
|---|---|---|---|---|---|
| R_A | A-P1 `14:42:34.459136Z`, A-P2 `14:42:44.023049Z`, A-P3 `14:42:51.249426Z`, A-P4a `14:42:58.388227Z` | `1c7b224b…3344b4` = V (label "TENANT SECTION FOUNDATIONS §3 variant V", path `cases/T-03-04/subject/V.md`) | `068e5b36…b07b6` = card | every rc.2 block path under `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`; section digests logged | joins |
| R_B | B-P4b `14:43:08.969710Z`, B-P5 `14:43:22.397798Z`, B-P6 `14:43:32.986122Z` | `1c7b224b…3344b4` = V | `068e5b36…b07b6` = card | same release path; section digests logged | joins |
| R_C | C-P1 `14:43:42.728151Z`, C-P2 `14:43:56.129027Z`, C-P3 `14:44:08.045977Z`, C-P4a `14:44:15.319382Z` | `d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf` (label "TENANT SECTION FOUNDATIONS.md#3-commitments", path `standards/FOUNDATIONS.md#3-commitments`), not V | `068e5b36…b07b6` = card | same release path | refused (§6) |

All timestamps are 2026-10-11. On the rc.2 manifest condition: the
instrument does not log the manifest digest; it logs the release path and
each section's SHA-256. R_A, R_B and this run's steps all name the same
release path `v2.5.1-rc.2`, and where two measured events in different
bundles read the same section they log the same digest (for example
`ac-017-interpretation-fidelity` is `0089d51d…cf78` in A-P1 and C-P1; the four
P5 sections are identical between B-P5 and this run's N-P5, §4). The manifest
digest `3d860ff4…` itself is not independently verified by this run; residual
R1 in §7.

Per-file digests of the bundles as they now stand (`shasum -a 256`, computed
at intake, used for condition 2 of C below):

```
R_A/steps/A-P1.out.md   52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f
R_A/steps/A-P2.out.md   2cd360b5e2c74b557bce07efb2e768ba39828f84721c6c5adf6755c65d174364
R_A/steps/A-P3.out.md   23cf09af7ac186cb6e09ce4f9261ab0374d2dd05340593e61a1967c832f545c5
R_A/steps/A-P4a.out.md  ec696190b548c65db5c40f8e0e379267e8dc805eab13801fee6347c1a2c352a4
R_B/steps/B-P4b.out.md  bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28
R_B/steps/B-P5.out.md   81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b
R_B/steps/B-P6.out.md   45f0642c5bc3b9a4f50967b76fbb851364fdc794a679ac09566bf7a66e88f8e7
R_C/steps/C-P1.out.md   fe2c1420b44600508155a52ede5a1f87d14a05cc491d16e06929f6da91a07567
R_C/steps/C-P2.out.md   6731e7a1d8ab822a24a3bc3cbd45bd1e6a9208291819115c14f7bf9d84768463
R_C/steps/C-P3.out.md   5ee726c97b1db8511be16c23545441a06c6caf13d3424bb8abad8ec275c17398
R_C/steps/C-P4a.out.md  167c9aad6c39b0eec044949a2efd4dc6f6c39992ac9213a63af0d755075f672e
```

Per-step authentication of the joining bundles (conditions 1 and 2 of C;
condition 3 is per route in §3):

| Step | Condition 1: measured event with V and card digests | Condition 2: `actor_ended.output_sha256` vs file now | Result |
|---|---|---|---|
| A-P1 | yes (`14:42:34.459136Z`) | logged `52603712…f78f` (`14:42:43.980844Z`) = file | authenticated |
| A-P2 | yes (`14:42:44.023049Z`) | logged `2cd360b5…4364` (`14:42:51.206008Z`) = file | authenticated |
| A-P3 | yes (`14:42:51.249426Z`) | logged `23cf09af…45c5` (`14:42:58.355820Z`) = file | authenticated |
| A-P4a | yes (`14:42:58.388227Z`) | logged `ec696190…52a4` (`14:43:08.931303Z`) = file | authenticated |
| B-P4b | yes (`14:43:08.969710Z`) | logged `bd56c2dc…be28` (`14:43:22.353999Z`) = file | authenticated |
| B-P5 | yes (`14:43:22.397798Z`) | logged `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9` (`14:43:32.943079Z`; same value in R_B/MANIFEST.md) ≠ file `81f1c935…880b` | fails condition 2; no judgment admitted |
| B-P6 | yes (`14:43:32.986122Z`) | logged `45f0642c…f8e7` (`14:43:42.682296Z`) = file | authenticated |
| (R21) | no measured event in R_B names `SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022`; R_B/MANIFEST.md row R21: "planned, not executed", no result file | no result | planned slot with no result; not coverage |

Observation on B-P5 (re-acquirable from the file, not relied on for any
judgment): the file as it stands contains the phrase "closure is total" once
and "closed outcome carriers" zero times (`grep -c`), consistent with CASE.md's
declared alteration. No line of this file is copied into this record.

## 3. Join: per-route coverage, before any step of this run

Covered judgment lines are copied byte-for-byte from the authenticated result
file named, with the trailing newline the instrument wrote; the last line of
each file ("STEP ...") is part of the file and is quoted once per file.

R01–R04, from `R_A/steps/A-P1.out.md` (`52603712…f78f`):

```
ROUTE AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | satisfied | by reference | evidence: rc.2 "Interpretation cannot treat absence as immateriality without a recorded basis and authority" against tenant "Conserves AC-017" under P1 Interpretation | residual: none
ROUTE AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | satisfied | by reference | evidence: rc.2 "Structural success is evidence for semantic review, not a substitute for it" against tenant "structural success never establishes fidelity" | residual: none
ROUTE AXIOMATIC_CALCULUS.md#ac-019-valid-model | satisfied | by reference | evidence: rc.2 "No generic checker may claim the semantic or authority subset unless the model supplies an exact lawful decision contract" against tenant "a semantic decision is lawful only under an exact decision contract" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | satisfied | by reference | evidence: rc.2 "Shared material does not establish identical meaning, basis, authority, or result" against tenant "Conserves ... RF-008" under P1, whose "two contracts give one representation two meanings" is compatible | residual: none
STEP A-P1 | routes 4 | bytes_seen 11391
```

R05–R06, from `R_A/steps/A-P2.out.md` (`2cd360b5…4364`):

```
ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | falsified | restated | evidence: rc.2 says "No universal resource quota or separate accounting carrier follows." The tenant says "every activation declares a token allowance before it begins, as UP-014 requires." | residual: The rc.2 section states no per-activation allowance obligation. It says the method's own execution work serves "an identified change, decision or assurance need" and that reuse is subject to "exact applicability and invalidation". The seeded obligation is not stated there, and the section's "No universal resource quota" statement contradicts it.
ROUTE DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | satisfied | by reference | evidence: rc.2 says "Prime review accounts for governance cost as well as implementation count." The tenant only lists UP-005 under P2's "Conserves" with no restated content. | residual: none

STEP A-P2 | routes 2 | bytes_seen 14189
```

R07–R08, from `R_A/steps/A-P3.out.md` (`23cf09af…45c5`):

```
ROUTE SPEC_METHOD.md#recursive-product-taxonomy | satisfied | by reference | evidence: "The role creates no new Product identity" and "do not confuse an immutable RC release cut or installed product with the mutable source project" bear on P3's "Conserves ... the recursive Product taxonomy" under Identity | residual: none
ROUTE WORLD_MODEL_METHOD.md#entity-cut-construction-law | satisfied | by reference | evidence: "identity, boundary, authority, state, evidence, treatment, covariance, and ambiguity" and "Boundary is interventional in character" bear on P3's "Conserves ... Entity Cut Construction Law" and "a boundary is a claim with a proof obligation" | residual: none
STEP A-P3 | routes 2 | bytes_seen 15662
```

R09–R10, from `R_A/steps/A-P4a.out.md` (`ec696190…52a4`):

```
ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition | satisfied | restated | evidence: "Composition retains both traversal identities, intermediate results, judgments, evidence, authority, provenance, and stop states" matches the tenant's "composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states"; "first result type and judgment satisfy the second traversal's exact domain and preconditions" matches "first's result type and judgment satisfy the second's domain and preconditions" | residual: The tenant says "steps" where AC-016 says "traversals". Whether the two terms denote the same thing is defined outside the given text, and nothing given contradicts it. The tenant omits AC-016's rule that composition cannot flatten proposal, evaluation and decision, and its statement that no universal F_P -> F_D -> F_H sequence is prescribed. The omission does not contradict AC-016.

ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | satisfied | by reference | evidence: "Composition law is required only when the governing evaluation combines their internal variables" and "Independently activated evaluations may instead return closed results to one declared conjunction or decision rule" bear on the tenant's "Two steps compose only when…" and "Conserves … RF-010" | residual: The tenant names RF-010 as conserved without restating it. Nothing in RF-010 contradicts the tenant's conditional typing rule, which applies only once composition occurs. RF-010's subject is frames and when composition law is required. The tenant's subject is composition of steps. The text does not show that the tenant section reads RF-010 as a general composition requirement.

STEP A-P4a | routes 2 | bytes_seen 10259
```

R11–R15, from `R_B/steps/B-P4b.out.md` (`bd56c2dc…be28`):

```
ROUTE AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | satisfied | by reference | evidence: "remains in `X` until an authorized disposition creates an exact successor model" bears on the tenant's "residual" typed instance in "Reframed from AC-009" | residual: none
ROUTE AXIOMATIC_CALCULUS.md#ac-013-transformation | satisfied | by reference | evidence: "Material residuals remain in the successor residual set" and the preserved/removed/introduced delta bear on the tenant's "transition" typed instance and "each continues to govern its own scope" | residual: The tenant's count of "nine statements of conservation" across the five clauses cannot be checked from this section alone.
ROUTE AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | satisfied | by reference | evidence: "retain their declared semantic, operation, evaluation, and decision authority" bears on the tenant's "authority" typed instance in "Reframed from AC-005" | residual: none
ROUTE DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | satisfied | by reference | evidence: "A bounded local action conserves governing truth; it does not rewrite it" bears on the tenant's "frame" typed instance in "Reframed from UP-017" | residual: none
ROUTE SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | satisfied | by reference | evidence: "Their production and invalidation must be recoverable" and "Admission is one semantic commit of the complete transition" bear on the tenant's "transition" and "successor claim" instances in "Reframed from UP-021" | residual: The section's main subject is admission of a complete enclosing relation, so it is only partly a conservation statement. The tenant's mapping of it to typed instances is not contradicted. The tenant's count of nine statements cannot be verified from this section alone.

STEP B-P4b | routes 5 | bytes_seen 25588
```

R16–R19: uncovered before this run's steps. Reason: the only result naming
these routes is `R_B/steps/B-P5.out.md`, whose digest as it stands
(`81f1c935…880b`) differs from the `output_sha256` logged at `actor_ended`
`2026-10-11T14:43:32.943079Z` (`9bd86b6c…88e9`); condition 2 of C fails; the
four judgments in it are not authenticated and none is copied.

R20, R22, R23, from `R_B/steps/B-P6.out.md` (`45f0642c…f8e7`):

```
ROUTE SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | satisfied | by reference | evidence: "semantic basis", "evidence basis" and "state projection" are distinguished; P6 lists UP-008 among the clauses it conserves, beside "evidence supports a claim on a basis" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | satisfied | by reference | evidence: "does not mint, widen, transfer, or reconstruct ... authority from ... evidence shape"; P6 says "authority permits or disposes within scope; neither is minted by the other" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | satisfied | by reference | evidence: "Evidence supplies observations" and "Decision authority disposes the result"; P6 says "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none
STEP B-P6 | routes 3 | bytes_seen 10971
```

R21: uncovered before this run's steps. Reason: planned slot with no result;
R_B/MANIFEST.md row "R21 | — | planned, not executed"; no `measured`,
`actor_started` or `actor_ended` event in `R_B/lifecycle.jsonl` names the
route's section `SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022`.

### Failure set (before and after this run's steps; unchanged)

One failure: R05, `SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014`,
falsified, restated, from `R_A/steps/A-P2.out.md` (`2cd360b5…4364`), produced
by step A-P2 (`actor_ended` `2026-10-11T14:42:51.206008Z`, model
`claude-sonnet-5-5`). Its judgment line
with the quoted evidence is carried unchanged in §3 above. Counterexample
quoted by the actor: rc.2 "No universal resource quota or separate accounting
carrier follows." against V's P2 "every activation declares a token allowance
before it begins, as UP-014 requires."

### R minus C before this run's steps

Admitted coverage C before: 18 routes (R01–R15, R20, R22, R23).
R minus C before: {R16, R17, R18, R19, R21}, five routes.

| Route | Reason uncovered |
|---|---|
| R16 `REFERENCE_FRAME_METHOD.md#rf-012-closed-results` | only result is B-P5.out.md; fails C condition 2 (digest mismatch) |
| R17 `REFERENCE_FRAME_METHOD.md#rf-014-capability-fit` | same |
| R18 `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` | same |
| R19 `DESIGN_MODULE_METHOD.md#8-totality-rule` | same |
| R21 `SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022` | planned slot, not executed; no result exists |

## 4. Steps started by this run (two of four)

Both steps were started through the instrument with the exact granted form
(cap 40000, this run directory, the card, V as the tenant block, the rc.2
sections of the uncovered routes from the contract's route table as blocks;
default model `sonnet`). No `--dry-run` and no `--calibrate` were used. The
instrument's measurement preceded each actor and is logged before
`actor_started`.

### Step N-P5 (routes R16–R19)

- `measured` `2026-10-11T14:51:02.235374Z`: cap 40000, total_bytes 11400,
  fits true; components: system 182, card 2540
  (`068e5b36…b07b6`), tenant block "TENANT SECTION FOUNDATIONS §3 variant V"
  6158 bytes (`1c7b224b…3344b4`), rc.2 `rf-012-closed-results` 698
  (`7e0331f9823c4ef5088af401fd41f7753975cc025c8b058899dcfc9304805784`),
  `rf-014-capability-fit` 392
  (`49ef0d704f5e797c1112138c536b4c4445c0f79c944d49f61cb26ded0bc9c48c`),
  `ac-007-constraint-and-refusal` 353
  (`bbe7100d2f45d792d51b6633750018520a707b2e319d1771e99abefd34790fea`),
  `8-totality-rule` 726
  (`01dfb8406a51fb924ed54e14f9cd2014afbb7ee1dc5c0a0f4a92dc9f64f7d78e`),
  header 351.
- Invalidator check against the producer's B-P5 `measured`
  (`2026-10-11T14:43:22.397798Z`): all four rc.2 section digests and byte
  counts equal; total_bytes equal (11400). The same rc.2 text was read.
- `actor_started` `2026-10-11T14:51:02.235817Z`: input_sha256
  `df78c4c1195bdb16fde4b2d9ed0bf5109d70c9bf5bab98e22c8fcde71c0be73e`
  (= `steps/N-P5.in.md` now), input_bytes 11400.
- `actor_ended` `2026-10-11T14:51:15.924750Z`: is_error false, model_ids
  `["claude-sonnet-5-5"]`, context_tokens 11401, output_tokens 1499,
  total_cost_usd 0.0568242 (list), duration_api_ms 11808, output_sha256
  `8ad4299ba45e1477004036756b2dabda838bad2ffec13cd39b2ea2b690e311e0`,
  output_bytes 1697.
- Authentication: condition 1 yes; condition 2: `steps/N-P5.out.md` now
  digests to `8ad4299b…11e0` = logged; condition 3: four ROUTE lines naming
  the sections of R16, R17, R18, R19. Wall by the shell: start
  `14:51:02 UTC`, end `14:51:15 UTC`.

Judgment lines, from `steps/N-P5.out.md` (`8ad4299b…11e0`), unchanged:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-012-closed-results | satisfied | by reference | evidence: rc.2 "`indeterminate`... `out_of_frame`... `invalid_basis`" bears on tenant "result algebra carries indeterminate, out_of_frame and invalid_basis as first-class outcomes" | residual: none
ROUTE REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | satisfied | by reference | evidence: rc.2 "The actor may not silently omit material relations to fit context" bears on tenant "A step can meet a condition outside its context; it cannot report success on one" | residual: The tenant names RF-014 only in a conserves list and gives it no content of its own. The rc.2 subject is actor capability fit, and the tenant frames the same concern as a step meeting a condition outside its context. Nothing contradicts that framing.
ROUTE AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | satisfied | by reference | evidence: rc.2 "follows the declared result algebra rather than being coerced to success" bears on tenant "it cannot report success on one" | residual: The tenant's claim that AC-007 is "restated once in CALCULUS §3" refers to a section I was not given. I did not judge it.
ROUTE DESIGN_MODULE_METHOD.md#8-totality-rule | satisfied | by reference | evidence: rc.2 "failure is returned in a typed and explicit form when practical" bears on tenant "Totality Rule" as conserved, with "result algebra" and "control model names the next move" | residual: The rc.2 section is a "should" preference for total semantic functions. The tenant's "cannot report success" is stronger but does not contradict it. The tenant restates no obligation as this clause's content.

STEP N-P5 | routes 4 | bytes_seen 11400
```

### Step N-P6-R21 (route R21)

- `measured` `2026-10-11T14:51:16.075249Z`: cap 40000, total_bytes 14538,
  fits true; components: system 182, card 2540 (`068e5b36…b07b6`), tenant
  block V 6158 (`1c7b224b…3344b4`), rc.2
  `assurance-boundary-congruence-and-method-qualification-stdo-up-022` 5451
  (`030c44b7e7cb2b59d4a7ef3fb04a9d1e6054db09a2cb422520824ce23687b893`),
  header 207. No earlier measured event in any bundle read this section, so
  there is no prior digest to compare; this is its first logged digest.
- `actor_started` `2026-10-11T14:51:16.075677Z`: input_sha256
  `190e349cded328efd04b8f538ac11b10e70bf940101c587b4bccec8322dd6056`
  (= `steps/N-P6-R21.in.md` now), input_bytes 14538.
- `actor_ended` `2026-10-11T14:51:23.244731Z`: is_error false, model_ids
  `["claude-sonnet-5-5"]`, context_tokens 12206, output_tokens 539,
  total_cost_usd 0.0504442 (list), duration_api_ms 5013, output_sha256
  `58b4e5b20c2fa67a656ecf3c12135b7dd8167f5b4c79443e7b3be1125b500a25`,
  output_bytes 574.
- Authentication: condition 1 yes; condition 2: `steps/N-P6-R21.out.md` now
  digests to `58b4e5b2…0a25` = logged; condition 3: one ROUTE line naming
  R21's section. Wall by the shell: start `14:51:15 UTC`, end `14:51:23 UTC`.

Judgment line, from `steps/N-P6-R21.out.md` (`58b4e5b2…0a25`), unchanged:

```
ROUTE SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | satisfied | by reference | evidence: rc.2 "Digest integrity and index generation establish identity and structure, not semantic fidelity" and "comparison ... proceeds under constructor authority instead of independently authorized evaluator authority" bear on the tenant's "Conserves ... UP-022" under P6 ("evidence supports a claim on a basis; authority permits or disposes within scope; neither is minted by the other") | residual: none

STEP N-P6-R21 | routes 1 | bytes_seen 14538
```

### R minus C after this run's steps

Admitted coverage C after: 23 routes (R01–R23). R minus C after: empty.
Coverage for R16–R19 is the new authenticated step N-P5 on basis V; coverage
for R21 is the new authenticated step N-P6-R21 on basis V. No judgment from
`R_B/steps/B-P5.out.md` and no judgment from R_C entered C at any point.

Two of the four granted starts remain unused; no retry was needed.

## 5. Composite and its computation

Rule (OUTER_CONTRACT.md "Composite rule"), applied in its stated order over R
after this run's steps:

1. satisfied only when every route is covered and every covered judgment is
   satisfied: every route is covered (23/23), but the covered judgment for
   R05 is falsified. Not satisfied.
2. otherwise falsified if any covered judgment is falsified: R05 is covered
   (A-P2 authenticated, §2) and falsified. **Composite = falsified.**

The later branches (invalid_basis, out_of_frame, indeterminate) are not
reached. For the record: no covered judgment is invalid_basis, out_of_frame
or indeterminate; all 22 other covered judgments are satisfied.

Before this run's steps the composite was also falsified by the same branch
(R05 falsified; five routes uncovered, which would have made it out_of_frame
only if no covered judgment were falsified). The two steps changed R minus C
from five routes to none; they did not and could not change the member,
because R05 survives the join (FOUNDATIONS §4; CALCULUS §3).

The composite record consists of §3 (every covered judgment line unchanged,
the failure set, R minus C with reasons), §4 (the five new lines), §6 (the
refused bundle) and §7 (conservation accounting). Nothing is dropped and no
judgment line is summarised in place.

## 6. Refused bundles

R_C is refused. Reason: it binds another basis. Every `measured` event in
`R_C/lifecycle.jsonl` (`65f3fd3d…99d6`) carries the tenant block
"TENANT SECTION FOUNDATIONS.md#3-commitments" with SHA-256
`d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf` (path
`standards/FOUNDATIONS.md#3-commitments`), not the contract's subject V
`1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4`. Its
R_C/MANIFEST.md declares the same basis in its tenant-block line. The card
digest and the rc.2 release path match, and its four result files digest to
their logged `output_sha256` values (§2 table), so its results are
authenticated for their own basis; equal field shapes and equal rc.2 section
digests do not supply a valid join under the contract's preconditions.
Consequently none of its ten judgments, including its satisfied judgment for
R05 in `R_C/steps/C-P2.out.md` (`6731e7a1…8463`), enters C, and no composite
relation over the mixed bases V and FOUNDATIONS §3 proper is declared.

Observation only, not a judgment and not relied on: `R_C/steps/C-P4a.out.md`
carries ROUTE lines whose member field is prefixed
`FOUNDATIONS.md#3-commitments→`, and one of them is out_of_frame. Since the
bundle is refused on its basis, this record does not evaluate those lines.

## 7. Conservation accounting of the join (FOUNDATIONS §4, AC-013 fields)

Preserved:
- the 18 authenticated judgment lines of R_A and R_B (A-P1 4, A-P2 2, A-P3 2,
  A-P4a 2, B-P4b 5, B-P6 3), each carried byte-for-byte with its evidence and
  residual text (§3);
- the known failure R05 with its quoted counterexample (§3);
- the step-actor residuals carried inside those lines (the "nine statements"
  count unverifiable from one section; "steps" versus "traversals"; "restated
  once in CALCULUS §3" not judged);
- R21's status as a planned slot with no result, now recorded as the reason
  it was uncovered before step N-P6-R21;
- all three bundles unmodified: their manifests, logs and files digest as
  listed in §1 and §2; this run wrote nothing under `results/`;
- V unmodified (`1c7b224b…3344b4` at intake and at the two step
  measurements).

Introduced:
- five authenticated judgment lines on basis V from steps N-P5 and N-P6-R21
  (§4), with their six log events in this run's `lifecycle.jsonl` (digest at
  the time of writing: `5c1b3ec64e0cbc4a5a5d662d9ed125bda2f3767495a000e9a45028fbefa2b92d`)
  and their files under `steps/` (digests in §8);
- the refusal record for R_C (§6);
- the composite and its computation (§5);
- the triage (§9);
- this record.

Removed: nothing. Two sets of judgments were never admitted, which is an
exclusion with a recorded reason, not a removal: the four lines of
`R_B/steps/B-P5.out.md` (authentication failure) and the ten lines of R_C
(basis mismatch).

External resolution witnesses:
- the instrument's `measured` events, which bind each step's rc.2 sections by
  SHA-256 before the actor exists; N-P5's four section digests equal B-P5's;
- the release path `v2.5.1-rc.2` named in every rc.2 block of R_A, R_B and
  this run;
- the `actor_ended` digests, which bind each result file.

Residuals:
- R1. The rc.2 manifest digest `3d860ff4…2782` named by the contract is not
  independently verified by this run: the instrument logs section digests and
  the release path, not the manifest, and reading the manifest is outside this
  constructor's grant. Equality of rc.2 binding between R_A, R_B and this run
  rests on the release path and on section-digest equality where sections
  overlap.
- R2. Whether the four unauthenticated judgments in B-P5.out.md agree with
  N-P5's four is not claimed either way; the altered file was not used.
- R3. All five step actors whose judgments enter C are `claude-sonnet-5-5`,
  and the constructor is `claude-fable-5-1`; under EVALUATION §3 these are
  not declared independent. The composite is construction output with
  self-review, not an independent assessment.
- R4. The coordinator's own spend is an unverified harness counter (§8).
- R5. The step-actor residuals listed under "Preserved" remain open; none
  changes a member.

## 8. Accounting

Per step actor started by this run, as the instrument logged it:

| Step | model_ids | context_tokens | output_tokens | total_cost_usd (list) | measured bytes | duration_api_ms | wall (shell `date -u`) |
|---|---|---|---|---|---|---|---|
| N-P5 | claude-sonnet-5-5 | 11401 | 1499 | 0.0568242 | 11400 | 11808 | 14:51:02 → 14:51:15 UTC |
| N-P6-R21 | claude-sonnet-5-5 | 12206 | 539 | 0.0504442 | 14538 | 5013 | 14:51:15 → 14:51:23 UTC |
| total (2 starts) | | 23607 | 2038 | 0.1072684 | 25938 | 16821 | 21 s |

Per-step token detail from `steps/*.usage.json`: N-P5 input 2,
cache_creation 10408, cache_read 991, thinking 849; N-P6-R21 input 2,
cache_creation 11213, cache_read 991, thinking 320. Session ids
`72391243-e8c1-4222-aba5-795edb51ba52` and `77017a32-932e-48da-b3a9-a2a942ac331d`.

Run-directory files at the time of writing (`shasum -a 256`):

```
lifecycle.jsonl            5c1b3ec64e0cbc4a5a5d662d9ed125bda2f3767495a000e9a45028fbefa2b92d
steps/N-P5.in.md           df78c4c1195bdb16fde4b2d9ed0bf5109d70c9bf5bab98e22c8fcde71c0be73e  (11218 bytes)
steps/N-P5.out.md          8ad4299ba45e1477004036756b2dabda838bad2ffec13cd39b2ea2b690e311e0  (1697 bytes)
steps/N-P5.usage.json      7ba528513383d6d4f22f2536cf592e39933f536e991deb3c0bf8735f4907313e
steps/N-P6-R21.in.md       190e349cded328efd04b8f538ac11b10e70bf940101c587b4bccec8322dd6056  (14356 bytes)
steps/N-P6-R21.out.md      58b4e5b20c2fa67a656ecf3c12135b7dd8167f5b4c79443e7b3be1125b500a25  (574 bytes)
steps/N-P6-R21.usage.json  d6b1455e6d684ec7bf73b3296c2a4106db1086ca73e6307b01eaf186f786983a
```

Coordinator (this constructor): unverified counter. Source: the harness's
`total_tokens` remaining-budget figure shown to the constructor context,
15,000,000 at activation and 14,861,487 at the last tool result before this
file was written; consumed by that measure 138,513 tokens, excluding the
write of this file. No list cost is available for the coordinator from
inside the activation.

Standing basis named in the intake: 418,289 bytes in total (CASE.md 10379,
OUTER_CONTRACT.md 4884, V.md 6104, three bundles 212352, FOUNDATIONS 15218,
CALCULUS 15850, SPEC_METHOD 11522, EVALUATION 8042, projection 120805,
instrument 10593, card 2540). Of this, read into the constructor context in
full: everything except the projection (1,200 bytes of 120,805 read) and the
bundles' eleven `*.in.md` step inputs (sizes taken, 147,186 bytes; only the
first 60 lines of `R_A/steps/A-P1.in.md` read, to confirm the input shape);
approximately 155 KB read.

Wall time: start `Sun 11 Oct 2026 14:48:55 UTC`; both actors done by
`14:51:23 UTC`; triage recorded at `14:53:24 UTC`; end stamp on the last line
of this file. Within the 45-minute allowance.

## 9. Triage of the detected failure (SPEC_METHOD §4)

Detected failure: R05 falsified (§3). V's P2 states, as the content of the
conserved clause UP-014, the obligation "every activation declares a token
allowance before it begins, as UP-014 requires"; the step actor quotes the
rc.2 section's "No universal resource quota or separate accounting carrier
follows." as the defeating statement. A re-acquirable observation from the
declared basis corroborates the direction of the defect without being a
judgment on rc.2 text: CALCULUS §6 (`b5fb31de…3821`) states the allowance
rule as "new; P0 with UP-014's selection rule", selected where capability fit
or a cost claim is the governed question, and itself says "No universal
quota, ticket count, actor count or accounting carrier follows." V's P2 is
inconsistent with the corpus's own CALCULUS §6 as well as with the cited
rc.2 clause.

- Change intent: remove from P2 the universal per-activation allowance
  obligation and its attribution to UP-014, so that P2 conserves UP-014 by
  reference as FOUNDATIONS §3 proper does (`2f15c6c1…38a22`), and the
  allowance rule stays where the corpus states it, CALCULUS §6, as new and
  selected. No change to CALCULUS §6 or to rc.2 is intended.
- Class: `requirement_reprice`. The sentence is a commitment in tier-1 law
  (FOUNDATIONS §3 is "the commitments as law") and misstates the standing of
  an obligation relative to the rc.2 builder (FOUNDATIONS §1: a conserved
  clause "governs unchanged"; a new obligation names its requiring principle).
  Correcting it changes constitutional truth of the corpus while direction
  holds. `realization_refactor` is rejected because the change is upstream of
  every consumer of P2 (CALCULUS §6, EVALUATION §7 cost measurement) and
  changes what they inherit; `design_reframe` is rejected because the
  defective statement is at the requirement layer, not a realisation of a
  sound one.
- Re-entry point: FOUNDATIONS §3 P2, the sentence citing UP-014, together
  with the UP-014 row of FOUNDATIONS §6 "Source dispositions" (conserved;
  consumed by SPEC_METHOD §3 and CALCULUS §6), which the corrected P2 must
  still satisfy.
- Owner: for V, the T-03-04 case owner (V is fixture material; CASE.md
  declares the sentence seeded; this constructor makes no repair). For the
  live standard, the owner of `standards/FOUNDATIONS.md` in the Claude tenant.
  Decision owner for anything beyond the join: Jim (OUTER_CONTRACT.md
  identity line).
- Carrier: this run record (the work lives and dies with one activation;
  SPEC_METHOD §4 carrier-by-lifetime). A durable ticket is the owner's choice
  if the live standard is to change.
- When triaged: `Sun 11 Oct 2026 14:53:24 UTC` (`date -u`).

## 10. Stop state, residuals, handoff

Stop state of this step (CALCULUS §3, over the step's own predicate "join
R_A and R_B under the contract, dispose R_C, return the composite with its
accounting and triage"): **satisfied**; construction-availability refinement
`candidate_ready`. This is distinct from the composite the step reports,
which is **falsified** (§5). No part of the task was out of grant, no context
exceeded the cap, no actor failed, and nothing was coerced.

Residuals: R1–R5 in §7. None blocks the composite; R1 is the only one a
different grant could close.

Handoff, executable without this run's conversation under the envelope each
names:

1. To consume the composite (any actor, read-only grant over this run
   directory and the inputs in §1): read this file; re-check the invalidators
   before reliance (CALCULUS §7): V `1c7b224b…3344b4`, card `068e5b36…b07b6`,
   instrument `aebcc671…5938`, the six bundle result files and this run's
   two result files at the digests in §2 and §8, and this run's
   `lifecycle.jsonl` at `5c1b3ec6…b92d`. Any change invalidates the affected
   lines; the rest survive.
2. To dispose the failure (Jim, or the FOUNDATIONS owner under Jim's
   authority): act on §9 at FOUNDATIONS §3 P2. Nothing here repairs V.
3. To close residual R1 (an actor granted to read
   `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/`):
   compute the installed manifest's SHA-256 and compare with
   `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; on
   match the rc.2 precondition is verified for all eleven producer steps and
   both steps of this run, which all name that release path.
4. To assess this run (an assessor other than the author, under a review Jim
   authorises, per CASE.md "Assessment"): freeze this directory at a named
   commit, record expectations from the two common sources first, then
   evaluate E1–E6 under EVALUATION §4. The assessor needs no step-actor
   start; every judgment is authenticated from the logs and files named here.
5. To extend coverage or re-produce any step (an actor with the run-B grant):
   the exact command form is in the T-03-04 run-B grant; the two unused
   starts of this run do not carry over. Re-production of an existing
   authenticated step is preservation, not progress (CALCULUS §5).

Unused allowance: two actor starts; wall time remaining at the end stamp.

End (`date -u`): see the next line, appended immediately after this file was
written.
End (`date -u`): `Sun 11 Oct 2026 14:57:41 UTC`
