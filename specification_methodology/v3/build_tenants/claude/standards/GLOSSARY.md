# GLOSSARY

Guide. A non-deciding locator index from indexed spellings to the clauses
of this corpus that declare their bounded contexts and own their concepts.
It realises the glossary that
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
names and adds nothing to that law. Its loci were generated from the
members' headings at this member's activation (P3). Every clause names the principle that
requires it (P0 to P6, FOUNDATIONS §3). A route written `rc.2 #anchor` is
into `stdo://releases/v2.5.1-rc.2/standards/GLOSSARY_GUIDE.md` and is
provenance only; nothing here depends on that cut to be applied.

## 1. Index contract

This member contains no semantic definition. It declares no bounded
context, concept, import, translation, equivalence, disambiguation or
authority. It is a non-deciding index into the clauses that own those
meanings in the selected complete STDO basis (P6, P1; rc.2
#index-contract).

Each row records an indexed spelling, the bounded-context identity that a
cited clause declares, and the exact owning concept clause. The owning
clause together with the selected basis identifies the candidate meaning;
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
section names the clause that declares its context. Where that clause and
the owning concept clause differ, the row records both and decides no
owner relation between them (P6, P1). The relation clause, where given,
points to a clause that relates the concept to another member or context;
the index states no relation itself (P1, P6).

A term with an owning clause and no context declared for it, or a term
whose owning member does not yet exist in this corpus, is not a valid row
under §1. Such terms are listed in §14 and §15 so that their owners can
act; the lists locate the gap and resolve no meaning (P5, P6).

## 3. Method identity

Context declared by
[SPEC_METHOD §1 Method identity](SPEC_METHOD.md#method-identity) (P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `STDO` | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | none |
| `O` pillar symbol | `urn:stdo:bounded-context:method-identity` | [`SPEC_METHOD.md#method-identity`](SPEC_METHOD.md#method-identity) | [`PROFILES.md#2-graph-execution`](PROFILES.md#2-graph-execution) |

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
which names frame declaration, activation, evaluation, basis, relation,
result, coverage, revision and qualification as its own concepts (P3,
P6). [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects) defines
the reference frame and the objects it binds, and
[ACTIVATION §3](ACTIVATION.md#3-result-algebra) defines the result
algebra; neither declares a context. The rows below cover the frame
objects and result members that §1's list names and the concepts defined
in REFERENCE_FRAME's own text; the other frame objects and the result
refinements are in §14 (P6, P1).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Reference Frame`; `Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) |
| `Frame Tuple` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#the-frame-tuple`](FOUNDATIONS.md#the-frame-tuple) | [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) |
| `Frame Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) | none |
| `Frame-Set Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#4-frame-set-declaration`](REFERENCE_FRAME.md#4-frame-set-declaration) | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) |
| `Activated Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) |
| `Activation Packet` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) | [`ACTIVATION.md#1-the-step`](ACTIVATION.md#1-the-step) |
| `Evaluation` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | none |
| `Engagement Atom`; `Semantic Atom` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#engagement-atom-and-semantic-atom`](REFERENCE_FRAME.md#engagement-atom-and-semantic-atom) | none |
| `Coverage Ledger` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#coverage-ledger`](REFERENCE_FRAME.md#coverage-ledger) | none |
| `Result Algebra` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra) | [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results); [`AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) |
| `satisfied`; `falsified`; `indeterminate`; `out_of_frame`; `invalid_basis` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra) | [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results) |
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

## 14. Terms awaiting a context declaration

These terms have an owning clause in this corpus, and no clause declares a
bounded context for them: FOUNDATIONS §2 and ACTIVATION declare none, and
REFERENCE_FRAME §1's list of its own concepts does not name them. Under §1
they are not valid rows. The owners of FOUNDATIONS, ACTIVATION and
REFERENCE_FRAME decide whether a declaration covers them (P5, P6).

| Term | Owning clause | What is missing |
|---|---|---|
| `Evaluation Family`; `Workspace`; `Material-Relation Manifold`; `Coordinate`; `Topology`; `Capability Envelope`; `Frame Set`; `Active Frame Configuration`; `Lens`; `Role`, `Persona`, `Abstraction`, `Component` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | a bounded-context declaration that names the concept |
| construction availability: `candidate_ready`; `refused`; `incomplete`; `re_entry_requested` | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra) | a bounded-context declaration that names the refinement |
| disposition: `accept`; `local_repair`; `re_enter`; `reject` | [`ACTIVATION.md#disposition`](ACTIVATION.md#disposition) | a bounded-context declaration that names the refinement |
| ambiguity outcome: `resolved`; `carried`; `escalated`; `blocked` | [`ACTIVATION.md#3-result-algebra`](ACTIVATION.md#3-result-algebra) | a bounded-context declaration that names the refinement; [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) cites it and does not claim it |

## 15. Terms awaiting an owning member

The predecessor indexed these terms in the contexts
`urn:stdo:bounded-context:graph-native-odd` and
`urn:stdo:bounded-context:traversal-occurrence-profile`. The members that
receive those profiles, ODD and TRAVERSAL_OCCURRENCE, are not yet in this
corpus, and no clause here declares either context. PROFILES §2 names the
graph-execution profile and does not declare its context. Under §1 no row
can be written; the rows are written when those members exist (P5, P6).
`F_D`, `F_P` and `F_H` are indexed in the axiomatic-calculus context in
§4; that row creates no graph-native meaning (P1).

| Predecessor context | Terms |
|---|---|
| graph-native ODD | `ODD`; `Outcome-Driven Development`; `GTL`; `Graph Transformation Language`; `ABG`; `Edge Traversal`; `Traversal`; `Probabilistic Compute`; `F_D`; `F_P`; `F_H` |
| traversal occurrence | `Traversal Occurrence Profile`; `Sigma_occurrence`; `Occurrence`; `Framework Event`; `Typed Lineage`; `Mutable Subject`; `Event Frontier`; `Traversal Occurrence Profile Basis` |

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
| #method-identity-index | conserved; both terms in the method-identity context at SPEC_METHOD §1; the `O` relation clause moves from rc.2 ODD_METHOD to PROFILES §2, which names the graph-execution profile | §3 |
| #axiomatic-calculus-index | conserved; all fourteen rows in the axiomatic-calculus context at the tenant's AXIOMATIC_CALCULUS sections | §4 |
| #traversal-occurrence-profile-index | unresolved: the receiving member TRAVERSAL_OCCURRENCE is not yet written and no clause of this corpus declares `urn:stdo:bounded-context:traversal-occurrence-profile`, so under §1 no row can resolve; the seven rows' terms are listed pending | §15 |
| #semantic-resolution-index | conserved; all eight terms, owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §5 | §5 |
| #product-definition-routing-index | conserved; all eleven terms, owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §1, §3, §4 and §7 | §6 |
| #release-publication-index | conserved; all seven terms at RELEASE §2 | §7 |
| #reference-frame-evaluation-index | conserved; the reference frame at FOUNDATIONS §2 Frame objects with REFERENCE_FRAME §1 declaring the context, both specialist families at EXECUTIVE_BASELINE §11 | §8 |
| #build-tenancy-index | conserved; four rows owner moved from rc.2 SPEC_METHOD to PRODUCT_DEFINITION §8, the work-item row at TICKETS §4 | §9 |
| #recursive-product-index | conserved; all eight terms, owner moved from rc.2 SPEC_METHOD to FOUNDATIONS §2 Product lineage objects | §10 |
| #product-assurance-index | conserved; five rows owner moved from rc.2 SPEC_METHOD to ASSURANCE §2, `Unit Test` from rc.2 DESIGN_MODULE_METHOD to ASSURANCE §15 with DESIGN_MODULE as relation | §11 |
| #graph-native-odd-index | unresolved: the receiving member ODD is not yet written and no clause of this corpus declares `urn:stdo:bounded-context:graph-native-odd`, so under §1 no row can resolve; the eight rows' terms are listed pending, and `F_D`, `F_P`, `F_H` keep their axiomatic-calculus row | §15 |
| #ambiguity-governance-index | conserved; both terms at SPEC_METHOD §5 | §12 |
| #world-model-index | conserved; all nine terms at WORLD_MODEL §6, the Builder Project relation at its specialisation clause | §13 |
