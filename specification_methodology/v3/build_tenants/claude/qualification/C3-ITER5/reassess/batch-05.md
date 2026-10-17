# I5-03 reading batch 05

Rows: 25. Members: ['GLOSSARY_GUIDE.md', 'IDENTITY_METHOD.md', 'ODD_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `GLOSSARY_GUIDE.md#reference-frame-evaluation-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#reference-frame-evaluation-index` at rc.2:

```text
## Reference-Frame Evaluation Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Reference Frame`; `Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME_METHOD.md#reference-frame`](REFERENCE_FRAME_METHOD.md#reference-frame) |
| `Product` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set`](STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set) |
| `Owner` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set`](STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set) |
```

Successor, `GLOSSARY.md#8-reference-frame-evaluation`:

```text
## 8. Reference-frame evaluation

Context declared by
[REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit)
(P3). Its import declaration,
[Imports into this context](REFERENCE_FRAME.md#imports-into-this-context),
holds in the context the frame objects, ontology objects, authority kinds,
disjointness and frame tuple of FOUNDATIONS §2, the core results and their
conjunction of FOUNDATIONS §4, the step with its result refinements and
the closed result of ACTIVATION §1 to §3 and §7, and the qualification of
EVALUATION §7, each kept by its owner. A row for an imported concept cites
its owning section as owning concept clause and the import declaration as
relation clause (§2; P1, P6).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Reference Frame`; `Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit`](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) |
| `Frame Tuple` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#the-frame-tuple`](FOUNDATIONS.md#the-frame-tuple) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) |
| `Frame Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#minimal-frame-declaration`](REFERENCE_FRAME.md#minimal-frame-declaration) | none |
| `Frame-Set Declaration` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#4-frame-set-declaration`](REFERENCE_FRAME.md#4-frame-set-declaration) | [`PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis) |
| `Activated Frame` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) |
| `Activation Packet` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#11-the-activation-packet`](REFERENCE_FRAME.md#11-the-activation-packet) | [`ACTIVATION.md#1-the-step`](ACTIVATION.md#1-the-step) |
| `Evaluation` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| `Evaluation Family`; `Workspace`; `Material-Relation Manifold`; `Coordinate`; `Topology`; `Capability Envelope`; `Frame Set`; `Active Frame Configuration`; `Lens`; `Role`, `Persona`, `Abstraction`, `Component` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#frame-objects`](FOUNDATIONS.md#frame-objects) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| `Actor Identity` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#authority-kinds`](FOUNDATIONS.md#authority-kinds) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`SPEC_METHOD.md#11-build-tenant-binding`](SPEC_METHOD.md#11-build-tenant-binding) |
| `Engagement Atom`; `Semantic Atom` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#engagement-atom-and-semantic-atom`](REFERENCE_FRAME.md#engagement-atom-and-semantic-atom) | none |
| `Communication` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy`](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy) | [`ACTIVATION.md#configuration`](ACTIVATION.md#configuration) |
| `activate` outcome: `activated_frame`; `activation_refusal(capability)`; `activation_refusal(authority)`; `activation_refusal(basis)` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#5-method-functions`](REFERENCE_FRAME.md#5-method-functions) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| `conjoin` outcome: `decision(holds)`; `decision(fails)`; `conflict`; `indeterminate` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#5-method-functions`](REFERENCE_FRAME.md#5-method-functions) | [`FOUNDATIONS.md#conjunction-of-results`](FOUNDATIONS.md#conjunction-of-results) |
| `translate` outcome: `translated_value`; `declared_loss`; `refusal(condition)`; `refusal(authority)`; `refusal(basis)` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#5-method-functions`](REFERENCE_FRAME.md#5-method-functions) | [`REFERENCE_FRAME.md#evidence-or-coordinate-translation`](REFERENCE_FRAME.md#evidence-or-coordinate-translation) |
| `Coverage Ledger` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#coverage-ledger`](REFERENCE_FRAME.md#coverage-ledger) | none |
| coverage status: `covered`; `separately_covered`; `excluded_by_authority`; `conditionally_covered`; `conflicted`; `uncovered`; `unknown` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`REFERENCE_FRAME.md#coverage-ledger`](REFERENCE_FRAME.md#coverage-ledger) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| `Result Algebra`; core result algebra | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results); [`AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) |
| `satisfied`; `falsified`; `indeterminate`; `out_of_frame`; `invalid_basis` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results) |
| not performed, an evaluation with no closed result; refinement of the core | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| further refinement; parent value; child value; parent-value rule | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| conjunction of results; declared decision rule; composition of results | `urn:stdo:bounded-context:reference-frame-evaluation` | [`FOUNDATIONS.md#conjunction-of-results`](FOUNDATIONS.md#conjunction-of-results) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#result-conjunction`](REFERENCE_FRAME.md#result-conjunction) |
| size measurement | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#2-context-construction-under-an-envelope`](ACTIVATION.md#2-context-construction-under-an-envelope) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#rf-002-finite-attention`](REFERENCE_FRAME.md#rf-002-finite-attention) |
| admission and activation: `activated`; `admission_refused(authority)`; `admission_refused(basis)`; `closure_unresolved` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#admission-and-activation`](ACTIVATION.md#admission-and-activation) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#5-method-functions`](REFERENCE_FRAME.md#5-method-functions) |
| construction availability: `candidate_ready`; `refused`; `incomplete`; `re_entry_requested(authority)`; `re_entry_requested(basis)` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#construction-availability`](ACTIVATION.md#construction-availability) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| disposition: `accept`; `local_repair`; `re_enter`; `reject` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#disposition`](ACTIVATION.md#disposition) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| ambiguity outcome: `resolved`; `carried`; `escalated`; `blocked` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#ambiguity-outcome`](ACTIVATION.md#ambiguity-outcome) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle`](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle) |
| effects: `completed`; `not_effected`; `completion_unknown` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#effects`](ACTIVATION.md#effects) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context) |
| `Closed Result` | `urn:stdo:bounded-context:reference-frame-evaluation` | [`ACTIVATION.md#7-closed-result-and-reuse`](ACTIVATION.md#7-closed-result-and-reuse) | [`REFERENCE_FRAME.md#imports-into-this-context`](REFERENCE_FRAME.md#imports-into-this-context); [`REFERENCE_FRAME.md#rf-012-closed-results`](REFERENCE_FRAME.md#rf-012-closed-results) |
| `Product` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`](EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set) | none |
| `Owner` specialist frame family | `urn:stdo:bounded-context:reference-frame-evaluation` | [`EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`](EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set) | none |
```


### Row `GLOSSARY_GUIDE.md#release-publication-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#release-publication-index` at rc.2:

```text
## Release-Publication Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Project Release Namespace` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `Project Subtree` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `Candidate Source` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `RC Branch` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `Immutable RC Cut` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `Version-Line Selector` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
| `Release Branch` | `urn:stdo:bounded-context:release-publication` | [`RELEASE_METHOD.md#release-identities`](RELEASE_METHOD.md#release-identities) |
```

Successor, `GLOSSARY.md#7-release-publication`:

```text
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
```


### Row `GLOSSARY_GUIDE.md#semantic-resolution-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#semantic-resolution-index` at rc.2:

```text
## Semantic Resolution Index

| Indexed term | Bounded-context identity | Owning concept clause |
|---|---|---|
| `Term` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Concept Reference` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Bounded Context` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Semantic Address` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Semantic Import` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Semantic Translation` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Semantic Equivalence` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
| `Semantic Disambiguation` | `urn:stdo:bounded-context:semantic-resolution` | [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution) |
```

Successor, `GLOSSARY.md#5-semantic-resolution`:

```text
## 5. Semantic resolution

Context declared by
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
(P3).

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Term` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Concept Reference` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Bounded Context` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Semantic Address` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Semantic Import` | `urn:stdo:bounded-context:semantic-resolution` | [`FOUNDATIONS.md#imports-between-members`](FOUNDATIONS.md#imports-between-members) | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), which applies the import between bounded contexts |
| `Semantic Translation` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Semantic Equivalence` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
| `Semantic Disambiguation` | `urn:stdo:bounded-context:semantic-resolution` | [`PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution`](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | none |
```


### Row `GLOSSARY_GUIDE.md#traversal-occurrence-profile-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#traversal-occurrence-profile-index` at rc.2:

```text
## Traversal-Occurrence-Profile Index

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Traversal Occurrence Profile`; `Sigma_occurrence` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#position`](TRAVERSAL_OCCURRENCE_PROFILE.md#position) | [`TRAVERSAL_OCCURRENCE_PROFILE.md#imported-calculus-boundary`](TRAVERSAL_OCCURRENCE_PROFILE.md#imported-calculus-boundary) |
| `Occurrence` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#occurrence-identity`](TRAVERSAL_OCCURRENCE_PROFILE.md#occurrence-identity) | — |
| `Framework Event` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation`](TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation) | — |
| `Typed Lineage` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#causality-and-typed-lineage`](TRAVERSAL_OCCURRENCE_PROFILE.md#causality-and-typed-lineage) | — |
| `Mutable Subject` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation`](TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation) | — |
| `Event Frontier` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#event-frontier-and-projection`](TRAVERSAL_OCCURRENCE_PROFILE.md#event-frontier-and-projection) | — |
| `Traversal Occurrence Profile Basis` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE_PROFILE.md#exact-profile-identity`](TRAVERSAL_OCCURRENCE_PROFILE.md#exact-profile-identity) | — |
```

Successor, `GLOSSARY.md#15-traversal-occurrence`:

```text
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
| stop and decision values split by cause: `refusal(constraint)`; `refusal(basis)`; `refused(constraint)`; `refused(basis)`; `partial_effect(not_attained)`; `partial_effect(undecided)`; `partial(not_attained)`; `partial(undecided)` | `urn:stdo:bounded-context:traversal-occurrence-profile` | [`TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds`](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds) | [`AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal); [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
```


### Row `GLOSSARY_GUIDE.md#world-model-index` (disposition `conserved`)

Predecessor, `GLOSSARY_GUIDE.md#world-model-index` at rc.2:

```text
## World-Model Index

| Indexed term | Bounded-context identity | Owning concept clause | Relation clause |
|---|---|---|---|
| `Builder Project` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#builder-project`](WORLD_MODEL_METHOD.md#builder-project) | [`WORLD_MODEL_METHOD.md#builder-project-specialization-relation`](WORLD_MODEL_METHOD.md#builder-project-specialization-relation) |
| `Published Domain Artifact` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#published-domain-artifact`](WORLD_MODEL_METHOD.md#published-domain-artifact) | — |
| `World Model Object` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#world-model-object`](WORLD_MODEL_METHOD.md#world-model-object) | — |
| `Markov Object` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#markov-object`](WORLD_MODEL_METHOD.md#markov-object) | — |
| `Treatment Surface` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#treatment-surface`](WORLD_MODEL_METHOD.md#treatment-surface) | — |
| `Covariance Edge` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#covariance-edge`](WORLD_MODEL_METHOD.md#covariance-edge) | — |
| `Adjoint Mapping` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#adjoint-mapping`](WORLD_MODEL_METHOD.md#adjoint-mapping) | — |
| `Composed World Model` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#composed-world-model`](WORLD_MODEL_METHOD.md#composed-world-model) | — |
| `Query Plane` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL_METHOD.md#query-plane`](WORLD_MODEL_METHOD.md#query-plane) | — |
```

Successor, `GLOSSARY.md#13-world-model`:

```text
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
| cut admissibility: `cut_admissible`; `cut_inadmissible`; `discrimination_undecided` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| direction acceptance: `direction_verified`; `extraction_inadmissible`; `verification_failed`; `verification_inconclusive`; `representation_space_invalid` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| overlay publication: `published_verified`; `published_unverified` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| overlay storage: `storage_retained`; `storage_lossy` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| null-peer discrimination: `null_peer_discriminated`; `not_yet_lawful` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| promotion gate: `gate_met`; `gate_not_met` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
| saturation: `saturated`; `not_saturated` | `urn:stdo:bounded-context:world-model` | [`WORLD_MODEL.md#14-results-of-this-profile`](WORLD_MODEL.md#14-results-of-this-profile) | [`FOUNDATIONS.md#results`](FOUNDATIONS.md#results) |
```


### Row `IDENTITY_METHOD.md#1-scoped-identity` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#1-scoped-identity` at rc.2:

```text
### 1. Scoped Identity

Identity is always scoped.

At minimum, identity should be interpretable through:

- authority
- kind
- value

So the minimum semantic model is:

`identity = authority + kind + value`

Optional additional coordinates may include:

- parent scope
- revision
- publication version
- temporal coordinates
```

Successor, `IDENTITY.md#scoped-identity`:

```text
### Scoped identity

Identity is always scoped. At minimum, identity should be interpretable
through authority, kind and value. So the minimum semantic model is:

```text
identity = authority + kind + value
```

This is the scoped identity of an Object (FOUNDATIONS §2). Optional
additional coordinates may include parent scope, revision, publication
version and temporal coordinates (P3; rc.2 #1-scoped-identity).
```


### Row `IDENTITY_METHOD.md#consequence-for-implementations` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#consequence-for-implementations` at rc.2:

```text
## Consequence For Implementations

Implementations should prefer:

- typed identity readers
- explicit identity-kind distinctions
- source-of-authority parsing contracts

They should avoid:

- broad regex mining as the real identity model
- silent coercion between family ids and concrete ids
- leaking engine id grammar into domain semantics

If a project currently relies on those patterns, the first lawful repair is to
contain the immediate bug. The enduring repair is to publish explicit identity
law and move implementations onto it.
```

Successor, `IDENTITY.md#12-consequence-for-implementations`:

```text
## 12. Consequence for implementations

Implementations should prefer typed identity readers, explicit
identity-kind distinctions, and source-of-authority parsing contracts.
They should avoid broad regex mining as the real identity model, silent
coercion between family identities and concrete identities, and leaking
engine identity grammar into domain semantics (P3, P1;
rc.2 #consequence-for-implementations).

If a project currently relies on those patterns, the first lawful repair
is to contain the immediate bug. The enduring repair is to publish
explicit identity law and move implementations onto it (P3, P0).
```


### Row `IDENTITY_METHOD.md#defaults-from-a-bound-abg-realization` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#defaults-from-a-bound-abg-realization` at rc.2:

```text
### Defaults From A Bound ABG Realization

A consumer-bound realization of the ABG role may publish default identity
generators, validators, and normalizers for its own runtime surfaces and for
common default ODD surface kinds used by default `F_D` helpers.

These defaults are:

- starter conventions
- convenience contracts
- not universal doctrine

They are lawful only so long as derived domains may override them.
```

Successor, `DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation`:

```text
### Identity defaults from a bound runtime realisation

A consumer-bound realisation of the ABG role under the graph-execution
profile may publish default identity generators, validators and
normalisers for its own runtime surfaces and for the default ODD surface
kinds used by default `F_D` helpers; the permission is scoped to that role
and does not extend to other runtime realisations (P3, P6; provenance rc.2
IDENTITY_METHOD #defaults-from-a-bound-abg-realization). Their standing as
defaults and the identity law of their override, its preservation
conditions and its publication surface are
[IDENTITY §7](IDENTITY.md#7-default-formats-and-overrides).
```

Successor, `IDENTITY.md#derived-domain-overrides`:

```text
### Derived domain overrides

Default identity formats that a bound runtime realisation publishes are
starter conventions and convenience contracts, not universal doctrine;
they are lawful only so long as derived domains may override them (P3,
P6). What such a realisation publishes, and for which surfaces, is
realisation law outside this member
([DESIGN_MODULE §12](DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation)).

Derived domains may override identity format and structure for their own
kinds. An override is lawful only if it preserves (P3;
rc.2 #derived-domain-overrides):

- scoped uniqueness;
- explicit kind distinction;
- deterministic parsing or reading;
- non-aliasing between family and member identities; and
- stable downstream traceability.

Overrides are published in domain authority. They do not exist only as
ad hoc regex assumptions hidden in implementation code (P6, P3).
```


### Row `IDENTITY_METHOD.md#engine-owned-identity` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#engine-owned-identity` at rc.2:

```text
### Engine-Owned Identity

The substrate or runtime may define default identities for runtime-owned
objects, such as:

- runs
- graph calls
- jobs
- frames
- continuations
- events

For these, the engine may use opaque ids and engine-local generation rules.

Those rules should optimize for:

- uniqueness
- replay safety
- event-stream integrity

The engine should not impose domain-specific semantic grammar on domain-owned
objects.
```

Successor, `IDENTITY.md#engine-owned-identity`:

```text
### Engine-owned identity

The substrate or runtime may define default identities for runtime-owned
objects, such as runs, function calls, jobs, execution frames,
continuations and events. For these, the engine may use opaque identities and engine-local
generation rules. Those rules should optimise for uniqueness, replay
safety and event-stream integrity. The engine should not impose
domain-specific semantic grammar on domain-owned objects (P3, P6;
rc.2 #engine-owned-identity).
```


### Row `IDENTITY_METHOD.md#human-readable-vs-opaque-identity` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#human-readable-vs-opaque-identity` at rc.2:

```text
## Human-Readable vs Opaque Identity

Identity may be:

- opaque, such as a GUID or UUID
- human-readable, such as `REQ-F-CAPABILITY-001`
- hybrid, where one component is readable and another is opaque

The governing rule is:

- readability is a convenience for recognition
- uniqueness and scoped meaning are the actual law

Therefore:

- a GUID is lawful even when it carries no human meaning
- a readable id is lawful only if it still preserves uniqueness in scope
- no reader should infer that a readable id is safer or more authoritative than
  an opaque one merely because it looks meaningful

---
```

Successor, `IDENTITY.md#3-readable-and-opaque-identity`:

```text
## 3. Readable and opaque identity

Identity may be opaque, such as a GUID or UUID; human-readable, such as
`REQ-F-CAPABILITY-001`; or hybrid, where one component is readable and
another is opaque. The governing rule is that readability is a
convenience for recognition, and uniqueness and scoped meaning are the
actual law (P3, P1; rc.2 #human-readable-vs-opaque-identity). Therefore:

- a GUID is lawful even when it carries no human meaning;
- a readable identity is lawful only if it still preserves uniqueness in
  scope; and
- no reader should infer that a readable identity is safer or more
  authoritative than an opaque one merely because it looks meaningful.
```


### Row `IDENTITY_METHOD.md#identity-hierarchy` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#identity-hierarchy` at rc.2:

```text
## Identity Hierarchy

Identity should be made unique by hierarchy where appropriate.

One useful general model is:

`authority / kind / value / revision`

Not every serialization needs all four visible segments, but the semantic model
should be available.

Examples:

- `(<product-authority>, requirement, REQ-F-CAPABILITY-001)`
- `(<product-authority>, requirement_family, REQ-F-CAPABILITY)`
- `(<runtime-authority>, run, 550e8400-e29b-41d4-a716-446655440000)`
- `(<release-authority>, release, 1.0.0-rc.1)`

The important point is that:

- `REQ-F-CAPABILITY` and `REQ-F-CAPABILITY-001` are not the same kind of
  identity
- a runtime `run_id` and a domain requirement id do not belong to the same
  semantic category even if both serialize as strings

---
```

Successor, `IDENTITY.md#4-identity-hierarchy`:

```text
## 4. Identity hierarchy

Identity should be made unique by hierarchy where appropriate. One useful
general model is:

```text
authority / kind / value / revision
```

Not every serialisation needs all four visible segments, but the semantic
model should be available (P3; rc.2 #identity-hierarchy). Examples:

- `(<product-authority>, requirement, REQ-F-CAPABILITY-001)`
- `(<product-authority>, requirement_family, REQ-F-CAPABILITY)`
- `(<runtime-authority>, run, 550e8400-e29b-41d4-a716-446655440000)`
- `(<release-authority>, release, 1.0.0-rc.1)`

The important point is that `REQ-F-CAPABILITY` and `REQ-F-CAPABILITY-001`
are not the same kind of identity, and that a runtime `run_id` and a
domain requirement identity do not belong to the same semantic category
even if both serialise as strings (P3).
```


### Row `IDENTITY_METHOD.md#lawful` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#lawful` at rc.2:

```text
### Lawful

- runtime event ids generated as UUIDs by a consumer-bound realization of the
  ABG role
- requirement ids such as `REQ-F-CAPABILITY-001` when the domain defines them as
  concrete `requirement` identities
- family ids such as `REQ-F-CAPABILITY` when the domain defines them separately as
  `requirement_family`
- acceptance-criterion ids such as `REQ-F-CAPABILITY-001-AC-01` when the domain
  defines them as a separate `acceptance_criterion` identity kind
```

Successor, `IDENTITY.md#lawful`:

```text
### Lawful

Lawful (P3; rc.2 #lawful):

- runtime event identities generated as UUIDs by a consumer-bound runtime
  realisation;
- requirement identities such as `REQ-F-CAPABILITY-001` when the domain
  defines them as concrete `requirement` identities;
- family identities such as `REQ-F-CAPABILITY` when the domain defines
  them separately as `requirement_family`; and
- acceptance-criterion identities such as `REQ-F-CAPABILITY-001-AC-01`
  when the domain defines them as a separate `acceptance_criterion`
  identity kind.
```


### Row `IDENTITY_METHOD.md#minimum-questions` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#minimum-questions` at rc.2:

```text
## Minimum Questions

When defining or auditing an identity surface, ask:

1. What authority owns this identity?
2. What kind of thing does this identity denote?
3. What scope makes it unique?
4. Is the identity stable enough for the governed lifecycle?
5. Is the readable form only convenience, or is it being over-trusted?
6. Can a parser distinguish families, members, aliases, and revisions without
   ambiguity?
7. Is this an engine/runtime id, a domain semantic id, or a release id?

If those questions cannot be answered, the identity surface is under-defined.

---
```

Successor, `IDENTITY.md#10-minimum-questions`:

```text
## 10. Minimum questions

When defining or auditing an identity surface, ask (P3, P6;
rc.2 #minimum-questions):

1. What authority owns this identity?
2. What kind of thing does this identity denote?
3. What scope makes it unique?
4. Is the identity stable enough for the governed lifecycle?
5. Is the readable form only convenience, or is it being over-trusted?
6. Can a parser distinguish families, members, aliases and revisions
   without ambiguity?
7. Is this an engine or runtime identity, a domain semantic identity, or
   a release identity?

If those questions cannot be answered, the identity surface is
under-defined (P3).
```


### Row `IDENTITY_METHOD.md#unlawful` (disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#unlawful` at rc.2:

```text
### Unlawful

- treating `REQ-F-CAPABILITY-*` or `REQ-F-CAPABILITY` as a concrete requirement merely
  because a broad regex matched it
- using release version as the identity of every live source object
- assuming a readable string is globally unique without its authority and kind

---
```

Successor, `IDENTITY.md#unlawful`:

```text
### Unlawful

Unlawful (P3; rc.2 #unlawful):

- treating `REQ-F-CAPABILITY-*` or `REQ-F-CAPABILITY` as a concrete
  requirement merely because a broad regex matched it;
- using release version as the identity of every live source object; and
- assuming a readable string is globally unique without its authority
  and kind.
```


### Row `ODD_METHOD.md#1-position` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#1-position` at rc.2:

```text
## 1. Position

`ODD_METHOD.md` exists to make one instruction precise:

`using ODD_METHOD, build this product`

That instruction should mean something stronger than:

- write some product docs
- sketch a graph
- add a few helper scripts

It means:

- build the product as a GTL/ABG domain product
- define typed domain assets and nodes
- publish named graph functions as the constructive carrier
- bind them into a GTL module
- let ABG own traversal governance, runtime facts, and provenance
- let ABG own continuation and re-entry after each publish boundary
- keep product commands and services as cooperative bounded-step subsystems that
  publish assets or evidence and return control to ABG
- expose visible current state as projection over constructive history

This is a programming paradigm, not only a documentation preference.

The paradigm is:

`product = typed asset/domain model + GTL-defined graph functions + ABG traversal-control runtime + governed projection/query surfaces`

If the constructive carrier remains hidden in imperative loops, local service logic, or product-specific orchestration scripts, the product is not yet built using ODD method.

Within this method, `ODD`, `GTL`, and `ABG` name normative capability roles
and construction algebra, not a required repository, package, vendor, or
concrete implementation:

- `ODD` means **Outcome-Driven Development** and names the graph-native
  product-authoring profile;
- `GTL` means **Graph Transformation Language** and names the typed declarative
  graph-language role; and
- `ABG` names the singular traversal-governance and runtime-truth authority
  role.

`ODD_METHOD.md` owns those concepts in the graph-native bounded context
`urn:stdo:bounded-context:graph-native-odd` under the selected complete STDO
basis. The context covers the ODD product shape, GTL language role, ABG method
role, graph assets, vectors, functions, traversals, and graph/runtime worker and
evaluator shorthands defined by this standard. It does not absorb a consuming
Product's domain semantics or a concrete runtime's same-spelled carriers.

A consumer binds those roles to concrete conforming realizations in its own
Product, requirements, design, and immutable dependency identity. A consumer,
reference realization, or historical product may prove or falsify conformance;
it does not supply method authority.

The method has two core jobs:

1. describe the product as a declared asset graph in graph-native terms
2. ensure automation never outruns a lawful manual traversal of the same graph

The graph is not decoration around the process. The graph is the process model. GTL is the language expression of the method. ABG is the traversal governance, binding, and runtime-truth substrate that realizes the GTL program without owning the domain's internal HOW.

---
```

Successor, `ODD.md#1-position`:

```text
## 1. Position

This profile makes one instruction precise: `using ODD, build this
product`. The instruction should mean something stronger than writing
product documents, sketching a graph or adding a few helper scripts (P0,
P2). It means:

- build the product as a GTL/ABG domain product;
- define typed domain assets and nodes;
- publish named graph functions as the constructive carrier;
- bind them into a GTL module;
- let ABG own traversal governance, runtime facts and provenance;
- let ABG own continuation and re-entry after each publish boundary;
- keep product commands and services as cooperative bounded-step
  subsystems that publish assets or evidence and return control to ABG;
- expose visible current state as a projection over constructive history.

ODD is a programming paradigm, not only a documentation preference. Its form
is `product = typed asset/domain model + GTL-defined graph functions + ABG
traversal-control runtime + governed projection/query surfaces`. A product
whose constructive carrier stays hidden in imperative loops, local service
logic or product-specific orchestration scripts is not yet built with this
profile (P0, P6).

ODD, GTL and ABG name normative capability roles and a construction
algebra, not a required repository, package, vendor or concrete
implementation. ODD, Outcome-Driven Development, names the graph-native
product-authoring profile. GTL, Graph Transformation Language, names the
role of the typed declarative graph language. ABG names the role of the
singular traversal-governance and runtime-truth authority (P1, P6).

This profile owns those concepts in the graph-native bounded context
`urn:stdo:bounded-context:graph-native-odd` under the selected complete
STDO basis. The context covers the ODD product shape, the GTL language
role, the ABG method role, graph assets, vectors, functions, traversals and
the graph and runtime worker and evaluator shorthands defined here. It does
not absorb a consuming Product's domain semantics, nor a concrete runtime's
carriers that happen to share a spelling (P1, P3).

A consumer binds the roles to concrete conforming realisations in its own
Product, requirements, design and immutable dependency identity. A
consumer, a reference realisation or a historical product may prove or
falsify conformance; none of them supplies method authority (P6).

The profile has two core jobs: to describe the product as a declared asset
graph in graph-native terms, and to ensure that automation never outruns a
lawful manual traversal of the same graph. The graph is the process model,
not decoration around a process. GTL is the language expression of the
profile. ABG is the substrate of traversal governance, binding and runtime
truth that realises the GTL program without owning the domain's internal
HOW (P0, P6).

### Foundation to law

This member is material family F18, outcome-driven development. The table
below shows which of its rules follow from which premises, in the format
of [FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. Under
[PROFILES §1](PROFILES.md#1-the-boundary) the family imports the families
its rows rest on; their rules and choices keep their owners:

- F1, frames and context
  ([REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit)),
  for acquisition under ACTIVATION §2;
- F2, transitions, steps and configuration ([ACTIVATION §1](ACTIVATION.md#1-the-step));
- F3, results and their combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results));
- F4, work state, resumption and reuse ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart));
- F6, claims, evidence, assessment and acceptance ([EVALUATION §1](EVALUATION.md#1-claims));
- F9, the `a_c` calculus ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position));
- F10, constitutional chain, outcome and build-tenant binding ([SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain));
- F11, change management and ambiguity ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management));
- F12, binding a project to the method
  ([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence));
- F13, work carriers ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution));
- F15, release and successor conservation ([RELEASE §1](RELEASE.md#1-context-and-position)).

Its instance premises hold where a product is built with this profile;
they are adopted with it and do not follow from the foundations (P1, P6):

- I1: a selected Product outcome is admitted as external authority for
  the work;
- I2: the work changes a mutable workspace, beside which an immutable
  ledger and event log record the admitted work;
- I3: bounded probabilistic workers carry out the constructive actions,
  and their reports and artifacts are observations;
- I4: the product is built with an installed release of a method product,
  which may be an earlier release of the product itself.

Each commitment in the premise column carries its standing from
[FOUNDATIONS §3](FOUNDATIONS.md#3-commitments).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent), P4a (independent), P0 (recovered); I2 | By P3 identity is declared, so each bounded state is a node over explicit typed assets with a declared identity, never one hidden workspace object (I2); by P4a steps compose only through declared result types and domains, so each admissible transition is a vector that declares its required upstream assets, target, evaluators and gates, and output contract; by P0 an actor holds only what it acquired in a bounded step, so the work is a traversal that takes one admissible vector at a time until the selected target closes | [§5](#5-graph-model), with [Nodes](#nodes), [Vectors](#vectors) and [Traversal](#traversal); [§11.1](#111-typed-assets-and-nodes-are-explicit) | the graph as the product's process model and traversal as its workflow, and `asset_surface` as the declaration of a produced or consumed boundary: this member; which nodes, vectors and assets a product declares: the product | 5, 2, 3 |
| P0 (recovered), P6 (independent); I3; F2 (imported) | within one bounded step the worker's internal path is its own and the traversal contract is its admissible external space; the worker cannot close the edge, emit runtime events, mutate ledgers or decide re-entry, because its output is a candidate until evaluated and its report is an observation, not authority | [§5 Probabilistic compute](#probabilistic-compute); A5 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | one vector or edge traversal as the bounded step, declared as a binding in §5 Probabilistic compute: this member | 5, 8, 9 |
| P1 (independent), P3 (independent); F9 (imported), F11 (imported) | By P1 equal spelling fixes no meaning and by P3 identity is declared, so this profile's traversal and its F_D, F_P and F_H shorthands are concepts of its own bounded context and not the `a_c` traversal record or functor kinds by equal spelling (F9); F_P and F_H relate to the source concepts of SPEC_METHOD §5 only through declared specialisations that state direction, preserved meaning, narrowed scope and invalidation (F11) | this member's lead; [§1](#1-position), the bounded-context paragraph; [§5 Probabilistic compute](#probabilistic-compute) | the bounded context and the F_P and F_H specialisations: this member, under PROFILES §1 | 5, 6 |
| P4a (independent), P4b (derived from P0 and P2); F2 (imported) | By P4a a step composes only through its declared contract, so a graph function realises an outer vector, which stays the callable contract; by P4b a later step needs step-produced facts recorded, so where the function refines that vector into inner steps the inner boundaries are published and a later step reads earlier outputs only through its declared environment; and F2 makes the loop govern each published inner boundary as it governs the outer one | [§5 Graph functions](#graph-functions); [§11.4](#114-the-gtl-module-is-the-operative-publication-surface), second paragraph; [§11.8](#118-cumulative-environment-law-is-mandatory); A14 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the cumulative carried environment as the specialised contract for carrying earlier outputs, with its three declarations at "should": this member | 5, 3, 4 |
| P0 (recovered), P3 (independent), P6 (independent) | every operative constructive step has a named, typed and published carrier that a later actor and the runtime can re-acquire, because a later actor holds declared sources and not another actor's private memory, and no undeclared surface carries authority; no operative step, callable surface or capability stays only in prose, prompt memory, an orchestration loop or a service method, and a caller binds to the published outer carrier, never to a hidden inner vector | [§11.2](#112-graph-functions-are-the-primary-constructive-carrier); [§11.3](#113-the-function-catalogue-is-published); [§11.4](#114-the-gtl-module-is-the-operative-publication-surface), first paragraph; [§8](#8-responsibility-layers-and-local-binding), last paragraph | `GraphFunction` as the carrier; a machine-readable function catalogue whose retained functions should expose at minimum name, inputs, outputs, intent and public or helper role; the GTL module as the publication surface: this member; which functions, graphs and catalogue entries a product publishes: the product | 5, 4, 1 |
| P0 (recovered), P6 (independent); I3 | imperative code transports or persists facts and decides nothing that the declared carrier owns: domain meaning, semantic target movement, step selection, closure, lineage and constructive workflow truth, because what is decided only in imperative code is decided by no declared owner | [§11.2A](#112a-outcome-first-realisation-order); [§14](#14-dogfooding-rule) | the order outcome traversal, declarative carrier, minimal adapter code, with the outcome traversal's declarations; building the product's own framework behaviour through its graph functions: this member | 5, 4 |
| P6 (independent), P0 (recovered), P3 (independent); I3; F2 (imported) | By P6 authority exists only through a grant and by P3 an identity is one and declared, so each traversal has exactly one execution authority, which owns its selection and advance, actor invocation and supervision, retry, continuation and re-entry, runtime events and closure fold; by P0 and I3 a bounded step, product code, a plugin, a service or a query returns evidence, policy input and control and holds none of these (F2), so two controllers that can each claim one traversal leave the product not ODD-correct | [§10 ABG](#abg), [ODD product](#odd-product) and [Query and service layers](#query-and-service-layers); [§11.5A](#115a-abg-owns-continuation-and-re-entry); [§11.5B](#115b-execution-authority-audit); A15 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | ABG as the role of that single authority, with its ownership list and the product's; the five-surface audit inventory, the changes that require the audit and the conditions that prevent closure: this member; the concrete realisation of the ABG role: the consumer (§1) | 5, 8, 9 |
| P6 (independent), P1 (independent), P3 (independent), P5 (derived from P0 and P6) | By P6 authority is scoped, so model synthesis, gap discovery, next-action selection and action evaluation hold separate authorities and no command, report, query, service or summary becomes a rival source of traversal truth; by P5 a projection decides only what its evidence establishes, so visible state is a projection that reconciles to the admitted truth it reads or fails closed; by P1 and P3 equal names establish no identity | [§11.5](#115-current-state-is-a-projection-over-constructive-history); [§11.5C](#115c-projection-source-coherence); A0, A4a, A11, A12, A16 and the constitutional equation in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the four functions `synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action`, and the duty of a design, ticket, module or proof to name the one it implements or consumes: this member; domain asset meaning, catalogue meaning and gap interpretation: the product (A15) | 5, 6, 9 |
| P6 (independent), P0 (recovered); I2, I3; F2 (imported), F6 (imported) | no edge closes from an artifact, a worker report, process success or liveness alone; closure is a fold over admitted evidence, the workspace counts only through the ledger, and an evaluator attends only to admitted ledger rows reachable through declared lineage, because a report or artifact is an observation, not authority, and a step's context is its declared material, never the workspace | A1, A1a, A1b, A6, A7 and A10 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the governed work pair of workspace, ledger, event log and evaluator work, and the ledger's fields: this member; carrier names other than those of the loop: the implementation, which keeps the authority shape (§11.5D) | 5, 7, 9 |
| P4b (derived from P0 and P2), P3 (independent); I2; F4 (imported) | By P4b every closure-relevant callout is a step-produced fact the outer contract needs, so it is admitted to the immutable ledger and event log; by P3 a correction keeps the identity of what it corrects, so it appends or supersedes and never rewrites; under F4 and I2 every closure decision and next-action selection is reproducible by replay from carriers that each reference their causal predecessors | A1a, A13 and A13a in [§11.5D](#115d-constructive-evaluation-and-yield-loop); [§11.5](#115-current-state-is-a-projection-over-constructive-history) | the replay inputs listed in A13 and the predecessor chain of A13a: this member | 5, 2, 9 |
| P5 (derived from P0 and P6), P0 (recovered); F4 (imported) | By P5 work that is still lawful but not yet decided has no failure to classify, and by P0 the next actor holds only what is recorded, so such work returns control without failure classification, keeping the same edge and a replay-visible resume basis (F4) | A9, and A4 on `post_yield_resume`, in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | `yield` as the lawful iteration boundary, distinct from retry, block and timeout: this member | 5 |
| P2 (independent), P6 (independent); I1; F10 (imported), F11 (imported) | By P2 only work with a route to the selected outcome is justified, so the selected outcome bounds the loop: every action binds the current gap to exact target assets and obligations before invocation, and only published lawful actions are ranked; by P6 no further material work is selected without another admitted basis once a terminal condition of the loop is reached, and a reprice requests constitutional re-entry (F10, F11) and selects nothing; by P6 edge closure is evidence toward Product acceptance, not acceptance | the selected-outcome paragraphs, the intent-lineage paragraph, A2, A3, A4 on `post_reprice` and A16 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | which outcome is selected and accepted: its owner under [SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation); the re-entry a reprice requests: its owning relation under SPEC_METHOD §4 | 5, 1 |
| P5 (derived from P0 and P6), P6 (independent); F3 (imported) | By F3 every result is stated in the core or in a refinement mapped into it, so the closure decision is a closed sum type, `evaluate_next` is total, and each closure decision and each audit outcome maps to exactly one core value for a named predicate, its cause being part of the value where the cause decides it (P5); by P6 a closure decision answers the edge predicate and is not a disposition of ACTIVATION §3, which answers the acceptance predicate, so neither counts toward the other; a selection decides no predicate, so it maps to no core value | A4, A8 and its mapping in [§11.5D](#115d-constructive-evaluation-and-yield-loop); the audit mapping in [§9](#9-method-governance-and-audit) | the seven closure decisions, their causes and the default of graph following in A4: this member; the priority policy: the product (A15) | 5, 3, 9 |
| P6 (independent), P1 (independent), P3 (independent); F12 (imported) | By P6 each part of an ODD product has one owner: one WHAT surface, one HOW relation, runtime truth with the traversal authority and domain meaning with the product; by P1 and P3 the split binds by authority and not by directory names, and a runtime frame's name does not enrol it among the evaluation frames (F12), while an evaluation frame may take a runtime frame as its subject or coordinate without collapsing the two | [§10](#10-what-an-odd-product-is), with [Product specification](#product-specification-software-development-topology) and [Product realisation](#product-realisation-software-development-topology) | the ten-part application boundary and `specification/` and `build_tenants/` as the default software-development locations: this member; the actual locations: the product's definition under PRODUCT_DEFINITION | 5, 1, 7 |
| P1 (independent), P2 (independent), P6 (independent); F10 (imported) | By P6 this profile decides only what it owns, graph-native structure and product shape, and neither a product's domain semantics nor its current line; by P2 domain-correct work also needs the constitutional chain (F10), the domain method's semantic law and the product's local authority surfaces; by P1 where a product also adopts a domain profile, each governs its own questions and the two compose | [§2](#2-method-role); [§3](#3-method-composition) | the split between graph-native structure and product shape, owned here, and world-model semantics, publication and composition law, owned by [WORLD_MODEL](WORLD_MODEL.md#1-position); which domain method and local surfaces apply: the product | 5, 1, 2 |
| P0 (recovered), P2 (independent); F1 (imported) | an actor building an ODD product acquires the general method, the product's domain method where one exists, and its local authority surfaces before it acts, then identifies and declares the graph carrier and loop, and implements code last, because it holds only the declared sources it acquires and the selected outcome sets which obligations matter | [§17](#17-invocation-rule); [§18](#18-cold-start-reading-order) | the fourteen-step sequence and the two reading orders, with "usually" for the effect of skipping the order: this member | 5, 1, 7 |
| P6 (independent), P2 (independent); F11 (imported) | By P6 a structural pattern becomes shared law only when this profile is changed (F11), so usage and repetition approve nothing; by P2 a move the profile does not clearly cover is evaluated against it, and a move found worth incorporating is not fully approved until the profile is updated | [§9](#9-method-governance-and-audit) | the audit questions, at "should", and the three audit outcomes: this member; a change to this profile: the method's change management (SPEC_METHOD §4) | 5, 1, 9 |
| P1 (independent), P3 (independent) | By P1 a capability class is a layer idea whose meaning each product binds to its own typed assets, and by P3 identity is declared, so shared structural law and a product's local semantic bindings stay distinct, and copying another product's local names without semantic need is not reuse of the method | [§8](#8-responsibility-layers-and-local-binding); [§11.6](#116-product-specific-semantics-sit-above-the-shared-carrier) | the capability classes listed, as examples: this member; local asset names, asset meanings, proof lanes and query overlays: the product | 5, 6, 1 |
| P6 (independent); F6 (imported) | ODD, GTL and ABG name capability roles, not a required implementation; a consumer, a reference realisation or a historical product may prove or falsify conformance and supplies no method authority, because evidence never mints authority | [§1](#1-position), the paragraphs on roles and on consumer binding | the concrete realisations of the GTL and ABG roles: the consumer, in its own Product, requirements, design and immutable dependency identity | 9, 5, 8 |
| P0 (recovered), P6 (independent); I3; F13 (imported) | automation decides nothing that the declared surfaces do not: each automated move is one an actor holding only those surfaces could make, because a later actor re-acquires declared sources and not private memory, and authority comes only from declared owners; an agentic worker's artifacts take effect only through admission against deterministic criteria, and conformance evidence is not ratification | [§11.7](#117-manual-walkthrough-must-still-be-lawful); [§11.7A](#117a-conforming-agentic-development) | the manual walkthrough as the test of automation, and its agentic form as the conformance proof of the method: this member; the admission criteria for produced artifacts: [SPEC_METHOD](SPEC_METHOD.md) and [TICKETS](TICKETS.md) | 5, 9, 7 |
| P6 (independent), P5 (derived from P0 and P6); F6 (imported) | By P6 only the real authority-bearing input decides, so negative evidence for a boundary exercises the supported authority path with that input invalidated and shows refusal before the prohibited effect (F6); by P5 a manufactured refusal, blocked event, gap or verdict proves nothing about that path, and absence in source, package, installation and runtime are distinct claims | [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010) | the concrete test and evidence mechanism: the consumer | 9, 5 |
| P3 (independent), P6 (independent); I4; F15 (imported) | By P3 the installed builder and the product it builds, and the selected immutable release and mutable source, are distinct identities (F15), and by P6 they hold distinct authority: the selected release governs a consumer and mutable source governs none; a mismatch is repaired by installing one complete release (I4), a release version is no graph truth (P3), and where an installable development form exists, decisive proof runs against it (P6) | [§4](#4-method-library-classes); [§7](#7-self-host-boundary); [§13](#13-installed-dev-rule); [§15](#15-release-boundary) | which release a consumer selects: the consumer ([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)); which members are method members: the [standards README](README.md#documents); the isolated environment and the proving lane of §13, at "should": this member | 1, 2, 9 |
| P6 (independent), P3 (independent); F12 (imported) | By P6 the installed product provides the method, runtime and carrier surfaces and assumes no knowledge of a target project's domain, over which it holds no grant; by P3 the target project owns its definition, constitutional surfaces, realisation roots and domain outputs as its own identity (F12) | [§6](#6-product-boundary) | the default scaffold names and `build_tenants/` as the default realisation root: this member, as defaults; the target project's domain, surfaces and outputs: the target project | 1, 5 |
| P4a (independent), P2 (independent); F3 (imported) | By P4a a refined inner chain closes the enclosing carrier only when the enclosing contract still holds after fold-back and zoomed and unzoomed views agree; by P2 and F3 a live requirement without a proof witness is a gap that keeps the enclosing carrier open until it is realised, deferred or repriced out of the active branch; that a scenario bundle should make clear the boundary, assets, vectors, paths and evidence that close it is this member's choice | [§11.9](#119-global-convergence-must-be-stable-under-zoom); [§12](#12-scenario-rule) | which scenarios a product keeps and which proof witness fits a requirement class: the product; deferring or repricing a requirement out of the active branch: the requirement's owner | 5, 3, 9 |
| P5 (derived from P0 and P6); F3 (imported) | By F3 results conjoin and by P5 an unestablished clause establishes nothing, so an ODD product is built correctly only when every clause of §11 holds: the clauses form a conjunction, and one failing or unestablished clause leaves the product not built correctly | [§11](#11-core-law), its lead | which clauses make up the core law: this member | 5, 3 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, nodes, vectors and typed assets: [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which asks first whether a boundary moves a typed asset from one state to another, and [DESIGN_MODULE Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members); [§11.7](#117-manual-walkthrough-must-still-be-lawful), steps 1 and 2; [§11.7A](#117a-conforming-agentic-development), where admission enforces an artifact as a constructor enforces a typed asset under §11.1; [§17](#17-invocation-rule), step 5; [§19](#19-ramp-up-checklist), question 2; [§16](#16-failure-pattern), pattern 1.
- Row 2, the bounded probabilistic step: [PROFILES §1](PROFILES.md#1-the-boundary), whose declared-binding rule takes its shape from the F_P and F_H specialisations §5 owns, and [PROFILES §2](PROFILES.md#2-graph-execution), which keeps the bounded-step binding and the worker's internal solution strategy outside the framework; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-09; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which names A5 as the ODD specialisation of prompt construction; [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which keeps probabilistic worker boundaries out of imperative prompt or dispatch code; [§11.5B](#115b-execution-authority-audit) and [§11.7A](#117a-conforming-agentic-development), which read F_P and F_D at the audit and at the method layer.
- Row 3, the bounded context: [PROFILES §1](PROFILES.md#1-the-boundary), which keeps the traversal record and the functor kinds as terms of AXIOMATIC_CALCULUS §5 apart from the profile's shorthands; [§11.5B](#115b-execution-authority-audit), which binds F_P and F_H to the source concepts of SPEC_METHOD §5 through §5 Probabilistic compute.
- Row 4, graph functions and refinement: [PROFILES §2](PROFILES.md#2-graph-execution), which keeps the refinement binding with §11.8 as its specialised contract; [DESIGN_MODULE Atomic functions and higher-order composition](DESIGN_MODULE.md#atomic-functions-and-higher-order-composition), where a product under this profile binds its composition and effect algebra to GTL composition and ABG interpretation; [§11.7](#117-manual-walkthrough-must-still-be-lawful), step 2; [§17](#17-invocation-rule), steps 6 and 8; [§19](#19-ramp-up-checklist), question 3; [§16](#16-failure-pattern), patterns 2 and 7.
- Row 5, published constructive carriers: [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which is not used to hide graph functions inside service methods, and [DESIGN_MODULE §11 Design review questions](DESIGN_MODULE.md#design-review-questions) 29 to 31; [UX §3](UX.md#3-product-truth-and-admitted-carriers), where a published graph function or lawful composition is an admitted carrier; [§9](#9-method-governance-and-audit), which asks which public graph functions carry the transition; [§17](#17-invocation-rule), steps 6 to 8; [§19](#19-ramp-up-checklist), questions 3 to 5; [§16](#16-failure-pattern), patterns 9 and 10.
- Row 6, outcome-first realisation order: [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which orders outcome traversal, declarative carrier structure and deterministic module realisation and reprices a module that owns next work or closure, with the graph-execution checks of the [DESIGN_MODULE Functional realisation checklist](DESIGN_MODULE.md#functional-realisation-checklist); [§17](#17-invocation-rule), step 14; [§16](#16-failure-pattern), patterns 10 and 11. §14 Dogfooding has no separate consumer; it binds only a product that provides this profile's framework behaviour, and a violation shows as §16 pattern 10.
- Row 7, one execution authority: [PROFILES §2](PROFILES.md#2-graph-execution), which indexes the ownership split of §10; [UX §3](UX.md#3-product-truth-and-admitted-carriers), where an ABG event or command boundary is an admitted carrier, [UX §8](UX.md#8-continuation-and-replay), whose view does not own continuation because the runtime does, and [UX Relationship to other members](UX.md#relationship-to-other-members), where UX surfaces are projection and query surfaces under this profile; [DESIGN_MODULE §2](DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation), which keeps continuation and re-entry decisions out of deterministic controllers, and [DESIGN_MODULE Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members); [§9](#9-method-governance-and-audit), which asks whether a command, service or query surface replaces ABG continuation and whether the §11.5B audit holds; [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010), whose supported relation leaves traversal, event, continuation and replay truth with ABG; [§17](#17-invocation-rule), step 10; [§19](#19-ramp-up-checklist), questions 6 and 9; [§16](#16-failure-pattern), patterns 11 and 12.
- Row 8, projection over constructive history and evaluation separation: [§9](#9-method-governance-and-audit), which asks which projected or query state is exposed without replacing ABG runtime truth; [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010), where no query or projection may become a rival traversal controller; [§17](#17-invocation-rule), step 13; [§19](#19-ramp-up-checklist), questions 7 and 8; [§16](#16-failure-pattern), pattern 14. No section of another member applies these rules; UX §3 binds a UX projection surface to admitted carriers under its own rule.
- Row 9, evidence before closure and the ledger: [§9](#9-method-governance-and-audit), which asks which proof or closure lane justifies a capability; [§11.5B](#115b-execution-authority-audit), where the closure fold stays with ABG and a worker self-report or product postflight closes nothing; [§17](#17-invocation-rule), step 11; [§19](#19-ramp-up-checklist), questions 10 and 12; [§16](#16-failure-pattern), pattern 6.
- Row 10, admitted facts, correction and replayability: [§11.5B](#115b-execution-authority-audit), where runtime event emission, append and replay stay with ABG and a direct append or side-ledger mutation is forbidden; [§11.5C](#115c-projection-source-coherence), where runtime status views derive from ABG runtime facts, events, replay or projection truth; [§17](#17-invocation-rule), step 11; [§19](#19-ramp-up-checklist), question 10.
- Row 11, yield: [§17](#17-invocation-rule), step 12; [§19](#19-ramp-up-checklist), question 11; [§16](#16-failure-pattern), pattern 13. No section of another member applies it: yield is a closure decision of this member's loop, read elsewhere only through its core value.
- Row 12, the selected outcome and lawful action selection: [§17](#17-invocation-rule), step 11, from intent lineage through target binding and lawful action selection; [§19](#19-ramp-up-checklist), question 10; [§16](#16-failure-pattern), pattern 14. No section of another member applies these rules; the selected outcome they bind to is SPEC_METHOD §3's, which this member applies and which applies nothing of it.
- Row 13, closure decisions and the core mapping: [§19](#19-ramp-up-checklist), question 11; [§16](#16-failure-pattern), pattern 13. No section of another member applies these rules; a consumer of a closure decision or audit outcome reads its core value under FOUNDATIONS §4 Results.
- Row 14, the ODD product and its ownership split: [PROFILES §2](PROFILES.md#2-graph-execution), which indexes §10 as the ownership split of graph execution; [DESIGN_MODULE Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members), [UX §2](UX.md#2-role-and-composition) and [WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports), which leave graph-native product shape to this profile; [§17](#17-invocation-rule), steps 4 to 9; [§18](#18-cold-start-reading-order); [§19](#19-ramp-up-checklist), questions 1 to 7.
- Row 15, method role and composition: [UX §2](UX.md#2-role-and-composition) and [UX Relationship to other members](UX.md#relationship-to-other-members), [WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports) and [DESIGN_MODULE Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members), each of which composes with this profile and leaves it what it owns; [§17](#17-invocation-rule), steps 1 to 3; [§18](#18-cold-start-reading-order), whose closing paragraph divides structural expectation, domain law and current line.
- Row 16, invocation and reading order: [§19](#19-ramp-up-checklist), whose questions test what the sequence and the reading order produce. No section of another member applies them: they bind the actor who enters this member, and the acquisition they require is F1's rule, imported in the premise column.
- Row 17, method governance and audit: [§11.7A](#117a-conforming-agentic-development), where shared method change still follows §9 and repeated agentic execution ratifies nothing. No section of another member applies it; the audit governs moves under this profile, and shared-law adoption across members is SPEC_METHOD §6's rule.
- Row 18, responsibility layers and local binding: [§9](#9-method-governance-and-audit), whose audit asks which layer or capability class is implemented and which local typed assets bind it, and distinguishes shared structural law from local semantic bindings; [§19](#19-ramp-up-checklist), questions 2 and 6. No section of another member applies these rules; they bind a product's binding of this profile's layers, which the product declares in its own authority surfaces.
- Row 19, capability roles and consumer binding: [DESIGN_MODULE Identity defaults from a bound runtime realisation](DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation), where a consumer-bound realisation of the ABG role publishes defaults for its own runtime surfaces; [§11.5B](#115b-execution-authority-audit), where the execution authority is the one consumer-bound realisation of the ABG role; [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010), where the consumer owns the concrete test and evidence mechanism.
- Row 20, manual walkthrough and conforming agentic development: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which names §11.7A as the ODD specialisation of prompt construction; [§11.7A](#117a-conforming-agentic-development), whose walkthrough is §11.7's conformance proof; [§19](#19-ramp-up-checklist), question 14; [§16](#16-failure-pattern), patterns 3 and 15.
- Row 21, real authority-path negative proof: no separate consumer applies. The property binds negative evidence for an ODD or graph-native boundary; the consumer owns the concrete test and evidence mechanism, as the section says, and the negative-proof rules of other members, TICKETS §6 Mixed-state negative proof and SPEC_METHOD §7 Hard-break discipline, are their own and name this section nowhere.
- Row 22, builder, release and source distinctions: [§11.7](#117-manual-walkthrough-must-still-be-lawful), where automation that collapses the installed builder and the product under development into one authority surface is unlawful, for §7; otherwise no separate consumer applies: the generic rules that §4, §13 and §15 specialise are PRODUCT_DEFINITION §4's, RELEASE §4's and ASSURANCE §5's, which name this member nowhere.
- Row 23, product boundary: [§11.7](#117-manual-walkthrough-must-still-be-lawful), where automation that depends on implementation-carrier knowledge the installed product should not have is unlawful; [§17](#17-invocation-rule), step 3; [§16](#16-failure-pattern), pattern 4.
- Row 24, convergence under zoom and scenarios: [§17](#17-invocation-rule), step 9; [§19](#19-ramp-up-checklist), questions 12 and 13; [§16](#16-failure-pattern), patterns 5, 6 and 8. No section of another member applies these rules; ASSURANCE §4 and §6 own the generic scenario-bundle and significant-path law and name this member nowhere.
- Row 25, the core-law conjunction: [§16](#16-failure-pattern), which declares the profile violated when any pattern holds; [§11.5B](#115b-execution-authority-audit), whose closure conditions leave the product not ODD-correct over GTL/ABG when any one is present; [§19](#19-ramp-up-checklist), whose closing sentence reads an unanswered question as a product not yet ODD-shaped.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

Sections that add no rule of their own (A0 to A16 are the axioms of
§11.5D):

- §1's first two paragraphs say what the instruction `using ODD, build
  this product` means by naming rules of §5, §10 and §11, which the rows
  trace.
- §16 lists fifteen failure patterns. Each is the violation of a rule a
  row traces: 1, §5 Nodes and Vectors; 2, §5 Graph functions; 3, §11.7;
  4, §6 and §11.7; 5, §12; 6, A6 and §11.9; 7, §11.8; 8, §11.9; 9, §11.2,
  §11.2A and §10 Query and service layers; 10, §11.2A; 11, §11.2A and
  §11.5A; 12, §11.5B; 13, A9; 14, A0, A12 and A16; 15, §11.7A.
- §19 asks fourteen questions, each for the surface that a traced rule
  requires: 1, §17 step 4; 2, §11.1; 3, §11.2; 4, §11.3; 5, §11.4; 6, §10
  and A15; 7, §11.5; 8, §11.5C; 9, §11.5B; 10, §11.5D; 11, A8 and A9; 12
  and 13, §11.9; 14, §11.7A. Its closing sentence is a diagnostic over
  those surfaces. Whether a product is built correctly is decided by §11,
  and whether a move complies by the audit of §9.
- §20 is a compression of this member and owns no determination (§20).
- §21 records where each predecessor claim is carried and decides no
  outcome ([FOUNDATIONS §3](FOUNDATIONS.md#foundation-to-law)).

The table is new in this corpus. Purpose and material relation: an actor
started on this member sees which rules follow from the foundations and
which are choices, and who owns each choice, so no choice is presented as
derived (P6, P1).
```


### Row `ODD_METHOD.md#10-what-an-odd-product-is` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#10-what-an-odd-product-is` at rc.2:

```text
## 10. What An ODD Product Is

An ODD product is a configured GTL/ABG domain product whose constructive work is carried by published graph functions over typed domain assets.

The stable app boundary is:

```text
App
= Bootstrap Surface
+ Initialization Surface
+ Domain Configuration
+ Typed Domain Assets / Nodes
+ GTL Function Catalog
+ GTL Module
+ Policy Hook Bindings
+ ABG Runtime
+ Projection / Query Surface
+ Proof Surface
```

Read the ownership split strictly.

The `Product Specification` and `Product Realization` subsections below name
the **default topology for a software-development ODD product** in this
ecosystem. `SPEC_METHOD.md`'s `stdo_<label>.json` definition binds the actual
locations. ODD method at the universal layer commits to the authority split
(one `WHAT` surface, one `HOW` relation, runtime owned by ABG, product owning
domain meaning) but not to specific directory names. Existing projects and
other ODD product types may use another layout while preserving that split.

The Product Definition Overlay's `reference_frame_bases` bindings use
`REFERENCE_FRAME_METHOD.md`'s evaluation-frame meaning. An ABG runtime `Frame`,
attention frame, zoom frame, or overlay frame remains an ABG-owned runtime
contract in `WHAT` and `HOW`; its name does not enroll it in the project's
collective evaluation frame set. A declared evaluation frame may inspect such
a runtime frame as its exact subject or coordinate without collapsing the two.

### Product Specification (software-development topology)

The Product Definition Overlay's `what` bindings locate the authoritative `WHAT`.
`specification/` is the default software-development location.

It defines:

- intent
- product position
- goals
- requirements
- scenarios

### Product Realization (software-development topology)

The Product Definition Overlay's `how` bindings locate the authoritative `HOW`.
`build_tenants/` is the default software-development location.

It carries:

- design
- GTL publications
- code
- tests
- local proof surfaces

### ABG

ABG owns:

- traversal
- dispatch
- actor invocation
- process supervision
- graph-call realization
- runtime facts
- runtime event emission and replay
- frames
- continuations
- retry and correction control
- closure folds over runtime truth
- re-entry after publish boundaries
- lineage and provenance

### ODD Product

The ODD product owns:

- domain asset meaning
- graph-function meaning
- published function catalog
- policy overlays
- domain query projections
- closure and gap interpretation for its domain

### Query And Service Layers

Service or query layers may own:

- transport
- sessions
- routing
- browser-safe projection
- API surfaces

They do not own runtime truth.

They also do not own continuation truth.

Do not hide the real constructive carrier behind the word `service`.

---
```

Successor, `ODD.md#10-what-an-odd-product-is`:

```text
## 10. What an ODD product is

An ODD product is a configured GTL/ABG domain product whose constructive
work is carried by published graph functions over typed domain assets. Its
stable application boundary is (P6, P3):

```text
App
= Bootstrap Surface
+ Initialization Surface
+ Domain Configuration
+ Typed Domain Assets / Nodes
+ GTL Function Catalog
+ GTL Module
+ Policy Hook Bindings
+ ABG Runtime
+ Projection / Query Surface
+ Proof Surface
```

The ownership split is read strictly. The two topology subsections below
name the default topology of a software-development ODD product in this
ecosystem; the product's `stdo_<label>.json` definition under
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) binds the actual locations. At
the universal layer this profile commits to the authority split (one WHAT
surface, one HOW relation, runtime owned by ABG, product owning domain
meaning) and not to directory names; existing projects and other ODD
product types may use another layout that keeps the split (P6, P1).

The product definition's `reference_frame_bases` bindings carry the
evaluation-frame meaning of [REFERENCE_FRAME](REFERENCE_FRAME.md). An ABG
runtime `Frame`, attention frame, zoom frame or overlay frame stays an
ABG-owned runtime contract in WHAT and HOW; its name does not enrol it in
the project's collective evaluation frame set. A declared evaluation frame
may inspect such a runtime frame as its exact subject or coordinate
without collapsing the two (P1, P3).

### Product specification (software-development topology)

The product definition's `what` bindings locate the authoritative WHAT;
`specification/` is the default software-development location. It defines
intent, product position, goals, requirements and scenarios (P6).

### Product realisation (software-development topology)

The product definition's `how` bindings locate the authoritative HOW;
`build_tenants/` is the default software-development location. It carries
design, GTL publications, code, tests and local proof surfaces (P6).

### ABG

ABG owns traversal; dispatch; actor invocation; process supervision;
graph-call realisation; runtime facts; runtime event emission and replay;
frames; continuations; retry and correction control; closure folds over
runtime truth; re-entry after publish boundaries; lineage and provenance
(P6).

### ODD product

The ODD product owns domain asset meaning, graph-function meaning, the
published function catalogue, policy overlays, domain query projections,
and closure and gap interpretation for its domain (P6, P1).

### Query and service layers

Service or query layers may own transport, sessions, routing,
browser-safe projection and API surfaces. They own neither runtime truth
nor continuation truth. The real constructive carrier is never hidden
behind the word service (P6).
```


### Row `ODD_METHOD.md#11-core-law` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#11-core-law` at rc.2:

```text
## 11. Core Law

An ODD product is built correctly only when all of the following are true.

### 11.1 Typed Assets And Nodes Are Explicit

The product works over explicit typed assets or typed nodes.

It does not work over:

- one hidden project blob
- one giant mutable workspace object
- one undocumented service payload

Concrete assets must bind explicitly into typed domain boundaries.

Where an asset is a real produced or consumed boundary, declare its `asset_surface`.

### 11.2 Graph Functions Are The Primary Constructive Carrier

Every operative constructive step is carried by:

- one named `GraphFunction`, or
- one lawful graph-function composition

Do not leave the real carrier inside:

- orchestration loops
- bespoke Python pipeline runners
- controller scripts
- service methods that only happen to call GTL-adjacent helpers

### 11.2A Outcome-First Realization Order

If ODD introduces an edge traversal as the unit of compute, an ODD product must
use that unit of compute to build its own operative framework behavior.

The required realization order is:

1. declare the outcome traversal over typed assets
2. publish the declarative GTL/ABG carrier structure
3. implement only the minimal imperative adapter code that remains necessary

Outcome traversal means the product declares the governed movement before
implementation:

- source asset type
- target asset type
- edge traversal or graph-function name
- closure or evaluation obligation
- lineage obligation
- ambiguity or gap obligation
- allowed `F_D`, `F_P`, and `F_H` bindings

Declarative carrier structure means:

- GTL graph functions
- typed nodes
- vectors
- operator bindings
- evaluator bindings
- carrier schemas
- policy declarations
- projection declarations
- lineage ledger declarations

Imperative adapter code is lawful only where it transports or persists facts:

- file or network IO
- CLI or API transport
- event persistence
- runtime invocation
- projection rendering
- tool execution that has already been admitted by a declared traversal

Imperative code must not own domain meaning, semantic target movement, step
selection, closure semantics, lineage truth, or constructive workflow truth.

If framework behavior is implemented imperatively first and only later
described with GTL vocabulary, the product is ODD-shaped but not yet ODD-built.

### 11.3 The Function Catalog Is Published

The live line must publish a machine-readable function catalog.

At minimum, each retained function should expose:

- name
- inputs
- outputs
- intent
- public or helper role

If the callable surface exists only in prose or prompt memory, the product is under-built.

### 11.4 The GTL Module Is The Operative Publication Surface

The product must publish:

- the public graph-function carriers
- the graph or graphs those carriers traverse
- typed node and vector surfaces
- semantic jobs or equivalent outer callable contracts bound to the public carrier

Do not bind callers directly to hidden inner vectors.

Where a public carrier refines into inner executable structure, publish the live traversal boundaries explicitly through lawful GTL boundary surfaces such as `RefinementBoundary` or `CandidateFamily`.

The outer public carrier remains the callable contract.

### 11.5 Current State Is A Projection Over Constructive History

Visible current state is a projection.

It is not a replacement for runtime truth.

The ODD query lane may expose:

- asset views
- function catalog views
- checkpoint overlays
- provenance overlays
- domain-specific explainability overlays

It must not redefine ABG runtime facts.

### 11.5A ABG Owns Continuation And Re-Entry

An ODD application over GTL/ABG is a cooperative subsystem, not a replacement
runtime.

ABG owns:

- continuation authority
- re-entry after publish boundaries
- graph-call lifecycle
- step selection over the declared graph

The product may:

- publish typed assets and evidence
- execute one admitted bounded constructive step
- publish downstream read models or domain overlays
- return control to ABG

The product must not:

- own a hidden continuation loop
- carry multi-step controller memory across publish boundaries
- infer later steps locally instead of re-entering through ABG
- treat public `next` and explicit graph-function continuation as rival
  authorities inside one controller
- build product-local orchestration that effectively replaces ABG

If an application attempts to replace ABG continuation with tenant-local
control flow, it is no longer behaving as an ODD application over GTL/ABG. It
has drifted into a different architecture that only happens to publish some
ODD-shaped artifacts.

### 11.5B Execution Authority Audit

Any ODD product over GTL/ABG that changes runtime, `start`/`iterate`, worker
transport, actor invocation, process supervision, plugin dispatch, event
projection, closure, assurance, retry, or continuation semantics must include
an execution-authority audit before activation and closure.

The audit must prove that there is exactly one execution authority for the
affected traversal. For a consumer using the GTL and ABG roles, that authority
is the one consumer-bound realization of the ABG role. This remains true when
the realization under change itself implements that role. A different
realization is lawful only under an explicitly ratified, non-overlapping
runtime scope.

The audit must inventory at least these surfaces:

| Surface | Lawful owner | Product or plugin role | Forbidden local implementation |
| --- | --- | --- | --- |
| Traversal selection and vector advance | ABG | Declare graph functions, vectors, assets, and domain policy inputs | Product-local runner deciding the next traversal step |
| Actor invocation and process supervision | ABG | Provide actor bindings, prompts, payload adapters, and evidence adapters | Product-local worker `spawn`, `spawnSync`, `exec`, timeout, kill, or stdout/stderr supervision outside the ABG actor seam |
| Retry, correction, continuation, and re-entry | ABG | Publish bounded-step outputs and return control | Product-local retry loops, carry-over controller memory, or hidden `next` authority |
| Runtime event emission, append, replay, and projection | ABG | Map domain evidence into admitted event payloads | Direct event append, side ledger mutation, or projection reconstruction that bypasses ABG runtime truth |
| Closure fold and assurance gate | ABG, with product policy and gain inputs | Provide domain interpretation, evaluators, gap reasons, and policy weights | Worker self-report or product postflight directly closing the runtime unit |

Where these surfaces admit a consequential entity transformation, ABG's
admission authority is the graph-native specialization of `STDO-UP-016`. ABG's
broader execution, supervision, retry, and projection authority continues to
derive from existing ODD law, and is not thereby reclassified as admission
authority. `F_P` and `F_H` are the ODD projections of the candidate-producer
and human-adjudication roles that `STDO-UP-016` declares generically.

The audit is not satisfied by reviewing produced artifacts alone. It must
include a code, call-graph, or static-surface review appropriate to the
language and tenant, and it must name the evidence used to rule out hidden
execution authority.

Non-closure conditions include:

- a downstream product contains its own `start` or `iterate` loop for an ABG
  traversal
- product or plugin code supervises worker processes outside the ABG actor seam
- product or plugin code constructs retry, continuation, or re-entry state
  outside ABG
- product or plugin code appends runtime events or mutates runtime ledgers
  without ABG admission
- plugin output carries next-vector, closure, actor-invocation, process, or
  runtime-event authority instead of evidence or policy input
- two controllers can each claim authority for one traversal

If any of those conditions are present, the product may be useful, but it is
not currently ODD-correct over GTL/ABG.

### 11.5C Projection-Source Coherence

Projection and query lanes are downstream read models over admitted carrier,
runtime, event, or source truth.

They may summarize, index, filter, or render that truth.

They must not reconstruct an alternate authority surface beside the admitted
carrier.

For an ODD product, this means:

- function catalog views must reconcile to the admitted GTL module or public
  carrier
- asset ownership and start-target views must be derived from, or structurally
  compared against, the admitted carrier they expose
- runtime status views must derive from ABG runtime facts, events, replay, or
  projection truth
- domain query overlays must fail closed when the carrier they describe is
  missing, stale, or structurally divergent

Name equality is not enough.

A same-named graph function, node, carrier, policy, or route with different
inputs, outputs, vectors, declarations, ownership, or closure law is a different
truth surface until reconciled.

Negative proof for a projection must include structural drift, not only missing
source truth.

### 11.5D Constructive Evaluation And Yield Loop

Every ODD product over GTL/ABG must preserve one constructive evaluation loop
from intent lineage and model synthesis through observation to next lawful
action.

This is the method-level homeostasis loop. The constitutional surface names the
operative functions directly: `synthesize_model`, `eval_gap`, `evaluate_next`,
and `evaluate_action`.

The selected Product outcome under `STDO-UP-013` is external authority for this
loop. Product models, gaps, assurance, ledgers, and projections may interpret
that outcome but cannot author, select, or enlarge it. `evaluate_next` may
select material work only within that outcome or an admitted bounded
prerequisite or experiment. Graph or edge closure is evidence toward Product
acceptance; it is not Product or release acceptance. When the selected outcome
is accepted, an admitted prerequisite is discharged, an admitted experiment's
stated decision is resolved, another admitted terminal condition is reached, or
its governing basis or bound is exhausted, rejected, withdrawn, superseded,
repriced away, or falsified, the loop selects no further material work without
another admitted basis. A `reprice` disposition requests lawful constitutional
re-entry; it does not perform the reprice or select the successor outcome.

The loop is framework-independent. Product implementations may use different
carrier names, but they must preserve this authority shape:

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

The objects have these method-level meanings:

| Object | Definition | Authority |
| --- | --- | --- |
| `IntentLineage` | Admitted source intent and its lineage refs: human, imported source, prior product, intent engine, or prior synthesized construction intent. | ABG event-log truth over source intent. It seeds the product model and must not invent graph actions. |
| `ProductAssetModel` | Desired and known typed asset model synthesized from intent lineage, prior model, and admitted product truth. | Product-owned model truth whose publication basis is carried by admitted events and product-owned projection refs. It is not runtime fact or action authority. |
| `Worksite` | Current workspace, runtime archive, transform assets, product asset root, profile, and observed file or process state. | Observable substrate, not authority by itself. |
| `RuntimeEventLog` | Append-only admitted runtime facts. | ABG runtime truth. |
| `RuntimeProjection` | Replay-derived current runtime state over event log and execution basis. | ABG projection truth. |
| `ObservationSnapshot` | Read-only view of runtime truth plus worksite facts relevant to construction. | ABG evaluator carrier with product domain rows. |
| `GapPressureRow` | Typed pressure over missing, partial, blocked, waiting, or ambiguous assets and evidence. | Product domain meaning over admitted observation. |
| `TargetObligationBinding` | Exact binding from gap pressure to the selected Product outcome, any admitted prerequisite or experiment basis, target assets, required roles, evidence refs, and admissible graph outcomes. | Product domain binding over GTL/ABG action authority. |
| `ActionCatalog` | Published lawful graph actions: graph functions, vectors, targets, inputs, and eligible outcomes. | GTL/product publication consumed by ABG. |
| `NextActionBasis` | Sum type naming why `evaluate_next` is being called: `initial_selection`, `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. `post_reprice` records a re-entry request and carries no action-selection authority. | Dispatch basis for next-action evaluation. It is not a separate controller. |
| `PriorityProjection` | Deterministic ranking over bound lawful actions under visible policy. | ABG evaluator kernel plus product policy. |
| `ConstructionIntent` | Admitted selected action for one bounded graph invocation, preserving the selected outcome or admitted bounded-basis refs carried by its target binding. | ABG admission and traversal authority. |
| `AdmittedEvidence` | Admitted worker, process, product, execution, materialization, liveness, and postflight evidence. | ABG/product admission, not worker self-closure. |
| `EdgeFulfillmentLedger` | Evidence and convergence carrier for one edge attempt or version. | Closure evidence truth. |
| `EdgeClosureDecision` | Sum type over the ledger: close, yield, retry, repair, re-enter, reprice, block. | Closure decision truth. |
| `NextActionProjection` | Read model that observes `NextActionBasis` plus current truth and selects a next graph action only when lawful. | ABG next-action evaluation projection with product policy. |

The loop has one model synthesis function and three distinct evaluation
functions. They may share underlying libraries, but they must not share
authority:

| Function | Inputs | Output | Boundary |
| --- | --- | --- | --- |
| `synthesize_model` | `IntentLineage + prior ProductAssetModel + admitted product truth` | `ProductAssetModel` | Model synthesis. It may update desired and known typed asset truth. It must not observe the worksite, select work, invoke work, or close work. |
| `eval_gap` | `ProductAssetModel + RuntimeEventLog + RuntimeProjection + Worksite` | `ObservationSnapshot + GapPressureRow` | Read-only gap discovery. It compares desired model truth to observed reality and emits missing, partial, blocked, waiting, or ambiguous asset pressure. It does not choose work and does not close work. |
| `evaluate_next` | `NextActionBasis + fresh eval_gap + TargetObligationBinding + ActionCatalog + Policy` | `PriorityProjection + NextActionProjection + selected_action` | Next-action selection. `TargetObligationBinding` carries the exact selected Product outcome and any admitted bounded-basis refs. `NextActionBasis` is either `initial_selection(IntentLineage, ProductAssetModel)` or one explicit post-action basis derived from an `EdgeClosureDecision`: `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. Except for unresolved `post_reprice`, which returns typed no-action pending separately admitted constitutional authority, it may select only published lawful graph actions that bind to the gap and governing basis. It does not admit construction intent and does not evaluate the result of an action. |
| `evaluate_action` | `ConstructionIntent + AdmittedEvidence + TargetObligationBinding + Policy` | `EdgeFulfillmentLedger + EdgeClosureDecision` | Action-result evaluation. It decides close, yield, retry, repair, re-enter, reprice, or block for the action just taken. It does not choose the next graph action. |

The word `evaluator` is not sufficient by itself. A design, ticket, code module,
or proof must name which function it is implementing or consuming:
`synthesize_model`, `eval_gap`, `evaluate_next`, or `evaluate_action`.

Intent has lineage through the loop. Bootstrap or external intent may come from a
human, imported source, prior product, or intent engine. That intent seeds the
product asset model used by `eval_gap`. Current construction intent is
synthesized against that model and the observed gap, then admitted by a distinct
admission step after `evaluate_next` selects a published graph action. Intent
does not invent unpublished actions; gap-derived action selection provides the
selected action basis for admitting current construction intent over an
already-published graph function or vector. `ConstructionIntent` must cite the
lineage, selected action, and `TargetObligationBinding` that preserve the exact
selected Product outcome and any admitted bounded-basis refs.

The loop is governed by these axioms:

**A0. One Surface**

There is one authoritative computational surface for traversal consequence:

```text
IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

No CLI branch, prompt prose, postflight string, gap-dossier action list, query
projection, service method, or local operator summary may become a rival source
of traversal truth.

**A1. Worksite Is Observed, Not Trusted**

The file system, process output, screen logs, worker artifacts, and product
files are observations. They become authority only after admission into typed
evidence and fold into ledger and decision truth.

**A1a. Workspace-Ledger Governed Work Pair**

The worksite/workspace and ledger form the governed work pair:

```text
W = mutable workspace under construction
L = immutable governed ledger of work over W
E = immutable event log / replay spine
Ev = evaluator work over L
```

The workspace is where F_P construction occurs. The ledger is the immutable
governed account of closure-relevant work over that workspace. The ledger is not
a copy of the workspace; it is the admitted trace of callout basis, observed
deltas, file refs, digests, execution evidence, obligations touched, claims
made, evaluator inputs, evaluator outputs, and admission status.

The loop is:

```text
F_P acts in W.
Admission records governed facts in L.
E orders and anchors L entries with predecessor refs.
Ev evaluates a declared L snapshot, not ambient W.
Ev output is itself F_P work and is admitted back into L/E.
L/E constrain the next lawful F_P action in W.
```

The consistency rule is:

```text
W can change without being true.
L can be true without being the whole W.
Closure can only use W through L.
Eval can only judge W through L.
Eval only affects traversal after its own L/E admission.
```

Every closure-relevant F_P callout that does work needs ledger admission.
Evaluator work is not outside F_P merely because it reads ledgers. Evaluator work
is F_P work over governed ledger state, and its result must be admitted into the
immutable ledger/event spine before it can affect closure, routing, or traversal.
Corrections append or supersede ledger/event facts; they do not rewrite the
governed history of work.

**A1b. Ledger Is Governed Attention**

A ledger is the system's governed attention over construction history.

This is a structural analogy, not an implementation dependency on transformer
attention. Model attention selects from context through learned weights. ODD
ledger attention is typed, immutable, lineage-constrained, policy-bounded, and
replayable.

An evaluator may attend only to admitted ledger rows reachable through declared
lineage, predecessor refs, target binding, policy, and the relevant event-log
cursor. Workspace facts, worker prose, archives, summaries, or controller memory
outside that reachable ledger set are not inside the evaluator's lawful
attention surface.

Lineage is therefore not only provenance bookkeeping. Lineage is the attention
graph: it determines which evidence the evaluator may see, what must be ignored,
and which predecessor chain makes the judgment reproducible.

**A2. Exact Target Binding**

Every constructive action must bind the current gap to exact target assets and
obligations before invocation:

```text
selected Product outcome ref
+ optional admitted prerequisite or experiment basis ref
+ gap pressure + target assets + required roles + evidence refs
-> TargetObligationBinding
```

A broad edge cannot satisfy a specific product or evidence gap unless the
binding proves that edge is the lawful action for those exact assets.

**A3. Published Action Law**

`evaluate_next` may rank only published lawful actions from the action catalog.
If the desired action is unpublished, the lawful result is a typed no-action
disposition, not fallback to a broad executive graph or local script.

**A4. Evaluate_Next Totality**

`evaluate_next` must be total.

If `NextActionBasis` is `initial_selection`, `evaluate_next` selects from the
current model, current gap, target binding, catalog, and policy. If
`NextActionBasis` is `post_yield_resume`, `evaluate_next` resumes or yields the
same edge from replay-visible resume truth without classifying the action as
failure. If `NextActionBasis` is `post_close_graph_continuation`,
`evaluate_next` may select the next graph edge after the current edge is closed,
or no action when the graph is complete. For `post_retry`, `post_repair`,
`post_reenter`, and `post_block`:

```text
if higher-priority lawful action exists:
  select it
else if current graph edge remains lawful:
  follow the graph
else if authority is missing:
  reprice or block
else:
  block with typed no-action disposition
```

For `post_reprice`, `evaluate_next` must return a typed no-action disposition
while constitutional re-entry remains unresolved. The reprice decision cannot
authorize a replacement action. Work may be evaluated again only after lawful
re-entry separately admits an exact selected Product outcome or bounded basis
and supplies it through a new `initial_selection` or basis-bearing resume.

Default graph following is ordinary, but it is still an `evaluate_next`
decision, not hidden sequential control.

**A4a. Evaluation Function Separation**

`synthesize_model`, `eval_gap`, `evaluate_next`, and `evaluate_action` are
separate authority functions.

`synthesize_model` may synthesize the current product asset model from
event-log-backed intent lineage, prior model, and admitted product truth only.
It must not observe the worksite, admit construction intent, invoke work, close
work, or select next action.

`eval_gap` may emit observation and gap pressure only. It must not admit
construction intent, invoke work, close work, or select next action.

`evaluate_action` may fold admitted action evidence into ledger and closure
decision only. It must not select the next graph action.

`evaluate_next` may bind target obligations, rank lawful published actions, and
publish next-action projection. It must not admit construction intent or decide
whether the prior action closed, yielded, failed, or requires repair except by
consuming the admitted `EdgeClosureDecision`.

Any module that lets one of these functions perform another function's authority
creates a rival control surface and violates A0.

**A5. F_P Freedom, F_D Authority**

F_P may inspect, discover, reason, draft, transform, and propose within the
bounded action. F_P must not close the edge, emit runtime events, mutate ledgers,
or decide re-entry. F_D/ABG/product admission owns durable evidence and closure
truth.

**A6. Evidence Before Closure**

No edge closes from raw artifact presence, raw worker report, raw process
success, or CLI summary. Closure is a fold over admitted evidence:

```text
AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
```

**A7. Ledger Is Evidence, Not Action Selector**

`EdgeFulfillmentLedger` records evidence and convergence:

```text
counts
obligation rows
materialization refs
liveness refs
admission refs
edge_converged
```

It does not select the next action. Action selection belongs to `evaluate_next`
over `EdgeClosureDecision` plus fresh `eval_gap` truth.

**A8. Closure Decision Is A Sum Type**

The closure decision vocabulary is:

```text
close
yield
retry
repair
re-enter
reprice
block
```

Each disposition is replay-visible and must carry basis and reason refs
sufficient to reproduce the decision.

**A9. Yield Is Lawful Iterate**

`yield` is the lawful iteration boundary:

```text
same edge or attempt remains lawful
progress or waiting state is admitted
resume basis is replay-visible
control returns without failure classification
```

Yield is not retry. Yield is not block. Yield is not timeout. Yield is not a
local CLI loop. It is the pressure-release state that lets long-running,
bounded, or partially productive work return control without losing the current
edge.

**A10. Liveness Does Not Close Semantic Truth**

Liveness observes activity, inactivity, process state, and interruption. It can
support yield or liveness interruption. It cannot by itself declare semantic
failure, semantic closure, or requirement non-satisfaction.

**A11. Re-Entry Is Graph Law**

Repair and re-entry are graph actions selected by `evaluate_next` from admitted
closure truth and published action authority. They are not local retry branches
over strings.

`evaluate_action` may emit `repair` or `re-enter` as a closure disposition.
`evaluate_next` selects which published graph action realizes that repair or
re-entry. Disposition is conceptual; selection is invocational.

**A12. Public Query Is A Read-Only Evaluation View**

A public query or gaps view may render read-only outputs from `eval_gap`,
`evaluate_action`, and `evaluate_next`: gap pressure, closure decision, and
next-action projection. It must not append events, invoke workers, admit intent,
run `evaluate_action`, or choose traversal by itself.

**A13. Replayability**

Every closure decision and next-action selection must be reproducible from:

```text
RuntimeEventLog
+ execution basis
+ ABG event-log-backed IntentLineage
+ ProductAssetModel publication basis and its event refs
+ selected Product outcome identity and admitted bounded-basis refs
+ GapPressureRow
+ TargetObligationBinding
+ ActionCatalog
+ admitted evidence
+ EdgeFulfillmentLedger
+ EdgeClosureDecision
+ NextActionBasis
+ visible policy refs
```

If replay cannot reproduce the decision, the implementation has created hidden
state.

**A13a. Causal Chain Integrity**

Each governing admitted or replay-derived carrier and projection in the loop
must reference its causal predecessor refs:

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> NextActionProjection (selected_action)
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionBasis
-> NextActionProjection (next)
```

The target binding must be reachable from the exact selected Product outcome
and any admitted bounded-basis refs. The first `NextActionProjection` in the
chain carries the selected action that admits `ConstructionIntent`, which
preserves those authority refs. The second `NextActionProjection` is the
post-action projection produced from `NextActionBasis` plus fresh `eval_gap`
truth. Both must be reachable from their predecessor refs.

A13 requires that the decision can be reproduced from the inputs. A13a
requires that each governing carrier or projection carry the predecessor refs
that make reproduction reachable without external joins. A broken predecessor
chain is non-replayable at the carrier level and therefore fails A13.

**A14. Recursive Published Refinement**

The homeostasis loop recurses over published refinement.

If a graph function refines an outer vector into published inner vectors, each
inner vector boundary obeys `synthesize_model`, `eval_gap`, `evaluate_next`, and
`evaluate_action` with its own visible model, gap, binding, action, evidence,
ledger, closure, and next-action projection.

If the inner realization is intentionally opaque, it is ordinary implementation
inside one bounded action. It may use local control flow to compute the action's
internal result, but it must not publish, dispatch, retry, repair, re-enter, or
close graph work as a hidden traversal controller. Once a refinement is
published as graph structure, it is governed by the loop recursively.

**A15. Method Ownership**

ABG owns runtime truth, event replay, graph-call lifecycle, actor/process
supervision, continuation, and re-entry mechanics. The product owns domain asset
meaning, graph-function catalog meaning, gap interpretation, and priority
policy. Design Module Method governs realization modules inside that split; it
must not fragment `eval_gap`, `evaluate_next`, or `evaluate_action` into
module-local decision authorities.

**A16. Constitutional Override**

For any ticket, design, code module, or proof that touches `synthesize_model`,
`eval_gap`, `evaluate_next`, `evaluate_action`, traversal, gap evaluation,
action selection, construction intent, worker invocation, evidence admission,
fulfillment, liveness, closure, re-entry, public query, or live proof, the
causally applicable members of this axiom set and the constitutional equation
are the controlling acceptance constraints for the selected Product outcome
and affected published boundary. Unchanged accepted relations cite their
accepted basis rather than being re-proven. The axiom family does not authorize
horizontal realization growth, create Product work, or widen the selected
outcome.

Ticket-local closure wording, test names, source-grep checks, compact CLI
summaries, or implementation notes cannot weaken the constitutional loop. If a
ticket appears complete by its local checklist but leaves a rival traversal
consequence path, the ticket is not constitutionally complete. The lawful
result is to request lawful re-entry, keep the gap as a closure blocker, or
admit separately bounded paydown under an independently selected Product
outcome or prerequisite basis.

The following artifacts may provide evidence, diagnostics, or read-model
context only. They must not independently close an edge, select a next action,
or route retry, repair, or re-entry:

```text
gap dossier
postflight report
assurance report
materialization manifest
runtime liveness projection
run summary
worker prose
screen or PTY transcript
prompt package
harness target argument
source-grep test
CLI branch or compact output
public query or gaps view
service method output
```

If any of those artifacts conflict with the admitted `EdgeFulfillmentLedger`,
`EdgeClosureDecision`, or `NextActionProjection`, the ledger, decision, and
projection chain wins. If that chain is absent, the edge has not
constitutionally closed and the next action has not been constitutionally
selected.

The constitutional equation is:

```text
let U = (selected_product_outcome_ref, optional_admitted_bounded_basis_ref)
let L = project_intent_lineage_from_event_log(source_intent_refs, prior_intent_refs)
let M0 = synthesize_model(L, prior_model, admitted_product_truth)
let G0 = eval_gap(M0, RuntimeEventLog, RuntimeProjection, Worksite)
let O = G0.observation
let B0 = bind(U, G0.pressures, ActionCatalog, target obligations)
let Q0 = initial_selection(L, M0)
let N0 = evaluate_next(Q0, G0, B0, ActionCatalog, Policy)
let I = admit_construction_intent(L, B0, N0.selected_action, N0.next_action_projection)
let E = admit_evidence(invoke(I))
let A = evaluate_action(I, E, B0, Policy)
let M1 = synthesize_model(L, M0, admitted_product_truth)
let G1 = eval_gap(M1, RuntimeEventLog, RuntimeProjection, Worksite)
let B1 = bind(U, G1.pressures, ActionCatalog, target obligations)
let Q1 = next_action_basis_from(A.decision)
let N1 = evaluate_next(Q1, G1, B1, ActionCatalog, Policy)

return N1
```

Where:

```text
A.ledger = EdgeFulfillmentLedger
A.decision = EdgeClosureDecision
A.decision.disposition in {close, yield, retry, repair, re-enter, reprice, block}
Q0.kind = initial_selection
Q1.kind in {
  post_yield_resume,
  post_close_graph_continuation,
  post_retry,
  post_repair,
  post_reenter,
  post_reprice,
  post_block
}
Q1.kind = post_reprice and no separately admitted constitutional basis
  => N1 = typed no-action pending re-entry
```

The implementation is correct only when the next work decision is derived from
that equation, `U` remains causally reachable through the target binding and
construction intent, and no other path can decide what work happens next.

### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law

### 11.7 Manual Walkthrough Must Still Be Lawful

Automation must remain true for a manual walkthrough.

A human operator, using only the declared authority surfaces, should be able to:

1. identify the current asset state (current typed asset or node)
2. identify the next lawful vector and its public graph-function carrier (vector is the constitutional transition contract; the graph function is the published constructive program that realizes it — see §5.2 and §5.3)
3. determine the required inputs, evaluators, output contract, and carried environment
4. construct or assess the next asset (produced asset or checkpoint)
5. repeat until target-relative closure is reached

Automation may make this faster, safer, or more repeatable. It may not invent a different process.

**Automation is lawful** when it:

- renders prompts
- scaffolds artifacts
- selects the next traversal step
- runs workers
- collects evidence
- assesses closure

**Automation is unlawful** when it:

- skips undeclared nodes
- fabricates authority not present in the declared surfaces
- collapses multiple constitutional transitions into one opaque step without declaring the refinement
- depends on implementation-carrier knowledge that the installed product should not have
- collapses the installed builder and the product under development into one authority surface during self-host work

If the team cannot explain the manual traversal, the automation is not yet method-safe. If automation cannot be explained in these terms, it is ahead of the method.

### 11.7A Conforming Agentic Development

ODD method is the premise for conforming agentic development over the graph-native worksite. An agentic coder produces governed work by following the constitutional process over a minimal declared authority packet, with the artifacts it produces gated by admission. `SPEC_METHOD.md` governs the general constitutional process and `TICKET_METHOD.md` governs artifact admission; this section names the ODD specialization and composes that law rather than re-declaring it.

Conformance has two halves: an F_P proof that the process is followable, and an F_D gate that admits the produced artifacts.

**The walkthrough is the conformance proof.**

§11.7 requires automation to remain true for a manual walkthrough. The agentic form of that law is a conformance test of the method itself: an agentic coder executes the constitutional process end-to-end on real work — intake triage, smallest lawful re-entry, the spec/requirement/design/ticket chain, the constructive evaluation loop of §11.5D, and closure proof — using only the declared authority surfaces. The agentic coder is F_P over the constitutional process.

The agent works from a minimal declared authority packet, not from memory and not from wholesale hidden context. `SPEC_METHOD.md` already requires declared context — input/output contract, required context, role, evaluator regime, and provenance — for any agentic work unit. The ODD addition is that the packet carries only the smallest declared authority sufficient to decide the step, with its source refs, and that conformance is enforced by admitting the produced artifact rather than by enlarging what the agent must hold. Compression is prompt input, never the deciding authority.

The walkthrough proves at two levels:

- the work it produces must be lawful: correct change-class, traceable, admitted
- a point where the walkthrough cannot proceed is a method defect only when a competent agent, correctly configured and using the declared authority, still cannot decide — ambiguity, a missing step, contradictory authority, or an un-decidable change-class in an owning surface. That defect is repriced into the owning authority surface, the same way a failed manual traversal is a graph defect under §11.7.

An agent that ignored the declared authority, relied on stale memory, or reasoned badly has produced agent error, not a method defect. Admission rejects the malformed artifact either way, so a bad agent turn neither becomes law nor silently indicts the method.

This proof is independent of any automated runtime. A live lane that depends on external execution conditions — an overloaded model API, a flaky transport — cannot prove the constitutional process is sound, because it conflates process validity with runtime availability. The walkthrough proves the process; the runtime only executes it.

**The validator is the conformance gate.**

The constitutional process is an interface contract, and interface conformance is enforced by validating artifacts against the contract, not by the conformer holding the contract.

ODD does not re-declare the artifact rules. Tickets, change-class declarations, design-module derivations, and execution contracts are admitted under `SPEC_METHOD.md` and `TICKET_METHOD.md`, which already require that a drafted classification be admitted or rejected against deterministic criteria rather than taken as automatic truth. ODD requires only that agentic development pass through that admission: the agentic coder produces the artifact; the declared admission gates it deterministically, fail-closed, naming the violated rule — exactly as a typed asset is enforced by its constructor (§11.1).

This preserves the F_P/F_D split at the method layer. The agentic coder is F_P: it reasons, drafts, and proposes within the declared packet. Admission is F_D: it decides whether the produced artifact conforms. The walkthrough establishes that the process is followable; admission establishes that each act of following it conforms.

**Conformance is not approval-by-usage.**

A passed admission and a completed walkthrough are conformance evidence, not ratification. Shared method change still follows §9: grey work is not made constitutional by repeated agentic execution. The agentic coder conforms to the method; it does not amend the method by acting.

### 11.7B Real Authority-Path Negative Proof (`STDO-UP-010`)

Negative proof for an ODD or graph-native boundary exercises the supported
Product authority path. It must not manufacture the refusal state, blocked
event, gap, or verdict that the system is supposed to derive.

Closure-grade negative evidence identifies the supported entry and governing
authority, invalidates the real authority-bearing input, exercises the
supported path, proves refusal before the prohibited effect, and establishes
that no legacy, fallback, reconstruction, or parallel path succeeds. Source,
packaged, installed, and runtime absence are distinct claims.

Where these identities apply, the supported relation is:

```text
public entry
  -> admitted GTL composition owns traversal topology
  -> named GraphFunction supplies the callable work contract
  -> implementation or plugin binding realizes only its admitted seam
  -> ABG owns traversal, event, continuation, and replay truth
  -> replay-derived projection
  -> typed Product outcome or continuation
```

No CLI, SDK, service, adapter, plugin, fixture, query, or projection may become
a rival traversal controller. The consumer owns the concrete test and evidence
mechanism; this section owns the property that mechanism must prove.

### 11.8 Cumulative Environment Law Is Mandatory

Do not model composition as "the last output feeds the next input".

The real ODD law is cumulative typed environment.

Each retained `GraphFunction` should declare:

- `environment.requires`
- `environment.provides`
- `environment.carries`

Later functions may require any typed binding available in the cumulative carried environment, not only the immediately previous output.

If a product publishes graph functions without this cumulative environment law, the line is graph-shaped but structurally wrong.

### 11.9 Global Convergence Must Be Stable Under Zoom

Local green arcs are not enough.

If an outer public carrier is refined into inner executable structure, then:

- the refined inner chain must close lawfully
- the enclosing coarse contract must also remain true after fold-back
- zoomed and unzoomed views must agree on whether the enclosing carrier is open or closed

For current product closure, live current requirements that lack an executable proof witness keep the enclosing carrier open until they are:

- realized
- explicitly deferred
- explicitly repriced out of the active branch

For the active software line, the immediate pressure is usually realized testcase or archived test evidence, but the governing law is proof-lane aware: the witness must be a governed realized proof surface appropriate to the requirement class.

---
```

Successor, `ODD.md#11-core-law`:

```text
## 11. Core law

An ODD product is built correctly only when every clause of this section
holds (P6).

### 11.1 Typed assets and nodes are explicit

The product works over explicit typed assets or typed nodes. It does not
work over one hidden project blob, one giant mutable workspace object or one
undocumented service payload. Concrete assets must bind explicitly into
typed domain boundaries. Where an asset is a real produced or consumed boundary,
its `asset_surface` is declared (P3).

### 11.2 Graph functions are the primary constructive carrier

Every operative constructive step is carried by one named `GraphFunction`
or one lawful graph-function composition. The real carrier is never left
inside orchestration loops, bespoke Python pipeline runners, controller
scripts, or service methods that only happen to call GTL-adjacent helpers
(P0, P4a).

### 11.2A Outcome-first realisation order

Because this profile makes an edge traversal the unit of compute, an ODD
product must use that unit of compute to build its own operative framework
behaviour. The required order is: declare the outcome
traversal over typed assets; publish the declarative GTL/ABG carrier
structure; implement only the minimal imperative adapter code that remains
necessary (P0, P6).

An outcome traversal declares the governed movement before
implementation: source asset type; target asset type; edge traversal or
graph-function name; closure or evaluation obligation; lineage obligation;
ambiguity or gap obligation; allowed `F_D`, `F_P` and `F_H` bindings. The
declarative carrier structure is GTL graph functions, typed nodes,
vectors, operator bindings, evaluator bindings, carrier schemas, policy
declarations, projection declarations and lineage ledger declarations
(P0, P3).

Imperative adapter code is lawful only where it transports or persists
facts: file or network IO; CLI or API transport; event persistence;
runtime invocation; projection rendering; tool execution already admitted
by a declared traversal. Imperative code must not own domain meaning,
semantic target movement, step selection, closure semantics, lineage truth
or constructive workflow truth. Framework behaviour implemented
imperatively first and only later described in GTL vocabulary is
ODD-shaped but not yet ODD-built (P6, P0).

### 11.3 The function catalogue is published

The live line must publish a machine-readable function catalogue. At
minimum each retained function should expose its name, inputs, outputs,
intent, and public or helper role. A callable surface that exists only in
prose or in prompt memory leaves the product under-built (P6, P3).

### 11.4 The GTL module is the operative publication surface

The product must publish the public graph-function carriers, the graph or
graphs those carriers traverse, typed node and vector surfaces, and the
semantic jobs or equivalent outer callable contracts bound to the public
carrier. Callers are never bound directly to hidden inner vectors (P4a,
P3).

Where a public carrier refines into inner executable structure, the live
traversal boundaries are published explicitly through lawful GTL boundary
surfaces such as `RefinementBoundary` or `CandidateFamily`. The outer
public carrier remains the callable contract (P4a, P3).

### 11.5 Current state is a projection over constructive history

Visible current state is a projection and does not replace runtime truth.
The ODD query lane may expose asset views, function catalogue views,
checkpoint overlays, provenance overlays and domain-specific
explainability overlays; it must not redefine ABG runtime facts (P3, P6).

### 11.5A ABG owns continuation and re-entry

An ODD application over GTL/ABG is a cooperative subsystem, not a
replacement runtime. ABG owns continuation authority, re-entry after
publish boundaries, the graph-call lifecycle, and step selection over the
declared graph (P6, P0).

The product may publish typed assets and evidence, execute one admitted
bounded constructive step, publish downstream read models or domain
overlays, and return control to ABG. The product must not own a hidden
continuation loop; carry multi-step controller memory across publish
boundaries; infer later steps locally instead of re-entering through ABG;
treat public `next` and explicit graph-function continuation as rival
authorities inside one controller; or build product-local orchestration
that in effect replaces ABG (P6).

An application that replaces ABG continuation with tenant-local control
flow no longer behaves as an ODD application over GTL/ABG. It has drifted
into a different architecture that only happens to publish some
ODD-shaped artifacts (P6).

### 11.5B Execution authority audit

An ODD product over GTL/ABG that changes runtime, `start` or `iterate`,
worker transport, actor invocation, process supervision, plugin dispatch,
event projection, closure, assurance, retry or continuation semantics
must include an execution-authority audit before activation and closure
(P6).

The audit must prove that exactly one execution authority exists for the
affected traversal. For a consumer using the GTL and ABG roles, that
authority is the one consumer-bound realisation of the ABG role, including
when the realisation under change itself implements that role. A
different realisation is lawful only under an explicitly ratified,
non-overlapping runtime scope (P6, P3).

The audit must inventory at least these surfaces (P6):

| Surface | Lawful owner | Product or plugin role | Forbidden local implementation |
| --- | --- | --- | --- |
| Traversal selection and vector advance | ABG | Declare graph functions, vectors, assets, and domain policy inputs | Product-local runner deciding the next traversal step |
| Actor invocation and process supervision | ABG | Provide actor bindings, prompts, payload adapters, and evidence adapters | Product-local worker `spawn`, `spawnSync`, `exec`, timeout, kill, or stdout/stderr supervision outside the ABG actor seam |
| Retry, correction, continuation, and re-entry | ABG | Publish bounded-step outputs and return control | Product-local retry loops, carry-over controller memory, or hidden `next` authority |
| Runtime event emission, append, replay, and projection | ABG | Map domain evidence into admitted event payloads | Direct event append, side ledger mutation, or projection reconstruction that bypasses ABG runtime truth |
| Closure fold and assurance gate | ABG, with product policy and gain inputs | Provide domain interpretation, evaluators, gap reasons, and policy weights | Worker self-report or product postflight directly closing the runtime unit |

Where these surfaces admit a consequential entity transformation, ABG's
admission authority is the graph-native specialisation of transformation
admission completeness, whose admission semantics
[ACTIVATION §4](ACTIVATION.md#complete-enclosing-relation-admission) owns;
the software-design profile restates the predecessor rule in
[DESIGN_MODULE, Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016)
(provenance rc.2
[STDO-UP-016](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)).
ABG's broader execution, supervision, retry and projection authority
continues to derive from this profile and is not thereby reclassified as
admission authority. `F_P` and `F_H` are the ODD projections of the
candidate-producer and human-adjudication roles, which this profile binds
to the source concepts of SPEC_METHOD §5 in
[§5 Probabilistic compute](#probabilistic-compute) (P6, P1).

Reviewing produced artifacts alone does not satisfy the audit. It must
include a code, call-graph or static-surface review appropriate to the
language and tenant, and it must name the evidence used to rule out hidden
execution authority (P6).

Any of these conditions prevents closure (P6):

- a downstream product contains its own `start` or `iterate` loop for an
  ABG traversal;
- product or plugin code supervises worker processes outside the ABG
  actor seam;
- product or plugin code constructs retry, continuation or re-entry state
  outside ABG;
- product or plugin code appends runtime events or mutates runtime ledgers
  without ABG admission;
- plugin output carries next-vector, closure, actor-invocation, process
  or runtime-event authority instead of evidence or policy input;
- two controllers can each claim authority for one traversal.

When any is present, the product may be useful but is not currently
ODD-correct over GTL/ABG (P6).

### 11.5C Projection-source coherence

Projection and query lanes are downstream read models over admitted
carrier, runtime, event or source truth. They may summarise, index,
filter or render that truth; they must not reconstruct an alternate
authority surface beside the admitted carrier (P3, P6).

For an ODD product: function catalogue views must reconcile to the
admitted GTL module or public carrier; asset ownership and start-target
views must be derived from, or structurally compared against, the admitted
carrier they expose; runtime status views must derive from ABG runtime
facts, events, replay or projection truth; domain query overlays must fail
closed when the carrier they describe is missing, stale or structurally
divergent (P3, P6).

Name equality is not enough. A same-named graph function, node, carrier,
policy or route with different inputs, outputs, vectors, declarations,
ownership or closure law is a different truth surface until reconciled.
Negative proof for a projection must include structural drift, not only
missing source truth (P3, P6).

### 11.5D Constructive evaluation and yield loop

Every ODD product over GTL/ABG must preserve one constructive evaluation
loop running from intent lineage and model synthesis through observation
to the next lawful action. This is the profile's homeostasis loop, and
its constitutional surface names the operative functions directly:
`synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action`
(P2, P5, P6). The loop is this profile's binding of
[ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation):
it corrects towards the required conditions as observations arrive,
guarantees neither convergence nor the adequacy of those conditions, and
its diagnoses distinguish the four causes named there (P2, P6).

The selected Product outcome under STDO-UP-013
([SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation)) is external
authority for this loop. Product models, gaps, assurance, ledgers and
projections may interpret that outcome but cannot author, select or
enlarge it. `evaluate_next` may select material work only within that
outcome or within an admitted bounded prerequisite or experiment. Graph or
edge closure is evidence toward Product acceptance and is neither Product
nor release acceptance (P2, P6).

The loop selects no further material work without another admitted basis
once the selected outcome is accepted; an admitted prerequisite is
discharged; an admitted experiment's stated decision is resolved; another
admitted terminal condition is reached; or its governing basis or bound
is exhausted, rejected, withdrawn, superseded, repriced away or
falsified. A `reprice` disposition requests lawful constitutional
re-entry; it neither performs the reprice nor selects the successor
outcome (P2, P6).

The loop is framework-independent. Implementations may use other carrier
names but must keep this authority shape (P6, P4a):

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

The objects have these meanings (P3, P6):

| Object | Definition | Authority |
| --- | --- | --- |
| `IntentLineage` | Admitted source intent and its lineage refs: human, imported source, prior product, intent engine, or prior synthesized construction intent. | ABG event-log truth over source intent. It seeds the product model and must not invent graph actions. |
| `ProductAssetModel` | Desired and known typed asset model synthesized from intent lineage, prior model, and admitted product truth. | Product-owned model truth whose publication basis is carried by admitted events and product-owned projection refs. It is not runtime fact or action authority. |
| `Worksite` | Current workspace, runtime archive, transform assets, product asset root, profile, and observed file or process state. | Observable substrate, not authority by itself. |
| `RuntimeEventLog` | Append-only admitted runtime facts. | ABG runtime truth. |
| `RuntimeProjection` | Replay-derived current runtime state over event log and execution basis. | ABG projection truth. |
| `ObservationSnapshot` | Read-only view of runtime truth plus worksite facts relevant to construction. | ABG evaluator carrier with product domain rows. |
| `GapPressureRow` | Typed pressure over missing, partial, blocked, waiting, or ambiguous assets and evidence. | Product domain meaning over admitted observation. |
| `TargetObligationBinding` | Exact binding from gap pressure to the selected Product outcome, any admitted prerequisite or experiment basis, target assets, required roles, evidence refs, and admissible graph outcomes. | Product domain binding over GTL/ABG action authority. |
| `ActionCatalog` | Published lawful graph actions: graph functions, vectors, targets, inputs, and eligible outcomes. | GTL/product publication consumed by ABG. |
| `NextActionBasis` | Sum type naming why `evaluate_next` is being called: `initial_selection`, `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. `post_reprice` records a re-entry request and carries no action-selection authority. | Dispatch basis for next-action evaluation. It is not a separate controller. |
| `PriorityProjection` | Deterministic ranking over bound lawful actions under visible policy. | ABG evaluator kernel plus product policy. |
| `ConstructionIntent` | Admitted selected action for one bounded graph invocation, preserving the selected outcome or admitted bounded-basis refs carried by its target binding. | ABG admission and traversal authority. |
| `AdmittedEvidence` | Admitted worker, process, product, execution, materialization, liveness, and postflight evidence. | ABG/product admission, not worker self-closure. |
| `EdgeFulfillmentLedger` | Evidence and convergence carrier for one edge attempt or version. | Closure evidence truth. |
| `EdgeClosureDecision` | Sum type over the ledger: close, yield, retry, repair, re-enter, reprice, block. | Closure decision truth. |
| `NextActionProjection` | Read model that observes `NextActionBasis` plus current truth and selects a next graph action only when lawful. | ABG next-action evaluation projection with product policy. |

The loop has one model-synthesis function and three distinct evaluation
functions. They may share underlying libraries; they must not share
authority (P6):

| Function | Inputs | Output | Boundary |
| --- | --- | --- | --- |
| `synthesize_model` | `IntentLineage + prior ProductAssetModel + admitted product truth` | `ProductAssetModel` | Model synthesis. It may update desired and known typed asset truth. It must not observe the worksite, select work, invoke work, or close work. |
| `eval_gap` | `ProductAssetModel + RuntimeEventLog + RuntimeProjection + Worksite` | `ObservationSnapshot + GapPressureRow` | Read-only gap discovery. It compares desired model truth to observed reality and emits missing, partial, blocked, waiting, or ambiguous asset pressure. It does not choose work and does not close work. |
| `evaluate_next` | `NextActionBasis + fresh eval_gap + TargetObligationBinding + ActionCatalog + Policy` | `PriorityProjection + NextActionProjection + selected_action` | Next-action selection. `TargetObligationBinding` carries the exact selected Product outcome and any admitted bounded-basis refs. `NextActionBasis` is either `initial_selection(IntentLineage, ProductAssetModel)` or one explicit post-action basis derived from an `EdgeClosureDecision`: `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. Except for unresolved `post_reprice`, which returns typed no-action pending separately admitted constitutional authority, it may select only published lawful graph actions that bind to the gap and governing basis. It does not admit construction intent and does not evaluate the result of an action. |
| `evaluate_action` | `ConstructionIntent + AdmittedEvidence + TargetObligationBinding + Policy` | `EdgeFulfillmentLedger + EdgeClosureDecision` | Action-result evaluation. It decides close, yield, retry, repair, re-enter, reprice, or block for the action just taken. It does not choose the next graph action. |

The word evaluator is not sufficient by itself. A design, ticket, code
module or proof must name which function it implements or consumes:
`synthesize_model`, `eval_gap`, `evaluate_next` or `evaluate_action`
(P6, P3).

Intent has lineage through the loop. Bootstrap or external intent may come
from a human, an imported source, a prior product or an intent engine;
that intent seeds the product asset model that `eval_gap` uses. Current
construction intent is synthesised against that model and the observed
gap, then admitted by a distinct admission step after `evaluate_next`
selects a published graph action. Intent does not invent unpublished
actions: gap-derived action selection supplies the selected action basis
for admitting current construction intent over an already-published graph
function or vector. `ConstructionIntent` must cite the lineage, the
selected action and the `TargetObligationBinding` that preserve the exact
selected Product outcome and any admitted bounded-basis refs (P4b, P6).

The loop is governed by the axioms A0 to A16, each a labelled paragraph
below (P6).

A0 One surface. There is one authoritative computational surface for
traversal consequence (P6, P3):

```text
IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

No CLI branch, prompt prose, postflight string, gap-dossier action list,
query projection, service method or local operator summary may become a
rival source of traversal truth (P6).

A1 Worksite is observed, not trusted. The file system, process output,
screen logs, worker artifacts and product files are observations. They
become authority only after admission into typed evidence and their fold
into ledger and decision truth (P6, P3).

A1a Workspace-ledger governed work pair. The worksite or workspace and the
ledger form the governed work pair (P3, P4b):

```text
W = mutable workspace under construction
L = immutable governed ledger of work over W
E = immutable event log / replay spine
Ev = evaluator work over L
```

The workspace is where F_P construction happens. The ledger is the
immutable governed account of closure-relevant work over that workspace;
it is not a copy of the workspace but the admitted trace of callout basis,
observed deltas, file refs, digests, execution evidence, obligations
touched, claims made, evaluator inputs, evaluator outputs and admission
status. The loop is (P3, P6):

```text
F_P acts in W.
Admission records governed facts in L.
E orders and anchors L entries with predecessor refs.
Ev evaluates a declared L snapshot, not ambient W.
Ev output is itself F_P work and is admitted back into L/E.
L/E constrain the next lawful F_P action in W.
```

The consistency rule is (P3, P6):

```text
W can change without being true.
L can be true without being the whole W.
Closure can only use W through L.
Eval can only judge W through L.
Eval only affects traversal after its own L/E admission.
```

Every closure-relevant F_P callout that does work needs ledger admission.
Evaluator work is not outside F_P merely because it reads ledgers: it is
F_P work over governed ledger state, and its result must be admitted into
the immutable ledger and event spine before it can affect closure, routing
or traversal. Corrections append or supersede ledger and event facts; they
do not rewrite the governed history of work (P4b, P6, P3).

A1b Ledger is governed attention. A ledger is the system's governed
attention over construction history. This is a structural analogy and not
an implementation dependency on transformer attention: model attention
selects from context through learned weights, while ODD ledger attention
is typed, immutable, lineage-constrained, policy-bounded and replayable.
An evaluator may attend only to admitted ledger rows reachable through
declared lineage, predecessor refs, target binding, policy and the
relevant event-log cursor. Workspace facts, worker prose, archives,
summaries and controller memory outside that reachable ledger set lie
outside the evaluator's lawful attention surface. Lineage is therefore
not only provenance bookkeeping: it is the attention graph that decides
which evidence the evaluator may see, what it must ignore, and which
predecessor chain makes the judgment reproducible (P0, P6, P3).

A2 Exact target binding. Every constructive action must bind the current
gap to exact target assets and obligations before invocation (P2, P3):

```text
selected Product outcome ref
+ optional admitted prerequisite or experiment basis ref
+ gap pressure + target assets + required roles + evidence refs
-> TargetObligationBinding
```

A broad edge cannot satisfy a specific product or evidence gap unless the
binding proves that edge is the lawful action for those exact assets
(P2).

A3 Published action law. `evaluate_next` may rank only published lawful
actions from the action catalogue. If the desired action is unpublished,
the lawful result is a typed no-action disposition, not a fallback to a
broad executive graph or a local script (P6, P5).

A4 `evaluate_next` totality. `evaluate_next` must be total. On
`initial_selection` it selects from the current model, current gap, target
binding, catalogue and policy. On `post_yield_resume` it resumes or yields
the same edge from replay-visible resume truth without classifying the
action as failure. On `post_close_graph_continuation` it may select the
next graph edge after the current edge closed, or no action when the graph
is complete. On `post_retry`, `post_repair`, `post_reenter` and
`post_block` it follows this rule (P5, P6):

```text
if higher-priority lawful action exists:
  select it
else if current graph edge remains lawful:
  follow the graph
else if authority is missing:
  reprice or block
else:
  block with typed no-action disposition
```

On `post_reprice`, `evaluate_next` must return a typed no-action
disposition while constitutional re-entry stays unresolved. The reprice
decision cannot authorise a replacement action; work may be evaluated
again only after lawful re-entry separately admits an exact selected
Product outcome or bounded basis and supplies it through a new
`initial_selection` or a basis-bearing resume. Default graph following is
ordinary, but it is still an `evaluate_next` decision and not hidden
sequential control (P5, P2, P6).

Selection is not a result of the core. `evaluate_next`'s selection, a
typed no-action disposition included, selects what is invoked next and is
not a value of the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results); it maps to no core
value. The closure decision it follows, where there is one, carries the
core value, as mapped under A8 below, and selection stays invocational
(A11) (P5, P6).

A4a Evaluation function separation. `synthesize_model`, `eval_gap`,
`evaluate_next` and `evaluate_action` are separate authority functions.
`synthesize_model` may synthesise the current product asset model from
event-log-backed intent lineage, prior model and admitted product truth
only; it must not observe the worksite, admit construction intent, invoke
work, close work or select the next action. `eval_gap` may emit
observation and gap pressure only; it must not admit construction intent,
invoke work, close work or select the next action. `evaluate_action` may
fold admitted action evidence into ledger and closure decision only; it
must not select the next graph action. `evaluate_next` may bind target
obligations, rank lawful published actions and publish the next-action
projection; it must not admit construction intent or decide whether the
prior action closed, yielded, failed or needs repair except by consuming
the admitted `EdgeClosureDecision`. A module that lets one of these
functions exercise another's authority creates a rival control surface
and violates A0 (P6).

A5 F_P freedom, F_D authority. F_P may inspect, discover, reason, draft,
transform and propose within the bounded action. F_P must not close the
edge, emit runtime events, mutate ledgers or decide re-entry. F_D, ABG and
product admission own durable evidence and closure truth (P0, P6). An F_P
worker must not be given an F_D-authored semantic extraction recipe when
the edge requires F_P judgment (P0, P6; provenance rc.2
authority_compressions/design_module_method.compressed.md, a claim no
rc.2 body states).

A6 Evidence before closure. No edge closes from raw artifact presence, a
raw worker report, raw process success or a CLI summary. Closure is a fold
over admitted evidence (P6):

```text
AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
```

A7 Ledger is evidence, not action selector. `EdgeFulfillmentLedger`
records evidence and convergence (P6, P3):

```text
counts
obligation rows
materialization refs
liveness refs
admission refs
edge_converged
```

It does not select the next action. Action selection belongs to
`evaluate_next` over `EdgeClosureDecision` plus fresh `eval_gap` truth
(P6).

A8 Closure decision is a sum type. The closure decision vocabulary is
closed (P5, P6):

```text
close
yield
retry
repair
re-enter
reprice
block
```

Each disposition is replay-visible and must carry basis and reason refs
sufficient to reproduce the decision (P5, P6).

Mapping of the closure decision to the core result algebra, new in this
corpus. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
every outcome in the core or in a refinement that maps each refined value
to exactly one core value and adds no core value. Material relation: a
composite over the edge joins each closure decision as one core value, so
a failure, an undecided closure and a needed re-entry stay distinct (P5,
P6). The closure decision is `evaluate_action`'s result over admitted
evidence, mapped for the predicate "the edge's obligations are fulfilled
on the exact basis". The bounded action it judges has its own step result
under [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
for "a candidate is available", and neither value counts toward the
other's predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Each decision keeps its own vocabulary and its basis and reason refs
beside its core value (P5, P6).

Refined by cause. Where a decision would map to one of two core values
according to its cause, the cause is part of the refined value, written
in parentheses as in `re-enter(basis)`, and each refined value maps once
(FOUNDATIONS §4 Results, Refinements). The cause is read from the
decision's basis and reason refs, which A8 requires to be sufficient to
reproduce it. The seven decisions of A8 stay the closed vocabulary; a
refined value names a decision and its cause and adds no decision (P5,
P6). The causes are:

- `retry(defeated)`: admissible evidence defeats the edge for this attempt
  while the same action stays lawful; `retry(undecided)`: every other
  retry, as after a liveness interruption, which alone never gives
  `retry(defeated)` (A10).
- `repair(implementation)` and `repair(proof)`: the edge's governing
  relation, basis and target binding stay coherent, and a local defect,
  in the implementation or in its proof, keeps the edge from closing, so
  a repair of the same edge is the lawful next action (A11).
  `repair(implementation)`: admitted evidence shows the implementation
  failing an edge obligation; `repair(proof)`: every other repair, the
  defect being in the proof.
- `re-enter(undeclared)` and `block(undeclared)`: the cause is a relation,
  capability or authority that no admitted basis declares;
  `re-enter(basis)` and `block(basis)`: every other cause, the current
  basis being unable to support the edge, as when it is stale, substituted
  or unrepairable. A decision with both causes records both and takes the
  `basis` value, as
  [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
  decides for `re_entry_requested`.

| Decision | Core value | Ground |
|---|---|---|
| `close` | satisfied | the ledger's admitted evidence fulfils the edge's obligations on the exact basis |
| `yield` | indeterminate | the edge stays lawful and the admitted evidence, progress or a waiting state, does not yet decide its obligations; the replay-visible resume basis names what would decide; no failure is classified, as A9 requires |
| `retry(defeated)` | falsified | the evidence that defeats the edge for this attempt is the counterexample; A9 separates this failure-classified re-attempt from yield |
| `retry(undecided)` | indeterminate | the attempt ended without evidence that decides the edge's obligations; the decision's reason refs name the re-attempt that would decide |
| `repair(implementation)` | falsified | the failing obligation row is the counterexample (P5, P6) |
| `repair(proof)` | indeterminate | the defect is in the proof, so the admitted evidence cannot decide the obligation; the decision's reason refs name the repaired proof that would decide (P5, P6) |
| `re-enter(undeclared)` | out_of_frame | the edge cannot close on its current basis because an upstream asset or governing relation must change, and the change needs a relation, capability or authority that no admitted basis declares; the decision names it and its owner |
| `re-enter(basis)` | invalid_basis | the edge cannot close on its current basis because an upstream asset or governing relation must change, and that basis cannot support the edge |
| `reprice` | out_of_frame | further work needs a selected outcome or bound that no admitted basis declares; the decision names it, its owner and the constitutional re-entry it requests, which is the reconfiguration pressure of out_of_frame ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or indeterminate) |
| `block(undeclared)` | out_of_frame | `evaluate_action` decides that the action just taken leaves the edge unable to proceed, because it needs a relation, capability or authority that no admitted basis declares |
| `block(basis)` | invalid_basis | `evaluate_action` decides that the action just taken leaves the edge unable to proceed on its current basis, which cannot support it |

Closure decisions and dispositions. The closure decisions of A8 and their
refined values are this member's, and they answer the edge predicate
above. The dispositions `accept`, `local_repair`, `re_enter` and `reject`
are owned by [ACTIVATION §3 Disposition](ACTIVATION.md#disposition) and
answer another predicate, "the candidate is accepted at its declared
boundary". A closure decision is not a disposition and is never recorded
as one, and no disposition is a closure decision: `repair` is not
`local_repair`, and `re-enter` is not `re_enter`. Edge closure is
evidence toward acceptance and never acceptance itself (the
selected-outcome paragraphs above). Their core values differ because their
predicates differ. `repair(proof)` is `indeterminate`, because a
defective proof leaves the edge's obligations undecided, while
`local_repair` is `falsified`, because the local defect defeats
acceptance of the candidate. `re-enter(undeclared)` is `out_of_frame`,
because the change needs a relation, capability or authority that no
admitted basis declares, while `re_enter` is `invalid_basis`. Neither
value counts toward the other's predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
In §11.5D, §16 and §19 "disposition" names a closure decision (the
selected-outcome paragraphs, A8, A11, the constitutional equation, §16
item 13 and §19 question 11) or, in "typed no-action disposition", a
selection of `evaluate_next` (A3, A4); there it never names a disposition
of ACTIVATION §3. The dispositions of §21 are the successor dispositions
of [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
(P1, P5, P6). Purpose and material relation:
a consumer that read an edge's `repair` as `local_repair`, or `re-enter`
as `re_enter`, would take an undecided edge for a defeated candidate, or a
missing declaration for an unsupporting basis; the material relation is
whether a closure decision is combined as an acceptance result.

A9 Yield is lawful iterate. `yield` is the lawful iteration boundary (P5):

```text
same edge or attempt remains lawful
progress or waiting state is admitted
resume basis is replay-visible
control returns without failure classification
```

Yield is not retry, not block, not timeout and not a local CLI loop. It is
the pressure-release state that lets long-running, bounded or partially
productive work return control without losing the current edge (P5, P0).

A10 Liveness does not close semantic truth. Liveness observes activity,
inactivity, process state and interruption. It can support yield or a
liveness interruption; it cannot by itself declare semantic failure,
semantic closure or requirement non-satisfaction (P6).

A11 Re-entry is graph law. Repair and re-entry are graph actions selected
by `evaluate_next` from admitted closure truth and published action
authority, not local retry branches over strings. `evaluate_action` may
emit `repair` or `re-enter` as a closure disposition; `evaluate_next`
selects which published graph action realises that repair or re-entry.
Disposition is conceptual; selection is invocational (P6, P5).

A12 Public query is a read-only evaluation view. A public query or gaps
view may render read-only outputs of `eval_gap`, `evaluate_action` and
`evaluate_next`: gap pressure, closure decision and next-action
projection. It must not append events, invoke workers, admit intent, run
`evaluate_action` or choose traversal by itself (P6, P3).

A13 Replayability. Every closure decision and next-action selection must
be reproducible from (P3, P6):

```text
RuntimeEventLog
+ execution basis
+ ABG event-log-backed IntentLineage
+ ProductAssetModel publication basis and its event refs
+ selected Product outcome identity and admitted bounded-basis refs
+ GapPressureRow
+ TargetObligationBinding
+ ActionCatalog
+ admitted evidence
+ EdgeFulfillmentLedger
+ EdgeClosureDecision
+ NextActionBasis
+ visible policy refs
```

If replay cannot reproduce the decision, the implementation has created
hidden state (P3).

A13a Causal chain integrity. Each governing admitted or replay-derived
carrier and projection in the loop must reference its causal predecessor
refs (P3, P4b):

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> NextActionProjection (selected_action)
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionBasis
-> NextActionProjection (next)
```

The target binding must be reachable from the exact selected Product
outcome and any admitted bounded-basis refs. The first
`NextActionProjection` in the chain carries the selected action that
admits `ConstructionIntent`, which preserves those authority refs. The
second is the post-action projection produced from `NextActionBasis` plus
fresh `eval_gap` truth. Both must be reachable from their predecessor
refs. A13 requires that the decision be reproducible from the inputs;
A13a requires that each governing carrier or projection carry the predecessor refs
that make reproduction reachable without external joins. A broken
predecessor chain is non-replayable at the carrier level and therefore
fails A13 (P3, P4b).

A14 Recursive published refinement. The homeostasis loop recurses over
published refinement. If a graph function refines an outer vector into
published inner vectors, each inner vector boundary obeys
`synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action` with
its own visible model, gap, binding, action, evidence, ledger, closure and
next-action projection. An intentionally opaque inner realisation is
ordinary implementation inside one bounded action: it may use local
control flow to compute the action's internal result, but it must not
publish, dispatch, retry, repair, re-enter or close graph work as a hidden
traversal controller. Once a refinement is published as graph structure,
the loop governs it recursively (P4a, P0, P6).

A15 Method ownership. ABG owns runtime truth, event replay, the graph-call
lifecycle, actor and process supervision, continuation, and re-entry
mechanics. The product owns domain asset meaning, graph-function
catalogue meaning, gap interpretation and priority policy. The
software-design profile (DESIGN_MODULE, tier 3; PROFILES §3) governs
realisation modules inside that split and must not fragment `eval_gap`,
`evaluate_next` or `evaluate_action` into module-local decision
authorities (P6).

A16 Constitutional override. For any ticket, design, code module or proof
that touches `synthesize_model`, `eval_gap`, `evaluate_next`,
`evaluate_action`, traversal, gap evaluation, action selection,
construction intent, worker invocation, evidence admission, fulfilment,
liveness, closure, re-entry, public query or live proof, the causally
applicable members of this axiom set and the constitutional equation below
are the controlling acceptance constraints for the selected Product
outcome and the affected published boundary. Unchanged accepted relations
cite their accepted basis and are not proved again. The axiom family
authorises no horizontal realisation growth, creates no Product work and
does not widen the selected outcome (P6, P2).

Ticket-local closure wording, test names, source-grep checks, compact CLI
summaries and implementation notes cannot weaken the constitutional loop.
A ticket that looks complete by its local checklist but leaves a rival
traversal-consequence path is not constitutionally complete; the lawful
result is to request lawful re-entry, keep the gap as a closure blocker,
or admit separately bounded paydown under an independently selected
Product outcome or prerequisite basis (P6, P2).

These artifacts may provide evidence, diagnostics or read-model context
only; they must not independently close an edge, select a next action, or
route retry, repair or re-entry (P6):

```text
gap dossier
postflight report
assurance report
materialization manifest
runtime liveness projection
run summary
worker prose
screen or PTY transcript
prompt package
harness target argument
source-grep test
CLI branch or compact output
public query or gaps view
service method output
```

If any of them conflicts with the admitted `EdgeFulfillmentLedger`,
`EdgeClosureDecision` or `NextActionProjection`, the ledger, decision and
projection chain wins. If that chain is absent, the edge has not
constitutionally closed and the next action has not been constitutionally
selected (P6).

The constitutional equation is (P6, P4a):

```text
let U = (selected_product_outcome_ref, optional_admitted_bounded_basis_ref)
let L = project_intent_lineage_from_event_log(source_intent_refs, prior_intent_refs)
let M0 = synthesize_model(L, prior_model, admitted_product_truth)
let G0 = eval_gap(M0, RuntimeEventLog, RuntimeProjection, Worksite)
let O = G0.observation
let B0 = bind(U, G0.pressures, ActionCatalog, target obligations)
let Q0 = initial_selection(L, M0)
let N0 = evaluate_next(Q0, G0, B0, ActionCatalog, Policy)
let I = admit_construction_intent(L, B0, N0.selected_action, N0.next_action_projection)
let E = admit_evidence(invoke(I))
let A = evaluate_action(I, E, B0, Policy)
let M1 = synthesize_model(L, M0, admitted_product_truth)
let G1 = eval_gap(M1, RuntimeEventLog, RuntimeProjection, Worksite)
let B1 = bind(U, G1.pressures, ActionCatalog, target obligations)
let Q1 = next_action_basis_from(A.decision)
let N1 = evaluate_next(Q1, G1, B1, ActionCatalog, Policy)

return N1
```

where (P5):

```text
A.ledger = EdgeFulfillmentLedger
A.decision = EdgeClosureDecision
A.decision.disposition in {close, yield, retry, repair, re-enter, reprice, block}
Q0.kind = initial_selection
Q1.kind in {
  post_yield_resume,
  post_close_graph_continuation,
  post_retry,
  post_repair,
  post_reenter,
  post_reprice,
  post_block
}
Q1.kind = post_reprice and no separately admitted constitutional basis
  => N1 = typed no-action pending re-entry
```

The implementation is correct only when the next work decision is derived
from that equation, `U` stays causally reachable through the target
binding and the construction intent, and no other path can decide what
work happens next (P6, P2).

### 11.6 Product-specific semantics sit above the shared carrier

This profile gives the product shape, not the domain semantics. The same
ODD structural law can build many different domain products, and each
product defines its own asset meanings, proof lanes and query overlays.
Structural GTL law and product-specific semantic law are never confused
(P1).

### 11.7 Manual walkthrough must still be lawful

Automation must stay true for a manual walkthrough. A human operator using
only the declared authority surfaces should be able to (P0, P6):

1. identify the current asset state, the current typed asset or node;
2. identify the next lawful vector and its public graph-function carrier,
   the vector being the constitutional transition contract and the graph
   function the published constructive program that realises it (§5
   Vectors and Graph functions);
3. determine the required inputs, evaluators, output contract and carried
   environment;
4. construct or assess the next asset, a produced asset or checkpoint;
5. repeat until target-relative closure is reached.

Automation may make this faster, safer or more repeatable; it may not
invent a different process. Automation is lawful when it renders prompts,
scaffolds artifacts, selects the next traversal step, runs workers,
collects evidence and assesses closure. Automation is unlawful when it
skips undeclared nodes; fabricates authority absent from the declared
surfaces; collapses several constitutional transitions into one opaque
step without declaring the refinement; depends on implementation-carrier
knowledge the installed product should not have; or collapses the
installed builder and the product under development into one authority
surface during self-host work (P0, P6).

If the team cannot explain the manual traversal, the automation is not yet
method-safe. Automation that cannot be explained in these terms is ahead
of the method (P0, P6).

### 11.7A Conforming agentic development

This profile is the premise for conforming agentic development over the
graph-native worksite. An agentic coder produces governed work by
following the constitutional process over a minimal declared authority
packet, and admission gates the artifacts it produces. SPEC_METHOD governs
the general constitutional process and [TICKETS](TICKETS.md) governs
artifact admission; this section names the ODD specialisation and composes
that law without declaring it again (P6, P0).

Conformance has two halves: an F_P proof that the process can be followed,
and an F_D gate that admits the produced artifacts (P6).

The walkthrough is the conformance proof. §11.7 requires automation to
stay true for a manual walkthrough; its agentic form is a conformance test
of the method itself. An agentic coder executes the constitutional process
end to end on real work, using only the declared authority surfaces:
intake triage, the smallest lawful re-entry, the specification,
requirement, design and ticket chain, the constructive evaluation loop of
§11.5D, and closure proof. The agentic coder is F_P over the
constitutional process (P0, P6).

The agent works from a minimal declared authority packet, not from memory
and not from wholesale hidden context. The general method already requires
declared context for any agentic work unit: input and output contract,
required context, role, evaluator regime and provenance (SPEC_METHOD;
[ACTIVATION §1](ACTIVATION.md#1-the-step)). The ODD addition is that the
packet carries only the smallest declared authority sufficient to decide
the step, with its source refs, and that conformance is enforced by
admitting the produced artifact rather than by enlarging what the agent
must hold. Compression is prompt input and never the deciding authority
(P0, P6). What a derived surface may decide is owned by
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Acquisition and Standalone scope; this section adds only the ODD limit
that follows. A derived surface or projected frame of the general method may
orient the agent to source precedence, lawful re-entry and traceability;
it must not be used to decide product-specific behaviour, which must come
from the current product authority packet (P6, P1; provenance rc.2
authority_compressions/spec_method.compressed.md, a claim no rc.2 body
states).

The walkthrough proves at two levels. The work it produces must be lawful:
correct change class, traceable, admitted. A point where the walkthrough
cannot proceed is a method defect only when a competent agent, correctly
configured and using the declared authority, still cannot decide because
of ambiguity, a missing step, contradictory authority or an undecidable
change class in an owning surface. That defect is repriced into the owning
authority surface, as a failed manual traversal is a graph defect under
§11.7 (P6, P5).

An agent that ignored the declared authority, relied on stale memory or
reasoned badly has produced agent error, not a method defect. Admission
rejects the malformed artifact either way, so a bad agent turn neither
becomes law nor silently indicts the method (P6).

This proof is independent of any automated runtime. A live lane that
depends on external execution conditions, such as an overloaded model API
or a flaky transport, cannot prove the constitutional process sound,
because it conflates process validity with runtime availability. The
walkthrough proves the process; the runtime only executes it (P6, P5).

The validator is the conformance gate. The constitutional process is an
interface contract, and interface conformance is enforced by validating
artifacts against the contract, not by the conformer holding the contract.
This profile does not declare the artifact rules again: tickets,
change-class declarations, design-module derivations and execution
contracts are admitted under SPEC_METHOD and TICKETS, which already require
a drafted classification to be admitted or rejected against deterministic
criteria rather than taken as automatic truth. This profile requires only
that agentic development pass through that admission. The agentic coder
produces the artifact; the declared admission gates it deterministically,
fail-closed and naming the violated rule, exactly as a typed asset is
enforced by its constructor (§11.1) (P6, P3).

This keeps the F_P and F_D split at the method layer. The agentic coder is
F_P: it reasons, drafts and proposes within the declared packet. Admission
is F_D: it decides whether the produced artifact conforms. The walkthrough
establishes that the process can be followed; admission establishes that
each act of following it conforms (P6, P0).

Conformance is not approval by usage. A passed admission and a completed
walkthrough are conformance evidence, not ratification. Shared method
change still follows §9: repeated agentic execution does not make grey
work constitutional. The agentic coder conforms to the method; it does not
amend the method by acting (P6).

### 11.7B Real authority-path negative proof (STDO-UP-010)

Negative proof for an ODD or graph-native boundary exercises the supported
Product authority path. It must not manufacture the refusal state, blocked
event, gap or verdict that the system is supposed to derive (P6, P5;
provenance rc.2 #117b-real-authority-path-negative-proof-stdo-up-010).

Closure-grade negative evidence identifies the supported entry and the
governing authority; invalidates the real authority-bearing input;
exercises the supported path; proves refusal before the prohibited
effect; and establishes that no legacy, fallback, reconstruction or
parallel path succeeds. Source, packaged, installed and runtime absence
are distinct claims (P6, P3).

Where these identities apply, the supported relation is (P6, P4a):

```text
public entry
  -> admitted GTL composition owns traversal topology
  -> named GraphFunction supplies the callable work contract
  -> implementation or plugin binding realizes only its admitted seam
  -> ABG owns traversal, event, continuation, and replay truth
  -> replay-derived projection
  -> typed Product outcome or continuation
```

No CLI, SDK, service, adapter, plugin, fixture, query or projection may
become a rival traversal controller. The consumer owns the concrete test
and evidence mechanism; this section owns the property that mechanism
must prove (P6).

### 11.8 Cumulative environment law is mandatory

Composition is not modelled as "the last output feeds the next input".
The ODD law is a cumulative typed environment (P4a, P4b).

Each retained `GraphFunction` should declare `environment.requires`,
`environment.provides` and `environment.carries`. A later function may
require any typed binding available in the cumulative carried
environment, not only the immediately previous output (P4a, P4b).

A product that publishes graph functions without this cumulative
environment law has a line that is graph-shaped but structurally wrong
(P4a, P6).

### 11.9 Global convergence must be stable under zoom

Local green arcs are not enough. When an outer public carrier is refined
into inner executable structure, the refined inner chain must close
lawfully; the enclosing coarse contract must also stay true after
fold-back; and zoomed and unzoomed views must agree on whether the
enclosing carrier is open or closed (P4a, P2).

For current product closure, live current requirements that lack an
executable proof witness keep the enclosing carrier open until they are
realised, explicitly deferred, or explicitly repriced out of the active
branch. For the active software line the immediate pressure is usually a
realised testcase or archived test evidence, but the governing law is
proof-lane aware: the witness must be a governed realised proof surface
appropriate to the requirement class (P2, P6).
```


### Row `ODD_METHOD.md#111-typed-assets-and-nodes-are-explicit` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#111-typed-assets-and-nodes-are-explicit` at rc.2:

```text
### 11.1 Typed Assets And Nodes Are Explicit

The product works over explicit typed assets or typed nodes.

It does not work over:

- one hidden project blob
- one giant mutable workspace object
- one undocumented service payload

Concrete assets must bind explicitly into typed domain boundaries.

Where an asset is a real produced or consumed boundary, declare its `asset_surface`.
```

Successor, `ODD.md#111-typed-assets-and-nodes-are-explicit`:

```text
### 11.1 Typed assets and nodes are explicit

The product works over explicit typed assets or typed nodes. It does not
work over one hidden project blob, one giant mutable workspace object or one
undocumented service payload. Concrete assets must bind explicitly into
typed domain boundaries. Where an asset is a real produced or consumed boundary,
its `asset_surface` is declared (P3).
```


### Row `ODD_METHOD.md#112-graph-functions-are-the-primary-constructive-carrier` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#112-graph-functions-are-the-primary-constructive-carrier` at rc.2:

```text
### 11.2 Graph Functions Are The Primary Constructive Carrier

Every operative constructive step is carried by:

- one named `GraphFunction`, or
- one lawful graph-function composition

Do not leave the real carrier inside:

- orchestration loops
- bespoke Python pipeline runners
- controller scripts
- service methods that only happen to call GTL-adjacent helpers
```

Successor, `ODD.md#112-graph-functions-are-the-primary-constructive-carrier`:

```text
### 11.2 Graph functions are the primary constructive carrier

Every operative constructive step is carried by one named `GraphFunction`
or one lawful graph-function composition. The real carrier is never left
inside orchestration loops, bespoke Python pipeline runners, controller
scripts, or service methods that only happen to call GTL-adjacent helpers
(P0, P4a).
```


### Row `ODD_METHOD.md#112a-outcome-first-realization-order` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#112a-outcome-first-realization-order` at rc.2:

```text
### 11.2A Outcome-First Realization Order

If ODD introduces an edge traversal as the unit of compute, an ODD product must
use that unit of compute to build its own operative framework behavior.

The required realization order is:

1. declare the outcome traversal over typed assets
2. publish the declarative GTL/ABG carrier structure
3. implement only the minimal imperative adapter code that remains necessary

Outcome traversal means the product declares the governed movement before
implementation:

- source asset type
- target asset type
- edge traversal or graph-function name
- closure or evaluation obligation
- lineage obligation
- ambiguity or gap obligation
- allowed `F_D`, `F_P`, and `F_H` bindings

Declarative carrier structure means:

- GTL graph functions
- typed nodes
- vectors
- operator bindings
- evaluator bindings
- carrier schemas
- policy declarations
- projection declarations
- lineage ledger declarations

Imperative adapter code is lawful only where it transports or persists facts:

- file or network IO
- CLI or API transport
- event persistence
- runtime invocation
- projection rendering
- tool execution that has already been admitted by a declared traversal

Imperative code must not own domain meaning, semantic target movement, step
selection, closure semantics, lineage truth, or constructive workflow truth.

If framework behavior is implemented imperatively first and only later
described with GTL vocabulary, the product is ODD-shaped but not yet ODD-built.
```

Successor, `ODD.md#112a-outcome-first-realisation-order`:

```text
### 11.2A Outcome-first realisation order

Because this profile makes an edge traversal the unit of compute, an ODD
product must use that unit of compute to build its own operative framework
behaviour. The required order is: declare the outcome
traversal over typed assets; publish the declarative GTL/ABG carrier
structure; implement only the minimal imperative adapter code that remains
necessary (P0, P6).

An outcome traversal declares the governed movement before
implementation: source asset type; target asset type; edge traversal or
graph-function name; closure or evaluation obligation; lineage obligation;
ambiguity or gap obligation; allowed `F_D`, `F_P` and `F_H` bindings. The
declarative carrier structure is GTL graph functions, typed nodes,
vectors, operator bindings, evaluator bindings, carrier schemas, policy
declarations, projection declarations and lineage ledger declarations
(P0, P3).

Imperative adapter code is lawful only where it transports or persists
facts: file or network IO; CLI or API transport; event persistence;
runtime invocation; projection rendering; tool execution already admitted
by a declared traversal. Imperative code must not own domain meaning,
semantic target movement, step selection, closure semantics, lineage truth
or constructive workflow truth. Framework behaviour implemented
imperatively first and only later described in GTL vocabulary is
ODD-shaped but not yet ODD-built (P6, P0).
```


### Row `ODD_METHOD.md#113-the-function-catalog-is-published` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#113-the-function-catalog-is-published` at rc.2:

```text
### 11.3 The Function Catalog Is Published

The live line must publish a machine-readable function catalog.

At minimum, each retained function should expose:

- name
- inputs
- outputs
- intent
- public or helper role

If the callable surface exists only in prose or prompt memory, the product is under-built.
```

Successor, `ODD.md#113-the-function-catalogue-is-published`:

```text
### 11.3 The function catalogue is published

The live line must publish a machine-readable function catalogue. At
minimum each retained function should expose its name, inputs, outputs,
intent, and public or helper role. A callable surface that exists only in
prose or in prompt memory leaves the product under-built (P6, P3).
```


### Row `ODD_METHOD.md#114-the-gtl-module-is-the-operative-publication-surface` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#114-the-gtl-module-is-the-operative-publication-surface` at rc.2:

```text
### 11.4 The GTL Module Is The Operative Publication Surface

The product must publish:

- the public graph-function carriers
- the graph or graphs those carriers traverse
- typed node and vector surfaces
- semantic jobs or equivalent outer callable contracts bound to the public carrier

Do not bind callers directly to hidden inner vectors.

Where a public carrier refines into inner executable structure, publish the live traversal boundaries explicitly through lawful GTL boundary surfaces such as `RefinementBoundary` or `CandidateFamily`.

The outer public carrier remains the callable contract.
```

Successor, `ODD.md#114-the-gtl-module-is-the-operative-publication-surface`:

```text
### 11.4 The GTL module is the operative publication surface

The product must publish the public graph-function carriers, the graph or
graphs those carriers traverse, typed node and vector surfaces, and the
semantic jobs or equivalent outer callable contracts bound to the public
carrier. Callers are never bound directly to hidden inner vectors (P4a,
P3).

Where a public carrier refines into inner executable structure, the live
traversal boundaries are published explicitly through lawful GTL boundary
surfaces such as `RefinementBoundary` or `CandidateFamily`. The outer
public carrier remains the callable contract (P4a, P3).
```


### Row `ODD_METHOD.md#115-current-state-is-a-projection-over-constructive-history` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#115-current-state-is-a-projection-over-constructive-history` at rc.2:

```text
### 11.5 Current State Is A Projection Over Constructive History

Visible current state is a projection.

It is not a replacement for runtime truth.

The ODD query lane may expose:

- asset views
- function catalog views
- checkpoint overlays
- provenance overlays
- domain-specific explainability overlays

It must not redefine ABG runtime facts.
```

Successor, `ODD.md#115-current-state-is-a-projection-over-constructive-history`:

```text
### 11.5 Current state is a projection over constructive history

Visible current state is a projection and does not replace runtime truth.
The ODD query lane may expose asset views, function catalogue views,
checkpoint overlays, provenance overlays and domain-specific
explainability overlays; it must not redefine ABG runtime facts (P3, P6).
```


### Row `ODD_METHOD.md#115a-abg-owns-continuation-and-re-entry` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#115a-abg-owns-continuation-and-re-entry` at rc.2:

```text
### 11.5A ABG Owns Continuation And Re-Entry

An ODD application over GTL/ABG is a cooperative subsystem, not a replacement
runtime.

ABG owns:

- continuation authority
- re-entry after publish boundaries
- graph-call lifecycle
- step selection over the declared graph

The product may:

- publish typed assets and evidence
- execute one admitted bounded constructive step
- publish downstream read models or domain overlays
- return control to ABG

The product must not:

- own a hidden continuation loop
- carry multi-step controller memory across publish boundaries
- infer later steps locally instead of re-entering through ABG
- treat public `next` and explicit graph-function continuation as rival
  authorities inside one controller
- build product-local orchestration that effectively replaces ABG

If an application attempts to replace ABG continuation with tenant-local
control flow, it is no longer behaving as an ODD application over GTL/ABG. It
has drifted into a different architecture that only happens to publish some
ODD-shaped artifacts.
```

Successor, `ODD.md#115a-abg-owns-continuation-and-re-entry`:

```text
### 11.5A ABG owns continuation and re-entry

An ODD application over GTL/ABG is a cooperative subsystem, not a
replacement runtime. ABG owns continuation authority, re-entry after
publish boundaries, the graph-call lifecycle, and step selection over the
declared graph (P6, P0).

The product may publish typed assets and evidence, execute one admitted
bounded constructive step, publish downstream read models or domain
overlays, and return control to ABG. The product must not own a hidden
continuation loop; carry multi-step controller memory across publish
boundaries; infer later steps locally instead of re-entering through ABG;
treat public `next` and explicit graph-function continuation as rival
authorities inside one controller; or build product-local orchestration
that in effect replaces ABG (P6).

An application that replaces ABG continuation with tenant-local control
flow no longer behaves as an ODD application over GTL/ABG. It has drifted
into a different architecture that only happens to publish some
ODD-shaped artifacts (P6).
```


### Row `ODD_METHOD.md#115b-execution-authority-audit` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#115b-execution-authority-audit` at rc.2:

```text
### 11.5B Execution Authority Audit

Any ODD product over GTL/ABG that changes runtime, `start`/`iterate`, worker
transport, actor invocation, process supervision, plugin dispatch, event
projection, closure, assurance, retry, or continuation semantics must include
an execution-authority audit before activation and closure.

The audit must prove that there is exactly one execution authority for the
affected traversal. For a consumer using the GTL and ABG roles, that authority
is the one consumer-bound realization of the ABG role. This remains true when
the realization under change itself implements that role. A different
realization is lawful only under an explicitly ratified, non-overlapping
runtime scope.

The audit must inventory at least these surfaces:

| Surface | Lawful owner | Product or plugin role | Forbidden local implementation |
| --- | --- | --- | --- |
| Traversal selection and vector advance | ABG | Declare graph functions, vectors, assets, and domain policy inputs | Product-local runner deciding the next traversal step |
| Actor invocation and process supervision | ABG | Provide actor bindings, prompts, payload adapters, and evidence adapters | Product-local worker `spawn`, `spawnSync`, `exec`, timeout, kill, or stdout/stderr supervision outside the ABG actor seam |
| Retry, correction, continuation, and re-entry | ABG | Publish bounded-step outputs and return control | Product-local retry loops, carry-over controller memory, or hidden `next` authority |
| Runtime event emission, append, replay, and projection | ABG | Map domain evidence into admitted event payloads | Direct event append, side ledger mutation, or projection reconstruction that bypasses ABG runtime truth |
| Closure fold and assurance gate | ABG, with product policy and gain inputs | Provide domain interpretation, evaluators, gap reasons, and policy weights | Worker self-report or product postflight directly closing the runtime unit |

Where these surfaces admit a consequential entity transformation, ABG's
admission authority is the graph-native specialization of `STDO-UP-016`. ABG's
broader execution, supervision, retry, and projection authority continues to
derive from existing ODD law, and is not thereby reclassified as admission
authority. `F_P` and `F_H` are the ODD projections of the candidate-producer
and human-adjudication roles that `STDO-UP-016` declares generically.

The audit is not satisfied by reviewing produced artifacts alone. It must
include a code, call-graph, or static-surface review appropriate to the
language and tenant, and it must name the evidence used to rule out hidden
execution authority.

Non-closure conditions include:

- a downstream product contains its own `start` or `iterate` loop for an ABG
  traversal
- product or plugin code supervises worker processes outside the ABG actor seam
- product or plugin code constructs retry, continuation, or re-entry state
  outside ABG
- product or plugin code appends runtime events or mutates runtime ledgers
  without ABG admission
- plugin output carries next-vector, closure, actor-invocation, process, or
  runtime-event authority instead of evidence or policy input
- two controllers can each claim authority for one traversal

If any of those conditions are present, the product may be useful, but it is
not currently ODD-correct over GTL/ABG.
```

Successor, `ODD.md#115b-execution-authority-audit`:

```text
### 11.5B Execution authority audit

An ODD product over GTL/ABG that changes runtime, `start` or `iterate`,
worker transport, actor invocation, process supervision, plugin dispatch,
event projection, closure, assurance, retry or continuation semantics
must include an execution-authority audit before activation and closure
(P6).

The audit must prove that exactly one execution authority exists for the
affected traversal. For a consumer using the GTL and ABG roles, that
authority is the one consumer-bound realisation of the ABG role, including
when the realisation under change itself implements that role. A
different realisation is lawful only under an explicitly ratified,
non-overlapping runtime scope (P6, P3).

The audit must inventory at least these surfaces (P6):

| Surface | Lawful owner | Product or plugin role | Forbidden local implementation |
| --- | --- | --- | --- |
| Traversal selection and vector advance | ABG | Declare graph functions, vectors, assets, and domain policy inputs | Product-local runner deciding the next traversal step |
| Actor invocation and process supervision | ABG | Provide actor bindings, prompts, payload adapters, and evidence adapters | Product-local worker `spawn`, `spawnSync`, `exec`, timeout, kill, or stdout/stderr supervision outside the ABG actor seam |
| Retry, correction, continuation, and re-entry | ABG | Publish bounded-step outputs and return control | Product-local retry loops, carry-over controller memory, or hidden `next` authority |
| Runtime event emission, append, replay, and projection | ABG | Map domain evidence into admitted event payloads | Direct event append, side ledger mutation, or projection reconstruction that bypasses ABG runtime truth |
| Closure fold and assurance gate | ABG, with product policy and gain inputs | Provide domain interpretation, evaluators, gap reasons, and policy weights | Worker self-report or product postflight directly closing the runtime unit |

Where these surfaces admit a consequential entity transformation, ABG's
admission authority is the graph-native specialisation of transformation
admission completeness, whose admission semantics
[ACTIVATION §4](ACTIVATION.md#complete-enclosing-relation-admission) owns;
the software-design profile restates the predecessor rule in
[DESIGN_MODULE, Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016)
(provenance rc.2
[STDO-UP-016](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)).
ABG's broader execution, supervision, retry and projection authority
continues to derive from this profile and is not thereby reclassified as
admission authority. `F_P` and `F_H` are the ODD projections of the
candidate-producer and human-adjudication roles, which this profile binds
to the source concepts of SPEC_METHOD §5 in
[§5 Probabilistic compute](#probabilistic-compute) (P6, P1).

Reviewing produced artifacts alone does not satisfy the audit. It must
include a code, call-graph or static-surface review appropriate to the
language and tenant, and it must name the evidence used to rule out hidden
execution authority (P6).

Any of these conditions prevents closure (P6):

- a downstream product contains its own `start` or `iterate` loop for an
  ABG traversal;
- product or plugin code supervises worker processes outside the ABG
  actor seam;
- product or plugin code constructs retry, continuation or re-entry state
  outside ABG;
- product or plugin code appends runtime events or mutates runtime ledgers
  without ABG admission;
- plugin output carries next-vector, closure, actor-invocation, process
  or runtime-event authority instead of evidence or policy input;
- two controllers can each claim authority for one traversal.

When any is present, the product may be useful but is not currently
ODD-correct over GTL/ABG (P6).
```
