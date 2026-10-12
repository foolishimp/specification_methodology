# PROFILES

Tier 3. How domain profiles import the core and what stays out of it. A
profile adds domain obligations, bindings and vocabulary; it imports
[FOUNDATIONS](FOUNDATIONS.md), [ACTIVATION](ACTIVATION.md),
[EVALUATION](EVALUATION.md) and [SPEC_METHOD](SPEC_METHOD.md) by reference
and restates none of them.

## 1. The boundary

The core names no runtime, no carrier and no executor. Terms owned outside
the core, by a profile, a realisation or an rc.2 member, never enter tier
1 or 2 except in a disposition table: graph, edge, vector, traversal,
ledger, event log, worksite, HoG, F_D, F_P, F_H, Markov overlay, module,
screen, entity cut. A profile may bind a core mechanism to one of these;
the binding is declared in the profile with its direction, preserved
meaning, narrowed scope and invalidation. The declared-binding rule is new
(P0 boundary, P1); its shape follows ODD's specialisations of F_P and F_H,
which
[ODD probabilistic compute](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#probabilistic-compute)
owns in the graph-native context and carries as their provenance.

A worked application, a hello world or a data mapper is an external test
subject; its particulars cannot become generic method functionality by
precedent.

## 2. Graph execution

Graph execution is two tier-3 members, indexed here; each restates its
predecessor in full in its own text and declares its bindings under §1
(P0 boundary, P1):

| Member | Receives | Binds or adds |
|---|---|---|
| [ODD](ODD.md) | rc.2 ODD_METHOD, all 48 rows | the bounded step of FOUNDATIONS P0 to one vector or edge traversal and the graph-native F_P, F_D and F_H shorthands, with F_P and F_H as declared specialisations of SPEC_METHOD §5 ([§5 Probabilistic compute](ODD.md#probabilistic-compute)); the refinement of ACTIVATION §4 to graph functions under the cumulative environment law ([§5 Graph functions](ODD.md#graph-functions), [§11.8](ODD.md#118-cumulative-environment-law-is-mandatory)) |
| [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md) | rc.2 TRAVERSAL_OCCURRENCE_PROFILE, all 25 rows | an optional closed model-family signature over one exact `a_c` basis of AXIOMATIC_CALCULUS for immutable occurrence histories over a mutable subject, with OP-001 to OP-007 |

The ownership split of graph execution (runtime, product, service layers)
is [ODD §10](ODD.md#10-what-an-odd-product-is); the worker's internal
solution strategy stays outside the framework under
[ODD §5](ODD.md#probabilistic-compute). Where another member says that
this section keeps the ODD binding, the binding is the one ODD states and
this section indexes (P0, P1).

## 3. Software design

Imports the core and binds: the derivation of operation identities from
discovered functionality through an ontology, logical completeness, prime
contraction, the irreducible carrier set and projections
([ontology-first design](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#4b-ontology-first-design-rule),
[prime law](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#5-prime-law),
[carrier set](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#5a-irreducible-architectural-carrier-set-rule),
[ontology projection](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#ontology-projection-law));
transformation admission completeness
([UP-016](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016));
invariant reconstruction sufficiency
([UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018));
computational realisation projection
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019));
foundation selection
([UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023)).
All of DESIGN_MODULE_METHOD is conserved by reference. The derivation chain
is the profile's largest reasoning cost; the profile requires it where it
applies, and ACTIVATION §6 asks every obligation to pay for the ambiguity it
removes. Whether a design boundary with no material alternative must still
pay the full chain is a question for the profile's owner, carried here as a
residual and not decided by this corpus.

## 4. UX

Imports the core and binds reader and task obligations, operational
projection and screen-level acceptance. Conserved by reference:
[UX_METHOD](stdo://releases/v2.5.1-rc.2/standards/UX_METHOD.md).

## 5. World model

Imports the core and binds entity recovery and the entity cut as the
published identity-bearing unit
([entity cut](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law)),
the attribute ledger
([attribute ledger law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#attribute-ledger-law)),
composition of local artifacts
([composition law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#composition-law)),
and the Markov-object construct at candidate status
([epistemic status](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct)).
All of WORLD_MODEL_METHOD is conserved by reference.
Nothing in the core depends on the construct being established.

## 6. Source dispositions

| rc.2 member | Disposition |
|---|---|
| ODD_METHOD | conserved in full in ODD (all 48 rows; its §21), indexed in §2; the generic parts (bounded unit, refinement, loop structure) are generalised into ACTIVATION; the declared-binding rule of §1 is new |
| TRAVERSAL_OCCURRENCE_PROFILE | conserved in full in TRAVERSAL_OCCURRENCE (all 25 rows; its Source dispositions), indexed in §2 |
| baseline runtime bindings | received with STDO_REFERENCE_FRAME_BASELINE by EXECUTIVE_BASELINE and disposed there |
| DESIGN_MODULE_METHOD | conserved by reference in §3; UP-005, UP-017, UP-018, UP-019, UP-023 and the totality rule are consumed by tier 1; the per-boundary cost of the derivation chain is a residual question for the profile's owner |
| UX_METHOD | conserved by reference in §4 |
| WORLD_MODEL_METHOD | conserved by reference in §5; identity and entity-cut law consumed by FOUNDATIONS P3 |
| Authority compressions, schemas, templates | not applicable in this draft; derived views are produced from the tier 1–2 documents when a thread selects them |
