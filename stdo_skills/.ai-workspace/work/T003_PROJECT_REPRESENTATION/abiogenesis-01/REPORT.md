# ABIogenesis project representation test

The nominated-project workflow completed successfully. The Codex `stdo-work` route prepared ABIogenesis's declared source scope, obtained grounded interpretations for all 42 chunks, accepted them through the public submission command, and built the model, recoverable carrier and interactive explorer. Independent checks found no actionable defect in the six selected semantic samples. This is a successful bounded representation test, not acceptance of the complete interpretation or qualification of ABIogenesis.

[Open the explorer](run/generation/proposal/explorer.html) · [Independent review](review/independent-001/REVIEW.md) · [Machine-readable result](REPORT.json)

## Scope and method

The subject is `/Users/jim/src/apps/abiogenesis`, selected through `stdo_abiogenesis.json`. Its installed methodology is **STDO v3.0.2**, manifest `f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477`. The source selection is the complete declared WHAT scope: `specification/INTENT.md`, `specification/PRODUCT.md` and `specification/requirements/`. Implementation and design files are outside that selection.

The source checkpoint observed at intake was `f63f030b902cefd15221359d02a8bf9c5b8a9565`. Exact working-tree bytes, rather than HEAD alone, identify this run: the source manifest is `c8f9e1f8a187cded5d919f319659add7e04330c37ad0a11856486276a0cf173f`; the Definition hash is `6d4caf2b6c6dd4c6e6386aba751e0967749103f2d19d96dfba36eaa68f8f7d28`. All selected files remained current at build, independent readback and reuse.

This was one coordinated Codex authoring run using four bounded source frames: Product/Intent, runtime, GTL and governance. Each author consumed actual public `task` responses; the Executive submitted the answers sequentially. Author identity is caller-declared and process isolation is not claimed. This is not a fresh headless Codex-versus-Claude host comparison. Provider mode was **direct**: the Graphify build tenant supplied the a_c machinery, but upstream Graphify was not invoked. Lean was not selected; the formal gate is `not_performed`.

## Delivered representation

| Item | Result |
| --- | ---: |
| Selected source files | 86 |
| Selected source bytes | 714,081 |
| Authored and submitted chunks | 42 of 42 |
| Source sections dispositioned | 421 |
| Retained section dispositions | 270 |
| Residual section dispositions | 112 |
| Omitted section dispositions, each with a reason | 39 |
| Model records | 1,373 |
| Objects | 479 |
| Constraints | 607 |
| Authored relations | 122 |
| Latitude records | 62 |
| Residual records | 103 |

Section dispositions and record families count different things. Residuals include deferred scope, unavailable referenced material and limits of local interpretation; **103 residuals does not mean 103 implementation defects**. Judgments, transformations and traversals have empty operational populations under the selected descriptive adapter.

| Artifact | Bytes |
| --- | ---: |
| [Model](run/generation/proposal/model.json) | 5,719,271 |
| [Carrier](run/generation/proposal/carrier.json) | 28,986,752 |
| [Coverage](run/generation/proposal/coverage.json) | 296,378 |
| [Explorer](run/generation/proposal/explorer.html) | 12,570,378 |

Canonical model identity: `6ad4fa0ef54a8fc705562acf695fce0a0855b0a0d68d6fc99dcf026e98a8b38a`. This differs from the serialized JSON file hash. [BUILD.json](run/BUILD.json) records both the semantic identity and every artifact byte hash.

## Checks and useful results

The actual public `build` returned `built`; subsequent `status` returned `built` with no pending chunks. A second public `build` returned `reused` with identical artifact pins. Readback validates the model, recovers the exact model document from the carrier, and binds the artifacts to current source, provider and submissions.

The independent reviewer recorded expectations before inspecting the model. All 19 artifact checks passed, including all 86 source files, exact carrier recovery, exact explorer data reconstruction and embedded source bytes. All 1,180 unique quotations, appearing in 1,636 grounding occurrences, occur within their declared frozen source spans. The six semantic samples preserved:

1. GTL declarations, HoG traversal and ABG admission as separate authorities, including the F_D/F_P/F_H boundaries.
2. Pure catalog readiness versus runtime admission and event truth.
3. Fixed invocation basis versus progressing producer output, and physical effects that can survive failed admission.
4. Selection of preregistered GraphFunctions versus out-of-scope dynamic generation.
5. Product-owned release allocation, including the distinction between an unqualified preview and final qualified acceptance.
6. The explicit R1–R10 dependency chain, same-candidate/test/causal-episode obligation, two fresh reads and conditions that leave the root open.

The explorer was exercised in Chrome against the actual generated HTML. Search, family selection, dependency navigation, the retained reading trail, 3D rendering and the source dialog worked. Searching **R10** with **All records** selected, choosing **R10 Replay and CLI agree on typed terminal outcome**, and following **Authored: requires** opens R9. The source button then opens `PRODUCT.md:1541`, highlights the exact row, and shows the surrounding R1–R10 table and qualification paragraph. See [browser observations](browser-observations.json). The temporary loopback server was stopped after testing; the HTML embeds its resources and source material.

Older Consensus and human-response requirement wording is retained under the owning Product's release precedence. It is not promoted into a new release obligation or a confirmed live-code defect. Likewise, source-reported implementation gaps remain source assertions until independently checked against implementation.

## Timing and limits

Preparation began at `2026-11-01T04:05:46Z`; the build receipt was retained at approximately `04:23:18Z`, about **17 minutes 32 seconds** later. This interval includes authoring, coordination and submission, and excludes initial intake and subsequent review/browser checks. Final assembly took **6.26 seconds**, status readback **4.47 seconds**, and checked reuse **5.34 seconds**. Token and monetary cost were not measured. The expanded artifacts and a single successful run establish no compression or cost advantage.

The result is useful as source-linked documentation for discovering constraints and following explicitly represented dependencies. Complete semantic fidelity, cross-chunk identity consolidation and global dependency completeness remain unqualified. A source dependency omitted by an author cannot be recovered merely by structurally validating the resulting model. Displayed arrows do not establish a proved inference, and no Lean result is claimed for this run.

No ABIogenesis source or implementation was changed. No ABI build, runtime proof, release, installation, commit or push was performed. All new test artifacts are confined to this directory; pre-existing work remains in place.

## Evidence and repeat check

[Activation](ACTIVATION.json), [source/project binding](run/PROJECT.json), [prepare response](prepare.stdout.json), [submissions](submissions), [build response](build.json), [status response](final-status.json), [reuse response](reuse-build.json), and [independent review](review/independent-001/REVIEW.md) retain the concrete path.

From the `specification_methodology` repository:

```sh
python3 -B a_c/build_tenants/graphify/code/ac_project.py status \
  --run stdo_skills/.ai-workspace/work/T003_PROJECT_REPRESENTATION/abiogenesis-01/run
```

The status command requires the selected source and machinery to remain current. If ABIogenesis subsequently changes, preserve this frozen result and prepare a fresh run rather than treating it as current.
