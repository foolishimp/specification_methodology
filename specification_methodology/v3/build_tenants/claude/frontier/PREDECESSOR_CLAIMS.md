# Predecessor Claims, Claude tenant copy

Source: `specification/requirements/PREDECESSOR_CLAIMS.md` at commit `b83ed1c`, SHA-256 `61449a6b0447e7d967403373cebe44fea661fbc30e9602ebc91c0ec24332b9d7`, copied byte for byte below this paragraph with only the heading changed. This copy's Disposition and Successor locus columns are filled by Writer activations member by member, each within its declared cone, and are reviewed before the Executive consolidates them into the common file through the common pen. Every row starts `unresolved`.

Status: PROPOSED on branch `common/c3-contract`; mechanical enumeration from the installed manifest, no disposition recorded. Awaits Jim's review before merge.

STDO 3 is the successor of the installed `stdo://releases/v2.5.1-rc.2/` (manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`). Under [Successor Baseline Conservation (STDO-UP-015)](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015) every predecessor claim capable of affecting the successor receives exactly one semantic disposition, and an unresolved disposition blocks qualification of the affected claim. This file is the frontier an Executive holds: the enumeration of what must be disposed, at a selected granularity, with each row's current state. Coverage: all 52 standards members of the manifest (member set SHA-256 `2f54671dfde54a6ad87347ac7190028af5e21021988247edf8068ab6248ef7e8`): the 16 Markdown bodies at heading-section granularity and the 36 compression, schema and template members at member granularity; plus the 19 auxiliary members the manifest publishes (licence, plugin, release note) at member granularity.

## Granularity and rules

- One row per heading section of each rc.2 standard, at the member's digest below. A section's row covers the text under that heading up to the next heading of any level; a parent's row does not cover its children. Finer claims inside a section are disposed with it unless a tenant splits the row, which is recorded as a child row.
- Identifiers (`UP-nnn`, `AC-nnn`, `RF-nnn`, `OP-nnn`, `STDO-SURFACE-nnn`) are listed where the heading carries them. A row without an identifier is still a claim.
- Disposition takes exactly one of UP-015's four values: `conserved` (the successor retains the claim; under the Product's [standalone successor requirement](README.md#standalone-successor-requirement), restated in the successor's own text), `superseded` (an accepted successor relation replaces it, named), `intentionally removed` (Jim as Product authority removes it, with the reason), `not applicable` (no successor effect, with a bounded reason). `unresolved` is the only other state and it blocks qualification.
- A route to the predecessor is not a disposition. Conservation is semantic (UP-015) and is evidenced by an author-independent source comparison, never by naming similarity or by the absence of a patch.
- Successor locus names where the disposition lands in a tenant's realisation (document and section). Each tenant keeps its own copy of the disposition and locus columns; this common file records the Executive's consolidated state after acceptance.
- The 36 non-body standards members and the auxiliary members are listed last, one row each at the manifest digest. A compression carries the claims of the body it compresses and is disposed with reference to that body's rows; a schema, template or plugin member carries its own claims. Their disposition may remain `unresolved` during construction and must be resolved before any RC cut.

## Members

| Member | Bytes | Sections | SHA-256 |
|---|---|---|---|
| `AXIOMATIC_CALCULUS.md` | 37,849 | 39 | `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d` |
| `DESIGN_MODULE_METHOD.md` | 121,432 | 62 | `5cb69556bba1171ec347cac96811c50071f0648a367103aa215070239b93785e` |
| `GLOSSARY_GUIDE.md` | 18,945 | 14 | `da6d81df61d61e685bcf1ef69187839a52d72af7f1d61af050244f856efe0cd0` |
| `IDENTITY_METHOD.md` | 11,350 | 23 | `e65b875464cc93a3f9186d915ad88603755de34bac6f27072562ed34c13f64cd` |
| `ODD_METHOD.md` | 71,327 | 48 | `b33dd5b868e66e27c583b3237e93421ab12d502b38368bf075973c1bf7faef2d` |
| `POSTING_GUIDE.md` | 4,959 | 9 | `63ee8b6fde9803e38970e85fb2c4e0aa398632720b6a5f1cff8fb1291398c59a` |
| `README.md` | 2,330 | 1 | `7eb1ab99072963acf373af422cf698f1623dbd0628e7aff7a3ec5af4e72f8659` |
| `REFERENCE_FRAME_METHOD.md` | 55,118 | 81 | `6e9148d7c8eff847abf172315b0e282e4477f3d40866b28f7fef21c41cb067e7` |
| `RELEASE_METHOD.md` | 26,086 | 22 | `582bc15451855670495e559db3ae6a89ba37edaa3656f33499d02220cbdb141c` |
| `SPEC_METHOD.md` | 157,952 | 79 | `7f12d32ef4e5720d5d59ee5ace50de6c1a12cc56afa53dd67a8ee4c54f8fb8a4` |
| `STDO_REFERENCE_FRAME_BASELINE.md` | 133,684 | 69 | `29ac1367a77bf686e621a3e1b88bb39a0ba8e6c44b40e2b29904a7eb5606571d` |
| `TICKET_METHOD.md` | 60,674 | 49 | `f031ce7fb3b5b366ffaee5996ae76e861697ad86897cc04c06b67da249fe0eca` |
| `TRAVERSAL_OCCURRENCE_PROFILE.md` | 65,332 | 25 | `618bb7c8f9f1eab8283cf595ac9da3533f0f9cf80a684c6f42e09142da6590c1` |
| `UX_METHOD.md` | 27,217 | 24 | `a7cca45d6064d7fc864edd86e3913c9462cfe2a52ae3d1519c6a031713dccae7` |
| `WORLD_MODEL_METHOD.md` | 51,197 | 81 | `123ddcd05130aa95508c9fcfa194bf083caae3657baedaba0ce9214009453762` |
| `WRITING_GUIDE.md` | 3,092 | 9 | `29e50edc00997b76c20fad74724991b8cfffbe692ee6cabab208ad7a0c1b63fd` |

Total: 635 section rows across 16 standards, 67 carrying identifiers.

## README.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/README.md`

A member with no sub-headings is one row for its whole text.

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Standards Library (whole member) | `#standards-library` |  | 2,330 | unresolved | |

## AXIOMATIC_CALCULUS.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Position | `#position` |  | 1,866 | unresolved | |
| Derivation Provenance | `#derivation-provenance` |  | 3,724 | unresolved | |
| Scope | `#scope` |  | 659 | unresolved | |
| Core Signature | `#core-signature` |  | 4,767 | unresolved | |
| Typed Records | `#typed-records` |  | 560 | unresolved | |
| &nbsp;&nbsp;Semantic Object | `#semantic-object` |  | 333 | unresolved | |
| &nbsp;&nbsp;Typed Relation | `#typed-relation` |  | 396 | unresolved | |
| &nbsp;&nbsp;Constraint | `#constraint` |  | 537 | unresolved | |
| &nbsp;&nbsp;Latitude | `#latitude` |  | 337 | unresolved | |
| &nbsp;&nbsp;Residual | `#residual` |  | 611 | unresolved | |
| Fundamental Laws | `#fundamental-laws` |  | 20 | unresolved | |
| &nbsp;&nbsp;AC-001 Closed Signature | `#ac-001-closed-signature` | AC-001 | 390 | unresolved | |
| &nbsp;&nbsp;AC-002 Scoped Identity | `#ac-002-scoped-identity` | AC-002 | 218 | unresolved | |
| &nbsp;&nbsp;AC-003 Reference Closure | `#ac-003-reference-closure` | AC-003 | 426 | unresolved | |
| &nbsp;&nbsp;AC-004 Relation Typing | `#ac-004-relation-typing` | AC-004 | 227 | unresolved | |
| &nbsp;&nbsp;AC-005 Authority Conservation | `#ac-005-authority-conservation` | AC-005 | 323 | unresolved | |
| &nbsp;&nbsp;AC-006 Basis Coherence | `#ac-006-basis-coherence` | AC-006 | 246 | unresolved | |
| &nbsp;&nbsp;AC-007 Constraint And Refusal | `#ac-007-constraint-and-refusal` | AC-007 | 274 | unresolved | |
| &nbsp;&nbsp;AC-008 Explicit Latitude | `#ac-008-explicit-latitude` | AC-008 | 221 | unresolved | |
| &nbsp;&nbsp;AC-009 Residual Conservation | `#ac-009-residual-conservation` | AC-009 | 258 | unresolved | |
| &nbsp;&nbsp;AC-010 Material Closure | `#ac-010-material-closure` | AC-010 | 558 | unresolved | |
| &nbsp;&nbsp;AC-011 Projection | `#ac-011-projection` | AC-011 | 435 | unresolved | |
| &nbsp;&nbsp;AC-012 Overlay | `#ac-012-overlay` | AC-012 | 355 | unresolved | |
| &nbsp;&nbsp;AC-013 Transformation | `#ac-013-transformation` | AC-013 | 6,410 | unresolved | |
| &nbsp;&nbsp;AC-014 Judgment Separation | `#ac-014-judgment-separation` | AC-014 | 448 | unresolved | |
| Traversals And Functor Kinds | `#traversals-and-functor-kinds` |  | 1,875 | unresolved | |
| &nbsp;&nbsp;AC-015 Functor Classification | `#ac-015-functor-classification` | AC-015 | 202 | unresolved | |
| &nbsp;&nbsp;AC-016 Typed Composition | `#ac-016-typed-composition` | AC-016 | 556 | unresolved | |
| Interpretation And Models | `#interpretation-and-models` |  | 1,235 | unresolved | |
| &nbsp;&nbsp;AC-017 Interpretation Fidelity | `#ac-017-interpretation-fidelity` | AC-017 | 377 | unresolved | |
| &nbsp;&nbsp;AC-018 Structural And Semantic Separation | `#ac-018-structural-and-semantic-separation` | AC-018 | 324 | unresolved | |
| &nbsp;&nbsp;AC-019 Valid Model | `#ac-019-valid-model` | AC-019 | 800 | unresolved | |
| Subject And Carrier Boundaries | `#subject-and-carrier-boundaries` |  | 895 | unresolved | |
| &nbsp;&nbsp;AC-020 Layer And Release Separation | `#ac-020-layer-and-release-separation` | AC-020 | 733 | unresolved | |
| Exact Calculus Identity | `#exact-calculus-identity` |  | 3,655 | unresolved | |
| Application Boundary | `#application-boundary` |  | 392 | unresolved | |
| External Imports And Specializations | `#external-imports-and-specializations` |  | 385 | unresolved | |
| Exclusions | `#exclusions` |  | 471 | unresolved | |
| Conformance Obligations | `#conformance-obligations` |  | 1,251 | unresolved | |

## DESIGN_MODULE_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| 1. Purpose | `#1-purpose` |  | 2,536 | unresolved | |
| 2. Position | `#2-position` |  | 653 | unresolved | |
| 3. Core Rule | `#3-core-rule` |  | 343 | unresolved | |
| 3A. ODD Alignment And Escalation Rule | `#3a-odd-alignment-and-escalation-rule` |  | 1,404 | unresolved | |
| 3B. Boundary Closure Evaluators | `#3b-boundary-closure-evaluators` |  | 356 | unresolved | |
| &nbsp;&nbsp;1. Authority Seam Closure | `#1-authority-seam-closure` |  | 1,200 | unresolved | |
| &nbsp;&nbsp;2. Essential Carrier Consolidation | `#2-essential-carrier-consolidation` |  | 613 | unresolved | |
| &nbsp;&nbsp;3. Enforcement After Proof | `#3-enforcement-after-proof` |  | 743 | unresolved | |
| 3B. Ingress Collapse Rule | `#3b-ingress-collapse-rule` |  | 758 | unresolved | |
| 4. Functional Bias Without Language Mandate | `#4-functional-bias-without-language-mandate` |  | 934 | unresolved | |
| 4A. Python Typing Rule | `#4a-python-typing-rule` |  | 1,778 | unresolved | |
| 4B. Ontology-First Design Rule | `#4b-ontology-first-design-rule` |  | 2,538 | unresolved | |
| &nbsp;&nbsp;Proportional Design Sequencing | `#proportional-design-sequencing` |  | 3,794 | unresolved | |
| &nbsp;&nbsp;Decision-Complete Symbolic Design | `#decision-complete-symbolic-design` |  | 1,870 | unresolved | |
| &nbsp;&nbsp;Bounded Frame Conservation (`STDO-UP-017`) | `#bounded-frame-conservation-stdo-up-017` | UP-017 | 2,941 | unresolved | |
| &nbsp;&nbsp;Native Constructability Before Design Acceptance (`STDO-UP-002`) | `#native-constructability-before-design-acceptance-stdo-up-002` | UP-002 | 660 | unresolved | |
| &nbsp;&nbsp;Capability And Foundation Selection (`STDO-UP-023`) | `#capability-and-foundation-selection-stdo-up-023` | UP-023 | 6,741 | unresolved | |
| &nbsp;&nbsp;Entity And Lifecycle Completeness | `#entity-and-lifecycle-completeness` |  | 1,664 | unresolved | |
| &nbsp;&nbsp;Authority Model | `#authority-model` |  | 1,659 | unresolved | |
| &nbsp;&nbsp;Transformation Admission Completeness (`STDO-UP-016`) | `#transformation-admission-completeness-stdo-up-016` | UP-016 | 4,144 | unresolved | |
| &nbsp;&nbsp;Atomic Functions And Higher-Order Composition | `#atomic-functions-and-higher-order-composition` |  | 2,012 | unresolved | |
| &nbsp;&nbsp;Prime Semantic Atoms And Universal Domain | `#prime-semantic-atoms-and-universal-domain` |  | 1,526 | unresolved | |
| &nbsp;&nbsp;Whole-Family Prime Contraction | `#whole-family-prime-contraction` |  | 1,380 | unresolved | |
| &nbsp;&nbsp;Recursive Prime And Root Conservation (`STDO-UP-003`) | `#recursive-prime-and-root-conservation-stdo-up-003` | UP-003 | 1,159 | unresolved | |
| &nbsp;&nbsp;Ontology Projection Law | `#ontology-projection-law` |  | 1,420 | unresolved | |
| 5. Prime Law | `#5-prime-law` |  | 2,910 | unresolved | |
| &nbsp;&nbsp;Boundary And Governance Cost (`STDO-UP-005`) | `#boundary-and-governance-cost-stdo-up-005` | UP-005 | 652 | unresolved | |
| 5A. Irreducible Architectural Carrier Set Rule | `#5a-irreducible-architectural-carrier-set-rule` |  | 2,466 | unresolved | |
| &nbsp;&nbsp;IACS Revision Obligation | `#iacs-revision-obligation` |  | 951 | unresolved | |
| 5B. Promotion Test | `#5b-promotion-test` |  | 1,299 | unresolved | |
| 5C. Boundary Inflation Prohibition | `#5c-boundary-inflation-prohibition` |  | 1,087 | unresolved | |
| 5D. Reference-Derived Module Design Rule | `#5d-reference-derived-module-design-rule` |  | 1,623 | unresolved | |
| 5E. Ontology And Three-View Behavioral Design Gate | `#5e-ontology-and-three-view-behavioral-design-gate` |  | 1,517 | unresolved | |
| &nbsp;&nbsp;Ontology evidence | `#ontology-evidence` |  | 865 | unresolved | |
| &nbsp;&nbsp;Invariant Reconstruction Sufficiency (`STDO-UP-018`) | `#invariant-reconstruction-sufficiency-stdo-up-018` | UP-018 | 3,117 | unresolved | |
| &nbsp;&nbsp;Domain model | `#domain-model` |  | 1,261 | unresolved | |
| &nbsp;&nbsp;Sequence model | `#sequence-model` |  | 935 | unresolved | |
| &nbsp;&nbsp;State model | `#state-model` |  | 560 | unresolved | |
| &nbsp;&nbsp;Cross-view axiom evaluation | `#cross-view-axiom-evaluation` |  | 1,777 | unresolved | |
| &nbsp;&nbsp;Gate and retrospective work | `#gate-and-retrospective-work` |  | 2,373 | unresolved | |
| &nbsp;&nbsp;Computational Realization Projection (`STDO-UP-019`) | `#computational-realization-projection-stdo-up-019` | UP-019 | 5,091 | unresolved | |
| 5F. Theoretical Framing For Boundary Law | `#5f-theoretical-framing-for-boundary-law` |  | 1,897 | unresolved | |
| 6. Design Module Taxonomy | `#6-design-module-taxonomy` |  | 1,757 | unresolved | |
| 6A. Design To Module To (Implementation, Unit Tests) Evidence Route | `#6a-design-to-module-to-implementation-unit-tests-evidence-route` |  | 3,379 | unresolved | |
| 6B. Module-Derived Unit Test Rule | `#6b-module-derived-unit-test-rule` |  | 1,759 | unresolved | |
| 6C. Module Lifecycle Confirmation Rule | `#6c-module-lifecycle-confirmation-rule` |  | 2,201 | unresolved | |
| 7. Immutable Carrier Rule | `#7-immutable-carrier-rule` |  | 585 | unresolved | |
| 8. Totality Rule | `#8-totality-rule` |  | 659 | unresolved | |
| 9. Effect-Edge Rule | `#9-effect-edge-rule` |  | 660 | unresolved | |
| 10. No Semantic Center Rule | `#10-no-semantic-center-rule` |  | 705 | unresolved | |
| 11. Coupling Rule | `#11-coupling-rule` |  | 643 | unresolved | |
| 11A. Governance/Strategy Separation Rule | `#11a-governancestrategy-separation-rule` |  | 1,320 | unresolved | |
| 11B. Opportunistic Optimization Rule | `#11b-opportunistic-optimization-rule` |  | 2,411 | unresolved | |
| 11C. Recurrence Extraction Rule | `#11c-recurrence-extraction-rule` |  | 2,564 | unresolved | |
| 11D. Post-Ticket Design Review Rule | `#11d-post-ticket-design-review-rule` |  | 3,775 | unresolved | |
| 12. Interface Bleed Prohibition | `#12-interface-bleed-prohibition` |  | 669 | unresolved | |
| 13. Proxy Interface Prohibition | `#13-proxy-interface-prohibition` |  | 640 | unresolved | |
| 14. Design Review Questions | `#14-design-review-questions` |  | 8,641 | unresolved | |
| 14A. Functional Realization Review Checklist | `#14a-functional-realization-review-checklist` |  | 8,895 | unresolved | |
| 15. Adoption Guidance | `#15-adoption-guidance` |  | 2,160 | unresolved | |
| 16. Relationship To Other Method Surfaces | `#16-relationship-to-other-method-surfaces` |  | 2,090 | unresolved | |
| 17. Non-Goals | `#17-non-goals` |  | 627 | unresolved | |

## GLOSSARY_GUIDE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/GLOSSARY_GUIDE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Index Contract | `#index-contract` |  | 948 | unresolved | |
| Method Identity Index | `#method-identity-index` |  | 474 | unresolved | |
| Axiomatic-Calculus Index | `#axiomatic-calculus-index` |  | 2,556 | unresolved | |
| Traversal-Occurrence-Profile Index | `#traversal-occurrence-profile-index` |  | 1,787 | unresolved | |
| Semantic Resolution Index | `#semantic-resolution-index` |  | 1,562 | unresolved | |
| Product-Definition Routing Index | `#product-definition-routing-index` |  | 2,520 | unresolved | |
| Release-Publication Index | `#release-publication-index` |  | 1,187 | unresolved | |
| Reference-Frame Evaluation Index | `#reference-frame-evaluation-index` |  | 777 | unresolved | |
| Build-Tenancy Index | `#build-tenancy-index` |  | 957 | unresolved | |
| Recursive Product Index | `#recursive-product-index` |  | 1,435 | unresolved | |
| Product-Assurance Index | `#product-assurance-index` |  | 1,110 | unresolved | |
| Graph-Native ODD Index | `#graph-native-odd-index` |  | 1,477 | unresolved | |
| Ambiguity-Governance Index | `#ambiguity-governance-index` |  | 454 | unresolved | |
| World-Model Index | `#world-model-index` |  | 1,661 | unresolved | |

## IDENTITY_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Position | `#position` |  | 657 | unresolved | |
| Core Law | `#core-law` |  | 12 | unresolved | |
| &nbsp;&nbsp;1. Scoped Identity | `#1-scoped-identity` |  | 326 | unresolved | |
| &nbsp;&nbsp;2. Uniqueness Law | `#2-uniqueness-law` |  | 404 | unresolved | |
| &nbsp;&nbsp;3. Type Law | `#3-type-law` |  | 499 | unresolved | |
| &nbsp;&nbsp;4. Stability Law | `#4-stability-law` |  | 411 | unresolved | |
| Human-Readable vs Opaque Identity | `#human-readable-vs-opaque-identity` |  | 604 | unresolved | |
| Identity Hierarchy | `#identity-hierarchy` |  | 759 | unresolved | |
| Authority Split | `#authority-split` |  | 19 | unresolved | |
| &nbsp;&nbsp;Engine-Owned Identity | `#engine-owned-identity` |  | 435 | unresolved | |
| &nbsp;&nbsp;Domain-Owned Identity | `#domain-owned-identity` |  | 488 | unresolved | |
| Authority Identity And Conservation (`STDO-UP-004`) | `#authority-identity-and-conservation-stdo-up-004` | UP-004 | 1,363 | unresolved | |
| Default Formats And Overrides | `#default-formats-and-overrides` |  | 33 | unresolved | |
| &nbsp;&nbsp;Defaults From A Bound ABG Realization | `#defaults-from-a-bound-abg-realization` |  | 419 | unresolved | |
| &nbsp;&nbsp;Derived Domain Overrides | `#derived-domain-overrides` |  | 459 | unresolved | |
| &nbsp;&nbsp;Override Publication Surface | `#override-publication-surface` |  | 1,060 | unresolved | |
| Parsing Law | `#parsing-law` |  | 838 | unresolved | |
| Release Version Boundary | `#release-version-boundary` |  | 639 | unresolved | |
| Minimum Questions | `#minimum-questions` |  | 573 | unresolved | |
| Examples | `#examples` |  | 12 | unresolved | |
| &nbsp;&nbsp;Lawful | `#lawful` |  | 470 | unresolved | |
| &nbsp;&nbsp;Unlawful | `#unlawful` |  | 288 | unresolved | |
| Consequence For Implementations | `#consequence-for-implementations` |  | 541 | unresolved | |

## ODD_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| 1. Position | `#1-position` |  | 2,827 | unresolved | |
| 2. Method Role | `#2-method-role` |  | 906 | unresolved | |
| 3. Method Composition | `#3-method-composition` |  | 1,456 | unresolved | |
| 4. Method Folder Semantics | `#4-method-folder-semantics` |  | 1,660 | unresolved | |
| 5. Graph Model | `#5-graph-model` |  | 125 | unresolved | |
| &nbsp;&nbsp;Nodes | `#nodes` |  | 458 | unresolved | |
| &nbsp;&nbsp;Vectors | `#vectors` |  | 232 | unresolved | |
| &nbsp;&nbsp;Probabilistic Compute | `#probabilistic-compute` |  | 3,160 | unresolved | |
| &nbsp;&nbsp;Graph Functions | `#graph-functions` |  | 379 | unresolved | |
| &nbsp;&nbsp;Traversal | `#traversal` |  | 323 | unresolved | |
| 6. Product Boundary | `#6-product-boundary` |  | 1,576 | unresolved | |
| 7. Self-Host Boundary Rule | `#7-self-host-boundary-rule` |  | 756 | unresolved | |
| 8. Responsibility Layers And Local Binding | `#8-responsibility-layers-and-local-binding` |  | 1,347 | unresolved | |
| 9. Method Governance And Audit | `#9-method-governance-and-audit` |  | 1,926 | unresolved | |
| 10. What An ODD Product Is | `#10-what-an-odd-product-is` |  | 1,464 | unresolved | |
| &nbsp;&nbsp;Product Specification (software-development topology) | `#product-specification-software-development-topology` |  | 281 | unresolved | |
| &nbsp;&nbsp;Product Realization (software-development topology) | `#product-realization-software-development-topology` |  | 280 | unresolved | |
| &nbsp;&nbsp;ABG | `#abg` |  | 313 | unresolved | |
| &nbsp;&nbsp;ODD Product | `#odd-product` |  | 210 | unresolved | |
| &nbsp;&nbsp;Query And Service Layers | `#query-and-service-layers` |  | 287 | unresolved | |
| 11. Core Law | `#11-core-law` |  | 92 | unresolved | |
| &nbsp;&nbsp;11.1 Typed Assets And Nodes Are Explicit | `#111-typed-assets-and-nodes-are-explicit` |  | 384 | unresolved | |
| &nbsp;&nbsp;11.2 Graph Functions Are The Primary Constructive Carrier | `#112-graph-functions-are-the-primary-constructive-carrier` |  | 366 | unresolved | |
| &nbsp;&nbsp;11.2A Outcome-First Realization Order | `#112a-outcome-first-realization-order` |  | 1,502 | unresolved | |
| &nbsp;&nbsp;11.3 The Function Catalog Is Published | `#113-the-function-catalog-is-published` |  | 311 | unresolved | |
| &nbsp;&nbsp;11.4 The GTL Module Is The Operative Publication Surface | `#114-the-gtl-module-is-the-operative-publication-surface` |  | 602 | unresolved | |
| &nbsp;&nbsp;11.5 Current State Is A Projection Over Constructive History | `#115-current-state-is-a-projection-over-constructive-history` |  | 348 | unresolved | |
| &nbsp;&nbsp;11.5A ABG Owns Continuation And Re-Entry | `#115a-abg-owns-continuation-and-re-entry` |  | 1,057 | unresolved | |
| &nbsp;&nbsp;11.5B Execution Authority Audit | `#115b-execution-authority-audit` |  | 3,352 | unresolved | |
| &nbsp;&nbsp;11.5C Projection-Source Coherence | `#115c-projection-source-coherence` |  | 1,078 | unresolved | |
| &nbsp;&nbsp;11.5D Constructive Evaluation And Yield Loop | `#115d-constructive-evaluation-and-yield-loop` |  | 23,882 | unresolved | |
| &nbsp;&nbsp;11.6 Product-Specific Semantics Sit Above The Shared Carrier | `#116-product-specific-semantics-sit-above-the-shared-carrier` |  | 363 | unresolved | |
| &nbsp;&nbsp;11.7 Manual Walkthrough Must Still Be Lawful | `#117-manual-walkthrough-must-still-be-lawful` |  | 1,544 | unresolved | |
| &nbsp;&nbsp;11.7A Conforming Agentic Development | `#117a-conforming-agentic-development` |  | 4,380 | unresolved | |
| &nbsp;&nbsp;11.7B Real Authority-Path Negative Proof (`STDO-UP-010`) | `#117b-real-authority-path-negative-proof-stdo-up-010` | UP-010 | 1,274 | unresolved | |
| &nbsp;&nbsp;11.8 Cumulative Environment Law Is Mandatory | `#118-cumulative-environment-law-is-mandatory` |  | 559 | unresolved | |
| &nbsp;&nbsp;11.9 Global Convergence Must Be Stable Under Zoom | `#119-global-convergence-must-be-stable-under-zoom` |  | 846 | unresolved | |
| 12. Scenario Rule | `#12-scenario-rule` |  | 649 | unresolved | |
| 13. Installed-Dev Rule | `#13-installed-dev-rule` |  | 433 | unresolved | |
| 14. Dogfooding Rule | `#14-dogfooding-rule` |  | 599 | unresolved | |
| 15. Release Boundary | `#15-release-boundary` |  | 383 | unresolved | |
| 16. Failure Pattern | `#16-failure-pattern` |  | 1,849 | unresolved | |
| 17. Invocation Rule | `#17-invocation-rule` |  | 1,816 | unresolved | |
| 18. Cold-Start Reading Order | `#18-cold-start-reading-order` |  | 95 | unresolved | |
| &nbsp;&nbsp;General ODD Product | `#general-odd-product` |  | 391 | unresolved | |
| &nbsp;&nbsp;World-Model Product | `#world-model-product` |  | 789 | unresolved | |
| 19. Ramp-Up Checklist | `#19-ramp-up-checklist` |  | 1,293 | unresolved | |
| 20. Canonical Compression | `#20-canonical-compression` |  | 1,063 | unresolved | |

## POSTING_GUIDE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/POSTING_GUIDE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Boundary | `#boundary` |  | 294 | unresolved | |
| Location | `#location` |  | 557 | unresolved | |
| Carrier Identity | `#carrier-identity` |  | 416 | unresolved | |
| Categories | `#categories` |  | 411 | unresolved | |
| Structure | `#structure` |  | 415 | unresolved | |
| Discussion State And Mutability | `#discussion-state-and-mutability` |  | 1,117 | unresolved | |
| Posting Rules | `#posting-rules` |  | 450 | unresolved | |
| Ratification | `#ratification` |  | 205 | unresolved | |
| Shared Method Adoption And Propagation (`STDO-UP-012`) | `#shared-method-adoption-and-propagation-stdo-up-012` | UP-012 | 808 | unresolved | |

## REFERENCE_FRAME_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Canonical Compression | `#canonical-compression` |  | 1,658 | unresolved | |
| Position | `#position` |  | 1,445 | unresolved | |
| Core Claims | `#core-claims` |  | 1,196 | unresolved | |
| Definitions | `#definitions` |  | 15 | unresolved | |
| &nbsp;&nbsp;Evaluation | `#evaluation` |  | 535 | unresolved | |
| &nbsp;&nbsp;Workspace | `#workspace` |  | 357 | unresolved | |
| &nbsp;&nbsp;Basis | `#basis` |  | 356 | unresolved | |
| &nbsp;&nbsp;Material relation | `#material-relation` |  | 371 | unresolved | |
| &nbsp;&nbsp;Material-relation manifold | `#material-relation-manifold` |  | 418 | unresolved | |
| &nbsp;&nbsp;Coordinate | `#coordinate` |  | 401 | unresolved | |
| &nbsp;&nbsp;Topology | `#topology` |  | 530 | unresolved | |
| &nbsp;&nbsp;Evidence | `#evidence` |  | 266 | unresolved | |
| &nbsp;&nbsp;Authority | `#authority` |  | 1,207 | unresolved | |
| &nbsp;&nbsp;Disjointness And Independence | `#disjointness-and-independence` |  | 964 | unresolved | |
| &nbsp;&nbsp;Capability envelope | `#capability-envelope` |  | 439 | unresolved | |
| &nbsp;&nbsp;Reference frame | `#reference-frame` |  | 1,573 | unresolved | |
| &nbsp;&nbsp;Activated frame | `#activated-frame` |  | 251 | unresolved | |
| &nbsp;&nbsp;Frame set | `#frame-set` |  | 343 | unresolved | |
| &nbsp;&nbsp;Active frame configuration | `#active-frame-configuration` |  | 309 | unresolved | |
| &nbsp;&nbsp;Lens | `#lens` |  | 382 | unresolved | |
| &nbsp;&nbsp;Role, persona, abstraction, and component | `#role-persona-abstraction-and-component` |  | 432 | unresolved | |
| Reference Frame Laws | `#reference-frame-laws` |  | 24 | unresolved | |
| &nbsp;&nbsp;RF-001 Evaluation Relativity | `#rf-001-evaluation-relativity` | RF-001 | 171 | unresolved | |
| &nbsp;&nbsp;RF-002 Finite Attention | `#rf-002-finite-attention` | RF-002 | 298 | unresolved | |
| &nbsp;&nbsp;RF-003 Material Sufficiency | `#rf-003-material-sufficiency` | RF-003 | 402 | unresolved | |
| &nbsp;&nbsp;RF-004 Irrelevance Exclusion | `#rf-004-irrelevance-exclusion` | RF-004 | 245 | unresolved | |
| &nbsp;&nbsp;RF-005 Exact Basis And Coordinates | `#rf-005-exact-basis-and-coordinates` | RF-005 | 290 | unresolved | |
| &nbsp;&nbsp;RF-006 Authority Conservation | `#rf-006-authority-conservation` | RF-006 | 296 | unresolved | |
| &nbsp;&nbsp;RF-007 Semantic, Evidence, And Verdict Separation | `#rf-007-semantic-evidence-and-verdict-separation` | RF-007 | 436 | unresolved | |
| &nbsp;&nbsp;RF-008 Overlap Without Identity Collapse | `#rf-008-overlap-without-identity-collapse` | RF-008 | 289 | unresolved | |
| &nbsp;&nbsp;RF-009 No Assumed Hierarchy | `#rf-009-no-assumed-hierarchy` | RF-009 | 497 | unresolved | |
| &nbsp;&nbsp;RF-010 Composition On Demand | `#rf-010-composition-on-demand` | RF-010 | 429 | unresolved | |
| &nbsp;&nbsp;RF-011 Topology Mutation And Recharting | `#rf-011-topology-mutation-and-recharting` | RF-011 | 286 | unresolved | |
| &nbsp;&nbsp;RF-012 Closed Results | `#rf-012-closed-results` | RF-012 | 623 | unresolved | |
| &nbsp;&nbsp;RF-013 Reconstructable Activation | `#rf-013-reconstructable-activation` | RF-013 | 275 | unresolved | |
| &nbsp;&nbsp;RF-014 Capability Fit | `#rf-014-capability-fit` | RF-014 | 317 | unresolved | |
| &nbsp;&nbsp;RF-015 Residual Uncertainty | `#rf-015-residual-uncertainty` | RF-015 | 276 | unresolved | |
| &nbsp;&nbsp;RF-016 Implementation Neutrality | `#rf-016-implementation-neutrality` | RF-016 | 280 | unresolved | |
| &nbsp;&nbsp;RF-017 Proportional Compression | `#rf-017-proportional-compression` | RF-017 | 588 | unresolved | |
| &nbsp;&nbsp;Engagement Atom And Semantic Prime | `#engagement-atom-and-semantic-prime` |  | 784 | unresolved | |
| Human Frame-Set Declaration | `#human-frame-set-declaration` |  | 899 | unresolved | |
| &nbsp;&nbsp;Frame-Set Optimization | `#frame-set-optimization` |  | 1,283 | unresolved | |
| Method Functions | `#method-functions` |  | 945 | unresolved | |
| Engagement | `#engagement` |  | 14 | unresolved | |
| &nbsp;&nbsp;Establish The Evaluation Basis | `#establish-the-evaluation-basis` |  | 385 | unresolved | |
| &nbsp;&nbsp;Applicability And Required Results | `#applicability-and-required-results` |  | 1,293 | unresolved | |
| &nbsp;&nbsp;Select And Activate | `#select-and-activate` |  | 521 | unresolved | |
| &nbsp;&nbsp;Evaluate | `#evaluate` |  | 247 | unresolved | |
| &nbsp;&nbsp;Return A Closed Result | `#return-a-closed-result` |  | 878 | unresolved | |
| &nbsp;&nbsp;Reconfigure When Necessary | `#reconfigure-when-necessary` |  | 527 | unresolved | |
| Using Frames In Conjunction | `#using-frames-in-conjunction` |  | 93 | unresolved | |
| &nbsp;&nbsp;Independently Activated Co-Evaluation | `#independently-activated-co-evaluation` |  | 394 | unresolved | |
| &nbsp;&nbsp;Result Conjunction | `#result-conjunction` |  | 733 | unresolved | |
| &nbsp;&nbsp;Evidence Or Coordinate Translation | `#evidence-or-coordinate-translation` |  | 250 | unresolved | |
| &nbsp;&nbsp;Material Composition | `#material-composition` |  | 459 | unresolved | |
| Frame Relations | `#frame-relations` |  | 1,131 | unresolved | |
| Workspace Coverage | `#workspace-coverage` |  | 22 | unresolved | |
| &nbsp;&nbsp;Coverage Basis | `#coverage-basis` |  | 404 | unresolved | |
| &nbsp;&nbsp;Evaluation Inventory | `#evaluation-inventory` |  | 1,025 | unresolved | |
| &nbsp;&nbsp;Coverage Dimensions | `#coverage-dimensions` |  | 518 | unresolved | |
| &nbsp;&nbsp;Coverage Ledger | `#coverage-ledger` |  | 983 | unresolved | |
| &nbsp;&nbsp;Interaction Coverage | `#interaction-coverage` |  | 282 | unresolved | |
| &nbsp;&nbsp;Authority Coverage | `#authority-coverage` |  | 363 | unresolved | |
| &nbsp;&nbsp;Failure Coverage | `#failure-coverage` |  | 279 | unresolved | |
| &nbsp;&nbsp;High-Risk Separately Activated Coverage | `#high-risk-separately-activated-coverage` |  | 424 | unresolved | |
| &nbsp;&nbsp;Operational Full Coverage | `#operational-full-coverage` |  | 905 | unresolved | |
| Completeness Boundary | `#completeness-boundary` |  | 1,109 | unresolved | |
| Discovery And Revision | `#discovery-and-revision` |  | 26 | unresolved | |
| &nbsp;&nbsp;Missing-Frame Signals | `#missing-frame-signals` |  | 680 | unresolved | |
| &nbsp;&nbsp;Diagnostic Order | `#diagnostic-order` |  | 496 | unresolved | |
| &nbsp;&nbsp;Revision Actions | `#revision-actions` |  | 604 | unresolved | |
| Agentic Use | `#agentic-use` |  | 1,143 | unresolved | |
| &nbsp;&nbsp;Minimal Frame Activation Binding | `#minimal-frame-activation-binding` |  | 1,458 | unresolved | |
| &nbsp;&nbsp;Worked Binding: Product-Chain Drift Evaluation | `#worked-binding-product-chain-drift-evaluation` |  | 4,368 | unresolved | |
| Frame Qualification | `#frame-qualification` |  | 1,467 | unresolved | |
| &nbsp;&nbsp;Method Self-Qualification | `#method-self-qualification` |  | 3,430 | unresolved | |
| Anti-Patterns | `#anti-patterns` |  | 1,485 | unresolved | |
| Minimal Frame Declaration | `#minimal-frame-declaration` |  | 1,086 | unresolved | |
| Minimal Frame-Set Declaration | `#minimal-frame-set-declaration` |  | 814 | unresolved | |
| Minimal Evaluation Result | `#minimal-evaluation-result` |  | 417 | unresolved | |
| Closure | `#closure` |  | 918 | unresolved | |

## RELEASE_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Release-Publication Context | `#release-publication-context` |  | 329 | unresolved | |
| Position | `#position` |  | 1,357 | unresolved | |
| Release Identities | `#release-identities` |  | 1,168 | unresolved | |
| Project-Qualified Git Refs | `#project-qualified-git-refs` |  | 1,529 | unresolved | |
| Project-Subtree Release Identity | `#project-subtree-release-identity` |  | 1,479 | unresolved | |
| Historical Ref And Public-URI Conservation | `#historical-ref-and-public-uri-conservation` |  | 1,251 | unresolved | |
| Phases | `#phases` |  | 619 | unresolved | |
| Mutable Candidate Construction | `#mutable-candidate-construction` |  | 541 | unresolved | |
| Immutable RC Publication | `#immutable-rc-publication` |  | 1,563 | unresolved | |
| Exact-Cut Qualification | `#exact-cut-qualification` |  | 1,117 | unresolved | |
| Monotonic Version-Line Advancement | `#monotonic-version-line-advancement` |  | 1,429 | unresolved | |
| Selector And Consumer Adoption | `#selector-and-consumer-adoption` |  | 2,440 | unresolved | |
| Naming | `#naming` |  | 898 | unresolved | |
| Release-Scoped Assets | `#release-scoped-assets` |  | 804 | unresolved | |
| Coordinated Release-Matched Asset Cohorts | `#coordinated-release-matched-asset-cohorts` |  | 2,089 | unresolved | |
| &nbsp;&nbsp;Two-Commit Construction And One Publication Transaction | `#two-commit-construction-and-one-publication-transaction` |  | 2,527 | unresolved | |
| &nbsp;&nbsp;Qualification And Recovery | `#qualification-and-recovery` |  | 1,410 | unresolved | |
| Product Subject And Repository Carrier | `#product-subject-and-repository-carrier` |  | 836 | unresolved | |
| Acceptance Criteria | `#acceptance-criteria` |  | 748 | unresolved | |
| External Qualification Dependencies | `#external-qualification-dependencies` |  | 537 | unresolved | |
| Successor Baseline Conservation (`STDO-UP-015`) | `#successor-baseline-conservation-stdo-up-015` | UP-015 | 1,185 | unresolved | |
| Open Questions | `#open-questions` |  | 191 | unresolved | |

## SPEC_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Canonical Compression | `#canonical-compression` |  | 2,678 | unresolved | |
| Position | `#position` |  | 574 | unresolved | |
| STDO Method Identity | `#stdo-method-identity` |  | 836 | unresolved | |
| Probabilistic Work Boundary | `#probabilistic-work-boundary` |  | 1,499 | unresolved | |
| Recursive Product Taxonomy | `#recursive-product-taxonomy` |  | 2,924 | unresolved | |
| Manifesto | `#manifesto` |  | 1,738 | unresolved | |
| Spec-Drivenness Litmus | `#spec-drivenness-litmus` |  | 1,316 | unresolved | |
| Process Constitution | `#process-constitution` |  | 2,563 | unresolved | |
| STDO Product Definition Overlay And Layout Independence | `#stdo-product-definition-overlay-and-layout-independence` |  | 2,941 | unresolved | |
| &nbsp;&nbsp;Required Definition Relations | `#required-definition-relations` |  | 2,033 | unresolved | |
| &nbsp;&nbsp;Constitutional-Set Sufficiency | `#constitutional-set-sufficiency` |  | 1,964 | unresolved | |
| &nbsp;&nbsp;Shared Installed Release Basis And Toolchain Manager | `#shared-installed-release-basis-and-toolchain-manager` |  | 6,894 | unresolved | |
| &nbsp;&nbsp;&nbsp;&nbsp;Explicit Complete Consumer Update | `#explicit-complete-consumer-update` |  | 3,276 | unresolved | |
| &nbsp;&nbsp;Bounded-Context Semantic Resolution | `#bounded-context-semantic-resolution` |  | 4,717 | unresolved | |
| &nbsp;&nbsp;Local Constitutional Binding | `#local-constitutional-binding` |  | 1,508 | unresolved | |
| &nbsp;&nbsp;Collective Reference-Frame Basis | `#collective-reference-frame-basis` |  | 4,713 | unresolved | |
| &nbsp;&nbsp;WHAT, HOW, And Work Carriers | `#what-how-and-work-carriers` |  | 1,822 | unresolved | |
| &nbsp;&nbsp;Recursive Discovery And Explicit Composition | `#recursive-discovery-and-explicit-composition` |  | 3,173 | unresolved | |
| &nbsp;&nbsp;Semantic-Resolution Conformance Cases | `#semantic-resolution-conformance-cases` |  | 1,669 | unresolved | |
| One Constitutional Surface And Version Boundary (`STDO-SURFACE-001`) | `#one-constitutional-surface-and-version-boundary-stdo-surface-001` | STDO-SURFACE-001 | 2,041 | unresolved | |
| Constitutional Chain | `#constitutional-chain` |  | 4,052 | unresolved | |
| Sprint Execution Boundary | `#sprint-execution-boundary` |  | 2,635 | unresolved | |
| Ambiguity Governance Rule | `#ambiguity-governance-rule` |  | 3,434 | unresolved | |
| Operational Lifecycle Sufficiency Rule | `#operational-lifecycle-sufficiency-rule` |  | 1,889 | unresolved | |
| Change Management Rule | `#change-management-rule` |  | 174 | unresolved | |
| &nbsp;&nbsp;Universal Intake Triage | `#universal-intake-triage` |  | 3,368 | unresolved | |
| &nbsp;&nbsp;Computed Classification And Treatment | `#computed-classification-and-treatment` |  | 4,857 | unresolved | |
| Consistency Gate Rule | `#consistency-gate-rule` |  | 1,199 | unresolved | |
| Product Outcome Conservation (`STDO-UP-013`) | `#product-outcome-conservation-stdo-up-013` | UP-013 | 4,432 | unresolved | |
| Proportional Method And Delivery (`STDO-UP-014`) | `#proportional-method-and-delivery-stdo-up-014` | UP-014 | 4,218 | unresolved | |
| Agentic Construction Execution (`STDO-UP-020`) | `#agentic-construction-execution-stdo-up-020` | UP-020 | 696 | unresolved | |
| &nbsp;&nbsp;Sufficient Execution Intake | `#sufficient-execution-intake` |  | 937 | unresolved | |
| &nbsp;&nbsp;Bounded Causal Construction | `#bounded-causal-construction` |  | 540 | unresolved | |
| &nbsp;&nbsp;Construction, Assessment, And Delegation | `#construction-assessment-and-delegation` |  | 2,253 | unresolved | |
| &nbsp;&nbsp;Proportional Disposition | `#proportional-disposition` |  | 1,114 | unresolved | |
| &nbsp;&nbsp;Transition Evidence And Proof Cadence | `#transition-evidence-and-proof-cadence` |  | 977 | unresolved | |
| &nbsp;&nbsp;Checkpoint, Continuation, Progress, And Churn | `#checkpoint-continuation-progress-and-churn` |  | 1,744 | unresolved | |
| Complete Enclosing-Relation Admission (`STDO-UP-021`) | `#complete-enclosing-relation-admission-stdo-up-021` | UP-021 | 3,070 | unresolved | |
| &nbsp;&nbsp;Standing Structural Qualification | `#standing-structural-qualification` |  | 2,842 | unresolved | |
| Core Interface Migration Rule | `#core-interface-migration-rule` |  | 1,302 | unresolved | |
| &nbsp;&nbsp;Constitutional Migration Options | `#constitutional-migration-options` |  | 4,436 | unresolved | |
| &nbsp;&nbsp;What Counts As A Core Interface | `#what-counts-as-a-core-interface` |  | 445 | unresolved | |
| &nbsp;&nbsp;Required Migration Protocol | `#required-migration-protocol` |  | 802 | unresolved | |
| &nbsp;&nbsp;Bridge Prohibition | `#bridge-prohibition` |  | 758 | unresolved | |
| &nbsp;&nbsp;Projection Discipline | `#projection-discipline` |  | 593 | unresolved | |
| &nbsp;&nbsp;Inside-Out First Sequencing | `#inside-out-first-sequencing` |  | 1,012 | unresolved | |
| &nbsp;&nbsp;Hard-Break Discipline | `#hard-break-discipline` |  | 1,155 | unresolved | |
| &nbsp;&nbsp;Proof-Last Rule For Core Interface Changes | `#proof-last-rule-for-core-interface-changes` |  | 717 | unresolved | |
| &nbsp;&nbsp;Closure Criterion | `#closure-criterion` |  | 1,661 | unresolved | |
| Release Version Boundary | `#release-version-boundary` |  | 875 | unresolved | |
| Evidence Rules | `#evidence-rules` |  | 96 | unresolved | |
| &nbsp;&nbsp;Proof Target Identity And Adequacy (`STDO-UP-001`) | `#proof-target-identity-and-adequacy-stdo-up-001` | UP-001 | 594 | unresolved | |
| &nbsp;&nbsp;Semantic, Evidence, And Projection Separation (`STDO-UP-008`) | `#semantic-evidence-and-projection-separation-stdo-up-008` | UP-008 | 727 | unresolved | |
| &nbsp;&nbsp;Assurance-Boundary Congruence And Method Qualification (`STDO-UP-022`) | `#assurance-boundary-congruence-and-method-qualification-stdo-up-022` | UP-022 | 5,342 | unresolved | |
| Verification Layers | `#verification-layers` |  | 1,477 | unresolved | |
| Testing Strategy Taxonomy | `#testing-strategy-taxonomy` |  | 4,014 | unresolved | |
| &nbsp;&nbsp;Fixture And Proof Portability Rule | `#fixture-and-proof-portability-rule` |  | 829 | unresolved | |
| Test Authority Rule | `#test-authority-rule` |  | 470 | unresolved | |
| Scenario Bundle Rule | `#scenario-bundle-rule` |  | 969 | unresolved | |
| Installed Dev Proof Rule | `#installed-dev-proof-rule` |  | 619 | unresolved | |
| Significant Path Coverage Rule | `#significant-path-coverage-rule` |  | 659 | unresolved | |
| Requirement Categories | `#requirement-categories` |  | 1,790 | unresolved | |
| Reconstruction Litmus | `#reconstruction-litmus` |  | 2,684 | unresolved | |
| Design Rule | `#design-rule` |  | 864 | unresolved | |
| Renewal Path | `#renewal-path` |  | 1,504 | unresolved | |
| Trace Closure And Anti-Drift Rule | `#trace-closure-and-anti-drift-rule` |  | 101 | unresolved | |
| &nbsp;&nbsp;Ownership | `#ownership` |  | 206 | unresolved | |
| &nbsp;&nbsp;Downstream Closure | `#downstream-closure` |  | 709 | unresolved | |
| &nbsp;&nbsp;Drift Signals | `#drift-signals` |  | 1,397 | unresolved | |
| Live Surface Immutability | `#live-surface-immutability` |  | 1,091 | unresolved | |
| Fundamental Migration Rule | `#fundamental-migration-rule` |  | 3,159 | unresolved | |
| Transformation Wave Rule | `#transformation-wave-rule` |  | 1,485 | unresolved | |
| Legacy Classification Rule | `#legacy-classification-rule` |  | 786 | unresolved | |
| Requirement Classification Rules | `#requirement-classification-rules` |  | 769 | unresolved | |
| Specification Surface Rule | `#specification-surface-rule` |  | 2,539 | unresolved | |
| Bootstrap Rule | `#bootstrap-rule` |  | 6,674 | unresolved | |
| Method | `#method` |  | 4,613 | unresolved | |
| ADR Conventions | `#adr-conventions` |  | 910 | unresolved | |
| &nbsp;&nbsp;ADR Folder Convention | `#adr-folder-convention` |  | 1,692 | unresolved | |

## STDO_REFERENCE_FRAME_BASELINE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Canonical Compression | `#canonical-compression` |  | 3,571 | unresolved | |
| Status And Authority Boundary | `#status-and-authority-boundary` |  | 4,292 | unresolved | |
| Engagement Applicability | `#engagement-applicability` |  | 1,767 | unresolved | |
| Empirical Revision Boundary | `#empirical-revision-boundary` |  | 1,789 | unresolved | |
| Profile Terms | `#profile-terms` |  | 17 | unresolved | |
| &nbsp;&nbsp;Engagement frame | `#engagement-frame` |  | 258 | unresolved | |
| &nbsp;&nbsp;Specialist frame | `#specialist-frame` |  | 407 | unresolved | |
| &nbsp;&nbsp;Generic specialist-frame family | `#generic-specialist-frame-family` |  | 699 | unresolved | |
| &nbsp;&nbsp;Testing frame | `#testing-frame` |  | 562 | unresolved | |
| &nbsp;&nbsp;Authoritative Product path | `#authoritative-product-path` |  | 504 | unresolved | |
| &nbsp;&nbsp;Material combinatorial complexity | `#material-combinatorial-complexity` |  | 691 | unresolved | |
| &nbsp;&nbsp;Executive | `#executive` |  | 630 | unresolved | |
| Executive Attention, Evaluation, And Action | `#executive-attention-evaluation-and-action` |  | 3,774 | unresolved | |
| &nbsp;&nbsp;Event-Driven Executive Attention | `#event-driven-executive-attention` |  | 1,749 | unresolved | |
| &nbsp;&nbsp;Executive Drift Locks | `#executive-drift-locks` |  | 1,307 | unresolved | |
| &nbsp;&nbsp;Product-Chain Basis | `#product-chain-basis` |  | 1,435 | unresolved | |
| &nbsp;&nbsp;Worker | `#worker` |  | 346 | unresolved | |
| &nbsp;&nbsp;Reviewer | `#reviewer` |  | 444 | unresolved | |
| &nbsp;&nbsp;Technical triage, severity, priority, and boundary effect | `#technical-triage-severity-priority-and-boundary-effect` |  | 1,947 | unresolved | |
| &nbsp;&nbsp;Work result | `#work-result` |  | 2,021 | unresolved | |
| &nbsp;&nbsp;Exact candidate | `#exact-candidate` |  | 551 | unresolved | |
| &nbsp;&nbsp;Baseline-adoption projection | `#baseline-adoption-projection` |  | 492 | unresolved | |
| Non-Hierarchical Frame Configuration | `#non-hierarchical-frame-configuration` |  | 1,391 | unresolved | |
| Derived Executive Frame | `#derived-executive-frame` |  | 3,017 | unresolved | |
| &nbsp;&nbsp;Steel-Thread Delivery | `#steel-thread-delivery` |  | 1,827 | unresolved | |
| Derived Worker Frame | `#derived-worker-frame` |  | 2,854 | unresolved | |
| Derived Reviewer Frame | `#derived-reviewer-frame` |  | 4,236 | unresolved | |
| Derived Generic Specialist Frame Set | `#derived-generic-specialist-frame-set` |  | 10,024 | unresolved | |
| Derived Product Testing Frame Set | `#derived-product-testing-frame-set` |  | 1,395 | unresolved | |
| &nbsp;&nbsp;Derived User-Acceptance Frame | `#derived-user-acceptance-frame` |  | 3,431 | unresolved | |
| &nbsp;&nbsp;Derived End-To-End Frame | `#derived-end-to-end-frame` |  | 2,767 | unresolved | |
| &nbsp;&nbsp;Derived Integration Frame | `#derived-integration-frame` |  | 2,522 | unresolved | |
| &nbsp;&nbsp;Derived Unit-Test Frame | `#derived-unit-test-frame` |  | 4,046 | unresolved | |
| &nbsp;&nbsp;Combinatorial Coverage And Testing-Value Index | `#combinatorial-coverage-and-testing-value-index` |  | 2,916 | unresolved | |
| &nbsp;&nbsp;Legitimate-Path And Technical-Debt Erasure | `#legitimate-path-and-technical-debt-erasure` |  | 2,528 | unresolved | |
| &nbsp;&nbsp;Testing Evidence Composition | `#testing-evidence-composition` |  | 1,186 | unresolved | |
| &nbsp;&nbsp;Assurance Subject Acquisition And Evaluation | `#assurance-subject-acquisition-and-evaluation` |  | 1,609 | unresolved | |
| &nbsp;&nbsp;Counterexample Localization | `#counterexample-localization` |  | 1,327 | unresolved | |
| Derived End-To-End Interface Integration Frame | `#derived-end-to-end-interface-integration-frame` |  | 4,400 | unresolved | |
| &nbsp;&nbsp;Interface Integration Claim Boundaries | `#interface-integration-claim-boundaries` |  | 1,665 | unresolved | |
| &nbsp;&nbsp;Interface Integration Obligations | `#interface-integration-obligations` |  | 5,074 | unresolved | |
| &nbsp;&nbsp;Computational Whole-Path Evaluation | `#computational-whole-path-evaluation` |  | 1,244 | unresolved | |
| &nbsp;&nbsp;Interface Integration Qualification | `#interface-integration-qualification` |  | 2,144 | unresolved | |
| Complete Engagement Transition | `#complete-engagement-transition` |  | 343 | unresolved | |
| &nbsp;&nbsp;1. Existing Authority Selects The Basis | `#1-existing-authority-selects-the-basis` |  | 280 | unresolved | |
| &nbsp;&nbsp;2. Executive Activates Worker | `#2-executive-activates-worker` |  | 1,192 | unresolved | |
| &nbsp;&nbsp;3. Worker Returns To Executive | `#3-worker-returns-to-executive` |  | 888 | unresolved | |
| &nbsp;&nbsp;4. Executive Evaluates The Work Result | `#4-executive-evaluates-the-work-result` |  | 848 | unresolved | |
| &nbsp;&nbsp;5A. Candidate Does Not Require Independent Review | `#5a-candidate-does-not-require-independent-review` |  | 405 | unresolved | |
| &nbsp;&nbsp;5B. Candidate Requires Independent Review | `#5b-candidate-requires-independent-review` |  | 843 | unresolved | |
| &nbsp;&nbsp;6. Reviewer Returns To Executive | `#6-reviewer-returns-to-executive` |  | 644 | unresolved | |
| &nbsp;&nbsp;Reviewer Result And Triage Projection | `#reviewer-result-and-triage-projection` |  | 2,199 | unresolved | |
| &nbsp;&nbsp;7. Executive Disposes And Checkpoints | `#7-executive-disposes-and-checkpoints` |  | 1,134 | unresolved | |
| &nbsp;&nbsp;Executive Promotion Constraint Projection | `#executive-promotion-constraint-projection` |  | 801 | unresolved | |
| Handoff Projection | `#handoff-projection` |  | 2,964 | unresolved | |
| Coverage Application | `#coverage-application` |  | 3,905 | unresolved | |
| Missing-Frame And Re-Entry Application | `#missing-frame-and-re-entry-application` |  | 997 | unresolved | |
| Product-Owned Adoption Or Project-Defined Configuration | `#product-owned-adoption-or-project-defined-configuration` |  | 59 | unresolved | |
| &nbsp;&nbsp;Existing Authority Selects The Configuration | `#existing-authority-selects-the-configuration` |  | 767 | unresolved | |
| &nbsp;&nbsp;Adopt This Baseline | `#adopt-this-baseline` |  | 1,157 | unresolved | |
| &nbsp;&nbsp;Define A Project Configuration | `#define-a-project-configuration` |  | 1,154 | unresolved | |
| &nbsp;&nbsp;Extension Versus Replacement | `#extension-versus-replacement` |  | 555 | unresolved | |
| Actor Binding And Independence | `#actor-binding-and-independence` |  | 861 | unresolved | |
| Profile Qualification | `#profile-qualification` |  | 5,304 | unresolved | |
| Baseline-Specific Project-Basis Additions | `#baseline-specific-project-basis-additions` |  | 1,192 | unresolved | |
| Baseline-Specific Activation Additions | `#baseline-specific-activation-additions` |  | 887 | unresolved | |
| Failure Classification | `#failure-classification` |  | 4,272 | unresolved | |
| Anti-Patterns | `#anti-patterns` |  | 3,945 | unresolved | |
| Closure | `#closure` |  | 5,131 | unresolved | |

## TICKET_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Core Model | `#core-model` |  | 14 | unresolved | |
| &nbsp;&nbsp;Goals | `#goals` |  | 336 | unresolved | |
| &nbsp;&nbsp;Tickets | `#tickets` |  | 367 | unresolved | |
| &nbsp;&nbsp;Sprints | `#sprints` |  | 949 | unresolved | |
| &nbsp;&nbsp;Comments | `#comments` |  | 380 | unresolved | |
| &nbsp;&nbsp;Execution Contracts | `#execution-contracts` |  | 1,388 | unresolved | |
| &nbsp;&nbsp;Milestone And Phase-Scoped Truth (`STDO-UP-006`) | `#milestone-and-phase-scoped-truth-stdo-up-006` | UP-006 | 671 | unresolved | |
| Default Layout | `#default-layout` |  | 747 | unresolved | |
| Authority | `#authority` |  | 858 | unresolved | |
| Sprint Rules | `#sprint-rules` |  | 16 | unresolved | |
| &nbsp;&nbsp;One Durable Record Per Sprint | `#one-durable-record-per-sprint` |  | 431 | unresolved | |
| &nbsp;&nbsp;Sprint Manifest Required Fields | `#sprint-manifest-required-fields` |  | 1,031 | unresolved | |
| &nbsp;&nbsp;Sprint Status | `#sprint-status` |  | 589 | unresolved | |
| &nbsp;&nbsp;Sprint Admission | `#sprint-admission` |  | 688 | unresolved | |
| &nbsp;&nbsp;Sprint Compliance Escrow | `#sprint-compliance-escrow` |  | 1,298 | unresolved | |
| &nbsp;&nbsp;Sprint Close Review | `#sprint-close-review` |  | 1,174 | unresolved | |
| Ticket Rules | `#ticket-rules` |  | 16 | unresolved | |
| &nbsp;&nbsp;One Durable Record Per Ticket | `#one-durable-record-per-ticket` |  | 592 | unresolved | |
| &nbsp;&nbsp;Multi-Build-Tenant Ticket Independence | `#multi-build-tenant-ticket-independence` |  | 2,874 | unresolved | |
| &nbsp;&nbsp;Required Fields | `#required-fields` |  | 1,201 | unresolved | |
| &nbsp;&nbsp;Allowed Types | `#allowed-types` |  | 158 | unresolved | |
| &nbsp;&nbsp;Ticket Category | `#ticket-category` |  | 1,026 | unresolved | |
| &nbsp;&nbsp;Inside-Out First Ticket Sequencing | `#inside-out-first-ticket-sequencing` |  | 958 | unresolved | |
| &nbsp;&nbsp;Change Class | `#change-class` |  | 1,143 | unresolved | |
| &nbsp;&nbsp;Upward Propagation Check | `#upward-propagation-check` |  | 1,424 | unresolved | |
| &nbsp;&nbsp;Triage Metadata | `#triage-metadata` |  | 371 | unresolved | |
| &nbsp;&nbsp;Work-Carrier-To-Execution Rule | `#work-carrier-to-execution-rule` |  | 4,127 | unresolved | |
| &nbsp;&nbsp;Execution Contract Admission | `#execution-contract-admission` |  | 1,064 | unresolved | |
| &nbsp;&nbsp;Execution And Verification Authority Separation (`STDO-UP-007`) | `#execution-and-verification-authority-separation-stdo-up-007` | UP-007 | 2,835 | unresolved | |
| &nbsp;&nbsp;Recorded Judgment And Owner-Ruling Continuity | `#recorded-judgment-and-owner-ruling-continuity` |  | 2,560 | unresolved | |
| &nbsp;&nbsp;Bounded-Context Term Binding | `#bounded-context-term-binding` |  | 1,020 | unresolved | |
| &nbsp;&nbsp;Evaluation Criteria And Non-Closure Conditions | `#evaluation-criteria-and-non-closure-conditions` |  | 1,132 | unresolved | |
| &nbsp;&nbsp;Condition-Based Closure And Reuse | `#condition-based-closure-and-reuse` |  | 1,395 | unresolved | |
| &nbsp;&nbsp;Test Case Authority | `#test-case-authority` |  | 2,215 | unresolved | |
| &nbsp;&nbsp;Implementation Migration Category | `#implementation-migration-category` |  | 4,944 | unresolved | |
| &nbsp;&nbsp;Migration Strategy Requirements | `#migration-strategy-requirements` |  | 1,097 | unresolved | |
| &nbsp;&nbsp;Recurring Realization And Library Declaration | `#recurring-realization-and-library-declaration` |  | 1,322 | unresolved | |
| &nbsp;&nbsp;Multi-Build-Tenant Review Rule | `#multi-build-tenant-review-rule` |  | 517 | unresolved | |
| &nbsp;&nbsp;Implementation Migration Review Disambiguation | `#implementation-migration-review-disambiguation` |  | 2,243 | unresolved | |
| &nbsp;&nbsp;Impacted Interface Review Checklist | `#impacted-interface-review-checklist` |  | 1,922 | unresolved | |
| &nbsp;&nbsp;Required Break Order And Break-To-Closure Map | `#required-break-order-and-break-to-closure-map` |  | 1,435 | unresolved | |
| &nbsp;&nbsp;Mixed-State Negative Proof | `#mixed-state-negative-proof` |  | 1,699 | unresolved | |
| &nbsp;&nbsp;Allowed Status | `#allowed-status` |  | 240 | unresolved | |
| &nbsp;&nbsp;Ticket Lanes | `#ticket-lanes` |  | 766 | unresolved | |
| &nbsp;&nbsp;One-Truth State Projection And Drift Refusal (`STDO-UP-009`) | `#one-truth-state-projection-and-drift-refusal-stdo-up-009` | UP-009 | 635 | unresolved | |
| Recommended Ticket Shape | `#recommended-ticket-shape` |  | 4,934 | unresolved | |
| Operating Mode | `#operating-mode` |  | 557 | unresolved | |
| Relationship To Other Surfaces | `#relationship-to-other-surfaces` |  | 742 | unresolved | |
| Future Extensions | `#future-extensions` |  | 508 | unresolved | |

## TRAVERSAL_OCCURRENCE_PROFILE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/TRAVERSAL_OCCURRENCE_PROFILE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Position | `#position` |  | 892 | unresolved | |
| Scope | `#scope` |  | 721 | unresolved | |
| Imported Calculus Boundary | `#imported-calculus-boundary` |  | 2,544 | unresolved | |
| Closed Semantic-Object Sorts | `#closed-semantic-object-sorts` |  | 4,521 | unresolved | |
| &nbsp;&nbsp;Finite Reference-Domain Table | `#finite-reference-domain-table` |  | 16,318 | unresolved | |
| Closed Event-Kind Population | `#closed-event-kind-population` |  | 1,504 | unresolved | |
| Closed Relation Families | `#closed-relation-families` |  | 8,905 | unresolved | |
| Closed Constraint, Judgment, Residual, And Stop Kinds | `#closed-constraint-judgment-residual-and-stop-kinds` |  | 6,798 | unresolved | |
| Occurrence Identity | `#occurrence-identity` |  | 1,781 | unresolved | |
| &nbsp;&nbsp;OP-001 Seed Acyclicity | `#op-001-seed-acyclicity` | OP-001 | 248 | unresolved | |
| Candidate, Judgment, Event, And Relation Separation | `#candidate-judgment-event-and-relation-separation` |  | 3,758 | unresolved | |
| &nbsp;&nbsp;OP-002 Atomic Semantic Admission | `#op-002-atomic-semantic-admission` | OP-002 | 581 | unresolved | |
| &nbsp;&nbsp;OP-003 Correction Without Erasure | `#op-003-correction-without-erasure` | OP-003 | 253 | unresolved | |
| Causality And Typed Lineage | `#causality-and-typed-lineage` |  | 748 | unresolved | |
| &nbsp;&nbsp;OP-004 Precedence Is Not Authority | `#op-004-precedence-is-not-authority` | OP-004 | 303 | unresolved | |
| Mutable-Subject Effect Relation | `#mutable-subject-effect-relation` |  | 3,806 | unresolved | |
| &nbsp;&nbsp;OP-005 Mutable Reality Conservation | `#op-005-mutable-reality-conservation` | OP-005 | 496 | unresolved | |
| &nbsp;&nbsp;OP-006 Immutable Iteration History | `#op-006-immutable-iteration-history` | OP-006 | 298 | unresolved | |
| Event Frontier And Projection | `#event-frontier-and-projection` |  | 1,024 | unresolved | |
| &nbsp;&nbsp;OP-007 Scope Conservation | `#op-007-scope-conservation` | OP-007 | 246 | unresolved | |
| Authority And Adoption | `#authority-and-adoption` |  | 966 | unresolved | |
| Exact Profile Identity | `#exact-profile-identity` |  | 172 | unresolved | |
| &nbsp;&nbsp;Closed Profile Signature | `#closed-profile-signature` |  | 5,576 | unresolved | |
| Exclusions | `#exclusions` |  | 563 | unresolved | |
| Conformance Obligations | `#conformance-obligations` |  | 2,222 | unresolved | |

## UX_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/UX_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| 1. Position | `#1-position` |  | 709 | unresolved | |
| &nbsp;&nbsp;1A. Constitutional Authority Rule | `#1a-constitutional-authority-rule` |  | 736 | unresolved | |
| 2. Method Role | `#2-method-role` |  | 871 | unresolved | |
| 3. Method Composition | `#3-method-composition` |  | 684 | unresolved | |
| &nbsp;&nbsp;3A. UX Projection And Constructive Carrier Boundary | `#3a-ux-projection-and-constructive-carrier-boundary` |  | 1,349 | unresolved | |
| 4. Process Model — Elm Architecture | `#4-process-model-elm-architecture` |  | 926 | unresolved | |
| 4A. Process Model Without Language Or Framework Mandate | `#4a-process-model-without-language-or-framework-mandate` |  | 1,781 | unresolved | |
| 5. State Transition Law | `#5-state-transition-law` |  | 1,389 | unresolved | |
| 6. Effect Membrane Rule | `#6-effect-membrane-rule` |  | 1,202 | unresolved | |
| 7. AssetSurface Binding Rule | `#7-assetsurface-binding-rule` |  | 1,328 | unresolved | |
| 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation | `#8-ux-twin-of-odd-115a-view-does-not-own-continuation` |  | 997 | unresolved | |
| &nbsp;&nbsp;8A. Msg-Replay Proof Requirement | `#8a-msg-replay-proof-requirement` |  | 925 | unresolved | |
| 9. View Shape Rule | `#9-view-shape-rule` |  | 981 | unresolved | |
| 10. Type Sharing Rule | `#10-type-sharing-rule` |  | 928 | unresolved | |
| 11. Accessibility Minimum | `#11-accessibility-minimum` |  | 925 | unresolved | |
| 12. Realization Discretion | `#12-realization-discretion` |  | 705 | unresolved | |
| 13. Adoption Guidance | `#13-adoption-guidance` |  | 1,060 | unresolved | |
| &nbsp;&nbsp;13A. Scaffold And Exemption Law | `#13a-scaffold-and-exemption-law` |  | 1,022 | unresolved | |
| &nbsp;&nbsp;13B. UX Sprint Compliance Escrow | `#13b-ux-sprint-compliance-escrow` |  | 2,821 | unresolved | |
| 14. Failure Pattern | `#14-failure-pattern` |  | 1,833 | unresolved | |
| 15. Review Questions | `#15-review-questions` |  | 1,305 | unresolved | |
| 16. Relationship To Other Method Surfaces | `#16-relationship-to-other-method-surfaces` |  | 977 | unresolved | |
| 17. Non-Goals | `#17-non-goals` |  | 378 | unresolved | |
| 18. Canonical Compression | `#18-canonical-compression` |  | 1,349 | unresolved | |

## WORLD_MODEL_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Position | `#position` |  | 1,093 | unresolved | |
| Method Role | `#method-role` |  | 2,639 | unresolved | |
| &nbsp;&nbsp;Builder-Project Specialization Relation | `#builder-project-specialization-relation` |  | 2,004 | unresolved | |
| Constitutional Intents | `#constitutional-intents` |  | 453 | unresolved | |
| Manifesto | `#manifesto` |  | 1,766 | unresolved | |
| What A World Model Is | `#what-a-world-model-is` |  | 1,080 | unresolved | |
| Theoretical Underpinnings Of The Markov Object | `#theoretical-underpinnings-of-the-markov-object` |  | 1,020 | unresolved | |
| &nbsp;&nbsp;What An Effective Blanket Actually Is | `#what-an-effective-blanket-actually-is` |  | 1,473 | unresolved | |
| &nbsp;&nbsp;Four Working Refinements Indicated By The Empirical Program | `#four-working-refinements-indicated-by-the-empirical-program` |  | 2,562 | unresolved | |
| &nbsp;&nbsp;Epistemic Status Of The Construct | `#epistemic-status-of-the-construct` |  | 2,051 | unresolved | |
| &nbsp;&nbsp;Relation To Design Module Method | `#relation-to-design-module-method` |  | 1,048 | unresolved | |
| Method Objectives | `#method-objectives` |  | 675 | unresolved | |
| Core Claims | `#core-claims` |  | 15 | unresolved | |
| &nbsp;&nbsp;Source Systems Remain Sovereign | `#source-systems-remain-sovereign` |  | 204 | unresolved | |
| &nbsp;&nbsp;Domains Are Functional Surfaces | `#domains-are-functional-surfaces` |  | 196 | unresolved | |
| &nbsp;&nbsp;Data Is Evidence, Not Meaning By Itself | `#data-is-evidence-not-meaning-by-itself` |  | 138 | unresolved | |
| &nbsp;&nbsp;World Models Externalize Expert Cognition | `#world-models-externalize-expert-cognition` |  | 154 | unresolved | |
| &nbsp;&nbsp;Mappings Are Semantic Treatments | `#mappings-are-semantic-treatments` |  | 197 | unresolved | |
| &nbsp;&nbsp;Fully Qualified Naming Is Mandatory | `#fully-qualified-naming-is-mandatory` |  | 204 | unresolved | |
| &nbsp;&nbsp;Value Lists Are Domain Artifacts Too | `#value-lists-are-domain-artifacts-too` |  | 167 | unresolved | |
| &nbsp;&nbsp;The World Model Sits Above APIs And Schemas | `#the-world-model-sits-above-apis-and-schemas` |  | 229 | unresolved | |
| &nbsp;&nbsp;Probability Belongs In The Epistemic Overlay | `#probability-belongs-in-the-epistemic-overlay` |  | 833 | unresolved | |
| Single Truth Surface | `#single-truth-surface` |  | 613 | unresolved | |
| Evidence Hierarchy | `#evidence-hierarchy` |  | 674 | unresolved | |
| Method Units | `#method-units` |  | 16 | unresolved | |
| &nbsp;&nbsp;App | `#app` |  | 44 | unresolved | |
| &nbsp;&nbsp;Builder Project | `#builder-project` |  | 423 | unresolved | |
| &nbsp;&nbsp;Published Domain Artifact | `#published-domain-artifact` |  | 100 | unresolved | |
| &nbsp;&nbsp;Fragment | `#fragment` |  | 76 | unresolved | |
| &nbsp;&nbsp;World Model Object | `#world-model-object` |  | 373 | unresolved | |
| &nbsp;&nbsp;Assurance | `#assurance` |  | 211 | unresolved | |
| &nbsp;&nbsp;Attribute Ledger | `#attribute-ledger` |  | 352 | unresolved | |
| &nbsp;&nbsp;Markov Object | `#markov-object` |  | 1,224 | unresolved | |
| &nbsp;&nbsp;Entity Cut | `#entity-cut` |  | 620 | unresolved | |
| &nbsp;&nbsp;Markov-Object Overlay | `#markov-object-overlay` |  | 352 | unresolved | |
| &nbsp;&nbsp;Treatment Surface | `#treatment-surface` |  | 81 | unresolved | |
| &nbsp;&nbsp;Covariance Edge | `#covariance-edge` |  | 109 | unresolved | |
| &nbsp;&nbsp;Adjoint Mapping | `#adjoint-mapping` |  | 66 | unresolved | |
| &nbsp;&nbsp;Temporal Reference Artifact | `#temporal-reference-artifact` |  | 138 | unresolved | |
| &nbsp;&nbsp;Composed World Model | `#composed-world-model` |  | 178 | unresolved | |
| &nbsp;&nbsp;Projection | `#projection` |  | 94 | unresolved | |
| &nbsp;&nbsp;Query Plane | `#query-plane` |  | 208 | unresolved | |
| Method Flow | `#method-flow` |  | 58 | unresolved | |
| &nbsp;&nbsp;1. Observe | `#1-observe` |  | 211 | unresolved | |
| &nbsp;&nbsp;2. Trace | `#2-trace` |  | 257 | unresolved | |
| &nbsp;&nbsp;3. Extract | `#3-extract` |  | 304 | unresolved | |
| &nbsp;&nbsp;4. Assure | `#4-assure` |  | 337 | unresolved | |
| &nbsp;&nbsp;5. Ledger | `#5-ledger` |  | 232 | unresolved | |
| &nbsp;&nbsp;6. Bound | `#6-bound` |  | 244 | unresolved | |
| &nbsp;&nbsp;7. Materialize | `#7-materialize` |  | 224 | unresolved | |
| &nbsp;&nbsp;8. Relate | `#8-relate` |  | 163 | unresolved | |
| &nbsp;&nbsp;9. Publish | `#9-publish` |  | 209 | unresolved | |
| &nbsp;&nbsp;10. Compose | `#10-compose` |  | 218 | unresolved | |
| &nbsp;&nbsp;11. Align (Optional) | `#11-align-optional` |  | 379 | unresolved | |
| &nbsp;&nbsp;12. Project | `#12-project` |  | 259 | unresolved | |
| &nbsp;&nbsp;13. Compile (Optional) | `#13-compile-optional` |  | 594 | unresolved | |
| &nbsp;&nbsp;14. Serve Or Query (Optional) | `#14-serve-or-query-optional` |  | 269 | unresolved | |
| Representation Law | `#representation-law` |  | 1,040 | unresolved | |
| Materialization Law | `#materialization-law` |  | 1,870 | unresolved | |
| Publication Law | `#publication-law` |  | 777 | unresolved | |
| Attribute Ledger Law | `#attribute-ledger-law` |  | 692 | unresolved | |
| Entity Cut Construction Law | `#entity-cut-construction-law` |  | 257 | unresolved | |
| &nbsp;&nbsp;Admissibility | `#admissibility` |  | 1,039 | unresolved | |
| &nbsp;&nbsp;Discrimination | `#discrimination` |  | 1,571 | unresolved | |
| &nbsp;&nbsp;Publication | `#publication` |  | 615 | unresolved | |
| Markov Object Construction Law | `#markov-object-construction-law` |  | 832 | unresolved | |
| &nbsp;&nbsp;1. Paired Evidence Collection | `#1-paired-evidence-collection` |  | 633 | unresolved | |
| &nbsp;&nbsp;2. Identity-Direction Extraction | `#2-identity-direction-extraction` |  | 672 | unresolved | |
| &nbsp;&nbsp;3. Verification By Treatment | `#3-verification-by-treatment` |  | 1,213 | unresolved | |
| &nbsp;&nbsp;4. Core And Coat Decomposition | `#4-core-and-coat-decomposition` |  | 514 | unresolved | |
| &nbsp;&nbsp;5. Null-Peer Discrimination | `#5-null-peer-discrimination` |  | 666 | unresolved | |
| &nbsp;&nbsp;6. Overlay Publication | `#6-overlay-publication` |  | 1,217 | unresolved | |
| &nbsp;&nbsp;7. Storage Shape | `#7-storage-shape` |  | 760 | unresolved | |
| Saturation Law | `#saturation-law` |  | 549 | unresolved | |
| Composition Law | `#composition-law` |  | 655 | unresolved | |
| Projection Law | `#projection-law` |  | 765 | unresolved | |
| Control Plane And Data Plane | `#control-plane-and-data-plane` |  | 1,121 | unresolved | |
| Proof Law | `#proof-law` |  | 891 | unresolved | |
| World-Model-Driven Development | `#world-model-driven-development` |  | 893 | unresolved | |
| Method Output | `#method-output` |  | 770 | unresolved | |
| Companion Surfaces | `#companion-surfaces` |  | 972 | unresolved | |

## WRITING_GUIDE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/WRITING_GUIDE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Core Rule | `#core-rule` |  | 153 | unresolved | |
| Style Rules | `#style-rules` |  | 452 | unresolved | |
| Remove These Habits | `#remove-these-habits` |  | 277 | unresolved | |
| Good Prose | `#good-prose` |  | 230 | unresolved | |
| Bad Prose | `#bad-prose` |  | 316 | unresolved | |
| Method Alignment | `#method-alignment` |  | 241 | unresolved | |
| Specification Artifact Practice | `#specification-artifact-practice` |  | 602 | unresolved | |
| Practical Layer Checks | `#practical-layer-checks` |  | 310 | unresolved | |
| Current-Surface Writing | `#current-surface-writing` |  | 486 | unresolved | |

## Standards members beyond the sixteen bodies

Base route: `stdo://releases/v2.5.1-rc.2/standards/`

| Member | Kind | SHA-256 | Disposition | Successor locus |
|---|---|---|---|---|
| `authority_compressions/README.md` | compression | `ac695b50fbe503e65fd8cb50c69ebe14ec818cc19bdb24941f514cc3c403eb88` | unresolved | |
| `authority_compressions/axiomatic_calculus.compressed.md` | compression | `30d8615f171298e8b40d112eff4fee56e302b63f9e5968272b7e7291f76c7bda` | unresolved | |
| `authority_compressions/design_module_method.compressed.md` | compression | `a6edc3a5fdde1946e9e47f08841b34e1e0a6ea6b937a42e2a7d9b132f53692ee` | unresolved | |
| `authority_compressions/odd_method.compressed.md` | compression | `49968bace86260d6ffa25433598245ec89a23646b3743872aaf40bc99dbc1c6b` | unresolved | |
| `authority_compressions/spec_method.compressed.md` | compression | `fe309ca1397ca7073ed9775bcb4da3c293678ce835fc26d4cd05bffd732091c0` | unresolved | |
| `authority_compressions/stdo_bootstrap.md` | compression | `f7bec3f86d9f24d1fb22acc553ade2eb0861105ec4cd2f1afa7290cc85c5b61a` | unresolved | |
| `authority_compressions/stdo_compressed.md` | compression | `3dfe3bf0913925f5daac497cef7920fdfd0a4f3d4afea1bfc996b0715119819e` | unresolved | |
| `authority_compressions/ticket_method.compressed.md` | compression | `d7ad2a08f71a0f4f4ac9478e2f9f3c08ca22d947b27e30f08476dbbb926745d8` | unresolved | |
| `authority_compressions/traversal_occurrence_profile.compressed.md` | compression | `bfecda2c2e2f1c2f9e1ad97713d6a708227c2f47d4d95ce380d978b0df3877ce` | unresolved | |
| `authority_compressions/ux_method.compressed.md` | compression | `f3323f1f4704360f59fea6d7a8a7ba92be3e1c7d0bc921725da97fdeaf44ad54` | unresolved | |
| `schemas/installed-release-manifest.schema.json` | schema | `711a2eea44b995a043d4d9e02c8427723fc830de1a9f0f3c8c66e8ddb7aee4c2` | unresolved | |
| `schemas/product-definition.schema.json` | schema | `e0a3b544dae6c83bf941096b440700d02fa988fd2767f3b4ab297a1a03f67abf` | unresolved | |
| `templates/AGENTS_TEMPLATE.md` | template | `e27610545d3b9648ca8655052a067b64f93941dd096afd8e8b25c8722b1cb20e` | unresolved | |
| `templates/CLAUDE_TEMPLATE.md` | template | `e27610545d3b9648ca8655052a067b64f93941dd096afd8e8b25c8722b1cb20e` | unresolved | |
| `templates/GOALS_TEMPLATE.md` | template | `2dc711293f5e7129389efe0e5c3ea86e111c528569e6b72dad983cdbc2c71c3d` | unresolved | |
| `templates/INTENT_TEMPLATE.md` | template | `85b1e6c83b30d619e9f7f8018315022b6963edaa03f908e7aac38a16d5bdab26` | unresolved | |
| `templates/PRODUCT_DEFINITION_TEMPLATE.json` | template | `e4189e5e51d525b7d7926ca88c9b9182b4686b8adf81108e72e24b847db94d34` | unresolved | |
| `templates/PRODUCT_TEMPLATE.md` | template | `0e5365e4c87faecbaccb20aa8a106364afcd07635ca52dffbbf4a223873256f9` | unresolved | |
| `templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` | template | `82ffcba100061fa4d63ef8b282815add4f85ae499530ea7f56b38befd5a68d8c` | unresolved | |
| `templates/README.md` | template | `6e30d6e945a758bb4d34612c181a4ac694f9c19b8533b67d7ae0e73a57195a31` | unresolved | |
| `templates/build_tenants/TENANT_REGISTRY_TEMPLATE.md` | template | `8dd5d925a82f63683c9702a5fe8732eaa4afaead626ddfe49e270fb0a79e08a9` | unresolved | |
| `templates/build_tenants/common/README_TEMPLATE.md` | template | `e88790f0521229ca41cadc82af434908e5d8782748ccc93eb287d0e2fb5efae8` | unresolved | |
| `templates/build_tenants/common/design/README_TEMPLATE.md` | template | `7bfaf3873571c9d8a267aa8acc8e47522fc48cd90cfdef9d50216c9ae008e6bd` | unresolved | |
| `templates/build_tenants/common/design/adrs/ADR_TEMPLATE.md` | template | `07d28d93675b86b51953b84584aa7119cf80269354a76aa2356ff18397c7c4cd` | unresolved | |
| `templates/build_tenants/common/design/adrs/README_TEMPLATE.md` | template | `57fd95e135d36059611bca65bc091dafb94809ab521db834a4457513f91737e7` | unresolved | |
| `templates/build_tenants/variant/README_TEMPLATE.md` | template | `0236d71e75b917f4b008474478eda7662e62fc7b11cc7409b8299b2e26f3ef96` | unresolved | |
| `templates/build_tenants/variant/design/README_TEMPLATE.md` | template | `da70241069c9f98d09f6e179c2687966fca70a4546b9c52d2e8aee78644626e1` | unresolved | |
| `templates/build_tenants/variant/design/adrs/ADR_TEMPLATE.md` | template | `d2f77e99fcbafb0b3a2603e4c5854333ae22b65d78ed82a418f7a3b9ecbd988b` | unresolved | |
| `templates/build_tenants/variant/design/adrs/README_TEMPLATE.md` | template | `ae46291f42650da55c279b2aa09ac9ae1c91285b50ff73c0f4d2e538f68a3591` | unresolved | |
| `templates/build_tenants/variant/design/fp/INTENT_TEMPLATE.md` | template | `76e33d7a4a75d77644eec20f6d5d3611894320eab05e36580d29cf90c28a4490` | unresolved | |
| `templates/build_tenants/variant/design/fp/README_TEMPLATE.md` | template | `4542edc7e3a51bfba843530f1ee6b03fd3615f27a65d0f8815ae054225a5594c` | unresolved | |
| `templates/build_tenants/variant/design/fp/edge-overrides/EDGE_OVERRIDE_TEMPLATE.json` | template | `996e1f2cd55090519e7c487ec46333afd2994a546c15190bb11d862e3a0683c4` | unresolved | |
| `templates/build_tenants/variant/design/fp/edge-overrides/README_TEMPLATE.md` | template | `1432362afe35b5816259e6bef0163ffc38db6639557cd4541d2804ff04d02991` | unresolved | |
| `templates/docs/README_TEMPLATE.md` | template | `9c3425ff8b49c2b5573e9b8f0130b7a3e5f7d3ddcc01204aec363327e0872e7f` | unresolved | |
| `templates/requirements/README_TEMPLATE.md` | template | `4eacc1d3604e4859b60fc29c4bc6555fcd5de11d9ca1773258eedfb398e0f4a9` | unresolved | |
| `templates/requirements/STARTER_REQUIREMENTS_TEMPLATE.md` | template | `67e2061e7eb7757bdb71cff5775cfea90b33b5019ba31e1509e4d456cf66e5dd` | unresolved | |

36 rows.

## Auxiliary members

Published with the release outside `standards/`, per the manifest's `auxiliary` section.

| Member | Kind | SHA-256 | Disposition | Successor locus |
|---|---|---|---|---|
| `LICENSE` | licence | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` | unresolved | |
| `plugins/spec/.claude-plugin/plugin.json` | plugin | `b67bcd1c104ac7ccf962e47bc45b274f58cb3045a2c6e63a8f280f932038e593` | unresolved | |
| `plugins/spec/.codex-plugin/plugin.json` | plugin | `8287f192470a23cea9a70fa95086962718b932f2e9c2bcb19f8a708f44612667` | unresolved | |
| `plugins/spec/LICENSE` | plugin | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` | unresolved | |
| `plugins/spec/claude-skills/refresh/SKILL.md` | plugin | `a501d0d6df6e6736a33180d876f8c83a157f5f0248f195d1687bce876f3a2b79` | unresolved | |
| `plugins/spec/references/GETTING_STARTED.md` | plugin | `bfde7bb046086e99f77bcb84bbb432fb814c8a1b9962297c6834c28e68bbdcc6` | unresolved | |
| `plugins/spec/references/PRODUCT_BASIS.md` | plugin | `4dcf0bb305732dcb280187804889426bd5abcd7188d9bb8df8b16af265a0b23f` | unresolved | |
| `plugins/spec/references/REFRESH.md` | plugin | `ced18a9ba499843f4321148d2d8df3ec0da7ebe8ecdb95ca282ff7dba5d53a8c` | unresolved | |
| `plugins/spec/skills/stdo-help/SKILL.md` | plugin | `3a77b5a010f4a30debce45e4b6cd846bc84a135358c0d7369178a9512d693ee2` | unresolved | |
| `plugins/spec/skills/stdo-help/agents/openai.yaml` | plugin | `af3add1ac0464524f1fbb33dd63c49787c1c905e883a3cbd0d48a8075474a20e` | unresolved | |
| `plugins/spec/skills/stdo-review/SKILL.md` | plugin | `99f3d12012c7c3a39fc6ac5b80f4cc54c40d2709c536ec17a535647608ecf4db` | unresolved | |
| `plugins/spec/skills/stdo-review/agents/openai.yaml` | plugin | `e736f9789012d0365e5dec0973cd394a48009aa06548b83cea5912643eb7d9d4` | unresolved | |
| `plugins/spec/skills/stdo-status/SKILL.md` | plugin | `eef2081ec8a3db8a4f76db6408aa563c34c26b1e65e24417967956cc65655678` | unresolved | |
| `plugins/spec/skills/stdo-status/agents/openai.yaml` | plugin | `b8a9e5843fcb27d5a774ae34ebabe91b039d1999af1b4efd57dcdc5a16383e37` | unresolved | |
| `plugins/spec/skills/stdo-ticket/SKILL.md` | plugin | `419f12c3339e70ab3c02aa391e619463ebd20f2602287e1028a91bfe2cdeff85` | unresolved | |
| `plugins/spec/skills/stdo-ticket/agents/openai.yaml` | plugin | `0ca0733a5bf692cf9b9318c1eb1a64d66262b60b2357b59e24fa4d6dfc4d0d99` | unresolved | |
| `plugins/spec/skills/stdo-work/SKILL.md` | plugin | `39d9f88af4b574c4e30f45adc3b19ed324c25ae453d7359112af71aa9d4d4d8f` | unresolved | |
| `plugins/spec/skills/stdo-work/agents/openai.yaml` | plugin | `88995a63dc11355deb2f72948a84702f555cc52a4398843f391c7901c0bf7d3f` | unresolved | |
| `release/release-note.md` | release note | `2593a003a5cddccc225bfdd450f71be627453bc48dd80fbad55e298f5fbc34fe` | unresolved | |

19 rows.
