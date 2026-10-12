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
| Position | `#position` |  | 1,866 | conserved | `AXIOMATIC_CALCULUS.md#1-position` |
| Derivation Provenance | `#derivation-provenance` |  | 3,724 | conserved; the derivation account is carried with absolute rc.2 routes beside the successor member that now states each commitment; "ODD" and "GTL" generalised to profile, realisation and carrier; "graph, runtime, ODD, or application shorthand" generalised to a runtime, a profile, a realisation or an application, which include the graph case; field correction: the predecessor says the resolved address array is recorded under `derivation_basis.release_uri`, the locus says `derivation_basis.principle_refs`, the array field that the record shape in both editions actually declares for it (`release_uri` holds one URI); a correction that tightens the text to the record, not a change of law | `AXIOMATIC_CALCULUS.md#derivation-provenance` |
| Scope | `#scope` |  | 659 | conserved | `AXIOMATIC_CALCULUS.md#scope` |
| Core Signature | `#core-signature` |  | 4,767 | conserved; the carrier list "records, tables, graphs, terms" generalised to records, tables, terms, clauses, code or any other representation, which includes graphs | `AXIOMATIC_CALCULUS.md#2-signature` |
| Typed Records | `#typed-records` |  | 560 | conserved | `AXIOMATIC_CALCULUS.md#3-typed-records` |
| &nbsp;&nbsp;Semantic Object | `#semantic-object` |  | 333 | conserved | `AXIOMATIC_CALCULUS.md#semantic-object` |
| &nbsp;&nbsp;Typed Relation | `#typed-relation` |  | 396 | conserved | `AXIOMATIC_CALCULUS.md#typed-relation` |
| &nbsp;&nbsp;Constraint | `#constraint` |  | 537 | conserved | `AXIOMATIC_CALCULUS.md#constraint` |
| &nbsp;&nbsp;Latitude | `#latitude` |  | 337 | conserved | `AXIOMATIC_CALCULUS.md#latitude` |
| &nbsp;&nbsp;Residual | `#residual` |  | 611 | conserved | `AXIOMATIC_CALCULUS.md#residual` |
| Fundamental Laws | `#fundamental-laws` |  | 20 | not applicable: heading with no claim text (20 bytes); its children are disposed individually | `AXIOMATIC_CALCULUS.md#4-fundamental-laws` |
| &nbsp;&nbsp;AC-001 Closed Signature | `#ac-001-closed-signature` | AC-001 | 390 | conserved | `AXIOMATIC_CALCULUS.md#ac-001-closed-signature` |
| &nbsp;&nbsp;AC-002 Scoped Identity | `#ac-002-scoped-identity` | AC-002 | 218 | conserved; scoped identity is defined at FOUNDATIONS.md §2 Object, the law is in the locus; "graph position" generalised to position in any structure, which includes it | `AXIOMATIC_CALCULUS.md#ac-002-scoped-identity` |
| &nbsp;&nbsp;AC-003 Reference Closure | `#ac-003-reference-closure` | AC-003 | 426 | conserved | `AXIOMATIC_CALCULUS.md#ac-003-reference-closure` |
| &nbsp;&nbsp;AC-004 Relation Typing | `#ac-004-relation-typing` | AC-004 | 227 | conserved | `AXIOMATIC_CALCULUS.md#ac-004-relation-typing` |
| &nbsp;&nbsp;AC-005 Authority Conservation | `#ac-005-authority-conservation` | AC-005 | 323 | conserved; authority kinds are defined at FOUNDATIONS.md §2, the law is in the locus | `AXIOMATIC_CALCULUS.md#ac-005-authority-conservation` |
| &nbsp;&nbsp;AC-006 Basis Coherence | `#ac-006-basis-coherence` | AC-006 | 246 | conserved; basis is defined at FOUNDATIONS.md §2, the law is in the locus | `AXIOMATIC_CALCULUS.md#ac-006-basis-coherence` |
| &nbsp;&nbsp;AC-007 Constraint And Refusal | `#ac-007-constraint-and-refusal` | AC-007 | 274 | conserved; stated as a law over constraints using the algebra defined once in `ACTIVATION.md#3-result-algebra`, consistent with its three-case boundary; the declared algebra is tightened to the core or a declared refinement with a total mapping | `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` |
| &nbsp;&nbsp;AC-008 Explicit Latitude | `#ac-008-explicit-latitude` | AC-008 | 221 | conserved; generic form over any two values at FOUNDATIONS.md §4 | `AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude` |
| &nbsp;&nbsp;AC-009 Residual Conservation | `#ac-009-residual-conservation` | AC-009 | 258 | conserved | `AXIOMATIC_CALCULUS.md#ac-009-residual-conservation` |
| &nbsp;&nbsp;AC-010 Material Closure | `#ac-010-material-closure` | AC-010 | 558 | conserved; applied by ACTIVATION.md §2 | `AXIOMATIC_CALCULUS.md#ac-010-material-closure` |
| &nbsp;&nbsp;AC-011 Projection | `#ac-011-projection` | AC-011 | 435 | conserved; applied by ACTIVATION.md §2 | `AXIOMATIC_CALCULUS.md#ac-011-projection` |
| &nbsp;&nbsp;AC-012 Overlay | `#ac-012-overlay` | AC-012 | 355 | conserved | `AXIOMATIC_CALCULUS.md#ac-012-overlay` |
| &nbsp;&nbsp;AC-013 Transformation | `#ac-013-transformation` | AC-013 | 6,410 | conserved in full; FOUNDATIONS.md §4 conservation accounting consumes its delta fields | `AXIOMATIC_CALCULUS.md#ac-013-transformation` |
| &nbsp;&nbsp;AC-014 Judgment Separation | `#ac-014-judgment-separation` | AC-014 | 448 | conserved; the judgment object is defined at FOUNDATIONS.md §2, the record and the law are in the locus | `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation` |
| Traversals And Functor Kinds | `#traversals-and-functor-kinds` |  | 1,875 | conserved; the stop algebra is tied to the one result algebra of ACTIVATION.md §3 (tightening); the traversal record's ownership against same-spelled terms is made explicit | `AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds` |
| &nbsp;&nbsp;AC-015 Functor Classification | `#ac-015-functor-classification` | AC-015 | 202 | conserved | `AXIOMATIC_CALCULUS.md#ac-015-functor-classification` |
| &nbsp;&nbsp;AC-016 Typed Composition | `#ac-016-typed-composition` | AC-016 | 556 | conserved; P4a at FOUNDATIONS.md §3 is its generic form over steps | `AXIOMATIC_CALCULUS.md#ac-016-typed-composition` |
| Interpretation And Models | `#interpretation-and-models` |  | 1,235 | conserved | `AXIOMATIC_CALCULUS.md#6-interpretation-and-models` |
| &nbsp;&nbsp;AC-017 Interpretation Fidelity | `#ac-017-interpretation-fidelity` | AC-017 | 377 | conserved | `AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity` |
| &nbsp;&nbsp;AC-018 Structural And Semantic Separation | `#ac-018-structural-and-semantic-separation` | AC-018 | 324 | conserved; generic form over every review at EVALUATION.md §2 | `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation` |
| &nbsp;&nbsp;AC-019 Valid Model | `#ac-019-valid-model` | AC-019 | 800 | conserved; the checker rule's generic form at EVALUATION.md §2 | `AXIOMATIC_CALCULUS.md#ac-019-valid-model` |
| Subject And Carrier Boundaries | `#subject-and-carrier-boundaries` |  | 895 | conserved | `AXIOMATIC_CALCULUS.md#7-layers` |
| &nbsp;&nbsp;AC-020 Layer And Release Separation | `#ac-020-layer-and-release-separation` | AC-020 | 733 | conserved; applied to release lineage by SPEC_METHOD.md §6 | `AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation` |
| Exact Calculus Identity | `#exact-calculus-identity` |  | 3,655 | conserved; every determination of the identity law and the record shape is restated; the record instance (the coordinates) is a release artefact issued after the bytes exist, not a claim of the section; this edition's identity is bound at its own release under RELEASE and AC-020 and the predecessor's coordinates are recorded as provenance | `AXIOMATIC_CALCULUS.md#8-calculus-identity` |
| Application Boundary | `#application-boundary` |  | 392 | conserved | `AXIOMATIC_CALCULUS.md#application-boundary` |
| External Imports And Specializations | `#external-imports-and-specializations` |  | 385 | conserved | `AXIOMATIC_CALCULUS.md#external-imports-and-specialisations` |
| Exclusions | `#exclusions` |  | 471 | conserved; "graph storage topology" and "world-model ontology" generalised to any storage topology and any domain ontology | `AXIOMATIC_CALCULUS.md#exclusions` |
| Conformance Obligations | `#conformance-obligations` |  | 1,251 | conserved | `AXIOMATIC_CALCULUS.md#10-conformance-obligations` |

## DESIGN_MODULE_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| 1. Purpose | `#1-purpose` |  | 2,536 | conserved; the biases, goals, co-evolution condition on same-pass derivation, bounded traversal, non-replacement and scope | `DESIGN_MODULE.md#purpose` |
| 2. Position | `#2-position` |  | 653 | conserved; the four "should" clauses and functional discipline without a functional language | `DESIGN_MODULE.md#position` |
| 3. Core Rule | `#3-core-rule` |  | 343 | conserved; stated once in SPEC_METHOD §2 Realisation shape at "should" force, scoped to boundaries the design profile governs; DESIGN_MODULE points there | `SPEC_METHOD.md#realisation-shape`; `DESIGN_MODULE.md#core-rule` |
| 3A. ODD Alignment And Escalation Rule | `#3a-odd-alignment-and-escalation-rule` |  | 1,404 | conserved; the graph-execution profile named for ODD, its own terms kept in this tier-3 profile | `DESIGN_MODULE.md#2-graph-execution-alignment-and-escalation` |
| 3B. Boundary Closure Evaluators | `#3b-boundary-closure-evaluators` |  | 356 | conserved | `DESIGN_MODULE.md#3-boundary-closure-evaluators` |
| &nbsp;&nbsp;1. Authority Seam Closure | `#1-authority-seam-closure` |  | 1,200 | conserved; with the four source-coherence requirements | `DESIGN_MODULE.md#authority-seam-closure` |
| &nbsp;&nbsp;2. Essential Carrier Consolidation | `#2-essential-carrier-consolidation` |  | 613 | conserved | `DESIGN_MODULE.md#essential-carrier-consolidation` |
| &nbsp;&nbsp;3. Enforcement After Proof | `#3-enforcement-after-proof` |  | 743 | conserved | `DESIGN_MODULE.md#enforcement-after-proof` |
| 3B. Ingress Collapse Rule | `#3b-ingress-collapse-rule` |  | 758 | conserved | `DESIGN_MODULE.md#ingress-collapse` |
| 4. Functional Bias Without Language Mandate | `#4-functional-bias-without-language-mandate` |  | 934 | conserved | `DESIGN_MODULE.md#functional-bias-without-language-mandate` |
| 4A. Python Typing Rule | `#4a-python-typing-rule` |  | 1,778 | conserved | `DESIGN_MODULE.md#python-typing` |
| 4B. Ontology-First Design Rule | `#4b-ontology-first-design-rule` |  | 2,538 | conserved; the proportionality relation it applies is ACTIVATION §6 | `DESIGN_MODULE.md#5-ontology-first-design` |
| &nbsp;&nbsp;Proportional Design Sequencing | `#proportional-design-sequencing` |  | 3,794 | conserved in full; the four definitions, both modes, counterfactual evidence, no prior gate where no material alternative remains, evidence not authority, one bounded design_reframe; the general proportionality relation is ACTIVATION §6, pointed to | `DESIGN_MODULE.md#proportional-design-sequencing`; `ACTIVATION.md#6-cost-and-proportionality` |
| &nbsp;&nbsp;Decision-Complete Symbolic Design | `#decision-complete-symbolic-design` |  | 1,870 | conserved in full; the nineteen-term M(B) and the decision-complete criterion as the design-gate acceptance criterion | `DESIGN_MODULE.md#decision-complete-symbolic-design` |
| &nbsp;&nbsp;Bounded Frame Conservation (`STDO-UP-017`) | `#bounded-frame-conservation-stdo-up-017` | UP-017 | 2,941 | conserved; the five frame items, several governing frames, evaluation and re-entry, subordinate frames, falsifier, derivation order; the seam rule is ACTIVATION §1 Execution unit and §4 Refinement, P4b's frame instance FOUNDATIONS §3, both pointed to | `DESIGN_MODULE.md#bounded-frame-conservation-up-017`; `ACTIVATION.md#execution-unit`; `ACTIVATION.md#4-totality-and-refinement` |
| &nbsp;&nbsp;Native Constructability Before Design Acceptance (`STDO-UP-002`) | `#native-constructability-before-design-acceptance-stdo-up-002` | UP-002 | 660 | conserved | `DESIGN_MODULE.md#native-constructability-up-002` |
| &nbsp;&nbsp;Capability And Foundation Selection (`STDO-UP-023`) | `#capability-and-foundation-selection-stdo-up-023` | UP-023 | 6,741 | conserved in full; discovery record, comparison, elimination, dominance, frontier, trade-off owner, role preservation, recursion, proportional application; the candidate-not-adjudication law is FOUNDATIONS §4 Shared machinery, pointed to | `DESIGN_MODULE.md#capability-and-foundation-selection-up-023`; `FOUNDATIONS.md#4-algebra` |
| &nbsp;&nbsp;Entity And Lifecycle Completeness | `#entity-and-lifecycle-completeness` |  | 1,664 | conserved | `DESIGN_MODULE.md#entity-and-lifecycle-completeness` |
| &nbsp;&nbsp;Authority Model | `#authority-model` |  | 1,659 | conserved | `DESIGN_MODULE.md#authority-model` |
| &nbsp;&nbsp;Transformation Admission Completeness (`STDO-UP-016`) | `#transformation-admission-completeness-stdo-up-016` | UP-016 | 4,144 | conserved in full; binds ACTIVATION §4 as sole owner of the admission and standing-test semantics (UP-021) | `DESIGN_MODULE.md#transformation-admission-completeness-up-016`; `ACTIVATION.md#complete-enclosing-relation-admission` |
| &nbsp;&nbsp;Atomic Functions And Higher-Order Composition | `#atomic-functions-and-higher-order-composition` |  | 2,012 | conserved | `DESIGN_MODULE.md#atomic-functions-and-higher-order-composition` |
| &nbsp;&nbsp;Prime Semantic Atoms And Universal Domain | `#prime-semantic-atoms-and-universal-domain` |  | 1,526 | conserved | `DESIGN_MODULE.md#prime-semantic-atoms-and-admitted-domain` |
| &nbsp;&nbsp;Whole-Family Prime Contraction | `#whole-family-prime-contraction` |  | 1,380 | conserved in full | `DESIGN_MODULE.md#whole-family-prime-contraction` |
| &nbsp;&nbsp;Recursive Prime And Root Conservation (`STDO-UP-003`) | `#recursive-prime-and-root-conservation-stdo-up-003` | UP-003 | 1,159 | conserved in full | `DESIGN_MODULE.md#recursive-prime-and-root-conservation-up-003` |
| &nbsp;&nbsp;Ontology Projection Law | `#ontology-projection-law` |  | 1,420 | conserved | `DESIGN_MODULE.md#ontology-projection` |
| 5. Prime Law | `#5-prime-law` |  | 2,910 | conserved | `DESIGN_MODULE.md#6-prime-law` |
| &nbsp;&nbsp;Boundary And Governance Cost (`STDO-UP-005`) | `#boundary-and-governance-cost-stdo-up-005` | UP-005 | 652 | conserved; the distinct boundaries and the six contraction failures restated; the proportionality relation is ACTIVATION §6, pointed to | `DESIGN_MODULE.md#boundary-and-governance-cost-up-005`; `ACTIVATION.md#6-cost-and-proportionality` |
| 5A. Irreducible Architectural Carrier Set Rule | `#5a-irreducible-architectural-carrier-set-rule` |  | 2,466 | conserved; the IACS is the carrier inventory ASSURANCE §2, §7 and §15 bind | `DESIGN_MODULE.md#irreducible-architectural-carrier-set` |
| &nbsp;&nbsp;IACS Revision Obligation | `#iacs-revision-obligation` |  | 951 | conserved; the assurance-congruence law (UP-022) written as EVALUATION §1 and §3 | `DESIGN_MODULE.md#iacs-revision` |
| 5B. Promotion Test | `#5b-promotion-test` |  | 1,299 | conserved | `DESIGN_MODULE.md#promotion-test` |
| 5C. Boundary Inflation Prohibition | `#5c-boundary-inflation-prohibition` |  | 1,087 | conserved | `DESIGN_MODULE.md#boundary-inflation-prohibition` |
| 5D. Reference-Derived Module Design Rule | `#5d-reference-derived-module-design-rule` |  | 1,623 | conserved | `DESIGN_MODULE.md#reference-derived-module-design` |
| 5E. Ontology And Three-View Behavioral Design Gate | `#5e-ontology-and-three-view-behavioral-design-gate` |  | 1,517 | conserved | `DESIGN_MODULE.md#7-ontology-and-three-view-design-gate` |
| &nbsp;&nbsp;Ontology evidence | `#ontology-evidence` |  | 865 | conserved | `DESIGN_MODULE.md#ontology-evidence` |
| &nbsp;&nbsp;Invariant Reconstruction Sufficiency (`STDO-UP-018`) | `#invariant-reconstruction-sufficiency-stdo-up-018` | UP-018 | 3,117 | conserved in full; the four-decision table, both boundaries, the falsifier and the withheld-history test; the general reconstruction-without-history rule is ACTIVATION §1 Intake, pointed to | `DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018`; `ACTIVATION.md#intake` |
| &nbsp;&nbsp;Domain model | `#domain-model` |  | 1,261 | conserved | `DESIGN_MODULE.md#domain-model` |
| &nbsp;&nbsp;Sequence model | `#sequence-model` |  | 935 | conserved | `DESIGN_MODULE.md#sequence-model` |
| &nbsp;&nbsp;State model | `#state-model` |  | 560 | conserved | `DESIGN_MODULE.md#state-model` |
| &nbsp;&nbsp;Cross-view axiom evaluation | `#cross-view-axiom-evaluation` |  | 1,777 | conserved | `DESIGN_MODULE.md#cross-view-axiom-evaluation` |
| &nbsp;&nbsp;Gate and retrospective work | `#gate-and-retrospective-work` |  | 2,373 | conserved | `DESIGN_MODULE.md#gate-and-retrospective-work` |
| &nbsp;&nbsp;Computational Realization Projection (`STDO-UP-019`) | `#computational-realization-projection-stdo-up-019` | UP-019 | 5,091 | conserved in full; cost separation and dimension declaration are ACTIVATION §6, shared machinery FOUNDATIONS §4, both pointed to | `DESIGN_MODULE.md#computational-realisation-projection-up-019`; `ACTIVATION.md#6-cost-and-proportionality`; `FOUNDATIONS.md#4-algebra` |
| 5F. Theoretical Framing For Boundary Law | `#5f-theoretical-framing-for-boundary-law` |  | 1,897 | conserved | `DESIGN_MODULE.md#8-theoretical-framing` |
| 6. Design Module Taxonomy | `#6-design-module-taxonomy` |  | 1,757 | conserved | `DESIGN_MODULE.md#9-module-taxonomy` |
| 6A. Design To Module To (Implementation, Unit Tests) Evidence Route | `#6a-design-to-module-to-implementation-unit-tests-evidence-route` |  | 3,379 | conserved in full; restated in tier-2 terms under the binding DESIGN_MODULE declares | `ASSURANCE.md#14-design-to-module-evidence-route` |
| 6B. Module-Derived Unit Test Rule | `#6b-module-derived-unit-test-rule` |  | 1,759 | conserved in full; ownership written as the authority-source split of ASSURANCE §2 | `ASSURANCE.md#15-module-derived-unit-tests` |
| 6C. Module Lifecycle Confirmation Rule | `#6c-module-lifecycle-confirmation-rule` |  | 2,201 | conserved in full | `ASSURANCE.md#16-module-lifecycle-confirmation` |
| 7. Immutable Carrier Rule | `#7-immutable-carrier-rule` |  | 585 | conserved | `DESIGN_MODULE.md#immutable-carriers` |
| 8. Totality Rule | `#8-totality-rule` |  | 659 | conserved; P5 and the result algebra are FOUNDATIONS §3 and ACTIVATION §3, pointed to | `DESIGN_MODULE.md#totality` |
| 9. Effect-Edge Rule | `#9-effect-edge-rule` |  | 660 | conserved | `DESIGN_MODULE.md#effect-edge` |
| 10. No Semantic Center Rule | `#10-no-semantic-center-rule` |  | 705 | conserved | `DESIGN_MODULE.md#no-semantic-centre` |
| 11. Coupling Rule | `#11-coupling-rule` |  | 643 | conserved | `DESIGN_MODULE.md#coupling` |
| 11A. Governance/Strategy Separation Rule | `#11a-governancestrategy-separation-rule` |  | 1,320 | conserved | `DESIGN_MODULE.md#governance-and-strategy-separation` |
| 11B. Opportunistic Optimization Rule | `#11b-opportunistic-optimization-rule` |  | 2,411 | conserved | `DESIGN_MODULE.md#opportunistic-optimisation` |
| 11C. Recurrence Extraction Rule | `#11c-recurrence-extraction-rule` |  | 2,564 | conserved; ticket-level recording at TICKETS §6 | `DESIGN_MODULE.md#recurrence-extraction` |
| 11D. Post-Ticket Design Review Rule | `#11d-post-ticket-design-review-rule` |  | 3,775 | conserved | `DESIGN_MODULE.md#post-ticket-design-review` |
| 12. Interface Bleed Prohibition | `#12-interface-bleed-prohibition` |  | 669 | conserved | `DESIGN_MODULE.md#interface-bleed-prohibition` |
| 13. Proxy Interface Prohibition | `#13-proxy-interface-prohibition` |  | 640 | conserved | `DESIGN_MODULE.md#proxy-interface-prohibition` |
| 14. Design Review Questions | `#14-design-review-questions` |  | 8,641 | conserved; all 56 questions | `DESIGN_MODULE.md#design-review-questions` |
| 14A. Functional Realization Review Checklist | `#14a-functional-realization-review-checklist` |  | 8,895 | conserved; all 43 checks and the 14 hard-gate checks | `DESIGN_MODULE.md#functional-realisation-checklist` |
| 15. Adoption Guidance | `#15-adoption-guidance` |  | 2,160 | conserved | `DESIGN_MODULE.md#adoption` |
| 16. Relationship To Other Method Surfaces | `#16-relationship-to-other-method-surfaces` |  | 2,090 | conserved | `DESIGN_MODULE.md#relationship-to-other-members` |
| 17. Non-Goals | `#17-non-goals` |  | 627 | conserved; stated once in SPEC_METHOD §2 Realisation shape, scoped to boundaries the design profile governs; DESIGN_MODULE points there | `SPEC_METHOD.md#realisation-shape`; `DESIGN_MODULE.md#non-goals` |

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
| Position | `#position` |  | 657 | conserved | `IDENTITY.md#1-position` |
| Core Law | `#core-law` |  | 12 | not applicable: heading with no claim text (12 bytes); its four children are disposed individually | `IDENTITY.md#2-core-law` |
| &nbsp;&nbsp;1. Scoped Identity | `#1-scoped-identity` |  | 326 | conserved | `IDENTITY.md#scoped-identity` |
| &nbsp;&nbsp;2. Uniqueness Law | `#2-uniqueness-law` |  | 404 | conserved | `IDENTITY.md#uniqueness` |
| &nbsp;&nbsp;3. Type Law | `#3-type-law` |  | 499 | conserved; three example kinds generalised to remove profile terms (graph_function, asset_surface, graph_call) | `IDENTITY.md#type` |
| &nbsp;&nbsp;4. Stability Law | `#4-stability-law` |  | 411 | conserved | `IDENTITY.md#stability` |
| Human-Readable vs Opaque Identity | `#human-readable-vs-opaque-identity` |  | 604 | conserved | `IDENTITY.md#3-readable-and-opaque-identity` |
| Identity Hierarchy | `#identity-hierarchy` |  | 759 | conserved | `IDENTITY.md#4-identity-hierarchy` |
| Authority Split | `#authority-split` |  | 19 | not applicable: heading with no claim text (19 bytes); its two children are disposed individually | `IDENTITY.md#5-authority-split` |
| &nbsp;&nbsp;Engine-Owned Identity | `#engine-owned-identity` |  | 435 | conserved; "graph calls" generalised to "function calls" and "frames" to "execution frames" | `IDENTITY.md#engine-owned-identity` |
| &nbsp;&nbsp;Domain-Owned Identity | `#domain-owned-identity` |  | 488 | conserved | `IDENTITY.md#domain-owned-identity` |
| Authority Identity And Conservation (`STDO-UP-004`) | `#authority-identity-and-conservation-stdo-up-004` | UP-004 | 1,363 | conserved in full; the F_H projection generalised to a profile term; applied to acceptance in EVALUATION §5 | `IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004` |
| Default Formats And Overrides | `#default-formats-and-overrides` |  | 33 | not applicable: heading with no claim text (33 bytes); its three children are disposed individually | `IDENTITY.md#7-default-formats-and-overrides` |
| &nbsp;&nbsp;Defaults From A Bound ABG Realization | `#defaults-from-a-bound-abg-realization` |  | 419 | conserved; the "may publish" permission and its graph-profile reading restated in DESIGN_MODULE §12; starter conventions and convenience contracts, not universal doctrine, lawful only while overridable, in IDENTITY §7 | `DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation`; `IDENTITY.md#derived-domain-overrides` |
| &nbsp;&nbsp;Derived Domain Overrides | `#derived-domain-overrides` |  | 459 | conserved | `IDENTITY.md#derived-domain-overrides` |
| &nbsp;&nbsp;Override Publication Surface | `#override-publication-surface` |  | 1,060 | conserved; "bound ABG realization" generalised to "bound runtime realisation" | `IDENTITY.md#override-publication-surface` |
| Parsing Law | `#parsing-law` |  | 838 | conserved | `IDENTITY.md#8-parsing` |
| Release Version Boundary | `#release-version-boundary` |  | 639 | superseded; the "latest-accepted" selector is replaced by the release law the clause cites (RELEASE §1 selector paragraph, §3 Exact-cut qualification, §8 Acceptance criteria: highest-ordinal published, never moved by acceptance); the row's other determinations are restated unchanged in IDENTITY §9 | `IDENTITY.md#9-release-version-boundary`; `RELEASE.md#1-context-and-position`; `RELEASE.md#exact-cut-qualification`; `RELEASE.md#acceptance-criteria` |
| Minimum Questions | `#minimum-questions` |  | 573 | conserved | `IDENTITY.md#10-minimum-questions` |
| Examples | `#examples` |  | 12 | not applicable: heading with no claim text (12 bytes); its two children are disposed individually | `IDENTITY.md#11-examples` |
| &nbsp;&nbsp;Lawful | `#lawful` |  | 470 | conserved; the ABG realisation generalised to a runtime realisation | `IDENTITY.md#lawful` |
| &nbsp;&nbsp;Unlawful | `#unlawful` |  | 288 | conserved | `IDENTITY.md#unlawful` |
| Consequence For Implementations | `#consequence-for-implementations` |  | 541 | conserved | `IDENTITY.md#12-consequence-for-implementations` |

## ODD_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| 1. Position | `#1-position` |  | 2,827 | conserved; the instruction written `using ODD, build this product`; its eight meanings, the paradigm equation, the three role expansions, the bounded-context URN, consumer binding and the two core jobs restated | `ODD.md#1-position` |
| 2. Method Role | `#2-method-role` |  | 906 | conserved; WORLD_MODEL_METHOD written as the world-model profile (WORLD_MODEL, tier 3) | `ODD.md#2-method-role` |
| 3. Method Composition | `#3-method-composition` |  | 1,456 | conserved | `ODD.md#3-method-composition` |
| 4. Method Folder Semantics | `#4-method-folder-semantics` |  | 1,660 | conserved; the three classes and the rule that only method members are constitutional restated, the class named by its predecessor membership (`*_METHOD.md`); which successor members form the class, now that no suffix marks it, is a residual for README or PRODUCT_DEFINITION; the authoring path `specification/standards/` written generically, its successor path bound at packaging | `ODD.md#4-method-library-classes` |
| 5. Graph Model | `#5-graph-model` |  | 125 | conserved | `ODD.md#5-graph-model` |
| &nbsp;&nbsp;Nodes | `#nodes` |  | 458 | conserved; the ten example names kept as illustrative | `ODD.md#nodes` |
| &nbsp;&nbsp;Vectors | `#vectors` |  | 232 | conserved | `ODD.md#vectors` |
| &nbsp;&nbsp;Probabilistic Compute | `#probabilistic-compute` |  | 3,160 | conserved; the three graph-native URNs, both directional specialisations with their preservation, exclusion and invalidation law; the source concepts' owner written SPEC_METHOD §5; kept distinct from the a_c functor kinds of AXIOMATIC_CALCULUS §5 | `ODD.md#probabilistic-compute` |
| &nbsp;&nbsp;Graph Functions | `#graph-functions` |  | 379 | conserved; the three forms and the outer-contract rule | `ODD.md#graph-functions` |
| &nbsp;&nbsp;Traversal | `#traversal` |  | 323 | conserved | `ODD.md#traversal` |
| 6. Product Boundary | `#6-product-boundary` |  | 1,576 | conserved | `ODD.md#6-product-boundary` |
| 7. Self-Host Boundary Rule | `#7-self-host-boundary-rule` |  | 756 | conserved | `ODD.md#7-self-host-boundary` |
| 8. Responsibility Layers And Local Binding | `#8-responsibility-layers-and-local-binding` |  | 1,347 | conserved | `ODD.md#8-responsibility-layers-and-local-binding` |
| 9. Method Governance And Audit | `#9-method-governance-and-audit` |  | 1,926 | conserved; "ODD_METHOD.md" written as this profile | `ODD.md#9-method-governance-and-audit` |
| 10. What An ODD Product Is | `#10-what-an-odd-product-is` |  | 1,464 | conserved; the application boundary block carried exactly; the `reference_frame_bases` meaning routed to REFERENCE_FRAME | `ODD.md#10-what-an-odd-product-is` |
| &nbsp;&nbsp;Product Specification (software-development topology) | `#product-specification-software-development-topology` |  | 281 | conserved | `ODD.md#product-specification-software-development-topology` |
| &nbsp;&nbsp;Product Realization (software-development topology) | `#product-realization-software-development-topology` |  | 280 | conserved | `ODD.md#product-realisation-software-development-topology` |
| &nbsp;&nbsp;ABG | `#abg` |  | 313 | conserved; all thirteen ABG ownerships | `ODD.md#abg` |
| &nbsp;&nbsp;ODD Product | `#odd-product` |  | 210 | conserved | `ODD.md#odd-product` |
| &nbsp;&nbsp;Query And Service Layers | `#query-and-service-layers` |  | 287 | conserved | `ODD.md#query-and-service-layers` |
| 11. Core Law | `#11-core-law` |  | 92 | conserved; the all-clauses condition | `ODD.md#11-core-law` |
| &nbsp;&nbsp;11.1 Typed Assets And Nodes Are Explicit | `#111-typed-assets-and-nodes-are-explicit` |  | 384 | conserved | `ODD.md#111-typed-assets-and-nodes-are-explicit` |
| &nbsp;&nbsp;11.2 Graph Functions Are The Primary Constructive Carrier | `#112-graph-functions-are-the-primary-constructive-carrier` |  | 366 | conserved | `ODD.md#112-graph-functions-are-the-primary-constructive-carrier` |
| &nbsp;&nbsp;11.2A Outcome-First Realization Order | `#112a-outcome-first-realization-order` |  | 1,502 | conserved | `ODD.md#112a-outcome-first-realisation-order` |
| &nbsp;&nbsp;11.3 The Function Catalog Is Published | `#113-the-function-catalog-is-published` |  | 311 | conserved; "at minimum" and "should" kept | `ODD.md#113-the-function-catalogue-is-published` |
| &nbsp;&nbsp;11.4 The GTL Module Is The Operative Publication Surface | `#114-the-gtl-module-is-the-operative-publication-surface` |  | 602 | conserved | `ODD.md#114-the-gtl-module-is-the-operative-publication-surface` |
| &nbsp;&nbsp;11.5 Current State Is A Projection Over Constructive History | `#115-current-state-is-a-projection-over-constructive-history` |  | 348 | conserved | `ODD.md#115-current-state-is-a-projection-over-constructive-history` |
| &nbsp;&nbsp;11.5A ABG Owns Continuation And Re-Entry | `#115a-abg-owns-continuation-and-re-entry` |  | 1,057 | conserved | `ODD.md#115a-abg-owns-continuation-and-re-entry` |
| &nbsp;&nbsp;11.5B Execution Authority Audit | `#115b-execution-authority-audit` |  | 3,352 | conserved; the five-surface inventory carried exactly; UP-016 keeps its rc.2 route, its successor home being the software-design profile | `ODD.md#115b-execution-authority-audit` |
| &nbsp;&nbsp;11.5C Projection-Source Coherence | `#115c-projection-source-coherence` |  | 1,078 | conserved | `ODD.md#115c-projection-source-coherence` |
| &nbsp;&nbsp;11.5D Constructive Evaluation And Yield Loop | `#115d-constructive-evaluation-and-yield-loop` |  | 23,882 | conserved in full; the authority chain, the sixteen-object table, the four-function table, every axiom block, the constitutional equation and its where-clause carried exactly; A0 to A16 as labelled paragraphs; UP-013 routed to SPEC_METHOD §3; Design Module Method written as the software-design profile | `ODD.md#115d-constructive-evaluation-and-yield-loop` |
| &nbsp;&nbsp;11.6 Product-Specific Semantics Sit Above The Shared Carrier | `#116-product-specific-semantics-sit-above-the-shared-carrier` |  | 363 | conserved | `ODD.md#116-product-specific-semantics-sit-above-the-shared-carrier` |
| &nbsp;&nbsp;11.7 Manual Walkthrough Must Still Be Lawful | `#117-manual-walkthrough-must-still-be-lawful` |  | 1,544 | conserved; "§5.2 and §5.3" written as §5 Vectors and Graph functions | `ODD.md#117-manual-walkthrough-must-still-be-lawful` |
| &nbsp;&nbsp;11.7A Conforming Agentic Development | `#117a-conforming-agentic-development` |  | 4,380 | conserved; SPEC_METHOD.md and TICKET_METHOD.md written as SPEC_METHOD and TICKETS | `ODD.md#117a-conforming-agentic-development` |
| &nbsp;&nbsp;11.7B Real Authority-Path Negative Proof (`STDO-UP-010`) | `#117b-real-authority-path-negative-proof-stdo-up-010` | UP-010 | 1,274 | conserved in full, with the supported-relation block carried exactly; this section is UP-010's only successor home | `ODD.md#117b-real-authority-path-negative-proof-stdo-up-010` |
| &nbsp;&nbsp;11.8 Cumulative Environment Law Is Mandatory | `#118-cumulative-environment-law-is-mandatory` |  | 559 | conserved; "mandatory", "should declare", "may require" and "structurally wrong" kept; ACTIVATION §4 states refinement in the chained form this law rejects (residual) | `ODD.md#118-cumulative-environment-law-is-mandatory` |
| &nbsp;&nbsp;11.9 Global Convergence Must Be Stable Under Zoom | `#119-global-convergence-must-be-stable-under-zoom` |  | 846 | conserved; "usually" kept | `ODD.md#119-global-convergence-must-be-stable-under-zoom` |
| 12. Scenario Rule | `#12-scenario-rule` |  | 649 | conserved | `ODD.md#12-scenario-rule` |
| 13. Installed-Dev Rule | `#13-installed-dev-rule` |  | 433 | conserved | `ODD.md#13-installed-dev-rule` |
| 14. Dogfooding Rule | `#14-dogfooding-rule` |  | 599 | conserved | `ODD.md#14-dogfooding-rule` |
| 15. Release Boundary | `#15-release-boundary` |  | 383 | conserved | `ODD.md#15-release-boundary` |
| 16. Failure Pattern | `#16-failure-pattern` |  | 1,849 | conserved; all fifteen patterns | `ODD.md#16-failure-pattern` |
| 17. Invocation Rule | `#17-invocation-rule` |  | 1,816 | conserved; all fourteen steps and the three exclusions | `ODD.md#17-invocation-rule` |
| 18. Cold-Start Reading Order | `#18-cold-start-reading-order` |  | 95 | conserved; "usually" kept | `ODD.md#18-cold-start-reading-order` |
| &nbsp;&nbsp;General ODD Product | `#general-odd-product` |  | 391 | conserved; nine steps with successor member names | `ODD.md#general-odd-product` |
| &nbsp;&nbsp;World-Model Product | `#world-model-product` |  | 789 | conserved; ten steps with successor member names | `ODD.md#world-model-product` |
| 19. Ramp-Up Checklist | `#19-ramp-up-checklist` |  | 1,293 | conserved; all fourteen questions | `ODD.md#19-ramp-up-checklist` |
| 20. Canonical Compression | `#20-canonical-compression` |  | 1,063 | conserved | `ODD.md#20-canonical-compression` |

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
| Canonical Compression | `#canonical-compression` |  | 1,658 | conserved | `REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit` |
| Position | `#position` |  | 1,445 | conserved | `REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit` |
| Core Claims | `#core-claims` |  | 1,196 | conserved | `REFERENCE_FRAME.md#2-core-claims` |
| Definitions | `#definitions` |  | 15 | not applicable: heading with no claim text (15 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Evaluation | `#evaluation` |  | 535 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Workspace | `#workspace` |  | 357 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Basis | `#basis` |  | 356 | conserved | `FOUNDATIONS.md#2-ontology` |
| &nbsp;&nbsp;Material relation | `#material-relation` |  | 371 | conserved | `FOUNDATIONS.md#2-ontology` |
| &nbsp;&nbsp;Material-relation manifold | `#material-relation-manifold` |  | 418 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Coordinate | `#coordinate` |  | 401 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Topology | `#topology` |  | 530 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Evidence | `#evidence` |  | 266 | conserved | `FOUNDATIONS.md#2-ontology` |
| &nbsp;&nbsp;Authority | `#authority` |  | 1,207 | conserved | `FOUNDATIONS.md#authority-kinds` |
| &nbsp;&nbsp;Disjointness And Independence | `#disjointness-and-independence` |  | 964 | conserved | `FOUNDATIONS.md#disjointness-and-independence` |
| &nbsp;&nbsp;Capability envelope | `#capability-envelope` |  | 439 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Reference frame | `#reference-frame` |  | 1,573 | conserved | `FOUNDATIONS.md#frame-objects; FOUNDATIONS.md#the-frame-tuple` |
| &nbsp;&nbsp;Activated frame | `#activated-frame` |  | 251 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Frame set | `#frame-set` |  | 343 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Active frame configuration | `#active-frame-configuration` |  | 309 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Lens | `#lens` |  | 382 | conserved | `FOUNDATIONS.md#frame-objects` |
| &nbsp;&nbsp;Role, persona, abstraction, and component | `#role-persona-abstraction-and-component` |  | 432 | conserved | `FOUNDATIONS.md#frame-objects` |
| Reference Frame Laws | `#reference-frame-laws` |  | 24 | not applicable: heading with no claim text (24 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;RF-001 Evaluation Relativity | `#rf-001-evaluation-relativity` | RF-001 | 171 | conserved | `REFERENCE_FRAME.md#rf-001-evaluation-relativity` |
| &nbsp;&nbsp;RF-002 Finite Attention | `#rf-002-finite-attention` | RF-002 | 298 | conserved | `REFERENCE_FRAME.md#rf-002-finite-attention` |
| &nbsp;&nbsp;RF-003 Material Sufficiency | `#rf-003-material-sufficiency` | RF-003 | 402 | conserved | `REFERENCE_FRAME.md#rf-003-material-sufficiency` |
| &nbsp;&nbsp;RF-004 Irrelevance Exclusion | `#rf-004-irrelevance-exclusion` | RF-004 | 245 | conserved | `REFERENCE_FRAME.md#rf-004-irrelevance-exclusion` |
| &nbsp;&nbsp;RF-005 Exact Basis And Coordinates | `#rf-005-exact-basis-and-coordinates` | RF-005 | 290 | conserved | `REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates` |
| &nbsp;&nbsp;RF-006 Authority Conservation | `#rf-006-authority-conservation` | RF-006 | 296 | conserved | `REFERENCE_FRAME.md#rf-006-authority-conservation` |
| &nbsp;&nbsp;RF-007 Semantic, Evidence, And Verdict Separation | `#rf-007-semantic-evidence-and-verdict-separation` | RF-007 | 436 | conserved | `REFERENCE_FRAME.md#rf-007-semantic-evidence-and-verdict-separation` |
| &nbsp;&nbsp;RF-008 Overlap Without Identity Collapse | `#rf-008-overlap-without-identity-collapse` | RF-008 | 289 | conserved | `REFERENCE_FRAME.md#rf-008-overlap-without-identity-collapse` |
| &nbsp;&nbsp;RF-009 No Assumed Hierarchy | `#rf-009-no-assumed-hierarchy` | RF-009 | 497 | conserved | `REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy` |
| &nbsp;&nbsp;RF-010 Composition On Demand | `#rf-010-composition-on-demand` | RF-010 | 429 | conserved | `REFERENCE_FRAME.md#rf-010-composition-on-demand` |
| &nbsp;&nbsp;RF-011 Topology Mutation And Recharting | `#rf-011-topology-mutation-and-recharting` | RF-011 | 286 | conserved | `REFERENCE_FRAME.md#rf-011-topology-mutation-and-recharting` |
| &nbsp;&nbsp;RF-012 Closed Results | `#rf-012-closed-results` | RF-012 | 623 | conserved | `REFERENCE_FRAME.md#rf-012-closed-results` |
| &nbsp;&nbsp;RF-013 Reconstructable Activation | `#rf-013-reconstructable-activation` | RF-013 | 275 | conserved | `REFERENCE_FRAME.md#rf-013-reconstructable-activation` |
| &nbsp;&nbsp;RF-014 Capability Fit | `#rf-014-capability-fit` | RF-014 | 317 | conserved | `REFERENCE_FRAME.md#rf-014-capability-fit` |
| &nbsp;&nbsp;RF-015 Residual Uncertainty | `#rf-015-residual-uncertainty` | RF-015 | 276 | conserved | `REFERENCE_FRAME.md#rf-015-residual-uncertainty` |
| &nbsp;&nbsp;RF-016 Implementation Neutrality | `#rf-016-implementation-neutrality` | RF-016 | 280 | conserved | `REFERENCE_FRAME.md#rf-016-implementation-neutrality` |
| &nbsp;&nbsp;RF-017 Proportional Compression | `#rf-017-proportional-compression` | RF-017 | 588 | conserved | `REFERENCE_FRAME.md#rf-017-proportional-compression` |
| &nbsp;&nbsp;Engagement Atom And Semantic Prime | `#engagement-atom-and-semantic-prime` |  | 784 | conserved | `REFERENCE_FRAME.md#engagement-atom-and-semantic-atom` |
| Human Frame-Set Declaration | `#human-frame-set-declaration` |  | 899 | conserved | `REFERENCE_FRAME.md#4-frame-set-declaration` |
| &nbsp;&nbsp;Frame-Set Optimization | `#frame-set-optimization` |  | 1,283 | conserved | `REFERENCE_FRAME.md#frame-set-selection` |
| Method Functions | `#method-functions` |  | 945 | conserved | `REFERENCE_FRAME.md#5-method-functions` |
| Engagement | `#engagement` |  | 14 | not applicable: heading with no claim text (14 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Establish The Evaluation Basis | `#establish-the-evaluation-basis` |  | 385 | conserved | `ACTIVATION.md#intake` |
| &nbsp;&nbsp;Applicability And Required Results | `#applicability-and-required-results` |  | 1,293 | conserved | `ACTIVATION.md#applicability` |
| &nbsp;&nbsp;Select And Activate | `#select-and-activate` |  | 521 | conserved | `ACTIVATION.md#2-context-construction-under-an-envelope` |
| &nbsp;&nbsp;Evaluate | `#evaluate` |  | 247 | conserved | `ACTIVATION.md#3-result-algebra` |
| &nbsp;&nbsp;Return A Closed Result | `#return-a-closed-result` |  | 878 | conserved | `ACTIVATION.md#7-closed-result-and-reuse` |
| &nbsp;&nbsp;Reconfigure When Necessary | `#reconfigure-when-necessary` |  | 527 | conserved | `ACTIVATION.md#4-totality-and-refinement` |
| Using Frames In Conjunction | `#using-frames-in-conjunction` |  | 93 | conserved | `REFERENCE_FRAME.md#6-frames-in-conjunction` |
| &nbsp;&nbsp;Independently Activated Co-Evaluation | `#independently-activated-co-evaluation` |  | 394 | conserved | `REFERENCE_FRAME.md#independently-activated-co-evaluation` |
| &nbsp;&nbsp;Result Conjunction | `#result-conjunction` |  | 733 | conserved | `REFERENCE_FRAME.md#result-conjunction` |
| &nbsp;&nbsp;Evidence Or Coordinate Translation | `#evidence-or-coordinate-translation` |  | 250 | conserved | `REFERENCE_FRAME.md#evidence-or-coordinate-translation` |
| &nbsp;&nbsp;Material Composition | `#material-composition` |  | 459 | conserved | `REFERENCE_FRAME.md#material-composition` |
| Frame Relations | `#frame-relations` |  | 1,131 | conserved | `REFERENCE_FRAME.md#7-frame-relations` |
| Workspace Coverage | `#workspace-coverage` |  | 22 | not applicable: heading with no claim text (22 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Coverage Basis | `#coverage-basis` |  | 404 | conserved | `REFERENCE_FRAME.md#coverage-basis` |
| &nbsp;&nbsp;Evaluation Inventory | `#evaluation-inventory` |  | 1,025 | conserved | `REFERENCE_FRAME.md#evaluation-inventory` |
| &nbsp;&nbsp;Coverage Dimensions | `#coverage-dimensions` |  | 518 | conserved | `REFERENCE_FRAME.md#coverage-dimensions` |
| &nbsp;&nbsp;Coverage Ledger | `#coverage-ledger` |  | 983 | conserved | `REFERENCE_FRAME.md#coverage-ledger` |
| &nbsp;&nbsp;Interaction Coverage | `#interaction-coverage` |  | 282 | conserved | `REFERENCE_FRAME.md#interaction-coverage` |
| &nbsp;&nbsp;Authority Coverage | `#authority-coverage` |  | 363 | conserved | `REFERENCE_FRAME.md#authority-coverage` |
| &nbsp;&nbsp;Failure Coverage | `#failure-coverage` |  | 279 | conserved | `REFERENCE_FRAME.md#failure-coverage` |
| &nbsp;&nbsp;High-Risk Separately Activated Coverage | `#high-risk-separately-activated-coverage` |  | 424 | conserved | `REFERENCE_FRAME.md#high-risk-separately-activated-coverage` |
| &nbsp;&nbsp;Operational Full Coverage | `#operational-full-coverage` |  | 905 | conserved | `REFERENCE_FRAME.md#operational-full-coverage` |
| Completeness Boundary | `#completeness-boundary` |  | 1,109 | conserved | `REFERENCE_FRAME.md#9-completeness-boundary` |
| Discovery And Revision | `#discovery-and-revision` |  | 26 | not applicable: heading with no claim text (26 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Missing-Frame Signals | `#missing-frame-signals` |  | 680 | conserved | `REFERENCE_FRAME.md#missing-frame-signals` |
| &nbsp;&nbsp;Diagnostic Order | `#diagnostic-order` |  | 496 | conserved | `REFERENCE_FRAME.md#diagnostic-order` |
| &nbsp;&nbsp;Revision Actions | `#revision-actions` |  | 604 | conserved | `REFERENCE_FRAME.md#revision-actions` |
| Agentic Use | `#agentic-use` |  | 1,143 | conserved | `REFERENCE_FRAME.md#11-the-activation-packet` |
| &nbsp;&nbsp;Minimal Frame Activation Binding | `#minimal-frame-activation-binding` |  | 1,458 | conserved | `REFERENCE_FRAME.md#minimal-activation-binding` |
| &nbsp;&nbsp;Worked Binding: Product-Chain Drift Evaluation | `#worked-binding-product-chain-drift-evaluation` |  | 4,368 | not applicable: a non-normative worked example by its own statement; it carries no determination beyond the binding shape, which is conserved at REFERENCE_FRAME.md#minimal-activation-binding; its subject (product-chain drift) is tier-2 matter and a successor worked binding is produced by a qualification case against the owning tier-2 member |  |
| Frame Qualification | `#frame-qualification` |  | 1,467 | conserved | `EVALUATION.md#frame-qualification` |
| &nbsp;&nbsp;Method Self-Qualification | `#method-self-qualification` |  | 3,430 | conserved | `EVALUATION.md#method-self-qualification` |
| Anti-Patterns | `#anti-patterns` |  | 1,485 | conserved | `REFERENCE_FRAME.md#12-violations` |
| Minimal Frame Declaration | `#minimal-frame-declaration` |  | 1,086 | conserved | `REFERENCE_FRAME.md#minimal-frame-declaration` |
| Minimal Frame-Set Declaration | `#minimal-frame-set-declaration` |  | 814 | conserved | `REFERENCE_FRAME.md#minimal-frame-set-declaration` |
| Minimal Evaluation Result | `#minimal-evaluation-result` |  | 417 | conserved | `REFERENCE_FRAME.md#minimal-evaluation-result` |
| Closure | `#closure` |  | 918 | conserved | `REFERENCE_FRAME.md#14-closure` |

## RELEASE_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Release-Publication Context | `#release-publication-context` |  | 329 | conserved | `RELEASE.md#1-context-and-position` |
| Position | `#position` |  | 1,357 | conserved | `RELEASE.md#1-context-and-position` |
| Release Identities | `#release-identities` |  | 1,168 | conserved; the generic release objects are restated in FOUNDATIONS §2 Release objects | `RELEASE.md#2-release-identities`; `FOUNDATIONS.md#product-lineage-objects` |
| Project-Qualified Git Refs | `#project-qualified-git-refs` |  | 1,529 | conserved | `RELEASE.md#project-qualified-git-refs` |
| Project-Subtree Release Identity | `#project-subtree-release-identity` |  | 1,479 | conserved | `RELEASE.md#project-subtree-release-identity` |
| Historical Ref And Public-URI Conservation | `#historical-ref-and-public-uri-conservation` |  | 1,251 | conserved | `RELEASE.md#historical-ref-and-public-uri-conservation` |
| Phases | `#phases` |  | 619 | conserved | `RELEASE.md#3-phases` |
| Mutable Candidate Construction | `#mutable-candidate-construction` |  | 541 | conserved | `RELEASE.md#mutable-candidate-construction` |
| Immutable RC Publication | `#immutable-rc-publication` |  | 1,563 | conserved | `RELEASE.md#immutable-rc-publication` |
| Exact-Cut Qualification | `#exact-cut-qualification` |  | 1,117 | conserved | `RELEASE.md#exact-cut-qualification` |
| Monotonic Version-Line Advancement | `#monotonic-version-line-advancement` |  | 1,429 | conserved | `RELEASE.md#monotonic-version-line-advancement` |
| Selector And Consumer Adoption | `#selector-and-consumer-adoption` |  | 2,440 | conserved; the plan object, its hashing and the manager commands are defined once in PRODUCT_DEFINITION §4 | `RELEASE.md#4-selector-and-consumer-adoption`; `PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager` |
| Naming | `#naming` |  | 898 | conserved | `RELEASE.md#5-naming` |
| Release-Scoped Assets | `#release-scoped-assets` |  | 804 | conserved | `RELEASE.md#release-scoped-assets` |
| Coordinated Release-Matched Asset Cohorts | `#coordinated-release-matched-asset-cohorts` |  | 2,089 | conserved | `RELEASE.md#7-coordinated-release-matched-asset-cohorts` |
| &nbsp;&nbsp;Two-Commit Construction And One Publication Transaction | `#two-commit-construction-and-one-publication-transaction` |  | 2,527 | conserved | `RELEASE.md#two-commit-construction-and-one-publication-transaction` |
| &nbsp;&nbsp;Qualification And Recovery | `#qualification-and-recovery` |  | 1,410 | conserved | `RELEASE.md#qualification-and-recovery` |
| Product Subject And Repository Carrier | `#product-subject-and-repository-carrier` |  | 836 | conserved | `RELEASE.md#product-subject-and-repository-carrier` |
| Acceptance Criteria | `#acceptance-criteria` |  | 748 | conserved | `RELEASE.md#acceptance-criteria` |
| External Qualification Dependencies | `#external-qualification-dependencies` |  | 537 | conserved | `RELEASE.md#external-qualification-dependencies` |
| Successor Baseline Conservation (`STDO-UP-015`) | `#successor-baseline-conservation-stdo-up-015` | UP-015 | 1,185 | conserved in full; applied to this corpus in FOUNDATIONS §1 and to acceptance evidence in EVALUATION §5 | `RELEASE.md#9-successor-baseline-conservation-stdo-up-015`; `FOUNDATIONS.md#1-vocabulary-of-standing`; `EVALUATION.md#5-acceptance` |
| Open Questions | `#open-questions` |  | 191 | conserved; both questions carried as open | `RELEASE.md#10-open-questions` |

## SPEC_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Canonical Compression | `#canonical-compression` |  | 2,678 | conserved; restated as the canonical statement with each clause's owning section named | `SPEC_METHOD.md#canonical-statement` |
| Position | `#position` |  | 574 | conserved | `SPEC_METHOD.md#position` |
| STDO Method Identity | `#stdo-method-identity` |  | 836 | conserved; the bounded-context identity is carried unchanged; the owners of T, D and O are named by successor member | `SPEC_METHOD.md#method-identity` |
| Probabilistic Work Boundary | `#probabilistic-work-boundary` |  | 1,499 | conserved; restated as the work-boundary object and P0's boundary commitment; the profile binding to one traversal is generalised and kept by PROFILES §2 | `FOUNDATIONS.md#work-boundary`; `FOUNDATIONS.md#3-commitments` |
| Recursive Product Taxonomy | `#recursive-product-taxonomy` |  | 2,924 | conserved; the eight objects with their concept identities, the six governing rules, the compiler analogy and the load-bearing claim restated as ontology | `FOUNDATIONS.md#product-lineage-objects`; applied at `SPEC_METHOD.md#6-lineage-and-release` |
| Manifesto | `#manifesto` |  | 1,738 | conserved | `SPEC_METHOD.md#manifesto` |
| Spec-Drivenness Litmus | `#spec-drivenness-litmus` |  | 1,316 | conserved; all thirteen conditions | `SPEC_METHOD.md#spec-drivenness-litmus` |
| Process Constitution | `#process-constitution` |  | 2,563 | conserved; the definition overlay's binding is at PRODUCT_DEFINITION §1 and §8 | `SPEC_METHOD.md#process-constitution` |
| STDO Product Definition Overlay And Layout Independence | `#stdo-product-definition-overlay-and-layout-independence` |  | 2,941 | conserved; the product-definition-routing bounded context is owned by PRODUCT_DEFINITION rather than SPEC_METHOD; `IDENTITY_METHOD.md` carried as the IDENTITY member | `PRODUCT_DEFINITION.md#1-overlay-and-layout-independence` |
| &nbsp;&nbsp;Required Definition Relations | `#required-definition-relations` |  | 2,033 | conserved | `PRODUCT_DEFINITION.md#2-required-definition-relations` |
| &nbsp;&nbsp;Constitutional-Set Sufficiency | `#constitutional-set-sufficiency` |  | 1,964 | conserved; "Design Module Method Ontology" carried as the design profile's accepted design ontology of a realisation boundary | `PRODUCT_DEFINITION.md#3-constitutional-set-sufficiency` |
| &nbsp;&nbsp;Shared Installed Release Basis And Toolchain Manager | `#shared-installed-release-basis-and-toolchain-manager` |  | 6,894 | conserved in full (basis pair, manifest binding, adoption and fleet plans, hashing rule, seven manager functions, store and registry law, physical-entry rule, selector and basis fields, six command boundaries, fail-closed list, schema-locator rule, agent bootstrap marker law, exact prune list); `RELEASE_METHOD.md` carried as the RELEASE member | `PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager` |
| &nbsp;&nbsp;&nbsp;&nbsp;Explicit Complete Consumer Update | `#explicit-complete-consumer-update` |  | 3,276 | conserved in full | `PRODUCT_DEFINITION.md#explicit-complete-consumer-update` |
| &nbsp;&nbsp;Bounded-Context Semantic Resolution | `#bounded-context-semantic-resolution` |  | 4,717 | conserved; the semantic-resolution bounded context is owned by PRODUCT_DEFINITION; `GLOSSARY_GUIDE.md` carried as the GLOSSARY member; relation kinds related to AC-012 without redefinition | `PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution` |
| &nbsp;&nbsp;Local Constitutional Binding | `#local-constitutional-binding` |  | 1,508 | conserved | `PRODUCT_DEFINITION.md#6-local-constitutional-binding` |
| &nbsp;&nbsp;Collective Reference-Frame Basis | `#collective-reference-frame-basis` |  | 4,713 | conserved; `REFERENCE_FRAME_METHOD.md` carried as REFERENCE_FRAME and `STDO_REFERENCE_FRAME_BASELINE.md` as the Executive baseline profile member; the activation packet and the step are pointed to REFERENCE_FRAME §11 and ACTIVATION §1 | `PRODUCT_DEFINITION.md#7-collective-reference-frame-basis` |
| &nbsp;&nbsp;WHAT, HOW, And Work Carriers | `#what-how-and-work-carriers` |  | 1,822 | conserved; the build-tenancy bounded context is owned by PRODUCT_DEFINITION; the generic WHAT/HOW law is SPEC_METHOD §2 and carrier selection SPEC_METHOD §4 and TICKETS | `PRODUCT_DEFINITION.md#8-what-how-and-work-carriers` |
| &nbsp;&nbsp;Recursive Discovery And Explicit Composition | `#recursive-discovery-and-explicit-composition` |  | 3,173 | conserved | `PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition` |
| &nbsp;&nbsp;Semantic-Resolution Conformance Cases | `#semantic-resolution-conformance-cases` |  | 1,669 | conserved; "Reference Frame Method evaluation context" carried as the reference-frame-evaluation bounded context of REFERENCE_FRAME §1 | `PRODUCT_DEFINITION.md#10-semantic-resolution-conformance-cases` |
| One Constitutional Surface And Version Boundary (`STDO-SURFACE-001`) | `#one-constitutional-surface-and-version-boundary-stdo-surface-001` | STDO-SURFACE-001 | 2,041 | conserved; "standard" carried as "member" | `PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary` |
| Constitutional Chain | `#constitutional-chain` |  | 4,052 | conserved; the WHAT and HOW bindings are at PRODUCT_DEFINITION §8 | `SPEC_METHOD.md#constitutional-chain` |
| Sprint Execution Boundary | `#sprint-execution-boundary` |  | 2,635 | conserved; sprint and ticket mechanics at TICKETS | `SPEC_METHOD.md#sprint-execution-boundary` |
| Ambiguity Governance Rule | `#ambiguity-governance-rule` |  | 3,434 | conserved; the bounded-context and concept identities carried unchanged; the ambiguity outcome refinement is ACTIVATION §3 and the hard stops ACTIVATION §4; the profile shorthands named are generalised to "a profile's runtime shorthands" | `SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle` |
| Operational Lifecycle Sufficiency Rule | `#operational-lifecycle-sufficiency-rule` |  | 1,889 | conserved | `SPEC_METHOD.md#operational-lifecycle-sufficiency` |
| Change Management Rule | `#change-management-rule` |  | 174 | conserved | `SPEC_METHOD.md#4-change-management` |
| &nbsp;&nbsp;Universal Intake Triage | `#universal-intake-triage` |  | 3,368 | conserved; the six determinations, the triangulation across frames, the smallest sufficient configuration, the six classes with their re-entry and flows, the below-Goals assertion and the drift rule | `SPEC_METHOD.md#universal-intake-triage`; `SPEC_METHOD.md#change-classes` |
| &nbsp;&nbsp;Computed Classification And Treatment | `#computed-classification-and-treatment` |  | 4,857 | conserved; C, J and O, the producer and its output fields, the four-step ordered walk, the nonconformance rule, unknown treatment, retry and reuse restored in full | `SPEC_METHOD.md#computed-classification-and-treatment` |
| Consistency Gate Rule | `#consistency-gate-rule` |  | 1,199 | conserved | `SPEC_METHOD.md#consistency-gate` |
| Product Outcome Conservation (`STDO-UP-013`) | `#product-outcome-conservation-stdo-up-013` | UP-013 | 4,432 | conserved in full; the acceptance interval is also EVALUATION §5 and the outcome object FOUNDATIONS §2; "Prime" generalised to "the prime law of a design profile" | `SPEC_METHOD.md#3-outcome-conservation` |
| Proportional Method And Delivery (`STDO-UP-014`) | `#proportional-method-and-delivery-stdo-up-014` | UP-014 | 4,218 | conserved; the relation, effective reasoning complexity, the constraint test, the symbolic-design paragraph, the disproportion test and the method's own execution in ACTIVATION §6; the delivery priority in SPEC_METHOD §8; "Ontology, IACS, Prime" generalised to "a detailed algebra or semantic design view" | `ACTIVATION.md#6-cost-and-proportionality`; `SPEC_METHOD.md#8-bounded-execution-in-this-method` |
| Agentic Construction Execution (`STDO-UP-020`) | `#agentic-construction-execution-stdo-up-020` | UP-020 | 696 | conserved; the normative relation and the non-prescription of worker internals; SPEC_METHOD §8 binds the generic terms to the product outcome | `ACTIVATION.md#1-the-step` |
| &nbsp;&nbsp;Sufficient Execution Intake | `#sufficient-execution-intake` |  | 937 | conserved; all six intake items; the design-profile input laws consumed by reference to PROFILES §3 | `ACTIVATION.md#intake` |
| &nbsp;&nbsp;Bounded Causal Construction | `#bounded-causal-construction` |  | 540 | conserved | `ACTIVATION.md#execution-unit` |
| &nbsp;&nbsp;Construction, Assessment, And Delegation | `#construction-assessment-and-delegation` |  | 2,253 | conserved; "Executive" written "coordinating role" in tier 1; the proxy limits also at EVALUATION §5 | `ACTIVATION.md#roles-and-delegation` |
| &nbsp;&nbsp;Proportional Disposition | `#proportional-disposition` |  | 1,114 | conserved; the four dispositions with conditions, global correctness and the repeated-rejection rule | `ACTIVATION.md#disposition` |
| &nbsp;&nbsp;Transition Evidence And Proof Cadence | `#transition-evidence-and-proof-cadence` |  | 977 | conserved | `ACTIVATION.md#transition-evidence` |
| &nbsp;&nbsp;Checkpoint, Continuation, Progress, And Churn | `#checkpoint-continuation-progress-and-churn` |  | 1,744 | conserved; checkpoint, preservation checkpoint fields, restart, the progress categories and the six falsifiers; "Product" written "the selected outcome" in tier 1 | `ACTIVATION.md#5-work-state-and-restart` |
| Complete Enclosing-Relation Admission (`STDO-UP-021`) | `#complete-enclosing-relation-admission-stdo-up-021` | UP-021 | 3,070 | conserved in full | `ACTIVATION.md#complete-enclosing-relation-admission` |
| &nbsp;&nbsp;Standing Structural Qualification | `#standing-structural-qualification` |  | 2,842 | conserved; all ten forms with their required observations | `ACTIVATION.md#standing-structural-qualification` |
| Core Interface Migration Rule | `#core-interface-migration-rule` |  | 1,302 | conserved | `SPEC_METHOD.md#core-interface-migration` |
| &nbsp;&nbsp;Constitutional Migration Options | `#constitutional-migration-options` |  | 4,436 | conserved | `SPEC_METHOD.md#constitutional-migration-options` |
| &nbsp;&nbsp;What Counts As A Core Interface | `#what-counts-as-a-core-interface` |  | 445 | conserved | `SPEC_METHOD.md#what-counts-as-a-core-interface` |
| &nbsp;&nbsp;Required Migration Protocol | `#required-migration-protocol` |  | 802 | conserved | `SPEC_METHOD.md#required-migration-protocol` |
| &nbsp;&nbsp;Bridge Prohibition | `#bridge-prohibition` |  | 758 | conserved | `SPEC_METHOD.md#bridge-prohibition` |
| &nbsp;&nbsp;Projection Discipline | `#projection-discipline` |  | 593 | conserved | `SPEC_METHOD.md#projection-discipline` |
| &nbsp;&nbsp;Inside-Out First Sequencing | `#inside-out-first-sequencing` |  | 1,012 | conserved | `SPEC_METHOD.md#inside-out-first-sequencing` |
| &nbsp;&nbsp;Hard-Break Discipline | `#hard-break-discipline` |  | 1,155 | conserved | `SPEC_METHOD.md#hard-break-discipline` |
| &nbsp;&nbsp;Proof-Last Rule For Core Interface Changes | `#proof-last-rule-for-core-interface-changes` |  | 717 | conserved | `SPEC_METHOD.md#proof-last-rule` |
| &nbsp;&nbsp;Closure Criterion | `#closure-criterion` |  | 1,661 | conserved; the retention relation is cited by live surface immutability | `SPEC_METHOD.md#closure-criterion` |
| Release Version Boundary | `#release-version-boundary` |  | 875 | conserved; release mechanics stay with RELEASE, carried by provenance until that member exists | `SPEC_METHOD.md#6-lineage-and-release` |
| Evidence Rules | `#evidence-rules` |  | 96 | not applicable: heading with no claim beyond naming its three children (96 bytes), which are disposed individually | `SPEC_METHOD.md#9-evidence` |
| &nbsp;&nbsp;Proof Target Identity And Adequacy (`STDO-UP-001`) | `#proof-target-identity-and-adequacy-stdo-up-001` | UP-001 | 594 | conserved; the six named relations and the weaker-property rule including release proof | `EVALUATION.md#1-claims` |
| &nbsp;&nbsp;Semantic, Evidence, And Projection Separation (`STDO-UP-008`) | `#semantic-evidence-and-projection-separation-stdo-up-008` | UP-008 | 727 | conserved; the three bases, the three invalidation cases and the digest rule | `EVALUATION.md#2-separation` |
| &nbsp;&nbsp;Assurance-Boundary Congruence And Method Qualification (`STDO-UP-022`) | `#assurance-boundary-congruence-and-method-qualification-stdo-up-022` | UP-022 | 5,342 | conserved in full; boundary congruence, mechanical enforcement and the quantifier rule in §1, freeze and post-exposure revision in §3, the comparison rule in §6, the qualification protocol, derived guidance and the falsifiers in §7 | `EVALUATION.md#1-claims`; `EVALUATION.md#3-independent-assessment`; `EVALUATION.md#6-conformance-of-realisations`; `EVALUATION.md#method-self-qualification` |
| Verification Layers | `#verification-layers` |  | 1,477 | conserved; the profile-flavoured example (compositional graphs, Fragment types, discovery workflow) generalised to a reusable composable unit | `ASSURANCE.md#1-verification-layers` |
| Testing Strategy Taxonomy | `#testing-strategy-taxonomy` |  | 4,014 | conserved in full (both authority sources, sandbox-only UAT, harnessed and live modes, necessary-not-sufficient rule, terminology list); the product-assurance bounded context is owned by ASSURANCE; `DESIGN_MODULE_METHOD.md` carried as the DESIGN_MODULE member and "IACS" as the carrier inventory the design declares | `ASSURANCE.md#2-testing-strategy-taxonomy` |
| &nbsp;&nbsp;Fixture And Proof Portability Rule | `#fixture-and-proof-portability-rule` |  | 829 | conserved | `ASSURANCE.md#fixture-and-proof-portability` |
| Test Authority Rule | `#test-authority-rule` |  | 470 | conserved | `ASSURANCE.md#3-test-authority` |
| Scenario Bundle Rule | `#scenario-bundle-rule` |  | 969 | conserved | `ASSURANCE.md#4-scenario-bundle` |
| Installed Dev Proof Rule | `#installed-dev-proof-rule` |  | 619 | conserved | `ASSURANCE.md#5-installed-dev-proof` |
| Significant Path Coverage Rule | `#significant-path-coverage-rule` |  | 659 | conserved | `ASSURANCE.md#6-significant-path-coverage` |
| Requirement Categories | `#requirement-categories` |  | 1,790 | conserved | `SPEC_METHOD.md#requirement-categories-and-classification` |
| Reconstruction Litmus | `#reconstruction-litmus` |  | 2,684 | conserved; the generic layered-sufficiency law in EVALUATION §6, the five layer derivations and the per-layer diagnoses in SPEC_METHOD §2; the design-view coverage gate stays with the design profile | `EVALUATION.md#6-conformance-of-realisations`; `SPEC_METHOD.md#reconstruction-litmus` |
| Design Rule | `#design-rule` |  | 864 | conserved | `SPEC_METHOD.md#design-rule` |
| Renewal Path | `#renewal-path` |  | 1,504 | conserved | `SPEC_METHOD.md#renewal-path` |
| Trace Closure And Anti-Drift Rule | `#trace-closure-and-anti-drift-rule` |  | 101 | conserved | `SPEC_METHOD.md#trace-closure-and-anti-drift` |
| &nbsp;&nbsp;Ownership | `#ownership` |  | 206 | conserved | `SPEC_METHOD.md#trace-closure-and-anti-drift` |
| &nbsp;&nbsp;Downstream Closure | `#downstream-closure` |  | 709 | conserved | `SPEC_METHOD.md#trace-closure-and-anti-drift` |
| &nbsp;&nbsp;Drift Signals | `#drift-signals` |  | 1,397 | conserved; all ten signals | `SPEC_METHOD.md#trace-closure-and-anti-drift` |
| Live Surface Immutability | `#live-surface-immutability` |  | 1,091 | conserved | `SPEC_METHOD.md#live-surface-immutability` |
| Fundamental Migration Rule | `#fundamental-migration-rule` |  | 3,159 | conserved; the eight rules, three classifications, seven steps and three migration conditions | `SPEC_METHOD.md#fundamental-migration` |
| Transformation Wave Rule | `#transformation-wave-rule` |  | 1,485 | conserved | `SPEC_METHOD.md#transformation-wave` |
| Legacy Classification Rule | `#legacy-classification-rule` |  | 786 | conserved | `SPEC_METHOD.md#requirement-categories-and-classification` |
| Requirement Classification Rules | `#requirement-classification-rules` |  | 769 | conserved | `SPEC_METHOD.md#requirement-categories-and-classification` |
| Specification Surface Rule | `#specification-surface-rule` |  | 2,539 | conserved | `SPEC_METHOD.md#specification-surface-rule` |
| Bootstrap Rule | `#bootstrap-rule` |  | 6,674 | conserved in full (scaffold bindings, authority split, singular-authority rule, folder shape, requirement sources, fourteen-step sequence); the predecessor's own mutable source path is generalised to the method's source workspace | `PRODUCT_DEFINITION.md#12-bootstrap` |
| Method | `#method` |  | 4,613 | conserved; the four procedures in full; the design-module co-evolution predicate named without its symbol | `SPEC_METHOD.md#procedures` |
| ADR Conventions | `#adr-conventions` |  | 910 | conserved | `SPEC_METHOD.md#10-design-records` |
| &nbsp;&nbsp;ADR Folder Convention | `#adr-folder-convention` |  | 1,692 | conserved | `SPEC_METHOD.md#10-design-records` |

## STDO_REFERENCE_FRAME_BASELINE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Canonical Compression | `#canonical-compression` |  | 3,571 | conserved; the testing-frame evidence topology is stated with the testing frames | `EXECUTIVE_BASELINE.md#1-canonical-compression`; `ASSURANCE.md#the-set` |
| Status And Authority Boundary | `#status-and-authority-boundary` |  | 4,292 | conserved; the ownership table is rewritten onto tenant members | `EXECUTIVE_BASELINE.md#2-status-and-authority-boundary` |
| Engagement Applicability | `#engagement-applicability` |  | 1,767 | conserved; direct entry itself is ACTIVATION §1 Roles and delegation, the profile additions are restated here | `EXECUTIVE_BASELINE.md#3-engagement-applicability` |
| Empirical Revision Boundary | `#empirical-revision-boundary` |  | 1,789 | conserved | `EXECUTIVE_BASELINE.md#4-empirical-revision-boundary` |
| Profile Terms | `#profile-terms` |  | 17 | not applicable: heading with no claim text (17 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Engagement frame | `#engagement-frame` |  | 258 | conserved | `EXECUTIVE_BASELINE.md#engagement-frame` |
| &nbsp;&nbsp;Specialist frame | `#specialist-frame` |  | 407 | conserved | `EXECUTIVE_BASELINE.md#specialist-frame` |
| &nbsp;&nbsp;Generic specialist-frame family | `#generic-specialist-frame-family` |  | 699 | conserved | `EXECUTIVE_BASELINE.md#generic-specialist-frame-family` |
| &nbsp;&nbsp;Testing frame | `#testing-frame` |  | 562 | conserved; defined in tier 2 because the testing frames use it | `ASSURANCE.md#terms` |
| &nbsp;&nbsp;Authoritative Product path | `#authoritative-product-path` |  | 504 | conserved; defined in tier 2 because the testing frames use it | `ASSURANCE.md#terms` |
| &nbsp;&nbsp;Material combinatorial complexity | `#material-combinatorial-complexity` |  | 691 | conserved; defined in tier 2 because the testing frames use it | `ASSURANCE.md#terms` |
| &nbsp;&nbsp;Executive | `#executive` |  | 630 | conserved | `EXECUTIVE_BASELINE.md#executive` |
| Executive Attention, Evaluation, And Action | `#executive-attention-evaluation-and-action` |  | 3,774 | conserved; three duties, no-mutation rule, attention cycle | `EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action` |
| &nbsp;&nbsp;Event-Driven Executive Attention | `#event-driven-executive-attention` |  | 1,749 | conserved | `EXECUTIVE_BASELINE.md#event-driven-attention` |
| &nbsp;&nbsp;Executive Drift Locks | `#executive-drift-locks` |  | 1,307 | conserved; the five locks as a table with their failure consequences | `EXECUTIVE_BASELINE.md#drift-locks` |
| &nbsp;&nbsp;Product-Chain Basis | `#product-chain-basis` |  | 1,435 | conserved; the role map in the basis is PRODUCT_DEFINITION §7 | `EXECUTIVE_BASELINE.md#product-chain-basis` |
| &nbsp;&nbsp;Worker | `#worker` |  | 346 | conserved | `EXECUTIVE_BASELINE.md#worker` |
| &nbsp;&nbsp;Reviewer | `#reviewer` |  | 444 | conserved | `EXECUTIVE_BASELINE.md#reviewer` |
| &nbsp;&nbsp;Technical triage, severity, priority, and boundary effect | `#technical-triage-severity-priority-and-boundary-effect` |  | 1,947 | conserved; severity, priority, frame result and boundary effect kept distinct; the per-result projection is EVALUATION §4 | `EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect` |
| &nbsp;&nbsp;Work result | `#work-result` |  | 2,021 | conserved; the total mapping is ACTIVATION §3 construction availability, the variant readings and refusal exclusion restated here | `EXECUTIVE_BASELINE.md#work-result` |
| &nbsp;&nbsp;Exact candidate | `#exact-candidate` |  | 551 | conserved | `EXECUTIVE_BASELINE.md#exact-candidate` |
| &nbsp;&nbsp;Baseline-adoption projection | `#baseline-adoption-projection` |  | 492 | conserved | `EXECUTIVE_BASELINE.md#baseline-adoption-projection` |
| Non-Hierarchical Frame Configuration | `#non-hierarchical-frame-configuration` |  | 1,391 | conserved | `EXECUTIVE_BASELINE.md#7-non-hierarchical-frame-configuration` |
| Derived Executive Frame | `#derived-executive-frame` |  | 3,017 | conserved; eleven-element table | `EXECUTIVE_BASELINE.md#8-derived-executive-frame` |
| &nbsp;&nbsp;Steel-Thread Delivery | `#steel-thread-delivery` |  | 1,827 | conserved | `EXECUTIVE_BASELINE.md#steel-thread-delivery` |
| Derived Worker Frame | `#derived-worker-frame` |  | 2,854 | conserved; eleven-element table | `EXECUTIVE_BASELINE.md#9-derived-worker-frame` |
| Derived Reviewer Frame | `#derived-reviewer-frame` |  | 4,236 | conserved; eleven-element table | `EXECUTIVE_BASELINE.md#10-derived-reviewer-frame` |
| Derived Generic Specialist Frame Set | `#derived-generic-specialist-frame-set` |  | 10,024 | conserved; all twelve families as a table | `EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set` |
| Derived Product Testing Frame Set | `#derived-product-testing-frame-set` |  | 1,395 | conserved; the set in tier 2, its relation to the Proof family in the profile | `ASSURANCE.md#the-set`; `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames` |
| &nbsp;&nbsp;Derived User-Acceptance Frame | `#derived-user-acceptance-frame` |  | 3,431 | conserved | `ASSURANCE.md#user-acceptance-frame` |
| &nbsp;&nbsp;Derived End-To-End Frame | `#derived-end-to-end-frame` |  | 2,767 | conserved | `ASSURANCE.md#end-to-end-frame` |
| &nbsp;&nbsp;Derived Integration Frame | `#derived-integration-frame` |  | 2,522 | conserved | `ASSURANCE.md#integration-frame` |
| &nbsp;&nbsp;Derived Unit-Test Frame | `#derived-unit-test-frame` |  | 4,046 | conserved | `ASSURANCE.md#unit-frame` |
| &nbsp;&nbsp;Combinatorial Coverage And Testing-Value Index | `#combinatorial-coverage-and-testing-value-index` |  | 2,916 | conserved | `ASSURANCE.md#8-combinatorial-coverage-and-testing-value` |
| &nbsp;&nbsp;Legitimate-Path And Technical-Debt Erasure | `#legitimate-path-and-technical-debt-erasure` |  | 2,528 | conserved | `ASSURANCE.md#9-legitimate-path-and-technical-debt-erasure` |
| &nbsp;&nbsp;Testing Evidence Composition | `#testing-evidence-composition` |  | 1,186 | conserved | `ASSURANCE.md#10-testing-evidence-composition` |
| &nbsp;&nbsp;Assurance Subject Acquisition And Evaluation | `#assurance-subject-acquisition-and-evaluation` |  | 1,609 | conserved | `ASSURANCE.md#11-assurance-subject-acquisition-and-evaluation` |
| &nbsp;&nbsp;Counterexample Localization | `#counterexample-localization` |  | 1,327 | conserved | `ASSURANCE.md#12-counterexample-localisation` |
| Derived End-To-End Interface Integration Frame | `#derived-end-to-end-interface-integration-frame` |  | 4,400 | conserved; frame identity unchanged, resolving in the reference-frame-evaluation context; its family relation in the profile | `ASSURANCE.md#13-end-to-end-interface-integration-frame`; `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames` |
| &nbsp;&nbsp;Interface Integration Claim Boundaries | `#interface-integration-claim-boundaries` |  | 1,665 | conserved | `ASSURANCE.md#claim-boundaries` |
| &nbsp;&nbsp;Interface Integration Obligations | `#interface-integration-obligations` |  | 5,074 | conserved | `ASSURANCE.md#obligations` |
| &nbsp;&nbsp;Computational Whole-Path Evaluation | `#computational-whole-path-evaluation` |  | 1,244 | conserved; the family names of the composition in the profile | `ASSURANCE.md#computational-whole-path-evaluation`; `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames` |
| &nbsp;&nbsp;Interface Integration Qualification | `#interface-integration-qualification` |  | 2,144 | conserved; all ten cases | `ASSURANCE.md#qualification` |
| Complete Engagement Transition | `#complete-engagement-transition` |  | 343 | conserved | `EXECUTIVE_BASELINE.md#12-complete-engagement-transition` |
| &nbsp;&nbsp;1. Existing Authority Selects The Basis | `#1-existing-authority-selects-the-basis` |  | 280 | conserved | `EXECUTIVE_BASELINE.md#1-existing-authority-selects-the-basis` |
| &nbsp;&nbsp;2. Executive Activates Worker | `#2-executive-activates-worker` |  | 1,192 | conserved | `EXECUTIVE_BASELINE.md#2-executive-activates-worker` |
| &nbsp;&nbsp;3. Worker Returns To Executive | `#3-worker-returns-to-executive` |  | 888 | conserved | `EXECUTIVE_BASELINE.md#3-worker-returns-to-executive` |
| &nbsp;&nbsp;4. Executive Evaluates The Work Result | `#4-executive-evaluates-the-work-result` |  | 848 | conserved | `EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result` |
| &nbsp;&nbsp;5A. Candidate Does Not Require Independent Review | `#5a-candidate-does-not-require-independent-review` |  | 405 | conserved | `EXECUTIVE_BASELINE.md#5a-candidate-does-not-require-independent-review` |
| &nbsp;&nbsp;5B. Candidate Requires Independent Review | `#5b-candidate-requires-independent-review` |  | 843 | conserved | `EXECUTIVE_BASELINE.md#5b-candidate-requires-independent-review` |
| &nbsp;&nbsp;6. Reviewer Returns To Executive | `#6-reviewer-returns-to-executive` |  | 644 | conserved | `EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive` |
| &nbsp;&nbsp;Reviewer Result And Triage Projection | `#reviewer-result-and-triage-projection` |  | 2,199 | conserved; tier-1 law with assessor and decision owner | `EVALUATION.md#result-and-triage-projection`; `EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive` |
| &nbsp;&nbsp;7. Executive Disposes And Checkpoints | `#7-executive-disposes-and-checkpoints` |  | 1,134 | conserved | `EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints` |
| &nbsp;&nbsp;Executive Promotion Constraint Projection | `#executive-promotion-constraint-projection` |  | 801 | conserved; all four rows | `EXECUTIVE_BASELINE.md#promotion-constraint-projection` |
| Handoff Projection | `#handoff-projection` |  | 2,964 | conserved; all eight projections | `EXECUTIVE_BASELINE.md#13-handoff-projection` |
| Coverage Application | `#coverage-application` |  | 3,905 | conserved; all fourteen rows | `EXECUTIVE_BASELINE.md#14-coverage-application` |
| Missing-Frame And Re-Entry Application | `#missing-frame-and-re-entry-application` |  | 997 | conserved; REFERENCE_FRAME §10 order with the two profile-specific steps stated | `EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application` |
| Product-Owned Adoption Or Project-Defined Configuration | `#product-owned-adoption-or-project-defined-configuration` |  | 59 | not applicable: heading with no claim text (59 bytes); its children are disposed individually |  |
| &nbsp;&nbsp;Existing Authority Selects The Configuration | `#existing-authority-selects-the-configuration` |  | 767 | conserved | `EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration` |
| &nbsp;&nbsp;Adopt This Baseline | `#adopt-this-baseline` |  | 1,157 | conserved | `EXECUTIVE_BASELINE.md#adopt-this-baseline` |
| &nbsp;&nbsp;Define A Project Configuration | `#define-a-project-configuration` |  | 1,154 | conserved | `EXECUTIVE_BASELINE.md#define-a-project-configuration` |
| &nbsp;&nbsp;Extension Versus Replacement | `#extension-versus-replacement` |  | 555 | conserved | `EXECUTIVE_BASELINE.md#extension-versus-replacement` |
| Actor Binding And Independence | `#actor-binding-and-independence` |  | 861 | conserved | `EXECUTIVE_BASELINE.md#17-actor-binding-and-independence` |
| Profile Qualification | `#profile-qualification` |  | 5,304 | conserved; all twenty-six trial obligations | `EXECUTIVE_BASELINE.md#18-profile-qualification` |
| Baseline-Specific Project-Basis Additions | `#baseline-specific-project-basis-additions` |  | 1,192 | conserved | `EXECUTIVE_BASELINE.md#project-basis-additions` |
| Baseline-Specific Activation Additions | `#baseline-specific-activation-additions` |  | 887 | conserved | `EXECUTIVE_BASELINE.md#activation-additions` |
| Failure Classification | `#failure-classification` |  | 4,272 | conserved; all twenty-eight rows | `EXECUTIVE_BASELINE.md#20-failure-classification` |
| Anti-Patterns | `#anti-patterns` |  | 3,945 | conserved; all thirty-two | `EXECUTIVE_BASELINE.md#21-anti-patterns` |
| Closure | `#closure` |  | 5,131 | conserved; all twenty-four conditions | `EXECUTIVE_BASELINE.md#22-closure` |

## TICKET_METHOD.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Core Model | `#core-model` |  | 14 | not applicable: heading with no claim text (14 bytes); its children are disposed individually | `TICKETS.md#1-work-carriers` |
| &nbsp;&nbsp;Goals | `#goals` |  | 336 | conserved | `TICKETS.md#goals` |
| &nbsp;&nbsp;Tickets | `#tickets` |  | 367 | conserved | `TICKETS.md#ticket-records` |
| &nbsp;&nbsp;Sprints | `#sprints` |  | 949 | conserved; the sprint boundary is SPEC_METHOD §4, the mechanics and the ticket-versus-iteration-entry rule here | `TICKETS.md#sprints` |
| &nbsp;&nbsp;Comments | `#comments` |  | 380 | conserved | `TICKETS.md#comments` |
| &nbsp;&nbsp;Execution Contracts | `#execution-contracts` |  | 1,388 | conserved; the three lifetimes, the five purposes and the seven-step loop | `TICKETS.md#execution-contracts` |
| &nbsp;&nbsp;Milestone And Phase-Scoped Truth (`STDO-UP-006`) | `#milestone-and-phase-scoped-truth-stdo-up-006` | UP-006 | 671 | conserved | `TICKETS.md#milestones-and-phase-scoped-truth-up-006` |
| Default Layout | `#default-layout` |  | 747 | conserved | `TICKETS.md#default-layout` |
| Authority | `#authority` |  | 858 | conserved; the four bindings, no mandatory ACTIVE_TASKS.md, the board as projection unless rebound with no rival | `TICKETS.md#bindings-and-projections` |
| Sprint Rules | `#sprint-rules` |  | 16 | not applicable: heading with no claim text (16 bytes); its children are disposed individually | `TICKETS.md#3-sprint-rules` |
| &nbsp;&nbsp;One Durable Record Per Sprint | `#one-durable-record-per-sprint` |  | 431 | conserved | `TICKETS.md#one-durable-record-per-sprint` |
| &nbsp;&nbsp;Sprint Manifest Required Fields | `#sprint-manifest-required-fields` |  | 1,031 | conserved; all seventeen fields and the four field meanings | `TICKETS.md#manifest-fields` |
| &nbsp;&nbsp;Sprint Status | `#sprint-status` |  | 589 | conserved | `TICKETS.md#sprint-status` |
| &nbsp;&nbsp;Sprint Admission | `#sprint-admission` |  | 688 | conserved | `TICKETS.md#sprint-admission` |
| &nbsp;&nbsp;Sprint Compliance Escrow | `#sprint-compliance-escrow` |  | 1,298 | conserved in full; the five conditions, the eligible and never-hidden lists and the exit rule; "public graph functions or AssetSurface contracts" generalised to "public published-function or public carrier contracts", "UX" to "user-interface" | `TICKETS.md#compliance-escrow` |
| &nbsp;&nbsp;Sprint Close Review | `#sprint-close-review` |  | 1,174 | conserved | `TICKETS.md#close-review` |
| Ticket Rules | `#ticket-rules` |  | 16 | not applicable: heading with no claim text (16 bytes); its children are disposed individually | `TICKETS.md#4-ticket-rules` |
| &nbsp;&nbsp;One Durable Record Per Ticket | `#one-durable-record-per-ticket` |  | 592 | conserved | `TICKETS.md#one-durable-record-per-ticket` |
| &nbsp;&nbsp;Multi-Build-Tenant Ticket Independence | `#multi-build-tenant-ticket-independence` |  | 2,874 | conserved; the build-tenancy bounded context is cited at PRODUCT_DEFINITION §8, where the tenant places rc.2's what-how-and-work-carriers | `TICKETS.md#multi-build-tenant-independence` |
| &nbsp;&nbsp;Required Fields | `#required-fields` |  | 1,201 | conserved | `TICKETS.md#required-fields` |
| &nbsp;&nbsp;Allowed Types | `#allowed-types` |  | 158 | conserved | `TICKETS.md#types` |
| &nbsp;&nbsp;Ticket Category | `#ticket-category` |  | 1,026 | conserved | `TICKETS.md#category` |
| &nbsp;&nbsp;Inside-Out First Ticket Sequencing | `#inside-out-first-ticket-sequencing` |  | 958 | conserved | `TICKETS.md#inside-out-sequencing` |
| &nbsp;&nbsp;Change Class | `#change-class` |  | 1,143 | conserved; the classes themselves are SPEC_METHOD §4, which names them the triage target of every carrier | `TICKETS.md#change-class` |
| &nbsp;&nbsp;Upward Propagation Check | `#upward-propagation-check` |  | 1,424 | conserved in full; consumption of the computed classification, the realization_refactor precondition and the upward walk to the first missing layer | `TICKETS.md#upward-propagation-check` |
| &nbsp;&nbsp;Triage Metadata | `#triage-metadata` |  | 371 | conserved | `TICKETS.md#triage-metadata` |
| &nbsp;&nbsp;Work-Carrier-To-Execution Rule | `#work-carrier-to-execution-rule` |  | 4,127 | conserved; the table, the ticket-shaped rule, the creation rules and the obligation-retention order here; the step-side admission relation (drafting versus admission, the admitted-result coordinates, the durable result surface) is ACTIVATION §1, defined once there | `TICKETS.md#carrier-selection`; `ACTIVATION.md#admission` |
| &nbsp;&nbsp;Execution Contract Admission | `#execution-contract-admission` |  | 1,064 | conserved; logging and availability here; the states and the self-certification rule at ACTIVATION §1; basis admission at SPEC_METHOD §3 | `TICKETS.md#execution-contract-admission`; `ACTIVATION.md#admission`; `SPEC_METHOD.md#3-outcome-conservation` |
| &nbsp;&nbsp;Execution And Verification Authority Separation (`STDO-UP-007`) | `#execution-and-verification-authority-separation-stdo-up-007` | UP-007 | 2,835 | conserved; the generic assessment protocol is EVALUATION §3 | `TICKETS.md#execution-and-verification-authority-separation-up-007` |
| &nbsp;&nbsp;Recorded Judgment And Owner-Ruling Continuity | `#recorded-judgment-and-owner-ruling-continuity` |  | 2,560 | conserved; the generic reuse law is ACTIVATION §7 | `TICKETS.md#recorded-judgment-and-owner-ruling-continuity` |
| &nbsp;&nbsp;Bounded-Context Term Binding | `#bounded-context-term-binding` |  | 1,020 | conserved; the resolution law is PRODUCT_DEFINITION §5 | `TICKETS.md#bounded-context-term-binding` |
| &nbsp;&nbsp;Evaluation Criteria And Non-Closure Conditions | `#evaluation-criteria-and-non-closure-conditions` |  | 1,132 | conserved | `TICKETS.md#evaluation-criteria-and-non-closure-conditions` |
| &nbsp;&nbsp;Condition-Based Closure And Reuse | `#condition-based-closure-and-reuse` |  | 1,395 | conserved; "Executive appointment" generalised to "coordinating appointment" | `TICKETS.md#condition-based-closure-and-reuse` |
| &nbsp;&nbsp;Test Case Authority | `#test-case-authority` |  | 2,215 | conserved in full; the derivation chain, the predicate rules, the five-step order with its eight fields, the defect and re-triage rules; "graph" and "graph-function" generalised to "published function"; ASSURANCE §3 points here | `TICKETS.md#test-case-authority` |
| &nbsp;&nbsp;Implementation Migration Category | `#implementation-migration-category` |  | 4,944 | conserved; the declaration, the checklist, the fields and the closure rules here; the slice-promotion rule is SPEC_METHOD §7, its ticket-local consequence here | `TICKETS.md#declaration-and-checklist`; `TICKETS.md#closure-of-a-migration-ticket`; `SPEC_METHOD.md#constitutional-migration-options` |
| &nbsp;&nbsp;Migration Strategy Requirements | `#migration-strategy-requirements` |  | 1,097 | conserved | `TICKETS.md#strategy-requirements` |
| &nbsp;&nbsp;Recurring Realization And Library Declaration | `#recurring-realization-and-library-declaration` |  | 1,322 | conserved | `TICKETS.md#recurring-realisation-and-library-declaration` |
| &nbsp;&nbsp;Multi-Build-Tenant Review Rule | `#multi-build-tenant-review-rule` |  | 517 | conserved | `TICKETS.md#multi-build-tenant-review` |
| &nbsp;&nbsp;Implementation Migration Review Disambiguation | `#implementation-migration-review-disambiguation` |  | 2,243 | conserved; question 8's "F_D-like checks" and "F_P-like path" generalised to "other deterministic checks" and "constructive or probabilistic path" | `TICKETS.md#review-disambiguation` |
| &nbsp;&nbsp;Impacted Interface Review Checklist | `#impacted-interface-review-checklist` |  | 1,922 | conserved | `TICKETS.md#impacted-interface-review-checklist` |
| &nbsp;&nbsp;Required Break Order And Break-To-Closure Map | `#required-break-order-and-break-to-closure-map` |  | 1,435 | conserved | `TICKETS.md#break-order-and-break-to-closure-map` |
| &nbsp;&nbsp;Mixed-State Negative Proof | `#mixed-state-negative-proof` |  | 1,699 | conserved; "graph function" generalised to "published function" | `TICKETS.md#mixed-state-negative-proof` |
| &nbsp;&nbsp;Allowed Status | `#allowed-status` |  | 240 | conserved | `TICKETS.md#status` |
| &nbsp;&nbsp;Ticket Lanes | `#ticket-lanes` |  | 766 | conserved | `TICKETS.md#lanes` |
| &nbsp;&nbsp;One-Truth State Projection And Drift Refusal (`STDO-UP-009`) | `#one-truth-state-projection-and-drift-refusal-stdo-up-009` | UP-009 | 635 | conserved | `TICKETS.md#one-truth-state-projection-and-drift-refusal-up-009` |
| Recommended Ticket Shape | `#recommended-ticket-shape` |  | 4,934 | conserved; the sprint, ordinary and migration shapes carried verbatim | `TICKETS.md#8-recommended-shapes` |
| Operating Mode | `#operating-mode` |  | 557 | conserved | `TICKETS.md#operating-mode` |
| Relationship To Other Surfaces | `#relationship-to-other-surfaces` |  | 742 | conserved | `TICKETS.md#relationship-to-other-surfaces` |
| Future Extensions | `#future-extensions` |  | 508 | conserved; the listed growths, the default-carrier rule and the substitution law | `TICKETS.md#carrier-substitution` |

## TRAVERSAL_OCCURRENCE_PROFILE.md

Base route: `stdo://releases/v2.5.1-rc.2/standards/TRAVERSAL_OCCURRENCE_PROFILE.md`

| Section | Anchor | Identifiers | Bytes | Disposition | Successor locus |
|---|---|---|---|---|---|
| Position | `#position` |  | 892 | conserved; both URN blocks carried exactly | `TRAVERSAL_OCCURRENCE.md#position` |
| Scope | `#scope` |  | 721 | conserved | `TRAVERSAL_OCCURRENCE.md#scope` |
| Imported Calculus Boundary | `#imported-calculus-boundary` |  | 2,544 | conserved; `RecordKind_ac` and `Population_M` pointed to AXIOMATIC_CALCULUS §2 | `TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary` |
| Closed Semantic-Object Sorts | `#closed-semantic-object-sorts` |  | 4,521 | conserved; the nineteen-sort table carried exactly | `TRAVERSAL_OCCURRENCE.md#closed-semantic-object-sorts` |
| &nbsp;&nbsp;Finite Reference-Domain Table | `#finite-reference-domain-table` |  | 16,318 | conserved; the basis codes, every table row, the external-resolution expansion and `ResolutionRefDomain` carried exactly | `TRAVERSAL_OCCURRENCE.md#finite-reference-domain-table` |
| Closed Event-Kind Population | `#closed-event-kind-population` |  | 1,504 | conserved | `TRAVERSAL_OCCURRENCE.md#closed-event-kind-population` |
| Closed Relation Families | `#closed-relation-families` |  | 8,905 | conserved; the twenty-four relation kinds, qualifier record, value domains, contract, cardinality function and congruence law carried exactly | `TRAVERSAL_OCCURRENCE.md#closed-relation-families` |
| Closed Constraint, Judgment, Residual, And Stop Kinds | `#closed-constraint-judgment-residual-and-stop-kinds` |  | 6,798 | conserved; the four kind populations and three tables carried exactly; functor-kind laws pointed to AXIOMATIC_CALCULUS §5; no mapping of the stop kinds to the core algebra is declared (residual) | `TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds` |
| Occurrence Identity | `#occurrence-identity` |  | 1,781 | conserved | `TRAVERSAL_OCCURRENCE.md#occurrence-identity` |
| &nbsp;&nbsp;OP-001 Seed Acyclicity | `#op-001-seed-acyclicity` | OP-001 | 248 | conserved | `TRAVERSAL_OCCURRENCE.md#op-001-seed-acyclicity` |
| Candidate, Judgment, Event, And Relation Separation | `#candidate-judgment-event-and-relation-separation` |  | 3,758 | conserved | `TRAVERSAL_OCCURRENCE.md#candidate-judgment-event-and-relation-separation` |
| &nbsp;&nbsp;OP-002 Atomic Semantic Admission | `#op-002-atomic-semantic-admission` | OP-002 | 581 | conserved | `TRAVERSAL_OCCURRENCE.md#op-002-atomic-semantic-admission` |
| &nbsp;&nbsp;OP-003 Correction Without Erasure | `#op-003-correction-without-erasure` | OP-003 | 253 | conserved | `TRAVERSAL_OCCURRENCE.md#op-003-correction-without-erasure` |
| Causality And Typed Lineage | `#causality-and-typed-lineage` |  | 748 | conserved | `TRAVERSAL_OCCURRENCE.md#causality-and-typed-lineage` |
| &nbsp;&nbsp;OP-004 Precedence Is Not Authority | `#op-004-precedence-is-not-authority` | OP-004 | 303 | conserved | `TRAVERSAL_OCCURRENCE.md#op-004-precedence-is-not-authority` |
| Mutable-Subject Effect Relation | `#mutable-subject-effect-relation` |  | 3,806 | conserved | `TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation` |
| &nbsp;&nbsp;OP-005 Mutable Reality Conservation | `#op-005-mutable-reality-conservation` | OP-005 | 496 | conserved | `TRAVERSAL_OCCURRENCE.md#op-005-mutable-reality-conservation` |
| &nbsp;&nbsp;OP-006 Immutable Iteration History | `#op-006-immutable-iteration-history` | OP-006 | 298 | conserved | `TRAVERSAL_OCCURRENCE.md#op-006-immutable-iteration-history` |
| Event Frontier And Projection | `#event-frontier-and-projection` |  | 1,024 | conserved | `TRAVERSAL_OCCURRENCE.md#event-frontier-and-projection` |
| &nbsp;&nbsp;OP-007 Scope Conservation | `#op-007-scope-conservation` | OP-007 | 246 | conserved | `TRAVERSAL_OCCURRENCE.md#op-007-scope-conservation` |
| Authority And Adoption | `#authority-and-adoption` |  | 966 | conserved | `TRAVERSAL_OCCURRENCE.md#authority-and-adoption` |
| Exact Profile Identity | `#exact-profile-identity` |  | 172 | conserved | `TRAVERSAL_OCCURRENCE.md#exact-profile-identity` |
| &nbsp;&nbsp;Closed Profile Signature | `#closed-profile-signature` |  | 5,576 | conserved; the signature, basis and identity blocks and the ten-fragment list carried exactly, the fragments resolving to this member's headings; the member path written `standards/TRAVERSAL_OCCURRENCE.md` and the calculus clause `#2-signature`, the carried block's "Core Signature clause" being AXIOMATIC_CALCULUS §2 Signature; the rc.2 edition count "fourteen members" superseded by AXIOMATIC_CALCULUS §8, which retains the principle-ref set without a hard-coded count | `TRAVERSAL_OCCURRENCE.md#closed-profile-signature` |
| Exclusions | `#exclusions` |  | 563 | conserved | `TRAVERSAL_OCCURRENCE.md#exclusions` |
| Conformance Obligations | `#conformance-obligations` |  | 2,222 | conserved; all twenty-one obligations | `TRAVERSAL_OCCURRENCE.md#conformance-obligations` |

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
