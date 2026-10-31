# Review: the a_c Lean formalisation (T-011, T-012, T-013) at `037dc6fb7`

Reviewer: Claude Fable 5.1, at the owner's request ("review the unreleased work on
specification_methodology on the mathematical completeness proof on a_c").
Commentary, not law. No tenant file was edited; the probe and reproduction
artefacts below are the reviewer's own. Local clock 2026-11-01 02:52 (UTC+11).

## Verdict

**Sound, reproduced, and not a completeness proof of a_c.**

The three unreleased commits (`a971d3858`, `21585e1ac`, `037dc6fb7`; `main`
equals `origin/main`; a_c has never been released) deliver one bounded theorem,
kernel-checked and independently reviewed: for a finite model and a declared
required-dependency relation, an accepted certificate's set is exactly the
reflexive-transitive reachability set of the seeds, is dependency-closed, is
least among seed-containing closed sets, and is unique; the projection conserves
every retained record byte for byte and names every residual; an insufficient
budget refuses without truncation. I reproduced the tenant's public check on this
host and ran the reusable gate on the toy subject; both agree with the records.

The word "completeness" holds in one precise sense only: the certified closure
contains every record reachable under the declared relation and nothing else. No
theorem in the tenant concerns the calculus's consistency, soundness or logical
completeness, and `specification/requirements/formalisation.md` (lines 29 to 33)
says none follows. Semantic completeness of the relation itself, whether the
author declared every dependency that matters, is outside the kernel by design.
AC-010 makes material closure conditional on an exact relation `R`; the tenant
inherits that condition rather than discharging it.

Two actionable items: the documented public check fails on a default macOS shell
(F1, one line), and the kernel does not tie the declared edge relation to the
typed references it also carries (F2, a design choice for the owner).

## Subject

| Item | Identity |
|---|---|
| Commits reviewed | `a971d3858` (T-011/T-012 checkpoint), `21585e1ac` (T-013 scale and reuse), `037dc6fb7` (T-013 delivery); head `037dc6fb7` |
| Owning clause | `AXIOMATIC_CALCULUS.md` `cbe2edb9…`, AC-010 Material Closure and AC-011 Projection, installed `stdo://releases/v2.5.1-rc.2/` |
| Generic Lean core | `AC/Model.lean`, `Closure.lean`, `Projection.lean`, `Structure.lean`, `GateProof.lean`, 700 lines; Lean 4.35.0 `eb6cafb7`, Mathlib `56a00585` |
| Gate runtime identity on this host | `f492806bfb58bcabad63a89caa4c62c57bd37f8ed99b8fed764a9a6c5b8908c9` (25 pins), equal to the T-013 record |
| Authority read | `a_c/README.md`, `specification/{INTENT,GOALS,PRODUCT,REFERENCE_FRAME_BASIS}.md`, `requirements/formalisation.md`, `build_tenants/lean/design/*`, tickets T-011..T-013, the T-011 final review, the T-012 final review, the T-013 scale, view-repair, runtime-specialization and delivery records |

## The mathematics, traced

| Proposition | Lean | Assessment |
|---|---|---|
| Membership equals reachability | `certificate_exact_reachability`, `Closure.lean:100-107`; forward by induction over the witness trace (`witness_reachable`), backward by induction over `ReflTransGen` into a closed set (`reachable_in_closed`) | Correct. `Reachable` is `∃ seed ∈ seeds, ReflTransGen (fun a b => b ∈ d a) seed x`, the right direction for "a requires b". |
| Leastness | `certificate_least`, `:118-124` | Correct and non-circular. It quantifies over every finite seed-containing closed candidate; the only premise is the Boolean certificate check. |
| Fixed point | `certificate_fixed_point`, `:127-143` | This is AC-010's equation `Q = Z ∪ required(Q)` at the accepted set. Correct. |
| Uniqueness | `certificate_unique`, `:146-154` | Uniqueness of successful certificates for the same inputs. Correct; the design note is right that larger fixed points exist (disconnected cycles) and are refused, which the T-011 reviewer's kernel control shows. |
| Projection conservation | `project_ok_properties`, `Projection.lean:82-98`; `projection_record_conservation`, `projection_authority_basis_conservation`, `:115-125` | Correct. A real `.ok` is eliminated back into the checks and the exact `makeProjection`. Conservation is `rfl` because no record is rebuilt, which is the right design rather than a weak theorem. |
| Residuals accounted | `projection_all_residuals_accounted`, `:156-164` | Every parent residual is retained-unresolved or named excluded. Correct. |
| Budget refusal | `insufficient_budget_refuses`, `:107-113`; `project`, `:65-71` | One error branch, no prefix result. Correct. |
| Scale certificates | `Structure.lean`: sorted character lists, adjacent `<` chain, `String.ofList` injectivity, chunked edge and reference bounds, implying the unchanged `Model.WellFormed` (`wellFormed_of_range`, `:201-221`) | Correct. The optimisation is a certificate for the same proposition, not a weaker one. |
| Proof-directed runtime | `projectWithProof_eq_project`, `GateProof.lean:22-28` | Correct. Runtime equals `project` on the proved domain. |
| Concrete instances | `Fixture.lean`, `Toy.lean`, generated `GateViews.lean` per request; `decide +kernel`, `debug.skipKernelTC false`; `Audit.lean` pins the proposition types | All 204 deciding theorems depend only on `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, `native_decide`, added axiom or `unsafe` in `AC/`. |

Non-vacuity: the premises are executable Boolean checks discharged in the kernel
on the real data. The truncated-certificate rejection and the T-011 reviewer's
disconnected-cycle control show the checker is not satisfied by arbitrary closed
sets. I reran the rejection.

## Reproduction on this host

Darwin-arm64, the tenant's private toolchain, 2026-11-01. All Lean runs were
sequential. The first `check.py` run failed at the test stage (F1); the second ran
with `TMPDIR` pointing at a directory without a symlinked ancestor.

| Step | Result |
|---|---|
| Compiler, Mathlib and dependency pins | match `toolchain-lock.json` and `lake-manifest.json` |
| Source import and custody | pass, 2.2 s |
| Python tests | 77 run; 1 failure on the first run (F1), 77 pass on the second |
| `lake build` | up to date, 645 jobs |
| Axiom audit | 204 theorems, every one `[propext, Classical.choice, Quot.sound]` |
| `leanchecker --fresh AC` | pass, 66.5 s |
| Actual Lean output versus independent Python expectation | equal; output SHA-256 `2f900f4dd946d3ace83d528c5b44d9ca229f5bf3accf9852d5f583cb52980fce`, equal to the T-011 review |
| Truncated certificate | rejected by the kernel as false |
| Report | `check-report.json` here, SHA-256 `86bbb97be5d50a31256324b528a7c017fc9bdd3a78e7c6e97ee80e36b904023a` |

Reusable gate on the toy subject (`fixtures/toy/MODEL.json`):

| Request | Status | Elapsed | Evidence manifest |
|---|---|---|---|
| Model only | verified | 25 s | `39c5d462…` |
| Seed `urn:a-c:toy:object:a`, budget 9 | verified; 18 generated theorems, standard axioms | 22 s | `2f45a695…` |
| Same seed, budget 8 | refused: "Insufficient record budget; verified refusal, no truncated projection" | 22 s | `6039bb8e…` |
| `check-evidence` on the budget-9 bundle | verified by local origin reuse; zero proof, replay and runtime invocations | 6.8 s | separate bundle |

## Findings

**F1, S3, reproducibility, actionable.** `python3 scripts/check.py` fails on a
default macOS shell. `tests/test_gate_codegen.py:31` creates its evidence under
`tempfile.TemporaryDirectory()`, which resolves under `$TMPDIR` at
`/var/folders/…`; `/var` is a symlink; `scripts/formal_reuse.py:71` refuses
"Symlink path is outside the protected acquisition contract" before the generator
runs, so the test observes `refused` where it expects `incomplete`. The recorded
control runs set `TMPDIR` explicitly (`run_python_controls.py:17`,
`run_controls.py:27`) and so never saw this. The other gate test already uses
`tempfile.TemporaryDirectory(dir=ROOT/'.cache')` (`test_formal_gate.py:55`). Fix:
the same `dir=` argument in the generator test, or `check.py` exporting a
nonsymlinked `TMPDIR`. One line, `realization_refactor`. Until then the README's
public command is not reproducible as written. First-run log retained here as
`adapter-tests-failing.log`.

**F2, design, for the owner.** The kernel does not tie `Model.edges` to
`Model.references`. `BridgeGap.lean` (here, with its log): a two-record model with
a governing local reference `0 → 1` and an empty edge list is `WellFormed`, its
certificate for seed `0` with an empty trace passes, `project` succeeds with
closure `{0}`, and `1` is excluded, all with the standard axioms. So "exact
closure" is exact relative to the edge list the Python importer emitted
(`import_fixture.py`, the `edges` block near line 375). The only guard that this
list reflects the governing references, relation records and attachments is the
importer's own re-import check in the same process. This is inside FR-006's
declared boundary and `design/BOUNDARIES.md` says so, so it is not a conformance
defect. But the relation is the one thing the theorem is about, and one of its
three rules is derivable in Lean today: the probe's six-line `governingCovered`
is decidable and `gap` fails it. The other two rules (relation endpoints,
attachment subjects) live inside opaque payload strings; carrying them as typed
fields, as references already are, would let the kernel check all three and turn
the importer's edge derivation into a checked projection. Cost: `WellFormed` and
the `Structure` certificates change, so every contract and the support manifest
re-establish; the extra kernel work is a chunked `all` over 16,498 references for
the full subject, comparable to `refBounds`. This is a `design_reframe` in the
tenant HOW under unchanged FR-003 and FR-006. It needs the owner's selection.

**F3, S4, wording.** `certificate_seed_inclusion` (`Closure.lean:109-111`) takes
the certificate hypothesis and does not use it; seed inclusion holds for any
trace. Harmless, but the deciding-theorem list presents it as certificate-bound.

**F4, S4, record drift.** T-011 line 6 and T-012 lines 6 and 148 still say the
work is uncommitted and unpushed. It was pushed at `a971d3858` and the a_c README
says so. Live status lines should be current.

**F5, standing, not a defect.** Unestablished and recorded as such: practical
benefit (the matched Worker pair found a defect in each arm and no causal
benefit), cost (270 s and 12.7 to 14.6 GB child RSS per cold full-size run,
Darwin-arm64 only), fresh-host qualification, and the semantic selection of
required edges, which stays an F_P judgment. I did not review the Graphify-side
integration (`build_tenants/graphify/code/ac_formal_gate.py`).

## Answer to the owner's question

There is no mathematical completeness proof of a_c, and the records never claim
one. There is a correct, kernel-checked, reproduced proof that the material
closure operation of AC-010 is computed exactly and least under a declared
relation, and that AC-011 projection conserves records and refuses truncation.
A completeness result about the calculus itself would first need a stated
semantics to be complete with respect to; that is unstarted work and a separate
decision. If more of the calculus is to be formalised next, AC-003 reference
closure and AC-009 residual conservation beyond projection are finite, cheap and
adjacent to what exists, and F2 would narrow the trusted bridge for the theorem
already proved.

## Reviewer artefacts in this directory

| File | SHA-256 |
|---|---|
| `BridgeGap.lean` (probe) | `386ff27d7a3f8e36e4009ec6ddfd3ff4bab16b1d044a8e779c7368820e109034` |
| `BridgeGap.log` | kernel output of the probe, exit 0 |
| `check-report.json` | `86bbb97be5d50a31256324b528a7c017fc9bdd3a78e7c6e97ee80e36b904023a` |
| `adapter-tests-failing.log` | `6801211d50e1547ee8f8cc23a5bd2297c0b654446bd65f163031944bb9cb889a` |

Gate bundles and the second check's logs stay in the reviewer's scratch; their
result digests are `c9c2b33e…` (model only), `150773f2…` (budget 9),
`942d641f…` (budget 8), `b947c933…` (recheck).
