# Evidence Carrier: STDO 2.4.1 Fresh-Constructor Qualification

- recorded_at: 2026-08-17T04:03:50Z
- actor: Claude Opus 5 fresh capable constructor
- session_id: `e212d5eb-dd92-43a7-8e27-2542e7aef375`
- frozen_result_uuid: `f8bc286f-820b-4288-818b-8636f8ad1a1b`
- relation: compact projection of the constructor result frozen before
  independent release review
- repository_edits_by_constructor: none

## Frozen Constructor Projection

# STDO 2.4.1 Amendment Qualification — Durable Trial Record

## 1. Actor, Session, Independence, Freeze

**Actor.** Fresh capable constructor for the STDO `2.4.1` amendment trial; distinct from the STDO 2.4.1 authoring Worker (`input_owner`). Constructor result under `SPEC_METHOD.md` `STDO-UP-022` — not evaluator, Reviewer, or Executive.

**Two-segment session, one envelope.** Segment 1: read-only evaluation of all 23 cases, shell denied. Segment 2: authorized read-only identity/inventory verification only. **No repository edit, tag, push, or publication in either segment.**

**Freeze.** The 23-case evaluation was frozen at the end of segment 1, **before any digest was computed**. Segment 2 confirmed the subject and changed no result. This document is a projection of that frozen result, not a new evaluation.

**Non-authorship.** No byte of any candidate, protected, or input file was authored by this actor.

**Reference-exposure boundary (held across both segments).** Withheld and never read: expected-output/answer-key artifacts; prior qualification results; prior review verdicts; `.ai-workspace/comments/` except the one declared-input file; `.ai-workspace/tickets/`; ABIogenesis material; author memory. `authority_compressions/*` and `templates/*` were digest-verified but **never read as content** — release members, not directly cited governing standards.

**Envelope.** Candidate `DESIGN_MODULE_METHOD.md` (`STDO-UP-023`, §5E, §6A/§6B), candidate `STDO_REFERENCE_FRAME_BASELINE.md` (Profile Terms, Derived Product Testing Frame Set, Profile Qualification), cited `SPEC_METHOD.md` `STDO-UP-022`, `REFERENCE_FRAME_METHOD.md` (result algebra, Result Conjunction, Frame Relations), `PRODUCT.md`, `releases/v2.4.1.md`, declared-inputs file. No supplemental method or authority input.

## 2. Verified Identities — all matched

| Element | Verified value |
|---|---|
| candidate standards aggregate | `0f46a3d583f321da0445331566ef878e11e19e16e71c54fb9a8e66c5fff4ce91` |
| `DESIGN_MODULE_METHOD.md` | `89659b99abe7af87a7cc0241d9f167b8a74acdbfe7b721544151cd1ce5d876d1` |
| `STDO_REFERENCE_FRAME_BASELINE.md` | `1d208cc2b141ba3717b5842ce0ad881fe6662c58a55e3f3cdd170af1d5f61bed` |
| `design_module_method.compressed.md` | `393db42220fed186500b8c4b8f77e66de1994ac36ff248926f379df6441aa4bb` |
| `stdo_compressed.md` | `7ad8a3908bfef4d6efa932289ad623726ab55f18e7ba855b01c8717707775b9d` |
| `AGENTS_TEMPLATE.md` | `4f8d04243b0b74b13dffdc31975c30a88ec4a96de7edf29d0a9aa144e5d68a85` |
| `CLAUDE_TEMPLATE.md` | `fb6482ae80e28cdeb1b2f2a94f4fa87f0ac5bed7b348e084746dbfc700f78475` |
| `specification/PRODUCT.md` | `aa1eb79808be2b82acc59d58b27965dbbce3d14135c11084461b7191493cf066` |
| `releases/v2.4.1.md` | `7756e23f34ccd06280549ebb81fb1cdd0a8b77da291516ddd46f16a511ca27ea` (previously self-referential; now independently confirmed) |
| declared input file | `f06e4b5be3dc5da79905469921e3f55706ae4cdd6d7f8b40a922ce72bdc6455e` |
| predecessor commit | `e05984c4f3b75525e6d962f6b9d72bbedd8e271a` (type `commit`) |
| annotated tag | `66118f3c5808536df5e5393d725e54e4eebc45f4` (type `tag`, name `v2.4.0`, target `e05984c4…`) |
| predecessor aggregate | `1571aab5bf9cc3605222d79502117c4873e4e5e136e07f909f4d4ad3684a4cc5` |
| inventory | 43 members predecessor, 43 candidate |
| disposition | **6 changed (`M`), 0 added, 0 removed, 37 byte-conserved** — confirmed by `git diff --name-status` and digest-set intersection |

**Verification: `satisfied`.** The evaluated bytes are the declared candidate subject. **G-1 closed.** No mismatch, so `invalid_basis` does not apply.

## 3. Derived Foundation-Selection Outputs

**Normalized capability `CAP-N1`** (labels `ATLAS`/`route`/`engine`/`route_core.ts` removed per DMM 590): *deterministic traversal over an immutable directed multigraph providing (a) stable total successor ordering under a declared key, (b) cycle detection, (c) path enumeration bounded by an explicit parameter, (d) total explicit typed failure values for cycle-detected, bound-exceeded, and malformed-input conditions; no hidden global or mutable state; identical results across repeated executions on equal input.*

**Relation/mechanics factoring.** Authority-bearing: `ROUTE-VALIDATE-R3` (owner `AT-ROUTE`; semantic validator; subject admitted `RouteSet@AT-B0`; scope route identity, edge endpoint existence, declared direction; basis `AT-PRODUCT-7 + ROUTE-SCHEMA-3 + AT-B0`; lifecycle after admission before traversal; refusals missing endpoint, duplicate identity, unsupported direction; excluded meaning traversal order, signing policy, store admission, release disposition, Product acceptance) and `AT-BUILD`'s traversal + canonical bundle construction. Mechanics: all of `CAP-N1`, owning nothing. Load-bearing: edge endpoint existence is computable by any mechanic, but its **meaning as a route-semantic refusal on the declared basis** is `AT-ROUTE`'s (DMM 600).

**Hard eliminations** (DMM 647). `LINEAGE-G3` — two independent grounds: lacks bounded path enumeration; cycle failure aborts without typed locus. `LOCAL-G1-R2` — authority posture as stated mixes `AT-ROUTE` refusal with traversal; under the alternative reading (posture describes incumbent `G1`) it is dominated instead — off-frontier either way.

**Dominance** (strict four-part test, DMM 654–660). `G4 ≻ LOCAL-G1-R2` and `G5 ≻ LOCAL-G1-R2` — established. `G4 ≻ NATIVE-G2` — established **conditionally**: license evidenced non-discriminating because runtime `R20` is already the Product's admitted substrate and `G2` adds no external package; **falsifier** — if `R20`'s license cannot be evidenced inside the admitted Apache-2.0-compatible posture, dominance fails and `G2` returns to the frontier. `G4` vs `G5` — **not established either direction** (`G4` better on fit, integration/migration, proof, exit; `G5` strictly better on runtime 29 vs 34 ms). `G5 ≻ NATIVE-G2` — **not established**: exit/reversibility not evidenced as comparable.

**Undominated frontier:** `{ FOUNDATION-G4, FOUNDATION-G5 }`, plus `NATIVE-G2` iff the `R20` falsifier fires.

**Owner-priority disposition (`AT-DESIGN`): `FOUNDATION-G4`** — derived, held open by F-03. P1 hard constraints: all preserve `AT-ROUTE`; `G4`'s optional assigned role does not change ownership (630–633) → non-selecting. P2 determinism/recovery outrank runtime *below 75 ms*: 34/29/42 all below → **runtime demoted, `G5`'s 5 ms advantage non-decisive**; `G4` unconditioned typed cycle+bound failures vs `G5` deterministic only after a local adapter vs `G2` locally composed algebra → `G4`. P3 proof/integration/deletion: `G4` lowest on all three. P4 supply-chain currency: all pass, `G5`'s advisory resolved, `G4` no worse.

## 4. F-01 .. F-12

| Case | Result | Decisive evidence | Residual | Invalidation |
|---|---|---|---|---|
| F-01 | `satisfied` | pass triggered (587); `CAP-N1` delabelled (590); mechanics separated per eight-field schema (592–600) | labelled phrase must not re-enter as a comparison constraint | change to `AT-PRODUCT-7`, `ROUTE-SCHEMA-3`, or `AT-B0` |
| F-02 | `satisfied` — pass not required | 693–695 exempts a trivial helper that cannot affect authority, Product behavior, lifecycle cost, or the design network; all four negatives hold | exemption conditioned on all four continuing to hold; not a class exemption | helper becoming a public contract or crossing an effect/authority boundary |
| F-03 | `satisfied` (structure) / `indeterminate` (residual materiality) | seven fields × five categories present; four residuals disposed immaterial with reasons; **maintained-external is not** — 617–619 requires the immateriality reason | one registry's entries never assessed for deterministic ordering, inside the category holding both frontier members; two lawful readings, record states neither. Version basis asserted, not exhibited | **617 holds selection closure open** |
| F-04 | discovery `falsified`; selection `invalid_basis` | 613–614: an unsearched category records `not_applicable` or a named gap with reason; neither present → no lawful discovery basis | none — structural | **fails on structure alone**; that the removed category held both frontier members is incidental |
| F-05 | `satisfied` | §3 eliminations, dominance, frontier derivable from `EVID-7` | `G2` membership hinges on the `R20` falsifier; `G5 ≻ G2` unestablished on exit | new evidence on `R20` license, `G2` exit cost, or `G1-R2` posture |
| F-06a | relation `satisfied`; disposition `FOUNDATION-G4`; closure `indeterminate` | P1–P4 as §3; 663 non-operative (no breadth claimed) | falsifiers per 671 — `G5`: adapter-conditioned determinism + adapter-order proof + adapter-deletion exit at a non-decisive runtime edge; `G2`: 180-line composition + required property proof | derived but **not closed** — F-03 holds it open; also re-enters on ceiling, priority, or basis change |
| F-06b | `indeterminate`; `re_entry_requested` to `AT-DESIGN` | 665–669: selection lawful **only** through priorities declared for the exact Product and basis; otherwise an explicit design gap | frontier `{G4, G5}` intact | **not resolved by** runtime, dependency count, line count, source order, familiarity, sunk cost, or local-code preference (626–629, 669–671) |
| F-07 | `falsified` — `G4` eliminated | 647: hard licensing failure eliminates; **elimination branch, not a weighted dimension** | reduced frontier resolves to `FOUNDATION-G5`, still held open by F-03 | **superior runtime cannot rescue a GPL-only candidate** — `G5`'s best-in-ledger 29 ms is unavailable to `G4` as an offset |
| F-08 | `satisfied` — lawful assigned role | 673–676: assigned role lawful when owner, role kind, subject, scope, basis, lifecycle, refusal invariants preserved; all eight verified; excluded meaning not widened; 679–681 ownership follows the relation | assignment must be recorded in accepted design; capability beyond scope stays unassigned | 672: reuse confers no authority; any widening re-enters at `AT-ROUTE` |
| F-09 | `falsified` — three independent grounds | (1) signing policy is `AT-SECURITY`'s and in `R3`'s excluded meaning → widening (676–677); (2) publication admission is `AT-STORE`'s / release `AT-RELEASE`'s → widening + second admission relation, `STDO-UP-016` falsity condition (831–834); (3) reminting owner as `FOUNDATION-G4` contradicts 679–681 | none — decided by text without inference | all dependent selection evidence and design acceptance void; re-entry at `AT-ROUTE`, `AT-SECURITY`, `AT-STORE`, `AT-RELEASE` |
| F-10 | `falsified`; evidence invalidated; relation re-enters | 618–620: a later applicable candidate that could materially alter the frontier invalidates affected selection evidence; `G6` also satisfies dominance, and 659–660 forbids selecting a dominated candidate | if any material unknown remains on `G6`, dominance unestablished (658) — `G6` joins the frontier and F-06 re-runs over `{G4,G5,G6}` | the `DISC-7` cutoff does **not** protect the prior selection (617) |
| F-11 | `satisfied` | 685–687: the subproblem recursively re-enters before its implementation is retained; nested pass needs its own normalization, discovery, ledger, dominance, frontier, priorities; retained code provisional | nested pass has its own residuals; inherits no closure | if the subproblem changes a material parent dimension, the **parent** selection re-enters; 687–689 distinguishes this from §11C recurrence extraction |
| F-12a | `falsified` twice over | 626–629 excludes source-order/sunk-cost preference; `G3` independently eliminated. Lawful contrast: 621–626 lets a predecessor *constrain the admitted set at migration altitude* — a different, externally owned relation | none | 670–671: unsupported preference is not design closure |
| F-12b | `falsified` | 682–683: generic local code "is lawful only when it wins the same comparison; it is not the default"; local-code preference named in 628; `G1-R2` eliminated or dominated | none | 660–661: local rebuild inadmissible when a lawful foundation composition dominates it |

## 5. Testing-Frame Configuration

| Frame | Claims | Subject / path | Population | Oracle | Falsification |
|---|---|---|---|---|---|
| User acceptance | `CL-U1` live, `CL-U2` harnessed (`SIGN-FAKE`) | `ATLAS-7@install-44` via `atlas build routes.yaml --output atlas.bundle` as `route-editor` | goal, entry, permissions, inputs, configuration, ordinary dependencies, declared substitution, visible state, refusal/recovery | Product-defined outcome — exact admitted bundle or typed refusal — from Product law | user cannot obtain the outcome through the supported surface, or only via hidden setup/unavailable capability |
| End to end | `CL-E1` required-path, `CL-E2` forbidden-path | same subject; CLI → admission → validation → traversal → bundle → signature → store → receipt | every material owner edge, exact identities, owner-issued projections, competing paths | accepted-design composition law + owner-issued receipts per edge | a material edge unexercised, **or** outcome via bypass/obsolete executor/fallback/competing authority — equal output no defense (160–163) |
| Integration | `CL-I1` real, `CL-I2` substitute (narrowed) | `AT-BUILD → AT-SECURITY`, one boundary | graph kind 3 × cycle state 3 × policy 2 × retry 3 = **54** | declared joint interface contract | a covered combination violates the joint contract |
| Unit | `CL-N1` `receipt_format`, `CL-N2` `route_traversal` | one exact module boundary + revision, module-bounded | module-owned laws, operators, states, transitions, boundary classes, failures | **independently derived from the owned law** (482, 494–496) | a module-owned law fails on a module-bounded case |

**Conjunction (derived).** Mandatory: `CL-U1`; `CL-E1` **plus** forbidden-path exclusion (both sides, 575–580); `CL-I1`; both unit lanes. Narrowed-admissible: `CL-U2`, `CL-I2`, each only for its declared claim. Agreeing basis: subject `ATLAS-7@install-44`, checkpoint `AT-B0`, ordinary-path identity, configuration identity, module revision. Decision authority: `AT-RELEASE` / `AT-PRODUCT` — 408 bars testing frames from minting it; RFM 631 bars authority transfer. Veto: a falsified forbidden-path exclusion vetoes the path claim regardless of other green. Missing/indeterminate mandatory result → `indeterminate`, not a decision. **Applied to this evidence, `conjoin` returns `conflict`** (`CL-E2` veto; `MUT-2` self-invalidation; `AQ-2` inadmissible; `AQ-3` gap; `CF-3`/`CF-4` unresolved). 638–641: conflict remains visible and **cannot be hidden by aggregate green**. This is a conjunction result form, not a release grade.

**Production closure — `falsified` on the declared scope.** `PATH-POS` establishes required-path reachability (side 1). `PATH-NEG` and `CL-E2` **contradict each other over the same graph**: one asserts `legacy-build` unreachable/fail-closed, the other asserts it reachable from the supported CLI under one configuration. 585–590 places configuration switches and fallbacks inside production closure. Inside the claimed scope → `PATH-NEG` falsified; different configuration → bounded, side 2 `indeterminate`. **Not established under either reading.**

**Assurance/source closure — `falsified` by `SRC-OLD`, lawful for `TEST-SEAM`.** `SRC-OLD` fires both disjuncts of 598–600 independently: manufactures aggregate green without executing the installed Product, **and** reintroduces the removed path via its `legacy-build` import. `TEST-SEAM` satisfies all three conditions of 596–598 (isolated from distribution, excluded from ordinary-path evidence, declared) — **lawful and explicitly not a production-path failure**; conditioned on continued exclusion.

## 6. T-01 .. T-11

| Case | Result | Decisive evidence | Residual | Invalidation |
|---|---|---|---|---|
| T-01 | `satisfied` | frames derived from claim/subject/path/population/oracle/falsification; 147–149 denies frame status to files, suites, runners, labels, coverage, actors | `CL-E2`'s configuration identity not exhibited though 436 requires it | any change to subject, path, population, oracle, falsification |
| T-02a | `satisfied`, bounded; supplies **mandatory live-mode** signing evidence | 424–427: live sandbox UAT mandatory where a claim depends on real external compute/transport | one scenario; other populations, refusals, recovery unevaluated | dependency/mode, role, capability, configuration, acceptance-meaning change (413) |
| T-02b | `satisfied` only for exercised composed relations; **cannot close live signing** | 421–424 limits a substitute to relations actually exercised; 426–427: harnessed green and substitute-based unit/integration/E2E "are not sufficient" | live signing boundary unevaluated | no volume of substitute-based evidence closes a live-signing claim; only `CL-U1`, only for what it exercised |
| T-03a | `satisfied` for exercised path/coordinates | 439 evidence set: entry invocation, semantic path and authority edges, owner receipts, durable events | supplies **only side 1** of 575–577 | superseded by T-03b |
| T-03b | `falsified` | 160–163 and 614: outcome through bypass/obsolete executor/fallback/competing authority falsifies path conformance **even with equal output**; reachability under a configuration places `legacy-build` inside production closure (585–590); `STDO-UP-016` 835–837 also falsified | none — equal bundle bytes are the trap this clause closes | all claims resting on path singularity lose basis; `CL-E1` retains only that the path *can* be traversed |
| T-04a | `satisfied` — both integration altitude | 459: no integration result establishes an unevaluated Product outcome; 466–469 restricts `CL-I2` to serialization, not live policy conformance | `CL-I2`'s equivalence boundary declared → narrowing lawful | participant substitution or interface/carrier revision (464) |
| T-04b | `satisfied` — reduction lawful | 54 full; all-pairs lower bound **9** (3×3), commonly 9–12, with the declared 3-way embedded; 561–563 permits reduction where residuals are retained — input uses the retain branch; 563–565 met for one high-consequence interaction | **derived gap: residual under-declared.** Input retains only 4-way; **3-way combinations other than the declared one are neither covered nor retained** (e.g. `(disconnected, stale, exhausted)`, `(malformed evidence, stale, exhausted)`) | residual statement must be extended before the result enters a conjunction |
| T-05a | `satisfied` — lane **required, small** | DMM 1778–1779 (code without a module-derived lane is not closure-ready); baseline 488–489 (every coded module; public contracts are valid subjects); 505–507 (low complexity justifies a small lane, **not omission and not hundreds of implementation-shaped tests**); derived from ownership (1740–1755), not helper layout | none | module boundary, owned law, or public contract change |
| T-05b | `satisfied` — same obligation, larger strategy | 481 evidence menu (equivalence classes, exhaustive where available, property-based, metamorphic, algebra oracles, boundary cases, killed mutations); oracle independence mandatory (482, 494–496); 498–501 redirect inapplicable — complexity is in owned law | cycle/ordering laws overlap `CL-I1`; the lane proves the law, not the composition | module revision, algorithm, state space, oracle, generator change (485) |
| T-05c | `satisfied` — complexity changes **size and strategy only** | 390–392, 489–490: complexity does not decide eligibility; 509–512: no Product, user, installed-path, cross-module, or release claim closes from unit evidence regardless of count, coverage, mutation score, runtime, or pass rate | 507: unit volume has no independent closure value | — |
| T-06 | relation `satisfied`; output on this evidence **`conflict`** | §5 conjunction | none for the relation | 638–641: conflict cannot be hidden by aggregate green; no lane mints another's claim |
| T-07a | side 1 `satisfied`; side 2 / production closure `falsified` | §5; 581–582: successor passing does not prove predecessor removal | the configuration coordinate decides between `falsified` and `indeterminate` | packaging, configuration-switch, registry, consumer, fresh-process change |
| T-07b | `falsified` | 598–600, both disjuncts independently | none | every closure that could have rested on `SRC-OLD`'s aggregate is suspect until re-established against the installed Product |
| T-07c | `satisfied` — lawful, **not** a production-closure failure | 596–598, all three conditions hold | conditioned on continued exclusion | packaging change moving it into distribution, or any ordinary-path use |
| T-08a | `satisfied` — lawful path-sensitive mutation | 615–617 satisfied: isolation ✓ (temporary copy), restoration unnecessary (original unmutated), exact-subject relation holds; supplies 609–610 evidence | none | — |
| T-08b | `falsified` — **self-invalidating** | 615–617: mutation without isolation, restoration, and revalidation invalidates its own assurance basis; **all three fail simultaneously**; `STDO-UP-022` exact-subject congruence breached | invalidated set **cannot be precisely bounded** — no temporal order declared; conservatively all install-bound results on `install-44` are suspect | **loses basis:** `MUT-2`'s own result; any `CL-U1`/`CL-E1`/`PATH-POS`/`PATH-NEG` observation at or after the edit (413/443 runnable-subject change); `CL-I1`/`CL-I2` if run against the mutated install (464). **NOT invalidated:** `CL-N1`/`CL-N2` — module- and revision-bound, not install-bound (485) |
| T-09a | `satisfied` — relations correct and separated | 645–649 acquisition through the exact owner surface; 654–657 equality/completeness/membership are admitted generic mechanics over owner-issued evidence; 660–663 oracle from Product/requirement/design law | bounded to what the projections expose | projection contract change at `AT-STORE` or `AT-BUILD` |
| T-09b | `falsified` — two independent grounds | 649–652 bars reconstructing owner state from raw payloads/events/**logs**/labels then grading it as the subject; 664–666 requires the actual owner-issued subject, not a second implementation of owner meaning; 657–659 bars generic mechanics from "choosing current history" — reconstructing the *current* store prefix is exactly that; the "Governor-like" label confers nothing (147–149) | none | all claims resting on `AQ-2` void; re-acquire via `projectAdmittedReceipt` / `projectBuildLineage` |
| T-09c | `indeterminate` + **named gap** to `AT-SECURITY` | 666–667: absent owner seam → named assurance/design gap; the harness does not fill it with rival semantics; inference from logs/timing/byte shape forbidden | `CL-I1`'s policy-dimension oracle is bounded to the request/response contract — narrower than policy conformance, and the narrowing must be retained | re-entry to `AT-SECURITY` to declare a seam; until then no frame closes the claim |
| T-10 | `satisfied` — all four forms exercised and distinct | §7 | — | none authorizes broader test expansion, compatibility repair, another controller, or reinterpretation of upstream meaning (690–693) |
| T-11 | `satisfied` — bounded enumerable residual and invalidation set derivable | §8 | bounded by the declared claims | §8 |

## 7. Four Causal-Frontier Forms

Line 674: earliest is **minimal under the declared causal relation, not first in log or clock order**; the graph uses owner edges.

| Case | Form | Frontier / owner | Evidence | Invalidated |
|---|---|---|---|---|
| CF-1 | **(i) unique locus** | malformed route-admission carrier — `AT-ROUTE` | sole causally minimal violated relation; all later failures derive from it | downstream traversal/bundle/signature/store observations lose independent falsification value — **consequences, not counterexamples**; no downstream repair authorized |
| CF-2 | **(ii) jointly established incomparable set** | `{invalid signature acceptance — AT-SECURITY; wrong-store admission — AT-STORE}` | incomparable in causal order, both established, **both necessary** | published-subject claim falsified; **both** relations re-enter; 688 forbids collapsing into one arbitrary owner — neither is exonerated by the other, repairing one leaves the explanation incomplete |
| CF-3 | **(iii) unresolved alternative frontiers** | `{store refusal before admission — AT-STORE}` **or** `{transport loss after admission}` | receipt absent; evidence supports either, cannot establish which | receipt-delivery claim unresolved, **both alternatives live**; 688 forbids reporting as a joint cause — explicitly not CF-2-shaped; resolution needs a seam distinguishing pre/post-admission state (same shape as `AQ-3`) |
| CF-4 | **(iv) `indeterminate`** | none — no bounded frontier | only a user-visible timeout; no bounded owner-edge evidence; a timeout is not itself an owner-edge violation and log order cannot substitute | **no owner may be charged**; gap recorded; no downstream claim established or refuted; failure unlocalized |

## 8. Residuals And Invalidation (T-11)

**Residuals.** (1) Live signing conformance beyond `CL-U1`'s single scenario. (2) Uncovered 3-way interactions plus all 4-way at the composition boundary. (3) User populations, roles, refusal paths, recovery beyond one `route-editor` scenario. (4) `CL-E2`'s configuration identity and the space where `legacy-build` is reachable. (5) Signing-policy status observability. (6) `CF-3`'s alternatives and `CF-4`'s unbounded frontier. (7) Fresh-process, replay, reconstruction, migration (557) — no input supplied. (8) Receipt durability beyond one observation. (9) Whether the module revision proved equals the revision inside `install-44`. (10) Concurrency — undeclared at every altitude.

**Invalidation.** Runnable-subject or install-identity change — **already triggered by `MUT-2`**; Product/requirement/interface/role/capability/acceptance-meaning change (413); dependency realization or harnessed↔live mode change (406, 413); configuration or version-combination change including the `legacy-build` switch (443, 464); interface/carrier revision or participant substitution (464); module boundary, owned law, algorithm, state space, oracle, generator, or population change (485); packaging change moving `TEST-SEAM` into distribution (596–598); **cross-population** — an `STDO-UP-023` re-entry from F-10 or F-11 invalidates `CL-N2`'s unit population and `CL-I1`'s participant identity.

## 9. Retained Gaps G-2 .. G-8 — Synthetic Expected Method Outputs, Not Candidate Defects

In every case the candidate clause reached a determinate disposition and **correctly refused to manufacture closure** over a datum the synthetic trial input did not supply. `STDO-UP-023` 617 and baseline 666 mandate exactly this. G-1 is closed and no longer retained.

| # | Gap | Kind | Method behavior demonstrated | Owner |
|---|---|---|---|---|
| G-2 | `DISC-7` maintained-external residual states no immateriality reason | synthetic input | 617 **held selection closure open** rather than defaulting favorably | `AT-DESIGN` |
| G-3 | version basis asserted, not exhibited | synthetic input | derived immaterial with the reason stated | `AT-DESIGN` |
| G-4 | `CL-E2` configuration identity absent (436) | synthetic input | bounded T-07a between `falsified` and `indeterminate` rather than picking the favorable one | frame declaration |
| G-5 | `CL-I1` retains 4-way but not uncovered 3-way | synthetic input | 561–565 exposed the un-retained band between all-pairs and the declared residual | frame declaration |
| G-6 | no owner seam for signing-policy status | synthetic-Product design gap | 666–667 produced a **named gap** instead of admitting rival semantics | `AT-SECURITY` |
| G-7 | `LOCAL-G1-R2` posture ambiguous | synthetic input | off-frontier under **both** readings — not decision-relevant | none |
| G-8 | no temporal order over install-identity observations | synthetic input | conservative over-inclusion of `MUT-2`'s invalidated set | frame declaration |

**No case was unevaluable because the candidate method text under-determines it.** Every `indeterminate` (F-03, F-06a, F-06b, T-09c, CF-3, CF-4) is a result the method prescribes.

## 10. Reconstruction

```sh
find specification/standards -type f | LC_ALL=C sort | xargs shasum -a 256 | shasum -a 256   # 0f46a3d5…4ce91
find specification/standards -type f | wc -l                                                 # 43
shasum -a 256 specification/standards/DESIGN_MODULE_METHOD.md \
  specification/standards/STDO_REFERENCE_FRAME_BASELINE.md \
  specification/standards/authority_compressions/design_module_method.compressed.md \
  specification/standards/authority_compressions/stdo_compressed.md \
  specification/standards/templates/AGENTS_TEMPLATE.md \
  specification/standards/templates/CLAUDE_TEMPLATE.md \
  specification/PRODUCT.md releases/v2.4.1.md \
  .ai-workspace/comments/codex/20260817T034022Z_INPUT_stdo_2_4_1_amendment_qualification.md
git cat-file -t e05984c4f3b75525e6d962f6b9d72bbedd8e271a          # commit
git cat-file tag 66118f3c5808536df5e5393d725e54e4eebc45f4 | head -5   # tag v2.4.0 -> e05984c4…
git diff --name-status e05984c4f3b75525e6d962f6b9d72bbedd8e271a -- specification/standards   # 6 M, 0 A, 0 D
git ls-tree -r --name-only e05984c4f3b75525e6d962f6b9d72bbedd8e271a -- specification/standards | wc -l   # 43
T=$(mktemp -d); git archive e05984c4f3b75525e6d962f6b9d72bbedd8e271a specification/standards | tar -x -C "$T"
(cd "$T" && find specification/standards -type f|LC_ALL=C sort|xargs shasum -a 256|shasum -a 256)  # 1571aab5…4a4cc5
(cd "$T" && find specification/standards -type f|LC_ALL=C sort|xargs shasum -a 256) > "$T/old.txt"
find specification/standards -type f|LC_ALL=C sort|xargs shasum -a 256 > "$T/new.txt"
comm -12 <(sort "$T/old.txt") <(sort "$T/new.txt") | wc -l        # 37
rm -rf "$T"
```

**Reproduce the evaluation.** Withhold per `STDO-UP-022`: comments except the one input file, tickets, expected outputs, prior verdicts, ABIogenesis material, author memory. Read: the input file; DMM 583–695, 1254–1358, 1657–1779; baseline 1–260, 375–693, 848–878, 882–903, 981–996, 1000–1053; `SPEC_METHOD.md` `STDO-UP-022` at 1221ff; RFM 397–402, 621–648, 651–673; `PRODUCT.md`; `releases/v2.4.1.md`. Do **not** read `authority_compressions/*` or `templates/*`. Derive in order: delabelled capability → relation/mechanics factoring → discovery disposition against seven fields per category → eliminations → pairwise strict dominance → frontier → F-rows → four frame declarations without `CL-*` labels → T-rows → four localization forms → residuals. Use only `satisfied`/`falsified`/`indeterminate`/`out_of_frame`/`invalid_basis`. Freeze before reference-outcome exposure.

**Divergence points:** materiality of the maintained-external residual; `R20` license posture; whether the 75 ms ceiling makes 34 vs 29 ms non-discriminating; `G1-R2` elimination vs domination; T-07a `falsified` vs `indeterminate`.

## 11. Closed Work Result To Executive

```text
work_result:            candidate_ready
reference_frame_result: satisfied
actor:                  fresh capable constructor, distinct from the STDO 2.4.1 authoring Worker
subject:                the two changed 2.4.1 method populations — DESIGN_MODULE_METHOD.md
                        STDO-UP-023, and the claim-relative Product-testing configuration
                        in STDO_REFERENCE_FRAME_BASELINE.md
exact candidate:        aggregate 0f46a3d5…4ce91 over 43 members; DMM 89659b99…5d876d1;
                        BASELINE 1d208cc2…d61bed; PRODUCT aa1eb798…93cf066;
                        release note 7756e23f…a27eea; input f06e4b5b…c6455e
predecessor:            v2.4.0 — tag 66118f3c…c45f4 -> commit e05984c4…8e271a;
                        aggregate 1571aab5…4a4cc5 over 43 members
disposition:            6 changed, 0 added, 0 removed, 37 byte-conserved — VERIFIED
identity verification:  satisfied; all declared values matched, including the previously
                        self-referential release-note digest. G-1 CLOSED; invalid_basis N/A.
trial completion:       all 23 cases and sub-cases evaluated to a bounded result form.
                        No case unevaluable due to candidate method text.
retained gaps:          G-2..G-8 — synthetic input / synthetic-Product gaps, EXPECTED METHOD
                        OUTPUTS, NOT CANDIDATE DEFECTS. None closed by inference or default.
sufficiency:            within the declared envelope, both changed populations were sufficient
                        for a fresh capable constructor to derive every required trial output
                        without reference outcomes, author memory, prior verdicts, or
                        supplemental authority input.
freeze:                 evaluation frozen before any digest was computed; segment-2
                        verification confirmed the subject and changed no result.
NOT performed:          release review, release grading, Executive disposition, publication or
                        tag inference, candidate byte edit, tag, push, independent Reviewer
                        assessment. Carries no publication authority; asserts no release readiness.
```
