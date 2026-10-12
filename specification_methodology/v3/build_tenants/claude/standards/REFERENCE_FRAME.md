# REFERENCE_FRAME

Tier 1. Owns the reference frame as a first-class object: what a frame is
and the laws every frame obeys, how a frame set is declared and selected,
how frames relate and act together, how coverage of a workspace is audited
and bounded, how a frame set is revised, and what an actor receives when it
is activated on a frame. Consumes the definitions of
[FOUNDATIONS §2](FOUNDATIONS.md) (frame objects, authority kinds,
disjointness and independence, the frame tuple) and adds none. The bounded
step that activates one frame, and the result algebra, are
[ACTIVATION](ACTIVATION.md); qualification of a frame and of this method is
[EVALUATION §7](EVALUATION.md). Every clause names the principle that
requires it (P0 to P6, FOUNDATIONS §3). A route written `rc.2 #anchor` is
into `stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md` and
is provenance only; nothing here depends on that cut to be applied.

## 1. The frame as the engagement unit

An actor, human or computational, has finite context, attention, time and
capability. A workspace may hold more material truth, history, topology,
authority and evidence than one actor can evaluate at once. This member
makes that limit explicit (P0; rc.2 #canonical-compression):

```text
declared evaluation family
  + exact workspace and topology basis
  + finite material relations and coordinates
  + applicable invariants and authorities
  + admissible evidence and exclusions
  + actor capability envelope
  = activated reference frame
  -> one member of the result algebra of ACTIVATION §3
```

A project engages a body of work through a declared frame set (P6, P2):

```text
workspace and governed outcome
  + accumulated practice and historical failures
  + available actor capabilities
  + human judgment
  -> declared frame set
  -> bounded evaluations
  -> conjunction or translation where required
  -> coverage ledger and residual uncertainty
  -> empirical frame-set revision
```

The reference frame is the atomic engagement unit: the unit that is
activated and evaluated as one bounded context. Frame-set selection,
activation, evaluation, conjunction, translation, coverage and revision are
separate functions over it (§5). A frame supports a bounded evaluation
without first containing a universal theory of its possible relationships.
"Atomic" is said at engagement altitude only. It does not assert that every
relation inside the frame is one irreducible semantic atom; a frame may
carry several semantic atoms and several owner relations without merging
their meaning or authority (P1, P3).

Scope. This member governs how finite actors construct and use bounded
reasoning or execution contexts over a changing body of work. It applies to
human work, agentic work, deterministic evaluation, probabilistic
construction, assurance and mixed work wherever the governing product or
method permits them. It is engagement law only: it defines no application
profile, role mapping, product-owned frame-basis binding, domain product,
specification taxonomy, design ontology, runtime, workflow, adoption
relation or assurance implementation. Other members and products import or
specialise its relations under their own authority, and that external
relation neither enters nor amends this member (P2: an obligation stops
where its purpose stops). This member owns the reference-frame-evaluation
bounded context, `urn:stdo:bounded-context:reference-frame-evaluation`,
under its exact publication basis, and owns only its own concepts: frame
declaration, activation, evaluation, basis, relation, result, coverage,
revision and qualification. A same-spelled profile, product, role or
runtime carrier is not imported by proximity or nominal match (P3, P1;
rc.2 #position).

Statement of ownership, new in this corpus. The reference-frame-evaluation
context explicitly includes, as concepts of that context owned at their
defining loci, the frame objects of
[FOUNDATIONS §2](FOUNDATIONS.md#frame-objects), the frame tuple included,
and the result algebra of [ACTIVATION §3](ACTIVATION.md#3-result-algebra),
its refinements and dispositions included. Where the list above names
evaluation or result, it names these included concepts and defines neither
a second time. This inclusion is the explicit owner relation that
[PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)
requires for a concept of this context defined in another member (P1, P3).

Substrate. A reference frame may be represented in prose, structured data,
a prompt, a design asset, a typed carrier, a runtime context or any other
form its consumer selects. No class, aggregate, actor, controller, service,
registry, graph or frame engine is required (P2; RF-016).

## 2. Core claims

Ten claims that the laws of §3 make precise (rc.2 #core-claims):

1. No finite actor is presumed to hold the complete material workspace in
   active attention (P0).
2. A useful frame is finite and sufficient for a declared evaluation family
   (P0, P2).
3. The evaluations to be made determine the material attention surface
   (P2).
4. Human authority may declare a practical project frame set from
   accumulated practice without deriving a unique frame partition
   mechanically (P6).
5. Frames may overlap, compose, refine, restrict, translate or succeed one
   another; hierarchy is one optional relation among these (P3).
6. Several frames may be used together without composing their internal
   coordinate systems (P4a).
7. Coverage is relative to a declared workspace, governed outcome,
   evaluation inventory, basis and time (P3, P6).
8. A frame selection or a frame result acquires no semantic, operation or
   decision authority from its breadth, usefulness, actor or
   implementation technology (P6).
9. Unknown and out-of-frame results are lawful pressure for
   reconfiguration; they are neither failed evaluations nor implied
   acceptance (P5).
10. Historical failures, resets and invisible violations are evidence for
    improving a frame declaration, an activation, an actor assignment or a
    frame set (P4b, P6).

## 3. Laws

Every frame, declared or activated, obeys the following. The objects named
are defined in FOUNDATIONS §2.

### RF-001 Evaluation relativity

Every frame declares the evaluation family it supports. A frame with no
declared evaluation family has no testable sufficiency boundary (P2; rc.2
#rf-001-evaluation-relativity).

### RF-002 Finite attention

An activated frame contains a finite attention surface that fits the
selected actor's declared capability envelope. A frame that needs
undeclared ambient memory, conversation history or an effectively global
workspace context is not reconstructable for that actor (P0; rc.2
#rf-002-finite-attention). ACTIVATION §2 measures the fit where the
contract selects measurement.

### RF-003 Material sufficiency

Every known relation whose lawful change can alter the evaluation result,
the validity of the basis, the sufficiency of evidence, operation authority
or decision authority appears in the frame or enters through a declared
authoritative input. Omitting a material relation makes the frame
insufficient. The law does not require proving that no undiscovered
material relation exists (P2; P0 with the open-world premise; rc.2
#rf-003-material-sufficiency).

### RF-004 Irrelevance exclusion

Relations that cannot affect the declared evaluation stay outside active
attention unless they are needed to establish that irrelevance. A frame
does not expand because adjacent workspace material exists (P2; rc.2
#rf-004-irrelevance-exclusion).

### RF-005 Exact basis and coordinates

Every result binds its exact subject, basis, coordinates and evidence
scope. A stale, advanced, ambiguous or mismatched basis returns
`invalid_basis` or requires reactivation. Apparent equality never
substitutes for declared coordinate equality (P3, P1; rc.2
#rf-005-exact-basis-and-coordinates).

### RF-006 Authority conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer or reconstruct semantic, evaluation, operation or decision
authority from actor identity, available capability, evidence shape,
implementation reachability or frame selection (P6; rc.2
#rf-006-authority-conservation).

### RF-007 Semantic, evidence and verdict separation

Semantic law defines what the evaluation means. Evidence supplies
observations. The evaluator applies the declared relation. Where the
evaluation performs a material operation, the existing operation owner
supplies the exact grant. Decision authority disposes the result. A frame
declaration keeps these roles distinguishable even when one actor lawfully
performs several of them (P6; rc.2
#rf-007-semantic-evidence-and-verdict-separation). EVALUATION §2 applies
this law to review.

### RF-008 Overlap without identity collapse

Frames may share entities, variables, evidence or coordinates. Shared
material establishes neither identical meaning nor identical basis,
authority or result. Every cross-frame equality or translation an
evaluation uses is declared where it is used (P1, P3; rc.2
#rf-008-overlap-without-identity-collapse).

### RF-009 No assumed hierarchy

Frames may relate through disjointness, overlap, refinement, restriction,
translation, temporal succession, composition or governance (§7). Parent
and child relations apply only where explicitly declared. Functional
decomposition, authority precedence, frame configuration, subject topology
and evaluation dependency are distinct relation structures; a consumer may
align them where the governed subject warrants it and may not silently
treat them as one hierarchy (P3, P1; rc.2 #rf-009-no-assumed-hierarchy).

### RF-010 Composition on demand

Using several frames does not require composing their internal manifolds.
Composition law is required only when the governing evaluation combines
their internal variables, transports evidence or values across them, or
treats their operations as one material execution relation. Independently
activated evaluations may instead return closed results to one declared
conjunction or decision rule (P4a; §6; rc.2
#rf-010-composition-on-demand).

### RF-011 Topology mutation and recharting

An activated frame declares the topology changes capable of invalidating
its coordinates or its materiality judgment. A detected material topology
mutation causes reevaluation, frame revision or recharting before the
previous result is reused. Material revision of the frame itself
invalidates for reuse every result bound to the prior revision coordinate;
§10 Revision actions states that rule (P3, P4b; rc.2
#rf-011-topology-mutation-and-recharting).

### RF-012 Closed results

Every evaluation returns a member of its declared result algebra. A
performed evaluation returns a member; an evaluation not performed because
a declared capability was not exercised owes the step's stop state, not a
member (ACTIVATION §3, third case). The core
algebra is defined once, in ACTIVATION §3: `satisfied`, `falsified`,
`indeterminate`, `out_of_frame` and `invalid_basis`, with the meanings and
the no-coercion rule given there; this member does not define it a second
time. An externally owned compatible extension may refine that algebra
while preserving explicit indeterminate, out-of-frame and invalid-basis
pressure; it may neither add a core member nor coerce one to success (P5;
rc.2 #rf-012-closed-results).

### RF-013 Reconstructable activation

A fresh competent actor inside the declared capability envelope can
reconstruct the activated evaluation from the frame declaration, the exact
subject, the basis and the admissible inputs, without undocumented
conversational or historical context (P0 with the actor-change premise;
rc.2 #rf-013-reconstructable-activation).

### RF-014 Capability fit

Frame adequacy includes actor usability. When the material manifold
exceeds an actor's capability envelope, human authority may select
another actor, refine the frame, sequence activations or provide a lawful
compression (RF-017); the selection is human authority's, exercised
directly or in advance through the grant, and ACTIVATION §2 says which of
these a step selects itself and which re-enter the grant's owner. The
actor may not silently omit material relations to fit its context (P0, P5;
rc.2 #rf-014-capability-fit).

### RF-015 Residual uncertainty

Coverage and evaluation results retain known uncertainty. Unresolved
relations, uncovered evaluations, contested evidence and unknown capability
stay explicit. Absence of a recorded counterexample is not evidence of
universal completeness (P4b, P6; open-world premise; rc.2
#rf-015-residual-uncertainty).

### RF-016 Implementation neutrality

This member requires the declared relations and the observable outcomes.
It requires no frame runtime, universal carrier, registry, controller,
prompt format, repository layout, collaboration topology, worker count or
software framework (P2; rc.2 #rf-016-implementation-neutrality).

### RF-017 Proportional compression

A frame compresses accumulated practice when its declaration preserves the
material distinctions and failure detections its evaluation family requires
while fitting its capability envelope. Compression does not require a
unique smallest frame. Intentional overlap is retained where it supplies
independently activated evaluation, different capability fit, different
evidence altitude or useful fault detection. Frames are merged only when
the merged frame preserves evaluation meaning, authority, capability fit
and proportional reasoning cost (P2, P0; rc.2
#rf-017-proportional-compression).

### Engagement atom and semantic atom

A reference frame is atomic at engagement altitude: it is activated and
evaluated as one bounded attention unit. Semantic irreducibility is a
separate question: one frame may contain several semantic atoms, and one
semantic atom may take part in several frames (P1, P3). Where an adopting
method supplies a semantic-contraction law for its domain atoms, that law
governs the domain atom family. Frame-set contraction asks a different
question: whether two frame declarations support the same evaluation
relation without material difference in evidence, authority, capability
fit, evaluation or assurance independence, or failure detection. A frame
set is not contracted to a disjoint minimum because its material variables
overlap (P2; RF-017; rc.2 #engagement-atom-and-semantic-prime).

## 4. Frame-set declaration

Human authority may declare an initial project frame set from accumulated
development practice, known failure modes, domain expertise, the governed
outcome's risk and knowledge of the available agents and other actors. The
declaration need not reconstruct the set from the workspace bottom up (P6,
P2; rc.2 #human-frame-set-declaration). It records:

- the governed workspace and outcome;
- the known evaluation inventory;
- the selected frames and their capability envelopes;
- intentional overlaps and separately activated checks;
- known frame dependencies or translations;
- semantic, evaluation, operation where material, decision and acceptance
  authority;
- known exclusions and residual uncertainty; and
- the conditions for revision.

Human selection is a lawful source of method structure. It proves neither
that the selected set is complete nor that the frames hold authority over
the subject relations they inspect (P6; RF-006, RF-015).

### Frame-set selection

Frame-set selection is a constrained coverage problem. For the known
material evaluations E(W, G) of workspace W and governed outcome G, a
selected frame set S meets the baseline coverage constraint when, for every
evaluation e in E(W, G), there is a frame F in S and an available actor a
inside F's capability envelope K_F such that F with a is capable of e (P2,
P0; rc.2 #frame-set-optimization). Selection also weighs actor context and
competence; evaluation risk and consequence; acquisition and reasoning
cost; evidence availability; useful independently activated overlap;
translation and reconciliation cost; historical blind spots; and
reversibility when the set proves inadequate. No optimisation algorithm is
prescribed. Human authority may accept a non-minimal set where its added
cost buys material risk reduction or better actor fit (P2, P6).

These considerations create no universal resource ledger, benchmark, budget
or measurement gate. A resource control applies only through an explicitly
selected frame and its owning applicability and work scope; ACTIVATION §6
is that selection where capability fit or a cost claim is the governed
question. Frame selection cannot waive another applicable semantic,
authority, evidence or independence constraint (P2, P6).

## 5. Method functions

The frame and the functions over it remain distinct. An application may
realise the following relations in any conforming form; the signatures
describe relations, not callable software interfaces (P2; RF-016; rc.2
#method-functions):

```text
declare(human_authority, workspace, outcome, practices, capabilities)
  -> frame_set

activate(frame, evaluation, subject, basis, actor)
  -> activated_frame | activation_refusal

evaluate(activated_frame, admissible_evidence)
  -> result + evidence + residuals

conjoin(decision_rule, frame_results)
  -> decision | conflict | indeterminate

translate(source_frame, target_frame, value_or_evidence, mapping)
  -> translated_value | declared_loss | refusal

audit_coverage(workspace, outcome, evaluation_inventory, frame_set)
  -> coverage_ledger

revise(frame_set, new_evidence, failures, capability_change, topology_change)
  -> proposed_frame_set_delta
```

`declare` is §4; `activate`, `evaluate` and the closed result are
ACTIVATION §1 to §3 and §7; `conjoin` and `translate` are §6;
`audit_coverage` is §8; `revise` is §10. EVALUATION §7 qualifies each.

## 6. Frames in conjunction

Frames act together through four distinct relations, and only where the
evaluation requires one (P4a; RF-010; rc.2 #using-frames-in-conjunction).

### Independently activated co-evaluation

Several frames may evaluate the same subject through separate activations
and return closed results. They may overlap in subject, manifold or
evidence sources; neither evaluation consumes or influences the other's
unclosed working result. This serves assurance independence, different
evidence altitudes and distinct failure perspectives (P6; FOUNDATIONS §2,
evaluation independence; rc.2 #independently-activated-co-evaluation).

### Result conjunction

A declared decision rule consumes closed frame results. The rule states
which results are mandatory; how conflict and indeterminacy are handled;
which basis relations must agree; which decision authority owns the
conjunction; and whether any result may veto or defer the decision.
Conjunction does not transfer the semantic authority of a contributing
frame (P6, P4a). Every mandatory constraint is satisfied with valid
applicable evidence. Common agreement cannot discard a constraint or a
material counterexample that only one contributor found. A missing,
wrong-subject, conflicted or indeterminate mandatory result stays
unresolved under the declared rule; aggregate green status cannot replace
it (P4b, P5; FOUNDATIONS §4 conservation accounting; rc.2
#result-conjunction).

### Evidence or coordinate translation

One frame supplies evidence or a value consumed inside another. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law and refusal conditions (P1, P4b;
rc.2 #evidence-or-coordinate-translation).

### Material composition

Several frame-governed operations form one material execution or reasoning
relation. The owning application declares the composition, the shared
invariants, the effect or decision order where material, closure, failure,
and the conservation of semantic, operation and decision authority.
Composition is introduced only when the evaluation requires it; a possible
future interaction does not require a general composition law in every
frame (P4a, P6, P2; rc.2 #material-composition).

## 7. Frame relations

Frames may relate as (rc.2 #frame-relations):

- disjoint: no material variable, coordinate, evidence or result dependency
  is shared for the declared evaluations;
- overlapping: some material variables, evidence or entities are shared;
- complementary: distinct evaluations jointly inform one decision;
- alternative: different frames can evaluate the same claim under declared
  capability or evidence conditions;
- refinement: one frame resolves a material distinction left aggregated in
  another;
- restriction: one frame evaluates a lawful subset of another frame's
  domain;
- translated: values or evidence move through a declared coordinate map;
- temporally successive: a later frame evaluates a changed basis;
- composed: several frame relations form one governed evaluation or
  action; or
- governing and subordinate: one frame inherits declared constraints from
  another where a real authority or decomposition relation exists.

No relation is the default universal frame topology. A project declares
only the relations its evaluations and coverage claims need (P3, P2;
RF-009).

## 8. Workspace coverage

### Coverage basis

Coverage is evaluated against the tuple Coverage(W, G, B, E, S, T): the
workspace W, the governed outcome G, the exact basis B, the known
evaluation inventory E, the declared frame set S and the time or immutable
checkpoint T of the claim. Changing any material member may invalidate the
coverage result (P3, P6; rc.2 #coverage-basis).

### Evaluation inventory

The coverage evaluator derives the known evaluation inventory from every
material available source, including where applicable: goals, intent,
product definition, requirements and accepted method; accepted design, its
ontology, identities, lifecycles, authorities and algorithms;
implementation capabilities and externally observable behaviour;
operational, release, security, safety and governance obligations; direct
and indirect dependencies and interaction seams; evidence, tests,
scenarios, qualification and acceptance claims; historical tickets,
check-ins, commentary, post-mortems, incidents and rejected candidates;
days-long loops, resets, repeated repairs and discovered rival paths; known
agent capability limits and prior invisible violations; and applicable
external law, contracts or standards. The inventory records provenance and
materiality. Artifact presence, file count, operation count, test count or
repository reachability proves no evaluation coverage (P2, P6; rc.2
#evaluation-inventory).

### Coverage dimensions

The audit applies cross-cutting lenses to the inventory. Typical
dimensions are outcome and capability; identity and authority; lifecycle
and temporal behaviour; topology and interaction seams; transport and
representation; evidence and proof; change, failure, recovery and
rollback; historical regression; and actor capability and context fit.
These are lenses (FOUNDATIONS §2): they become frames only when separately
instantiated as bounded evaluation families (P2; rc.2
#coverage-dimensions).

### Coverage ledger

The ledger holds at least, for each evaluation (P4b, P6; rc.2
#coverage-ledger):

| Field | Meaning |
|---|---|
| evaluation | the exact question or predicate |
| provenance | the source establishing materiality |
| subject and basis | the exact workspace coordinate |
| selected frames | the frames capable of evaluating it |
| actor envelope | the competence and context required |
| semantic authority | the owner of the evaluated meaning |
| operation authority | the existing owner grant for construction, transformation, admission, publication or mutation where the evaluation performs one; otherwise none |
| decision authority | the owner of the disposition |
| evidence | the required observations and their provenance |
| dependencies | material frame or seam relations |
| status | the coverage disposition |
| residual | uncertainty, exclusion or re-entry condition |

The baseline coverage statuses are `covered`, `separately_covered`,
`conditionally_covered`, `conflicted`, `uncovered`, `unknown` and
`excluded_by_authority`.

### Interaction coverage

Evaluation-row coverage is insufficient when two covered relations interact
in a way capable of changing the governed outcome. Every material
interaction is covered by one frame, a declared conjunction, a translation
or a material composition evaluation (P4a, P2; rc.2
#interaction-coverage).

### Authority coverage

Every material evaluation identifies semantic and decision authority.
Every material operation also identifies its existing construction,
transformation, admission, publication or mutation authority. A frame set
with broad observational reach, an unresolved decision owner or an
effectful path without operation authority is not closed (P6; rc.2
#authority-coverage).

### Failure coverage

Coverage includes known success, refusal, boundary, integration, recovery,
reconstruction and competing-path cases where they are material.
Historical failures stay first-class coverage inputs until a declared frame
detects or excludes their recurrence (P4b, P5; rc.2 #failure-coverage).

### High-risk separately activated coverage

Human authority may require independently activated frame coverage for
evaluations whose failure has high consequence, weak observability, strong
confirmation bias or a history of local proof masking. Such coverage uses a
separately activated evaluation relation and declares any additional
assurance-independence conditions. A persona label alone establishes
neither relation (P6; rc.2 #high-risk-separately-activated-coverage).

### Operational full coverage

A frame set has operational full coverage for its declared tuple when
(rc.2 #operational-full-coverage):

1. every known material evaluation is covered by at least one capable
   frame;
2. every material interaction has a declared evaluation, conjunction,
   translation or composition relation;
3. every evaluation has semantic and decision authority, and every
   material operation has its inherited operation authority;
4. every mandatory claim has an admissible evidence path and a refusal
   path;
5. the required independently activated overlaps and
   assurance-independence conditions are present;
6. no unresolved frame-result conflict is hidden by aggregation;
7. excluded evaluations cite their governing authority; and
8. uncovered and unknown residuals are explicit and compatible with the
   claim.

Operational full coverage is relative to its tuple. It is not a claim that
no undiscovered evaluation exists (P6; P0 with the open-world premise).

## 9. Completeness boundary

Without an independently established closed-domain completeness predicate,
a finite frame set cannot establish the absence of every undiscovered
material evaluation by inspecting its own declared inventory. A finite,
formally closed domain may support exhaustive coverage relative to that
domain and its completeness predicate; the result does not generalise
beyond that boundary. Formal incompleteness results motivate this caution;
they do not by themselves prove that a particular workspace or frame set is
incomplete (P0 with the open-world premise; P6; rc.2
#completeness-boundary).

Coverage therefore stays falsifiable and externally challengeable.
Challenge sources include human knowledge outside the current frame set;
independent review; historical failures and predecessor systems; mutation,
adversarial and counterexample search; live operation and user behaviour;
adjacent workspace or domain comparison; and changes in actor capability,
law, dependencies or topology. The method requires an explicit residual
boundary and never a claim of metaphysical or universal completeness
(RF-015).

## 10. Discovery and revision

### Missing-frame signals

These observations trigger frame diagnosis (P4b, P5; rc.2
#missing-frame-signals):

- a competent actor repeatedly cannot see a known material violation;
- a local repair creates or duplicates another authority path;
- work repeatedly resets after apparently valid local completion;
- long implementation loops produce no stable closure;
- proof passes while the claimed outcome stays unbound;
- a material failure is visible only after broad integration;
- reviewers repeatedly expand context without reaching a decidable
  question;
- two actors use the same frame name but evaluate different material
  relations; or
- a topology mutation leaves prior verdicts apparently current.

### Diagnostic order

Diagnosis asks, in this order (P2; rc.2 #diagnostic-order):

1. Was the correct declared frame activated?
2. Were the subject and basis exact?
3. Was the actor inside the capability envelope?
4. Was admissible evidence available?
5. Is a material variable or invariant missing from the frame?
6. Is a required conjunction or translation missing?
7. Is the evaluation family itself wrong or incomplete?
8. Is another frame required?

Question 1 is answered by family inclusion, not by set membership. An
evaluation is within a frame's family when the question it decides is one
the frame's declared evaluation family states, at the frame's declared
coordinates (RF-001). Membership of the frame in the frame set, the frame's
name, a role label or similar wording of the question does not place an
evaluation in the frame's family; an activation of a frame on an evaluation
outside its family answers question 1 no, whatever the frame's standing in
the set. The test is a tightening the predecessor implies and does not
state (P2, the evaluations determine the attention surface; P1, a name
carries no meaning; the material relation drawn is evaluation-to-family
inclusion; rc.2 #diagnostic-order, #evaluation, where similar wording
proves no shared family, #rf-001-evaluation-relativity and
#applicability-and-required-results, where a frame name or listed family is
no activation trigger by itself).

The order prevents every difficult evaluation from creating another frame.

### Revision actions

A revision may (P4b; rc.2 #revision-actions): clarify activation or
evidence acquisition; change the capability envelope; add or remove a
material relation; split an overloaded frame; merge duplicative frames
where capability and authority stay sound; add intentional overlap; add or
revise a conjunction or translation; retire a frame whose evaluation family
is no longer material; or revise the project evaluation inventory. Every
material revision changes frame identity or revision coordinates and states
which prior activations, results and coverage claims require reevaluation
(P3, P4b).

Stated plainly: a material revision of a frame produces a new frame
revision coordinate. Every prior closed result bound to the previous
revision of a materially revised frame is bound to a mismatched coordinate
(RF-005) and is invalidated for reuse until it is re-checked against the
new revision (RF-011; ACTIVATION §7). The revision record lists those
results as reopened; a result leaves that list only by a recorded re-check
that finds it demonstrably independent of the change, or by re-evaluation
on the new revision. A material revision does not select which of the
results bound to the prior revision it reopens, and silence does not keep
a result closed. A non-material revision, for example one that clarifies an
activation or acquires evidence without changing any declaration, produces
no new coordinate and reopens no result; the revision record states that
the revision is non-material. This restates what RF-005, RF-011 and the sentence
above carry in combination (P3, P4b; rc.2 #revision-actions,
#rf-005-exact-basis-and-coordinates, #return-a-closed-result, whose
demonstrably independent surviving results are the re-check's one
survival route).

## 11. The activation packet

An actor receives one activated frame or one declared active frame
configuration, never an implied demand to reconstruct the complete
workspace from ambient context (P0; rc.2 #agentic-use). The minimum
activation packet contains:

- frame identity and revision;
- the evaluation and its result algebra;
- the exact subject and basis;
- the material relations and applicable invariants;
- semantic, evaluation, operation where material, and decision authority;
- admissible evidence and tools;
- the capability and context envelope;
- exclusions and prohibited assumptions;
- declared frame dependencies or conjunction outputs; and
- invalidation, stop and reconfiguration conditions.

The actor may own its internal reasoning and search where the governing
method permits. It returns through the declared result relation. Hidden
internal reasoning is no substitute for required evidence, provenance or
authority (P6). Frame size is optimised for reliable evaluation, not for
maximum context loading: a more capable actor may activate a broader frame
and a less capable one may use a lawful refinement sequence, and both
preserve the same material invariants and authority relations (P0, P2;
RF-014).

### Minimal activation binding

The following carrier-neutral content is sufficient to bind one declared
frame for one evaluation. It may be written in Markdown, structured data, a
prompt or another consumer-selected carrier without changing the relation
(P0, RF-016; rc.2 #minimal-frame-activation-binding).

```markdown
# Reference-Frame Activation: <stable activation identity>

## Frame
- declaration identity and revision:
- exact evaluation and closed result algebra:

## Subject And Basis
- exact subject or candidate identity:
- workspace, authority, dependency, configuration, and time basis:

## Attention Surface
- material relations and applicable invariants:
- exact source and semantic references:
- explicit exclusions and prohibited assumptions:

## Actor And Authority
- actor and capability envelope:
- semantic and evaluation authority:
- operation authority, subject, and territory where material:
- decision, acceptance, and publication authority:

## Evidence And Relations
- admissible evidence and acquisition route:
- dependency, overlap, input, conjunction, or translation relations used:
- expected result consumer and return relation:

## Stop And Change
- invalidation conditions:
- stop, residual, re-entry, and reconfiguration conditions:
```

Every field resolves through stable identities and source references.
Paths, line numbers, member counts, summaries and matching labels may aid
navigation or diagnostics; they do not substitute for the declared identity
and basis (P3).

## 12. Violations

Each of the following is a violation of this member where it supports a
frame or coverage claim (rc.2 #anti-patterns):

1. one omniscient frame is presumed to contain the complete method or
   workspace (P0);
2. a module, file, service, role, persona, prompt or lens is called a
   frame without a declared evaluation relation (RF-001);
3. functional decomposition, authority hierarchy and frame topology are
   silently treated as one tree (RF-009);
4. every active frame is required to compose with every other frame
   (RF-010);
5. composition machinery is introduced without a material cross-frame
   evaluation (RF-010);
6. frame selection or broad visibility is treated as semantic authority
   (RF-006);
7. evidence is flattened across bases or coordinates and treated as one
   executed or observed relation (RF-005, RF-008);
8. `satisfied` is returned where the lawful result is `indeterminate`,
   `out_of_frame` or `invalid_basis` (RF-012);
9. coverage is inferred from artifact, file, operation, test, review or
   actor count (§8);
10. a frame silently grows beyond the selected actor's capability envelope
    (RF-002, RF-014);
11. a topology mutation reuses a stale activation without recharting
    (RF-011);
12. every failure creates another frame before activation, basis,
    evidence, capability and evaluation defects are excluded (§10);
13. intentional overlap is contracted although it supplies independently
    activated failure detection or materially different capability fit
    (RF-017); or
14. a generic runtime, registry, controller or universal carrier is
    presented as required by this member (RF-016).

## 13. Minimal declarations

The three carrier-neutral shapes below are the least content that declares
a frame, a frame set and an evaluation result. Each is sufficient as
written in Markdown or any other consumer-selected carrier (P0, P2;
RF-016).

### Minimal frame declaration

(rc.2 #minimal-frame-declaration)

```markdown
# Frame: <stable local identity>

## Evaluation Family
<questions, predicates, and closed result algebra>

## Subject And Basis
<workspace boundary, exact identity, version/time/topology coordinates>

## Material Manifold
<entities, variables, relations, states, and interactions>

## Coordinates And Equality
<how positions are distinguished and related>

## Invariants
<applicable governing laws>

## Authorities
<frame-set, semantic, evaluation, operation where material, and decision authority>

## Evidence
<admissible sources, provenance, and exclusions>

## Capability Envelope
<competence, context, access, tools, evaluation/assurance independence, configuration>

## Boundary And Exclusions
<irrelevant material, prohibited assumptions, and out-of-frame conditions>

## Optional Frame Relations
<inputs, outputs, overlaps, conjunctions, or translations actually used>

## Invalidation And Recharting
<changes that stale this frame or its results>

## Qualification
<representative cases, counterexamples, and known residuals>
```

### Minimal frame-set declaration

(rc.2 #minimal-frame-set-declaration)

```markdown
# Frame Set: <stable local identity>

## Governed Workspace And Outcome
<workspace, outcome, basis, and time>

## Human Authority
<declaration and acceptance authority>

## Evaluation Inventory
<known material evaluations and provenance>

## Selected Frames
<frame identities, revisions, and capability envelopes>

## Coverage Rationale
<mapping from evaluations to capable frames>

## Intentional Overlap
<separately activated checks, assurance-independence conditions, or alternative capability fit>

## Conjunction And Translation
<only the cross-frame relations required by evaluations>

## Residual Uncertainty
<uncovered, unknown, conditional, or excluded evaluations>

## Revision Triggers
<history, topology, capability, evidence, or outcome changes>
```

### Minimal evaluation result

(rc.2 #minimal-evaluation-result)

```markdown
# Frame Evaluation Result

- frame identity and revision:
- activation identity:
- evaluation:
- subject and basis:
- actor and capability envelope:
- semantic, evaluation, operation where material, and decision authority:
- admissible evidence:
- result:
- inference relation:
- residual uncertainty:
- invalidation conditions:
- consuming decision or conjunction:
```

## 14. Closure

A project operates under this member when (rc.2 #closure):

1. human authority has declared the governed workspace, outcome,
   evaluation inventory and frame set (§4);
2. every active frame is finite, evaluation-bound, basis-bound,
   authority-safe and usable inside its actor capability envelope (§3);
3. frame results preserve semantic, evidence, inference and decision
   distinctions (RF-007);
4. cross-frame conjunction, translation or composition exists only where a
   material evaluation requires it (§6);
5. workspace coverage maps every known material evaluation and interaction
   to a capable frame or an explicit residual (§8);
6. operational full coverage is stated relative to its exact tuple (§8);
7. topology, capability, evidence and historical failures can trigger
   frame revision or recharting (§10); and
8. no executable frame machinery, global context, universal completeness
   or domain authority is inferred from adopting this member (RF-016, §9).

## 15. Source dispositions

RF rows received by this member. Rows that land in FOUNDATIONS, ACTIVATION
or EVALUATION are listed in those members. Anchors are into rc.2
REFERENCE_FRAME_METHOD.md; a locus is a section of this file.

| Anchor | Disposition | Locus |
|---|---|---|
| #canonical-compression | conserved | §1 |
| #position | conserved | §1 (scope, substrate); the bounded-context identity is carried unchanged |
| #core-claims | conserved | §2 |
| #reference-frame-laws | not applicable: heading with no claim text (24 bytes); its children are disposed individually | §3 |
| #rf-001-evaluation-relativity | conserved | §3 RF-001 |
| #rf-002-finite-attention | conserved | §3 RF-002; measurement of fit in ACTIVATION §2 |
| #rf-003-material-sufficiency | conserved | §3 RF-003 |
| #rf-004-irrelevance-exclusion | conserved | §3 RF-004 |
| #rf-005-exact-basis-and-coordinates | conserved | §3 RF-005 |
| #rf-006-authority-conservation | conserved | §3 RF-006 |
| #rf-007-semantic-evidence-and-verdict-separation | conserved | §3 RF-007; applied to review in EVALUATION §2 |
| #rf-008-overlap-without-identity-collapse | conserved | §3 RF-008 |
| #rf-009-no-assumed-hierarchy | conserved | §3 RF-009 |
| #rf-010-composition-on-demand | conserved | §3 RF-010; §6 |
| #rf-011-topology-mutation-and-recharting | conserved | §3 RF-011 |
| #rf-012-closed-results | conserved; the tenant text carries a labelled tightening: unexercised capability owes stop state | §3 RF-012; the algebra itself is defined once in ACTIVATION §3 |
| #rf-013-reconstructable-activation | conserved | §3 RF-013 |
| #rf-014-capability-fit | conserved | §3 RF-014; the step's own selection among fit options is ACTIVATION §2 |
| #rf-015-residual-uncertainty | conserved | §3 RF-015 |
| #rf-016-implementation-neutrality | conserved | §3 RF-016 |
| #rf-017-proportional-compression | conserved | §3 RF-017 |
| #engagement-atom-and-semantic-prime | conserved; the predecessor's "Prime or equivalent" is generalised to any semantic-contraction law an adopting method supplies (the design profile's prime law is one such; tier 1 names no profile term) | §3 Engagement atom and semantic atom |
| #human-frame-set-declaration | conserved | §4 |
| #frame-set-optimization | conserved | §4 Frame-set selection |
| #method-functions | conserved | §5 |
| #using-frames-in-conjunction | conserved | §6 |
| #independently-activated-co-evaluation | conserved | §6 |
| #result-conjunction | conserved | §6 |
| #evidence-or-coordinate-translation | conserved | §6 |
| #material-composition | conserved | §6 |
| #frame-relations | conserved | §7 |
| #workspace-coverage | not applicable: heading with no claim text (22 bytes); its children are disposed individually | §8 |
| #coverage-basis | conserved | §8 |
| #evaluation-inventory | conserved; "Ontology" written as the design's ontology | §8 |
| #coverage-dimensions | conserved | §8 |
| #coverage-ledger | conserved | §8 |
| #interaction-coverage | conserved | §8 |
| #authority-coverage | conserved | §8 |
| #failure-coverage | conserved | §8 |
| #high-risk-separately-activated-coverage | conserved | §8 |
| #operational-full-coverage | conserved | §8 |
| #completeness-boundary | conserved | §9 |
| #discovery-and-revision | not applicable: heading with no claim text (26 bytes); its children are disposed individually | §10 |
| #missing-frame-signals | conserved | §10 |
| #diagnostic-order | conserved; the tenant text carries a labelled tightening: family inclusion, not membership | §10 |
| #revision-actions | conserved; the tenant text carries a labelled tightening: prior results reopen by default | §10 |
| #agentic-use | conserved | §11 |
| #minimal-frame-activation-binding | conserved | §11 |
| #worked-binding-product-chain-drift-evaluation | not applicable: a non-normative worked example by its own statement; it carries no determination beyond the binding of §11, which is conserved; its subject (product-chain drift) is tier-2 matter, and a worked binding for the successor is produced by a qualification case against the tier-2 member that owns the subject | none |
| #anti-patterns | conserved | §12 |
| #minimal-frame-declaration | conserved | §13 |
| #minimal-frame-set-declaration | conserved | §13 |
| #minimal-evaluation-result | conserved | §13 |
| #closure | conserved | §14 |
