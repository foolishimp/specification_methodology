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

2026-10-13T20:34Z — Returns and dispositions:
- RA5 returned for FOUNDATIONS at `a929514` (`fbfe915`) with five material findings:
  - the RF-010 triggers were dropped;
  - the independence cases for P1 to P3 vary only capacity;
  - P4b has no argument;
  - index rows point to tables that do not yet exist;
  - the import owner is inverted in §6.

  Disposition: `local_repair` as A5c, together with RA1's open 1b, 1c and 4b.
- B6 (UX, WORLD_MODEL, PROFILES, F20, F21) started.
- A4c returned `candidate_ready`, committed `a4542ef`. All RA4 findings and RA1's open ACTIVATION minors are repaired. A4c disclosed the same read-before-measure variance as A4b.
- B8 (IDENTITY, AXIOMATIC_CALCULUS, F8, F9) started. Ruling given to B8: a per-traversal stop-state binding may refine a TRAVERSAL value but never re-map `refusal(constraint)` away from `falsified`, and never raises standing.
- A8 returned `candidate_ready`, committed `59ae2a4`: F1 (36 rows), F6 and F7 are in place, and EVALUATION's FOUNDATIONS §1 citation is re-pointed to RELEASE §9. A8 disclosed a stray scratch file written outside the territory and deleted at once. B7 (ASSURANCE, RELEASE, F14, F15) started.
- B5 returned `candidate_ready`, committed `f3408e6`. Design axiom verdicts map for the predicate "the design meets the axiom, or the axiom does not apply": `not_applicable` maps to `satisfied`, needs a false applicability premise, and never counts as conformance. Design verdicts are acceptance results bound to ACTIVATION §3. Both readings are confirmed and flagged for cross-family attention in the handoff.
- C3, independent oracles for REFERENCE_FRAME, AXIOMATIC_CALCULUS and TRAVERSAL test tasks written from sources only, started.
- A5c returned `candidate_ready`, committed `681aae3`. Ruling on its open conjunction case: the declared decision rule states how non-mandatory results count. A non-mandatory `falsified` result is kept in the record, never discarded. A material counterexample to a mandatory constraint falsifies the conjunction whoever found it (predecessor RF-010). Otherwise the declared rule's value over the mandatory results stands. A5d applies this together with three small cross-file items.

2026-10-13T20:51Z — Returns and dispositions:
- B6 returned `candidate_ready`, committed `8830728`. UX §15 and WORLD_MODEL §14 map once, with "not admissible" split by cause. The unrun verification has no result. PROFILES §1 owns the profile import rule, and F20 and F21 are in place. The person's name is replaced in UX §15 and PROFILES §7. B9 (CONFORMANCE mapped to the 31 discriminators) started.
- B8 returned `candidate_ready`, committed `098e9db`. AC-007 maps value by value into FOUNDATIONS §4, which unifies RF-012 and AC-007. Operation stops are bound, and F8 and F9 are in place. Ruling on B8's question: a further refinement maps each child to its parent's core value; a different core value needs a different parent value at the owning member. B3b started.
- A5d returned `candidate_ready`, committed `3085798`: the conjunction ruling applied, F1 owners aligned, and the F16 label fixed.
- C1 (the verbatim frame generator, port 5, and the frames for the C3S-01 to C3S-03 tasks) started.
- B7 returned `candidate_ready`, committed `bafb3f9`. ASSURANCE and RELEASE refer to the result owners, RELEASE §9 owns the successor disposition values, and F14 and F15 are in place. Reading confirmed: each successor disposition is a claim that qualification evaluates in the core, under EXPECTATIONS ambiguity A3. Its row 402 supersedes A5a's row 402.
- C5 (independent oracles and three new tasks: configuration, build-tenant binding, stale summary) started.
- B3b returned `candidate_ready`, committed `2ba64b4`. TRAVERSAL refusal causes are bound to AC-007, and stop splits keep their parent's value. Ruling on its question: a basis mismatch inside a model or a qualifier record is AC-007's "mixed bases", `refusal(basis)`, which maps to `invalid_basis`. B1b (consistency repairs in AXIOMATIC_CALCULUS, TRAVERSAL, SPEC_METHOD and DESIGN_MODULE) started.

2026-10-13T20:52Z — C3 returned: independent oracles for the cases below, written before any frame or run, by an actor that read no candidate text. Each copied task is byte-identical to its source.

| Case | Tasks |
|---|---|
| C3S-01 | REFERENCE_FRAME, F-01 tasks A and B |
| C3S-02 | AXIOMATIC_CALCULUS, F-02 task A |
| C3S-03 | TRAVERSAL_OCCURRENCE, F-03 task F |

Source of two rulings the oracles cite: on 2026-10-12, Codex's cross-family review of the Claude candidate required that:
- TRAVERSAL `partial_effect` and `partial` map to `falsified` only on demonstrated non-attainment, and otherwise to `indeterminate`;
- a refusal for a falsified constraint, structural constraints included, maps to `falsified`, with `invalid_basis` only for an invalid-basis refusal or a co-emitted `invalid_basis` decision.

T-002-CLAUDE records both in its execution record (the entries for the Codex review and for W26, R25 and W28). B3 and B3b keep both.

C3 recorded four ambiguities: occ-25, the revision of Task B's E1, the meaning of coverage status, and Task A's acceptable values. They are carried to the assessment step.

2026-10-13T21:21Z — Returns and dispositions:
- B9 returned `candidate_ready`, committed `dd04639`. CONFORMANCE accounts for the 31 discriminators: 11 to cases and 20 to named logical-review checks. New case rows CD-01 (configuration), CD-02 (binding) and CD-03 (stale summary) are added. No case has a recorded pass.
- I1 (integration: frontier deltas, span, GLOSSARY, README, FOUNDATIONS index marks) started.
- B1b returned `candidate_ready`, committed `224081c`:
  - the stop-value parent rule is stated once in AXIOMATIC_CALCULUS §5;
  - a basis mismatch is mixed bases;
  - SPEC_METHOD's hard stops become a reference to ACTIVATION §4;
  - the stale P0 note is removed from DESIGN_MODULE.

  Ruling on its question: requirement status values (Active, Deferred, Superseded, Orphaned) are declared states, not results; assigned to the SPEC_METHOD repair after RBa.
- RBa (SPEC_METHOD, PRODUCT_DEFINITION, TICKETS) started.
- C1 returned `candidate_ready` and was regenerated by the Executive after B1b's commit. The 35 generator tests pass and `--check` exits 0. Committed `4ca18ba`: four frames of 57 to 85 KB.
- RBb (EXECUTIVE_BASELINE, DESIGN_MODULE) started.
- C5 returned (`0e6cef1`): oracles for C3S-04 to C3S-08, including three new tasks; no candidate text was read.
- C4 returned (`fbd5d37`): five more frames of 67 to 88 KB, and `--check` exits 0. Gap found: no member owns the "three accounts of a construction" that the common PRODUCT says apply across the build-tenant binding. Assigned to the SPEC_METHOD repair after RBa.
- RBc (ODD, TRAVERSAL, AXIOMATIC_CALCULUS, IDENTITY, CONFORMANCE) started.
- RBd returned (`f0456ed`): minor findings only; 22 changed determinations sampled, none lost. Disposition: `local_repair` as Rd.
- RBb returned (`a5a9a9f`). Its two material findings are F-1 (no field for an effect of unknown completion in the work-result record) and F-2 (F16 leaves rules untraced). It confirms that DESIGN_MODULE's `not_applicable` mapping is truthful and that rows 516 and 543 are `superseded`. RBb questions rows 522, 560 and 565, which change meaning but are recorded `conserved`. The earlier confirmation of 560 and 565 is withdrawn pending re-examination: each row whose meaning changed under the single result algebra requirement becomes `superseded` with the same replacement relation. Disposition: `local_repair` as Rb.

2026-10-13T21:36Z — Returns and dispositions:
- I1 returned `candidate_ready`, committed `4bb1f4e`:
  - 75 delta rows applied to the frontier copy, with conflicts resolved toward the later delta and recorded;
  - 0 locus failures across 660 `conserved` or `superseded` rows;
  - the re-proof span is 266 of 691 rows;
  - 46 GLOSSARY rows added;
  - the README routes are current, and the set-4 route and the person's name are removed;
  - six "table pending" marks are cleared.

  Accepted: I1's change to frontier rows 176, 179 and 180, which match the GLOSSARY move. Flagged for review: I1's extension of the GLOSSARY §2 locator rule.
- D12 (bootstrap frame, template entry point, plugin routes, a_c status note) started.
- RBa returned (`2d6b7bc`). §11 satisfies binding items 1 to 6, and nothing was lost from the old §11. Material findings M1 (TICKETS repricing dispositions unmapped) and M2 (PRODUCT_DEFINITION toolchain outcomes unmapped). Disposition: `local_repair` as Ra, which also carries:
  - requirement status values as declared states;
  - the three accounts of a construction, defined once in FOUNDATIONS §2 as an added choice owned by the Intent and applied in SPEC_METHOD §11;
  - the F11 standing lead.
- Rd returned `candidate_ready`, committed `fe24ae3`: RBd's minor findings repaired. Open for the handoff: the UX §4 compliance-test disagreement with the predecessor stays pending the product owner.
- C2 (the finite-oracle template, port 6, with an instance over FOUNDATIONS §4 conjunction) started.
- RBc returned (`c77aa5e`). Material M1: AC-007 let a basis condition outrank a demonstrated constraint violation, and F9 presented that precedence as derived. The predecessor AC-007 states no precedence. Ruling (option a): a refusal that names a demonstrated violation keeps `refusal(constraint)`, which maps to `falsified`. The basis condition is recorded with it as its own `invalid_basis` result. A refusal that names only basis conditions maps to `invalid_basis`. Reason: a known failure survives every join and a counterexample is never discarded (FOUNDATIONS §4; predecessor RF Result Conjunction). This is consistent with the 2026-10-12 meaning. The precedence is an added choice owned by AXIOMATIC_CALCULUS. Disposition: `local_repair` as Rc, with RBc's minor findings.

2026-10-13T21:52Z — Returns and dispositions:
- Rb returned `candidate_ready`, committed `59ed097`. EXECUTIVE_BASELINE carries an effect of unknown completion in the work-result record and requires it to be reconciled before work is reactivated, and F16 covers the whole member. Rows 516, 522, 543, 560 and 565 are each split into a `conserved` parent and a `superseded` child: the predecessor's mapping from core result to work-result variant is replaced under item 3 of the single result algebra requirement. This replaces the earlier `conserved` reading of 522, 560 and 565.
- D12 returned `candidate_ready`; non-frame files committed `9aa4491`:
  - the bootstrap frame (57,625 B) generated;
  - the template entry point set to `standards/frames/bootstrap.md`;
  - plugin routes current;
  - the a_c programs declared bound to the members' text from before the rebuild, with re-encoding open.

  Frames are held uncommitted until they are regenerated after the repairs. Row 802's declared deviation goes to I2.
- Ra returned `candidate_ready`, committed `fb25f2a`:
  - TICKETS repricing dispositions are declared recorded states, not results;
  - PRODUCT_DEFINITION toolchain outcomes are mapped through ACTIVATION §3;
  - the three accounts of a construction are defined in FOUNDATIONS §2 and applied as SPEC_METHOD §11 rule 7;
  - requirement statuses are declared states;
  - RBa's minor findings are repaired.
- I2 (second integration: Ra, Rb and D12 deltas; the general parent-value rule in FOUNDATIONS §4; GLOSSARY) started.
- Rc returned `candidate_ready`, committed `99f0e3a`. The ruling on demonstrated violations is applied in AC-007 and TRAVERSAL, and C3S-02 still expects `falsified`. RBc's minor findings are repaired. Residuals:
  - TRAVERSAL `:904–905` and `:946` still attach `refuse_missing` to a judgment-level refusal;
  - two basis reclassifications to `refusal(basis)` need cross-family confirmation.
- RX, a working consistency check across the whole candidate, started.

2026-10-13T22:35Z — Returns and dispositions:
- I2 returned `candidate_ready`, committed `b90315b`:
  - 40 frontier edits from Ra, Rb and D12, with the `superseded` child rows inserted after their parents and row 802's deviation accepted;
  - the general parent-value rule in FOUNDATIONS §4;
  - two GLOSSARY rows.

  The inflated SPAN.md was not committed; the span script keyed rows by line number.
- RX returned (`122d928`), a consistency check across the whole candidate:
  - RX-1 (bootstrap frame not committed) and RX-2 (frame copies differing from their owners) were blocking, and both are the frames deliberately held until regeneration;
  - RX-3 to RX-12 were minor. Of 2,716 links, 1 was broken; there was no second owner of the core values and no raised standing; 21 of 21 family tables were present.

  Disposition: I3 for the minor findings, then frame regeneration by the Executive.
- I3 returned `candidate_ready`, committed `24348b0`:
  - RX-3 to RX-12 repaired;
  - Rc's frontier rows applied;
  - TRAVERSAL judgment-level refusals take their cause from AC-007;
  - the span script keys rows by member and anchor, giving a re-proof span of 303 of 696 rows and 0 locus failures across 666 rows.
- Role change to Writer: frames regenerated at the final member text and committed with the bootstrap frame and manifest (`600dbfd`). `generate_frames.py --check` exits 0, and the 35 generator tests pass. Link check across the members: 2,658 relative links, with every problem inside `standards/frames/`. Frames are verbatim excerpts one directory deeper, and their copied relative links do not resolve there, because C1 did not port Codex's link rewriting (`relocate`). This is recorded as a residual. Role back to Executive.
- C6 (fresh-actor runs: 9 tasks, 2 repetitions each, Sonnet, 110,000-byte cap, spend stop at USD 15) started.

2026-10-13T22:46Z — Returns and dispositions:
- C2 returned `candidate_ready`, committed `967ab8b`. It is the finite-oracle template (port 6), with an exhaustive check of the FOUNDATIONS §4 conjunction rule: 516 cases and 1,404 joins, 24,531 assertions, and both wrong variants caught on 206 cases each. The C2 author wrote both the encoding and the check. RC12 is therefore asked to judge the encoding's fidelity.

  Ruling on C2's question: the pattern is ported with a few lines copied verbatim, and the design's port row 6 is corrected to say so (Executive as Writer, in the same commit).
- RC12, a working review of the generator, the frames and the finite oracle, started.
- C6 returned `candidate_ready`, committed `735262d`. Eighteen runs (nine tasks, two each) on `claude-sonnet-5-5`, all exited 0. Every measured context equals its dry run and is under the 110,000-byte cap. Spend was USD 3.2215 at list price. No oracle text reached any actor.

  On C6's note: the frames and their SHA-256 values were committed in `standards/frames/FRAME_INPUTS.json` at `600dbfd`, which precedes every run. That commit is the pre-run record of the frame digests that C3S-01 to C3S-03 require.

  Variance: C3S-04 to C3S-08 CASE.md files name the F-02 card, and C6 used the generic `C3S-CARD.md` as briefed.
- AS1 (C3S-01 to C3S-04) and AS2 (C3S-05 to C3S-08), assessment by actors that wrote neither frames, oracles nor outputs, started.

2026-10-13T23:08Z — Returns and close of this run:
- RC12 returned (`6eea724`).
  - The generator and frames hold: 35 tests pass, and all 146 `Source:` digests and section digests match.
  - Material RC12-3: the finite check constrains only that a gap or a not-performed result is never `satisfied`, and two FOUNDATIONS §4 clauses are not encoded. Its README overclaims.
  - Minor: RC12-1, RC12-2 and RC12-4 to RC12-9. The ruling RC12-8 calls unrecorded is in the C2 entry above.

  Disposition: recorded open, not repaired in this run. The product owner has asked whether the candidate should carry code at all.
- AS2 returned (`0c69364`): C3S-05 to C3S-08. 4 of 8 runs are `satisfied`, all 8 reached their required core results, and no failure traces to method text or frames. Minor method findings M1 to M3.
- AS1 returned: C3S-01 to C3S-04. All 10 runs are `falsified` under strict grading. The required core result was reached in four of five tasks; C3S-03 was not (occ-24). Method-text findings MT-1 to MT-6, with MT-1 a conservation defect in REFERENCE_FRAME §10. Disposition: recorded open for the next round.
- Handoff written: [HANDOFF.md](HANDOFF.md). This run stops here, at the product owner's review. No member is accepted, no merge is requested, and the pen has transcribed nothing yet.

2026-10-14T00:41Z — Cross-family review received. Codex reviewed this candidate at `768cf8c`: `.ai-workspace/comments/codex/20261014T000519Z_REVIEW_CLAUDE_V3_REVISION_2_PURPOSE_AND_IMPLEMENTATION.md`, SHA-256 `758baef0ed7c14fc9afae3695fba1f39765c05c7cf88e1fde09383f0d8012fe8`, relayed by the product owner. Its verdict: retain the core architecture and require changes before acceptance. Each finding was checked against the source. Executive dispositions:

- **F1 (High), accepted:** REFERENCE_FRAME §10 lets an unchanged frame declaration stand as a reason to reopen no result. It is the same clause as AS1 MT-1 and was inherited from the base. Disposition `local_repair`, separating the two questions:
  - whether the frame definition needs a new coordinate;
  - whether affected results stay valid, which the reuse rule in ACTIVATION §7 owns.

  Harmless explanatory metadata preserves reuse. Changed admissible evidence or a wrong-family activation reopens the affected claims, and demonstrably independent work is kept.
- **F2 (High), accepted:** introduced by B3 in this rebuild. The split `partial_effect(ended)` → `falsified` and `partial_effect(unknown)` → `indeterminate` lets an unknown termination mask an established failure of the intended outcome. Codex's closed-interval counterexample is decisive. Disposition `local_repair` in TRAVERSAL, keeping ACTIVATION §3 Effects consistent:
  - established non-attainment of the declared predicate → `falsified`, with the effect's completion recorded separately as `completion_unknown` and its residual kept;
  - an undecidable outcome → `indeterminate`.

  Blind retry stays prohibited in both cases. This also decides the occ-24 oracle conflict in favour of C3S-03's `falsified`, wherever the fixture's facts establish non-attainment.
- **F3 (High, completion gap), accepted:** no a_c interpretation is current. This was already stated in the handoff. The common specification has since added a Constraint Surfaces And Logic Compression requirement (the iteration 3 inputs on `main`), which makes a current interpretation required work, not optional.
- **F4 (Medium), accepted:** the finite check does not reject an invented reported value. It is the same finding as RC12-3. Disposition `local_repair`: specify the permissible reported values independently, add mutations that change only the reported value, and state the limited domain.
- **F5 (Low), accepted:** the frames' copied relative links break. Disposition `local_repair`: the generator rebases relative links for the frames directory, and source identities and section digests stay over the owner bytes.

Codex also notes that the common specification's new Foundational Reduction requirement is not retroactive to this rebuild's `a7eba66` basis, and that a Claude iteration 3 needs an explicitly bound task. No repair has started. The product owner is asked whether to repair F1, F2, F4 and F5 now on this branch, and whether the Claude line starts iteration 3.
