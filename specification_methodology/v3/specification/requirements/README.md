# Common Requirements

The common requirements bind both build tenants' candidates. This file holds the requirements that come from this Product. The other files hold the rest:

- [PRINCIPLES](PRINCIPLES.md): the working foundations, the candidate first principles both tenants built from at C1, and their review questions.
- [CAPABILITIES](CAPABILITIES.md): the capability questions. Each capability's acceptance contract is selected separately.
- [A_C_DEPENDENCY](A_C_DEPENDENCY.md): the exact a_c theory and checker this product depends on, and the limits of what the checker proves.
- [PREDECESSOR_CLAIMS](PREDECESSOR_CLAIMS.md): the frontier under STDO-UP-015, with one row per predecessor claim giving its disposition and successor locus.

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

Restated on the axioms. The successor is on its axioms when three relationships hold:

1. Foundation to law. A family of deciding contracts is a group of related rules that decide outcomes; a material family is one whose outcomes matter to the product. Each material family identifies three things:
   - the foundational premises it rests on;
   - the consequences that follow from them;
   - any additional domain or policy choices, with their owners.

   The whole set of members is accounted for. A demonstration over a few members is not presented as a derivation of every member.
2. Ownership and use. The Spec Method and the profiles use the shared contracts at the points where an actor actually enters and applies them, not only by cross-reference, without conflicting definitions or competing owners. An explanatory cross-reference alone does not establish this relationship.
3. Standalone conservation. Text the successor owns supplies every conserved determination needed for use.

Unchanged predecessor text satisfies these where it carries the relationships. Copied text does not establish the foundational relationship just by being present, and the share of text rewritten is not evidence that a relationship holds.

## Bounded Transitions And Reference Frames

Source: [Construction And Context Management](../PRODUCT.md#construction-and-context-management), [P4–P6](PRINCIPLES.md#p4-typed-composition-and-conservation), and the installed [Reference Frame laws](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws).

1. Construction binds the described current state, destination constraints and the obligations each selected transition must preserve. Discovery and evaluation may change the known work. A destination change follows its owning authority and re-entry rules. Completion requires sufficient evidence against the applicable destination and its acceptance conditions; an explicit stop retains the unresolved outcome.
2. Context management selects a frame that fits the actor's declared capability and contains the contract and material sufficient for its task. Known material relations appear in the frame or enter through declared authoritative inputs. Irrelevant material stays outside active attention unless needed to establish irrelevance. Capacity pressure never licenses omission of a material obligation; refine the task, select a capable actor or return the applicable stop.
3. Context fit and adequate attention are evaluated separately. Bytes or tokens measure the selected representation's size. Actual-use evidence evaluates whether the actor applies the frame adequately to its declared task and conditions. It establishes no universal attention score. Time, spend and other resource limits remain those of the selected execution binding.
4. Worker, Reviewer and Executive responsibilities are derived frames for construction, assessment and coordination. The frame binds its subject, result, actor capability and admitted authority. Selection or naming of a frame grants no authority. Required reviewer independence retains its authorship and evidence conditions; frames may share governing sources and relevant evidence. A fresh context alone does not satisfy independence. A sufficient directly authorised task may use one frame; these responsibilities impose no universal three-actor sequence.
5. Resumption starts from the current material state and retains applicable valid work. New observations may invalidate affected claims, and unknown effects are resolved sufficiently for the next dependent action. The method imposes no universal reset or complete-history replay obligation; the applicable recovery contract determines the necessary observations and effects. Closed results support bounded handoffs without transferring private working context; their reuse retains the existing validity and independence conditions.

Purpose and material relation: finite context and attention require bounded, sufficient work and assessment. These obligations preserve the selected destination through decomposition, coordination and recovery without deriving purpose or authority from resource limits. They use existing design, frame and work records.

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
