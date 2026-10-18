# I5-03 reading batch 13

Rows: 28. Members: ['SPEC_METHOD.md', 'STDO_REFERENCE_FRAME_BASELINE.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `SPEC_METHOD.md#universal-intake-triage` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#universal-intake-triage` at rc.2:

```text
### Universal Intake Triage

There is one front door for substantive change.

The intake label does not determine the process class.

That means a reported:

- bug
- feature request
- issue
- regression
- operator finding
- release blocker
- scenario failure

all enter through the same intake-triage process.

Intake triage must determine:

- whether the report represents a substantive change at all
- the affected product boundary and intended scope
- the lawful change class
- the lawful re-entry point into the constitutional chain
- the downstream surfaces and evidence that must be repriced, re-derived, or
  re-proved
- whether the work remains within the currently declared release scope or
  requires repricing of that release plan

No bug, feature, issue, or other intake may bypass this triage by going
straight to code, tests, or release handling.

The purpose of triage is not to create a separate tracking bureaucracy. It is
to classify impact correctly so the change enters the method at the right
constitutional boundary.

Triage triangulates a failure across applicable reference frames over the same
subject and basis. Each frame tests candidate diagnoses against its material
workspace variables, governing relations and evidence. Their combined results
constrain the supported cause, preserve unresolved alternatives and uncertainty,
and identify the smallest sufficient lawful scope of repair. The frame that
exposes a failure need not contain its cause. Repeating the same analysis under
different frame names supplies no additional causal evidence.

Use the smallest sufficient applicable frame configuration under
[frame applicability and conjunction](REFERENCE_FRAME_METHOD.md#method-functions), with
[causal localization](STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization)
where required. This does not prescribe a reviewer count or a new review round;
required independence remains intact. A diagnosis does not grant repair effects
or establish that governing meaning must change: a candidate may instead need
correction under sufficient existing law.

The minimum lawful change classes are:

- `goal_reprice`: current bounded work-wave focus changes; re-enters at Goals and may flow through Intent, Product, Requirements, Design, Code, and Evidence where that focus changes deeper constitutional truth
- `intent_reprice`: directional or scope change; re-enters at Intent and flows through Product, Requirements, Design, Code, and Evidence
- `product_reprice`: current product realization changes while directional intent remains stable; re-enters at Product and flows through Requirements, Design, Code, and Evidence
- `requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Code, and Evidence
- `design_reframe`: realization structure changes while active intent and requirement truth remain stable; re-enters at Design and flows through Code and Evidence
- `realization_refactor`: local code, configuration, or attribute change with no intended constitutional or structural change; re-enters at the realized surface only and must prove no upstream drift

Smaller changes may re-enter below Goals only if they explicitly assert that no
upstream constitutional surface is changing.

The absence of a declared change class is process drift.
```

Successor, `SPEC_METHOD.md#universal-intake-triage`:

```text
### Universal intake triage

There is one front door for substantive change. The intake label does not
determine the process class: a reported bug, feature request, issue,
regression, operator finding, release blocker or scenario failure all enter
through the same intake triage (P2, P6; rc.2 #universal-intake-triage).

Intake triage determines six things: whether the report represents a
substantive change at all; the affected product boundary and intended
scope; the lawful change class; the lawful re-entry point into the
constitutional chain; the downstream surfaces and evidence that must be
repriced, re-derived or re-proved, a determination whose evidence part is
the selection `S_Δ` over the impact cover `I(Δ)` of the affected surfaces
([FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse));
and whether the work remains within the
currently declared release scope or requires repricing of that release
plan. No bug, feature, issue or other intake bypasses this triage by going
straight to code, tests or release handling. The purpose is not a separate
tracking bureaucracy; it is to classify impact correctly so the change
enters the method at the right constitutional boundary.

Triage diagnoses among the four causes of
[ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation),
a defective realisation, an inadequate governing requirement or design, an
inaccurate predictive model, and insufficient observation, and routes each
supported repair to the owner of its cause rather than inferring it from
the intake label; severity and priority follow the policies that
[TICKETS](TICKETS.md) owns; a bug list projects existing work state. This
paragraph applies ACTIVATION §1 Feedback and diagnosis and states no
second relation (P2, P6).

Triage triangulates a failure across the applicable reference frames over
the same subject and basis. Each frame tests candidate diagnoses against
its material workspace variables, governing relations and evidence; their
combined results constrain the supported cause, preserve unresolved
alternatives and uncertainty, and identify the smallest sufficient lawful
scope of repair. The frame that exposes a failure need not contain its
cause. Repeating the same analysis under different frame names supplies no
additional causal evidence. The smallest sufficient applicable frame
configuration is used, under frame applicability and frames in conjunction
(REFERENCE_FRAME §5 and §6). The frames' results combine under the one
[conjunction of results](FOUNDATIONS.md#conjunction-of-results): each
keeps the diagnosis it evaluated as its predicate, a counterexample that
one frame finds survives the join, and a frame planned and not applied
leaves its diagnosis open, never ruled out. Counterexample localisation
applies where required (ASSURANCE; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#counterexample-localization). This prescribes no reviewer count and no new
review round; required independence stays intact. A diagnosis grants no
repair effects and does not establish that governing meaning must change: a
candidate may instead need correction under sufficient existing law (P6).
```

Successor, `SPEC_METHOD.md#change-classes`:

```text
### Change classes

The minimum lawful change classes, each with its re-entry point and the
layers its repricing flows through (P4b, P2):

| Class | Change | Re-enters at | Flows through |
|---|---|---|---|
| `goal_reprice` | current bounded work-wave focus changes | Goals | Intent, Product, Requirements, Design, Code and Evidence where that focus changes deeper constitutional truth |
| `intent_reprice` | directional or scope change | Intent | Product, Requirements, Design, Code, Evidence |
| `product_reprice` | current product realisation changes while directional intent stays stable | Product | Requirements, Design, Code, Evidence |
| `requirement_reprice` | constitutional truth changes while project direction stays stable | Requirements | Design, Code, Evidence |
| `design_reframe` | realisation structure changes while active intent and requirement truth stay stable | Design | Code, Evidence |
| `realization_refactor` | local code, configuration or attribute change with no intended constitutional or structural change | the realised surface only | nothing upstream; it must prove no upstream drift |

Smaller changes may re-enter below Goals only if they explicitly assert
that no upstream constitutional surface is changing. The absence of a
declared change class is process drift. A changed governing relation is
accepted only at its owner; accepting it inside the acting frame is a
violation whatever the size of the delta (ACTIVATION §1; provenance rc.2
DESIGN_MODULE_METHOD #invariant-reconstruction-sufficiency-stdo-up-018).
Triage records the change intent, the class, the re-entry point and when
triage occurred, wherever substantive work begins.
[TICKETS §4](TICKETS.md#change-class) records the class on the carrier.

The change classes are declared states of a change that intake triage
records, not results, and map to no core value. An evaluation that reads
a declared class returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). A close classification
of [TICKETS §3](TICKETS.md#close-review) that names a layer, such as
`design_reframe`, is a result for its own predicate, mapped there, and
carries the class at which the work re-enters as its domain outcome.
Purpose and material relation: a declared class is never combined as an
evaluation result, so a change classed `realization_refactor` cannot stand
in for a `satisfied` result that no upstream drift occurred (P5, P1).
```


### Row `SPEC_METHOD.md#verification-layers` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#verification-layers` at rc.2:

```text
## Verification Layers

Each layer in the chain preserves a distinct kind of truth:

| Layer | What it preserves | Primary question answered |
|-------|-------------------|---------------------------|
| **Requirements** | Invariant truth | "What must be true?" |
| **Design** | Structural choice | "How is that truth realized?" |
| **Scenarios** | Operational meaning | "Can the realized system actually do the claimed thing?" |

Without scenarios, important capabilities can appear "covered" because the words exist in requirements and design. Scenarios force the sharper question: can the product *really* do the thing? A requirement can say "compositional graphs" and a design ADR can describe Fragment types, but only a scenario asks "can I model a reusable discovery workflow and apply it twice?"

Scenarios are the product-owner layer. They are concrete, end-to-end use cases that validate the chain from intent to realized behavior. When a scenario cannot be written, the capability is not yet real. When a scenario fails, the gap is between the system's actual behavior and its claimed capability — not between the spec's words and the spec's other words.

Scenarios do not replace requirement categories. They primarily validate capability claims and other behavior with concrete operational meaning. Constraints, governance rules, and verification-infrastructure requirements may require different evidence in addition to, or instead of, end-to-end scenarios.

---
```

Successor, `ASSURANCE.md#1-verification-layers`:

```text
## 1. Verification layers

Each layer of the chain ([SPEC_METHOD §2 Constitutional chain](SPEC_METHOD.md#constitutional-chain)) preserves a distinct kind of truth
(P2, P6; rc.2 #verification-layers):

| Layer | What it preserves | Primary question answered |
|---|---|---|
| Requirements | invariant truth | what must be true? |
| Design | structural choice | how is that truth realised? |
| Scenarios | operational meaning | can the realised system actually do the claimed thing? |

Without scenarios a capability can appear covered because the words exist
in requirements and design. Scenarios force the sharper question: can the
product really do the thing? A requirement can name a reusable composable
unit and a design record can describe the types that realise it, but only
a scenario asks whether a user can build such a unit and apply it twice
(P6).

Scenarios are the product-owner layer: concrete, end-to-end use cases that
validate the chain from intent to realised behaviour. When a scenario
cannot be written, the capability is not yet real. When a scenario fails,
the gap is between the system's actual behaviour and its claimed
capability, not between the specification's words and its other words (P2,
P6).

Scenarios do not replace requirement categories. They primarily validate
capability claims and other behaviour with concrete operational meaning.
Constraints, governance rules and verification-infrastructure requirements
may require different evidence in addition to, or instead of, end-to-end
scenarios (P2).

### Foundation to law: assurance and testing

This family (F14 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides what evidence proves a claim about a realised product and how
that evidence is organised. Its instance premises, which the commitments
do not supply, are named in the rows as follows: runnable product, a
product's realisation can be executed or observed, in a source form and in
a deployed, installed or otherwise runnable form, to produce evidence;
composition, a product is composed of modules, interfaces and owners along
causal paths, so its claims range from one module's law to a user's
outcome; users, some claims are about outcomes a user obtains through the
product's supported surfaces; external boundaries, a product or its proof
may depend on workers, transports or fixtures outside its source boundary;
designed modules, a design profile may govern a realisation boundary and
declare module ownership. Each commitment's standing is written as the
table of commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P2 (independent); P6 (independent); instance: runnable product, users | By P6 each layer keeps its own authority, so requirements, design and scenarios preserve distinct truths. By P2 a capability matters as the use it serves, so it is not yet real while no concrete scenario for it can be written, and a failing scenario locates a gap between actual behaviour and claimed capability; scenarios do not replace the evidence other kinds of requirement need. | [§1](#1-verification-layers) | the three layers and scenarios as the product-owner layer: domain choices of this member; the layers of the chain: [SPEC_METHOD §2 Constitutional chain](SPEC_METHOD.md#constitutional-chain) (family F10) | 1, 5, 9 |
| P6 (independent); P2 (independent); P1 (independent); instance: runnable product | By P6 a proof has authority only through what authorises it, so every executable proof surface declares its authority source, and its expected results derive from that authority, never from current implementation behaviour. By P1 and P2 a name or breadth of execution carries no authority, so breadth of execution is not authority, and a project's lane names map back to one taxonomy before closure is claimed. | [§2](#2-testing-strategy-taxonomy) | the two primary authorities, design or module conformance and UAT, the product-assurance bounded context and the terminology list: domain choices of this member; each project's lane names: that project, mapped back here | 4, 9 |
| P6 (independent); P1 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: runnable product, users, external boundaries | By P6 acceptance needs evidence of the claim itself, and by P1 a substitute is not the thing substituted, so acceptance evidence comes only from the composed product form exercised through its declared surfaces, and a substituted external worker or transport proves only the relations exercised. By P5 a claim about the real boundary is undecided without evidence that crosses it, so narrower green lanes are necessary and not sufficient for it. | [§2](#2-testing-strategy-taxonomy), the sandbox paragraphs; [§7 User-acceptance frame](#user-acceptance-frame), last paragraph | the sandbox lane and its harnessed and live modes: domain choices of this member | 8, 9 |
| P3 (independent); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: external boundaries | By P3 a lane binds an exact source boundary, so a required closure lane is reproducible from it: an external dependency is checked in, declared with its acquisition rule, or the lane is classified outside required closure. By P5 a missing fixture means the evaluation was not performed, so it is reported as such, never as a product semantic failure. | [§2 Fixture and proof portability](#fixture-and-proof-portability) | the three admissible forms: domain choices of this member | 8, 9 |
| P6 (independent); P2 (independent); instance: composition | By P6 a proof needs written authority, so every live requirement's proof rests on written, traceable test-case authority. By P2 a behaviour claim is about use, so where a requirement claims meaningful behaviour the proving surface should be an ordered sequence through a coherent use; an undeclared path leaves coverage unjudgeable and an unexercised one leaves the behaviour unproved, so the significant paths are declared and exercised. | [§3](#3-test-authority); [§4](#4-scenario-bundle); [§6](#6-significant-path-coverage) | the scenario bundle and the five usual significant paths: domain choices of this member; the derivation of each test case from admitted work: [TICKETS §7](TICKETS.md#test-case-authority) (family F13) | 1, 5, 9 |
| P6 (independent); P3 (independent); instance: runnable product | By P3 a claim about an installable system binds its installed form, and by P6 a source-level check is evidence of another subject, so the decisive proof runs against an installed development form as an external target, and source-level checks do not replace it. | [§5](#5-installed-dev-proof) | the preference for a fresh sandbox, at "should": a policy choice of this member; the install and development-product roles: [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects) (family F15) | 8, 9 |
| P0 (recovered); P6 (independent); P1 (independent); P4a (independent); instance: composition | By P0 a finite actor evaluates one bounded claim at a time, and by P4a results combine only through declared relations, so where testing frames are selected, testing is a claim-relative set of frames, each bound to one exact claim, subject, path, population, oracle and falsifier, and every result stays bound to its claim. By P1 and P6 a label, runner, count or coverage measure confers no assurance, so a broader frame cannot make a narrower law true, and narrower green results cannot establish an unevaluated broader claim. | [§7](#7-product-testing-frame-set), Terms and The set; [§10](#10-testing-evidence-composition) | the four ordinary frames and their declarations: domain choices of this member; selecting the set for a claim: the governing frame configuration ([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)) or the admitted work authority; the mapping of engagement roles onto the frames: [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) (family F16) | 3, 7, 9 |
| P6 (independent); P3 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: runnable product, composition | By P3 a path claim binds the exact path, and by P5 an absence is shown only by evidence, so a product path claim needs two-sided evidence: the required path witnessed through the supported ordinary path, and each forbidden path absent or refused, in the production graph and in the assurance graph. By P6 equal output is evidence of output, not of path, so equal output through a forbidden path falsifies the path claim. | [§7 Terms](#terms), authoritative Product path; [§9](#9-legitimate-path-and-technical-debt-erasure) | path-sensitive mutation where proportionate and safe: a policy choice of this member | 4, 9 |
| P2 (independent); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P4a (independent); instance: composition | By P2 a test's value is what it decides for the claim, so testing value is the material combinations a frame discriminates for its claim, not a count. By P5 an omitted interaction is undecided, so a reduced covering set is lawful only with a reason why the omitted interactions cannot change the claim, or with them kept as residuals; by P4a and P6 code coverage shows only what was visited. | [§7 Terms](#terms), material combinatorial complexity; [§8](#8-combinatorial-coverage-and-testing-value) | the eight index terms and the nine product factors: domain choices of this member; any scalar score: Product, requirement or accepted-design authority | 3, 9 |
| P6 (independent); P1 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: runnable product | By P6 the owner issues the subject, and by P1 a reconstruction is not the subject, so the assurance subject is the owner-issued subject, acquired through its owner surface, and an evaluator never builds a parallel owner state and evaluates it as the product. By P5 a missing owner projection leaves its claim undecided, so it stays a named gap. | [§11](#11-assurance-subject-acquisition-and-evaluation) | none | 6, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise); P1 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance: composition | By P5 a counterexample locates only as far as its evidence supports, and by P4b it persists until disposed, so it is returned to the earliest causal frontier the evidence supports. By P1 the four forms mean different things, so a unique locus, a joint set, unresolved alternatives and an unbounded frontier stay distinct, each read as one core value; localisation authorises no repair. | [§12](#12-counterexample-localisation) | the four localisation forms: domain choices of this member; any resulting change: the re-entry of [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) (family F11) | 3, 9 |
| P0 (recovered); P1 (independent); P4a (independent); P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent); instance: composition, users | By P0 and P4a each seam is a separately declared relation, so across an interface chain contract sufficiency, boundary congruence, path realisation and user usability are distinct claims with distinct results, and a full usability claim needs all four and their conjunction. By P1 and P5 a seam is evaluated only on its own coordinates, so each seam binds its domains, available context, translation, current observation, actual path and diagnostic cause; by P6 diagnosis grants no repair, and a complete-path result is not replaced by local successes. | [§13](#13-end-to-end-interface-integration-frame), Claim boundaries, Obligations and Computational whole-path evaluation | the frame identity, its twelve elements, the four claims, the six obligations and the ten qualification cases: domain choices of this member; activation: the governing frame configuration or admitted work authority; the family names: [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) (family F16); computational realisation and recurrence law: [DESIGN_MODULE](DESIGN_MODULE.md) (family F17) | 4, 7, 9 |
| P6 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P2 (independent); instance: designed modules | By P6 the accepted ontology, design and module boundary are the authority for a designed module, so where a design profile governs a boundary, implementation and unit tests derive from them, and evidence feeds back without selecting the semantic answer. By P4b and P2 module proof needs a record that traces to the module's ownership, so module-owned unit tests are authoritative for module proof and should trace to module ownership, not helper shape, and a module without that lane is not closure-ready. | [§14](#14-design-to-module-evidence-route); [§15](#15-module-derived-unit-tests) | the two evidence chains, the completeness requirements and the traceability sources: domain choices of this member; the binding of the written terms to the profile's objects: [DESIGN_MODULE](DESIGN_MODULE.md) (family F17) | 4, 9 |
| P2 (independent); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: designed modules | By P2 every lifecycle phase of a designed surface bears on its outcome, and by P5 an unanswered phase is undecided, so before closure each phase is answered, declared not applicable with a reason, or recorded as a named gap. By P6 implementation proves a lifecycle path only within its own authority, and a gap proceeds only when governed. | [§16](#16-module-lifecycle-confirmation) | the nine stated items: domain choices of this member; the lifecycle chain and its markers: [SPEC_METHOD §2 Operational lifecycle sufficiency](SPEC_METHOD.md#operational-lifecycle-sufficiency) (family F10) | 1, 9 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §16. §17 records dispositions and decides
nothing.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the verification layers: no separate consumer applies. The layers are applied inside this member, by §2 to §6, which the rows below trace; [SPEC_METHOD §9](SPEC_METHOD.md#9-evidence) names §1 to §6 as the rules of realisation proof and applies none of them to a case, and EXECUTIVE_BASELINE §2 names this member as the owner of the taxonomy and states no application of §1.
- Row 2, the authority source of a proof surface and the lane mapping: [DESIGN_MODULE §6 Irreducible architectural carrier set](DESIGN_MODULE.md#irreducible-architectural-carrier-set), the carrier inventory to which design and module conformance tests bind; this member's [§15](#15-module-derived-unit-tests), which keeps module-derived unit proof within the product-assurance bounded context and leaves acceptance meaning with Product authority.
- Row 3, acceptance evidence from the composed product: this member's [§13 Obligations](#obligations), where a live claim needs live evidence under §2; otherwise no separate consumer applies: which lane a project runs is its assurance design, and the acceptance decision that consumes the evidence is EVALUATION §5's and RELEASE §8's, which apply the claim law of EVALUATION and name these paragraphs nowhere.
- Row 4, fixture and proof portability: no separate consumer applies. A lane's external dependencies are declared by the project's assurance design under this paragraph; a missing fixture is reported as an evaluation not performed, in the core value of FOUNDATIONS §4 Results that this paragraph applies; no section of another member names it.
- Row 5, test authority, scenario bundles and significant paths: [TICKETS §7 Test case authority](TICKETS.md#test-case-authority), the ticket-local rule of the general test authority law; [SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate), where implementation behaviour is evidence and not authority and the test authority rule is this member's.
- Row 6, installed dev proof: [ODD §13](ODD.md#13-installed-dev-rule), which binds the rule for its profile; the install and development-product roles are FOUNDATIONS §2 Product lineage objects', as the choice column states; which installed form a claim binds is the claim's own.
- Row 7, the testing frames and evidence composition: [EXECUTIVE_BASELINE §1](EXECUTIVE_BASELINE.md#1-canonical-compression), where the four frames are activated inside the engagement relation and no narrower green frame establishes an unevaluated composition; [§5 Terms owned by ASSURANCE](EXECUTIVE_BASELINE.md#terms-owned-by-assurance); [§8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), where unit evidence covers module-owned laws under the frames and the frames keep their distinct claims; [§11 Relation to the testing and interface frames](EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames); [§12 step 2](EXECUTIVE_BASELINE.md#2-executive-activates-worker), whose activation names the testing claims, subjects, topology and populations, and [step 4](EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result), where a missing or contradicted frame result is read under §10; [§14](EXECUTIVE_BASELINE.md#14-coverage-application), whose rows for the user outcome, the installed path, material interfaces and module-owned laws name the frames; [§16 Adopt this baseline](EXECUTIVE_BASELINE.md#adopt-this-baseline), whose inventory the adoption declares; [§18](EXECUTIVE_BASELINE.md#18-profile-qualification), obligations 12 to 15; this member's [§13](#13-end-to-end-interface-integration-frame), which relates its families to the frames of §7, and [§15](#15-module-derived-unit-tests), whose lane claims, and leaves unclosed, what the unit frame of §7 states.
- Row 8, path claims: [EXECUTIVE_BASELINE §5 Terms owned by ASSURANCE](EXECUTIVE_BASELINE.md#terms-owned-by-assurance), for the authoritative Product path; [§12 step 2](EXECUTIVE_BASELINE.md#2-executive-activates-worker) and [§16 Adopt this baseline](EXECUTIVE_BASELINE.md#adopt-this-baseline), whose activation and inventory carry the forbidden-path exclusions; [§14](EXECUTIVE_BASELINE.md#14-coverage-application), whose row for obsolete and rival paths names the production-closure and assurance-closure graphs; [§18](EXECUTIVE_BASELINE.md#18-profile-qualification), obligation 13, where an end-to-end frame falsifies an equal output obtained through a forbidden path.
- Row 9, testing value and combinatorial coverage: [EXECUTIVE_BASELINE §5 Terms owned by ASSURANCE](EXECUTIVE_BASELINE.md#terms-owned-by-assurance), for material combinatorial complexity; [§12 step 2](EXECUTIVE_BASELINE.md#2-executive-activates-worker) and [§16 Adopt this baseline](EXECUTIVE_BASELINE.md#adopt-this-baseline), whose activation and inventory carry the material combination populations; [§18](EXECUTIVE_BASELINE.md#18-profile-qualification), obligation 14, where omitted higher-order combinations stay residuals; [§20](EXECUTIVE_BASELINE.md#20-failure-classification), where one sunny path reported as combinatorial coverage is an undeclared interaction population.
- Row 10, the assurance subject: [EXECUTIVE_BASELINE §20](EXECUTIVE_BASELINE.md#20-failure-classification), where a harness that derives owner state from raw events beside an installed owner projection is an invalid assurance subject, and [§21](EXECUTIVE_BASELINE.md#21-anti-patterns), items 25 and 27; this member's [§13 Obligations](#obligations), whose evidence acquisition follows §11.
- Row 11, counterexample localisation: [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), where localisation applies to a supported diagnosis where required; [EXECUTIVE_BASELINE §20](EXECUTIVE_BASELINE.md#20-failure-classification), where a symptom assigned to one owner without causal-frontier evidence is unsupported localisation, and [§21](EXECUTIVE_BASELINE.md#21-anti-patterns), item 26; this member's [§13 Obligations](#obligations), obligation 6, which applies §12 to preserve diagnostic cause.
- Row 12, the interface integration frame: [DESIGN_MODULE §7 Computational realisation projection](DESIGN_MODULE.md#computational-realisation-projection-up-019), where component-local success establishes no complete-path claim; [EXECUTIVE_BASELINE §11 Relation to the testing and interface frames](EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames), which relates the frame's families to the Executive's generic specialist frames.
- Row 13, the design-to-module route and module-derived unit tests: [DESIGN_MODULE §9](DESIGN_MODULE.md#9-module-taxonomy), where a boundary's modules are proved under this assurance law; [§6 Irreducible architectural carrier set](DESIGN_MODULE.md#irreducible-architectural-carrier-set), the inventory to which unit proof binds; [§12 Adoption](DESIGN_MODULE.md#adoption), where a module-derived unit test lane is published before closure is claimed; [EXECUTIVE_BASELINE §18](EXECUTIVE_BASELINE.md#18-profile-qualification), obligation 15, where every coded module has a module-derived unit lane; [FOUNDATIONS §4 Parallel derivation and mutual assurance](FOUNDATIONS.md#parallel-derivation-and-mutual-assurance), whose example instantiates the route's paths in acceptance and build-level tests.
- Row 14, module lifecycle confirmation: [DESIGN_MODULE §5 Entity and lifecycle completeness](DESIGN_MODULE.md#entity-and-lifecycle-completeness), which keeps the entity lifecycle apart from the operational lifecycle this section confirms; [§9](DESIGN_MODULE.md#9-module-taxonomy); [§12 Relationship to other members](DESIGN_MODULE.md#relationship-to-other-members), where the rule detects lifecycle signal and decides no release eligibility or acceptance.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `SPEC_METHOD.md#what-counts-as-a-core-interface` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#what-counts-as-a-core-interface` at rc.2:

```text
### What Counts As A Core Interface

A core interface includes any shared contract or carrier that materially governs:

- runtime closure
- reporting or status truth
- topology or frame progression
- proof or qualification outcome
- event or projection semantics
- identity or binding resolution
- provider or resolver behavior

If changing the interface can alter how multiple surfaces decide "what is true
now," it is a core interface change.
```

Successor, `SPEC_METHOD.md#what-counts-as-a-core-interface`:

```text
### What counts as a core interface

A core interface is any shared contract or carrier that materially governs
runtime closure, reporting or status truth, topology or frame progression,
proof or qualification outcome, event or projection semantics, identity or
binding resolution, or provider or resolver behaviour. If changing the
interface can alter how multiple surfaces decide what is true now, it is a
core interface change (P3; rc.2 #what-counts-as-a-core-interface).
```


### Row `SPEC_METHOD.md#what-how-and-work-carriers` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#what-how-and-work-carriers` at rc.2:

```text
### WHAT, HOW, And Work Carriers

`SPEC_METHOD.md` owns the build-tenancy bounded context
`urn:stdo:bounded-context:build-tenancy` under the selected complete STDO basis.
It governs the realization relation defined here: one constitutional product
`WHAT` is realized by one or more independent project-owned `HOW` tenants. A
**build tenant** is one such realization. **Build tenancy** is the one-or-more
relation; one tenant is its singleton case and multi-build-tenancy begins when
the same `WHAT` has more than one independent realization.

`what.intent`, `what.product`, and `what.specification` locate the current
constitutional `WHAT`. Intent and Product each have one canonical entrypoint;
specification may cite more than one requirement or specification surface.

The **Tenant Registry** is the canonical `how.build_tenants` collection for the
product's independent `HOW` realizations. Each entry has stable identity and
locates its root, design, and implementation surfaces. The **Common Build-Tenant Surface**
is the realization law bound by `how.common` and
explicitly adopted across more than one tenant. A separate
`TENANT_REGISTRY.md` may remain as a human-readable companion or generated
projection, but it cannot become a second tenant-identity or location
authority.

`ticketing.goals` locates the current work-wave carrier.
`ticketing.tickets` locates the durable ticket root and the minimum backlog,
active, and completed lanes. `ticketing.comments` locates the commentary
root. `ticketing.sprints` optionally locates bounded execution-batch
manifests. These bindings may resolve to directories, repository resources,
tracker collections, API endpoints, or product-scoped queries. Goals own the
bounded work wave, ticket state remains ticket authority, and comments remain
non-authoritative commentary.
```

Successor, `PRODUCT_DEFINITION.md#8-what-how-and-work-carriers`:

```text
## 8. WHAT, HOW and work carriers

This member owns the build-tenancy bounded context,
`urn:stdo:bounded-context:build-tenancy`, under the selected complete STDO
basis. These concepts of the context are owned in other members, each by
an explicit owner relation (§5) (P1, P3):

- the build tenant, the relation by which one constitutional product WHAT
  is realised by one or more independent project-owned HOW tenants, and
  each tenant's build-tenant binding:
  [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), its terms and
  rule 1;
- the multi-build-tenant work-item relation:
  [TICKETS §4](TICKETS.md#multi-build-tenant-independence).

In this context build tenancy is that one-or-more relation; one tenant is
its singleton case, and multi-build-tenancy begins when the same WHAT has
more than one independent realisation (P3, P2; rc.2
#what-how-and-work-carriers).

`what.intent`, `what.product` and `what.specification` locate the current
constitutional WHAT. Intent and Product each have one canonical entrypoint;
specification may cite more than one requirement or specification surface
(P3).

The Tenant Registry is the canonical `how.build_tenants` collection for the
product's independent HOW realisations. Each entry has stable identity and
locates its root, design and implementation surfaces; the tenant's
binding, which those surfaces declare, is governed by SPEC_METHOD §11.
The Common Build-Tenant Surface is the realisation law bound by `how.common` and
explicitly adopted across more than one tenant. A separate
`TENANT_REGISTRY.md` may remain as a human-readable companion or generated
projection and cannot become a second tenant-identity or location
authority (P3, P6).

`ticketing.goals` locates the current work-wave carrier.
`ticketing.tickets` locates the durable ticket root and the minimum
backlog, active and completed lanes. `ticketing.comments` locates the
commentary root. `ticketing.sprints` optionally locates bounded
execution-batch manifests. These bindings may resolve to directories,
repository resources, tracker collections, API endpoints or product-scoped
queries. Goals own the bounded work wave, ticket state stays ticket
authority, and comments stay non-authoritative commentary (P6, P3). Which
carrier a given work item takes is SPEC_METHOD §4 and the [TICKETS](TICKETS.md) member;
this section binds where each carrier kind lives.
```

Successor, `SPEC_METHOD.md#11-build-tenant-binding`:

```text
## 11. Build-tenant binding

This section owns the relation between a product's WHAT and the build
tenants that realise it: what a tenant binds, what stays fixed while it
chooses, and what its evidence shows. It applies to every product built
with this method (P2, P1, P6).

Terms used in this section:

- A build tenant is one independent, project-owned HOW realisation of a
  product's WHAT. The build-tenancy context of
  [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)
  names it, and the product definition's tenant registry locates each one.
- The requirements calculus of a product is the set of obligations its
  WHAT states, the outcomes it permits, and its rules for refining and
  composing the work that realises it.
- A computational calculus is a declared set of executable operations,
  with the laws by which they compose, the transformations they permit,
  and their effects and resource behaviour, as far as these are material
  to the obligations.
- An execution environment is the concrete means that performs those
  operations: a technology stack; a human process, made of people, roles,
  documents, communication channels and decision procedures; or a
  combination of the two.
- A tenant's build-tenant binding has two parts: its calculus binding,
  from the requirements calculus to its computational calculus, and its
  execution binding, from that computational calculus to its execution
  environment. A tenant's registry entry locates the tenant; it is not the
  binding.
- A generic procedure is a method procedure whose scope is independent of
  the selected execution environment. It and its projections preserve the
  bindings Rule 2 permits: code, an event stream or reconstruction from a
  complete history is required only where the governing obligations or
  the selected execution binding require it, and an adequate human
  process using current records and direct observation is a permitted
  execution binding of a generic procedure that requires none of them
  (P1, P6; law carried from the common binding requirement).
- Author identity and actor identity are as
  [EVALUATION §3](EVALUATION.md#3-independent-assessment) defines them:
  authorship is one condition of an assessment's independence there, and
  an actor's identity is not an authority.
  Operation kind is what an operation does, such as construct, assess,
  relay, record, measure or decide, together with the authority that kind
  of operation requires.

Rules:

1. Realisations of one WHAT. One WHAT is realised by one or more
   independent build tenants, whatever the physical layout. The WHAT is
   constitutional and each tenant's realisation is HOW; a tenant-local
   realisation stays derivative until its governing truth is ratified in
   specification (§2). Each tenant binds the product's requirements
   calculus to a declared computational calculus and binds that calculus
   to a concrete execution environment. Both bindings are that tenant's
   design and realisation: they are declared in its existing design and
   realisation surfaces, chosen under the Design rule (§2) and recorded as
   design decisions (§10), and the method requires no further carrier. The
   tenant owns its binding, its realisation and their evidence; the WHAT
   keeps its meaning (P2, P6).
2. Selection. The execution environment may be a technology stack, a
   human process or a combination. Its selection stays within the
   requirements calculus, including every human decision that calculus
   requires: no choice of environment removes a required human decision or
   a required independent assessment. Author identity, actor identity and
   operation kind stay distinct, and none determines another. Who authored
   a tenant does not select its environment; one actor may perform
   operations of several kinds, each under its own grant; and an actor's
   identity neither decides the kind of an operation nor grants authority
   for it. A person performing an operation does not by that make it human
   adjudication: §5 states the admission that makes an operation human
   adjudication and how a person who decides under policy without it is
   governed. The same holds for every decision the requirements reserve to
   a human: the person the governing authority admits for it takes it, and
   a person's part elsewhere in the process does not (P6, P1).
3. Material content. For the obligations it serves, the binding
   identifies:
   - the operations, each with its inputs, outputs, effects and outcome
     values; each outcome value maps to exactly one core value under
     [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and an intended
     external effect, one of uncertain completion included, is recorded as
     [ACTIVATION §3 Effects](ACTIVATION.md#effects) states;
   - the composition laws, and the transformations the calculus permits;
   - the resource measures;
   - the operational assumptions on which conformance depends, among them
     those about actors, tools, availability and failure.

   Human effort, elapsed time, communication and machine resources are
   measured where a selected obligation needs them. Each measure states its
   unit and its boundary: what is counted, and where measurement starts and
   stops. A resource claim without its unit or its boundary supports no
   conformance claim. The size of a selected context is measured as
   [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
   step 3 measures it, against the capacity the binding declares for the
   actor. The law for declaring, measuring and honouring resource limits
   is [ACTIVATION §6 Resource limits](ACTIVATION.md#resource-limits), and
   this rule binds it: the values of a step's time, spend and other
   resource limits, and the units and boundaries the environment can
   measure, are those of the execution binding, stated before the
   activation they limit. Where a configuration states its resource limits
   and its assumptions about failure
   ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)), it takes
   them from this binding (P0, P2, P5).
4. Conformance evidence. The obligations of the requirements calculus
   decide fitness; the kind of executor alone neither accepts nor rejects a
   realisation. Evidence establishes how the bound realisation satisfies
   the required meaning and constraints, including the applicable
   authority, independence, failure and recovery conditions. Conformance is
   judged under
   [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations), and two
   conforming tenants need not behave identically outside the contract.
   Each assessment returns a core value for its predicate, and the tenant's
   conformance is their
   [conjunction](FOUNDATIONS.md#conjunction-of-results), with the
   obligations of the requirements calculus as its required coverage. A
   convenient stack never weakens an obligation. An execution plan that
   merges two required independent assessments, or substitutes an
   automated result for a required human decision, is a counterexample to
   the obligation it weakens, so the binding's conformance for that
   obligation is `falsified`; in any run under such a plan the lost
   assessment or decision has no applicable closed result. Matching
   outputs, lower cost or a faster run do not discharge the lost
   independence or authority. A claim that a binding preserves categorical
   structure is a further claim: it meets the Formal fragment of
   [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra) and stays distinct from
   conformance on the equivalence ladder of EVALUATION §6 (P6, P1, P4b).
5. Reuse. A computational calculus may be reused across tenants and
   execution environments wherever each binding satisfies its laws, and
   each binding shows that it does. A different language, tool, team or
   person does not by itself require a different calculus: replacing the
   executor of an operation while the calculus's laws hold changes the
   execution binding, not the calculus (P1, P4a).
6. Representation. A representation of the requirements calculus or of a
   binding in a_c, the axiomatic calculus of
   [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md), prescribes no executor and
   does not establish execution conformance by structural validation alone
   ([AC-018](AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation)).
   An a_c model of a human process that passes structural validation
   neither selects an automated executor nor shows that the process meets
   its requirements; execution conformance needs its own evidence under
   rule 4 (P1, P6).
7. Three accounts. The algorithmic, informational and computational
   accounts of a construction, which
   [FOUNDATIONS §2 Accounts of a construction](FOUNDATIONS.md#accounts-of-a-construction)
   defines, apply across the binding, from the requirements calculus
   through the computational calculus to the execution environment. The
   binding keeps the three accounts apart. A mapping from one account to
   another is a transformation: what it preserves, the law that licenses
   it, and whether it is exact or approximate with its adequacy relation
   and end-to-end bound, are stated and discharged under
   [ACTIVATION §4 Refinement](ACTIVATION.md#refinement), and where it is
   recorded in a_c its record is
   [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation). The binding adds
   only which accounts the mapping joins and the evidence, in its
   execution environment, that discharges the preservation (P1, P0, P4a,
   P6).

Application in this method. The relation governs realisation at four
points. The Design rule (§2) places the choice of stack, human process or
combination in design, and that choice is the execution binding.
Ambiguity governance (§5) treats the choice as the step that narrows the
executable realisation class, so a major ambiguity about stack or
execution admissibility is recorded and governed there. A change to a
binding enters through intake triage and takes its change class (§4); a
change that needs a weaker obligation is a change to the WHAT at its
owning layer, never a tenant's choice. The steps of construction (§8) are
carried out under the binding of the tenant doing the work (P2, P6).

Development of several tenants. How a source project keeps its tenants'
work apart and merges it, including branches, working copies, territories,
review points and the merge rule, is that project's own law, bound in its
product definition as local axioms
([PRODUCT_DEFINITION §6](PRODUCT_DEFINITION.md#6-local-constitutional-binding))
or chosen in a tenant's design. This method prescribes none of these
mechanics. What it does prescribe for several tenants, the independence
of each tenant's ticket lifecycle and the review of each tenant's
tickets, is
[TICKETS §4](TICKETS.md#multi-build-tenant-independence) and
[§6 Multi-build-tenant review](TICKETS.md#multi-build-tenant-review)
(P6, P0).

Purpose and material relation: the same obligations can be realised by
different means, software, people or both. The tenant owns its choice of
means and the evidence for it while the WHAT keeps its meaning, so a
particular stack never becomes method machinery and a human or mixed
process needs no parallel method. The material relation is whether the
kind of executor, a person's participation, a tool's convenience or a
structural validation can change what satisfies an obligation, or grant
authority (P2, P1, P6). Two determinations conserve the predecessor's
constitutional chain (rc.2 #constitutional-chain): one WHAT realised by
one or more independent tenants whatever the layout, and tenant-local
realisation derivative until ratified (rule 1). Rule 4 applies by
reference the law of EVALUATION §6 that conforming tenants need not
behave identically outside the contract, which is new in that member.
The rest of this section is new in this corpus.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#1-existing-authority-selects-the-basis` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#1-existing-authority-selects-the-basis` at rc.2:

```text
### 1. Existing Authority Selects The Basis

Goals, Product, requirements, accepted design, ticket, release, or an admitted
bounded proxy selects the outcome and work authority under its existing STDO
owner. The Product-owned Project Reference-Frame Basis projects that decision.
```

Successor, `EXECUTIVE_BASELINE.md#1-existing-authority-selects-the-basis`:

```text
### 1. Existing authority selects the basis

Goals, Product, requirements, accepted design, a ticket, release law or an
admitted bounded proxy selects the outcome and the work authority under its
existing owner. The Product-owned Project Reference-Frame Basis
(PRODUCT_DEFINITION §7) projects that decision (P6; rc.2
#1-existing-authority-selects-the-basis).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#3-worker-returns-to-executive` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#3-worker-returns-to-executive` at rc.2:

```text
### 3. Worker Returns To Executive

Every coordinated Worker activation terminates in one closed work result sent
to Executive. Direct work uses its declared result consumer:

```text
WorkerResult
  = candidate_ready(exact_subject, transition_evidence, residuals)
  | refused(reason, authority, evidence)
  | incomplete(residuals, evidence, stop_basis)
  | re_entry_requested(owner, material_relation, evidence)
```

The notation is explanatory and mandates no schema.

Each variant accompanies exactly one Reference Frame Method result under the
mapping in `Work result`: `satisfied -> candidate_ready`, `falsified ->
refused`, `indeterminate -> incomplete`, and `out_of_frame | invalid_basis ->
re_entry_requested`. The mapping applies only after lawful activation.

The Worker does not send a candidate directly into an implicitly active
Reviewer. It stops after returning the result.
```

Successor, `EXECUTIVE_BASELINE.md#3-worker-returns-to-executive`:

```text
### 3. Worker returns to Executive

Every coordinated Worker activation ends in one closed work result sent to
the Executive; direct work uses its declared result consumer (P5, P6; rc.2
#3-worker-returns-to-executive):

```text
WorkerResult
  = candidate_ready(exact_subject, transition_evidence, residuals)
  | refused(reason, authority, evidence)
  | incomplete(residuals, evidence, stop_basis)
  | re_entry_requested(owner, material_relation, evidence)
```

The notation explains and mandates no schema. The material relation of
`re_entry_requested` names its cause, authority or basis, which is part of
the value. Each value maps to exactly one core value for "a candidate is
available" under
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability),
read as in §5 Work result; the mapping applies only after lawful
activation. The Worker does not send a candidate directly into an
implicitly active Reviewer. It stops after returning the result (P5,
P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#4-executive-evaluates-the-work-result` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#4-executive-evaluates-the-work-result` at rc.2:

```text
### 4. Executive Evaluates The Work Result

For `refused`, `incomplete`, or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable `STDO-UP-020` disposition or reactivates work only when the current
authority already permits that action. None of these variants can be treated as
accepted progress merely because work occurred.

For `candidate_ready`, the Executive verifies the exact subject and determines
whether independent assessment is required by `STDO-UP-007`,
`STDO-UP-020`, `STDO-UP-022`, Product, release, risk, or the admitted work
contract. Green aggregate status cannot satisfy this step when a required
user-acceptance, end-to-end, integration, unit, or negative-path result is
missing, bound to another subject, or contradicted by a material frame result.
```

Successor, `EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result`:

```text
### 4. Executive evaluates the work result

For `refused`, `incomplete` or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable disposition, or reactivates work only where current authority
already permits that action. None of these variants is accepted progress
because work occurred (P6, P5; rc.2 #4-executive-evaluates-the-work-result).

Whatever the variant, an effect of uncertain completion, one the work
result names `completion_unknown` or names `not_effected` with its end not
established ([ACTIVATION §3 Effects](ACTIVATION.md#effects)), is
reconciled under
[ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart), sufficiently for
the next dependent action, before work is reactivated, the effect is
repeated or any action that depends on it is taken (P5, P6).

For `candidate_ready`, the Executive verifies the exact subject and decides
whether independent assessment is required. It applies the boundaries at
which this method requires it,
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007);
the execution relation's assessment where required (ACTIVATION §1); method
qualification ([EVALUATION §7](EVALUATION.md#7-qualification-of-frames-and-of-the-method));
and the further boundaries the governing basis adds, as
[EVALUATION §3](EVALUATION.md#3-independent-assessment) permits: Product,
release, risk or the admitted work contract. What counts as independent is
EVALUATION §3's. Green aggregate status cannot satisfy this step when a
required user-acceptance, end-to-end, integration, unit or negative-path
result is missing, bound to another subject, or contradicted by a material
frame result (P6; ASSURANCE §10).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#5a-candidate-does-not-require-independent-review` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#5a-candidate-does-not-require-independent-review` at rc.2:

```text
### 5A. Candidate Does Not Require Independent Review

In the coordinated branch, when independent review is not required, Executive
consumes the exact candidate, Worker self-review, transition evidence, and any mandatory
specialist-frame results. It applies `STDO-UP-020` disposition within its
decision envelope.

Self-review remains Worker evidence. The disposition does not relabel it as
independent.
```

Successor, `EXECUTIVE_BASELINE.md#5a-candidate-does-not-require-independent-review`:

```text
### 5A. Candidate does not require independent review

In the coordinated branch, when independent review is not required, the
Executive consumes the exact candidate, the Worker's self-review, the
transition evidence and any mandatory specialist results, and applies the
disposition within its decision envelope. Self-review stays Worker
evidence; the disposition does not relabel it as independent (P6; rc.2
#5a-candidate-does-not-require-independent-review).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#5b-candidate-requires-independent-review` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#5b-candidate-requires-independent-review` at rc.2:

```text
### 5B. Candidate Requires Independent Review

When independent review is required, the Executive activates the Reviewer with:

- exact candidate and governing basis;
- exact claim, composition boundary, population, scope, and exclusions;
- applicable STDO and project authority;
- required evidence and ordinary assurance path;
- required user-acceptance, end-to-end, integration, unit, combinatorial, and
  negative-path frame results with their exact claims and populations;
- the Product-selected severity scale and exact affected Product claims;
- Reviewer capability and independence envelope; and
- invalidation and stop conditions.

The candidate is frozen before material reference exposure where
`STDO-UP-022` requires it. Otherwise the subject is stabilized to the exactness
required by `STDO-UP-007`, `STDO-UP-020`, and the claim.
```

Successor, `EXECUTIVE_BASELINE.md#5b-candidate-requires-independent-review`:

```text
### 5B. Candidate requires independent review

When independent review is required, the Executive activates the Reviewer
with (P6, P3; rc.2 #5b-candidate-requires-independent-review):

- the exact candidate and governing basis;
- the exact claim, composition boundary, population, scope and exclusions;
- the applicable method and project authority;
- the required evidence and the ordinary assurance path;
- the required user-acceptance, end-to-end, integration, unit,
  combinatorial and negative-path frame results, with their exact claims and
  populations;
- the Product-selected severity scale and the exact affected Product claims;
- the Reviewer's capability and independence envelope; and
- invalidation and stop conditions.

Where EVALUATION §7 requires it, the candidate is frozen before material
reference exposure. Otherwise the subject is stabilised to the exactness
that EVALUATION §3, ACTIVATION §7 and the claim require (P3, P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#6-reviewer-returns-to-executive` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#6-reviewer-returns-to-executive` at rc.2:

```text
### 6. Reviewer Returns To Executive

The Reviewer returns one closed evaluation containing:

- frame and activation identity;
- exact subject, basis, claim, scope, exclusions, and evaluated population;
- Reviewer actor and independence conditions;
- evidence and ordinary assurance path acquired;
- Reference Frame Method result;
- findings, counterexamples, and adjacent observations;
- for each finding, affected claim, severity, causal assessment and confidence,
  blast radius, workaround, repair complexity, regression risk, and residual
  uncertainty where supportable; and
- invalidation conditions and re-entry owner where applicable.
```

Successor, `EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive`:

```text
### 6. Reviewer returns to Executive

The Reviewer returns one closed evaluation in the shape of EVALUATION §4,
which here contains (P6, P5; rc.2 #6-reviewer-returns-to-executive):

- frame and activation identity;
- the exact subject, basis, claim, scope, exclusions and evaluated
  population;
- the Reviewer actor and the independence conditions;
- the evidence and the ordinary assurance path acquired;
- the core result (FOUNDATIONS §4 Results);
- findings, counterexamples and adjacent observations;
- for each finding, where supportable: the affected claim, severity, causal
  assessment and confidence, blast radius, workaround, repair complexity,
  regression risk and residual uncertainty; and
- invalidation conditions and, where applicable, the re-entry owner.

The finding-level triage payload projects over the result algebra as
EVALUATION §4 (Result and triage projection) states; in this profile the
assessor there is the Reviewer and the decision owner is the Executive. The
Reviewer returns to the Executive, not to the Worker, and returns no
disposition; a recommendation is evidence only (EVALUATION §4). It does not
edit the candidate, direct the repair or authorise continuation (P6; rc.2
#reviewer-result-and-triage-projection).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#7-executive-disposes-and-checkpoints` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#7-executive-disposes-and-checkpoints` at rc.2:

```text
### 7. Executive Disposes And Checkpoints

The Executive verifies that every consumed result remains bound to the current
subject and basis, revalidates the complete Product view and current MVP or
release mandate, applies any declared result conjunction, assigns priority,
records the effect on the current promotion boundary, and acts on exactly one
`STDO-UP-020` disposition within its grant:

- `accept`;
- `local_repair`;
- `re_enter`; or
- `reject`.

`STDO-UP-020` remains the owner of each disposition, exact accepted checkpoint,
and next already-authorized bounded action. A repair creates a new candidate.
An affected review is reactivated against that candidate. Acceptance does not
widen the Product outcome or authorize an unselected successor.

Severity does not mechanically select priority or block promotion. Priority
does not erase severity or waive a hard stop. The Executive determines blocking
from the exact affected claim, current mandate, applicable hard stops, and
Product-owned cutoff policy. An unsupported technical assessment is returned
through a new or refined activation rather than silently rewritten.
```

Successor, `EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints`:

```text
### 7. Executive disposes and checkpoints

The Executive verifies that every consumed result is still bound to the
current subject and basis, revalidates the complete Product view and the
current MVP or release mandate, applies any declared result conjunction
(FOUNDATIONS §4 Conjunction of results), assigns priority, records the
effect on the current promotion boundary, and acts on exactly one
disposition within its grant: `accept`, `local_repair`, `re_enter` or
`reject` (ACTIVATION §3; P6, P5; rc.2
#7-executive-disposes-and-checkpoints).

ACTIVATION §3 and §5 stay the owners of each disposition, the exact accepted
checkpoint and the next already-authorised bounded action. The disposition
is the acceptance result; neither `candidate_ready` nor a satisfied review
result is acceptance (FOUNDATIONS §4 Results). A repair creates
a new candidate, and an affected review is reactivated against it.
Acceptance does not widen the Product outcome or authorise an unselected
successor (P4b, EVALUATION §5).

When a finding blocks the current promotion boundary, and that severity
selects neither priority nor a block and priority waives no hard stop, is
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
read with the Executive as the decision owner; this profile restates none
of it. The Executive records its determination as the current-boundary
effect (§5 Technical triage, severity, priority and boundary effect). An
unsupported technical assessment returns through a new or refined
activation rather than being silently rewritten (P6, P1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#actor-binding-and-independence` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#actor-binding-and-independence` at rc.2:

```text
## Actor Binding And Independence

Frames and actors are separate identities. One actor may occupy several frames
across different activations where authority and any claimed independence are
preserved. Different humans, agents, deterministic tools, or mixed
configurations may occupy them. This profile prescribes no actor count.

Where independent review is required, `STDO-UP-007` controls. The activation
records the exact subject and verdict carrier, and the Reviewer is not the
author of that subject. `STDO-UP-022` adds its declared capability,
configuration, comparison-basis, reference-exposure, and freeze conditions for
generic method qualification.

An Executive may inspect a subject to adjudicate a result. That Executive
evaluation does not become an additional independent Reviewer result merely
because the actor used reviewer-like tools.

---
```

Successor, `EXECUTIVE_BASELINE.md#17-actor-binding-and-independence`:

```text
## 17. Actor binding and independence

Frames and actors are separate identities: activation binds an actor to
a frame ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)). In
this configuration, as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)
permits for any configuration, one actor may occupy several frames across
different activations where authority and any claimed independence are
preserved. Humans, agents, deterministic tools or mixed configurations may
occupy them. The profile prescribes no actor count (P3, P6, RF-016; rc.2
#actor-binding-and-independence).

Where independent review is required, the activation records the exact
subject and verdict carrier, which
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007)
requires for a traceable verdict, and
[EVALUATION §3](EVALUATION.md#3-independent-assessment) decides what
counts as independent: the Reviewer is not the author of that subject,
and a fresh context of the author is still the author. For generic method
qualification,
EVALUATION §7 adds its declared capability, configuration, comparison
basis, reference-exposure and freeze conditions (P6).

An Executive may inspect a subject to adjudicate a result. That inspection
does not become an additional independent Reviewer result because the actor
used reviewer-like tools (P6, P1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#adopt-this-baseline` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#adopt-this-baseline` at rc.2:

```text
### Adopt This Baseline

A baseline-adoption projection records the following content inside that
Product-owned basis:

- exact selected complete STDO, Reference Frame Method, and profile identities;
- existing authority admitting adoption;
- governed workspace, Product scope, outcome, basis, and time;
- local Executive, Worker, and Reviewer capability envelopes and actor-binding
  rules;
- generic specialist-frame declarations or authoritative acquisition paths,
  plus an authority-bound non-material or explicit residual disposition for
  each Product, Product Composition, Design, Design Component, Public Boundary,
  Entity, Operator, Owner, Effect, Reuse/Foundation, Install, and Proof family;
- specialist-frame declarations or authoritative acquisition paths;
- testing-frame declarations, exact Product and module claims, ordinary-path
  identities, combinatorial populations, scenario matrix, oracles, and
  forbidden-path inventory where testing evidence is material;
- local subject, evidence, checkpoint, and review-result coordinates;
- coverage ledger and accepted residual boundary; and
- invalidation and frame-set revision conditions.
```

Successor, `EXECUTIVE_BASELINE.md#adopt-this-baseline`:

```text
### Adopt this baseline

A baseline-adoption projection records inside that Product-owned basis
(P6, P3; rc.2 #adopt-this-baseline):

- the exact selected complete method, REFERENCE_FRAME and profile
  identities;
- the existing authority admitting adoption;
- the governed workspace, Product scope, outcome, basis and time;
- local Executive, Worker and Reviewer capability envelopes and
  actor-binding rules;
- generic family declarations or authoritative acquisition paths, with an
  authority-bound non-material or explicit residual disposition for each of
  the twelve families of §11;
- specialist-frame declarations or authoritative acquisition paths;
- where testing evidence is material: testing-frame declarations, exact
  Product and module claims, ordinary-path identities, combinatorial
  populations, the scenario matrix, oracles and the forbidden-path
  inventory (ASSURANCE §7 to §9);
- local subject, evidence, checkpoint and review-result coordinates;
- the coverage ledger and the accepted residual boundary; and
- invalidation and frame-set revision conditions.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#anti-patterns` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#anti-patterns` at rc.2:

```text
## Anti-Patterns

This profile is misapplied when:

1. Executive, Worker, or Reviewer is treated as a persona without a declared
   evaluation and authority relation;
2. the frames are treated as an organizational hierarchy;
3. Executive is made a universal context, semantic interpreter, or
   implementation controller;
4. Worker sends a candidate directly into an implied Reviewer activation;
5. an activation refusal is relabeled as a Worker result or any Worker result
   variant is selected without its required Reference Frame Method result;
6. refused, incomplete, or re-entry work results have no route to Executive;
7. Worker accepts its own result, infers continuation, or treats its role label
   or broad workspace access as mutation authority;
8. Reviewer relies on Worker narrative instead of acquiring the material live
   subject;
9. Reviewer trusts tests without reviewing their semantics where they can
   change the proof;
10. Reviewer edits or directs repair while retaining independent-review status;
11. changed candidate or basis reuses the predecessor verdict;
12. results from different coordinates are flattened into one relation;
13. a local axioms file is treated as authority without an owning
    Goals/Product/requirement/design decision;
14. this profile restates `STDO-UP-020`, `STDO-UP-007`, or `STDO-UP-022` as
    peer constitutional law;
15. a project-defined configuration silently changes selected STDO law;
16. consumer-specific realization machinery or a renamed architectural
    equivalent is presented as a universal requirement;
17. test labels or runner choice substitute for declaring the exact testing
    frame, subject, claim, population, oracle, path, and falsification condition;
18. unit-test, assertion, snapshot, line, branch, or function count is used as a
    Product-confidence or closure measure;
19. implementation-shaped unit tests are treated as independent design,
    architecture, integration, installed, or user-outcome assurance;
20. interface, persistence, orchestration, authority, configuration, or user
    complexity is mocked away and then counted as unit-test coverage;
21. helper-level tests become the canonical proof surface for a module-owned
    algebra or for a broader Product composition;
22. an expected output is accepted without proving the required authoritative
    path or while a material rival path remains reachable;
23. one end-to-end sunny path substitutes for a declared combinatorial
    population, interaction-strength justification, failure coverage, and
    residual set;
24. UAT gains capabilities, information, setup paths, or interfaces unavailable
    to the declared user;
25. a harness, fixture, proof script, or expected-value builder reconstructs
    owner-issued runtime meaning and treats that reconstruction as the assurance
    subject;
26. a downstream symptom is assigned to one owner when the evidence establishes
    a joint causal frontier, unresolved alternatives, or no bounded frontier, or
    localization is used to authorize wider repair;
27. a mutation, sabotage, fixture, or proof capture changes the exact assurance
    subject without isolation, restoration, and revalidation;
28. aggregate green status hides a missing or conflicting user-acceptance,
    end-to-end, integration, unit, or negative-path frame result;
29. a generic specialist-frame family is treated as a required component,
    actor, service, file, runtime type, stage, or new semantic owner; or
30. a material generic family is omitted because no artifact shares its name,
    or several families are flattened into one broad frame without preserving
    their distinct evaluation and result relations;
31. Reviewer assigns priority, decides promotion blocking, directs repair, or
    starts another activation; or
32. Executive collapses severity, priority, frame result, promotion-boundary
    effect, and disposition into one status value.

---
```

Successor, `EXECUTIVE_BASELINE.md#21-anti-patterns`:

```text
## 21. Anti-patterns

The profile is misapplied when (P6, P2; rc.2 #anti-patterns):

1. Executive, Worker or Reviewer is treated as a persona without a declared
   evaluation and authority relation;
2. the frames are treated as an organisational hierarchy;
3. the Executive is made a universal context, semantic interpreter or
   implementation controller;
4. the Worker sends a candidate directly into an implied Reviewer
   activation;
5. an activation refusal is relabelled as a Worker result, or a work-result
   variant is selected without its required core result;
6. refused, incomplete or re-entry work results have no route to the
   Executive;
7. the Worker accepts its own result, infers continuation, or treats its
   role label or broad workspace access as mutation authority;
8. the Reviewer relies on the Worker's narrative instead of acquiring the
   material live subject;
9. the Reviewer trusts tests without reviewing their semantics where they
   can change the proof;
10. the Reviewer edits or directs repair while keeping independent-review
    status;
11. a changed candidate or basis reuses the predecessor verdict;
12. results from different coordinates are flattened into one relation;
13. a local axioms file is treated as authority without an owning Goals,
    Product, requirement or design decision;
14. this profile restates the execution relation (ACTIVATION §1 and §3),
    independent assessment (EVALUATION §3) or the assurance-boundary law
    (EVALUATION §1 and §7) as peer constitutional law;
15. a project-defined configuration silently changes selected method law;
16. consumer-specific realisation machinery, or a renamed architectural
    equivalent, is presented as a universal requirement;
17. test labels or runner choice stand in for declaring the exact testing
    frame, subject, claim, population, oracle, path and falsification
    condition;
18. unit-test, assertion, snapshot, line, branch or function count is used
    as a Product-confidence or closure measure;
19. implementation-shaped unit tests are treated as independent design,
    architecture, integration, installed or user-outcome assurance;
20. interface, persistence, orchestration, authority, configuration or user
    complexity is mocked away and then counted as unit coverage;
21. helper-level tests become the canonical proof surface for a
    module-owned algebra or for a broader Product composition;
22. an expected output is accepted without proving the required
    authoritative path, or while a material rival path stays reachable;
23. one sunny end-to-end path stands in for a declared combinatorial
    population, an interaction-strength justification, failure coverage and
    a residual set;
24. UAT gains capabilities, information, setup paths or interfaces
    unavailable to the declared user;
25. a harness, fixture, proof script or expected-value builder
    reconstructs owner-issued runtime meaning and treats the reconstruction
    as the assurance subject;
26. a downstream symptom is assigned to one owner when the evidence
    establishes a joint causal frontier, unresolved alternatives or no
    bounded frontier, or localisation is used to authorise a wider repair;
27. a mutation, sabotage, fixture or proof capture changes the exact
    assurance subject without isolation, restoration and revalidation;
28. aggregate green status hides a missing or conflicting user-acceptance,
    end-to-end, integration, unit or negative-path result;
29. a generic family is treated as a required component, actor, service,
    file, runtime type, stage or new semantic owner;
30. a material generic family is omitted because no artifact shares its
    name, or several families are flattened into one broad frame without
    preserving their distinct evaluation and result relations;
31. the Reviewer assigns priority, decides promotion blocking, directs
    repair or starts another activation; or
32. the Executive collapses severity, priority, frame result,
    promotion-boundary effect and disposition into one status value.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#assurance-subject-acquisition-and-evaluation` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#assurance-subject-acquisition-and-evaluation` at rc.2:

```text
### Assurance Subject Acquisition And Evaluation

Acquiring the assurance subject and evaluating it are distinct relations.
Where a claim depends on owner-issued Product, runtime, lifecycle, admission,
replay, or projection truth, the testing frame acquires that truth through the
exact runnable owner surface, validator, projection, receipt, or reconstruction
relation. A harness, fixture, expected-value builder, proof script, assurance
evaluator, or Reviewer does not reconstruct a parallel owner state from raw
payloads, events, logs, filenames, labels, or implementation fragments and then
evaluate that self-authored state as if it were the Product subject.

After lawful acquisition, an independently derived oracle may evaluate the
governing claim. Generic assurance mechanics may compute bytes, digests,
ordering, equality, set membership, completeness, and conjunction over
owner-issued evidence. Those mechanics remain evidence evaluators: they cannot
mint owner carriers, choose current history, select the authoritative path,
interpret domain lifecycle or admission meaning, or become a runtime fallback.

This rule does not require an evaluator to trust the implementation under test
as its semantic oracle. The oracle derives from Product, requirement, and
accepted-design law. It does require the assurance subject to be the actual
owner-issued subject rather than a second implementation of the owner's
runtime meaning. If the required owner projection or observable seam is absent,
the result retains a named assurance or design gap; the proof harness does not
fill it with rival semantics.
```

Successor, `ASSURANCE.md#11-assurance-subject-acquisition-and-evaluation`:

```text
## 11. Assurance subject acquisition and evaluation

Acquiring the assurance subject and evaluating it are distinct relations
(P6, P1; provenance #assurance-subject-acquisition-and-evaluation). Where a
claim depends on owner-issued Product, runtime, lifecycle, admission,
replay or projection truth, the testing frame acquires that truth through
the exact runnable owner surface, validator, projection, receipt or
reconstruction relation. A harness, fixture, expected-value builder, proof
script, assurance evaluator or assessor does not reconstruct a parallel
owner state from raw payloads, events, logs, filenames, labels or
implementation fragments and then evaluate that self-authored state as if
it were the Product subject. Where the acquired observation cannot
separate two admissible subjects, the frame returns further evidence, a
justified narrower scope or `indeterminate`, and the binding of the
observation itself needs support
([FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation),
Observation sufficiency) (P1, P6).

After lawful acquisition, an independently derived oracle may evaluate the
governing claim. Generic assurance mechanics may compute bytes, digests,
ordering, equality, set membership, completeness and conjunction over
owner-issued evidence. Those mechanics stay evidence evaluators: they
cannot mint owner carriers, choose the current history, select the
authoritative path, interpret domain lifecycle or admission meaning, or
become a runtime fallback (P6; EVALUATION §2).

The rule does not require an evaluator to trust the implementation under
test as its semantic oracle; the oracle derives from Product, requirement
and accepted-design law. It requires the assurance subject to be the actual
owner-issued subject rather than a second implementation of the owner's
runtime meaning. If the required owner projection or observable seam is
absent, the result keeps a named assurance or design gap; the proof harness
does not fill it with rival semantics (P6, P5).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#authoritative-product-path` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#authoritative-product-path` at rc.2:

```text
### Authoritative Product path

An **authoritative Product path** is the declared ordinary causal composition
from a supported user or Public entry through the exact selected interfaces,
owners, state transitions, effects, persistence and recovery boundaries, and
outcome projection required by the Product claim. Producing an expected output
through a bypass, obsolete executor, test-only seam, undeclared fallback, or
competing authority falsifies path conformance even when the output value is
equal.
```

Successor, `ASSURANCE.md#terms`:

```text
### Terms

A testing frame is a frame (REFERENCE_FRAME §1) whose evaluation executes
or observes a declared subject to discriminate one exact claim through an
explicit oracle, evidence population, path boundary and falsification
condition. A test file, suite, runner, fixture, scenario label, coverage
percentage or actor does not become a testing frame by existing. A testing
frame's authority is bounded by the claim actually exercised; test count,
assertion count, source coverage, runtime duration and framework category
do not widen it (P6, P1; provenance rc.2 STDO_REFERENCE_FRAME_BASELINE
#testing-frame).

An authoritative Product path is the declared ordinary causal composition
from a supported user or public entry, through the exact selected
interfaces, owners, state transitions, effects, persistence and recovery
boundaries, to the outcome projection the Product claim requires.
Producing an expected output through a bypass, an obsolete executor, a
test-only seam, an undeclared fallback or a competing authority falsifies
path conformance even when the output value is equal (P6, P3; provenance
#authoritative-product-path).

Material combinatorial complexity is the claim-relative population of
independent dimensions and interactions whose combinations can change an
outcome, violate an invariant, select another authority path or expose a
failure. At unit altitude it includes module-owned laws, behaviour at the
public module contract included, with their algebraic operators,
calculation regimes, states, transitions, boundary classes and failure
cases. Cross-participant interface, Product, persistence, configuration and
user-role combinations belong to the integration, end-to-end or
user-acceptance frames; they are not mocked away and counted as unit
evidence (P2, P6; provenance #material-combinatorial-complexity).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#baseline-adoption-projection` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#baseline-adoption-projection` at rc.2:

```text
### Baseline-adoption projection

A **baseline-adoption projection** consumes the Product-owned Project
Reference-Frame Basis defined by
`SPEC_METHOD.md#collective-reference-frame-basis`. Where that basis adopts this
profile, the projection records the selected profile mapping, exact outcome,
actor envelopes, evidence coordinates, and revision conditions needed in
addition to the Product binding. It is not a second frame-basis definition and
does not mint the authority it projects.

---
```

Successor, `EXECUTIVE_BASELINE.md#baseline-adoption-projection`:

```text
### Baseline-adoption projection

A baseline-adoption projection consumes the Product-owned Project
Reference-Frame Basis of PRODUCT_DEFINITION §7. Where that basis adopts
this profile, the projection records the selected profile mapping, exact
outcome, actor envelopes, evidence coordinates and revision conditions
needed in addition to the Product binding (§16). It is not a second
frame-basis definition and mints none of the authority it projects (P6;
rc.2 #baseline-adoption-projection).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#baseline-specific-activation-additions` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#baseline-specific-activation-additions` at rc.2:

```text
## Baseline-Specific Activation Additions

Every activation first carries the generic binding defined by
`REFERENCE_FRAME_METHOD.md#minimal-frame-activation-binding`.

For Worker activation, that binding is also the `STDO-UP-020` sufficient
execution intake and adds the exact inherited operation grant, mutation
subject, and write territory where applicable. For Reviewer activation, it
adds the exact claim, composition boundary, evaluated population, oracle,
ordinary or module path, falsification condition, and
`STDO-UP-007`/`STDO-UP-022` independence and assurance basis, Product-selected
severity scale, and required technical-triage capability. For Executive
activation, it adds the current Product-role map, MVP or release mandate,
evaluation frontier, closed-result and technical-triage ledger, priority and
boundary policy, conjunction rule, and exact disposition grant.

---
```

Successor, `EXECUTIVE_BASELINE.md#activation-additions`:

```text
### Activation additions

Every activation first carries the generic binding of REFERENCE_FRAME §11
(minimal activation binding). This profile adds, by frame (P0, P6; rc.2
#baseline-specific-activation-additions):

| Frame | Added to the generic binding |
|---|---|
| Worker | the binding is also the sufficient execution intake of ACTIVATION §1, and adds the exact inherited operation grant, mutation subject and write territory where applicable |
| Reviewer | the exact claim, composition boundary, evaluated population, oracle, ordinary or module path, falsification condition, the independence and assurance basis (EVALUATION §3 and §7), the Product-selected severity scale and the required technical-triage capability |
| Executive | the current Product-role map, the MVP or release mandate, the evaluation frontier, the closed-result and technical-triage ledger, the priority and boundary policy, the conjunction rule and the exact disposition grant |
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#baseline-specific-project-basis-additions` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#baseline-specific-project-basis-additions` at rc.2:

```text
## Baseline-Specific Project-Basis Additions

An adopting Product starts from the Project Reference-Frame Basis binding owned
by `SPEC_METHOD.md` and projected by
`templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md`. This optional profile
adds only the following profile-specific content. It is not a competing basis
definition or adoption authority.

```markdown
# STDO Baseline Adoption Additions

- exact STDO Reference Frame Baseline identity:
- Executive, Worker, and Reviewer declaration or acquisition references:
- role-specific actor capability, authority, and independence bindings:
- Product-selected severity and priority scales, current-boundary cutoff,
  non-waivable hard stops, and Reviewer-to-Executive triage relation:
- Worker result to Frame Method result mapping:
- twelve generic specialist-family declarations, non-material evidence, or
  explicit residuals:
- Product-testing claims, frame topology, material combination populations,
  scenario matrix, oracles, and required and forbidden authoritative paths:
- profile-specific activation refusal, closed-result, conjunction, and return
  relations:
- profile-specific qualification evidence and residuals:
```

---
```

Successor, `EXECUTIVE_BASELINE.md#project-basis-additions`:

```text
### Project-basis additions

The items of the template below add to the adoption record that
[§16 Adopt this baseline](#adopt-this-baseline) owns; an adopting Product
records both lists as one record, and where an item appears in both, the
§16 statement decides it, so the two lists are one record and not rivals.

An adopting Product starts from the Project Reference-Frame Basis of
PRODUCT_DEFINITION §7 and its starter template. This profile adds only the
following profile-specific content; it is not a competing basis definition
or adoption authority (P6, P2; rc.2
#baseline-specific-project-basis-additions):

```markdown
# Executive Baseline Adoption Additions

- exact Executive baseline profile identity:
- Executive, Worker and Reviewer declaration or acquisition references:
- role-specific actor capability, authority and independence bindings:
- Product-selected severity and priority scales, current-boundary cutoff,
  non-waivable hard stops, and the Reviewer-to-Executive triage relation:
- work-result to core-result mapping: ACTIVATION §3 construction
  availability, recorded by reference, with each project refinement of a
  work-result value mapped to its parent value's core value (ACTIVATION §3):
- the twelve generic family declarations, non-material evidence or
  explicit residuals:
- Product-testing claims, frame topology, material combination
  populations, scenario matrix, oracles, and required and forbidden
  authoritative paths:
- profile-specific activation refusal, closed-result, conjunction and
  return relations:
- profile-specific qualification evidence and residuals:
```
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#canonical-compression` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#canonical-compression` at rc.2:

```text
## Canonical Compression

`REFERENCE_FRAME_METHOD.md` defines the finite engagement atom. The selected
complete STDO cut defines specification, design, construction, assessment,
disposition, checkpoint, continuation, identity, and release law. This profile
maps three practical engagement frames onto those existing owners:

```text
existing project authority
  + selected complete STDO and Reference Frame Method basis
  + exact governed Product or Product-chain outcome and workspace basis
  + known evaluation inventory, dependencies, and residuals
  -> sufficient direct Worker activation, or materially required coordination
  -> where coordinated: Executive outcome/basis lock and finite ready frontier
  -> Worker and applicable specialist evaluations; Reviewer only where required
  -> closed results, applicable technical triage, and declared conjunction
  -> existing bounded decision authority, result recording, and next lawful action
  -> updated basis, coverage, residuals, and frontier
  -> repeat or stop
```

The three available frames are overlapping evaluation contexts, not a hierarchy
or actor topology. The Worker supplies the candidate subject but never activates the
Reviewer. The Reviewer evaluates but does not implement. The Executive applies
only decision authority already granted by Product, Goals, requirements,
accepted design, ticket, identity, or release law. The Worker carries only the
construction or transformation authority in its admitted intake. No frame gains
admission, publication, mutation, or other operation authority from its label.

This profile also derives twelve generic specialist-frame families: Product,
Product Composition, Design, Design Component, Public Boundary, Entity,
Operator, Owner, Effect, Reuse/Foundation, Install, and Proof. They separate recurring evaluation
questions that otherwise collapse across constitutional `WHAT`, structural
`HOW`, identity, authority, effects, foundations, installed subjects, and
evidence. They are available frame families, not mandatory actors, stages,
components, services, files, or runtime types. An activation selects only the
families material to its exact evaluation and retains an explicit residual for
any material family it cannot cover.

This profile also derives four Product-testing specialist-frame families:
user acceptance, end to end, integration, and unit. They are activated inside
the same conditionally selected engagement relation; they are not new
roles, stages, authorities, or a testing hierarchy. Their ordinary evidence
topology is:

```text
Product and accepted design
  |- user-outcome claims -> user-acceptance frames
  |- runnable causal-path claims -> end-to-end frames
  |- composition-boundary claims -> integration frames
  `- module-owned laws -> unit frames

bound results -> declared conjunction -> Product or release disposition
```

The fan-out assigns claims to their congruent evidence frames; it is not an
authority hierarchy or a claim that one frame decomposes into another.
Evidence may relate through declared conjunction, translation, falsification,
and re-entry. A broader frame cannot make a module-owned law true, and any
number of narrower green frames cannot establish an unevaluated Product
composition or user outcome.

A project may adopt this profile or define another reference-frame
configuration. That choice is admitted by the existing project authority that
owns the affected decision. A local axioms file may carry the decision; the file
does not become a new constitutional owner merely by carrying it.

---
```

Successor, `EXECUTIVE_BASELINE.md#1-canonical-compression`:

```text
## 1. Canonical compression

REFERENCE_FRAME defines the finite engagement unit. The selected complete
method cut defines specification, design, construction, assessment,
disposition, checkpoint, continuation, identity and release law. This
profile maps three practical engagement frames onto those owners; it owns
only the bindings its lead names and no rule of those owners (P6, P0; rc.2
#canonical-compression):

```text
existing project authority
  + selected complete method basis, REFERENCE_FRAME included
  + exact governed Product or Product-chain outcome and workspace basis
  + known evaluation inventory, dependencies and residuals
  -> a sufficient direct Worker activation, or coordination where material
  -> when coordinated: Executive locks outcome and basis, holds a finite ready frontier
  -> Worker and the applicable specialist evaluations; Reviewer only where required
  -> closed results, technical triage where applicable, declared conjunction
  -> existing bounded decision authority, result recording, next lawful action
  -> updated basis, coverage, residuals and frontier
  -> repeat or stop
```

The three frames are overlapping evaluation contexts. They are neither a
hierarchy nor an actor topology (P6; RF-009). The Worker supplies the
candidate and never activates the Reviewer. The Reviewer evaluates and does
not implement. The Executive applies only decision authority already
granted by Product, Goals, requirements, accepted design, a ticket, identity
law or release law. The Worker carries only the construction or
transformation authority of its admitted intake. No frame acquires
admission, publication, mutation or any other operation authority from its
label (P6).

The profile derives twelve generic specialist-frame families (§11):
Product, Product Composition, Design, Design Component, Public Boundary,
Entity, Operator, Owner, Effect, Reuse/Foundation, Install and Proof. They
keep apart recurring evaluation questions that otherwise collapse across
constitutional WHAT, structural HOW, identity, authority, effects,
foundations, installed subjects and evidence. They are available families,
not mandatory actors, stages, components, services, files or runtime types.
An activation selects only the families material to its exact evaluation
and keeps an explicit residual for any material family it cannot cover (P2,
P1).

The four product testing frames (user acceptance, end to end, integration,
unit) are tier-2 law in ASSURANCE §7. Under this profile they are activated
inside the same conditionally selected engagement relation; they add no
role, stage, authority or testing hierarchy. Their evidence topology, the
assignment of claims to congruent evidence frames, is ASSURANCE §7; a
broader frame cannot make a module-owned law true, and any number of
narrower green frames cannot establish an unevaluated Product composition
or user outcome (P6, P4a).

A project may adopt this profile or define another frame configuration
(§16). The executive configuration is selected where it fits the task; it
is not the method's default (§7 The executive configuration). Adopting the
profile is the Product authority's act (PRODUCT_DEFINITION §7), and each
decision a configuration makes is admitted by the existing authority that
owns it (ACTIVATION §1 Configuration, Admission of a configuration; §16).
A local axioms file may carry the decision; carrying it does not make the
file a new constitutional owner (P6).
```

Successor, `ASSURANCE.md#the-set`:

```text
### The set

Where the governing frame configuration (PRODUCT_DEFINITION §7) or the
admitted work authority selects testing frames for a Product promotion,
closure or release-assurance claim, testing is configured as a
claim-relative set of testing frames. Placement in this member makes the
set, and the law of §8 to §13 that serves it, available; it adopts nothing,
and each activation is decided by ACTIVATION §1 (Applicability). The kind
of runner does not select the frame; the evaluated claim, subject, path,
population, oracle and falsification boundary do (P6, P2; provenance
#derived-product-testing-frame-set). Each frame's `invalidation` row,
here and in §13, lists named instances of the material input change or
the changed basis of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); it adds no
other kind of invalidator. The ordinary configuration holds four
distinct frames:

- user acceptance evaluates the Product outcome from the user's supported
  frame;
- end to end evaluates the complete runnable causal realisation of that
  outcome;
- integration evaluates one material composition boundary and its
  interaction population; and
- unit evaluates one module-owned law; internal combinatorial complexity
  decides the proportional size and strategy of that evidence, not whether
  the law is eligible for unit proof.

They add no role, stage, authority or testing hierarchy. Their ordinary
evidence topology assigns each claim to its congruent frame (P6, P4a;
provenance #canonical-compression):

```text
Product and accepted design
  |- user-outcome claims -> user-acceptance frames
  |- runnable causal-path claims -> end-to-end frames
  |- composition-boundary claims -> integration frames
  `- module-owned laws -> unit frames

bound results -> declared conjunction -> Product or release disposition
```

The fan-out assigns claims to evidence; it is neither an authority
hierarchy nor a claim that one frame decomposes into another. Evidence
may relate through declared conjunction
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
translation (REFERENCE_FRAME §6), falsification and re-entry (P4a). A
broader frame cannot make a module-owned
law true, and any number of narrower green frames cannot establish an
unevaluated Product composition or user outcome (EVALUATION §1, the weaker
property never substitutes for the claimed one).

The frames may overlap, and one execution may supply evidence to several of
them; every result stays bound to its own claim. A label such as `UAT`,
`E2E`, `integration` or `unit` has no assurance value without the
corresponding frame declaration (P1, P6). Each frame below is given in the
shape of a frame declaration (REFERENCE_FRAME §13); "core result", here
and in §13, is a value of the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), recorded with the
predicate the frame's claim states.
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition` at rc.2:

```text
## Complete Engagement Transition

The following steps describe the coordinated branch selected under Engagement
Applicability. Direct Worker engagement preserves the same sufficient intake,
work-result algebra, closure conditions and owner boundaries without inserting
Executive appointment or a review that no applicable condition requires.

### 1. Existing Authority Selects The Basis

Goals, Product, requirements, accepted design, ticket, release, or an admitted
bounded proxy selects the outcome and work authority under its existing STDO
owner. The Product-owned Project Reference-Frame Basis projects that decision.

### 2. Executive Activates Worker

In the coordinated branch, Executive applies `REFERENCE_FRAME_METHOD.md`
activation to the `STDO-UP-020` sufficient execution intake. The activation identifies:

- selected complete STDO and project authority;
- exact governed outcome and checkpoint;
- affected causal relation set and governing invariants;
- selected computational relations and specialist frames;
- testing claims, exact subjects, frame topology, material combination
  populations, ordinary paths, oracles, and forbidden-path exclusions where
  testing evidence is required;
- Worker authority, capability envelope, and the exact inherited operation
  grant, subject, and write territory where mutation is authorized;
- evidence and qualification obligations;
- exclusions, prohibited competing paths, stop conditions, and re-entry
  conditions; and
- the exact bounded action already authorized.

If activation detects a known capability, authority, subject, basis, or
topology mismatch, it returns `activation_refusal` directly to Executive. No
Worker frame is active, no Worker evaluation occurs, and Executive must not
manufacture a Worker result to represent the failed activation.

### 3. Worker Returns To Executive

Every coordinated Worker activation terminates in one closed work result sent
to Executive. Direct work uses its declared result consumer:

```text
WorkerResult
  = candidate_ready(exact_subject, transition_evidence, residuals)
  | refused(reason, authority, evidence)
  | incomplete(residuals, evidence, stop_basis)
  | re_entry_requested(owner, material_relation, evidence)
```

The notation is explanatory and mandates no schema.

Each variant accompanies exactly one Reference Frame Method result under the
mapping in `Work result`: `satisfied -> candidate_ready`, `falsified ->
refused`, `indeterminate -> incomplete`, and `out_of_frame | invalid_basis ->
re_entry_requested`. The mapping applies only after lawful activation.

The Worker does not send a candidate directly into an implicitly active
Reviewer. It stops after returning the result.

### 4. Executive Evaluates The Work Result

For `refused`, `incomplete`, or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable `STDO-UP-020` disposition or reactivates work only when the current
authority already permits that action. None of these variants can be treated as
accepted progress merely because work occurred.

For `candidate_ready`, the Executive verifies the exact subject and determines
whether independent assessment is required by `STDO-UP-007`,
`STDO-UP-020`, `STDO-UP-022`, Product, release, risk, or the admitted work
contract. Green aggregate status cannot satisfy this step when a required
user-acceptance, end-to-end, integration, unit, or negative-path result is
missing, bound to another subject, or contradicted by a material frame result.

### 5A. Candidate Does Not Require Independent Review

In the coordinated branch, when independent review is not required, Executive
consumes the exact candidate, Worker self-review, transition evidence, and any mandatory
specialist-frame results. It applies `STDO-UP-020` disposition within its
decision envelope.

Self-review remains Worker evidence. The disposition does not relabel it as
independent.

### 5B. Candidate Requires Independent Review

When independent review is required, the Executive activates the Reviewer with:

- exact candidate and governing basis;
- exact claim, composition boundary, population, scope, and exclusions;
- applicable STDO and project authority;
- required evidence and ordinary assurance path;
- required user-acceptance, end-to-end, integration, unit, combinatorial, and
  negative-path frame results with their exact claims and populations;
- the Product-selected severity scale and exact affected Product claims;
- Reviewer capability and independence envelope; and
- invalidation and stop conditions.

The candidate is frozen before material reference exposure where
`STDO-UP-022` requires it. Otherwise the subject is stabilized to the exactness
required by `STDO-UP-007`, `STDO-UP-020`, and the claim.

### 6. Reviewer Returns To Executive

The Reviewer returns one closed evaluation containing:

- frame and activation identity;
- exact subject, basis, claim, scope, exclusions, and evaluated population;
- Reviewer actor and independence conditions;
- evidence and ordinary assurance path acquired;
- Reference Frame Method result;
- findings, counterexamples, and adjacent observations;
- for each finding, affected claim, severity, causal assessment and confidence,
  blast radius, workaround, repair complexity, regression risk, and residual
  uncertainty where supportable; and
- invalidation conditions and re-entry owner where applicable.

### Reviewer Result And Triage Projection

The Reviewer payload projection is total across the Reference Frame Method
result algebra. `complete`, `indeterminate`, and `not_applicable` below classify
the finding-level triage payload; they are not new evaluation results,
dispositions, priorities, or lifecycle states.

| Reference Frame Method result | Finding and triage payload | Executive consumption constraint |
|---|---|---|
| `satisfied` | explicit no-finding state; triage `not_applicable`; evidence, residuals, and invalidation remain present | priority and current-boundary effect are `not_applicable` to this review result unless another exact consumed result supplies a finding |
| `falsified` | one or more exact findings; triage is `complete` where supported and preserves `indeterminate` fields where evidence cannot close them | apply Product-owned priority and boundary policy without mechanically mapping severity to disposition |
| `indeterminate` | partial finding or observation state; triage `indeterminate`; exact evidence gaps and residual uncertainty | retain uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or a closed finding |
| `out_of_frame` | the evaluated claim requires an undeclared material relation or evaluator capability; triage `indeterminate`; name the missing relation or capability and exact reconfiguration pressure | refine or reconfigure a capable activation and retain the claim as unresolved; do not consume the result as satisfaction or falsification |
| `invalid_basis` | basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse result consumption and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. Reviewer returns it separately with triage
`not_applicable` to that claim and exact repricing or re-entry pressure. The
Executive returns it to its declared owner without creating a claim-relative
block or another review round from severity alone.

The Reviewer returns to Executive, not Worker. It does not edit the candidate,
direct the repair, or authorize continuation.

### 7. Executive Disposes And Checkpoints

The Executive verifies that every consumed result remains bound to the current
subject and basis, revalidates the complete Product view and current MVP or
release mandate, applies any declared result conjunction, assigns priority,
records the effect on the current promotion boundary, and acts on exactly one
`STDO-UP-020` disposition within its grant:

- `accept`;
- `local_repair`;
- `re_enter`; or
- `reject`.

`STDO-UP-020` remains the owner of each disposition, exact accepted checkpoint,
and next already-authorized bounded action. A repair creates a new candidate.
An affected review is reactivated against that candidate. Acceptance does not
widen the Product outcome or authorize an unselected successor.

Severity does not mechanically select priority or block promotion. Priority
does not erase severity or waive a hard stop. The Executive determines blocking
from the exact affected claim, current mandate, applicable hard stops, and
Product-owned cutoff policy. An unsupported technical assessment is returned
through a new or refined activation rather than silently rewritten.

### Executive Promotion Constraint Projection

| Consumed condition | Required Executive constraint |
|---|---|
| valid falsification of a mandatory claim governed by a non-waivable hard stop | current promotion boundary blocks regardless of assigned priority or decision cutoff |
| valid finding below the Product-owned decision cutoff with no hard stop | no mechanical block follows; apply the Product-owned policy and retain any accepted residual explicitly |
| observation outside the exact evaluated claim | treat as bounded repricing or re-entry input; do not create a claim-relative block or another review round by severity label |
| unsupported or materially incomplete technical assessment | reactivate a capable evaluation or retain `indeterminate`; do not rewrite Reviewer evidence |

---
```

Successor, `EXECUTIVE_BASELINE.md#12-complete-engagement-transition`:

```text
## 12. Complete engagement transition

The steps below describe the coordinated branch selected under §3. Direct
Worker engagement keeps the same sufficient intake, work-result algebra,
closure conditions and owner boundaries without inserting an Executive
appointment, or a review that no applicable condition requires (P0, P6;
rc.2 #complete-engagement-transition).

### 1. Existing authority selects the basis

Goals, Product, requirements, accepted design, a ticket, release law or an
admitted bounded proxy selects the outcome and the work authority under its
existing owner. The Product-owned Project Reference-Frame Basis
(PRODUCT_DEFINITION §7) projects that decision (P6; rc.2
#1-existing-authority-selects-the-basis).

### 2. Executive activates Worker

In the coordinated branch the Executive applies `activate` (REFERENCE_FRAME
§5) to the sufficient execution intake of ACTIVATION §1. The packet is
REFERENCE_FRAME §11; for this step it identifies (P0, P6; rc.2
#2-executive-activates-worker):

- the selected complete method and project authority;
- the exact governed outcome and checkpoint;
- the affected causal relation set and the governing invariants;
- the selected computational relations and specialist frames;
- where testing evidence is required: the testing claims, exact subjects,
  frame topology, material combination populations, ordinary paths,
  oracles and forbidden-path exclusions (ASSURANCE §7 to §9);
- the Worker's authority and capability envelope, and, where mutation is
  authorised, the exact inherited operation grant, subject and write
  territory;
- the evidence and qualification obligations;
- exclusions, prohibited competing paths, stop conditions and re-entry
  conditions; and
- the exact bounded action already authorised.

If activation detects a known capability, authority, subject, basis or
topology mismatch, it returns `activation_refusal` directly to the
Executive, with the cause and core value REFERENCE_FRAME §5 gives it. No
Worker frame is active, no Worker evaluation occurs, and the
Executive does not manufacture a Worker result to represent the failed
activation (P5, P6).

### 3. Worker returns to Executive

Every coordinated Worker activation ends in one closed work result sent to
the Executive; direct work uses its declared result consumer (P5, P6; rc.2
#3-worker-returns-to-executive):

```text
WorkerResult
  = candidate_ready(exact_subject, transition_evidence, residuals)
  | refused(reason, authority, evidence)
  | incomplete(residuals, evidence, stop_basis)
  | re_entry_requested(owner, material_relation, evidence)
```

The notation explains and mandates no schema. The material relation of
`re_entry_requested` names its cause, authority or basis, which is part of
the value. Each value maps to exactly one core value for "a candidate is
available" under
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability),
read as in §5 Work result; the mapping applies only after lawful
activation. The Worker does not send a candidate directly into an
implicitly active Reviewer. It stops after returning the result (P5,
P6).

### 4. Executive evaluates the work result

For `refused`, `incomplete` or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable disposition, or reactivates work only where current authority
already permits that action. None of these variants is accepted progress
because work occurred (P6, P5; rc.2 #4-executive-evaluates-the-work-result).

Whatever the variant, an effect of uncertain completion, one the work
result names `completion_unknown` or names `not_effected` with its end not
established ([ACTIVATION §3 Effects](ACTIVATION.md#effects)), is
reconciled under
[ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart), sufficiently for
the next dependent action, before work is reactivated, the effect is
repeated or any action that depends on it is taken (P5, P6).

For `candidate_ready`, the Executive verifies the exact subject and decides
whether independent assessment is required. It applies the boundaries at
which this method requires it,
[TICKETS UP-007](TICKETS.md#execution-and-verification-authority-separation-up-007);
the execution relation's assessment where required (ACTIVATION §1); method
qualification ([EVALUATION §7](EVALUATION.md#7-qualification-of-frames-and-of-the-method));
and the further boundaries the governing basis adds, as
[EVALUATION §3](EVALUATION.md#3-independent-assessment) permits: Product,
release, risk or the admitted work contract. What counts as independent is
EVALUATION §3's. Green aggregate status cannot satisfy this step when a
required user-acceptance, end-to-end, integration, unit or negative-path
result is missing, bound to another subject, or contradicted by a material
frame result (P6; ASSURANCE §10).

### 5A. Candidate does not require independent review

In the coordinated branch, when independent review is not required, the
Executive consumes the exact candidate, the Worker's self-review, the
transition evidence and any mandatory specialist results, and applies the
disposition within its decision envelope. Self-review stays Worker
evidence; the disposition does not relabel it as independent (P6; rc.2
#5a-candidate-does-not-require-independent-review).

### 5B. Candidate requires independent review

When independent review is required, the Executive activates the Reviewer
with (P6, P3; rc.2 #5b-candidate-requires-independent-review):

- the exact candidate and governing basis;
- the exact claim, composition boundary, population, scope and exclusions;
- the applicable method and project authority;
- the required evidence and the ordinary assurance path;
- the required user-acceptance, end-to-end, integration, unit,
  combinatorial and negative-path frame results, with their exact claims and
  populations;
- the Product-selected severity scale and the exact affected Product claims;
- the Reviewer's capability and independence envelope; and
- invalidation and stop conditions.

Where EVALUATION §7 requires it, the candidate is frozen before material
reference exposure. Otherwise the subject is stabilised to the exactness
that EVALUATION §3, ACTIVATION §7 and the claim require (P3, P6).

### 6. Reviewer returns to Executive

The Reviewer returns one closed evaluation in the shape of EVALUATION §4,
which here contains (P6, P5; rc.2 #6-reviewer-returns-to-executive):

- frame and activation identity;
- the exact subject, basis, claim, scope, exclusions and evaluated
  population;
- the Reviewer actor and the independence conditions;
- the evidence and the ordinary assurance path acquired;
- the core result (FOUNDATIONS §4 Results);
- findings, counterexamples and adjacent observations;
- for each finding, where supportable: the affected claim, severity, causal
  assessment and confidence, blast radius, workaround, repair complexity,
  regression risk and residual uncertainty; and
- invalidation conditions and, where applicable, the re-entry owner.

The finding-level triage payload projects over the result algebra as
EVALUATION §4 (Result and triage projection) states; in this profile the
assessor there is the Reviewer and the decision owner is the Executive. The
Reviewer returns to the Executive, not to the Worker, and returns no
disposition; a recommendation is evidence only (EVALUATION §4). It does not
edit the candidate, direct the repair or authorise continuation (P6; rc.2
#reviewer-result-and-triage-projection).

### 7. Executive disposes and checkpoints

The Executive verifies that every consumed result is still bound to the
current subject and basis, revalidates the complete Product view and the
current MVP or release mandate, applies any declared result conjunction
(FOUNDATIONS §4 Conjunction of results), assigns priority, records the
effect on the current promotion boundary, and acts on exactly one
disposition within its grant: `accept`, `local_repair`, `re_enter` or
`reject` (ACTIVATION §3; P6, P5; rc.2
#7-executive-disposes-and-checkpoints).

ACTIVATION §3 and §5 stay the owners of each disposition, the exact accepted
checkpoint and the next already-authorised bounded action. The disposition
is the acceptance result; neither `candidate_ready` nor a satisfied review
result is acceptance (FOUNDATIONS §4 Results). A repair creates
a new candidate, and an affected review is reactivated against it.
Acceptance does not widen the Product outcome or authorise an unselected
successor (P4b, EVALUATION §5).

When a finding blocks the current promotion boundary, and that severity
selects neither priority nor a block and priority waives no hard stop, is
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
read with the Executive as the decision owner; this profile restates none
of it. The Executive records its determination as the current-boundary
effect (§5 Technical triage, severity, priority and boundary effect). An
unsupported technical assessment returns through a new or refined
activation rather than being silently rewritten (P6, P1).

### Promotion constraint projection

(P6, P5; rc.2 #executive-promotion-constraint-projection)

The projection is the table of
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
with the Executive as its decision owner, for the consumed conditions it
names: a valid falsification of a mandatory claim governed by a
non-waivable hard stop; any other finding meeting one of that section's
four conditions, a finding below the Product-owned decision cutoff
included; a finding meeting none of them; and an observation outside the
exact evaluated claim. For the Executive, the governed outcome or decision
that section names is read under the current Product mandate, so the Executive
determines blocking from the exact affected claim, the current mandate,
the applicable hard stops and the Product-owned cutoff policy. This
profile adds one row, its application of the
`indeterminate` row of
[EVALUATION §4 Result and triage projection](EVALUATION.md#result-and-triage-projection)
and of the Executive's exclusions (§8):

| Consumed condition | Required Executive constraint |
|---|---|
| an unsupported or materially incomplete technical assessment | a capable evaluation is reactivated, or `indeterminate` is kept; Reviewer evidence is not rewritten |
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#computational-whole-path-evaluation` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#computational-whole-path-evaluation` at rc.2:

```text
### Computational Whole-Path Evaluation

For material computational composition or recurrence work, compose the selected
interface claims with Operator, Owner, Reuse/Foundation and Proof to evaluate
one complete producer-to-consumer path under `DESIGN_MODULE_METHOD.md`
`STDO-UP-019` and recurrence law. Bind fact establishment, each consumer,
validity and invalidation, effects, retained alternatives and accumulated work.
Evaluate equivalent computation across different domain names without assuming
semantic equivalence. Qualification challenges the design's declared workload
and operational assumptions; it preserves independent scope, freshness and
effect checks that serve distinct supported obligations.

Return an identifiable complete-path result and its evidence to the declared
decision consumer. A collection of local successes cannot replace that result.
Design-only evidence establishes only the design claim; actual work claims
require observations on the selected path. Reuse valid unchanged results and
activate affected reassessment on material path, basis or workload change. This
is a bounded composition of existing frames, not a permanent actor, extra
specialist family, per-helper review or separate accounting ledger.
```

Successor, `ASSURANCE.md#computational-whole-path-evaluation`:

```text
### Computational whole-path evaluation

For material computational composition or recurrence work, the selected
interface claims are composed with evaluations of the path's operators,
owners, reused foundations and proof, to evaluate one complete
producer-to-consumer path under the design profile's computational
realisation and recurrence law (DESIGN_MODULE). The evaluation binds fact
establishment, each consumer, validity and invalidation, effects, retained
alternatives and accumulated work. It evaluates equivalent computation
across different domain names without assuming semantic equivalence.
Qualification challenges the design's declared workload and operational
assumptions, and preserves the independent scope, freshness and effect
checks that serve distinct supported obligations (P4a, P1, P2; provenance
#computational-whole-path-evaluation).

An identifiable complete-path result and its evidence return to the
declared decision consumer; a collection of local successes cannot replace
that result. Design-only evidence establishes only the design claim; claims
about actual work need observations on the selected path. Valid unchanged
results are reused, and affected reassessment is activated on a material
change of path, basis or workload. This is a bounded composition of
existing frames, not a permanent actor, an extra frame family, a per-helper
review or a separate accounting ledger (P4b, P2).
```

Successor, `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames`:

```text
### Relation to the testing and interface frames

Where this set is adopted, the product testing frames of ASSURANCE §7 supply
claim-congruent evidence to one or more Proof evaluations. Proof is not a
testing hierarchy or an aggregate-green frame: user-acceptance, end-to-end,
integration and unit results keep their distinct claims and coordinates (P6,
P4a; rc.2 #derived-product-testing-frame-set).

The end-to-end interface integration frame (ASSURANCE §13) relates the
Public Boundary, Design, Operator, Owner and Proof families to the
integration, end-to-end and user-acceptance frames. Its computational
whole-path evaluation composes the selected interface claims with Operator,
Owner, Reuse/Foundation and Proof. Neither adds a thirteenth family, a fifth
testing type, a role or a universal activation gate (P2; rc.2
#derived-end-to-end-interface-integration-frame,
#computational-whole-path-evaluation).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization` at rc.2:

```text
### Counterexample Localization

A testing counterexample is returned to its earliest supported causal frontier
on the declared path. The frontier contains the causally minimal violated owner
relations or seam coordinates established by the evidence; earliest means
minimal under the declared causal relation, not first in log or clock order.

The localization result represents exactly one of:

- one unique violated locus;
- a jointly established set of incomparable earliest violated loci whose
  combined violation is necessary to the supported causal explanation;
- unresolved alternative frontiers when the evidence supports several possible
  causal explanations but cannot establish which occurred; or
- `indeterminate` when the evidence cannot support a bounded frontier.

Localization records the subject, basis, frontier form and members, causal
evidence, expected relations, observed counterexample, and downstream claims
invalidated by it. It does not collapse a jointly established set into one
arbitrary owner or misreport unresolved alternatives as a joint cause.

A localized frontier does not itself authorize broader test expansion,
compatibility repair, another controller, or reinterpretation of unchanged
upstream meaning. Any resulting scope or design change follows the existing
re-entry relation.

---
```

Successor, `ASSURANCE.md#12-counterexample-localisation`:

```text
## 12. Counterexample localisation

A testing counterexample is returned to its earliest supported causal
frontier on the declared path. The frontier holds the causally minimal
violated owner relations or seam coordinates the evidence establishes;
earliest means minimal under the declared causal relation, not first in log
or clock order (P5, P6; provenance #counterexample-localization).

The localisation result represents exactly one of (P5, P1):

- one unique violated locus;
- a jointly established set of incomparable earliest violated loci whose
  combined violation is necessary to the supported causal explanation;
- unresolved alternative frontiers, when the evidence supports several
  possible causal explanations but cannot establish which occurred; or
- `indeterminate`, when the evidence cannot support a bounded frontier.

The four forms are a refinement of the core under the rule of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), for the predicate "the
evidence establishes the counterexample's earliest violated loci on the
declared path". One unique violated locus and a jointly established set
map to `satisfied`. Unresolved alternative frontiers map to
`indeterminate`, naming the alternatives that further evidence must
decide between. The fourth form is the core value `indeterminate` itself,
naming the evidence a bounded frontier needs. The form travels with the
value as the domain outcome, so a joint set stays distinct from a unique
locus and unresolved alternatives stay distinct from an unbounded
frontier. Purpose and material relation: a localisation combines with
other results in the one core, and an unresolved causal explanation is
never read as an established one (P5, P1, P6).

Localisation records the subject, basis, frontier form and members, causal
evidence, expected relations, the observed counterexample and the
downstream claims it invalidates. It does not collapse a jointly
established set into one arbitrary owner, and it does not report
unresolved alternatives as a joint cause (P5, P4b).

A localised frontier does not itself authorise broader test expansion,
compatibility repair, another controller or a reinterpretation of unchanged
upstream meaning. A resulting scope or design change follows the existing
re-entry relation (SPEC_METHOD §4; P6).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#coverage-application` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#coverage-application` at rc.2:

```text
## Coverage Application

The three engagement frames do not claim to contain the complete STDO Product
or project workspace. They organize finite evaluations over specialist frames.

| Known evaluation | Primary engagement frame | Authority or specialist input |
|---|---|---|
| exact method, project, and work basis | Executive | complete STDO cut; current Goals/Product/requirements/design/work authority |
| affected causal cone and frame configuration | Executive, challenged by Worker and Reviewer | `STDO-UP-017..020`; domain, identity, dependency, implementation, and history frames |
| generic specialist-family coverage and cross-frame seam conservation | Executive for configuration; Worker and Reviewer for their exact evaluations | material Product, Product Composition, Design, Design Component, Public Boundary, Entity, Operator, Owner, Effect, Reuse/Foundation, Install, and Proof declarations or authoritative acquisition paths; explicit non-material and residual dispositions |
| bounded realization and self-review | Worker | accepted design; `STDO-UP-023` capability/foundation selection where material; capability/reuse, implementation, environment, and proof frames |
| candidate and transition evidence | Worker | `STDO-UP-020` and exact identity/evidence relations |
| user can obtain the Product-defined outcome through supported surfaces | Worker for execution and self-review; Reviewer where independent assurance is required | derived user-acceptance frame; Product, requirement, UX, identity, installed-subject, and acceptance inputs |
| complete authoritative installed path realizes the outcome | Worker for execution and self-review; Reviewer where independently assessed | derived end-to-end frame; composition, authority, lifecycle, persistence, recovery, replay, and negative-reachability inputs |
| material interfaces compose across their interaction population | Worker and Reviewer according to the claim | derived integration frames; actual participant, carrier, state, configuration, failure, and recovery inputs |
| module-owned laws hold | Worker and Reviewer according to the claim | derived unit frames; Ontology, IACS, public module contract, algebra, calculation, state-machine, invariant, and module-bounded combination inputs |
| obsolete and rival Product paths are absent, unreachable, or refused | Worker for deletion evidence; Reviewer for exact-subject challenge where required | distinct production-closure and assurance/source-closure graphs; package, consumer, mutation, sabotage, reconstruction, and history frames |
| independent exact-subject assessment and technical triage where required | Reviewer | `STDO-UP-007`, `STDO-UP-020`, `STDO-UP-022`, Product-selected severity scale, live implementation and assurance frames |
| result conjunction, priority, promotion-boundary effect, and disposition | Executive | exact closed Worker, Reviewer, and mandatory specialist results; current Product and MVP or release mandate; Product-owned triage policy |
| checkpoint and continuation | Executive under existing authority | `STDO-UP-020`; current Goals/Product/release boundary |
| missing-frame and topology-change response | Executive with pressure from any frame | Reference Frame Method coverage and revision functions |

The Executive derives the complete known evaluation inventory from the selected
STDO members, project domain, outcome, history, dependencies, and workspace.
Operational full coverage retains every unknown, uncovered, conditional,
conflicted, or authority-excluded residual required by
`REFERENCE_FRAME_METHOD.md`.

Executive visibility is not coverage. Every material evaluation still requires
a capable frame, admissible evidence, and identified semantic and decision
owners. Every material construction, transformation, admission, publication,
or mutation also requires its existing operation owner and exact grant.

---
```

Successor, `EXECUTIVE_BASELINE.md#14-coverage-application`:

```text
## 14. Coverage application

The three engagement frames do not claim to contain the complete Product or
project workspace. They organise finite evaluations over specialist frames
(P0, P2; rc.2 #coverage-application).

| Known evaluation | Primary engagement frame | Authority or specialist input |
|---|---|---|
| exact method, project and work basis | Executive | the complete method cut; current Goals, Product, requirements, design and work authority |
| affected causal cone and frame configuration | Executive, challenged by Worker and Reviewer | ACTIVATION §1 intake and execution unit with the design profile's bounded-frame conservation laws; domain, identity, dependency, implementation and history frames |
| generic family coverage and cross-frame seam conservation | Executive for configuration; Worker and Reviewer for their exact evaluations | material declarations or authoritative acquisition paths for the twelve families of §11; explicit non-material and residual dispositions |
| bounded realisation and self-review | Worker | accepted design; the design profile's capability-and-foundation selection where material; capability and reuse, implementation, environment and proof frames |
| candidate and transition evidence | Worker | ACTIVATION §7 and the exact identity and evidence relations |
| a user can obtain the Product-defined outcome through supported surfaces | Worker for execution and self-review; Reviewer where independent assurance is required | the user-acceptance frame (ASSURANCE §7); Product, requirement, UX, identity, installed-subject and acceptance inputs |
| the complete authoritative installed path realises the outcome | Worker for execution and self-review; Reviewer where independently assessed | the end-to-end frame (ASSURANCE §7); composition, authority, lifecycle, persistence, recovery, replay and negative-reachability inputs |
| material interfaces compose across their interaction population | Worker and Reviewer according to the claim | integration frames (ASSURANCE §7); actual participant, carrier, state, configuration, failure and recovery inputs |
| module-owned laws hold | Worker and Reviewer according to the claim | unit frames (ASSURANCE §7); the design's ontology and carrier inventory, public module contract, algebra, calculation, state-machine, invariant and module-bounded combination inputs |
| obsolete and rival Product paths are absent, unreachable or refused | Worker for deletion evidence; Reviewer for exact-subject challenge where required | the distinct production-closure and assurance/source-closure graphs (ASSURANCE §9); package, consumer, mutation, sabotage, reconstruction and history frames |
| independent exact-subject assessment and technical triage where required | Reviewer | EVALUATION §3 and §7; ACTIVATION §1; the Product-selected severity scale; live implementation and assurance frames |
| result conjunction, priority, promotion-boundary effect and disposition | Executive | the exact closed Worker, Reviewer and mandatory specialist results; current Product and MVP or release mandate; the Product-owned triage policy |
| checkpoint and continuation | Executive under existing authority | ACTIVATION §5; the current Goals, Product and release boundary |
| missing-frame and topology-change response | Executive, with pressure from any frame | REFERENCE_FRAME §8 and §10 |

The Executive derives the complete known evaluation inventory from the
selected method members, the project domain, the outcome, history,
dependencies and the workspace. Operational full coverage keeps every
unknown, uncovered, conditional, conflicted or authority-excluded residual
REFERENCE_FRAME §8 requires (P4b, P5).

Executive visibility is not coverage. Every material evaluation still needs
a capable frame, admissible evidence and identified semantic and decision
owners; every material construction, transformation, admission, publication
or mutation also needs its existing operation owner and exact grant (P6;
REFERENCE_FRAME §8, authority coverage).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-frame` at rc.2:

```text
### Derived End-To-End Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Does the exact Product subject realize the claimed outcome through the complete authoritative Product path, including every material interface, owner, state transition, effect, persistence, continuation, recovery, and projection boundary? |
| subject and basis | exact deployed, installed, or otherwise runnable Product form, composition design, supported entry, selected owner and dependency set, ordinary runtime configuration, and Product claim |
| material manifold | complete causal producers and consumers from entry to outcome; interface contracts; authority transitions; state, event, persistence, process, continuation, retry, recovery, and projection relations; competing paths |
| coordinates | artifact and installed-tree identity, entry, operation, selected definition and owner, path and edge identities, process, event prefix, state, configuration, dependency, result, replay, and scenario identity |
| governing invariants | Product and accepted-design composition laws; exact-subject and assurance congruence; path singularity where required; lifecycle, authority, persistence, replay, recovery, and release law |
| authority | bounded evaluation only; observation may expose internal evidence but may not bypass, repair, replace, or reinterpret the Product path |
| evidence | supported entry invocation, observed semantic path and authority edges, owner receipts, durable events, state transitions, outputs, replay or reconstruction where claimed, installed artifact identity, and negative-path observations |
| capability envelope | ability to execute and observe the complete Product path without changing it, distinguish authoritative from rival paths, and reproduce material state and failure relations |
| exclusions | source-only substitutes for runnable-Product claims, direct invocation below the supported entry, test doubles at claimed real boundaries, test-only routing, hidden retries or repair, omitted persistence or fresh-process boundaries, and output equality without path evidence |
| result | one Reference Frame Method result bound to the exact end-to-end claim, with exercised composition edges, unexercised material paths, counterexamples, and residual combinations |
| invalidation | material artifact, install, dependency, configuration, interface, owner, path, lifecycle, persistence, recovery, projection, test semantics, or evidence-population change |

The expected output is necessary but not sufficient. Reaching it through a
forbidden or obsolete path falsifies the end-to-end claim. A test is not end to
end merely because it starts and finishes in one process, crosses many lines,
or carries an end-to-end label.
```

Successor, `ASSURANCE.md#end-to-end-frame`:

```text
### End-to-end frame

(P6, P3; provenance #derived-end-to-end-frame)

| Frame element | End to end |
|---|---|
| evaluation family | Does the exact Product subject realise the claimed outcome through the complete authoritative Product path, including every material interface, owner, state transition, effect, persistence, continuation, recovery and projection boundary? |
| subject and basis | the exact deployed, installed or otherwise runnable Product form, the composition design, the supported entry, the selected owner and dependency set, the ordinary runtime configuration and the Product claim |
| material manifold | the complete causal producers and consumers from entry to outcome; interface contracts; authority transitions; state, event, persistence, process, continuation, retry, recovery and projection relations; competing paths |
| coordinates | artifact and installed-tree identity, entry, operation, selected definition and owner, path and edge identities, process, event prefix, state, configuration, dependency, result, replay and scenario identity |
| governing invariants | Product and accepted-design composition law; exact-subject and assurance congruence; path singularity where required; lifecycle, authority, persistence, replay, recovery and release law |
| authority | bounded evaluation only; observation may expose internal evidence but may not bypass, repair, replace or reinterpret the Product path |
| evidence | supported entry invocation, the observed semantic path and authority edges, owner receipts, durable events, state transitions, outputs, replay or reconstruction where claimed, installed artifact identity, and negative-path observations |
| capability envelope | ability to execute and observe the complete Product path without changing it, to tell the authoritative path from rival paths, and to reproduce material state and failure relations |
| exclusions | source-only substitutes for runnable-Product claims, direct invocation below the supported entry, test doubles at claimed real boundaries, test-only routing, hidden retries or repair, omitted persistence or fresh-process boundaries, and equal output without path evidence |
| result | one core result bound to the exact end-to-end claim, with the exercised composition edges, unexercised material paths, counterexamples and residual combinations |
| invalidation | a material change of artifact, install, dependency, configuration, interface, owner, path, lifecycle, persistence, recovery, projection, test semantics or evidence population |

The expected output is necessary and not sufficient. Reaching it through a
forbidden or obsolete path falsifies the end-to-end claim. A test is not end
to end because it starts and finishes in one process, crosses many lines or
carries an end-to-end label (P6, P1).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-interface-integration-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-interface-integration-frame` at rc.2:

```text
## Derived End-To-End Interface Integration Frame

`urn:stdo:reference-frame:end-to-end-interface-integration:v1` is a composite
refinement in `urn:stdo:bounded-context:reference-frame-evaluation`. Acquire it
from this heading under the exact selected baseline basis. It relates
[Public Boundary, Design, Operator, Owner and Proof](#derived-generic-specialist-frame-set)
to [Integration](#derived-integration-frame),
[End To End](#derived-end-to-end-frame) and
[User Acceptance](#derived-user-acceptance-frame). It adds neither a thirteenth
generic family nor a fifth testing type, role or universal activation gate.

| Frame element | Derived application |
|---|---|
| evaluation family | Does one outcome remain constructable, understandable and correctly realized across its material interface chain, with sufficient participant context and conserved meaning, authority and cause? |
| subject and basis | one Product outcome and independently stated oracle; governing requirements and design basis, exact source/workspace checkpoint, contracts and finite case population; declared participant roles, functional path, dependencies, configuration and capabilities for design; actual participants, callable selection, supported entry/exit and exact runnable artifact/install for claims over their realization |
| material manifold | producers, consumers, transformations and effect owners as declared for design or actually selected for realized claims; functional preconditions/postconditions, value/reference domains, lifecycle/time, supplied context, mutable subject, refusals, observations and user-visible result at each material seam |
| coordinates and equality | distinct Product, artifact/install, workspace, observation, invocation, candidate, admitted result and evidence identities; exact revisions, domain, units, cardinality, ordering, empty/null/default meaning and validity interval; equal shape or output does not imply equal meaning, provenance or authority |
| governing invariants | selected Product/requirement/design/interface law; Reference Frame Method declaration, conjunction and translation law; the claim boundaries and obligations below; existing testing and assurance owners retain their laws |
| authority | existing owners retain semantic, operation, admission and reserved decision authority; the activation grants bounded evaluation, with construction only under its existing exact operation grant; the declared decision consumer disposes the closed result |
| evidence | source-linked contracts and both selected sides; design relations and explicitly unresolved realization facts for design claims; actual supplied request/context and response, callable/configuration identity, owner validation/effect/observation records and ordinary caller outcome for claims over those realized relations; independently derived expected relations and disclosed substitution limits |
| capability envelope | competence in the outcome, functional composition, domain/lifecycle semantics, participant capabilities and causal diagnosis; sufficient access to the exact subject and evidence without altering a reviewed subject; required independence remains claim-relative |
| exclusions | hidden context or privilege, rival contract truth, inferred authority, undeclared substitutes, private/test-only paths for ordinary-path claims, candidate output treated as admission, fixture success treated as real user evidence, and unsupported whole-Product or all-future-case conclusions |
| result and relations | each activated claim returns `satisfied`, `falsified`, `indeterminate`, `out_of_frame` or `invalid_basis` with its exact evidence, coverage, causal findings and residuals; shared evidence is referenced once and mandatory claims compose only through a declared same-basis or lawful-translation conjunction to the named decision consumer |
| invalidation | material contract, domain, participant, prompt/context, capability, callable path, configuration, translation, relevant workspace observation, lifecycle, oracle or evidence-population change invalidates affected conclusions; unchanged valid evidence and owner rulings remain reusable |
| qualification | representative sensitivity and refusal cases below, bound to actual subjects, actor envelopes and independently stated expected relations; mechanical source checks do not supply semantic or live-user qualification |

### Interface Integration Claim Boundaries

| Claim | Evaluation and evidence boundary |
|---|---|
| Contract sufficiency | Can each participant determine and perform its responsibility from the declared interface and available context? Source-grounded design evaluation may establish this claim without an implemented runtime; unresolved realizability or actor-context questions remain explicit. |
| Boundary congruence | Do the actual selected producers, transformations and consumers preserve the declared domains, meanings, lifecycle and authority? Acquire both sides and their exchanges for an actual-composition claim; design correspondence alone does not prove implementation behavior. |
| Path realization | Does the exact runnable subject use the authoritative entry-to-outcome path through its material state, effect and observation boundaries? Matching output through another path is insufficient. |
| User usability | Can the ordinary human, LLM or software caller obtain the selected outcome using only its declared context, access and supported surface? Internal success or validator-aware fixtures cannot establish this claim. |

The activation selects claims from the work's applicability and states the
scope reason for unselected claims. Design-only work does not require
unavailable runtime evidence or report runtime/UAT satisfaction. An unknown
material condition keeps its dependent claim unresolved; omission cannot
close it. A full end-to-end usability claim requires all four distinct results
and their explicit conjunction. Transport, parse, admission, semantic
satisfaction, operation completion and user success are not interchangeable.

### Interface Integration Obligations

Reuse existing truth surfaces. The working record adds only missing
cross-interface relations; schemas, prompts, adapters, indexes and tests do
not become another contract owner. For each material seam:

1. Bind the functional input domain, producer success postconditions, consumer
   preconditions, permitted effects, refusals and observable exit. Direct
   successful handoff requires the producer guarantees to meet the consumer
   preconditions. An interface may instead emit candidates: candidate output,
   later admission and semantic assessment remain distinct declared stages.
   A normal model refusal or inadmissible candidate does not by itself falsify
   an adequately declared candidate interface; evaluate the exact promised
   outcome and refusal behavior.
2. Make material actor obligations and domains available through the actual
   interface/context or an exact locator the actor can lawfully resolve.
   Bind the LLM role, instructions, supplied context, tools and model/transport
   configuration where material. Generic governance access does not replace
   the Product-specific contract or authorize inference of hidden validator
   rules. Existing deterministic owners compute available facts and expose
   their owned relation to context and validation through reuse or proven
   equivalent projections. Semantic actors judge meaning within that domain;
   reserved owner rulings, eligibility, authority and admission are not
   inferred from an actor response or frame label.
3. Preserve domain and temporal meaning through serialization, parsing,
   normalization and adaptation. A lawful translation binds source/target
   coordinates, preserved meaning, accepted loss, provenance, governing owner
   and refusal conditions. Distinguish proposed, admitted, assessed and
   completed states; active input from historical context; current validity
   from mere byte availability. Equal wire shape is not a translation proof.
4. Observe the relevant current mutable workspace for each later operation.
   Bind that observation separately from immutable authority, artifacts,
   history and prior candidates. Changed support invalidates dependent
   conclusions; unaffected accepted work remains reusable. A snapshot does
   not replace the current subject, and an actor change alone is no reason to
   repeat still-valid work.
5. Follow the actual callable path and existing effect owners through the
   selected exit and any required fresh observation. Hidden fallback, state
   injection, manually repaired output, private entry or undeclared retry
   cannot support an ordinary real-path claim. A pure function acquires no new
   event lifecycle merely because this frame evaluates it.
6. Preserve diagnostic cause through wrappers and projections. Apply
   [Counterexample Localization](#counterexample-localization): report the
   supported causal frontier, not merely the first log or clock occurrence.
   Retain the originating seam, bounded field/path, expected domain or basis,
   observed mismatch and evidence locator where available, plus downstream
   symptoms, successful work and declared continuation or block. Preserve
   joint causes, alternative frontiers and indeterminacy; do not invent a
   unique cause. Product redaction rules still govern sensitive content.
   Missing required diagnostic evidence remains a named gap. Return the
   smallest supported owner/re-entry; diagnosis grants no repair or retry.

Evidence acquisition follows
[Assurance Subject Acquisition And Evaluation](#assurance-subject-acquisition-and-evaluation).
Acquire owner facts through existing surfaces and evaluate them with an
independent contract-derived oracle. Computed facts, contextual judgments and
reserved owner rulings retain their distinct owners and validity scopes.

For an LLM-interface usability claim, use clean-room LLM UAT with the ordinary
supplied context and permitted tools, without private implementation knowledge
or fixture assistance. Expected outcomes precede response inspection. Include
the sunny case and ordinary ambiguity/negative cases material to the claim.
Disclose substitutes; replayed or fabricated responses prove only their stated
narrower relation, not live-provider usability. Do not edit responses or
silently retry until green. Live claims require live evidence under the
existing UAT law, not a new universal live-provider requirement during design.

Apply [Steel-Thread Delivery](#steel-thread-delivery): an early sunny thread
can establish bounded evidence while unexercised claims remain open. This
frame adds no exhaustive-hardening prerequisite, scenario quota, controller,
runtime, generator, routine human approval, new ledger or automatic extra
agent. Existing authority selects proportionate assurance and any further
operation. Return the four claim dispositions, exact exercised subject/path,
supported mismatch, retained work, substitutions, residuals and invalidators
in the existing work carrier; the result is not acceptance or a next-action
grant.

### Computational Whole-Path Evaluation

For material computational composition or recurrence work, compose the selected
interface claims with Operator, Owner, Reuse/Foundation and Proof to evaluate
one complete producer-to-consumer path under `DESIGN_MODULE_METHOD.md`
`STDO-UP-019` and recurrence law. Bind fact establishment, each consumer,
validity and invalidation, effects, retained alternatives and accumulated work.
Evaluate equivalent computation across different domain names without assuming
semantic equivalence. Qualification challenges the design's declared workload
and operational assumptions; it preserves independent scope, freshness and
effect checks that serve distinct supported obligations.

Return an identifiable complete-path result and its evidence to the declared
decision consumer. A collection of local successes cannot replace that result.
Design-only evidence establishes only the design claim; actual work claims
require observations on the selected path. Reuse valid unchanged results and
activate affected reassessment on material path, basis or workload change. This
is a bounded composition of existing frames, not a permanent actor, extra
specialist family, per-helper review or separate accounting ledger.

### Interface Integration Qualification

These are representative source-contract discriminators, not an executed
trial, universal test quota or whole-Product qualification. Each selected
case binds its own exact subject, oracle, evidence and claim scope.

| Case | Required discrimination |
|---|---|
| Empty and nonempty eligible domains | Ordinary context makes both domains usable; a universal empty-value workaround cannot replace the governing domain. A hidden required rule defeats contract sufficiency even if the validator correctly refuses. |
| Adequate candidate contract and rejected response | Distinguish legitimate refusal/admission filtering from an inadequate interface or a violated success guarantee; model variability alone is not frame failure. |
| Same-response or historical-only reference | Eligibility and lifecycle come from the owning domain; available or equal-looking references are not automatically current admissible inputs. |
| Individually valid but temporally mismatched carriers | Different observations or admission states can falsify boundary congruence despite matching shapes. |
| Meaning-changing translation | Loss of units, default, identity or ordering is detected against the independent outcome oracle, even when both shapes validate. |
| Fixture knows a hidden rule | Mechanical success leaves user usability unproved; it cannot conceal missing ordinary actor context. |
| Expected output through a forbidden path | Path realization is falsified; output equality does not discharge the actual-path obligation. |
| Changed workspace and reusable accepted work | Refresh affected context and dependent evidence while preserving unaffected valid work; history does not substitute for the current subject. |
| Wrapped or ambiguous failure | Preserve the supported originating causal frontier and uncertainty without replacing it with a downstream symptom or an invented unique cause. |
| Design-only sufficient contract | A bounded contract result can close while runtime and user claims remain unclaimed or unresolved according to their applicability; no runtime/UAT satisfaction is inferred. |

---
```

Successor, `ASSURANCE.md#13-end-to-end-interface-integration-frame`:

```text
## 13. End-to-end interface integration frame

`urn:stdo:reference-frame:end-to-end-interface-integration:v1` is a
composite refinement whose identity resolves in
`urn:stdo:bounded-context:reference-frame-evaluation` (owned by
REFERENCE_FRAME) under the exact selected basis; its assurance law is
stated here. It relates the evaluation of public boundaries, design,
operators, owners and proof to the integration, end-to-end and
user-acceptance frames of §7. Like the set, it is available and is
activated only where the governing frame configuration or admitted work
authority selects it. It adds no fifth testing type, role or
universal activation gate (P2, P3; provenance
#derived-end-to-end-interface-integration-frame).

| Frame element | End-to-end interface integration |
|---|---|
| evaluation family | Does one outcome stay constructable, understandable and correctly realised across its material interface chain, with sufficient participant context and conserved meaning, authority and cause? |
| subject and basis | one Product outcome and an independently stated oracle; the governing requirements and design basis, exact source or workspace checkpoint, contracts and finite case population; for design claims, the declared participant roles, functional path, dependencies, configuration and capabilities; for claims over their realisation, the actual participants, callable selection, supported entry and exit, and the exact runnable artifact or install |
| material manifold | the producers, consumers, transformations and effect owners, as declared for design claims or actually selected for realised claims; at each material seam, the functional preconditions and postconditions, value and reference domains, lifecycle and time, supplied context, mutable subject, refusals, observations and user-visible result |
| coordinates and equality | distinct Product, artifact or install, workspace, observation, invocation, candidate, admitted result and evidence identities; exact revisions, domain, units, cardinality, ordering, empty, null or default meaning and validity interval; equal shape or output implies no equal meaning, provenance or authority |
| governing invariants | the selected Product, requirement, design and interface law; REFERENCE_FRAME declaration and translation law; the conjunction of results of FOUNDATIONS §4; the claim boundaries and obligations below; the existing testing and assurance owners keep their laws |
| authority | existing owners keep semantic, operation, admission and reserved decision authority; the activation grants bounded evaluation, with construction only under its existing exact operation grant; the declared decision consumer disposes the closed result |
| evidence | source-linked contracts and both selected sides; for design claims, design relations and explicitly unresolved realisation facts; for claims over realised relations, the actual supplied request, context and response, callable and configuration identity, owner validation, effect and observation records and the ordinary caller's outcome; independently derived expected relations and disclosed substitution limits |
| capability envelope | competence in the outcome, functional composition, domain and lifecycle semantics, participant capabilities and causal diagnosis; sufficient access to the exact subject and evidence without altering a reviewed subject; required independence stays claim-relative |
| exclusions | hidden context or privilege, rival contract truth, inferred authority, undeclared substitutes, private or test-only paths for ordinary-path claims, candidate output treated as admission, fixture success treated as real user evidence, and unsupported whole-Product or all-future-case conclusions |
| result and relations | each activated claim returns a core result with its exact evidence, coverage, causal findings and residuals; shared evidence is referenced once; mandatory claims compose only through a declared same-basis or lawful-translation conjunction (FOUNDATIONS §4 Conjunction of results) to the named decision consumer |
| invalidation | a material change of contract, domain, participant, prompt or context, capability, callable path, configuration, translation, relevant workspace observation, lifecycle, oracle or evidence population invalidates the affected conclusions; unchanged valid evidence and owner rulings stay reusable |
| qualification | the representative sensitivity and refusal cases below, bound to actual subjects, actor envelopes and independently stated expected relations; mechanical source checks supply no semantic or live-user qualification |

### Claim boundaries

(P6, P1; provenance #interface-integration-claim-boundaries)

| Claim | Evaluation and evidence boundary |
|---|---|
| contract sufficiency | Can each participant determine and perform its responsibility from the declared interface and the available context? Source-grounded design evaluation may establish this claim without an implemented runtime; unresolved realisability or actor-context questions stay explicit. |
| boundary congruence | Do the actual selected producers, transformations and consumers preserve the declared domains, meanings, lifecycle and authority? An actual-composition claim acquires both sides and their exchanges; design correspondence alone proves no implementation behaviour. |
| path realisation | Does the exact runnable subject use the authoritative entry-to-outcome path through its material state, effect and observation boundaries? Matching output through another path is insufficient. |
| user usability | Can the ordinary human, LLM or software caller obtain the selected outcome using only its declared context, access and supported surface? Internal success or validator-aware fixtures cannot establish this claim. |

The activation selects claims from the work's applicability (ACTIVATION §1)
and states the scope reason for each unselected claim; an unselected claim
has no result. Design-only work
does not require unavailable runtime evidence and does not report runtime or
UAT satisfaction. An unknown material condition keeps its dependent claim
unresolved: the claim's result is never `satisfied` and names the
condition as what would decide it
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Standing); omission
cannot close it. A full end-to-end usability claim
needs all four distinct results and their explicit conjunction
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
in which an unselected claim is uncovered coverage. Transport,
parse, admission, semantic satisfaction, operation completion and user
success are not interchangeable (P5, P6).

### Obligations

Existing truth surfaces are reused. The working record adds only missing
cross-interface relations; schemas, prompts, adapters, indexes and tests do
not become another contract owner (P6, P2; provenance
#interface-integration-obligations). For each material seam:

1. Bind the functional input domain, producer success postconditions,
   consumer preconditions, permitted effects, refusals and observable exit.
   Direct successful handoff requires the producer's guarantees to meet the
   consumer's preconditions. An interface may instead emit candidates:
   candidate output, later admission and semantic assessment stay distinct
   declared stages. A normal model refusal or an inadmissible candidate does
   not by itself falsify an adequately declared candidate interface; the
   exact promised outcome and refusal behaviour are evaluated (P4a, P5).
2. Make material actor obligations and domains available through the
   actual interface or context, or through an exact locator the actor can
   lawfully resolve. Bind the LLM role, instructions, supplied context,
   tools and model or transport configuration where material. Generic
   governance access does not replace the Product-specific contract or
   authorise inference of hidden validator rules. Existing deterministic
   owners compute the available facts and expose their owned relation to
   context and validation by reuse or a proven equivalent projection.
   Semantic actors judge meaning within that domain; reserved owner
   rulings, eligibility, authority and admission are not inferred from an
   actor response or a frame label (P0, P6, P1).
3. Preserve domain and temporal meaning through serialisation, parsing,
   normalisation and adaptation. A lawful translation binds source and
   target coordinates, preserved meaning, accepted loss, provenance,
   governing owner and refusal conditions. Distinguish proposed, admitted,
   assessed and completed states; active input from historical context;
   current validity from mere byte availability. Equal wire shape is no
   translation proof (P1, P3; REFERENCE_FRAME §6).
4. Observe the relevant current mutable workspace for each later
   operation, and bind that observation separately from immutable
   authority, artifacts, history and prior candidates. Changed support
   invalidates dependent conclusions; unaffected accepted work stays
   reusable. A snapshot does not replace the current subject, and a change
   of actor alone is no reason to repeat still-valid work (P3, P4b;
   ACTIVATION §7).
5. Follow the actual callable path and the existing effect owners through
   the selected exit and any required fresh observation. A hidden fallback,
   state injection, manually repaired output, private entry or undeclared
   retry cannot support an ordinary real-path claim. A pure function
   acquires no new event lifecycle because this frame evaluates it (P6,
   P3).
6. Preserve diagnostic cause through wrappers and projections. Apply §12:
   report the supported causal frontier, not merely the first log or clock
   occurrence. Keep the originating seam, bounded field or path, expected
   domain or basis, observed mismatch and evidence locator where available,
   with downstream symptoms, successful work and the declared continuation
   or block. Preserve joint causes, alternative frontiers and
   indeterminacy; do not invent a unique cause. Product redaction rules
   still govern sensitive content. Missing required diagnostic evidence
   stays a named gap. Return the smallest supported owner or re-entry;
   diagnosis grants no repair or retry (P5, P4b, P6).

Evidence acquisition follows §11: owner facts are acquired through existing
surfaces and evaluated with an independent contract-derived oracle.
Computed facts, contextual judgments and reserved owner rulings keep their
distinct owners and validity scopes (P6).

For an LLM-interface usability claim, clean-room LLM UAT is used, with the
ordinary supplied context and permitted tools and without private
implementation knowledge or fixture assistance. Expected outcomes are
recorded before responses are inspected. The sunny case and the ordinary
ambiguity and negative cases material to the claim are included.
Substitutes are disclosed; replayed or fabricated responses prove only
their stated narrower relation, not live-provider usability. Responses are
not edited, and nothing is silently retried until green. Live claims need
live evidence under §2, not a new universal live-provider requirement
during design (P6, P5; EVALUATION §3, expectations before exposure).

An early sunny thread can establish bounded evidence while the unexercised
claims stay open (the sequencing heuristic of SPEC_METHOD §8). This frame
adds no exhaustive-hardening prerequisite, scenario quota, controller,
runtime, generator, routine human approval, new ledger or automatic extra
agent. Existing authority selects proportionate assurance and any further
operation. The result returns, for each of the four claims, its core
result or the scope reason it was not selected, the exact
exercised subject and path, the supported mismatch, retained work,
substitutions, residuals and invalidators in the existing work carrier; it
is neither acceptance nor a grant of the next action (P2, P6; ACTIVATION
§6).

### Computational whole-path evaluation

For material computational composition or recurrence work, the selected
interface claims are composed with evaluations of the path's operators,
owners, reused foundations and proof, to evaluate one complete
producer-to-consumer path under the design profile's computational
realisation and recurrence law (DESIGN_MODULE). The evaluation binds fact
establishment, each consumer, validity and invalidation, effects, retained
alternatives and accumulated work. It evaluates equivalent computation
across different domain names without assuming semantic equivalence.
Qualification challenges the design's declared workload and operational
assumptions, and preserves the independent scope, freshness and effect
checks that serve distinct supported obligations (P4a, P1, P2; provenance
#computational-whole-path-evaluation).

An identifiable complete-path result and its evidence return to the
declared decision consumer; a collection of local successes cannot replace
that result. Design-only evidence establishes only the design claim; claims
about actual work need observations on the selected path. Valid unchanged
results are reused, and affected reassessment is activated on a material
change of path, basis or workload. This is a bounded composition of
existing frames, not a permanent actor, an extra frame family, a per-helper
review or a separate accounting ledger (P4b, P2).

### Qualification

These are representative source-contract discriminators: not an executed
trial, a universal test quota or whole-Product qualification. Each selected
case binds its own exact subject, oracle, evidence and claim scope (P6,
P5; provenance #interface-integration-qualification; EVALUATION §7).

| Case | Required discrimination |
|---|---|
| empty and non-empty eligible domains | Ordinary context makes both domains usable; a universal empty-value workaround cannot replace the governing domain. A hidden required rule defeats contract sufficiency even when the validator correctly refuses. |
| adequate candidate contract and rejected response | Legitimate refusal or admission filtering is told apart from an inadequate interface or a violated success guarantee; model variability alone is no frame failure. |
| same-response or historical-only reference | Eligibility and lifecycle come from the owning domain; available or equal-looking references are not automatically current admissible inputs. |
| individually valid but temporally mismatched carriers | Different observations or admission states can falsify boundary congruence despite matching shapes. |
| meaning-changing translation | Loss of units, default, identity or ordering is detected against the independent outcome oracle, even when both shapes validate. |
| fixture knows a hidden rule | Mechanical success leaves user usability unproved; it cannot hide missing ordinary actor context. |
| expected output through a forbidden path | Path realisation is falsified; equal output does not discharge the actual-path obligation. |
| changed workspace and reusable accepted work | Affected context and dependent evidence are refreshed while unaffected valid work is kept; history does not stand in for the current subject. |
| wrapped or ambiguous failure | The supported originating causal frontier and its uncertainty are kept, not replaced by a downstream symptom or an invented unique cause. |
| design-only sufficient contract | A bounded contract result can close while runtime and user claims stay unclaimed or unresolved according to their applicability; no runtime or UAT satisfaction is inferred. |
```

Successor, `EXECUTIVE_BASELINE.md#relation-to-the-testing-and-interface-frames`:

```text
### Relation to the testing and interface frames

Where this set is adopted, the product testing frames of ASSURANCE §7 supply
claim-congruent evidence to one or more Proof evaluations. Proof is not a
testing hierarchy or an aggregate-green frame: user-acceptance, end-to-end,
integration and unit results keep their distinct claims and coordinates (P6,
P4a; rc.2 #derived-product-testing-frame-set).

The end-to-end interface integration frame (ASSURANCE §13) relates the
Public Boundary, Design, Operator, Owner and Proof families to the
integration, end-to-end and user-acceptance frames. Its computational
whole-path evaluation composes the selected interface claims with Operator,
Owner, Reuse/Foundation and Proof. Neither adds a thirteenth family, a fifth
testing type, a role or a universal activation gate (P2; rc.2
#derived-end-to-end-interface-integration-frame,
#computational-whole-path-evaluation).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-executive-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-executive-frame` at rc.2:

```text
## Derived Executive Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Is the bounded outcome and execution basis authorized? Which frames and actors are capable? Is a returned result exact and current? What priority, current-boundary effect, `STDO-UP-020` disposition, and next action follow from the current Product mandate? |
| subject and basis | complete selected STDO cut; exact Goals/Product/requirements/design/work authority; current MVP or release mandate; current workspace and checkpoint; open findings and technical triage; Product-selected triage policy; proxy grant where used |
| material manifold | outcome, mandate, affected causal cone, evaluation inventory, frame configuration, actor envelopes, evidence obligations, returned results and technical triage, priority, boundary effect, re-entry owners, and already-authorized continuation boundary |
| coordinates | exact method, project, outcome, mandate, authority, checkpoint, candidate, evidence, finding, triage-policy, and actor identities |
| governing invariants | `RF-001..017`; `STDO-UP-017..020`; applicable identity, ticket, assurance, and release law |
| authority | existing Product/work frame-set and decision authority or its admitted bounded proxy; no operation authority or other authority arises from the Executive label |
| evidence | live authority surfaces, frame results, Reviewer technical triage, exact candidate identity, transition evidence, coverage residuals, and specialist-frame results |
| capability envelope | enough method, Product, release or MVP, authority, workspace, triage, and actor-selection competence to configure, prioritize, and dispose the bounded evaluation; implementation expertise may be delegated to specialist frames |
| exclusions | candidate/Product/worktree byte mutation and implementation effects while occupying Executive, implementation ownership, silently rewriting Reviewer evidence or severity, independent-review claims without a qualifying activation, semantic reconstruction owned elsewhere, and disposition outside the admitted grant |
| result | one Reference Frame Method result, assigned priority and current-boundary effect, plus an existing `STDO-UP-020` disposition where the basis is decidable |
| invalidation | material method, authority, outcome, mandate, triage policy, checkpoint, candidate, evidence, finding, capability, or topology change |

The Executive frame does not introduce `authorize` or `no_action` as peer
STDO dispositions. Activation is the `REFERENCE_FRAME_METHOD.md` function;
bounded candidate disposition remains exactly `accept`, `local_repair`,
`re_enter`, or `reject` under `STDO-UP-020`.

Priority and current-boundary effect are decision projections, not additional
Reference Frame Method results or `STDO-UP-020` dispositions. If Executive
cannot rely on the supplied severity or technical assessment, it reactivates a
capable evaluation or retains the uncertainty; it does not silently rewrite the
Reviewer result.

### Steel-Thread Delivery

Executive sequences delivery around a steel thread: the smallest real,
runnable path from a supported Product entry to a material outcome through
the selected composition. Establish that path early and expand it in bounded
increments. Where it already exists, extend or revalidate the affected
thread. Select increments by consequential uncertainty, dependency and
interface reach, and failure impact.

Early end-to-end and integration evidence prunes incompatible construction
choices before they spread. Use it to settle the exercised interfaces,
preserve working composition, and concentrate construction on unresolved
obligations. Each passing thread establishes only the relations and
conditions actually exercised; untested branches, interaction combinations,
refusal and recovery paths retain their material proof obligations. Revisit
settled construction decisions when material counterevidence invalidates
their basis.

During construction, use focused deterministic regression and targeted
judgment probes to resolve material uncertainty. Use unit evidence for
module-owned laws under the testing frames. Schedule substantial,
resource-intensive user-acceptance cycles near release or when a bounded
capability is considered complete enough to qualify. An early focused user
probe remains appropriate when it decides a material outcome uncertainty.

The [Product testing frames](#derived-product-testing-frame-set) retain their
distinct claims and govern the necessary scenarios, independent assessments,
and repetitions. Reuse qualified results while their exact subject and basis
remain valid; rerun affected assurance when a material change invalidates it.
Executive selects this sequence under the existing mandate and activates
construction through the existing operation grants.

---
```

Successor, `EXECUTIVE_BASELINE.md#8-derived-executive-frame`:

```text
## 8. Derived Executive frame

The Executive frame, in the shape of a frame declaration (REFERENCE_FRAME
§13; P6, P0; rc.2 #derived-executive-frame):

| Frame element | Executive |
|---|---|
| evaluation family | Is the bounded outcome and execution basis authorised? Which frames and actors are capable? Is a returned result exact and current? Which priority, current-boundary effect, disposition and next action follow from the current Product mandate? |
| subject and basis | the complete selected method cut; the exact Goals, Product, requirements, design and work authority; the current MVP or release mandate; the current workspace and checkpoint; open findings and their technical triage; the Product-selected triage policy; the proxy grant where one is used |
| material manifold | outcome, mandate, affected causal cone, evaluation inventory, frame configuration, actor envelopes, evidence obligations, returned results and technical triage, priority, boundary effect, re-entry owners and the boundary of already-authorised continuation |
| coordinates | exact method, project, outcome, mandate, authority, checkpoint, candidate, evidence, finding, triage-policy and actor identities |
| governing invariants | RF-001 to RF-017 (REFERENCE_FRAME §3); the execution relation and intake of ACTIVATION §1 with the design profile's bounded-frame conservation laws; applicable identity, carrier, assurance and release law |
| authority | the existing Product or work frame-set and decision authority, or its admitted bounded proxy; no operation or other authority arises from the label |
| evidence | live authority surfaces, frame results, Reviewer technical triage, exact candidate identity, transition evidence, coverage residuals and specialist results |
| capability envelope | enough method, Product, release or MVP, authority, workspace, triage and actor-selection competence to configure, prioritise and dispose the bounded evaluation; implementation expertise may be delegated to specialist frames |
| exclusions | candidate, Product or worktree byte mutation and implementation effects while occupying the frame; implementation ownership; silently rewriting Reviewer evidence or severity; claiming independent review without a qualifying activation; semantic reconstruction owned elsewhere; disposition outside the admitted grant |
| result | one core result (FOUNDATIONS §4 Results), the assigned priority and current-boundary effect, and one existing disposition (ACTIVATION §3 Disposition) where the basis is decidable |
| invalidation | a material change of method, authority, outcome, mandate, triage policy, checkpoint, candidate, evidence, finding, capability or topology |

The frame adds no `authorize` or `no_action` disposition. Activation is the
`activate` function of REFERENCE_FRAME §5; candidate disposition stays
exactly `accept`, `local_repair`, `re_enter` or `reject` (ACTIVATION §3,
Disposition). Priority and current-boundary effect are decision
projections, neither core results nor dispositions. If the Executive cannot
rely on a supplied severity or technical assessment, it reactivates a
capable evaluation or keeps the uncertainty; it never silently rewrites the
Reviewer result (P5, P6).

### Steel-thread delivery

The Executive sequences delivery around a steel thread: the smallest real,
runnable path from a supported Product entry to a material outcome through
the selected composition. The path is established early and widened in
bounded increments; where it already exists, the affected thread is extended
or revalidated. Increments are chosen for consequential uncertainty,
dependency and interface reach, and failure impact (P2; rc.2
#steel-thread-delivery; the generic sequencing heuristic is SPEC_METHOD §8).
The steel thread is this profile's selected strategy under the
construction relation ([ACTIVATION §1 Strategy](ACTIVATION.md#construction-relation)):
its rationale is early feedback on the end-to-end composition at the cost
of later widening; other strategies remain lawful for other
configurations; no superiority over them is claimed, and the rationale
states the objective the selection serves and its cost (P2, P6).

Early end-to-end and integration evidence prunes incompatible construction
choices before they spread; it settles the exercised interfaces, keeps
working composition, and concentrates construction on unresolved
obligations. Each passing thread establishes only the relations and
conditions actually exercised; untested branches, interaction combinations,
and refusal and recovery paths keep their material proof obligations.
Settled construction decisions are revisited when material counterevidence
invalidates their basis (P6, P4b).

During construction, focused deterministic regression and targeted
judgment probes resolve material uncertainty, and unit evidence covers
module-owned laws under the testing frames (ASSURANCE §7). Substantial,
resource-intensive user-acceptance cycles are scheduled near release or
when a bounded capability is complete enough to qualify; an early focused
user probe stays appropriate where it decides a material outcome
uncertainty (P2, ACTIVATION §7 proof cadence).

The product testing frames keep their distinct claims and govern the
necessary scenarios, independent assessments and repetitions. Qualified
results are reused while their exact subject and basis stay valid; affected
assurance is rerun when a material change invalidates it. The Executive
selects this sequence under the existing mandate and activates construction
only through the existing operation grants (P6, P4b).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-integration-frame` (disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-integration-frame` at rc.2:

```text
### Derived Integration Frame

| Frame element | Derived application |
|---|---|
| evaluation family | Do the actual participants at one declared material composition boundary satisfy their joint contract across the combinations of state, authority, configuration, timing, failure, and recovery that can change the boundary result? |
| subject and basis | exact interface or composition declaration, actual participating implementations or exact substitutes admitted by the bounded claim, governing Product/requirement/design law, and interaction population |
| material manifold | both sides of the boundary, shared carriers, preconditions, postconditions, authority and ownership, ordering, state, configuration, failure, retry, recovery, translation, and competing participants |
| coordinates | participant and version identities, interface and carrier revision, state, configuration, dependency, interaction case, input, output, failure, and evidence identity |
| governing invariants | declared interface and composition laws, complete participant admission, atomicity and reconstruction where applicable, and exact assurance boundary under `STDO-UP-022` |
| authority | bounded boundary evaluation only; no integration result establishes an unevaluated Product outcome or authorizes a substitute participant |
| evidence | actual exchanges, admitted carriers, state transitions, contract verdicts, failures, retries, recovery observations, interaction combinations, and participant identities |
| capability envelope | competence and access to exercise and observe the real composition seam, identify participant substitution, and vary every material interaction dimension |
| exclusions | mocks or stubs that hide the claimed real contract, one-sided contract assertions, happy-path-only exchange, helper-call equivalence, flattened versions or states, and projection of a boundary result to the whole Product without a governing relation |
| result | one Reference Frame Method result for the declared integration claim, with covered combinations, counterexamples, omitted interactions, and invalidation conditions |
| invalidation | material participant, interface, carrier, state, configuration, dependency, timing, failure, recovery, or interaction-population change |

A substitute or test double may support a deliberately narrower claim only when
its equivalence boundary and exclusions are explicit. Its result cannot be
promoted to evidence that the real participant or Product composition was
exercised.
```

Successor, `ASSURANCE.md#integration-frame`:

```text
### Integration frame

(P6, P4a; provenance #derived-integration-frame)

| Frame element | Integration |
|---|---|
| evaluation family | Do the actual participants at one declared material composition boundary satisfy their joint contract across the combinations of state, authority, configuration, timing, failure and recovery that can change the boundary result? |
| subject and basis | the exact interface or composition declaration, the actual participating implementations or exact substitutes the bounded claim admits, the governing Product, requirement and design law, and the interaction population |
| material manifold | both sides of the boundary, shared carriers, preconditions, postconditions, authority and ownership, ordering, state, configuration, failure, retry, recovery, translation and competing participants |
| coordinates | participant and version identities, interface and carrier revision, state, configuration, dependency, interaction case, input, output, failure and evidence identity |
| governing invariants | declared interface and composition law, complete participant admission, atomicity and reconstruction where applicable, and the exact assurance boundary (EVALUATION §1) |
| authority | bounded boundary evaluation only; no integration result establishes an unevaluated Product outcome or authorises a substitute participant |
| evidence | actual exchanges, admitted carriers, state transitions, contract verdicts, failures, retries, recovery observations, interaction combinations and participant identities |
| capability envelope | competence and access to exercise and observe the real composition seam, identify participant substitution and vary every material interaction dimension |
| exclusions | mocks or stubs that hide the claimed real contract, one-sided contract assertions, happy-path-only exchange, helper-call equivalence, flattened versions or states, and projection of a boundary result to the whole Product without a governing relation |
| result | one core result for the declared integration claim, with covered combinations, counterexamples, omitted interactions and invalidation conditions |
| invalidation | a material change of participant, interface, carrier, state, configuration, dependency, timing, failure, recovery or interaction population |

A substitute or test double may support a deliberately narrower claim only
when its equivalence boundary and exclusions are explicit. Its result
cannot be promoted to evidence that the real participant or Product
composition was exercised (P6, EVALUATION §1).
```
