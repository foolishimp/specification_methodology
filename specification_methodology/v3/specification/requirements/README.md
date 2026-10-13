# Common Requirements

The common contract governs both tenant realisations.

- [PRINCIPLES](PRINCIPLES.md): the working foundations and their review questions.
- [CAPABILITIES](CAPABILITIES.md): capability questions; each capability's acceptance contract is selected separately.
- [A_C_DEPENDENCY](A_C_DEPENDENCY.md): exact theory, mechanical dependency and proof limits.
- [PREDECESSOR_CLAIMS](PREDECESSOR_CLAIMS.md): the STDO-UP-015 frontier, one row per predecessor claim with its disposition and successor locus.

Working foundation statements are evaluated content. The installed 2.5.1-rc.2 release is builder law and the predecessor the successor evolves. The Product Definition's local axioms are the Product's [identity](../PRODUCT.md#product-identity-and-lineage) and [development isolation](../PRODUCT.md#development-isolation) sections; its override and disambiguation arrays are empty.

## Successor Disposition Requirement

Source: [STDO-UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015), installed law. Every predecessor claim capable of affecting the successor receives exactly one disposition before the successor is accepted: `conserved` (the successor retains the claim), `superseded` (an accepted successor relation replaces it, named), `intentionally removed` (the product owner as Product authority, with the reason) or `not applicable` (no successor effect, with a bounded reason). Conservation is semantic: naming similarity does not prove it and patch absence does not prove loss. UP-015 does not by itself require a retained claim to be rewritten into successor prose. `reframed` is a note on how a conserved claim was carried, not a disposition.

## Standalone Successor Requirement

Source: this Product. The successor stands alone: every `conserved` claim is restated in the successor's own text, so that the successor is complete and applicable without the predecessor remaining operative. A route to the predecessor is evidence of where a claim came from, not of its conservation; under this requirement a route alone satisfies no disposition. The requirement is the reason the construction order is axioms first and then the full predecessor corpus restated.

Restated on the axioms. The successor is on its axioms when three relationships hold:

1. Foundation to law. Each material family of deciding contracts identifies its applicable foundational premises, its conditional consequences, and its additional domain or policy choices with their owners. The full corpus is accounted for; a bounded demonstration is not presented as derivation of every member.
2. Ownership and use. Spec Method and profiles consume the shared contracts, along actual entry and application paths, without conflicting definitions or competing owners. An explanatory cross-reference alone does not establish this relationship.
3. Standalone conservation. Successor-owned text supplies every conserved determination needed for use.

Unchanged predecessor prose satisfies these where it carries the relationships. Copied text does not establish the foundational relationship by its presence, and the share of text rewritten is not evidence that a relationship holds.

## Single Ownership Requirement

Source: this Product's [Intent](../INTENT.md#what-the-product-is).

A determination is a rule, definition, value set or procedure step that an actor must apply. Its owner is an owning locus: one section of one member. Owner here names a place in the text, not decision authority.

1. Within one candidate, every determination has exactly one owning locus. Each tenant candidate is its own scope; the same determination in the two candidates does not make a second owner.
2. The owning tier follows the [tier obligations](../PRODUCT.md#c3-construction-contract): foundations own what holds for any method; Spec Method owns what holds for this method; a domain or operational profile owns only its own bindings; guides own their posting, writing and glossary conventions; packaging owns no method determination.
3. Every other locus refers to the owner or refines it. A refinement names its owner and maps each of its values or cases back to the owner's; it never contradicts or redefines the owner's determination.
4. A projected frame's copy of a clause names its owning locus and is not a second owner. A copy that differs from its owner is a conformance defect, repaired by re-projecting from the owner.
5. Conserved text restated under the [standalone successor requirement](#standalone-successor-requirement) is the successor's own owning locus for that determination, not a duplicate of the predecessor.
6. A part ported under [Cross-Synthesis](../PRODUCT.md#cross-synthesis) takes one owning locus in the receiving candidate.
7. Where two loci decide the same question, one is made the owner and the other refers to or refines it. No precedence rule between loci substitutes for that.

Purpose and material relation: a question decided at two loci is interpreted twice and can be answered two ways. One owning locus gives one answer per question within a candidate. The [single result algebra requirement](#single-result-algebra-requirement) is this requirement applied to results.

## Single Result Algebra Requirement

Source: this Product ([Result Algebra](../PRODUCT.md#result-algebra)). It unifies the RF-012 and AC-007 evaluation algebras ([C1 Disposition](PRINCIPLES.md#c1-disposition)).

1. The foundations tier owns exactly one core result algebra. Constraint, judgment, frame, stop, work and effect results are stated in it or as refinements of it.
2. A member or profile that needs finer outcomes defines a refinement. Every refined value maps to exactly one core value; no outcome exists outside the core.
3. A refinement never raises a result's standing. A falsified or failed result never maps to a satisfied or successful one. A result that admissible evidence cannot decide never maps to satisfied. An evaluation that was not performed stays distinct from one whose evidence cannot decide. An effect of unknown completion never maps to no effect or to completed.
4. The core value travels with the evaluated predicate and the original domain outcome. A mapping never owns domain meaning; the domain owner keeps it.
5. A step having produced a candidate never maps to the candidate's fitness or acceptance. Availability, assessment and acceptance remain separate results.
6. Conjunction and composition of results are defined once, over the core.
7. A projected frame whose task returns a result carries the core algebra or its profile's mapping into it.

Purpose and material relation: this is the [single ownership requirement](#single-ownership-requirement) applied to results, as the [Intent](../INTENT.md#what-the-product-is) directs; one outcome vocabulary across tiers removes competing ownership of results. Items 3 to 5 retain the distinctions that failure, undecidability, non-performance and uncertain effects must keep under composition ([P5 and P6](PRINCIPLES.md)).

## Categorical Demonstration Standard

Source: this Product ([Categorical Construction](../PRODUCT.md#categorical-construction)) and the [categorical groundwork strategy](../../.ai-workspace/comments/claude/20261013T012745Z_STRATEGY_categorical_groundwork.md#what-the-method-must-supply).

A categorical claim about the method, or about a construction made with it, is established only with:

1. Objects and arrows. The objects, arrows, arrow equality, identities and associative composition of each category claimed are shown.
2. Preservation per layer. Each refinement layer states what it preserves of the layer above and discharges that obligation. An exact step preserves meaning. An approximate step states its adequacy relation and an end-to-end bound; fixed-tolerance closeness does not compose step by step.
3. Licensing laws. A construction step is admissible under the laws declared for its subject. With no law declared, only universally valid steps are admissible.
4. Joins. A map between categories is defined on objects and arrows and shows its functor laws before a functor is claimed. Conformance, equivalence and functorial preservation are distinct claims.
5. Representation and evidence. Laws, records and maps are written in a_c; a_c, its interpretations and its carriers keep separate identities. Structural validation checks structure only. Each claim names its evidence class: mechanically checked, established by mathematical argument, tested against an independently specified oracle, or unresolved.
6. Worked join. One algorithm category joined with one computation category is the acceptance instance.

A categorical statement without this demonstration is a hypothesis. Purpose and material relation: the categorical direction ([Intent](../INTENT.md#demonstration-standard)) is useful only where its constructions preserve meaning, and these items are what preservation must show.
