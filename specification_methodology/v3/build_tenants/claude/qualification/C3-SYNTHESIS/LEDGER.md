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

2026-10-14T00:50Z — Owner instruction, recorded verbatim. To the question "Codex's five findings check out against the source. How should the Claude line proceed?", the product owner answered: "Repair now, then iteration 3 (Recommended)". That option read: "Fix F1, F2, F4 and F5 on the tenant branch now … Then start iteration 3 under the new Reduction and Constraint Surfaces requirements, using the fixed rules as its base."

This admits:
- revision 2b, repairing F1, F2, F4 and F5 on this branch against the `a7eba66` basis;
- then a Claude-line iteration 3, bound to the current common specification on `main`.

Started in parallel:
- RF1: REFERENCE_FRAME §10 (F1).
- TR2: TRAVERSAL partial effects, with ACTIVATION §3 Effects consistency (F2).
- TL: finite-check reported values (F4) and frame link rebasing (F5).

2026-10-14T01:07Z — Revision 2b returns:
- RF1, committed `3940e7a`. In REFERENCE_FRAME §10, the question whether a frame needs a new revision coordinate is now separate from whether a result stays valid, which ACTIVATION §7 owns. The tenant-added sentence "reopens no result" is removed here and at `:170`. The predecessor's nine revision actions are kept.
- TR2, committed `85a96d8`. `partial_effect`, and decision `partial`, now split into `(not_attained)` → `falsified` and `(undecided)` → `indeterminate`. Whether the effect has ended is a separate residual. ACTIVATION §3 Effects requires `completed` to establish the end, and reconciliation before retry also covers `not_effected` whose end is not established.
- I4, committed `de7c617`: GLOSSARY, EXECUTIVE_BASELINE, SPEC_METHOD and frontier rows 547 and 641 aligned; "uncertain completion" now covers both values.
- TL, committed `719449f`:
  - the finite check gains reported-value properties P6 to P8, and four value-only mutations are each detected;
  - the domain is stated, and the two §4 clauses it does not encode are explicitly excluded;
  - the generator rebases frame links, and 42 tests pass.
- Role change to Writer: frames regenerated and design row 5 updated (`716e20c`). `--check` exits 0, and all 2,672 relative links across the members and frames resolve; 526 were broken before.
- RV2b (working review of RF1, TR2 and I4) and R0i3 (independent expectations for iteration 3) are running. Next: rerun C3S-01 task B and C3S-03 on the regenerated frames, then iteration 3.

2026-10-14T01:17Z — Iteration 3 on hold. The product owner asked: "how can you do I3 without i3.specificaiton completeing which codex is holding the pen on?".

The objection is correct. The common iteration 3 specification is still being written by the common pen: `main` moved from `1317e43` to `6c2debb` within the hour, and the main checkout holds uncommitted edits to common files. Binding iteration 3 to a moving, unsigned snapshot would have produced work and an oracle that both need redoing.

Executive disposition:
- I3-1 is stopped before writing anything.
- Claude-line iteration 3 construction waits until the common pen freezes the iteration 3 specification and the product owner signs it off.
- The inward merge of `6c2debb` (`6368875`) stays, because it only brings common text in under Development Isolation.
- `qualification/C3-ITER3/EXPECTATIONS.md` is provisional, bound to the unfrozen `6c2debb`. It will be re-derived against the signed-off commit.
- Revision 2b continues, since its repairs depend only on the `a7eba66` basis: RV2b, then the reruns of C3S-01 task B and C3S-03.

2026-10-14T01:50Z — Revision 2b closed for this round:
- RV2b found F1 and F2 closed. Its Medium RV2b-1 and Low RV2b-2 to RV2b-7 were repaired by R2c (`9ff93c8`), and the frames regenerated (`48a0683`; `--check` exits 0; 2,680 links resolve).
- C6b reran C3S-01 task B and C3S-03 twice each on the revision 2b frames, for USD 0.84 (`cd9ec5e`).
- AS3 graded the reruns:
  - occ-24 is now `partial_effect(not_attained)` → `falsified` in both reruns, against `indeterminate` in r1 and r2.
  - Both task B reruns reopen the out-of-family result and the rows that depend on it.
  - Task B r4 has no failed required item; r3 still keeps one result closed (B21).
  - The C3S-03 reruns fail only on recording occ-23's predicate.
  - Remaining method findings MT-2 (narrowed), MT-7 and MT-8 are minor and held for the next round.
- The Codex findings F1, F2, F4 and F5 are repaired on this branch, pending cross-family confirmation. F3, the a_c interpretation, waits for iteration 3.

2026-10-14T14:42Z — Owner decisions, recorded verbatim:
- To "Do you sign off the iteration 3 specification at round 2 (55bbf9e), or wait for Codex's round 3 repairs?", the product owner answered "Wait for round 3 (Recommended)".
- To "Which line should start iteration 3?", the product owner answered "Claude line".

Effect: the Claude line's iteration 3 is admitted by the product owner. It starts only after:
1. the common pen repairs the round 2 findings and freezes round 3;
2. Claude reviews round 3;
3. the product owner signs off the specification at a named commit.

Iteration 3 then binds to that signed-off commit, merged inward. The provisional expectations in `qualification/C3-ITER3/EXPECTATIONS.md` are re-derived against that commit before any construction. Until then no Claude construction runs. The common pen is asked to record this owner decision in T-002-CLAUDE.

## Iteration 3

2026-10-14T16:01Z — Owner instruction, recorded verbatim. To "Do you want me to start Claude's iteration-3 build now?", the product owner answered ">.< yes".

The answer is read as the product owner confirming `EC-CLAUDE-I3-01` (admitted by the common pen at `651581c`; SHA-256 `3c928885b7c185d467ad3764289ae796b259c0982d71f8ee46be6b944860b859`) and starting it now. Effects:
- It settles round 3 findings RT2-01 and RT2-02 for this line, by owner action.
- His sign-off on the common specification is still open, so the open decisions in the round 3 review are carried as known gaps:
  - the changes to accepted conditions;
  - the pillar list;
  - the 51 Codex-line replacement relations.
- Nothing is assumed accepted.

Role change to Writer, for the contract's Git step:
- The 24 member hashes of input `C3-I3-R2-01` were checked at B `355aa86`: 24 match, 0 mismatch.
- The tenant tree drifted from the contract's preimage `5ab44d5` (`b75d6aa6…`) by one ledger entry (`81032c4`). It is not material, and it is reported as the contract requires.
- The recording commit `651581c` was merged inward (`22991db`). The tenant tree is unchanged by the merge (`1101bdb1…`), and `specification/` equals B.

Role back to Executive.

Oracle for this iteration: `qualification/C3-ITER3/ORACLE.md`. It is a byte copy of the independent oracle written from the `355aa86` specification for the review of the Codex iteration 3 candidate, by an actor that opened neither candidate. It holds 98 expectations, 12 negative expectations and 12 recorded ambiguities. It supersedes the provisional `EXPECTATIONS.md`, which was derived from the unfinished `6c2debb` and is kept as history.

Resources: no numeric cap is imposed by the owner. Under the contract, paid actor trials on this line bind a recorded allowance. Executive default: USD 15 for iteration 3 trials, balance USD 15.00, which the owner may change.

Next: I3-1, design re-entry and a verified reduction inventory and plan. It also establishes the current disposition of Codex's F1–F5 from source and evidence, as the contract requires.

2026-10-14T16:39Z — I3-1 returned `candidate_ready`, committed `1214524`:
- design REDUCTION.md: 26 clusters, about 100 rival or duplicate loci, with 20 of them checked at source;
- design INTERPRETATION.md: the a_c interpretation plan;
- the current state of F1–F5;
- 10 pillars, of which 5 are decided and 5 partial, and none yet bound in the family tables;
- deciding paths DP-01 to DP-40, with 8 measures and a pass/fail guard, fixed before any measurement;
- PLAN.md: about 55 activations in seven steps, with trials of USD 9.51 planned and a USD 3.00 reserve within the USD 15 allowance.

Corrections and variances:
- **F4 check now refuses.** The finite check binds a common requirement section that changed with the `651581c` merge. The earlier ledger entry that `--check` exits 0 was true at `719449f` and is stale now. It is re-bound in step 2.
- **Concurrency limit exceeded.** I3-1's helpers ran about 12 read-only contexts at once, over the limit of four. They were read-only, but this is a breach of the configuration, recorded here.
- **A Codex file was listed.** An incidental grep listed three lines of a Codex file, which was not opened.

Points for the product owner (PLAN §7):
- selecting the mechanical a_c evaluation;
- the MT-9, MT-2, B21, UX and occ-24 rulings;
- the replacement relations;
- cross-family evidence and assignment;
- sign-off.

Each point blocks only the work that depends on it.

Step 1 starts: I3-2a (FOUNDATIONS, ACTIVATION), I3-2b (EVALUATION, REFERENCE_FRAME, AXIOMATIC_CALCULUS, IDENTITY), I3-2c (SPEC_METHOD, TICKETS, RELEASE, ASSURANCE, PRODUCT_DEFINITION) and I3-2e (design records), with disjoint territories.

2026-10-14T17:23Z — Owner decisions, recorded verbatim:
- To "May the Claude line run the pinned Axiom Indexer (v2.5.1-rc.2, the a_c checker) on its frozen iteration-3 a_c program? …", the product owner answered "Yes, select it (Recommended)". The mechanical evaluation is selected under A_C_DEPENDENCY: verify the installed checker against its pinned digests, validate the program, and project the frame indexes. The result is structural validation only.
- To "Paid fresh-actor trials for this iteration: is my default allowance of USD 15 right? …", the product owner answered "No paid trials". The allowance is USD 0. Step 6's paid trials are dropped. The deciding-path comparisons are done as desk traces by non-author reviewers. Criterion 4 (actual use) stays unevidenced in this iteration and is reported as such.

Step 1 returned, committed as one commit (I3-2a, I3-2b, I3-2c, I3-2e):
- the shared owners are settled, and the rivals refer or refine with maps;
- the Pillar column is added (F2 to F5 filled; the rest pending);
- EVALUATION §5 owns when a finding blocks promotion;
- AXIOMATIC_CALCULUS §9 states constraint surfaces;
- F2's recurrence at PRODUCT_DEFINITION is confirmed and repaired;
- the inventory gains R30 to R34 and DP-41 to DP-46, both added before any measurement;
- delta rows re-read: 28, 20 and 21. No meaning changes, so no supersessions are proposed.

Variance: all four activations exceeded the 300,000-byte default, at an estimated 307 to 420 KB acquired, not instrumented. Recorded against the CONSTRUCTION_BINDING limits.

Open items routed to step 2: WRITING_GUIDE and POSTING_GUIDE, the pillar 2 owner (IDENTITY proposed), DP-41 to DP-46 tracing, and the pillar column for F1 and F6 to F21.

2026-10-14T17:46Z — Paused for token budget at the product owner's request ("how can i reduce token usage, i am almost out of tokens"). I3-3a was committed. I3-2r, I3-3g and I3-3d were stopped mid-work before writing any file; the worktree was clean, so nothing was stashed. Step 2 stopped with I3-3a, I3-3b and I3-3c committed. Remaining: I3-2r (WC-1 repairs), I3-3d, I3-3f to I3-3k, I3-3e, then steps 3 to 7. The resume plan uses one activation at a time, scoped narrowly, with working checks combined.

2026-10-14T17:56Z — Resumed on the product owner's instruction to finish iteration 3 sequentially, with no parallel agents and at most one sonnet subagent at a time. I3-2r returned `candidate_ready` (`ea564f0`, `b35a796`): WC1-01 to -09, -11, -15, -16 and the R12 instances repaired; FOUNDATIONS §3 index F16 = 1–9, F17 = 1, 2, 3, 4, 5, 6, 7, 9, F18 = 1–9. Row 517 (`incomplete` pairing) becomes a proposed `superseded`, pending the product owner. WC1-12 goes to I3-3f; WC1-10, -13, -14 to I3-3j.

Execution decisions for the rest of the iteration:
- **Non-author rules.** The main session wrote all member text, so it cannot meet the exit proofs that need a non-author actor (I3-4a, I3-4b, the desk traces, I3-7v, I3-7w). Those run in a sonnet subagent with exact file and line scope, one at a time: (A) after I3-3e, the combined step-2 working check, which also covers I3-2r's diff, with the I3-4a and I3-4b re-assessment; (B) after the freeze, the combined final review against ORACLE with the desk-traced path comparisons. Everything else is author work and is labelled same-author working evidence.
- **Delta keys.** Deltas key rows by frontier line number. Integration applies them by the rc.2 anchor column, and a script checks that each delta row matches exactly one frontier row.
- **Step 4 scope.** The PLAN's smallest coherent return: fragments G1 to G4 (shared owners) with refinement maps, declared as partial coverage in `a_c/i3/README.md` and the handoff. The checker tag `axiom_indexer/v2.5.1-rc.2` resolves to tag `9bff233c…`, commit `9a9c4797…`, subtree `6dae168d…`, as INTERPRETATION §5 requires.

2026-10-14T18:38Z — Step 2 returned, with I3-4c and I3-5s. Commits `9ac4601` (I3-3g), `68f888e` (I3-3d), `510e338` (I3-3f), `616b885` (I3-3h), `e9e2d2a` (I3-3j), `cc6c24c` (I3-3k), `eca2760` (I3-3i), `2a2af3a` (I3-3e), `d906b37` (I3-4c), `d267233` (I3-5s), `bb0dd66` (WC-2), `1908f25` (I3-3r).
- Every family table now argues "By … so …" with a Pillar column; the FOUNDATIONS §3 index has every Pillar cell. Pillar 2's generic law is IDENTITY §2 Boundaries and sufficiency claims, which WORLD_MODEL refines. CONFORMANCE maps the 52 discriminators and 3 closure checks. The finite check passes `--check`.
- Integration 1 rebound the frontier to `355aa86` (script: all 707 keyed rows present once, 8 tenant child rows) and applied the deltas from a read-only sonnet extraction.
- Every `superseded` cell, in the frontier and in the members' disposition tables, now reads "proposed and pending the product owner's acceptance". New proposals this iteration: three EXECUTIVE_BASELINE child rows (I3-3a), DESIGN_MODULE `#15-adoption-guidance` (I3-3b), UX `#1a` and `#13` (I3-3d), WRITING_GUIDE `#current-surface-writing` (I3-3f); the ACTIVATION `incomplete` pairing re-marked (WC1-16).
- WC-2, a non-author sonnet working check of step 2 with the I3-4a and I3-4b row re-assessment, returned `local_repair`: 1 High, 3 Medium, 8 Low; table check 71 of 204 rows, 62 real, 9 weak, 0 hollow. I3-3r repaired all twelve by restoring predecessor meaning.
- Variances: WC-2 read about 365 KB, over its 350 KB guide; of about 75 rows it verified about 30 against both texts and judged the rest from the deltas, so I3-4a and I3-4b are partly evidenced. That gap is carried to the handoff, not filled by the author. A second subagent was used only for the read-only extraction; agents ran one at a time.
- Step 4 is narrowed by variance, for the owner's token limit: the i3 interpretation encodes only the shared-owner determinations of the result algebra and conjunction, authority kinds, reuse and invalidation, the promotion block, the step-result refinements, boundaries (pillar 2) and constraint surfaces (pillar 10). Every other heading section of G1 to G4 is disposed `not-encoded-i3`, which is uncovered and blocks C3 closure for interpretation coverage (conformance discriminator 14). Frame indexes are made only for tasks whose deciding owners are encoded.

2026-10-14T18:39Z — Step 3 returned (I3-4c at `d906b37`, I3-4d). Source-settlement commit: `3ab7ef9`. Every member file is settled at it; step 4 encodes from it, and member text changes after it only through step 7.

2026-10-14T18:45Z — Step 4 returned and the candidate is frozen (I3-6). Commits `d267233` (I3-5s), `79a9db0` (I3-5e, I3-5m, I3-5k), `416bdb5` (I3-5v).
- Interpretation `a_c/i3/`: 64 clauses quoted verbatim from the settled members, 4 frame indexes, no residuals; G1 to G4 dispositions 15 `encoded`, 8 `no determination`, 181 `not-encoded-i3`; G5 to G13 not encoded. Partial coverage blocks C3 closure for interpretation coverage.
- Checker, as the product owner selected: the pinned Axiom Indexer `v2.5.1-rc.2` was verified against its tag, commit, tree, subtree, all seven member SHA-256 values and the aggregate `55a2061b…`; `validate` `valid` with 0 diagnostics; 4 indexes projected in both modes; a second run was byte-identical. Structural validation only.
- Frames: 12, including the new `acceptance-release` and `member-build-assess`; `generate_frames.py --check` exits 0.
- Variance: `standards/README.md`'s paragraph on the `a_c` sets was corrected after the source-settlement commit `3ab7ef9`, to name `i3/` current as INTERPRETATION §7 requires. README is not encoded, so no clause is stale.

**Freeze.** Subject S2 for every assessment is commit `416bdb5` on `tenant/claude/c3-synthesis`. Digests (SHA-256 of the sorted `shasum -a 256` lines of each tree's files):
- 23 members `standards/*.md`: `e755bdbdc659e4094a2f9b98c4dc85c93ffa361d1c7cf3eb5ab6620aa5f644ce`
- all of `standards/`: `14a6bbddef635937653300fea3cefe6b38c44682700b13242f08eaade27a5763`
- `standards/frames/`: `c50eea10e8118f4080e3790d0e2dfbec0b6daa1443d498e566c14093bb65cbcb`
- `a_c/i3/`: `528cdf1da297369cd6a7039772d1606922d0d9b71db235d4cefa4cc822ea68cd`
- `qualification/instruments/`: `7c2b3f752ffa5b54706ac105fc27d921c827eae51be15a1cdfdb3b91d41823b5`
- `plugins/`: `5e73f8e3b36c85bbd5ced9e19f0630e9f4f7761fa6b4a1fb669398a1c1f14d7f`
- `frontier/PREDECESSOR_CLAIMS.md`: `e490204a175667b38eb57c542dba78329ec891856cd9219adbaaa02b0114db0d`

Next: step 6 as one combined final working review against ORACLE by a non-author sonnet subagent, with the desk-traced deciding-path comparisons and the interpretation fidelity cases written before the model is opened. No paid trials (owner decision); criterion 4 stays unevidenced.

2026-10-14T18:46Z — Step 6 started: one non-author sonnet working reviewer on S2 `416bdb5` does the combined final review against ORACLE, writes 8 interpretation fidelity cases from the prose before opening the model and then judges them, and desk-traces deciding paths. Variance, declared before any trace exists: for the owner's token limit only a systematic sample is traced, every sixth path, DP-01, DP-07, DP-13, DP-19, DP-25, DP-31, DP-37 and DP-43, from route entry on S0, S1 and S2. The other 38 paths are not traced and are reported as such. Frame-entry traces are not run. No paid fresh-actor runs (owner decision).

2026-10-14T19:08Z — Steps 6 and 7 returned; candidate re-frozen (I3-8f) at `2beed8d`; iteration 3 closed for this session with a handoff.
- FINAL (non-author sonnet, on `416bdb5`): `local_repair`, 0 High, 4 Medium, 7 Low; fidelity 3 faithful, 3 defects, 2 not encoded; desk trace of DP-43 only (reviewer over budget at about 510 KB), against S0 "not established", against S1 "simpler" on condition of the modal-force convention.
- I3-8r repaired FR-01, FR-03 to FR-06 and FR-08 to FR-11. It added one proposed supersession, `#proportional-disposition-returning-party`. FR-02 and FR-07, the indicative-for-"must" convention, go to the product owner. The finite result file, stale since I3-3e on its whole-file FOUNDATIONS digest, was regenerated. The checker re-ran `valid` on two byte-identical runs.
- Re-freeze digests at `2beed8d`: members `7e8349f9…83ec`, standards `4f5c5c1d…1910`, frames `3b5913a2…275a`, `a_c/i3` `b316f78f…7762`, instruments `e79af6ec…7bd6`, plugins `5e73f8e3…4d7f`, frontier `c8cd19a0…17f6`.
- Handoff: `qualification/C3-ITER3/HANDOFF.md`. Criterion 4 unevidenced; 45 of 46 deciding paths untraced; I3-4a and I3-4b partly evidenced; interpretation partial; the step 7 repairs unreviewed. A cross-family review is still needed. No merge, no push, no acceptance claim.

## Iteration 4

2026-10-15T11:05Z — Owner instruction, recorded verbatim: "ive approved i4, this means that the build tenants may proceed". Read as the product owner's ratification of the I4 common specification at its latest freeze, C3-I4-03 at `3c4c503` (the only I4 freeze with a satisfied readback and no open finding; my readback of it is at `8bd17af` on `main`), and as the start of this line's iteration 4. The common pen's records of the exact-commit ratification (T-001) and of this line's admission (T-002-CLAUDE) were pending when this entry was written; this line binds the owner's words and the exact commit, and will merge the pen's records inward when they land.

Role change to Writer, for the Git step:
- `main` at `8bd17af` merged inward at `7c60f32`; `specification/`, `AGENTS.md`, `CLAUDE.md`, `build_tenants/README.md` and `stdo_3.json` are byte-identical to `3c4c503`.
- The C3-I4-03 snapshot: 25 of 25 members reproduce from `3c4c503`; at the merged tree 23 match and the two tickets differ only by the recording `a960032`, which the snapshot excludes from its members.
- `PREDECESSOR_CLAIMS.md` is unchanged since `355aa86`; the frontier inventory stands.

Role back to Executive.

- Plan: `qualification/C3-ITER4/PLAN.md`. Work list: T-002 "Iteration 4 staging", Claude column, I4-01 to I4-09, in the order I4-01, I4-08, I4-03, I4-04, I4-02, I4-06, I4-07, I4-05, I4-09.
- Donor: the Codex candidate at `fb855df`, package `d490dd6`; read only through `git show`.
- Actor facts for this session: Claude family; author of the candidate; not fresh (full I3 context). Same-family nonauthor reviewers will be Sonnet subagents with exact scope, one at a time (D8).
- Open owner decisions carried: D5 (criterion 4 stays `unresolved` until decided); the proposed replacement relations; the UX replacement; identity and packaging.

2026-10-15T11:19Z — I4-01 returned `candidate_ready`: `qualification/C3-ITER4/REBIND.md` accounts for 24 changed common decisions between `355aa86` and `3c4c503`, each with its effect and task or a no-change reason. Rebound in this commit: the frontier header (input, status, ticket rule), CONSTRUCTION_BINDING §2 (I4 binding; §1's port-review sentence superseded by Cross-Synthesis), design README (I4 pointer). Codex's bounded Stage 1 reading of `2beed8d` reported no implementation defect; its note on stale "state found" counts in REDUCTION.md goes to I4-08.

2026-10-15T11:58Z — I4-08 and I4-03 returned `candidate_ready` (`e45edca`). Rebind text repairs: ACTIVATION §2 step 3 carries the ratified fit rule (`indeterminate` without a measurement or supported bound; a correct result does not satisfy fit); CROSS_SYNTHESIS names the I4 donor and the ratified port-review allocation, its I3 default historical; REDUCTION §2 labels the "state found" as the state at I3-1 and binds the unchanged pillar list. Ports (`qualification/C3-ITER4/ports.md`): C1 and C6 excluded with reasons; C2 selected, realised only under D5 option A; C3 adapted as `frontier/REVIEW.json` (645 rows; 611 conserved, 15 superseded proposed, 19 not applicable; 126 rows flagged `modal_conversion`; every `semantic_review.result` `indeterminate` until a nonauthor assessment is recorded; 12 predecessor anchors unresolved: 10 tenant child rows and 2 UX slug mismatches); C4 adapted as `a_c/i3/consumers.json` (64 clauses, 1,329 link-derived consumer bindings, support `cites`, semantics unresolved); C5 adapted as `tools/ac_controls.py` (identity positive and adverse hold; `validate` rejects a duplicated clause and a dangling source; a dropped clause changes the projection; the positive reproduction fails because the frozen `a_c/i3` artifacts are stale against the ACTIVATION edit, exactly as the checker should report; regenerated at the freeze). The six I3 ports go to the I4-09 readback. Posted to the pen on `main` at `708dfb9`: the proposed replacement relations by question (Q1 to Q8).
- Variance: the I4-04 reading batches (`reassess/batch-01..08.md`, 140 rows, 680 KB) are committed as the reviewer's exact subject. 9 delta-judged titles of WC-2 could not be matched to frontier rows and stay as WC-2 left them.

2026-10-15T12:20Z — I4-06 (frames) returned `candidate_ready`. The generator gained a `rows: frame-anchors` route mode that copies, from a family table, only the rows that cite a section the frame carries (TO1), recorded per route as `rows={selected,total,excerpt_sha256}`; 33 family-table routes added across the 12 frames by a script that kept only tables with at least one matching row; `--check` exits 0; `links.py` reports only its two known false positives (`X_v`, the common conformance anchor) and their frame copies. Declared capacity raised from 100,000 to 150,000 bytes; total frame bytes 956,476 to 1,201,993, largest `configuration` 147,702; per-frame M4a increases recorded in REDUCTION §4.3 (TO1 realised, acceptance `unresolved` until frame-entry traces exist). F5 residual closed: `kind` is `verbatim_reference_frames_rebased_links`; `a_c/README.md` says verbatim with rebased links. Criterion 4 remains `unresolved` (D5 open). I4-07: REDUCTION §4.1 subjects rebound (S1 is `2beed8d`), §4.2 states the ratified standing of verdicts (`satisfied`, `indeterminate`, `falsified`, `unresolved`); DESK-TRACES §0 restates DP-43 as `indeterminate` against both baselines and the 45 untraced paths as `unresolved`.

2026-10-15T13:05Z — I4-04, batch 01 returned (`reassess/batch-01.json`; one Sonnet same-family nonauthor in a fresh context; 16 rows of AXIOMATIC_CALCULUS and DESIGN_MODULE_METHOD; 210,153 subagent tokens, 17 minutes): 14 `conserved`, 0 `changed`, 2 `indeterminate`, modal force preserved on 15. Merged into `frontier/REVIEW_ASSESSMENTS.json` and `REVIEW.json` (assessed 14). Repairs of the two indeterminate rows, in this commit: DESIGN_MODULE §4 Functional bias now says that both lists bind as an obligation of the profile (the predecessor's "must prefer" and "must avoid"); DESIGN_MODULE §11 Post-ticket design review maps the predecessor's 4B and 5E invalidators onto ACTIVATION §7's three and says no fourth exists. Both rows stay `indeterminate` in the record until read back on the successor.
- Budget note for the product owner: one batch of 16 rows cost about 210,000 Sonnet tokens. Batches 02 to 08 (124 rows) would cost about 1.5 million at the same rate. Under D8 and the owner's token constraint, the readbacks R2b (ports) and R2a (repairs) run first, because the ratified text requires them for every port and every repair; batches 02 to 08 and R1 run only if budget remains, and otherwise stay `indeterminate` with their exact scope stated in the handoff.

2026-10-15T13:40Z — Owner instructions, recorded verbatim, in order: "i dont want sonnet - opus 5.5 high/xhigh are superior"; "V3 implementation is sufficiently constrained that you can run the whole thing through Fable, i had a free reset, so we can go max"; "since this the basic constitutional document behind everything - we shouldnt hold back"; "the only issue with fable max is it becomeing trapped in rabbit hole iterations"; "creating churn". Read as: the token constraint of D8 is lifted for this iteration; every further reading runs on Fable at max effort in a fresh context (never a fork, which would inherit the author's context); D5 option A is funded as one isolated Fable actor per frame with no external spend, which this line records as its reading of the instruction pending the owner's correction; one subagent at a time stands; and each review gets one triage and one repair round, with one successor readback, no more. Readings already made are not re-run: batch 01 (Sonnet) and R2b (Sonnet) stand as working evidence, R2a ran on Opus 5.5 high.

2026-10-15T13:45Z — R2b (ports; `reviews/R2b.json`; 211,793 Sonnet tokens, 41 minutes) and R2a (repairs and I4 edits; `reviews/R2a.json`; 115,868 Opus tokens, 5 minutes) returned and were triaged once (`reviews/TRIAGE-R2.md`). R2b: 13 findings (1 High, 5 Medium, 7 Low); 10 repaired, 2 declined with reasons, 1 explained and scheduled for the freeze. R2a: FR-01, FR-03, FR-05 repaired; FR-06, FR-08, FR-11 partly; 8 findings (3 Medium, 5 Low), 7 repaired, 1 declined (the §5 purpose sentence exists). Material repairs: the import rule has one owner (REFERENCE_FRAME §1 no longer restates FOUNDATIONS §2); `block-outside-claim` is a prohibition again with its condition; the frames' preface makes no sufficiency claim; the new ACTIVATION, EVALUATION and RELEASE sentences cite their principles and are marked as law carried from the common contract; the identity control reads the common dependency contract and refuses a tampered member. Program rebuilt (64 clauses, `assemble --check` 0, `test_assemble.py` OK); generator tests 45 OK; frames `--check` 0; loci 754 resolve; links show only the two known false positives.

2026-10-15T14:20Z — R1 (family tables of EXECUTIVE_BASELINE, DESIGN_MODULE and ODD; `reviews/R1.json`; Fable max, fresh context; 136,262 tokens, 12 minutes) returned and was triaged once (`reviews/TRIAGE-R1.md`): 70 rows, 11 flagged, 14 findings (1 Medium, 13 Low), all repaired in the tables: premise citations completed (P3 for uniqueness, P4b for non-re-acquirability, P5 for failing closed, P2 for a projection duty), the derived commitments written with their bases in seven DESIGN_MODULE rows, F15 and F13 imported by EXECUTIVE_BASELINE and F18 by DESIGN_MODULE, one policy moved from a P2 consequence to the choice column, and per-clause attributions written for 18 ODD rows. The rule links of the 70 rows stay `unresolved`. Frames regenerated, `--check` 0; loci 754 resolve; links show the two known false positives. I4-04 batch 02 (DESIGN_MODULE_METHOD, 17 rows) is running on Fable at max.

2026-10-15T14:35Z — I4-04 batch 02 (DESIGN_MODULE_METHOD, 17 rows; Fable max, fresh context; 105,648 tokens, 8 minutes): 17 `conserved`, 0 `changed`, 0 `indeterminate`; merged (`tools/merge_batch.py`), assessed rows now 31 of 140. Batch 03 running.

2026-10-16T00:10Z — I4-04 batch 03 (DESIGN_MODULE_METHOD, IDENTITY_METHOD, REFERENCE_FRAME_METHOD, RELEASE_METHOD, SPEC_METHOD; 27 rows; Fable max; 105,871 tokens, 8 minutes): 23 `conserved`, 1 `changed` (`REFERENCE_FRAME_METHOD.md#return-a-closed-result`: "is not transferred" bars what the predecessor merely permitted to omit, and the shared-mechanical-evidence permission is absent at the locus), 3 `indeterminate` (two because the locus delegates to an owner section not in the batch, FOUNDATIONS §2 What creates no authority and FOUNDATIONS §4 Results; one, `#revision-actions`, because reopening every prior-revision result by default may exceed what RF-005 and RF-011 implied). Merged; assessed 54 of 140. Batch 04 running. The repair of the changed row and the decision on `#revision-actions` follow in this session; the owner-delegated rows go to the successor readback with their owner sections supplied.

2026-10-16T00:25Z — Repair of the batch 03 `changed` row at ACTIVATION §7: the working context "need not be transferred" (a permission to omit, as the predecessor had it), may still be attached, and independent evaluations may share valid mechanical evidence under EVALUATION §3, which owns that permission. The three `indeterminate` rows of batch 03 and the two repaired rows of batch 01 are listed in `reassess/successor-readback.json` with the owner and predecessor sections a reader needs; they go to the successor readback. `#revision-actions` keeps its text: the reopening by default follows RF-005 (a mismatched basis is `invalid_basis` or needs reactivation) with the demonstrably-independent survival route of `#return-a-closed-result`; the reader decides with those sections supplied, and a `changed` verdict there becomes a proposed replacement relation.

2026-10-16T00:40Z — I4-04 batch 04 (SPEC_METHOD, 16 rows; Fable max; 89,998 tokens, 5 minutes): 15 `conserved`, 0 `changed`, 1 `indeterminate` (`SPEC_METHOD.md#ambiguity-governance-rule`: the hard-stop classes are delegated to ACTIVATION §4, not in the batch; added to the successor-readback list with that section). Merged; assessed 70 of 140. Batch 05 running.

2026-10-16T01:00Z — I4-04 batch 05 (SPEC_METHOD, STDO_REFERENCE_FRAME_BASELINE; 18 rows; Fable max; 103,564 tokens, 8 minutes): 14 `conserved`, 1 `changed` (`#define-a-project-configuration`: a tenth required record item, the allocation explanation of ACTIVATION §1 Configuration, is new law and needs its own replacement relation), 3 `indeterminate` (`SPEC_METHOD.md#transition-evidence-and-proof-cadence`: the assessor's disposition became a disjunction; `#canonical-compression` of the baseline: adoption narrowed to the Product authority, the Q2 question; `#closure`: delegated to TICKETS §7, not supplied). Merged; assessed 85 of 140. Batch 06 running. Repairs and frontier dispositions follow.

2026-10-16T01:15Z — Repairs from batch 05: ACTIVATION §8 Transition evidence identifies the assessor's recommended disposition where an assessor was activated, the decision owner's beside it (no disjunction); two frontier child rows added as proposed replacements (`#canonical-compression-adoption-authority` under Q2; `#define-a-project-configuration-allocation-explanation`, a new Q9) with the parents' dispositions narrowed to "save the clause split to the child row below"; `reassess/REPLACEMENTS-SUPPLEMENT.md` carries both for the pen. `#closure` and the repaired transition-evidence row are on the successor-readback list. Checks: 707 common rows present once, 11 tenant child rows; 758 loci resolve; frames `--check` 0; program current.

2026-10-16T01:35Z — I4-04 batch 06 (STDO_REFERENCE_FRAME_BASELINE, TICKET_METHOD; 12 rows; Fable max; 93,104 tokens, 6 minutes): 9 `conserved`, 1 `changed` (`#work-result`: the reader found the `incomplete` to `falsified` change, which is exactly the clause the frontier already split to the proposed-replacement child row under Q1; the packet did not show child rows; recorded as an executive note, no text change), 2 `indeterminate` (`#executive-attention-evaluation-and-action`: the packet carried the heading's empty direct text, a packet defect now fixed by a `--whole` option that gives a locus with its subsections; `#derived-generic-specialist-frame-set`: five trailing predecessor paragraphs are not at the one named locus, their carriers to be named in the row). Merged; assessed 95 of 140. Batch 07 running.

2026-10-16T01:50Z — I4-04 batch 07 (TICKET_METHOD, TRAVERSAL_OCCURRENCE_PROFILE, UX_METHOD; 22 rows; Fable max; 90,508 tokens, 4 minutes): 22 `conserved`, 0 `changed`, 0 `indeterminate`. Merged; assessed 117 of 140. Batch 08 running.

2026-10-16T02:05Z — I4-04 batch 08 (UX_METHOD, WORLD_MODEL_METHOD; 12 rows; Fable max; 80,727 tokens, 4 minutes): 11 `conserved`, 0 `changed`, 1 `indeterminate` (`UX_METHOD.md#8a-msg-replay-proof-requirement`: the recorded-exemption exit of UX §15 needs the rc.2 §12 escrow text; added to the successor readback with it). All eight batches read: 140 rows, 125 `conserved`, 3 `changed` (one repaired at ACTIVATION §7, two covered by proposed-replacement child rows), 12 `indeterminate` (two repaired, the rest owner-delegated or packet defects), all 12 plus the repaired rows on the successor-readback list (`reassess/batch-09.md`, 12 rows, generated with whole sections and the extra sections each reading asked for). Cost of the seven Fable batches: 669,420 tokens, 47 minutes.

2026-10-16T02:30Z — Successor readback batch 09 (12 rows; Fable max; 169,230 tokens, 10 minutes): 10 `conserved` (the owner-delegated and packet-defect rows settle as conserved with the sections supplied, among them `#revision-actions`, `#executive-attention-evaluation-and-action`, `#derived-generic-specialist-frame-set`, `#canonical-compression` of REFERENCE_FRAME_METHOD, `#authority-identity-and-conservation`, `#ambiguity-governance-rule`, `#8a-msg-replay-proof-requirement`, `#return-a-closed-result` as repaired, `#transition-evidence-and-proof-cadence` as repaired, `#11d-post-ticket-design-review-rule` as repaired), 1 `changed` (`DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate`: the batch 01 repair had added a recorded-reason exception the predecessor's "must avoid" does not admit; the exception is now removed), 1 `indeterminate` (`#closure`: TICKETS §7 was supplied without its subsections, a packet defect). Merged over the earlier verdicts. Standing over the 140 rows: 135 `conserved`; 3 `changed` of which 2 are the clauses split to proposed-replacement child rows (Q1, Q9) and 1 is repaired and awaits readback; 2 `indeterminate` of which 1 is the clause split to the Q2 child row and 1 awaits readback with TICKETS §7 whole. Those two rows go with the ports' successor readback (`reassess/batch-10.md`, `reviews/PORTS-PACKET-2.md`), one activation.

2026-10-16T03:00Z — R2b-2 and batch 10 returned (Fable max; 161,592 tokens, 12 minutes) and were triaged (`reviews/TRIAGE-R2b2.md`): 11 of 13 R2b findings read back as repaired, 2 partly (the row-3 record, now corrected; the positive reproductions, at the freeze); 6 new findings, all repaired (records; one declaration sentence in REFERENCE_FRAME §1). Batch 10: DESIGN_MODULE §4's binding sentence no longer conditions the preferred shapes on practicality; `#closure` names EXECUTIVE_BASELINE §11 as the locus of condition 22's twelve families. One last readback of these three items runs now (`reassess/batch-11.md`); after it the conservation reading closes with whatever standing remains.

2026-10-16T03:30Z — Last readback, batch 11 (Fable max; 76,322 tokens, 6 minutes): all three items `conserved` (DESIGN_MODULE §4 both lists bind with only the predecessor's one "where practical"; the baseline `#closure` with EXECUTIVE_BASELINE §11 and TICKETS §7 supplied; the REFERENCE_FRAME §1 declaration meets the import rule). The I4-04 conservation reading closes. Standing over the 140 rows read (126 modal conversions and 14 delta-judged rows of WC-2): 137 `conserved` by a same-family nonauthor reading on the successor text; 3 not `conserved` as the parent row was read, each being exactly the clause the frontier splits to a proposed-replacement child row (`#work-result`, Q1; `#define-a-project-configuration`, Q9; the baseline `#canonical-compression`, Q2), recorded with an executive note. No row remains `indeterminate`. Of the 505 other `conserved` rows of the frontier, which rewrote no "must" or "shall" and which WC-2 did not mark delta-judged, 30 were verified by WC-2 at I3 and the rest carry the author's disposition only; they are reported as such in the handoff. Cost of the whole reading, eleven activations: 1,355,000 tokens, about 1 hour 50 minutes. Desk trace DP-01 running on Fable at max at S2 `23b6556`.

2026-10-16T03:50Z — I4-07 desk trace DP-01 (review: combine three mandatory results; Fable max, fresh context; 143,755 tokens, 11 minutes; `paths/DP-01.md`): against S0 `indeterminate` and against S1 `indeterminate`. On S2 the guard passes, four rival deciders and two reconciliations of the predecessor are gone and hops fall from 21 to 5, an elimination witness; the verdict is not `satisfied` because the entry README grew from 2,330 to 28,087 bytes and no tradeoff declared before measurement explains it, and the rule binds the trace to the declared tradeoffs. S1 and S2 are byte-identical on this route. The adverse M4a change is reported against both baselines. DP-07 running.

2026-10-16T04:05Z — I4-07 desk trace DP-07 (resume: a retained summary disagrees with the workspace; Fable max; 149,119 tokens, 12 minutes; `paths/DP-07.md`): `indeterminate` against both baselines, for the same reason as DP-01: every measure but M4a falls against S0 (M2 3→0, M3 3→0, M4b 33,766→22,144, M5 13→4), and the entry README's growth is the one increase no pre-declared tradeoff explains; against S1 the route is already free of rivals and reconciliations. DP-13 running.

2026-10-16T04:30Z — I4-07 desk trace DP-13 (profile: close a sprint with one item partly done and one rejected; Fable max; 149,297 tokens, 15 minutes; `paths/DP-13.md`): `indeterminate` against both baselines. Against S0 the guard passes, two reconciliations are removed and the hop and acquisition increases are the declared TO2 and TO3 tradeoffs and a preserved distinction; the entry README's growth is again the one increase no pre-declared tradeoff names. The tracer notes that S0 reaches its deciding loci only by whole-member reads, no section-level route existing in the predecessor's README. Against S1 the route is byte-identical. DP-19 running.

2026-10-16T04:55Z — I4-07 desk trace DP-19 (profile: who adopts the UX, design, traversal and executive profiles, with which binding fields; Fable max; 186,692 tokens, 17 minutes; `paths/DP-19.md`): `indeterminate` against both baselines. Against S0 an elimination witness (rivals 4 to 1, reconciliations 5 to 2, guard passes); the increases in hops (8 to 15) and acquisition are the README's growth, the PROFILES index and two member leads, none covered by a pre-declared tradeoff. Findings for the frontier and the next iteration: EXECUTIVE_BASELINE §16 and §19 carry two field lists that still decide the same question (conserved from rc.2, a rival the candidate did not contract); PROFILES §1 introduces a "binding" homonym. Against S1 the route is byte-identical. DP-25 running.

2026-10-16T05:15Z — I4-07 desk trace DP-25 (member: assess a member with a conditional obligation of unknown applicability and a design `not_applicable`; Fable max; 128,689 tokens, 10 minutes; `paths/DP-25.md`): `indeterminate` against both baselines. Against S0 an elimination witness (rivals 2 to 0, reconciliations 1 to 0, hops 8 to 1); the increases are the entry README's growth and the size of the one owning section acquired, neither covered by a pre-declared tradeoff. Against S1 the route differs only by the I4 applicability sentence of ACTIVATION §1. DP-31 running.

2026-10-16T05:35Z — I4-07 desk trace DP-31 (resume through the plugin's status skill after an effect of uncertain completion, in a project bootstrapped from the templates; Fable max; 118,236 tokens, 10 minutes; `paths/DP-31.md`): against S0 `satisfied`, the first path to meet the pre-declared rule in full: the guard passes, the one rival and the one reconciliation are removed, and the rise in hops and acquisition is the declared tradeoff TO2 (generic resumption law now owned by ACTIVATION §5 and reached by the skill's named-section route). On S0 the owner of the uncertain-effect reconciliation rule is unreachable by route. Against S1 `indeterminate`: the loci are byte-identical. DP-37, the last of the sample, running.

2026-10-16T05:55Z — I4-07 desk trace DP-37 (profile: a UX requirement is ambiguous and the UX law is needed where no frame carries it; Fable max; 173,281 tokens, 18 minutes; `paths/DP-37.md`): `indeterminate` against both baselines; one rival and two reconciliations removed against S0, the guard passes on S2 and fails on S0 (ambiguity exits unmapped there); the entry README's growth and three route-forced non-deciding UX hops are the uncovered increases. The sample is complete: 7 traces, 1,048,000 tokens, about 1 hour 35 minutes; reading in `paths/SUMMARY.md`. Result: DP-31 `satisfied` against the predecessor; six `indeterminate` with an elimination witness each, all for the undeclared README-size tradeoff; all seven `indeterminate` against `2beed8d` because the routes did not change at I4. Criterion 6 stays `unresolved` for the candidate: 1 of 46 paths `satisfied` against the predecessor, 38 untraced.
- The actual-use trial (D5 option A, `trial/DESIGN.md`) starts: writer TT-01 running on Fable at max. The subject commit of the trial is `23b6556`; the isolated read-only copy of `standards/` for arms A3 and A5 is at the session scratch directory `trial_standards`, byte-identical to that commit.
