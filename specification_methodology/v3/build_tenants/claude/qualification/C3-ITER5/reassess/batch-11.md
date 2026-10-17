# I5-03 reading batch 11

Rows: 20. Members: ['SPEC_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `SPEC_METHOD.md#change-management-rule` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#change-management-rule` at rc.2:

```text
## Change Management Rule

Every substantive change begins with intake triage, an explicit declared change
intent, and a lawful re-entry point into the constitutional chain.

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

### Computed Classification And Treatment

Intake supplies one reusable classification result rather than requiring each
role to reconstruct the same facts. `C` denotes reproducible facts and declared
rule application; `J` denotes residual semantic or materiality judgment; `O`
denotes a ruling reserved to its actual owner. These annotations grant no
authority and introduce no calculus kind, runtime, classifier interface, or
mandatory document.

The explicitly selected source, worksite, or qualification capability produces
C over the exact request and desired outcome, known targets and effects,
operation grant and work lifetime, Product Definition and governing basis,
baseline and available candidate, declared relations, accepted design and
trace bindings, evidence, and applicable rules. Its output identifies the
producer and procedure revision, inputs, result, scope, source routes,
reproduction relation, unknowns and invalidators. Missing candidate or evidence
is an input state, not a claim that nothing changed.

The computed result must expose:

1. **Authority traversal.** Follow explicit source, ownership, dependency,
   composition and projection declarations from the affected targets and
   effects. Identify each reached layer and owner, its exact basis and
   changed/unchanged/unknown relation, the traversed edges, and the unresolved
   frontier. Include root, authority and grant changes even when Public bytes
   are equal. An absent edge does not prove irrelevance; undeclared or
   semantically uncertain materiality remains J.
2. **Public delta.** Enumerate the complete relevant serialized member universe
   under its owning declaration and applicable projection, including helper and
   generated dependencies. Report added and removed identities and every
   retained member with changed typed value or bytes, with exact before/after
   values. A rename is removal plus addition unless its owner supplies an
   identity-preserving relation. Missing candidate, incomplete enumeration,
   ambiguous identity or unavailable projection leaves the affected delta
   unknown; membership equality alone proves no value equality.
3. **Accepted-design coverage.** Join changed bytes and relations to explicit
   accepted scope, traces and acceptance evidence. Distinguish covered,
   missing, stale, ambiguous and outside-scope evidence. A filename, listed
   artifact or digest alone establishes no accepted coverage. Current trace
   coverage is a computed fact; residual semantic sufficiency remains J.
4. **Rule-determined treatment.** Apply only declared rules with sufficient
   input facts, recording their owners, matched predicates and consequences.
   Expose the smallest lawful re-entry, next action, applicable evidence or
   assessment, reserved ruling and carrier lifetime, with any conflict or
   missing premise still unresolved. A label or filename cannot select the
   route. When rules settle the question, invent no residual judgment.

A Public delta or other nonconformance does not itself require changing the
governing contract. If that contract remains sufficient for the authorized
outcome, reject or locally repair the candidate within its grant. Re-enter
the actual governing owner when the explicitly selected desired outcome
requires changed meaning or an applicable assessment establishes governing
insufficiency. C determines that consequence only from sufficient declared
premises; unresolved intended meaning or necessity is J and any reserved
decision remains O. Candidate behavior cannot author its own target law.

Unknown treatment withholds dependent reliance or promotion, not unrelated
authorized work. An existing bounded construction or evidence grant may permit
the cheapest useful discriminator, including obtaining the first candidate,
without asserting that the candidate is conformant. It carries its own exact subject,
territory, operations and stop conditions. Update the affected C result before
dependent effects or promotion rely on newly available evidence. Correct a
mistaken route at its smallest affected owner; preserve the original cause,
attempted subject, observed effect state and valid progress. Retry requires
the applicable outcome, authority and safe-recovery conditions; an unknown
effect state cannot be silently treated as no effect.

A new role, conversation or resumption reuses valid C after checking exact
applicability. Changed request, candidate, basis, owner/root relation,
projection, design trace/acceptance, rule, configuration or material evidence
invalidates its affected claims before reliance. Preserve predecessor and
successor identities, changed inputs, surviving facts and affected J
dependencies; recompute the wider frontier where independence is unproved.
`TICKET_METHOD.md` owns the existing carrier and recorded-J/O continuity rules.

---
```

Successor, `SPEC_METHOD.md#4-change-management`:

```text
## 4. Change management

Every substantive change begins with intake triage, an explicit declared
change intent and a lawful re-entry point into the constitutional chain
(P4b, P2; rc.2 #change-management-rule).

### Foundation to law: change management and ambiguity

This family (F11 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides how a change enters the chain, how its classification is computed
and reused, how ambiguity is governed and how a shared interface is
migrated. Its instance premises, which the commitments do not supply, are
named in the rows as follows: changing specification, the specification
changes while work proceeds; one front door, reports of every kind arrive
at one product; shared interfaces, a shared interface has several
producers and consumers; reserved decisions, a decision may be taken
under declared policy or be reserved to a human authority. Standing of
the commitments cited (FOUNDATIONS §3): P0 recovered; P1, P2, P3, P4a and
P6 independent; P4b derived from P0 and P2, with P0's premise that
step-produced facts are not re-acquirable; P5 derived from P0 and P6,
with P0's open-world premise.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 independent; P2 independent; instance: changing specification, one front door | By P6 a governing relation is accepted only by its owner, so a change re-enters at the layer that owns what it changes and is accepted there. By P2 the work follows what changes, not what the report is called, so the label a report arrives under does not select its process, and a change that re-enters below Goals asserts that nothing above it changes. | [§4](#4-change-management); [Universal intake triage](#universal-intake-triage), the six determinations; [Change classes](#change-classes); [Procedures](#procedures) | the six change classes with their names, re-entry points and flows, and the four procedures: domain choices of this member; where the class is recorded: [TICKETS §4](TICKETS.md#change-class) | 1, 9 |
| P1 independent; P6 independent; P5 derived; instance: one front door | By P1 a frame's name carries no meaning, and by P5 a diagnosis holds only where evidence tests it, so a diagnosis is supported only by frames that test it against their own variables and evidence, and the same analysis under another frame name adds no evidence. The frame that exposes a failure need not contain its cause, and by P6 a diagnosis grants no repair. | [Universal intake triage](#universal-intake-triage), the triangulation | the smallest sufficient frame configuration for each case: chosen under [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) and §6 | 7, 9 |
| P4b derived; P6 independent; P3 independent; instance: changing specification | By P4b a computed classification cannot be re-derived from memory, so it is recorded with its producer, inputs, unknowns and invalidators, and by P3 it is reused only after its applicability to the exact basis is checked. By P6 fact, judgment and ruling are distinct authorities, so they stay apart, and candidate behaviour cannot author its own target law. | [Computed classification and treatment](#computed-classification-and-treatment) | the C, J and O annotations, the order of the four steps and the material inputs of C named as instances of the reuse rule's: domain choices of this member; reuse and invalidation: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); continuity of recorded judgments and rulings: [TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) | 3, 9 |
| P5 derived; instance: changing specification | By P5 an unknown is not a value, so an unknown relation, delta or effect stays unknown: it withholds the reliance and promotion that depend on it, not unrelated authorised work, and an effect of uncertain completion is never treated as no effect. | [Computed classification and treatment](#computed-classification-and-treatment), its last paragraphs | none | 3, 9 |
| P6 independent; P4b derived; P5 derived; instance: changing specification | By P5 inconsistent surfaces cannot all be satisfied, so no gate closes while the affected surfaces are inconsistent. By P6 and P4b closure is decided only by recorded evidence for the declared obligations, so closure is their conjunction with valid evidence; an event, an aggregate or a status does not replace it, and implementation behaviour is evidence, not authority. | [Consistency gate](#consistency-gate) | none; the closure condition, which the gate applies to its change span: [TICKETS §7](TICKETS.md#condition-based-closure-and-reuse); reuse: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse) | 3, 9 |
| P2 independent; P0 recovered; instance: changing specification | By P2 proof serves the outcome, and by P0 an actor can carry only bounded deferred work, so proof cost may be deferred inside a batch only while the deferred cost stays local, visible, bounded and repayable. A sprint batches work and admits none, so it is not an authority layer, and a carrier is chosen for the lifetime the work needs. | [Sprint execution boundary](#sprint-execution-boundary); [Carriers](#carriers) | the sprint with its required statements and close triggers: a policy choice of this member, its mechanics at [TICKETS §3](TICKETS.md#3-sprint-rules); whether escrow suits a domain: the profile that adopts it | 1, 5 |
| P5 derived; P6 independent; P2 independent; instance: reserved decisions | By P5 an ambiguity left unrecorded would be read as resolved, so major ambiguity at a boundary is detected and recorded with its outcome, and no dependent claim rests on an ambiguity that is carried, escalated or blocked as if it were resolved. By P2 whether it blocks depends on the risk the outcome bears, so it is policy, and by P6 a hard stop holds whatever the policy. | [§5](#5-ambiguity-governance-and-lifecycle); [Spec-drivenness litmus](#spec-drivenness-litmus) item 12 | the risk appetite, which sets the threshold between probabilistic decision and human adjudication: the project's declared policy; the order of narrowing, the major and micro split and the two concept identities: domain choices of this member; the hard-stop classes: [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) | 6, 9 |
| P3 independent; P6 independent; instance: shared interfaces | By P3 each identity and state binds one authority, and by P6 two authorities on one acceptance path compete, so one authority governs each request, fact, identity, state and projection on an acceptance path. A migration therefore stays incomplete while old and new contracts both stay authoritative, a projection stays downstream of the authoritative carrier, and a promoted slice does not close its migration. | [Core interface migration](#core-interface-migration); [Constitutional migration options](#constitutional-migration-options); [What counts as a core interface](#what-counts-as-a-core-interface); [Required migration protocol](#required-migration-protocol); [Bridge prohibition](#bridge-prohibition); [Projection discipline](#projection-discipline); [Transformation wave](#transformation-wave) | the two strategies, the presumption for bounded evolution, and the old-path classes `remove`, `replace`, `re-authorize` and `temporary scaffolding`: policy and domain choices of this member; selecting fundamental re-adoption: the human authority owning the affected product boundary | 2, 4, 9 |
| P6 independent; P4a independent; P4b derived; instance: shared interfaces | By P4a producers and consumers compose only through a shared declared contract, so complete migration-closure proof is valid only once they share the new contract. By P6 and P4b a break is shown by evidence that persists, so each break shows that its severed seam is rejected, and a retained mechanism identifies its own supported obligation and owner. | [Inside-out first sequencing](#inside-out-first-sequencing); [Hard-break discipline](#hard-break-discipline); [Proof-last rule](#proof-last-rule); [Closure criterion](#closure-criterion) | the inside-out order, from the source carrier outward: a policy choice of this member | 4, 9 |
| P3 independent; P6 independent; instance: changing specification | By P6 inherited material has no authority in a new line unless that line adopts it, and by P3 adoption binds the new line's own surfaces, so in a fundamental migration nothing carries forward by default: inherited material has no authority in the new line until it is explicitly re-adopted and classified. | [Fundamental migration](#fundamental-migration) | the classes `carry_across`, `redundant` and `rewrite`: domain choices of this member | 1, 9 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §4, §5 and §7.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, re-entry at the owning layer and the change classes: [§3](#3-outcome-conservation), where a change to an outcome's meaning or scope re-enters at the product; [§8](#8-bounded-execution-in-this-method), whose re-entry conditions are the change classes; [§11](#11-build-tenant-binding), Application in this method, where a change to a binding enters through intake triage and takes its class; [Requirement categories and classification](#requirement-categories-and-classification), where the change classes are declared states that map to no core value; [TICKETS §4 Change class](TICKETS.md#change-class), [Upward propagation check](TICKETS.md#upward-propagation-check), [Triage metadata](TICKETS.md#triage-metadata) and [Status](TICKETS.md#status), which record the class, the re-entry point and the walk that finds them; [TICKETS §3 Sprint admission](TICKETS.md#sprint-admission), which batches away no intake triage, and [Close review](TICKETS.md#close-review), whose layer-naming classification carries the class at which the work re-enters; [TICKETS §7 Test case authority](TICKETS.md#test-case-authority), whose derivation chain starts at the ticket's intake triage and re-entry point; [ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation), Feedback and diagnosis, where a bug enters the same intake; [RELEASE §1](RELEASE.md#1-context-and-position), where release handling is downstream of intake triage, and [§3 Mutable candidate construction](RELEASE.md#mutable-candidate-construction), where bounded fixes follow it; [ASSURANCE §2](ASSURANCE.md#2-testing-strategy-taxonomy), where tests derive from the ticket's lawful re-entry point, [§12](ASSURANCE.md#12-counterexample-localisation), where a resulting change follows the re-entry relation, and [§14](ASSURANCE.md#14-design-to-module-evidence-route), where an unchanged `realization_refactor` cites the accepted relation; [DESIGN_MODULE §5 Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), [Native constructability](DESIGN_MODULE.md#native-constructability-up-002), [§10 Opportunistic optimisation](DESIGN_MODULE.md#opportunistic-optimisation) and [Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review), where a reframe or admitted follow-up enters at the smallest lawful re-entry point; [FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction) and [Parallel derivation and mutual assurance](FOUNDATIONS.md#parallel-derivation-and-mutual-assurance), where a change to the governing outcome or a proposed correction follows the change authority; [ODD §11.7A](ODD.md#117a-conforming-agentic-development), where an agentic coder works through intake triage and the smallest lawful re-entry, and the [ODD family table](ODD.md#foundation-to-law), whose rows for the selected outcome and for method governance import F11; the [UX family table](UX.md#foundation-to-law), whose row for product truth and admitted carriers imports F11 for the re-entry that authors a missing carrier; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-10, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 41.
- Row 2, the triangulation: no separate consumer applies. The frames that test a diagnosis are selected under REFERENCE_FRAME §5 and §6, as the choice column states; the four causes a diagnosis distinguishes are [ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation)'s, Feedback and diagnosis, which names this section as its consumer; and localisation of a counterexample is [ASSURANCE §12](ASSURANCE.md#12-counterexample-localisation)'s, which this section applies.
- Row 3, the computed classification and its reuse: [TICKETS §4 Upward propagation check](TICKETS.md#upward-propagation-check), where triage consumes the classification and a new role repeats no unchanged walk; [TICKETS §7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), whose C, J and O are this section's annotations; [EXECUTIVE_BASELINE §5 Work result](EXECUTIVE_BASELINE.md#work-result), which references the current classification through its carriers and reconstructs no unchanged C, J or O.
- Row 4, an unknown stays unknown: [TICKETS §4 Upward propagation check](TICKETS.md#upward-propagation-check), where missing or ambiguous evidence leaves the affected treatment unknown and proves no absence of the governing layer.
- Row 5, the consistency gate: [Specification surface rule](#specification-surface-rule), whose span check leaves the gate open while the affected surfaces disagree; otherwise no separate consumer applies: the closure condition the gate applies is [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse)'s, which names this gate as its consumer, and reuse of the gate's evidence is ACTIVATION §7's, as the choice column states.
- Row 6, the sprint boundary and carriers: [TICKETS §1 Sprints](TICKETS.md#sprints), where sprints operate under the boundary this section states, and [§3 Compliance escrow](TICKETS.md#compliance-escrow), where escrow satisfies no closure until paid down, accepted or repriced; [UX §12 UX sprint compliance escrow](UX.md#ux-sprint-compliance-escrow), the profile statement the boundary admits of when escrow suits UX, and the [UX family table](UX.md#foundation-to-law), whose row for scaffold, exemption and escrow imports F11; [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), which binds where each carrier kind lives and selects none.
- Row 7, ambiguity governance: [Reconstruction litmus](#reconstruction-litmus), whose sufficiency depends on this governance, and [Operational lifecycle sufficiency](#operational-lifecycle-sufficiency), which carries an unanswered phase as governed debt under it; [§11](#11-build-tenant-binding), rule 2, where this section's admission makes an operation human adjudication, and Application in this method, where a major ambiguity about stack or execution admissibility is recorded and governed here; [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), which takes the default ambiguity policy and its risk appetite from this section and owns the hard stops; [ODD §5 Probabilistic compute](ODD.md#probabilistic-compute) and [§11.5B](ODD.md#115b-execution-authority-audit), which bind the F_P and F_H roles to this section's candidate-producer and human-adjudication concepts through declared specialisations; [UX §1 Authority](UX.md#authority), where an ambiguous case fails closed under this section, and the [UX family table](UX.md#foundation-to-law), whose row for UX realisation authority imports F11 for the ambiguity outcomes.
- Row 8, core interface migration: [TICKETS §5 Evaluation criteria and non-closure conditions](TICKETS.md#evaluation-criteria-and-non-closure-conditions), where a deferral follows the path-relative authority and disposition rules of Constitutional migration options, [§6 Declaration and checklist](TICKETS.md#declaration-and-checklist), the local enforcement surface of the migration law, and [Closure of a migration ticket](TICKETS.md#closure-of-a-migration-ticket), where an accepted slice closes no migration; [Requirement categories and classification](#requirement-categories-and-classification), where the old-path classes are declared states; [DESIGN_MODULE §5 Native constructability](DESIGN_MODULE.md#native-constructability-up-002) and [§10 Proxy interface prohibition](DESIGN_MODULE.md#proxy-interface-prohibition), under the Bridge prohibition, [§5 Capability and foundation selection](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), which overrides no strategy presumption of Constitutional migration options, and [Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016), where a superseded responsibility stays subject to Core interface migration.
- Row 9, inside-out sequencing, hard breaks, proof last and the closure criterion: [TICKETS §4 Inside-out sequencing](TICKETS.md#inside-out-sequencing); [TICKETS §6 Break order and break-to-closure map](TICKETS.md#break-order-and-break-to-closure-map), under the Hard-break discipline, and [Declaration and checklist](TICKETS.md#declaration-and-checklist), the local enforcement surface of the inside-out law; [Live surface immutability](#live-surface-immutability), where a retained transitional responsibility satisfies the retention relation of the Closure criterion; [DESIGN_MODULE §10 Recurrence extraction](DESIGN_MODULE.md#recurrence-extraction), where a superseded responsibility is retired or satisfies that relation.
- Row 10, fundamental migration: [TICKETS §6 Strategy requirements](TICKETS.md#strategy-requirements), where inherited implementation is classified `carry_across`, `redundant` or `rewrite` and unclassified material blocks closure; [Requirement categories and classification](#requirement-categories-and-classification), where the inherited-material classes and the three implementation classifications are declared states; [DESIGN_MODULE §5 Capability and foundation selection](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), which does not choose between bounded evolution and fundamental re-adoption.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

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

### Computed classification and treatment

Intake supplies one reusable classification result rather than requiring
each role to reconstruct the same facts (P4b, P6, P1; rc.2
#computed-classification-and-treatment). Three annotations keep the kinds
of determination apart: C denotes reproducible facts and declared rule
application; J denotes residual semantic or materiality judgment; O denotes
a ruling reserved to its actual owner. The annotations grant no authority,
an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and introduce no calculus kind, runtime, classifier interface or mandatory
document.

The explicitly selected source, worksite or qualification capability
produces C over the exact request and desired outcome, the known targets
and effects, the operation grant and work lifetime, the product definition
and governing basis, the baseline and the available candidate, the declared
relations, the accepted design and trace bindings, the evidence and the
applicable rules. Its output identifies the producer and procedure
revision, the inputs, the result, the scope, the source routes, the
reproduction relation, the unknowns and the invalidators. A missing
candidate or missing evidence is an input state, not a claim that nothing
changed.

The computed result exposes four things, in this order:

1. Authority traversal. Follow the explicit source, ownership, dependency,
   composition and projection declarations from the affected targets and
   effects. Identify each reached layer and owner, its exact basis and its
   changed, unchanged or unknown relation, the traversed edges and the
   unresolved frontier. Include root, authority and grant changes even when
   public bytes are equal. An absent edge does not prove irrelevance;
   undeclared or semantically uncertain materiality remains J.
2. Public delta. Enumerate the complete relevant serialised member universe
   under its owning declaration and applicable projection, including helper
   and generated dependencies. Report added and removed identities and
   every retained member with changed typed value or bytes, with exact
   before and after values. A rename is removal plus addition unless its
   owner supplies an identity-preserving relation. A missing candidate,
   incomplete enumeration, ambiguous identity or unavailable projection
   leaves the affected delta unknown; membership equality alone proves no
   value equality (P3).
3. Accepted-design coverage. Join changed bytes and relations to explicit
   accepted scope, traces and acceptance evidence. Distinguish covered,
   missing, stale, ambiguous and outside-scope evidence. A filename, listed
   artifact or digest alone establishes no accepted coverage. Current trace
   coverage is a computed fact; residual semantic sufficiency remains J.
4. Rule-determined treatment. Apply only declared rules with sufficient
   input facts, recording their owners, matched predicates and
   consequences. Expose the smallest lawful re-entry, the next action, the
   applicable evidence or assessment, the reserved ruling and the carrier
   lifetime, with any conflict or missing premise still unresolved. A label
   or filename cannot select the route. When rules settle the question, no
   residual judgment is invented.

The values these steps assign, a relation changed, unchanged or unknown,
an identity added, removed or retained with a changed value, and evidence
covered, missing, stale, ambiguous or outside scope, are facts of the
computed result. They are not results of an evaluation and map to no core
value. An evaluation that consumes them returns its own core value with
its predicate under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and
an unknown it consumes stays unknown. Purpose and material relation: a
classification fact is never combined as an evaluation result, so
evidence classified covered, or a relation classified unchanged, cannot
stand in for a `satisfied` result (P5, P1).

A public delta or other nonconformance does not itself require changing
the governing contract. If that contract remains sufficient for the
authorised outcome, the candidate is rejected or locally repaired within
its grant. The actual governing owner is re-entered when the explicitly
selected desired outcome requires changed meaning or an applicable
assessment establishes governing insufficiency. C determines that
consequence only from sufficient declared premises; unresolved intended
meaning or necessity is J, and any reserved decision remains O. Candidate
behaviour cannot author its own target law (P6).

Unknown treatment withholds dependent reliance or promotion, not unrelated
authorised work. An existing bounded construction or evidence grant may
permit the cheapest useful discriminator, including obtaining the first
candidate, without asserting that the candidate is conformant; it carries
its own exact subject, territory, operations and stop conditions. The
affected C result is updated before dependent effects or promotion rely on
newly available evidence. A mistaken route is corrected at its smallest
affected owner, preserving the original cause, the attempted subject, the
observed effect state and valid progress. Retry requires the applicable
outcome, authority and safe-recovery conditions; an effect of uncertain
completion (`completion_unknown`, or `not_effected` with its end not
established, under [ACTIVATION §3 Effects](ACTIVATION.md#effects)) cannot
be silently treated
as no effect, and is reconciled as ACTIVATION §5 states before any retry
or dependent action (P5).

A new role, conversation or resumption reuses valid C after checking exact
applicability; reuse and invalidation are
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), which this
paragraph applies to C. The material inputs of C, whose change is that
rule's material input change and invalidates the affected claims of C
before reliance, are by name: the request, the candidate, an owner or
root relation, a projection, a design trace or acceptance, a rule
applied, the configuration and the material evidence. A changed basis
and a declared revising observation, that rule's other two
invalidators, invalidate likewise. Predecessor and
successor identities, changed inputs, surviving facts and affected J
dependencies are preserved; the wider frontier is recomputed where
independence is unproved (ACTIVATION §7).
[TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) owns
the existing carrier and the recorded J and O continuity rules (provenance
rc.2 TICKET_METHOD #recorded-judgment-and-owner-ruling-continuity).

### Consistency gate

No gate closes while the affected active surfaces are internally
inconsistent (P6, P4b; rc.2 #consistency-gate-rule). For the declared
change span the framework proves that the upstream surface remains
sufficient for the downstream surface, that downstream artifacts do not
contradict active upstream truth, and that tests and qualification prove
the active intended behaviour rather than stale precedent. If that proof is
missing the change remains open even if one local artifact already looks
correct.

The gate closes only under the closure condition that
[TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse)
owns, applied here with the obligations declared for the change span as
its required coverage. A material counterexample
to a mandatory constraint, a required judgment or ruling without a closed
result, or an obligation that no evidence addresses keeps the gate from
closing, and each stays recorded by kind (P5, P6). Reuse of the gate's
evidence and results is
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse); TICKETS §7
records the work state on its carrier. A
review event, a passing aggregate, a completed artifact or a status change
cannot substitute for that conjunction (EVALUATION §5).

When a code and test mismatch appears during ticketed work, implementation
behaviour is evidence but not authority. The mismatch is reconciled through
the admitted ticket, its intake triage, its lawful re-entry point and the
governing requirement, design, module, carrier or closure surface.
[TICKETS §7](TICKETS.md#test-case-authority) defines the ticket-local
test-case authority rule (ASSURANCE §3 states the test authority rule).

### Sprint execution boundary

A sprint is a bounded execution-control surface, not a new layer in the
constitutional chain (P6, P2; rc.2 #sprint-execution-boundary). It may
batch work, coordinate tickets or iteration entries, price proof cost and
force close review under existing goals, intent, product definition,
requirements and design authority; it does not create, supersede, weaken
or override that authority.

A lawful sprint states at least: the goal or work wave it serves; the
upstream authority surfaces it depends on; the scope it admits; the
product, requirement, design, runtime, data-contract or governance
boundaries it excludes; the change classes it expects to contain; the
local proof or compliance debt, if any, that may be deferred during the
sprint; the closure trigger and closure law; and the paydown or repricing
path for debt discovered at close.

Sprints exist because proof cost is not uniform. For some work, especially
projection-surface and user-interface iteration, proving every micro-change
before the next change can cost more than making the bounded change visible
and correcting it at close. That optimisation is lawful only when the
deferred cost remains local, visible, bounded and repayable. Deferred
compliance inside a sprint is escrow, not acceptance: it satisfies no
method, release or product closure until it is paid down, explicitly
accepted under the governing method, or repriced into the appropriate
upstream surface.

A sprint may be recommended for close when its timebox expires, its
intended scope has been reached, accumulated changed surface area makes
continued iteration more expensive than review, review uncertainty makes
more work unsafe without reconciliation, or discovered gaps suggest the
sprint boundary is no longer the right container. Sprint close is a
forensic reconciliation event, not automatic approval: close review
compares the accumulated work and evidence against the governing
authority, classifies each gap, accepts compliant work, opens paydown work
for local debt, and escalates any authority drift through the lawful
change class. If a sprint discovers a goal, intent, product, requirement,
design, runtime, data-contract, governance or other product-truth change,
the sprint manifest does not authorise landing it; the work is split,
escalated, repriced or carried as explicit paydown.
[TICKETS §3](TICKETS.md#3-sprint-rules) defines the sprint mechanics,
including compliance escrow, and §4 the ticket mechanics; a profile may
define when sprint compliance escrow is an appropriate cost optimisation
for its domain (PROFILES).

### Carriers

The carrier of a work item is selected for its required lifetime: a
durable ticket where the work needs identity across sessions; a
sprint-local entry where its only value is traceability inside a batch; a
run or return record where the work lives and dies with one activation.
The triage fields are required wherever substantive work begins; a ticket
per change is not (P2, P4b; [TICKETS §1](TICKETS.md#1-work-carriers) owns
the carrier model and
[TICKETS §5](TICKETS.md#carrier-selection) the selection of the smallest
lawful carrier; provenance rc.2 TICKET_METHOD
#core-model and #triage-metadata).

### Procedures

When any substantive intake arrives (P2, P4b; rc.2 #method): triage the
intake and classify the change; determine the lawful re-entry point into
the constitutional chain; identify the affected downstream span that must
remain consistent; only then treat the work as implementation, repricing or
release-bound change.

When a feature is introduced or changed: update goals if the current
bounded work wave or overriding concerns have changed; update intent if the
purpose or scope has changed; update product if the current product
realisation, terms, boundaries or end-state shape have changed; update
requirements so the invariant truths are explicit as a decomposition of the
product definition, including any lifecycle obligations or named lifecycle
ambiguity gaps, and classify each new or changed requirement by category;
establish or update design so it owns the governing structural HOW, where
under the design profile its decision-completeness rule applies (design,
implementation and tests may co-evolve only when its co-evolution predicate
holds, otherwise the smallest causally closed affected design set is
accepted before retained implementation establishes an unresolved,
contradictory or materially non-equivalent relation;
[DESIGN_MODULE](DESIGN_MODULE.md)), and
where that profile does not apply design, implementation and tests may
co-evolve when upstream truth leaves no unresolved material design
decision, and when such a decision remains the affected design is accepted
before retained implementation establishes it, ADRs being one valid design
form; write scenarios for capability claims that require operational proof
and define other evidence surfaces for non-capability requirements where
appropriate; prefer declarative expression of the problem and acceptance
surface before adding imperative mechanism; check the reconstruction
boundary, whether current goals support current intent, current intent the
current product, current product the intended requirements, current
requirements the intended design, and current design the intended
implementation; record any major ambiguity discovered at the active
boundary and govern it by declared risk appetite rather than silent
convenience; develop code under the selected design relation and reconcile
design, implementation and tests before promotion or closure; use events,
projection and delta to verify whether reality still satisfies the
requirements.

When bootstrapping a project or repricing a requirement surface: resolve
the applicable product definition, verify its exact installed basis, load
its declared bootstrap entrypoint (PRODUCT_DEFINITION §12), then load the
goals surface or the bound equivalent current work-wave carrier; perform
the goals-to-intent step and write or confirm the intent surface; perform
the intent-to-product step and write or confirm the product definition as
the current bridge; gather requirement source material from the relevant
constitutional inputs; perform the product-to-requirements step and write
the resulting live surface under the requirement surface; store
requirements as individual files or grouped families, whichever best
preserves clarity and avoids monolithic sprawl; make the requirement
surface the sole live requirement authority before proceeding to design and
code; prefer declarative structure over procedural workaround while shaping
the new surface; record any major ambiguity that remains at the current
boundary before downstream realisation proceeds; only after that surface
exists should downstream design and implementation be treated as
constitutionally grounded.

When a real use case reveals a gap: run intake triage first and classify
the report as a lawful change; then write the scenario as the first
substantive project artifact for the gap so the pressure becomes concrete
and testable; run gap analysis, asking whether this is a missing
implementation or a constitutional insufficiency; if constitutional,
reprice goals when the current work wave changes, write a new intent, then
flow forward through product, requirements, design and code; if
implementation, write requirements and design as needed, then implement.
The intake source does not change this rule: a bug report, feature request,
failed test case, release blocker or operator observation still enters
through intake triage first, then follows the lawful change class selected
there.
```


### Row `SPEC_METHOD.md#checkpoint-continuation-progress-and-churn` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#checkpoint-continuation-progress-and-churn` at rc.2:

```text
### Checkpoint, Continuation, Progress, And Churn

Acceptance binds one exact checkpoint. The next already-authorized bounded
action may begin without renewed human approval; acceptance does not widen the
Product outcome or affected relation set.

A preservation checkpoint may retain unfinished or unaccepted work under an
existing exact operation grant. Identify its parent or predecessor, included
territory, concurrent-writer disposition and durable evidence location. It is
neither acceptance, promotion nor publication. A proposed restart identifies
why repair of retained work is insufficient, which obligations and evidence
survive, and which causal assumptions change; reconstructability alone does
not select reconstruction.

Accepted material Product movement is progress. Prerequisite work names the
Product obligation it enables. Preservation and repeated proof are evidence,
not new progress. Rejected or superseded construction is churn. Discovery of
previously hidden distance revises the forecast but is not itself negative
implementation progress. Paperwork, code volume, test count, commit count, and
review count are not Product progress by themselves.

These are semantic categories, not a numeric progress algorithm. Consumers may
derive their own progress and churn projections from them.

This protocol is false if execution proceeds from unreconstructable context,
if a constructor's report substitutes for required independent live evidence,
if a bounded proxy changes a governing relation outside its delegation, if
unrelated incompleteness blocks a closed causal cone, if a same-process test is
used to prove materially cross-process authority, or if rejected activity is
reported as accepted Product progress.

---
```

Successor, `ACTIVATION.md#5-work-state-and-restart`:

```text
## 5. Work state and restart

Work state is the tuple of: the current persistent workspace; the governing
basis; the applicable closed results and judgments with their invalidators;
the residuals; and the known uncertainty over external effects. It is an
object (P3); its carrier (files, an event stream, another admitted owner) is
a profile or realisation choice. Resumption, checkpointing and the
progress account of this section are generic procedures
([SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)): they require
no particular carrier (P1, P6).

Resumption is re-entry of the same method over the current work state,
starting from the current material state, by a possibly different actor.
It recovers applicable progress, re-checks the invalidators of each reused
result (§7), reopens only affected support, and reconciles uncertain
external effects, sufficiently for the next dependent action, before any
repetition or dependent action. Resumption does not imply idempotence: an
action whose external effect may have occurred is not repeated blindly;
the lawful next moves are reconciliation, yield or stop.

Checkpoint. Acceptance binds one exact checkpoint. The next
already-authorised bounded action may begin without renewed human approval;
acceptance does not widen the selected outcome or the affected relation set
(P6, P2). A preservation checkpoint may retain unfinished or unaccepted
work under an existing exact operation grant; it identifies its parent or
predecessor, the included territory, the concurrent-writer disposition and
the durable evidence location, and it is neither acceptance, promotion nor
publication. A proposed restart, which reconstructs from less than the
retained work, identifies why repair of retained work is insufficient,
which obligations and evidence survive, and which causal assumptions
change; reconstructability alone does not select reconstruction. Conserves
[UP-020 checkpoint and continuation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#checkpoint-continuation-progress-and-churn);
the generic work-state object, the reconciliation of uncertain external
effects and the non-idempotence rule are new (P0, P5 with the open-world
premise).

Progress is accepted material movement toward the selected outcome;
prerequisite work names the obligation it enables; preservation and
repeated proof are evidence, not new progress; rejected or superseded
construction is churn; discovering previously hidden distance revises the
forecast and is not negative progress. Paperwork, code volume, test count,
commit count and review count are not progress by themselves. These are
semantic categories, not a numeric progress algorithm; a consumer may
derive its own progress and churn projections from them (P2). A member,
profile or project that distinguishes finer categories for its own
outcome states them as a refinement of these, naming this paragraph and
mapping each of its categories to one of progress, prerequisite work,
evidence that is not new progress, churn or forecast revision; a category
it cannot map is a change to this owner, not a parallel category (P2, P6).

The execution protocol of §1, §3 and this section is false if execution
proceeds from unreconstructable context; if a constructor's report
substitutes for required independent live evidence; if a bounded proxy
changes a governing relation outside its delegation; if unrelated
incompleteness blocks a closed causal cone; if a same-process test is used
to prove materially cross-process authority (§7); or if rejected activity
is reported as accepted progress.

Foundation to law. This family, work state, resumption and reuse, covers
this section and §7. Its instance premises are: (a) a workspace that
persists across activations; (b) work that spans activations; (c) actors
that may change between activations; (d) external effects in an open
world. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent), P0 (recovered); instance premises a, b | By P3 work state binds an exact basis, and by P0 an actor holds only part of it at a time, so work state is an object: the workspace, the governing basis, the applicable closed results and judgments, the residuals and the uncertainty over external effects | [§5](#5-work-state-and-restart), first paragraph | its carrier (files, an event stream, another admitted owner): the profile or realisation | 2, 5 |
| P0 (recovered), P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); instance premises a, c | By P0 an actor's context is bounded and disposable, by P3 the workspace binds the exact state, and by P4b recorded facts persist where the context does not, so the workspace is the truth surface and an actor's context a disposable account of it; current evidence corrects the account; discarding the account resets nothing | [The workspace and an actor's account](#the-workspace-and-an-actors-account) | the observations and reconciliations a resumption needs: the recovery contract, which is the resuming step's intake with the work state | 6, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise d | By P5 an effect of uncertain completion is undecided, and by P6 repeating an effect needs evidence that it is safe, so an effect of uncertain completion is reconciled before any repetition or dependent action; resumption does not imply idempotence | [§5](#5-work-state-and-restart) Resumption; [§3 Effects](#effects) | none | 4, 5 |
| P2 (independent), P6 (independent); instance premise b | By P2 progress is movement toward the selected outcome, and by P6 acceptance binds what was evaluated, so acceptance binds one exact checkpoint; a restart states why repair of retained work is insufficient; progress is accepted movement towards the selected outcome, not a count; finer progress categories refine these with a map | [§5](#5-work-state-and-restart) Checkpoint and Progress | progress and churn projections: their consumer | 5 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P0 (recovered), P6 (independent); instance premise c | By P4b and P0 private working context does not survive the actor, and by P6 a reused judgment is not a new independent one, so handoff is by closed results without private working context; reuse checks exact applicability and three invalidators, a material input change (newly acquired material evidence included), a changed basis and a declared revising observation, and a domain trigger is an instance of one of them; a reused judgment does not satisfy a required independent judgment | [§7](#7-closed-result-and-reuse) | the revising observation a result declares, and its other invalidation conditions: the producer of that result | 7, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise c | By P5 a transition's outcome is undecided without its evidence, and by P6 a proof establishes only the authority it was produced under, so a reviewable transition names its exact candidate, changes, proof and disposition; a same-process proof does not establish a reconstructable authority claim where the loss of process state is a counterexample | [Transition evidence](#transition-evidence) | the representation of transition evidence: its consumer | 9 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, work state as an object: [§1 Transitions](#transitions), where the current state is the work state this section records; [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed, and [Assertions and observation](FOUNDATIONS.md#assertions-and-observation), where unresolved work and an unexercised capability are a state of the work, carried as a residual and not a result; [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where a step's work state carries an unrun verification as a residual; [REFERENCE_FRAME §10 Revision actions](REFERENCE_FRAME.md#revision-actions), where results reopened without a material revision are recorded in the work state; [UX §8 Msg-replay proof](UX.md#msg-replay-proof), whose Msg log is the surface's recorded work state, and the [UX family table](UX.md#foundation-to-law), whose row for continuation and replay imports F4; the [ODD family table](ODD.md#foundation-to-law), whose rows for the immutable ledger and for yield import F4 for a replay-visible work state.
- Row 2, the workspace and an actor's account: [§1 Transitions](#transitions), where an actor's context is an account of the current state and not the state itself; [EXECUTIVE_BASELINE §20](EXECUTIVE_BASELINE.md#20-failure-classification), where a compression, summary or prior result that replaces current source authority is evidence substitution and a retained account never overrules current evidence; [UX §8 Msg-replay proof](UX.md#msg-replay-proof), where replay is resumption from the recorded work state; [CONFORMANCE §4](CONFORMANCE.md#4-cases-from-the-common-discriminators), case CD-03, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 38 and 39.
- Row 3, resumption and effects of uncertain completion: [§1 Construction relation](#construction-relation), Control, where resumption reacquires current reality and unknown effects are resolved before the next dependent action; [EXECUTIVE_BASELINE §12 step 4](EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result), [§7 The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration), failure assumptions, and [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), whose work result names each intended effect with its value, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the effect field imports F4 for the reconciliation; [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update), where an update of uncertain completion is reconciled from the presented preimages before any repetition; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), where a retry waits on that reconciliation; [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds) and [Mutable-subject effect relation](TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation), where an effect whose end is not established is reconciled before any repetition; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where recovery reacquires current reality and need not erase valid work; [CONFORMANCE §4](CONFORMANCE.md#4-cases-from-the-common-discriminators), case CD-03, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 38 and 39.
- Row 4, checkpoint and progress: [SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation), whose four kinds of evidence refine the progress categories for a product outcome, and [§8](SPEC_METHOD.md#8-bounded-execution-in-this-method), where construction ends at the exact accepted checkpoint and the next already-authorised bounded action; [EXECUTIVE_BASELINE §14](EXECUTIVE_BASELINE.md#14-coverage-application), where checkpoint and continuation are the Executive's under existing authority; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-03, where a restart proposal states why repair of retained work is insufficient.
- Row 5, closed result and reuse: [§6](#6-cost-and-proportionality), the method's own execution, where reuse stays subject to exact applicability and invalidation; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), [§8 Coverage basis](REFERENCE_FRAME.md#coverage-basis) and [§10 Revision actions](REFERENCE_FRAME.md#revision-actions), where whether a closed result or a coverage result stays valid is decided by the reuse rule; [EVALUATION §2](EVALUATION.md#2-separation), [§3](EVALUATION.md#3-independent-assessment), where shared mechanical evidence may be reused and judgment may not, and [§6](EVALUATION.md#6-conformance-of-realisations), where an accepted relation is reused after checking applicability and invalidation; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), which applies the rule to computed classification, and [Consistency gate](SPEC_METHOD.md#consistency-gate); [TICKETS §7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) and [Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse); [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability), [§5 Work result](EXECUTIVE_BASELINE.md#work-result), [§6 Attention cycle](EXECUTIVE_BASELINE.md#attention-cycle) and [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), specialist result, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Product chain imports F4 for the repair that invalidates affected results; [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design), [Capability and foundation selection (UP-023)](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), [§7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work) and [§10 Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review), and the [DESIGN_MODULE family table](DESIGN_MODULE.md#foundation-to-law), whose row for that review imports F4; [ASSURANCE §7 The set](ASSURANCE.md#the-set), whose invalidation rows name instances of this rule's invalidators, and [§13 Obligations](ASSURANCE.md#obligations), item 4; [WORLD_MODEL §2 Builder Project specialisation](WORLD_MODEL.md#builder-project-specialisation), whose invalidation conditions are instances of them; [CONFORMANCE §1](CONFORMANCE.md#1-counterexamples-from-the-builders-own-history), case C-04, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 21 and 36.
- Row 6, transition evidence: [TICKETS §7 Execution and verification authority separation (UP-007)](TICKETS.md#execution-and-verification-authority-separation-up-007), where the reviewable transition is carried by an existing surface and no new ceremony is required; [EXECUTIVE_BASELINE §5 Exact candidate](EXECUTIVE_BASELINE.md#exact-candidate), [§8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), for the proof cadence, [§9](EXECUTIVE_BASELINE.md#9-derived-worker-frame), where `candidate_ready` binds the exact candidate and the transition evidence, [§12 step 5B](EXECUTIVE_BASELINE.md#5b-candidate-requires-independent-review), [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), work result, and [§14](EXECUTIVE_BASELINE.md#14-coverage-application), where candidate and transition evidence are the Worker's.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### The workspace and an actor's account

The workspace and its authoritative inputs persist across activations and
are the continuing truth surface of the work: the surface whose current
material state decides what the work has and has not done. An actor's
context is an account of that state. It is bounded, because it is a
projection of the state (§2); revisable, because an observation can
correct it; and disposable, because a step records its closed results and
step-produced facts before it returns (§1 Admission; P4b). An account is
never a second truth surface, and no later activation needs a prior
actor's context: its intake reconstructs the governing relations without
it (§1 Intake) (P0, P3, P6).

Acquisition ([§2](#2-context-construction-under-an-envelope)) observes the
current subject and its authoritative inputs. Where they materially
disagree with a cached belief, a retained summary or a prior result, the
actor reconciles the disagreement: current evidence corrects the account,
and what the evidence cannot decide stays an explicit unknown. A stored
belief, a summary or a successful prior result never overrules contrary
current evidence. A prior result is relied on only after its
applicability and invalidators are checked against the current subject
and inputs (§7). The actor corrects its account within its grant; where
resolving the disagreement needs an operation, a territory or a decision
outside the grant, the step stops with `re_entry_requested(authority)`,
naming the owner of what it needs (§3 Construction availability) (P5,
P6).

Discarding an actor's private context resets nothing: the workspace, the
applicable valid work and the outstanding obligations remain as the work
state records them. A missing trace in a context, a memory or a summary is
no evidence about the subject. It shows neither that work was not done
nor that an external effect did not occur, nor that it ended; an effect
of uncertain completion keeps the value `completion_unknown`, or its end
stays not established beside its `not_effected` value, until evidence
about the subject decides it (§3 Effects) (P5).

Work that an interruption left partly written is part of the current
material state from which resumption (above) starts, and is assessed as
it stands; an assessment that was not performed has no result and is
never recorded as performed
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); §3 Construction
availability). The method imposes no universal reset and no obligation to
replay the complete history. The recovery contract that applies, which is
the resuming step's intake with the work state, determines which
observations and which effect reconciliations the next dependent action
needs. Handoff between actors is by closed results, which carry no private
working context and keep their validity and independence conditions (§7)
(P0, P4b).

Purpose and material relation: finite context (P0) means an actor's
context ends or is replaced while the work continues, and discarding it is
safe only because the step-produced facts the outer contract needs are
recorded (P4b). Treating the account as the truth surface would let a
stale account overrule the workspace; treating a discarded account as a
reset would erase progress or repeat an effect that occurred (P5, P6). The
material relation is whether a decision relies on an account that current
evidence contradicts, or reads a missing record as undone work or an
absent effect. This subsection is new in this corpus. The workspace, the
work state and the closed results carry it, and no further carrier is
required.
```


### Row `SPEC_METHOD.md#collective-reference-frame-basis` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#collective-reference-frame-basis` at rc.2:

```text
### Collective Reference-Frame Basis

A **Project Reference-Frame Basis** is the Product-owned accepted declaration
of the shared frame set through which finite actors collectively engage one
governed Product scope or outcome. It binds:

```text
Project Reference-Frame Basis
  = exact Reference Frame Method and optional profile basis
  + admitting authorities and governed scopes
  + frame declarations and evaluation inventory
  + actor-binding rules and capability envelopes
  + semantic, evaluation, operation, and decision grants
  + result, conjunction, translation, and coverage relations
  + lifecycle activation triggers and invalidation law
```

`REFERENCE_FRAME_METHOD.md` supplies frame principles only.
`STDO_REFERENCE_FRAME_BASELINE.md` supplies one optional profile only. Neither
surface selects, adopts, or owns a Product binding. The adopting Product's
existing authority owns the concrete declaration and every grant it contains.

`reference_frame_bases` is the non-empty locator set for the accepted frame
bases through which finite actors collectively engage the governed Product and
its work. Each entry names:

- the URI carrying one accepted frame-basis declaration;
- every existing Goals, Product, requirement, accepted-design, or other lawful
  authority that admits the declaration; and
- the exact Product, bounded context, build tenant, outcome, or other governed
  scope to which it applies.

The referenced declaration owns the selected frame set, method or profile
basis, governed outcome, actor-binding rules, capability envelopes, grant
requirements, triggers, coverage, result relations, and invalidation law. It
may adopt an available profile or define a project configuration. The JSON
entry locates that declaration and its authority relation; it does not contain
the binding, adopt the profile, restate the frames, or create frame-set
authority.

Profile availability, Product adoption, and execution-scoped activation are
three distinct relations. Inclusion in a selected method cut makes a profile
available. Only Product authority may adopt it. Only an exact authorized work
instruction may activate one bound frame for an actor and subject.

The collective basis and an actor activation are distinct. An **Agent Frame Activation**
is the execution-scoped binding of one agent to an applicable
frame declaration or active configuration, exact evaluation, subject, basis,
evidence boundary, and capability envelope. The Product definition records the
durable shared basis. A ticket or other authorized work instruction carries the
activation packet. That execution binding does not mutate the Product Definition
Overlay. The overlay does not register agents, assign permanent frames, or
persist temporary active frame configurations.

Frames and actors remain separate identities. Several agents may activate
overlapping subsets of one frame set; one agent may activate different frames
over time. Neither an actor name nor a broad frame grants semantic, operation,
review, acceptance, or disposition authority beyond the cited owners and the
exact activation.

The Project Reference-Frame Basis also records the Product-role map when the
governed outcome crosses a chain of Products. The map keeps mutable Source
Projects, Product Definitions, candidate checkpoints, Release Cuts, released
Products, Installs, Artifacts, and dependent Products as distinct identities,
and records each Development Product as a role binding over its exact
underlying Install identity. Every directed Product-composition edge names its
source and target roles, governing authority and contracts, lifecycle,
evidence boundary, refusal, and invalidation conditions. Common actors,
repositories, files, implementations, outputs, or tool access create no
composition or identity relation.

An accepted Project Reference-Frame Basis may be expressed entirely as
source-linked prose. The starter at
`templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` projects this binding
law into one copyable shape. The template is not authority and no schema,
axiomatic representation, prompt framework, or runtime frame engine is needed
to use the method. An adopting Product replaces every placeholder with its own
exact identities, owners, scopes, sources, grants, results, and invalidation
conditions, then admits that completed declaration under existing authority.

A Product, domain, or runtime carrier also named `Frame` is not included by
nominal match. It remains governed by its bound `WHAT` and `HOW` and may be the
subject or coordinate of an evaluation frame. It enters the collective frame
set only through an explicit frame declaration with the required evaluation
and authority relations.
```

Successor, `PRODUCT_DEFINITION.md#7-collective-reference-frame-basis`:

```text
## 7. Collective reference-frame basis

A Project Reference-Frame Basis is the Product-owned accepted declaration
of the shared frame set through which finite actors collectively engage one
governed Product scope or outcome (P0, P6; rc.2
#collective-reference-frame-basis). It binds:

```text
Project Reference-Frame Basis
  = exact reference-frame law and optional profile basis
  + admitting authorities and governed scopes
  + frame declarations and evaluation inventory
  + actor-binding rules and capability envelopes
  + semantic, evaluation, operation and decision grants
  + result, conjunction, translation and coverage relations
  + lifecycle activation triggers and invalidation law
```

[REFERENCE_FRAME](REFERENCE_FRAME.md) supplies frame principles only, and
its §4 the shape of a frame-set declaration; a profile member (the
Executive baseline, tier 3) supplies one optional profile only. Neither
selects, adopts or owns a Product binding. The adopting Product's existing
authority owns the concrete declaration and every grant it contains (P6).

`reference_frame_bases` is the non-empty locator set for the accepted
frame bases through which finite actors collectively engage the governed
Product and its work. Each entry names (P6, P3):

- the URI carrying one accepted frame-basis declaration;
- every existing Goals, Product, requirement, accepted-design or other
  lawful authority that admits the declaration; and
- the exact Product, bounded context, build tenant, outcome or other
  governed scope to which it applies.

The referenced declaration owns the selected frame set, the method or
profile basis, the governed outcome, the actor-binding rules, the
capability envelopes, the grant requirements, the triggers, the coverage,
the result relations and the invalidation law. It may adopt an available
profile or define a project configuration. The JSON entry locates that
declaration and its authority relation; it does not contain the binding,
adopt the profile, restate the frames or create frame-set authority (P6).

Profile availability, Product adoption and execution-scoped activation are
three distinct relations. Inclusion in a selected method cut makes a
profile available; only Product authority may adopt it; only an exact
authorised work instruction may activate one bound frame for an actor and
subject (P6, P3).

The collective basis and an actor activation are distinct. An Agent Frame
Activation is the execution-scoped binding of one agent to an applicable
frame declaration or active configuration, an exact evaluation, subject,
basis, evidence boundary and capability envelope; what the agent receives
is the activation packet of REFERENCE_FRAME §11, and the step it performs
is ACTIVATION §1. The Product Definition records the durable shared basis;
a ticket or other authorised work instruction carries the activation
packet. An Agent Frame Activation does not mutate the overlay, and the overlay
registers no agents, assigns no permanent frames and persists no temporary
active frame configuration (P3, P0).

Frames and actors keep separate identities. Several agents may activate
overlapping subsets of one frame set; one agent may activate different
frames over time. Neither an actor name nor a broad frame grants semantic,
operation, review, acceptance or disposition authority beyond the cited
owners and the exact activation (P6, P3).

The Project Reference-Frame Basis also records the Product-role map when
the governed outcome crosses a chain of Products. The map keeps mutable
source projects, Product Definitions, candidate checkpoints, release cuts,
released Products, installs, artifacts and dependent Products as distinct
identities (SPEC_METHOD §6), and records each development product as a
role binding over its exact underlying install identity. Every directed
Product-composition edge names its source and target roles, governing
authority and contracts, lifecycle, evidence boundary, refusal and
invalidation conditions. Common actors, repositories, files,
implementations, outputs or tool access create no composition or identity
relation (P3, P6).

An accepted Project Reference-Frame Basis may be expressed entirely as
source-linked prose. The starter at
`templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` projects this binding
law into one copyable shape. The template is not authority, and no schema,
axiomatic representation, prompt framework or runtime frame engine is
needed to use the method. An adopting Product replaces every placeholder
with its own exact identities, owners, scopes, sources, grants, results and
invalidation conditions, then admits that completed declaration under
existing authority (P2, P6).

A Product, domain or runtime carrier also named `Frame` is not included by
nominal match. It stays governed by its bound WHAT and HOW and may be the
subject or a coordinate of an evaluation frame. It enters the collective
frame set only through an explicit frame declaration with the required
evaluation and authority relations (P1, P3).
```


### Row `SPEC_METHOD.md#constitutional-migration-options` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#constitutional-migration-options` at rc.2:

```text
### Constitutional Migration Options

Core interface and major implementation replacement work has two lawful
constitutional strategies:

- **Inside-Out Hard-Break Migration**: use this when the project remains on the
  same implementation line and the authoritative source truth is being replaced
  in place. The work proceeds from source carrier outward through a sequence of
  deliberate breaks and repairs.
- **Fundamental Re-Adoption Migration**: use this when the rewrite is major and
  the project is intentionally re-deriving itself on a materially different
  implementation basis, such as a new runtime model, carrier model, type
  system, execution substrate, or realization tree. The prior implementation is
  moved sideways and treated as reference material, not live authority.

Where bounded evolution and fundamental re-adoption are both lawful and
feasible, and a working predecessor can reach the admitted Product outcome
without retaining competing or ambiguous authority, evolution on the supported
Product path is the rebuttable selection presumption. This does not require
continuing an unsafe or constitutionally inadmissible predecessor path. It
conserves accepted predecessor semantics and Product feedback; it does not
require preserving an internal implementation or public mechanism that Product
authority explicitly supersedes.

When bounded evolution includes a core-interface migration, it uses the
Inside-Out Hard-Break strategy. Bounded evolution is a strategy-selection
presumption, not a third migration strategy.

Fundamental re-adoption requires explicit selection by the human authority
owning the affected Product boundary. The selection compares re-adoption with
bounded evolution across Product value, feedback latency, authority risk,
reversibility, total cost, and retained predecessor semantics. It also states a
bounded abort or re-entry condition. Implementation scale or architectural
preference alone does not select re-adoption.

Both strategies share these non-negotiable rules:

- no proxy interface partial implementation may stand in for the new contract in
  any acceptance path
- no bridge or fallback path may remain silently authoritative
- promotion of an affected Product outcome requires one unambiguous
  authoritative path for that outcome
- competing or ambiguous executable authority on the promoted acceptance path
  blocks that outcome
- residual material from the superseded interface family outside the promoted
  path may be deferred only when it is explicitly non-authoritative for the
  promoted outcome or governs an explicitly specified, disjoint Product or
  compatibility scope with deterministic routing, cannot falsify current or
  retained Product claims, and retains a bounded migration, qualification, or
  release disposition
- tests are leak detectors and proof surfaces, not the migration plan

For this rule, the affected acceptance path is the full causal closure of the
outcome: every admitted entrypoint, producer, consumer, resolver, fallback,
shared state surface, event, projection, and proof surface capable of changing,
interpreting, or closing the outcome. Singular authority means one governing
authority across that closure, not one selected successful trace. If the same
request, fact, identity, state, or projection is admissible to old and new
authority, authority is competing and promotion blocks.

Product-slice promotion and complete migration closure are distinct claims. An
intermediate Product outcome may be promoted while its enclosing migration
remains open only when the outcome's acceptance path has singular authority and
the residual implementation satisfies the deferment rule above. That promotion
does not close the migration or waive its final retirement criteria. The
slice's identity and acceptance criteria derive from Product plus every causally
applicable live requirement, accepted design relation, and retained predecessor
claim. Ticket or review wording cannot narrow that authority away.

Active migration status does not renew an accepted slice's exhausted growth
authority. Work that only discharges already admitted removal, demotion, and
migration-closure proof obligations may continue within that existing bound
without claiming further Product progress. Further material producer or
consumer growth requires another still-live basis admitted under
`STDO-UP-013`; ticket activity alone is not that basis.
```

Successor, `SPEC_METHOD.md#constitutional-migration-options`:

```text
### Constitutional migration options

Core interface and major implementation replacement work has two lawful
constitutional strategies (P3, P6; rc.2 #constitutional-migration-options).
Inside-out hard-break migration applies when the project remains on the
same implementation line and the authoritative source truth is being
replaced in place; the work proceeds from the source carrier outward
through a sequence of deliberate breaks and repairs. Fundamental
re-adoption migration applies when the rewrite is major and the project is
intentionally re-deriving itself on a materially different implementation
basis, such as a new runtime model, carrier model, type system, execution
substrate or realisation tree; the prior implementation is moved sideways
and treated as reference material, not live authority.

Where bounded evolution and fundamental re-adoption are both lawful and
feasible, and a working predecessor can reach the admitted product outcome
without retaining competing or ambiguous authority, evolution on the
supported product path is the rebuttable selection presumption. This does
not require continuing an unsafe or constitutionally inadmissible
predecessor path; it conserves accepted predecessor semantics and product
feedback, and it does not require preserving an internal implementation or
public mechanism that product authority explicitly supersedes. When bounded
evolution includes a core-interface migration, it uses the inside-out
hard-break strategy; bounded evolution is a strategy-selection presumption,
not a third strategy.

Fundamental re-adoption requires explicit selection by the human authority
owning the affected product boundary. The selection compares re-adoption
with bounded evolution across product value, feedback latency, authority
risk, reversibility, total cost and retained predecessor semantics, and
states a bounded abort or re-entry condition. Implementation scale or
architectural preference alone does not select re-adoption (P6, P2).

Both strategies share these non-negotiable rules: no proxy interface
partial implementation stands in for the new contract in any acceptance
path; no bridge or fallback path remains silently authoritative; promotion
of an affected product outcome requires one unambiguous authoritative path
for that outcome; competing or ambiguous executable authority on the
promoted acceptance path blocks that outcome; residual material from the
superseded interface family outside the promoted path may be deferred only
when it is explicitly non-authoritative for the promoted outcome or governs
an explicitly specified, disjoint product or compatibility scope with
deterministic routing, cannot falsify current or retained product claims,
and retains a bounded migration, qualification or release disposition;
tests are leak detectors and proof surfaces, not the migration plan.

For this rule the affected acceptance path is the full causal closure of
the outcome: every admitted entrypoint, producer, consumer, resolver,
fallback, shared state surface, event, projection and proof surface capable
of changing, interpreting or closing the outcome. Singular authority means
one governing authority across that closure, not one selected successful
trace. If the same request, fact, identity, state or projection is
admissible to old and new authority, authority is competing and promotion
blocks (P3).

Product-slice promotion and complete migration closure are distinct claims.
An intermediate product outcome may be promoted while its enclosing
migration remains open only when the outcome's acceptance path has singular
authority and the residual implementation satisfies the deferment rule
above. That promotion neither closes the migration nor waives its final
retirement criteria. The slice's identity and acceptance criteria derive
from the product plus every causally applicable live requirement, accepted
design relation and retained predecessor claim; ticket or review wording
cannot narrow that authority away. Active migration status does not renew
an accepted slice's exhausted growth authority: work that only discharges
already admitted removal, demotion and migration-closure proof obligations
may continue within that existing bound without claiming further product
progress; further material producer or consumer growth requires another
still-live basis admitted under §3, and ticket activity alone is not that
basis.
```


### Row `SPEC_METHOD.md#construction-assessment-and-delegation` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#construction-assessment-and-delegation` at rc.2:

```text
### Construction, Assessment, And Delegation

The constructor owns bounded implementation and self-review. Where independent
assessment supports promotion, the assessor evaluates the exact live code,
authority paths, proof, and installed subject rather than treating the
constructor's summary as sufficient evidence. This preserves the independent-
review relation; it does not prescribe an actor count. One actor may occupy
different roles across different claims when independence for the assessed
claim is preserved.

The governing authority relation declares whether a bounded proxy may accept
and advance routine actions. A proxy may accept preservation, require local
repair, reject a violating candidate, and advance to the next already-
authorized action. It cannot change Product meaning, requirements, governing
authority, or accepted design. Such a change re-enters at its owning relation.

Human ceremony is not required at every transition when the governing basis,
affected cone, decision envelope, and re-entry conditions are already
accepted. This delegation does not weaken direct-human acceptance where
Product or release law requires it.

When one capable context has sufficient existing work authority, exact intake
and operation grant, it may enter directly as constructor or Writer. No
Executive activation is required solely to appoint that Writer. The applicable
frame configuration selects coordination when material contexts, authority,
capability or required independence need it; a role or frame name alone does
not create that need. Direct entry preserves execution-contract admission,
the smallest lawful carrier, required assessment and reserved decisions. It
permits bounded work and condition-based result recording, not self-acceptance
at a boundary owned elsewhere.

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Record actual role transitions in the existing work
carrier; a status change alone requires neither a new grant nor rehashing an
unchanged subject. A material change to the operation, subject, territory,
authority or validity conditions still requires the affected binding to be
resolved before effect. Executive mutation restrictions remain applicable.
```

Successor, `ACTIVATION.md#roles-and-delegation`:

```text
### Roles and delegation

Roles are relations over steps that a configuration allocates
(Configuration above), not kinds of actor and not a fixed inventory.
Where a configuration's operations include construction, assessment or
disposition, this member names the responsibility for each: a
constructor owns the bounded implementation and its self-review; an
assessor evaluates a frozen candidate independently; a decision owner
disposes. A configuration may allocate other responsibilities. Where
independent assessment supports promotion, the assessor evaluates the
exact live subject, its authority paths, proof and installed state, not
the constructor's summary (EVALUATION §3). This preserves the
independent-review relation and prescribes no actor count: one actor may
occupy different roles across different claims when independence for the
assessed claim is preserved; no role name confers an operation
([RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality);
P6; provenance rc.2 SPEC_METHOD #construction-assessment-and-delegation).

The governing authority relation declares whether a bounded proxy may
accept and advance routine actions. Inside a step, a proxy so declared may
accept preservation, require local repair, reject a violating candidate
and advance to the next already-authorised action; what it cannot change,
and the re-entry such a change requires, is the proxy limit of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), which
this paragraph applies and does not restate. Human ceremony is not
required at every transition when the governing basis, the affected cone,
the decision envelope and the re-entry conditions are already accepted;
this delegation does not weaken direct human acceptance where the
governing product or release law requires it (P6).

When one capable context has sufficient existing work authority, exact
intake and operation grant, it may enter directly as constructor. No
coordinating activation is required solely to appoint that constructor.
The applicable configuration (Configuration above) selects
coordination when material contexts, authority, capability or required
independence need it; a role or frame name alone does not create that
need. Direct entry preserves
execution-contract admission (Admission above), the smallest lawful
carrier, the required assessment and the reserved decisions; it permits
bounded work and condition-based result recording, not self-acceptance at a
boundary owned elsewhere (P0, P6).

Recording a result without review. Where the applicable law requires no
independent assessment and reserves no acceptance, the constructor that
holds the grant may record the satisfied bounded result, with the conditions
it found satisfied and their evidence, in the existing durable result
surface (Admission above), without adding a carrier, coordinating
appointment, review or recreated design view solely to mark completion. The
recording waives no condition that actually applies, states only
conditions that were evaluated, as an actor cannot report an evaluation it
did not perform
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed), and is
no disposition at a boundary owned elsewhere
(§3 Disposition). Where an assessment or a reserved acceptance does apply,
it stays required, and an insufficiency found during the work withholds
the dependent effect and returns the question to its owner. Carriers and
profiles refer to this paragraph and add only their own carrier binding
(P0, P2, P6; provenance rc.2 SPEC_METHOD
#construction-assessment-and-delegation). Purpose and material relation:
requiring a review or a ceremony that no law requires adds reasoning cost
without removing ambiguity (§6), while recording a satisfied result where
a review or acceptance is required would read construction as acceptance.

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Actual role transitions are recorded in the existing
work carrier; a status change alone requires neither a new grant nor
rehashing an unchanged subject. A material change to the operation, the
subject, the territory, the authority or the validity conditions requires
the affected binding to be resolved before effect. Where the selected
configuration restricts its coordinating role from mutation, as the
executive configuration (Configuration above) restricts its Executive,
the restriction that the coordinating role mutates nothing remains
applicable; an operation grant covering the sequence does not lift it
(P6, P3).
```

Successor, `FOUNDATIONS.md#authority-kinds`:

```text
### Authority kinds

Authority takes these kinds (P6): frame-set authority, the human authority
that declares or accepts a project frame set; semantic authority, the
owner of meaning for a material relation; evaluation authority, the role
permitted to perform an evaluation; operation authority, the owner-issued
grant to construct, transform, admit, publish or mutate a material subject
where an evaluation performs such an operation; decision authority, the
role permitted to accept, reject or otherwise dispose a result; and actor
identity, the human, agent, tool or process performing the work, which is
an identity and not an authority. These may coincide in a lawful case and
never collapse by default. A read-only evaluation declares no operation
authority; an effectful evaluation inherits the exact operation grant from
its existing owner, and the frame does not create that grant (P6, P3).

What creates no authority. Authority of any kind exists only by an
admitted grant or an explicit authority decision of its owner, with an
identifiable basis. None of the following mints, widens, transfers or
reconstructs semantic, evaluation, operation or decision authority (P6,
P3):

- actor identity, an actor's capability, its tools or its access;
- a name, label, display label, status label, role name, capability
  string, locator, file name or path;
- declaring, naming, selecting, activating or executing a frame, or
  occupying a role;
- implementation reachability, a reachable code path or an available
  operation;
- the shape of evidence or of a payload, or the availability of evidence
  inside a frame;
- a passing check, a successful step, a completed review or a count of
  any of them;
- copying, interpreting, encoding, evaluating, transporting, projecting,
  compressing, importing or acquiring material;
- drafting, admitting or retaining a work contract, beyond what its owner
  has admitted;
- composition, delegation, adapters, wrappers and registries, which may
  restrict admitted authority or carry it faithfully, and never widen its
  scope, add a role, increase its cardinality or change its kind.

Elevation, transfer, split, merge, proxy grant, revocation and retirement
each need an explicit authority decision with an identifiable basis. A
member that names an instance of this list for its own domain cites this
paragraph and adds only the instance.

Proxy limit. Human authority may act directly, or through an explicitly
admitted bounded proxy where the governing identity and authority law
permits it; proxy identity and human-authority identity stay distinct
(P6, P3). A proxy acts only inside its existing grant. It cannot change
the governing outcome's meaning, the requirements, the governing authority
or the accepted design; such a change re-enters at its owning relation.
Proxy authority does not make a constructor's self-review independent,
confers no unrelated runtime or domain authority, and does not replace
direct human acceptance where the governing product or release law
requires it. The contents of a proxy grant are
[IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and the decisions a proxy may take inside a step are
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)'s.

Purpose and material relation of the list and the proxy limit: each
member that names what cannot create authority decides the same question,
so one list keeps the answer the same in every member, and a capability,
a label or a passing check can never be read as a permission (P6).
```


### Row `SPEC_METHOD.md#design-rule` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#design-rule` at rc.2:

```text
## Design Rule

Requirements state what control or delivery surfaces must exist.

Design decides the concrete mechanism that realizes them.

If a technology stack, carrier, or runtime is not already constrained by an
upstream constitutional surface, choosing it is part of design rather than a
separate upstream authority.

That boundary matters especially for agent-facing bootstrap and control surfaces:

- requirements may say that authoritative bootstrap or control surfaces must be present, carry bare axioms, and route to the canonical method
- design decides whether those surfaces are entry documents, embedded blocks, standalone compiled artifacts, or another lawful topology

If filenames and placement are hardcoded in requirements without constitutional necessity, the requirement surface has absorbed design detail and made re-derivation harder.

---
```

Successor, `SPEC_METHOD.md#design-rule`:

```text
### Design rule

Requirements state what control or delivery surfaces must exist; design
decides the concrete mechanism that realises them. If a technology stack,
carrier or runtime is not already constrained by an upstream constitutional
surface, choosing it is part of design, not a separate upstream authority
(P2, P1; rc.2 #design-rule). A tenant's choice of stack, human process or
combination is its execution binding, declared in that design under §11.
The boundary matters especially for
agent-facing bootstrap and control surfaces: requirements may say that
authoritative bootstrap or control surfaces must be present, carry bare
axioms and route to the canonical method; design decides whether those
surfaces are entry documents, embedded blocks, standalone compiled
artifacts or another lawful topology (PRODUCT_DEFINITION §12). If
filenames and placement are hardcoded in requirements without
constitutional necessity, the requirement surface has absorbed design
detail and made re-derivation harder.
```


### Row `SPEC_METHOD.md#drift-signals` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#drift-signals` at rc.2:

```text
### Drift Signals

- Unowned requirements, ungrounded design records, deferred requirements
  without explicit deferment, and code without trace authority are design
  drift.
- If an ADR or other design artifact has no requirement grounding, it is design
  without constitutional authority.
- If code behavior has no design owner, the design has already drifted.
- If shipping code or tests cannot trace back out to live requirement and
  design authority, they are ungoverned product surface.
- If tests validate implementation habit rather than requirement truth, they
  lock in drift.
- If events and projection reveal persistent delta, either code is wrong or the
  requirement/design stack is stale.
- If a capability has requirements and design but no scenario, its operational
  meaning is unverified.
- If a requirement is treated as a product feature when it is actually a
  guarantee, governance rule, or verification obligation, the requirement
  surface has been misclassified.
- If a live constitutional artifact is corrected by in-place mutation rather
  than supersession or withdrawal, constitutional history has been corrupted.
- If a real use case reveals a gap not expressible in current requirements, a
  new intent is needed, not a code hack.

Trace closure is stricter than documentation completeness. It is the rule that
closes the constitution over realized behavior.

---
```

Successor, `SPEC_METHOD.md#trace-closure-and-anti-drift`:

```text
### Trace closure and anti-drift

Spec-driven development requires constitutional trace closure: the rule
that closes the constitution over realised behaviour, stricter than
documentation completeness (P6, P4b; rc.2
#trace-closure-and-anti-drift-rule).

Ownership: every live requirement family maps to one or more owning design
decisions; every ADR or other design record grounds itself in requirements
through an explicit `Implements:` line (rc.2 #ownership).

Downstream closure: no live requirement remains a free-floating statement
of intent; if it is live it is realised through the downstream chain or
explicitly deferred with an honest surface that records the deferment, so
every live requirement family has downstream closure, realised in design,
code and tests or explicitly deferred. No shipping code or tests exist as
ungoverned behaviour: behaviour that exists traces back to live
requirements and the design decisions that authorise it. No hidden product
surface is allowed; behaviour without trace authority is accidental law
even if it works (rc.2 #downstream-closure).

Drift signals (rc.2 #drift-signals): unowned requirements, ungrounded
design records, deferred requirements without explicit deferment, and code
without trace authority are design drift. An ADR or other design artifact
with no requirement grounding is design without constitutional authority.
Code behaviour with no design owner means the design has already drifted.
Shipping code or tests that cannot trace back out to live requirement and
design authority are ungoverned product surface. Tests that validate
implementation habit rather than requirement truth lock in drift. Events
and projection that reveal persistent delta mean either the code is wrong
or the requirement and design stack is stale. A capability with
requirements and design but no scenario has unverified operational meaning.
A requirement treated as a product feature when it is a guarantee,
governance rule or verification obligation is misclassified. A live
constitutional artifact corrected by in-place mutation rather than
supersession or withdrawal has corrupted constitutional history. A real use
case that reveals a gap not expressible in current requirements needs a new
intent, not a code hack.
```


### Row `SPEC_METHOD.md#fundamental-migration-rule` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#fundamental-migration-rule` at rc.2:

```text
## Fundamental Migration Rule

A fundamental migration is a constitutional reset, not an in-place refactor.

This rule applies when a project intentionally abandons a prior constitutional shape and re-derives itself on a new branch, version line, or methodology basis.

In that case:

- inherited constitutional documents from the prior line become migration source material, not live authority in the new line
- it is lawful to zero inherited constitutional surfaces on the migration line and rebuild them from first principles
- nothing carries forward by default; every retained statement, requirement, design choice, or guide rule must be explicitly re-adopted
- every carry-forward is intentional and should land in the correct layer: goals, intent, product, requirements, design, guide, or template
- old design and code may be used as reference implementations, but they do not govern the new constitutional surface unless explicitly re-derived and re-adopted
- absence from the new constitutional surface means "not yet adopted" and carries no automatic authority from the prior line
- the prior implementation may be moved sideways as a reference line, but that
  sideways line has no live implementation authority in the new line
- every inherited module, interface, carrier, projection, and proof surface must
  be explicitly classified before reuse

The required implementation classifications are:

- `carry_across`: the module remains materially the same and is intentionally
  re-adopted into the new line
- `redundant`: the module is no longer needed in the new line
- `rewrite`: the module remains needed but must be rebuilt under the new
  requirements and design

Unclassified inherited implementation is a defect.

The purpose of this rule is to prevent accidental law from leaking through migration by mere inheritance. Fundamental migration is controlled adoption, not passive preservation.

When performing a fundamental migration:

1. Declare the migration line and treat the prior line as source material.
2. Establish fresh constitutional surfaces for method, goals, intent, product, requirements, and design.
3. Move the prior implementation sideways if needed so it cannot continue as ambient live authority.
4. Classify inherited constitutional material as adopted, superseded, deferred, or orphaned.
5. Classify inherited implementation material as `carry_across`, `redundant`, or `rewrite`.
6. Copy forward only what is intentionally retained.
7. Re-derive downstream design and code from the new constitutional surfaces, not from ambient precedent.

For a fundamental migration:

- `carry_across` does not mean automatic copy-forward; it means explicit
  re-adoption under the new line
- direct runtime, projection, prompt, proof, or review dependence on the
  sideways implementation line is bridge debt
- proxy interfaces that partially imitate the target line while still depending
  on the sideways line are not lawful closure

This is a lawful form of supersession, not a violation of live-surface immutability, because the new line is creating a new constitutional surface rather than silently mutating the old one.

---
```

Successor, `SPEC_METHOD.md#fundamental-migration`:

```text
### Fundamental migration

A fundamental migration is a constitutional reset, not an in-place
refactor. It applies when a project intentionally abandons a prior
constitutional shape and re-derives itself on a new branch, version line or
methodology basis (P3, P6; rc.2 #fundamental-migration-rule). In that case:
inherited constitutional documents from the prior line become migration
source material, not live authority in the new line; it is lawful to zero
inherited constitutional surfaces on the migration line and rebuild them
from first principles; nothing carries forward by default, and every
retained statement, requirement, design choice or guide rule must be
explicitly re-adopted; every carry-forward is intentional and should land in the
correct layer, goals, intent, product, requirements, design, guide or template; old
design and code may be used as reference implementations but do not govern
the new constitutional surface unless explicitly re-derived and re-adopted;
absence from the new constitutional surface means not yet adopted and
carries no automatic authority from the prior line; the prior
implementation may be moved sideways as a reference line, and that sideways
line has no live implementation authority in the new line; every inherited
module, interface, carrier, projection and proof surface is explicitly
classified before reuse.

The required implementation classifications are `carry_across` (the module
remains materially the same and is intentionally re-adopted into the new
line), `redundant` (no longer needed in the new line) and `rewrite`
(still needed but rebuilt under the new requirements and design).
Unclassified inherited implementation is a defect. The purpose is to
prevent accidental law from leaking through migration by mere inheritance:
fundamental migration is controlled adoption, not passive preservation.

Performing a fundamental migration: declare the migration line and treat
the prior line as source material; establish fresh constitutional surfaces
for method, goals, intent, product, requirements and design; move the
prior implementation sideways if needed so it cannot continue as ambient
live authority; classify inherited constitutional material as adopted,
superseded, deferred or orphaned; classify inherited implementation
material as `carry_across`, `redundant` or `rewrite`; copy forward only
what is intentionally retained; re-derive downstream design and code from
the new constitutional surfaces, not from ambient precedent. In a
fundamental migration `carry_across` does not mean automatic copy-forward
but explicit re-adoption under the new line; direct runtime, projection,
prompt, proof or review dependence on the sideways implementation line is
bridge debt; proxy interfaces that partially imitate the target line while
still depending on the sideways line are not lawful closure. This is a
lawful form of supersession, not a violation of live surface immutability
(§2), because the new line creates a new constitutional surface rather than
silently mutating the old one.

The four classes of inherited constitutional material record the
adoption decision the new line takes on each inherited statement. For an
inherited requirement, the legacy classifications of
[§2 Requirement categories and classification](#requirement-categories-and-classification)
record a different thing: the standing of a requirement that is in the
live surface. The two relate as follows, and are not one classification:
- an adopted requirement enters the live surface as Active, or as Deferred
  when it is adopted as an explicitly not-yet-operative obligation;
- a requirement whose adoption is deferred is not in the live surface: it
  has no legacy classification and no authority until it is adopted,
  because absence from the new surface means "not yet adopted";
- a superseded or orphaned inherited requirement takes Superseded or
  Orphaned, with that table's meanings.

For other inherited
constitutional material the classes keep their names and the steps
above. They are declared states of the new line's surfaces and, as §2
states, none of them is or supplies the
[RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
disposition of a predecessor claim (P3, P6). Purpose and material
relation: an inherited requirement in a migration falls under both this
step and the legacy classification rule, and stating how the two records
relate leaves no two records of one standing to reconcile (P3).
```


### Row `SPEC_METHOD.md#hard-break-discipline` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#hard-break-discipline` at rc.2:

```text
### Hard-Break Discipline

Inside-out migration is a hard-break sequence over one interface family.

The migration wave is the ordered set of those breaks. It is not a separate mode
that permits competing or ambiguous dual truth over the same request, fact,
identity, state, or projection. Explicitly specified, deterministically routed,
non-overlapping Product or compatibility scopes may coexist while the enclosing
migration remains open.

For each break:

1. publish or admit the new deepest authoritative source carrier
2. deliberately sever one old authoritative seam
3. keep that seam broken
4. repair outward from source truth to consumers, then projections, then
   prompts/reports, then proof surfaces
5. run negative proof that the severed seam is rejected rather than merely
   unused

During this sequence:

- tests may discover missed interfaces, but they do not replace the required
  interface inventory
- newly discovered affected interfaces remain part of the same migration wave
  unless the work is explicitly repriced upward
- re-enabling the old seam through wrappers, fallbacks, projections, or prompt
  paths is a migration defect
```

Successor, `SPEC_METHOD.md#hard-break-discipline`:

```text
### Hard-break discipline

Inside-out migration is a hard-break sequence over one interface family.
The migration wave is the ordered set of those breaks; it is not a separate
mode that permits competing or ambiguous dual truth over the same request,
fact, identity, state or projection. Explicitly specified, deterministically
routed, non-overlapping product or compatibility scopes may coexist while
the enclosing migration remains open (P3; rc.2 #hard-break-discipline).

For each break: publish or admit the new deepest authoritative source
carrier; deliberately sever one old authoritative seam; keep that seam
broken; repair outward from source truth to consumers, then projections,
then prompts and reports, then proof surfaces; run negative proof that the
severed seam is rejected rather than merely unused. During the sequence,
tests may discover missed interfaces but do not replace the required
interface inventory; newly discovered affected interfaces remain part of
the same migration wave unless the work is explicitly repriced upward;
re-enabling the old seam through wrappers, fallbacks, projections or prompt
paths is a migration defect.
```


### Row `SPEC_METHOD.md#installed-dev-proof-rule` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#installed-dev-proof-rule` at rc.2:

```text
## Installed Dev Proof Rule

Where a system has an installable or runnable development form, the decisive
proving lane runs against an installed development version as if it were an
independent project or externalized target, not only against the source tree in
place.

That proof should prefer:

- fresh sandbox or equivalent isolated environment
- installed or built development artifact
- execution through the same declared entry/control/runtime surfaces the real
  product uses

Direct source-level or unit-level checks may remain useful, but they do not
replace installed-dev proof of the system under test.

---
```

Successor, `ASSURANCE.md#5-installed-dev-proof`:

```text
## 5. Installed dev proof

Where a system has an installable or runnable development form, the
decisive proving lane runs against an installed development version as if
it were an independent project or an externalised target, not only against
the source tree in place (P6, P3; rc.2 #installed-dev-proof-rule). That
proof should prefer a fresh sandbox or equivalent isolated environment, an
installed or built development artifact, and execution through the same
declared entry, control and runtime surfaces the real product uses. Direct
source-level or unit-level checks may stay useful; they do not replace
installed-dev proof of the system under test (P6; SPEC_METHOD §6 for the
install and development-product roles).
```


### Row `SPEC_METHOD.md#legacy-classification-rule` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#legacy-classification-rule` at rc.2:

```text
## Legacy Classification Rule

Every inherited or legacy requirement must be classified as one of:

| Classification | Meaning | Action |
|---------------|---------|--------|
| **Deferred** | Retained in the live surface as an explicit not-yet-operative or not-yet-realized obligation | Keep with an honest deferment surface and do not present as current closure |
| **Superseded** | Ownership has moved to a newer constitutional surface or design decision | Add Implements/Supersedes to the governing design record |
| **Active** | Remains live constitutional law in the current surface | Must have an owning design decision — write or update one |
| **Orphaned** | No longer part of the intended system | Remove or explicitly supersede |

Nothing live may remain unclassified.

---
```

Successor, `SPEC_METHOD.md#requirement-categories-and-classification`:

```text
### Requirement categories and classification

Every live requirement family is categorised by the kind of truth it
asserts, so that the requirement surface is not treated as a feature list
(P1, P2; rc.2 #requirement-categories):

| Category | Meaning | Typical question |
|---|---|---|
| Capability | a behaviour, function or surface the system must provide | what can the system do |
| Constraint / Guarantee | an invariant, law, safety property, portability rule or semantic guarantee that bounds how the system may behave | what must always remain true |
| Governance | a policy or control rule over lifecycle, authority, visibility, release or operator action | what governs use and change |
| Verification | a requirement on tests, evidence, traceability, qualification or forensic surfaces | how do we know the claim is true |

Requirements remain part of the constitutional layer in all four cases. A
category is not a priority label and not a claim that the requirement is
user-facing; it states what kind of project truth the requirement owns.
Requirements describe the full constitutional what; design describes the
structural how, with ADRs one durable design form; scenarios validate the
operational meaning of capability claims. Not every requirement should be
translated into a marketed feature; some are better expressed as
guarantees, constraints, governance rules or verification obligations.
Requirements should also avoid freezing concrete realisation choices
prematurely:
unless a path, filename or packaging rule is itself constitutional, it
belongs to design.

Every live requirement family is classified on two independent axes (P3,
P1; rc.2 #requirement-classification-rules): lifecycle status (Active,
Deferred, Superseded, Orphaned) and requirement category (the four above).
The axes answer different questions: status says whether the requirement
still belongs in the constitution and whether it is operative or explicitly
deferred; category says what kind of truth it asserts. A live requirement
is incomplete if either axis is missing. In project documents the
classification is explicit in the requirement's header metadata: `Status`
carries lifecycle status and `Category` carries the kind.

Every inherited or legacy requirement is classified as one of these, and
nothing live remains unclassified (P3; rc.2 #legacy-classification-rule):

| Classification | Meaning | Action |
|---|---|---|
| Deferred | retained in the live surface as an explicit not-yet-operative or not-yet-realised obligation | keep with an honest deferment surface; do not present as current closure |
| Superseded | ownership has moved to a newer constitutional surface or design decision | add Implements and Supersedes to the governing design record |
| Active | remains live constitutional law in the current surface | has an owning design decision; write or update one |
| Orphaned | no longer part of the intended system | remove or explicitly supersede |

The lifecycle statuses (Active, Deferred, Superseded, Orphaned), the
categories and the legacy classifications are declared states of a
requirement, not results, and map to no core value. So are the other
declared classes of this member: the kinds of evidence of §3 (material
advance, prerequisite readiness, preservation, regression), the old-path
classes of §7 Required migration protocol, the inherited-material
classes adopted, superseded, deferred and orphaned and the
implementation classifications `carry_across`, `redundant` and `rewrite`
of §7 Fundamental migration, and the ADR `Status:` values of §10; the change
classes are declared states under §4 Change classes. Each records
a declared classification of its subject, not the answer to a predicate
that an evaluation decides. An evaluation that reads them returns its own
core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a declared state is never combined as an evaluation result, so
a requirement marked Active, or evidence classed as material advance,
cannot stand in for a `satisfied` result, and a requirement marked
Deferred or Orphaned cannot stand in for a `falsified` one (P5, P1).

The legacy classification answers one question: what standing an
inherited requirement holds in the project's own live requirement
surface. The disposition of a predecessor claim under
[RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
answers another: what a successor release does with a claim of the
released predecessor it evolves, a claim that qualification evaluates.
Where a project's work is also such a successor, each predecessor claim
takes its RELEASE §9 disposition by that section's predicates, and no
lifecycle status or legacy classification supplies or replaces it: a
requirement marked Active may still be `superseded` where its meaning
changed, Superseded names no accepted successor relation, and Orphaned
is not an intentional removal. Purpose and material relation: two
vocabularies with overlapping words would otherwise let a project-level
record stand in for a successor disposition that its owner has not made
(P6, P3).
```


### Row `SPEC_METHOD.md#live-surface-immutability` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#live-surface-immutability` at rc.2:

```text
## Live Surface Immutability

The project may accumulate multiple live domain surfaces over time. A live surface is versioned constitutional history, not scratch space.

- Engine code, design documents, tests, and tooling may be refactored aggressively while they remain mutable implementation surfaces.
- Live domain artifacts, once published as live constitutional surfaces, are immutable in place.
- If a live domain artifact is wrong, the valid actions are:
  - supersede it with a new version, or
  - withdraw/delete it from the live surface.
- Transitional implementation paths, migration scaffolds, and fallback behaviors have no permanent authority in the live surface. Once superseded, they are retired; any retained responsibility satisfies the Core Interface Migration Rule's retention relation.

The past is preserved by version control, operational event history where present, and superseded constitutional artifacts. Spec-driven development does not require shipping compatibility shims forever, but it also does not allow silent mutation of live constitutional history.

---
```

Successor, `SPEC_METHOD.md#live-surface-immutability`:

```text
### Live surface immutability

A project may accumulate multiple live domain surfaces over time. A live
surface is versioned constitutional history, not scratch space (P3; rc.2
#live-surface-immutability). Engine code, design documents, tests and
tooling may be refactored aggressively while they remain mutable
implementation surfaces. Live domain artifacts, once published as live
constitutional surfaces, are immutable in place; if one is wrong, the valid
actions are to supersede it with a new version or to withdraw or delete it
from the live surface. Transitional implementation paths, migration
scaffolds and fallback behaviours have no permanent authority in the live
surface: once superseded they are retired, and any retained responsibility
satisfies the retention relation of §7 (closure criterion). The past is
preserved by version control, operational event history where present and
superseded constitutional artifacts. The method does not require shipping
compatibility shims forever, and it does not allow silent mutation of live
constitutional history.
```


### Row `SPEC_METHOD.md#local-constitutional-binding` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#local-constitutional-binding` at rc.2:

```text
### Local Constitutional Binding

A local axiom, override, or disambiguation does not gain authority from its file
category or from being listed in the overlay. Every local entry names:

- the URI carrying the local decision;
- the existing Product, requirement, accepted-design, or other lawful authority
  that owns it;
- the clause or ambiguity it overrides or resolves where applicable; and
- the exact scope to which it applies.

Each `local_constitution.disambiguations` binding additionally names:

- `term` — the exact lexical label being resolved;
- `context` — the bounded-context identity in which the resolution applies;
- `disambiguates` — the complete material candidate concept or clause
  references;
- `resolves_to` — the exact selected concept reference, which is one member of
  `disambiguates`;
- `basis` — every selected semantic basis needed to interpret the candidates
  and resolution; and
- `uri`, `authority`, and `applies_to` — the owning resolution carrier, lawful
  authority, and exact governed scope.

The referenced `uri` owns the resolution. When candidates cross bounded
contexts, that carrier also declares the complete import, translation, or
equivalence relation required above. The overlay metadata makes the relation
discoverable and checkable; it does not restate the source-owned meanings or
mint the decision.

An empty local array explicitly declares that no local entry of that kind is
bound for the product. Omission is not an equivalent declaration.
```

Successor, `PRODUCT_DEFINITION.md#6-local-constitutional-binding`:

```text
## 6. Local constitutional binding

A local axiom, override or disambiguation gains no authority from its file
category or from being listed in the overlay. Every local entry names (P6;
rc.2 #local-constitutional-binding):

- the URI carrying the local decision;
- the existing Product, requirement, accepted-design or other lawful
  authority that owns it;
- the clause or ambiguity it overrides or resolves, where applicable; and
- the exact scope to which it applies.

Each `local_constitution.disambiguations` binding additionally names (P1,
P3):

- `term`: the exact lexical label being resolved;
- `context`: the bounded-context identity in which the resolution applies;
- `disambiguates`: the complete material candidate concept or clause
  references;
- `resolves_to`: the exact selected concept reference, which is one member
  of `disambiguates`;
- `basis`: every selected semantic basis needed to interpret the
  candidates and the resolution; and
- `uri`, `authority` and `applies_to`: the owning resolution carrier, the
  lawful authority and the exact governed scope.

The referenced `uri` owns the resolution. When the candidates cross bounded
contexts, that carrier also declares the complete import, translation or
equivalence relation §5 requires. The overlay metadata makes the relation
discoverable and checkable; it neither restates the source-owned meanings
nor mints the decision (P6).

An empty local array explicitly declares that no local entry of that kind
is bound for the product. Omission is not an equivalent declaration (P6,
P4b).
```


### Row `SPEC_METHOD.md#method` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#method` at rc.2:

```text
## Method

When any substantive intake arrives:

1. Triage the intake and classify the change.
2. Determine the lawful re-entry point into the constitutional chain.
3. Identify the affected downstream span that must remain consistent.
4. Only then treat the work as implementation, repricing, or release-bound change.

When a feature is introduced or changed:

1. Update **Goals** if the current bounded work wave or overriding concerns have changed.
2. Update **Intent** if the purpose or scope has changed.
3. Update **Product** if the current product realization, terms, boundaries, or end-state shape have changed.
4. Update **Requirements** so the invariant truths are explicit as a decomposition of the product definition, including any lifecycle obligations or named lifecycle ambiguity gaps, and classify each new or changed requirement by category.
5. Establish or update **Design** so it owns the governing structural `HOW`.
   When `DESIGN_MODULE_METHOD.md` applies, use its decision-completeness rule:
   design, implementation, and tests may co-evolve only when
   `co_evolution_admissible(B)` holds. Otherwise accept the smallest causally
   closed affected design set before retained implementation establishes an
   unresolved, contradictory, or materially non-equivalent relation.

   When `DESIGN_MODULE_METHOD.md` does not apply, design, implementation, and
   tests may co-evolve when upstream truth leaves no unresolved material design
   decision. When such a decision remains, accept the affected design before
   retained implementation establishes it. ADRs are one valid design form.
6. Write **Scenarios** for capability claims that require operational proof, and define other evidence surfaces for non-capability requirements where appropriate.
7. Prefer declarative expression of the problem and acceptance surface before adding imperative mechanism.
8. Check the reconstruction boundary: can the current goals support the current intent, can the current intent support the current product, can the current product support the intended requirements, can the current requirements support the intended design, and can the current design support the intended implementation?
9. Record any major ambiguity discovered at the active boundary, and govern it according to declared risk appetite rather than silent convenience.
10. Develop **Code** under the selected design relation and reconcile design,
    implementation, and tests before promotion or closure.
11. Use **Events, Projection, and Delta** to verify whether reality still satisfies the requirements.

When bootstrapping a project or repricing a requirement surface:

1. Resolve the applicable Product Definition, verify its exact installed STDO
   basis, load its declared bootstrap entrypoint, and then load `GOALS.md` or
   the bound equivalent current epic carrier.
2. Perform the `goals → intent` step and write or confirm `INTENT.md`.
3. Perform the `intent → product` step and write or confirm `PRODUCT.md` as the current product-definition bridge.
4. Gather requirement source material from the relevant constitutional inputs.
5. Perform the `product → requirements` step and write the resulting live surface under `requirements/`.
6. Store requirements as individual files or grouped requirement families, whichever best preserves clarity and avoids monolithic sprawl.
7. Make `requirements/` the sole live requirement authority before proceeding to design and code.
8. Prefer declarative structure over procedural workaround while shaping the new requirement surface.
9. Record any major ambiguity that remains at the current boundary before downstream realization proceeds.
10. Only after that surface exists should downstream design and implementation be treated as constitutionally grounded.

When a real use case reveals a gap:

1. Run intake triage first and classify the report as a lawful change.
2. Then write the **Scenario** as the first substantive project artifact for the
   gap so the pressure becomes concrete and testable.
3. Run **Gap Analysis** — is this a missing implementation or a constitutional insufficiency?
4. If constitutional: reprice **Goals** when the current work wave changes, write a new **Intent**, then flow forward (product → requirements → design → code).
5. If implementation: write requirements/design as needed, then implement.

The intake source does not change this rule.

A bug report, feature request, failed testcase, release blocker, or operator
observation still enters through intake triage first, then follows the lawful
change class selected there.

---
```

Successor, `SPEC_METHOD.md#procedures`:

```text
### Procedures

When any substantive intake arrives (P2, P4b; rc.2 #method): triage the
intake and classify the change; determine the lawful re-entry point into
the constitutional chain; identify the affected downstream span that must
remain consistent; only then treat the work as implementation, repricing or
release-bound change.

When a feature is introduced or changed: update goals if the current
bounded work wave or overriding concerns have changed; update intent if the
purpose or scope has changed; update product if the current product
realisation, terms, boundaries or end-state shape have changed; update
requirements so the invariant truths are explicit as a decomposition of the
product definition, including any lifecycle obligations or named lifecycle
ambiguity gaps, and classify each new or changed requirement by category;
establish or update design so it owns the governing structural HOW, where
under the design profile its decision-completeness rule applies (design,
implementation and tests may co-evolve only when its co-evolution predicate
holds, otherwise the smallest causally closed affected design set is
accepted before retained implementation establishes an unresolved,
contradictory or materially non-equivalent relation;
[DESIGN_MODULE](DESIGN_MODULE.md)), and
where that profile does not apply design, implementation and tests may
co-evolve when upstream truth leaves no unresolved material design
decision, and when such a decision remains the affected design is accepted
before retained implementation establishes it, ADRs being one valid design
form; write scenarios for capability claims that require operational proof
and define other evidence surfaces for non-capability requirements where
appropriate; prefer declarative expression of the problem and acceptance
surface before adding imperative mechanism; check the reconstruction
boundary, whether current goals support current intent, current intent the
current product, current product the intended requirements, current
requirements the intended design, and current design the intended
implementation; record any major ambiguity discovered at the active
boundary and govern it by declared risk appetite rather than silent
convenience; develop code under the selected design relation and reconcile
design, implementation and tests before promotion or closure; use events,
projection and delta to verify whether reality still satisfies the
requirements.

When bootstrapping a project or repricing a requirement surface: resolve
the applicable product definition, verify its exact installed basis, load
its declared bootstrap entrypoint (PRODUCT_DEFINITION §12), then load the
goals surface or the bound equivalent current work-wave carrier; perform
the goals-to-intent step and write or confirm the intent surface; perform
the intent-to-product step and write or confirm the product definition as
the current bridge; gather requirement source material from the relevant
constitutional inputs; perform the product-to-requirements step and write
the resulting live surface under the requirement surface; store
requirements as individual files or grouped families, whichever best
preserves clarity and avoids monolithic sprawl; make the requirement
surface the sole live requirement authority before proceeding to design and
code; prefer declarative structure over procedural workaround while shaping
the new surface; record any major ambiguity that remains at the current
boundary before downstream realisation proceeds; only after that surface
exists should downstream design and implementation be treated as
constitutionally grounded.

When a real use case reveals a gap: run intake triage first and classify
the report as a lawful change; then write the scenario as the first
substantive project artifact for the gap so the pressure becomes concrete
and testable; run gap analysis, asking whether this is a missing
implementation or a constitutional insufficiency; if constitutional,
reprice goals when the current work wave changes, write a new intent, then
flow forward through product, requirements, design and code; if
implementation, write requirements and design as needed, then implement.
The intake source does not change this rule: a bug report, feature request,
failed test case, release blocker or operator observation still enters
through intake triage first, then follows the lawful change class selected
there.
```


### Row `SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001` at rc.2:

```text
## One Constitutional Surface And Version Boundary (`STDO-SURFACE-001`)

The shared methodology is modular in authorship and singular in authority.
Each law has one owning standard; other standards consume it by reference. The
standards become operative only as one complete released STDO version.

A released cut identifies its exact member set, member digests, review basis,
human acceptance, and immutable identity. Compressions, templates, comments,
candidate work, installed copies, and mutable source are derived, evidential, or
authoring surfaces. They cannot become a selectable partial constitution or
reinterpret the owning standards.

Within their declared scope, derived instructions preserve the owning clauses'
applicability, obligations, permissions, exclusions, decision owners and
invalidators. A projected prohibition cannot lose its condition or lawful
alternative even when every source digest is correct. A summary, bootstrap or
index cannot require a stricter or weaker relation by compression. Its
references must be resolvable within the declared actor's access; otherwise the
required meaning is supplied directly.

STDO owns normative construction algebra, authority relations, abstract state
and transition laws, admissibility conditions, necessary causal order, and
evidence invariants. Consumers own concrete Product realization: instantiated
types and schemas, files, tools, runtime and orchestration machinery, tests,
and executable conformance implementation. A concrete form is method law only
when the method explicitly accepts it as an interoperability boundary.

A shared-method amendment cannot create an executable tool, workflow engine,
runtime, assurance system, or consumer realization as STDO Product scope
without separate explicit human authorization. An agent recording a ruling
cannot widen its subject, implication, authority, or change class.

Only a released method version is publication authority. Mutable method source
may author a future cut; it must not silently govern a consumer.

---
```

Successor, `PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary`:

```text
## 11. One constitutional surface and version boundary

STDO-SURFACE-001. The shared methodology is modular in authorship and
singular in authority. Each law has one owning member; other members
consume it by reference. The members become operative only as one complete
released version of the method (P6, P3; rc.2
#one-constitutional-surface-and-version-boundary-stdo-surface-001).

A released cut identifies its exact member set, member digests, review
basis, human acceptance and immutable identity. Compressions, templates,
comments, candidate work, installed copies and mutable source are derived,
evidential or authoring surfaces. They cannot become a selectable partial
constitution and cannot reinterpret the owning members (P3, P6).

Within their declared scope, derived instructions preserve the owning
clauses' applicability, obligations, permissions, exclusions, decision
owners and invalidators. A projected prohibition cannot lose its condition
or its lawful alternative, even when every source digest is correct. A
summary, bootstrap or index cannot require a stricter or weaker relation by
compression. Its references are resolvable within the declared actor's
access; otherwise the required meaning is supplied directly (P4b, P1;
FOUNDATIONS §4, reference versus body).

Staleness binding. What a derived surface is, when it is stale, and
what an actor uses in its place are
[ACTIVATION §2 Staleness of derived surfaces](ACTIVATION.md#staleness-of-derived-surfaces);
which questions a derived surface decides on its own is ACTIVATION §2,
Standalone scope. This member refines that law for the derived surfaces
a released cut or an installation carries, among them compressions,
templates, bootstraps, indexes and projected frames. Each carries the
path and digest of each deciding source it was derived from, and of each
index it watches (GLOSSARY §2). A change to any of those digests is the
source change that makes it stale under that law, and it must be
regenerated or explicitly re-accepted before an installation treats it
as current. What a matching digest establishes is stated above
(EVALUATION §7). The raw owning members of the same
selected cut remain the deciding authority: a question that a stale or
insufficient carrier cannot decide is decided from them, as ACTIVATION
§2 states (P3, P5, P6; provenance rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states).

The method owns normative construction algebra, authority relations,
abstract state and transition laws, admissibility conditions, necessary
causal order and evidence invariants. Consumers own concrete Product
realisation: instantiated types and schemas, files, tools, runtime and
orchestration machinery, tests and executable conformance implementation.
A concrete form is method law only when the method explicitly accepts it
as an interoperability boundary, as §1 does for the definition schema and
template (P2, P6).

A shared-method amendment cannot create an executable tool, workflow
engine, runtime, assurance system or consumer realisation as STDO Product
scope without separate explicit human authorisation. An agent recording a
ruling cannot widen its subject, implication, authority or change class
(P6).

Only a released method version is publication authority. Mutable method
source may author a future cut; it must not silently govern a consumer
(P6, P3).
```


### Row `SPEC_METHOD.md#position` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#position` at rc.2:

```text
## Position

Spec-driven development treats specification as constitutional source, not as
commentary on code after the fact.

The point is to make software re-derivable, auditable, and correctable under
explicit authority.

Its overriding bias is declarative rather than imperative.

In the age of LLMs, the system should primarily declare truths, structures,
interfaces, constraints, and evidence surfaces, then let lawful processing
derive and realize work from that declared surface.

Imperative procedure still exists, but it is subordinate to declared authority.

---
```

Successor, `SPEC_METHOD.md#position`:

```text
### Position

Spec-driven development treats specification as constitutional source, not
as commentary on code after the fact. Its point is to make software
re-derivable, auditable and correctable under explicit authority. Its
overriding bias is declarative rather than imperative: the system should
primarily declare truths, structures, interfaces, constraints and evidence
surfaces, and let lawful processing derive and realise work from that
declared surface.
Imperative procedure still exists and is subordinate to declared authority
(P6, P1; rc.2 #position).

Constitutional examples use neutral capability and authority identities:
they demonstrate enabled capabilities rather than cite a consumer as
precedent, whose particulars cannot become method law
([PROFILES §1](PROFILES.md#1-the-boundary)) (P1, P6; provenance rc.2
authority_compressions/stdo_compressed.md, spec_method.compressed.md and
ticket_method.compressed.md, a claim no rc.2 body states).
```


### Row `SPEC_METHOD.md#probabilistic-work-boundary` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#probabilistic-work-boundary` at rc.2:

```text
## Probabilistic Work Boundary

Spec-driven development exists to govern the boundary around work, not to absorb
the worker's internal solution strategy into the framework.

For any probabilistic, agentic, or delegated work unit, the live specification
and design should declare:

- the input and output contract
- the required context
- the capability or role expectation
- the admissible evidence and evaluator regime
- the provenance obligation
- the lawful stop, hold, gap, continuation, or completion states

The worker, tool, agent, or domain implementation owns the internal HOW inside
that declared boundary unless the product explicitly promotes part of that HOW
into reusable declared structure.

Deterministic checks and validation are evidence surfaces. They may optimize or
prove a domain-local path where the domain can make part of the work precise.
They do not authorize the methodology, runtime, or framework to absorb domain
solution strategy as constitutional law.

In graph-native refinements such as `ODD_METHOD.md`, this boundary is usually
one vector or edge traversal. The traversal is the admissible external space.
Any unconstrained part of a probabilistic worker's reasoning remains hidden
worker-internal traversal and must be forced back through declared contracts,
evidence, provenance, and control truth.

If a framework layer begins prescribing domain solution strategy beyond the
declared work contract and control truth, it has crossed its authority boundary.

---
```

Successor, `FOUNDATIONS.md#work-boundary`:

```text
### Work boundary

The method governs the boundary around a probabilistic, agentic or
delegated work unit; it does not absorb the worker's internal solution
strategy into the framework (P0, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary`).
The declared boundary of such a unit is an object with six parts, which the
live specification and design should declare: the input and output contract; the
required context; the capability or role expectation; the admissible
evidence and evaluator regime; the provenance obligation; and the lawful
stop, hold, gap, continuation or completion states. The worker, tool, agent
or domain implementation owns the internal HOW inside that boundary unless
the product explicitly promotes part of that HOW into reusable declared
structure. The step of ACTIVATION §1 is this unit with its intake, context
and result algebra made exact.
```

Successor, `FOUNDATIONS.md#3-commitments`:

```text
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

### Construction synthesis

The commitments together govern movement from an observed current state
to an acceptable destination under finite resources. This is a synthesis
of their relations, stated once so that every consumer of the construction
relation, which [ACTIVATION §1](ACTIVATION.md#construction-relation), a
tier 1 foundations member of this corpus, owns, can see which commitment grounds each part. It is derived, not a further
commitment, and has the standing of a consequence under Foundation to law
below (P6). It is law carried from the common requirements' synthesis of
their principles.

| Commitment | Contribution to construction |
|---|---|
| P0 Bounded construction | the outer contract is realised through steps whose contexts fit the actors' envelopes, so acquisition and work are bounded; the actor's internal path within a step is its own |
| P1 Interpretation | the required conditions, the observed state and the predictions about an action's effects are different accounts; the meaning needed to compare them is preserved |
| P2 Purpose | Z is selected with the criteria by which a strategy and a realised outcome are adequate; work with no route to Z is unjustified |
| P3 Identity and state | the persistent subject, its current observations and its dependencies, from which work continues, stay distinct from any account of them |
| P4a Typed composition | outer obligations are carried through bounded steps, refinement and the composition boundaries between them |
| P4b Conservation of step-produced facts | what a step produced and cannot re-acquire is conserved through the loop of observation, correction and reuse |
| P5 Totality | resource tradeoffs, recursive progress, recovery and truthful stops are accounted for, and an undecided outcome is reported as undecided |
| P6 Justification and authority | what the results support, and who may change the model, act or accept delivery, are established and not minted |

The construction relation states the obligations this synthesis places on
construction. Finite capacity motivates bounded work; purpose, meaning,
identity, compatibility, evidence and authority retain their own
premises. Strategy selection and domain controls are added choices within
those obligations, each with its owner. Feedback, a useful model and
locally valid steps do not by themselves prove reachability, stability,
optimality or termination (P5, P6).

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

Consumers. After the table, a paragraph names, for each row, the sections
in this or other members that apply the rule where an actor enters it,
each linked to the consumer's own locus, or states that no separate
consumer applies and
the scope of that absence. A blank field or a generic referral establishes
neither coverage nor non-applicability. The paragraph is a trace like the
table: a consumer named in it applies the rule and decides nothing the
owning section does not (P2, P6; law carried from the common standalone
successor requirement).

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
table (P1, P6). Every family table in this corpus has its consumers paragraph.

| ID | Family | Table | Accounts for | Pillar |
|---|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple | 1–9 |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1 including the construction relation, §4; SPEC_METHOD §8 except delivery priority | 1, 3, 4, 5, 6, 7, 8, 9 |
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
| F22 | Assurance relations | [FOUNDATIONS §4 Assurance relations](#assurance-relations) | FOUNDATIONS §4 Preservation through construction, Assertions and observation, Parallel derivation and mutual assurance, Quantified assurance, Change impact and evidence reuse, Formal representation | 2, 3, 4, 6, 7, 9, 10 |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §3 Construction synthesis relates the commitments to the
  construction relation that ACTIVATION §1 states and decides no outcome of
  its own. §2 Work boundary is the object that P0's boundary
  commitment states. §2 Accounts of a construction states a distinction
  and decides no outcome of its own; family F10 traces its use at
  SPEC_METHOD §11. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the family-import rule, which families a profile imports and how a row cites them under the import rule of §2, that every profile table cites in its
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


### Row `SPEC_METHOD.md#process-constitution` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#process-constitution` at rc.2:

```text
## Process Constitution

This methodology is not only a local operating note for one implementation. It is the process constitution for building projects by spec-driven development.

Its role is meta-constitutional:

- it defines how goals, intent, product, requirements, design, code, evidence, and repricing relate
- it defines what counts as specification sufficiency
- it defines what kinds of requirement truth exist
- it defines how authority flows during iterative delivery

Therefore, if a project's implementation disappears, this methodology should still be sufficient to bootstrap a new spec-driven project process from scratch.

The important boundary is:

- `SPEC_METHOD.md` defines the process constitution
- `GOALS.md` conventionally names the current overriding concerns for the active body of work
- `INTENT.md` conventionally names domain direction
- `PRODUCT.md` conventionally names the current product-definition surface of the mutable source project
- `specification/requirements/` is the conventional live requirement surface derived from product definition
- a shared design surface plus any tenant-local design surfaces choose the concrete mechanism
- the product's `stdo_<label>.json` definition binds the actual authority
  locations; these conventional names do not require an existing project to
  move or duplicate its files
- the definition's `how.build_tenants` entries locate the project-owned
  realizations beneath one shared specification

The authoritative split is strict:

- the surfaces bound by `what` define `WHAT`
- design and realization surfaces define `HOW`
- no build-tenant, design, code, definition overlay, or derived surface may
  become co-equal constitutional authority with the bound `WHAT`

In the default scaffold, `requirements/` is a folder under `specification/`.
Requirements may instead be stored at any URI bound by the product definition,
as individual files or grouped into requirement families. The purpose of the
default shape is to avoid collapsing the constitutional surface into one
monolithic requirements document, not to make folder placement constitutional.

This is one expression of the broader declarative bias: we prefer declaring requirement structure and family boundaries over maintaining one imperative catch-all document.

So if project-specific design and code disappeared, recovery would proceed through this methodology plus the surviving domain specification. Methodology alone can bootstrap the process; methodology plus domain specification can reconstruct the project.

---
```

Successor, `SPEC_METHOD.md#process-constitution`:

```text
### Process constitution

This method is the process constitution for building projects by
spec-driven development, not a local operating note for one implementation.
Its role is meta-constitutional: it defines how goals, intent, product,
requirements, design, code, evidence and repricing relate; what counts as
specification sufficiency; what kinds of requirement truth exist; and how
authority flows during iterative delivery. If a project's implementation
disappears, the method should still be sufficient to bootstrap a new
spec-driven project process from scratch; the method plus the surviving domain specification
can reconstruct the project (P2, P0; rc.2 #process-constitution).

The boundary between surfaces is this: this member defines the process
constitution; a goals surface, conventionally `GOALS.md`, names the current
overriding concerns for the active body of work; an intent surface,
conventionally `INTENT.md`, names domain direction; a product-definition
surface, conventionally `PRODUCT.md`, names the current product definition
of the mutable source project; a requirement surface, conventionally
`specification/requirements/`, is the live requirement surface derived from
the product definition; a shared design surface plus any tenant-local design
surfaces choose the concrete mechanism. The product's definition binds the
actual authority locations
([PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)); the conventional names
require no existing project to move or duplicate its files, and the
definition's tenant registry entries locate the project-owned realisations
beneath one shared specification
([PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)).

The authoritative split is strict: the surfaces bound as WHAT define WHAT;
design and realisation surfaces define HOW; no build tenant, design, code,
definition overlay or derived surface becomes co-equal constitutional
authority with the bound WHAT (P6).

In the default scaffold `requirements/` is a folder under `specification/`.
Requirements may instead be stored at any location the product definition
binds, as individual files or grouped into requirement families. The default
shape exists to avoid collapsing the constitutional surface into one
monolithic requirements document, not to make folder placement
constitutional. This is one expression of the declarative bias: declaring
requirement structure and family boundaries is preferred over maintaining
one imperative catch-all document (P2).
```


### Row `SPEC_METHOD.md#product-outcome-conservation-stdo-up-013` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#product-outcome-conservation-stdo-up-013` at rc.2:

```text
## Product Outcome Conservation (`STDO-UP-013`)

Every Product-outcome-bearing work wave identifies one explicitly selected,
unresolved, directly verifiable Product-defined outcome and declares the
acceptance interval for that instance. Product-progress claims and promotion
onto the supported Product path are judged against that same outcome.

Evidence distinguishes material advance, prerequisite readiness, preservation,
and regression. Only material advance projects Product progress. Prerequisite
work names the Product obligation it enables and remains bounded. Preservation
is useful evidence but is not progress.

The exact bound outcome instance stops selecting later Product-progress work
when the owning authority accepts it. Its witnesses remain regression and
preservation evidence. Acceptance exhausts only that instance and its declared
acceptance interval. It does not discharge an enduring guarantee, recurring
obligation, or broader Product family beyond the accepted instance. Further
work against the accepted instance is preservation, a named bounded
prerequisite for another admitted outcome, or a new change requiring lawful
repricing; it is not additional progress against the accepted instance.

Selecting the next unresolved outcome already defined by Product is a Goals and
work-sequencing decision. Changing an outcome's meaning or scope, or introducing
a new Product outcome, requires lawful re-entry at Product.

Evidence evaluates and constrains its bound Product claim. Completion of a
proof surface, matrix, coverage ledger, inventory, design-method artifact, test
suite, or other evidence surface cannot by itself select, enlarge, or replace
the Product outcome. If an assurance capability is explicitly defined as
Product behavior, delivery of that capability is judged as Product progress;
its evidence still does not author the claim. The same artifact may be Product
output for one claim and evidence for another only when those roles are
declared separately.

Within a Product-outcome-bearing work wave, material realization growth derives
authority from the selected unresolved Product outcome, an admitted named
bounded prerequisite to it, or an admitted named bounded experiment whose
stated observation discriminates a stated decision for it. A prerequisite or
experiment authorizes only its declared provisional bound. It does not select
or enlarge the Product outcome, authorize downstream work, confer promotion or
closure, or waive applicable Prime, design, safety, authority, or release law.

Admission or renewal of a prerequisite or experiment belongs to the authority
owning the selected work wave, or its explicitly bounded proxy, and is recorded
in the existing durable Goals or ticket authority. The admitted basis states
its provisional bound and exhaustion or falsification condition. Satisfaction
of an experiment's stated decision-discriminating observation exhausts that
experiment. Drafting or validating a ticket or execution contract, retaining
active status, or holding a prior admission cannot create, extend, or renew the
basis.

Acceptance of the selected outcome, discharge of an admitted prerequisite, or
resolution of an admitted experiment's stated decision exhausts that basis. A
basis or bound also ends when another admitted terminal condition is reached or
it is rejected, withdrawn, superseded, repriced away, or falsified by evidence.
Ended authority cannot be renewed by repair, continuation, evidence, active
ticket or run state, or prior admission; further material work requires a new
admission by the owning authority or its explicitly bounded proxy.

Retention as supported Product behavior, required evidence, regression
protection, or bounded donor material does not confer further growth authority.
Consumers own deletion, archival, quarantine, and salvage mechanics. Salvage
carries only the explicitly re-adopted semantics; it does not inherit the
enclosing work's authority, dependencies, completion claim, or power to select
further work.

A regression or unresolved gap blocks further promotion on the affected path
until repaired, repriced, or accepted by the owning authority. It does not
globally serialize independent work. Parallel work may proceed under its own
admitted basis but cannot be laundered into the governed outcome's progress
claim.

Outcome success is necessary delivery evidence, not complete Product or release
closure.
```

Successor, `SPEC_METHOD.md#3-outcome-conservation`:

```text
## 3. Outcome conservation

Every product-outcome-bearing work wave identifies one explicitly selected,
unresolved, directly verifiable product-defined outcome and declares the
acceptance interval for that instance. Product-progress claims and
promotion onto the supported product path are judged against that same
outcome (P2; rc.2 #product-outcome-conservation-stdo-up-013; FOUNDATIONS §2
Outcome U is the generic object).

Evidence distinguishes material advance, prerequisite readiness,
preservation and regression. The four refine the progress
categories of [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)
(Progress) for a product outcome: material advance is progress there,
accepted material movement toward the selected product outcome, and only
material advance projects product progress; prerequisite readiness is
its prerequisite work, which names the product obligation it enables and
here also remains bounded; preservation is its preservation and repeated
proof, useful evidence, not progress; regression maps to evidence that
is not new progress, and this member adds one need to it: the promotion
block in the last paragraph of this section. Churn and the revision of the forecast are
ACTIVATION §5's, unchanged here.

The exact bound outcome instance stops selecting later product-progress
work when the owning authority accepts it; its witnesses remain regression
and preservation evidence. Acceptance exhausts only that instance and its
declared acceptance interval; it does not discharge an enduring guarantee,
a recurring obligation or a broader product family beyond the accepted
instance. Further work against the accepted instance is preservation, a
named bounded prerequisite for another admitted outcome, or a new change
requiring lawful repricing; it is not additional progress against the
accepted instance (EVALUATION §5).

Selecting the next unresolved outcome already defined by the product is a
goals and work-sequencing decision. Changing an outcome's meaning or scope,
or introducing a new product outcome, requires lawful re-entry at the
product (§4).

Evidence evaluates and constrains its bound product claim. Completion of a
proof surface, matrix, coverage ledger, inventory, design-method artifact,
test suite or other evidence surface cannot by itself select, enlarge or
replace the product outcome. If an assurance capability is explicitly
defined as product behaviour, delivery of that capability is judged as
product progress; its evidence still does not author the claim. The same
artifact may be product output for one claim and evidence for another only
when those roles are declared separately (P6).

Within a product-outcome-bearing work wave, material realisation growth
derives its authority from the selected unresolved product outcome, an
admitted named bounded prerequisite to it, or an admitted named bounded
experiment whose stated observation discriminates a stated decision for it.
A prerequisite or experiment authorises only its declared provisional
bound; it does not select or enlarge the product outcome, authorise
downstream work, confer promotion or closure, or waive applicable design,
safety, authority or release law, including the prime law of a design
profile where one applies.

Admission or renewal of a prerequisite or experiment belongs to the
authority owning the selected work wave, or its explicitly bounded proxy,
and is recorded in the existing durable goals or ticket authority. The
admitted basis states its provisional bound and its exhaustion or
falsification condition. Satisfaction of an experiment's stated
decision-discriminating observation exhausts that experiment. Drafting or
validating a ticket or execution contract, retaining active status, or
holding a prior admission cannot create, extend or renew the basis
(ACTIVATION §1, Admission).

Acceptance of the selected outcome, discharge of an admitted prerequisite,
or resolution of an admitted experiment's stated decision exhausts that
basis. A basis or bound also ends when another admitted terminal condition
is reached or it is rejected, withdrawn, superseded, repriced away or
falsified by evidence. Ended authority cannot be renewed by repair,
continuation, evidence, active ticket or run state, or prior admission;
further material work requires a new admission by the owning authority or
its explicitly bounded proxy (P6).

Retention as supported product behaviour, required evidence, regression
protection or bounded donor material confers no further growth authority.
Consumers own deletion, archival, quarantine and salvage mechanics. Salvage
carries only the explicitly re-adopted semantics; it inherits neither the
enclosing work's authority, dependencies or completion claim nor its power
to select further work.

A regression or unresolved gap blocks further promotion on the affected
path until repaired, repriced or accepted by the owning authority. It does
not globally serialise independent work: parallel work may proceed under
its own admitted basis and cannot be laundered into the governed outcome's
progress claim. Outcome success is necessary delivery evidence, not
complete product or release closure (§6).
```


### Row `SPEC_METHOD.md#proportional-disposition` (disposition `conserved`)

Predecessor, `SPEC_METHOD.md#proportional-disposition` at rc.2:

```text
### Proportional Disposition

Assessment returns one of these semantic dispositions:

| Disposition | Condition |
|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent |
| `re_enter` | Product, requirement, identity, lifecycle, authority, public contract, or accepted design must change |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path |

Global correctness means conserving every global relation affected by the
bounded action. It does not require proving the whole Product inside every
local action.

Repeated rejection against one unchanged boundary requires reassessment of the
frame altitude, causal cone, common components, design-versus-code placement,
and authority sufficiency. The method sets no rejection-count threshold,
mandatory review-round count, or review state machine; it prohibits repeating
an unchanged failed construction relation as if iteration alone could close it.
```

Successor, `ACTIVATION.md#disposition`:

```text
### Disposition

The decision owner disposes an assessed candidate with one of four
semantic dispositions (§1, Roles and delegation; P6, P5; provenance rc.2
SPEC_METHOD #proportional-disposition). An assessor may recommend one; the
recommendation is evidence for the decision owner, never a disposition
([EVALUATION §4](EVALUATION.md#4-review-results)). The disposition is the
acceptance result: it consumes the candidate's availability and assessment
results and stays separate from both (FOUNDATIONS §4 Results). Each maps
to the core for the predicate "the candidate is accepted at its declared
boundary":

| Disposition | Condition | Core value |
|---|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation | satisfied |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent | falsified |
| `re_enter` | the governing outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design must change | invalid_basis |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | falsified |

For `local_repair` the local defect, and for `reject` the violated relation
or the competing truth path, is the counterexample to accepting this
candidate; a repaired candidate is a new candidate with its own results.
For `re_enter` the governing basis the candidate was built and assessed on
must change, so that basis cannot support acceptance; the change re-enters
at its owning relation (§4). The core values are new; they place
acceptance in the one core, as FOUNDATIONS §4 Results requires, so that a
consumer combining results cannot take availability or assessment as
acceptance (P6).

Global correctness means conserving every global relation affected by the
bounded action; it does not require proving the whole product inside every
local action (P4b). Repeated rejection against one unchanged boundary
requires reassessment of the frame altitude, the causal cone, the common
components, the design-versus-code placement and the authority
sufficiency. The method sets no rejection-count threshold, mandatory
review-round count or review state machine; it prohibits repeating an
unchanged failed construction relation as if iteration alone could close
it (P2).
```
