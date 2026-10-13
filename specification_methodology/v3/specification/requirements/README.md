# Common Requirements

The common requirements bind both build tenants' candidates. This file holds the requirements that come from this Product. The other files hold the rest:

- [PRINCIPLES](PRINCIPLES.md): the working foundations, the candidate first principles both tenants built from at C1, and their review questions.
- [CAPABILITIES](CAPABILITIES.md): the capabilities required by the reconstruction and the questions that test their adequacy. Each trial binds its own subject and acceptance scope.
- [A_C_DEPENDENCY](A_C_DEPENDENCY.md): the exact a_c theory and checker this product depends on, and the limits of what the checker proves.
- [PREDECESSOR_CLAIMS](PREDECESSOR_CLAIMS.md): the frontier under STDO-UP-015, with one row per predecessor claim giving its disposition and, where required, its successor locus.

The working foundation statements in PRINCIPLES are content under evaluation, not installed law. The installed 2.5.1-rc.2 release is the law the builders work under, and it is the predecessor the new release evolves from.

The Product Definition (`stdo_3.json`) adds two local axioms: the Product's [identity](../PRODUCT.md#product-identity-and-lineage) and [development isolation](../PRODUCT.md#development-isolation) sections. Its override and disambiguation lists are empty, so it overrides no installed rule and disambiguates no installed term.

A determination is a rule, definition, list of allowed values or procedure step that an actor must apply.

## Successor Disposition Requirement

Source: [STDO-UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015), a rule of the installed release. Every predecessor claim that could affect the successor receives exactly one disposition before the successor is accepted:

- `conserved`: the successor keeps the claim;
- `superseded`: an accepted successor relation replaces the claim, and is named;
- `intentionally removed`: the product owner, as Product authority, removes the claim and gives the reason;
- `not applicable`: the claim has no effect on the successor, with a bounded reason.

Conservation is about meaning. Similar naming does not prove it, and the absence of an edit carrying a claim does not prove the claim was lost. UP-015 does not by itself require a kept claim to be rewritten in the successor's wording. `reframed` is a note on how a conserved claim was carried, not a disposition.

## Standalone Successor Requirement

Source: this Product. The successor stands alone. Every `conserved` claim is stated in the successor's own text, so that the successor is complete and usable without the predecessor in force. A link to the predecessor shows where a claim came from, not that it is conserved. Under this requirement a link alone satisfies no disposition. This requirement is why construction comes in this order: the axioms first, then the whole predecessor restated on them.

Restated on the axioms. The successor is on its axioms when four relationships hold:

1. Foundation to law. A family of deciding contracts is a group of related rules that decide outcomes; a material family is one whose outcomes matter to the product. Each material family identifies three things:
   - the foundational premises it rests on;
   - the consequences that follow from them;
   - any additional domain or policy choices, with their owners.

   The whole set of members is accounted for. A demonstration over a few members is not presented as a derivation of every member.
2. Ownership and use. The Spec Method and the profiles use the shared contracts at the points where an actor actually enters and applies them, not only by cross-reference, without conflicting definitions or competing owners. An explanatory cross-reference alone does not establish this relationship.
3. Standalone conservation. Text the successor owns supplies every conserved determination needed for use.
4. Reduction. The pillars determine the shared laws and their specialisations under the [reduction requirement](#foundational-reduction-requirement). Repeated determinations are contracted into their shared owners, and material independent mechanisms that remain have a stated need.

Unchanged predecessor text satisfies these where it carries the relationships. Copied text does not establish the foundational relationship just by being present, and the share of text rewritten is not evidence that a relationship holds.

## Foundational Reduction Requirement

Source: this Product's [Foundational Reduction](../PRODUCT.md#foundational-reduction). The reconstruction must make the method simpler to determine and apply while preserving its necessary distinctions.

1. Account for each pillar's material contribution. Separate foundational premises, derived consequences, domain policies and implementation choices. A named calculus or a conceptual correspondence is insufficient without the deciding rules and consumers it governs.
2. Identify recurring determinations across the predecessor and the candidate. Establish one shared owner and replace their independent determination at each affected consumer with that law or an explicit refinement. Adding a common introduction while the consumers retain rival rules does not satisfy reduction.
3. Preserve required distinctions while consolidating machinery. Different domains may use the same transformation without acquiring equal identity, meaning, authority or evidence. A retained material primitive or independent policy identifies the distinction it supplies and why the shared contracts do not already decide it. This is stated in existing design and proof surfaces, not a new record for every helper.
4. Reconstruct member boundaries from those responsibilities. Predecessor files, headings, procedural stages and actor arrangements impose no one-to-one successor partition. A conserved determination may move to a shared owner. Its consumers carry their necessary bindings; they do not reproduce the common law as a second authority. Intentionally removing a material obligation still requires its owning decision under the disposition requirement.
5. Demonstrate contraction on actual deciding paths. Identify which independently interpreted rules, mechanisms, exceptions or cross-document reconciliations are removed or made unnecessary, and which remain justified. Compare the resulting decisions and acquisition with the predecessor and the preceding candidate where available. Word count, a diagram, rewritten prose and a passing structural checker cannot establish this claim alone.
6. Challenge the reconstruction with independently specified successful, refused and unresolved cases where applicable, including cross-domain composition, failure preservation and recovery. Disclose the compared subjects, tasks, acquisition conditions and evidence limits. A few selected cases establish only their covered relations; complete predecessor accounting and member acceptance remain required.

## Constraint Surfaces And Logic Compression

Source: this Product's [Foundational Reduction](../PRODUCT.md#foundational-reduction) and [Method Structure](../PRODUCT.md#method-structure).

1. A constraint surface states the obligations and permitted freedom for a declared subject and work boundary: its objects and meanings, relevant predicates and dependencies, admissible operations, required results, authority, evidence and explicit unresolved conditions. It constrains work without prescribing the worker's internal solution strategy beyond those obligations.
2. The method's a_c interpretation represents this logic from its owning prose. Its objects, relations and constraints retain the distinction between a premise, a derived consequence, a policy choice, an observation and an unresolved claim. The dependency structure may share premises and contain revisable relationships; no tree-only encoding or execution order is imposed.
3. Each represented determination resolves to its current owning source and basis. Its material dependencies, exceptions, permitted latitude and failure or uncertainty outcomes remain recoverable. A missing premise or omitted obligation cannot become permission or a satisfied result. A dependent action with an unresolved required premise is handled through its declared result and recovery contract.
4. A task projection carries sufficient relevant constraints and the required material inputs or acquisition routes under the frame requirement. Abstract rules alone do not supply observations, a valid effect grant or task context. Actor context remains disposable; the workspace and selected authoritative inputs remain the basis of reacquisition.
5. Prose, formal interpretation and acquired views express the same owned determination for their declared use. A representation that changes the permitted or required work is a fidelity defect unless the change is an explicitly authorised successor. An approximate representation declares its adequacy relation and end-to-end bound; exact authority and permission distinctions are not silently weakened by approximation.
6. Ordinary entry selects the current exact interpretation and its limits. Historical models are identified as historical. Required fidelity evidence compares source and representation on independently specified permissible, prohibited and unresolved cases; a source-first reviewer checks the relationship and its uncovered scope.
7. Mechanical validation, mathematical argument, semantic judgment and actual-use evidence establish their respective claims. Logic compression does not make every predicate decidable or confer operation or acceptance authority. The [a_c dependency contract](A_C_DEPENDENCY.md) retains its separate theory, interpretation, carrier and checker boundaries.

## Bounded Transitions And Reference Frames

Source: [Construction And Context Management](../PRODUCT.md#construction-and-context-management), [P4–P6](PRINCIPLES.md#p4-typed-composition-and-conservation), and the installed [Reference Frame laws](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws), including [RF-009 No Assumed Hierarchy](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-009-no-assumed-hierarchy).

1. Construction binds the described current state, destination constraints and the obligations each selected transition must preserve. Discovery and evaluation may change the known work. A destination change follows its owning authority and re-entry rules. Completion requires sufficient evidence against the applicable destination and its acceptance conditions; an explicit stop retains the unresolved outcome.
2. Context management selects a frame that fits the actor's declared capability and contains the contract and material sufficient for its task. Known material relations appear in the frame or enter through declared authoritative inputs. Irrelevant material stays outside active attention unless needed to establish irrelevance. Capacity pressure never licenses omission of a material obligation; refine the task, select a capable actor or return the applicable stop.
3. Context fit and adequate attention are evaluated separately. Bytes or tokens measure the selected representation's size. Actual-use evidence evaluates whether the actor applies the frame adequately to its declared task and conditions. It establishes no universal attention score. Time, spend and other resource limits remain those of the selected execution binding.
4. A configuration assigns responsibilities and information exchanges to frames from the task's operations, dependencies, actor capabilities and assurance requirements. Its design explains the allocation, including material resource limits and assumptions about failure. It may use one frame or several, fixed or adaptive allocation, with no prescribed role inventory or hierarchy. The permitted allocation and reconfiguration preserve material dependencies, outstanding obligations, effects, admitted authority and required independence. Functional decomposition, communication, authority and evaluation dependency remain distinct. Selection or naming of a frame grants no authority. Each activation still binds its subject, result, capability and admitted authority. Required reviewer independence retains its authorship and evidence conditions; common sources and relevant evidence may be shared, while a fresh context alone does not satisfy independence.
5. The material workspace and its authoritative external inputs persist across activations; an actor's context is a disposable projection, not a second truth surface. An activation observes the subject and basis its contract binds, including committed snapshots and declared external systems; an absent sparse file is not evidence of absence. Admissible contrary evidence reopens the affected claim under its drift and re-entry rules. It does not silently rebind the basis, change a governing requirement or confer authority. Acquisition reconciles material disagreement with cached beliefs or summaries. Discarding private context does not reset the workspace. Resumption starts from the current material state and retains applicable valid work. New observations may invalidate affected claims, and unknown effects are resolved sufficiently for the next dependent action. The method imposes no universal reset or complete-history replay obligation; the applicable recovery contract determines the necessary observations and effects. Closed results support bounded handoffs without transferring private working context; their reuse retains the existing validity and independence conditions.

Purpose and material relation: finite context and attention require bounded, sufficient work and assessment. Task structure and assurance requirements constrain how that work is organised. These obligations preserve the selected destination through decomposition, coordination and recovery without deriving purpose or authority from resource limits. The configuration is stated in existing design, frame and work records; no additional carrier is required.

## Build-Tenant Binding Requirement

Source: this Product's [Build-Tenant Binding](../PRODUCT.md#build-tenant-binding). Each candidate's Spec Method states and applies this relation between a product's common WHAT and its tenant realisations.

1. A build tenant binds the common requirements calculus to a declared computational calculus and binds that calculus to a concrete execution environment. These bindings are part of its existing design and realisation surfaces.
2. The execution environment may be a technology stack, a human process or a combination. Its selection remains within the common requirements, including any required human decision. Author identity, actor identity and operation kind remain distinct; a person performing an operation does not by itself make that operation human adjudication.
3. The binding identifies the operations, composition laws, effects, resource measures and operational assumptions material to conformance. Human effort, elapsed time, communication and machine resources are measured where the selected obligations need them, with their units and boundaries stated.
4. Conformance evidence establishes how the bound realisation satisfies the required meaning and constraints, including applicable authority, independence, failure and recovery conditions. A convenient stack cannot weaken an obligation. A categorical preservation claim also meets the [demonstration standard](#categorical-demonstration-standard).
5. A computational calculus may be reused across tenants and execution environments where the bindings satisfy its laws. A different language, tool or team does not by itself require a different calculus.
6. Representation of the requirements and bindings in a_c does not prescribe their executor or establish execution conformance through structural validation alone.

Purpose and material relation: the same common obligations can be realised through different means. The tenant owns those choices and their evidence, while the common specification retains its meaning. This keeps a particular stack from becoming universal method machinery and permits human and mixed processes without a parallel methodology.

## Single Ownership Requirement

Source: this Product's [Intent](../INTENT.md#what-the-product-is).

A determination's owner is an owning locus: one section of one member. Owner here names a place in the text, not a person with decision authority.

1. Within one candidate, every determination has exactly one owning locus. Each tenant candidate is its own scope, so the same determination appearing in both candidates is not a second owner.
2. The owning tier follows the [tier obligations](../PRODUCT.md#c3-construction-contract):
   - the Foundations own what holds for any method;
   - the Spec Method owns what holds for this method;
   - a domain profile, such as world modelling, or an operational profile, such as the frame catalogues and Executive procedure, owns only its own bindings: the terms and choices it adds for its domain or operation;
   - the guides own their posting, writing and glossary conventions;
   - packaging owns no method determination.
3. Every other locus refers to the owner or refines it. A refinement names its owner and maps each of its values or cases back to the owner's. It never contradicts or redefines the owner's determination.
4. A reference frame's copy of a clause names its owning locus and is not a second owner. A copy that differs from its owner is a conformance defect, repaired by copying again from the owner.
5. Conserved text restated under the [standalone successor requirement](#standalone-successor-requirement) is the successor's own owning locus for that determination, not a duplicate of the predecessor.
6. A part ported under [Cross-Synthesis](../PRODUCT.md#cross-synthesis) takes one owning locus in the receiving candidate.
7. Where two loci decide the same question, one is made the owner and the other refers to it or refines it. No rule of precedence between loci substitutes for that.

Purpose and material relation, meaning why the requirement exists and what it protects: a question decided in two places is interpreted twice and can be answered two ways. One owning locus gives one answer per question within a candidate. The [single result algebra requirement](#single-result-algebra-requirement) is this requirement applied to results.

## Single Result Algebra Requirement

Source: this Product ([Result Algebra](../PRODUCT.md#result-algebra)). It unifies the previous release's two evaluation algebras, which C1 left to be unified ([C1 Disposition](PRINCIPLES.md#c1-disposition)):

- RF-012, the closed results of reference-frame evaluations;
- AC-007, the constraint and refusal outcomes of a_c.

1. The Foundations own exactly one core result algebra. Results of constraints, judgements, frames, stops, work and effects are stated in it or as refinements of it.
2. A member or profile that needs finer outcomes defines a refinement. Every refined value maps to exactly one core value, and no outcome exists outside the core.
3. A refinement never raises a result's standing:
   - a falsified or failed result never maps to a satisfied or successful one;
   - a result that admissible evidence cannot decide never maps to satisfied;
   - an evaluation that was not performed stays distinct from one whose evidence cannot decide;
   - an effect whose completion is unknown never maps to no effect or to completed.
4. The core value travels with the evaluated predicate and the original domain outcome. A mapping never owns domain meaning; the domain owner keeps it.
5. A step having produced a candidate never maps to the candidate's fitness or acceptance. Availability, assessment and acceptance remain separate results.
6. Conjunction and composition of results are defined once, over the core.
7. A reference frame whose task returns a result carries the core algebra or its profile's mapping into it.

Purpose and material relation: this is the [single ownership requirement](#single-ownership-requirement) applied to results, as the [Intent](../INTENT.md#what-the-product-is) directs. One set of outcome values across the tiers removes competing ownership of results. Items 3 to 5 keep, when results are combined, the distinctions between failure, undecidability, non-performance and uncertain effects. Those distinctions are required by [P5 and P6](PRINCIPLES.md): finite capacity with graceful handling, and justified claims with separate authority.

## Categorical Demonstration Standard

Source: this Product ([Categorical Construction](../PRODUCT.md#categorical-construction)) and the [categorical groundwork strategy](../../.ai-workspace/comments/claude/20261013T012745Z_STRATEGY_categorical_groundwork.md#what-the-method-must-supply).

A categorical claim about the method, or about a construction made with it, is established only with items 1 to 5, as far as they apply to it. Acceptance of the categorical capability, and any claim that asserts the worked join itself, also require item 6:

1. Objects and arrows. For each category claimed: its objects, its arrows, when two arrows are equal, its identities, and associative composition.
2. Preservation per layer. Each refinement layer states what it preserves of the layer above and discharges that obligation. An exact step preserves meaning. An approximate step states its adequacy relation (how close is close enough) and an end-to-end bound. A fixed tolerance at each step does not compose into an end-to-end bound.
3. Licensing laws. A construction step is admissible under the laws declared for its subject. With no law declared, only universally valid steps, which hold whatever laws the subject has, are admissible.
4. Joins. A map between categories is defined on objects and arrows. Its functor laws, that it preserves identities and composition, are shown before it is claimed to be a functor. Conformance, equivalence and functorial preservation are distinct claims.
5. Representation and evidence.
   - Laws, records and maps are represented in a_c, retaining which statements are premises, derived consequences or declared choices.
   - a_c, its interpretations and its carriers (the files and tools that hold it) keep separate identities.
   - Structural validation checks structure only.
   - Each claim names its evidence class: mechanically checked, established by mathematical argument, tested against an independently specified oracle, or unresolved.
6. Worked join. One algorithm category joined with one computation category is the acceptance instance for the categorical capability.

A categorical statement without the demonstration it requires is a hypothesis. Purpose and material relation: the categorical direction ([Intent](../INTENT.md#mission)) is useful only where its constructions preserve meaning, and these items are what preservation must show.
