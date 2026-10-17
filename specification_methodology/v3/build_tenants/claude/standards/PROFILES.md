# PROFILES

Tier 3. Owns the boundary between the core and the profiles, the
declared-binding rule and the import rule that every profile applies
(§1), and indexes the profiles (§2 to §6). A profile is a domain or
operational specialisation of the method; the members of tiers 1 and 2
are the core.

## 1. The boundary

The core names no runtime, no carrier and no executor. Terms owned outside
the core, by a profile, a realisation or an rc.2 member, never enter tier
1 or 2 except in a disposition table: graph, edge, vector, ledger, event
log, worksite, HoG, Markov overlay, screen, entity cut, and the design
profile's IACS and Prime. The traversal record and the functor kinds F_D,
F_P and F_H are tier-1 calculus terms owned by AXIOMATIC_CALCULUS §5, and
"module" is a generic term, as the predecessor's generic testing law uses
it; neither is restricted here. A profile may bind a core mechanism to one of these;
the binding is declared in the profile with its direction, preserved
meaning, narrowed scope and invalidation. In this member "binding" means
that declared binding of a core mechanism; a Product's adoption binding is
[PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)'s,
and a carrier binding to a typed contract is [UX §7](UX.md#7-carrier-binding)'s;
the three are not interchanged. The declared-binding rule is new
(P0 boundary, P1); its shape follows ODD's specialisations of F_P and F_H,
which [ODD §5 Probabilistic compute](ODD.md#probabilistic-compute) owns in
the graph-native context and carries as their provenance; the
predecessor's section is rc.2
[ODD probabilistic compute](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#probabilistic-compute).

Import rule. A profile imports the generic families of tiers 1 and 2 that
its rules rest on, and owns only its own bindings: the terms and choices
it adds for its domain or operation, among them the declared bindings
above (P1, P6). It imports each concept it uses from a member of tiers 1
and 2 under
[FOUNDATIONS §2 Imports between members](FOUNDATIONS.md#imports-between-members),
which states what an import is, and restates none of that member's rules.
Its family table, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
names each imported family by its ID and the section that holds its table,
in the premise column; the profile's rules rest on that family's
consequences, with the standing FOUNDATIONS §3 gives them, and the
family's rules and choices keep their owners. A profile that refines
another profile declares the refinement in its lead; the refined profile
keeps its rules, and the refining profile owns only what it adds (P1, P6).
The import rule is new in this corpus. Purpose and material relation:
each profile table cites the families it rests on without restating them,
so no generic rule gains a second owner in a profile and no choice a
profile adds is presented as following from the foundations (P6, P1).

A worked application, a hello world or a data mapper is an external test
subject; its particulars cannot become generic method functionality by
precedent.

## 2. Graph execution

Graph execution is two tier-3 members, indexed here; each restates its
predecessor in full in its own text and declares its bindings under §1
(P0 boundary, P1):

| Member | Receives | Binds or adds |
|---|---|---|
| [ODD](ODD.md) | rc.2 ODD_METHOD, all 48 rows | the bounded step of FOUNDATIONS P0 to one vector or edge traversal and the graph-native F_P, F_D and F_H shorthands, with F_P and F_H as declared specialisations of SPEC_METHOD §5 ([§5 Probabilistic compute](ODD.md#probabilistic-compute)); the refinement of ACTIVATION §4 to graph functions, with the cumulative environment law of §11.8 declared as its specialised contract for carrying earlier outputs ([§5 Graph functions](ODD.md#graph-functions), [§11.8](ODD.md#118-cumulative-environment-law-is-mandatory)) |
| [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md) | rc.2 TRAVERSAL_OCCURRENCE_PROFILE, all 26 rows, 25 conserved and 1 proposed superseded, pending the product owner | an optional closed model-family signature over one exact `a_c` basis of AXIOMATIC_CALCULUS for immutable occurrence histories over a mutable subject, with OP-001 to OP-007 |

The ownership split of graph execution (runtime, product, service layers)
is [ODD §10](ODD.md#10-what-an-odd-product-is); the worker's internal
solution strategy stays outside the framework under
[ODD §5](ODD.md#probabilistic-compute). Where another member says that
this section keeps the ODD binding, the binding is the one ODD states and
this section indexes (P0, P1).

## 3. Software design

[DESIGN_MODULE](DESIGN_MODULE.md) is the software-design profile. It
imports the core and binds: ontology-first derivation of operation
identities from discovered functionality through logical completeness,
Prime contraction, the irreducible architectural carrier set and its
projections; proportional design sequencing with the decision-complete
design gate; bounded frame conservation; native constructability;
capability and foundation selection; transformation admission
completeness; invariant reconstruction sufficiency; computational
realisation projection; the module taxonomy and realisation rules; and
the design review questions and checklist. Its design-to-module evidence
route, module-derived unit tests and module lifecycle confirmation are
ASSURANCE §14 to §16, and its core rule and non-goals SPEC_METHOD §2
Realisation shape. The per-boundary cost of the derivation chain is
decided there (DESIGN_MODULE §5 Proportional design sequencing, §7 Gate
and retrospective work) (P2, P0).

## 4. UX

[UX](UX.md) is the UX profile. It refines DESIGN_MODULE for modules that
realise a UX surface, imports the core, and binds: the Elm process model
with typed State, Msg, Update, View, Cmd and Sub; the boundary between UX
messages and admitted product carriers; the state transition law; the
effect membrane; binding to AssetSurface or an equivalent typed contract;
view continuation and the Msg-replay proof; view shape; type sharing with
runtime validation at untrusted seams; the accessibility minimum;
realisation discretion; adoption with the scaffold and exemption law and
UX sprint compliance escrow; the failure patterns and review questions;
and its refinements of the core result algebra, each value mapped to one
core value (UX §15). Its binding of TICKETS §3's generalised escrow terms
is declared in its lead (P6, P2).

## 5. World model

[WORLD_MODEL](WORLD_MODEL.md) is the world-model profile. It imports the
core and binds: the imported product-lineage concepts and the Builder
Project specialisation; the Markov-object construct at candidate status
with its effective blanket, working refinements, epistemic status and
promotion gate; the core claims and units; entity recovery and the entity
cut as the published identity-bearing unit, with its admissibility,
discrimination and publication law; the attribute ledger; the
representation, materialisation and publication laws; Markov-object
overlay construction; saturation; composition of local artifacts;
projection; the control and data planes; the proof law and
world-model-driven development; and its refinements of the core result
algebra, each value mapped to one core value (WORLD_MODEL §14). Its
binding of FOUNDATIONS §2 Object
and P3's boundary claim to the entity cut is declared in its lead.
Nothing in the core depends on the construct being established (P3, P6).

## 6. Engagement baseline

[EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) is the optional
engagement-baseline profile. It imports the core and describes the
executive configuration, one configuration in the sense of
[ACTIVATION §1 Configuration](ACTIVATION.md#configuration), with three
engagement frames (Executive, Worker, Reviewer) and a catalogue of
specialist frames, mapped onto the law of tiers 1 and 2. Its frame names
bind the responsibilities that configuration allocates under
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation),
not roles imported by spelling, as its lead declares (P1, P6).

## 7. Source dispositions

Each cell names where the rows of one rc.2 member receive their
dispositions. Every row's disposition is one of the four values of
[RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015); a
row with none is unresolved, which blocks qualification of the claim it
affects.

| rc.2 member | Disposition |
|---|---|
| ODD_METHOD | conserved in full in ODD (all 48 rows; its §21), indexed in §2; the generic parts (bounded unit, refinement, loop structure) are generalised into ACTIVATION; the declared-binding rule of §1 is new |
| TRAVERSAL_OCCURRENCE_PROFILE | 25 rows conserved and 1 proposed superseded, pending the product owner, disposed in TRAVERSAL_OCCURRENCE, Source dispositions; indexed in §2 |
| baseline runtime bindings | disposed row by row in EXECUTIVE_BASELINE, with STDO_REFERENCE_FRAME_BASELINE; §6 is its index entry |
| DESIGN_MODULE_METHOD | disposed row by row in DESIGN_MODULE, with 6A to 6C in ASSURANCE §14 to §16 and the core rule and non-goals in SPEC_METHOD §2; §3 is its index entry; the first-pass residual on the cost of the derivation chain is answered by DESIGN_MODULE §5 and §7 |
| UX_METHOD | disposed row by row in UX; §4 is its index entry. The first-pass description of UX by reader and task obligations, operational projection and screen-level acceptance was candidate text with no source in UX_METHOD, so it is no predecessor claim; it is withdrawn |
| WORLD_MODEL_METHOD | disposed row by row in WORLD_MODEL; §5 is its index entry; the generic identity and boundary law stays FOUNDATIONS §2 and P3 and IDENTITY, and the entity-cut law is WORLD_MODEL §9, bound to P3 by WORLD_MODEL's declared binding |
| Authority compressions, schemas, templates | schemas and templates conserved under standards/schemas/ and standards/templates/; the ten compressions and the requirements template's bootstrap entrypoint have no disposition yet, so they are unresolved, pending the product owner's ruling on supersession by projected frames |
| no rc.2 member | the import rule of §1 is new in this corpus and receives no predecessor claim |
