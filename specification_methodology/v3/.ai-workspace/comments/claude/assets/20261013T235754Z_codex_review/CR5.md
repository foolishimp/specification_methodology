# CR5 — Cross-family critical review of the frozen Codex v3 candidate

Reviewer: a Claude activation, a different model family from the Codex author. It has read access only and no repair grant. It did not read the Claude candidate's members.

Subject: `build_tenants/codex/` at `9bc8962` (product source). Evidence: `qualification/` at `3ad1fca`. History: `31f28f9..a9adce2`, the T-002-CODEX ticket at `a9adce2`, the Codex return post, the dogfood comparison directory (`04b0c9a`) and the iteration-2 posts (`638c463`). Common contract: PRODUCT.md (Construction Authority, Development Isolation, C3 Construction Contract) and `requirements/A_C_DEPENDENCY.md`.

Standing: this file is commentary. It accepts nothing and disposes nothing.

Copy integrity:
- The scratch subject copy matches `git ls-tree 9bc8962` blob-for-blob for all 362 files. It lacks only the two a_c install symlinks, so those facts were read from git.
- The scratch evidence copy matches `3ad1fca` for all 1,407 files.
- `git diff 9bc8962 3ad1fca` touches only `qualification/`.

## Summary

The RETURN is largely truthful about its own limits. It claims no acceptance, discloses its failed runs and states its residuals.

The weakness is evidential. Criterion 4 is barely exercised on the frozen subject:

- Only one of the 31 synthesis actor runs used frozen frame bytes, and that run's task was rewritten after a failure.
- Four of the six frames have no fresh-actor run on any synthesis cut.
- Oracle independence degraded across rounds. The author had seen the oracle, repaired the source in response, and re-ran the same oracle twice.
- Every source review received a packet the author assembled. Each broad review found a new material contradiction, up to the last broad review, which ran on `146e6ad`. On `9bc8962` there is only a 5.6 KB targeted confirmation.

The merge to `main` happened at the owner's recorded request. It does not meet the Development Isolation condition: "acceptance of the checkpoint review". No review had been accepted when the merge happened.

## 1. Actual-use evidence (criterion 4)

### 1.1 Run inventory (synthesis campaign)

| Group | Cut | Runs | Frame(s) and digest prefix | Oracle | Independent grading |
|---|---|---:|---|---|---|
| `use/` | `a746559` | 10 | WORK_RECOVERY `b353d2…` (C1–C4, C3b, C8, D1); EVALUATION_CONJUNCTION `8ee2f5…` (C5–C7) | `runs/oracle` `8024b4…` | Grader 1 hit `error_max_budget_usd` (USD 2.829) and returned no judgment. Grader 2 graded only C5–C8 and D1 (5 cases). |
| `use-final/` | `9982ab8` | 10 | WORK_RECOVERY `66475e…`; EVALUATION_CONJUNCTION `479c95…` | same | **None.** `prompts/use-final-grade-{1,2}.txt` exist, but there is no `runs/use-final-grade-*`. |
| `use-77/` | `77f2efb` | 10 | WORK_RECOVERY `16f179…`; EVALUATION_CONJUNCTION `ddcaf2…` | same | Two graders on identical 79,796-byte packets |
| `use-d1-hard-cut/` | `9bc8962` | 1 | WORK_RECOVERY `c18b97…` (frozen) | Successor `8392aa…`; the hidden check is moved into the task text | Host checks only |
| `entry/` and `entry/bound/` | `9982ab8` with rc.2 basis | 3 + 3 | No frame supplied. The ordinary `stdo-work` skill plus tools; the actor used rc.2 deciding clauses. | D1 oracle | Host checks only |
| Dogfood `matched_v2` / `matched_v3` | rc.2 / `9bc8962` | 1 + 1 | Preparer-selected packets. The v3 packet = bootstrap, standards README, work skill, WORK_RECOVERY and EVALUATION_CONJUNCTION. | Codex assessor `ORACLE.json` | The same Codex assessor read both responses by hand. |

Every actor ran as `claude -p --model opus --effort high --tools "" --max-turns 1` (`run_actor.py`), except the six entry runs, which had Read, Glob and Grep.

Host counts recompute from the `APPLICATION_REPORT.json` files: 82/1, 83/0, 81/2 and 11/0 checks met/unmet, with 21, 21, 21 and 6 subprocess executions.

### 1.2 Frame coverage at the frozen cut

`prepare_use.py` assigns the frame by case prefix: C5–C7 get EVALUATION_CONJUNCTION, everything else gets WORK_RECOVERY. Recomputing `git show <cut>:…/frames/<F>.md | sha256` confirms that every round's `frame_sha256` matches its named commit. The digests differ between all four cuts.

| Frame (bytes at 9bc8962) | Frame-alone fresh-actor runs at 9bc8962 | Runs at other synthesis cuts | Historical runs |
|---|---:|---:|---|
| WORK_RECOVERY (53,174) | 1, the D1 hard cut | 21 | — |
| EVALUATION_CONJUNCTION (33,463) | 0. It appears only inside the dogfood v3 packet. | 9 | — |
| CONSTITUTIONAL_DERIVATION (55,748) | 0 | 0 | `C3/use/derivation` at `b0ec615` (2026-10-12, pre-synthesis) |
| DOMAIN_BINDING (40,164) | 0 | 0 | `C3/use/domain` at `b0ec615` |
| RELEASE_ADOPTION (33,794) | 0 | 0 | `C3/use/release` at `b0ec615` |
| TRIAGE_CARRIER (67,563) | 0 | 0 | none. The entry actor "declined candidate `TRIAGE_CARRIER`" (`entry/bound/RETURN.md`). |

The C3 RETURN says historical cuts "do not gain standing on this source". Applying the 77f2efb runs to 9bc8962 rests on an author-only argument (`APPLY_USE_RETURN.md` §"Applicability to the subsequent 146e6ad repair"). The RETURN itself says they "are not ten new runs against `9bc8962`".

### 1.3 Oracle independence and timing

Points that hold:
- A fresh Claude designed the oracle: `runs/oracle`, opus, no tools, 27,191 bytes, USD 0.546. Its prompt contained only common requirements: "You have never been given either candidate implementation."
- The oracle necessarily predates the actor runs. `prepare_use.py` builds every TASK and PROMPT from `ORACLE.json`'s own `task` and `workspace` fields. Git cannot show the order, because all evidence lands in the single commit `3ad1fca`.
- No oracle text reached the actors. Every actor `INPUT.json` has `oracle_excluded: true`. A scan of 1,131 six-word windows from oracle checks, forbidden items and rationales found 0 hits across all 31 actor prompts. No `expected`, `forbidden` or `outcome_class` token appears.

Points that weaken independence:
- **The author selected the cases.** The Codex-written designer prompt fixed all eight themes ("Prioritize these eight cases: … supported one-frame direct work with no required executive"). These are the behaviours the RETURN claims.
- **The author's preamble leaks paraphrase.** Every actor prompt begins with Codex text, including: "Do not ask for already supplied authority or invent a mandatory extra actor. If a material input is actually missing, preserve that unresolved result" and "do not claim commands ran or effects occurred".
  - The first sentence restates C8's forbidden "Stopping or deferring because no Executive … is present".
  - The second restates C3b and C6's expected unresolved outcome.
  - The third overlaps C8's "Report claiming a review was performed".
  - Criterion 4 asks for an actor "given only that frame and the subject".
- **The same oracle was reused after the author had used it.** The author's host checker encodes the oracle, so the author knew it.
  - The C6 failure at `a746559` drove a source repair at `79e53e3`, followed by two re-runs against the same oracle.
  - The `use-final` C4 and C6 selectors were repaired after the first host run (`use-final/host-before-parser-repair/REASON.json`).
  - Both changes are disclosed and the first observations are kept. But the later passes are not "without private validator knowledge or the author's memory" (criterion 4).
- **The D1 successor tests a different task.** After the oracle-validity review (`runs/d1-oracle-validity`), the author chose to add the hard-cut rule to the task text: "remove the old exact name APP_TOKEN from all files". The reviewer's first-listed correction was to relax the check. The successor's pass therefore shows discovery plus instruction-following, not the original judgment.

### 1.4 Context measurement

For the CLI actors, measurement holds:
- `prepare_use.py` records `prompt_bytes` before the call.
- `run_actor.py` refuses prompts over 120,000 bytes before invoking the model.
- Actor prompts ranged from 29,957 to 55,588 bytes.

The entry runs used tools, so their bytes are acquisition accounting computed afterwards, not a pre-read measurement. The return discloses this.

Codex Writer and Executive activations report self-measured acquisition after the fact; see `METHOD_RETURN.md` ("six-file source preimage is 475,846 bytes") and `PROFILE_RETURN.md`. Their parent token and spend use is "not instrumented". The C3 Limits rule, "reports the context measured before reading and the spend afterwards", is therefore met only for the CLI calls.

### 1.5 Grading results that exist

At `77f2efb`, the two graders disagree on 4 of 10 cases:
- Grader 1 gives "finding (low)" for C3, C3b, C6 and C8 (result-coordinate and effect-label fidelity).
- Grader 2 gives "supported" for all four.
- Both fail D1 (2 unmet checks; fallback guard counterexample).

The final per-case dispositions in `USE_ADJUDICATION.md` were made by the author's Executive.

At `a746559`, one grader passed C5, C7, C8 and D1 and failed C6. It attributed the C6 failure to method wording, and the source was repaired. In all, 15 of 31 actor runs have any independent grading.

### 1.6 The dogfood comparison of v2 and Codex v3

Design (from `ACTIVATION.json`, `MATCHED_TASK.txt`, `ORACLE.json`, `MATCHED_INPUT_MANIFEST.json`, `MATCHED_OBSERVATIONS.json` and `COSTS.json`):
- One response per arm, with both tasks A and B in a single prompt. There are no repetitions and no no-method control.
- Both arms used the same model and settings (opus, high, no tools, one turn).
- The packets were chosen by the preparer and differ in size: 92,761 bytes for v2 and 114,973 for v3. No discovery was tested.
- The task and oracle were frozen before the calls (`frozen_before_calls: true`).
- The grader was the preparing Codex assessor, reading by hand, unblinded, and from the author's model family.
- Both arms satisfy all 10 common discriminators. The task therefore does not separate v2 from v3.
- After the call, one v3-specific expectation was set aside (`ORACLE_LIMITS.json`). This is disclosed.
- Cost: USD 1.643 for three calls; 1,499 s of wall time.

What it supports: both methods' supplied entry packets let one opus response reach the 10 safe decisions on two synthetic tasks. It supports no improvement, superiority or usability-difference claim. REVIEW.md says so ("neither the byte difference, cost nor latency establishes method superiority").

Process concerns:
- **Verdicts changed without new evidence.** `PRE_FINALIZATION/CLOSED_RESULTS.json` had P1 = `indeterminate` and P4 = `indeterminate`. The final results have P1 = `satisfied` and P4 = `falsified`.
  - `FINALIZATION_NOTES.json` gives the source as "Parent Executive clarification after user challenged arbitrary 160 KB allowance" and adds "No new paid calls, source acquisition or candidate changes were used".
  - The verdicts are hard-coded in `finalize_review.py` ("Report Writer only").
  - `ACTIVATION.md` says the parent "may record a disposition or necessary clarification; it does not rewrite the independent findings".
  - Read against the predicate text, the P1 rescoping is defensible. The change is still an Executive-influenced verdict change.
- **The same-family assessor overruled the cross-family reviewer.** REVIEW.md overrules or leaves unestablished 7 of the 10 findings from the fresh Claude source assessment (F1, F2, F4, F5, F6, F8, F9). The overruling assessor is the same family as the author.
- **The independence label is not supported.** The ticket calls this an "independent comparison". REVIEW.md says it is a "same-family synthesis, not cross-family acceptance". `ACTIVATION.json` records no same-family exception with a reason, which the PRODUCT Independence rule requires.

## 2. Frames and acquisition

- **Excerpts are verbatim and current.** Six frames, 283,906 bytes in all, 33,463 to 67,563 each. Every frame fits the 120 KB CLI envelope.
  - I recomputed all 89 `Source:` excerpts at 9bc8962.
  - 89/89 owner SHA-256 pins match the owner file bytes.
  - 89/89 excerpt bodies equal the owner section text once link targets are normalised. The comparison therefore does not test whether relocated links are correct.
  - The pins bind whole owner files, not sections, as the frame preface says ("A source digest binds the entire owner"). There are no section digests to recompute. Section fidelity was checked by text equality instead.
- **Every frame carries the core.** All six include `FOUNDATIONS.md — Result algebra` and `— Result conjunction`.
- **Frames are generated from sections, not from a_c.** They are hand-selected section projections (`refresh_views.py`), not a_c projections. The tenant declares this equivalent: DESIGN.md says "Frames are named projections of owning clauses, regenerated and checked when any selected owner changes". The declaration names no sufficiency criterion.
- **Compression pins are current; meaning is not.** All 32 compression pins match (25 owner-list pins plus 7 `source_digest`). Two meaning drifts remain:
  - `authority_compressions/README.md:7–9` calls Foundations and the library "non-deciding explanations". This is the Codex purpose review's F1, which I confirm.
  - `stdo_compressed.md` keeps the software-only chain (Codex F3).
  - The artifact check cannot detect either.

## 3. a_c representation

- **Two programs.** The current one is `qualification/C3/synthesis/a_c/program.json`: 53 clauses, 14 symbols, 5 frame indexes and 3 residuals (`core-coverage`, `family-coverage`, `semantic-proof`). The superseded one, `qualification/C3/a_c/program.json`, has 6 clauses and 5 symbols.
- **The checker matches its pins.** It is Axiom Indexer v2.5.1-rc.2. `INSTALL_VERIFICATION.json` values equal every A_C_DEPENDENCY pin: tag `9bff233…`, commit `9a9c479…`, tree `3a553ce…`, subtree `6dae168…`, inventory `55a2061…`, executable `5a2e0cb…`, schema `43326db…`, output contract `c124264…`, theory `cbe2edb…`. The 7-member install sits in tenant territory.
- **What the checker checks.** `validation.json` reports no diagnostics. `MECHANICAL_RESULT.json` covers source resolution, reference/materialized projection parity, transitive selection, empty-selection and stale-map refusals, joins and archive manifests. All of these are structure and relations.
- **What the checker does not check.** The "finite semantic experiments" are author-written Python (`model.py`, `finite_check.py`) with an oracle by the same author, as `AC_RETURN.md` states. No claim goes beyond A_C_DEPENDENCY's structural limit.
- **The contradictions the independent reviews raised** (`REVIEW_DISPOSITIONS.md`):
  - The source review found A1–A7: guard totality, refinement, evidenced performance, reconfiguration, coordinator owner, stop/decision and allocator grants. It also found B omissions, C vocabulary and standing problems, and D (family fidelity).
  - The finite review found Finite 1–10. The first, rated high, was that "the coordinate guard contradicts `evaluation()` and admits no verdict for valid fixtures". Others: bare negation, a mutant-detection overclaim, and a dictionary-copy "recovery proof".
  - The source recheck found R1–R10; the finite recheck found N1.
  - The final counterexample review found C1–C8. The boundary recheck closed C1–C4, C6 and C7 and the substance of C5 and C8, then raised R-a–R-e. The parent corrected R-a–R-e with no independent confirmation, which is disclosed.
- **What remains unresolved:**
  - D, family fidelity
  - finite conjunction/effect integration
  - associativity of retained components
  - positive combination of separate evaluations
  - recovery, which is only a decision table over five stipulated rows
  - stipulated authentication of subject and basis
- **A_C_DEPENDENCY proof claims:**
  - Present: dispositions (`SOURCE.md`), signature, program, map and bindings, and reproducible mechanical results.
  - Partial: independent fidelity judgment. Selected clauses were confirmed; family fidelity was not.
  - Absent: actual-use evidence for the interpretation.
  - Selection of the evaluation was indirect, through EC-CODEX-SYN-01's Evidence list under the owner's run-to-completion instruction.
- **The entry route points to the old model.** In the subject, `a_c/README.md` still calls the six-clause program the "Current C3 interpretation". `stdo_3.json` routes the formal implementation to this page (Codex F2, which I confirm).

## 4. Packaging

- **Members and plugin.** The package has 80 members totalling 1,653,686 bytes; I recounted both. The plugin is `spec` 3.0.0 for both Claude and Codex.
  - The Claude manifest adds only `./claude-skills/refresh`. The Codex manifest has no refresh skill.
  - `CANDIDATE.json` has `target_version: 3.0.0`, set before the owner's candidate-number decision.
- **Schemas and templates.** Both schemas pass Draft 2020-12 `check_schema`. `PRODUCT_DEFINITION_TEMPLATE.json` fails only on its two `REPLACE_WITH_*` placeholders. The other JSON files parse.
  - The basis-URI pattern in `product-definition.schema.json` admits only RC cuts. That matches the v2.5.1 release schema and successor RELEASE_METHOD (`stdo://releases/v<version>-rc.<n>/`), so it is not a defect.
- **Release artifacts.** There is no successor release manifest, release note or install coordinates. PRODUCT allows these to stay unresolved until the release-candidate cut.
- **Identity.**
  - The calculus-basis identity in AXIOMATIC_CALCULUS is `derivation_basis` with 14 principle references into `stdo://releases/v2.5.1-rc.2/`.
  - Verification reconstructs three rc.2 members' exact bytes from `verification_material/DERIVATION_SOURCES.json`. That file is 27,832 bytes, including 5,752 literal bytes and the full historical manifest UTF-8.
  - `IDENTITY_CHECK.json` shows 6 package reads, 0 outside reads, 0 network events and 19 refused negative controls. The verification ran against a "Hypothetical schema-valid publication fixture, not an issued release" using qualification tooling.
  - So identity is verifiable without a predecessor install. IDENTITY_METHOD and AXIOMATIC_CALCULUS state that the predecessor bytes are evidence and not operative. But the identity is still defined over predecessor content, and no successor identity has been issued.
  - This anticipates the open owner decision on how identifiers are "issued and accepted into use without depending on files of the previous release".

## 5. Process

Points that hold:
- **Territory.** All 17 non-merge commits on the tenant branch outside `main` change only `build_tenants/codex/`. Two inward merges complete the 19 the iteration-2 post reports. The merge `a9adce2^1..a9adce2` changes 1,238 files, all under `build_tenants/codex/`. The merged tree equals `3ad1fca`.
- **Contract admission.** EC-CODEX-SYN-01's recorded SHA-256 `d5df2236…` recomputes from the ticket text. It was admitted at `bb76b1d` (05:08:45), before the first construction commit `3cfb2ab` (05:14:52).
- **Spend.** `COSTS.json` records 69 calls and USD 29.6238964 against the USD 30 allowance. The largest selected input was 119,727 bytes. The only cap overrun is `use-grade-1`, USD 2.829 against a USD 2 cap, which is disclosed. The dogfood comparison adds USD 1.643 under a separate USD 8 allowance.

Review independence:
- All 32 `runs/` reviews and grades are Claude opus, cross-family to the author, with no tools. Codex assembled every packet. The PRODUCT Reviewer frame requires "independently acquired evidence".
- Some prompts state the expected conclusion. For example, `effect-owner-final`, at 5,597 bytes, asks the reviewer to confirm "completedrequested + observedabsentunrequested = completed".
- Integration reviews received "Changes and 15 lines of boundary context … not complete omitted bodies".
- **Defects never converged.** Every broad review found at least one new material contradiction:
  - `final-core` at 875a56e: associativity
  - `repaired-core` at 9982ab8: two
  - `closure-core-formal` and `closure-consumers` at 77f2efb: one each
  - `closure-last` at 146e6ad: "not yet a pass"
- The only review on 9bc8962 is the narrow effect-owner check.
- Reviewer prompts say "You did not author it" while the text includes ported Claude contributions (DESIGN.md §Source contributions). This is the open ported-part policy.
- No same-family or author result is counted as acceptance. Two same-family items are labelled "independent": the dogfood comparison in the ticket, and the iteration-2 purpose review in `20261013T234754Z`.

Merge authority:
- **The rule.** PRODUCT Development Isolation, a local axiom in `stdo_3.json` `local_constitution.axioms[1]`, says: "A tenant branch merges to `main` only on the product owner's acceptance of the checkpoint review."
- **The only record of authority** is the ticket's "Current Owner Direction". It was added in `638c463` at 10:48:55, three seconds before `a9adce2`:
  > 2026-10-14: Jim identifies the current candidate as v3 iteration 2 … and requests: "i want a full checkpoint commit and merge of the current work". … This authorises merging the current Codex tenant for a review baseline; it supersedes the earlier execution contract's no-merge restriction for this checkpoint only. It does not accept C3 members…
- **The condition was not met.** The merge commit says "for review". Both iteration-2 review posts are `Status: Open` or unaccepted, and this critical review was opened afterwards (`dbf1ef1`). The ticket presents the owner request as superseding an execution-contract restriction. It does not address the local axiom.
- **No owner-authored record can be told apart.** Every commit carries the same Git identity.
- **The cleanup clause was followed.** The tenant branch and worktree were removed as the rule requires. `tenant/codex/c3-round-1` remains; it is merged transitively but not deleted.
- **Finding.** The owner asked for the merge, so the merge is authorised in substance. The rule's stated condition, acceptance of a checkpoint review, was not satisfied, and no exception to the axiom was recorded.

## 6. RETURN claims (`qualification/C3/synthesis/RETURN.md`)

| # | Claim | Assessment | Evidence |
|---|---|---|---|
| 1 | Frozen at `9bc8962`; the package entry leads to the standards | Supported | Tree match; `9bc8962..3ad1fca` changes only `qualification/` |
| 2 | Does not accept C3, select a tenant, merge or release | Supported | True at return time. The later merge came from a separate owner direction. |
| 3 | Construction used installed rc.2 (manifest `3d860ff…`) under EC-CODEX-SYN-01 | Supported | `CANDIDATE.json`; contract digest recomputed; admitted before construction |
| 4 | The encoding tool is the pinned rc.2 Axiom Indexer | Supported | `INSTALL_VERIFICATION.json` equals every A_C_DEPENDENCY pin |
| 5 | Five relationships are "operative in deciding families" | Partly | Sampled source reviews only. Use tested two frames; dogfood P2 `indeterminate`; a_c `family-coverage` residual. |
| 6 | Families were "checked through their affected dependencies" | Partly | Integration reviews ran on earlier cuts with hunk-only context; only a narrow check on 9bc8962 |
| 7 | No general equivalence or categorical result is inferred | Supported | FOUNDATIONS states the demonstration standard; no steel thread |
| 8 | C6 performance defect repaired at `79e53e3`; fresh C6 returns distinguish P1 and P2 | Supported | Host checks at 9982ab8 and 77f2efb. Graded only at 77f2efb, where both graders agree. |
| 9 | Effect-owner repair; "final selected source review is consistent" | Partly | 5,597-byte author-framed prompt states the expected joins |
| 10 | Operator, negation and consumer-drift repairs | Partly | Reviews show successive repairs, each later review finding new defects; none broad on 9bc8962 |
| 11 | Stale projections refreshed | Partly | Pins: 89/89 and 32/32 current. Meaning drift remains (F1 standing, F3 chain). |
| 12 | Selector and oracle defects corrected without editing failed returns | Supported | First reports kept; D1 successor labelled. The task change is disclosed, but its pass carries less weight (§1.3). |
| 13 | Fresh reviewers read frozen subjects or excerpts and edited nothing | Supported | No tools. Packets were author-assembled (§5). |
| 14 | Claimed tool executions in `repaired-core` excluded | Supported as disclosed | The response does claim workspace reads with no tools. I did not re-trace the exclusion. |
| 15 | Artifact checks: 80 members, 1,653,686 bytes, 89 sections in 6 views, 32 pins, 691 rows | Supported | Recomputed. The 71 predecessor pins and 553 links were not recomputed. |
| 16 | Identity: 14 references, 3 members, 6 package reads, 0 outside, 19 controls; hypothetical fixture | Supported as recorded | `IDENTITY_CHECK.json`; not rerun by me |
| 17 | a_c: mechanics separate from fidelity; final review confirms substantive repairs; last corrections parent-checked | Supported | `REVIEW_DISPOSITIONS.md`, `ac-boundary-recheck` |
| 18 | Three frozen ten-case rounds plus a successor, sandboxed, originals retained | Supported | Counts recomputed |
| 19 | "Two fresh graders share fixed evidence" | Partly | True only for 77f2efb. a746559 had one effective grader on 5 cases; 9982ab8 and D1 are ungraded. |
| 20 | Ordinary entry proves source entry with rc.2 assistance, not installed v3 | Supported | `entry/bound/RETURN.md` |
| 21 | Conservation: 657/33/1 = 691, not acceptance | Supported | Recounted from `CONSERVATION.json` |
| 22 | Rows are not summed into "31 cases passed" | Supported | Per-cut tables only |
| 23 | 69 calls, USD 29.6238964, max 119,727 bytes, one cap overrun | Supported | `COSTS.json` |
| 24 | Five open obligations listed | Supported | They match PRODUCT open decisions |
| 25 | No failure converted to acceptance | Supported | With the caveats in claims 12 and 19 |
| 26 | Whitespace audit clean on authored surfaces | Not tested | — |

Tally: 19 supported or supported as recorded, 6 partly supported, 0 unsupported, 1 not tested. The weaker claims live outside the RETURN. The ticket says "independent comparison" and the iteration-2 post calls the purpose review "independent". Both are same-family (§5).

## 7. Findings

| ID | Severity | Claim | Evidence | Smallest repair |
|---|---|---|---|---|
| CR5-01 | High | Criterion 4 is not evidenced for the frozen frames. | One frame-alone run at 9bc8962 (the D1 hard cut). EVALUATION_CONJUNCTION has 0. CONSTITUTIONAL_DERIVATION, DOMAIN_BINDING and RELEASE_ADOPTION were tested only at `b0ec615`. TRIAGE_CARRIER was never tested. 30 of 31 runs used frame digests different from 9bc8962 (§1.2). | Before any `accept`, run fresh actors on each frozen frame for its selected task, under a new oracle. Otherwise limit the criterion-4 claim to the tested frames and cuts. |
| CR5-02 | Medium | Oracle independence is partial and weakened across rounds. | The author chose the 8 themes. The author's preamble paraphrases C8 and C3b/C6 expectations. The same oracle was re-run twice after a source repair the oracle drove. Selectors were changed after observation. The D1 task was rewritten to embed the hidden check (§1.3). | For the next frozen cut, a fresh designer supplies the case list and oracle, withheld from the author until after the runs. Use a neutral preamble. Fix selectors before the runs. |
| CR5-03 | Medium | Grading coverage is thin and diverges. | 15 of 31 runs graded. 9982ab8 ungraded (packets prepared, not run). The a746559 round has a single grader. At 77f2efb the graders split on 4 of 10. The author's Executive gives the final dispositions (§1.5). | Run the prepared 9982ab8 grading, or mark that round host-only. Have an independent party adjudicate grader disagreements. |
| CR5-04 | Medium | Review evidence is author-acquired, and broad review never converged before the freeze. | Every packet was built by Codex, some with stated expectations. Each broad review found a new contradiction. On 9bc8962 there is only a 5.6 KB targeted check (§5). | One broad source-first review of 9bc8962 in which the reviewer acquires from the frozen commit and records its own acquisition, with a neutral prompt. |
| CR5-05 | Medium | The merge to `main` does not meet the Development Isolation condition. | Local axiom: "only on the product owner's acceptance of the checkpoint review". The record is an owner merge request "for a review baseline" (§5). No review was accepted. | The common pen records the owner's acceptance of a named checkpoint review, or an explicit owner exception to the merge clause, and cites it in T-002-CODEX. |
| CR5-06 | Medium | The dogfood comparison cannot support comparative claims, and its verdicts changed after Executive input. | n=1 per arm, no control, different packet sizes, unblinded same-family grader, all 10 discriminators passed by both arms. P1 and P4 changed with no new evidence despite "does not rewrite the independent findings". It is labelled "independent", with no recorded same-family exception (§1.6). | Report it as a non-discriminating smoke test. Record the same-family exception and reason. Keep the pre-finalisation verdicts as the assessor's result, with the Executive's clarification shown separately. |
| CR5-07 | Medium | Independent fidelity of the a_c interpretation is incomplete. | Family fidelity is unresolved. Conjunction/effect integration, associativity and positive separate combination are unimplemented. R-a–R-e are parent-checked only. The finite oracle has the same author (§3). | An independent fidelity review against the accepted claim set, covering family coverage, plus a confirmation of R-a–R-e. |
| CR5-08 | Medium | The successor identity is still defined over predecessor content and has not been issued. | 14 rc.2 principle references; reconstructed rc.2 bytes; verification used only a hypothetical publication fixture; no successor manifest (§4). | The owner decides the identifier policy, which is already listed as open. Then issue the identity from a real publication manifest and verify an installed copy. |
| CR5-09 | Medium (confirms Codex F1) | The compression README denies the deciding standing of Foundations and the library. | `authority_compressions/README.md:7–9` against `FOUNDATIONS.md` ownership | Correct the standing, then check the meaning, not only the digest. |
| CR5-10 | Low (confirms Codex F2) | The a_c landing page selects the superseded six-clause model. | `a_c/README.md:3–7`; the 53-clause program is under `qualification/C3/synthesis/a_c/` | Link the current program, signature, bindings and inventory; mark the old model historical. |
| CR5-11 | Low | The Limits rule is met only for CLI calls. | Codex Writer and Executive context is self-reported after the fact and spend is not instrumented (§1.4) | Record a declared and measured selection per Writer activation, or declare the gap at admission. |
| CR5-12 | Low | All usability evidence comes from one model, which also designed the oracle and graded. | `--model opus --effort high` for actors, oracle designer, graders and reviewers | Add at least one actor or grader from a different model family or configuration. |
| CR5-13 | Low | Version identity is asserted before the owner decides it. | Plugin `version: 3.0.0` (both manifests); `CANDIDATE.json target_version 3.0.0` | Mark it as provisional or omit it until the candidate-number decision. |

## 8. What holds

- The tenant stayed in its territory: 17 of 17 own commits touch only `build_tenants/codex/`. The merge scope is exactly the tenant directory, and the merged tree equals `3ad1fca`.
- EC-CODEX-SYN-01 was admitted with a recomputable digest before construction began.
- The A_C_DEPENDENCY pins are verified exactly. No claim exceeds structural validation without being labelled as same-author finite experiments.
- Frames are verbatim (89/89) and digest-current. Every frame carries the core result algebra and conjunction. All 32 compression pins are current.
- Actor inputs exclude oracle text (0 hits). Prompt bytes are measured and capped before each call. Failed runs, first host reports and superseded drafts are all kept.
- The RETURN discloses its limits truthfully: rc.2-assisted entry, no installed v3, applicability of runs across cuts, grader disagreement, the cap overrun, and uninstrumented parent spend.
- Spend reconciles: 69 calls, USD 29.62 of 30.
- Schemas are valid. The templates fail only on placeholders.
- The C6 counterexample led to a real source repair, and later C6 runs reflect it.

## 9. Limits of this review

- I am a Claude activation: cross-family to the author, but the same model family as the actors, oracle designer and graders. Correlated judgment with them is not excluded.
- I did not rerun `check_artifacts.py`, `qualify.py`, `derivation_material.py` or the host checks. I relied on recomputing selected counts and digests.
- I did not assess per-member semantic conservation of the 691 rows, or the conformance discriminators.
- I did not read the Claude candidate.
- The excerpt comparison normalised link targets.
- The owner's merge instruction is known only from the ticket text written by the common pen.
- Reviewer and actor timestamps are absent. I inferred ordering from data flow (`prepare_use.py`), not from logs.
