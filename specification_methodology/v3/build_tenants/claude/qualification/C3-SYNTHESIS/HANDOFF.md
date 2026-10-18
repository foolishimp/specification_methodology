# C3 Cross-Synthesis Handoff, Claude Line

This is the Claude line's return for the product owner's review. Nothing here is acceptance. Every review in this rebuild was a same-family working check: a fresh Claude context that did not write its subject. Under this line's reading of independence, the tenant is the author, so none of those checks counts towards acceptance. Acceptance needs a cross-family review and the product owner's decision.

- Branch: `tenant/claude/c3-synthesis`.
- Worktree: `/Users/jim/src/apps/specification_methodology-claude`.
- Cut from `main` at `47ef3e8`, with `main` at `a7eba66` merged inward.
- The full record, with every activation, return, ruling and default in time order, is the [ledger](LEDGER.md).

## What was asked

> so i'm giving you the go ahead to refactor v3/claude under the new requirement & specification, you are not to block and will review the work in the morning

This was read as rebuilding the Claude candidate on its own base at `31f28f9`, not from nothing, against the common specification as at `a7eba66`. The rebuild takes the named parts from the Codex candidate that the cross-assessments nominated, per the [proposal](../../../../.ai-workspace/comments/claude/20261013T174341Z_STRATEGY_cross_synthesis_rebuild.md). Where a decision was open, a default was taken and recorded in the ledger; see "Defaults Taken For The Open Decisions" there.

## What the candidate now does

The method is prose. Its 23 members in `standards/` are Markdown, and so are the frames in `standards/frames/`. Code exists only as qualification tooling under `qualification/`, covered below.

| New common obligation | Where the candidate addresses it (same-family checks only) |
|---|---|
| Restated on the axioms, relation 1 (foundation to law) | FOUNDATIONS §3 states premises P0 to P6, each with its standing: recovered, independent or derived. It owns the four-column table format and indexes 21 families of deciding rules. Each family has its table in its owning member, at the point where an actor enters it. |
| Relation 2 (ownership and use) | Members use the shared contracts where their actors apply them. PROFILES §1 owns the profile import rule. FOUNDATIONS §2 owns imports between members, and PRODUCT_DEFINITION §5 refines it. |
| Single ownership | One owner each for: the core results and conjunction (FOUNDATIONS §4); size measurement (ACTIVATION §2 step 3); the hard stops (ACTIVATION §4); configuration (ACTIVATION §1); the build-tenant binding (SPEC_METHOD §11). Other members refer to these owners. |
| Single result algebra | FOUNDATIONS §4 Results owns the five core values: `satisfied`, `falsified`, `indeterminate`, `out_of_frame` and `invalid_basis`. Every profile and member value maps once into them, including AC-007's constraint results and operation stops, which unifies the predecessor's two algebras. An evaluation that was not performed has no result, and conjunction keeps that gap apart. |
| Bounded transitions and frames | ACTIVATION §1 adds Transitions (A to Z) and Configuration, with no fixed role inventory. The Executive, Writer and Reviewer arrangement is one configuration, owned by EXECUTIVE_BASELINE §7. ACTIVATION §5 states that the workspace is the continuing truth surface and an actor's context is a disposable account of it. Size shows only that a context fits; adequate attention is shown by actual use (EVALUATION §7). |
| Build-tenant binding | SPEC_METHOD §11 states items 1 to 6 as method law. The three accounts of a construction are defined in FOUNDATIONS §2 and applied in §11. The tenant's own binding is in `design/CONSTRUCTION_BINDING.md`. |
| Categorical demonstration | FOUNDATIONS §4 Formal fragment carries items 1, 4 and 5 for the candidate's own categorical statements. EVALUATION §6 holds the equivalence ladder. The categorical diagram H1 stays a hypothesis. |
| 31 conformance discriminators | CONFORMANCE maps 11 to cases and 20 to named logical-review checks. No case has a recorded pass. |

Parts taken from the Codex candidate at `31f28f9`, listed in [`design/CROSS_SYNTHESIS.md`](../../design/CROSS_SYNTHESIS.md):

- the foundation-to-law table format;
- the premise standing discipline;
- reference-only import declarations and the equivalence ladder;
- verbatim digest-bound frames, with a manifest and the rule to acquire the deciding owner directly;
- the finite-check pattern.

Frontier copy ([`frontier/PREDECESSOR_CLAIMS.md`](../../frontier/PREDECESSOR_CLAIMS.md)):

| Disposition | Now (696 rows) | At the base (691 rows) |
|---|---|---|
| `conserved` | 659 | 658 |
| `superseded` | 7 | 2 |
| `not applicable` | 20 | 20 |
| `unresolved` | 10 | 11 |

The five new rows are `superseded` children split from EXECUTIVE_BASELINE parent rows. Every `conserved` or `superseded` locus resolves (666 rows checked). The re-proof span is 303 rows ([`span/SPAN.md`](span/SPAN.md)): these need the claim-by-claim comparison again.

## Rulings to review

Each ruling is in the ledger with its reason.

1. **Five core values, not six.** Non-performance is the absence of a closed result. Conjunction keeps it apart from undecidable evidence and from uncovered coverage. The alternative is a sixth value, `not_performed`, with RF-012 becoming `superseded`.
2. **A demonstrated violation stays `falsified`.** This holds even when the refusal also names a basis condition, which is reported beside it as its own `invalid_basis` result. A known failure is never hidden. The predecessor AC-007 states no precedence, so this is an added choice owned by AXIOMATIC_CALCULUS.
3. **Mappings into the core:**
   - a missing capability that refuses activation maps to `out_of_frame`;
   - a work step's `incomplete` maps to `falsified`, and only for the predicate "a candidate is available";
   - a further refinement keeps its parent's core value.
4. **A basis mismatch is AC-007's "mixed bases"** (`refusal(basis)`, `invalid_basis`). It is never a violated signature constraint. Two reclassifications rest on this same-family ruling and need cross-family confirmation.
5. **Predecessor rows 516, 522, 543, 560 and 565 are split.** The predecessor tied a core result to a work-result variant, which no longer holds once `refused` and `incomplete` both map to `falsified`.
6. **DESIGN_MODULE `not_applicable` maps to `satisfied`** for "the design meets the axiom, or the axiom does not apply". It needs an evidenced false applicability premise and never counts as conformance.
7. **Non-mandatory failures are never discarded.** The declared decision rule states how non-mandatory results count. A material counterexample to a mandatory constraint falsifies the conjunction, whoever found it.
8. **Dropped tenant-added sentence.** "superseded: the successor clause and what changed are named" had no predecessor source and was dropped.

## Actual-use evidence

Nine tasks were run twice each, a total of 18 fresh Sonnet actors. Each actor had only its frame and task, ran with no tools outside any repository, and its context was measured before start under a 110,000-byte cap. Spend was USD 3.22.

The oracles were written before any frame existed, by actors who read no candidate text. The tasks cover:
- REFERENCE_FRAME, AXIOMATIC_CALCULUS, TRAVERSAL_OCCURRENCE, EXECUTIVE_BASELINE and DESIGN_MODULE: the five members whose criterion 4 evidence was not established in the first pass;
- three new tasks: configuration, build-tenant binding and a stale summary.

C3S-01 to C3S-04 ([AS1](reviews/AS1.md)): all 10 runs `falsified` under strict grading.

| Case | Required core result | Main failures |
|---|---|---|
| C3S-01 A (REFERENCE_FRAME) | reached | format only (sentence limits) |
| C3S-01 B | reached | the reopen list was missed |
| C3S-02 (AXIOMATIC_CALCULUS) | reached | r1 lacks a scope ground and offers a grant as a cure; r2 fails on format only |
| C3S-03 (TRAVERSAL_OCCURRENCE) | not reached under this oracle | occ-24: both actors gave `indeterminate`; the new oracle requires `falsified` |
| C3S-04 (EXECUTIVE_BASELINE) | reached in all five rows | no residual owner named; format |

Method-text findings from AS1, all open:
- **MT-1:** REFERENCE_FRAME §10 says a change that "clarifies an activation" is non-material and reopens nothing. The predecessor has no such clause. The clause is inherited: it was already in the base at `31f28f9` and was not introduced by this rebuild. It is a conservation defect to repair or justify.
- **MT-2:** REFERENCE_FRAME §10 gives no standing for an out-of-family activation's result.
- **MT-3, and an oracle conflict on occ-24.** Two independent oracles derived from the same predecessor disagree.
  - The first pass's F-03 oracle, as amended by R25, requires occ-24 `indeterminate`. Both actors answered that.
  - Tonight's C3S-03 oracle requires `falsified`.
  - The base text already made `partial_effect` conditional on what the effect evidence establishes. This rebuild split that condition into `partial_effect(ended)` and `partial_effect(unknown)`, which is consistent with the 12 October meaning: `falsified` only on demonstrated non-attainment.
  - Whether occ-24's facts demonstrate that the effect ended decides the question. It needs a ruling, preferably cross-family, and neither oracle has been edited. MT-3 is one possible cause, not a demonstrated one.
- **MT-4:** REFERENCE_FRAME §5 `activation_refusal(authority)` does not separate an authority that was refused from one that was never recorded.
- **MT-5 and MT-6:** minor.

AS1 found no frame fidelity defect. Every task with a sentence limit saw it exceeded, and the routing card contributes to that.

C3S-05 to C3S-08 ([AS2](reviews/AS2.md)):

| Case | Result |
|---|---|
| C3S-05 | both runs `satisfied` |
| C3S-06 | both runs `satisfied` |
| C3S-07 | both runs `falsified` on one item (the oracle asks for an executor statement the task does not raise) |
| C3S-08 | one run `satisfied`, one `falsified` on one item (actor application) |

All eight reached their required core results, and none of their failures traces to method text or frame content.

## Open

- **Acceptance.** Every member needs a cross-family review under criteria 1 to 6, together with the claim-by-claim comparison for the 303 span rows.
- **Ported-part review.** How ported parts are reviewed is the product owner's open decision. The default here: ported text is compared with its source byte for byte and with the predecessor by a Claude reviewer who did not port it, and Codex reviews the Claude-written text around it.
- **Compressed summaries.** The ten rows stay `unresolved` until the product owner rules. They must close before a release-candidate cut.
- **a_c interpretation.** Programs set-2 to set-6 are bound to member text from before this rebuild, and re-encoding is open. The verbatim frames are the activation unit.
- **Finite check (RC12-3, material).** The check proves only that a gap or a not-performed result is never `satisfied`. It does not constrain which value a conjunction reports, and two §4 clauses are not encoded. Its README claims more than this and should be read with [RC12](reviews/RC12.md).
- **Frame links.** Frames are verbatim excerpts one directory deeper, so their copied relative links do not resolve there. The link-rewriting step from Codex was not ported.
- **Code.** The tooling under `qualification/` is outside the method: the frame generator and tests, the finite check, the span script, and the first-pass run instrument. If the product owner wants no code in the candidate, it can be removed. The cost is hand-checking each frame against its source.
- **Minor method findings from the runs.** FOUNDATIONS §4 gives no default reported value when no decision rule is declared. SPEC_METHOD §11 rule 2 does not say whether a requirement naming a role is the admission. The way DESIGN_MODULE §7's gate combines with the generic disposition is unstated.
- **Process variances.**
  - Two Writers, A4b and A4c, measured their inputs after reading them, against the C3 Limits.
  - Host-added context in subagents is not measurable.
  - Ledger entries are written before the pen transcribes them into T-002-CLAUDE.
- **Common specification.** Not reviewed cross-family by Claude: Codex's revision `e38d45a..a7eba66`. The expectations author recorded ambiguities A1 to A9 in [EXPECTATIONS](EXPECTATIONS.md).
