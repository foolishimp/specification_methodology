# Independent Exact-Carrier Review: STDO 2.4.1-rc.1

## 1. Reviewer Identity, Authority, And Independence

- **role**: independently authorized evaluator and exact-carrier Reviewer under
  `TICKET_METHOD.md` `STDO-UP-007` and `SPEC_METHOD.md` `STDO-UP-022`.
- **actor**: Claude Opus 5, review session distinct from every prior actor.
- **non-identity declarations**: not the Codex authoring Worker; not
  fresh-constructor session `e212d5eb-dd92-43a7-8e27-2542e7aef375`; not the
  human Product owner.
- **authorship**: no byte of any candidate, protected, evidence, or ticket file
  was authored by this actor.
- **repository mutation**: none. No edit, commit, branch, tag, push, repair, or
  publication was performed. Work was read-only in detached worktree
  `/private/tmp/stdo241-review-CeTVhP`. This record is written outside the
  worktree and is not committed.
- **evidence policy**: every predicate below was reacquired directly from
  repository bytes. No summary claim, green count, checkbox, or declared digest
  was accepted without reproducing it. Where a predicate could not be
  reacquired, that is recorded as a residual rather than passed.
- **comparison predicate**: the exact tag commit tree conserves complete
  `v2.4.0` semantics except where the declared `2.4.1` amendment extends them;
  every protected identity claim reproduces; no changed byte creates law the
  governing sources do not admit.
- **governing basis read**: `RELEASE_METHOD.md`; `SPEC_METHOD.md`
  `STDO-UP-020` and `STDO-UP-022`; `TICKET_METHOD.md` `STDO-UP-007`;
  `REFERENCE_FRAME_METHOD.md` result algebra; `DESIGN_MODULE_METHOD.md`
  (`STDO-UP-023`, unit-lane law, review projections);
  `STDO_REFERENCE_FRAME_BASELINE.md`; `PRODUCT.md`; `GOALS.md`;
  `releases/v2.4.1.md`; active `T-010`; declared qualification input;
  fresh-constructor result; pre-RC checkpoint; closed `T-007`/`T-008`/`T-009`.

## 2. Exact Basis

| Element | Value | Reproduced |
|---|---|---|
| annotated tag | `v2.4.1-rc.1` | yes |
| tag object | `a4b66bd24862f024c7c909e675de839104179d11` | yes |
| commit | `c37452a390e8456863eeb4e3d5bf9c9a237a44ed` | yes |
| tree | `02976636453e1ce90c2f02e6f2c142b08cd8cf30` | yes |
| predecessor commit | `e05984c4f3b75525e6d962f6b9d72bbedd8e271a` | yes |
| predecessor tag object | `66118f3c5808536df5e5393d725e54e4eebc45f4` | yes |
| working tree | clean; no untracked, no ignored | yes |
| delta | exactly one commit, `c37452a`, parent `e05984c` | yes |

The isolated basis is clean: `git status --porcelain --ignored` is empty, so the
`find`-based canonical aggregate observes only tracked candidate bytes.

## 3. Reconstruction Commands

```sh
git rev-parse v2.4.1-rc.1                      # a4b66bd2...
git cat-file -p v2.4.1-rc.1                    # tag -> commit c37452a3...
git cat-file -p c37452a390e8456863eeb4e3d5bf9c9a237a44ed   # tree 02976636..., parent e05984c4...
git status --porcelain --ignored               # empty

# Candidate identity
find specification/standards -type f | wc -l                                        # 43
find specification/standards -type f | LC_ALL=C sort | xargs shasum -a 256 | shasum -a 256
                                                                                    # 0f46a3d5...4ce91
shasum -a 256 specification/PRODUCT.md                                              # aa1eb798...3cf066
shasum -a 256 releases/v2.4.1.md                                                    # 7756e23f...a27eea

# Predecessor identity, isolated
T=$(mktemp -d); git archive e05984c4f3b75525e6d962f6b9d72bbedd8e271a | tar -x -C "$T"
(cd "$T" && find specification/standards -type f | wc -l)                           # 43
(cd "$T" && find specification/standards -type f | LC_ALL=C sort | xargs shasum -a 256 | shasum -a 256)
                                                                                    # 1571aab5...4a4cc5
git diff --name-status e05984c c37452a -- specification/standards                   # 6 M, 0 A, 0 D

# Digest-pin fidelity (14 pins)
grep -n 'source_digest\|source_digests' -A12 specification/standards/authority_compressions/stdo_compressed.md
(cd specification/standards && shasum -a 256 REFERENCE_FRAME_METHOD.md STDO_REFERENCE_FRAME_BASELINE.md \
  SPEC_METHOD.md DESIGN_MODULE_METHOD.md ODD_METHOD.md TICKET_METHOD.md UX_METHOD.md \
  IDENTITY_METHOD.md RELEASE_METHOD.md POSTING_GUIDE.md)

# Bootstrap parity
diff specification/standards/templates/AGENTS_TEMPLATE.md specification/standards/templates/CLAUDE_TEMPLATE.md

# Consumer-local law scan
grep -rniE 'ATLAS|AT-ROUTE|AT-BUILD|AT-SECURITY|AT-STORE|AT-DESIGN|AT-RELEASE|route-editor|SIGN-FAKE|FOUNDATION-G|LOCAL-G1|legacy-build|install-44|DISC-7|EVID-7' \
  specification/standards specification/PRODUCT.md releases/v2.4.1.md

# Gates
git ls-remote --tags origin | grep v2.4 ; git ls-remote --heads origin | grep 2.4
git rev-parse --verify release/2.4.1 ; git rev-parse --verify v2.4.1     # both must fail
```

## 4. Findings, Ordered By Severity

No finding rises to a blocking severity. No finding requires a protected-byte
change. Findings are ordered highest to lowest.

### R-1 (residual, non-blocking) — the "four initial testing repairs" are not independently reacquirable from the carrier

`PRODUCT.md` (195-197), `GOALS.md` `R1` (150), and `T-010` acceptance condition
(273-274) each assert that "the four supplied testing-profile findings" were
repaired. **No carrier document enumerates those four findings.** `T-010`
115-117 identifies their source as "the external testing-amendment review
supplied by direct human authority", whose "reviewed source blob was
`813cd92f...`" — an object not present in this repository and superseded by
current authoring bytes.

Under `STDO-UP-007` ("A claimed independent review may support promotion or
closure only when its exact subject and verdict are durably traceable through an
existing ticket, commentary, qualification, or release-evidence carrier"), the
four findings' verdict is **not** durably traceable. I therefore could not
reacquire a 1:1 mapping from four named findings onto four repairs.

What I *could* and *did* verify is the seven enumerated testing-profile
obligations in `T-010` §Candidate Scope (144-163). All seven are satisfied in
candidate bytes — see the per-population table. The repair *content* is
complete and verifiable; only the four-finding *framing* lacks a carrier.

Why this does not block: the promotion at this gate does not rest on that
external review. The operative gates are fresh-constructor qualification and
this independent exact-subject review, both of which evaluate candidate bytes
directly. `T-009`'s own Publication Closure already records a comparable
"historical release-process evidence debt" and explicitly declines to convert
unchecked historical boxes into evidence — the same honest treatment applies
here. Disposition: record as release-process evidence debt; do not restate the
four-finding claim as reacquired evidence. This lives entirely in excluded
source-project state (`GOALS.md`, `T-010`) and one protected descriptive line in
`PRODUCT.md` that is true-as-stated but unverifiable from the carrier.

### R-2 (coverage observation) — this review is the first independent evidence on four of the six changed members

The fresh constructor declares (§1) that `authority_compressions/*` and
`templates/*` were "digest-verified but **never read as content**." Those are
**four of the six changed members**. Before this review, compression projection
fidelity and Codex/Claude bootstrap parity therefore rested only on the
authoring Worker's own checkpoint (69-78) — Worker self-review, which
`STDO-UP-007` forbids relabelling as independent.

I discharged both populations directly and both pass:

- **Digest-pin fidelity: 14/14 exact.** `stdo_compressed.md` pins ten sources;
  `design_module_method.compressed.md` and the four standalone compressions pin
  their own. Every pinned value equals the actual current source digest. The
  `stale_if_source_digest_changes: true` guard is satisfied on every compression,
  including the four unchanged ones whose sources were also unchanged.
- **Bootstrap parity: byte-identical delta.** The 49 added lines in
  `AGENTS_TEMPLATE.md` and `CLAUDE_TEMPLATE.md` are byte-for-byte identical.
  Whole-file `diff` yields exactly four differences, all pure platform labels:
  title (`Codex`/`Claude`), bootstrap sentence subject, child-override filename
  set, and precedence-list ordering. Equal minimum semantics after platform-label
  normalization: **confirmed**, not assumed.

Not a defect. Recorded so the Executive knows which actor supplied which
evidence.

### R-3 (minor) — benign projection-wording variance for one candidate category

The foundation candidate-category list is worded slightly differently across
surfaces: `DESIGN_MODULE_METHOD.md` 606 "accepted predecessor or
immutable-lineage realizations"; `releases/v2.4.1.md` "immutable-lineage";
`PRODUCT.md` 126-127 "native or standard, immutable-lineage";
`design_module_method.compressed.md` "predecessor-lineage". All four denote the
same category and no comparison result turns on the wording. Separately,
`PRODUCT.md` compresses DMM's twelve numbered obligations into eleven by merging
the no-presumptive-preference clause into the dimensions clause; the merged text
retains "without source-order, familiarity, sunk-cost, local-code, or
dependency-count preference" in full. DMM owns the law in both cases; these are
faithful projections, not claim divergence. No action.

### R-4 (minor) — systematic ~1-line offset in the constructor's DMM citations

The trial record hangs verdicts on specific line numbers. I spot-checked
thirteen decisive ones. Several carry a consistent one-line offset (cites 590
for text at 591-592; 613-614 for 614-615; 647 for 648; 673-681 for 674-683).
**Every substantive claim is correct against the actual text**, including the
exact-quote citations (682-683 "Generic local code is lawful only when it wins
the same comparison; it is not the default"; 660-661; 665-669; 685-689). No
verdict depends on the offset. No action.

### R-5 (expected gate state) — remaining gates are correctly open

`release/2.4.1` and `v2.4.1` are absent locally and at `origin` — verified by
`git rev-parse --verify` (fails) and `git ls-remote` (absent). `GOALS.md`
milestones `R5`, `R6`, `R7` are marked `pending`, and `T-010` acceptance
conditions 311-316 are unchecked. No surface overclaims review, acceptance, or
publication. Correct.

### R-6 (observation) — `T-010` active at the RC cut is lawful

`T-010` remains `status: active` with `review_status:
candidate_02_fresh_construction_passed_ready_for_rc`. This is correct: its four
remaining acceptance conditions are exactly independent review, immutable-RC
review, human acceptance, and final publication. Closing it before those
transitions would be the defect. Lawful under `TICKET_METHOD.md`.

## 5. Per-Population Verdict Table

| # | Mandated population | Verdict | Basis reacquired |
|---|---|---|---|
| 1 | Exact tag commit tree | `satisfied` | tag `a4b66bd2` → commit `c37452a3` → tree `02976636`; all three reproduced |
| 2 | Clean isolated basis | `satisfied` | `git status --porcelain --ignored` empty; single-commit delta from `e05984c` |
| 3 | 43-member / six-changed / 37-conserved identity | `satisfied` | `find` count 43 both sides; `git diff --name-status` = 6 M, 0 A, 0 D |
| 4 | All protected digests | `satisfied` | aggregate `0f46a3d5…`, PRODUCT `aa1eb798…`, note `7756e23f…`, all six changed-member digests — each recomputed and matched |
| 5 | Predecessor conservation | `satisfied` | v2.4.0 extracted in isolation: 43 members, aggregate `1571aab5…`, tag object `66118f3c…` — all matched; `release/2.4.0` and `v2.4.0` unmoved at `e05984c4` locally and at origin |
| 6 | Source digest fidelity | `satisfied` | 14/14 compression pins equal actual source digests |
| 7a | Compression projection fidelity — `STDO-UP-023` | `satisfied` | Both changed compressions carry the complete relation: six-label normalization, relation/mechanics factoring, five candidate categories, seven-field bounded discovery with material-gap refusal and later-candidate invalidation, the material-dimension list, hard elimination with unknowns retained, the four-part dominance test, undominated-frontier selection via declared owner priorities with gap retention, assigned-role conservation, ownership-follows-relation, local-code-is-not-default, and recursive re-entry distinct from recurrence review. Five deleted lines are digest/date pin updates only; no claim removed |
| 7b | Compression projection fidelity — testing profile | `satisfied` | `stdo_compressed.md` carries a dedicated `## Product Testing Frame Compression` section projecting all eight profile relations: claim fan-out plus declared conjunction; UAT/E2E runnable subject, forbidden-path falsification, and substitute limits; integration narrowing; DMM-owned unit lane with complexity governing volume not eligibility and no cross-lane closure; coverage retention with green/count barred as assurance; the two closure graphs and the lawful test-only seam; acquisition-versus-oracle separation with a missing projection remaining a gap; and all four causal-frontier forms. `T-010` condition 300 ("Aggregate and DMM compressions project the changed law") is satisfied for **both** halves of the changed law |
| 8 | Codex/Claude bootstrap semantic parity | `satisfied` | 49 added lines byte-identical; whole-file differences are four platform labels only |
| 9 | Apache-2.0 and plugin conservation | `satisfied` | `LICENSE` and `plugins/spec/LICENSE` both `cfc7749b…` (byte-equal); marketplace `ad88de53…`; plugin `77cb1a4a…` at version `2.1.0`, license `Apache-2.0`; SKILL `1ca76a37…`; README `cc6a4838…`. All six equal the release-note table and all are outside the 43-member inventory |
| 10 | Absence of consumer-local law | `satisfied` | Scan of all 43 members + PRODUCT + note + GOALS for 21 synthetic-trial and consumer tokens: zero leaks. Only `ABIogenesis` appears, in pre-existing text explicitly declaring it discovery evidence and not STDO authority, plus baseline misapplication condition 16 forbidding its machinery as universal |
| 11 | Four initial testing repairs | `indeterminate` (framing) / `satisfied` (content) | The four findings are not enumerated in any carrier and their source blob `813cd92f…` is absent — see R-1. The seven enumerated `T-010` testing obligations (144-163) are each verified present in baseline bytes |
| 12 | Repair 1 — foundation role authority | `satisfied` | DMM 674-683: reuse confers no authority; assigned role lawful only with owner/kind/subject/scope/basis/lifecycle/refusal preserved; "Ownership belongs to the declared relation, not necessarily to locally written code" |
| 13 | Repair 2 — undominated selection | `satisfied` | DMM 651-652 (explicit undominated frontier), 654-663 (strict four-part dominance), 665-672 (selection only via declared priorities/risk tolerances; "not necessarily the fewest dependencies, smallest immediate edit, lowest local line count, or richest feature set"; unresolved frontier stays an explicit design gap) |
| 14 | Repair 3 — finite discovery | `satisfied` | DMM 610-620: seven-field per-category record; unsearched category records `not_applicable` or a named gap with reason; closure only for the declared basis and cutoff; material gap prevents selection; later qualifying candidate invalidates affected evidence and re-enters |
| 15 | Repair 4 — causal frontier | `satisfied` | Baseline 672-688 defines all four forms and forbids collapsing a jointly established set into one arbitrary owner or misreporting alternatives as joint cause; restated at 1046-1047, 1129, 1199, 1260-1261 |
| 16 | Repair 5 — full normalization | `satisfied` | The complete six-label list appears in DMM 591-592, `stdo_compressed.md` 168-169, `design_module_method.compressed.md` 190-191, `AGENTS_TEMPLATE.md` 73-74, `CLAUDE_TEMPLATE.md` 73-74, and DMM review question 49 (2321-2324). No projection omits a label |
| 17 | No duplicate execution/admission/recurrence/release authority | `satisfied` | Baseline assigns conjunction and result algebra to `REFERENCE_FRAME_METHOD.md` (76) and result conjunction/disposition to Executive (865); unit result carries "no Product, installed, integration, user-acceptance, architecture, path-selection, or release authority" (480); misapplication condition 11 forbids new execution authority or local constitutional layer (1231); profile creates no second qualification process (1003). DMM 687-689 explicitly separates `STDO-UP-023` from §11C recurrence extraction. DMM's four hunks are pure additions; the three outside `STDO-UP-023` are review-checklist projections, not new authority |
| 18 | Optional profile — UAT | `satisfied` | 404-427: exact deployed/installed/runnable subject; primary only for the declared user-outcome claim; mints no acceptance authority; harnessed substitute limited to exercised composed relations; live sandbox UAT mandatory where a claim depends on real external compute or transport |
| 19 | Optional profile — E2E | `satisfied` | Complete authoritative causal path; 575-580 two-sided evidence; equal output through a forbidden path is a counterexample |
| 20 | Optional profile — integration | `satisfied` | One declared composition boundary and interaction population; substitute proves only its narrower admitted claim |
| 21 | Optional profile — unit | `satisfied` | Every coded module retains a module-derived lane (baseline 1035) citing the **pre-existing** DMM law at 1776-1779, present byte-identically in `v2.4.0` — existing owner cited, not new law; complexity controls evidence size and strategy, not eligibility |
| 22 | Optional profile — conjunction | `satisfied` | Bound results → declared conjunction → Product/release disposition; conflict "remains visible to Executive disposition and cannot be hidden by aggregate green status"; baseline 759-762 additionally bars green aggregate from satisfying the `candidate_ready` verification step |
| 23 | Optional profile — coverage | `satisfied` | 560-569: finite interaction population with declared adequacy; covering-array reduction lawful only with an explanation or retained residuals; high-consequence relations normally require higher strength; source/line/branch/function coverage explicitly cannot establish semantic combination coverage, path selection, or absence of a rival path |
| 24 | Optional profile — closure | `satisfied` | 582-600: production closure vs assurance/source closure as two distinct finite graphs; test-only seam lawful under three conditions (isolated from distribution, excluded from ordinary-path evidence, declared); obsolete assurance consumer that can falsely close or reintroduce the path remains a defect |
| 25 | Optional profile — acquisition | `satisfied` | 643-667: acquisition through the exact runnable owner surface, then a separately law-derived oracle; generic mechanics may compare owner-issued evidence but cannot mint carriers, choose current history, select the authoritative path, or become a runtime fallback; absent owner projection retains a named gap rather than rival semantics |
| 26 | Optional profile — localization | `satisfied` | See row 15 |
| 27 | Optional profile remains optional / no new authority | `satisfied` | Release note and `PRODUCT.md` both state it creates no further testing, Product, design, review, disposition, or release authority; baseline 244, 830, 1003, 1231, 1266 corroborate |
| 28 | Fresh-constructor coverage F-01..F-12, T-01..T-11 | `satisfied` | All 23 cases plus sub-cases present with relation, basis, result, evidence, residual, and invalidation. Thirteen decisive DMM/baseline citations spot-checked against actual bytes: all substantively correct (see R-4) |
| 29 | Retained synthetic gaps G-2..G-8 correctly classified | `satisfied` | Each traced to the governing clause. G-2 (DMM 617-618 requires an immaterial residual to record why it cannot change the decision — the input omits it, so closure correctly stayed open); G-3, G-4, G-7, G-8 (input under-specification, each producing a bounded rather than favorable result); G-5 (baseline 561-565 — the input retained only 4-way, leaving uncovered 3-way combinations un-retained; the constructor **derived** this gap rather than being handed it, which is affirmative evidence of profile sufficiency); G-6 (baseline 666-667 produces a named gap for an absent owner seam). All seven are synthetic-input or synthetic-Product gaps exercising refusal branches. **None indicates candidate method under-determination.** I concur with the classification |
| 30 | Qualification case semantics vs `candidate_ready` label | `satisfied` | Inspected directly rather than trusting the label. The trial contains `invalid_basis` (F-04), seven `falsified` results, and a `conflict` conjunction. These are the **correct** method outputs for cases the input deliberately constructed to violate (GPL-only candidate, authority-widening assignment, superior later candidate, unisolated mutation, rival-reconstruction oracle). The frame predicate is method *sufficiency* — whether the candidate text determines a bounded result for every case — and it does for all 23. `satisfied` on that predicate is correct and does not violate RFM 1042 |
| 31 | Product / release-note / ticket coherence | `satisfied` | `PRODUCT.md` binds the 43-member subject and the exact aggregate; the release note's predecessor block, disposition, changed-member table, and auxiliary-asset table each reproduce; `T-010`'s Candidate 02 table matches all nine digests; the checkpoint's declared values match; `GOALS.md` names the same subject and aggregate. No surface disagrees |
| 32 | `STDO-UP-015` successor conservation | `satisfied` | The 37 conserved members are byte-identical, so no predecessor claim is lost there. All nine deletions in the two changed normative members are list-punctuation reflow as items are appended (`; and` → `;`) plus two genuine **strengthenings** (green aggregate barred from satisfying `candidate_ready`; Worker row gains the `STDO-UP-023` reference). No claim is removed, narrowed, or left undisposed, so the release note's blanket conservation statement is adequate here. `PRODUCT.md`'s rewrite replaces the rolling *description* of the current amendment while its Published Product Basis section explicitly enumerates the conserved predecessor relations; the normative law itself is byte-conserved |
| 33 | Release-note final-readiness (`RELEASE_METHOD.md` 241-244) | `satisfied` | `releases/v2.4.1.md` carries no candidate, review, acceptance, branch, tag-existence, or publication state and explicitly disclaims implied refs. It requires no later tracked edit at tap |
| 34 | Normal RC publication path | `satisfied` | Checkpoint declares `selected_release_path: normal_rc_then_tap`. RC Publish Flow steps 4-7 are complete and verified at origin: commit `c37452a` pushed; `rc/2.4.1` at `c37452a` locally and at origin; annotated tag `v2.4.1-rc.1` (`a4b66bd2`) at origin. Naming shape matches `RELEASE_METHOD.md` §Naming |
| 35 | Remaining gates | `satisfied` (correctly open) | `release/2.4.1` and `v2.4.1` absent locally and at origin; `GOALS` R5/R6/R7 pending; `T-010` 311-316 unchecked. Step 7 (independent exact-cut review) is discharged by this record; steps 10-13 remain |
| 36 | Deterministic checks | `satisfied` | Both JSON manifests parse; `git diff --check` clean; fence parity even in all eight changed/protected Markdown files |
| 37 | Conserved index members describing changed members | `satisfied` | `specification/standards/README.md` and `authority_compressions/README.md` are both inside the protected 43 and both byte-conserved. Read directly: each is a pure surface-name list with **no** per-member content claim, no `STDO-UP-*` identifier enumeration, no section or member counts, and no digest table. The compression index explicitly delegates pinning — "Each compression file carries the source path and digest it was derived from" — so DMM gaining `STDO-UP-023` and the baseline gaining four testing frames leaves neither index stale. Byte conservation is correct here, not merely permitted |
| 38 | Documentation reconciliation (`RELEASE_METHOD.md` §Documentation Reconciliation) | `satisfied` | The two release-facing root documents are byte-conserved and deliberately version-agnostic. `README.md` (a protected release-scoped auxiliary asset, digest `cc6a4838…`) carries **no** version number, referring only to "one immutable released STDO cut identified by version" and directing readers to `releases/`. `PROVENANCE.md` records authoring origin and distribution history with no current-cut claim. Neither names `2.4.0` or `2.4.1`, so neither requires reconciliation at this RC or a later edit at tap |

## 6. Residuals

1. **R-1**: the four initial testing-profile findings are not enumerable from any
   carrier; their source blob `813cd92f…` is absent. Verified by content against
   `T-010`'s seven enumerated obligations, not by 1:1 finding mapping.
2. Compression *semantic* fidelity is assessed as faithful projection by reading
   both compressions against their sources. It is not mechanically enforced —
   the `stale_if_source_digest_changes` guard detects source movement, not
   projection drift. This is an inherent property of the compression design, not
   a `2.4.1` defect.
3. The fresh constructor read `releases/v2.4.1.md` before freeze. That file
   summarizes method text and contains no expected `F-*`/`T-*` case results, and
   it is declared in the constructor's envelope, so it is not an answer key under
   `STDO-UP-022`. Noted for completeness only.
4. This review record is not itself a repository-durable carrier. Under
   `STDO-UP-007`, recording it in the carrier is a separate act requiring
   authority this Reviewer does not hold and did not exercise.
5. Compression *semantic* projection was assessed by reading both compressions
   against their sources for both halves of the changed law. Row 7b establishes
   coverage of every profile relation, not a line-by-line equivalence proof;
   the compressions are declared read models, not deciding authority.
6. Fresh-constructor sufficiency is bounded to its declared envelope and to the
   two changed method populations. It is not evidence about the 37 conserved
   members, which are covered here by byte conservation.

## 7. Protected-Byte Impact

**No finding requires a change to protected bytes.**

The protected sets are the 43 `specification/standards/` members,
`specification/PRODUCT.md`, and `releases/v2.4.1.md`. Every finding above is
either (a) confined to excluded mutable source-project state (`GOALS.md`,
`T-010`, comments), (b) an evidence-traceability residual that no byte change
would cure because the missing artifact is external and superseded, or (c) a
benign wording variance among faithful projections that changes no claim.

This conclusion was specifically stress-tested against the two ways a
byte-conserved member could nonetheless be stale: an index that enumerates the
content of a changed member, and a release-facing document pinning a version.
Both were read directly (rows 37 and 38) and neither condition holds.

Consequently the reviewed subject requires no replacement candidate, and the
qualification bound to aggregate `0f46a3d5…4ce91` remains valid for this exact
carrier.

## 8. Reference Frame Method Result

```text
reference_frame_result: satisfied
```

Selected from the closed set `satisfied | falsified | indeterminate |
out_of_frame | invalid_basis` per `REFERENCE_FRAME_METHOD.md` 397-402.

**Why `satisfied`.** The declared predicate — that `v2.4.1-rc.1` is the exact
declared subject, conserves complete `v2.4.0` semantics outside the declared
amendment, and adds no law the governing sources do not admit — holds on the
exact basis. Every protected identity reproduced independently.

**Why not the alternatives.** `invalid_basis` does not apply: the subject and
basis are exact, clean, and fully reproducible. `out_of_frame` does not apply:
no evaluation required an undeclared material relation. `falsified` does not
apply: no declared counterexample defeats the predicate; the deletions are
reflow and strengthening, there is no consumer-local leak, no stale pin, no
authority duplication, and no bootstrap divergence. `indeterminate` was
considered on account of R-1 and rejected: R-1 leaves one *descriptive framing*
unreacquirable while the underlying repair content is fully verified against
`T-010`'s own enumerated scope, so admissible evidence does decide the governing
predicate. R-1 is carried as a residual under `STDO-UP-022`'s
claim-cannot-outrun-evidence rule rather than as an undecidable result.

## 9. Recommended `STDO-UP-020` Executive Disposition

```text
recommended_disposition: accept
```

Selected from `accept | local_repair | re_enter | reject` per `SPEC_METHOD.md`
`STDO-UP-020` Proportional Disposition.

The candidate closes its declared cone and preserves every affected governing
relation. `local_repair` is unwarranted because no implementation or proof
defect was found in protected bytes and no byte change would cure R-1.
`re_enter` is unwarranted because no Product, requirement, identity, lifecycle,
authority, public contract, or accepted-design change is needed. `reject` is
unwarranted because no governing relation is violated and no undisposed
competing truth path exists.

**Recommended handling of R-1**: record the four-finding traceability gap as
release-process evidence debt on the continuing source branch, in the same
manner `T-009` already records its historical debt. This is a source-state
notation and must not alter protected bytes; doing so would create a new
release subject and invalidate this review.

**This recommendation is a finding only.** It is not applied. This record
performs no Executive disposition, infers no human acceptance, and effects no
publication. `RELEASE_METHOD.md` Candidate Flow steps 10-13 — human acceptance
of the exact release subject, final carrier, and final-delta relation, then
publication of `release/2.4.1` and annotated `v2.4.1` — remain open and belong
to the human Product authority.
