# Common Requirements

The common requirements bind both build tenants' candidates. This file holds the requirements that come from this Product. The other files hold the rest:

- [PRINCIPLES](PRINCIPLES.md): the working foundations accepted at C1, each with its review question.
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

1. Foundation to law. Each material family of deciding contracts is a group of rules that decide outcomes. Each identifies three things:
   - the foundational premises it rests on;
   - the consequences that follow from them;
   - any additional domain or policy choices, with their owners.

   The whole set of members is accounted for. A bounded demonstration is not presented as a derivation of every member.
2. Ownership and use. The Spec Method and the profiles use the shared contracts along the paths by which they are actually entered and applied, without conflicting definitions or competing owners. An explanatory cross-reference alone does not establish this relationship.
3. Standalone conservation. Text the successor owns supplies every conserved determination needed for use.

Unchanged predecessor text satisfies these where it carries the relationships. Copied text does not establish the foundational relationship just by being present, and the share of text rewritten is not evidence that a relationship holds.

## Single Ownership Requirement

Source: this Product's [Intent](../INTENT.md#what-the-product-is).

A determination's owner is an owning locus: one section of one member. Owner here names a place in the text, not a person with decision authority.

1. Within one candidate, every determination has exactly one owning locus. Each tenant candidate is its own scope, so the same determination appearing in both candidates is not a second owner.
2. The owning tier follows the [tier obligations](../PRODUCT.md#c3-construction-contract):
   - the Foundations own what holds for any method;
   - the Spec Method owns what holds for this method;
   - a domain or operational profile owns only its own bindings;
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

A categorical claim about the method, or about a construction made with it, is established only with:

1. Objects and arrows. For each category claimed: its objects, its arrows, when two arrows are equal, its identities, and associative composition.
2. Preservation per layer. Each refinement layer states what it preserves of the layer above and discharges that obligation. An exact step preserves meaning. An approximate step states its adequacy relation (how close is close enough) and an end-to-end bound. A fixed tolerance at each step does not compose into an end-to-end bound.
3. Licensing laws. A construction step is admissible under the laws declared for its subject. With no law declared, only universally valid steps are admissible.
4. Joins. A map between categories is defined on objects and arrows. Its functor laws, that it preserves identities and composition, are shown before it is claimed to be a functor. Conformance, equivalence and functorial preservation are distinct claims.
5. Representation and evidence.
   - Laws, records and maps are written in a_c.
   - a_c, its interpretations and its carriers (the files and tools that hold it) keep separate identities.
   - Structural validation checks structure only.
   - Each claim names its evidence class: mechanically checked, established by mathematical argument, tested against an independently specified oracle, or unresolved.
6. Worked join. One algorithm category joined with one computation category is the acceptance instance.

A categorical statement without this demonstration is a hypothesis. Purpose and material relation: the categorical direction ([Intent](../INTENT.md#mission)) is useful only where its constructions preserve meaning, and these items are what preservation must show.
