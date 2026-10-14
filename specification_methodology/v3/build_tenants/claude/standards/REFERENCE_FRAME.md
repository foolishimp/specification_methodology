# REFERENCE_FRAME

Tier 1. Owns the reference frame as a first-class object of engagement:
the laws every frame obeys, how a frame set is declared and selected, how
frames relate and act together, how coverage of a workspace is audited and
bounded, how a frame set is revised, and what an actor receives when it is
activated on a frame. The frame objects, the step that activates a frame,
the core result algebra with its conjunction, and qualification belong to
other members; this member imports them unchanged and defines none of them
(§1, Imports into this context). Each clause names the principle that
requires it (P0 to P6, FOUNDATIONS §3), as FOUNDATIONS §1 requires. A route
written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md` and is
provenance only; nothing here depends on that cut to be applied.

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
  -> one closed result in the core algebra of FOUNDATIONS §4 Results
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
relation or assurance implementation. Other members and products may import or
specialise its relations under their own authority, and that external
relation neither enters nor amends this member (P2: an obligation stops
where its purpose stops). This member owns the reference-frame-evaluation
bounded context, `urn:stdo:bounded-context:reference-frame-evaluation`,
under its exact publication basis. This member owns only its frame
declaration, activation, evaluation, basis, relation, result, coverage,
revision and qualification concepts. The context also holds the concepts
imported below, each kept by its owner. A same-spelled profile, product,
role or runtime carrier is not imported by proximity or nominal match (P3,
P1; rc.2 #position).

Substrate. A reference frame may be represented in prose, structured data,
a prompt, a design asset, a typed carrier, a runtime context or any other
form its consumer selects. No class, aggregate, actor, controller, service,
registry, graph or frame engine is required (P2; RF-016).

### Imports into this context

This member imports the concepts below into
`urn:stdo:bounded-context:reference-frame-evaluation` under the import rule
of [FOUNDATIONS §2](FOUNDATIONS.md#imports-between-members). Source and
target meanings are identical owner-qualified references, not new local
definitions. Direction is from the named source to this context; loss is
none and no translation or ownership transfer is asserted. FOUNDATIONS,
ACTIVATION and EVALUATION declare no bounded-context identity, so each
row's source context is its member; the target context and its owner are
declared in Scope above (P1, P3).

| Referenced concept | Source context | Exact source concept and owner |
|---|---|---|
| evaluation, evaluation family, workspace, material-relation manifold, coordinate, topology, capability envelope, reference frame, activated frame, frame set, active frame configuration, lens; role, persona, abstraction and component | FOUNDATIONS | [Frame objects](FOUNDATIONS.md#frame-objects), FOUNDATIONS §2 |
| subject, outcome, basis, material relation, evidence, actor, claim, judgment, residual | FOUNDATIONS | [Ontology](FOUNDATIONS.md#2-ontology), FOUNDATIONS §2 |
| frame-set, semantic, evaluation, operation and decision authority; actor identity | FOUNDATIONS | [Authority kinds](FOUNDATIONS.md#authority-kinds), FOUNDATIONS §2 |
| frame disjointness, evaluation independence and assurance independence | FOUNDATIONS | [Disjointness and independence](FOUNDATIONS.md#disjointness-and-independence), FOUNDATIONS §2 |
| the frame tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩ | FOUNDATIONS | [The frame tuple](FOUNDATIONS.md#the-frame-tuple), FOUNDATIONS §2 |
| the core result values, their meanings and standing, the evaluation not performed, and refinements of the core | FOUNDATIONS | [Results](FOUNDATIONS.md#results), FOUNDATIONS §4 |
| conjunction and composition of results, with the declared decision rule | FOUNDATIONS | [Conjunction of results](FOUNDATIONS.md#conjunction-of-results), FOUNDATIONS §4 |
| activation as a step: intake, admission, applicability, context construction with its size measurement, activation and evaluation | ACTIVATION | [The step](ACTIVATION.md#1-the-step), ACTIVATION §1; [Context construction under an envelope](ACTIVATION.md#2-context-construction-under-an-envelope), ACTIVATION §2 |
| the step's result refinements and disposition | ACTIVATION | [Step results and disposition](ACTIVATION.md#3-step-results-and-disposition), ACTIVATION §3 |
| the closed result and its reuse | ACTIVATION | [Closed result and reuse](ACTIVATION.md#7-closed-result-and-reuse), ACTIVATION §7 |
| qualification of a frame and of this method | EVALUATION | [Qualification of frames and of the method](EVALUATION.md#7-qualification-of-frames-and-of-the-method), EVALUATION §7 |

These are reference-only imports into
`urn:stdo:bounded-context:reference-frame-evaluation`. They provide no
semantic, evaluation, operation or decision authority. Scope bounds what
this member owns; a concept of those kinds that another member defines,
such as evaluation, basis, the activation step, the core results or
qualification, is imported here, and this member defines it no second
time. A refinement this member states, such as the function outcomes of §5
or the coverage statuses of §8, names its owner in this table and maps
back to it. A frame or frame family that a profile or product declares in
this context is that owner's specialisation under Scope above and is not
imported here (P1, P3, P6).
The declaration is new in this corpus. Purpose and material relation: each
concept used here keeps one owning section, so its meaning cannot diverge
between that owner and this member (P1, P6).

### Foundation to law

This family, frames and context (F1 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law)),
decides how a finite actor engages a body of work through bounded reference
frames: how a frame is declared, sized, bound, activated, related to other
frames, used to audit coverage and revised. It covers this member; the
context construction of
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope);
and the frame objects, authority kinds, disjointness and independence and
frame tuple of [FOUNDATIONS §2](FOUNDATIONS.md#frame-objects). A rule in
another member is marked "outside this member" in the third column; the
table owns none of the rules it names. Its instance premises are: (a) a
workspace holds more material than one actor's capability envelope (its
competence, context capacity, tools and access) can evaluate at once; (b)
the evaluations to be made are declared questions about a governed
outcome; (c) several frames and actors may bear on one workspace, and their
material may overlap; (d) the workspace, its topology and the actors'
capabilities change between activations; (e) an actor may read both owning
sources and surfaces derived from them by copying, projection or
compression. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. Two of P0's
premises are cited by name: its actor-change premise, that the actor of one
step need not be the actor of the next and may re-acquire declared sources
but not private memory; and its open-world premise, that the world is open.
The standing of the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P0 (recovered); instance premise a | By P0 an actor's attention is finite, and by (a) the workspace exceeds it, so no finite actor is presumed to hold the complete workspace in active attention. The unit of engagement is one activated reference frame, activated and evaluated as one bounded context; frame-set selection, activation, evaluation, conjunction, translation, coverage and revision are separate functions over it | [§1](#1-the-frame-as-the-engagement-unit), the two compressions and the engagement unit; [§2](#2-core-claims) claim 1; [§12](#12-violations) item 1 | none | 7 |
| P1 (independent), P3 (independent), P2 (independent); instance premise c | By P1 and P3 meaning and authority stay with their owners however material is grouped, and by P2 frames are chosen for the evaluation, so a frame is atomic at engagement altitude only: it may carry several semantic atoms and owner relations without merging their meaning or authority, and one semantic atom may take part in several frames. A frame set is not contracted to a disjoint minimum because its material variables overlap | [§1](#1-the-frame-as-the-engagement-unit), "Atomic"; [Engagement atom and semantic atom](#engagement-atom-and-semantic-atom) | a semantic-contraction law for a domain's atoms: the adopting method that supplies it, such as the design profile's [Prime law](DESIGN_MODULE.md#6-prime-law) | 6, 7 |
| P2 (independent), P3 (independent), P1 (independent) | By P2 each member governs only the question it owns, and by P1 and P3 a specialisation keeps its own meaning and owner, so this member's law stops at engagement: it defines no application profile, role mapping, product-owned frame-basis binding, domain product, runtime, workflow or assurance implementation. A member or product that specialises its relations does so under its own authority, and that relation neither enters nor amends this member; a same-spelled carrier enters the context by no proximity or nominal match | [§1](#1-the-frame-as-the-engagement-unit), Scope | the bounded-context identity `urn:stdo:bounded-context:reference-frame-evaluation`: this member; each specialisation: the profile or product that declares it | 1, 7 |
| P1 (independent), P3 (independent), P6 (independent) | By P1 and P3 a concept means what its owner defines on its basis, and by P6 using it grants nothing, so a concept used here that another member defines keeps that owner and that meaning. It enters by a reference-only import, which grants no semantic, evaluation, operation or decision authority; a refinement this member states names its owner and maps back to the core | [Imports into this context](#imports-into-this-context) | which concepts are imported, and from which member: this member's declaration; the import rule: [FOUNDATIONS §2 Imports between members](FOUNDATIONS.md#imports-between-members), traced in family F12 | 2, 7 |
| P0 (recovered), P1 (independent), P2 (independent), P3 (independent), P6 (independent) | By P0 an actor engages only a finite specification, and by P1 and P3 a carrier is a representation of it, not the relation, so a reference frame is a finite specification of the attention, coordinates, authority, evidence and result relations one evaluation family requires. It specifies a relation, not a required schema or runtime carrier; a prompt, context packet or program is a projection of an activated frame, not the frame. A frame is bound only when every material coordinate resolves to an exact source, subject, basis, authority, evidence route, actor envelope, result relation and invalidation condition, and representation cannot create, widen or replace that binding | [FOUNDATIONS §2 The frame tuple](FOUNDATIONS.md#the-frame-tuple) and [Frame objects](FOUNDATIONS.md#frame-objects), Workspace, Material-relation manifold, Reference frame and Active frame configuration, outside this member | the twelve components ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩: FOUNDATIONS §2 The frame tuple | 6, 7 |
| P2 (independent), P1 (independent); instance premise b | By P2 a frame exists for an evaluation, and by P1 wording carries no meaning of its own, so a frame's sufficiency can be tested only against the evaluation family it declares, so every frame declares one; a module, file, service, role, persona, prompt or lens with no declared evaluation relation is not a frame. Similar wording does not show that two evaluations share a family: an evaluation is within a frame's family only when the question it decides is one that family states at the frame's declared coordinates, whatever the frame's name or its membership in the set | [RF-001](#rf-001-evaluation-relativity); [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Evaluation, Evaluation family and Role, persona, abstraction, component, outside this member; [Diagnostic order](#diagnostic-order), question 1; [§12](#12-violations) item 2 | each frame's evaluation family: the frame's declaration, made under the frame-set authority (§4) | 7 |
| P0 (recovered, with its actor-change premise), P2 (independent), P6 (independent); instance premise a | By P0 and its actor-change premise an attention surface must fit and be reconstructable by the actor that uses it, so an activated frame's attention surface is finite and fits the selected actor's declared envelope; a frame that needs undeclared ambient memory, conversation history or an effectively global workspace context is not reconstructable for that actor. Where the envelope declares a context capacity, the selected context's size is measured before the actor reads it, over a stated boundary, and recorded with the capacity and the comparison; context outside the boundary is recorded as not measured. The measurement applies there and only there, is no budget and no universal gate, and shows fit and nothing else | [RF-002](#rf-002-finite-attention); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 3, the size measurement, outside this member; [§12](#12-violations) item 10 | the capacity and its unit, bytes or tokens: the actor's declared envelope; the measured boundary, and time, spend and other resource limits: the selected execution binding ([SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)) | 7, 8 |
| P2 (independent), P0 (recovered, with its open-world premise), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P2 and P5 a result is sound only if every relation that can change it is present, and by P0's open-world premise relations not held are not thereby absent, so every known relation whose lawful change can alter the result, the validity of the basis, the sufficiency of evidence, operation authority or decision authority appears in the frame or enters through a declared authoritative input, and omitting one makes the frame insufficient; the law does not require proof that no undiscovered material relation exists. The context starts as the material closure of the intake's seed set (the subject, outcome and affected relations it names) under that relation family, and a closure that is not finite and unique on the exact basis stops the step and is not guessed | [RF-003](#rf-003-material-sufficiency); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 1, outside this member | the closure law: [AC-010](AXIOMATIC_CALCULUS.md#ac-010-material-closure); the stop's outcome, `closure_unresolved`: [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation) | 6, 7 |
| P2 (independent) | By P2 attention is spent only on what bears on the evaluation, so relations that cannot affect the declared evaluation stay outside active attention unless they are needed to establish that irrelevance; adjacent material, or the presence of the corpus, is no reason to load or read it. The closure is projected to the selected context with its boundary recorded | [RF-004](#rf-004-irrelevance-exclusion); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 2 and Acquisition, outside this member | the seams the boundary records (excluded, external, unresolved, translated, invalidation-sensitive): ACTIVATION §2 step 2, applying [AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection) | 7 |
| P3 (independent), P1 (independent) | By P3 a result binds its exact basis, and by P1 equal names or shapes do not establish equal meaning, so every result binds its exact subject, basis, coordinates and evidence scope. A stale, advanced, ambiguous or mismatched basis returns `invalid_basis` or requires reactivation; equal names, values, shapes, locations or apparent topology positions never substitute for declared coordinate equality | [RF-005](#rf-005-exact-basis-and-coordinates); [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Coordinate, outside this member; [§12](#12-violations) item 7 | each frame's coordinate and equality law: its declaration (C of the frame tuple) | 2, 7 |
| P6 (independent), P3 (independent); instance premise c | By P6 authority exists only through an admitted grant, and by P3 it binds its owner and scope, so a frame carries and applies admitted authority and never mints, widens, transfers or reconstructs it from actor identity, capability, evidence shape, implementation reachability or frame selection; declaring, selecting, activating or executing a frame, or naming a role, grants none. The kinds of authority may coincide in a lawful case and never collapse by default, and actor identity is not an authority. A read-only evaluation declares no operation authority; an effectful one inherits the exact operation grant from its existing owner. A proxy for human authority keeps its identity distinct from the human authority's | [RF-006](#rf-006-authority-conservation); [FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds) and [Frame objects](FOUNDATIONS.md#frame-objects), Role, persona, abstraction, component, outside this member; [§2](#2-core-claims) claim 8; [§12](#12-violations) item 6 | the division into frame-set, semantic, evaluation, operation and decision authority, with actor identity apart, and frame-set authority as human authority: FOUNDATIONS §2 Authority kinds; when a bounded proxy may act: [IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004) | 7, 9 |
| P6 (independent) | By P6 meaning, evidence, application, operation and decision are separate authorities, so semantic law defines what the evaluation means, evidence supplies observations, the evaluator applies the declared relation, the existing operation owner supplies any operation grant, and decision authority disposes the result; a frame declaration keeps these roles distinguishable even when one actor performs several. The evaluator applies the frame's declared invariants, evidence rules and result algebra and records every assumption whose failure could change the result | [RF-007](#rf-007-semantic-evidence-and-verdict-separation); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) Evaluation, outside this member | none; [EVALUATION §2](EVALUATION.md#2-separation) applies this law to review (family F6) | 7, 9 |
| P1 (independent), P3 (independent); instance premise c | By P1 shared material does not share meaning, and by P3 each frame binds its own basis, so frames may share entities, variables, evidence or coordinates; shared material establishes neither identical meaning nor identical basis, authority or result, and every cross-frame equality or translation an evaluation uses is declared where it is used | [RF-008](#rf-008-overlap-without-identity-collapse); [§12](#12-violations) item 7 | none | 2, 7 |
| P3 (independent), P1 (independent), P6 (independent), P2 (independent); instance premise c | By P3 and P1 a relation holds only where it is declared, and by P6 and P2 each structure answers its own question, so parent and child relations among frames apply only where declared. Functional decomposition, communication, authority precedence, frame configuration, subject topology and evaluation dependency are distinct relation structures, which a consumer may align where the governed subject warrants it and never silently treats as one hierarchy; an exchange of information grants no authority and establishes neither a decomposition nor an evaluation dependency. No frame relation is the default topology, and a project declares only the relations its evaluations and coverage claims need | [RF-009](#rf-009-no-assumed-hierarchy); [§7](#7-frame-relations); [§12](#12-violations) item 3 | the ten named frame relations: this member (§7); which relations a project declares, and where it aligns relation structures: that project, for its governed subject | 4, 7 |
| P6 (independent), P1 (independent); instance premise c | By P6 and P1 each kind of independence is a different relation, so frame disjointness (structural), evaluation independence (procedural) and assurance independence (claim-relative) are three relations: disjoint frames need not be independently evaluated, independently activated evaluations need not be disjoint, and the unqualified word "independent" establishes none of them. Separately activated evaluations may overlap in subject, manifold or evidence, and neither consumes nor influences the other's unclosed working result | [FOUNDATIONS §2 Disjointness and independence](FOUNDATIONS.md#disjointness-and-independence), outside this member; [Independently activated co-evaluation](#independently-activated-co-evaluation) | the conditions a verdict needs to count as independent assurance: the governing assurance law ([EVALUATION §3](EVALUATION.md#3-independent-assessment), family F6) | 7, 9 |
| P4a (independent), P6 (independent), P2 (independent) | By P4a composition is needed only where parts combine through declared relations, and by P2 nothing is composed that the evaluation does not need, so using several frames does not require composing their internal manifolds. Composition law is required only when the evaluation combines their internal variables, transports evidence or values across them, or treats their operations as one material execution relation. Independently activated evaluations may instead return closed results to one declared conjunction or decision rule. A material composition is introduced only when the evaluation requires it, and declares its shared invariants, effect or decision order where material, closure, failure and the conservation of semantic, operation and decision authority | [RF-010](#rf-010-composition-on-demand); [§6](#6-frames-in-conjunction), Result conjunction and Material composition; [§12](#12-violations) items 4 and 5 | each material composition: the owning application; the conjunction: [FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results) (family F3); the choices its declared rule leaves open: the member or profile that applies the conjunction, in its declared rule | 3, 4, 7 |
| P1 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance premise c | By P1 a value carried across frames keeps its meaning only through a declared relation, and by P4b what is lost must travel with it, so where one frame supplies evidence or a value consumed inside another, the translation declares source and target coordinates, preserved meaning, accepted loss, provenance, equality law and refusal conditions; a loss inside the accepted loss travels with the value as a residual | [Evidence or coordinate translation](#evidence-or-coordinate-translation); [§5](#5-method-functions), the outcomes of `translate` | the accepted loss and the refusal conditions of each translation: its declarer | 3, 6, 7 |
| P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance premise d | By P3 a result binds coordinates that a topology change can alter, and by P4b a stale result persists until re-evaluated, so an activated frame declares the topology changes capable of invalidating its coordinates or its materiality judgment, and a detected material topology mutation causes reevaluation, frame revision or recharting before a previous result is reused. A material revision of a frame produces a new revision coordinate and states which prior activations, results and coverage claims need reevaluation; every result bound to the prior revision is reopened until a recorded re-check finds it independent of the change or it is re-evaluated, and silence keeps no result closed. A revision that changes no declaration of the frame needs no new coordinate, and an unchanged declaration is no ground for keeping a result closed: whether a closed result stays valid is decided by the reuse rule of ACTIVATION §7 | [RF-011](#rf-011-topology-mutation-and-recharting); [Revision actions](#revision-actions); [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Topology, outside this member; [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), the reuse rule, outside this member; [§12](#12-violations) item 11 | each frame's invalidation and rechart conditions: its declaration (J of the frame tuple); the revision actions listed: this member (§10) | 2, 7 |
| P0 (recovered, with its actor-change premise), P6 (independent), P2 (independent), P3 (independent) | By P0's actor-change premise a frame must work for a fresh actor, and by P6 and P3 that actor receives only declared, bound inputs, so a fresh competent actor inside the declared envelope can reconstruct the activated evaluation from the frame declaration, the exact subject, the basis and the admissible inputs, without undocumented conversational or historical context. An actor receives one activated frame or one declared active frame configuration, never an implied demand to reconstruct the workspace from ambient context; it may own its internal reasoning where the governing method permits, returns through the declared result relation, and hidden reasoning substitutes for no required evidence, provenance or authority. Every field of the binding resolves through stable identities and source references, for which paths, line numbers, counts, summaries and matching labels do not substitute | [RF-013](#rf-013-reconstructable-activation); [§11](#11-the-activation-packet); [Minimal activation binding](#minimal-activation-binding) | the packet's minimum contents and the binding's fields: this member; the carrier: its consumer (RF-016) | 7, 9 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise a | By P0 an actor's envelope is finite, and by P5 a step cannot report success on what it did not hold, so frame adequacy includes actor usability. When the material manifold exceeds an actor's envelope, the lawful responses are another actor, a refined frame or outer contract, sequenced activations, a lawful compression or `out_of_frame`; silently omitting material relations to fit is never one of them, and a frame never silently grows beyond the selected actor's envelope. Actor capability may justify a different frame size or activation sequence, and can neither waive an invariant nor widen authority | [RF-014](#rf-014-capability-fit); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 3, the responses when the context does not fit, outside this member; [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Capability envelope, outside this member; [§11](#11-the-activation-packet), frame size; [§12](#12-violations) item 10 | the selection among these responses: human authority, directly or in advance through the grant; which responses a step selects within its grant (refinement, sequencing, compression) and which re-enter the owner of the grant or envelope (another actor, a larger envelope): ACTIVATION §2 step 3 | 7, 8 |
| P2 (independent), P0 (recovered), P6 (independent) | By P2 a compression serves the evaluation, and by P0 it must fit the envelope, so a compression preserves the material distinctions and failure detections the evaluation family requires while fitting the envelope; it need not be a unique smallest frame. Intentional overlap is kept where it supplies independently activated evaluation, different capability fit, different evidence altitude or useful fault detection, and frames are merged only when the merged frame preserves evaluation meaning, authority, capability fit and proportional reasoning cost. Whether a compression preserved what the evaluation needs is a claim: the compressing step records the compression and its preservation argument | [RF-017](#rf-017-proportional-compression); [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 3, compression, outside this member; [§12](#12-violations) item 13 | whether that claim is assessed independently: the promotion it serves ([EVALUATION §3](EVALUATION.md#3-independent-assessment)) | 6, 7 |
| P0 (recovered, with its open-world premise), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent) | By P0's open-world premise unknown relations exist, and by P4b and P6 an absence of a counterexample is not evidence, so coverage and evaluation results keep known uncertainty explicit: unresolved relations, uncovered evaluations, contested evidence and unknown capability. Absence of a recorded counterexample is not evidence of completeness. Without an independently established closed-domain completeness predicate, a finite frame set cannot establish, by inspecting its own inventory, that no material evaluation is undiscovered; coverage therefore stays falsifiable and states an explicit residual boundary | [RF-015](#rf-015-residual-uncertainty); [§9](#9-completeness-boundary) | a closed-domain completeness predicate, where one is used: the owner of that domain, who establishes it independently | 7, 9 |
| P2 (independent), P0 (recovered) | By P2 the method requires only what the outcome needs, and by P0 an actor needs the relations, not a carrier, so this member requires the declared relations and the observable outcomes, and no frame runtime, universal carrier, registry, controller, prompt format, repository layout, collaboration topology, worker count or software framework. A frame and the method functions may be realised in any conforming form, and the signatures describe relations, not callable interfaces; the minimal declarations are the least content that declares a frame, a frame set and an evaluation result, in any carrier | [RF-016](#rf-016-implementation-neutrality); [§1](#1-the-frame-as-the-engagement-unit), Substrate; [§5](#5-method-functions), the signatures; [§13](#13-minimal-declarations); [§12](#12-violations) item 14 | the carrier: its consumer; the fields of the three minimal declarations: this member, with the out_of_frame residual field carrying what [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) requires | 7, 8 |
| P6 (independent), P2 (independent); instance premise b | By P6 human authority may declare what it owns, and by P2 and (b) a declaration serves the outcome from known evidence, so human authority may declare a project frame set from accumulated practice, known failure modes, domain expertise, the outcome's risk and knowledge of the available actors, without reconstructing it from the workspace bottom up. The declaration records the governed workspace and outcome, the evaluation inventory, the frames and their envelopes, intentional overlaps, dependencies or translations, the authorities, exclusions and residual uncertainty, and the conditions for revision. Human selection proves neither that the set is complete nor that its frames hold authority over the relations they inspect, and a frame set need not be a partition, tree, stack or exhaustive ontology | [§4](#4-frame-set-declaration); [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Frame set, outside this member; [§2](#2-core-claims) claim 4 | the frame set: the frame-set authority, which FOUNDATIONS §2 Authority kinds names as human authority; the items the declaration records: this member | 1, 7, 9 |
| P2 (independent), P0 (recovered), P6 (independent); instance premises a, b | By P2 coverage serves the governed outcome, and by P0 each evaluation needs a capable actor, so a selected frame set meets the baseline coverage constraint when every known material evaluation has a frame in the set and an available actor inside that frame's envelope capable of it. Selection weighs further considerations under no prescribed algorithm; they create no universal resource ledger, benchmark, budget or measurement gate, a resource control applies only through an explicitly selected frame and its owning scope, and selection waives no other semantic, authority, evidence or independence constraint | [Frame-set selection](#frame-set-selection) | the weighing, and whether a non-minimal set is accepted for its risk reduction or actor fit: human authority; the cost control where a cost claim is the governed question: [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) (family F5) | 5, 7 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent) | By P5 each outcome answers its own predicate, and by P6 an outcome is not its acceptance, so the outcomes of `activate`, `conjoin` and `translate`, and the coverage statuses, each answer their own named predicate. A refused activation performs no evaluation; `decision(holds)` assesses the composite predicate and is not its acceptance; a coverage status is a result of the audit, never of the covered evaluation, and an excluded row is met by its cited exclusion, never covered or performed | [§5](#5-method-functions), the outcome table and the paragraph after it; [Coverage ledger](#coverage-ledger), the status table and the paragraph after it | the outcome and status names and their causes: this member; the mapping of each into one core value follows [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Refinements (family F3) | 3, 7 |
| P3 (independent), P2 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance premises b, d | By P3 coverage binds an exact tuple, and by P4b and P6 its inventory is a recorded, evidenced fact, so coverage is evaluated against an exact tuple of workspace, governed outcome, basis, evaluation inventory, frame set and time, and a change of any material member may invalidate it. The inventory is derived from every material available source and records provenance and materiality; artifact presence, file, operation, test, review or actor count proves no coverage. Coverage dimensions are lenses, which become frames only when instantiated as bounded evaluation families. The ledger holds, for each evaluation, its subject and basis, frames, envelope, authorities, evidence, dependencies, status and residual | [Coverage basis](#coverage-basis); [Evaluation inventory](#evaluation-inventory); [Coverage dimensions](#coverage-dimensions); [Coverage ledger](#coverage-ledger), the fields; [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Lens, outside this member; [§2](#2-core-claims) claim 7; [§12](#12-violations) item 9 | the sources listed, the typical dimensions and the ledger's minimum fields: this member | 7, 9 |
| P4a (independent), P2 (independent), P6 (independent) | By P4a interacting relations compose only through declared relations, and by P2 an interaction that can change the outcome must be evaluated, so coverage by evaluation row is insufficient where two covered relations interact in a way capable of changing the governed outcome, so every material interaction is covered by one frame, a declared conjunction, a translation or a material composition. Every material evaluation identifies its semantic and decision authority and every material operation its existing operation authority; a frame set with an unresolved decision owner, or an effectful path without operation authority, is not closed | [Interaction coverage](#interaction-coverage); [Authority coverage](#authority-coverage) | none | 4, 7 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise) | By P4b and P5 a known failure persists as an input until it is detected or excluded, so coverage includes known success, refusal, boundary, integration, recovery, reconstruction and competing-path cases where they are material, and a historical failure stays a coverage input until a declared frame detects or excludes its recurrence | [Failure coverage](#failure-coverage) | a policy of this member: the list of case kinds coverage includes where material (success, refusal, boundary, integration, recovery, reconstruction and competing path) | 7, 9 |
| P6 (independent) | By P6 independence is a relation established by evidence, not a label, so independently activated coverage uses a separately activated evaluation relation and declares any additional assurance-independence conditions; a persona label establishes neither relation | [High-risk separately activated coverage](#high-risk-separately-activated-coverage) | which evaluations require it (high consequence, weak observability, strong confirmation bias or a history of local proof masking): human authority | 7, 9 |
| P6 (independent), P0 (recovered, with its open-world premise) | By P6 a coverage claim holds only on its conditions, and by P0's open-world premise unknown residuals stay explicit, so a frame set has operational full coverage for its declared tuple only when its eight conditions hold, among them that no unresolved frame-result conflict is hidden by aggregation and that uncovered and unknown residuals are explicit. The claim is relative to that tuple and is not a claim that no undiscovered evaluation exists | [Operational full coverage](#operational-full-coverage) | each exclusion: the governing authority the excluded row cites | 7, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise), P2 (independent), P6 (independent) | By P4b and P5 failures and violations are evidence that persists, and by P2 and P6 diagnosis serves the outcome without granting repair, so historical failures, resets and invisible violations are evidence for improving a frame declaration, activation, actor assignment or frame set, and the listed signals trigger frame diagnosis. Diagnosis excludes activation, basis, capability, evidence, missing-relation, missing-conjunction and evaluation-family defects before it adds another frame | [Missing-frame signals](#missing-frame-signals); [Diagnostic order](#diagnostic-order); [§2](#2-core-claims) claim 10; [§12](#12-violations) item 12 | the signals listed and the order of the eight questions: this member | 7, 9 |
| P0 (recovered, with its actor-change premise), P3 (independent), P6 (independent); instance premise e | By P0's actor-change premise and P3 an input is acquired by exact identity from the selected basis, and by P6 absence from view grants nothing, so declared inputs are acquired by exact identity, and only from the exact selected basis: a declared input absent from the actor's view is neither licence to read elsewhere nor evidence that it is absent, and a candidate source, a moving selector or another basis is no substitute. Where a derived surface is stale, missing or insufficient for a named question, the deciding owner sections are acquired directly. Acquisition is read-only, grants no role, operation or decision, and a missing binding is returned with its outcome before any dependent action | [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) step 4 and Acquisition, outside this member | acquiring a current derived surface in preference to its owning sections where it serves the task: ACTIVATION §2 Acquisition; which derived surfaces are published: their publisher, and none owns a determination | 2, 7 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P3 (independent), P6 (independent) | By P0 an actor loads only what its frame declares, and by P5 and P3 a declaration is not evidence about one activation, so activation binds each reusable frame declaration to the exact subject and basis and loads the declared material relations and evidence sources, never an undifferentiated workspace dump; a reusable declaration is not evidence that a particular activation was correct. When no available frame and actor pairing can lawfully perform the evaluation, activation returns `out_of_frame` or the refusal whose cause holds, and work does not proceed through implied context | [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) Activation, outside this member; [FOUNDATIONS §2 Frame objects](FOUNDATIONS.md#frame-objects), Activated frame, outside this member | who selects the frame: the actor or the assigning authority, as the configuration allocates ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration), family F2) | 7, 8 |
| P6 (independent), P1 (independent); instance premise e | By P6 a derived surface owns no determination, and by P1 it is a representation of its sources, so a derived surface or projected frame decides standalone only the questions its own source members own. For a question another member owns, or one that joins the law of several owners, the step returns `out_of_frame` naming the owning members, and the question is decided from those members or from a derived surface whose declared sources include every owner | [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) Standalone scope, outside this member | none | 6, 7, 9 |
| P6 (independent), P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise) | By P6 a prompt holds no authority of its own, and by P0 and P5 it carries only what the step needs, so a prompt is a rendered contract over typed authority, not source law. It projects the current authority references, obligations, contracts, boundaries, proof expectations and fallback conditions the step needs, and the material Acquisition selects; it carries no historical workaround prose unless a current surface still needs that constraint. Construction starts from the highest live authority surface the question needs and names an unresolved upstream authority gap before fallback context is read | [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) Prompt construction, outside this member | the design, ODD, UX and ticket specialisations: [DESIGN_MODULE §11](DESIGN_MODULE.md#11-review), [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) and [§11.7A](ODD.md#117a-conforming-agentic-development), [UX §7](UX.md#7-carrier-binding), and [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and [§7](TICKETS.md#7-authority-judgment-closure-and-state) | 6, 7 |

RF-012, and the mapping of the outcomes of §5 and the coverage statuses of
§8 into the core, apply the core result algebra and its refinement rule;
they are traced in family F3 at
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and the rows above trace
only what those rules decide about frames. Claim 9 of §2 and item 8 of §12
state RF-012 and go with it to F3. §2 states ten core claims that the rules
named in the rows, or RF-012, make precise; it adds no rule of its own. §12
lists violations, each of the rule it cites, and each is traced in that
rule's row or, for item 8, in F3. §14 states when a project operates under this member: when the
rules named in the rows hold for its frame set, with no frame machinery,
global context, universal completeness or domain authority inferred from
adopting the member. §15 records dispositions and decides nothing.

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
#rf-002-finite-attention). The fit is tested in
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
which owns the measurement of the context's size and when it applies.
Whether the actor attends adequately to a frame that fits is a separate
question, answered by actual-use evidence under
[EVALUATION §7](EVALUATION.md#frame-qualification); a size measurement
does not answer it (P0, P6).

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
authority from anything that creates none. That list is
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)'; its
instances in a frame include actor identity, available capability,
evidence shape, implementation reachability and frame selection (P6;
rc.2 #rf-006-authority-conservation).

### RF-007 Semantic, evidence and verdict separation

The separation of semantic law, evidence, the evaluator's application
and the disposing decision authority is
[EVALUATION §2](EVALUATION.md#2-separation)'s. This law binds it to a
frame: a frame declaration keeps these roles distinguishable even when
one actor lawfully performs several of them, and where the evaluation
performs a material operation, the existing operation owner supplies the
exact grant as a further role the declaration keeps apart (P6; rc.2
#rf-007-semantic-evidence-and-verdict-separation).

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
decomposition, communication, authority precedence, frame configuration,
subject topology and evaluation dependency are distinct relation
structures; a consumer may align them where the governed subject warrants
it and may not silently treat them as one hierarchy (P3, P1; rc.2
#rf-009-no-assumed-hierarchy). Communication is the exchange of
information between frames, or between the actors activated on them. An
exchange by itself grants no authority, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and establishes neither a decomposition nor an
evaluation dependency (P6, P1). Communication is new
in this list. Purpose and material relation: a configuration assigns
information exchanges as well as responsibilities
([ACTIVATION §1](ACTIVATION.md#configuration)), and an exchange read as a
grant or as a dependency would move authority or change a result without a
declared relation.

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

Every performed evaluation of a frame returns one closed result in the
frame's declared result algebra: the core algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), or a refinement mapped
into it under that section. That section owns the five core values
(`satisfied`, `falsified`, `indeterminate`, `out_of_frame` and
`invalid_basis`), their meanings and the rules over them: that nothing is
coerced to success; that a refinement adds no core value, keeps
indeterminate, out-of-frame and invalid-basis pressure explicit and raises
no result's standing; and that an evaluation not performed has no result,
its stop state being
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition). This law
applies them to every frame and defines none of them (P5; rc.2
#rf-012-closed-results).

### RF-013 Reconstructable activation

A fresh competent actor inside the declared capability envelope can
reconstruct the activated evaluation from the frame declaration, the exact
subject, the basis and the admissible inputs, without undocumented
conversational or historical context (P0 with the actor-change premise;
rc.2 #rf-013-reconstructable-activation).

### RF-014 Capability fit

Frame adequacy includes actor usability. When the material manifold
exceeds an actor's capability envelope, the remedies are those of
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
step 3, which owns the list: among them selecting another actor, refining
the frame into steps, sequencing activations and a lawful compression
(RF-017). Choosing among them is human authority's, exercised directly or
in advance through the grant; ACTIVATION §2 says which of them a step
selects itself and which re-enter the grant's owner. The actor may not
silently omit material relations to fit its context (P0, P5; rc.2
#rf-014-capability-fit).

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

These considerations create no universal resource ledger, benchmark,
budget or measurement gate: cost is selected, not universal, under
[ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality), which owns
resource limits, and these four are its instances in frame selection. In
frame selection a resource control applies only through an explicitly
selected frame and its owning applicability and work scope; ACTIVATION §6
is that selection where a cost claim is the governed question. The test
that an activated frame's context fits the selected actor is RF-002's,
distinct from the actor context that selection weighs, and
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
owns its measurement and when the measurement applies. Frame selection
cannot waive another applicable semantic, authority, evidence or
independence constraint (P2, P6).

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

`declare` is §4; `activate` and `evaluate` are ACTIVATION §1 and §2;
`evaluate` returns its result under RF-012, and the closed result is
returned and reused under ACTIVATION §7; `conjoin` and `translate` are §6;
`audit_coverage` is §8, which maps the statuses of its ledger to the core;
`revise` is §10. EVALUATION §7 qualifies each.

The outcomes of `activate`, `conjoin` and `translate` form a refinement of
the core algebra, stated under the refinement rule of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results): each outcome below maps
to exactly one core value for the predicate its function names, the value
travels with that predicate and with the outcome, whose meaning stays here,
and an outcome named in the signatures above that would map to more than
one core value according to its cause carries the cause in its name, as in
`activation_refusal(basis)` (P5, P6). The refinement is new in this
corpus. Purpose and material relation: a consumer that combines these
outcomes with other results reads them in the one core, so a refusal, a
conflict or a loss outside the accepted loss is neither mistaken for
success nor merged with an evaluation that was not performed.

| Function and predicate | Outcome | Cause | Core value |
|---|---|---|---|
| `activate`: the frame is activated for this evaluation, subject, basis and actor | `activated_frame` | the frame declaration is bound to the exact evaluation, subject, basis and actor | `satisfied` |
| | `activation_refusal(capability)` | the frame declares a capability the evaluation needs, and the selected actor's declared envelope lacks it; the refusal names that capability and its owner where the subject gives one | `out_of_frame` |
| | `activation_refusal(authority)` | the activation needs semantic, evaluation, operation or decision authority that is not admitted to it; the refusal names that authority's owner | `out_of_frame` |
| | `activation_refusal(basis)` | the subject or basis is stale, advanced, ambiguous or mismatched (RF-005), a topology mismatch included: the subject's topology is not the topology basis the frame declares (RF-011) | `invalid_basis` |
| `conjoin`: the composite predicate holds under the declared decision rule | `decision(holds)` | the conjunction of FOUNDATIONS §4 reports `satisfied` | `satisfied` |
| | `decision(fails)` | the conjunction reports `falsified`, and no mandatory result for the same claim is `satisfied` | `falsified` |
| | `conflict` | the conjunction reports `falsified` while mandatory results for the same claim disagree, one `satisfied` and another `falsified`; the counterexample survives the join, and the disagreement stays unresolved for the decision authority | `falsified` |
| | `indeterminate` | the conjunction reports `indeterminate` | `indeterminate` |
| `translate`: the value or evidence enters the target frame as the declared translation states | `translated_value` | the value or evidence is carried into the target coordinates with its declared meaning | `satisfied` |
| | `declared_loss` | the value or evidence is carried with a loss inside the declared accepted loss; the loss travels with it as a residual (P4b) | `satisfied` |
| | `refusal(condition)` | a refusal condition the translation declares holds, a loss outside the accepted loss included; or the value or evidence fails identity or equality under the translation's declared equality law | `falsified` |
| | `refusal(authority)` | an authority mismatch the translation does not declare: the value or evidence carries semantic, evaluation, operation or decision authority whose relation to the target frame's authority the translation states neither as preserved nor as a refusal condition; the refusal names that authority's owner | `out_of_frame` |
| | `refusal(basis)` | the source value or evidence binds a stale, advanced, ambiguous or mismatched basis or coordinate (RF-005) | `invalid_basis` |

Where no frame the actor can use declares a material relation or
capability the evaluation needs, `activate` returns `out_of_frame` itself
([ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Activation). Where the conjunction reports `out_of_frame` or
`invalid_basis`, `conjoin` returns that value; the signatures name no
outcome for either case, and a basis mismatch is this returned
`invalid_basis`, as EVALUATION §7 names it for `conjoin`. Under a
declared veto or deferral, `conjoin` returns the outcome above whose cause
holds for the value the conjunction reports
([FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results)), or that value
itself where it is `out_of_frame` or `invalid_basis`. A planned
assessment without a closed result, and required coverage that no planned
assessment addresses, are no outcome of `conjoin`:
[FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results) records them
beside the reported value, and they map to no core value. The outcomes of
`activate` answer whether a frame was activated, never the
evaluation's claim: a refused activation performs no evaluation.
`decision(holds)` assesses the composite predicate and is not its
acceptance, which is a separate result
([FOUNDATIONS §4](FOUNDATIONS.md#results)).

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

A declared decision rule consumes the closed results of several frames.
The rule, what it must state, and the conjunction it computes are
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
over the core values of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results);
this member defines no conjunction of its own. The outcomes of `conjoin`
map to the core as §5 states (P4a, P5, P6; rc.2 #result-conjunction).

### Evidence or coordinate translation

One frame supplies evidence or a value consumed inside another. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law and refusal conditions (P1, P4b;
rc.2 #evidence-or-coordinate-translation). What a statement of preserved
meaning and accepted loss must show, and the law that licenses the
step, are
[ACTIVATION §4, Refinement](ACTIVATION.md#refinement), and where the
translation is represented in `a_c` it is recorded in the preservation,
introduced, removed and residual fields of
[AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation). This section adds
only the frame fields: the source and target coordinates, the
provenance, the equality law and the refusal conditions.

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
coverage result; whether a change does is decided by
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): it does when it
could change that result, as a material input change or a changed basis
(P3, P6; rc.2 #coverage-basis).

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

The statuses form a refinement of the core, stated under the refinement
rule of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). They answer
whether a row's coverage obligation is met, for the predicate "on the
declared coverage tuple, a capable frame of S covers the evaluation with
no unresolved conflict among the frames, results or authorities that
cover it, or a governing authority the row cites excludes it". Each status
maps to exactly one core value, and the value travels with that predicate
and with the status, whose meaning stays here (P5, P6):

| Status | Cause | Core value |
|---|---|---|
| `covered` | a capable frame of S evaluates it on the tuple, with no unresolved conflict among what covers it | `satisfied` |
| `separately_covered` | separately activated frames of S each evaluate it on the tuple, with no unresolved conflict among them (High-risk separately activated coverage) | `satisfied` |
| `excluded_by_authority` | the governing authority the row cites excludes the evaluation from the claim (Operational full coverage, item 7) | `satisfied` |
| `conditionally_covered` | a capable frame of S covers it only under a condition the audit has not established; the residual names the condition and the evidence that would decide it | `indeterminate` |
| `conflicted` | the frames, results or authorities that cover it conflict, and the conflict is unresolved; the conflict is the counterexample and stays unresolved for the decision authority (Operational full coverage, item 6) | `falsified` |
| `uncovered` | no capable frame of S evaluates it, and no cited authority excludes it; that absence is the counterexample | `falsified` |
| `unknown` | the admissible evidence cannot decide whether a capable frame of S covers it, as where the actor capability or the materiality is unknown | `indeterminate` |

These values are results of `audit_coverage` for this predicate, never
results of the covered evaluation itself. `satisfied` for an excluded row
establishes that the obligation is met by the cited exclusion, never that
the evaluation is covered or was performed; the status keeps that
distinction (FOUNDATIONS §4 Results, Recording). In a conjunction over the
governed claim, an evaluation whose row is `uncovered` is required
coverage that no planned assessment addresses
([FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results)), never a
`falsified` component. Where the coverage tuple itself is stale, advanced,
ambiguous or mismatched, the audit returns `invalid_basis` (RF-005) and
assigns no status. The mapping is new in this corpus. Purpose and material
relation: a coverage claim combined with other results is read in the one
core, so a conditional, conflicted, unknown or uncovered row is never read
as covered, and a cited exclusion is never read as a failure (P5, P6).

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
a result closed. The reopening by default is a tightening the predecessor
implies and does not state (P3, P4b; rc.2 #revision-actions, which makes
the revision state the results that require reevaluation,
#rf-005-exact-basis-and-coordinates, #rf-011-topology-mutation-and-recharting
and #return-a-closed-result, whose demonstrably independent surviving
results are the re-check's one survival route).

Whether a revision needs a new frame revision coordinate turns on the
frame's declarations; whether a result already closed stays valid is a
separate question. A revision is material when it changes a frame
declaration in a way that is material under
[FOUNDATIONS §2](FOUNDATIONS.md#2-ontology). A revision that changes no
declaration of the frame needs no new coordinate. That answer decides
nothing about any result: an unchanged declaration is no ground for
keeping a result closed. Whether a closed result stays valid is decided
by the reuse rule of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), with materiality
as [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines it, and that rule
can reopen results although no declaration changed; results it reopens
without a material revision are recorded as reopened in the work state
([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)). For example, a
clarification that finds a recorded activation outside its frame's family,
so that the result fails the exact applicability check of ACTIVATION §7
([RF-001](#rf-001-evaluation-relativity);
[Diagnostic order](#diagnostic-order) question 1), or newly acquired
admissible evidence that is material to a closed result, a material
input change under ACTIVATION §7, reopens that result
and every coverage ledger row and coverage claim that consumed it, and
preserves every demonstrably independent surviving result. A harmless
explanatory clarification, which changes no material input and is no
revising observation, invalidates no result by itself;
reuse still requires the consumer's exact applicability check (P3, P6;
rc.2 #return-a-closed-result).

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
- out_of_frame residual (missing relation or capability, owner, reconfiguration pressure):
- invalidation conditions:
- consuming decision or conjunction:
```

The out_of_frame residual field is new in this corpus; it carries what
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) requires an out_of_frame
result to name, and reads `none` for any other result (P5).

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
REFERENCE_FRAME_METHOD.md; a locus is a section of this file unless it names
another member.

| Anchor | Disposition | Locus |
|---|---|---|
| #canonical-compression | conserved | §1 |
| #position | conserved; the context also holds the concepts other members define, by reference-only import (§1 Imports into this context) | §1 (scope, substrate, imports); the bounded-context identity and the bound on what this member owns are carried unchanged |
| #core-claims | conserved | §2 |
| #reference-frame-laws | not applicable: heading with no claim text (24 bytes); its children are disposed individually | §3 |
| #rf-001-evaluation-relativity | conserved | §3 RF-001 |
| #rf-002-finite-attention | conserved | §3 RF-002; the fit test and the size measurement are ACTIVATION §2; adequate attention is evaluated from actual use under EVALUATION §7 |
| #rf-003-material-sufficiency | conserved | §3 RF-003 |
| #rf-004-irrelevance-exclusion | conserved | §3 RF-004 |
| #rf-005-exact-basis-and-coordinates | conserved | §3 RF-005 |
| #rf-006-authority-conservation | conserved; the list of what creates no authority is FOUNDATIONS §2 Authority kinds, with the five frame instances here | §3 RF-006 |
| #rf-007-semantic-evidence-and-verdict-separation | conserved; EVALUATION §2 owns the separation, and RF-007 binds it to a frame declaration with the operation-grant role | §3 RF-007; EVALUATION §2 |
| #rf-008-overlap-without-identity-collapse | conserved | §3 RF-008 |
| #rf-009-no-assumed-hierarchy | conserved; communication is added as a distinct relation structure, new in this corpus, with its purpose stated | §3 RF-009 |
| #rf-010-composition-on-demand | conserved | §3 RF-010; §6 |
| #rf-011-topology-mutation-and-recharting | conserved | §3 RF-011 |
| #rf-012-closed-results | conserved; the five values, their meanings, the no-coercion and refinement rules and the evaluation not performed are owned by FOUNDATIONS §4 Results, with the stop state in ACTIVATION §3; RF-012 states the law over frames and defines none of them | FOUNDATIONS §4 Results; §3 RF-012 |
| #rf-013-reconstructable-activation | conserved | §3 RF-013 |
| #rf-014-capability-fit | conserved; the remedy list and the step's own selection among them are ACTIVATION §2 | §3 RF-014; ACTIVATION §2 |
| #rf-015-residual-uncertainty | conserved | §3 RF-015 |
| #rf-016-implementation-neutrality | conserved | §3 RF-016 |
| #rf-017-proportional-compression | conserved | §3 RF-017 |
| #engagement-atom-and-semantic-prime | conserved; the predecessor's "Prime or equivalent" is generalised to any semantic-contraction law an adopting method supplies (the design profile's prime law is one such; tier 1 names no profile term) | §3 Engagement atom and semantic atom |
| #human-frame-set-declaration | conserved | §4 |
| #frame-set-optimization | conserved | §4 Frame-set selection; the fit test and its measurement are ACTIVATION §2, cost proportionality ACTIVATION §6 |
| #method-functions | conserved; the mapping of the outcomes of `activate`, `conjoin` and `translate` to the core, each split by cause where needed, is new | §5 |
| #using-frames-in-conjunction | conserved | §6 |
| #independently-activated-co-evaluation | conserved | §6 |
| #result-conjunction | conserved; the conjunction and its declared rule are owned by FOUNDATIONS §4 Conjunction of results; §6 names the frame relation and refers | FOUNDATIONS §4 Conjunction of results; §6 Result conjunction |
| #evidence-or-coordinate-translation | conserved; the six declared items kept; preservation and loss refer to ACTIVATION §4 Refinement and AC-013 | §6 |
| #material-composition | conserved | §6 |
| #frame-relations | conserved | §7 |
| #workspace-coverage | not applicable: heading with no claim text (22 bytes); its children are disposed individually | §8 |
| #coverage-basis | conserved | §8 |
| #evaluation-inventory | conserved; "Ontology" written as the design's ontology | §8 |
| #coverage-dimensions | conserved | §8 |
| #coverage-ledger | conserved; the mapping of the coverage statuses to the core is new | §8 Coverage ledger |
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
| #minimal-evaluation-result | conserved; the out_of_frame residual field is new | §13 |
| #closure | conserved | §14 |

New law with no predecessor row: the table of family F1 (§1 Foundation to
law), in the format of FOUNDATIONS §3 Foundation to law; it decides nothing
and names the rule that states each consequence. Purpose and material
relation: a reader sees which rules of frames and context follow from the
commitments and which are added choices with their owners, so no added
choice is presented as derived (P6, P2).
