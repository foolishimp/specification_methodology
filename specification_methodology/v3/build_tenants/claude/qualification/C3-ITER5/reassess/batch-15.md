# I5-03 reading batch 15

Rows: 17. Members: ['TICKET_METHOD.md', 'TRAVERSAL_OCCURRENCE_PROFILE.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `TICKET_METHOD.md#tickets` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#tickets` at rc.2:

```text
### Tickets

Tickets are the enduring work records.

Each ticket is:

- one durable record; one markdown file is the default carrier
- the source of truth for that unit of work
- durable across sessions
- typed, so bugs and features share one system

Tickets are used when work needs independent durable identity for:

- feature work
- bug tracking
- spikes
- chores
```

Successor, `TICKETS.md#ticket-records`:

```text
### Ticket records

Tickets are the enduring work records. Each ticket is one durable record,
one markdown file being the default carrier; the source of truth for that
unit of work; durable across sessions; and typed, so that bugs and features
share one system. A ticket is used when work needs independent durable
identity: feature work, bug tracking, spikes and chores (P3, P4b; rc.2
#tickets).
```


### Row `TICKET_METHOD.md#upward-propagation-check` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#upward-propagation-check` at rc.2:

```text
### Upward Propagation Check

Triage consumes `SPEC_METHOD.md#computed-classification-and-treatment` for the
declared owner/layer traversal, complete relevant Public membership and value
delta, accepted-design scope and trace coverage, and rule-determined treatment.
The owning work carrier references that exact result and its residuals; a new
role does not repeat an unchanged walk.

Before declaring `realization_refactor` for a bug, establish that the current
requirement and accepted realizing design govern the affected behavior and
remain sufficient for the authorized outcome. Their mere presence proves no
coverage. Missing or ambiguous evidence leaves the affected treatment unknown;
it is not proof that the governing layer itself is absent.

If the governing requirement is actually missing or insufficient, re-enter its
owner; if that requirement is sufficient but the realizing design is missing or
insufficient, re-enter Design. Follow any actual upstream Goal, Intent or
Product change to its owner rather than stopping at a familiar file. When the
current requirement and accepted design suffice and implementation deviates,
repair or reject the candidate under `realization_refactor`. A candidate's
Public violation does not select a new contract. An explicitly changed desired
outcome or established governing insufficiency follows the owning re-entry;
unresolved meaning remains J and reserved choice O.
```

Successor, `TICKETS.md#upward-propagation-check`:

```text
### Upward propagation check

Triage consumes the computed classification of
[SPEC_METHOD §4](SPEC_METHOD.md#computed-classification-and-treatment) for
the declared owner and layer traversal, the complete relevant public
membership and value delta, the accepted-design scope and trace coverage,
and the rule-determined treatment. The owning work carrier references that
exact result and its residuals; a new role does not repeat an unchanged
walk (P4b, P2; rc.2 #upward-propagation-check).

Before declaring `realization_refactor` for a bug, establish that the
current requirement and the accepted realising design govern the affected
behaviour and remain sufficient for the authorised outcome. Their presence
proves no coverage. Missing or ambiguous evidence leaves the affected
treatment unknown; it is not proof that the governing layer itself is
absent (P6).

The re-entry rule is SPEC_METHOD §4's: the
[change classes](SPEC_METHOD.md#change-classes) with their re-entry
points, and the smallest lawful re-entry that step 4 of
[Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment)
exposes, with the paragraph after the four steps: a candidate's public
violation does not select a new contract, and the governing owner is
re-entered only for an explicitly changed desired outcome or an
established governing insufficiency. For a bug, this check
refines that rule into an upward walk from the realised surface that
checks each layer and stops at the highest layer found missing or
insufficient for the authorised outcome, and the class is the one that
re-enters there:

| Where the walk stops | Change class | Action |
|---|---|---|
| the governing requirement is missing or insufficient | `requirement_reprice` | re-enter the requirement's owner |
| the requirement is sufficient, and the realising design is missing or insufficient | `design_reframe` | re-enter Design |
| an actual upstream Goal, Intent or Product change | `goal_reprice`, `intent_reprice` or `product_reprice` | follow the change to its owner rather than stopping at a familiar file |
| the current requirement and accepted design suffice, and the implementation deviates | `realization_refactor` | repair or reject the candidate |

Unresolved meaning remains J and a reserved choice remains O, as that
paragraph states (P2, P6).
```


### Row `TICKET_METHOD.md#work-carrier-to-execution-rule` (disposition `conserved`)

Predecessor, `TICKET_METHOD.md#work-carrier-to-execution-rule` at rc.2:

```text
### Work-Carrier-To-Execution Rule

Every execution governed by this method uses one run-scoped execution contract.
The required lifetime of the work or obligation selects the smallest lawful
source carrier. First establish applicable upstream work authority, then select
the first matching row. For work inside an admitted sprint, the local carrier
boundary is that sprint; otherwise it is the current run.

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and work or an open obligation needs independent state beyond the local carrier boundary | use one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and work stays inside one admitted sprint with no state required after sprint close | use the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and work ends in the current run with no independent surviving state | use an intake-drafted run-scoped contract | do not create a durable ticket |

`Ticket-shaped` describes the categorization, closure criteria, proof surface,
non-closure conditions, and other required execution-contract fields. It does
not create durable ticket identity or ticket-lane state.

Absence of a durable ticket neither requires nor authorizes creating one. An
exact Product-authorized work instruction may supply upstream work authority
for a one-run contract; a generic request or model-widened scope cannot. Create
or update a durable ticket only when the table requires surviving state and the
actor holds ticket-state authority.

An explicit instruction from ticket-state authority to create a durable record
selects that durability. It does not admit an execution contract or widen its
upstream work authority.

The system may draft, validate, admit, and execute a contract in one invocation.
Drafting and admission remain distinct relations within that invocation; no
separate turn, ticket, or approval ceremony is implied. Execution begins only
after deterministic admission or explicit human override of the exact contract.
The drafting model must not infer admission from its own draft, ticket or sprint
presence, lane placement, or `active` status.

The admitted result identifies the Product-bound admission mechanism and
authority, exact contract identity or digest, decision, and evidence, including
any exact human override. If those coordinates are absent, the contract remains
drafted or rejected; prose asserting `admitted` is not admission evidence.

The admitted contract also names one Product-bound durable result/evidence
surface. Every execution result, withheld closure, and residual obligation is
recorded there before return. A conversation return alone is not durable
evidence. If no such surface is authorized and available, contract admission
refuses.

Absent or rejected admission returns the missing work authority without
execution. Before return, an obligation that must survive the run becomes a
sprint-local entry when its lifetime remains inside the admitted sprint;
otherwise it is recorded as a durable ticket only under ticket-state authority.
If that authority is absent, retain the obligation in the contract's named
durable result/evidence surface or an already-authorized enclosing carrier,
mark closure withheld on ticket-state authority, and return the required
re-entry.

Execution and closure use the same admitted categorization, criteria, proof
surface, and non-closure conditions. Resulting state still flows through proof,
gap analysis, and repricing.
```

Successor, `TICKETS.md#carrier-selection`:

```text
### Carrier selection

Every execution governed by this method uses one run-scoped execution
contract. The required lifetime of the work or obligation selects the
smallest lawful source carrier: first establish the applicable upstream
work authority, then select the first matching row below. For work inside
an admitted sprint the local carrier boundary is that sprint; otherwise it
is the current run (P2, P4b, P6; rc.2 #work-carrier-to-execution-rule).

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and the work or an open obligation needs independent state beyond the local carrier boundary | one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and the work stays inside one admitted sprint with no state required after sprint close | the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and the work ends in the current run with no independent surviving state | an intake-drafted run-scoped contract | do not create a durable ticket |

"Ticket-shaped" describes the categorisation, closure criteria, proof
surface, non-closure conditions and the other required execution-contract
fields (§4, Required fields). It creates no durable ticket identity and no
ticket-lane state (P3).

Absence of a durable ticket neither requires nor authorises creating one.
An exact product-authorised work instruction may supply the upstream work
authority for a one-run contract; a generic request or a model-widened
scope cannot. A durable ticket is created or updated only when the table
requires surviving state and the actor holds ticket-state authority. An
explicit instruction from ticket-state authority to create a durable record
selects that durability; it does not admit an execution contract or widen
its upstream work authority (P6, P2).

The step side of admission is [ACTIVATION §1](ACTIVATION.md#admission) and
is defined there once: drafting versus admission inside one invocation, the
condition under which execution may begin, what admission may never be
inferred from (including ticket or sprint presence, lane placement and
`active` status), the coordinates an admitted result carries, the recording
of every result, withheld closure and residual obligation before return,
and refusal when no durable result and evidence surface is available. This
member adds the carrier side (P6, P4b). The admission mechanism and the
durable result and evidence surface are the ones the product definition
binds. When that surface is the ticket or the sprint manifest, the admitted
result with its coordinates is recorded there. A carrier's lane, status or
prose that asserts admission without those coordinates is not admission
evidence, and the contract it describes remains drafted or rejected.

When admission is absent or rejected, ACTIVATION §1 returns the missing
work authority without execution. Before that return, an obligation that
must survive the run is carried as follows (P4b, P6): it becomes a
sprint-local entry when its lifetime stays inside the admitted sprint;
otherwise it is recorded as a durable ticket, only under ticket-state
authority; where that authority is absent, it is retained in the
contract's named durable result and evidence surface or in an
already-authorised enclosing carrier, closure is marked withheld on
ticket-state authority, and the required re-entry is returned.

Execution and closure use the same admitted categorisation, criteria,
proof surface and non-closure conditions. The resulting state still flows
through proof, gap analysis and repricing (P6, P2).
```

Successor, `ACTIVATION.md#admission`:

```text
### Admission

Drafting a step's contract and admitting it are distinct relations, even
inside one invocation that drafts, validates, admits and executes; no
separate turn, carrier or approval ceremony is implied by the distinction.
A contract carries at minimum the states drafted, admitted, rejected and
superseded ([TICKETS §5](TICKETS.md#execution-contract-admission)).
Execution begins only after deterministic admission or an
explicit human override of the exact contract. The drafting actor never
infers admission from its own draft, from the presence of a carrier
(ticket, sprint entry, work contract), from lane placement or from an
`active` label. The admitted result identifies the admission mechanism and
its authority, the exact contract identity or digest, the decision and the
evidence, including any human override; absent those coordinates the
contract stays drafted or rejected, and prose asserting admission is not
admission evidence (P6; the actor cannot self-certify its own execution
basis). Admission validates the contract against its cited outcome,
prerequisite or experiment basis; it does not admit that basis, and
drafting, admitting or retaining a contract creates or renews no authority
its owner has not admitted (P6, P2;
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). Only an admitted contract activates a step: no
result, child completion, tool output, model response, shared actor or
lateral handoff activates another step or authorises continuation by
itself, and a profile that routes results names its instances of this
rule. Purpose and material relation: a profile and a template each stated
this list for one configuration, so the generic rule had no owner (P6).
The admitted contract names one
durable result and evidence surface; every result, withheld closure and
residual obligation is recorded there before return, a conversation return
alone is not durable evidence, and if no such surface is authorised and
available, admission refuses (P4b). Absent or rejected admission returns
the missing work authority without execution, as `admission_refused` with
its cause ([§3 Admission and activation](#admission-and-activation)).
Provenance:
[work-carrier-to-execution rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
and
[execution contract admission](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-contract-admission);
the selection of the carrier (ticket, sprint entry, run-scoped contract)
is tier-2 law in the [TICKETS](TICKETS.md) member, which disposes those rows.
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#authority-and-adoption` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#authority-and-adoption` at rc.2:

```text
## Authority And Adoption

This profile owns only the application-neutral record, relation, identity,
causal, effect-boundary, frontier, and refusal laws above.

It grants no semantic, operation, evaluation, admission, decision, correction,
continuation, or closure authority. Every material operation and judgment
resolves an existing owner-issued grant. Copying a profile record or adopting
the profile transfers no authority.

A Product adoption declares at least:

- the exact traversal-occurrence-profile basis;
- the exact subject and subject-binding interpretation;
- mappings from Product concepts to profile sorts and relation kinds;
- operation, actor, executor, admission, projection, and decision authorities;
- event scope and frontier laws;
- invalidation and re-entry conditions; and
- qualification evidence proving that no Product distinction was lost.

An absent or incomplete adoption means the profile is available but inactive
for that Product.
```

Successor, `TRAVERSAL_OCCURRENCE.md#authority-and-adoption`:

```text
## Authority and adoption

This profile owns only the application-neutral record, relation, identity,
causal, effect-boundary, frontier and refusal laws above. It grants no
semantic, operation, evaluation, admission, decision, correction,
continuation or closure authority. Every material operation and judgment
resolves an existing owner-issued grant. Copying a profile record or
adopting the profile transfers no authority (P6).

Only Product authority adopts the profile, as
[PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)
states for every available profile; this section adds no adopter. For
this profile, a Product adoption declares at least (P6, P1):

- the exact traversal-occurrence-profile basis;
- the exact subject and subject-binding interpretation;
- mappings from Product concepts to profile sorts and relation kinds;
- operation, actor, executor, admission, projection and decision
  authorities;
- event scope and frontier laws;
- invalidation and re-entry conditions; and
- qualification evidence proving that no Product distinction was lost.

An absent or incomplete adoption means the profile is available but
inactive for that Product (P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation` at rc.2:

```text
## Candidate, Judgment, Event, And Relation Separation

The admission relation is:

```text
RelationClaim c
  -> Judgment j_c over unchanged c
  -> candidate FrameworkEvent e binding c, j_c, and source frontier F_k
  -> Judgment j_e over unchanged e
  -> deterministic TypedRelation r materialized from (c, j_c, e, j_e, basis)
  -> successor frontier F_k_plus_1
  -> SemanticAdmissionCut a = (c, j_c, e, j_e, r, F_k, F_k_plus_1)
  -> Judgment j_a over unchanged a
```

Only `j_c.decision = admitted`, `j_e.decision = admitted`, and
`j_a.decision = admitted` admit the complete semantic cut. `c`, `j_c`, `e`,
`j_e`, `r`, `a`, and `j_a` have distinct identities and authority.
Construction of `c` does not admit it. Judgment does not rewrite its subject.
An event does not inherit the candidate's authority. Materialization cannot
change the relation kind, endpoints, qualifiers, or basis accepted by `j_c`.

The three judgments are exact inherited `Judgment` records:

```text
j_c.kind = claim_admission
j_c.subject = c.id
j_c.subject_digest = sha256(canonical bytes of c)

j_e.kind = event_admission
j_e.subject = e.id
j_e.subject_digest = sha256(canonical bytes of e)

j_a.kind = semantic_cut_admission
j_a.subject = a.id
j_a.subject_digest = sha256(canonical bytes of a)
```

Each judgment has the complete inherited context, owner, scope, basis,
evaluator, authority, decision, evidence, provenance, and decision-time
fields. A missing cut judgment, non-`admitted` decision, wrong subject or
digest, or cross-basis judgment refuses the semantic cut.

An admission event identity binds its event kind, payload digest, scope,
optional occurrence, exact claim, claim judgment, source frontier, owner,
scope, and basis. The materialized relation identity binds the unchanged claim,
claim judgment, event, event judgment, and profile basis.
`frontier_contains(F, e)` holds exactly when `e` appears once in
`F.value.member_event_refs`; neither representation may contain an extra or
missing event.

For claim admission, `e.value.event_kind_ref` is exactly
`urn:stdo:traversal-occurrence:event-kind:claim-admission`. The following refs
are identical, not merely equivalent or adjacent:

```text
c.value.source_frontier_ref
  = e.value.source_frontier_ref
  = a.value.source_frontier_ref
```

`a.value.successor_frontier_ref` resolves a frontier whose exact member set is
the source frontier member set plus `e.id` once. The cut's claim, claim
judgment, event, event judgment, relation, source frontier, and successor
frontier refs each resolve the unchanged record judged or materialized.

All seven cut subjects, all three judgments, and the three required relation
records share the exact profile basis. The source and successor frontiers also
share `projection_basis_ref` and `precedence_law_ref`; the only permitted
frontier-content delta is addition of `e.id` once. The cut includes exactly:

```text
admits_claim(e, c)
materializes_relation(e, r)
frontier_contains(F_k_plus_1, e)
```

Each edge has the exact inherited relation shape and
`OccurrenceRelationQualifiers`. Missing, extra, reversed, duplicate, or
cross-basis required edges refuse the cut. The source frontier must not already
contain `e`; duplicate frontier members refuse before set comparison.

A first event needs no fictional predecessor. Re-admission of the same claim,
claim judgment, event judgment, source frontier, basis, and authority returns
the existing byte-equal semantic cut. Any non-identical collision refuses
`refuse_duplicate`; it never mints rival facts.

The endpoints of a pre-admission `RelationClaim` already exist. The generated
`admits_claim` and `materializes_relation` records are post-admission relations,
not claims that contain their own future event endpoint.

### OP-002 Atomic Semantic Admission

For a relation claim, one admitted semantic cut contains the unchanged claim,
its admission judgment, the event and its scope/admission judgment, the
deterministic materialized relation, the exact source frontier, and the unique
successor frontier. The source frontier named by the claim, event, and cut is
identical. The successor equals that frontier plus exactly the admitted event.
Missing, conflicting, or inconsistent members refuse the cut. This is semantic
atomicity; the profile does not prescribe a storage or transaction mechanism.

### OP-003 Correction Without Erasure

`corrects_event(new, existing)` retains both immutable events. Correction
changes later projection through an explicit selection law. It does not delete,
rewrite, or retrospectively re-identify the corrected fact.
```

Successor, `TRAVERSAL_OCCURRENCE.md#candidate-judgment-event-and-relation-separation`:

```text
## Candidate, judgment, event and relation separation

The admission relation is (P6, P3):

```text
RelationClaim c
  -> Judgment j_c over unchanged c
  -> candidate FrameworkEvent e binding c, j_c, and source frontier F_k
  -> Judgment j_e over unchanged e
  -> deterministic TypedRelation r materialized from (c, j_c, e, j_e, basis)
  -> successor frontier F_k_plus_1
  -> SemanticAdmissionCut a = (c, j_c, e, j_e, r, F_k, F_k_plus_1)
  -> Judgment j_a over unchanged a
```

Only `j_c.decision = admitted`, `j_e.decision = admitted` and
`j_a.decision = admitted` together admit the complete semantic cut. `c`,
`j_c`, `e`, `j_e`, `r`, `a` and `j_a` have distinct identities and
authority. Constructing `c` does not admit it. A judgment does not rewrite
its subject. An event does not inherit the candidate's authority.
Materialisation cannot change the relation kind, endpoints, qualifiers or
basis that `j_c` accepted (P6, P3).

The three judgments are exact inherited `Judgment` records (P6):

```text
j_c.kind = claim_admission
j_c.subject = c.id
j_c.subject_digest = sha256(canonical bytes of c)

j_e.kind = event_admission
j_e.subject = e.id
j_e.subject_digest = sha256(canonical bytes of e)

j_a.kind = semantic_cut_admission
j_a.subject = a.id
j_a.subject_digest = sha256(canonical bytes of a)
```

Each judgment has the complete inherited context, owner, scope, basis,
evaluator, authority, decision, evidence, provenance and decision-time
fields. A missing cut judgment, a decision other than `admitted`, a wrong
subject or digest, or a judgment across bases refuses the semantic cut
(P6, P5).

An admission event's identity binds its event kind, payload digest,
scope, optional occurrence, exact claim, claim judgment, source frontier,
owner, scope and basis. The materialised relation's identity binds the
unchanged claim, claim judgment, event, event judgment and profile basis.
`frontier_contains(F, e)` holds exactly when `e` appears once in
`F.value.member_event_refs`; neither representation may hold an extra or a
missing event (P3).

For claim admission, `e.value.event_kind_ref` is exactly
`urn:stdo:traversal-occurrence:event-kind:claim-admission`, and these refs
are identical, not merely equivalent or adjacent (P3):

```text
c.value.source_frontier_ref
  = e.value.source_frontier_ref
  = a.value.source_frontier_ref
```

`a.value.successor_frontier_ref` resolves a frontier whose exact member
set is the source frontier's member set plus `e.id` once. The cut's claim,
claim judgment, event, event judgment, relation, source frontier and
successor frontier refs each resolve the unchanged record judged or
materialised (P3, P4b).

All seven cut subjects, all three judgments and the three required
relation records share the exact profile basis. The source and successor
frontiers also share `projection_basis_ref` and `precedence_law_ref`, and
the only permitted difference in frontier content is the addition of
`e.id` once. The cut includes exactly (P3, P4b):

```text
admits_claim(e, c)
materializes_relation(e, r)
frontier_contains(F_k_plus_1, e)
```

Each edge has the exact inherited relation shape and
`OccurrenceRelationQualifiers`. Missing, extra, reversed, duplicate or
cross-basis required edges refuse the cut. The source frontier must not
already contain `e`, and duplicate frontier members refuse before any set
comparison (P3, P5).

A first event needs no fictional predecessor. Re-admission of the same
claim, claim judgment, event judgment, source frontier, basis and
authority returns the existing byte-equal semantic cut. Any collision that
is not identical refuses with `refuse_duplicate` and never mints rival
facts (P3, P6).

The endpoints of a pre-admission `RelationClaim` already exist. The
generated `admits_claim` and `materializes_relation` records are
post-admission relations, not claims that contain their own future event
endpoint (P3).

### OP-002 Atomic semantic admission

For a relation claim, one admitted semantic cut contains the unchanged
claim, its admission judgment, the event and its scope and admission
judgment, the deterministic materialised relation, the exact source
frontier, and the unique successor frontier. The source frontier that the
claim, the event and the cut name is one identical frontier, and the
successor equals that frontier plus exactly the admitted event. Missing,
conflicting or inconsistent members refuse the cut. This atomicity is
semantic; the profile prescribes no storage or transaction mechanism (P3,
P4b, P6).

### OP-003 Correction without erasure

`corrects_event(new, existing)` keeps both immutable events. A correction
changes later projection through an explicit selection law; it does not
delete, rewrite or retrospectively re-identify the corrected fact (P3,
P4b).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#causality-and-typed-lineage` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#causality-and-typed-lineage` at rc.2:

```text
## Causality And Typed Lineage

Three graph families remain distinct:

```text
G_id          identity-dependency DAG
G_occ_cause   declared occurrence-causation DAG
G_evt_cause   declared event-causation DAG
```

Each is acyclic under its own typed relation. Cause is established only by an
admitted causal claim under competent authority and evidence. Timestamp,
ordinal, adjacency, containment, common subject, shared actor, correlation,
and arrival order do not create cause.

The wider typed-lineage graph may lawfully contain opposing edges of different
kinds. For example, one event may support another while the second corrects
the first. A cycle in the untyped union is not a causal cycle unless one
declared causal subgraph itself cycles.

### OP-004 Precedence Is Not Authority

A projection may use a declared precedence coordinate to select current truth.
The coordinate, comparison law, basis, and admitting authority are explicit.
The coordinate orders eligible facts; it does not gain semantic, admission,
causal, or decision authority.
```

Successor, `TRAVERSAL_OCCURRENCE.md#causality-and-typed-lineage`:

```text
## Causality and typed lineage

Three graph families stay distinct (P3, P6):

```text
G_id          identity-dependency DAG
G_occ_cause   declared occurrence-causation DAG
G_evt_cause   declared event-causation DAG
```

Each is acyclic under its own typed relation. Cause is established only by
an admitted causal claim under competent authority and evidence.
Timestamp, ordinal, adjacency, containment, a common subject, a shared
actor, correlation and arrival order do not create cause (P6, P3).

The wider typed-lineage graph may lawfully contain opposing edges of
different kinds: one event may support another while the second corrects
the first. A cycle in the untyped union is not a causal cycle unless one
declared causal subgraph itself cycles (P3).

### OP-004 Precedence is not authority

A projection may use a declared precedence coordinate to select current
truth. The coordinate, its comparison law, its basis and its admitting
authority are explicit. The coordinate orders eligible facts; it gains no
semantic, admission, causal or decision authority (P6, P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-constraint-judgment-residual-and-stop-kinds` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-constraint-judgment-residual-and-stop-kinds` at rc.2:

```text
## Closed Constraint, Judgment, Residual, And Stop Kinds

The core constraint kinds are:

```text
identity_dependency_acyclic
occurrence_causation_acyclic
event_causation_acyclic
occurrence_seed_complete
relation_claim_admissible
semantic_cut_complete
pre_effect_current
operation_grant_contains_effect
event_scope_compatible
frontier_complete
transition_subject_complete
```

The core judgment kinds are:

```text
model_validation
occurrence_admission
event_admission
claim_admission
semantic_cut_admission
effect_readiness
transition_evaluation
frontier_projection
```

The core residual kinds are:

```text
unobserved_subject_state
partial_effect
unresolved_cause
unresolved_scope
competing_lineage
stale_frontier
stale_currentness
unobserved_external_mutation
```

The core stop kinds are:

```text
hold
gap
refusal
invalid_basis
out_of_scope
partial_effect
```

Every constraint predicate returns exactly one of `satisfied`, `falsified`,
`indeterminate`, or `invalid_basis`. `satisfied` maps to the judgment's positive
decision, which is the first decision listed below; `invalid_basis` maps only
to `invalid_basis`. The constraint table fixes every other mapping. An
implementation cannot turn an omitted result, residual, or stop into success.

The closed judgment domains are:

| Judgment kind | Unchanged subject | Decision domain | Required evidence | Stop, residual, and re-entry law |
|---|---|---|---|---|
| `model_validation` | `OccurrenceModelSubject` | `valid`, `hold`, `refused`, `invalid_basis` | exact model id/digest, profile basis, and typed graph populations | refusal or invalid basis; unresolved refs retain `gap` until repaired |
| `occurrence_admission` | `Occurrence` | `admitted`, `hold`, `refused`, `invalid_basis` | exact occurrence id/digest and resolved pre-existing seed inputs | missing seed retains `hold` plus `unresolved_cause`; re-enter with a new complete occurrence candidate |
| `event_admission` | `FrameworkEvent` | `admitted`, `hold`, `refused`, `invalid_basis`, `out_of_scope` | exact event id/digest, payload digest, scope authority, and source frontier | unresolved scope retains `hold` plus `unresolved_scope`; incompatible scope refuses |
| `claim_admission` | `RelationClaim` | `admitted`, `hold`, `refused`, `invalid_basis` | exact claim id/digest, endpoints, qualifiers, claimant authority, and current source frontier | unresolved cause or stale frontier retains `hold`; re-enter with a new claim over the current frontier |
| `semantic_cut_admission` | `SemanticAdmissionCut` | `admitted`, `hold`, `refused`, `invalid_basis` | exact seven-member cut and source/successor frontier equality | incomplete or inconsistent cut refuses; stale source frontier retains `hold` plus `stale_frontier` and requires reconstruction |
| `effect_readiness` | `EffectSubject` | `ready`, `stale`, `unauthorized`, `hold`, `invalid_basis` | exact pre-observation, invocation, operation, grant, territory, and invalidation state | stale yields `hold` plus `stale_currentness` and re-observation; unauthorized yields `refusal` and no dispatch |
| `transition_evaluation` | `TransitionSubject` | `satisfied`, `falsified`, `partial`, `indeterminate`, `refused`, `invalid_basis` | exact pre/post observations, intended outcome, disposition, and bounded effect evidence | partial yields `partial_effect`; indeterminate retains `hold` plus a declared residual; refused yields `refusal` |
| `frontier_projection` | `Projection` | `admitted`, `hold`, `gap`, `refused`, `invalid_basis` | exact projection/frontier ids and digests, complete members, basis, precedence law, boundary, and residuals | stale frontier retains `hold` plus `stale_frontier`; unresolved lineage retains `gap`; re-enter with a new projection |

Each is an inherited `Judgment` and therefore carries unchanged subject id and
digest, evaluator, authority, evidence, provenance, and decision coordinate.
The judgment kind defines the applicable stops and residuals; none is inferred
from prose.

The closed constraint domains are:

| Constraint kind | Subject | Deciding judgment | `falsified` mapping | `indeterminate` mapping |
|---|---|---|---|---|
| `identity_dependency_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `occurrence_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `event_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `occurrence_seed_complete` | `Occurrence` | `occurrence_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `relation_claim_admissible` | `RelationClaim` | `claim_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` or `stale_frontier` |
| `semantic_cut_complete` | `SemanticAdmissionCut` | `semantic_cut_admission` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
| `pre_effect_current` | `EffectSubject` | `effect_readiness` | `stale` plus `hold` and `stale_currentness` | `hold` plus `stale_currentness` |
| `operation_grant_contains_effect` | `EffectSubject` | `effect_readiness` | `unauthorized` plus `refusal` | `hold` plus `unobserved_subject_state` |
| `event_scope_compatible` | `FrameworkEvent` | `event_admission` | `out_of_scope` plus `refusal` | `hold` plus `unresolved_scope` |
| `frontier_complete` | `Projection` | `frontier_projection` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
| `transition_subject_complete` | `TransitionSubject` | `transition_evaluation` | `refused` plus `refusal` | `indeterminate` plus `unobserved_subject_state` |

Each constraint declares zero latitude unless its exact record names a
`latitude_ref`. Silence is not latitude. The residual kind fixes re-entry:

| Residual kind | Subject | Required re-entry |
|---|---|---|
| `unobserved_subject_state` | `SubjectBinding` | acquire a bounded observation or retain hold |
| `partial_effect` | `EffectInvocation` | acquire post-observation and explicit disposition |
| `unresolved_cause` | claim or event | acquire authority and evidence or retain unresolved |
| `unresolved_scope` | `FrameworkEvent` | declare lawful scope or refuse admission |
| `competing_lineage` | `EventFrontier` | apply an authorized `frontier_projection` judgment |
| `stale_frontier` | `Projection` | construct a new exact frontier and projection |
| `stale_currentness` | `EffectSubject` | re-observe and re-judge before effect |
| `unobserved_external_mutation` | `SubjectBinding` | observe or retain an explicit material unknown |

`Sigma_occurrence.FunctorKind` contains exact refs to `F_D`, `F_P`, and `F_H`
from `b_ac` and no other functor kind. The profile changes none of their laws.
```

Successor, `TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds`:

```text
## Closed constraint, judgment, residual and stop kinds

The core constraint kinds are (P3, P5):

```text
identity_dependency_acyclic
occurrence_causation_acyclic
event_causation_acyclic
occurrence_seed_complete
relation_claim_admissible
semantic_cut_complete
pre_effect_current
operation_grant_contains_effect
event_scope_compatible
frontier_complete
transition_subject_complete
```

The core judgment kinds are (P6):

```text
model_validation
occurrence_admission
event_admission
claim_admission
semantic_cut_admission
effect_readiness
transition_evaluation
frontier_projection
```

The core residual kinds are (P4b, P5):

```text
unobserved_subject_state
partial_effect
unresolved_cause
unresolved_scope
competing_lineage
stale_frontier
stale_currentness
unobserved_external_mutation
```

The core stop kinds are (P5):

```text
hold
gap
refusal
invalid_basis
out_of_scope
partial_effect
```

Every constraint predicate returns exactly one of `satisfied`,
`falsified`, `indeterminate` or `invalid_basis`. This value set refines
the constraint outcomes of
[AXIOMATIC_CALCULUS AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
by excluding `out_of_frame`. The reason: each constraint in the table
below is evaluated only on the record kind its row names and inside the
scope its row declares, so AC-007's out-of-scope case, a predicate asked
outside its `applies_to`, does not arise. An event whose declared scope
conflicts with the admitting authority falsifies `event_scope_compatible`;
the stop `out_of_scope` is that falsification, mapped below with the
difference from `out_of_frame` stated. `satisfied` maps to the
judgment's positive decision, the first decision listed below;
`invalid_basis` maps only to `invalid_basis`; the constraint table fixes
every other mapping. An implementation cannot turn an omitted result, a
residual or a stop into success (P5, P6).

The closed judgment domains are (P6, P5):

| Judgment kind | Unchanged subject | Decision domain | Required evidence | Stop, residual, and re-entry law |
|---|---|---|---|---|
| `model_validation` | `OccurrenceModelSubject` | `valid`, `hold`, `refused`, `invalid_basis` | exact model id/digest, profile basis, and typed graph populations | refusal or invalid basis; unresolved refs retain `gap` until repaired |
| `occurrence_admission` | `Occurrence` | `admitted`, `hold`, `refused`, `invalid_basis` | exact occurrence id/digest and resolved pre-existing seed inputs | missing seed retains `hold` plus `unresolved_cause`; re-enter with a new complete occurrence candidate |
| `event_admission` | `FrameworkEvent` | `admitted`, `hold`, `refused`, `invalid_basis`, `out_of_scope` | exact event id/digest, payload digest, scope authority, and source frontier | unresolved scope retains `hold` plus `unresolved_scope`; incompatible scope refuses |
| `claim_admission` | `RelationClaim` | `admitted`, `hold`, `refused`, `invalid_basis` | exact claim id/digest, endpoints, qualifiers, claimant authority, and current source frontier | unresolved cause or stale frontier retains `hold`; re-enter with a new claim over the current frontier |
| `semantic_cut_admission` | `SemanticAdmissionCut` | `admitted`, `hold`, `refused`, `invalid_basis` | exact seven-member cut and source/successor frontier equality | incomplete or inconsistent cut refuses; stale source frontier retains `hold` plus `stale_frontier` and requires reconstruction |
| `effect_readiness` | `EffectSubject` | `ready`, `stale`, `unauthorized`, `hold`, `invalid_basis` | exact pre-observation, invocation, operation, grant, territory, and invalidation state | stale yields `hold` plus `stale_currentness` and re-observation; unauthorized yields `refusal` and no dispatch |
| `transition_evaluation` | `TransitionSubject` | `satisfied`, `falsified`, `partial`, `indeterminate`, `refused`, `invalid_basis` | exact pre/post observations, intended outcome, disposition, and bounded effect evidence | partial yields `partial_effect`; indeterminate retains `hold` plus a declared residual; refused yields `refusal` |
| `frontier_projection` | `Projection` | `admitted`, `hold`, `gap`, `refused`, `invalid_basis` | exact projection/frontier ids and digests, complete members, basis, precedence law, boundary, and residuals | stale frontier retains `hold` plus `stale_frontier`; unresolved lineage retains `gap`; re-enter with a new projection |

Each is an inherited `Judgment` and so carries the unchanged subject id
and digest, evaluator, authority, evidence, provenance and decision
coordinate. The judgment kind defines the applicable stops and residuals;
none is inferred from prose (P6, P3).

The closed constraint domains are (P5):

| Constraint kind | Subject | Deciding judgment | `falsified` mapping | `indeterminate` mapping |
|---|---|---|---|---|
| `identity_dependency_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `occurrence_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `event_causation_acyclic` | `OccurrenceModelSubject` | `model_validation` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `occurrence_seed_complete` | `Occurrence` | `occurrence_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` |
| `relation_claim_admissible` | `RelationClaim` | `claim_admission` | `refused` plus `refusal` | `hold` plus `unresolved_cause` or `stale_frontier` |
| `semantic_cut_complete` | `SemanticAdmissionCut` | `semantic_cut_admission` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
| `pre_effect_current` | `EffectSubject` | `effect_readiness` | `stale` plus `hold` and `stale_currentness` | `hold` plus `stale_currentness` |
| `operation_grant_contains_effect` | `EffectSubject` | `effect_readiness` | `unauthorized` plus `refusal` | `hold` plus `unobserved_subject_state` |
| `event_scope_compatible` | `FrameworkEvent` | `event_admission` | `out_of_scope` plus `refusal` | `hold` plus `unresolved_scope` |
| `frontier_complete` | `Projection` | `frontier_projection` | `refused` plus `refusal` | `hold` plus `stale_frontier` |
| `transition_subject_complete` | `TransitionSubject` | `transition_evaluation` | `refused` plus `refusal` | `indeterminate` plus `unobserved_subject_state` |

Each constraint declares zero latitude unless its exact record names a
`latitude_ref`; silence is not latitude. The residual kind fixes re-entry
(P5, P4b):

| Residual kind | Subject | Required re-entry |
|---|---|---|
| `unobserved_subject_state` | `SubjectBinding` | acquire a bounded observation or retain hold |
| `partial_effect` | `EffectInvocation` | acquire post-observation and explicit disposition |
| `unresolved_cause` | claim or event | acquire authority and evidence or retain unresolved |
| `unresolved_scope` | `FrameworkEvent` | declare lawful scope or refuse admission |
| `competing_lineage` | `EventFrontier` | apply an authorized `frontier_projection` judgment |
| `stale_frontier` | `Projection` | construct a new exact frontier and projection |
| `stale_currentness` | `EffectSubject` | re-observe and re-judge before effect |
| `unobserved_external_mutation` | `SubjectBinding` | observe or retain an explicit material unknown |

Mapping to the core result algebra, new in this corpus. Purpose:
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states every outcome in
the core or in a refinement that maps each refined value to exactly one
core value, and
[AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds)
requires a traversal's stop algebra to map totally to that core (P5).
Material relation: a consumer that joins an occurrence's results with
other results reads each decision, stop and effect disposition as one
core value with its predicate, so a refusal, a held judgment or a partial
effect is neither read as success nor mistaken for another case (P5, P6).
The profile states three refinements, each with the predicate its mapping
is for:

| Refinement | Predicate of the mapping | Stated in |
|---|---|---|
| judgment decisions | the first decision the judgment kind lists holds for the unchanged subject on the exact basis | this section |
| stop kinds | the traversal application can reach its declared result on the exact basis | this section |
| effect dispositions | the intended effect occurred ([ACTIVATION §3 Effects](ACTIVATION.md#effects)) | [Mutable-subject effect relation](#mutable-subject-effect-relation) |

A judgment decision is the evaluation's result and a stop is the step's.
Where values emitted together map to different core values, as `stale`
with `hold` does, each answers its own predicate. The stop's predicate is
not the predicate of
[construction availability](ACTIVATION.md#construction-availability), "a
candidate is available", and no value counts toward another predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Each value keeps its own vocabulary, residual and re-entry law beside its
core value (FOUNDATIONS §4 Results, Recording) (P5, P6).

Refined by cause. Where a stop or decision would map to one of two core
values according to its cause, the cause is part of the refined value,
written in parentheses as in `refusal(basis)`, and each refined value maps
once (FOUNDATIONS §4 Results, Refinements). The cause is read from what
the record already carries: for a refusal, the conditions it names; for a
`partial_effect` or `partial`, the effect evidence and the bounded
post-observation, read against the intended outcome under its outcome
contract and comparison basis (`IntendedOutcome`).
A refusal's cause is the one that the operation-outcome
rows `refusal(constraint)` and `refusal(basis)` of
[AXIOMATIC_CALCULUS AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
state for the conditions the refusal names: `constraint` where it names a
demonstrated violation by the record, model, carrier, transformation or
application under judgment, whatever condition of the basis it also names,
and `basis` where it names only conditions of the basis, a violation
inside an input that the operation acts on as its basis included. AC-007
gives each cause its core value and reports a basis condition named beside
a violation as its own invalid_basis result. Where a relation qualifier
records the cause, it records it and does not choose it, so this profile
and AC-007 give one refusal one value. The closed populations above are
unchanged; a refined value names a kind and its cause and adds no kind
(P5, P3). The causes are:

- `refusal(basis)`: the refusal names one or more conditions of the basis
  the operation acts on, as AC-007 lists for that value, and no
  demonstrated violation by what is under judgment; where a relation
  qualifier records its cause, it carries `refuse_invalid_basis`, which
  records a condition of the basis and no other cause. A basis mismatch
  inside the model or a record is the mixed bases that AC-007 lists for
  this value, a condition of the basis, so a refusal that names only such
  a mismatch has this cause: a coordinate and basis mismatch or a
  basis-relation mismatch refused at model validation
  ([Finite reference-domain table](#finite-reference-domain-table)), a
  qualifier basis mismatch refused at structural admission
  ([Closed relation families](#closed-relation-families)) and a
  cross-basis required edge that refuses a semantic admission cut
  ([Candidate, judgment, event and relation separation](#candidate-judgment-event-and-relation-separation)).
  None is the counterexample of a structural constraint. A refusal emitted
  with an `invalid_basis` decision, as `model_validation`'s "refusal or
  invalid basis" allows, has this cause where it names no demonstrated
  violation, because that decision names a condition of the basis and its
  repair. Where the refusal also names a demonstrated violation by what is
  under judgment, it has cause `constraint` below, as AC-007 rules, and
  the co-emitted `invalid_basis` decision is the basis condition's own
  result: it keeps invalid_basis for its own predicate, because the
  constraint rule above maps `invalid_basis` only to that core value and
  the judgment table keeps `refused` and `invalid_basis` distinct.
- `refusal(constraint)`: every other refusal, that is, every refusal that
  names a demonstrated violation by what is under judgment, whatever
  condition of the basis it also names, or names no condition that AC-007
  lists for `refusal(basis)`. The record, model, carrier, transformation
  or application under judgment violates a constraint of the occurrence
  signature, as AC-007 states for this value, and a basis condition the
  refusal also names is recorded with it and reported as its own
  invalid_basis result. It follows a falsified constraint, and the defect
  it names is the counterexample; where a relation qualifier records its
  cause, it carries `refuse_missing`, `refuse_duplicate`,
  `refuse_wrong_type` or `refuse_out_of_scope`. The falsified constraint
  is one of three: a row of the constraint table, which maps `falsified`
  to `refused` plus `refusal`; a structural constraint, named below; or
  the requirement that an admitted event carry a lawful declared scope. A
  refusal of admission under the `unresolved_scope` re-entry is a
  judgment-level refusal, which no relation qualifier records, and it takes
  this cause from the condition it names under AC-007, as every refusal
  does: `event_admission` requires the event's scope authority as evidence
  and the re-entry names the lawful scope declaration as what must be
  supplied, so the event candidate still lacking it when the re-entry
  closes is a demonstrated violation by the event under judgment and the
  counterexample. The `unresolved_scope` residual is retained, naming the
  undeclared scope, and re-entry is a new event
  candidate with a lawful declared scope. A seed that falsifies
  `occurrence_seed_complete`, an event scope missing when that re-entry
  closes or incompatible with the admitting authority, and a duplicate,
  missing, extra, reversed or mismatched edge are each a defect of the
  occurrence or event under judgment that violates a constraint of the
  signature. None is the seed set, scope or required-edge semantics of the
  basis the operation acts on, which AC-007 lists for `refusal(basis)`, so
  a refusal for any of them has this cause there. The same defect can bear
  on the predicate of another operation that acts on that record as its
  basis, as AC-007 rules (P5, P6).
- `refused(basis)` and `refused(constraint)`: decision `refused` of any
  judgment, by the cause of the refusal it yields, which the conditions
  that refusal names decide under AC-007 as above: `refused(basis)` when
  that refusal is `refusal(basis)`, otherwise `refused(constraint)`.
- `partial_effect(not_attained)`: the admitted evidence establishes that
  the intended outcome is not met and that no later completion of the
  effect can meet it. The effect evidence and the bounded
  post-observation, read under the outcome contract, show the intended
  outcome not met where nothing left of the effect can meet it, for
  example where the effect has ended short, or an interval that the
  outcome contract bounds has closed with only part reached, or the part
  already done has itself defeated the outcome, such as an effect that
  has already deleted a record the outcome requires, which no later
  completion of the effect restores. The evidence
  of non-attainment, such as the unreached part, is the counterexample.
  Whether the effect has ended is not part of this cause: where the
  evidence does not establish the end, the `partial_effect`
  residual records it beside the value, as
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) states.
- `partial_effect(undecided)`: every other `partial_effect`, that is,
  one whose admitted evidence does not establish non-attainment. The
  admitted evidence cannot decide whether the intended outcome is or will be met:
  the bounded post-observation that the
  [effect law](#mutable-subject-effect-relation) requires is not yet
  acquired, or it shows part reached while a later completion of the
  effect could still meet the outcome, or it shows the outcome met while
  the effect may still be acting, so whether the outcome is met once the
  effect settles is undecided, or a response was lost and no
  counterexample is observed. A lost response, an absent record or an
  actor's context holding no trace of the effect is no evidence about the
  subject, so it establishes neither non-attainment nor the end of the
  effect ([ACTIVATION §3 Effects](ACTIVATION.md#effects)).
- `partial(not_attained)` and `partial(undecided)`: decision `partial` of
  `transition_evaluation`, by the cause of the stop `partial_effect` it
  yields.

| Value | Core value | Ground |
|---|---|---|
| stop `hold` | indeterminate | the step stops with the deciding evidence not yet admitted (missing seed, unresolved cause or scope, stale frontier or currentness, unobserved state), so the admissible evidence cannot decide whether the application can reach its declared result ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); rc.2 RF-012); its residual names the evidence that would decide |
| stop `gap` | invalid_basis | a reference or lineage member the judgment requires is unresolved, its resolution still open as AC-007 defines for `gap`, so the closure it rests on is undefined on this basis (AC-003, AC-010) and the basis cannot support the judgment until repaired |
| stop `refusal(constraint)` | falsified | the falsified constraint's defect is the counterexample, as construction availability maps `refused` to falsified (P5, P6) |
| stop `refusal(basis)` | invalid_basis | the basis cannot support the judgment; the constraint rule above maps `invalid_basis` only to that core value |
| stop `invalid_basis` | invalid_basis | the same core value; the constraint rule above maps `invalid_basis` only to it |
| stop `out_of_scope` | falsified | it is emitted only with `refusal`, when `event_scope_compatible` is falsified by a declared scope that conflicts with the admitting authority; an event scope not yet declared is `hold` plus `unresolved_scope` while the signature declares the scope relation, so the ground of out_of_frame, a missing declaration in the frame, is absent, and the spelling is not the core's out_of_frame; a refusal of admission once that re-entry closes without the declaration is stop `refusal(constraint)`, its cause taken from AC-007's condition as for every refusal, not this stop (P5, P6) |
| stop `partial_effect(not_attained)` | falsified | the unreached part of the intended outcome, which no later completion of the effect can reach, defeats the declared result; an end of the effect that the evidence does not establish takes no part in the value and is recorded in the `partial_effect` residual, which stays with the value with explicit re-entry before any further effect (P5, P6) |
| stop `partial_effect(undecided)` | indeterminate | an effect that has begun and whose evidence cannot decide whether the intended outcome is or will be met supplies no counterexample ([Mutable-subject effect relation](#mutable-subject-effect-relation)), so the admissible evidence cannot decide; the `partial_effect` residual names the post-observation and explicit disposition that would decide (P5, P6) |
| decision `partial(not_attained)` | falsified | the post-observation, read under the outcome contract, shows part of the intended outcome not reached and not reachable by any later completion of the effect, which defeats the transition's positive decision whether or not the effect has ended (P5, P6) |
| decision `partial(undecided)` | indeterminate | the admissible evidence cannot decide whether the transition reaches the intended outcome; the decision's required evidence includes the post-observation, and a missing one is `indeterminate` plus `unobserved_subject_state` under `transition_subject_complete`; the `partial_effect` residual names the explicit disposition that would decide (P5, P6) |
| decision `refused(constraint)` | falsified | the image of a falsified constraint under the constraint table, or of a falsified structural constraint named below (P5, P6) |
| decision `refused(basis)` | invalid_basis | as stop `refusal(basis)` (P5) |

The remaining judgment decisions follow the constraint rule above: the
first decision each judgment lists maps to satisfied; `out_of_scope`,
`unauthorized` and `stale`, which the constraint table makes the images
of a falsified constraint, map to falsified; `hold`, the image of an
indeterminate constraint, maps to indeterminate; `gap` maps to
invalid_basis on the ground of the stop so named; and `invalid_basis` and
the `falsified` and `indeterminate` of `transition_evaluation` map to the
core values so named (P5, P6).

This mapping holds for every traversal under this profile's signature; a
traversal does not re-map it. `hold`, `gap`, `refusal(constraint)` and
`refusal(basis)` have the meanings and core values that
[AXIOMATIC_CALCULUS AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
gives them, as the table above states. A traversal record's `stop_states`
may refine those four values by cause for that traversal, by a binding
declared in the shape of [PROFILES §1](PROFILES.md#1-the-boundary): its
direction, preserved meaning, narrowed scope and invalidation. A refined
value adds no kind and takes its core value under the parent-value rule
of [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds),
which this profile applies and does not restate. The other stops and
every judgment decision keep the mapping above unrefined, and a record
that declares no binding takes it unrefined (P5, P3, P1).

A structural refusal is one whose source is this profile's closed
structure rather than a row of the constraint table: an unknown or missing
required field under the closed value contract
([Closed semantic-object sorts](#closed-semantic-object-sorts)); a
missing population, hidden record, ambiguous ref, unknown record kind or
undeclared field domain
([Imported calculus boundary](#imported-calculus-boundary)); a missing
row, target outside its row, wrong population or sort, unresolved
external target, cardinality violation or nested coordinate or witness
defect refused at model validation
([Finite reference-domain table](#finite-reference-domain-table)); an
unknown event kind, wrong payload sort, mismatched payload digest or
forbidden claim or occurrence field refused at event admission
([Closed event-kind population](#closed-event-kind-population)); and a
qualifier-record defect refused at structural admission, a ref outside
the closed `ProfileRecordRef` union, resolved under a wrong population or
sort or absent from its declared external domain, and a duplicate,
missing, extra, reversed or mismatched edge refused at occurrence
admission ([Closed relation families](#closed-relation-families)). Each
is the refusal of a falsified structural constraint: the closed structure
is the declared predicate, and the unknown kind, unknown or missing
field, wrong type or mismatched edge is the counterexample that defeats
it (FOUNDATIONS §4 Results). A basis mismatch at any of these sources
is not among them: it is the mixed bases of AC-007, a condition of the
basis, so a refusal that names only such a mismatch takes
`refusal(basis)`, as stated for that value above. A stop `refusal` or
decision `refused` from such a source therefore takes
`refusal(constraint)` or `refused(constraint)`, and takes
`refusal(basis)` or `refused(basis)` only under the cause stated for
those values, as every refusal does: a source in the closed structure
does not make a refusal an invalid basis (P5, P6). A required reference
that `model_validation` leaves unresolved, its resolution still open as
AC-007 defines for `gap`, is not refused: it retains `gap` until repaired
and maps to invalid_basis by that stop's row. A reference evaluated to no
target, a local reference with no record in the closed populations
included, is dangling and refuses under
[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) (P5). Where a
relation qualifier records the cause of a refusal, the qualifier, not
the core value, records whether the defect is a missing, duplicate,
wrong-typed or out-of-scope input or an invalid basis; the stop keeps it
in its own vocabulary, so the mapping drops none of the distinctions the
qualifier draws (P5, P4b).

Neither core value to which the `partial` and `partial_effect` values map
records that the subject changed or whether the effect has ended. The
`partial_effect` residual and its re-entry carry both facts and survive
every join
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Falsified never licenses treating the effect as absent; indeterminate
never licenses treating it as absent or as complete; neither licenses
treating it as ended where the evidence does not establish its end. Under
either value the explicit re-entry precedes any further effect, and an
effect whose end is not established is reconciled under
[ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) before any
repetition (P5, P4b).

`Sigma_occurrence.FunctorKind` contains exact refs to `F_D`, `F_P` and
`F_H` from `b_ac` and no other functor kind. The profile changes none of
their laws, which are AXIOMATIC_CALCULUS §5 (P3, P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-event-kind-population` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-event-kind-population` at rc.2:

```text
## Closed Event-Kind Population

`FrameworkEvent.value.event_kind_ref` resolves exactly one member of this
closed population:

```text
EventKind_occurrence = {
  urn:stdo:traversal-occurrence:event-kind:claim-admission,
  urn:stdo:traversal-occurrence:event-kind:occurrence-admission,
  urn:stdo:traversal-occurrence:event-kind:effect-disposition,
  urn:stdo:traversal-occurrence:event-kind:external-fact-admission
}
```

| Event kind | Required payload | Required scope and bindings |
|---|---|---|
| `claim-admission` | exact `RelationClaim` | exact claim and claim-judgment refs; source frontier equals the claim frontier; occurrence ref follows `scope_class` |
| `occurrence-admission` | exact `Occurrence` | `occurrence_scoped`; occurrence ref equals the payload ref; claim fields absent |
| `effect-disposition` | exact `EffectDisposition` | `occurrence_scoped`; occurrence ref equals the invocation's occurrence; claim fields absent |
| `external-fact-admission` | exact non-event `ProfileRecordRef` | `subject_scoped` or `authority_scoped`; occurrence and claim fields absent |

The short labels in the table denote the exact identities above. Payload ref
and digest bind the unchanged payload. An unknown event kind, wrong payload
sort, mismatched payload digest, incompatible scope, or forbidden claim or
occurrence field refuses `event_admission`. A compatible extension declares a
new EventKind population and relation to this signature; it cannot add an
undeclared value to this population.
```

Successor, `TRAVERSAL_OCCURRENCE.md#closed-event-kind-population`:

```text
## Closed event-kind population

`FrameworkEvent.value.event_kind_ref` resolves exactly one member of this
closed population (P3):

```text
EventKind_occurrence = {
  urn:stdo:traversal-occurrence:event-kind:claim-admission,
  urn:stdo:traversal-occurrence:event-kind:occurrence-admission,
  urn:stdo:traversal-occurrence:event-kind:effect-disposition,
  urn:stdo:traversal-occurrence:event-kind:external-fact-admission
}
```

| Event kind | Required payload | Required scope and bindings |
|---|---|---|
| `claim-admission` | exact `RelationClaim` | exact claim and claim-judgment refs; source frontier equals the claim frontier; occurrence ref follows `scope_class` |
| `occurrence-admission` | exact `Occurrence` | `occurrence_scoped`; occurrence ref equals the payload ref; claim fields absent |
| `effect-disposition` | exact `EffectDisposition` | `occurrence_scoped`; occurrence ref equals the invocation's occurrence; claim fields absent |
| `external-fact-admission` | exact non-event `ProfileRecordRef` | `subject_scoped` or `authority_scoped`; occurrence and claim fields absent |

The short labels in the table denote the exact identities above. The
payload ref and digest bind the unchanged payload. An unknown event kind,
a wrong payload sort, a mismatched payload digest, an incompatible scope,
or a forbidden claim or occurrence field refuses `event_admission`. A
compatible extension declares a new event-kind population and its relation
to this signature; it cannot add an undeclared value to this population
(P3, P5).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature` at rc.2:

```text
### Closed Profile Signature

```text
TraversalOccurrenceSignature = {
  kind: "stdo.traversal-occurrence-signature",
  schema_version: 1,
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  calculus_signature_schema_clause_ref:
    absolute semantic address of the Core Signature clause inside that basis,
  occurrence_signature_clause_refs:
    sorted non-empty absolute semantic-address URI[],
  profile_member_sha256: "sha256:" + 64 lowercase hexadecimal characters
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes. Its identity is:

```text
sha256(JCS(TraversalOccurrenceSignature))
```

`calculus_signature_schema_clause_ref` resolves the exact inherited signature
schema and record law. `occurrence_signature_clause_refs` resolves exactly
these fragments against the publication member URI:

```text
#authority-and-adoption
#candidate-judgment-event-and-relation-separation
#causality-and-typed-lineage
#closed-constraint-judgment-residual-and-stop-kinds
#closed-event-kind-population
#closed-relation-families
#closed-semantic-object-sorts
#event-frontier-and-projection
#mutable-subject-effect-relation
#occurrence-identity
```

Together they define this profile's closed sorts, fields, value domains,
relations, constraints, judgments, residuals, stops, and exact functor-kind
refs. The list is duplicate-free and sorted by ascending unsigned UTF-16 code
units. `profile_member_sha256` equals the publication member digest. This gives
`occurrence_signature_sha256` one reconstructable preimage rather than an
implementation-defined serialization.

Every clause ref is an absolute URI whose base is the exact publication
`member_uri`; only its fragment differs. The calculus clause ref is an absolute
URI inside the exact calculus publication basis. Relative paths, mutable source
URIs, missing fragments, duplicate refs, or a ref outside those two exact
publication members refuse the signature.

The exact profile basis is then issued as:

```text
TraversalOccurrenceProfileBasis = {
  kind: "stdo.traversal-occurrence-profile-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:traversal-occurrence-profile",
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  occurrence_signature: TraversalOccurrenceSignature,
  occurrence_signature_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  publication_basis: {
    release_uri: absolute immutable release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

`occurrence_signature_sha256` equals the digest of the embedded canonical
signature. The basis record also uses RFC 8785 JSON Canonicalization Scheme
bytes. Duplicate object names are rejected before canonicalization. Its
identity is:

```text
urn:stdo:traversal-occurrence-profile-basis:sha256:
  + sha256(JCS(TraversalOccurrenceProfileBasis))
```

The imported calculus basis resolves as exact RFC 8785 bytes of an
`AxiomaticCalculusBasis` record with the required kind, schema, concept,
derivation basis, and publication basis. Its calculated identity equals both
`calculus_basis_identity` fields. Its publication manifest digest resolves the
exact manifest bytes; that manifest contains the calculus member path and
digest once; the resolved calculus member bytes have that digest; and
`calculus_signature_schema_clause_ref` is that exact member URI plus
`#core-signature`. Its distinct predecessor manifest resolves every sorted,
duplicate-free `principle_ref` inside the declared predecessor release. The
principle-ref population is exactly the absolute predecessor-release expansion
of every derivation address declared by the resolved calculus member, neither a
selected subset nor an independently invented list. For the calculus edition
bound by this profile publication candidate, that population has fourteen
members. Each referenced predecessor member resolves as exact bytes whose
digest occurs once in the predecessor manifest, and each fragment resolves one
heading in those bytes under the publication's semantic-address rule. A string
with the right shape, an unresolved basis record, a mismatched manifest or
member, a missing or extra principle ref, an invented or absent fragment, an
unbound predecessor byte sequence, or a same-carrier derivation refuses.

The profile publication member resolves by the same manifest/member rule. A
mutable source path, strategy post, implementation, or consumer mapping cannot
substitute for either imported basis or publication identity.

`publication_basis.release_uri` is one absolute immutable
`stdo://releases/v<version>-rc.<positive-ordinal>/` URI.
`publication_basis.member_uri` is exactly that URI plus
`standards/TRAVERSAL_OCCURRENCE_PROFILE.md`. The installed release manifest
named by `manifest_sha256` contains exactly one standards member with that path
and `member_sha256`; the same digest appears in the embedded signature.
Kind and schema-version values are exact. Every digest uses lowercase
`sha256:<64-hex>`. The signature and basis preimages are their exact RFC 8785
JCS values; a newline, alternate object order, duplicate name, non-I-JSON
value, or implementation-specific serialization cannot acquire the declared
identity.

Any change to the calculus basis, signature refs, closed signature, or profile
member bytes mints a new profile basis. Supersession is an external Product and
release judgment; an earlier basis never silently advances.
```

Successor, `TRAVERSAL_OCCURRENCE.md#closed-profile-signature`:

```text
### Closed profile signature

```text
TraversalOccurrenceSignature = {
  kind: "stdo.traversal-occurrence-signature",
  schema_version: 1,
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  calculus_signature_schema_clause_ref:
    absolute semantic address of the Core Signature clause inside that basis,
  occurrence_signature_clause_refs:
    sorted non-empty absolute semantic-address URI[],
  profile_member_sha256: "sha256:" + 64 lowercase hexadecimal characters
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes, and its
identity is (P3):

```text
sha256(JCS(TraversalOccurrenceSignature))
```

`calculus_signature_schema_clause_ref` resolves the exact inherited
signature schema and record law. `occurrence_signature_clause_refs`
resolves exactly these fragments against the publication member URI, each
a heading of this member (P3):

```text
#authority-and-adoption
#candidate-judgment-event-and-relation-separation
#causality-and-typed-lineage
#closed-constraint-judgment-residual-and-stop-kinds
#closed-event-kind-population
#closed-relation-families
#closed-semantic-object-sorts
#event-frontier-and-projection
#mutable-subject-effect-relation
#occurrence-identity
```

Together they define this profile's closed sorts, fields, value domains,
relations, constraints, judgments, residuals, stops and exact functor-kind
refs. The list is free of duplicates and sorted by ascending unsigned
UTF-16 code units. `profile_member_sha256` equals the publication member
digest. `occurrence_signature_sha256` thus has one reconstructable
preimage and no implementation-defined serialisation (P3).

Every clause ref is an absolute URI whose base is the exact publication
`member_uri`; only its fragment differs. The calculus clause ref is an
absolute URI inside the exact calculus publication basis. Relative paths,
mutable source URIs, missing fragments, duplicate refs or a ref outside
those two exact publication members refuse the signature (P3, P5).

The exact profile basis is then issued as (P3):

```text
TraversalOccurrenceProfileBasis = {
  kind: "stdo.traversal-occurrence-profile-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:traversal-occurrence-profile",
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  occurrence_signature: TraversalOccurrenceSignature,
  occurrence_signature_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  publication_basis: {
    release_uri: absolute immutable release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

`occurrence_signature_sha256` equals the digest of the embedded canonical
signature. The basis record also uses RFC 8785 JSON Canonicalization
Scheme bytes, with duplicate object names rejected before
canonicalisation. Its identity is (P3):

```text
urn:stdo:traversal-occurrence-profile-basis:sha256:
  + sha256(JCS(TraversalOccurrenceProfileBasis))
```

The imported calculus basis resolves as the exact RFC 8785 bytes of an
`AxiomaticCalculusBasis` record with the required kind, schema, concept,
derivation basis and publication basis. Its calculated identity equals
both `calculus_basis_identity` fields. Its publication manifest digest
resolves the exact manifest bytes; that manifest contains the calculus
member path and digest once; the resolved calculus member bytes have that
digest; and `calculus_signature_schema_clause_ref` is that exact member
URI plus the fragment of the calculus signature clause, `#2-signature` in
this corpus's AXIOMATIC_CALCULUS. Its distinct predecessor manifest
resolves every sorted principle ref, without duplicates, inside the
declared predecessor release. The principle-ref population is exactly the
absolute predecessor-release expansion of every derivation address that
the resolved calculus member declares: neither a selected subset nor an
independently invented list, and its size is whatever that member's
derivation account declares
([AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity)). Each
referenced predecessor member resolves as exact bytes whose digest occurs
once in the predecessor manifest, and each fragment resolves one heading
in those bytes under the publication's semantic-address rule. A string of
the right shape, an unresolved basis record, a mismatched manifest or
member, a missing or extra principle ref, an invented or absent fragment,
an unbound predecessor byte sequence, or a derivation from the same
carrier refuses (P3, P6, P5).

The profile publication member resolves by the same manifest and member
rule. A mutable source path, a strategy post, an implementation or a
consumer mapping cannot stand in for either imported basis or for the
publication identity (P3, P6).

`publication_basis.release_uri` is one absolute immutable
`stdo://releases/v<version>-rc.<positive-ordinal>/` URI.
`publication_basis.member_uri` is exactly that URI plus
`standards/TRAVERSAL_OCCURRENCE.md`. The installed release manifest named
by `manifest_sha256` contains exactly one standards member with that path
and `member_sha256`, and the same digest appears in the embedded
signature. Kind and schema-version values are exact. Every digest uses
lowercase `sha256:<64-hex>`. The signature and basis preimages are their
exact RFC 8785 JCS values; a newline, another object order, a duplicate
name, a value outside I-JSON or an implementation-specific serialisation
cannot acquire the declared identity (P3).

Any change to the calculus basis, the signature refs, the closed signature
or the profile member bytes mints a new profile basis. Supersession is an
external Product and release judgment, and an earlier basis never silently
advances (P3, P6). The predecessor edition's coordinates are provenance of
this edition, not its identity: cut `stdo://releases/v2.5.1-rc.2/`, member
`standards/TRAVERSAL_OCCURRENCE_PROFILE.md` SHA-256
`618bb7c8f9f1eab8283cf595ac9da3533f0f9cf80a684c6f42e09142da6590c1`,
concept identity unchanged (P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-relation-families` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-relation-families` at rc.2:

```text
## Closed Relation Families

`Sigma_occurrence.RelationKind` contains these typed relation families:

| Relation kind | Source | Target | Core law |
|---|---|---|---|
| `application_of` | `Occurrence` | `TraversalApplication` | target equals the occurrence's exact application seed |
| `applies_traversal` | `TraversalApplication` | exact inherited `Traversal` | target equals the application's and occurrence's traversal ref |
| `bound_to_subject` | `Occurrence` | `SubjectBinding` | exactly one stable subject binding |
| `intends` | `Occurrence` | `IntendedOutcome` | resolves before occurrence identity is minted |
| `observes_before` | `Occurrence` | `Observation` | observation precedes any admitted effect for the occurrence |
| `observes_after` | `Occurrence` | `Observation` | observation follows the admitted effect disposition when an effect occurs |
| `invokes_effect` | `Occurrence` | `EffectInvocation` | optional; requires an exact operation grant |
| `operation_of_kind` | `EffectOperation` | `OperationKind` | exactly one operation kind per operation instance |
| `targets_subject` | `EffectOperation` | `SubjectBinding` | exactly one effect target binding |
| `authorized_by` | `EffectInvocation` | `OperationGrant` | exact grant checked against operation kind, target, and territory |
| `disposition_for` | `EffectDisposition` | `EffectInvocation` | required except for `no_effect`; never rewrites the invocation |
| `evidenced_by` | `EffectInvocation` | `EffectEvidence` | evidence does not become the mutable subject |
| `event_for` | `FrameworkEvent` | `Occurrence` | optional and permitted only by the event's declared scope law |
| `frontier_contains` | `EventFrontier` | `FrameworkEvent` | complete membership under one exact frontier basis |
| `projects_frontier` | `Projection` | `EventFrontier` | exactly one unchanged frontier per projection |
| `identity_depends_on` | `ProfileRecordRef` | `ProfileRecordRef` | earlier identity input; acyclic |
| `causally_precedes_occurrence` | `Occurrence` | `Occurrence` | admitted material cause; acyclic |
| `causally_precedes_event` | `FrameworkEvent` | `FrameworkEvent` | admitted material cause; acyclic |
| `supports_event` | `FrameworkEvent` | `FrameworkEvent` | typed evidential lineage; not cause by implication |
| `corrects_event` | `FrameworkEvent` | `FrameworkEvent` | typed correction lineage; does not erase its target |
| `component_of_occurrence` | `Occurrence` | `Occurrence` | child application belongs to one declared composite application |
| `admits_claim` | `FrameworkEvent` | `RelationClaim` | event binds one unchanged claim and its exact admission judgment |
| `materializes_relation` | `FrameworkEvent` | exact inherited `TypedRelation` | identity derives from claim, both judgments, event, and profile basis |
| `transition_for` | `TransitionSubject` | `Occurrence` | binds the exact transition subject judged |

`ProfileRecordRef` is the closed union of the profile semantic-object records
in `O` and the exact inherited `E`, `C`, `L`, `X`, `V`, `T`, and `J`
populations in the same model. It introduces no ninth record kind. A ref
outside that union, resolved under a wrong population or sort, or absent from
the applicable declared external domain refuses.

Each relation is an exact `TypedRelation`. Its qualifiers close direction,
cardinality, basis, preservation, refusal, and invalidation semantics. The
table is not permission to omit inherited relation fields.

Every profile relation uses exactly this qualifier record:

```text
OccurrenceRelationQualifiers = {
  cardinality,
  authority_ref,
  evidence_refs,
  provenance_refs,
  invalidation_ref,
  inverse_kind_ref_or_none,
  preservation,
  loss,
  refusal
}
```

The qualifier value domains are closed:

```text
cardinality = exactly_one | zero_or_one | zero_or_more | one_or_more
preservation = identity_preserved | meaning_preserved | not_applicable
loss = none | declared_loss
refusal = refuse_missing | refuse_duplicate | refuse_wrong_type
        | refuse_invalid_basis | refuse_out_of_scope | not_applicable
```

The relation kind fixes the qualifier contract. For every core relation `k`:

```text
OccurrenceRelationQualifiers.cardinality = Cardinality_occurrence(k)
OccurrenceRelationQualifiers.preservation = meaning_preserved
OccurrenceRelationQualifiers.loss = none
OccurrenceRelationQualifiers.inverse_kind_ref_or_none = none
OccurrenceRelationQualifiers.refusal in {
  refuse_missing,
  refuse_duplicate,
  refuse_wrong_type,
  refuse_invalid_basis,
  refuse_out_of_scope
}
```

`not_applicable` is unavailable to a core profile relation because every core
relation has an exact preservation and refusal law. The remaining authority,
evidence, provenance, and invalidation refs are exact instance coordinates.

`Cardinality_occurrence` is the following total function over the closed core
relation-kind population:

| Relation kind | Exact cardinality qualifier |
|---|---|
| `application_of` | `exactly_one` |
| `applies_traversal` | `exactly_one` |
| `bound_to_subject` | `exactly_one` |
| `intends` | `exactly_one` |
| `observes_before` | `zero_or_one` |
| `observes_after` | `zero_or_one` |
| `invokes_effect` | `zero_or_one` |
| `operation_of_kind` | `exactly_one` |
| `targets_subject` | `exactly_one` |
| `authorized_by` | `exactly_one` |
| `disposition_for` | `zero_or_one` |
| `evidenced_by` | `zero_or_more` |
| `event_for` | `zero_or_one` |
| `frontier_contains` | `zero_or_more` |
| `projects_frontier` | `exactly_one` |
| `identity_depends_on` | `zero_or_more` |
| `causally_precedes_occurrence` | `zero_or_more` |
| `causally_precedes_event` | `zero_or_more` |
| `supports_event` | `zero_or_more` |
| `corrects_event` | `zero_or_more` |
| `component_of_occurrence` | `zero_or_one` |
| `admits_claim` | `exactly_one` |
| `materializes_relation` | `exactly_one` |
| `transition_for` | `exactly_one` |

Every relation and `RelationClaim.value.relation_qualifiers` has exactly those
nine fields and satisfies the contract selected by its exact relation kind.
The five identity-bearing qualifier fields resolve through the finite reference
table; the four enum fields use only the values above. A missing or extra
field, duplicate ref, unknown enum, kind/cardinality mismatch, incompatible
preservation, declared loss, non-null inverse, unavailable refusal,
unresolved authority, evidence, provenance, invalidation, or inverse-kind ref,
or qualifier basis mismatch refuses structural admission. Materialization
copies the accepted qualifier record byte-for-byte.

For every occurrence `o`, the value preimage and typed relations are exactly
congruent:

```text
target(application_of(o)) = o.value.application_ref
application_of(o).target.value.traversal_ref = o.value.traversal_ref
application_of(o).target.value.functor_kind_ref = o.value.functor_kind_ref
target(applies_traversal(application_of(o).target)) = o.value.traversal_ref
target(bound_to_subject(o)) = o.value.subject_binding_ref
target(intends(o)) = o.value.intended_outcome_ref
targets(identity_depends_on where source = o)
  = set(o.value.identity_dependency_refs)
sources(causally_precedes_occurrence where target = o)
  union sources(component_of_occurrence where target = o)
  = set(o.value.lineage_refs)
```

The equalities are set equality only after list and relation-population
uniqueness is proved. Relation identities and exact `(kind, source, target)`
triples are each duplicate-free; no conversion to a set may erase a duplicate.
Each singleton relation exists exactly once. A duplicate, missing, extra,
reversed, or mismatched edge refuses
`occurrence_admission`; a relation label cannot repair a different identity
preimage. `lineage_refs` contains only admitted occurrence-cause predecessors
and component occurrences of an aggregate. Support, correction, timestamp,
ordinal, adjacency, and correlation edges never enter occurrence lineage.

One occurrence has exactly one `application_of`, `bound_to_subject`, and
`intends` relation. Every traversal application has exactly one
`applies_traversal`; every effect operation has exactly one `operation_of_kind`
and one `targets_subject`; every effect invocation has exactly one
`authorized_by`. One occurrence has zero or one `invokes_effect`; and zero or one pre- and
post-observation relation of each declared observation kind. Every effect
invocation has zero or more `evidenced_by` relations. Every disposition except
`no_effect` has exactly one `disposition_for`; `no_effect` has none. Every
framework event has
zero or one `event_for`. Every projection has exactly one
`projects_frontier`. Every claim-admission event has exactly one `admits_claim`
and exactly one `materializes_relation`. Identity, causal, support, correction,
component, frontier-membership, and evidence relations are finite and
duplicate-free. `inverse_kind_ref_or_none` is explicit; silence does not imply
an inverse.
```

Successor, `TRAVERSAL_OCCURRENCE.md#closed-relation-families`:

```text
## Closed relation families

`Sigma_occurrence.RelationKind` contains these typed relation families
(P3, P4a):

| Relation kind | Source | Target | Core law |
|---|---|---|---|
| `application_of` | `Occurrence` | `TraversalApplication` | target equals the occurrence's exact application seed |
| `applies_traversal` | `TraversalApplication` | exact inherited `Traversal` | target equals the application's and occurrence's traversal ref |
| `bound_to_subject` | `Occurrence` | `SubjectBinding` | exactly one stable subject binding |
| `intends` | `Occurrence` | `IntendedOutcome` | resolves before occurrence identity is minted |
| `observes_before` | `Occurrence` | `Observation` | observation precedes any admitted effect for the occurrence |
| `observes_after` | `Occurrence` | `Observation` | observation follows the admitted effect disposition when an effect occurs |
| `invokes_effect` | `Occurrence` | `EffectInvocation` | optional; requires an exact operation grant |
| `operation_of_kind` | `EffectOperation` | `OperationKind` | exactly one operation kind per operation instance |
| `targets_subject` | `EffectOperation` | `SubjectBinding` | exactly one effect target binding |
| `authorized_by` | `EffectInvocation` | `OperationGrant` | exact grant checked against operation kind, target, and territory |
| `disposition_for` | `EffectDisposition` | `EffectInvocation` | required except for `no_effect`; never rewrites the invocation |
| `evidenced_by` | `EffectInvocation` | `EffectEvidence` | evidence does not become the mutable subject |
| `event_for` | `FrameworkEvent` | `Occurrence` | optional and permitted only by the event's declared scope law |
| `frontier_contains` | `EventFrontier` | `FrameworkEvent` | complete membership under one exact frontier basis |
| `projects_frontier` | `Projection` | `EventFrontier` | exactly one unchanged frontier per projection |
| `identity_depends_on` | `ProfileRecordRef` | `ProfileRecordRef` | earlier identity input; acyclic |
| `causally_precedes_occurrence` | `Occurrence` | `Occurrence` | admitted material cause; acyclic |
| `causally_precedes_event` | `FrameworkEvent` | `FrameworkEvent` | admitted material cause; acyclic |
| `supports_event` | `FrameworkEvent` | `FrameworkEvent` | typed evidential lineage; not cause by implication |
| `corrects_event` | `FrameworkEvent` | `FrameworkEvent` | typed correction lineage; does not erase its target |
| `component_of_occurrence` | `Occurrence` | `Occurrence` | child application belongs to one declared composite application |
| `admits_claim` | `FrameworkEvent` | `RelationClaim` | event binds one unchanged claim and its exact admission judgment |
| `materializes_relation` | `FrameworkEvent` | exact inherited `TypedRelation` | identity derives from claim, both judgments, event, and profile basis |
| `transition_for` | `TransitionSubject` | `Occurrence` | binds the exact transition subject judged |

`ProfileRecordRef` is the closed union of the profile semantic-object
records in `O` and the exact inherited `E`, `C`, `L`, `X`, `V`, `T` and `J`
populations in the same model; it introduces no ninth record kind. A ref
outside that union, resolved under a wrong population or sort, or absent
from the applicable declared external domain refuses (P3, P5).

Each relation is an exact `TypedRelation`. Its qualifiers close direction,
cardinality, basis, preservation, refusal and invalidation semantics; the
table is no permission to omit inherited relation fields. Every profile
relation uses exactly this qualifier record (P3):

```text
OccurrenceRelationQualifiers = {
  cardinality,
  authority_ref,
  evidence_refs,
  provenance_refs,
  invalidation_ref,
  inverse_kind_ref_or_none,
  preservation,
  loss,
  refusal
}
```

The qualifier value domains are closed (P3, P5):

```text
cardinality = exactly_one | zero_or_one | zero_or_more | one_or_more
preservation = identity_preserved | meaning_preserved | not_applicable
loss = none | declared_loss
refusal = refuse_missing | refuse_duplicate | refuse_wrong_type
        | refuse_invalid_basis | refuse_out_of_scope | not_applicable
```

The relation kind fixes the qualifier contract. For every core relation
`k` (P3):

```text
OccurrenceRelationQualifiers.cardinality = Cardinality_occurrence(k)
OccurrenceRelationQualifiers.preservation = meaning_preserved
OccurrenceRelationQualifiers.loss = none
OccurrenceRelationQualifiers.inverse_kind_ref_or_none = none
OccurrenceRelationQualifiers.refusal in {
  refuse_missing,
  refuse_duplicate,
  refuse_wrong_type,
  refuse_invalid_basis,
  refuse_out_of_scope
}
```

`not_applicable` is unavailable to a core profile relation, because every
core relation has an exact preservation and refusal law. The remaining
authority, evidence, provenance and invalidation refs are exact instance
coordinates. `Cardinality_occurrence` is this total function over the
closed core relation-kind population (P3, P5):

| Relation kind | Exact cardinality qualifier |
|---|---|
| `application_of` | `exactly_one` |
| `applies_traversal` | `exactly_one` |
| `bound_to_subject` | `exactly_one` |
| `intends` | `exactly_one` |
| `observes_before` | `zero_or_one` |
| `observes_after` | `zero_or_one` |
| `invokes_effect` | `zero_or_one` |
| `operation_of_kind` | `exactly_one` |
| `targets_subject` | `exactly_one` |
| `authorized_by` | `exactly_one` |
| `disposition_for` | `zero_or_one` |
| `evidenced_by` | `zero_or_more` |
| `event_for` | `zero_or_one` |
| `frontier_contains` | `zero_or_more` |
| `projects_frontier` | `exactly_one` |
| `identity_depends_on` | `zero_or_more` |
| `causally_precedes_occurrence` | `zero_or_more` |
| `causally_precedes_event` | `zero_or_more` |
| `supports_event` | `zero_or_more` |
| `corrects_event` | `zero_or_more` |
| `component_of_occurrence` | `zero_or_one` |
| `admits_claim` | `exactly_one` |
| `materializes_relation` | `exactly_one` |
| `transition_for` | `exactly_one` |

Every relation, and every `RelationClaim.value.relation_qualifiers`, has
exactly those nine fields and satisfies the contract its exact relation
kind selects. The five identity-bearing qualifier fields resolve through
the finite reference-domain table; the four enum fields use only the
values above. A missing or extra field, a duplicate ref, an unknown enum,
a kind and cardinality mismatch, an incompatible preservation, a declared
loss, a non-null inverse, an unavailable refusal, an unresolved authority,
evidence, provenance, invalidation or inverse-kind ref, or a qualifier
basis mismatch refuses structural admission. Materialisation copies the
accepted qualifier record byte for byte (P3, P5).

For every occurrence `o`, the value preimage and the typed relations are
exactly congruent (P3):

```text
target(application_of(o)) = o.value.application_ref
application_of(o).target.value.traversal_ref = o.value.traversal_ref
application_of(o).target.value.functor_kind_ref = o.value.functor_kind_ref
target(applies_traversal(application_of(o).target)) = o.value.traversal_ref
target(bound_to_subject(o)) = o.value.subject_binding_ref
target(intends(o)) = o.value.intended_outcome_ref
targets(identity_depends_on where source = o)
  = set(o.value.identity_dependency_refs)
sources(causally_precedes_occurrence where target = o)
  union sources(component_of_occurrence where target = o)
  = set(o.value.lineage_refs)
```

The equalities are set equalities only after list and relation-population
uniqueness is proved. Relation identities and exact `(kind, source,
target)` triples are each free of duplicates, and no conversion to a set
may erase a duplicate. Each singleton relation exists exactly once. A
duplicate, missing, extra, reversed or mismatched edge refuses
`occurrence_admission`, and a relation label cannot repair a different
identity preimage. `lineage_refs` contains only admitted occurrence-cause
predecessors and the component occurrences of an aggregate; support,
correction, timestamp, ordinal, adjacency and correlation edges never
enter occurrence lineage (P3, P5).

One occurrence has exactly one `application_of`, one `bound_to_subject`
and one `intends` relation. Every traversal application has exactly one
`applies_traversal`; every effect operation has exactly one
`operation_of_kind` and one `targets_subject`; every effect invocation has
exactly one `authorized_by`. One occurrence has zero or one
`invokes_effect`, and zero or one pre-observation and post-observation
relation of each declared observation kind. Every effect invocation has
zero or more `evidenced_by` relations. Every disposition other than
`no_effect` has exactly one `disposition_for`, and `no_effect` has none.
Every framework event has zero or one `event_for`. Every projection has
exactly one `projects_frontier`. Every claim-admission event has exactly
one `admits_claim` and exactly one `materializes_relation`. Identity,
causal, support, correction, component, frontier-membership and evidence
relations are finite and free of duplicates. `inverse_kind_ref_or_none`
is explicit; silence implies no inverse (P3, P4a).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-semantic-object-sorts` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-semantic-object-sorts` at rc.2:

```text
## Closed Semantic-Object Sorts

`Sigma_occurrence.Sort` contains exactly these core sort identities:

| Sort | Required `value` contract |
|---|---|
| `OccurrenceModelSubject` | `model_identity`, `model_sha256`, `profile_basis_ref` |
| `TraversalApplication` | `traversal_ref`, `functor_kind_ref`, `input_refs`, `application_contract_ref` |
| `Occurrence` | `application_ref`, `traversal_ref`, `functor_kind_ref`, `subject_binding_ref`, `intended_outcome_ref`, `lineage_refs`, `identity_dependency_refs` |
| `SubjectBinding` | `subject_ref`, `authority_ref`, `invalidation_ref`; no mutable content digest |
| `Observation` | `subject_binding_ref`, `observation_kind`, `observer_ref`, `evidence_ref`, `evidence_sha256`, `observation_coordinate_ref` |
| `IntendedOutcome` | `outcome_ref`, `outcome_contract_ref`, `comparison_basis_ref` |
| `OperationKind` | `operation_contract_ref`, `target_sort_ref`, `invalidation_ref` |
| `EffectOperation` | `operation_kind_ref`, `subject_binding_ref`, `effect_territory_ref`, `operation_contract_ref`, `invalidation_ref` |
| `OperationGrant` | `issuer_ref`, `subject_binding_ref`, `allowed_operation_kind_refs`, `allowed_effect_territory_ref`, `invalidation_ref` |
| `EffectInvocation` | `occurrence_ref`, `operation_ref`, `executor_ref`, `actor_ref`, `operation_grant_ref`, `effect_territory_ref`, `input_refs` |
| `EffectDisposition` | `invocation_ref_or_none`, `disposition`, `post_observation_ref_or_none`, `effect_evidence_refs`, `residual_ref_or_none` |
| `EffectEvidence` | `invocation_ref`, `evidence_kind`, `evidence_refs`, `evidence_sha256_refs`, `observation_limit_ref` |
| `RelationClaim` | `relation_kind_ref`, `source_ref`, `target_ref`, `relation_qualifiers`, `claimant_ref`, `claim_basis_ref`, `source_frontier_ref` |
| `FrameworkEvent` | `event_kind_ref`, `payload_ref`, `payload_sha256`, `scope_class`, `occurrence_ref_or_none`, `claim_ref_or_none`, `claim_judgment_ref_or_none`, `source_frontier_ref` |
| `EventFrontier` | `event_set_identity`, `member_event_refs`, `projection_basis_ref`, `precedence_law_ref` |
| `Projection` | `frontier_ref`, `projection_rule_ref`, `selected_relation_refs`, `boundary_refs`, `residual_refs` |
| `SemanticAdmissionCut` | `claim_ref`, `claim_judgment_ref`, `event_ref`, `event_judgment_ref`, `materialized_relation_ref`, `source_frontier_ref`, `successor_frontier_ref` |
| `EffectSubject` | `occurrence_ref`, `subject_binding_ref`, `pre_observation_ref`, `invocation_ref`, `operation_ref`, `operation_grant_ref`, `effect_territory_ref`, `currentness_invalidation_ref` |
| `TransitionSubject` | `occurrence_ref`, `subject_binding_ref`, `pre_observation_ref`, `post_observation_ref_or_none`, `intended_outcome_ref`, `effect_disposition_ref`, `effect_evidence_refs` |

Every row is a `SemanticObject` and therefore also carries exact `id`, `sort`,
`context`, `owner`, `scope`, and `basis`. The value contract is closed. An
unknown field or missing required field refuses structural admission.

`FrameworkEvent.value.occurrence_ref_or_none` is optional. An event whose
declared scope is independent of an occurrence is not assigned a fictional
occurrence to satisfy a total relation.

`claim_ref_or_none` and `claim_judgment_ref_or_none` are either both absent or
both exact. A claim-admission event requires both and a current
`source_frontier_ref`; another event kind refuses those fields unless its
compatible extension explicitly declares them.

The profile uses exact scoped identity refs, SHA-256 content digests, and
duplicate-free ordered identity-ref lists. `observation_kind` is one of
`pre_effect`, `post_effect`, or
`external_observation`. `EffectDisposition.value.disposition` is one of
`no_effect`, `completed_effect`, `partial_effect`, or `refused_effect`.
`scope_class` is one of `occurrence_scoped`, `subject_scoped`, or
`authority_scoped`. Another value requires a separately identified compatible
signature extension.
Every `_ref` resolves exactly once under AC-003. Every ref list is ordered by
the owning signature's declared order and rejects duplicates.

`TraversalApplication`, `OperationKind`, and `EffectOperation` are identity
records, not executors. An adopting Product declares its finite
`OperationKind` object population through its exact compatible signature and
mapping. The core profile declares the sort and closed record shape but no
consumer operation-kind instances. A model containing an `EffectOperation`
without an exact in-model `OperationKind` object or explicit compatible import
refuses.

### Finite Reference-Domain Table

This table is the complete specialization of
`RefDomain_Sigma_occurrence(record_kind, qualified_field)`. Source families use
the exact `O/E/C/L/X/V/T/J` populations. `O:S` means semantic-object sort `S`;
`AnyLocal` means the closed union `O union E union C union L union X union V
union T union J`; and `Sigma:K` means one exact member of the named closed
signature population. Empty cells mean no target in that class.

The basis codes are exact relations, not labels:

```text
B_model     = same M_occ,b and record basis
B_profile   = exact TraversalOccurrenceProfileBasis resolution
B_calculus  = exact imported AxiomaticCalculusBasis resolution
B_adopted   = exact Product-adoption basis relation named for that external kind
```

| Source family and qualified field | Card. | Local family | Local sort | External target kind | Basis |
|---|---:|---|---|---|---|
| `O:*.context` | 1 |  |  | `Context` | `B_adopted` |
| `O:*.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `O:*.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `O:*.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:*.sort` | 1 |  |  | `Sigma:Sort` | `B_profile` |
| `E/C/L/X/V/T/J.context` | 1 |  |  | `Context` | `B_adopted` |
| `E/C/L/X/V/T/J.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `E/C/L/X/V/T/J.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `E/C/L/X/V/T/J.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:OccurrenceModelSubject.value.model_identity` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `O:OccurrenceModelSubject.value.profile_basis_ref` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:TraversalApplication.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:TraversalApplication.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:TraversalApplication.value.input_refs` | 0..* | `AnyLocal` |  | `TraversalInput` | `B_model or B_adopted` |
| `O:TraversalApplication.value.application_contract_ref` | 1 |  |  | `ApplicationContract` | `B_adopted` |
| `O:Occurrence.value.application_ref` | 1 | `O` | `TraversalApplication` |  | `B_model` |
| `O:Occurrence.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:Occurrence.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:Occurrence.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Occurrence.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:Occurrence.value.lineage_refs` | 0..* | `O` | `Occurrence` |  | `B_model` |
| `O:Occurrence.value.identity_dependency_refs` | 0..* | `AnyLocal` |  |  | `B_model` |
| `O:SubjectBinding.value.subject_ref` | 1 |  |  | `MutableSubject` | `B_adopted` |
| `O:SubjectBinding.value.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:SubjectBinding.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:Observation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Observation.value.observer_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:Observation.value.evidence_ref` | 1 |  |  | `Evidence` | `B_adopted` |
| `O:Observation.value.observation_coordinate_ref` | 1 |  |  | `ObservationCoordinate` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_ref` | 1 |  |  | `Outcome` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_contract_ref` | 1 |  |  | `OutcomeContract` | `B_adopted` |
| `O:IntendedOutcome.value.comparison_basis_ref` | 1 |  |  | `ComparisonBasis` | `B_adopted` |
| `O:OperationKind.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:OperationKind.value.target_sort_ref` | 1 |  |  | `TargetSort` | `B_adopted` |
| `O:OperationKind.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectOperation.value.operation_kind_ref` | 1 | `O` | `OperationKind` |  | `B_model` |
| `O:EffectOperation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectOperation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectOperation.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:EffectOperation.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:OperationGrant.value.issuer_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:OperationGrant.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:OperationGrant.value.allowed_operation_kind_refs` | 1..* | `O` | `OperationKind` |  | `B_model` |
| `O:OperationGrant.value.allowed_effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:OperationGrant.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectInvocation.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectInvocation.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectInvocation.value.executor_ref` | 1 |  |  | `Executor` | `B_adopted` |
| `O:EffectInvocation.value.actor_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:EffectInvocation.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectInvocation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectInvocation.value.input_refs` | 0..* | `AnyLocal` |  | `EffectInput` | `B_model or B_adopted` |
| `O:EffectDisposition.value.invocation_ref_or_none` | 0..1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectDisposition.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:EffectDisposition.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `O:EffectDisposition.value.residual_ref_or_none` | 0..1 | `X` |  |  | `B_model` |
| `O:EffectEvidence.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectEvidence.value.evidence_refs` | 1..* |  |  | `Evidence` | `B_adopted` |
| `O:EffectEvidence.value.observation_limit_ref` | 1 |  |  | `ObservationLimit` | `B_adopted` |
| `O:RelationClaim.value.relation_kind_ref` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `O:RelationClaim.value.source_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.target_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.claimant_ref` | 1 |  |  | `Claimant` | `B_adopted` |
| `O:RelationClaim.value.claim_basis_ref` | 1 |  |  | `ClaimBasis` | `B_adopted` |
| `O:RelationClaim.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:FrameworkEvent.value.event_kind_ref` | 1 |  |  | `Sigma:EventKind_occurrence` | `B_profile` |
| `O:FrameworkEvent.value.payload_ref` | 1 | `AnyLocal` |  |  | `B_model` |
| `O:FrameworkEvent.value.occurrence_ref_or_none` | 0..1 | `O` | `Occurrence` |  | `B_model` |
| `O:FrameworkEvent.value.claim_ref_or_none` | 0..1 | `O` | `RelationClaim` |  | `B_model` |
| `O:FrameworkEvent.value.claim_judgment_ref_or_none` | 0..1 | `J` |  |  | `B_model` |
| `O:FrameworkEvent.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EventFrontier.value.event_set_identity` | 1 |  |  | `EventSetIdentity` | `B_model` |
| `O:EventFrontier.value.member_event_refs` | 0..* | `O` | `FrameworkEvent` |  | `B_model` |
| `O:EventFrontier.value.projection_basis_ref` | 1 |  |  | `ProjectionBasis` | `B_adopted` |
| `O:EventFrontier.value.precedence_law_ref` | 1 |  |  | `PrecedenceLaw` | `B_adopted` |
| `O:Projection.value.frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:Projection.value.projection_rule_ref` | 1 |  |  | `ProjectionRule` | `B_adopted` |
| `O:Projection.value.selected_relation_refs` | 0..* | `E` |  |  | `B_model` |
| `O:Projection.value.boundary_refs` | 0..* | `AnyLocal` |  | `ProjectionBoundary` | `B_model or B_adopted` |
| `O:Projection.value.residual_refs` | 0..* | `X` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_ref` | 1 | `O` | `RelationClaim` |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_ref` | 1 | `O` | `FrameworkEvent` |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.materialized_relation_ref` | 1 | `E` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:SemanticAdmissionCut.value.successor_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EffectSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:EffectSubject.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectSubject.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectSubject.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectSubject.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectSubject.value.currentness_invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:TransitionSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:TransitionSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:TransitionSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:TransitionSubject.value.effect_disposition_ref` | 1 | `O` | `EffectDisposition` |  | `B_model` |
| `O:TransitionSubject.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `E:<each RelationKind>.source/target` | 1 | exact family from relation table | exact sort from relation table | declared endpoint where table permits | `B_model or B_adopted` |
| `E:*.kind` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `E:*.qualifiers.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `E:*.qualifiers.evidence_refs` | 0..* |  |  | `Evidence` | `B_adopted` |
| `E:*.qualifiers.provenance_refs` | 0..* |  |  | `Provenance` | `B_adopted` |
| `E:*.qualifiers.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `E:*.qualifiers.inverse_kind_ref_or_none` | 0..1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `C:*.kind` | 1 |  |  | `Sigma:ConstraintKind` | `B_profile` |
| `C:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `C:*.predicate` | 1 |  |  | `PredicateContract` | `B_adopted` |
| `C:*.judgment_kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `C:*.latitude_ref` | 0..1 | `L` |  |  | `B_model` |
| `L:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `L:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `X:*.subject` | 1 | `AnyLocal` |  | `ResidualSubject` | `B_model or B_adopted` |
| `X:*.kind` | 1 |  |  | `Sigma:ResidualKind` | `B_profile` |
| `X:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `X:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `V:*.domain/codomain` | 1 |  |  | `TypeDomain` | `B_adopted` |
| `V:*.preconditions/postconditions` | 0..* | `C` |  |  | `B_model` |
| `V:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `V:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `V:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.traversal` | 1 | `V` |  |  | `B_model` |
| `T:*.domain_model/codomain_model` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `T:*.operation_authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `T:*.preconditions` | 0..* | `C` |  |  | `B_model` |
| `T:*.preservation_relation` | 1 | `E` |  |  | `B_model` |
| `T:*.preserved/introduced/removed` | 0..* | `AnyLocal` |  | `ModelMemberIdentity` | `B_model or B_adopted` |
| `T:*.residuals` | 0..* | `X` |  |  | `B_model` |
| `T:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `T:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `T:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `J:*.kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `J:*.subject` | 1 | `AnyLocal` |  | `JudgmentSubject` | `B_model or B_adopted` |
| `J:*.evaluator` | 1 |  |  | `Evaluator` | `B_adopted` |
| `J:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `J:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `J:*.decided_at` | 1 |  |  | `DecisionCoordinate` | `B_adopted` |

The inherited transformation's external-resolution coordinates are closed by
the following finite expansion rather than hidden inside the three local-delta
rows above:

```text
D_ext = {
  external_preserved,
  external_introduced,
  external_removed
}

W_ext = {
  external_resolution,
  domain_resolution,
  codomain_resolution
}

Q_ext = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

for every d in D_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(T, d[].q) = ResolutionRefDomain(q)

for every w in W_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(
    T,
    external_resolution_witnesses[].w.q
  ) = ResolutionRefDomain(q)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].domain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].codomain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].evidence
) = (1, empty, empty, {Evidence}, B_adopted)
```

`ResolutionRefDomain` is exact and dependent only where the resolution tuple
itself supplies the target coordinate:

```text
ResolutionRefDomain(external_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(reference_domain)
  = (1, empty, empty, {Sigma:ReferenceDomain}, B_profile)

ResolutionRefDomain(external_target_kind)
  = (1, empty, empty, {Sigma:ExternalTargetKind}, B_profile or B_adopted)

ResolutionRefDomain(resolved_target_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(basis_relation)
  = (1, empty, empty, {Sigma:BasisRelation}, B_profile)

ResolutionRefDomain(resolution_basis)
  = (1, empty, empty,
     {TraversalOccurrenceProfileBasis,
      AxiomaticCalculusBasis,
      ProductAdoptionBasis},
     B_profile or B_calculus or B_adopted)

ResolutionRefDomain(evidence_identity)
  = (1, empty, empty, {Evidence}, B_adopted)
```

Each member of `D_ext` is a duplicate-free finite `Resolution_M` value list.
`external_resolution_witnesses` is a duplicate-free finite inherited
`ExternalResolutionPreservationWitness` value list. Every coordinate has
exactly `Q_ext`; every witness has exactly `external_resolution`,
`domain_model`, `codomain_model`, `domain_resolution`,
`codomain_resolution`, `decision`, and `evidence`; and `decision` is exactly
`equal`. A missing or extra nested field, unresolved nested identity,
coordinate/basis mismatch, duplicate coordinate, or witness outside the exact
preserved population refuses model validation.

`id` fields own identities rather than reference them. Digests, closed enum
values, predicates, qualifiers other than the listed refs, uncertainty,
consequence, variation content, and refusal values are closed non-reference
content. A compatible extension changes this table by minting a new signature;
it cannot reinterpret an existing row. Every list is duplicate-free before
set comparison. A missing row, target outside its row, wrong local population
or sort, unresolved external target, cardinality violation, or basis-relation
mismatch refuses model validation.
```

Successor, `TRAVERSAL_OCCURRENCE.md#closed-semantic-object-sorts`:

```text
## Closed semantic-object sorts

`Sigma_occurrence.Sort` contains exactly these core sort identities (P3):

| Sort | Required `value` contract |
|---|---|
| `OccurrenceModelSubject` | `model_identity`, `model_sha256`, `profile_basis_ref` |
| `TraversalApplication` | `traversal_ref`, `functor_kind_ref`, `input_refs`, `application_contract_ref` |
| `Occurrence` | `application_ref`, `traversal_ref`, `functor_kind_ref`, `subject_binding_ref`, `intended_outcome_ref`, `lineage_refs`, `identity_dependency_refs` |
| `SubjectBinding` | `subject_ref`, `authority_ref`, `invalidation_ref`; no mutable content digest |
| `Observation` | `subject_binding_ref`, `observation_kind`, `observer_ref`, `evidence_ref`, `evidence_sha256`, `observation_coordinate_ref` |
| `IntendedOutcome` | `outcome_ref`, `outcome_contract_ref`, `comparison_basis_ref` |
| `OperationKind` | `operation_contract_ref`, `target_sort_ref`, `invalidation_ref` |
| `EffectOperation` | `operation_kind_ref`, `subject_binding_ref`, `effect_territory_ref`, `operation_contract_ref`, `invalidation_ref` |
| `OperationGrant` | `issuer_ref`, `subject_binding_ref`, `allowed_operation_kind_refs`, `allowed_effect_territory_ref`, `invalidation_ref` |
| `EffectInvocation` | `occurrence_ref`, `operation_ref`, `executor_ref`, `actor_ref`, `operation_grant_ref`, `effect_territory_ref`, `input_refs` |
| `EffectDisposition` | `invocation_ref_or_none`, `disposition`, `post_observation_ref_or_none`, `effect_evidence_refs`, `residual_ref_or_none` |
| `EffectEvidence` | `invocation_ref`, `evidence_kind`, `evidence_refs`, `evidence_sha256_refs`, `observation_limit_ref` |
| `RelationClaim` | `relation_kind_ref`, `source_ref`, `target_ref`, `relation_qualifiers`, `claimant_ref`, `claim_basis_ref`, `source_frontier_ref` |
| `FrameworkEvent` | `event_kind_ref`, `payload_ref`, `payload_sha256`, `scope_class`, `occurrence_ref_or_none`, `claim_ref_or_none`, `claim_judgment_ref_or_none`, `source_frontier_ref` |
| `EventFrontier` | `event_set_identity`, `member_event_refs`, `projection_basis_ref`, `precedence_law_ref` |
| `Projection` | `frontier_ref`, `projection_rule_ref`, `selected_relation_refs`, `boundary_refs`, `residual_refs` |
| `SemanticAdmissionCut` | `claim_ref`, `claim_judgment_ref`, `event_ref`, `event_judgment_ref`, `materialized_relation_ref`, `source_frontier_ref`, `successor_frontier_ref` |
| `EffectSubject` | `occurrence_ref`, `subject_binding_ref`, `pre_observation_ref`, `invocation_ref`, `operation_ref`, `operation_grant_ref`, `effect_territory_ref`, `currentness_invalidation_ref` |
| `TransitionSubject` | `occurrence_ref`, `subject_binding_ref`, `pre_observation_ref`, `post_observation_ref_or_none`, `intended_outcome_ref`, `effect_disposition_ref`, `effect_evidence_refs` |

Every row is a `SemanticObject` and so also carries exact `id`, `sort`,
`context`, `owner`, `scope` and `basis`. The value contract is closed: an
unknown field or a missing required field refuses structural admission
(P3, P5).

`FrameworkEvent.value.occurrence_ref_or_none` is optional. An event whose
declared scope is independent of any occurrence is not assigned a
fictional occurrence to satisfy a total relation (P3, P6).

`claim_ref_or_none` and `claim_judgment_ref_or_none` are both absent or
both exact. A claim-admission event requires both, and a current
`source_frontier_ref`; any other event kind refuses those fields unless
its compatible extension declares them explicitly (P3, P5).

The profile uses exact scoped identity refs, SHA-256 content digests and
ordered identity-ref lists without duplicates. `observation_kind` is one
of `pre_effect`, `post_effect` or `external_observation`.
`EffectDisposition.value.disposition` is one of `no_effect`,
`completed_effect`, `partial_effect` or `refused_effect`. `scope_class` is
one of `occurrence_scoped`, `subject_scoped` or `authority_scoped`. Any
other value requires a separately identified compatible signature
extension. Every `_ref` resolves exactly once under AC-003, and every ref
list is ordered by the owning signature's declared order and rejects
duplicates (P3, P5).

`TraversalApplication`, `OperationKind` and `EffectOperation` are identity
records, not executors. An adopting Product declares its finite
`OperationKind` object population through its exact compatible signature
and mapping; the core profile declares the sort and its closed record
shape and no consumer operation-kind instances. A model that contains an
`EffectOperation` without an exact in-model `OperationKind` object or an
explicit compatible import refuses (P3, P6).

### Finite reference-domain table

This table is the complete specialisation of
`RefDomain_Sigma_occurrence(record_kind, qualified_field)`. Source families
use the exact `O/E/C/L/X/V/T/J` populations. `O:S` means semantic-object
sort `S`; `AnyLocal` means the closed union `O union E union C union L
union X union V union T union J`; `Sigma:K` means one exact member of the
named closed signature population; an empty cell means no target in that
class. `Sigma:ReferenceDomain`, `Sigma:ExternalTargetKind` and
`Sigma:BasisRelation` are populations of this profile's signature, named
here and not by the calculus (P3).

The basis codes are exact relations, not labels (P3):

```text
B_model     = same M_occ,b and record basis
B_profile   = exact TraversalOccurrenceProfileBasis resolution
B_calculus  = exact imported AxiomaticCalculusBasis resolution
B_adopted   = exact Product-adoption basis relation named for that external kind
```

| Source family and qualified field | Card. | Local family | Local sort | External target kind | Basis |
|---|---:|---|---|---|---|
| `O:*.context` | 1 |  |  | `Context` | `B_adopted` |
| `O:*.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `O:*.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `O:*.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:*.sort` | 1 |  |  | `Sigma:Sort` | `B_profile` |
| `E/C/L/X/V/T/J.context` | 1 |  |  | `Context` | `B_adopted` |
| `E/C/L/X/V/T/J.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `E/C/L/X/V/T/J.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `E/C/L/X/V/T/J.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:OccurrenceModelSubject.value.model_identity` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `O:OccurrenceModelSubject.value.profile_basis_ref` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:TraversalApplication.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:TraversalApplication.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:TraversalApplication.value.input_refs` | 0..* | `AnyLocal` |  | `TraversalInput` | `B_model or B_adopted` |
| `O:TraversalApplication.value.application_contract_ref` | 1 |  |  | `ApplicationContract` | `B_adopted` |
| `O:Occurrence.value.application_ref` | 1 | `O` | `TraversalApplication` |  | `B_model` |
| `O:Occurrence.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:Occurrence.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:Occurrence.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Occurrence.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:Occurrence.value.lineage_refs` | 0..* | `O` | `Occurrence` |  | `B_model` |
| `O:Occurrence.value.identity_dependency_refs` | 0..* | `AnyLocal` |  |  | `B_model` |
| `O:SubjectBinding.value.subject_ref` | 1 |  |  | `MutableSubject` | `B_adopted` |
| `O:SubjectBinding.value.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:SubjectBinding.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:Observation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Observation.value.observer_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:Observation.value.evidence_ref` | 1 |  |  | `Evidence` | `B_adopted` |
| `O:Observation.value.observation_coordinate_ref` | 1 |  |  | `ObservationCoordinate` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_ref` | 1 |  |  | `Outcome` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_contract_ref` | 1 |  |  | `OutcomeContract` | `B_adopted` |
| `O:IntendedOutcome.value.comparison_basis_ref` | 1 |  |  | `ComparisonBasis` | `B_adopted` |
| `O:OperationKind.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:OperationKind.value.target_sort_ref` | 1 |  |  | `TargetSort` | `B_adopted` |
| `O:OperationKind.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectOperation.value.operation_kind_ref` | 1 | `O` | `OperationKind` |  | `B_model` |
| `O:EffectOperation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectOperation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectOperation.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:EffectOperation.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:OperationGrant.value.issuer_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:OperationGrant.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:OperationGrant.value.allowed_operation_kind_refs` | 1..* | `O` | `OperationKind` |  | `B_model` |
| `O:OperationGrant.value.allowed_effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:OperationGrant.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectInvocation.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectInvocation.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectInvocation.value.executor_ref` | 1 |  |  | `Executor` | `B_adopted` |
| `O:EffectInvocation.value.actor_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:EffectInvocation.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectInvocation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectInvocation.value.input_refs` | 0..* | `AnyLocal` |  | `EffectInput` | `B_model or B_adopted` |
| `O:EffectDisposition.value.invocation_ref_or_none` | 0..1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectDisposition.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:EffectDisposition.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `O:EffectDisposition.value.residual_ref_or_none` | 0..1 | `X` |  |  | `B_model` |
| `O:EffectEvidence.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectEvidence.value.evidence_refs` | 1..* |  |  | `Evidence` | `B_adopted` |
| `O:EffectEvidence.value.observation_limit_ref` | 1 |  |  | `ObservationLimit` | `B_adopted` |
| `O:RelationClaim.value.relation_kind_ref` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `O:RelationClaim.value.source_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.target_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.claimant_ref` | 1 |  |  | `Claimant` | `B_adopted` |
| `O:RelationClaim.value.claim_basis_ref` | 1 |  |  | `ClaimBasis` | `B_adopted` |
| `O:RelationClaim.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:FrameworkEvent.value.event_kind_ref` | 1 |  |  | `Sigma:EventKind_occurrence` | `B_profile` |
| `O:FrameworkEvent.value.payload_ref` | 1 | `AnyLocal` |  |  | `B_model` |
| `O:FrameworkEvent.value.occurrence_ref_or_none` | 0..1 | `O` | `Occurrence` |  | `B_model` |
| `O:FrameworkEvent.value.claim_ref_or_none` | 0..1 | `O` | `RelationClaim` |  | `B_model` |
| `O:FrameworkEvent.value.claim_judgment_ref_or_none` | 0..1 | `J` |  |  | `B_model` |
| `O:FrameworkEvent.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EventFrontier.value.event_set_identity` | 1 |  |  | `EventSetIdentity` | `B_model` |
| `O:EventFrontier.value.member_event_refs` | 0..* | `O` | `FrameworkEvent` |  | `B_model` |
| `O:EventFrontier.value.projection_basis_ref` | 1 |  |  | `ProjectionBasis` | `B_adopted` |
| `O:EventFrontier.value.precedence_law_ref` | 1 |  |  | `PrecedenceLaw` | `B_adopted` |
| `O:Projection.value.frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:Projection.value.projection_rule_ref` | 1 |  |  | `ProjectionRule` | `B_adopted` |
| `O:Projection.value.selected_relation_refs` | 0..* | `E` |  |  | `B_model` |
| `O:Projection.value.boundary_refs` | 0..* | `AnyLocal` |  | `ProjectionBoundary` | `B_model or B_adopted` |
| `O:Projection.value.residual_refs` | 0..* | `X` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_ref` | 1 | `O` | `RelationClaim` |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_ref` | 1 | `O` | `FrameworkEvent` |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.materialized_relation_ref` | 1 | `E` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:SemanticAdmissionCut.value.successor_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EffectSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:EffectSubject.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectSubject.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectSubject.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectSubject.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectSubject.value.currentness_invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:TransitionSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:TransitionSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:TransitionSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:TransitionSubject.value.effect_disposition_ref` | 1 | `O` | `EffectDisposition` |  | `B_model` |
| `O:TransitionSubject.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `E:<each RelationKind>.source/target` | 1 | exact family from relation table | exact sort from relation table | declared endpoint where table permits | `B_model or B_adopted` |
| `E:*.kind` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `E:*.qualifiers.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `E:*.qualifiers.evidence_refs` | 0..* |  |  | `Evidence` | `B_adopted` |
| `E:*.qualifiers.provenance_refs` | 0..* |  |  | `Provenance` | `B_adopted` |
| `E:*.qualifiers.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `E:*.qualifiers.inverse_kind_ref_or_none` | 0..1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `C:*.kind` | 1 |  |  | `Sigma:ConstraintKind` | `B_profile` |
| `C:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `C:*.predicate` | 1 |  |  | `PredicateContract` | `B_adopted` |
| `C:*.judgment_kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `C:*.latitude_ref` | 0..1 | `L` |  |  | `B_model` |
| `L:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `L:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `X:*.subject` | 1 | `AnyLocal` |  | `ResidualSubject` | `B_model or B_adopted` |
| `X:*.kind` | 1 |  |  | `Sigma:ResidualKind` | `B_profile` |
| `X:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `X:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `V:*.domain/codomain` | 1 |  |  | `TypeDomain` | `B_adopted` |
| `V:*.preconditions/postconditions` | 0..* | `C` |  |  | `B_model` |
| `V:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `V:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `V:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.traversal` | 1 | `V` |  |  | `B_model` |
| `T:*.domain_model/codomain_model` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `T:*.operation_authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `T:*.preconditions` | 0..* | `C` |  |  | `B_model` |
| `T:*.preservation_relation` | 1 | `E` |  |  | `B_model` |
| `T:*.preserved/introduced/removed` | 0..* | `AnyLocal` |  | `ModelMemberIdentity` | `B_model or B_adopted` |
| `T:*.residuals` | 0..* | `X` |  |  | `B_model` |
| `T:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `T:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `T:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `J:*.kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `J:*.subject` | 1 | `AnyLocal` |  | `JudgmentSubject` | `B_model or B_adopted` |
| `J:*.evaluator` | 1 |  |  | `Evaluator` | `B_adopted` |
| `J:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `J:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `J:*.decided_at` | 1 |  |  | `DecisionCoordinate` | `B_adopted` |

The external-resolution coordinates of the inherited transformation are
closed by this finite expansion and are not hidden inside the three
local-delta rows above (P3, P4b):

```text
D_ext = {
  external_preserved,
  external_introduced,
  external_removed
}

W_ext = {
  external_resolution,
  domain_resolution,
  codomain_resolution
}

Q_ext = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

for every d in D_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(T, d[].q) = ResolutionRefDomain(q)

for every w in W_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(
    T,
    external_resolution_witnesses[].w.q
  ) = ResolutionRefDomain(q)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].domain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].codomain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].evidence
) = (1, empty, empty, {Evidence}, B_adopted)
```

`ResolutionRefDomain` is exact, and it is dependent only where the
resolution tuple itself supplies the target coordinate (P3):

```text
ResolutionRefDomain(external_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(reference_domain)
  = (1, empty, empty, {Sigma:ReferenceDomain}, B_profile)

ResolutionRefDomain(external_target_kind)
  = (1, empty, empty, {Sigma:ExternalTargetKind}, B_profile or B_adopted)

ResolutionRefDomain(resolved_target_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(basis_relation)
  = (1, empty, empty, {Sigma:BasisRelation}, B_profile)

ResolutionRefDomain(resolution_basis)
  = (1, empty, empty,
     {TraversalOccurrenceProfileBasis,
      AxiomaticCalculusBasis,
      ProductAdoptionBasis},
     B_profile or B_calculus or B_adopted)

ResolutionRefDomain(evidence_identity)
  = (1, empty, empty, {Evidence}, B_adopted)
```

Each member of `D_ext` is a finite `Resolution_M` value list without
duplicates. `external_resolution_witnesses` is a finite inherited
`ExternalResolutionPreservationWitness` value list without duplicates.
Every coordinate has exactly `Q_ext`; every witness has exactly
`external_resolution`, `domain_model`, `codomain_model`,
`domain_resolution`, `codomain_resolution`, `decision` and `evidence`;
and `decision` is exactly `equal`. A missing or extra nested field, an
unresolved nested identity, a coordinate and basis mismatch, a duplicate
coordinate, or a witness outside the exact preserved population refuses
model validation (P3, P5).

`id` fields own identities rather than reference them. Digests, closed
enum values, predicates, qualifiers other than the listed refs,
uncertainty, consequence, variation content and refusal values are closed
non-reference content. A compatible extension changes this table by
minting a new signature; it cannot reinterpret an existing row. Every list
is free of duplicates before any set comparison. A missing row, a target
outside its row, a wrong local population or sort, an unresolved external
target, a cardinality violation or a basis-relation mismatch refuses model
validation (P3, P5).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#conformance-obligations` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#conformance-obligations` at rc.2:

```text
## Conformance Obligations

Review and qualification cover at least:

1. instantiation under one exact `a_c` basis, the exact eight-member
   `RecordKind_ac` population function, and closed reference domains without
   inherited-field shadowing;
2. exact inherited record families, direct coordinates, and disjoint local and
   external identity populations;
3. complete occurrence seeds, exact congruence with every mirroring relation,
   and future-result and future-event refusal;
4. first-event admission without a fictional predecessor;
5. distinct candidate, judgment, event, materialized relation, cut, and cut-
   judgment identities with unchanged-subject digest binding;
6. idempotent or refused duplicate admission;
7. cycles in each identity or causal subgraph;
8. lawful opposing support and correction edges in wider typed lineage;
9. exact closed event-kind population, payload, digest, scope, and binding law,
   including scope-independent events with no fabricated `event_for` relation;
10. functor kind, traversal, operation kind, operation instance, executor,
    actor, grant, invocation, target, and territory separation;
11. missing, stale, mismatched, and out-of-territory operation grants;
12. no-effect, complete-effect, partial-effect, and refused-effect cases;
13. preservation of the external mutable subject as reality carrier;
14. fresh occurrence identity on traversal reapplication;
15. component and aggregate occurrence identities for retained composite
    applications;
16. stale pre-effect observation and grant-currentness refusal;
17. incomplete semantic-admission batch refusal, including missing or
    non-admitted cut judgment and unequal claim/event/cut source frontiers;
18. frontier completeness, staleness, and correction selection;
19. timestamp, ordinal, adjacency, containment, and correlation non-causation;
20. Product adoption absence and incomplete-mapping refusal; and
21. profile-basis reconstruction from exact JCS, kinds, schemas, immutable
    URIs, digests, calculus address, and unique publication membership.

Representative examples or checkers establish only the claims they actually
evaluate. They do not become an occurrence engine or semantic authority.
```

Successor, `TRAVERSAL_OCCURRENCE.md#conformance-obligations`:

```text
## Conformance obligations

Review and qualification cover at least (P6, P5):

1. instantiation under one exact `a_c` basis, the exact eight-member
   `RecordKind_ac` population function, and closed reference domains
   without shadowing an inherited field;
2. exact inherited record families, direct coordinates, and disjoint
   local and external identity populations;
3. complete occurrence seeds, exact congruence with every mirroring
   relation, and refusal of future results and future events;
4. first-event admission without a fictional predecessor;
5. distinct candidate, judgment, event, materialised relation, cut and
   cut-judgment identities with the unchanged subject's digest bound;
6. idempotent or refused duplicate admission;
7. cycles in each identity or causal subgraph;
8. lawful opposing support and correction edges in wider typed lineage;
9. the exact closed event-kind population, payload, digest, scope and
   binding law, including scope-independent events with no fabricated
   `event_for` relation;
10. separation of functor kind, traversal, operation kind, operation
    instance, executor, actor, grant, invocation, target and territory;
11. missing, stale, mismatched and out-of-territory operation grants;
12. no-effect, complete-effect, partial-effect and refused-effect cases;
13. preservation of the external mutable subject as the reality carrier;
14. fresh occurrence identity on traversal reapplication;
15. component and aggregate occurrence identities for retained composite
    applications;
16. refusal on a stale pre-effect observation and on grant currentness;
17. refusal of an incomplete semantic-admission batch, including a
    missing or non-admitted cut judgment and unequal claim, event and cut
    source frontiers;
18. frontier completeness, staleness and correction selection;
19. non-causation by timestamp, ordinal, adjacency, containment and
    correlation;
20. absent Product adoption and refusal of an incomplete mapping; and
21. profile-basis reconstruction from exact JCS, kinds, schemas,
    immutable URIs, digests, the calculus address and unique publication
    membership.

Representative examples or checkers establish only the claims they
actually evaluate. They do not become an occurrence engine or a semantic
authority (P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#event-frontier-and-projection` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#event-frontier-and-projection` at rc.2:

```text
## Event Frontier And Projection

An `EventFrontier` binds the complete event member set evaluated, its exact
basis, and the declared precedence law. A projection judgment points to one
unchanged `Projection` identity and digest; that projection binds exactly one
unchanged frontier.

For profile basis `b`, scope `s`, and precedence law `p`, there is one empty
frontier `F_0(b,s,p)`. Admitting event `e_k_plus_1` constructs a successor whose
member set is exactly `members(F_k) union {e_k_plus_1}`. Frontier identity binds
the profile basis, scope, precedence law, sorted event identities, and event
content digests. Projection identity binds the exact frontier, projection
rule, selected relation ids, boundary ids, and residual ids.

New events create a new frontier. A prior projection does not silently advance.
Latest-only summaries do not prove frontier completeness. Competing
corrections, unresolved scope, missing causal inputs, or a stale basis remain
residuals or stops according to the selected projection law.

### OP-007 Scope Conservation

Every event carries its declared scope class. `event_for` is present only when
the scope law names one exact occurrence. Subject-wide, publication-wide, or
otherwise occurrence-independent facts remain independent.
```

Successor, `TRAVERSAL_OCCURRENCE.md#event-frontier-and-projection`:

```text
## Event frontier and projection

An `EventFrontier` binds the complete member set of events evaluated, its
exact basis and its declared precedence law. A projection judgment points
to one unchanged `Projection` identity and digest, and that projection
binds exactly one unchanged frontier (P3).

For profile basis `b`, scope `s` and precedence law `p` there is one empty
frontier `F_0(b,s,p)`. Admitting event `e_k_plus_1` constructs a successor
whose member set is exactly `members(F_k) union {e_k_plus_1}`. Frontier
identity binds the profile basis, scope, precedence law, sorted event
identities and event content digests. Projection identity binds the exact
frontier, the projection rule, and the selected relation, boundary and
residual ids (P3, P4b).

New events create a new frontier, and a prior projection does not silently
advance. Latest-only summaries do not prove frontier completeness.
Competing corrections, unresolved scope, missing causal inputs or a stale
basis remain residuals or stops according to the selected projection law
(P3, P5).

### OP-007 Scope conservation

Every event carries its declared scope class. `event_for` is present only
when the scope law names one exact occurrence. Facts that are
subject-wide, publication-wide or otherwise independent of any occurrence
stay independent (P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#exact-profile-identity` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#exact-profile-identity` at rc.2:

```text
## Exact Profile Identity

The stable concept identity does not identify one immutable profile edition.
After publication bytes exist, the signature preimage is issued as:

### Closed Profile Signature

```text
TraversalOccurrenceSignature = {
  kind: "stdo.traversal-occurrence-signature",
  schema_version: 1,
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  calculus_signature_schema_clause_ref:
    absolute semantic address of the Core Signature clause inside that basis,
  occurrence_signature_clause_refs:
    sorted non-empty absolute semantic-address URI[],
  profile_member_sha256: "sha256:" + 64 lowercase hexadecimal characters
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes. Its identity is:

```text
sha256(JCS(TraversalOccurrenceSignature))
```

`calculus_signature_schema_clause_ref` resolves the exact inherited signature
schema and record law. `occurrence_signature_clause_refs` resolves exactly
these fragments against the publication member URI:

```text
#authority-and-adoption
#candidate-judgment-event-and-relation-separation
#causality-and-typed-lineage
#closed-constraint-judgment-residual-and-stop-kinds
#closed-event-kind-population
#closed-relation-families
#closed-semantic-object-sorts
#event-frontier-and-projection
#mutable-subject-effect-relation
#occurrence-identity
```

Together they define this profile's closed sorts, fields, value domains,
relations, constraints, judgments, residuals, stops, and exact functor-kind
refs. The list is duplicate-free and sorted by ascending unsigned UTF-16 code
units. `profile_member_sha256` equals the publication member digest. This gives
`occurrence_signature_sha256` one reconstructable preimage rather than an
implementation-defined serialization.

Every clause ref is an absolute URI whose base is the exact publication
`member_uri`; only its fragment differs. The calculus clause ref is an absolute
URI inside the exact calculus publication basis. Relative paths, mutable source
URIs, missing fragments, duplicate refs, or a ref outside those two exact
publication members refuse the signature.

The exact profile basis is then issued as:

```text
TraversalOccurrenceProfileBasis = {
  kind: "stdo.traversal-occurrence-profile-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:traversal-occurrence-profile",
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  occurrence_signature: TraversalOccurrenceSignature,
  occurrence_signature_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  publication_basis: {
    release_uri: absolute immutable release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

`occurrence_signature_sha256` equals the digest of the embedded canonical
signature. The basis record also uses RFC 8785 JSON Canonicalization Scheme
bytes. Duplicate object names are rejected before canonicalization. Its
identity is:

```text
urn:stdo:traversal-occurrence-profile-basis:sha256:
  + sha256(JCS(TraversalOccurrenceProfileBasis))
```

The imported calculus basis resolves as exact RFC 8785 bytes of an
`AxiomaticCalculusBasis` record with the required kind, schema, concept,
derivation basis, and publication basis. Its calculated identity equals both
`calculus_basis_identity` fields. Its publication manifest digest resolves the
exact manifest bytes; that manifest contains the calculus member path and
digest once; the resolved calculus member bytes have that digest; and
`calculus_signature_schema_clause_ref` is that exact member URI plus
`#core-signature`. Its distinct predecessor manifest resolves every sorted,
duplicate-free `principle_ref` inside the declared predecessor release. The
principle-ref population is exactly the absolute predecessor-release expansion
of every derivation address declared by the resolved calculus member, neither a
selected subset nor an independently invented list. For the calculus edition
bound by this profile publication candidate, that population has fourteen
members. Each referenced predecessor member resolves as exact bytes whose
digest occurs once in the predecessor manifest, and each fragment resolves one
heading in those bytes under the publication's semantic-address rule. A string
with the right shape, an unresolved basis record, a mismatched manifest or
member, a missing or extra principle ref, an invented or absent fragment, an
unbound predecessor byte sequence, or a same-carrier derivation refuses.

The profile publication member resolves by the same manifest/member rule. A
mutable source path, strategy post, implementation, or consumer mapping cannot
substitute for either imported basis or publication identity.

`publication_basis.release_uri` is one absolute immutable
`stdo://releases/v<version>-rc.<positive-ordinal>/` URI.
`publication_basis.member_uri` is exactly that URI plus
`standards/TRAVERSAL_OCCURRENCE_PROFILE.md`. The installed release manifest
named by `manifest_sha256` contains exactly one standards member with that path
and `member_sha256`; the same digest appears in the embedded signature.
Kind and schema-version values are exact. Every digest uses lowercase
`sha256:<64-hex>`. The signature and basis preimages are their exact RFC 8785
JCS values; a newline, alternate object order, duplicate name, non-I-JSON
value, or implementation-specific serialization cannot acquire the declared
identity.

Any change to the calculus basis, signature refs, closed signature, or profile
member bytes mints a new profile basis. Supersession is an external Product and
release judgment; an earlier basis never silently advances.
```

Successor, `TRAVERSAL_OCCURRENCE.md#exact-profile-identity`:

```text
## Exact profile identity

The stable concept identity does not identify one immutable profile
edition. Once publication bytes exist, the signature preimage is issued as
below (P3, P6).

### Closed profile signature

```text
TraversalOccurrenceSignature = {
  kind: "stdo.traversal-occurrence-signature",
  schema_version: 1,
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  calculus_signature_schema_clause_ref:
    absolute semantic address of the Core Signature clause inside that basis,
  occurrence_signature_clause_refs:
    sorted non-empty absolute semantic-address URI[],
  profile_member_sha256: "sha256:" + 64 lowercase hexadecimal characters
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes, and its
identity is (P3):

```text
sha256(JCS(TraversalOccurrenceSignature))
```

`calculus_signature_schema_clause_ref` resolves the exact inherited
signature schema and record law. `occurrence_signature_clause_refs`
resolves exactly these fragments against the publication member URI, each
a heading of this member (P3):

```text
#authority-and-adoption
#candidate-judgment-event-and-relation-separation
#causality-and-typed-lineage
#closed-constraint-judgment-residual-and-stop-kinds
#closed-event-kind-population
#closed-relation-families
#closed-semantic-object-sorts
#event-frontier-and-projection
#mutable-subject-effect-relation
#occurrence-identity
```

Together they define this profile's closed sorts, fields, value domains,
relations, constraints, judgments, residuals, stops and exact functor-kind
refs. The list is free of duplicates and sorted by ascending unsigned
UTF-16 code units. `profile_member_sha256` equals the publication member
digest. `occurrence_signature_sha256` thus has one reconstructable
preimage and no implementation-defined serialisation (P3).

Every clause ref is an absolute URI whose base is the exact publication
`member_uri`; only its fragment differs. The calculus clause ref is an
absolute URI inside the exact calculus publication basis. Relative paths,
mutable source URIs, missing fragments, duplicate refs or a ref outside
those two exact publication members refuse the signature (P3, P5).

The exact profile basis is then issued as (P3):

```text
TraversalOccurrenceProfileBasis = {
  kind: "stdo.traversal-occurrence-profile-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:traversal-occurrence-profile",
  calculus_basis_identity: exact AxiomaticCalculusBasis identity,
  occurrence_signature: TraversalOccurrenceSignature,
  occurrence_signature_sha256: "sha256:" + 64 lowercase hexadecimal characters,
  publication_basis: {
    release_uri: absolute immutable release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

`occurrence_signature_sha256` equals the digest of the embedded canonical
signature. The basis record also uses RFC 8785 JSON Canonicalization
Scheme bytes, with duplicate object names rejected before
canonicalisation. Its identity is (P3):

```text
urn:stdo:traversal-occurrence-profile-basis:sha256:
  + sha256(JCS(TraversalOccurrenceProfileBasis))
```

The imported calculus basis resolves as the exact RFC 8785 bytes of an
`AxiomaticCalculusBasis` record with the required kind, schema, concept,
derivation basis and publication basis. Its calculated identity equals
both `calculus_basis_identity` fields. Its publication manifest digest
resolves the exact manifest bytes; that manifest contains the calculus
member path and digest once; the resolved calculus member bytes have that
digest; and `calculus_signature_schema_clause_ref` is that exact member
URI plus the fragment of the calculus signature clause, `#2-signature` in
this corpus's AXIOMATIC_CALCULUS. Its distinct predecessor manifest
resolves every sorted principle ref, without duplicates, inside the
declared predecessor release. The principle-ref population is exactly the
absolute predecessor-release expansion of every derivation address that
the resolved calculus member declares: neither a selected subset nor an
independently invented list, and its size is whatever that member's
derivation account declares
([AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity)). Each
referenced predecessor member resolves as exact bytes whose digest occurs
once in the predecessor manifest, and each fragment resolves one heading
in those bytes under the publication's semantic-address rule. A string of
the right shape, an unresolved basis record, a mismatched manifest or
member, a missing or extra principle ref, an invented or absent fragment,
an unbound predecessor byte sequence, or a derivation from the same
carrier refuses (P3, P6, P5).

The profile publication member resolves by the same manifest and member
rule. A mutable source path, a strategy post, an implementation or a
consumer mapping cannot stand in for either imported basis or for the
publication identity (P3, P6).

`publication_basis.release_uri` is one absolute immutable
`stdo://releases/v<version>-rc.<positive-ordinal>/` URI.
`publication_basis.member_uri` is exactly that URI plus
`standards/TRAVERSAL_OCCURRENCE.md`. The installed release manifest named
by `manifest_sha256` contains exactly one standards member with that path
and `member_sha256`, and the same digest appears in the embedded
signature. Kind and schema-version values are exact. Every digest uses
lowercase `sha256:<64-hex>`. The signature and basis preimages are their
exact RFC 8785 JCS values; a newline, another object order, a duplicate
name, a value outside I-JSON or an implementation-specific serialisation
cannot acquire the declared identity (P3).

Any change to the calculus basis, the signature refs, the closed signature
or the profile member bytes mints a new profile basis. Supersession is an
external Product and release judgment, and an earlier basis never silently
advances (P3, P6). The predecessor edition's coordinates are provenance of
this edition, not its identity: cut `stdo://releases/v2.5.1-rc.2/`, member
`standards/TRAVERSAL_OCCURRENCE_PROFILE.md` SHA-256
`618bb7c8f9f1eab8283cf595ac9da3533f0f9cf80a684c6f42e09142da6590c1`,
concept identity unchanged (P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#exclusions` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#exclusions` at rc.2:

```text
## Exclusions

This profile is not:

- a change to pure `a_c` or pure Reference Frame law;
- a mandatory profile for every symbolic model;
- a concrete subject or workspace ontology;
- a process, traversal, retry, continuation, or closure engine;
- an event store, event-log schema, projection implementation, or state carrier;
- a mutation, admission, evaluation, or decision authority;
- a prospective-frame or sensor-population profile;
- a guarantee that every framework event belongs to an occurrence; or
- a claim that every typed lineage graph is acyclic.
```

Successor, `TRAVERSAL_OCCURRENCE.md#exclusions`:

```text
## Exclusions

This profile is not (P2, P6):

- a change to pure `a_c` or to pure reference-frame law;
- a mandatory profile for every symbolic model;
- a concrete subject or workspace ontology;
- a process, traversal, retry, continuation or closure engine;
- an event store, event-log schema, projection implementation or state
  carrier;
- a mutation, admission, evaluation or decision authority;
- a prospective-frame or sensor-population profile;
- a guarantee that every framework event belongs to an occurrence; or
- a claim that every typed lineage graph is acyclic.
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#finite-reference-domain-table` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#finite-reference-domain-table` at rc.2:

```text
### Finite Reference-Domain Table

This table is the complete specialization of
`RefDomain_Sigma_occurrence(record_kind, qualified_field)`. Source families use
the exact `O/E/C/L/X/V/T/J` populations. `O:S` means semantic-object sort `S`;
`AnyLocal` means the closed union `O union E union C union L union X union V
union T union J`; and `Sigma:K` means one exact member of the named closed
signature population. Empty cells mean no target in that class.

The basis codes are exact relations, not labels:

```text
B_model     = same M_occ,b and record basis
B_profile   = exact TraversalOccurrenceProfileBasis resolution
B_calculus  = exact imported AxiomaticCalculusBasis resolution
B_adopted   = exact Product-adoption basis relation named for that external kind
```

| Source family and qualified field | Card. | Local family | Local sort | External target kind | Basis |
|---|---:|---|---|---|---|
| `O:*.context` | 1 |  |  | `Context` | `B_adopted` |
| `O:*.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `O:*.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `O:*.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:*.sort` | 1 |  |  | `Sigma:Sort` | `B_profile` |
| `E/C/L/X/V/T/J.context` | 1 |  |  | `Context` | `B_adopted` |
| `E/C/L/X/V/T/J.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `E/C/L/X/V/T/J.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `E/C/L/X/V/T/J.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:OccurrenceModelSubject.value.model_identity` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `O:OccurrenceModelSubject.value.profile_basis_ref` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:TraversalApplication.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:TraversalApplication.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:TraversalApplication.value.input_refs` | 0..* | `AnyLocal` |  | `TraversalInput` | `B_model or B_adopted` |
| `O:TraversalApplication.value.application_contract_ref` | 1 |  |  | `ApplicationContract` | `B_adopted` |
| `O:Occurrence.value.application_ref` | 1 | `O` | `TraversalApplication` |  | `B_model` |
| `O:Occurrence.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:Occurrence.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:Occurrence.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Occurrence.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:Occurrence.value.lineage_refs` | 0..* | `O` | `Occurrence` |  | `B_model` |
| `O:Occurrence.value.identity_dependency_refs` | 0..* | `AnyLocal` |  |  | `B_model` |
| `O:SubjectBinding.value.subject_ref` | 1 |  |  | `MutableSubject` | `B_adopted` |
| `O:SubjectBinding.value.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:SubjectBinding.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:Observation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Observation.value.observer_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:Observation.value.evidence_ref` | 1 |  |  | `Evidence` | `B_adopted` |
| `O:Observation.value.observation_coordinate_ref` | 1 |  |  | `ObservationCoordinate` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_ref` | 1 |  |  | `Outcome` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_contract_ref` | 1 |  |  | `OutcomeContract` | `B_adopted` |
| `O:IntendedOutcome.value.comparison_basis_ref` | 1 |  |  | `ComparisonBasis` | `B_adopted` |
| `O:OperationKind.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:OperationKind.value.target_sort_ref` | 1 |  |  | `TargetSort` | `B_adopted` |
| `O:OperationKind.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectOperation.value.operation_kind_ref` | 1 | `O` | `OperationKind` |  | `B_model` |
| `O:EffectOperation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectOperation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectOperation.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:EffectOperation.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:OperationGrant.value.issuer_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:OperationGrant.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:OperationGrant.value.allowed_operation_kind_refs` | 1..* | `O` | `OperationKind` |  | `B_model` |
| `O:OperationGrant.value.allowed_effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:OperationGrant.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectInvocation.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectInvocation.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectInvocation.value.executor_ref` | 1 |  |  | `Executor` | `B_adopted` |
| `O:EffectInvocation.value.actor_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:EffectInvocation.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectInvocation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectInvocation.value.input_refs` | 0..* | `AnyLocal` |  | `EffectInput` | `B_model or B_adopted` |
| `O:EffectDisposition.value.invocation_ref_or_none` | 0..1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectDisposition.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:EffectDisposition.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `O:EffectDisposition.value.residual_ref_or_none` | 0..1 | `X` |  |  | `B_model` |
| `O:EffectEvidence.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectEvidence.value.evidence_refs` | 1..* |  |  | `Evidence` | `B_adopted` |
| `O:EffectEvidence.value.observation_limit_ref` | 1 |  |  | `ObservationLimit` | `B_adopted` |
| `O:RelationClaim.value.relation_kind_ref` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `O:RelationClaim.value.source_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.target_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.claimant_ref` | 1 |  |  | `Claimant` | `B_adopted` |
| `O:RelationClaim.value.claim_basis_ref` | 1 |  |  | `ClaimBasis` | `B_adopted` |
| `O:RelationClaim.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:FrameworkEvent.value.event_kind_ref` | 1 |  |  | `Sigma:EventKind_occurrence` | `B_profile` |
| `O:FrameworkEvent.value.payload_ref` | 1 | `AnyLocal` |  |  | `B_model` |
| `O:FrameworkEvent.value.occurrence_ref_or_none` | 0..1 | `O` | `Occurrence` |  | `B_model` |
| `O:FrameworkEvent.value.claim_ref_or_none` | 0..1 | `O` | `RelationClaim` |  | `B_model` |
| `O:FrameworkEvent.value.claim_judgment_ref_or_none` | 0..1 | `J` |  |  | `B_model` |
| `O:FrameworkEvent.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EventFrontier.value.event_set_identity` | 1 |  |  | `EventSetIdentity` | `B_model` |
| `O:EventFrontier.value.member_event_refs` | 0..* | `O` | `FrameworkEvent` |  | `B_model` |
| `O:EventFrontier.value.projection_basis_ref` | 1 |  |  | `ProjectionBasis` | `B_adopted` |
| `O:EventFrontier.value.precedence_law_ref` | 1 |  |  | `PrecedenceLaw` | `B_adopted` |
| `O:Projection.value.frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:Projection.value.projection_rule_ref` | 1 |  |  | `ProjectionRule` | `B_adopted` |
| `O:Projection.value.selected_relation_refs` | 0..* | `E` |  |  | `B_model` |
| `O:Projection.value.boundary_refs` | 0..* | `AnyLocal` |  | `ProjectionBoundary` | `B_model or B_adopted` |
| `O:Projection.value.residual_refs` | 0..* | `X` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_ref` | 1 | `O` | `RelationClaim` |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_ref` | 1 | `O` | `FrameworkEvent` |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.materialized_relation_ref` | 1 | `E` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:SemanticAdmissionCut.value.successor_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EffectSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:EffectSubject.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectSubject.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectSubject.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectSubject.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectSubject.value.currentness_invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:TransitionSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:TransitionSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:TransitionSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:TransitionSubject.value.effect_disposition_ref` | 1 | `O` | `EffectDisposition` |  | `B_model` |
| `O:TransitionSubject.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `E:<each RelationKind>.source/target` | 1 | exact family from relation table | exact sort from relation table | declared endpoint where table permits | `B_model or B_adopted` |
| `E:*.kind` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `E:*.qualifiers.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `E:*.qualifiers.evidence_refs` | 0..* |  |  | `Evidence` | `B_adopted` |
| `E:*.qualifiers.provenance_refs` | 0..* |  |  | `Provenance` | `B_adopted` |
| `E:*.qualifiers.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `E:*.qualifiers.inverse_kind_ref_or_none` | 0..1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `C:*.kind` | 1 |  |  | `Sigma:ConstraintKind` | `B_profile` |
| `C:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `C:*.predicate` | 1 |  |  | `PredicateContract` | `B_adopted` |
| `C:*.judgment_kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `C:*.latitude_ref` | 0..1 | `L` |  |  | `B_model` |
| `L:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `L:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `X:*.subject` | 1 | `AnyLocal` |  | `ResidualSubject` | `B_model or B_adopted` |
| `X:*.kind` | 1 |  |  | `Sigma:ResidualKind` | `B_profile` |
| `X:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `X:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `V:*.domain/codomain` | 1 |  |  | `TypeDomain` | `B_adopted` |
| `V:*.preconditions/postconditions` | 0..* | `C` |  |  | `B_model` |
| `V:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `V:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `V:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.traversal` | 1 | `V` |  |  | `B_model` |
| `T:*.domain_model/codomain_model` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `T:*.operation_authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `T:*.preconditions` | 0..* | `C` |  |  | `B_model` |
| `T:*.preservation_relation` | 1 | `E` |  |  | `B_model` |
| `T:*.preserved/introduced/removed` | 0..* | `AnyLocal` |  | `ModelMemberIdentity` | `B_model or B_adopted` |
| `T:*.residuals` | 0..* | `X` |  |  | `B_model` |
| `T:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `T:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `T:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `J:*.kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `J:*.subject` | 1 | `AnyLocal` |  | `JudgmentSubject` | `B_model or B_adopted` |
| `J:*.evaluator` | 1 |  |  | `Evaluator` | `B_adopted` |
| `J:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `J:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `J:*.decided_at` | 1 |  |  | `DecisionCoordinate` | `B_adopted` |

The inherited transformation's external-resolution coordinates are closed by
the following finite expansion rather than hidden inside the three local-delta
rows above:

```text
D_ext = {
  external_preserved,
  external_introduced,
  external_removed
}

W_ext = {
  external_resolution,
  domain_resolution,
  codomain_resolution
}

Q_ext = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

for every d in D_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(T, d[].q) = ResolutionRefDomain(q)

for every w in W_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(
    T,
    external_resolution_witnesses[].w.q
  ) = ResolutionRefDomain(q)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].domain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].codomain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].evidence
) = (1, empty, empty, {Evidence}, B_adopted)
```

`ResolutionRefDomain` is exact and dependent only where the resolution tuple
itself supplies the target coordinate:

```text
ResolutionRefDomain(external_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(reference_domain)
  = (1, empty, empty, {Sigma:ReferenceDomain}, B_profile)

ResolutionRefDomain(external_target_kind)
  = (1, empty, empty, {Sigma:ExternalTargetKind}, B_profile or B_adopted)

ResolutionRefDomain(resolved_target_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(basis_relation)
  = (1, empty, empty, {Sigma:BasisRelation}, B_profile)

ResolutionRefDomain(resolution_basis)
  = (1, empty, empty,
     {TraversalOccurrenceProfileBasis,
      AxiomaticCalculusBasis,
      ProductAdoptionBasis},
     B_profile or B_calculus or B_adopted)

ResolutionRefDomain(evidence_identity)
  = (1, empty, empty, {Evidence}, B_adopted)
```

Each member of `D_ext` is a duplicate-free finite `Resolution_M` value list.
`external_resolution_witnesses` is a duplicate-free finite inherited
`ExternalResolutionPreservationWitness` value list. Every coordinate has
exactly `Q_ext`; every witness has exactly `external_resolution`,
`domain_model`, `codomain_model`, `domain_resolution`,
`codomain_resolution`, `decision`, and `evidence`; and `decision` is exactly
`equal`. A missing or extra nested field, unresolved nested identity,
coordinate/basis mismatch, duplicate coordinate, or witness outside the exact
preserved population refuses model validation.

`id` fields own identities rather than reference them. Digests, closed enum
values, predicates, qualifiers other than the listed refs, uncertainty,
consequence, variation content, and refusal values are closed non-reference
content. A compatible extension changes this table by minting a new signature;
it cannot reinterpret an existing row. Every list is duplicate-free before
set comparison. A missing row, target outside its row, wrong local population
or sort, unresolved external target, cardinality violation, or basis-relation
mismatch refuses model validation.
```

Successor, `TRAVERSAL_OCCURRENCE.md#finite-reference-domain-table`:

```text
### Finite reference-domain table

This table is the complete specialisation of
`RefDomain_Sigma_occurrence(record_kind, qualified_field)`. Source families
use the exact `O/E/C/L/X/V/T/J` populations. `O:S` means semantic-object
sort `S`; `AnyLocal` means the closed union `O union E union C union L
union X union V union T union J`; `Sigma:K` means one exact member of the
named closed signature population; an empty cell means no target in that
class. `Sigma:ReferenceDomain`, `Sigma:ExternalTargetKind` and
`Sigma:BasisRelation` are populations of this profile's signature, named
here and not by the calculus (P3).

The basis codes are exact relations, not labels (P3):

```text
B_model     = same M_occ,b and record basis
B_profile   = exact TraversalOccurrenceProfileBasis resolution
B_calculus  = exact imported AxiomaticCalculusBasis resolution
B_adopted   = exact Product-adoption basis relation named for that external kind
```

| Source family and qualified field | Card. | Local family | Local sort | External target kind | Basis |
|---|---:|---|---|---|---|
| `O:*.context` | 1 |  |  | `Context` | `B_adopted` |
| `O:*.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `O:*.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `O:*.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:*.sort` | 1 |  |  | `Sigma:Sort` | `B_profile` |
| `E/C/L/X/V/T/J.context` | 1 |  |  | `Context` | `B_adopted` |
| `E/C/L/X/V/T/J.owner` | 1 |  |  | `Owner` | `B_adopted` |
| `E/C/L/X/V/T/J.scope` | 1 |  |  | `GovernedScope` | `B_adopted` |
| `E/C/L/X/V/T/J.basis` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:OccurrenceModelSubject.value.model_identity` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `O:OccurrenceModelSubject.value.profile_basis_ref` | 1 |  |  | `TraversalOccurrenceProfileBasis` | `B_profile` |
| `O:TraversalApplication.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:TraversalApplication.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:TraversalApplication.value.input_refs` | 0..* | `AnyLocal` |  | `TraversalInput` | `B_model or B_adopted` |
| `O:TraversalApplication.value.application_contract_ref` | 1 |  |  | `ApplicationContract` | `B_adopted` |
| `O:Occurrence.value.application_ref` | 1 | `O` | `TraversalApplication` |  | `B_model` |
| `O:Occurrence.value.traversal_ref` | 1 | `V` |  |  | `B_model` |
| `O:Occurrence.value.functor_kind_ref` | 1 |  |  | `Sigma:FunctorKind` | `B_calculus` |
| `O:Occurrence.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Occurrence.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:Occurrence.value.lineage_refs` | 0..* | `O` | `Occurrence` |  | `B_model` |
| `O:Occurrence.value.identity_dependency_refs` | 0..* | `AnyLocal` |  |  | `B_model` |
| `O:SubjectBinding.value.subject_ref` | 1 |  |  | `MutableSubject` | `B_adopted` |
| `O:SubjectBinding.value.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:SubjectBinding.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:Observation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:Observation.value.observer_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:Observation.value.evidence_ref` | 1 |  |  | `Evidence` | `B_adopted` |
| `O:Observation.value.observation_coordinate_ref` | 1 |  |  | `ObservationCoordinate` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_ref` | 1 |  |  | `Outcome` | `B_adopted` |
| `O:IntendedOutcome.value.outcome_contract_ref` | 1 |  |  | `OutcomeContract` | `B_adopted` |
| `O:IntendedOutcome.value.comparison_basis_ref` | 1 |  |  | `ComparisonBasis` | `B_adopted` |
| `O:OperationKind.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:OperationKind.value.target_sort_ref` | 1 |  |  | `TargetSort` | `B_adopted` |
| `O:OperationKind.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectOperation.value.operation_kind_ref` | 1 | `O` | `OperationKind` |  | `B_model` |
| `O:EffectOperation.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectOperation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectOperation.value.operation_contract_ref` | 1 |  |  | `OperationContract` | `B_adopted` |
| `O:EffectOperation.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:OperationGrant.value.issuer_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `O:OperationGrant.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:OperationGrant.value.allowed_operation_kind_refs` | 1..* | `O` | `OperationKind` |  | `B_model` |
| `O:OperationGrant.value.allowed_effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:OperationGrant.value.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:EffectInvocation.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectInvocation.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectInvocation.value.executor_ref` | 1 |  |  | `Executor` | `B_adopted` |
| `O:EffectInvocation.value.actor_ref` | 1 |  |  | `Actor` | `B_adopted` |
| `O:EffectInvocation.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectInvocation.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectInvocation.value.input_refs` | 0..* | `AnyLocal` |  | `EffectInput` | `B_model or B_adopted` |
| `O:EffectDisposition.value.invocation_ref_or_none` | 0..1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectDisposition.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:EffectDisposition.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `O:EffectDisposition.value.residual_ref_or_none` | 0..1 | `X` |  |  | `B_model` |
| `O:EffectEvidence.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectEvidence.value.evidence_refs` | 1..* |  |  | `Evidence` | `B_adopted` |
| `O:EffectEvidence.value.observation_limit_ref` | 1 |  |  | `ObservationLimit` | `B_adopted` |
| `O:RelationClaim.value.relation_kind_ref` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `O:RelationClaim.value.source_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.target_ref` | 1 | `AnyLocal` |  | `DeclaredRelationEndpoint` | `B_model or B_adopted` |
| `O:RelationClaim.value.claimant_ref` | 1 |  |  | `Claimant` | `B_adopted` |
| `O:RelationClaim.value.claim_basis_ref` | 1 |  |  | `ClaimBasis` | `B_adopted` |
| `O:RelationClaim.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:FrameworkEvent.value.event_kind_ref` | 1 |  |  | `Sigma:EventKind_occurrence` | `B_profile` |
| `O:FrameworkEvent.value.payload_ref` | 1 | `AnyLocal` |  |  | `B_model` |
| `O:FrameworkEvent.value.occurrence_ref_or_none` | 0..1 | `O` | `Occurrence` |  | `B_model` |
| `O:FrameworkEvent.value.claim_ref_or_none` | 0..1 | `O` | `RelationClaim` |  | `B_model` |
| `O:FrameworkEvent.value.claim_judgment_ref_or_none` | 0..1 | `J` |  |  | `B_model` |
| `O:FrameworkEvent.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EventFrontier.value.event_set_identity` | 1 |  |  | `EventSetIdentity` | `B_model` |
| `O:EventFrontier.value.member_event_refs` | 0..* | `O` | `FrameworkEvent` |  | `B_model` |
| `O:EventFrontier.value.projection_basis_ref` | 1 |  |  | `ProjectionBasis` | `B_adopted` |
| `O:EventFrontier.value.precedence_law_ref` | 1 |  |  | `PrecedenceLaw` | `B_adopted` |
| `O:Projection.value.frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:Projection.value.projection_rule_ref` | 1 |  |  | `ProjectionRule` | `B_adopted` |
| `O:Projection.value.selected_relation_refs` | 0..* | `E` |  |  | `B_model` |
| `O:Projection.value.boundary_refs` | 0..* | `AnyLocal` |  | `ProjectionBoundary` | `B_model or B_adopted` |
| `O:Projection.value.residual_refs` | 0..* | `X` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_ref` | 1 | `O` | `RelationClaim` |  | `B_model` |
| `O:SemanticAdmissionCut.value.claim_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_ref` | 1 | `O` | `FrameworkEvent` |  | `B_model` |
| `O:SemanticAdmissionCut.value.event_judgment_ref` | 1 | `J` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.materialized_relation_ref` | 1 | `E` |  |  | `B_model` |
| `O:SemanticAdmissionCut.value.source_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:SemanticAdmissionCut.value.successor_frontier_ref` | 1 | `O` | `EventFrontier` |  | `B_model` |
| `O:EffectSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:EffectSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:EffectSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:EffectSubject.value.invocation_ref` | 1 | `O` | `EffectInvocation` |  | `B_model` |
| `O:EffectSubject.value.operation_ref` | 1 | `O` | `EffectOperation` |  | `B_model` |
| `O:EffectSubject.value.operation_grant_ref` | 1 | `O` | `OperationGrant` |  | `B_model` |
| `O:EffectSubject.value.effect_territory_ref` | 1 |  |  | `EffectTerritory` | `B_adopted` |
| `O:EffectSubject.value.currentness_invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `O:TransitionSubject.value.occurrence_ref` | 1 | `O` | `Occurrence` |  | `B_model` |
| `O:TransitionSubject.value.subject_binding_ref` | 1 | `O` | `SubjectBinding` |  | `B_model` |
| `O:TransitionSubject.value.pre_observation_ref` | 1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.post_observation_ref_or_none` | 0..1 | `O` | `Observation` |  | `B_model` |
| `O:TransitionSubject.value.intended_outcome_ref` | 1 | `O` | `IntendedOutcome` |  | `B_model` |
| `O:TransitionSubject.value.effect_disposition_ref` | 1 | `O` | `EffectDisposition` |  | `B_model` |
| `O:TransitionSubject.value.effect_evidence_refs` | 0..* | `O` | `EffectEvidence` |  | `B_model` |
| `E:<each RelationKind>.source/target` | 1 | exact family from relation table | exact sort from relation table | declared endpoint where table permits | `B_model or B_adopted` |
| `E:*.kind` | 1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `E:*.qualifiers.authority_ref` | 1 |  |  | `Authority` | `B_adopted` |
| `E:*.qualifiers.evidence_refs` | 0..* |  |  | `Evidence` | `B_adopted` |
| `E:*.qualifiers.provenance_refs` | 0..* |  |  | `Provenance` | `B_adopted` |
| `E:*.qualifiers.invalidation_ref` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `E:*.qualifiers.inverse_kind_ref_or_none` | 0..1 |  |  | `Sigma:RelationKind` | `B_profile` |
| `C:*.kind` | 1 |  |  | `Sigma:ConstraintKind` | `B_profile` |
| `C:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `C:*.predicate` | 1 |  |  | `PredicateContract` | `B_adopted` |
| `C:*.judgment_kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `C:*.latitude_ref` | 0..1 | `L` |  |  | `B_model` |
| `L:*.applies_to` | 1 | `AnyLocal` |  |  | `B_model` |
| `L:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `X:*.subject` | 1 | `AnyLocal` |  | `ResidualSubject` | `B_model or B_adopted` |
| `X:*.kind` | 1 |  |  | `Sigma:ResidualKind` | `B_profile` |
| `X:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `X:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `V:*.domain/codomain` | 1 |  |  | `TypeDomain` | `B_adopted` |
| `V:*.preconditions/postconditions` | 0..* | `C` |  |  | `B_model` |
| `V:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `V:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `V:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.traversal` | 1 | `V` |  |  | `B_model` |
| `T:*.domain_model/codomain_model` | 1 |  |  | `ModelContentIdentity` | `B_adopted` |
| `T:*.operation_authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `T:*.preconditions` | 0..* | `C` |  |  | `B_model` |
| `T:*.preservation_relation` | 1 | `E` |  |  | `B_model` |
| `T:*.preserved/introduced/removed` | 0..* | `AnyLocal` |  | `ModelMemberIdentity` | `B_model or B_adopted` |
| `T:*.residuals` | 0..* | `X` |  |  | `B_model` |
| `T:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `T:*.stop_states` | 1..* |  |  | `Sigma:StopKind` | `B_profile` |
| `T:*.invalidation` | 1 |  |  | `InvalidationContract` | `B_adopted` |
| `T:*.re_entry` | 1 | `V` |  | `ReEntryContract` | `B_model or B_adopted` |
| `J:*.kind` | 1 |  |  | `Sigma:JudgmentKind` | `B_profile` |
| `J:*.subject` | 1 | `AnyLocal` |  | `JudgmentSubject` | `B_model or B_adopted` |
| `J:*.evaluator` | 1 |  |  | `Evaluator` | `B_adopted` |
| `J:*.authority` | 1 |  |  | `AuthorityGrant` | `B_adopted` |
| `J:*.evidence/provenance` | 0..* |  |  | `EvidenceOrProvenance` | `B_adopted` |
| `J:*.decided_at` | 1 |  |  | `DecisionCoordinate` | `B_adopted` |

The external-resolution coordinates of the inherited transformation are
closed by this finite expansion and are not hidden inside the three
local-delta rows above (P3, P4b):

```text
D_ext = {
  external_preserved,
  external_introduced,
  external_removed
}

W_ext = {
  external_resolution,
  domain_resolution,
  codomain_resolution
}

Q_ext = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

for every d in D_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(T, d[].q) = ResolutionRefDomain(q)

for every w in W_ext and q in Q_ext:
  RefDomain_Sigma_occurrence(
    T,
    external_resolution_witnesses[].w.q
  ) = ResolutionRefDomain(q)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].domain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].codomain_model
) = (1, empty, empty, {ModelContentIdentity}, B_adopted)

RefDomain_Sigma_occurrence(
  T,
  external_resolution_witnesses[].evidence
) = (1, empty, empty, {Evidence}, B_adopted)
```

`ResolutionRefDomain` is exact, and it is dependent only where the
resolution tuple itself supplies the target coordinate (P3):

```text
ResolutionRefDomain(external_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(reference_domain)
  = (1, empty, empty, {Sigma:ReferenceDomain}, B_profile)

ResolutionRefDomain(external_target_kind)
  = (1, empty, empty, {Sigma:ExternalTargetKind}, B_profile or B_adopted)

ResolutionRefDomain(resolved_target_identity)
  = (1, empty, empty,
     {sibling external_target_kind},
     sibling basis_relation over sibling resolution_basis)

ResolutionRefDomain(basis_relation)
  = (1, empty, empty, {Sigma:BasisRelation}, B_profile)

ResolutionRefDomain(resolution_basis)
  = (1, empty, empty,
     {TraversalOccurrenceProfileBasis,
      AxiomaticCalculusBasis,
      ProductAdoptionBasis},
     B_profile or B_calculus or B_adopted)

ResolutionRefDomain(evidence_identity)
  = (1, empty, empty, {Evidence}, B_adopted)
```

Each member of `D_ext` is a finite `Resolution_M` value list without
duplicates. `external_resolution_witnesses` is a finite inherited
`ExternalResolutionPreservationWitness` value list without duplicates.
Every coordinate has exactly `Q_ext`; every witness has exactly
`external_resolution`, `domain_model`, `codomain_model`,
`domain_resolution`, `codomain_resolution`, `decision` and `evidence`;
and `decision` is exactly `equal`. A missing or extra nested field, an
unresolved nested identity, a coordinate and basis mismatch, a duplicate
coordinate, or a witness outside the exact preserved population refuses
model validation (P3, P5).

`id` fields own identities rather than reference them. Digests, closed
enum values, predicates, qualifiers other than the listed refs,
uncertainty, consequence, variation content and refusal values are closed
non-reference content. A compatible extension changes this table by
minting a new signature; it cannot reinterpret an existing row. Every list
is free of duplicates before any set comparison. A missing row, a target
outside its row, a wrong local population or sort, an unresolved external
target, a cardinality violation or a basis-relation mismatch refuses model
validation (P3, P5).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#imported-calculus-boundary` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#imported-calculus-boundary` at rc.2:

```text
## Imported Calculus Boundary

For exact `AxiomaticCalculusBasis` identity `b_ac`, this profile declares:

```text
Sigma_occurrence = instantiate_signature(b_ac, OccurrenceSignatureDefinition)
```

`OccurrenceSignatureDefinition` imports the exact finite `RecordKind_ac` set
unchanged and declares the complete finite sets of closed sorts, relation
kinds, constraint kinds, judgment kinds, residual kinds, stop kinds, auxiliary
value domains, field reference domains, and exact inherited functor-kind refs
below. A conflicting calculus basis, inherited field meaning, record shape,
population, value domain, reference domain, relation domain, authority
coordinate, or refusal law makes instantiation invalid.

An occurrence model remains an ordinary `a_c` model:

```text
M_occ,b = (b, I, O, E, C, L, X, V, T, J)
M_occ,b satisfies a_c[Sigma_occurrence]

Population_M_occ = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object -> O,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation -> E,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint -> C,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude -> L,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual -> X,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal -> V,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation -> T,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment -> J
}
```

Only profile semantic objects use `SemanticObject.value`. Relations,
constraints, latitude, residuals, traversals, transformations, and judgments
retain their exact inherited `a_c` record families and coordinates.

`Population_M_occ` is total over and exactly equal to `RecordKind_ac`. Every
fundamental record occurs in exactly one finite population, local identities
are unique across the disjoint union, and every other member of `I` resolves
once through a profile-declared external reference domain and basis relation.
The profile adds sorts and value domains, never another fundamental record
kind. Its `RefDomain_Sigma_occurrence(record_kind, qualified_field)` closes
every identity-bearing value field and inherited record field to an exact
local record kind and semantic-object sort or one declared external target
kind. `qualified_field` includes the source sort or kind and complete nested
field path; nominally equal field labels never merge their domains.
Missing populations, hidden records, locally-and-externally ambiguous refs,
unknown record kinds, and undeclared field domains refuse model validation.
```

Successor, `TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary`:

```text
## Imported calculus boundary

For an exact `AxiomaticCalculusBasis` identity `b_ac`, the profile declares
(P3, P4a):

```text
Sigma_occurrence = instantiate_signature(b_ac, OccurrenceSignatureDefinition)
```

`instantiate_signature` and `OccurrenceSignatureDefinition` are this
profile's own notation; the calculus defines neither.
`OccurrenceSignatureDefinition` imports the exact finite `RecordKind_ac`
set unchanged and declares the complete finite sets of closed sorts,
relation kinds, constraint kinds, judgment kinds, residual kinds, stop
kinds, auxiliary value domains, field reference domains and exact
inherited functor-kind refs given below. Instantiation is invalid when the
calculus basis, an inherited field meaning, a record shape, a population, a
value domain, a reference domain, a relation domain, an authority
coordinate or a refusal law conflicts (P3, P5).

An occurrence model stays an ordinary `a_c` model (P3):

```text
M_occ,b = (b, I, O, E, C, L, X, V, T, J)
M_occ,b satisfies a_c[Sigma_occurrence]

Population_M_occ = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object -> O,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation -> E,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint -> C,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude -> L,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual -> X,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal -> V,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation -> T,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment -> J
}
```

Only the profile's semantic objects use `SemanticObject.value`. Relations,
constraints, latitude, residuals, traversals, transformations and
judgments keep their exact inherited `a_c` record families and coordinates
(P3).

`Population_M_occ` is total over `RecordKind_ac` and exactly equal to it.
Every fundamental record occurs in exactly one finite population, local
identities are unique across the disjoint union, and every other member of
`I` resolves once through a reference domain and basis relation that the
profile declares as external. The profile adds sorts and value domains and
never another fundamental record kind. Its
`RefDomain_Sigma_occurrence(record_kind, qualified_field)` closes every
identity-bearing value field and inherited record field either to one
exact local record kind and semantic-object sort or to one declared
external target kind. `qualified_field` includes the source sort or kind
and the complete nested field path, so field labels that are nominally
equal never merge their domains. Missing populations, hidden records, refs
ambiguous between local and external, unknown record kinds and undeclared
field domains refuse model validation (P3, P5).
```
