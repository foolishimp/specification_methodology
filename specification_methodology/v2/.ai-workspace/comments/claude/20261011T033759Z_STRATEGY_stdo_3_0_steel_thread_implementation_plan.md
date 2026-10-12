# STRATEGY: STDO 3.0 Steel-Thread Implementation Plan

**Author**: Claude
**Product direction**: Jim
**Date**: 2026-10-11T03:37:59Z
**Updated**: 2026-10-11T04:05:00Z
**Status**: Draft
**Addresses**: [STDO 3.0 working Product definition](../codex/20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md), its [competitive baseline](../codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md), and Jim's 2026-10-11 foundational-principles discussion with Codex
**Discussion state**: One of two candidate plans Jim is evaluating. Commentary, not authority.

## Summary

Jim asked for a plan of the form
{current STDO, ABG realisation lessons, STDO 3.0 proposal, foundational
principles} → proposed structure → proposed implementation plan: a deep
attempt at the principles first, reviewed at that layer; then the capability
and feature list; then a series of steel-thread document-building threads,
each proven through a_c as an independent test of both STDO 3.0 and a_c.

This post proposes that plan. Its main choices are: recover existing law
before writing new law; order the axioms by derivation so the generative one
(finite capacity under a governing outer contract) is first; keep three tiers
(foundations, Spec Method, operational realisations) with no runtime
vocabulary in the foundations; treat the prose standards and the a_c program
as two carriers of one meaning so their disagreement is a test; review the
principles layer before any document set is built; and turn the ABG lessons
into runnable counterexamples rather than prose.

Amended 2026-10-11 after Jim's direction: the first review is at the
principles layer, not a steel thread, and STDO 3.0 is a new peer Product root
with Codex and Claude as independent build tenants under one shared WHAT.

## Analysis

### Inputs and what each contributes

| Input | Supplies | Consolidation move | Output |
|---|---|---|---|
| STDO 2.5.1 RC2, installed `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4…` | Existing formulations of every principle: proportionality (`SPEC_METHOD.md` UP-014), bounded-frame conservation (`DESIGN_MODULE_METHOD.md` UP-017), activation (`SPEC_METHOD.md` UP-020), finite attention (`REFERENCE_FRAME_METHOD.md` RF-002), functor kinds and typed composition (`AXIOMATIC_CALCULUS.md` AC-015/016), recursive product taxonomy and WHAT/HOW tenants (`SPEC_METHOD.md`) | Recover, do not rewrite. For each foundational principle, locate its current clause(s) and record exact source routes. Where none exists, mark a demonstrated gap | Principle-to-clause recovery table |
| ABG realisation, March to October 2026 | The failure classes the method did not prevent | Turn each lesson into a counterexample scenario naming the mechanism that should have caught it | Conformance scenario list below |
| STDO 3.0 STRATEGY post, 2026-10-06 | Product statement, four-stage chain, finite-attention core, readers, document owners, five open decisions, matrix result F27–F30 = 4/12 | Keep as the Product definition carrier; amend in place | Updated Product definition |
| Foundational principles, Jim and Codex, 2026-10-11 | Six axioms; three tiers; five questions per Spec Method mechanism | Order the axioms by derivation. Finite capacity and purpose are generative; identity and justification are independent; composition and interpretation follow. Mark the hypotheses: categorical equivalence of 𝒜 and ℐ, universal algorithmic capture of meaning, the stronger Markov-boundary properties | Ordered axiom base |

The recovery table is the first real deliverable. It shows how much of 3.0
is restructuring and how much is new law, which decides the size of
everything after it.

### Why finite capacity is the first axiom

State the core once: a finite actor realises an outer contract A→X through
bounded steps, each with a selected context that fits and carries enough to
preserve the outer obligation. The other principles then follow from it.
Purpose through decomposition exists because the actor is bounded, so each
intermediate boundary inherits its purpose from the step it serves.
Conservation is the obligation on each step's output, because steps are
where material is lost. Totality exists because a bounded actor meets
conditions outside its context. Cost exposure and proportionality are how
spend is measured against the scarce resource. Shared machinery exists to
keep steps small enough to fit. A native representation and a reader route
exist so a fresh bounded actor can recover the meaning (F27, F28);
effectiveness and resource measurement are the same resource measured (F29,
F30). Runtime terms (HoG, F_D/F_P, worksites, event logs) are one runtime's
way of doing bounded traversal, which puts them on the profile side of the
line.

Two principles do not derive from it. One WHAT with several HOWs comes from
specification; objecthood comes from ontology. They are independent
foundations that the core sits beside. The categorical diagram
ℐ ← 𝒜 → 𝒞_H is added law until its objects, arrows, identities and
composition laws are defined (`AXIOMATIC_CALCULUS.md` line 724 already says
so); it stays a labelled hypothesis.

### Proposed structure

Three tiers, one meaning, two carriers.

Tier 1, foundations: INTENT, PRODUCT, ONTOLOGY, ALGEBRA, CALCULUS,
EVALUATION. These hold the axioms and the generic account of bounded
computation. No ABG, ODD, HoG or F_D/F_P vocabulary here.

Tier 2, Spec Method: LIFECYCLE plus the mechanisms: intent → Product → common
WHAT → admissible HOWs → bounded construction → evaluation → re-entry →
accept, continue, yield or terminate. Each mechanism carries its five-question
justification: which principle requires it, what transformation it performs,
which distinctions it preserves, which alternative realisations satisfy the
same contract, and what observable result demonstrates its adequacy.

Tier 3, operational realisations and profiles: SOFTWARE_DESIGN,
GRAPH_EXECUTION (ODD roles, HoG binding, ledger and events), UX, WORLD_MODEL
(Markov object as candidate), plus reference frames, build tenants and
tooling. Each profile imports Tier 1 and Tier 2 by reference and adds only
domain obligations.

Two carriers of the same WHAT: the prose standards and the a_c program. The
a_c program is not documentation of the prose; it is a second realisation of
the same clauses, which is what makes it an independent test. When prose and
a_c disagree, exactly one of three things is defective: the clause is
ambiguous (a 3.0 defect), a_c cannot express it (an a_c defect), or the
encoding is wrong (an encoding defect). Every disagreement is triaged to its
owner before repair. Compressions and the glossary are derived from the
carriers, never authored.

Placement, decided 2026-10-11: a new peer source project beside the 2.x
child in this checkout (`stdo_3_0/` or `stdo_3/`), with its own Product
Definition whose builder basis is `stdo://releases/v2.5.1-rc.2/`, a shared
`specification/` holding the WHAT (INTENT, PRODUCT, GOALS,
REFERENCE_FRAME_BASIS, requirements, conformance), and `build_tenants/codex/`
and `build_tenants/claude/` each holding one independent realisation
(design, documents, a_c program, qualification). The 2.x child is untouched
and the 2.5.1 cohort in `stack_release.json` is unchanged. The axiom base,
capability list and conformance scenarios are WHAT; document organisation,
wording and encoding are tenant HOW. Tenants do not read each other's
realisation before review. PRODUCT.md declares the selected tenant per cut.

### Candidate STDO 3.0 capabilities

To be fixed in Thread 0.

| Tier | Capability |
|---|---|
| 1 | Ordered axiom base with recovered sources and explicit hypotheses |
| 1 | Generic bounded-computation calculus: context selection, capacity fit, refinement, composition, observation, gap, next action, stop, re-entry |
| 1 | Conservation stated once and applied uniformly at every boundary |
| 1 | Claim, evidence, judgment and authority distinctions with acceptance conditions |
| 2 | WHAT/HOW with conformance, semantic equivalence and computational equivalence as separate claims |
| 2 | Bounded activation: grant, territory, context, return contract, re-entry |
| 2 | Totality dispositions: continue, refine, recover, yield, re-enter, terminate |
| 2 | Cost obligation on every activation and return (F30) |
| 2 | Restart as iteration over existing work state with reconciliation |
| 2 | Lifecycle: ticket-first, closure by stated condition, RC lineage, predecessor and successor |
| 3 | Native representation (a_c) with fresh-context recovery as its acceptance test (F27) |
| 3 | Reader routes: README, GUIDE, WORKED_EXAMPLE including a defective candidate (F28) |
| 3 | Profiles importing foundations without duplication; GRAPH_EXECUTION owns ODD and HoG bindings |
| 3 | Conformance scenarios and counterexamples, run and recorded (F29) |

### Implementation plan

Thread 0, Product definition. Amend the 2026-10-06 STRATEGY post with the
ordered axiom base, the three-tier structure, the capability list, placement,
and numeric budgets (per-thread token and time budget; per-actor context cap
for trials). Closes when each of the five open decisions in that post has an
answer or an explicit deferral with an owner.

Thread 1, principles layer, one per tenant. Each tenant makes its deep
attempt at the foundations: the ordered axiom base; for each axiom its
recovered 2.5.1 clause(s) with exact source routes, or a marked gap; the
derivation showing which principles follow from the generative axioms and
which are independent; the hypotheses, labelled; and, for each Spec Method
mechanism the tenant intends to realise, its five-question justification.
This is the first review. The reviewer judges substance at that layer:
whether the axioms are recovered rather than invented, whether the
derivation order holds, whether anything is contradictory or duplicated,
whether the hypotheses are honest, and whether each mechanism is justified
by a principle rather than by precedent. No document set, worked example or
trial is required for this review. Closes when the review returns a closed
result and Jim accepts the principles layer for that tenant.

Thread 2, capabilities and features. From the accepted principles, fix the
3.0 capability list and the conformance scenarios in the shared WHAT. The
candidate list above is the starting point; the accepted principles decide
what stays, what is added and what has no principle requiring it. Closes
when each capability names its requiring principle and its observable
acceptance result.

Threads 3 onward, steel threads, one per capability cluster per tenant.
Each carries one capability end to end: Tier 1 clause → Tier 2 mechanism →
Tier 3 realisation → a_c encoding → fresh-context trial. The first steel
thread should be finite capacity → totality → bounded activation with
context selection and re-entry, because it is the generative axiom, it is
where the ABG lessons concentrate (restarts, context cap, the 504.8 MB
manifest, F_D drift), it is the matrix's weakest area, and the current a_c
view was found not to carry it at depth, so it tests a_c hardest. Its trial
is the matrix's first: a fresh-context actor, given only the 3.0 documents
and a_c map, performs a bounded activation on a task whose required basis
exceeds its declared context cap, then a coupled case that cannot fit; the
same task runs against 2.5.1 RC2 as baseline; record fidelity under
independent assessment, reconstruction tokens, outcome and the explicit
limit or escalation.

A steel thread closes when: the recovery table for its capability is
complete; the Tier 1, 2 and 3 clauses exist; `ac.py validate` is green and
`ac.py join` resolves every selected section to exact source; the
fresh-context trial has numbers for 3.0 and for the baseline; an independent
reviewer has read the trial data rather than its labels; and the thread's
own cost is recorded. Candidate order after the first: purpose and
specification (WHAT/HOW); composition and conservation; evaluation and
justification; execution and resources; lifecycle and release; readers and
representation; profiles; conformance and qualification. The order is
adjustable once the first steel thread shows the real cost per thread.

Each thread is a ticket on `main` with a performed intake triage, declared
gates, a stated closure condition, an independent reviewer and a budget. All
declared gates run on every review, including WRITING_GUIDE lint and link and
whitespace checks.

### a_c as the independent test

The a_c tool is `axiom_indexer/build_tenants/core/code/ac.py` (validate,
join) in this checkout. The a_c.STDO program for the operative cut is
`stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.2/`
(program, logical map, source corpus and validation report, 2026-09-30).
Correction 2026-10-11: the first version of this post said no rc.2 encoding
existed; that read came from the retired `~/src/apps/stdo_representation`
checkout, not this one. The rc.2 program is a baseline for the fresh-context
trial; it supplies no qualification of 3.0. The steel thread encodes the one
chosen principle against the 3.0 draft rather than refreshing the 2.5.x
program.

Per thread: author the a_c program for the thread's clauses from the exact
3.0 source routes; run `validate` with a bindings file and emit the logical
map; run `join` on Executive-selected sections to produce the fresh-context
trial prompt; run the trial; triage every validation diagnostic and every
trial failure to 3.0 prose, a_c tool or encoding. An a_c defect is a ticket in
the a_c project, not a reason to bend the 3.0 clause.

### Conformance scenarios from the ABG lessons

These become the counterexamples 3.0 must catch. Each names the mechanism
under test.

| Lesson | Mechanism under test |
|---|---|
| Day-one "re-running is cheap" with no cost term | Every activation declares a budget; every return reports spend |
| 40/40 green stamped over PENDING witnesses | Review reads the data under every label; destination delta is judged first |
| Eight restarts carrying the pattern in method stance | Restart is iteration over existing work state with reconciliation; a fresh start needs justification |
| Runtime construction duplicated per handoff (T-288) | Review counts dynamic reads, validations and derivations, not static clones |
| 504.8 MB manifest parsed to select 182 entries | Selective acquisition is a declared contract; transferred context is counted |
| 2.4 GB report | Report volume is separated from model traffic in cost accounting |
| Provider permission profile missed at intake | Operational variables are activation intake fields |
| STDO 2.0 as a correctness amplifier of a wrong vector | Product-outcome gate precedes engine completeness |
| F_D drift into F_P responsibility | Boundary conformance case |
| Scenario patched around a framework defect | Owner triage before repair |
| Closure by reviewer approval rather than stated condition | Closure-law case |
| Carrier and ticket churn findings | Substance-over-carrier review case |

The matrix's eight proposed trials cover the positive paths. Together these
form the CONFORMANCE member and the F29 evidence.

### Release and non-goals

Cut `rc/stdo/3.0.0` only after the conformance scenarios run green on the
whole member set and the a_c program validates against it. No odd_* product
(ABIogenesis, odd_manager, odd_glc) re-pins before an RC is published; this
is the STDO 2.0 premature-tap lesson.

Not in scope: any runtime; any ABIogenesis source change; any adoption or
effectiveness claim before the trials have numbers; any import of HoG,
F_D/F_P or worksite vocabulary into Tier 1.

## Recommended Action

1. Jim evaluates this plan against the Codex plan. Suggested checks for
   either: does it start from a recovery of existing law or from new text;
   does the first thread test the generative axiom end to end, including
   a_c, before anything widens; does every mechanism carry its five-question
   justification; does each thread close on a stated condition with recorded
   cost; do the ABG lessons appear as runnable counterexamples.
2. Set up the 3.0 Product root and shared WHAT (Thread 0), then open Thread 1
   in each tenant. The first review is at the principles layer.
3. Open steel threads only after both the accepted principles and the
   capability list exist, with budget and context cap declared before the
   first activation.

Keep the original Date when amending this post and update Updated.
