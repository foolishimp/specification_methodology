# I4-09 successor readback batch 09

Rows: 12. Each row gives the predecessor section at the installed rc.2 and the successor loci at the current tree with their subsections, then the extra sections the earlier reading said it needed. Judge each row under INSTRUCTIONS.md; the `why` line says what the earlier reading found.


### Row `DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate` (earlier reading: batch 01 indeterminate; repaired: both lists bind; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate` at rc.2:

```text
Projects using this method must prefer:

- immutable data carriers over mutable shared objects
- closed typed carriers over open dict or string protocols
- parsing and admitting foreign data once at ingress
- explicit return values over hidden mutation
- explicit failure carriers over ambient exception-driven control flow where
  practical
- composition of small transforms over long controller procedures

Projects using this method must avoid:

- one giant mutable workspace object
- one orchestration method that owns semantic law
- hidden read/write coupling through globals, shared registries, or mutable
  service state
- typed envelopes over open payload truth
- dynamic payload mutation at the semantic center
- effectful helpers that both decide meaning and perform writes
- proxy interfaces that partially imitate a new design while preserving the old
  authority path

---
```

Successor, `DESIGN_MODULE.md#functional-bias-without-language-mandate` (with its subsections):

```text
Projects using this profile prefer (P4a, P5, P6;
rc.2 #4-functional-bias-without-language-mandate): immutable data carriers over
mutable shared objects; closed typed carriers over open dictionary or
string protocols; parsing and admitting foreign data once at ingress;
explicit return values over hidden mutation; explicit failure carriers
over ambient exception-driven control flow where practical; and
composition of small transforms over long controller procedures.

They avoid: one giant mutable workspace object; one orchestration method
that owns semantic law; hidden read and write coupling through globals,
shared registries or mutable service state; typed envelopes over open
payload truth; dynamic payload mutation at the semantic centre; effectful
helpers that both decide meaning and perform writes; and proxy interfaces
that partially imitate a new design while preserving the old authority
path (P6, P4a; §10).

Both lists bind. A project that adopts this profile prefers the first
and avoids the second as an obligation of the profile, not as a
description of practice: a realisation that takes an avoided shape, or
forgoes a preferred one where it is practical, does not conform unless
its design module records the reason (P6, P2; the predecessor's "must
prefer" and "must avoid").
```


### Row `DESIGN_MODULE_METHOD.md#11d-post-ticket-design-review-rule` (earlier reading: batch 01 indeterminate; repaired: predecessor invalidators mapped onto ACTIVATION §7's three; disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#11d-post-ticket-design-review-rule` at rc.2:

```text
When a ticket adopts this method and claims its boundary has been processed, the
design-method closure claim should not rest on implementation status alone.

The processed boundary must be checked against its accepted design basis and
exact closure claim before the ticket claims closure under this method. This
check may be part of the ticket's normal verification; it does not require a
separate artifact, review round, or reviewer.

`TICKET_METHOD.md` remains the authority for ticket status, closure mechanics,
reopening, dependency handling, and follow-up ticket recording. This rule states
what the design check must cover when this method governs the ticketed
boundary.

That check must determine:

- whether the boundary stayed lawful under the current design and module assets
- whether the exact claim includes every causally applicable live requirement,
  accepted design relation, and retained predecessor claim
- whether the exact closure claim leaves competing or ambiguous authority on
  its acceptance path
- whether implementation established a material architectural decision with
  durable consequences that forecloses an admitted Product outcome
- whether any discovered issue falsifies the current claim or an applicable
  hard stop

The check reconstructs the complete selected function from governing
requirements through the accepted Ontology, Prime atoms, IACS, views, target
modules, implementation, and module-owned proof. It does not begin and end with
the previous review findings. Exact hashes establish subject identity; headings
and artifact presence establish location; green tests establish only the
properties they actually assert. None supplies a missing semantic relation or
substitutes a weaker property for the governed claim.

The complete selected function is the causal closure of the declared claim,
not the whole Product or the whole history of its construction. The existing
4B and 5E unchanged-boundary rules permit reuse of a current accepted Ontology,
design verdict and sufficient reconstruction evidence after checking their
exact scope, traces, applicability and invalidators. A new role, conversation
or review occurrence does not itself require re-authoring that evidence or
recreating the three views. Missing, stale or ambiguous coverage is not a
no-delta proof. A material changed relation or new counterexample requires
affected reconstruction and the applicable design gate, conserving supported
unaffected relations. This reuse does not weaken 5E's complete Ontology and
three-view coverage for a new or materially changed boundary.

The required consequence is:

- an issue that falsifies the current claim or applicable hard stop blocks the
  design-method closure claim
- ticket or review wording cannot narrow applicable active authority away
- boundary-local cleanup or commonization is absorbed only when required to make
  the current claim true, preserve singular authority, satisfy accepted design,
  or avoid the durable architectural foreclosure above
- other cleanup, recurrence, generality, and cross-boundary opportunities are
  repricing inputs; they do not automatically widen the subject, block its
  bounded claim, or require a follow-up ticket
- any repricing admitted by the owning authority enters through the smallest
  lawful re-entry point

This rule keeps design closure truthful without turning discovery into automatic
scope expansion. Current defects and hard stops remain blocking. Useful
observations may survive as repricing input. Unclaimed future capability and
optional cleanup do not become implicit work.

No processed ticket that has adopted this method should claim design-method
closure until this bounded design check is complete.

---
```

Successor, `DESIGN_MODULE.md#post-ticket-design-review` (with its subsections):

```text
When a ticket applies this profile to its boundary and claims that
boundary has been processed, the design-method closure claim should not rest on
implementation status alone (P6, P2;
rc.2 #11d-post-ticket-design-review-rule). The processed boundary is checked
against its accepted design basis and exact closure claim before the
ticket claims closure under this profile. The check may be part of the
ticket's normal verification; it does not require a separate artifact,
review round or reviewer. TICKETS remains the authority for ticket status,
closure mechanics, reopening, dependency handling and follow-up ticket
recording; this rule states what the design check covers when this
profile governs the ticketed boundary.

The check determines whether the boundary stayed lawful under the current
design and module assets; whether the exact claim includes every causally
applicable live requirement, accepted design relation and retained
predecessor claim; whether the exact closure claim leaves competing or
ambiguous authority on its acceptance path; whether implementation
established a material architectural decision with durable consequences
that forecloses an admitted Product outcome; and whether any discovered
issue falsifies the current claim or an applicable hard stop (P6, P4b).

The check reconstructs the complete selected function from governing
requirements through the accepted Ontology, Prime atoms, IACS, views,
target modules, implementation and module-owned proof; it does not begin
and end with the previous review findings. Exact hashes establish subject
identity; headings and artifact presence establish location; green tests
establish only the properties they actually assert. None supplies a
missing semantic relation or substitutes a weaker property for the
governed claim (P6; EVALUATION §1).

The complete selected function is the causal closure of the declared
claim, not the whole Product or the whole history of its construction. The
unchanged-boundary rules of §5 and §7 permit reuse of a current accepted
Ontology, design verdict and sufficient reconstruction evidence as closed
results under [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse),
which owns reuse and its three invalidators: the check confirms their
exact scope, traces and applicability, and that none of those invalidators
has occurred. The invalidators those rules name are instances of
ACTIVATION §7's three, and no fourth exists: a reprice of a governing
source, which invalidates only the affected Ontology relations and
downstream projections until their impact is re-evaluated (§5), is a
changed basis for those relations and projections; a later candidate
that satisfies the applicability criteria and could materially alter the
lawful frontier (§7) is a material input change for the affected
selection evidence; new evidence or another material dimension that
defeats a dominance relation (§7) is a material input change for that
relation. A new role, conversation or review occurrence is not one of
them, so it does not itself require re-authoring that evidence or
recreating the three views. Missing, stale or ambiguous coverage is not a
no-delta proof. A material changed relation or a new counterexample is an
instance of that section's material input change: it requires affected
reconstruction and the applicable design gate, conserving supported
unaffected relations. This reuse does not weaken §7's complete Ontology
and three-view coverage for a new or materially changed boundary (P2, P6).

The required consequence: an issue that falsifies the current claim or an
applicable hard stop blocks the design-method closure claim, because that
claim is then `falsified`, which never becomes `satisfied`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)), and a hard stop is not
waived ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). Whether
a finding also blocks the boundary's current promotion is decided by
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion).
The check's determinations above are this profile's domain triggers for
that section's four conditions: a discovered falsifying issue for the
first; competing or ambiguous authority on the acceptance path for the
second; a boundary that is not lawful under the current design and module
assets, or a claim that omits a causally applicable requirement, accepted design
relation or retained predecessor claim, for the third; and the durable
architectural foreclosure for the fourth. Applied to this check: ticket or
review wording cannot narrow applicable active authority away;
boundary-local clean-up or commonisation is absorbed only when required to
make the current claim true, preserve singular authority, satisfy accepted
design, or avoid the durable architectural foreclosure above; other
clean-up, recurrence, generality and cross-boundary opportunities are
observations outside the exact claim, which EVALUATION §5 returns as
repricing inputs that do not automatically widen the subject, block its
bounded claim or require a follow-up ticket; and any repricing admitted by
the owning authority enters through the smallest lawful re-entry point
(SPEC_METHOD §4) (P6, P2). The rule keeps design closure truthful without turning discovery
into automatic scope expansion: current defects and hard stops remain
blocking, useful observations may survive as repricing input, and
unclaimed future capability and optional clean-up do not become implicit
work. No processed ticket that applies this profile should claim
design-method closure until this bounded design check is complete.
```

Successor, `ACTIVATION.md#7-closed-result-and-reuse` (with its subsections):

```text
A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.

### Transition evidence

A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and, where an assessor was
activated, the assessor's recommended disposition, with the decision
owner's disposition beside it once one is made (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b; provenance rc.2 SPEC_METHOD
#transition-evidence-and-proof-cadence).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).
```

Successor, `EVALUATION.md#when-a-finding-blocks-promotion` (with its subsections):

```text
A finding is a defect a review reports against the exact claim it
evaluated (§4). Blocking current promotion is the decision owner's act
over that finding (§4, Result and triage projection). This section is the
one statement of when a finding can block; profiles and work carriers
refer to it and add only their domain triggers.

A review verdict is bounded by the exact reviewed claim and its applicable
hard stops ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). A
finding can block current promotion only when it:

1. falsifies that claim;
2. exposes competing or ambiguous authority on the claim's acceptance
   path;
3. violates applicable active authority, safety or retained accepted
   behaviour; or
4. establishes a material architectural decision with durable
   consequences that forecloses an admitted Product outcome.

These conditions are necessary. Which of them suffice is decided as
follows:

| Consumed condition | Effect on the current promotion boundary |
|---|---|
| a valid falsification of a mandatory claim governed by a non-waivable hard stop | the boundary blocks, whatever the assigned priority or the decision cutoff |
| any other finding meeting one of the four conditions | the decision owner decides blocking from the exact affected claim, the governed outcome or decision the work serves ([ACTIVATION §1, Intake](ACTIVATION.md#intake)), the applicable hard stops and the Product-owned cutoff policy; below that cutoff no block follows mechanically, and an accepted residual is retained explicitly |
| a finding meeting none of the four conditions | it does not block |
| an observation outside the exact reviewed claim | repricing or re-entry input, returned as §4 states: by itself it does not widen the reviewed subject, block its bounded claim, or require a new ticket, artifact, review round or implementation increment |

Severity selects neither priority nor a block mechanically, and priority
neither erases severity nor waives a hard stop. The decision cutoff is the
adopting Product's policy; this member sets no cutoff (P6, P2; conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)'s
blocking conditions). The table is new tier-1 law: it states for the
decision owner of any promotion boundary the rule that the predecessor's
[Executive promotion constraint projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection)
states for the Executive only, which
[EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md#promotion-constraint-projection)
keeps as its instance. Purpose and material
relation: the method stated these conditions in a work carrier, a design
profile and the Executive profile, so an actor reconciled three texts; one
statement gives every review consumer the same answer, and the conditions
keep a bounded review from blocking on observations outside its claim
while a non-waivable hard stop still blocks.
```

Extra, rc.2 `DESIGN_MODULE_METHOD.md` lines 354-358:

```text
relation identities plus a version or basis that makes source change,
staleness, and the affected projection set decidable. A reprice of a governing
source invalidates only the affected Ontology relations and downstream
projections until their impact is re-evaluated. Code, tests, generated schemas,
or a single implementing agent cannot self-ratify missing Ontology authority.
```

Extra, rc.2 `DESIGN_MODULE_METHOD.md` lines 617-621:

```text
frontier prevents selection; an immaterial residual records why it cannot change
the current decision. A later candidate that satisfies the applicability
criteria and could materially alter the lawful frontier invalidates the affected
selection evidence and re-enters this relation.
```

Extra, rc.2 `DESIGN_MODULE_METHOD.md` lines 657-661:

```text
and it is strictly better on at least one. A material unknown that could reverse
the relation prevents dominance and remains a gap. A dominated candidate cannot
be selected unless new evidence or another material dimension invalidates the
dominance relation. Therefore a local rebuild of generic mechanics is
inadmissible when an existing lawful foundation composition dominates it.
```

Extra, `standards/ACTIVATION.md#7-closed-result-and-reuse`:

```text
A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.
```


### Row `REFERENCE_FRAME_METHOD.md#return-a-closed-result` (earlier reading: batch 03 changed; repaired: need not be transferred; shared mechanical evidence pointed to EVALUATION §3; disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#return-a-closed-result` at rc.2:

```text
The result identifies the frame and activation, subject, basis, evaluation,
actor, evidence, verdict, residual uncertainty, and invalidation conditions.
The frame's internal working context does not need to be transferred when its
closed result and provenance are sufficient for the consuming decision.

An unchanged consumer checks exact applicability and reuses a valid closed
result. Role, conversation or resumption changes alone do not invalidate it.
Changed material inputs or a declared revising observation invalidates the
affected result before reliance; preserve its predecessor/successor relation
and any demonstrably independent surviving results. Required independent
evaluations may share valid mechanical evidence but must still supply their
own sufficiently acquired evidence and judgments under the declared
independence conditions.
```

Successor, `ACTIVATION.md#7-closed-result-and-reuse` (with its subsections):

```text
A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.

### Transition evidence

A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and, where an assessor was
activated, the assessor's recommended disposition, with the decision
owner's disposition beside it once one is made (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b; provenance rc.2 SPEC_METHOD
#transition-evidence-and-proof-cadence).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).
```

Extra, `standards/EVALUATION.md#3-independent-assessment`:

```text
A constructor's self-review is construction output, not assessment. Where
promotion needs independent assessment, the assessor evaluates the exact
live subject, authority paths, proof and installed state, not the
constructor's summary (P6, and P0 with its premise that a step's output is
a candidate until evaluated; instance premise (c) of §1 Foundation to law;
conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)).
This section decides what counts as independent assessment. Which
boundaries require it is a policy choice of the Spec Method, owned by
[TICKETS §7 Execution and verification authority separation](TICKETS.md#execution-and-verification-authority-separation-up-007);
a governing basis may add boundaries.

Protocol: where method qualification applies
([§7 Method self-qualification](#method-self-qualification)), the subject is
frozen by identity before material reference exposure; elsewhere it is
stabilised by an immutable identity or an equivalent exact-subject relation
sufficient for the claimed assessment. The assessor records its
expectations from the governing source before opening the candidate; it
reads the subject at that identity or relation, never a mutable working
tree; it makes no repair; it does not assess its
own authorship. Reusing the constructor's judgment does not satisfy
independence; shared mechanical evidence may be reused, judgment may not
(ACTIVATION §7). Any post-exposure revision is a declared intervention: it
is either a method constituent with its own qualification boundary or a new
qualification subject, and it cannot retroactively make the original
frozen construction pass. This law prescribes no actor type or count,
review-round count, engine, prompt or orchestration (UP-022).

Author identity is the party responsible for the content of a realised
subject. It is distinct from actor identity, whoever performs one
operation, which is an identity and not an authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)).
Authorship is one of the conditions on
which the independence of an assessment rests; the evidence conditions are
the other (P6, P3; provenance: the definition moves here from the build
binding terms of SPEC_METHOD §11, which refers to it).

Independence rests on authorship and on the evidence conditions above, not
on a new context. The assessor may read the same governing sources as the
constructor. A fresh context alone establishes no independence, and it
supplies no review authority the author lacks: an author that opens a
fresh context to review its own candidate is still its author, and its
review is self-review, which stays construction output and cannot be
relabelled as independent assessment (P6; UP-007 applied to a fresh
context). A contribution received from another author stays that
author's wherever it is carried, and that author's reading of it supplies
no independent acceptance of it (P6).

Independence across actor families is declared, not assumed. Whether two
activations of one model family are independent for a semantic judgment is a
policy the governing basis states for the claim; the default where it is not
stated is that they are not independent.
```


### Row `IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004` (earlier reading: batch 03 indeterminate: owner section not supplied; disposition `conserved`)

Predecessor, `IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004` at rc.2:

```text
Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity, or reachable code path. Its identity
preserves owner, kind, governed subject, scope, and governing basis.

Composition, delegation, adapters, projections, wrappers, and registries may
restrict or faithfully carry admitted authority. They must not silently widen
scope, add a role, increase cardinality, change kind, or reconstruct authority
from actor identity, payload shape, or available capability. Elevation,
transfer, split, merge, proxy grant, revocation, and retirement require an
explicit authority decision and identifiable basis.

Human authority may act directly or through an explicitly admitted bounded
proxy. Proxy actor identity and human-authority identity remain distinct;
graph-native surfaces may project the relation as `F_H`. A proxy grant names
its grantor, actor, subject, scope, permitted and excluded decisions, validity,
delegation rights, revocation, and provenance.

A direct or proxied decision preserves its source, subject and basis, acting
identity and mode, scope, change class, disposition, and supersession. Recording
a ruling cannot widen it. Proxy authority does not make implementer self-review
independent or confer unrelated runtime or domain authority.

---
```

Successor, `IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004` (with its subsections):

```text
Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity or reachable code path. Its identity
preserves owner, kind, governed subject, scope and governing basis (P6,
P3; rc.2 #authority-identity-and-conservation-stdo-up-004; the Authority
object and its kinds are FOUNDATIONS §2).

What composition, delegation, adapters, wrappers and registries may do
with admitted authority, what creates none, and which changes need an
explicit authority decision are stated once at
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority. Its instances for an identity-bearing relation are
these: a projection is such a carrier, and actor identity, payload shape
and available capability create no authority (P6, P4b).

Human authority may act directly or through an explicitly admitted
bounded proxy. Proxy actor identity and human-authority identity remain
distinct; a profile's own surfaces may project the human-authority
relation under that profile's term (PROFILES). A proxy grant names its
grantor, actor, subject, scope, permitted and excluded decisions,
validity, delegation rights, revocation and provenance (P6, P3).

A direct or proxied decision preserves its source, subject and basis,
acting identity and mode, scope, change class, disposition and
supersession. Recording a ruling cannot widen it. What a proxy can never
decide is stated at
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds); for
authority identity its instances are that proxy authority does not make
implementer self-review independent
([EVALUATION §3](EVALUATION.md#3-independent-assessment)) and confers no
unrelated runtime or domain authority (P6, P4b). EVALUATION §5 applies
this law to acceptance.
```

Extra, `standards/FOUNDATIONS.md#authority-kinds`:

```text
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


### Row `REFERENCE_FRAME_METHOD.md#canonical-compression` (earlier reading: batch 03 indeterminate: owner section not supplied; disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#canonical-compression` at rc.2:

```text
A human or computational actor has finite context, finite attention, finite
time, and bounded capability. A material workspace may contain more relevant
truth, history, topology, authority, and evidence than one actor can evaluate
at once.

The Reference Frame Method makes that limit explicit:

```text
declared evaluation family
  + exact workspace and topology basis
  + finite material relations and coordinates
  + applicable invariants and authorities
  + admissible evidence and exclusions
  + actor capability envelope
  = activated reference frame
  -> satisfied | falsified | indeterminate | out_of_frame | invalid_basis
```

A project engages a body of work through a declared frame set:

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

The reference frame is the atomic engagement unit. Frame-set selection,
activation, evaluation, conjunction, translation, coverage, and revision are
separate method functions. A frame does not need to contain a universal theory
of its possible relationships before it can support a bounded evaluation.

`Atomic engagement unit` names the unit that can be activated and evaluated as
one bounded context. It does not assert that every relation inside the frame is
one irreducible semantic atom. A frame may carry several semantic atoms and
several owner relations without merging their meaning or authority.

---
```

Successor, `REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit` (with its subsections):

```text
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
of [FOUNDATIONS §2](FOUNDATIONS.md#imports-between-members), which states
what an import is, its direction and loss, and that it transfers no
ownership and confers no authority; this declaration restates none of
that. FOUNDATIONS, ACTIVATION and EVALUATION declare no bounded-context
identity, so each row's source context is its member; the target context
and its owner are declared in Scope above (P1, P3).

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

Scope bounds what
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
```

Extra, `standards/FOUNDATIONS.md#results`:

```text
Every performed evaluation returns one value of the core result algebra,
directly or as a refined value mapped into it (P5):

| Value | Meaning |
|---|---|
| `satisfied` | the declared predicate holds on the exact basis |
| `falsified` | a declared counterexample defeats it |
| `indeterminate` | the available admissible evidence cannot decide it |
| `out_of_frame` | the evaluation requires an undeclared material relation or capability |
| `invalid_basis` | the subject or basis cannot support the evaluation |

This core is the only one. Results of constraints, judgments, frame
evaluations, stops, work steps and effects are stated in it or in a
refinement mapped into it, so that results from any members combine under
one rule ([Conjunction of results](#conjunction-of-results)). Purpose and
material relation: no combination can report success while a failure, an
undecided question, an unperformed evaluation or an uncertain effect
remains, and none of these can be mistaken for another (P5, P6).

Recording. A result records its core value together with the predicate
evaluated and the original domain outcome, which is the refined value
where a refinement produced it. A mapping into the core never owns domain
meaning: the member, profile or adopting Product that defines the refined
value keeps it, and a consumer that needs the domain distinction reads the
domain outcome, never the core value alone (P1, P6).

Standing. The standing of a result is what it establishes about its
predicate; it is distinct from the standing of a commitment (§1). Only
`satisfied` establishes the predicate. `falsified` establishes that the
predicate fails and names the counterexample. `indeterminate`,
`out_of_frame` and `invalid_basis` establish neither, and each names what
would decide: the evidence, the missing relation or capability with its
owner where the subject gives one, or the basis repair. By support for the
predicate, `satisfied` stands above each other value, and the other four
are not ordered among themselves.

No refinement or mapping raises a result's standing (P5, P6):

- a falsified or failed result never maps to a satisfied or successful one;
- a result that admissible evidence cannot decide never maps to
  `satisfied`;
- an evaluation that was not performed stays distinct from one whose
  evidence cannot decide: it has no
  [closed result](ACTIVATION.md#7-closed-result-and-reuse), and it is never mapped
  to `indeterminate` or to any other core value;
- an effect whose completion is unknown never maps to no effect or to
  completed.

Not performed. An evaluation that is required or planned and was not
performed has no closed result; an actor cannot report an evaluation it
did not perform (P6). Nothing is coerced to success: a failed,
indeterminate, out-of-frame, out-of-scope or invalid-basis result follows
the declared result algebra and returns its own value under it, never
`satisfied`, and a missing result, being no result, enters every
conjunction over it as a gap: a planned assessment without a closed result
where an assessment was planned, and uncovered coverage where none was.
This
conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
whose five values the table restates unchanged, and
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
whose rule that a failed, missing, indeterminate, out-of-scope or
invalid-basis result follows the declared algebra rather than being
coerced to success is the sentence before; both are restated here once.
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) states
RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this core and neither
defines it again.

Refinements. A member, profile or adopting Product that needs finer
outcomes defines a refinement. The refinement names the question it
answers and the predicate its mapping is for, and maps every refined value
to exactly one core value. No outcome exists outside the core; a
refinement adds no core value and keeps the pressure of `indeterminate`,
`out_of_frame` and `invalid_basis` explicit. Where a refined value would
map to one of two core values according to its cause, the cause is part of
the refined value and each resulting value maps once (P5, P1). A further
refinement, by a member, profile, project or adopting Product, may split a
refined value by cause. The parent-value rule governs every such split:
each child value names its parent value and its cause and keeps its
parent's core value; a child that needs a different core value needs a
different parent value, which only the owner of the parent declares; and
no child takes `satisfied` from a parent that is not `satisfied`. No
further refinement raises a result's standing (P5, P6, P1). Purpose and
material relation: a consumer that reads a parent value reads the same
core value from each of its children, so a split by cause adds a domain
distinction and never changes what the parent establishes (P5, P6). The
refinements for admission, activation and steps are
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition); each other
member, profile and adopting Product states its mapping where it defines
its values.

Availability, assessment and acceptance are separate results, each with its
own predicate: that a step produced a candidate; that the candidate meets
its declared criteria; and that the
[decision owner](ACTIVATION.md#roles-and-delegation) accepts it at its
boundary. A step having produced a candidate never maps to the candidate's
fitness or acceptance, and acceptance is never inferred from a successful
step (P6; [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition),
[EVALUATION §4](EVALUATION.md#4-review-results) and
[§5](EVALUATION.md#5-acceptance)).

Out of frame or indeterminate. The boundary between these values is drawn
on what the activated frame declares and on what the step did with it (P5,
finite capacity and graceful total handling; the material relation drawn
is the three-way out_of_frame boundary: capability not declared, capability
declared and exercised, capability declared and not exercised; rc.2 RF
#rf-012-closed-results). Three cases; the first two name core values, and
the third names none:

- `out_of_frame` when the claim requires a material relation or an
  evaluator capability that the activated frame does not declare. The
  result names the missing relation or capability, its owner where the
  subject gives one, and the reconfiguration pressure it creates
  ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement); rc.2 RF
  #reconfigure-when-necessary). A term the claim depends on and the frame
  leaves undefined is an undeclared material relation: its meaning can
  alter the result and it enters through no declared input (rc.2 RF
  #material-relation, RF-003; P1). Whether the step exercised anything is
  irrelevant to this value; the ground is the missing declaration.
- `indeterminate` when the available admissible evidence cannot decide the
  claim (rc.2 RF-012). The result names the evidence that would decide, as
  its residual uncertainty (rc.2 RF #return-a-closed-result). Where the
  claim also depends on an undeclared relation or capability,
  `out_of_frame` and `indeterminate` each have a lawful ground; the result
  names the value it returns and that ground, and this boundary excludes
  neither (P5).
- no value of its own when the step did not exercise a declared capability
  the evaluation requires. A result is returned wherever a sufficient
  evaluation or an applicable judgment exists without that capability,
  identifying its evidence, verdict and residual uncertainty like any
  closed result (rc.2 RF #rf-012-closed-results, #return-a-closed-result):
  a counterexample found by what was exercised, as when source inspection
  falsifies A in a claim of A and B, returns `falsified`, and common
  agreement cannot discard it (rc.2 RF #result-conjunction). Where none
  exists because the capability was not exercised, the evaluation was not
  performed and has no result: the step's stop state carries it,
  `incomplete` under
  [construction availability](ACTIVATION.md#construction-availability), and
  its work state ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart))
  carries the unexercised capability as a residual (P6). In either case
  the unexercised part, B above, has no result: in every conjunction over
  it, it is a planned assessment without a closed result, and the known
  failure A survives with it ([Conjunction of results](#conjunction-of-results)).
  The evaluation's result and the step's stop state answer different
  questions, so the step's stop value never becomes the evaluation's
  result.

Foundation to law for results and their combination (family F3). The
table covers every rule of §4 and the result grounds of §2 Imports
between members, in the format of
[Foundation to law](#foundation-to-law), which states the standing of its
consequences. Purpose and material relation: a reader of §4 sees which
commitments each result rule rests on and which choices it adds, with their
owners (P6, P2). Instance premises, which the commitments do not supply:
(i) an evaluation declares its predicate, subject and basis; (ii) results
of several evaluations, steps or members are combined into one decision;
(iii) members, profiles and adopting Products need outcomes finer than the
core.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section | 3, 9 |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule | 9 |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it | 6, 3 |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section | 9 |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it | 3, 6 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](EVALUATION.md#5-acceptance) names | 9 |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](ACTIVATION.md#construction-availability), construction availability | 7, 9 |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none | 6 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none | 3, 9 |
| P3 (independent), P5 (derived from P0 and P6), P6 (independent); (i), (ii) | a result supports its predicate only on the basis it binds, so a component held only on another basis has, on the basis the composite requires, no performed evaluation and is a gap, while an evaluation performed on a basis that cannot support it decides its own predicate as `invalid_basis`; one component is never answered both ways | [Conjunction of results](#conjunction-of-results), Stale results | none | 3, 9 |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](#4-algebra) Composition; [Conjunction of results](#conjunction-of-results), Composition of results; [RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation | 3, 4 |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation) | 3 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](#4-algebra) Reference versus body | none | 6, 7 |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it | 3 |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the accepted design of the realisation that would share it, which [DESIGN_MODULE §5](DESIGN_MODULE.md#capability-and-foundation-selection-up-023) refines for software design where that profile is selected | 4 |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim | 3 |

RF-012 in [REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.
```


### Row `REFERENCE_FRAME_METHOD.md#revision-actions` (earlier reading: batch 03 indeterminate: whether RF-005, RF-011 and #return-a-closed-result imply reopening by default; disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#revision-actions` at rc.2:

```text
A revision may:

- clarify activation or evidence acquisition;
- change the capability envelope;
- add or remove a material relation;
- split an overloaded frame;
- merge duplicative frames where capability and authority remain sound;
- add intentional overlap;
- add or revise a conjunction or translation;
- retire a frame whose evaluation family is no longer material; or
- revise the project evaluation inventory.

Every material revision changes frame identity or revision coordinates and
states which prior activations, results, and coverage claims require
reevaluation.

---
```

Successor, `REFERENCE_FRAME.md#revision-actions` (with its subsections):

```text
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
```

Extra, rc.2 `REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates`:

```text
Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.
```

Extra, rc.2 `REFERENCE_FRAME_METHOD.md#rf-011-topology-mutation-and-recharting`:

```text
An activated frame declares the topology changes capable of invalidating its
coordinates or materiality judgment. A detected material topology mutation
causes reevaluation, frame revision, or recharting before the previous result
is reused.
```

Extra, rc.2 `REFERENCE_FRAME_METHOD.md#return-a-closed-result`:

```text
The result identifies the frame and activation, subject, basis, evaluation,
actor, evidence, verdict, residual uncertainty, and invalidation conditions.
The frame's internal working context does not need to be transferred when its
closed result and provenance are sufficient for the consuming decision.

An unchanged consumer checks exact applicability and reuses a valid closed
result. Role, conversation or resumption changes alone do not invalidate it.
Changed material inputs or a declared revising observation invalidates the
affected result before reliance; preserve its predecessor/successor relation
and any demonstrably independent surviving results. Required independent
evaluations may share valid mechanical evidence but must still supply their
own sufficiently acquired evidence and judgments under the declared
independence conditions.
```

Extra, `standards/ACTIVATION.md#7-closed-result-and-reuse`:

```text
A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.
```


### Row `SPEC_METHOD.md#ambiguity-governance-rule` (earlier reading: batch 04 indeterminate: the hard-stop classes are delegated to ACTIVATION §4, not supplied; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#ambiguity-governance-rule` at rc.2:

```text
`SPEC_METHOD.md` owns the substrate-neutral ambiguity-governance bounded
context `urn:stdo:bounded-context:ambiguity-governance` under the selected
complete STDO basis. Graph/runtime shorthands such as `F_D`, `F_P`, and `F_H`
remain in the graph-native ODD context unless an explicit relation imports or
translates them.

Spec-driven development is not only a derivation pipeline. It is a governed
disambiguation pipeline.

The point of the upstream chain is to progressively reduce ambiguity:

- goals narrow active priority and work-wave focus
- intent narrows direction and scope
- product narrows current realization shape and terms
- requirements narrow constitutional obligation
- build-tenant or stack choice narrows executable realization class
- design narrows structural interpretation
- implementation narrows local realization detail

This narrowing is not uniform. The methodology distinguishes between:

- **major ambiguity**: ambiguity that materially changes architecture, stack,
  product boundary, execution/deployment admissibility, public contract shape,
  or other downstream realization law
- **micro ambiguity**: local implementation choice that remains inside an
  already-governed design boundary

Major ambiguity must always be surfaced and governed. It may not remain hidden
inside informal operator judgment, ambient precedent, or silent model choice.

Therefore, at each major boundary the process must:

- detect and record the major ambiguity that remains or is newly introduced
- identify the affected invariant, asset, or decision boundary
- record the decision taken if work proceeds
- record whether the ambiguity was resolved, carried forward, escalated, or
  blocked

Ambiguity detection is mandatory. Blocking is policy.

**Lawful Probabilistic Processing**
(`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing`) is
bounded non-human processing permitted by declared policy to carry or resolve
declared ambiguity. **Human Adjudication**
(`urn:stdo:concept:ambiguity-governance:human-adjudication`) is explicit human
judgment admitted by authority to resolve declared ambiguity where policy or
risk appetite requires it.

The default governance model is:

- ambiguity may be carried or decided by lawful probabilistic processing when
  project policy allows it
- ambiguity may be escalated to explicit human adjudication when project policy
  requires it
- the threshold between those actions is determined by declared risk appetite,
  not by silent convenience

Projects may therefore choose different ambiguity-handling policies. A lower
risk appetite escalates more major ambiguity to explicit human judgment. A
higher risk appetite permits more bounded probabilistic decision-making. In either
case, the ambiguity and the decision must be recorded.

Some conditions are not optional ambiguity decisions and therefore remain hard
stops regardless of risk appetite. Typical hard-stop classes include:

- violated invariant or guarantee
- absent required authority surface
- missing declared capability for an executional or operational stage
- undeclared irreversible side effect
- explicit policy gate requiring human approval

The methodology is therefore not "eliminate all ambiguity before work." It is
"make ambiguity visible, govern it explicitly, and reduce it progressively until
downstream realization is sufficiently constrained."

---
```

Successor, `SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle` (with its subsections):

```text
This member owns the substrate-neutral ambiguity-governance bounded context
`urn:stdo:bounded-context:ambiguity-governance` under the selected complete
basis; a profile's runtime shorthands for its own frames stay in that
profile's context unless an explicit relation imports or translates them
(P3, P1; rc.2 #ambiguity-governance-rule).

Spec-driven development is not only a derivation pipeline; it is a governed
disambiguation pipeline. The upstream chain progressively reduces
ambiguity: goals narrow active priority and work-wave focus; intent narrows
direction and scope; product narrows current realisation shape and terms;
requirements narrow constitutional obligation; build-tenant or stack
choice, a tenant's binding under §11, narrows the executable realisation
class; design narrows structural
interpretation; implementation narrows local realisation detail (P2).

The narrowing is not uniform. Major ambiguity materially changes
architecture, stack, product boundary, execution or deployment
admissibility, public contract shape or other downstream realisation law;
micro ambiguity is a local implementation choice inside an already-governed
design boundary. Major ambiguity is always surfaced and governed; it may
not remain hidden inside informal operator judgment, ambient precedent or
silent model choice. At each major boundary the process detects and
records the major ambiguity that remains or is newly introduced; identifies
the affected invariant, asset or decision boundary; records the decision
taken if work proceeds; and records whether the ambiguity was resolved,
carried forward, escalated or blocked. Those outcomes are `resolved`,
`carried`, `escalated` and `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), which
gives each its core value for the predicate "the declared ambiguity is
resolved on the exact basis". Only `resolved` is `satisfied`, so a later
boundary rests no dependent claim on an ambiguity that is carried,
escalated or blocked as if it were resolved. Ambiguity detection is
mandatory; blocking is policy (P6, P5).

Lawful probabilistic processing
(`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing`)
is bounded non-human processing permitted by declared policy to carry or
resolve declared ambiguity. Human adjudication
(`urn:stdo:concept:ambiguity-governance:human-adjudication`) is explicit
human judgment admitted by authority to resolve declared ambiguity where
policy or risk appetite requires it. That admission makes an operation
human adjudication. A person who relays, records or carries out a step
does not adjudicate by doing so, and a person who carries or decides a
declared ambiguity where policy permits it, without that admission, acts
under the policy and recording that govern lawful probabilistic
processing; who performs an operation does not decide its kind (§11, rule
2). The default governance model: ambiguity
may be carried or decided by lawful probabilistic processing when project
policy allows it; it may be escalated to explicit human adjudication when
project policy requires it; the threshold between those actions is
determined by declared risk appetite, not by silent convenience. Projects
may therefore choose different ambiguity-handling policies: a lower risk
appetite escalates more major ambiguity to explicit human judgment; a
higher one permits more bounded probabilistic decision-making. In either
case the ambiguity and the decision are recorded.

The hard stops of [ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)
hold regardless of risk appetite. The method is therefore not "eliminate
all ambiguity before work"; it is "make ambiguity visible, govern it
explicitly, and reduce it progressively until downstream realisation is
sufficiently constrained".

The operational lifecycle sufficiency rule (§2) is this governance applied
to lifecycle phases: an unanswered phase is a recorded gap, never a silent
absence.
```

Extra, `standards/ACTIVATION.md#4-totality-and-refinement`:

```text
Next moves after any non-satisfied result are named in advance: continue
within the current contract when supported; refine; recover; yield; re-enter
the owning relation; terminate. Each admitted condition class has a declared
next move, including an explicit unknown class. Total handling does not
claim that every external condition is recognised, that an invoked provider
terminates, or that every request can be completed. A hanging external call,
an unsatisfiable demand and a lost post-effect response are three different
cases and none is solved by adding a value to the algebra.

Which outcome of [§3 Ambiguity outcome](#ambiguity-outcome) a declared
ambiguity takes is decided by the applicable ambiguity policy and its risk
appetite, an added choice; for this method the owner of the default
policy is [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle),
and this section states none. The outcome is recorded either way.

Hard stops. Some conditions are not optional ambiguity decisions and
remain hard stops regardless of risk appetite. Typical hard-stop classes
include: a violated invariant or guarantee; an absent required authority
surface; a missing declared capability for an executional or operational
stage; an undeclared irreversible side effect; and an explicit policy gate
requiring human approval. A hard stop halts the work at its condition whatever the policy:
for a declared ambiguity, with the §3 Ambiguity outcome `blocked`;
otherwise, as a stop of [§1 Transitions](#transitions), Stops. This
section owns the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies them to the method's chain of authority surfaces (P6, P5;
provenance rc.2
[Ambiguity Governance Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule)).

Reconfiguration. An out_of_frame, invalid_basis, repeated indeterminate or
incompatible result causes one of: supply the missing admissible evidence;
select another actor inside the frame's capability envelope; activate
another existing frame; refine or extend a frame declaration; revise the
frame set (REFERENCE_FRAME §10); change the evaluation; or re-enter the
governing product or method relation. The next move follows the cause; a
difficult evaluation alone does not prove that another frame is required
(P5, P2; rc.2 RF #reconfigure-when-necessary).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#closure` (earlier reading: batch 05 indeterminate: the closure condition is delegated to TICKETS §7, not supplied; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#closure` at rc.2:

```text
Evaluate only the obligations applicable to the exact selected outcome and
engagement branch. A listed frame or available testing family does not make
its claim applicable. Every applicable obligation must be satisfied with valid
evidence and required J/O, with no active non-closure condition under
`TICKET_METHOD.md#condition-based-closure-and-reuse`. A closed indeterminate
result or a review event does not satisfy an unresolved obligation.

A project has applied this baseline to one outcome when:

1. existing project authority admits and projects the exact frame basis;
2. the complete selected STDO and Reference Frame Method remain the governing
   sources;
3. Executive, Worker, and Reviewer are available finite evaluation frames,
   activated only where applicable, not hierarchy or actor identities;
4. activation refusal remains distinct from Worker results, and every Worker
   result maps exclusively from one closed Reference Frame Method result and
   returns to its declared consumer, first to Executive in the coordinated
   branch;
5. existing work authority determines whether an exact candidate requires
   independent review; the coordinated Executive activates Reviewer where
   required, while the sufficient direct branch adds no such activation;
6. required Reviewer assessment binds the exact subject, evidence population,
   verdict, evidence-bound technical triage, and independence conditions;
7. an activated Executive consumes closed results and technical triage against
   the complete Product view and current MVP or release mandate, keeps severity, priority,
   frame result, and boundary effect distinct, and applies only the existing
   `STDO-UP-020` disposition and continuation relation;
8. specialist frames and result relations cover every known material
   evaluation and interaction or retain an explicit residual;
9. frame, basis, capability, evidence, and topology change can invalidate and
   rechart the configuration;
10. every material operation carries its existing owner's exact grant;
11. no new execution authority, local constitutional layer, actor topology,
    runtime, or universal completeness claim is inferred from the profile;
12. every material Product testing claim is assigned to an exact
    user-acceptance, end-to-end, integration, unit, or explicitly declared
    alternative frame rather than inferred from a suite label;
13. a user-outcome claim binds the declared user capability, exact Product
    subject, supported ordinary surface, environment, and observable outcome;
14. an end-to-end claim binds the exact deployed, installed, or otherwise
    runnable Product form and records the required authoritative causal path
    rather than accepting output equality through an unknown or forbidden path;
15. material interface and Product factors have a declared combinatorial
    population, adequate interaction strength, exercised scenario matrix, and
    explicit residual combinations;
16. unit-test evidence proves module-owned laws, including public module
    contracts, and its volume and strategy are proportional to useful
    discrimination of the module-bounded population rather than implementation
    size;
17. required paths have positive runnable-Product witnesses; the production
    closure excludes obsolete, rival, fallback, and bypass paths; and the
    assurance/source closure cannot falsely supply evidence or reintroduce a
    removed production path, while declared isolated test-only seams remain
    outside ordinary-path claims;
18. source or code coverage, test count, and aggregate green status do not
    substitute for Product, installed, path, composition, or user-frame proof;
19. test fixtures, mutations, sabotage, proof capture, and assurance tooling
    preserve or revalidate the exact subject they claim to evaluate;
20. owner-issued Product and runtime truth is acquired through the exact owner
    surface and evaluated by a separately derived oracle without a rival
    assurance-owned semantic interpreter;
21. counterexamples return a causally minimal supported frontier represented as
    one unique locus, a jointly established incomparable set, unresolved
    alternative frontiers, or `indeterminate` evidence;
22. every Product, Product Composition, Design, Design Component, Public
    Boundary, Entity, Operator, Owner, Effect, Reuse/Foundation, Install, and
    Proof family material to the outcome has an exact declaration or
    acquisition path, while every non-material or uncovered family has an
    authority-bound disposition;
23. every material cross-frame seam preserves or lawfully translates identity,
    coordinate and basis, carried value or evidence, lifecycle scope,
    authority, and provenance; and
24. no consumer-specific architecture, renamed local topology, runtime object,
    or component roster is inferred from the generic specialist set.

A project-defined frame configuration closes against
`REFERENCE_FRAME_METHOD.md`, the selected complete STDO cut, and its cited
existing project authorities. It need not claim conformance to this optional
baseline profile.
```

Successor, `EXECUTIVE_BASELINE.md#22-closure` (with its subsections):

```text
Only the obligations applicable to the exact selected outcome and
engagement branch are evaluated. A listed frame or an available testing
family does not make its claim applicable (ACTIVATION §1, Applicability).
The closure condition is
[TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse),
which this profile applies to the selected branch and does not restate: a
work item closes by that condition, not by a reviewer's approval
([EVALUATION §5](EVALUATION.md#5-acceptance)). Applied here, a closed
`indeterminate` result or a review event does not satisfy an unresolved
obligation, because `indeterminate` never maps to `satisfied`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) and a review's
occurrence is not the closing event (P5, P6; rc.2 #closure).

A project has applied this baseline to one outcome when (P6, P2):

1. existing project authority admits and projects the exact frame basis;
2. the complete selected method, REFERENCE_FRAME included, stays the
   governing source;
3. Executive, Worker and Reviewer are available finite evaluation frames,
   activated only where applicable, not a hierarchy or actor identities;
4. activation refusal stays distinct from Worker results, and every Worker
   result is one work-result value selected by its cause, maps to exactly
   one core value as ACTIVATION §3 states, and returns to its declared
   consumer, first to the Executive in the coordinated branch;
5. existing work authority decides whether an exact candidate requires
   independent review; the coordinated Executive activates the Reviewer
   where required, and the sufficient direct branch adds no such
   activation;
6. required Reviewer assessment binds the exact subject, evidence
   population, verdict, evidence-bound technical triage and independence
   conditions;
7. an activated Executive consumes closed results and technical triage
   against the complete Product view and the current MVP or release
   mandate, keeps severity, priority, frame result and boundary effect
   distinct, and applies only the existing disposition and continuation
   relation;
8. specialist frames and result relations cover every known material
   evaluation and interaction or keep an explicit residual;
9. frame, basis, capability, evidence and topology change can invalidate
   and rechart the configuration;
10. every material operation carries its existing owner's exact grant;
11. no new execution authority, local constitutional layer, actor topology,
    runtime or universal completeness claim is inferred from the profile;
12. every material Product testing claim is assigned to an exact
    user-acceptance, end-to-end, integration, unit or explicitly declared
    alternative frame rather than inferred from a suite label;
13. a user-outcome claim binds the declared user capability, the exact
    Product subject, the supported ordinary surface, the environment and
    the observable outcome;
14. an end-to-end claim binds the exact deployed, installed or otherwise
    runnable Product form and records the required authoritative causal
    path, rather than accepting equal output through an unknown or
    forbidden path;
15. material interface and Product factors have a declared combinatorial
    population, adequate interaction strength, an exercised scenario matrix
    and explicit residual combinations;
16. unit evidence proves module-owned laws, public module contracts
    included, with volume and strategy proportional to useful
    discrimination of the module-bounded population rather than to
    implementation size;
17. required paths have positive runnable-Product witnesses; the
    production closure excludes obsolete, rival, fallback and bypass paths;
    the assurance/source closure cannot falsely supply evidence or
    reintroduce a removed production path; and declared isolated test-only
    seams stay outside ordinary-path claims;
18. source or code coverage, test count and aggregate green status do not
    stand in for Product, installed, path, composition or user-frame proof;
19. test fixtures, mutations, sabotage, proof capture and assurance tooling
    preserve or revalidate the exact subject they claim to evaluate;
20. owner-issued Product and runtime truth is acquired through the exact
    owner surface and evaluated by a separately derived oracle, without a
    rival assurance-owned semantic interpreter;
21. counterexamples return a causally minimal supported frontier
    represented as one unique locus, a jointly established incomparable
    set, unresolved alternative frontiers, or `indeterminate`;
22. every one of the twelve families material to the outcome has an exact
    declaration or acquisition path, and every non-material or uncovered
    family has an authority-bound disposition;
23. every material cross-frame seam preserves or lawfully translates
    identity, coordinate and basis, carried value or evidence, lifecycle
    scope, authority and provenance; and
24. no consumer-specific architecture, renamed local topology, runtime
    object or component roster is inferred from the generic set.

A project-defined frame configuration closes against REFERENCE_FRAME, the
selected complete method cut and its cited existing project authorities. It
need not claim conformance to this optional profile (P6).
```

Extra, `standards/TICKETS.md#7-authority-judgment-closure-and-state`:

```text
The generic law is tier 1: a constructor's self-review is construction
output and the independent-assessment protocol is
[EVALUATION §3](EVALUATION.md#3-independent-assessment); acceptance as the
decision owner's disposition, and closure by stated condition rather than
by reviewer approval, is [EVALUATION §5](EVALUATION.md#5-acceptance); reuse
of a closed result is [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse).
This section states what those laws require of work carriers.
```


### Row `SPEC_METHOD.md#transition-evidence-and-proof-cadence` (earlier reading: batch 05 indeterminate; repaired: the assessor's recommended disposition is identified where an assessor was activated, the owner's beside it; disposition `conserved`)

Predecessor, `SPEC_METHOD.md#transition-evidence-and-proof-cadence` at rc.2:

```text
A reviewable transition identifies the exact candidate, affected relations,
changed realization paths, authority paths added or removed, retained and open
seams, focused proof, any required integration proof, explicit non-changes, and
the assessor disposition. Consumers choose the representation. Transition
evidence is a read model and does not become specification, design, or
admission authority.

Construction uses the cheapest focused proof capable of falsifying the active
relation. Expensive whole-candidate qualification occurs at a declared
candidate boundary rather than after every local edit, unless the affected
risk makes whole-candidate proof necessary.

A durable or reconstructable authority claim is not established solely by a
same-process proof when loss of incidental process state is a material
counterexample. Proof must destroy or exclude the incidental authority and
compare reconstructed semantic outcomes.
```

Successor, `ACTIVATION.md#transition-evidence` (with its subsections):

```text
A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and, where an assessor was
activated, the assessor's recommended disposition, with the decision
owner's disposition beside it once one is made (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b; provenance rc.2 SPEC_METHOD
#transition-evidence-and-proof-cadence).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).
```

Extra, `standards/ACTIVATION.md#disposition`:

```text
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


### Row `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` (earlier reading: batch 06 indeterminate: the packet gave the §6 heading's direct text, which is empty; the body is in its subsections; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` at rc.2:

```text
Executive is the profile frame for three inseparable duties over one governed
outcome:

1. **attention management** maintains the exact outcome and basis, Product-role
   map, evaluation inventory, dependency relation, unresolved frontier, actor
   envelopes, current MVP or release mandate, applicable triage policy, and
   residual boundary, then selects the smallest
   dependency-ready activation set sufficient for the next decision within the
   finite actor envelopes;
2. **evaluation orchestration** activates capable Workers, Reviewers, or
   specialists, preserves their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. **authorized action selection** assigns priority, determines the effect on
   the current promotion boundary, applies an existing disposition, and issues
   only the next already-authorized activation or action.

Executive does not contain the complete workspace, perform every evaluation,
or acquire Product meaning, implementation, mutation, acceptance, publication,
or other operation authority from the role. A material effect remains owned by
the actor carrying its exact operation grant.

An actor occupying Executive must not modify candidate, Product or worktree
bytes or perform an implementation effect. Filesystem or tool access and an
edit being small, test-only, reversible or apparently obvious supply no
exception. Mutation requires a separately activated Worker or Writer relation
with the exact operation grant, subject and write territory. A same-actor role
transition is explicit and recorded in the existing work carrier before the
effect; the actor is no longer acting as Executive for that effect. Recording
or delegating after an Executive edit cannot authorize it retroactively.

The attention cycle is:

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorized decision is ready:
    await decision-relevant input under Event-Driven Executive Attention
  record every closed result, technical triage, residual, and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts, and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

This relation requires no scheduler or frame engine. `M` may contain parallel
activations. Recursion follows declared evaluation dependencies and bounded
refinements; it does not nest or join undifferentiated copies of every frame.
The Executive retains the frontier and closed-result ledger in attention, not
the undocumented working context of every evaluator.

Severity supplied by Reviewer is evaluation evidence. Priority, current-boundary
effect, `STDO-UP-020` disposition, and subsequent action are Executive decisions.
They remain distinct ledger entries even when a Product-defined policy maps one
to another.

Every result returns to Executive, a declared conjunction, or another frame
through an explicit `D` relation. No lateral handoff, child completion, model
response, tool output, or shared actor implicitly activates another frame or
authorizes continuation. A consumer receives the closed result and its source
routes, not the child's hidden reasoning context.
```

Successor, `EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action` (with its subsections):

```text
### The three duties

The Executive is the frame for three inseparable duties over one governed
outcome (P0, P6, P2; rc.2 #executive-attention-evaluation-and-action):

1. attention management: it keeps the exact outcome and basis, the
   Product-role map, the evaluation inventory, the dependency relation, the
   unresolved frontier, the actor envelopes, the current MVP or release
   mandate, the applicable triage policy and the residual boundary, and it
   selects the smallest dependency-ready activation set sufficient for the
   next decision within the finite actor envelopes;
2. evaluation orchestration: it activates capable Workers, Reviewers or
   specialists, keeps their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. authorised action selection: it assigns priority, determines the effect
   on the current promotion boundary, applies an existing disposition, and
   issues only the next already-authorised activation or action.

The Executive does not contain the complete workspace and does not perform
every evaluation. It acquires no Product meaning, implementation, mutation,
acceptance, publication or other operation authority from the role. A
material effect stays owned by the actor that carries its exact operation
grant (P6, RF-002).

### No mutation while Executive

An actor occupying the Executive frame modifies no candidate, Product or
worktree bytes and performs no implementation effect. Filesystem or tool
access is no exception, and neither is an edit that is small, test-only,
reversible or apparently obvious. Mutation requires a separately activated
Worker or Writer relation carrying the exact operation grant, subject and
write territory. A same-actor role transition is explicit and is recorded in
the existing work carrier before the effect; for that effect the actor is no
longer acting as Executive. Recording or delegating after an Executive edit
cannot authorise the edit retroactively (P6, P3). This prohibition is this
profile's, and it applies wherever the executive configuration is selected
([ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Example; §7);
an operation grant covering a construction, status and checkpoint sequence
does not lift it
([ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)).

### Attention cycle

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorised decision is ready:
    await decision-relevant input (event-driven attention, below)
  record every closed result, technical triage, residual and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

The cycle needs no scheduler and no frame engine (RF-016). `M` may hold
parallel activations. Recursion follows declared evaluation dependencies and
bounded refinements; it does not nest or join undifferentiated copies of
every frame. The Executive holds the frontier and the closed-result ledger
in attention, not the undocumented working context of every evaluator (P0,
P4b, P2).

Severity supplied by the Reviewer is evaluation evidence. Priority,
current-boundary effect, disposition and the next action are Executive
decisions. They stay distinct ledger entries even where a Product-defined
policy maps one to another (P6, RF-007).

Every result returns to the Executive, to a declared conjunction or to
another frame through an explicit declared relation. That none of them
activates another frame or authorises continuation by itself is
[ACTIVATION §1 Admission](ACTIVATION.md#admission), applied here. A consumer receives the
closed result and its source routes, not the child's hidden reasoning
context (P6, P4a; ACTIVATION §7).

### Event-driven attention

Executive attention is event-driven by default. The Executive re-enters the
attention cycle for a decision-relevant closed result, a material exception
or changed basis, an owner request, or a declared deadline or checkpoint.
While Workers carry out their bounded grants and no other authorised
decision is ready, it waits. It does not repeatedly inspect unfinished work,
replay unchanged judgments or request status without a decision need (P0,
P2; rc.2 #event-driven-executive-attention).

It keeps the frontier, the return conditions and the valid evidence and
judgments. It refreshes affected support when a material observation
changes its basis, and revalidates the drift locks (below) before activation
and before disposition. Waiting waives no current-workspace verification,
evidence validity, required independent assessment, closed-result
consumption, or authority or closure duty (P6, P4b).

Where notification is unavailable or unreliable, or an actual supervision
obligation requires observation, the Executive uses bounded fallback
observation with a declared purpose, cadence or checkpoint, evidence target,
and stop or escalation condition. Silence proves neither progress nor
failure. A genuine blocker or material risk is investigated, with
intervention where required, within existing grants; unknown status alone
does not establish a stalled Worker (P5, P6).

Repeated no-progress observations, or returns with no new decision-relevant
evidence, require a bounded reassessment of the frame, grant, dependency or
evidence gap and a decision under existing authority. The Executive does not
keep polling or repeat the same repair on an unchanged basis (ACTIVATION §3,
Disposition). Reduced reasoning churn is not a lower-assurance path and is
no permission to reduce required actor capability; it introduces no
universal cost, budget or accounting gate (P2, P0; ACTIVATION §6).

### Drift locks

Before activation and before disposition, the Executive revalidates five
locks (P3, P6, P2; rc.2 #executive-drift-locks):

| Lock | Holds when |
|---|---|
| outcome lock | the selected Goal, Product outcome, boundary and lawful re-entry class, the current MVP or release mandate, and the triage policy are unchanged |
| basis lock | the subject, authority, dependency, configuration, topology, evidence, time and candidate coordinates are exact and current |
| Product-role lock | the mutable Source Project, Product Definition, Release Cut, Product, Install, Artifact and dependent Product identities stay distinct, and every Development Product role stays bound to its exact underlying Install |
| authority lock | the semantic, evaluation, operation, decision, acceptance and publication owners and grants are unchanged |
| coverage-and-return lock | every material evaluation and interaction is closed or an explicit residual, and every consumed result followed its declared return relation |

A failed lock takes the value or move its owner gives the case; this
profile adds none (P5, P6):

| Failed lock | Value or move, and its owner |
|---|---|
| changed Product meaning (outcome lock) | `re_enter` to the owning relation ([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)) |
| stale or substituted basis, before activation (basis lock) | the activation refuses: `activation_refusal(basis)`, `invalid_basis` ([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)) |
| stale or substituted basis of an evaluation performed on it | that evaluation's own result is `invalid_basis`, or it is reactivated on the current basis ([RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)) |
| stale basis of a held result, before disposition | for the disposition's conjunction the component has no applicable closed result: a gap, never relabelled `invalid_basis` and never counted as returned ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results), Stale results) |
| missing material scope | `out_of_frame`: at activation, as [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation) states; for an evaluation, on the ground [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) gives, an undeclared material relation or capability |
| missing operation authority (authority lock) | the activation refuses, `activation_refusal(authority)` (REFERENCE_FRAME §5), or the effect is refused |
| an unresolved mandatory conflict (coverage-and-return lock) | the conjunction is not `satisfied`; the conflict survives every join (FOUNDATIONS §4 Conjunction of results, Survival) |

The Executive repairs none of these by making its own frame larger (P5,
P6).

### Product-chain basis

A governed outcome may concern one Product or an explicit directed chain of
Products. Its basis records the distinct role of every mutable Source
Project, current Product Definition, exact candidate checkpoint, Release
Cut, Product, Install, Artifact, Development Product, dependent Product and
composition edge. Each Development Product role binds one exact underlying
Install identity. Each edge names its source and target roles, its governing
authority and contracts, its lifecycle, its evidence boundary, its refusal
and its invalidation (P3, P6; rc.2 #product-chain-basis; the Product-role
map in the basis is PRODUCT_DEFINITION §7, the lineage objects FOUNDATIONS
§2).

An installed Product may lawfully build its own successor or another
Product. That Development Product stays distinct from the mutable Source
Project and from the Product being authored. Directory nesting, shared code,
shared actors, source imports, tool reachability, matching labels or equal
outputs create no Product identity, composition edge or authority transfer
(P3, P1).

Exact basis does not make a Source Project immutable. A Worker may
cumulatively mutate the exact Source Project and write territory named by
its operation grant. A Reviewer evaluates an exact candidate checkpoint
produced from that workspace. A repair advances the workspace, creates a new
candidate and invalidates the affected results. A released Product, Release
Cut or exact Install stays immutable under its own lifecycle law and imposes
no immutability on the Source Project constructing a successor (P3, P4b).
```

Extra, `standards/EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action` (with its subsections):

```text
### The three duties

The Executive is the frame for three inseparable duties over one governed
outcome (P0, P6, P2; rc.2 #executive-attention-evaluation-and-action):

1. attention management: it keeps the exact outcome and basis, the
   Product-role map, the evaluation inventory, the dependency relation, the
   unresolved frontier, the actor envelopes, the current MVP or release
   mandate, the applicable triage policy and the residual boundary, and it
   selects the smallest dependency-ready activation set sufficient for the
   next decision within the finite actor envelopes;
2. evaluation orchestration: it activates capable Workers, Reviewers or
   specialists, keeps their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. authorised action selection: it assigns priority, determines the effect
   on the current promotion boundary, applies an existing disposition, and
   issues only the next already-authorised activation or action.

The Executive does not contain the complete workspace and does not perform
every evaluation. It acquires no Product meaning, implementation, mutation,
acceptance, publication or other operation authority from the role. A
material effect stays owned by the actor that carries its exact operation
grant (P6, RF-002).

### No mutation while Executive

An actor occupying the Executive frame modifies no candidate, Product or
worktree bytes and performs no implementation effect. Filesystem or tool
access is no exception, and neither is an edit that is small, test-only,
reversible or apparently obvious. Mutation requires a separately activated
Worker or Writer relation carrying the exact operation grant, subject and
write territory. A same-actor role transition is explicit and is recorded in
the existing work carrier before the effect; for that effect the actor is no
longer acting as Executive. Recording or delegating after an Executive edit
cannot authorise the edit retroactively (P6, P3). This prohibition is this
profile's, and it applies wherever the executive configuration is selected
([ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Example; §7);
an operation grant covering a construction, status and checkpoint sequence
does not lift it
([ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)).

### Attention cycle

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorised decision is ready:
    await decision-relevant input (event-driven attention, below)
  record every closed result, technical triage, residual and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

The cycle needs no scheduler and no frame engine (RF-016). `M` may hold
parallel activations. Recursion follows declared evaluation dependencies and
bounded refinements; it does not nest or join undifferentiated copies of
every frame. The Executive holds the frontier and the closed-result ledger
in attention, not the undocumented working context of every evaluator (P0,
P4b, P2).

Severity supplied by the Reviewer is evaluation evidence. Priority,
current-boundary effect, disposition and the next action are Executive
decisions. They stay distinct ledger entries even where a Product-defined
policy maps one to another (P6, RF-007).

Every result returns to the Executive, to a declared conjunction or to
another frame through an explicit declared relation. That none of them
activates another frame or authorises continuation by itself is
[ACTIVATION §1 Admission](ACTIVATION.md#admission), applied here. A consumer receives the
closed result and its source routes, not the child's hidden reasoning
context (P6, P4a; ACTIVATION §7).

### Event-driven attention

Executive attention is event-driven by default. The Executive re-enters the
attention cycle for a decision-relevant closed result, a material exception
or changed basis, an owner request, or a declared deadline or checkpoint.
While Workers carry out their bounded grants and no other authorised
decision is ready, it waits. It does not repeatedly inspect unfinished work,
replay unchanged judgments or request status without a decision need (P0,
P2; rc.2 #event-driven-executive-attention).

It keeps the frontier, the return conditions and the valid evidence and
judgments. It refreshes affected support when a material observation
changes its basis, and revalidates the drift locks (below) before activation
and before disposition. Waiting waives no current-workspace verification,
evidence validity, required independent assessment, closed-result
consumption, or authority or closure duty (P6, P4b).

Where notification is unavailable or unreliable, or an actual supervision
obligation requires observation, the Executive uses bounded fallback
observation with a declared purpose, cadence or checkpoint, evidence target,
and stop or escalation condition. Silence proves neither progress nor
failure. A genuine blocker or material risk is investigated, with
intervention where required, within existing grants; unknown status alone
does not establish a stalled Worker (P5, P6).

Repeated no-progress observations, or returns with no new decision-relevant
evidence, require a bounded reassessment of the frame, grant, dependency or
evidence gap and a decision under existing authority. The Executive does not
keep polling or repeat the same repair on an unchanged basis (ACTIVATION §3,
Disposition). Reduced reasoning churn is not a lower-assurance path and is
no permission to reduce required actor capability; it introduces no
universal cost, budget or accounting gate (P2, P0; ACTIVATION §6).

### Drift locks

Before activation and before disposition, the Executive revalidates five
locks (P3, P6, P2; rc.2 #executive-drift-locks):

| Lock | Holds when |
|---|---|
| outcome lock | the selected Goal, Product outcome, boundary and lawful re-entry class, the current MVP or release mandate, and the triage policy are unchanged |
| basis lock | the subject, authority, dependency, configuration, topology, evidence, time and candidate coordinates are exact and current |
| Product-role lock | the mutable Source Project, Product Definition, Release Cut, Product, Install, Artifact and dependent Product identities stay distinct, and every Development Product role stays bound to its exact underlying Install |
| authority lock | the semantic, evaluation, operation, decision, acceptance and publication owners and grants are unchanged |
| coverage-and-return lock | every material evaluation and interaction is closed or an explicit residual, and every consumed result followed its declared return relation |

A failed lock takes the value or move its owner gives the case; this
profile adds none (P5, P6):

| Failed lock | Value or move, and its owner |
|---|---|
| changed Product meaning (outcome lock) | `re_enter` to the owning relation ([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)) |
| stale or substituted basis, before activation (basis lock) | the activation refuses: `activation_refusal(basis)`, `invalid_basis` ([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)) |
| stale or substituted basis of an evaluation performed on it | that evaluation's own result is `invalid_basis`, or it is reactivated on the current basis ([RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)) |
| stale basis of a held result, before disposition | for the disposition's conjunction the component has no applicable closed result: a gap, never relabelled `invalid_basis` and never counted as returned ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results), Stale results) |
| missing material scope | `out_of_frame`: at activation, as [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation) states; for an evaluation, on the ground [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) gives, an undeclared material relation or capability |
| missing operation authority (authority lock) | the activation refuses, `activation_refusal(authority)` (REFERENCE_FRAME §5), or the effect is refused |
| an unresolved mandatory conflict (coverage-and-return lock) | the conjunction is not `satisfied`; the conflict survives every join (FOUNDATIONS §4 Conjunction of results, Survival) |

The Executive repairs none of these by making its own frame larger (P5,
P6).

### Product-chain basis

A governed outcome may concern one Product or an explicit directed chain of
Products. Its basis records the distinct role of every mutable Source
Project, current Product Definition, exact candidate checkpoint, Release
Cut, Product, Install, Artifact, Development Product, dependent Product and
composition edge. Each Development Product role binds one exact underlying
Install identity. Each edge names its source and target roles, its governing
authority and contracts, its lifecycle, its evidence boundary, its refusal
and its invalidation (P3, P6; rc.2 #product-chain-basis; the Product-role
map in the basis is PRODUCT_DEFINITION §7, the lineage objects FOUNDATIONS
§2).

An installed Product may lawfully build its own successor or another
Product. That Development Product stays distinct from the mutable Source
Project and from the Product being authored. Directory nesting, shared code,
shared actors, source imports, tool reachability, matching labels or equal
outputs create no Product identity, composition edge or authority transfer
(P3, P1).

Exact basis does not make a Source Project immutable. A Worker may
cumulatively mutate the exact Source Project and write territory named by
its operation grant. A Reviewer evaluates an exact candidate checkpoint
produced from that workspace. A repair advances the workspace, creates a new
candidate and invalidates the affected results. A released Product, Release
Cut or exact Install stays immutable under its own lifecycle law and imposes
no immutability on the Source Project constructing a successor (P3, P4b).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set` (earlier reading: batch 06 indeterminate: five trailing predecessor paragraphs not found at the one named locus; further loci to be named in the frontier row; disposition `conserved`)

Predecessor, `STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set` at rc.2:

```text
This profile declares the following generic frame families for Product work.
Each row is an evaluation archetype under `REFERENCE_FRAME_METHOD.md`, not a
complete frame declaration. An adopting project binds the exact subject,
basis, material manifold, coordinates, invariants, authority, evidence,
exclusions, result algebra, capability envelope, dependencies, and
invalidation conditions for every activated instance.

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation` under the selected STDO
basis. Under `SPEC_METHOD.md`'s Bounded-Context Semantic Resolution law,
`Product`, `Owner`, `Entity`, `Operator`, `Install`, and the other labels do not
become equal to same-spelled Product, authority, domain, or runtime concepts.
An explicit relation is required at every material cross-context seam.

| Frame family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| **Product** | Does one exact current Product claim, outcome, boundary, and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is current Intent, Product, requirements, acceptance meaning, and exact Product coordinates. | Product and requirement authority retain meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor behavior, or local convention changes Product meaning or substitutes a different Product subject. |
| **Product Composition** | Does one exact directed relation between Products preserve the source and target roles, Product Definition, Release Cut, Product, and Install identities, each Development Product role binding, governing contracts, authority, lifecycle, evidence boundary, and invalidation law? A chain is evaluated through bounded edge activations and declared conjunction. | Each Product retains its own meaning. The authority and contracts cited by the composition relation own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, common actor, source import, tool reachability, matching output, or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| **Design** | Does the accepted structural `HOW` satisfy the material constitutional `WHAT`, close the required design relations, and preserve their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction, or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure remains undeclared. |
| **Design Component** | Does one bounded design component and its direct causal dependency cone preserve its parent contract, internal relations, sibling seams, and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement, and runtime owners retain their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| **Public Boundary** | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal, and projection relations while preserving the selected interior owners? | Product, interface, identity, security, and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| **Entity** | Is one semantic, artifact, or runtime entity bound to its exact identity, kind, lifecycle, owner, representation, and applicable effect regime? | Product, domain, identity, requirement, and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache, or process instance substitutes for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| **Operator** | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects, and lawful compositions? | Product, requirements, accepted Ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command, or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| **Owner** | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants, and permitted delegation? | The existing Product, requirement, identity, accepted-design, release, or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame, or actor widens the grant. |
| **Effect** | Does one action obey its declared pure, observational, artifact, or runtime effect regime, including commit, failure, retry, recovery, compensation, admission, and projection law where material? | The applicable Product, requirement, design, artifact, runtime, and admission owners retain their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| **Reuse/Foundation** | Has one material generic capability or dependency been normalized and compared against credible lawful foundations with any irreducible local remainder and authority-bearing role preserved? | `DESIGN_MODULE_METHOD.md` `STDO-UP-023` and the existing tradeoff owner govern selection. The frame cannot transfer semantic authority to a foundation. | Incumbent or local code wins without bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favorably, or reuse acquires owner authority. |
| **Install** | Is the exact selected Product, release, artifact, dependency set, configuration, and callable entry resolved and exercised through its admitted installed coordinate independently of mutable source convenience? | Product, identity, release, dependency, packaging, and accepted-design authority define the installed subject. The frame returns installed identity, reachability, and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts, or a moving workspace substitute for the claimed installed subject. |
| **Proof** | Does one exact claim have congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary, and invalidation law? | The claim owner defines meaning; applicable testing, assurance, review, Product, and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, count or aggregate green substitutes for the claim, or proof tooling mutates the subject undetectably. |

These families are non-hierarchical and may overlap. Product does not outrank
Design by frame topology; Product authority already governs constitutional
meaning. Owner does not gain authority over Entity or Operator by being a
broader frame. Proof does not become Reviewer, acceptance, or disposition
authority. The existing authority graph remains controlling.

For each governed outcome, the known evaluation inventory dispositions every
family as one of:

- instantiated by one or more exact frame declarations or authoritative
  acquisition paths because the family is material;
- evidenced as non-material to the exact outcome by the authority capable of
  making that determination; or
- retained as an explicit uncovered, conditional, conflicted, or
  `out_of_frame` residual.

Absence of a named file, component, runtime object, or actor is not evidence
that a family is non-material. Conversely, adopting this profile does not
require a project to create twelve components or activate twelve frames for
every task.

When a generic frame is recursively refined, each child declaration records
its parent contract, purpose, material entities, identity and lifecycle
relations, semantic owners, direct sibling seams, applicable invariants, and
prohibited competing paths. Refinement opens only for a material distinction
needed to close the parent evaluation. This is a frame dependency relation,
not an organizational or runtime hierarchy.

Coverage records the union of admissible observations contributed by the
activated frames. A composite claim is `satisfied` only through a declared
conjunction in which every applicable constraint is satisfied and every
material cross-frame seam preserves or lawfully translates exact identity,
coordinate and basis, carried value or evidence, lifecycle scope, authority,
and provenance. A missing or non-commuting seam returns the applicable
`falsified`, `indeterminate`, `out_of_frame`, or `invalid_basis` result; no
frame is selected as dominant.

This generic set imports no consumer-specific frame, runtime role,
architectural topology, or renamed local substitute. A consumer may declare
such frames under its own Product or accepted-design authority when they are
material. They are not part of this baseline.

---
```

Successor, `EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set` (with its subsections):

```text
The profile declares the following generic families for Product work. Each
row is an evaluation archetype, not a complete frame declaration
(REFERENCE_FRAME §13). An adopting project binds, for every activated
instance, the exact subject, basis, material manifold, coordinates,
invariants, authority, evidence, exclusions, result algebra, capability
envelope, dependencies and invalidation conditions (P2, P6; rc.2
#derived-generic-specialist-frame-set).

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation`, owned by
REFERENCE_FRAME, under the selected basis. Under bounded-context semantic
resolution (PRODUCT_DEFINITION §5), `Product`, `Owner`, `Entity`,
`Operator`, `Install` and the other labels do not become equal to
same-spelled Product, authority, domain or runtime concepts; every material
cross-context seam needs an explicit relation (P1, P3).

| Family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| Product | Does one exact current Product claim, outcome, boundary and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is the current Intent, Product, requirements, acceptance meaning and exact Product coordinates. | Product and requirement authority keep meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor's behaviour or a local convention changes Product meaning or substitutes another Product subject. |
| Product Composition | Does one exact directed relation between Products preserve the source and target roles, the Product Definition, Release Cut, Product and Install identities, each Development Product role binding, the governing contracts, authority, lifecycle, evidence boundary and invalidation law? A chain is evaluated through bounded edge activations and a declared conjunction. | Each Product keeps its own meaning. The authority and contracts the composition relation cites own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, a common actor, a source import, tool reachability, matching output or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| Design | Does the accepted structural HOW satisfy the material constitutional WHAT, close the required design relations and keep their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure stays undeclared. |
| Design Component | Does one bounded design component, with its direct causal dependency cone, preserve its parent contract, internal relations, sibling seams and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement and runtime owners keep their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| Public Boundary | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal and projection relations while preserving the selected interior owners? | Product, interface, identity, security and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| Entity | Is one semantic, artifact or runtime entity bound to its exact identity, kind, lifecycle, owner, representation and applicable effect regime? | Product, domain, identity, requirement and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache or process instance stands in for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| Operator | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects and lawful compositions? | Product, requirements, the accepted ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| Owner | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants and permitted delegation? | The existing Product, requirement, identity, accepted-design, release or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame or actor widens the grant. |
| Effect | Does one action obey its declared pure, observational, artifact or runtime effect regime, including commit, failure, retry, recovery, compensation, admission and projection law where material? | The applicable Product, requirement, design, artifact, runtime and admission owners keep their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| Reuse/Foundation | Has one material generic capability or dependency been normalised and compared against credible lawful foundations, with any irreducible local remainder and authority-bearing role preserved? | The design profile's capability-and-foundation selection law and the existing trade-off owner govern selection. The frame cannot move semantic authority to a foundation. | Incumbent or local code wins without a bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favourably, or reuse acquires owner authority. |
| Install | Is the exact selected Product, release, artifact, dependency set, configuration and callable entry resolved and exercised through its admitted installed coordinate, independently of mutable source convenience? | Product, identity, release, dependency, packaging and accepted-design authority define the installed subject. The frame returns installed identity, reachability and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts or a moving workspace stand in for the claimed installed subject. |
| Proof | Does one exact claim have a congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary and invalidation law? | The claim owner defines meaning; the applicable testing, assurance, review, Product and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, a count or aggregate green stands in for the claim, or proof tooling mutates the subject undetectably. |

The families are non-hierarchical and may overlap (RF-008, RF-009).
Product does not outrank Design by frame topology; Product authority
already governs constitutional meaning. Owner gains no authority over
Entity or Operator by being a broader frame. Proof does not become Reviewer,
acceptance or disposition authority. The existing authority graph stays in
control (P6).

### Family dispositions

For each governed outcome the known evaluation inventory (REFERENCE_FRAME
§8) disposes every family as one of (P2, P6, P5):

- instantiated by one or more exact frame declarations or authoritative
  acquisition paths, because the family is material;
- evidenced as non-material to the exact outcome by the authority capable
  of that determination; or
- kept as an explicit uncovered, conditional, conflicted or `out_of_frame`
  residual.

The absence of a named file, component, runtime object or actor is no
evidence that a family is non-material. Conversely, adopting this profile
does not require a project to create twelve components or to activate
twelve frames for every task (P2, P1).

### Refinement and conjunction

When a generic frame is recursively refined, each child declaration records
its parent contract, purpose, material entities, identity and lifecycle
relations, semantic owners, direct sibling seams, applicable invariants and
prohibited competing paths. Refinement opens only for a material
distinction needed to close the parent evaluation. It is a frame dependency
relation, not an organisational or runtime hierarchy (P2, P4a; ACTIVATION
§4).

Coverage records the union of admissible observations the activated frames
contribute. A composite claim takes the value of its declared conjunction
under
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Reported value. This profile's declared rule makes each material
cross-frame seam a mandatory result or required coverage: the seam
preserves, or lawfully translates, exact identity, coordinate and basis,
carried value or evidence, lifecycle scope, authority and provenance
([REFERENCE_FRAME §6](REFERENCE_FRAME.md#evidence-or-coordinate-translation)
for translation). Each case of a seam enters the conjunction as that
section states (P4a, P5):

| Seam case | Input of the conjunction and value |
|---|---|
| no closed result applicable to the composite: not evaluated, or its only result is stale or bound to another subject or basis | a planned assessment without a closed result, a gap with no value of its own (FOUNDATIONS §4, the second input and Stale results) |
| a material seam that no planned assessment addresses | uncovered coverage, a gap with no value of its own (the third input) |
| evaluated and found not to preserve or lawfully translate what the rule requires | the seam's own result: `falsified`, or the outcome and core value that [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) gives a refused translation by its cause |
| evaluated, with evidence that cannot decide it | `indeterminate` |
| its evaluation needs a translation or relation that no frame declares | `out_of_frame` |
| evaluated on a stale, advanced, ambiguous or mismatched basis | `invalid_basis` for its own predicate ([RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)), held as a returned result |

A composite with any of these cases is never `satisfied`; it reports the
non-satisfied value that FOUNDATIONS §4, Reported value, gives, with each
gap recorded by kind. Which non-satisfied value it reports where several
are returned is the conjunction rule the adopting project declares (§19
Project-basis additions). This profile's own declared choice is that no
frame is selected as dominant.

The set imports no consumer-specific frame, runtime role, architectural
topology or renamed local substitute. A consumer may declare such frames
under its own Product or accepted-design authority when they are material;
they are not part of this baseline (P2, P6).

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

Extra, `standards/EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set` (with its subsections):

```text
The profile declares the following generic families for Product work. Each
row is an evaluation archetype, not a complete frame declaration
(REFERENCE_FRAME §13). An adopting project binds, for every activated
instance, the exact subject, basis, material manifold, coordinates,
invariants, authority, evidence, exclusions, result algebra, capability
envelope, dependencies and invalidation conditions (P2, P6; rc.2
#derived-generic-specialist-frame-set).

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation`, owned by
REFERENCE_FRAME, under the selected basis. Under bounded-context semantic
resolution (PRODUCT_DEFINITION §5), `Product`, `Owner`, `Entity`,
`Operator`, `Install` and the other labels do not become equal to
same-spelled Product, authority, domain or runtime concepts; every material
cross-context seam needs an explicit relation (P1, P3).

| Family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| Product | Does one exact current Product claim, outcome, boundary and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is the current Intent, Product, requirements, acceptance meaning and exact Product coordinates. | Product and requirement authority keep meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor's behaviour or a local convention changes Product meaning or substitutes another Product subject. |
| Product Composition | Does one exact directed relation between Products preserve the source and target roles, the Product Definition, Release Cut, Product and Install identities, each Development Product role binding, the governing contracts, authority, lifecycle, evidence boundary and invalidation law? A chain is evaluated through bounded edge activations and a declared conjunction. | Each Product keeps its own meaning. The authority and contracts the composition relation cites own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, a common actor, a source import, tool reachability, matching output or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| Design | Does the accepted structural HOW satisfy the material constitutional WHAT, close the required design relations and keep their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure stays undeclared. |
| Design Component | Does one bounded design component, with its direct causal dependency cone, preserve its parent contract, internal relations, sibling seams and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement and runtime owners keep their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| Public Boundary | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal and projection relations while preserving the selected interior owners? | Product, interface, identity, security and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| Entity | Is one semantic, artifact or runtime entity bound to its exact identity, kind, lifecycle, owner, representation and applicable effect regime? | Product, domain, identity, requirement and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache or process instance stands in for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| Operator | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects and lawful compositions? | Product, requirements, the accepted ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| Owner | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants and permitted delegation? | The existing Product, requirement, identity, accepted-design, release or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame or actor widens the grant. |
| Effect | Does one action obey its declared pure, observational, artifact or runtime effect regime, including commit, failure, retry, recovery, compensation, admission and projection law where material? | The applicable Product, requirement, design, artifact, runtime and admission owners keep their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| Reuse/Foundation | Has one material generic capability or dependency been normalised and compared against credible lawful foundations, with any irreducible local remainder and authority-bearing role preserved? | The design profile's capability-and-foundation selection law and the existing trade-off owner govern selection. The frame cannot move semantic authority to a foundation. | Incumbent or local code wins without a bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favourably, or reuse acquires owner authority. |
| Install | Is the exact selected Product, release, artifact, dependency set, configuration and callable entry resolved and exercised through its admitted installed coordinate, independently of mutable source convenience? | Product, identity, release, dependency, packaging and accepted-design authority define the installed subject. The frame returns installed identity, reachability and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts or a moving workspace stand in for the claimed installed subject. |
| Proof | Does one exact claim have a congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary and invalidation law? | The claim owner defines meaning; the applicable testing, assurance, review, Product and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, a count or aggregate green stands in for the claim, or proof tooling mutates the subject undetectably. |

The families are non-hierarchical and may overlap (RF-008, RF-009).
Product does not outrank Design by frame topology; Product authority
already governs constitutional meaning. Owner gains no authority over
Entity or Operator by being a broader frame. Proof does not become Reviewer,
acceptance or disposition authority. The existing authority graph stays in
control (P6).

### Family dispositions

For each governed outcome the known evaluation inventory (REFERENCE_FRAME
§8) disposes every family as one of (P2, P6, P5):

- instantiated by one or more exact frame declarations or authoritative
  acquisition paths, because the family is material;
- evidenced as non-material to the exact outcome by the authority capable
  of that determination; or
- kept as an explicit uncovered, conditional, conflicted or `out_of_frame`
  residual.

The absence of a named file, component, runtime object or actor is no
evidence that a family is non-material. Conversely, adopting this profile
does not require a project to create twelve components or to activate
twelve frames for every task (P2, P1).

### Refinement and conjunction

When a generic frame is recursively refined, each child declaration records
its parent contract, purpose, material entities, identity and lifecycle
relations, semantic owners, direct sibling seams, applicable invariants and
prohibited competing paths. Refinement opens only for a material
distinction needed to close the parent evaluation. It is a frame dependency
relation, not an organisational or runtime hierarchy (P2, P4a; ACTIVATION
§4).

Coverage records the union of admissible observations the activated frames
contribute. A composite claim takes the value of its declared conjunction
under
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Reported value. This profile's declared rule makes each material
cross-frame seam a mandatory result or required coverage: the seam
preserves, or lawfully translates, exact identity, coordinate and basis,
carried value or evidence, lifecycle scope, authority and provenance
([REFERENCE_FRAME §6](REFERENCE_FRAME.md#evidence-or-coordinate-translation)
for translation). Each case of a seam enters the conjunction as that
section states (P4a, P5):

| Seam case | Input of the conjunction and value |
|---|---|
| no closed result applicable to the composite: not evaluated, or its only result is stale or bound to another subject or basis | a planned assessment without a closed result, a gap with no value of its own (FOUNDATIONS §4, the second input and Stale results) |
| a material seam that no planned assessment addresses | uncovered coverage, a gap with no value of its own (the third input) |
| evaluated and found not to preserve or lawfully translate what the rule requires | the seam's own result: `falsified`, or the outcome and core value that [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) gives a refused translation by its cause |
| evaluated, with evidence that cannot decide it | `indeterminate` |
| its evaluation needs a translation or relation that no frame declares | `out_of_frame` |
| evaluated on a stale, advanced, ambiguous or mismatched basis | `invalid_basis` for its own predicate ([RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)), held as a returned result |

A composite with any of these cases is never `satisfied`; it reports the
non-satisfied value that FOUNDATIONS §4, Reported value, gives, with each
gap recorded by kind. Which non-satisfied value it reports where several
are returned is the conjunction rule the adopting project declares (§19
Project-basis additions). This profile's own declared choice is that no
frame is selected as dominant.

The set imports no consumer-specific frame, runtime role, architectural
topology or renamed local substitute. A consumer may declare such frames
under its own Product or accepted-design authority when they are material;
they are not part of this baseline (P2, P6).

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


### Row `UX_METHOD.md#8a-msg-replay-proof-requirement` (earlier reading: batch 08 indeterminate: the §15 recorded-exemption exit cannot be compared without the rc.2 §12 escrow text; disposition `conserved`)

Predecessor, `UX_METHOD.md#8a-msg-replay-proof-requirement` at rc.2:

```text
Every product UX surface must carry at least one executable Msg-replay proof for
each product-meaningful interaction family before claiming method closure.

A replay proof includes:

- an initial `State` fixture
- an ordered `Msg` log
- the expected final `State`
- the expected ordered `Cmd` values
- the success and failure `Msg` values returned by interpreted `Cmd`s
- injected deterministic values for time, randomness, generated ids, and
  external payloads

The proof fails if correctness depends on:

- DOM state not represented in `State`
- mutable refs, module variables, closures, timers, or effect-handler memory
- network or file results that bypass typed `Msg`
- view-local state that changes product behavior after unmount or replay

For a pure projection-only surface, the replay proof may be a no-effect proof:
`Msg` log plus final `State` and empty `Cmd` sequence.

---
```

Successor, `UX.md#msg-replay-proof` (with its subsections):

```text
Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
Purpose and material relation: the Msg log is the surface's recorded work
state, and replay is resumption from it
([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
A surface whose behaviour cannot be reproduced from its log holds state
that no later actor or session can recover or check, so the proof is the
evidence that the view owns no hidden continuation (P0, P4b). A
replay proof includes:

- an initial State fixture;
- an ordered Msg log;
- the expected final State;
- the expected ordered Cmd values;
- the success and failure Msg values returned by interpreted Cmds;
- injected deterministic values for time, randomness, generated ids and
  external payloads.

The proof fails if correctness depends on (P5, P4b):

- DOM state not represented in State;
- mutable refs, module variables, closures, timers or effect-handler
  memory;
- network or file results that bypass typed Msg;
- view-local state that changes product behaviour after unmount or
  replay.

For a pure projection-only surface, the replay proof may be a no-effect
proof: a Msg log plus the final State and an empty Cmd sequence (P2).
```

Successor, `UX.md#15-results-of-this-profile` (with its subsections):

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```

Extra, rc.2 `UX_METHOD.md#13a-scaffold-and-exemption-law`:

```text
A UX surface is governed by this method by default when any of these are true:

- it is reachable from the product shell
- it is used as proof for a ticket, requirement, design module, release, or
  review
- it can mutate product truth
- it can spawn, attach, resume, or dispatch work
- it can change Context, selection authority, closure, continuation, evidence,
  or provenance

A scaffold, prototype, debug pane, or temporary proof surface may be exempt only
when the design module or ticket records:

- the exemption scope
- the permitted operations
- whether mutation is forbidden or explicitly bounded
- a visible scaffold/debug label where user-facing
- the authoritative surface that will supersede it
- the retirement condition and owning ticket
- the non-closure condition preventing release if the scaffold remains

An exempt scaffold cannot become the production UX by accumulation. It must be
retired, repriced into a governed UX surface, or kept outside product closure.
```

Extra, rc.2 `UX_METHOD.md#13b-ux-sprint-compliance-escrow`:

```text
UX is the primary governed use case for sprint compliance escrow.

Under `SPEC_METHOD.md` and `TICKET_METHOD.md`, a UX sprint may defer local UX
compliance proof during a short iteration window when per-change proof cost is
higher than expected correction cost.

This is a cost-optimization rule. It does not weaken the UX process model.

A UX sprint may escrow:

- screenshots or walkthrough capture
- visual review
- copy, spacing, density, and layout cleanup
- accessibility review and remediation
- Msg-replay proof updates for product-meaningful interaction families
- design-module wording cleanup
- trace cleanup between changed UX states and governing authority

A UX sprint may not escrow:

- product-truth-changing `Msg` variants that lack an admitted carrier
- new or changed `AssetSurface` contracts or equivalent typed product contracts
- new navigation, information architecture, or selection authority that changes
  product meaning
- runtime, governance, closure, continuation, lineage, provenance, or evidence
  semantics
- release criteria or method law

If one of those appears, the sprint records the finding and the work exits the
UX sprint path through standalone repricing or sprint supersession. The UX layer
must still not become the hidden constructive carrier.

A UX sprint should close when continued iteration is more expensive or less
trustworthy than review. Valid close triggers include:

- the declared timebox ends
- accumulated changed states are too numerous for casual review
- screenshots or walkthrough evidence no longer explain the current surface
- interaction behavior changed beyond visual polish
- reviewer uncertainty makes more iteration unsafe without reconciliation

UX sprint close is a forensic walkthrough. The walkthrough reviews each changed
screen, state, and product-meaningful interaction against the cited authority.

Each finding is classified as:

- `accepted`: compliant with this method and the cited design
- `local_paydown`: local UX debt remains and is captured by a paydown ticket
- `design_reframe`: design authority must change
- `requirement_reprice`: requirement authority must change
- `product_reprice`: product definition must change
- `remove`: the change should be backed out or kept out of closure

The sprint may close with explicit local paydown tickets only where the debt is
local to UX realization and the governing method allows follow-up. It may not
close while product-truth carrier gaps, hidden state continuation, or authority
drift remain unclassified.

Method closure for a product UX surface still requires the §8A Msg-replay proof
and §11 accessibility obligations unless an explicit exemption is recorded. The
sprint can defer those obligations during iteration; it cannot erase them.

---
```

Extra, `standards/UX.md#15-results-of-this-profile` (with its subsections):

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```
