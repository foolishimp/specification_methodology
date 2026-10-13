# C3 Cross-Synthesis Ledger, Claude Line

This file is the Claude line's record of the cross-synthesis rebuild. The common pen (currently Codex) is the only writer of tickets, so decisions are recorded here, in the tenant's own territory, and the pen transcribes them into [T-002-CLAUDE](../../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md). Nothing here is acceptance. Member acceptance, the checkpoint and any merge to `main` remain the product owner's.

## Owner Instruction

The product owner, 2026-10-14 (local time), after reading the [cross-synthesis proposal](../../../../.ai-workspace/comments/claude/20261013T174341Z_STRATEGY_cross_synthesis_rebuild.md):

> so i'm giving you the go ahead to refactor v3/claude under the new requirement & specification, you are not to block and will review the work in the morning

Under T-002's Admission Mechanism, the product owner's explicit instruction is the only human override and is recorded verbatim. It admits this rebuild without a separately drafted execution contract. "Not to block" is read as: where the proposal left a decision open, the Executive takes the default below, records it, and continues.

## Basis

| Coordinate | Binding |
|---|---|
| Branch and worktree | `tenant/claude/c3-synthesis`, worktree `/Users/jim/src/apps/specification_methodology-claude`, sparse to `v3/specification/`, `v3/.ai-workspace/` and `v3/build_tenants/claude/` |
| Input commit | `47ef3e8cf8524fce51ee4c81205601ab2af52fa2` on `main`; its `specification/` is identical to `c0beefd` |
| Base | `build_tenants/claude/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac` (unchanged on `main` at the input commit) |
| Porting source | `build_tenants/codex/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read with `git show` under Porting reads |
| Builder | installed `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |

Input snapshot, SHA-256 of each member as read from the input commit:

| Member | SHA-256 |
|---|---|
| `specification/INTENT.md` | `d8221450da268fa69dac954caa25ed95f6098e20ce7dd1d5dba39a2a4f11e65a` |
| `specification/PRODUCT.md` | `edbcddfe79e54132774e4a20a363a0c2e12992bbb3c66c642244b09b0d61732a` |
| `specification/GOALS.md` | `56d0829d422606c5a339d762977a230b06b0f90d1c10671bc7869cb4c3126797` |
| `specification/REFERENCE_FRAME_BASIS.md` | `8f6d268bc51211ffccd7ab714b15891b6670429ecdabb9ffd8e0c8c0892090aa` |
| `specification/requirements/README.md` | `9b53473c8a787b23f14d747effca0c2cc0e031f3bb0d94ffb58140e1ce0e8159` |
| `specification/requirements/PRINCIPLES.md` | `0542778cdf097bf224f0e5305cf9a13f7bc9a30d39aa3f4e1d4c59c0ddf1803c` |
| `specification/requirements/CAPABILITIES.md` | `729f122f97e1f6f39ccee828319ca5203bfa74816d3bf2cc9f400080bce76cb4` |
| `specification/requirements/A_C_DEPENDENCY.md` | `e1ace7eb86a6c4a4a554c562fd3a9ec5b2c6e32027147b19c509bb52e370c9e4` |
| `specification/requirements/PREDECESSOR_CLAIMS.md` | `fbeb8fd2eda0af32873c287130457fc3800d44987da3b6675a00c8b4333c2f69` |
| `specification/conformance/README.md` | `a610a32dc17e0104a09a4b001fc220757211e0555301142e502bf0b5ff3ed5d4` |
| `stdo_3.json` | `20e9a5f259c32d31caf0edef1ddbd978ecdeb76ffc075aaea8cffa2979444a1a` |
| `build_tenants/README.md` | `04c609d730c68d67ef92d006ecfde45cdd9a02684210a5d4a5391d3be87a9ec3` |
| `.ai-workspace/tickets/active/T-002-c3-successor-construction.md` | `62022dfa3425b4d61cabc2712524d0e5816d5e540a12b02ccbd6f5081bf3865d` |
| `.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md` | `bcab947d499f13ceb836e8e314330e2c707c6902cf44180274a0360549f28ac6` |

If the common specification changes on `main` during the rebuild, the change is recorded here and the rebuild continues against this snapshot. The product owner decides whether to rebase.

## Defaults Taken For The Open Decisions

The numbers refer to the decisions in the proposal.

1. Basis: the snapshot above. Codex's two open findings on the common specification (the successor locus required for every disposition; the `stdo_3.json` route to a Codex directory that does not exist) do not change this line's work. This line follows acceptance criteria 1 and 3, so `not applicable` and `intentionally removed` rows carry a reason, not a locus.
2. Independence: every review in this rebuild is a same-family working check by a fresh Claude context that did not write the subject. Each is marked as such and none counts towards acceptance. Acceptance reviews are cross-family and remain open.
3. Ported parts: ported text stays verbatim where possible. It is compared byte for byte with its source at `31f28f9`. A Claude Reviewer that did not do the porting compares it with the previous release. Claude-written text around a port is left for Codex's cross-family review.
4. Ledger: this file, transcribed later by the common pen.
5. Porting commit: `31f28f9`. Codex's unmerged repair round at `5b4aebb` is not read.
6. Steel thread: not waited for. Its later corrections may reopen accepted Foundations members.
7. Compressed summaries: their ten rows stay `unresolved`, which is lawful during construction. They must close before a release-candidate cut.

## Configuration

One Executive (this Claude session) keeps the outcome, the basis and the frontier, and selects the next activation from bounded results. Writers are fresh Claude subagents, each given an exact file territory inside `build_tenants/claude/`. Reviewers are fresh Claude subagents that record expectations from the sources before opening the subject. At most three activations run at once. The Executive changes no candidate text. Git setup, commits and this ledger are Writer effects, and each is recorded below as a role change before the effect.

## Execution Record

2026-10-13T17:56Z (UTC) — Role change, Executive to Writer, for setup: branch `tenant/claude/c3-synthesis` cut from the input commit, sparse worktree created, this ledger written. Role returns to Executive after the setup commit.

2026-10-13T17:58Z — Activations W1 (design re-entry and verified work plan; territory `design/` and `qualification/C3-SYNTHESIS/PLAN.md`) and R0 (independent expectations; territory `qualification/C3-SYNTHESIS/EXPECTATIONS.md`) started together. R0 reads only the common specification and the installed release, and opens neither candidate.

2026-10-13T18:12Z — R0 returned `candidate_ready`: EXPECTATIONS.md (22,754 B). It contains 87 expectations across the eight items, 12 negative expectations, 10 ported-part checks and 8 recorded ambiguities in the common specification (A1 to A8). R0 confirms it opened neither candidate. Disclosure: it read the common `PREDECESSOR_CLAIMS.md` header, which summarises earlier Claude-line findings. Executive disposition: accept as the oracle for this rebuild's working reviews. A1 to A8 go to the product owner and the pen in the handoff. Role change to Writer to commit it and this entry, then back to Executive.

2026-10-13T18:13Z — Common input changed on `main` after the snapshot. The common pen committed `bb76b1d` and `a7eba66` for the Codex line. Material changes:
- PRODUCT Construction And Context Management and the Bounded Transitions requirement item 5 now treat the workspace as the continuing truth surface, with each actor's context as a disposable account of it;
- one new discriminator (31 in total): a fresh actor whose retained summary disagrees with the current workspace;
- the `stdo_3.json` route to the Codex candidate is corrected;
- GOAL-002 wording is signed off.

Role change to Writer: `main` at `a7eba66` merged inward (`923c755`), as Development Isolation directs for common changes. The snapshot now has these members, at `a7eba66` and matching the pen's Codex snapshot in T-002; all other members are unchanged:

| Member | SHA-256 |
|---|---|
| `specification/INTENT.md` | `dc80dd0e091afe33bfdd097a0850a94aef0d3a7e52ab46ac96b535e76afafec1` |
| `specification/PRODUCT.md` | `c2cfbb87cab2f181dcc7c1b7284a481e0391ea72b02ff2ac46c144eafdbc0b76` |
| `specification/GOALS.md` | `20d2a3a69fead88c0b93d3d35681475a5cab130c481c92474c7f2036f35d1662` |
| `specification/requirements/README.md` | `5d01452ee16fc1b8ac85be9d587fdc2f35687e5aa217c4de644314727882dd1d` |
| `specification/conformance/README.md` | `c4791ca16345345e5c5136a153d6e929d54ec1f191ad98d05ca57a4755485f95` |
| `stdo_3.json` | `e1ce90985492717d4784a0ca5e2426fb50f5f168547ec88ef72e58100836cb12` |
| `build_tenants/README.md` | `3f25650ae4ce45ee31381bee876c47b8e7cb78d6aef50e5654591c7f5f8fd82b` |

R0 is asked to add expectations for the two amendments. W1, still running, is told of the change. Role back to Executive.

2026-10-13T18:27Z — W1 returned `candidate_ready` (committed `087ebe1`):
- `design/` rewritten: DOCUMENT_STRUCTURE, README, new CONSTRUCTION_BINDING and CROSS_SYNTHESIS;
- PLAN.md (30,929 B): the verified gap list, 21 material families, the re-proof span (at least about 154 of 691 rows, to be committed by A6), and activation waves A to D with disjoint territories.

W1's corrections to the proposal are accepted:
- the eleventh unresolved row is the requirements template, not the bootstrap;
- there are 21 families, not about 14;
- premise standing is stated inline, and the gap is the missing family tables.

Executive disposition on design decision D1: `local_repair`. W1 proposed a sixth core result value, `not_performed`. Ruling: the core keeps RF-012's five values, so RF-012 stays `conserved`. An evaluation that was not performed has no closed result. Conjunction keeps three inputs apart: the core values returned, the planned assessments with no closed result, and the required coverage that no planned assessment addresses. A work step's `incomplete` maps to `falsified` only for "a candidate is available", never to `indeterminate`. A Reviewer step that ends `incomplete` leaves its criteria not performed.

Reason: item 3 of the common single result algebra requirement asks that non-performance stay distinct, not that it have its own core value. Item 4 carries the domain outcome with the value; R0 recorded both readings as ambiguity A2. The smaller change conserves RF-012 and does not widen the re-proof span. The alternative, a sixth core value with RF-012 `superseded`, goes to the product owner in the handoff.

Role change to Writer: DOCUMENT_STRUCTURE D1 and PLAN rows A1, A2 and B6 plus the fixed interfaces were edited to this ruling, then committed. Role back to Executive. Wave A starts: A1, A2 and A3.

2026-10-13T18:47Z — Wave A, first returns. Each Writer's subject was committed by the Executive acting as Writer, with role back to Executive after each commit.

- A2 returned `candidate_ready`, committed `823507e`. Changes to EVALUATION:
  - the equivalence ladder ported into §6, adapted in notation only (Codex FOUNDATIONS lines 254–258);
  - §7 owns actual-use evidence of adequate attention;
  - §3 states that an author's fresh context is not independent;
  - §4 refers to FOUNDATIONS Results.

  No frontier row changes disposition, and 8 rows are listed for re-proof.
- RW1, a working review of W1's design at `f7851aa`, started in parallel.
- A1 returned `candidate_ready`. Changes:
  - FOUNDATIONS §4 gains Results (the five values, standing, the no-raise rule, predicate and domain outcome, not-performed as no result) and Conjunction of results (three inputs kept apart);
  - ACTIVATION §3 is renamed "Step results and disposition": `incomplete` maps to `falsified` for "a candidate is available", and `re_entry_requested` is split by cause;
  - 7 delta rows go to A7; frontier rows 516 and 543 go to B2.

Executive rulings on A1's three readings:
- a conjunction whose returned values are all `satisfied` but which has a gap reports `indeterminate`, with each gap recorded by kind — confirmed. The gap record carries the not-performed distinction, which is the D1 ruling;
- the Executive disposition is mapped into the core as the acceptance result — confirmed under item 5 (availability, assessment and acceptance are separate results);
- rows 516 and 543: `superseded` only if their rc.2 claim maps `incomplete` to `indeterminate`, with the common single result algebra requirement named as the replacement relation; B2 verifies the claim text first.

RA1, a working review of A1, started.

2026-10-13T19:02Z — Returns and dispositions:
- A3 returned `candidate_ready`, committed `9d6dd49`. REFERENCE_FRAME refers to its owners for results, conjunction and measurement. Port 3 supplies the import declarations, partly verbatim. §5 outcomes are split by cause. Gap A3 reported, with no activation assigned: the §8 coverage statuses have no core mapping. It goes to the repair after RA23.
- RA23, a working review of A2 and A3, started.
- RW1 returned (`c02ee03`): all five questions `falsified`, with 6 material and 23 minor findings and nothing blocking. Disposition: `local_repair` as W1b on `design/`. The two that most need fixing are F1 (independence when the tenant is the author) and F14 (the frame generator must not cut sections at headings inside code blocks; this gates frame generation).
- RA1 returned (`9f9bd2f`) with two material findings:
  - five admission and activation outcomes in ACTIVATION have no core value;
  - `carried` and `blocked` are mapped to `indeterminate`, although an open ambiguity is a known state.

  Disposition: `local_repair` as A1b. The admission and activation outcomes get their own refinement, mapped by cause. `carried` and `blocked` map to `falsified` for "the ambiguity is resolved". RA1's minor findings are repaired at the same time.
- Outside the subject, RA1 found `gap`, `hold` and `refusal` outcomes in AXIOMATIC_CALCULUS with no mapping. These are added to B8's scope.
- A4a and A5a wait for A1b, because they edit the same members.

2026-10-13T19:15Z — Returns and dispositions:
- A1b returned `candidate_ready`, committed `858ebde`: admission and activation outcomes refined and mapped by cause; `carried` and `blocked` map to `falsified`; RA1's minor findings repaired. Its repairs are checked by the next working review of ACTIVATION. A1b asked for one ruling: a missing capability that refuses activation maps to `out_of_frame`, not `falsified`. The core defines `out_of_frame` as an evaluation that needs an undeclared material relation or capability, and ACTIVATION §2 step 3 already returns `out_of_frame` for a context that does not fit. Assigned to A3b.
- RA23 returned (`e4bd1be`): two material findings, M1 ("owns only" weakened in REFERENCE_FRAME §1) and M2 (an unmapped `translate` authority refusal), plus 8 minor. Disposition: `local_repair` as A3b on REFERENCE_FRAME and EVALUATION, together with the capability ruling and A3's unmapped §8 coverage statuses.
- A4a, for ACTIVATION §1 Transitions and Configuration, started.
- W1b returned `candidate_ready`, committed `105b5a4`: all 29 RW1 findings repaired. The design now reads "author" as the tenant, so every same-family review is a working check only. The design governs where PLAN rows differ; the stale rows are handled in the briefs of A5b and wave B.
- A5a, for the FOUNDATIONS §1 trim, §2 imports and the Actor row, started.

2026-10-13T19:33Z — Returns and dispositions:
- A3b returned `candidate_ready`, committed `b7b8e34`. RA23's M1 and M2 are repaired. `activation_refusal(capability)` now maps to `out_of_frame`, and topology mismatch to `invalid_basis`. The coverage statuses map to the core for "the coverage obligation is met"; an authorised exclusion counts as met, never as covered or performed. RA23's minor findings are repaired except m8, which goes to A5b.
- A gap in PLAN: the family tables for wave A members (F1 to F7) had no activation. They are assigned as follows: F2, F4 and F5 to A4b, F3 to A5b, and F1, F6 and F7 to a new activation A8 on REFERENCE_FRAME and EVALUATION.
- Wave B starts before A7, because the design fixes the table format (CROSS_SYNTHESIS Part 1). At most four activations run at once.
- B1 (SPEC_METHOD build-tenant binding, F10, F11) and B3 (ODD and TRAVERSAL mappings, F18, F19) started.
- A4a returned `candidate_ready`, committed `b5af087`: ACTIVATION §1 gains Transitions and Configuration, and the Executive, Writer and Reviewer roles become one example configuration. Its reading is confirmed: the predecessor's Executive mutation restriction binds wherever that configuration is selected.
- A4b (measurement owner, acquisition rule, workspace as truth surface, refinement licensing, F2, F4, F5) started.
- A5a returned `candidate_ready`, committed `951ac81`. Ruling on its one unplaced determination: "superseded: the successor clause and what changed are named" is dropped. It was added in the tenant with no predecessor source, it is stricter than the common Successor Disposition Requirement, and RELEASE's restated UP-015 governs `superseded`.
- A5b (premise standing column, Foundation to law format and family index, F3, formal fragment, RA23 m8) started.

2026-10-13T19:54Z — Returns and dispositions:
- B3 returned `candidate_ready`, committed `57f4526`. ODD closure decisions, ODD audit outcomes and the TRAVERSAL refusals, partial effects and effect dispositions are split by cause, and each maps to one core value. The meanings from the 12 October cross-family review are kept, and tables F18 and F19 are in place. B2 started.
- B1 returned `candidate_ready`, committed `73a0a44`. SPEC_METHOD §11 states the build-tenant binding as method law (items 1 to 6). The old §11 (this source project's local development law) is owned by the common Product's Development Isolation, and the tenant design binds it. F10 and F11 are in place. Rulings:
  - ACTIVATION §4 owns the hard stops, and SPEC_METHOD §5 becomes a reference;
  - the F2 index row also accounts for SPEC_METHOD §8.

  B4 started.
- A4b returned `candidate_ready`, committed `e31a9d9`. ACTIVATION §2 step 3 is the only owner of size measurement, which applies wherever an envelope declares a context capacity. Also added:
  - the acquisition rule (port 5, adapted);
  - the workspace as truth surface;
  - refinement licensing;
  - hard stops stated in full;
  - tables F2, F4 and F5.

  A4b disclosed that it measured its inputs after reading rather than before, and that its spend is unavailable. RA4, a working review of ACTIVATION covering A1b, A4a and A4b, started.

Follow-ups held for later activations:
- SPEC_METHOD §5 hard-stop sentence becomes a reference to ACTIVATION §4;
- standards README: where each member's dispositions live, and the README route (D1);
- design: the core mapping of the tool-operation outcomes in CONSTRUCTION_BINDING §3;
- B8: AXIOMATIC_CALCULUS outcomes and whether a traversal binding may re-map `refusal(constraint)`;
- RELEASE `:605–609` and `:657` (B7);
- EVALUATION `:449` (A8);
- GLOSSARY rows for the new terms (A7/B10);
- plugin `stdo-work` routed to ACTIVATION §2 Acquisition (D2).

2026-10-13T20:11Z — Returns and dispositions:
- A5b returned `candidate_ready`, committed `a929514`. FOUNDATIONS §3 gains a standing table using the four §1 terms, P0 names its sources, and P4a gets a non-entailment case. Also added: Foundation to law (the format, the standing of consequences, and the 21-family index), the formal fragment carrying categorical items 1, 4 and 5 with H1 kept as a hypothesis, and F3. RA5, a working review of FOUNDATIONS, started.
- B2 returned `candidate_ready`, committed `9439c26`. EXECUTIVE_BASELINE becomes an operational profile and gains a §7 "executive configuration" and F16. Work results are mapped once. Rows 516 and 543 are `superseded`: the predecessor text pairs `incomplete` with `indeterminate`, and the replacement relation is item 3 of the common single result algebra requirement. Rows 560 and 565 stay `conserved`, as B2 read them.
- A8 (F1, F6, F7 and EVALUATION `:449`) started.
- B4 returned `candidate_ready`, committed `2f2338b`. PRODUCT_DEFINITION §5 reads its relation kinds in FOUNDATIONS §2 terms, and "execution binding" is renamed. TICKETS close classifications are mapped as dispositions. F12 and F13 are in place. B5 started.

More follow-ups held:
- `FOUNDATIONS.md:914` (the semantic import owner, now FOUNDATIONS §2);
- the F10 lead shortening the P4b and P5 standing (SPEC_METHOD);
- PROFILES §6 "bind the tier-1 roles" and the PROFILES §1 import rule (B6);
- `WORLD_MODEL.md:25` stale owners (B6);
- the GLOSSARY Semantic Import and Build Tenant rows (B10);
- README `:34`, `:61` (D1).

2026-10-13T20:15Z — Correction to the entry that records A1b's return. It says RA1's minor findings were repaired. A1b's return lists six as unchanged: 1b, 1c and 4b in FOUNDATIONS, and 2b, 6b and 6c in ACTIVATION. RA4 found the discrepancy. Those six are open and are now assigned: the ACTIVATION three to A4c, the FOUNDATIONS three to the repair after RA5.

RA4 returned for ACTIVATION at `e31a9d9`: questions 1 to 4 `satisfied` (transitions, configuration, measurement and attention, workspace, refinement licensing). Questions 5 to 9 are `falsified` on 14 minor findings, none material. Disposition: `local_repair` as A4c on ACTIVATION, covering RA4's findings 5a (ACTIVATION part), 5b, 5c, 6a, 7a, 8a, 8b and 9b to 9e. RA4 also notes again that A4b measured its inputs after reading them, against the Limits of the C3 contract; the handoff carries this as a known variance.
