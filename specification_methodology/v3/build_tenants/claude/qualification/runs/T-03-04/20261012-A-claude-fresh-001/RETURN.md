# RETURN: T-03-04 run A, 20261012-A-claude-fresh-001

Constructor: a fresh context of the Claude family (harness-reported model id `claude-fable-5-1`), with no prior history of this project. Run id as assigned by the caller: `20261012-A-claude-fresh-001`. Start by `date -u`: `Sun 11 Oct 2026 14:48:40 UTC`. End by `date -u`: `Sun 11 Oct 2026 14:56:48 UTC`. This file is the only file written by this activation; nothing else was created or edited.

Every claim below is traceable to a SHA-256 digest computed in this run (`shasum -a 256`, and `hashlib.sha256` for the in-memory check) or to a timestamped event in a bundle's `lifecycle.jsonl`. Digest abbreviations (first eight hex digits followed by `…`) refer to the full digests in the intake table.

## 1. Intake (CALCULUS §1)

Outcome served. The T-03-04 shared task, run A (CASE.md, identity `urn:stdo-3:claude:case:T-03-04`): join bundles R_A and R_B under OUTER_CONTRACT.md (`urn:stdo-3:claude:contract:T-03-04:v-routes`), report the composite under the contract's composite rule, dispose R_C, record the join's conservation accounting, triage the detected failure under SPEC_METHOD §4, and return a handoff. The task serves CONFORMANCE rows T-03 and T-04 and the thread T2 discriminating case named in CASE.md.

Affected relation set. The contract's claim over V (subject, property, basis, witness relation, falsifier, excluded weaker property); the required obligation set R of 23 routes; admitted coverage C under the contract's three conditions; the join preconditions (same V digest, same card digest, same rc.2 manifest); the composite rule and its declared order of non-satisfied members; FOUNDATIONS §4 conservation accounting (R minus C, union of failures, failure and uncovered obligation survive every join); CALCULUS §3 result algebra and §4 refinement premises (coverage of outer obligations is a premise, not a conclusion); SPEC_METHOD §4 triage. Invariants held by this step: nothing is reported satisfied unless covered and authenticated; every covered judgment line is carried unchanged; no judgment from a bundle bound to another basis enters C; no composite relation over mixed bases is declared; V is not repaired and no bundle is altered; nothing outside this run directory is written.

Basis by identity and digest. All digests computed in this run; sizes by `wc -c`.

| Input (under `stdo_3/build_tenants/claude/`) | SHA-256 | bytes |
|---|---|---|
| `qualification/cases/T-03-04/CASE.md` | `67406c320242474110afdb94d5267a1fe633103ac6058a5d9825d2c50d1d29f3` | 10379 |
| `qualification/cases/T-03-04/OUTER_CONTRACT.md` | `a24dc63f4ae207b148d668b54def34fcc010c340f650bb6ed515c900bc96170c` | 4884 |
| `qualification/cases/T-03-04/subject/V.md` | `1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4` | 6104 |
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` | 15218 |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` | 15850 |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` | 8042 |
| `standards/SPEC_METHOD.md` | `c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4` | 11522 |
| `a_c/t2/projection-composition-conservation-materialized.json` (digested, not read) | `3a0a1cdb91184f12f1f0da31537da0f193aabbe40d267aa966d6e54179bcc231` | 120805 |
| `results/R_A/MANIFEST.md` | `10f91b83ff5968b902e8297621eac71b488a7381fc1204a146115ca1b8827d1f` | 2515 |
| `results/R_A/lifecycle.jsonl` | `bbf1e3cd2fa329e468525f792a5ad618ae3083c0fa1981ef13807dfd40bdc341` | 8903 |
| `results/R_A/steps/A-P1.out.md` | `52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f` | 1240 |
| `results/R_A/steps/A-P2.out.md` | `2cd360b5e2c74b557bce07efb2e768ba39828f84721c6c5adf6755c65d174364` | 974 |
| `results/R_A/steps/A-P3.out.md` | `23cf09af7ac186cb6e09ce4f9261ab0374d2dd05340593e61a1967c832f545c5` | 718 |
| `results/R_A/steps/A-P4a.out.md` | `ec696190b548c65db5c40f8e0e379267e8dc805eab13801fee6347c1a2c352a4` | 1779 |
| `results/R_B/MANIFEST.md` | `944360e40bb0352a763b67a3957122a072c5ecc35ded669ad2c0aa004fc7c695` | 2918 |
| `results/R_B/lifecycle.jsonl` | `9a4deff9b0fc068156cb17130a67315c51ede27571d07d293b487ad8aaa6f225` | 8419 |
| `results/R_B/steps/B-P4b.out.md` | `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28` | 1876 |
| `results/R_B/steps/B-P5.out.md` (as it now stands) | `81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b` | 1605 |
| `results/R_B/steps/B-P6.out.md` | `45f0642c5bc3b9a4f50967b76fbb851364fdc794a679ac09566bf7a66e88f8e7` | 941 |
| `results/R_C/MANIFEST.md` | `07b7d0fdc22b35cf7d4d5d1aa176445664928120d1f6f66a037f610a12d4b069` | 2624 |
| `results/R_C/lifecycle.jsonl` | `65f3fd3d3a48e53a8a4cbefdd20205cef609dd3edb0528b05b5319e9b97e99d6` | 8921 |
| `results/R_C/steps/C-P1.out.md` | `fe2c1420b44600508155a52ede5a1f87d14a05cc491d16e06929f6da91a07567` | 1662 |
| `results/R_C/steps/C-P2.out.md` | `6731e7a1d8ab822a24a3bc3cbd45bd1e6a9208291819115c14f7bf9d84768463` | 1356 |
| `results/R_C/steps/C-P3.out.md` | `5ee726c97b1db8511be16c23545441a06c6caf13d3424bb8abad8ec275c17398` | 829 |
| `results/R_C/steps/C-P4a.out.md` | `167c9aad6c39b0eec044949a2efd4dc6f6c39992ac9213a63af0d755075f672e` | 1711 |

The eleven `steps/*.in.md` files (147186 bytes in all) and eleven `steps/*.usage.json` files (16175 bytes) were digested and their `.in.md` digests compared with the logged `actor_started.input_sha256` (§2.2); their text was not read. Digests the contract declares and this run could not recompute: the card `qualification/instruments/ROUTE_CARD.md` `068e5b360208029540a60f2f2abdc7ba59ac1a958e62f6418dad8622570b07b6` (not among run A's named inputs; checked only as logged in every measured block) and the rc.2 manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` (rc.2 is unreadable under this grant).

Grant. Read every file in the table and compute digests of them. Zero step-actor starts; `bounded_step.py` not run. No reading of rc.2 text, of `qualification/runs/` other than this directory, of `qualification/received/`, `reviews/`, `design/`, `a_c/t1/`, or git history. Write exactly this file. Do not repair V, alter any bundle, or judge rc.2 text. Decisions reserved to others: disposition of V and of the fixture is the case owner's; anything beyond the join is Jim's (OUTER_CONTRACT.md, decision owner).

Re-entry conditions. Any of the following stops the join and returns to the grant owner: V's digest differs from the contract's; a measured block in an admitted bundle carries a card digest other than `068e5b36…`; a bundle names an rc.2 cut other than `v2.5.1-rc.2`; a lifecycle log is unparseable; coverage must be produced (needs an actor start, excluded here). None of the first four occurred. The fifth occurred for five routes and is carried as R minus C, as the contract's composite rule provides.

Allowance. 0 actor starts; 30 minutes wall; spend measured by the harness's `total_tokens left` marker (an unverified counter; §6).

## 2. Join

### 2.1 Bundle precondition checks

The contract joins two bundles only when both bind the same V digest, the same card digest and the same rc.2 manifest.

R_A. Four measured events (2026-10-11T14:42:34.459136Z A-P1, 14:42:44.023049Z A-P2, 14:42:51.249426Z A-P3, 14:42:58.388227Z A-P4a; log digest `bbf1e3cd…`). Each carries component `card` sha `068e5b36…` and component `block:TENANT SECTION FOUNDATIONS §3 variant V` sha `1c7b224b…` (6158 bytes), with the block path `qualification/cases/T-03-04/subject/V.md`. Every `RC.2 SECTION` block path is under `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`. V precondition: met. Card precondition: met. rc.2 precondition: the cut is identified by path (`v2.5.1-rc.2`) in every block; the manifest digest is recorded in no event and no manifest, and cannot be recomputed under this grant (residual RS-1). Admitted to the join.

R_B. Three measured events (14:43:08.969710Z B-P4b, 14:43:22.397798Z B-P5, 14:43:32.986122Z B-P6; log digest `9a4deff9…`). Same card sha, same tenant block name, sha and path, same rc.2 path prefix. V and card preconditions met; rc.2 as for R_A. Admitted to the join.

R_C. Four measured events (14:43:42.728151Z C-P1, 14:43:56.129027Z C-P2, 14:44:08.045977Z C-P3, 14:44:15.319382Z C-P4a; log digest `65f3fd3d…`). Each carries card sha `068e5b36…` but tenant block `block:TENANT SECTION FOUNDATIONS.md#3-commitments` sha `d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf` (5712 bytes), path `standards/FOUNDATIONS.md#3-commitments`; R_C MANIFEST.md (`07b7d0fd…`) states the same basis. V precondition: fails. Refused (§2.6).

### 2.2 Authentication of planned slots in the admitted bundles (conditions 1 and 2)

| Step | measured: cap / bytes / fits | tenant sha = V | card sha = card | actor_ended `output_sha256` | file digest now | bytes logged / now | condition 2 |
|---|---|---|---|---|---|---|---|
| A-P1 | 40000 / 11391 / true | yes | yes | `52603712…` | `52603712…` | 1240 / 1240 | holds |
| A-P2 | 40000 / 14189 / true | yes | yes | `2cd360b5…` | `2cd360b5…` | 974 / 974 | holds |
| A-P3 | 40000 / 15662 / true | yes | yes | `23cf09af…` | `23cf09af…` | 718 / 718 | holds |
| A-P4a | 40000 / 10259 / true | yes | yes | `ec696190…` | `ec696190…` | 1779 / 1779 | holds |
| B-P4b | 40000 / 25588 / true | yes | yes | `bd56c2dc…` | `bd56c2dc…` | 1876 / 1876 | holds |
| B-P5 | 40000 / 11400 / true | yes | yes | `9bd86b6c…` | `81f1c935…` | 1612 / 1605 | fails |
| B-P6 | 40000 / 10971 / true | yes | yes | `45f0642c…` | `45f0642c…` | 941 / 941 | holds |

Further checks on all seven steps: `actor_started.input_sha256` equals the current digest of `steps/<step>.in.md`; `actor_ended.is_error` is false; `model_ids` is `["claude-sonnet-5-5"]`; the trailing `STEP <step> | routes N | bytes_seen B` line of each output file has N equal to its number of ROUTE lines and B equal to the measured `total_bytes`; every rc.2 section named by a ROUTE line is a block in that step's measured context.

B-P5 observation. Replacing in memory the single occurrence of `closure is total` in the current `B-P5.out.md` with `closed outcome carriers` yields exactly the logged digest `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9`; the seven-byte difference matches. So the file differs from what the instrument wrote by that one substitution in R19's evidence and by nothing else. This does not admit the file: condition 2 is over the file as it now stands, and it fails. No judgment line is copied from it.

### 2.3 Per-route coverage

Each covered route's judgment line is reproduced byte for byte from the authenticated file named with it (extracted programmatically, then diffed against the source).

R01 — covered; step A-P1, file digest `52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | satisfied | by reference | evidence: rc.2 "Interpretation cannot treat absence as immateriality without a recorded basis and authority" against tenant "Conserves AC-017" under P1 Interpretation | residual: none
```
R02 — covered; step A-P1, file digest `52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | satisfied | by reference | evidence: rc.2 "Structural success is evidence for semantic review, not a substitute for it" against tenant "structural success never establishes fidelity" | residual: none
```
R03 — covered; step A-P1, file digest `52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-019-valid-model | satisfied | by reference | evidence: rc.2 "No generic checker may claim the semantic or authority subset unless the model supplies an exact lawful decision contract" against tenant "a semantic decision is lawful only under an exact decision contract" | residual: none
```
R04 — covered; step A-P1, file digest `52603712d5138916689ad0f6b13ebe9896074b7ca871ff1e6ffc51e62b42f78f`, judgment line carried unchanged:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | satisfied | by reference | evidence: rc.2 "Shared material does not establish identical meaning, basis, authority, or result" against tenant "Conserves ... RF-008" under P1, whose "two contracts give one representation two meanings" is compatible | residual: none
```
R05 — covered; step A-P2, file digest `2cd360b5e2c74b557bce07efb2e768ba39828f84721c6c5adf6755c65d174364`, judgment line carried unchanged:

```
ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | falsified | restated | evidence: rc.2 says "No universal resource quota or separate accounting carrier follows." The tenant says "every activation declares a token allowance before it begins, as UP-014 requires." | residual: The rc.2 section states no per-activation allowance obligation. It says the method's own execution work serves "an identified change, decision or assurance need" and that reuse is subject to "exact applicability and invalidation". The seeded obligation is not stated there, and the section's "No universal resource quota" statement contradicts it.
```
R06 — covered; step A-P2, file digest `2cd360b5e2c74b557bce07efb2e768ba39828f84721c6c5adf6755c65d174364`, judgment line carried unchanged:

```
ROUTE DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | satisfied | by reference | evidence: rc.2 says "Prime review accounts for governance cost as well as implementation count." The tenant only lists UP-005 under P2's "Conserves" with no restated content. | residual: none
```
R07 — covered; step A-P3, file digest `23cf09af7ac186cb6e09ce4f9261ab0374d2dd05340593e61a1967c832f545c5`, judgment line carried unchanged:

```
ROUTE SPEC_METHOD.md#recursive-product-taxonomy | satisfied | by reference | evidence: "The role creates no new Product identity" and "do not confuse an immutable RC release cut or installed product with the mutable source project" bear on P3's "Conserves ... the recursive Product taxonomy" under Identity | residual: none
```
R08 — covered; step A-P3, file digest `23cf09af7ac186cb6e09ce4f9261ab0374d2dd05340593e61a1967c832f545c5`, judgment line carried unchanged:

```
ROUTE WORLD_MODEL_METHOD.md#entity-cut-construction-law | satisfied | by reference | evidence: "identity, boundary, authority, state, evidence, treatment, covariance, and ambiguity" and "Boundary is interventional in character" bear on P3's "Conserves ... Entity Cut Construction Law" and "a boundary is a claim with a proof obligation" | residual: none
```
R09 — covered; step A-P4a, file digest `ec696190b548c65db5c40f8e0e379267e8dc805eab13801fee6347c1a2c352a4`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition | satisfied | restated | evidence: "Composition retains both traversal identities, intermediate results, judgments, evidence, authority, provenance, and stop states" matches the tenant's "composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states"; "first result type and judgment satisfy the second traversal's exact domain and preconditions" matches "first's result type and judgment satisfy the second's domain and preconditions" | residual: The tenant says "steps" where AC-016 says "traversals". Whether the two terms denote the same thing is defined outside the given text, and nothing given contradicts it. The tenant omits AC-016's rule that composition cannot flatten proposal, evaluation and decision, and its statement that no universal F_P -> F_D -> F_H sequence is prescribed. The omission does not contradict AC-016.
```
R10 — covered; step A-P4a, file digest `ec696190b548c65db5c40f8e0e379267e8dc805eab13801fee6347c1a2c352a4`, judgment line carried unchanged:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | satisfied | by reference | evidence: "Composition law is required only when the governing evaluation combines their internal variables" and "Independently activated evaluations may instead return closed results to one declared conjunction or decision rule" bear on the tenant's "Two steps compose only when…" and "Conserves … RF-010" | residual: The tenant names RF-010 as conserved without restating it. Nothing in RF-010 contradicts the tenant's conditional typing rule, which applies only once composition occurs. RF-010's subject is frames and when composition law is required. The tenant's subject is composition of steps. The text does not show that the tenant section reads RF-010 as a general composition requirement.
```
R11 — covered; step B-P4b, file digest `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | satisfied | by reference | evidence: "remains in `X` until an authorized disposition creates an exact successor model" bears on the tenant's "residual" typed instance in "Reframed from AC-009" | residual: none
```
R12 — covered; step B-P4b, file digest `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-013-transformation | satisfied | by reference | evidence: "Material residuals remain in the successor residual set" and the preserved/removed/introduced delta bear on the tenant's "transition" typed instance and "each continues to govern its own scope" | residual: The tenant's count of "nine statements of conservation" across the five clauses cannot be checked from this section alone.
```
R13 — covered; step B-P4b, file digest `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28`, judgment line carried unchanged:

```
ROUTE AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | satisfied | by reference | evidence: "retain their declared semantic, operation, evaluation, and decision authority" bears on the tenant's "authority" typed instance in "Reframed from AC-005" | residual: none
```
R14 — covered; step B-P4b, file digest `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28`, judgment line carried unchanged:

```
ROUTE DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | satisfied | by reference | evidence: "A bounded local action conserves governing truth; it does not rewrite it" bears on the tenant's "frame" typed instance in "Reframed from UP-017" | residual: none
```
R15 — covered; step B-P4b, file digest `bd56c2dcf857e588d6dea20d84619710f4202c384fcd389e4c9af97e0e0ebe28`, judgment line carried unchanged:

```
ROUTE SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | satisfied | by reference | evidence: "Their production and invalidation must be recoverable" and "Admission is one semantic commit of the complete transition" bear on the tenant's "transition" and "successor claim" instances in "Reframed from UP-021" | residual: The section's main subject is admission of a complete enclosing relation, so it is only partly a conservation statement. The tenant's mapping of it to typed instances is not contradicted. The tenant's count of nine statements cannot be verified from this section alone.
```
R16 — uncovered. Planned slot B-P5 (R_B MANIFEST.md row `R16 | B-P5 | produced`). Condition 1 holds (measured event 2026-10-11T14:43:22.397798Z: tenant block sha `1c7b224b…`, card sha `068e5b36…`, section present in the measured context). Condition 2 fails: actor_ended event 2026-10-11T14:43:32.943079Z logs output_sha256 `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9` (1612 bytes); the file `steps/B-P5.out.md` as it now stands digests to `81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b` (1605 bytes). The judgment in that file is not authenticated and is not copied. Run A's grant allows zero actor starts, so this step cannot produce coverage.
R17 — uncovered. Planned slot B-P5 (R_B MANIFEST.md row `R17 | B-P5 | produced`). Condition 1 holds (measured event 2026-10-11T14:43:22.397798Z: tenant block sha `1c7b224b…`, card sha `068e5b36…`, section present in the measured context). Condition 2 fails: actor_ended event 2026-10-11T14:43:32.943079Z logs output_sha256 `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9` (1612 bytes); the file `steps/B-P5.out.md` as it now stands digests to `81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b` (1605 bytes). The judgment in that file is not authenticated and is not copied. Run A's grant allows zero actor starts, so this step cannot produce coverage.
R18 — uncovered. Planned slot B-P5 (R_B MANIFEST.md row `R18 | B-P5 | produced`). Condition 1 holds (measured event 2026-10-11T14:43:22.397798Z: tenant block sha `1c7b224b…`, card sha `068e5b36…`, section present in the measured context). Condition 2 fails: actor_ended event 2026-10-11T14:43:32.943079Z logs output_sha256 `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9` (1612 bytes); the file `steps/B-P5.out.md` as it now stands digests to `81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b` (1605 bytes). The judgment in that file is not authenticated and is not copied. Run A's grant allows zero actor starts, so this step cannot produce coverage.
R19 — uncovered. Planned slot B-P5 (R_B MANIFEST.md row `R19 | B-P5 | produced`). Condition 1 holds (measured event 2026-10-11T14:43:22.397798Z: tenant block sha `1c7b224b…`, card sha `068e5b36…`, section present in the measured context). Condition 2 fails: actor_ended event 2026-10-11T14:43:32.943079Z logs output_sha256 `9bd86b6c3f5f3f44eee7a900c9b186db3ddf34ef6f123eb839b1e258183f88e9` (1612 bytes); the file `steps/B-P5.out.md` as it now stands digests to `81f1c93556f1fee7f10b3ae658ea63946660c69d8377ea5b6e61d2bdbc00880b` (1605 bytes). The judgment in that file is not authenticated and is not copied. Run A's grant allows zero actor starts, so this step cannot produce coverage.
R20 — covered; step B-P6, file digest `45f0642c5bc3b9a4f50967b76fbb851364fdc794a679ac09566bf7a66e88f8e7`, judgment line carried unchanged:

```
ROUTE SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | satisfied | by reference | evidence: "semantic basis", "evidence basis" and "state projection" are distinguished; P6 lists UP-008 among the clauses it conserves, beside "evidence supports a claim on a basis" | residual: none
```
R21 — uncovered. No step was produced for it: R_B MANIFEST.md row `R21 | — | planned, not executed`; R_B lifecycle.jsonl (digest `9a4deff9…`) holds no measured, actor_started or actor_ended event naming `SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022`; no file under R_B/steps/ carries a ROUTE line for it. This is uncovered required coverage, not an omitted judgment. Run A's grant allows zero actor starts, so this step cannot produce coverage.
R22 — covered; step B-P6, file digest `45f0642c5bc3b9a4f50967b76fbb851364fdc794a679ac09566bf7a66e88f8e7`, judgment line carried unchanged:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | satisfied | by reference | evidence: "does not mint, widen, transfer, or reconstruct ... authority from ... evidence shape"; P6 says "authority permits or disposes within scope; neither is minted by the other" | residual: none
```
R23 — covered; step B-P6, file digest `45f0642c5bc3b9a4f50967b76fbb851364fdc794a679ac09566bf7a66e88f8e7`, judgment line carried unchanged:

```
ROUTE REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | satisfied | by reference | evidence: "Evidence supplies observations" and "Decision authority disposes the result"; P6 says "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none
```

Admitted coverage C = {R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R20, R22, R23}; |C| = 18. Every member of C is authenticated by a measured event carrying V's and the card's digests, an actor_ended digest equal to the current file digest, and a ROUTE line naming the contract's section for that route.

### 2.4 Failure set

One covered judgment is falsified: R05 (step A-P2, file digest `2cd360b5…`, actor_ended 2026-10-11T14:42:51.206008Z). Its line, with its evidence, unchanged:

```
ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | falsified | restated | evidence: rc.2 says "No universal resource quota or separate accounting carrier follows." The tenant says "every activation declares a token allowance before it begins, as UP-014 requires." | residual: The rc.2 section states no per-activation allowance obligation. It says the method's own execution work serves "an identified change, decision or assurance need" and that reuse is subject to "exact applicability and invalidation". The seeded obligation is not stated there, and the section's "No universal resource quota" statement contradicts it.
```

The step actor's falsifier is the rc.2 sentence it quotes, "No universal resource quota or separate accounting carrier follows.", against V's P2 sentence "every activation declares a token allowance before it begins, as UP-014 requires" (V.md, digest `1c7b224b…`, paragraph P2). This run does not re-judge the route; it carries the actor's judgment as authenticated.

### 2.5 R minus C

| Route | rc.2 section | Reason uncovered |
|---|---|---|
| R16 | `REFERENCE_FRAME_METHOD.md#rf-012-closed-results` | planned slot B-P5 fails condition 2 (logged `9bd86b6c…`, file now `81f1c935…`); no actor start permitted in run A |
| R17 | `REFERENCE_FRAME_METHOD.md#rf-014-capability-fit` | same |
| R18 | `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` | same |
| R19 | `DESIGN_MODULE_METHOD.md#8-totality-rule` | same; this is the route whose evidence text was altered |
| R21 | `SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022` | planned, not executed: no step, no log event, no file; no actor start permitted in run A |

|R minus C| = 5. R21 is uncovered required coverage, carried as such; it is not a judgment of any member and is not dropped.

### 2.6 Refused bundles

R_C is refused. Reason: it binds another basis. Every measured event in `R_C/lifecycle.jsonl` (`65f3fd3d…`) carries the tenant block `FOUNDATIONS.md#3-commitments` with SHA-256 `d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf`; the contract's subject is V with SHA-256 `1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4`. Equal field shapes (same card, same rc.2 sections, same ROUTE line format in C-P1 to C-P3) do not supply a valid join; the typed precondition is the basis digest. None of R_C's ten judgments enters C. In particular, `C-P2.out.md` (`6731e7a1…`) judges the UP-014 route satisfied on that other basis; that judgment is not carried into this composite and does not offset R05. No composite relation over the two bases is declared by this contract (FOUNDATIONS §2, basis; P4a).

Observations about R_C recorded for its owner, not acted on: (a) `C-P4a.out.md` (`167c9aad…`) writes its two ROUTE lines as `ROUTE FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-016-typed-composition` and `ROUTE FOUNDATIONS.md#3-commitments→REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand`, a form that names no route in the contract's table (condition 3 would also fail for them under any contract using this table); (b) the first of those is judged `out_of_frame`, not satisfied, so CASE.md's description "Its step actor judged all ten routes satisfied" does not match the bundle for that route (nine satisfied, one out_of_frame). Neither observation changes the refusal or the composite.

## 3. Composite result and its computation

The contract's rule, applied in its declared order over R:

1. satisfied requires every route in R covered and every covered judgment satisfied. Not met on either count: five routes are uncovered (§2.5) and one covered judgment is falsified (§2.4).
2. otherwise falsified if any covered judgment is falsified. R05 is a covered, authenticated, falsified judgment. The composite is therefore falsified.
3. The invalid_basis, out_of_frame and indeterminate clauses are not reached. The out_of_frame clause's condition ("any route is uncovered and the joining step cannot produce coverage within its grant") does in fact hold for R16 to R19 and R21; under the contract's declared order it does not select the member, and the uncovered set is carried with the composite instead (CALCULUS §3: an application declares its own order among non-satisfied members; FOUNDATIONS §4: a known failure and an uncovered obligation survive every join).

Composite: falsified.

The composite record is §2.3 (every covered judgment line unchanged), §2.4 (the failure set with its evidence), §2.5 (R minus C with reasons), §2.6 (the refused bundle with its reason) and §4 (conservation accounting). Nothing is summarised in place of a judgment line.

## 4. Conservation accounting of the join (FOUNDATIONS §4, AC-013 fields)

Preserved:
- the 18 covered judgment lines, byte for byte, with their verdicts, evidence and residual text, from files `52603712…`, `2cd360b5…`, `23cf09af…`, `ec696190…`, `bd56c2dc…`, `45f0642c…`;
- the failure R05 with its quoted evidence;
- the uncovered obligation R21 as a planned slot with no result (R_B manifest row), not dropped and not converted into a judgment;
- the four B-P5 slots R16 to R19 as planned slots whose result fails authentication, not dropped and not copied;
- the production provenance of every admitted step: measured block (cap, bytes, fit, component digests), actor_started input digest, actor_ended output digest, model id, token and cost counters, by reference to `R_A/lifecycle.jsonl` (`bbf1e3cd…`) and `R_B/lifecycle.jsonl` (`9a4deff9…`);
- bundle R_C intact and untouched, with its own provenance (`65f3fd3d…`), preserved as refused material outside C;
- the identities of both joined bundles and of the subject V, by digest.

Introduced:
- the composite member (falsified) and its computation (§3);
- the coverage set C, R minus C with reasons, and the per-slot authentication findings (§2.2), including the B-P5 digest mismatch and the in-memory observation that the mismatch is exactly the one declared substitution;
- the refusal of R_C with the basis mismatch named by digest, and the two observations about C-P4a;
- the triage record (§5);
- this return record and its accounting.

Removed: nothing. No judgment line was removed, shortened or paraphrased; no bundle file was altered; R_C's judgments were never admitted, so their exclusion is a refusal at the precondition, not a removal from C.

External resolution witnesses: the instrument's `lifecycle.jsonl` events named by timestamp above; the file digests in the intake table; the `wc -c` sizes.

Residuals:
- RS-1. The rc.2 manifest digest `3d860ff4…` the contract names is not recorded in any bundle event or manifest and cannot be recomputed under this grant. The rc.2 precondition is verified only to the cut's identity by path and to the per-section digests the instrument logged. An actor with read access to the installed cut can close this by computing the manifest digest.
- RS-2. R16 to R19 are uncovered pending re-production on basis V (run B grant, or any later activation with actor starts).
- RS-3. R21 is uncovered pending production on basis V.
- RS-4. R05's falsification is a detected failure in the subject V, triaged in §5 and not repaired here.
- RS-5. The card digest `068e5b36…` is attested by the contract and by every measured block; this run did not recompute it (the card is not a run A input).
- RS-6. The semantic correctness of the 18 carried judgments is the step actors'; this run authenticated them and did not re-judge them (the constructor may not judge rc.2 text). An independent assessor who needs its own judgment acquires its own evidence (CALCULUS §7).
- RS-7. CASE.md's description of R_C does not match `C-P4a.out.md` on the AC-016 route (§2.6). Fixture description defect; owner: case owner.
- RS-8. The run id carries the date 20261012 while `date -u` in this environment reports 11 Oct 2026 and the bundles were produced at 2026-10-11T14:42Z to 14:44Z. Recorded as observed; not resolved here.

## 5. Triage of the detected failure (SPEC_METHOD §4)

Detected failure: R05, the UP-014 route from V's P2, judged falsified by step A-P2 (§2.4). The failing text is V's P2 clause "and every activation declares a token allowance before it begins, as UP-014 requires" (V.md `1c7b224b…`). The live tenant standard `standards/FOUNDATIONS.md` (`2f15c6c1…`, read in this run) does not carry this clause in its P2; the failure is confined to the fixture subject V.

Change intent. Remove the clause from P2 or re-source it correctly. The corpus already states an allowance rule, in CALCULUS §6 (`b5fb31de…`): "Where capability fit or a cost claim is the governed question, the activation declares its allowance and reports spend with its measurement source", marked there as "new; P0 with UP-014's selection rule", with "Cost is selected, not universal" and "No universal quota, ticket count, actor count or accounting carrier follows". V's clause states a universal obligation ("every activation") and gives it the standing conserved-from-UP-014; under FOUNDATIONS §1 a clause has one standing, and the step actor's quoted falsifier is the same "no universal quota" rule the corpus itself restates. The intent is therefore to make P2 state no more than its conserved routes support: either delete the clause (P2 then reads as FOUNDATIONS §3 proper) or replace "as UP-014 requires" with a reference to CALCULUS §6 and its selected scope, with standing new.

Class: realization_refactor. Upward walk: the work wave's goal and the intent (a faithful tier-1 corpus over rc.2) hold; the product shape holds; the requirement that every conserved route be faithful (FOUNDATIONS §1, the conformance discriminators) holds and is what detected the defect; the corpus design already places the allowance rule in CALCULUS §6 with the right standing and scope; the first defective layer is the document text of V's P2. The change is local to one clause with no intended upstream change. Two alternative branches are named for the owner, because the class depends on an intent only the owner can state: if the owner intends a universal per-activation allowance obligation, that contradicts CALCULUS §6 and FOUNDATIONS §3 P2's conserved routes and is a requirement_reprice at the shared WHAT, not a local edit; if the owner intends the allowance rule to become a P2 commitment rather than a CALCULUS §6 mechanism, that is a design_reframe of the corpus structure. Neither is selected here.

Re-entry point: paragraph P2 of `qualification/cases/T-03-04/subject/V.md`, at its owner. Any change to V changes the basis digest and invalidates every judgment on V before reliance (CALCULUS §7); all 23 routes would need re-production on the new digest.

Owner: the T-03-04 case owner (the Claude tenant author), who owns the fixture; Jim as decision owner for anything beyond the join. The constructor's grant excludes repairing V; the disposition under CALCULUS §3's disposition refinement is re_enter, recorded here and not applied.

When triaged: this activation, 2026-10-11 between 14:48:40 UTC and `Sun 11 Oct 2026 14:56:48 UTC`, at the point the join produced the failure set.

## 6. Accounting

Step actors started: 0 (allowance 0). `bounded_step.py` was not run. No step-actor tokens, list cost, model ids or measured bytes were produced by this run.

Coordinator (this activation): the harness's `total_tokens left` marker read 15000000 at activation and 14892424 at the last tool result observed before this record was composed, a consumption of about 107576 tokens to that point, excluding the composition and writing of this file. Source: the Claude Code harness context-budget marker shown to the constructor. Unverified counter; no list cost is available for it.

Standing basis, reported once in bytes: files read in full 120990 (CASE.md 10379, OUTER_CONTRACT.md 4884, V.md 6104, FOUNDATIONS.md 15218, CALCULUS.md 15850, EVALUATION.md 8042, SPEC_METHOD.md 11522, three manifests 8057, three lifecycle logs 26243, eleven `.out.md` files 14691); files digested but not read 284166 (projection 120805, eleven `.in.md` 147186, eleven `.usage.json` 16175); total 405156.

Production cost of the bundles as their manifests state it, carried as facts about the fixture and not as this run's spend: R_A 4 starts, 47137 context tokens, 3888 output tokens, USD 0.2123 list; R_B 3 starts, 38576, 3808, USD 0.1811; R_C 4 starts, 46405, 5432, USD 0.2249.

Wall time by `date -u`: start `Sun 11 Oct 2026 14:48:40 UTC`; end `Sun 11 Oct 2026 14:56:48 UTC`; elapsed `8 minutes 8 seconds`, within the 30-minute allowance.

## 7. Stop state, residuals, handoff

Stop state (CALCULUS §3, one core member): falsified. The activation's declared predicate is the contract's claim over V, computed by the contract's composite rule; the composite is falsified by R05, with R16 to R19 and R21 carried as uncovered. Under the construction-availability refinement this record is candidate_ready: the join was completed within grant and allowance and this file is a complete candidate for assessment. Next move named by the control model: re-entry at V's owner for R05 (§5); a later activation with actor starts for R minus C (path H1).

Residuals: RS-1 to RS-8 in §4.

Handoff. Each path names the envelope it needs and is executable from this file plus the named inputs, without this run's conversation.

H1. Produce coverage for R16 to R19 and R21 (run B grant: at most 4 step-actor starts through `qualification/instruments/bounded_step.py` with `qualification/instruments/ROUTE_CARD.md`, V as the tenant block, cap 40000 bytes). One step over the P5 routes (`rf-012-closed-results`, `rf-014-capability-fit`, `ac-007-constraint-and-refusal`, `8-totality-rule`; the original B-P5 context measured 11400 bytes) and one step over the P6 route `assurance-boundary-congruence-and-method-qualification-stdo-up-022` (the original three-section B-P6 context measured 10971 bytes, so one section fits the cap). Then: authenticate each new step by the three conditions of §2.2, recompute C and R minus C, and recompute the composite. While R05 stands, the composite stays falsified; if the new judgments are all satisfied and authenticated, R minus C becomes empty and the composite is falsified by R05 alone. Do not reuse any line from the current `B-P5.out.md`.

H2. Dispose R05 (owner: case owner; envelope: owner decision, no actor start). Choose among the three branches in §5. If V changes: new V digest, new contract subject, all 23 routes re-produced (the original grouping was 7 steps, 51501 plus 47959 bytes into actors); every judgment on `1c7b224b…` is invalidated for the new subject and preserved as history. If V is kept as a seeded fixture, record that the falsification is the intended observed failure and close the triage as carried.

H3. R_C: no resumption path under this contract. R_C may be joined only under a contract whose subject digest is `d654d395…` (FOUNDATIONS §3 proper), where its C-P4a ROUTE line form and the out_of_frame AC-016 judgment (§2.6) would have to be disposed by that contract's owner.

H4. Close RS-1 (envelope: read access to `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/`, no actor start): compute the installed cut's manifest digest and compare with `3d860ff4…`; if unequal, the rc.2 precondition fails for every bundle and this composite is invalidated before reliance.

H5. Assessment (EVALUATION §3, §4): an assessor other than the author reads this directory at a named commit, records expectations from the two common sources first, and returns a review result over E1 to E6. Freshness of the author's model family does not give assessor independence.
