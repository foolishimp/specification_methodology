# I4-02 packet: family tables of EXECUTIVE_BASELINE, DESIGN_MODULE and ODD, with the FOUNDATIONS commitments and format

Verbatim sections at the current tree. Line numbers are those of the member.


## `standards/FOUNDATIONS.md#3-commitments` (lines 369-653)

```markdown
## 3. Commitments

Each commitment has exactly one standing, in the terms §1 defines; the
table states it, with a distinction the commitment retains. The adopted
premises, which §1 identifies as the recovered and independent
commitments, are commitments adopted for the domain this method governs,
not theorems derived from finite capacity alone, that is, from the bound
on an actor's envelope (P0). Particular method rules need these premises
plus their stated domain and policy choices, each with its owner
([Foundation to law](#foundation-to-law)). An argument from the premises
preserves that distinction; it does not create authority (P6). Purpose
and material relation of this paragraph and the standing column: each
commitment shows what grounds it, so no premise is presented as derived
and no consequence is taken for a premise (P6).

| Commitment | Standing | Distinction retained |
|---|---|---|
| P0 Bounded construction | recovered | the actor's internal path within a step is its own |
| P1 Interpretation | independent | structural success never establishes fidelity |
| P2 Purpose | independent | an obligation with no route to the outcome is unjustified |
| P3 Identity | independent | current state, historical observation and representation identity stay separate |
| P4a Typed composition | independent | composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states |
| P4b Conservation of step-produced facts | derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable | sources a later step can re-acquire are governed by sufficiency, not conservation |
| P5 Totality | derived from P0 and P6, with P0's open-world premise | a step cannot report success on a condition outside its context |
| P6 Justification and authority | independent | neither evidence nor authority is minted by the other |

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope.
Sources, named as sources and not as proof (§1): finite attention within a
declared envelope ([RF-002](REFERENCE_FRAME.md#rf-002-finite-attention)),
material sufficiency ([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)),
material closure ([AC-010](AXIOMATIC_CALCULUS.md#ac-010-material-closure)),
the [work boundary](#work-boundary), and the refinement of one outer
contract into inner steps
([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement).
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P0's boundary commitment (the work boundary of §2): deterministic checks
and validation are evidence surfaces; they may optimise or prove a
domain-local path where the domain can make part of the work precise, and
they do not authorise the method, a runtime or a framework to absorb domain
solution strategy as constitutional law. Any unconstrained part of a
probabilistic worker's reasoning remains hidden worker-internal activity
and is forced back through the declared contracts, evidence, provenance and
control truth of the boundary. A framework layer that prescribes domain
solution strategy beyond the declared work contract and control truth has
crossed its authority boundary (P6). A profile may bind the unit to its own
traversal unit, in which that traversal is the admissible external space;
PROFILES §2 keeps that binding.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Non-entailment: let two steps fit their envelopes under one selected
outcome, keep declared identities, compose because the first's declared
result type, a length, meets the second's declared domain, record their
step-produced facts, return closed results and keep evidence apart from
authority, while the second reads the value under a contract no one
declares, in metres where the first wrote feet; P0 and P2 to P6 hold, yet
one representation has two meanings and no declared contract, which P1
forbids. "Algorithmic" means
explicit and structurally checkable; a semantic decision is lawful only
under an exact decision contract. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit
material obligations from the transformation they serve. Non-entailment:
let a finite actor realise a selected outer contract that names an
outcome, through steps that fit its envelope, read under declared
contracts, keep declared identities, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each interface's obligations are set by the capacity
available and not inherited from the transformation it serves; P0, P1 and
P3 to P6 hold, yet the same obligations count as adequate for opposite
outcomes and an obligation with no route to the outcome stands, which P2
forbids. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; a boundary is a claim with a proof obligation.
Non-entailment: let steps fit their envelopes under one selected outcome,
read under declared contracts, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each object's identity is taken from the place that
stores it and no authority, kind or value is declared, so an admissible
move makes one object two; P0 to P2 and P4a to P6 hold, yet identity is
neither declared nor kept across admissible change, which P3 forbids.
Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law),
restated in [WORLD_MODEL §9](WORLD_MODEL.md#9-entity-cut-construction).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's exact declared domain and preconditions.
Non-entailment: let a second step run on every output of the first, read it
under its own declared contract and return `invalid_basis` where the output
lies outside its declared domain, and let the composite keep only the
step-produced facts the outer contract needs. Each step fits its envelope and serves the selected
outcome, identities are declared and kept, the needed facts are recorded,
every result is closed and authority stays with its owners, so P0 to P3,
P4b, P5 and P6 hold. Yet the steps compose although the first's result type
need not meet the second's declared domain, and the first step's other
intermediate results and stop state are lost; P4a forbids both. The
retention has its own route to the outcome: when the composite is later
falsified or must be resumed, the kept intermediate results and stop state
locate the step to repair or restart, which a record of what the outer
contract needs does not supply (P2). Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them. The outer contract needs these facts (P2); the next
actor may re-acquire declared sources but not the producing step's private
result, because step-produced facts are not re-acquirable (P0); so only the
producing step can record them. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each is restated for its own scope by the
member §6 names.

P5 Totality. A step can meet a condition outside its context (P0's
open-world premise), and it cannot report success on one (P6). Its result
algebra therefore carries first-class outcomes other than success for such
a condition, and its control model names the next move. That these
outcomes are three, indeterminate, out_of_frame and invalid_basis, is a
declared choice conserved from RF-012, whose owner is §4
[Results](#results) (family F3, first row). Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in §4 [Results](#results), and are
stated as laws in
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal).

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope.
Non-entailment: a bounded actor satisfying all else can still take a green
label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004 ([IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)),
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6).

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the import rule that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).


```


## `standards/FOUNDATIONS.md#foundation-to-law` (lines 528-653)

```markdown
### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in five columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".
  A row never files the whole rule as the choice: the choice is only what
  the premises leave open.
- Pillar: the pillar contributions the row helps account for, by number.
  The pillars are the ten contributions that the Foundational Reduction of
  the Product that owns this corpus names, in its order: 1 specification
  and project structure; 2 world models, identity and Markov objects; 3
  algebraic calculus; 4 functional design; 5 outcome-driven development; 6
  information and interpretation; 7 reference frames; 8 computational
  calculus and execution binding; 9 evidence, correction and authority; 10
  axiomatic calculus. That Product owns the contributions and their
  wording. A Pillar cell is a trace, like the rest of the table: it is not
  a premise, adds no standing to the row, owns no choice, and does not
  claim that a pillar is an axiom or follows from finite capacity.

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table, the members or sections the table accounts for, and the pillar
contributions its table's rows name, which are the union of its rows'
Pillar cells. A row marked table pending names the section that is to
hold its table; until that table is written, the row names its members
and traces none of their rules. A Pillar cell marked pending names no
pillar: the family's table does not yet carry the Pillar column, and the
cell is filled from that table's rows when it does. The index decides
nothing: each rule is in its owning section, and each trace is in its
table (P1, P6).

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 9 |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 | 3, 4, 6, 7, 9 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 | 2, 4, 5, 6, 7, 9 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority | 1, 4, 5, 6, 7, 8, 9 |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 | 1, 2, 3, 6, 7, 8, 9 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE | 1, 3, 4, 6, 7, 8, 9 |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position) | IDENTITY | 1, 2, 6, 7, 8, 9 |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position) | AXIOMATIC_CALCULUS | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 | 1, 2, 3, 4, 5, 6, 8, 9 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 | 1, 2, 3, 4, 5, 6, 7, 9 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) | 1, 2, 4, 6, 7, 8, 9 |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS; POSTING_GUIDE §2, §7, §9 | 1, 2, 3, 4, 6, 7, 8, 9 |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers) | ASSURANCE | 1, 3, 4, 5, 6, 7, 8, 9 |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position) | RELEASE; FOUNDATIONS §2 Product lineage objects | 1, 2, 3, 6, 7, 8, 9 |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE | 1–9 |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE | 1, 2, 3, 4, 5, 6, 7, 9 |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD | 1–9 |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE | 1, 2, 3, 4, 6, 7, 8, 9, 10 |
| F20 | UX | [UX §1](UX.md#1-position) | UX | 1–9 |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position) | WORLD_MODEL | 1, 2, 3, 5, 6, 8, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the import rule that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations, no consequence is filed
as a choice, and no partial trace is presented as a derivation of the
whole method (P6, P2). The Pillar column binds each argument to the
contributions it helps account for, so a contribution that no row names
is visible as unaccounted (P2).


```


## `standards/EXECUTIVE_BASELINE.md#foundation-to-law` (lines 195-271)

```markdown
### Foundation to law

This member is material family F16, Engagement baseline (operational
profile). The table below shows which of its rules follow from which
premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. An actor enters the
family here, at the choice between direct entry and coordination. The
family imports seven families under
[PROFILES §1](PROFILES.md#1-the-boundary): F1, frames and context
([REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit));
F2, transitions, steps and configuration
([ACTIVATION §1](ACTIVATION.md#1-the-step)); F3, results and their
combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)); F4, work
state, resumption and reuse
([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)); F5,
proportionality and cost
([ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality)); F6, claims,
evidence, assessment and acceptance
([EVALUATION §1](EVALUATION.md#1-claims)); and F13, work carriers
([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)), for the
boundaries of independent review and the closure condition. A row that
cites an imported family uses that family's consequences as premises; the
rules that state them keep their owners, and the choice column names them
as imported, never as this profile's choices. Standing of the commitments
cited ([FOUNDATIONS §3](FOUNDATIONS.md#3-commitments)): P0 recovered; P1,
P2, P3, P4a and P6 independent; P4b derived from P0 and P2, with P0's
premise that step-produced facts are not re-acquirable; P5 derived from P0
and P6, with P0's open-world premise. Its instance premises hold where
the executive configuration is selected; they are adopted with it and do
not follow from the foundations (P1, P6):

- I1: the work is a series of bounded tasks under one governed outcome,
  and carrying out a bounded change and managing delivery across the tasks
  need separate attention;
- I2: existing project authority (Goals, Product, requirements, accepted
  design, a work item, identity or release law) holds every decision grant
  the configuration applies;
- I3: the actors are fallible and have finite context and attention, and a
  constructing actor may be probabilistic.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P1 (independent); F2 imported | By P6 authority exists only through an admitted grant, and F2 makes the executive configuration one lawful configuration among others, so this profile cannot hold a decision an owning clause holds: it owns only the terms and choices it adds, and where it conflicts with an owning clause, that clause controls. Inclusion in a method cut is no grant (P6), so it makes the profile available and does not adopt it. By P1 a name carries no meaning by its spelling, so each frame name binds only the responsibility the configuration allocates to it | [the lead](#executive_baseline); [§1](#1-canonical-compression); [§2](#2-status-and-authority-boundary) | the bindings the lead lists: this profile; adoption of the profile: the adopting Product's authority, through its basis ([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)) | 1, 7, 9 |
| P0 (recovered), P2 (independent); F2 imported | F2 makes a one-frame configuration lawful and lets a sufficient task be entered directly, with its admission, carrier and recording of a result without review ([ACTIVATION §1](ACTIVATION.md#roles-and-delegation)). By P2 an obligation with no route to the outcome is unjustified, so using this profile adds no review, ticket, diagram recreation or owner ceremony to such a task. By P0 the direct step still realises the same outer contract, so the direct route binds the same intake, territory, obligations, evidence, stop conditions and result consumer as the coordinated route | [§3](#3-engagement-applicability), before this section | the name Worker (Writer) for the directly entering frame: this profile | 1, 7 |
| P6 (independent), P2 (independent), P1 (independent) | By P6 evidence supports a claim and creates no authority, so delivery practice and observed failure enter frame selection, qualification and revision as evidence, never as method authority. By P2 a consumer's architecture, names, actors or topology served that consumer's outcome and have no route to a generic one, so none is imported. By P1 a precedent's form carries no meaning by itself, so it gives no semantic authority | [§4](#4-empirical-revision-boundary) | the six requirements of the engagement relation, as this profile's reading of its frames: this profile; the misfit signals: [REFERENCE_FRAME §10](REFERENCE_FRAME.md#missing-frame-signals), outside this member | 7, 9 |
| P0 (recovered), P2 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F2, F5 imported; I1, I3 | Under I1 carrying out a bounded change and managing delivery across tasks need separate attention, and by P0 each frame's context fits a finite envelope, so the two go to different frames. Under I3 a constructor can be wrong about its own candidate, and by P6 its self-review is construction output, so required assessment goes to a frame other than the constructor's. F2 requires a configuration's allocation to be explained, with its resource limits (declared under F5) and failure assumptions, and evaluated against the task, so this configuration states its explanation and fits only where I1 holds. By P5 an activation can fail, so a refused activation returns with its cause. By P6 selecting a configuration waives no grant, limit or prohibition, so each holds wherever it is selected | [§7 The executive configuration](#the-executive-configuration); [the lead](#executive_baseline); [§5](#5-profile-terms) Engagement frame, Executive, Worker, Reviewer | the three frames, their names and the explanation of their allocation: this profile; the values of the resource limits: the selected execution binding, under [ACTIVATION §6 Resource limits](ACTIVATION.md#resource-limits); the selection for a project: the existing authority that [§16](#16-adoption-or-project-defined-configuration) binds | 5, 7, 8, 9 |
| P6 (independent), P3 (independent); F2 imported; I2, I3 | Under I2 existing project authority holds every decision grant the configuration applies, and by P6 a label mints none ([FOUNDATIONS §2](FOUNDATIONS.md#authority-kinds)), so the Executive applies only decision authority already granted and acquires no operation authority from its label; a mutation needs the exact operation grant of the frame that performs it. By P3 an actor and the frame it occupies are distinct identities, so a role transition is a separate fact, known only where recorded. Under I3 a coordinator that changed the subject would dispose of its own construction on its own evidence (P6); that is this profile's reason for the choice in the next column, which the premises do not force | [§6](#6-executive-attention-evaluation-and-action) The three duties, No mutation while Executive; [§8](#8-derived-executive-frame) | the prohibition of every Executive edit, small, test-only or reversible ones included, and recording a role transition in the work carrier before the effect: this profile | 7, 9 |
| P0 (recovered), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P2 (independent), P3 (independent), P6 (independent); F2, F3, F4 imported; I1 | By P0 the Executive's envelope cannot hold every evaluator's working context, and by P4b the producing step records the facts the outer contract needs, so the Executive holds the frontier and the closed-result ledger and acquires more through its frame inputs or a further bounded evaluation, as F2's rule for a coordinator's bounded view requires. By P3 and P6 a result supports its claim only on the basis it binds, so the bases are revalidated before activation and before disposition, and a failed lock takes the value or move its owner gives (F2, F3). By P2 re-entering the cycle without a decision need has no route to the outcome, so attention waits for decision-relevant input, and by P6 waiting discharges no verification, evidence, assessment or authority duty | [§6](#6-executive-attention-evaluation-and-action) Attention cycle, Event-driven attention, Drift locks; [§7 The executive configuration](#the-executive-configuration), Coordination | the five locks, and event-driven attention as the default with bounded fallback observation: this profile | 5, 7, 9 |
| P3 (independent), P1 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F4 imported | By P3 identity is declared and survives admissible change, so the Source Project, Product Definition, candidate checkpoint, Release Cut, Product, Install, Artifact, Development Product and dependent Product of one chain are distinct declared identities, and a Development Product role binds one exact Install. By P1 a representation fixes no meaning, and by P6 nothing creates authority without a grant, so directory nesting, shared code or actors, source imports, tool reachability, matching labels or equal outputs create no identity, composition edge or authority transfer. A repair changes the subject, a material input change under F4, so it creates a new candidate and invalidates the affected results (P4b); a released identity's immutability does not pass to the Source Project, a distinct identity (P3) | [§6 Product-chain basis](#product-chain-basis) | the fields each composition edge names: this profile; the Product-role map in the basis: [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the lineage objects: [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects) | 1, 2 |
| P1 (independent), P3 (independent), P6 (independent), P0 (recovered), P4a (independent), P2 (independent); F1, F2 imported | F1 keeps the relation structures RF-009 lists distinct and never one hierarchy, and lets frames overlap without collapsing identity (RF-008), so the structures this configuration uses are instances of RF-009's list, and the Executive, Worker and Reviewer may share basis, outcome, checkpoint, candidate, evidence and residuals while each evaluates its own question and holds only its own authority (P6). By P0 and P4a an activated evaluation is one engagement frame with its material specialist frames on an exact subject and basis with a capable actor; by P2 a product schema or a frame runtime with no route to the outcome is not required | [§7](#7-non-hierarchical-frame-configuration), its opening | naming three of RF-009's structures in this configuration's terms, and the notation of an activated evaluation: this profile; the list of structures and its rule: [RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy), outside this member | 7 |
| P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P2 (independent) | By P6 evidence supports only the claim it bears on, so a passing thread establishes only the relations and conditions it exercised, and untested branches, combinations and refusal and recovery paths keep their proof obligations. By P4b a settled decision rests on its recorded basis, so material counterevidence reopens it. By P2 each increment is chosen for its route to the outcome: consequential uncertainty, dependency and interface reach, and failure impact | [§8 Steel-thread delivery](#steel-thread-delivery) | sequencing delivery around a steel thread as profile law, and scheduling substantial user-acceptance cycles near release: this profile; the generic sequencing heuristic: [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), outside this member | 5, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F3 imported | By P5 a step's result algebra carries outcomes other than success, and F3 maps each refined value to exactly one core value with its predicate; ACTIVATION §3 Construction availability is that refinement for "a candidate is available", with its values, grounds and map. So a Worker returns one of those values, selected by the cause ACTIVATION §3 states, and this profile states no ground of its own. By P6, as F3 states, availability is neither assessment nor acceptance, so no value is read as either; a refused activation creates no step, so it creates no Worker result | [§5 Work result](#work-result); [§9](#9-derived-worker-frame); [§12](#12-complete-engagement-transition) steps 2 and 3 | what the Worker reports and what its consumer does with each value: this profile. The values, grounds and core values ([ACTIVATION §3](ACTIVATION.md#construction-availability)) and the outcomes of `activate` ([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)) are imported, not chosen here | 3, 5, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F4 imported; I3 | By P5 a step can stop with an external effect whose completion its evidence cannot decide, as where a response is lost under I3, and F4 requires such an effect to be reconciled before any repetition or dependent action (ACTIVATION §5). The Executive cannot reconcile an effect it is not told of, so a work result names each intended external effect with its value, and the Executive has an effect of uncertain completion reconciled, sufficiently for the next dependent action, before reactivating work or taking that action | [§13](#13-handoff-projection), work result; [§12](#12-complete-engagement-transition) step 4; [§7 The executive configuration](#the-executive-configuration), failure assumptions | the effect field of the work-result projection: this profile. The effect values ([ACTIVATION §3 Effects](ACTIVATION.md#effects)) and the reconciliation rule ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) are imported | 4, 5 |
| P6 (independent), P1 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F6 imported; I3 | Under I3 a constructor can be wrong about its candidate, and by P6 its self-review is construction output (F6), so self-review stays Worker evidence, and where independent assessment is required a separately activated Reviewer that is not the author evaluates the exact live subject (F6). By P6 a verdict is evidence for the decision owner, so the Reviewer returns evidence-bound triage and no disposition, priority or next activation. By P1 and P5 a cause or repair risk the evidence cannot support is returned as uncertainty, not given precision | [§10](#10-derived-reviewer-frame); [§12](#12-complete-engagement-transition) steps 4 to 6; [§17](#17-actor-binding-and-independence) | the triage fields: this profile; the severity scale: the adopting Product. When independent assessment is required ([TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007), with the boundaries a governing basis adds) and what counts as independent ([EVALUATION §3](EVALUATION.md#3-independent-assessment)) are imported | 9 |
| P3 (independent), P6 (independent); F4, F6 imported | By P3 a subject's identity holds only as declared, and by P6 a verdict holds only on its basis, so a review evaluates an exact candidate whose identity cannot move under it: F6 requires a freeze before material reference exposure where generic method qualification applies, and elsewhere the subject is stabilised to the exactness the claim needs, the identity that transition evidence (F4) and traceability (F6) name. Neither premise requires a lifecycle state, so none named `frozen` is created | [§5 Exact candidate](#exact-candidate); [§12](#12-complete-engagement-transition) step 5B | the stabilisation where no freeze applies, an immutable identity or an equivalent exact-subject relation: this profile; the freeze and when it applies: [EVALUATION §7](EVALUATION.md#7-qualification-of-frames-and-of-the-method), imported | 2, 9 |
| P6 (independent), P1 (independent), P2 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F2, F3, F6 imported; I2 | By P6 evidence and decision are distinct, so severity, a grade of a finding's consequence, is evaluation evidence, while priority, the current-boundary effect and the disposition are decisions of the owner I2 names, and by P1 a policy that maps one to another does not make them one value (F6). F6 decides when a finding can block, so the current-boundary effect records the Executive's reading of a finding under that rule and decides nothing itself, and by F3 the decision returns through the core only through the one disposition applied. A hard stop holds whatever the priority (F2). By P2 an observation outside the claim has no route to that claim's outcome, so it opens no review round; by P5 an unsupported assessment is kept `indeterminate` or re-evaluated | [§5 Technical triage, severity, priority and boundary effect](#technical-triage-severity-priority-and-boundary-effect); [§12](#12-complete-engagement-transition) step 7 and Promotion constraint projection | the severity and priority scales, the decision cutoff, and which conditions of the outcome are hard stops: the adopting Product's basis ([§19](#19-baseline-specific-basis-and-activation-additions)); the three current-boundary effect states and the added row of the projection: this profile. When a finding can block ([EVALUATION §5](EVALUATION.md#when-a-finding-blocks-promotion)), what a hard stop is ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)) and the four dispositions ([ACTIVATION §3](ACTIVATION.md#disposition)) are imported | 5, 9 |
| P0 (recovered), P1 (independent), P2 (independent), P4a (independent), P5 (derived from P0 and P6, with P0's open-world premise); F1, F3 imported | By P1 a member, file, component or lens has no evaluation meaning until declared, so it becomes a specialist frame only through a complete frame declaration (F1). By P2 a family is instantiated only where material, and by P5 one that cannot be covered is an explicit residual, never dropped; by P0 no frame holds the whole workspace, so coverage is the union of what activated frames contribute, and visibility is not coverage. By P4a and F3 a composite claim is `satisfied` only through its declared conjunction; each seam case enters it as FOUNDATIONS §4 states, a seam without a result as a gap, and the composite is never `satisfied` while a gap or a non-satisfied mandatory seam remains | [§5](#5-profile-terms) Specialist frame, Generic specialist-frame family; [§11](#11-derived-generic-specialist-frame-set), with Refinement and conjunction; [§14](#14-coverage-application) | the twelve families, their questions and falsifiers, and the declared rule that every material seam is a mandatory result or required coverage, no frame dominant: this profile; each instance, and which non-satisfied value a composite reports where several are returned: the adopting project's declared conjunction rule ([§19](#19-baseline-specific-basis-and-activation-additions)) | 3, 7 |
| P4a (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P3 (independent), P6 (independent); F1, F2, F4 imported | By P4b a step's facts reach a later step only through what it records, and F4 hands work over by closed results without private working context, so every result returns through a declared relation with its closed result and source routes. By P6 and F2 a step begins only through admission and activation, so no handoff, completion, model response, tool output or shared actor activates another frame or authorises continuation. By P3 and P4a results of different candidates, bases or episodes keep their identities, so flattening projections establishes no relation among them; an equality or translation is declared (F1) | [§13](#13-handoff-projection); [§6](#6-executive-attention-evaluation-and-action) Attention cycle | the eight projections and their minimum content: this profile; their carriers: the existing project records | 5, 6, 7 |
| P5 (derived from P0 and P6, with P0's open-world premise), P2 (independent), P6 (independent); F1 imported | By P5 a frame that cannot decide returns a value other than success that names what would decide, so its closed result names the missing relation, coordinate, evidence, authority, capability or interaction. F1 orders diagnosis so that cheaper causes are checked before a frame is added (P2), and the Executive asks all eight questions of that order. By P6 an upstream change has an owner, so it re-enters there and the Executive does not repair it by enlarging its frame | [§15](#15-missing-frame-and-re-entry-application); [§20](#20-failure-classification); [§21](#21-anti-patterns) | the two readings of the diagnostic order (independence in question 3; specialist-frame inputs verified before question 5): this profile; which observations the failure table lists and which misapplications the anti-patterns name, as representative cases: this profile. Each entry applies a consequence traced in another row or an imported rule, and the failure table's first diagnosis routes evaluation and decides no verdict. The order itself ([REFERENCE_FRAME §10](REFERENCE_FRAME.md#diagnostic-order)) is imported | 7, 9 |
| P6 (independent), P3 (independent); F2 imported; I2 | Under I2 existing authority holds every decision grant, and by P6 position creates none, so existing authority selects the outcome and the work authority under its own owner, and F2 admits a configuration by the smallest authority owning each decision it makes. By P3 the basis and the mapping recorded in it are objects distinct from the authorities they cite, so the baseline-adoption projection records the profile mapping inside the Product-owned basis, defining no second basis and minting no authority. By P6 a local surface cannot amend its owner, so a departure from method law is a separate method basis or a non-conformance, never local frame selection | [§12](#12-complete-engagement-transition) step 1; [§5 Baseline-adoption projection](#baseline-adoption-projection); [§16](#16-adoption-or-project-defined-configuration); [§19](#19-baseline-specific-basis-and-activation-additions) | which authority owns which decision of this configuration (the list of §16), and the content of the adoption projection and of the basis additions: this profile; adoption and the content of the basis: the adopting Product ([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)) | 1, 9 |
| P6 (independent), P1 (independent), P5 (derived from P0 and P6, with P0's open-world premise); F6, F13 imported | By P6 a claim holds only on the evidence evaluated, so the profile is qualified only for the revisions, envelopes, branches and populations actually evaluated; by P1 a structural check establishes no semantic truth, so mechanical document checks and a source-linked Reviewer evaluation are bound together and neither is claimed as the other (F6). By P5 `indeterminate` never maps to `satisfied`, so a closed `indeterminate` result or a review event satisfies no unresolved obligation; the closure condition of a work item (F13) is applied to the selected branch only | [§18](#18-profile-qualification); [§22](#22-closure) | which cases a representative profile trial must establish (the twenty-six obligations), and which conditions record that this profile was applied to one outcome (the twenty-four conditions): this profile. Each obligation and condition applies a consequence traced in another row or an imported rule and adds no rule of its own. Frame and method qualification ([EVALUATION §7](EVALUATION.md#7-qualification-of-frames-and-of-the-method)) and the closure condition ([TICKETS §7](TICKETS.md#condition-based-closure-and-reuse)) are imported | 9 |

The table accounts for this whole member: the lead and §1 to §22, each
section traced by a row that names it or its parent section. Three parts add no
rule of their own: §5 Terms owned by ASSURANCE uses the tier-2 terms as
ASSURANCE §7 defines them; this table is a trace; and §23 records
dispositions and decides nothing. The rows name pillars 1 to 9. No row
names pillar 10, axiomatic calculus: this profile states no rule of the
a_c calculus and binds none.

The table is new in this corpus; it has no rc.2 row. Purpose and material
relation: a reader of this profile sees which of its rules rest on the
commitments and imported families, and which are choices this profile or
the adopting Product makes, so no profile choice is presented as following
from the foundations (P6, P2).


```


## `standards/DESIGN_MODULE.md#foundation-to-law` (lines 153-241)

```markdown
### Foundation to law

This member is material family F17, software design. The table below
shows which of its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. An actor enters the
family here, when it designs, implements or reviews a boundary that this
profile governs. The family imports these families under
[PROFILES §1](PROFILES.md#1-the-boundary), and its rows cite them as
premises: F1, frames and context, for
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds); F2,
transitions, steps and configuration ([ACTIVATION §1](ACTIVATION.md#1-the-step));
F3, results and their combination
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)); F4, work state,
resumption and reuse ([ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse));
F6, claims, evidence, assessment and acceptance
([EVALUATION §1](EVALUATION.md#1-claims)); F8, identity
([IDENTITY §1](IDENTITY.md#1-position)); F10, constitutional chain,
outcome and build-tenant binding ([SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain));
and F12, binding a project to the method
([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)).
Standing of the commitments cited
([FOUNDATIONS §3](FOUNDATIONS.md#3-commitments)): P0 recovered; P1, P2,
P3, P4a and P6 independent; P4b derived from P0 and P2, with P0's premise
that step-produced facts are not re-acquirable; P5 derived from P0 and P6,
with P0's open-world premise. Its instance premises hold where a project
adopts this profile for a boundary; they are adopted with it and do not
follow from the foundations (P1, P6):

- I1: a Product has decided the outcomes and capabilities it builds, and
  adopts this profile for a named boundary of its realisation;
- I2: realisation code can hold one meaning in typed carriers and explicit
  transforms or in orchestration, helpers, open payloads and shared
  mutable state, and in more than one place;
- I3: bounded actors design, implement, test, review and later change the
  boundary, and an actor taking a later local action generally does not
  hold the reasoning that produced the design;
- I4: a mechanism the boundary needs can be built locally or taken from
  existing foundations, and similar computation recurs across boundaries
  and over time.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P1 (independent); F10 imported; I1 | the constitutional chain decides what the Product does (F10) and authority stays with its owner (P6), so this profile governs only how a decided outcome is realised; one meaning admits several realisation shapes (P1), so a decision that functionality is required does not decide how many entities, functions, operations, carriers or modules exist; where the graph-execution profile governs, its graph carriers own the constructive law, so no deterministic module this profile governs replaces a graph function, edge traversal or graph module | [§1 Purpose](#purpose), [Position](#position), [Core rule](#core-rule); [§2](#2-graph-execution-alignment-and-escalation); [§8](#8-theoretical-framing); [§12 Relationship to other members](#relationship-to-other-members), [Non-goals](#non-goals) | the functional bias and its preferences at "should" force, and the profile's scope, which adopts no world-model theory (§8): this profile; the core rule and the non-goals: [SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape); the graph-native carrier law: [ODD](ODD.md#1-position) | 1, 4, 5 |
| P5 (derived), P6 (independent); F3 imported | an evaluation under this profile can meet a condition outside its context and cannot report success on it (P5), and a record is not a judgment (P6), so every performed evaluation returns a core value of F3, directly or through a refinement mapped where it is defined, and an entry of the design record, a `not_applicable` exclusion included, is not a result | [the head of this member](#design_module), Results and design records | the two refinements, their predicates and the record vocabularies: this profile; what an exclusion is: [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), Exclusion and the core | 3, 9 |
| P3 (independent), P1 (independent), P6 (independent); I2 | a meaning has one declared identity and is read through a declared contract (P3, P1), and code can hold one meaning in several places (I2), so a change that adds a place for a meaning adds a rival truth surface; hence a change adds no truth surface, and foreign input is lawful only at ingress, where it collapses into local carrier truth under a declared contract; a check is evidence, not authority (P6), so typing or schemas enforce only a seam already made real | [§3](#3-boundary-closure-evaluators) | that the three evaluators override other heuristics, at "should" force; the fail-closed test; the four-step ingress shape: this profile | 4, 6 |
| P4a (independent), P1 (independent), P6 (independent); I2 | steps compose only through declared result types and domains (P4a), and meaning holds only under a declared contract (P1); meaning held in closed typed carriers, explicit return values and small composed transforms can be checked, while meaning in open payloads, implicit `Any` or untyped definitions cannot (I2), so the latter are not typed design; a typing claim needs its evidence (P6), so a boundary whose strict checker does not run cleanly is not yet implementation-conformant | [§4](#4-functional-bias-and-typing) | the preferences and avoidances at "should" force, the Python rule, the requirement of a strict checking pass, and the conditions for `Any`, `cast` and `# type: ignore`: this profile; which strict checker and its configuration: the project | 4, 3 |
| P1 (independent), P3 (independent), P6 (independent); F10 imported; I1 | the constitutional WHAT owns Product meaning (F10) and no realisation mints authority (P6), so a new or materially changed semantic boundary derives its semantic model from one accepted Ontology subordinate to that WHAT, and implementation cannot self-ratify missing Ontology authority; identities are declared and survive change (P3), so the Ontology carries stable identities and a basis that makes staleness decidable; a projection keeps meaning only through a declared contract (P1), so every design projection traces to the Ontology, an untraceable element is ungrounded, and a realisation derived from a reference line shows its derivation, not code comparison alone | [§5](#5-ontology-first-design), its opening, [Ontology projection](#ontology-projection); [§6 Reference-derived module design](#reference-derived-module-design); [§7 Ontology evidence](#ontology-evidence) | the ten terms of the Ontology, the definition of a material semantic boundary and the evidence items: this profile; who accepts the Ontology: the design authority ([§7 Gate and retrospective work](#gate-and-retrospective-work)); proportionality: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality); the invalidators, of which a reprice is an instance: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse) | 1, 2, 6 |
| P2 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated), P6 (independent); I3 | implementation output is a candidate until evaluated (P0) and evidence does not mint authority (P6), and a later actor does not hold the design reasoning (I3), so a material relation that implementation fixes before design acceptance becomes a decision no one owns; adequacy is set by the outcome (P2), so where no material alternative remains a prior gate adds nothing; hence design, implementation and tests may evolve together only while the boundary is decision-complete, otherwise the affected design decision is accepted before retained implementation establishes it, and implementation is evidence about the design, never authority over it | [Proportional design sequencing](#proportional-design-sequencing); [Decision-complete symbolic design](#decision-complete-symbolic-design) | the nineteen terms of `M(B)` and the predicates `decision_complete(B)` and `co_evolution_admissible(B)`: this profile; the proportionality relation that selects between the two modes: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | 4, 9 |
| P4b (derived), P0 (recovered); F2 imported; I3 | a bounded design action is one transition inside a frame that does not own the relations its lawfulness depends on (P0, F2), and its actor does not hold the reasoning behind those relations (I3), so the relations must be recorded where it can re-acquire them (P4b); hence the action is evaluated against every governing frame it derives from, a result that changes a governing relation re-enters at that relation, and the selected method basis with the accepted design suffices, without conversation history, to decide whether the action preserves, changes, duplicates or violates each governing relation in its affected set | [Bounded frame conservation (UP-017)](#bounded-frame-conservation-up-017); [§7 Invariant reconstruction sufficiency (UP-018)](#invariant-reconstruction-sufficiency-up-018) | the five frame items, the four decisions and their core values: this profile; reconstruction without history: [ACTIVATION §1 Intake](ACTIVATION.md#intake); the seam rule: [ACTIVATION §1 Execution unit](ACTIVATION.md#execution-unit) | 7, 3 |
| P2 (independent), P5 (derived), P6 (independent); I4 | a design is adequate only if its outcome can be realised (P2), and success cannot be reported on a capability the substrate lacks (P5), so a design whose substrate cannot natively construct it is not acceptable, and the missing capability stays an explicit gap or re-enters; a mechanism can come from several sources (I4), and unknown evidence supports no claim (P6), so a material generic capability or dependency is chosen by a bounded, recorded discovery and comparison that eliminates on hard failures, keeps unknowns unknown and selects no dominated candidate; reuse confers no authority (P6) | [Native constructability (UP-002)](#native-constructability-up-002); [Capability and foundation selection (UP-023)](#capability-and-foundation-selection-up-023) | the substrate and the evidence mechanism: the consumer; the candidate sources and comparison dimensions: this profile; the priorities and risk tolerances that resolve a frontier: declared for the exact Product and applied by its existing trade-off owner; whether one implementation serves several instances: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery, which this procedure refines; what creates no authority: [FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds); invalidation of selection evidence: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse) | 4, 9 |
| P3 (independent), P5 (derived), P4a (independent) | an entity keeps its declared identity across admissible change (P3), so every lifecycle question of an entity (declare, read, update, retire) has an answer; a step cannot report success on a case it did not decide (P5), so silence is no answer: each question is answered by a lawful function, declared `not_applicable` with a reason, or named as an owned gap, and each discovered functionality item is derived, deferred, excluded or a named gap; steps compose only under declared types (P4a), so higher-order behaviour names its composition and effect algebra, and no private helper becomes an undeclared constructor | [Entity and lifecycle completeness](#entity-and-lifecycle-completeness); [Atomic functions and higher-order composition](#atomic-functions-and-higher-order-composition) | the matrix columns, the lifecycle readings at "should normally" force and the row dispositions: this profile; what a `not_applicable` entry is: [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), Exclusion and the core; the composition and effect algebra: the project, such as GTL and ABG under [ODD](ODD.md#1-position) | 2, 3, 4 |
| P6 (independent), P4b (derived); F1, F2 imported | authority permits only within its scope and is never minted by actor, capability, composition or projection (P6; F1, What creates no authority), so authority is part of the Ontology, actor and capability are not authority, and a composed function has no more authority than its inputs and constituents; an admission decision is a step-produced fact the outer contract needs (P4b), so each consequential entity-transition domain has one complete admission relation, with every competing path explicitly related to it | [Authority model](#authority-model); [Transformation admission completeness (UP-016)](#transformation-admission-completeness-up-016) | the authority roles, the named typed transition and owning admission boundary that carry an explicit authority decision in the design, and the fields of the admission relation: this profile; the list of what creates no authority: [FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds); admission and standing-qualification semantics: [ACTIVATION §4](ACTIVATION.md#complete-enclosing-relation-admission); authority identity: [IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004) | 9, 4 |
| P3 (independent), P6 (independent), P2 (independent) | a semantic meaning has one declared identity and owner (P3), so a realisation unit that introduces, duplicates or reinterprets it makes one meaning two; hence a top-level unit is Prime-conformant only when it projects accepted Prime atoms, each governing its declared domain, and adds no semantic authority (P6); a design is judged by the outcome it serves (P2), so contraction covers the whole candidate family, preserves root authority, and does not succeed when it increases authority centres, truth surfaces or review burden | [Prime semantic atoms and admitted domain](#prime-semantic-atoms-and-admitted-domain); [Whole-family Prime contraction](#whole-family-prime-contraction); [Recursive Prime and root conservation (UP-003)](#recursive-prime-and-root-conservation-up-003); [§6](#6-prime-law); [Boundary and governance cost (UP-005)](#boundary-and-governance-cost-up-005) | the Prime vocabulary, the review questions of contraction and the typical lawful reasons for a top-level unit: this profile; weighing ambiguity removed against reasoning complexity: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | 4, 2 |
| P3 (independent), P2 (independent); F6 imported | a carrier is an identity-bearing boundary, which is a claim with a proof obligation (P3), and a carrier with no route to the boundary's functionality or authority flow is unjustified (P2), so a schema or typed boundary declares from the accepted Ontology the smallest carrier set for that functionality and authority flow, any other shape is subordinate unless it passes a declared test, and extra boundaries are design debt; a revision changes a claim about the whole set, which is assessed on its whole basis (F6), so a revision re-derives the whole set and reruns its gates over all of it | [Irreducible architectural carrier set](#irreducible-architectural-carrier-set); [IACS revision](#iacs-revision); [Promotion test](#promotion-test); [Boundary inflation prohibition](#boundary-inflation-prohibition) | the IACS, Subordinate Payload, Promotion Test and Boundary Inflation terms, the six example roles and the five promotion grounds: this profile; the assurance law a revision consumes: [EVALUATION §1](EVALUATION.md#1-claims) | 4, 2 |
| P1 (independent), P5 (derived), P6 (independent); F3 imported; I3 | a view is a representation, not the meaning (P1), so each of three distinct views is a fidelity-checked projection of the accepted Ontology, not a peer truth surface, and a later actor reads the behaviour from them, not from memory (I3); a gate cannot report success on an axiom it did not decide (P5) and needs evidence for each claim (P6), so before promotion or a design-method closure claim every applicable axiom is evaluated across the views, and each verdict maps to one core value of F3; an axiom that does not apply satisfies only the declared disjunction and never counts as met | [§7](#7-ontology-and-three-view-design-gate); [Domain model](#domain-model), [Sequence model](#sequence-model), [State model](#state-model); [Cross-view axiom evaluation](#cross-view-axiom-evaluation) | the three Mermaid views, the stereotypes, the ten matrix columns, and the axiom verdicts with their disjunctive predicate: this profile; another text-native format: the project's ratification; applicability and exclusion: [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), Exclusion and the core | 6, 3, 9 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated); F3, F4, F6 imported | a produced design pack is a candidate until evaluated (P0), and acceptance is the owner's disposition, distinct from assessment (P6, F6), so the Ontology verdict and the design verdict are the design authority's dispositions at the design gate, and no assessment result or produced pack is the verdict; a combination with a non-satisfied mandatory result or a gap is never `satisfied` (F3), so without both verdicts `accepted` a new or semantically changed boundary is not promoted, published or closed, and implementation under co-evolution stays provisional evidence until the gate is accepted; an unchanged consumer reuses a closed result (F4), so an unchanged `realization_refactor` reuses its verdict on a proof of no delta | [Gate and retrospective work](#gate-and-retrospective-work) | the design gate as the acceptance boundary of a semantic boundary: this profile; the decision owner: the design authority that accepts the Ontology (§5); the dispositions and their core values: [ACTIVATION §3](ACTIVATION.md#disposition) | 9, 3 |
| P1 (independent), P3 (independent), P6 (independent); I2 | domain views do not show the machinery that realises them, and similar code can carry different meanings (I2); representation is not meaning (P1) and identity is declared, not read from shape (P3), so similarity yields only a commonisation candidate, a materially non-equivalent law requires separation, and at a material semantic boundary the design projects its computational realisation, giving each material algorithmic obligation a semantic and a realisation disposition; reuse mints no authority (P6), so a local realisation does not present an accepted relation as newly owned | [Computational realisation projection (UP-019)](#computational-realisation-projection-up-019) | the two-part disposition and its values: this profile; supported workloads and acceptance limits: the Product; the separation of costs: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality); shared machinery: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) | 4, 3, 6 |
| P0 (recovered), P1 (independent); I3 | a finite actor reasons over a bounded unit (P0), and later actors do not hold the design reasoning (I3), so modules are realisation-level units that bound traversal reasoning and are classified by role; the tier-2 assurance law names objects this profile defines, and each name keeps one meaning only under a declared binding (P1), so the binding at the head maps those names to this profile's objects, and the assurance law applies to them unchanged | [§9](#9-module-taxonomy); the binding at [the head of this member](#design_module) | the six module roles, at "recommended" force, and the binding: this profile; the design-to-module evidence route, module-derived unit tests and module lifecycle confirmation: [ASSURANCE §14 to §16](ASSURANCE.md#14-design-to-module-evidence-route) | 4, 1 |
| P3 (independent), P5 (derived); I2 | a value keeps its identity only across admissible change (P3), so source truth held in values that change only by admitted transition keeps one identity, while shared mutable state can change it unobserved (I2); a function with no outcome for part of its domain would report success on a case it did not decide (P5), so semantic functions should be total or as close to total as the language and problem allow | [§10](#10-realisation-rules): [Immutable carriers](#immutable-carriers), [Totality](#totality) | typed immutable values as the preferred carrier, at "should" force, and the justifications for mutation: this profile; the outcome values of a semantic function: the Product, as its domain values | 4, 2 |
| P6 (independent), P1 (independent); I2 | code can decide one meaning in several places (I2), and each further place is a possible rival authority (P6) whose reading has no declared contract (P1), so effects should be explicit and isolated at the edge, no controller should be the hidden semantic centre, and coupling should be reduced by dependency shape, so fewer places can invent meaning | [Effect edge](#effect-edge), [No semantic centre](#no-semantic-centre), [Coupling](#coupling) | the typical edges, the preferred sequence and the dependency direction, at "should" force: this profile | 4, 9 |
| P0 (recovered, with its boundary commitment), P6 (independent) | the method governs a step's boundary and not an actor's internal path (P0's boundary commitment), and authority acts only within its scope (P6), so a boundary that governs, observes or evaluates another actor publishes state, boundary and admissible routes, not strategy, unless strategy is part of its ratified responsibility | [Governance and strategy separation](#governance-and-strategy-separation) | the seven lawful publications and the four drifts: this profile | 9, 4 |
| P2 (independent), P6 (independent) | a change is justified by the claim it serves (P2), and a change outside that claim acts beyond the authority admitted for it (P6), so clean-up is lawful only when boundary-local and neutral in behaviour, authority, visibility and effect, and a cross-boundary opportunity is repricing input for its owner | [Opportunistic optimisation](#opportunistic-optimisation) | that clean-up should leave an opened boundary better, at "should" force, with its conditions and examples: this profile; admission of follow-up work: the owning authority at the smallest re-entry point ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)) | 1, 9 |
| P2 (independent), P3 (independent); I4 | similar computation recurs (I4), and each further local rebuild adds cost with no new route to the outcome (P2), while similar code does not establish one identity (P3), so a credible recurrence yields a commonisation review, never an automatic merge | [Recurrence extraction](#recurrence-extraction) | the rule of two, the third-rebuild threshold and the commonisation order: this profile; ticket-level recording: [TICKETS §6](TICKETS.md#recurring-realisation-and-library-declaration); whether one implementation serves several instances: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery | 4 |
| P6 (independent), P2 (independent); F3, F4, F6 imported | a closure claim needs evidence for the exact claim, and implementation status is not that evidence (P6, F6), so a bounded check reconstructs the function of the exact claim before the claim is made, reusing accepted evidence only under the reuse law (F4); a falsified claim is never `satisfied` (F3), so an issue that falsifies the claim or an applicable hard stop blocks the design-method closure claim; a discovery outside the claim has no route to that claim (P2), so it is repricing input, not scope | [Post-ticket design review](#post-ticket-design-review) | the check's five determinations as domain triggers and the absorption conditions for boundary-local clean-up: this profile; when a finding blocks current promotion: [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion); reuse and its invalidators: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); ticket status and closure mechanics: [TICKETS](TICKETS.md) | 9, 1 |
| P6 (independent), P1 (independent) | a meaning has one owner (P6) and is read through a declared contract (P1), so each interface family has one authoritative source truth that downstream interfaces consume, and a proxy that keeps an old authority path behind a new surface leaves two owners for one meaning, which is bridge debt | [Interface bleed prohibition](#interface-bleed-prohibition); [Proxy interface prohibition](#proxy-interface-prohibition) | retained compatibility with its own authority and proof: the project's design; the bridge prohibition: [SPEC_METHOD §7](SPEC_METHOD.md#bridge-prohibition) | 9, 6 |
| P6 (independent), P1 (independent), P2 (independent) | a design claim needs evidence (P6), so review checks the rules above for the boundary; a question that the carriers and transforms cannot answer shows meaning held outside a declared contract (P1), a realisation too coupled or too imperative; a prompt clause that enforces design law is justified only by its route to the behaviour it governs (P2), so it needs provenance and proof that it still causes or prevents that behaviour | [§11](#11-review) | the 56 questions, the 43 checks and the 14 hard-gate checks: this profile; prompt construction: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) | 9, 4 |
| P6 (independent), P2 (independent); F12 imported; I1 | an optional profile governs a boundary only where the authority that may adopt it has adopted it (P6, F12), so the project applies it consistently across the named boundary; a completion claim needs its evidence (P6), and obligations follow the boundary's outcome (P2), so a design-method completion claim for a new or materially changed boundary needs its declared or cited Ontology and evidence, and partial adoption names the adopted boundary and rule family and claims no completion whose evidence it skipped | [§12 Adoption](#adoption); [the head of this member](#design_module), which declares the profile optional | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the adopted boundary and rule family: that authority; the means of recording adoption, at "may" force: this profile | 1, 9 |
| P3 (independent), P6 (independent); F8 imported | identity is declared by its authority (P3, F8) and a default confers no authority (P6), so identity generators, validators and normalisers that a runtime realisation publishes are defaults, which the owner of the identity can override | [Identity defaults from a bound runtime realisation](#identity-defaults-from-a-bound-runtime-realisation) | the permission for a consumer-bound realisation of the ABG role to publish defaults for its own runtime surfaces and the default surface kinds, limited to that role: this profile; the defaults' standing and the override law: [IDENTITY §7](IDENTITY.md#7-default-formats-and-overrides) | 2 |

Consumers outside this member that apply these rows, each keeping its
owner: [ASSURANCE §14 to §16](ASSURANCE.md#14-design-to-module-evidence-route)
apply the module-taxonomy row through the binding at the head;
[UX](UX.md#1-position) refines the §4 and §10 rows for modules that
realise a UX surface ([PROFILES §4](PROFILES.md#4-ux)); TICKETS §6
records the recurrence row at ticket level;
[FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) Shared machinery is refined for
software design by the capability-selection row; and
[ACTIVATION §1 Intake](ACTIVATION.md#intake) uses the design evidence of
the frame-conservation row when this profile governs the boundary.

The table accounts for this whole member: the head, §1 to §12 and the
binding the head declares; §13 records dispositions and decides nothing.
Its Pillar column follows FOUNDATIONS §3. It is new in this corpus and has
no rc.2 row. Purpose and material relation: a reader of this profile sees
which of its rules rest on the commitments and imported families and which
are choices this profile, the adopting Product or another owner makes, so
no profile choice is presented as following from the foundations (P6, P2).


```


## `standards/ODD.md#foundation-to-law` (lines 77-169)

```markdown
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
| P3 (independent), P4a (independent); I2 | the product's states and transitions are declared: each bounded state is a node over explicit typed assets with a declared identity, never one hidden workspace object, and each admissible transition is a vector that declares its required upstream assets, target, evaluators and gates, and output contract; the work is a traversal that takes one admissible vector at a time until the selected target closes | [§5](#5-graph-model), with [Nodes](#nodes), [Vectors](#vectors) and [Traversal](#traversal); [§11.1](#111-typed-assets-and-nodes-are-explicit) | the graph as the product's process model and traversal as its workflow, and `asset_surface` as the declaration of a produced or consumed boundary: this member; which nodes, vectors and assets a product declares: the product | 5, 2, 3 |
| P0 (recovered), P6 (independent); I3; F2 (imported) | within one bounded step the worker's internal path is its own and the traversal contract is its admissible external space; the worker cannot close the edge, emit runtime events, mutate ledgers or decide re-entry, because its output is a candidate until evaluated and its report is an observation, not authority | [§5 Probabilistic compute](#probabilistic-compute); A5 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | one vector or edge traversal as the bounded step, declared as a binding in §5 Probabilistic compute: this member | 5, 8, 9 |
| P1 (independent), P3 (independent); F9 (imported), F11 (imported) | this profile's traversal and its F_D, F_P and F_H shorthands are concepts of its own bounded context: they are not the `a_c` traversal record or functor kinds by equal spelling, and F_P and F_H relate to the source concepts of SPEC_METHOD §5 only through declared specialisations that state direction, preserved meaning, narrowed scope and invalidation | this member's lead; [§1](#1-position), the bounded-context paragraph; [§5 Probabilistic compute](#probabilistic-compute) | the bounded context and the F_P and F_H specialisations: this member, under PROFILES §1 | 5, 6 |
| P4a (independent), P4b (derived from P0 and P2); F2 (imported) | a graph function realises an outer vector, which stays the callable contract; where the function refines that vector into inner steps, the inner boundaries are published, a later step reads earlier outputs only through its declared environment, and the loop governs each published inner boundary as it governs the outer one | [§5 Graph functions](#graph-functions); [§11.4](#114-the-gtl-module-is-the-operative-publication-surface), second paragraph; [§11.8](#118-cumulative-environment-law-is-mandatory); A14 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the cumulative carried environment as the specialised contract for carrying earlier outputs, with its three declarations at "should": this member | 5, 3, 4 |
| P0 (recovered), P3 (independent), P6 (independent) | every operative constructive step has a named, typed and published carrier that a later actor and the runtime can re-acquire, because a later actor holds declared sources and not another actor's private memory, and no undeclared surface carries authority; no operative step, callable surface or capability stays only in prose, prompt memory, an orchestration loop or a service method, and a caller binds to the published outer carrier, never to a hidden inner vector | [§11.2](#112-graph-functions-are-the-primary-constructive-carrier); [§11.3](#113-the-function-catalogue-is-published); [§11.4](#114-the-gtl-module-is-the-operative-publication-surface), first paragraph; [§8](#8-responsibility-layers-and-local-binding), last paragraph | `GraphFunction` as the carrier; a machine-readable function catalogue whose retained functions should expose at minimum name, inputs, outputs, intent and public or helper role; the GTL module as the publication surface: this member; which functions, graphs and catalogue entries a product publishes: the product | 5, 4, 1 |
| P0 (recovered), P6 (independent); I3 | imperative code transports or persists facts and decides nothing that the declared carrier owns: domain meaning, semantic target movement, step selection, closure, lineage and constructive workflow truth, because what is decided only in imperative code is decided by no declared owner | [§11.2A](#112a-outcome-first-realisation-order); [§14](#14-dogfooding-rule) | the order outcome traversal, declarative carrier, minimal adapter code, with the outcome traversal's declarations; building the product's own framework behaviour through its graph functions: this member | 5, 4 |
| P6 (independent), P0 (recovered); I3; F2 (imported) | each traversal has exactly one execution authority, which owns its selection and advance, actor invocation and supervision, retry, continuation and re-entry, runtime events and closure fold; a bounded step, product code, a plugin, a service or a query returns evidence, policy input and control and holds none of these, so two controllers that can each claim one traversal leave the product not ODD-correct | [§10 ABG](#abg), [ODD product](#odd-product) and [Query and service layers](#query-and-service-layers); [§11.5A](#115a-abg-owns-continuation-and-re-entry); [§11.5B](#115b-execution-authority-audit); A15 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | ABG as the role of that single authority, with its ownership list and the product's; the five-surface audit inventory, the changes that require the audit and the conditions that prevent closure: this member; the concrete realisation of the ABG role: the consumer (§1) | 5, 8, 9 |
| P6 (independent), P1 (independent), P3 (independent) | model synthesis, gap discovery, next-action selection and action evaluation hold separate authorities, and no command, report, query, service or summary becomes a rival source of traversal truth; visible state is a projection that reconciles to the admitted truth it reads or fails closed, and equal names establish no identity | [§11.5](#115-current-state-is-a-projection-over-constructive-history); [§11.5C](#115c-projection-source-coherence); A0, A4a, A11, A12, A16 and the constitutional equation in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the four functions `synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action`, and the duty of a design, ticket, module or proof to name the one it implements or consumes: this member; domain asset meaning, catalogue meaning and gap interpretation: the product (A15) | 5, 6, 9 |
| P6 (independent), P0 (recovered); I2, I3; F2 (imported), F6 (imported) | no edge closes from an artifact, a worker report, process success or liveness alone; closure is a fold over admitted evidence, the workspace counts only through the ledger, and an evaluator attends only to admitted ledger rows reachable through declared lineage, because a report or artifact is an observation, not authority, and a step's context is its declared material, never the workspace | A1, A1a, A1b, A6, A7 and A10 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | the governed work pair of workspace, ledger, event log and evaluator work, and the ledger's fields: this member; carrier names other than those of the loop: the implementation, which keeps the authority shape (§11.5D) | 5, 7, 9 |
| P4b (derived from P0 and P2), P3 (independent); I2; F4 (imported) | every closure-relevant callout is admitted to the immutable ledger and event log, a correction appends or supersedes and never rewrites, and every closure decision and next-action selection is reproducible by replay from carriers that each reference their causal predecessors | A1a, A13 and A13a in [§11.5D](#115d-constructive-evaluation-and-yield-loop); [§11.5](#115-current-state-is-a-projection-over-constructive-history) | the replay inputs listed in A13 and the predecessor chain of A13a: this member | 5, 2, 9 |
| P5 (derived from P0 and P6), P0 (recovered); F4 (imported) | work that is still lawful but not yet decided returns control without failure classification, keeping the same edge and a replay-visible resume basis | A9, and A4 on `post_yield_resume`, in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | `yield` as the lawful iteration boundary, distinct from retry, block and timeout: this member | 5 |
| P2 (independent), P6 (independent); I1; F10 (imported), F11 (imported) | the selected outcome bounds the loop: every action binds the current gap to exact target assets and obligations before invocation, only published lawful actions are ranked, no further material work is selected without another admitted basis once a terminal condition of the loop is reached, and a reprice requests constitutional re-entry and selects nothing; edge closure is evidence toward Product acceptance, not acceptance | the selected-outcome paragraphs, the intent-lineage paragraph, A2, A3, A4 on `post_reprice` and A16 in [§11.5D](#115d-constructive-evaluation-and-yield-loop) | which outcome is selected and accepted: its owner under [SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation); the re-entry a reprice requests: its owning relation under SPEC_METHOD §4 | 5, 1 |
| P5 (derived from P0 and P6), P6 (independent); F3 (imported) | the closure decision is a closed sum type and `evaluate_next` is total; each closure decision and each audit outcome maps to exactly one core value for a named predicate, its cause being part of the value where the cause decides it; a closure decision answers the edge predicate and is not a disposition of ACTIVATION §3, which answers the acceptance predicate, so neither counts toward the other; a selection maps to no core value | A4, A8 and its mapping in [§11.5D](#115d-constructive-evaluation-and-yield-loop); the audit mapping in [§9](#9-method-governance-and-audit) | the seven closure decisions, their causes and the default of graph following in A4: this member; the priority policy: the product (A15) | 5, 3, 9 |
| P6 (independent), P1 (independent), P3 (independent); F12 (imported) | each part of an ODD product has one owner: one WHAT surface, one HOW relation, runtime truth with the traversal authority and domain meaning with the product; the split binds by authority and not by directory names; a runtime frame's name does not enrol it among the evaluation frames, and an evaluation frame may take a runtime frame as its subject or coordinate without collapsing the two | [§10](#10-what-an-odd-product-is), with [Product specification](#product-specification-software-development-topology) and [Product realisation](#product-realisation-software-development-topology) | the ten-part application boundary and `specification/` and `build_tenants/` as the default software-development locations: this member; the actual locations: the product's definition under PRODUCT_DEFINITION | 5, 1, 7 |
| P1 (independent), P2 (independent), P6 (independent); F10 (imported) | this profile decides graph-native structure and product shape and neither a product's domain semantics nor its current line: domain-correct work also needs the constitutional chain, the domain method's semantic law and the product's local authority surfaces, and where a product also adopts a domain profile, each governs its own questions and the two compose | [§2](#2-method-role); [§3](#3-method-composition) | the split between graph-native structure and product shape, owned here, and world-model semantics, publication and composition law, owned by [WORLD_MODEL](WORLD_MODEL.md#1-position); which domain method and local surfaces apply: the product | 5, 1, 2 |
| P0 (recovered), P2 (independent); F1 (imported) | an actor building an ODD product acquires the general method, the product's domain method where one exists, and its local authority surfaces before it acts, then identifies and declares the graph carrier and loop, and implements code last, because it holds only the declared sources it acquires and the selected outcome sets which obligations matter | [§17](#17-invocation-rule); [§18](#18-cold-start-reading-order) | the fourteen-step sequence and the two reading orders, with "usually" for the effect of skipping the order: this member | 5, 1, 7 |
| P6 (independent), P2 (independent); F11 (imported) | a structural pattern becomes shared law only when this profile is changed, so usage and repetition approve nothing; a move the profile does not clearly cover is evaluated against it, and a move found worth incorporating is not fully approved until the profile is updated | [§9](#9-method-governance-and-audit) | the audit questions, at "should", and the three audit outcomes: this member; a change to this profile: the method's change management (SPEC_METHOD §4) | 5, 1, 9 |
| P1 (independent), P3 (independent) | shared structural law and a product's local semantic bindings stay distinct: a capability class is a layer idea that each product binds to its own typed assets, and copying another product's local names without semantic need is not reuse of the method | [§8](#8-responsibility-layers-and-local-binding); [§11.6](#116-product-specific-semantics-sit-above-the-shared-carrier) | the capability classes listed, as examples: this member; local asset names, asset meanings, proof lanes and query overlays: the product | 5, 6, 1 |
| P6 (independent); F6 (imported) | ODD, GTL and ABG name capability roles, not a required implementation; a consumer, a reference realisation or a historical product may prove or falsify conformance and supplies no method authority, because evidence never mints authority | [§1](#1-position), the paragraphs on roles and on consumer binding | the concrete realisations of the GTL and ABG roles: the consumer, in its own Product, requirements, design and immutable dependency identity | 9, 5, 8 |
| P0 (recovered), P6 (independent); I3; F13 (imported) | automation decides nothing that the declared surfaces do not: each automated move is one an actor holding only those surfaces could make, because a later actor re-acquires declared sources and not private memory, and authority comes only from declared owners; an agentic worker's artifacts take effect only through admission against deterministic criteria, and conformance evidence is not ratification | [§11.7](#117-manual-walkthrough-must-still-be-lawful); [§11.7A](#117a-conforming-agentic-development) | the manual walkthrough as the test of automation, and its agentic form as the conformance proof of the method: this member; the admission criteria for produced artifacts: [SPEC_METHOD](SPEC_METHOD.md) and [TICKETS](TICKETS.md) | 5, 9, 7 |
| P6 (independent), P5 (derived from P0 and P6); F6 (imported) | negative evidence for a boundary exercises the supported authority path with the real authority-bearing input invalidated and shows refusal before the prohibited effect; a manufactured refusal, blocked event, gap or verdict proves nothing about that path, and absence in source, package, installation and runtime are distinct claims | [§11.7B](#117b-real-authority-path-negative-proof-stdo-up-010) | the concrete test and evidence mechanism: the consumer | 9, 5 |
| P3 (independent), P6 (independent); I4; F15 (imported) | the installed builder and the product it builds, and the selected immutable release and mutable source, are distinct identities with distinct authority: the selected release governs a consumer and mutable source governs none, a mismatch is repaired by installing one complete release, a release version is no graph truth, and where an installable development form exists, decisive proof runs against it | [§4](#4-method-library-classes); [§7](#7-self-host-boundary); [§13](#13-installed-dev-rule); [§15](#15-release-boundary) | which release a consumer selects: the consumer ([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)); which members are method members: the [standards README](README.md#documents); the isolated environment and the proving lane of §13, at "should": this member | 1, 2, 9 |
| P6 (independent), P3 (independent); F12 (imported) | the installed product provides the method, runtime and carrier surfaces and assumes no knowledge of a target project's domain; the target project owns its definition, constitutional surfaces, realisation roots and domain outputs | [§6](#6-product-boundary) | the default scaffold names and `build_tenants/` as the default realisation root: this member, as defaults; the target project's domain, surfaces and outputs: the target project | 1, 5 |
| P4a (independent), P2 (independent); F3 (imported) | a refined inner chain closes the enclosing carrier only when the enclosing contract still holds after fold-back and zoomed and unzoomed views agree; a live requirement without a proof witness is a gap that keeps the enclosing carrier open until it is realised, deferred or repriced out of the active branch; a scenario bundle should make clear the boundary, assets, vectors, paths and evidence that close it | [§11.9](#119-global-convergence-must-be-stable-under-zoom); [§12](#12-scenario-rule) | which scenarios a product keeps and which proof witness fits a requirement class: the product; deferring or repricing a requirement out of the active branch: the requirement's owner | 5, 3, 9 |
| P5 (derived from P0 and P6); F3 (imported) | an ODD product is built correctly only when every clause of §11 holds: the clauses form a conjunction, so one failing or unestablished clause leaves the product not built correctly | [§11](#11-core-law), its lead | which clauses make up the core law: this member | 5, 3 |

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
