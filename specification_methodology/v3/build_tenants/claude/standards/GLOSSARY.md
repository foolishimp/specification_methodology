# GLOSSARY

Guide. A non-deciding locator index from indexed spellings to the clauses
of this corpus that declare their bounded contexts and own their concepts.
It realises the glossary that
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
names and adds nothing to that law. Every clause names the principle that
requires it (P0 to P6, FOUNDATIONS §3). A route written `rc.2 #anchor` is
into `stdo://releases/v2.5.1-rc.2/standards/GLOSSARY_GUIDE.md` and is
provenance only; nothing here depends on that cut to be applied.

## 1. Index contract

This member contains no semantic definition. It declares no bounded
context, concept, import, translation, equivalence, disambiguation or
authority. It is a non-deciding index into the clauses that own those
meanings in the selected complete STDO basis (P6, P1; rc.2
#index-contract).

Each row records an indexed spelling, the bounded-context identity
declared by the cited owning clause, and the exact owning concept clause.
The owning clause together with the selected basis identifies the candidate meaning;
the occurrence being resolved still supplies its own governed scope (P1,
P3). A row whose context or owning clause does not resolve is invalid, and
this index cannot repair it (P5, P6).

Repeated spellings in different rows are intentional. Equal spelling,
nearness in this index, a heading, or inclusion in this member creates no
identity, inheritance, import, equivalence or authority (P1, P3, P6).
Resolution follows
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution);
this index supplies no fallback decision (P1, P5).

## 2. Locator law

Every locus is a clause of this corpus, never of the predecessor cut; a
predecessor route appears only in §16 as provenance (P6, P3). Each
section names the clause that declares its context. A row's owning concept
clause declares the row's bounded-context identity and owns the concept,
in its own text or through the context-ownership statement of its own
member (P6, P1). The relation clause, where given, points to the defining
locus of a concept that the owning clause includes from another member,
or to a clause that relates the concept to another member or context; the
index states no relation itself (P1, P6).

A term without such an owning clause is not a valid row under §1, and
this index carries no such row (P5, P6).

Index watch. A derived surface or projected frame that relies on this
index to locate meaning watches it through the index's path and digest,
recorded separately from the deciding sources it was derived from. Locator
drift in this index then makes that surface or frame stale
([PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary),
staleness binding), and the watch does not make this index an owner of
meaning (P3, P6; provenance rc.2 authority_compressions/README.md, a claim
no rc.2 body states).

## 3. Method identity

Context declared by
[SPEC_METHOD §1 Method identity](SPEC_METHOD.md#method-identity) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO` | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | none |
| `O` pillar symbol | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | [`ODD.md#1-position`](ODD.md#1-position) |

## 4. Axiomatic calculus

Context declared by
[AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `a_c`; `Axiomatic Calculus`; `STDO Axiomatic Calculus for Governed Symbolic Systems` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#1-position`](AXIOMATIC_CALCULUS.md#1-position) | none |
| `a_c Signature` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#2-signature`](AXIOMATIC_CALCULUS.md#2-signature) | none |
| `a_c Model` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#2-signature`](AXIOMATIC_CALCULUS.md#2-signature) | [`AXIOMATIC_CALCULUS.md#6-interpretation-and-models`](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) |
| `Semantic Object` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#semantic-object`](AXIOMATIC_CALCULUS.md#semantic-object) | none |
| `Typed Relation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#typed-relation`](AXIOMATIC_CALCULUS.md#typed-relation) | none |
| `Constraint` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#constraint`](AXIOMATIC_CALCULUS.md#constraint) | none |
| `Latitude` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#latitude`](AXIOMATIC_CALCULUS.md#latitude) | none |
| `Residual` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#residual`](AXIOMATIC_CALCULUS.md#residual) | none |
| `Judgment` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-014-judgment-separation`](AXIOMATIC_CALCULUS.md#ac-014-judgment-separation) | none |
| `Functor Kind`; `F_D`; `F_P`; `F_H` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds`](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds) | none |
| `Material Closure` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-010-material-closure`](AXIOMATIC_CALCULUS.md#ac-010-material-closure) | none |
| `Projection` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#ac-011-projection`](AXIOMATIC_CALCULUS.md#ac-011-projection) | none |
| `Interpretation` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#6-interpretation-and-models`](AXIOMATIC_CALCULUS.md#6-interpretation-and-models) | none |
| `Axiomatic Calculus Basis` | `urn:stdo:bounded-context:axiomatic-calculus` | [`AXIOMATIC_CALCULUS.md#8-calculus-identity`](AXIOMATIC_CALCULUS.md#8-calculus-identity) | none |

## 5. Semantic resolution

Context declared by
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Term` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Concept Reference` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Bounded Context` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Semantic Address` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Semantic Import` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Semantic Translation` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Semantic Equivalence` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |
| `Semantic Disambiguation` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) |

## 6. Product-definition routing

Context declared by
[PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO Product Definition Overlay` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Definition Root` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Definition Label` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Product-Definition Identity` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | none |
| `Constitutional Set` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency`](PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency) | none |
| `Project Reference-Frame Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) | [`REFERENCE_FRAME.md#4-frame-set-declaration`](REFERENCE_FRAME.md#4-frame-set-declaration) |
| `Agent Frame Activation` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) |
| `Installed Release Basis` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |
| `Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | [`RELEASE.md#4-selector-and-consumer-adoption`](RELEASE.md#4-selector-and-consumer-adoption) |
| `Fleet Adoption Plan` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |
| `STDO Toolchain Manager` | `urn:stdo:bounded-context:product-definition-routing` | [`PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) | none |

## 7. Release publication

Context declared by
[RELEASE §1](RELEASE.md#1-context-and-position) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Project Release Namespace` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | none |
| `Project Subtree` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | [`RELEASE.md#project-subtree-release-identity`](RELEASE.md#project-subtree-release-identity) |
| `Candidate Source` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) |
| `RC Branch` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | none |
| `Immutable RC Cut` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) |
| `Version-Line Selector` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) |
| `Release Branch` | `urn:stdo:bounded-context:release-publication` | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) | none |

## 8. Reference-frame evaluation

Context declared by
[REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit),
whose statement of ownership includes in the context the frame objects of
FOUNDATIONS §2 and the result algebra of ACTIVATION §3, each owned at its
defining locus (P3, P6). A row for an included concept cites §1 as the
clause that declares the context and owns the concept in it, and its
defining locus as relation clause (P6, P1).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Reference Frame`; `Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) |
| `Frame Tuple` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`FOUNDATIONS.md#the-frame-tuple`](FOUNDATIONS.md#the-frame-tuple); [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) |
| `Frame Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) | none |
| `Frame-Set Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#4-frame-set-declaration`](REFERENCE_FRAME.md#4-frame-set-declaration) | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) |
| `Activated Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects); [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) |
| `Activation Packet` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) | [`ACTIVATION.md#1-the-step`](ACTIVATION.md#1-the-step) |
| `Evaluation` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) |
| `Engagement Atom`; `Semantic Atom` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#engagement-atom-and-semantic-atom`](REFERENCE_FRAME.md#engagement-atom-and-semantic-atom) | none |
| `Coverage Ledger` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#coverage-ledger`](REFERENCE_FRAME.md#coverage-ledger) | none |
| `Result Algebra` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra); [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results); [`AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) |
| `satisfied`; `falsified`; `indeterminate`; `out_of_frame`; `invalid_basis` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra); [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results) |
| `Evaluation Family`; `Workspace`; `Material-Relation Manifold`; `Coordinate`; `Topology`; `Capability Envelope`; `Frame Set`; `Active Frame Configuration`; `Lens`; `Role`, `Persona`, `Abstraction`, `Component` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) |
| construction availability: `candidate_ready`; `refused`; `incomplete`; `re_entry_requested` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra) |
| disposition: `accept`; `local_repair`; `re_enter`; `reject` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`ACTIVATION.md#disposition`](ACTIVATION.md#disposition) |
| ambiguity outcome: `resolved`; `carried`; `escalated`; `blocked` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra); [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |
| `Closed Result` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results) | [`ACTIVATION.md#7-closed-result-and-reuse`](ACTIVATION.md#7-closed-result-and-reuse) |
| `Product` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`](EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set) | none |
| `Owner` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`](EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set) | none |

## 9. Build tenancy

Context declared by
[PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Build Tenant` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Build Tenancy`; `Multi-Build-Tenancy` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Tenant Registry` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Common Build-Tenant Surface` | `urn:stdo:bounded-context:build-tenancy` | [`PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) |
| `Multi-Build-Tenant Work Item` | `urn:stdo:bounded-context:build-tenancy` | [`TICKETS.md#multi-build-tenant-independence`](TICKETS.md#multi-build-tenant-independence) |

## 10. Recursive product

Context declared by
[FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Substrate` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Development Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Source Project` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`WORLD_MODEL.md#builder-project-specialisation`](WORLD_MODEL.md#builder-project-specialisation) |
| `Release Cut` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`RELEASE.md#2-release-identities`](RELEASE.md#2-release-identities) |
| `Product` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Install` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Artifact` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | none |
| `Product Definition` | `urn:stdo:bounded-context:recursive-product-taxonomy` | [`FOUNDATIONS.md#product-lineage-objects`](FOUNDATIONS.md#product-lineage-objects) | [`PRODUCT_DEFINITION.md#1-overlay-and-layout-independence`](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) |

## 11. Product assurance

Context declared by
[ASSURANCE §2](ASSURANCE.md#2-testing-strategy-taxonomy) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Design/Module Conformance Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Unit Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#15-module-derived-unit-tests`](ASSURANCE.md#15-module-derived-unit-tests) | [`DESIGN_MODULE.md#9-module-taxonomy`](DESIGN_MODULE.md#9-module-taxonomy) |
| `UAT`; `Acceptance Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Sandbox Test` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Harnessed Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |
| `Live Sandbox UAT` | `urn:stdo:bounded-context:product-assurance` | [`ASSURANCE.md#2-testing-strategy-taxonomy`](ASSURANCE.md#2-testing-strategy-taxonomy) | none |

## 12. Ambiguity governance

Context declared by
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Lawful Probabilistic Processing` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) | none |
| `Human Adjudication` | `urn:stdo:bounded-context:ambiguity-governance` | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) | none |

## 13. World model

Context declared by
[WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Builder Project` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | [`WORLD_MODEL.md#builder-project-specialisation`](WORLD_MODEL.md#builder-project-specialisation) |
| `Published Domain Artifact` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `World Model Object` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `Markov Object` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | [`WORLD_MODEL.md#4-the-markov-object-construct`](WORLD_MODEL.md#4-the-markov-object-construct) |
| `Treatment Surface` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `Covariance Edge` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `Adjoint Mapping` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `Composed World Model` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |
| `Query Plane` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#6-units`](WORLD_MODEL.md#6-units) | none |

## 14. Graph-native ODD

Context declared by [ODD §1](ODD.md#1-position) (P3). `F_D`, `F_P` and
`F_H` are also indexed in the axiomatic-calculus context in §4; the two
rows create no identity between the contexts (P1).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `ODD`; `Outcome-Driven Development` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | none |
| `GTL`; `Graph Transformation Language` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | none |
| `ABG` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#1-position`](ODD.md#1-position) | [`ODD.md#abg`](ODD.md#abg) |
| `Edge Traversal`; `Traversal` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#traversal`](ODD.md#traversal) | none |
| `Probabilistic Compute` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | none |
| `F_D` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | none |
| `F_P` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |
| `F_H` | `urn:stdo:bounded-context:graph-native-odd` | [`ODD.md#probabilistic-compute`](ODD.md#probabilistic-compute) | [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |

## 15. Traversal occurrence

Context declared by
[TRAVERSAL_OCCURRENCE Position](TRAVERSAL_OCCURRENCE.md#position) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Traversal Occurrence Profile`; `Sigma_occurrence` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#position`](TRAVERSAL_OCCURRENCE.md#position) | [`TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary`](TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary) |
| `Occurrence` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#occurrence-identity`](TRAVERSAL_OCCURRENCE.md#occurrence-identity) | none |
| `Framework Event` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#candidate-judgment-event-and-relation-separation`](TRAVERSAL_OCCURRENCE.md#candidate-judgment-event-and-relation-separation) | none |
| `Typed Lineage` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#causality-and-typed-lineage`](TRAVERSAL_OCCURRENCE.md#causality-and-typed-lineage) | none |
| `Mutable Subject` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation`](TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation) | none |
| `Event Frontier` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#event-frontier-and-projection`](TRAVERSAL_OCCURRENCE.md#event-frontier-and-projection) | none |
| `Traversal Occurrence Profile Basis` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#exact-profile-identity`](TRAVERSAL_OCCURRENCE.md#exact-profile-identity) | none |

## 16. Source dispositions

Rows of rc.2 GLOSSARY_GUIDE.md. Anchors are into rc.2 GLOSSARY_GUIDE.md; a
locus is a section of this file. Every conserved row is restated in this
member's own text; a route is provenance only. An index section is
conserved when every predecessor row in it is indexed here with its
bounded-context identity unchanged and its locus moved to the successor
clause that owns the concept; the predecessor's owner moves are recorded
per row. Generalisations recorded here: the predecessor's section titles
drop "Index"; "the selected complete STDO release" is written "the
selected complete STDO basis"; the predecessor's reference to
`SPEC_METHOD.md#bounded-context-semantic-resolution` is written as
PRODUCT_DEFINITION §5, its successor owner.

| Anchor | Disposition | Locus |
|---|---|---|
| #index-contract | conserved; no definitions and the seven things not declared, non-deciding index into owning clauses of the selected basis, the three row elements, candidate meaning and governed scope, invalid unresolvable rows, intentional repetition and the five non-implications, resolution with no fallback; the locator law of §2 states how rows route here | §1; §2 |
| #method-identity-index | conserved; both terms in the method-identity context at SPEC_METHOD §1; the `O` relation clause at ODD §1, successor of rc.2 ODD_METHOD #1-position | §3 |
| #axiomatic-calculus-index | conserved; all fourteen rows in the axiomatic-calculus context at the tenant's AXIOMATIC_CALCULUS sections | §4 |
| #traversal-occurrence-profile-index | conserved; all seven rows in the traversal-occurrence-profile context at the same-named sections of TRAVERSAL_OCCURRENCE, which declares the context in its Position, with the imported-calculus relation | §15 |
| #semantic-resolution-index | conserved; all eight terms, owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §5 | §5 |
| #product-definition-routing-index | conserved; all eleven terms, owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §1, §3, §4 and §7 | §6 |
| #release-publication-index | conserved; all seven terms at RELEASE §2 | §7 |
| #reference-frame-evaluation-index | conserved; the reference frame owned in the context by REFERENCE_FRAME §1, whose statement of ownership includes the frame objects of FOUNDATIONS §2 at their defining locus, now the relation clause; both specialist families at EXECUTIVE_BASELINE §11; the successor's other frame objects and result algebra added under the same inclusion | §8 |
| #build-tenancy-index | conserved; four rows owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §8, the work-item row at TICKETS §4 | §9 |
| #recursive-product-index | conserved; all eight terms, owner moved from rc.2 SPEC_METHOD to FOUNDATIONS §2 Product lineage objects | §10 |
| #product-assurance-index | conserved; five rows owner moved from rc.2 SPEC_METHOD to ASSURANCE §2, `Unit Test` from rc.2 DESIGN_MODULE_METHOD to ASSURANCE §15 with DESIGN_MODULE as relation | §11 |
| #graph-native-odd-index | conserved; all eight rows in the graph-native-odd context at ODD §1 and §5, the ABG relation at ODD §10, the `F_P` and `F_H` relation at SPEC_METHOD §5 (rc.2 #ambiguity-governance-rule); `F_D`, `F_P`, `F_H` also keep their axiomatic-calculus row | §14 |
| #ambiguity-governance-index | conserved; both terms at SPEC_METHOD §5 | §12 |
| #world-model-index | conserved; all nine terms at WORLD_MODEL §6, the Builder Project relation at its specialisation clause | §13 |
