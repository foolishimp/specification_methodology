# C3 Iteration 3 Expectations (Independent Oracle, R0i3)

Commentary-class oracle for an iteration 3 reconstruction, written from the common specification and installed predecessor only. No tenant candidate, tenant ticket, `build_tenants/` content or `.ai-workspace/comments/` post was opened. It is tenant-neutral. Standings are named by kind (satisfied, failed, undecidable, not performed, unknown effect completion); each candidate owns its labels. It grants no acceptance.

## 1. Basis

- Common specification: `main` at `1317e4311cc00dd74112de20b7acda1c95e97f45`. The bytes were read with `git show main:specification_methodology/v3/specification/<path>`. The coordination checkout's working tree has uncommitted edits to GOALS, PRODUCT, `conformance/README` and `requirements/README`, so working-tree hashes will not match these.
- Previous basis for the delta: `a7eba6665f13bb4557560a54a04d8b9d51fcc7d2` ("Freeze common inputs for Codex cross-synthesis rebuild").

| Common file (at `main`) | SHA-256 |
|---|---|
| `INTENT.md` | `d813239dca237b37ffcb79f672ccb383e2acfc9eb804aaa7e0674fbc82d557c1` |
| `GOALS.md` | `776ecffffeb9d42a03d438eac55ba1eddef62bacc1c3e33cf77f9c410b1b7aff` |
| `PRODUCT.md` | `3d75f6e7f043cfc791b98aef1c0cb3105ef7f32b35425731efbb56a3bdddd663` |
| `REFERENCE_FRAME_BASIS.md` | `473175924e066a6af91e7469d9884b7a750e6c43ab6aed9406db85075b3cf097` |
| `conformance/README.md` | `65301ddf829a7eb8c1794b6d2457a387d7bb0d04e362d2d5305fd79b9f5219a9` |
| `requirements/README.md` | `966c1a5955de78dba7199d311db0952b3732a0cd3385555a600a180411a317cc` |
| `requirements/CAPABILITIES.md` | `49f2b455510459027ddbda997baf8055d8772763196667047d87e700282e3edd` |
| `requirements/A_C_DEPENDENCY.md` | `75b98c363ac6026018a4e74ba8b23364bc8d31ef3897a6d58a05a7fbed91297f` |
| `requirements/PRINCIPLES.md` | `009fca60d81e71586d9b3faf3f5cd932f902125fdfe8816c3d3b00cf15552fc7` |
| `requirements/PREDECESSOR_CLAIMS.md` (header, rules and member table only) | `fbeb8fd2eda0af32873c287130457fc3800d44987da3b6675a00c8b4333c2f69` |

- Installed predecessor `stdo://releases/v2.5.1-rc.2/`: `manifest.json` SHA-256 `3d860ff4…2ff2782` matches PRODUCT. The eleven cited members (AXIOMATIC_CALCULUS, REFERENCE_FRAME_METHOD, SPEC_METHOD, STDO_REFERENCE_FRAME_BASELINE, WORLD_MODEL, IDENTITY, DESIGN_MODULE, ODD, TRAVERSAL_OCCURRENCE, TICKET, RELEASE) were hashed locally; each matches the PREDECESSOR_CLAIMS member table.

Sources: P = PRODUCT, R = requirements/README, FR = Foundational Reduction Requirement, CS = Constraint Surfaces requirement, CR = conformance/README, RFB = REFERENCE_FRAME_BASIS, AC = A_C_DEPENDENCY. Tier (T) is given only where the C3 tier table, Method Structure or Single Ownership states it; no T means none is stated.

## 2. Expectations

### 2.1 Pillars (P §Foundational Reduction; FR-1)

Pillars are related accounts, not a document list, sequence or independent axioms; evidence maps each pillar to the deciding rules and consumers it governs, in existing design and proof surfaces.

- **PL-1 Specification and project structure.** E: one owner each for purpose and destination constraints, the Intent→Product→Specification→Realisation chain, and refinement from the common WHAT to independent HOW realisations. Specification, design, work records and commentary are distinguished by standing, and project layout is shown to express those relations rather than found them. F: commentary or posts can acquire law standing; or a folder layout is stated as a foundational premise with no relation that it expresses. T: Spec Method for the chain and work carriers; guides for posting.
- **PL-2 World models, identity and Markov objects.** E: objects, boundaries, state and material relations with the evidence supporting each boundary; bounded modelling and state-sufficiency are separate claims. The predecessor's candidate standing of the Markov construct is conserved or validly disposed, including the unmet promotion gate that "must not be relocated" (WORLD_MODEL §Epistemic Status Of The Construct), and an entity cut stays lawful without an identity direction. F: any object is called Markov, or its state sufficient, on boundary or interface grounds alone; or the gate is restated as met, moved or silently dropped. T: identity to foundations (ontology; IDENTITY_METHOD); world modelling to profiles. See AM-8.
- **PL-3 Functional design and algebra.** E: one owner for typed operation and composition law, invariant preservation, explicit failure (the predecessor's DESIGN_MODULE §8 Totality) and effect boundaries. Profiles reusing a transformation bind it without copying machinery or merging identity, authority or evidence. F: two consumers each define their own composition or failure-propagation rule; or one shared transformation is used to equate the identities or authority of two domains. T: composition in foundations; DESIGN_MODULE generic law in Spec Method; realisation law in profiles.
- **PL-4 Outcome-driven development.** E: typed transitions toward a selected outcome, with evaluation, continuation, recovery and termination outcomes, and with operation kind, actor and execution mechanism kept distinct. Runtime-specific bindings (ABG continuation, ODD §11.5A) stay in the profile, because runtimes are outside the product (P §Product Boundary). F: continuation without a termination or recovery outcome; an operation's kind inferred from who performed it; or ABG or HoG mechanics stated as generic law. T: profiles (ODD); work state and results in foundations.
- **PL-5 Information and interpretation.** E: subject, representation and meaning are distinct; every projection, translation or compression declares the distinctions it preserves for its consumer. F: structural agreement accepted as identical meaning; or a projection with no declared preserved distinctions. T: foundations.
- **PL-6 Reference frames.** E: the frame is first-class; acquisition is task-sufficient under finite context and attention; results are closed; allocation of work, information and authority is justified, not a fixed role inventory; frames are the unit every actor starts on (P §C3 Outcome). F: Executive, Worker and Reviewer are stated as foundational necessities; or a frame is accepted on byte fit alone. T: foundations; frame catalogues and Executive law in profiles.
- **PL-7 Computational realisation.** E: a binding of operations and their laws to human, machine or mixed execution, stating effects, resources, assumptions and measured costs with units and boundaries (R §Build-Tenant Binding 1–6). F: the binding only names a stack; a human process is excluded or treated as non-conforming by kind; or a cost or optimality claim has no measurement boundary. T: Spec Method.
- **PL-8 Evidence, correction and authority.** E: claim, observation, judgement and acceptance have distinct standing; changes are counterexample-driven and traced to the section owning the cause (P §Categorical Construction step 3); permission and ownership never derive from capability or a passing check. F: a passing check, a reviewer result or reachability confers acceptance or an operation grant; or a repair lands at the symptom without attributing the cause. T: foundations for evidence and authority law; Spec Method for change classes and re-entry.
- **PL-9 Axiomatic calculus.** E: an explicit, recoverable a_c representation of constraints, dependencies, permitted latitude and residual uncertainty. At least one task's constraint surface is shown to be constructed from it (see CS-*). F: a_c appears only as a named calculus, a correspondence table or a schema-valid file from which no task surface is derived. T: foundations receive AXIOMATIC_CALCULUS; the interpretation is cross-tier (P §Method Structure).

### 2.2 Reduction Requirement (R §Foundational Reduction Requirement 1–6)

- **FR-1 Pillar contribution with standing.** E: for each pillar, the deciding rules and the consumers it governs, with each rule's standing marked as foundational premise, derived consequence, domain policy or implementation choice. F: a pillar is related to the method only by correspondence ("ODD corresponds to functional design") with no deciding rule and no consumer named.
- **FR-2 Recurring determinations and shared owners.** A recurring determination is one question (what result standing, what confers authority, what establishes identity) decided at two or more loci in the predecessor or the candidate, each deciding it independently. E: each recurring determination has one shared owner. Every affected consumer either applies the owner's law or states a refinement that maps each of its values or cases back to the owner (R §Single Ownership 3). As a minimum, cluster RD-1 below is contracted, because the specification names it (R §Single Result Algebra). For RD-2 to RD-5, the candidate either contracts each cluster or states why it stays separate; silence is an undecidable finding, not automatic falsification. RD-6 to RD-8 were identified from headings only and serve as prompts. F: any consumer keeps its own outcome list with no mapping to the core, or keeps its own authority-conservation clause decided independently of the shared owner.

| Cluster | Predecessor loci | Shared question |
|---|---|---|
| RD-1 results | RF-012; AC-007; Baseline §Work result (an explicit mapping to RF-012); TRAVERSAL_OCCURRENCE §Closed … Stop Kinds (partly read) | the outcome standing of an evaluation or step |
| RD-2 authority conservation | RF-006; AC-005; IDENTITY §Authority Identity And Conservation (UP-004) | what does and does not carry or widen authority |
| RD-3 standing separation | RF-007; SPEC UP-008; AC-014; AC-018 | the difference between semantic law, evidence, judgement and projection |
| RD-4 identity | AC-002 (type, context, owner, scope, basis); IDENTITY §1 (authority + kind + value); RF-008 | what establishes the same identity; the two coordinate sets differ |
| RD-5 exact basis | RF-005; AC-006 | how a result binds its basis, and how staleness is handled |
| RD-6 projection and compression | AC-011, RF-017, UP-008 (read); SPEC §Projection Discipline, ODD §11.5C, WORLD_MODEL §Projection Law (headings) | what a view may omit |
| RD-7 composition | AC-016, WORLD_MODEL §Composition Law, DESIGN_MODULE §Atomic Functions…, RF §Material Composition (headings) | when two parts compose |
| RD-8 continuation and totality | DESIGN_MODULE §8 and ODD §11.5A (read); SPEC §Checkpoint, Continuation…, RELEASE §Qualification And Recovery (headings) | handling of failure, interruption and continuation |

Ticket status is work state and UP-020 dispositions are decisions; neither is a rival result algebra.

- **FR-3 Retained primitive with stated need.** E: every remaining independent mechanism or policy (an RF-017-style intentional overlap, a profile-only primitive) names the distinction it supplies and why shared contracts do not decide it, in an existing design or proof surface. F: an independent mechanism is retained with no stated distinction; or a per-helper justification record, new work carrier or process step is created. Contraction evidence in an existing qualification or proof surface conforms.
- **FR-4 Responsibility-based member boundaries.** E: a member map from every predecessor member to the successor owners that receive its content, with many-to-one and one-to-many mappings allowed (P §C3 disposition grant). Consumers carry their bindings and do not repeat the common law. F: a one-to-one file mirror in which each successor member restates its predecessor's own version of a shared law; or a profile copies a foundational law as a second authority.
- **FR-5 Contraction on deciding paths.** E: for named deciding paths (at minimum the standing of a combined result, plus at least one path from RD-2 to RD-5), the evidence lists the loci consulted, the rival rules, the exceptions and the cross-document reconciliations in three subjects: the predecessor, the preceding candidate (AM-1) and this candidate. It separates semantic conservation, demonstrated reduction and mere relocation (RFB §Activations). The comparison is stated in non-size terms, such as the effective-reasoning-complexity components of SPEC UP-014: independent concepts and authority surfaces, joins, exceptions, duplicated representations and states. F: a path still needs the same reconciliation but is reported as reduced; relocation is labelled reduction; or the only evidence is counts, a diagram or a checker pass. Dropping UP-014 without a disposition is a separate finding.
- **FR-6 Independent challenge cases.** E: successful, refused and unresolved cases covering cross-domain composition, failure preservation and recovery, specified independently of the author (§2.6 supplies a set). The evidence discloses the compared subjects, tasks, acquisition conditions and limits, and claims stay within the covered relations. F: only success cases; cases written after the results; or a generalisation from a few cases to "the method reduces".

### 2.3 Fourth Relationship: Reduction (R §Standalone Successor 4; P §Product Boundary; C3 criterion 6)

- **SS-4.** E: all four relationships, including reduction, are claimed and evidenced, and criterion 6 is evaluated per member. Unchanged predecessor text is used only at the shared owner its consumers apply. F: assessment under the earlier three-relationship reading; the share of rewritten text, retained layout or an added explanatory layer cited as evidence (P §Product Boundary); or unchanged text kept at several consumers that each still decide the question.

### 2.4 Constraint Surfaces (R §Constraint Surfaces 1–7)

- **CS-1 Surface content.** E: for each published frame task, the surface states the objects and meanings, predicates and dependencies, admissible operations, required results, authority, evidence and explicit unresolved conditions. It prescribes no internal solution strategy (conserving SPEC UP-014's procedure clause). F: a surface lacks authority or unresolved conditions; or it mandates one decomposition where variation affects no governed property.
- **CS-2 a_c interpretation from owning prose.** E: a_c records trace to owning prose and are typed premise, derived consequence, policy choice, observation or unresolved claim; shared premises and revisable relations are allowed. F: an observation encoded as a premise; an unresolved claim encoded as a fact; or a tree-only or execution-ordered encoding imposed as a requirement. T: cross-tier.
- **CS-3 Resolution to source and basis.** E: each represented determination resolves to its current owning locus and basis, with its dependencies, exceptions, latitude (AC-008) and failure or uncertainty outcomes recoverable (AC-009: absence is not resolution). F: a model resolves to a predecessor locus or a superseded candidate locus; or a missing premise lets a dependent action pass instead of taking its declared result or recovery route.
- **CS-4 Task projection.** E: a projection carries sufficient constraints plus the material inputs or acquisition routes for its task. The workspace and authoritative inputs stay the basis for reacquisition. F: a frame is a rule packet with no subject, evidence route or effect grant (CR row "task packet").
- **CS-5 Fidelity across prose, model and view.** E: source-to-representation comparisons show the same permitted and required work; an approximation declares its adequacy relation and end-to-end bound and leaves authority and permission exact. F: a view admits or forbids work that the prose does not; or an approximation coarsens a permission distinction.
- **CS-6 Current entry; historical marking; fidelity cases.** E: the ordinary entry (AM-5) binds the current exact source, signature, program, maps, digests and evidence boundary. Earlier models (iteration 2 models, the 2.5.1-rc.2 STDO Representation map) are labelled historical. Fidelity evidence uses independently specified permissible, prohibited and unresolved cases and a source-first review that states uncovered scope. F: the entry resolves to an older or peer model as current; or fidelity cases are author-written only.
- **CS-7 Evidence classes.** E: every claim names its class: mechanical, mathematical argument, semantic judgement, actual use or unresolved. "Mechanical" is used only for an evaluation that was actually selected and run against a verified installed checker (AC §Directed Mechanical Dependency). F: structural validity is offered as semantic fidelity or decidability; or a mechanical class is claimed while no installed copy or evaluation is selected.

### 2.5 Conformance Rows Added Since `a7eba66` (CR; criterion 5)

- **CF-1 Foundations introduction with rival consumer rules.** E: the deciding consumers use the shared determination or a refinement that maps back to it. F: a new foundations section exists while, for example, a frame profile keeps its own closed-result list unmapped.
- **CF-2 One shared law for several clauses.** E: each absorbed predecessor obligation and its consuming bindings are checked one by one. F: a bare link stands in for a dropped condition, such as a proxy-grant field from UP-004 lost in an authority consolidation.
- **CF-3 Exception deleted for size.** E: the exception keeps a valid disposition and its behaviour, or an owner removal decision is recorded. F: a rule is narrowed with no row disposition, such as the Markov promotion gate or the invalid-basis outcome.
- **CF-4 Helper promoted to public mechanism.** E: the distinction or independent boundary needing it is named. F: a named mechanism without one acquires a semantic or authority owner.
- **CF-5 Markov by small interface.** As PL-2; without stated assumptions and evidence the claim stays unresolved. F: a small interface or clean boundary cited as establishing Markov sufficiency.
- **CF-6 a_c omits a condition but passes schema.** E: judged unfaithful for every decision the condition affects. F: schema pass offered as authorising the work.
- **CF-7 Unresolved premise treated as freedom.** E: the dependency is kept and a stop, acquisition or refinement is applied. F: §2.6 case IC-5 or IC-7 resolves as permitted.
- **CF-8 Several solutions inside one surface.** E: every alternative that meets the contract is admitted. F: §2.6 case IC-6 rejects one admissible alternative for style or order.
- **CF-9 Entry to an earlier interpretation.** As CS-6; F: IC-9 admitted.

### 2.6 Independently Specified Cases (for FR-6, CS-6 and CF-7 to CF-9)

Mapping: successful = permissible and satisfied; refused = prohibited or failed; unresolved = unresolved or undecidable.

- **IC-1 (successful, cross-domain).** A world-model entity cut feeds an ODD transition with compatible types and a coherent basis. Expected: composition is admitted, the entity's identity is preserved and the source system's authority is not transferred.
- **IC-2 (unresolved, cross-domain).** The same composition, but the consuming transition requires state sufficiency and the boundary is only a Markov-overlay candidate. Expected: undecidable. A satisfied side does not raise the conjunction, and the dependent action stops, acquires or refines.
- **IC-3 (refused, failure preservation).** Assessment A fails and assessment B is satisfied, and the two are composed. Expected: the composite is not satisfied, and A's failure and citations survive.
- **IC-4 (unresolved, recovery).** A Writer is interrupted after a partial write, so effect completion is unknown. Expected: the result is mapped neither to no effect nor to completed. Resumption observes the workspace, and the dependent action waits until the effect is resolved enough to proceed.
- **IC-5 (prohibited, missing premise).** An a_c model of the Executive grant omits "no write grant". Asked "may the Executive edit the ticket?", expected: no. The source governs, and the model has a fidelity defect.
- **IC-6 (permissible, latitude).** Two member organisations both satisfy every obligation. Expected: both admissible.
- **IC-7 (unresolved, open decision).** A member containing a ported part is put up for `accept` while the ported-part review policy is open. Expected: not accepted, and the case stays unresolved.
- **IC-8 (successful, stale summary).** A retained summary says a member was accepted; the workspace disagrees. Expected: acquire, correct, keep applicable work, continue within the grant.
- **IC-9 (refused, historical entry).** The entry routes to the 2.5.1-rc.2 Representation map as the successor's interpretation. Expected: fails basis binding; not satisfied.

## 3. Negative Expectations

A conforming reconstruction must not do any of the following.

- **N-1** Offer word, byte or file counts, a diagram, rewritten prose or a structural pass as proof of reduction (FR-5; criterion 6).
- **N-2** Add a common introduction while the consumers keep rival rules (FR-2; CF-1).
- **N-3** Let an omitted premise or obligation become permission or a satisfied result (CS-3; CF-7).
- **N-4** Present a historical or peer a_c model as current (CS-6; CF-9).
- **N-5** Claim the mechanical evidence class without a selected evaluation and a verified installed checker (AC).
- **N-6** Present tenant a_c output as the released STDO Representation, or let it inherit that Product's acceptance (AC; P §Product Boundary).
- **N-7** Record `accept` without the owner-assigned independent review under that line's recorded grant, or accept a cone containing a ported part before the ported-part review decision (P §Open Owner Decisions).
- **N-8** Remove a material obligation or exception for size without an owner `intentionally removed` decision (CF-3; R §Successor Disposition).
- **N-9** Treat a link to the predecessor as conservation, or a matching label as semantic equivalence (R §Standalone Successor; criterion 2).
- **N-10** Make Markov, categorical or functor claims beyond their demonstrated scope (R §Categorical Demonstration Standard; CF-5).
- **N-11** Treat the pillars as a prescribed member list, a work sequence or independent axioms (P §Foundational Reduction; PRINCIPLES preface).
- **N-12** Let a_c or a projection confer operation or acceptance authority, or impose a tree-only encoding or an execution order (CS-2; CS-7).
- **N-13** Settle a rival-rule conflict with a precedence rule instead of an owner (R §Single Ownership 7).
- **N-14** Create a per-helper justification record, or a new work carrier or process step without need (FR-3; criterion 6).
- **N-15** Accept frames on byte fit alone, or count a fresh-context self-review as independent (criterion 4; CR).

## 4. Ambiguities (Readings, Not Resolved)

- **AM-1 Which candidate is "the preceding candidate" (FR-5).** Reading (a): the same line's iteration 2. For Codex that is the merge `a9adce2` (GOALS); for Claude it is the cross-synthesis base `31f28f9` or the accepted state `770c7f4` (PREDECESSOR_CLAIMS header), order not established here. Reading (b): the cross-synthesis base `31f28f9` for both lines. The candidate should declare its choice.
- **AM-2 Unchanged-text clause.** "Unchanged predecessor text satisfies these" now also covers relationship 4. Readings: (a) unchanged text satisfies reduction only at the single shared owner; (b) it cannot itself evidence reduction. This oracle takes (a) for text and (b) for evidence.
- **AM-3 Per-member criterion, cross-member property.** Criterion 6 is per member; reduction is cross-member. Reading: each member shows its consumer bindings; each cluster's contraction is assessed once across members.
- **AM-4 Standing categories differ by source.** CS-2 adds "observation"; FR-1 separates domain policy from implementation choice; INTENT, P §Method Structure and the Categorical Demonstration Standard item 5 list fewer. Reading: the union applies to a_c records.
- **AM-5 "Ordinary entry" is undefined.** Readings: the candidate's root README or entry document; or the frame catalogue; or the a_c index. This oracle requires all three to agree.
- **AM-6 Case authorship and "where applicable".** "Independently specified" names no specifier; this oracle is one source, not the only one. "Where applicable" (FR-6) and "where available" (FR-5) could license omission. Reading: refused and unresolved cases apply to any law with a failure outcome.
- **AM-7 Coverage of the a_c interpretation.** CS-2 says "the method's a_c interpretation", but AC binds evidence to each "selected, frozen tenant output", and no checker is selected. Reading (a): the interpretation must cover every owned determination (AC: coverage "follows the method's owned determinations"). Reading (b): it covers a selected fragment with declared uncovered scope.
- **AM-8 Tier for the Markov pillar, and plural loci.** The pillar's tier is split between foundations (identity) and profiles (world modelling). The profile tier no longer has to restate members "in full", so one claim may land in a shared owner plus a profile binding, while criterion 1 speaks of "a successor locus". Reading: plural loci are allowed if each resolves.
- **AM-9 No metric for "simpler to determine and apply".** Reading: use the components of SPEC UP-014 (a predecessor claim, itself subject to disposition) as the comparison vocabulary.
- **AM-10 Capability contracts.** P §Categorical Construction requires a selected acceptance contract per capability; CAPABILITIES now says the reconstruction "must provide" the pillar, reduction and constraint-surface capabilities. Reading: FR and CS act as those contracts; each trial's scope is set in its work contract.
- **AM-11 Frames from a_c or from an "equivalent".** Frames may come from a_c projections "or an equivalent the tenant declares" (P §Activation unit). Reading: an equivalent is admissible only with CS-5 fidelity evidence.

## Amendment 1 (6c2debb)

Same rules as above: written from the common specification and the installed predecessor only; no candidate opened.

### A1.1 Basis

New basis: `main` at `6c2debb1eb3791999f33f04f2a05061c94927b7b` ("Consolidate iteration 3 specification and review work frontier"), a descendant of `1317e43`. Read with `git show 6c2debb:…`. Changed common files:

| Common file (at `6c2debb`) | SHA-256 |
|---|---|
| `GOALS.md` | `db49984cc88edde71ee50d6a9a487d86a8ff1fe47a7ccf27f6bff558fbe5c769` |
| `PRODUCT.md` | `e9724fe4f22347cdbc0929f7988d1727f69782cbb1877f8273e5d3978ca6b440` |
| `conformance/README.md` | `515227236f145176708009e925344c4e6c4ba94d1cc66e4743acc5b73c03d445` |
| `requirements/README.md` | `a655a43a52ee2e508170695d3d9f85561f05d92fa17b5213afda385a950060a6` |

The other six files in §1 have the same SHA-256 at `6c2debb` as at `1317e43`.

### A1.2 New Expectations

- **A1-1 Family coverage includes inherited rules.** Source: R §Standalone Successor 1 (amended); CR row "family argument … omits inherited deciding rules". E: the candidate states its grouping of deciding rules into families. Each foundation-to-law argument names the material rules it covers, including rules carried unchanged from the predecessor, and gives each its premises, consequences and owned policy choices. F: an argument covers only rules edited in iteration 3; or a whole-member preamble or a coarse group ("all of the ticket profile rests on P2") stands in for a rule with no stated premise. T: not stated.
- **A1-2 Supersession names replacement and loci; proposed is not accepted.** Source: R §Successor Disposition (added paragraph); C3 criterion 3 (amended); CR row "conserved heading … different obligation". E: each `superseded` row names its claim, the replacement determination and the owning successor locus or loci. Proposed dispositions and replacements are marked as distinct from accepted ones. Any `conserved` row whose heading survives is checked by comparing meaning, including scope and exceptions. F: a superseded row names only the old section or a successor heading; a proposed replacement is reported as accepted; a refreshed hash is offered as semantic comparison or acceptance; or a heading kept with a narrowed scope is marked `conserved`. T: not stated.
- **A1-3 Scope, modal force, triggers and exceptions survive consolidation.** Source: R §Foundational Reduction 3 (added paragraph); CR row "domain rule … replaced by a shared-law reference". E: when a domain rule moves to a shared owner, its trigger, modal force (must, should, may), adoption conditions and exceptions are traceable in the shared law plus the domain binding. The shared owner supplies the determination; the domain owner supplies its additional binding or policy. F: DESIGN_MODULE §8's preference ("should be total or as close to total as … allow") becomes an unconditional "must be total"; or a profile's rule is replaced by "see Foundations X" while X refers back to the profile for the decision (circular referral). T: shared law in foundations or Spec Method; bindings in profiles.
- **A1-4 Generic determinations are available without an optional profile.** Source: R §Single Ownership 8 (new); CR row "required generic rule is owned only by an optional profile". E: every determination that generic use needs is owned at a foundations or Spec Method locus and can be applied with no profile selected. Profiles own only their additions and keep their selection boundary. F: a generic rule (for example, that precedence is not authority, TRAVERSAL_OCCURRENCE OP-004, or result conjunction) is owned only in an optional profile such as TRAVERSAL_OCCURRENCE, ODD or the frame catalogues; or generic use must adopt a profile to obtain it. T: foundations or Spec Method for the generic rule; profiles for additions.
- **A1-5 Refinements bind predicate and meaning-determining conditions at their owner.** Source: P §Result Algebra (amended); R §Single Result Algebra 2 (amended); CR row "member or profile defines its own result values" (modified). E: each refinement sits at its owning locus. It maps each value, on its declared predicate and with the conditions that determine its meaning, to exactly one core value. Missing conditions are explicit rather than guessed from a label. Where the core requires a domain mapping, the domain supplies it. F: a profile value maps to a core value by name alone ("`blocked` → undecidable") with no predicate or conditions; or a profile says "results follow the core algebra" where the core needs that profile's mapping. T: core in foundations; refinements at their domain owners.
- **A1-6 Recorded states are distinct from evaluations and decisions.** Source: R §Single Result Algebra (added paragraph); P §Result Algebra; CR row "lifecycle label or classification". E: each lifecycle state, classification or selected action states its purpose. Any evaluation or decision that uses it to decide compliance, admission, closure or disposition returns through the core contract. Assessing a condition and exercising authority on it are kept distinct even when they share a domain word. F: ticket `completed` decides closure, or a frontier row's `unresolved` decides qualification, with no core-routed evaluation; "it is only a status" is cited as an exemption; or one label is both the assessment and the authorised act. T: core contract in foundations; the state's owner states its purpose.
- **A1-7 Projections do not change modal standing.** Source: R §Constraint Surfaces 5; CR row "projection changes 'not required' into 'prohibited'". E: projection fidelity evidence includes cases where the source permits but does not require, and where it prefers but does not oblige. The projection keeps those standings. F: a frame turns TICKET §Allowed Status's "Projects may add `blocked`, `cancelled` …" into "only `backlog`, `active`, `completed` are allowed"; or a "should" becomes a "must". Matching digests or a valid schema are offered as repair. T: cross-tier.
- **A1-8 Frame trials bind their actual packet and expectations.** Source: C3 criterion 4 (amended); CR row "frame or task changes after its trial". E: each actual-use record identifies the exact frame bytes, subject, task, supplied instructions and independently specified expectations. Evidence for a changed packet or task is reported separately. Reuse on a successor frame argues applicability. A re-run after correction is labelled as such, not as an unchanged independent test. F: actor instructions contain the expected answer; the frame was edited after the trial while the trial still counts for the current frame; a matching source pin is offered as current task sufficiency; or a corrected re-run is reported as independent confirmation of the correction. T: not stated.
- **A1-9 Iteration 2 checkpoint is not acceptance.** Source: GOALS §Current Selection (amended). E: the candidate cites `a9adce2` and later construction as history or comparison inputs only. F: the iteration 2 merge or later construction is presented as member or checkpoint acceptance. T: not stated.

Additional cases (for A1-3, A1-6 and A1-7):

- **IC-10 (prohibited, modal drift).** A projection of the ticket-status rule forbids a `blocked` state. Expected: fidelity defect; work the source permits stays permitted.
- **IC-11 (unresolved, label without conditions).** A profile reports `blocked` with no predicate or conditions. Expected: the mapping is unresolved; it is neither guessed as failed nor treated as satisfied.

### A1.3 Changes To Existing Expectations

- **FR-2 note on ticket status and UP-020 (superseded).** "Neither is a rival result algebra" no longer stands alone. P §Result Algebra now forbids parallel "evaluation or decision outcomes". Ticket status and UP-020 dispositions must state their purpose and how any evaluation or decision using them returns through the core (A1-6). See AM-12.
- **RD-1** additionally needs A1-5: maps by value name alone no longer satisfy it.
- **FR-1 / SS-4** are extended by A1-1: family coverage includes inherited rules.
- **FR-3 and CF-2** are extended by A1-3: conservation of trigger, modal force and exceptions, and no circular referral.
- **CS-5** is extended by A1-7. **N-15 and PL-6** are extended by A1-8.
- **PL-2, PL-4 and PL-6** must satisfy A1-4. Generic identity, transition and frame law cannot live only in the world-model, ODD or frame-catalogue profiles.
- **AM-1:** GOALS now says "Iteration 2 remains checkpointed at `a9adce2`" without naming a line. Reading (a): this is still Codex's iteration 2. Reading (b): it is the iteration 2 checkpoint for both lines. The other readings stand.
- **AM-8** is partly resolved: superseded rows may have several loci (criterion 3). Criterion 1 still says "a successor locus" for conserved rows.
- **New AM-12 Decision outcomes and the core.** P §Result Algebra brings "decision outcomes" under the single algebra, but R §Single Result Algebra keeps assessment and authority distinct and lists only constraints, judgements, frames, stops, work and effects. Reading (a): dispositions (`accept`, `reject`, `re_enter`, `local_repair`) are themselves core values or refinements. Reading (b): dispositions are authorised acts whose deciding assessment returns through the core.
