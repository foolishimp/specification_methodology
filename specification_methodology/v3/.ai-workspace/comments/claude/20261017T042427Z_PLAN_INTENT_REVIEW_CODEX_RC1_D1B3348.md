# Plan and expectations: intent-level content review of the Codex RC1 candidate

Author: the Claude tenant session, acting at the product owner's
instruction as an independent reviewer of the Codex candidate: "i want a
deep content review, actual does the implementation deliver on the INTENT
of the specification, is the product met, dont trust codexes tests they
are not a metric". The reviewer is the author of the rival Claude
candidate; that bias is disclosed and the tests below are built to limit
it. Written before any text of the subject was opened.

Subject: the corrected Codex RC1 candidate at
`d1b33480b46f45bb46198a2f63ca197e84e40e55` on `tenant/codex/c3-iteration-5`,
read only under `build_tenants/codex/successor/` (standards, frames,
README, plugins) with `git show`. Basis: `specification/INTENT.md`,
`PRODUCT.md` (Product Boundary, Foundational Reduction, Construction And
Context Management, Universal Construction Model, Method Structure,
Build-Tenant Binding, Result Algebra, Categorical Construction) and
`requirements/README.md`, `requirements/ASSURANCE.md`, all at `4c340f7`.
Predecessor: the installed `v2.5.1-rc.2`.

Not used as evidence: the candidate's own returns, readbacks, reviews,
conservation and determinations records, checks and receipts. The
product owner's scoping applies to both lines: complete interpretation
coverage, the remaining actual-use expectation sets and the authority
compressions are out of scope; the interpretation is read for what it
claims, not for completeness.

## Expectations

Each is judged `delivered`, `partly`, `not delivered` or `cannot tell`,
with quotes from the candidate.

| # | Intent area | Delivered if | Not delivered if |
|---|---|---|---|
| E1 | A and Z | one owner defines A (bound current state, workspace versus acquired account, explicit unknowns) and Z (constraints on acceptable outcomes with acceptance conditions; several states may satisfy), and work, review and release consumers bind A and Z when they act | A and Z appear as an introduction while consumers decide with their own notions |
| E2 | universal scope | generic procedures hold for software, human and mixed execution; a human process can be bound without a parallel method | procedures presume code, a stack or an event stream where the obligation does not |
| E3 | lawful is not delivered | the text separates admissible construction from delivered outcome; calculi select no outcome; proofs keep premises | a lawful or passing construction is treated as delivery |
| E4 | three accounts and diagnosis | specification, observations and predictive model are separate; diagnosis among realisation, requirement or design, model and observation; a bug enters the same intake as change work | a bug label selects a repair class, or a model's prediction decides the outcome |
| E5 | strategy | strategies are selected on resources, feedback delay, risk and rework; none is imposed; a superiority claim states its basis | a strategy is prescribed or selected by name |
| E6 | preservation, progress, completion | the three are separate claims; continue, revise, repair, recover or stop with an explicit unresolved outcome; exhaustion proves neither achievement nor impossibility | completion is inferred from local steps, counts or exhausted effort |
| E7 | workspace and resumption | the workspace persists, an account is rebuilt against it; resumption keeps valid work; invalidation reopens affected claims; a destination change follows its owner | the account or a summary overrules the workspace, or recovery resets everything |
| E8 | parallel derivation | construction and tests derive from shared obligations; assertion and execution provenance; agreement proves neither fidelity nor outcome | tests copied from the implementation count as independent; agreement counts as proof |
| E9 | preservation obligations | step, join and end-to-end obligations connect local checks to Z | local passes are taken as end-to-end success |
| E10 | change and reuse | a change reassesses affected claims and retains evidence with established applicability; mandatory gates stay; required assurance governs selection | unchanged bytes alone justify reuse, or every change forces full re-execution by rule |
| E11 | observation and necessary conditions | a pass of a necessary condition establishes only it; an observation that cannot separate cases yields indeterminate or more evidence | a key-only test establishes the full obligation |
| E12 | reference frames | a frame carries sufficient material, rules, authority and result contract; fit and attention are separate; capacity never licenses omitting an obligation | frames are file bundles with no task contract, or capacity excuses omission |
| E13 | configuration | roles follow from operations, dependencies, capabilities and assurance; a configuration explains its allocation; naming grants no authority | a fixed role inventory or hierarchy is assumed as method law |
| E14 | produce, check, accept | the three are distinct acts; results record basis, evidence and unresolved matters for reuse without private memory | a review or passing check is acceptance |
| E15 | standalone | every conserved determination is in the successor's own text; predecessor links are provenance only | a deciding rule is supplied only by a link into rc.2 |
| E16 | tiers | foundations own shared laws, the Spec Method applies them, profiles own only their bindings, visibly in the member set | the predecessor's member set is kept with a foundations layer added beside it |
| E17 | foundation to law | material rule families state premises, consequences and policy choices with owners, inherited rules included | arguments cover new rules only, or name premises without the consequences they decide |
| E18 | reduction | recurring determinations are contracted into shared owners and consumers no longer decide them independently; predecessor document boundaries do not set the architecture; ordinary paths are simpler | consumers keep rival rules beside a new shared owner; retained layout carries the old reconciliations |
| E19 | single ownership | each determination has one owning locus; other loci refer or refine with a mapping | two loci decide the same question without one deferring |
| E20 | single result algebra | one core; every refinement maps each value to one core value with its predicate; not performed stays distinct from undecidable; unknown effects never become none; availability, assessment and acceptance separate; conjunction defined once | a member defines its own outcome set without a mapping |
| E21 | pillars | each of the ten pillar contributions governs deciding rules and consumers | pillars are named but govern nothing identifiable |
| E22 | ownership and use | the Spec Method and profiles apply the shared contracts where an actor enters, not only by cross-reference | the shared contract is cited in an introduction while the procedure decides on its own |
| E23 | categorical | three accounts across the tiers; mappings state what they preserve; categorical claims meet the demonstration standard or are labelled hypotheses | categorical language is used as established without the demonstration |
| E24 | build-tenant binding | the Spec Method states the binding of the requirements calculus to a computational calculus and an execution environment, human processes included; author, actor and operation kind distinct | the binding is a software-stack assumption or absent |
| E25 | a_c interpretation | the interpretation distinguishes premise, consequence, policy choice, observation and unresolved claim, binds its source and basis, and yields task constraint surfaces for its declared scope | the interpretation is a label index, or claims coverage or fidelity it does not show |
| E26 | self-application | the categorical construction sequence is defined as this project's strategy, with the steel thread contract, not activated without the owner | the steel thread is claimed run, or the sequence is method law for consumers |
| E27 | ordinary entry | an actor entering at the README reaches the owner for common tasks and decides them without reconciling rival rules | entry needs search or reconciliation of several deciders |
| E28 | precision | rules are decision-complete for their cases: triggers, exceptions, failure outcomes | rules are aspirational prose that leave the case undecided |
| E29 | conservation | predecessor obligations, scope, force, triggers and exceptions survive or are replaced by a recorded relation | an obligation is weakened or dropped without a relation |
| E30 | no needless additions | each new obligation states its purpose and material relation; no needless change to carriers or process | new process or carriers without a stated need |

## Tests

1. **Retention map (mechanical, by the reviewer).** For every successor member, the share of sections whose body is byte-identical to an rc.2 section; the same figure for the Claude candidate, so the number has a reference. A map of where to read, not a verdict (E16, E18).
2. **Standalone and single algebra (mechanical).** rc.2 links that carry deciding meaning rather than provenance; outcome vocabularies defined outside the core without a mapping (E15, E20).
3. **Rival deciders (one fresh-context reader).** About eight shared questions taken from the common conformance discriminators, for each the loci in the candidate that decide it and whether they defer to one owner (E18, E19, E22).
4. **Scenario walkthroughs (one fresh-context reader).** Four universal-construction and assurance scenarios from the common conformance README, entered at the candidate's README and followed by route only, plus one from a candidate frame; graded against the README's expected distinctions, which neither tenant wrote (E1 to E14, E27, E28).
5. **Reuse of the blind reads.** Tests 1 (owner texts) and 2 (28 conservation claims) read `1e4bed6`; they are carried forward only for sections the diff to `d1b3348` leaves unchanged (E8 to E11, E29).

Budget: two or three subagent activations, one at a time, about 0.5 to 0.7M
tokens in all. Result: one post on `main`, verdict per intent area with
quotes, and the overall verdict on whether the product is met. No
acceptance follows; the choice is the product owner's.
