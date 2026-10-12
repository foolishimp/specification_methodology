# REVIEW: v3 Intent and Product definitions against the original direction

**Author**: Claude
**Date**: 2026-10-12T23:06:13Z
**Addresses**: the common definitions of `specification_methodology/v3` at `main` `0239be7`, read against Jim's original direction; first part of the Claude and Codex comparison review
**Status**: Draft

## Summary

The common definitions govern the construction project in detail and define
the methodology thinly. Two parts of Jim's direction have no carrier: the
category goal and axiomatic programming as the method's computational model.
The Product spends most of its text on construction governance and selects
no capabilities, so "exceeds 2.5.1" has no common yardstick. Jim's C1
decision leaves no common axioms, so each candidate's axiom set must be
judged on its own. The finite-actor core, bounded steps under an outer
contract, the three tiers, the evidence and authority separations and the
successor conservation law are carried well. The definitions also break the
single-surface rule and carry stale checkpoint state.

The smallest lawful re-entry for the first two findings is an Intent change.
The Product findings follow from it as a Product change.

## Analysis

### Basis and boundary

Subject, read at `0239be7`: `specification/INTENT.md`, `PRODUCT.md`,
`GOALS.md`, `requirements/` and `conformance/README.md`.

Original direction, each file checked against the hash recorded in the C1
input snapshot of T-001:

| Source | Standing | SHA-256 prefix |
|---|---|---|
| Working Product Definition, 2026-10-06 | Jim's definition, recorded by Codex. Its document-structure section is marked as Codex's proposal. | `8c39c833` |
| Coverage matrix of 2.5.1 against other methods, 2026-10-06 | Analyst findings selected by Jim as Product evidence | `ff74fe1d` |
| Codex foundations plan, 2026-10-11 | Tenant proposal. Its foundations table and variables reconstruct Jim's discussion of that day. | `b2bf4e25` |
| Claude steel-thread plan, 2026-10-11 | Tenant proposal | `7fc3e28a` |
| Jim's goal correction, 2026-10-12 | Axioms first, then the full corpus restated; frames for single activation | conversation record |
| Jim's statement, 2026-10-13 | 3.0 lays the groundwork for using algebraic representation and calculus to build processes and software by defining and joining categories, such as algorithms with computation categories | conversation record |

Jim ruled that the review boundary includes the Intent. The category goal
therefore applies to the whole body of work, the definitions included.

Authorship. Codex held the common pen for setup and C1. I have held it since
2026-10-12 and wrote the C3 Construction Contract, the C3 disposition grant,
the standalone successor text in the Intent and requirements, GOAL-002, the
Goals revision record and the frontier consolidation. Findings 3, 6, 7 and 8
cover text I wrote, so they are self-review.

### Trace of the original direction

| Item | Source and standing | Current carrier | Assessment |
|---|---|---|---|
| STDO defines itself through Intent, Product, Specification, Realisation; recursion at material boundaries | 10-06, Jim | Intent, Direction | Carried. The matrix's distinguishing claim, coherent self-definition shown useful under finite attention, is not stated. |
| Axiomatic programming as the computational model: axioms constrain the admissible construction space, bounded probabilistic traversals carry the work | 10-06, Jim | none | Absent |
| Foundations as teleology, ontology, epistemology, algebra and calculus | 10-06, Jim | P1 to P6 in the common principles | Weakened. Covered as working questions that the file says are not law. |
| Outer contract A to X realised by bounded steps that branch, join and refine while preserving it | 10-06, Jim | P4, P5; the C3 activation unit | Carried |
| Reduce interpretive work while keeping every material distinction; reuse results under their bases and invalidation conditions | 10-06, Jim | Intent, Purpose; conformance discriminators | Carried in part. Reuse appears only as a discriminator. |
| The finite actor is the core user; every document names its reader, purpose and task; a worked example | 10-06, Jim | Audiences and tasks inside the C3 contract | Carried as construction configuration, not as Product. Worked examples are classed as external test subjects. |
| Can a bounded actor recover and apply the meaning with less reconstruction, keeping fidelity; shared effectiveness evidence | 10-06, Jim; matrix | C3 criterion 4: bytes measured, fresh-actor application | Partial. No comparison with 2.5.1 and no task-cost measure. |
| Capabilities to preserve, improve, introduce or remove, from the competitive evaluation | 10-06, Jim; matrix | Capability questions, still tentative | Not selected |
| a_c, a_c.STDO and carrier keep distinct identities; the a_c view supplies typed, source-linked context selection and re-entry | 10-06, Jim | a_c dependency file; frames as a_c projections | Identities and context selection carried. The dependency file names only mechanical evaluation. |
| General foundations, Spec Method, domain profiles | 10-11, Jim's discussion | Product Boundary; C3 tier table | Carried |
| Six commitments | 10-11, Jim's discussion | Common principles | Carried as questions; each tenant's answer accepted separately |
| Algorithms, information and computation as categories with maps between them; category and functor laws required | 10-11, Jim's discussion, already hedged | Principles, "Proposed Formalisation And Open Claims"; Intent and Product call them orthogonal concerns | Carried as hypothesis only |
| Documents named ONTOLOGY, ALGEBRA, CALCULUS and so on | 10-06, Codex proposal | Tenant HOW | Correctly left to tenants |
| Axioms first, then the full corpus restated; frames as the activation unit | 10-12, Jim | Intent, Product, C3 contract | Carried, and now dominates the Intent |
| Algebraic representation and calculus for building processes and software by defining and joining categories | 10-13, Jim | none | Absent |

### Findings

**1. The category goal has no carrier.** None of the original posts states
the goal as Jim stated it on 10-13. The nearest are the 10-06 core of
axiomatic programming, with algebra and calculus among the foundations, and
the 10-11 span of algorithms, information and computation. That span was
already framed as hypotheses in both plans, and the common definitions
inherited the framing. The Intent's standing says no universal mathematical
claim is established. P1 calls the claim that all meaning is
algorithmically representable an unresolved hypothesis. The principles demand proof of category and functor laws before
any claim. Nothing directs anyone to build the groundwork. Neither tenant was
asked to define objects, arrows, identity and composition for the method's
own constructs, or to join an algorithm category with a computation
category. Correction: state the goal in the Intent as direction. Keep the
demonstration standard as its acceptance condition: declared objects and
arrows, identity, associative composition, functor laws for each map, and
one worked join. Re-entry: Intent change.

**2. Axiomatic programming, the 10-06 core, is absent.** No common file
mentions it. The a_c dependency file gives a_c one purpose: "mechanical
evaluation of an explicitly selected frozen STDO 3 subject". The 10-06 role
of context selection survives, because the C3 contract makes frames a_c
projections. What is missing is the core claim: explicit axioms constrain the
admissible construction space, and a_c is the representation in which the
method's law and its categories are written and calculated. Correction: the
Intent states axiomatic programming as the computational model. The Product
states a_c's role as representation and calculus and keeps the separate
identities of a_c, its interpretations and carriers. Re-entry: Intent change,
then the Product and the a_c dependency file.

**3. The Product defines the construction project, not the methodology.**
SPEC_METHOD's surface rule says the Product states the current concrete
product definition and bridges intent to requirements. Two sections describe
the methodology. The other seven govern its construction: branches,
worktrees, pens, checkpoints and the Executive loop.

| Product section | Bytes |
|---|---|
| Product Boundary, Product Identity And Lineage | 3,707 |
| C3 contract, Development Isolation, Construction Authority, Shared Construction Contract, Open Owner Decisions, Checkpoints, Dependencies | 17,416 |

It states no capabilities, no users and tasks as Product meaning, no success
criteria, no reader routes and no worked example. Correction: move
construction governance to the frame basis, the ticket or design. The Product
then states what the methodology provides. Re-entry: Product change.

**4. No capability target, so "exceeds 2.5.1" has no yardstick.** This
follows from Jim's C2 decision, which closed C2 on acceptance criteria,
audiences and tasks. The capability file still holds tentative questions
"OPEN behind C1". The matrix's findings for 3.0 did not reach the Product:
- a short route from theory to useful work, with worked examples;
- bounded computation explicit in the native representation, judged by
  fresh-context recovery;
- tests of the evaluator as well as the constructor;
- shared effectiveness evidence of task, errors found, actor needs and cost;
- removal of redundant reconstruction and ceremony.

Correction: select capabilities. They are 2.5.1's thirteen logical
capabilities as conserved, plus the new ones the 10-06 definition and the
matrix name, plus category construction from finding 1. Re-entry: Product
change, then requirements.

**5. There are no common axioms.** This follows from Jim's C1 decision to
accept each tenant's principles separately. The common principles file says
it is not STDO 3 law. The Intent requires the axioms first, so each candidate
rests on its own axiom set. The comparison must judge each set on its own
terms. A release needs either Jim's selection of one set or a common axiom
basis. This is a decision for Jim.

**6. The Intent is dominated by successor mechanics.** The Purpose section
is 1,595 bytes. One paragraph of 1,185 bytes covers UP-015 dispositions, the
standalone successor, directory paths and construction order. The 10-06
definition of Intent is purpose, beneficiaries, values and desired outcomes.
The current Intent names no beneficiaries, values or outcomes. Correction:
move successor mechanics to the Product and requirements. The Intent states
why the methodology exists, for whom, and the direction, including findings 1
and 2. Re-entry: Intent change. Self-review.

**7. Checkpoint state is stale or contradictory.**
- Goals says "The current wave is C2" while its own table records C2 closed.
- Goals and the Product's open decisions say the C3 Executive and Reviewer
  actors are unbound, and that every execution contract stays drafted. C3
  construction ran with Claude as Executive on Jim's instruction of 10-12.
- The requirements index calls the frontier and the standalone successor
  requirement proposed and awaiting review. C3 was built and merged on both.
- The capability file says "OPEN behind C1". The conformance file says
  runnable cases await C2.
- The 195 KB frontier is a construction ledger. It sits in `requirements/`
  and opens with "PROPOSED on branch `common/c3-contract`".

Self-review for the C3 entries.

**8. The definitions break the single-surface rule.**
- Status lines in the Product, principles, capabilities, conformance and
  frontier files. Standing sections in the Intent and the a_c dependency.
- Dated decisions inside law. The Product has six, such as "Decided by Jim
  on 2026-10-12".
- History in live text, such as "Codex held the common construction pen for
  setup and C1" and "The earlier `rc/stdo_3/3.0.0` proposal is withdrawn".
- A Revision Record in Goals.
- Version branding in titles and prose: "STDO 3 Intent", "STDO 3 Product",
  "STDO 3 uses". The surface rule reserves version labels for release
  facts. The product is the STDO Specification Methodology.

Self-review for the C3-era entries.

### Carried well

- The finite actor, bounded steps under an outer contract, and truthful
  stops, in P4, P5 and the activation unit.
- The separations of interpretation from representation, evidence from
  claim, and judgment from authority, in P1 and P6.
- The three tiers and the bar against runtime vocabulary in the foundations.
- UP-015 successor conservation, with the standalone successor requirement
  closing the "route is not restatement" gap.
- Honest epistemic standing on mathematical claims. Finding 1 asks that this
  standard govern the pursuit of the category goal, not replace it.
- Independent tenants under one common WHAT, with selection reserved to Jim.

### Consequences for the comparison

- The candidates were built to these definitions. Where the definitions are
  silent, both candidates are graded on support for the original direction.
  The gap is attributed to the definitions, not to the tenants.
- Capture of 2.5.1 is measured against its thirteen logical capabilities and
  its Product Outcome list, plus sampled frontier rows. Exceeding 2.5.1 is
  measured against the matrix findings above. A new capability counts only
  when it names its purpose and material relation.
- The category criterion grades readiness: what each framework already
  defines, and what is missing, for defining and joining categories. Neither
  tenant was asked to deliver it.
- Each axiom set is judged on its own terms.

## Recommended Action

Decisions for Jim:

1. Accept the Intent change carrying the category goal and axiomatic
   programming as the computational model. The pen drafts it and Codex
   reviews it before merge.
2. Choose between one common axiom basis and per-tenant axiom sets with a
   selection at release.
3. Move construction governance out of the Product, and the frontier out of
   `requirements/`, as a Product change.
4. Run the comparison now against the current definitions plus the original
   direction, or after the Intent and Product change.
