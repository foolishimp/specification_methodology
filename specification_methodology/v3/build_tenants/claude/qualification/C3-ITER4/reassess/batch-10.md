# I4-09 successor readback batch-10

Rows: 2. Each row gives the predecessor section at the installed rc.2 and the successor loci at the current tree with their subsections, then the extra sections the earlier reading said it needed. Judge each row under INSTRUCTIONS.md; the `why` line says what the earlier reading found.


### Row `DESIGN_MODULE_METHOD.md#4-functional-bias-without-language-mandate` (earlier reading: batch 09 changed: a recorded-reason exception was added to the avoid list; repaired: the exception is removed, both lists bind without exception; disposition `conserved`)

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
forgoes a preferred one where it is practical, does not conform (P6, P2;
the predecessor's "must prefer" and "must avoid", which admit no
exception).
```


### Row `STDO_REFERENCE_FRAME_BASELINE.md#closure` (earlier reading: batch 09 indeterminate: TICKETS §7 was supplied without its subsections; now supplied whole; disposition `conserved`)

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

Extra, `standards/TICKETS.md#7-authority-judgment-closure-and-state` (with its subsections):

```text
The generic law is tier 1: a constructor's self-review is construction
output and the independent-assessment protocol is
[EVALUATION §3](EVALUATION.md#3-independent-assessment); acceptance as the
decision owner's disposition, and closure by stated condition rather than
by reviewer approval, is [EVALUATION §5](EVALUATION.md#5-acceptance); reuse
of a closed result is [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse).
This section states what those laws require of work carriers.

### Execution and verification authority separation (UP-007)

Authority to author or implement a change is not independent authority to
verify it. What counts as independent, including that the reviewer is
not the author of the reviewed subject, and the protocol an independent
assessment follows are
[EVALUATION §3](EVALUATION.md#3-independent-assessment). Where
independent review is required, the reviewer identifies the exact
subject, basis, scope, exclusions, evidence, verdict and unresolved
findings (P6; rc.2
#execution-and-verification-authority-separation-stdo-up-007). Review
findings must cite current authority and the code or proof paths they
rest on, not only historical commentary (P6, P1; provenance rc.2
authority_compressions/ticket_method.compressed.md, a claim no rc.2 body
states).

Self-review remains useful authoring evidence and cannot be relabelled as
independent. Human authority may accept or reject the claim; it does not
make implementer self-review independent. The boundaries at which this
method requires independent assessment are this member's policy, which
EVALUATION §3 names; a governing basis may add others, as that section
states. Independent review is required at
product, qualification, release and explicitly risk-bearing boundaries that
claim it, not for every local implementation step (P6, P2).

A claimed independent review may support promotion or closure only when its
exact subject and verdict are durably traceable through an existing ticket,
commentary, qualification or release-evidence carrier. A statement that
review occurred, an unbound conversation summary or an unavailable draft is
not the review verdict. This rule requires no separate receipt, carrier or
review round (P6, P4b).

A ticket's review verdict is bounded by the exact reviewed claim and its
applicable hard stops. When a finding blocks current promotion, and what a
valid observation outside that boundary does, are stated once at
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion);
this carrier applies that section to a ticket's review and adds no
trigger (P2, P6).

A direct or lawfully proxied human ruling receives a durable disposition
before the next affected acceptance boundary. Its source wording stays
distinct from agent interpretation. Opening a ticket records the
obligation and does not satisfy it, and an agent cannot widen the ruling
while recording it (P6, P4b).

Where the agentic construction relation applies (ACTIVATION §1, bound to
this method by [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method)),
the active work item identifies the selected execution basis, the bounded
affected relation set, the delegated construction and assessment authority,
and the re-entry conditions. It may point to accepted design and existing
evidence carriers rather than restate them. Ticket state, ticket prose or
an admitted execution contract cannot widen that basis or substitute for
the live-surface assessment the relation requires (P6, P0).

The reviewable transition (ACTIVATION §7, Transition evidence) may be
carried by an existing ticket, commentary, commit, qualification or
release-evidence surface. No new ticket state, document type, review round
or approval ceremony is required. This member carries selection and
traceability; ACTIVATION §1 and SPEC_METHOD §8 own the execution semantics
(P2, P6).

### Recorded judgment and owner-ruling continuity

A residual judgment that another activation needs is recorded once, with
its owning work, in the existing carrier selected under §5. The record
identifies the question; the exact subject and governing basis; the
supporting computed facts and evidence; the responsible actor and its
authority; the conclusion and its scope; the uncertainty; and a concrete
revising observation that lets a consumer determine whether the conclusion
still applies. A question settled by rule needs no invented J record (P4b,
P6; rc.2 #recorded-judgment-and-owner-ruling-continuity; C, J and O are
the annotations of [SPEC_METHOD §4](SPEC_METHOD.md#computed-classification-and-treatment)).

Later roles and resumed runs recover the result and check its
applicability rather than re-author unchanged judgment. Reuse and
invalidation are
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): changed material
inputs, a declared revising observation or a changed basis invalidate
the affected result, preserving the original result and its successor
relation and keeping only demonstrably independent results, and a new
role or conversation alone invalidates nothing. For a recorded judgment
the material inputs include its supporting computed facts and evidence,
and its declared revising observation is the one the record states;
reassessment covers what the change affects. The result may reference
current C outputs; reuse cannot silently turn unknown facts into
established premises (P4b, P5). Required independent assessment may consume valid C, but
its assessor acquires sufficient exact evidence and supplies its own
judgment under the actual independence condition; reusing the author's J
cannot satisfy that condition (P6; EVALUATION §3).

A direct or lawfully proxied owner ruling is recorded in its original
wording, with its owner, exact subject and basis, permitted scope and
effects, conditions and source, separately from agent interpretation. Later
work consumes that same ruling while it applies; it neither widens the
ruling nor requests unchanged authority again. New ambiguity or a
materially changed decision returns only the affected question to its
owner. J is not O, and recording either cannot create admission,
acceptance, effects or continuation beyond the original grant (P6, P3).

These results follow the lifetime of the existing run, sprint or durable
ticket and its named result and evidence surface. They require no separate
judgment registry, no ticket per judgment and no additional approval
ceremony (P2).

Repricing gives each affected obligation a disposition in that same
carrier: retained, superseded, deferred or withdrawn, with its owning
authority and applicable evidence links. Surviving work is preserved and
changed dependencies are explained; unaffected history is not copied into
a parallel ledger. An owner decision is presented as the short consequence
delta needed to decide it, with the original ruling preserved separately.
A general instruction to continue does not accept an undisclosed
architectural or scope change (P4b, P6, P2).

The four repricing dispositions are recorded states of the obligation,
set by its owning authority; they are not results and map to no core
value. Each records the standing the obligation keeps after repricing,
as the lifecycle statuses of
[SPEC_METHOD §2](SPEC_METHOD.md#requirement-categories-and-classification)
record a requirement's, and answers no predicate that an evaluation
decides on evidence. They differ from the disposition of an assessed
candidate ([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)), which
is the acceptance result that FOUNDATIONS §4 Results places in the core,
because a repricing disposition accepts no candidate; and from the
disposition of a predecessor claim
([RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)),
which is a claim that qualification evaluates. An evaluation that reads
them returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a recorded disposition is never combined as an evaluation
result, so a retained obligation is never read as satisfied, and a
superseded, deferred or withdrawn one never as discharged (P5, P1, P6).

### Condition-based closure and reuse

A work claim is complete only when every applicable declared obligation is
satisfied by valid evidence for its exact subject, basis and scope; every
required judgment and owner ruling is present and applicable; and no active
non-closure condition remains. A mandatory obligation whose applicability is
unknown, or whose evidence is insufficient, withholds the dependent claim;
evidence presence alone is not satisfaction. The existing owner decides any
reserved acceptance (P6, P5; rc.2 #condition-based-closure-and-reuse).
This condition is the
[conjunction of results](FOUNDATIONS.md#conjunction-of-results) with the
declared obligations as required coverage. This section owns the
closure condition of a work claim;
[SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate)
applies it as the gate over a declared change span.

Review evaluates these conditions; its occurrence is not the closing event.
Where applicable law requires no independent review or reserved
acceptance, a work claim is recorded as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)
states in Recording a result without review, with the ticket as the
existing carrier. The conditions that still apply include sprint-close
law (§3) and the design profile's law (P6, P2).

An unchanged obligation reuses valid applicable evidence and recorded J
and O under the reuse rule of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse). For a work
claim, the changed material inputs and revising observations that rule
names include a material counterexample, changed evidence and a stated
revising observation of a recorded J; with a changed basis, each
invalidates the affected claim and its dependent results before further
reliance. An unrelated observation is retained as bounded repricing input;
it does not reopen a satisfied claim or expand the work automatically.
Closure recording preserves the exact evaluated scope, the satisfied
conditions, the evidence and the remaining residuals (P4b, P2).

### Test case authority

Tests are proof projections from admitted work authority. Every
substantive test case should derive along this chain (P6, P2; rc.2
#test-case-authority):

```text
ticket -> intake triage -> lawful re-entry point -> governing requirement,
design, module, published function, carrier, or closure surface -> test expectation
```

Tests do not derive authority from the current implementation. An
acceptance predicate also needs an applicable supported entry or state and
an obligation under the governing operating or threat model. Existing test
presence cannot authorise an excluded threat or retain a superseded guard.
When that responsibility changes, the affected predicates are audited, and
unsupported expectations are retired under the owning basis without
inventing a replacement guard. An actual conflict in live authority
requires re-entry, not a test-only waiver (P6, P2).

Implementation behaviour is evidence. The code is never the arbiter of a
test's expected result when code and test disagree (P6). When a ticket is
fixed and a mismatch appears between implementation behaviour and test
expectation, review reconciles the mismatch in this order:

1. the ticket's `change_intent`, `change_class`, `re_entry_point`,
   `target_truth`, `superseded_truth`, `closure_law`,
   `evaluation_criteria` and `non_closure_conditions`;
2. the ticket's intake triage and lawful owning re-entry;
3. the governing requirement, design, module, published-function, carrier
   or other cited authority surface;
4. the test case expectation;
5. the implementation.

The implementation may show that a test is stale, incomplete or too
narrow; it cannot by itself authorise changing the expected result.
Changing a test only because the current code behaves differently is a
ticket-method defect. A test that predates a lawful ticket repricing is
updated or removed only after naming the governing ticket and the authority
change that superseded the old expectation. If the ticket is stale,
ambiguous or missing the authority needed to decide the expectation, the
work re-enters triage (§4) before either the code or the test is treated as
correct. A passing test is closure evidence only when its expectation
traces back to the admitted ticket and its governing authority chain (P6,
P4b). The general test authority law is ASSURANCE §3; this clause is its
ticket-local rule.

### One-truth state projection and drift refusal (UP-009)

Work state has one authority chain: goals own the bounded work wave, the
ticket owns ticket state, milestone authority owns subordinate milestone
state (§1), and accepted design owns realisation decisions. Comments,
dashboards, registers, indexes and generated summaries are projections
(P6, P3; rc.2 #one-truth-state-projection-and-drift-refusal-stdo-up-009).

Recency, visibility or repetition does not turn a projection into truth.
Contradiction between the owning ticket, its required milestones, the
current goals or the cited acceptance evidence blocks closure. Superseded
evidence remains history and cannot be projected as current acceptance
(P6, P4b).
```
