# C3-SYNTHESIS Expectations

Status: commentary, not specification or design. An independent Reviewer activation (R0) wrote this oracle without inspecting the candidate. Sources read: `specification/` (INTENT, PRODUCT, requirements/README, PRINCIPLES, A_C_DEPENDENCY, conformance/README, headers of PREDECESSOR_CLAIMS and CAPABILITIES) and installed UP-015, RF-001–017, AC-007, AC-017, AC-018. Not read: any candidate, comment or ticket, or the categorical groundwork strategy (under comments).

## Use

Sources: R `requirements/README.md`; P `PRODUCT.md`; C `conformance/README.md`; I `INTENT.md`; AD `requirements/A_C_DEPENDENCY.md`. R defines determination, owning locus, material family and refinement.

Terms:

- Point of use: the step where an actor applies a contract, such as the step that returns a review result. An explanatory cross-reference is not a point of use.
- Core value: a value of the candidate's core result algebra.

Tiers: F Foundations, SM Spec Method, Pf profiles, G guides, Pk packaging, n.s. none stated. Assigned only from P's tier table, R §Single Ownership 2 and P §Construction And Context Management.

Rules:

- Judge meaning. The tenant owns organisation, headings, member split and value spelling, including whether it uses RF-012's names or the builder's work-result names.
- [record] means the evidence is an activation or review record.
- Each expectation returns `satisfied`, `falsified` with a cited counterexample, `indeterminate`, or `not applicable` with a bounded reason.
- Find: the satisfying evidence. Fails: the falsifiers.

## 1. Standalone Successor (R §Standalone Successor Requirement)

- E-1-1 [R 1; I; F] Find: the foundational premises are identifiable, and each principle states its standing. Fails: premises cannot be told apart from derived rules; a choice is labelled derived.
- E-1-2 [R 1] Find: each material family names its premises, its consequences, and its domain or policy choices with their owners. Fails: a rule traces to no premise; a choice has no owner; a consequence does not follow from the premises it cites.
- E-1-3 [R 1] Find: every member is traced, or stated to have no material family, with a reason. Fails: a few traced members are presented as deriving all members; a member is silently missing.
- E-1-4 [R 2; SM, Pf] Find: at each point of use, SM and Pf apply F's frame, result, authority and evidence contracts in F's terms. Fails: a "see Foundations" preamble is the only link; a definition conflicts with F.
- E-1-5 [R 3] Find: owned text supplies every conserved determination needed for use. Fails: a determination is carried only by an `stdo://` link, "as in the predecessor" or an unowned compression; the predecessor applies where the candidate is silent.
- E-1-6 [R last ¶] Find: unchanged text, where used, carries relationships 1 and 2. Fails: the share of text rewritten is cited as evidence; copied text is said to rest on the axioms merely because it is present. A review that rejects text only because it is unchanged is itself defective.
- E-1-7 [P §Product Boundary] Find: every step works without the predecessor. Fails: applying a step requires reading a predecessor member.

## 2. Bounded Transitions And Reference Frames (R §Bounded Transitions; P §Construction And Context Management)

F owns frames, bounded activation, work state, evidence and authority. Pf and the tenants own concrete configurations.

- E-2-1 [R 1] Find: state, destination constraints and transition obligations are bound; destination changes go through their owner; completion needs evidence; a stop keeps its outcome open. Fails: completion is inferred from an empty list or a count; a stop discards its open outcome.
- E-2-2 [R 2; RF-003/004/014] Find: the frame fits the actor's capability, holds the contract and sufficient material (directly or by declared input) and excludes the irrelevant; overload leads to refinement, another actor or a stop. Fails: a material obligation may be dropped or summarised away to make the frame fit.
- E-2-3 [R 3] Find: fit and attention are evaluated separately. Size measures only size; adequacy comes from actual use. Resource limits belong to the binding. Fails: a byte or token threshold establishes adequacy; a universal attention score is defined.
- E-2-4 [R 4; RF-009] Find: allocation is derived from operations, dependencies, capabilities and assurance. It is explained with its resource limits and failure assumptions. Fails: F or SM requires a fixed role set, an Executive, a hierarchy or a sequence for all work; a profile's named arrangement is unexplained.
- E-2-5 [R 4; RF-009] Find: decomposition, communication, authority and evaluation dependency stay distinct. Reconfiguration keeps dependencies, obligations, effects, authority and independence. Fails: authority follows position in the decomposition; reassignment drops an obligation or an effect of uncertain completion.
- E-2-6 [R 4; RF-006] Find: naming or selecting a frame grants nothing. An activation binds its subject, result, capability and admitted authority. Fails: a role name is given as the source of a grant.
- E-2-7 [R 4] Find: independence rests on authorship and evidence conditions; shared sources are allowed. Fails: an author reviewing in a fresh context counts as independent.
- E-2-8 [R 5] Find: work resumes from the current state keeping valid work; observations invalidate only affected claims; unknown effects are resolved before dependent action; handoffs use closed results. Fails: progress is discarded; full replay is mandated; a handoff relies on a prior actor's memory.
- E-2-9 [R purpose] Find: the configuration is recorded in the existing design, frame and work records. Fails: a new mandatory configuration carrier is introduced without its purpose and material relation.

## 3. Build-Tenant Binding (R §Build-Tenant Binding Requirement; P §Build-Tenant Binding). Tier: SM

- E-3-1 [R opening] Find: SM owns the relation between a common WHAT and its tenant realisations. Fails: the relation is absent from SM, appears only in Pf, G or Pk, or has two owners.
- E-3-2 [R opening, 1] Find: the Spec Method applies the relation in governing realisation. Tenants declare their calculus and execution binding in their existing design and realisation surfaces. Fails: the definition is unused; a new carrier is added. See A1.
- E-3-3 [R 2; P §Source Project Construction] Find: a stack, human process or mix, chosen within the requirements and any required human decision; author, actor and operation kind distinct. Fails: authorship selects the environment; an operation counts as human adjudication only because a person performs it.
- E-3-4 [R 3] Find: the binding names its material operations, laws, effects, resource measures and assumptions, with units and boundaries where needed. Fails: a resource claim lacks a unit or a boundary.
- E-3-5 [R 4] Find: the evidence covers meaning, constraints, authority, independence, failure and recovery. Categorical claims meet §6. Fails: an obligation is weakened for convenience.
- E-3-6 [R 5–6] Find: a calculus may be reused wherever its laws hold. a_c does not select the executor. Fails: a separate calculus is required for each language or team; a_c validation is cited as execution evidence.

## 4. Single Ownership (R §Single Ownership Requirement)

Method: sample recurring determinations (core values, conjunction, UP-015 dispositions, independence, the frame contract, change classes, grants), and locate every locus that decides each one.

| ID | Source | Find | Fails |
|---|---|---|---|
| E-4-1 | R 1 | one owning locus per determination | two sections define one rule and neither refers to the other |
| E-4-2 | R 2 | each owner sits in the tier R 2 assigns | a profile owns a generic rule; packaging is the only decider (see A4) |
| E-4-3 | R 3 | other loci refer to the owner, or name it and map each value back | a refinement has no owner or mapping; a locus contradicts or redefines the owner |
| E-4-4 | R 4 | each frame copy names its owner and matches it | a copy differs from its owner or names none |
| E-4-5 | R 5 | restated text owns its determination | a predecessor member is named as owner |
| E-4-6 | R 7 | one locus is made owner | a precedence rule between loci stands in for an owner |

## 5. Single Result Algebra (R §Single Result Algebra Requirement; P §Result Algebra)

F owns the core. A refinement belongs to its member or profile.

| ID | Source | Find | Fails |
|---|---|---|---|
| E-5-1 | R 1 | one core in F, with its values, their meanings and its combination rules | two core value sets exist; the core is outside F |
| E-5-2 | R 1; P | constraint checks, judgements, frame evaluations, stops, work steps and effects each sit in the core or in a mapped refinement | any of the six has an unmapped outcome set |
| E-5-3 | R 2 | each refined value maps to exactly one core value | a value maps to two values, to "depends", or to none |
| E-5-4 | R 3 | no mapping raises a result's standing | failure maps to success; undecided maps to satisfied; "not performed" merges with undecidable; an unknown effect maps to "none" or "completed" (see A2) |
| E-5-5 | R 4 | the core value travels with its predicate and domain outcome | a record keeps only the core value; a mapping redefines the domain outcome |
| E-5-6 | R 5 | availability, assessment and acceptance are separate results | "produced" maps to fitness; acceptance is inferred from a successful step |
| E-5-7 | R 6; purpose ¶ | conjunction and composition are defined once over the core and keep failure, undecidability, non-performance and uncertain effects distinct after combination | a member defines its own combination rule; a combination erases these distinctions |
| E-5-8 | R 7 | each result-returning frame carries the core or its profile mapping | such a frame carries neither |
| E-5-9 | R source; PRINCIPLES §C1 Disposition | RF-012 and AC-007 outcomes are both disposed into one algebra | either survives as a parallel algebra |

## 6. Categorical Demonstration Standard (R §Categorical Demonstration Standard; P §Categorical Construction). Tier: n.s. (A5)

- E-6-1 [R opening; I §Direction] Find: each category, functor, join, equivalence or preservation claim carries items 1–5 as they apply, or is marked a hypothesis. Fails: "the refinement chain is a category" is stated without objects, arrows, arrow equality, identities and associative composition.
- E-6-2 [R 2] Find: each layer states and discharges what it preserves. Approximate steps give an adequacy relation and an end-to-end bound. Fails: per-step tolerances are presented as an end-to-end bound.
- E-6-3 [R 3] Find: each step is licensed by a declared law, or with no law, only universally valid steps are used. Fails: a partition or reassociation is used with no licensing law.
- E-6-4 [R 4] Find: maps are defined on objects and arrows. Functor laws are shown before a map is called a functor. Conformance, equivalence and functorial preservation are kept distinct. Fails: conformance is presented as equivalence.
- E-6-5 [R 5; AD] Find: a_c keeps premises, consequences and choices apart. The calculus, interpretation and carriers keep separate identities. Each claim names its evidence class. Fails: a claim names no evidence class; a checker pass is cited as truth.
- E-6-6 [R 6; P §Categorical Construction, §Open Owner Decisions] Find: the categorical capability and the worked join are presented as established only with the item-6 join of one algorithm category with one computation category, after the owner has selected the capability's acceptance contract. Fails: either is presented as established without that join or before that selection.
- E-6-7 [P §Product Boundary, §Categorical Construction] Find: the three accounts are independent of tiers; the reference design's layers are not rules; sheaf account, universal grade algebra and second-domain generality stay unresolved. Fails: a tier is defined as an account; any of these is stated as law.

## 7. Conformance Discriminators (C, row order; acceptance criterion 5)

Find: a logical review constructs each row's case against the member text, and the text yields the distinction C expects.

| ID | Case | Fails if | Tier |
|---|---|---|---|
| E-7-1 | a derivation or independence is claimed | premises or argument absent | n.s. |
| E-7-2 | information vs representation | a matching map or schema is cited as the same meaning | n.s. |
| E-7-3 | same identity, new content | an unchanged identifier is read as unchanged content | n.s. |
| E-7-4 | typed producer and consumer disagree | a join is accepted on matching names or shapes | n.s. |
| E-7-5 | A failed, B uncovered | A's failure is lost; B is reported satisfied or as an omitted planned judgement; a judgement is unauthenticated | n.s. |
| E-7-6 | misbound planned judgement | accepted because it was planned | n.s. |
| E-7-7 | context exceeds one actor | a split severs a dependency; silent truncation | F |
| E-7-8 | byte-fit frame hides a dependency | accepted because it fits | F |
| E-7-9 | author reviews in a fresh context | counted as independent | n.s. |
| E-7-10 | frame omits frontier items | out-of-view items are treated as closed | n.s. |
| E-7-11 | discovery; destination revised to pass | progress is counted; the original destination is treated as reached | n.s. |
| E-7-12 | direct task fits one frame | generic text requires a coordinator or a sequence | F/Pf |
| E-7-13 | no Executive; unfamiliar roles | judged by labels or topology | F/Pf |
| E-7-14 | redistribution with uncertain effects | self-organisation exempts it from a condition | F/Pf |
| E-7-15 | "optimal" arrangement | rests on familiarity, persistence or self-organisation | F/Pf |
| E-7-16 | compact result omits a blocker | missing information is assumed favourable | n.s. |
| E-7-17 | dependency invalidates a claim | reuse rests on an unchanged hash alone; all work is discarded | n.s. |
| E-7-18 | rules without context or authority | a rules-only packet is treated as activation-ready | F |
| E-7-19 | interrupted partial work | progress is erased; an unrun assessment is recorded | n.s. |
| E-7-20 | parse or map succeeds | cited as semantic acceptance | n.s. |
| E-7-21 | carrier or process change made law | new record, step or carrier with no stated purpose | SM |
| E-7-22 | software, human or mixed realisation | the kind of executor decides | SM |
| E-7-23 | assessments merged or a human decision automated | justified by speed, cost or matching output | SM |
| E-7-24 | one calculus across environments or operations | a calculus is required per stack; identity grants authority | SM |
| E-7-25 | a_c model of a human process validates | cited as conformance | SM |
| E-7-26 | two loci decide one question | E-4-1, E-4-3, E-4-4 or E-4-6 fails | n.s. |
| E-7-27 | a member defines result values | E-5-3, E-5-4 or E-5-5 fails | F |
| E-7-28 | a frame task returns a result | E-5-8 fails | F/Pf |
| E-7-29 | a functor or join is claimed | E-6-1 or E-6-4 fails | n.s. |
| E-7-30 | a rewrite or refinement is applied | E-6-2 or E-6-3 fails | n.s. |

## 8. Tier Obligations And Acceptance Criteria (P §C3 Construction Contract)

- E-8-1 [Outcome] Find: the axioms, with every member restated on them; for each PREDECESSOR_CLAIMS row, one disposition and one successor locus; frames assembled from the candidate. Fails: any of these is missing.
- E-8-2 [Frontier] Find: a member list, and a map from each predecessor member to the tenant members that receive it. Fails: a predecessor member is unmapped.
- E-8-3 [tier table: F, SM, G] Find: each row's "Owes" items are present and owned in that tier, and its "Receives" members are disposed into it. Fails: an F item (ontology, standing, result algebra, frames, bounded activation, work state, evidence, authority) is missing or owned elsewhere; an SM item is missing or owned only by a profile; a guide owns a method determination.
- E-8-4 [tier table: Pf] Find: each profile imports the tiers above it and restates its whole predecessor member: ODD, TRAVERSAL_OCCURRENCE, UX, WORLD_MODEL, the DESIGN_MODULE realisation law, and the baseline's frame catalogues and Executive law. Fails: a profile restates part of its member and links to the rest; Executive law sits in F or SM.
- E-8-5 [tier table: Pk; P §Open Owner Decisions] Find: the manifest, schemas, templates, compressions, bootstrap and plugin have dispositions. They may stay `unresolved` until a release-candidate cut. Fails: release-candidate readiness is claimed while these are unresolved; the fate of the compressions is stated as decided without the owner.
- E-8-6 [AC1] Find: each cone row has one disposition. Each `conserved` or `superseded` row has a locus that resolves. Fails: a row has two dispositions; `reframed` is used as a disposition; a locus does not resolve.
- E-8-7 [AC2; record] Find: a reviewer who is not the author compares the source and finds each conserved meaning in the candidate's own text. Fails: a link, matching label or lossy paraphrase is accepted; the author made the comparison.
- E-8-8 [AC3] Find: `superseded` names its accepted relation; `intentionally removed` names the owner's decision and reason; `not applicable` gives a bounded reason. Fails: a removal has no owner decision; a reason has no bounds.
- E-8-9 [AC4; Limits; record] Find: each selected task has a frame within declared limits, bytes measured before reading; a fresh actor given only frame and subject applies it correctly, judged against author-independent expectations. Fails: byte fit is cited as adequacy; the author wrote the expectations; no measured activation is recorded.
- E-8-10 [AC5] Find: each member has a logical review against all 30 rows of §7. Fails: a row passes on a mechanical check alone, or is skipped without a bounded reason.
- E-8-11 [AC6] Find: each new obligation names its purpose and material relation. Fails: a new record, step or carrier has no stated purpose; a carrier changes without need.
- E-8-12 [Activation unit] Find: frames come from a_c projections or a declared equivalent. They keep their dependencies and acquisition routes. Fails: a frame has no declared generation route.
- E-8-13 [Independence; record] Find: each review names its Reviewer and its author. A same-family review is declared with a reason and marked as such. Fails: the Reviewer authored the subject; a same-family review is undeclared.

## Negative Expectations

A conforming candidate does not:

- N-1 present a categorical claim as established without its demonstration (E-6-1);
- N-2 define a profile result value with no core mapping, or map a value upward (E-5-3, E-5-4);
- N-3 prescribe a fixed role inventory, hierarchy or sequence as generic method; Executive, Writer and Reviewer are one configuration under the installed builder (P §Construction Authority; E-2-4);
- N-4 treat size as evidence of adequate attention (E-2-3);
- N-5 let a predecessor link stand in for conservation (E-1-5);
- N-6 present a premise or choice as derived, or a partial demonstration as deriving all members (E-1-1, E-1-3);
- N-7 map production of a candidate to its fitness or acceptance (E-5-6);
- N-8 derive authority from a role, frame, identity or capability (E-2-6);
- N-9 cite a parse, map or a_c check as semantic acceptance (AD §Proof Claims);
- N-10 settle an open owner decision (P §Open Owner Decisions);
- N-11 use a precedence rule in place of an owner (E-4-6);
- N-12 present its a_c output as the released STDO Representation (AD).

## Ported Parts

A ported part is text copied from the Codex candidate (P §Development Isolation, §Cross-Synthesis). Each fails if:

- PT-1 its source is not the peer candidate at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, is a working tree, or is unrecorded;
- PT-2 it is not a named contribution in one member's cone whose record gives source location, single owning section in this line and supported disposition;
- PT-3 two owners remain; it must take one owning locus, and any earlier decider refers to it or refines it (R §Single Ownership 6);
- PT-4 a rule moved unchanged is not `conserved`, or `superseded` lacks an accepted replacement relation;
- PT-5 the Reviewer does not compare it with both its peer source and the predecessor; fidelity to the peer is not conservation;
- PT-6 its result values do not map into this line's core, or the peer's value names arrive as a parallel set;
- PT-7 a link to `build_tenants/codex/` remains, or a determination or term resolves only in the peer (R §Single Ownership 1; §Standalone Successor 3);
- PT-8 it is written outside `build_tenants/claude/`;
- PT-9 its cone is accepted before the owner decides how ported parts are reviewed, or it is reviewed by its source author's model family without that ruling (P §Open Owner Decisions);
- PT-10 it is exempted from §§1–7, or its standing in the peer line is counted here (P §Dependencies And Acceptance).

## Ambiguities Recorded

- **A1. "States and applies"** (R §Build-Tenant Binding; P §Source Project Construction "applying"). (a) The Spec Method states the relation and uses it to govern realisation; (b) the candidate also declares its own calculus, binding and evidence. R supports (a); E-3-2 tests (a). Record whether (b) is present; its absence fails only on an owner ruling.
- **A2. Distinct outcomes.** R 3 keeps non-performance, undecidability and unknown effect distinct: (a) by separate core values, or (b) by the domain outcome carried with a shared core value. Either way the distinction must survive combination (E-5-7).
- **A3. Dispositions.** P's six result kinds omit UP-015 dispositions and coordinator dispositions. These may map into the core or lie outside it. Record the candidate's reading.
- **A4. Packaging.** R makes a list of allowed values a determination, yet packaging owns no determination. A schema's value list is then either a copy that names its owner, or forbidden. R 4 covers only frame copies.
- **A5. Categorical tier.** No tier is named for the Categorical Demonstration Standard. P calls it "a general capability", so it may belong to F or SM.
- **A6. Applicability.** "As far as they apply" is a judgement, and P itself calls documents "objects". E-6-1 treats asserted composition, identity or functoriality as a claim; descriptive use labelled as direction passes.
- **A7. Materiality.** R §Standalone Successor 1 does not say who judges a family material, or what form the accounting takes.
- **A8. Unnominated parts.** P §Cross-Synthesis calls the nominated parts "proposed" and says the Executive "selects" them. Record a port from outside those reviews here rather than failing it; PT-1 to PT-10 still apply.
