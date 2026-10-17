# I5-03 reading batch 06

Rows: 47. Members: ['ODD_METHOD.md', 'POSTING_GUIDE.md', 'README.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `ODD_METHOD.md#115c-projection-source-coherence` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#115c-projection-source-coherence` at rc.2:

```text
### 11.5C Projection-Source Coherence

Projection and query lanes are downstream read models over admitted carrier,
runtime, event, or source truth.

They may summarize, index, filter, or render that truth.

They must not reconstruct an alternate authority surface beside the admitted
carrier.

For an ODD product, this means:

- function catalog views must reconcile to the admitted GTL module or public
  carrier
- asset ownership and start-target views must be derived from, or structurally
  compared against, the admitted carrier they expose
- runtime status views must derive from ABG runtime facts, events, replay, or
  projection truth
- domain query overlays must fail closed when the carrier they describe is
  missing, stale, or structurally divergent

Name equality is not enough.

A same-named graph function, node, carrier, policy, or route with different
inputs, outputs, vectors, declarations, ownership, or closure law is a different
truth surface until reconciled.

Negative proof for a projection must include structural drift, not only missing
source truth.
```

Successor, `ODD.md#115c-projection-source-coherence`:

```text
### 11.5C Projection-source coherence

Projection and query lanes are downstream read models over admitted
carrier, runtime, event or source truth. They may summarise, index,
filter or render that truth; they must not reconstruct an alternate
authority surface beside the admitted carrier (P3, P6).

For an ODD product: function catalogue views must reconcile to the
admitted GTL module or public carrier; asset ownership and start-target
views must be derived from, or structurally compared against, the admitted
carrier they expose; runtime status views must derive from ABG runtime
facts, events, replay or projection truth; domain query overlays must fail
closed when the carrier they describe is missing, stale or structurally
divergent (P3, P6).

Name equality is not enough. A same-named graph function, node, carrier,
policy or route with different inputs, outputs, vectors, declarations,
ownership or closure law is a different truth surface until reconciled.
Negative proof for a projection must include structural drift, not only
missing source truth (P3, P6).
```


### Row `ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop` at rc.2:

```text
### 11.5D Constructive Evaluation And Yield Loop

Every ODD product over GTL/ABG must preserve one constructive evaluation loop
from intent lineage and model synthesis through observation to next lawful
action.

This is the method-level homeostasis loop. The constitutional surface names the
operative functions directly: `synthesize_model`, `eval_gap`, `evaluate_next`,
and `evaluate_action`.

The selected Product outcome under `STDO-UP-013` is external authority for this
loop. Product models, gaps, assurance, ledgers, and projections may interpret
that outcome but cannot author, select, or enlarge it. `evaluate_next` may
select material work only within that outcome or an admitted bounded
prerequisite or experiment. Graph or edge closure is evidence toward Product
acceptance; it is not Product or release acceptance. When the selected outcome
is accepted, an admitted prerequisite is discharged, an admitted experiment's
stated decision is resolved, another admitted terminal condition is reached, or
its governing basis or bound is exhausted, rejected, withdrawn, superseded,
repriced away, or falsified, the loop selects no further material work without
another admitted basis. A `reprice` disposition requests lawful constitutional
re-entry; it does not perform the reprice or select the successor outcome.

The loop is framework-independent. Product implementations may use different
carrier names, but they must preserve this authority shape:

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

The objects have these method-level meanings:

| Object | Definition | Authority |
| --- | --- | --- |
| `IntentLineage` | Admitted source intent and its lineage refs: human, imported source, prior product, intent engine, or prior synthesized construction intent. | ABG event-log truth over source intent. It seeds the product model and must not invent graph actions. |
| `ProductAssetModel` | Desired and known typed asset model synthesized from intent lineage, prior model, and admitted product truth. | Product-owned model truth whose publication basis is carried by admitted events and product-owned projection refs. It is not runtime fact or action authority. |
| `Worksite` | Current workspace, runtime archive, transform assets, product asset root, profile, and observed file or process state. | Observable substrate, not authority by itself. |
| `RuntimeEventLog` | Append-only admitted runtime facts. | ABG runtime truth. |
| `RuntimeProjection` | Replay-derived current runtime state over event log and execution basis. | ABG projection truth. |
| `ObservationSnapshot` | Read-only view of runtime truth plus worksite facts relevant to construction. | ABG evaluator carrier with product domain rows. |
| `GapPressureRow` | Typed pressure over missing, partial, blocked, waiting, or ambiguous assets and evidence. | Product domain meaning over admitted observation. |
| `TargetObligationBinding` | Exact binding from gap pressure to the selected Product outcome, any admitted prerequisite or experiment basis, target assets, required roles, evidence refs, and admissible graph outcomes. | Product domain binding over GTL/ABG action authority. |
| `ActionCatalog` | Published lawful graph actions: graph functions, vectors, targets, inputs, and eligible outcomes. | GTL/product publication consumed by ABG. |
| `NextActionBasis` | Sum type naming why `evaluate_next` is being called: `initial_selection`, `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. `post_reprice` records a re-entry request and carries no action-selection authority. | Dispatch basis for next-action evaluation. It is not a separate controller. |
| `PriorityProjection` | Deterministic ranking over bound lawful actions under visible policy. | ABG evaluator kernel plus product policy. |
| `ConstructionIntent` | Admitted selected action for one bounded graph invocation, preserving the selected outcome or admitted bounded-basis refs carried by its target binding. | ABG admission and traversal authority. |
| `AdmittedEvidence` | Admitted worker, process, product, execution, materialization, liveness, and postflight evidence. | ABG/product admission, not worker self-closure. |
| `EdgeFulfillmentLedger` | Evidence and convergence carrier for one edge attempt or version. | Closure evidence truth. |
| `EdgeClosureDecision` | Sum type over the ledger: close, yield, retry, repair, re-enter, reprice, block. | Closure decision truth. |
| `NextActionProjection` | Read model that observes `NextActionBasis` plus current truth and selects a next graph action only when lawful. | ABG next-action evaluation projection with product policy. |

The loop has one model synthesis function and three distinct evaluation
functions. They may share underlying libraries, but they must not share
authority:

| Function | Inputs | Output | Boundary |
| --- | --- | --- | --- |
| `synthesize_model` | `IntentLineage + prior ProductAssetModel + admitted product truth` | `ProductAssetModel` | Model synthesis. It may update desired and known typed asset truth. It must not observe the worksite, select work, invoke work, or close work. |
| `eval_gap` | `ProductAssetModel + RuntimeEventLog + RuntimeProjection + Worksite` | `ObservationSnapshot + GapPressureRow` | Read-only gap discovery. It compares desired model truth to observed reality and emits missing, partial, blocked, waiting, or ambiguous asset pressure. It does not choose work and does not close work. |
| `evaluate_next` | `NextActionBasis + fresh eval_gap + TargetObligationBinding + ActionCatalog + Policy` | `PriorityProjection + NextActionProjection + selected_action` | Next-action selection. `TargetObligationBinding` carries the exact selected Product outcome and any admitted bounded-basis refs. `NextActionBasis` is either `initial_selection(IntentLineage, ProductAssetModel)` or one explicit post-action basis derived from an `EdgeClosureDecision`: `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. Except for unresolved `post_reprice`, which returns typed no-action pending separately admitted constitutional authority, it may select only published lawful graph actions that bind to the gap and governing basis. It does not admit construction intent and does not evaluate the result of an action. |
| `evaluate_action` | `ConstructionIntent + AdmittedEvidence + TargetObligationBinding + Policy` | `EdgeFulfillmentLedger + EdgeClosureDecision` | Action-result evaluation. It decides close, yield, retry, repair, re-enter, reprice, or block for the action just taken. It does not choose the next graph action. |

The word `evaluator` is not sufficient by itself. A design, ticket, code module,
or proof must name which function it is implementing or consuming:
`synthesize_model`, `eval_gap`, `evaluate_next`, or `evaluate_action`.

Intent has lineage through the loop. Bootstrap or external intent may come from a
human, imported source, prior product, or intent engine. That intent seeds the
product asset model used by `eval_gap`. Current construction intent is
synthesized against that model and the observed gap, then admitted by a distinct
admission step after `evaluate_next` selects a published graph action. Intent
does not invent unpublished actions; gap-derived action selection provides the
selected action basis for admitting current construction intent over an
already-published graph function or vector. `ConstructionIntent` must cite the
lineage, selected action, and `TargetObligationBinding` that preserve the exact
selected Product outcome and any admitted bounded-basis refs.

The loop is governed by these axioms:

**A0. One Surface**

There is one authoritative computational surface for traversal consequence:

```text
IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

No CLI branch, prompt prose, postflight string, gap-dossier action list, query
projection, service method, or local operator summary may become a rival source
of traversal truth.

**A1. Worksite Is Observed, Not Trusted**

The file system, process output, screen logs, worker artifacts, and product
files are observations. They become authority only after admission into typed
evidence and fold into ledger and decision truth.

**A1a. Workspace-Ledger Governed Work Pair**

The worksite/workspace and ledger form the governed work pair:

```text
W = mutable workspace under construction
L = immutable governed ledger of work over W
E = immutable event log / replay spine
Ev = evaluator work over L
```

The workspace is where F_P construction occurs. The ledger is the immutable
governed account of closure-relevant work over that workspace. The ledger is not
a copy of the workspace; it is the admitted trace of callout basis, observed
deltas, file refs, digests, execution evidence, obligations touched, claims
made, evaluator inputs, evaluator outputs, and admission status.

The loop is:

```text
F_P acts in W.
Admission records governed facts in L.
E orders and anchors L entries with predecessor refs.
Ev evaluates a declared L snapshot, not ambient W.
Ev output is itself F_P work and is admitted back into L/E.
L/E constrain the next lawful F_P action in W.
```

The consistency rule is:

```text
W can change without being true.
L can be true without being the whole W.
Closure can only use W through L.
Eval can only judge W through L.
Eval only affects traversal after its own L/E admission.
```

Every closure-relevant F_P callout that does work needs ledger admission.
Evaluator work is not outside F_P merely because it reads ledgers. Evaluator work
is F_P work over governed ledger state, and its result must be admitted into the
immutable ledger/event spine before it can affect closure, routing, or traversal.
Corrections append or supersede ledger/event facts; they do not rewrite the
governed history of work.

**A1b. Ledger Is Governed Attention**

A ledger is the system's governed attention over construction history.

This is a structural analogy, not an implementation dependency on transformer
attention. Model attention selects from context through learned weights. ODD
ledger attention is typed, immutable, lineage-constrained, policy-bounded, and
replayable.

An evaluator may attend only to admitted ledger rows reachable through declared
lineage, predecessor refs, target binding, policy, and the relevant event-log
cursor. Workspace facts, worker prose, archives, summaries, or controller memory
outside that reachable ledger set are not inside the evaluator's lawful
attention surface.

Lineage is therefore not only provenance bookkeeping. Lineage is the attention
graph: it determines which evidence the evaluator may see, what must be ignored,
and which predecessor chain makes the judgment reproducible.

**A2. Exact Target Binding**

Every constructive action must bind the current gap to exact target assets and
obligations before invocation:

```text
selected Product outcome ref
+ optional admitted prerequisite or experiment basis ref
+ gap pressure + target assets + required roles + evidence refs
-> TargetObligationBinding
```

A broad edge cannot satisfy a specific product or evidence gap unless the
binding proves that edge is the lawful action for those exact assets.

**A3. Published Action Law**

`evaluate_next` may rank only published lawful actions from the action catalog.
If the desired action is unpublished, the lawful result is a typed no-action
disposition, not fallback to a broad executive graph or local script.

**A4. Evaluate_Next Totality**

`evaluate_next` must be total.

If `NextActionBasis` is `initial_selection`, `evaluate_next` selects from the
current model, current gap, target binding, catalog, and policy. If
`NextActionBasis` is `post_yield_resume`, `evaluate_next` resumes or yields the
same edge from replay-visible resume truth without classifying the action as
failure. If `NextActionBasis` is `post_close_graph_continuation`,
`evaluate_next` may select the next graph edge after the current edge is closed,
or no action when the graph is complete. For `post_retry`, `post_repair`,
`post_reenter`, and `post_block`:

```text
if higher-priority lawful action exists:
  select it
else if current graph edge remains lawful:
  follow the graph
else if authority is missing:
  reprice or block
else:
  block with typed no-action disposition
```

For `post_reprice`, `evaluate_next` must return a typed no-action disposition
while constitutional re-entry remains unresolved. The reprice decision cannot
authorize a replacement action. Work may be evaluated again only after lawful
re-entry separately admits an exact selected Product outcome or bounded basis
and supplies it through a new `initial_selection` or basis-bearing resume.

Default graph following is ordinary, but it is still an `evaluate_next`
decision, not hidden sequential control.

**A4a. Evaluation Function Separation**

`synthesize_model`, `eval_gap`, `evaluate_next`, and `evaluate_action` are
separate authority functions.

`synthesize_model` may synthesize the current product asset model from
event-log-backed intent lineage, prior model, and admitted product truth only.
It must not observe the worksite, admit construction intent, invoke work, close
work, or select next action.

`eval_gap` may emit observation and gap pressure only. It must not admit
construction intent, invoke work, close work, or select next action.

`evaluate_action` may fold admitted action evidence into ledger and closure
decision only. It must not select the next graph action.

`evaluate_next` may bind target obligations, rank lawful published actions, and
publish next-action projection. It must not admit construction intent or decide
whether the prior action closed, yielded, failed, or requires repair except by
consuming the admitted `EdgeClosureDecision`.

Any module that lets one of these functions perform another function's authority
creates a rival control surface and violates A0.

**A5. F_P Freedom, F_D Authority**

F_P may inspect, discover, reason, draft, transform, and propose within the
bounded action. F_P must not close the edge, emit runtime events, mutate ledgers,
or decide re-entry. F_D/ABG/product admission owns durable evidence and closure
truth.

**A6. Evidence Before Closure**

No edge closes from raw artifact presence, raw worker report, raw process
success, or CLI summary. Closure is a fold over admitted evidence:

```text
AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
```

**A7. Ledger Is Evidence, Not Action Selector**

`EdgeFulfillmentLedger` records evidence and convergence:

```text
counts
obligation rows
materialization refs
liveness refs
admission refs
edge_converged
```

It does not select the next action. Action selection belongs to `evaluate_next`
over `EdgeClosureDecision` plus fresh `eval_gap` truth.

**A8. Closure Decision Is A Sum Type**

The closure decision vocabulary is:

```text
close
yield
retry
repair
re-enter
reprice
block
```

Each disposition is replay-visible and must carry basis and reason refs
sufficient to reproduce the decision.

**A9. Yield Is Lawful Iterate**

`yield` is the lawful iteration boundary:

```text
same edge or attempt remains lawful
progress or waiting state is admitted
resume basis is replay-visible
control returns without failure classification
```

Yield is not retry. Yield is not block. Yield is not timeout. Yield is not a
local CLI loop. It is the pressure-release state that lets long-running,
bounded, or partially productive work return control without losing the current
edge.

**A10. Liveness Does Not Close Semantic Truth**

Liveness observes activity, inactivity, process state, and interruption. It can
support yield or liveness interruption. It cannot by itself declare semantic
failure, semantic closure, or requirement non-satisfaction.

**A11. Re-Entry Is Graph Law**

Repair and re-entry are graph actions selected by `evaluate_next` from admitted
closure truth and published action authority. They are not local retry branches
over strings.

`evaluate_action` may emit `repair` or `re-enter` as a closure disposition.
`evaluate_next` selects which published graph action realizes that repair or
re-entry. Disposition is conceptual; selection is invocational.

**A12. Public Query Is A Read-Only Evaluation View**

A public query or gaps view may render read-only outputs from `eval_gap`,
`evaluate_action`, and `evaluate_next`: gap pressure, closure decision, and
next-action projection. It must not append events, invoke workers, admit intent,
run `evaluate_action`, or choose traversal by itself.

**A13. Replayability**

Every closure decision and next-action selection must be reproducible from:

```text
RuntimeEventLog
+ execution basis
+ ABG event-log-backed IntentLineage
+ ProductAssetModel publication basis and its event refs
+ selected Product outcome identity and admitted bounded-basis refs
+ GapPressureRow
+ TargetObligationBinding
+ ActionCatalog
+ admitted evidence
+ EdgeFulfillmentLedger
+ EdgeClosureDecision
+ NextActionBasis
+ visible policy refs
```

If replay cannot reproduce the decision, the implementation has created hidden
state.

**A13a. Causal Chain Integrity**

Each governing admitted or replay-derived carrier and projection in the loop
must reference its causal predecessor refs:

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> NextActionProjection (selected_action)
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionBasis
-> NextActionProjection (next)
```

The target binding must be reachable from the exact selected Product outcome
and any admitted bounded-basis refs. The first `NextActionProjection` in the
chain carries the selected action that admits `ConstructionIntent`, which
preserves those authority refs. The second `NextActionProjection` is the
post-action projection produced from `NextActionBasis` plus fresh `eval_gap`
truth. Both must be reachable from their predecessor refs.

A13 requires that the decision can be reproduced from the inputs. A13a
requires that each governing carrier or projection carry the predecessor refs
that make reproduction reachable without external joins. A broken predecessor
chain is non-replayable at the carrier level and therefore fails A13.

**A14. Recursive Published Refinement**

The homeostasis loop recurses over published refinement.

If a graph function refines an outer vector into published inner vectors, each
inner vector boundary obeys `synthesize_model`, `eval_gap`, `evaluate_next`, and
`evaluate_action` with its own visible model, gap, binding, action, evidence,
ledger, closure, and next-action projection.

If the inner realization is intentionally opaque, it is ordinary implementation
inside one bounded action. It may use local control flow to compute the action's
internal result, but it must not publish, dispatch, retry, repair, re-enter, or
close graph work as a hidden traversal controller. Once a refinement is
published as graph structure, it is governed by the loop recursively.

**A15. Method Ownership**

ABG owns runtime truth, event replay, graph-call lifecycle, actor/process
supervision, continuation, and re-entry mechanics. The product owns domain asset
meaning, graph-function catalog meaning, gap interpretation, and priority
policy. Design Module Method governs realization modules inside that split; it
must not fragment `eval_gap`, `evaluate_next`, or `evaluate_action` into
module-local decision authorities.

**A16. Constitutional Override**

For any ticket, design, code module, or proof that touches `synthesize_model`,
`eval_gap`, `evaluate_next`, `evaluate_action`, traversal, gap evaluation,
action selection, construction intent, worker invocation, evidence admission,
fulfillment, liveness, closure, re-entry, public query, or live proof, the
causally applicable members of this axiom set and the constitutional equation
are the controlling acceptance constraints for the selected Product outcome
and affected published boundary. Unchanged accepted relations cite their
accepted basis rather than being re-proven. The axiom family does not authorize
horizontal realization growth, create Product work, or widen the selected
outcome.

Ticket-local closure wording, test names, source-grep checks, compact CLI
summaries, or implementation notes cannot weaken the constitutional loop. If a
ticket appears complete by its local checklist but leaves a rival traversal
consequence path, the ticket is not constitutionally complete. The lawful
result is to request lawful re-entry, keep the gap as a closure blocker, or
admit separately bounded paydown under an independently selected Product
outcome or prerequisite basis.

The following artifacts may provide evidence, diagnostics, or read-model
context only. They must not independently close an edge, select a next action,
or route retry, repair, or re-entry:

```text
gap dossier
postflight report
assurance report
materialization manifest
runtime liveness projection
run summary
worker prose
screen or PTY transcript
prompt package
harness target argument
source-grep test
CLI branch or compact output
public query or gaps view
service method output
```

If any of those artifacts conflict with the admitted `EdgeFulfillmentLedger`,
`EdgeClosureDecision`, or `NextActionProjection`, the ledger, decision, and
projection chain wins. If that chain is absent, the edge has not
constitutionally closed and the next action has not been constitutionally
selected.

The constitutional equation is:

```text
let U = (selected_product_outcome_ref, optional_admitted_bounded_basis_ref)
let L = project_intent_lineage_from_event_log(source_intent_refs, prior_intent_refs)
let M0 = synthesize_model(L, prior_model, admitted_product_truth)
let G0 = eval_gap(M0, RuntimeEventLog, RuntimeProjection, Worksite)
let O = G0.observation
let B0 = bind(U, G0.pressures, ActionCatalog, target obligations)
let Q0 = initial_selection(L, M0)
let N0 = evaluate_next(Q0, G0, B0, ActionCatalog, Policy)
let I = admit_construction_intent(L, B0, N0.selected_action, N0.next_action_projection)
let E = admit_evidence(invoke(I))
let A = evaluate_action(I, E, B0, Policy)
let M1 = synthesize_model(L, M0, admitted_product_truth)
let G1 = eval_gap(M1, RuntimeEventLog, RuntimeProjection, Worksite)
let B1 = bind(U, G1.pressures, ActionCatalog, target obligations)
let Q1 = next_action_basis_from(A.decision)
let N1 = evaluate_next(Q1, G1, B1, ActionCatalog, Policy)

return N1
```

Where:

```text
A.ledger = EdgeFulfillmentLedger
A.decision = EdgeClosureDecision
A.decision.disposition in {close, yield, retry, repair, re-enter, reprice, block}
Q0.kind = initial_selection
Q1.kind in {
  post_yield_resume,
  post_close_graph_continuation,
  post_retry,
  post_repair,
  post_reenter,
  post_reprice,
  post_block
}
Q1.kind = post_reprice and no separately admitted constitutional basis
  => N1 = typed no-action pending re-entry
```

The implementation is correct only when the next work decision is derived from
that equation, `U` remains causally reachable through the target binding and
construction intent, and no other path can decide what work happens next.
```

Successor, `ODD.md#115d-constructive-evaluation-and-yield-loop`:

```text
### 11.5D Constructive evaluation and yield loop

Every ODD product over GTL/ABG must preserve one constructive evaluation
loop running from intent lineage and model synthesis through observation
to the next lawful action. This is the profile's homeostasis loop, and
its constitutional surface names the operative functions directly:
`synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action`
(P2, P5, P6). The loop is this profile's binding of
[ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation):
it corrects towards the required conditions as observations arrive,
guarantees neither convergence nor the adequacy of those conditions, and
its diagnoses distinguish the four causes named there (P2, P6).

The selected Product outcome under STDO-UP-013
([SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation)) is external
authority for this loop. Product models, gaps, assurance, ledgers and
projections may interpret that outcome but cannot author, select or
enlarge it. `evaluate_next` may select material work only within that
outcome or within an admitted bounded prerequisite or experiment. Graph or
edge closure is evidence toward Product acceptance and is neither Product
nor release acceptance (P2, P6).

The loop selects no further material work without another admitted basis
once the selected outcome is accepted; an admitted prerequisite is
discharged; an admitted experiment's stated decision is resolved; another
admitted terminal condition is reached; or its governing basis or bound
is exhausted, rejected, withdrawn, superseded, repriced away or
falsified. A `reprice` disposition requests lawful constitutional
re-entry; it neither performs the reprice nor selects the successor
outcome (P2, P6).

The loop is framework-independent. Implementations may use other carrier
names but must keep this authority shape (P6, P4a):

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

The objects have these meanings (P3, P6):

| Object | Definition | Authority |
| --- | --- | --- |
| `IntentLineage` | Admitted source intent and its lineage refs: human, imported source, prior product, intent engine, or prior synthesized construction intent. | ABG event-log truth over source intent. It seeds the product model and must not invent graph actions. |
| `ProductAssetModel` | Desired and known typed asset model synthesized from intent lineage, prior model, and admitted product truth. | Product-owned model truth whose publication basis is carried by admitted events and product-owned projection refs. It is not runtime fact or action authority. |
| `Worksite` | Current workspace, runtime archive, transform assets, product asset root, profile, and observed file or process state. | Observable substrate, not authority by itself. |
| `RuntimeEventLog` | Append-only admitted runtime facts. | ABG runtime truth. |
| `RuntimeProjection` | Replay-derived current runtime state over event log and execution basis. | ABG projection truth. |
| `ObservationSnapshot` | Read-only view of runtime truth plus worksite facts relevant to construction. | ABG evaluator carrier with product domain rows. |
| `GapPressureRow` | Typed pressure over missing, partial, blocked, waiting, or ambiguous assets and evidence. | Product domain meaning over admitted observation. |
| `TargetObligationBinding` | Exact binding from gap pressure to the selected Product outcome, any admitted prerequisite or experiment basis, target assets, required roles, evidence refs, and admissible graph outcomes. | Product domain binding over GTL/ABG action authority. |
| `ActionCatalog` | Published lawful graph actions: graph functions, vectors, targets, inputs, and eligible outcomes. | GTL/product publication consumed by ABG. |
| `NextActionBasis` | Sum type naming why `evaluate_next` is being called: `initial_selection`, `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. `post_reprice` records a re-entry request and carries no action-selection authority. | Dispatch basis for next-action evaluation. It is not a separate controller. |
| `PriorityProjection` | Deterministic ranking over bound lawful actions under visible policy. | ABG evaluator kernel plus product policy. |
| `ConstructionIntent` | Admitted selected action for one bounded graph invocation, preserving the selected outcome or admitted bounded-basis refs carried by its target binding. | ABG admission and traversal authority. |
| `AdmittedEvidence` | Admitted worker, process, product, execution, materialization, liveness, and postflight evidence. | ABG/product admission, not worker self-closure. |
| `EdgeFulfillmentLedger` | Evidence and convergence carrier for one edge attempt or version. | Closure evidence truth. |
| `EdgeClosureDecision` | Sum type over the ledger: close, yield, retry, repair, re-enter, reprice, block. | Closure decision truth. |
| `NextActionProjection` | Read model that observes `NextActionBasis` plus current truth and selects a next graph action only when lawful. | ABG next-action evaluation projection with product policy. |

The loop has one model-synthesis function and three distinct evaluation
functions. They may share underlying libraries; they must not share
authority (P6):

| Function | Inputs | Output | Boundary |
| --- | --- | --- | --- |
| `synthesize_model` | `IntentLineage + prior ProductAssetModel + admitted product truth` | `ProductAssetModel` | Model synthesis. It may update desired and known typed asset truth. It must not observe the worksite, select work, invoke work, or close work. |
| `eval_gap` | `ProductAssetModel + RuntimeEventLog + RuntimeProjection + Worksite` | `ObservationSnapshot + GapPressureRow` | Read-only gap discovery. It compares desired model truth to observed reality and emits missing, partial, blocked, waiting, or ambiguous asset pressure. It does not choose work and does not close work. |
| `evaluate_next` | `NextActionBasis + fresh eval_gap + TargetObligationBinding + ActionCatalog + Policy` | `PriorityProjection + NextActionProjection + selected_action` | Next-action selection. `TargetObligationBinding` carries the exact selected Product outcome and any admitted bounded-basis refs. `NextActionBasis` is either `initial_selection(IntentLineage, ProductAssetModel)` or one explicit post-action basis derived from an `EdgeClosureDecision`: `post_yield_resume`, `post_close_graph_continuation`, `post_retry`, `post_repair`, `post_reenter`, `post_reprice`, or `post_block`. Except for unresolved `post_reprice`, which returns typed no-action pending separately admitted constitutional authority, it may select only published lawful graph actions that bind to the gap and governing basis. It does not admit construction intent and does not evaluate the result of an action. |
| `evaluate_action` | `ConstructionIntent + AdmittedEvidence + TargetObligationBinding + Policy` | `EdgeFulfillmentLedger + EdgeClosureDecision` | Action-result evaluation. It decides close, yield, retry, repair, re-enter, reprice, or block for the action just taken. It does not choose the next graph action. |

The word evaluator is not sufficient by itself. A design, ticket, code
module or proof must name which function it implements or consumes:
`synthesize_model`, `eval_gap`, `evaluate_next` or `evaluate_action`
(P6, P3).

Intent has lineage through the loop. Bootstrap or external intent may come
from a human, an imported source, a prior product or an intent engine;
that intent seeds the product asset model that `eval_gap` uses. Current
construction intent is synthesised against that model and the observed
gap, then admitted by a distinct admission step after `evaluate_next`
selects a published graph action. Intent does not invent unpublished
actions: gap-derived action selection supplies the selected action basis
for admitting current construction intent over an already-published graph
function or vector. `ConstructionIntent` must cite the lineage, the
selected action and the `TargetObligationBinding` that preserve the exact
selected Product outcome and any admitted bounded-basis refs (P4b, P6).

The loop is governed by the axioms A0 to A16, each a labelled paragraph
below (P6).

A0 One surface. There is one authoritative computational surface for
traversal consequence (P6, P3):

```text
IntentLineage
-> ProductAssetModel
-> ObservationSnapshot
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionProjection
```

No CLI branch, prompt prose, postflight string, gap-dossier action list,
query projection, service method or local operator summary may become a
rival source of traversal truth (P6).

A1 Worksite is observed, not trusted. The file system, process output,
screen logs, worker artifacts and product files are observations. They
become authority only after admission into typed evidence and their fold
into ledger and decision truth (P6, P3).

A1a Workspace-ledger governed work pair. The worksite or workspace and the
ledger form the governed work pair (P3, P4b):

```text
W = mutable workspace under construction
L = immutable governed ledger of work over W
E = immutable event log / replay spine
Ev = evaluator work over L
```

The workspace is where F_P construction happens. The ledger is the
immutable governed account of closure-relevant work over that workspace;
it is not a copy of the workspace but the admitted trace of callout basis,
observed deltas, file refs, digests, execution evidence, obligations
touched, claims made, evaluator inputs, evaluator outputs and admission
status. The loop is (P3, P6):

```text
F_P acts in W.
Admission records governed facts in L.
E orders and anchors L entries with predecessor refs.
Ev evaluates a declared L snapshot, not ambient W.
Ev output is itself F_P work and is admitted back into L/E.
L/E constrain the next lawful F_P action in W.
```

The consistency rule is (P3, P6):

```text
W can change without being true.
L can be true without being the whole W.
Closure can only use W through L.
Eval can only judge W through L.
Eval only affects traversal after its own L/E admission.
```

Every closure-relevant F_P callout that does work needs ledger admission.
Evaluator work is not outside F_P merely because it reads ledgers: it is
F_P work over governed ledger state, and its result must be admitted into
the immutable ledger and event spine before it can affect closure, routing
or traversal. Corrections append or supersede ledger and event facts; they
do not rewrite the governed history of work (P4b, P6, P3).

A1b Ledger is governed attention. A ledger is the system's governed
attention over construction history. This is a structural analogy and not
an implementation dependency on transformer attention: model attention
selects from context through learned weights, while ODD ledger attention
is typed, immutable, lineage-constrained, policy-bounded and replayable.
An evaluator may attend only to admitted ledger rows reachable through
declared lineage, predecessor refs, target binding, policy and the
relevant event-log cursor. Workspace facts, worker prose, archives,
summaries and controller memory outside that reachable ledger set lie
outside the evaluator's lawful attention surface. Lineage is therefore
not only provenance bookkeeping: it is the attention graph that decides
which evidence the evaluator may see, what it must ignore, and which
predecessor chain makes the judgment reproducible (P0, P6, P3).

A2 Exact target binding. Every constructive action must bind the current
gap to exact target assets and obligations before invocation (P2, P3):

```text
selected Product outcome ref
+ optional admitted prerequisite or experiment basis ref
+ gap pressure + target assets + required roles + evidence refs
-> TargetObligationBinding
```

A broad edge cannot satisfy a specific product or evidence gap unless the
binding proves that edge is the lawful action for those exact assets
(P2).

A3 Published action law. `evaluate_next` may rank only published lawful
actions from the action catalogue. If the desired action is unpublished,
the lawful result is a typed no-action disposition, not a fallback to a
broad executive graph or a local script (P6, P5).

A4 `evaluate_next` totality. `evaluate_next` must be total. On
`initial_selection` it selects from the current model, current gap, target
binding, catalogue and policy. On `post_yield_resume` it resumes or yields
the same edge from replay-visible resume truth without classifying the
action as failure. On `post_close_graph_continuation` it may select the
next graph edge after the current edge closed, or no action when the graph
is complete. On `post_retry`, `post_repair`, `post_reenter` and
`post_block` it follows this rule (P5, P6):

```text
if higher-priority lawful action exists:
  select it
else if current graph edge remains lawful:
  follow the graph
else if authority is missing:
  reprice or block
else:
  block with typed no-action disposition
```

On `post_reprice`, `evaluate_next` must return a typed no-action
disposition while constitutional re-entry stays unresolved. The reprice
decision cannot authorise a replacement action; work may be evaluated
again only after lawful re-entry separately admits an exact selected
Product outcome or bounded basis and supplies it through a new
`initial_selection` or a basis-bearing resume. Default graph following is
ordinary, but it is still an `evaluate_next` decision and not hidden
sequential control (P5, P2, P6).

Selection is not a result of the core. `evaluate_next`'s selection, a
typed no-action disposition included, selects what is invoked next and is
not a value of the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results); it maps to no core
value. The closure decision it follows, where there is one, carries the
core value, as mapped under A8 below, and selection stays invocational
(A11) (P5, P6).

A4a Evaluation function separation. `synthesize_model`, `eval_gap`,
`evaluate_next` and `evaluate_action` are separate authority functions.
`synthesize_model` may synthesise the current product asset model from
event-log-backed intent lineage, prior model and admitted product truth
only; it must not observe the worksite, admit construction intent, invoke
work, close work or select the next action. `eval_gap` may emit
observation and gap pressure only; it must not admit construction intent,
invoke work, close work or select the next action. `evaluate_action` may
fold admitted action evidence into ledger and closure decision only; it
must not select the next graph action. `evaluate_next` may bind target
obligations, rank lawful published actions and publish the next-action
projection; it must not admit construction intent or decide whether the
prior action closed, yielded, failed or needs repair except by consuming
the admitted `EdgeClosureDecision`. A module that lets one of these
functions exercise another's authority creates a rival control surface
and violates A0 (P6).

A5 F_P freedom, F_D authority. F_P may inspect, discover, reason, draft,
transform and propose within the bounded action. F_P must not close the
edge, emit runtime events, mutate ledgers or decide re-entry. F_D, ABG and
product admission own durable evidence and closure truth (P0, P6). An F_P
worker must not be given an F_D-authored semantic extraction recipe when
the edge requires F_P judgment (P0, P6; provenance rc.2
authority_compressions/design_module_method.compressed.md, a claim no
rc.2 body states).

A6 Evidence before closure. No edge closes from raw artifact presence, a
raw worker report, raw process success or a CLI summary. Closure is a fold
over admitted evidence (P6):

```text
AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
```

A7 Ledger is evidence, not action selector. `EdgeFulfillmentLedger`
records evidence and convergence (P6, P3):

```text
counts
obligation rows
materialization refs
liveness refs
admission refs
edge_converged
```

It does not select the next action. Action selection belongs to
`evaluate_next` over `EdgeClosureDecision` plus fresh `eval_gap` truth
(P6).

A8 Closure decision is a sum type. The closure decision vocabulary is
closed (P5, P6):

```text
close
yield
retry
repair
re-enter
reprice
block
```

Each disposition is replay-visible and must carry basis and reason refs
sufficient to reproduce the decision (P5, P6).

Mapping of the closure decision to the core result algebra, new in this
corpus. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
every outcome in the core or in a refinement that maps each refined value
to exactly one core value and adds no core value. Material relation: a
composite over the edge joins each closure decision as one core value, so
a failure, an undecided closure and a needed re-entry stay distinct (P5,
P6). The closure decision is `evaluate_action`'s result over admitted
evidence, mapped for the predicate "the edge's obligations are fulfilled
on the exact basis". The bounded action it judges has its own step result
under [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
for "a candidate is available", and neither value counts toward the
other's predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Each decision keeps its own vocabulary and its basis and reason refs
beside its core value (P5, P6).

Refined by cause. Where a decision would map to one of two core values
according to its cause, the cause is part of the refined value, written
in parentheses as in `re-enter(basis)`, and each refined value maps once
(FOUNDATIONS §4 Results, Refinements). The cause is read from the
decision's basis and reason refs, which A8 requires to be sufficient to
reproduce it. The seven decisions of A8 stay the closed vocabulary; a
refined value names a decision and its cause and adds no decision (P5,
P6). The causes are:

- `retry(defeated)`: admissible evidence defeats the edge for this attempt
  while the same action stays lawful; `retry(undecided)`: every other
  retry, as after a liveness interruption, which alone never gives
  `retry(defeated)` (A10).
- `repair(implementation)` and `repair(proof)`: the edge's governing
  relation, basis and target binding stay coherent, and a local defect,
  in the implementation or in its proof, keeps the edge from closing, so
  a repair of the same edge is the lawful next action (A11).
  `repair(implementation)`: admitted evidence shows the implementation
  failing an edge obligation; `repair(proof)`: every other repair, the
  defect being in the proof.
- `re-enter(undeclared)` and `block(undeclared)`: the cause is a relation,
  capability or authority that no admitted basis declares;
  `re-enter(basis)` and `block(basis)`: every other cause, the current
  basis being unable to support the edge, as when it is stale, substituted
  or unrepairable. A decision with both causes records both and takes the
  `basis` value, as
  [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
  decides for `re_entry_requested`.

| Decision | Core value | Ground |
|---|---|---|
| `close` | satisfied | the ledger's admitted evidence fulfils the edge's obligations on the exact basis |
| `yield` | indeterminate | the edge stays lawful and the admitted evidence, progress or a waiting state, does not yet decide its obligations; the replay-visible resume basis names what would decide; no failure is classified, as A9 requires |
| `retry(defeated)` | falsified | the evidence that defeats the edge for this attempt is the counterexample; A9 separates this failure-classified re-attempt from yield |
| `retry(undecided)` | indeterminate | the attempt ended without evidence that decides the edge's obligations; the decision's reason refs name the re-attempt that would decide |
| `repair(implementation)` | falsified | the failing obligation row is the counterexample (P5, P6) |
| `repair(proof)` | indeterminate | the defect is in the proof, so the admitted evidence cannot decide the obligation; the decision's reason refs name the repaired proof that would decide (P5, P6) |
| `re-enter(undeclared)` | out_of_frame | the edge cannot close on its current basis because an upstream asset or governing relation must change, and the change needs a relation, capability or authority that no admitted basis declares; the decision names it and its owner |
| `re-enter(basis)` | invalid_basis | the edge cannot close on its current basis because an upstream asset or governing relation must change, and that basis cannot support the edge |
| `reprice` | out_of_frame | further work needs a selected outcome or bound that no admitted basis declares; the decision names it, its owner and the constitutional re-entry it requests, which is the reconfiguration pressure of out_of_frame ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or indeterminate) |
| `block(undeclared)` | out_of_frame | `evaluate_action` decides that the action just taken leaves the edge unable to proceed, because it needs a relation, capability or authority that no admitted basis declares |
| `block(basis)` | invalid_basis | `evaluate_action` decides that the action just taken leaves the edge unable to proceed on its current basis, which cannot support it |

Closure decisions and dispositions. The closure decisions of A8 and their
refined values are this member's, and they answer the edge predicate
above. The dispositions `accept`, `local_repair`, `re_enter` and `reject`
are owned by [ACTIVATION §3 Disposition](ACTIVATION.md#disposition) and
answer another predicate, "the candidate is accepted at its declared
boundary". A closure decision is not a disposition and is never recorded
as one, and no disposition is a closure decision: `repair` is not
`local_repair`, and `re-enter` is not `re_enter`. Edge closure is
evidence toward acceptance and never acceptance itself (the
selected-outcome paragraphs above). Their core values differ because their
predicates differ. `repair(proof)` is `indeterminate`, because a
defective proof leaves the edge's obligations undecided, while
`local_repair` is `falsified`, because the local defect defeats
acceptance of the candidate. `re-enter(undeclared)` is `out_of_frame`,
because the change needs a relation, capability or authority that no
admitted basis declares, while `re_enter` is `invalid_basis`. Neither
value counts toward the other's predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
In §11.5D, §16 and §19 "disposition" names a closure decision (the
selected-outcome paragraphs, A8, A11, the constitutional equation, §16
item 13 and §19 question 11) or, in "typed no-action disposition", a
selection of `evaluate_next` (A3, A4); there it never names a disposition
of ACTIVATION §3. The dispositions of §21 are the successor dispositions
of [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
(P1, P5, P6). Purpose and material relation:
a consumer that read an edge's `repair` as `local_repair`, or `re-enter`
as `re_enter`, would take an undecided edge for a defeated candidate, or a
missing declaration for an unsupporting basis; the material relation is
whether a closure decision is combined as an acceptance result.

A9 Yield is lawful iterate. `yield` is the lawful iteration boundary (P5):

```text
same edge or attempt remains lawful
progress or waiting state is admitted
resume basis is replay-visible
control returns without failure classification
```

Yield is not retry, not block, not timeout and not a local CLI loop. It is
the pressure-release state that lets long-running, bounded or partially
productive work return control without losing the current edge (P5, P0).

A10 Liveness does not close semantic truth. Liveness observes activity,
inactivity, process state and interruption. It can support yield or a
liveness interruption; it cannot by itself declare semantic failure,
semantic closure or requirement non-satisfaction (P6).

A11 Re-entry is graph law. Repair and re-entry are graph actions selected
by `evaluate_next` from admitted closure truth and published action
authority, not local retry branches over strings. `evaluate_action` may
emit `repair` or `re-enter` as a closure disposition; `evaluate_next`
selects which published graph action realises that repair or re-entry.
Disposition is conceptual; selection is invocational (P6, P5).

A12 Public query is a read-only evaluation view. A public query or gaps
view may render read-only outputs of `eval_gap`, `evaluate_action` and
`evaluate_next`: gap pressure, closure decision and next-action
projection. It must not append events, invoke workers, admit intent, run
`evaluate_action` or choose traversal by itself (P6, P3).

A13 Replayability. Every closure decision and next-action selection must
be reproducible from (P3, P6):

```text
RuntimeEventLog
+ execution basis
+ ABG event-log-backed IntentLineage
+ ProductAssetModel publication basis and its event refs
+ selected Product outcome identity and admitted bounded-basis refs
+ GapPressureRow
+ TargetObligationBinding
+ ActionCatalog
+ admitted evidence
+ EdgeFulfillmentLedger
+ EdgeClosureDecision
+ NextActionBasis
+ visible policy refs
```

If replay cannot reproduce the decision, the implementation has created
hidden state (P3).

A13a Causal chain integrity. Each governing admitted or replay-derived
carrier and projection in the loop must reference its causal predecessor
refs (P3, P4b):

```text
selected Product outcome and admitted bounded-basis refs
-> TargetObligationBinding

IntentLineage
-> ProductAssetModel
-> GapPressureRow
-> TargetObligationBinding
-> PriorityProjection
-> NextActionProjection (selected_action)
-> ConstructionIntent
-> AdmittedEvidence
-> EdgeFulfillmentLedger
-> EdgeClosureDecision
-> NextActionBasis
-> NextActionProjection (next)
```

The target binding must be reachable from the exact selected Product
outcome and any admitted bounded-basis refs. The first
`NextActionProjection` in the chain carries the selected action that
admits `ConstructionIntent`, which preserves those authority refs. The
second is the post-action projection produced from `NextActionBasis` plus
fresh `eval_gap` truth. Both must be reachable from their predecessor
refs. A13 requires that the decision be reproducible from the inputs;
A13a requires that each governing carrier or projection carry the predecessor refs
that make reproduction reachable without external joins. A broken
predecessor chain is non-replayable at the carrier level and therefore
fails A13 (P3, P4b).

A14 Recursive published refinement. The homeostasis loop recurses over
published refinement. If a graph function refines an outer vector into
published inner vectors, each inner vector boundary obeys
`synthesize_model`, `eval_gap`, `evaluate_next` and `evaluate_action` with
its own visible model, gap, binding, action, evidence, ledger, closure and
next-action projection. An intentionally opaque inner realisation is
ordinary implementation inside one bounded action: it may use local
control flow to compute the action's internal result, but it must not
publish, dispatch, retry, repair, re-enter or close graph work as a hidden
traversal controller. Once a refinement is published as graph structure,
the loop governs it recursively (P4a, P0, P6).

A15 Method ownership. ABG owns runtime truth, event replay, the graph-call
lifecycle, actor and process supervision, continuation, and re-entry
mechanics. The product owns domain asset meaning, graph-function
catalogue meaning, gap interpretation and priority policy. The
software-design profile (DESIGN_MODULE, tier 3; PROFILES §3) governs
realisation modules inside that split and must not fragment `eval_gap`,
`evaluate_next` or `evaluate_action` into module-local decision
authorities (P6).

A16 Constitutional override. For any ticket, design, code module or proof
that touches `synthesize_model`, `eval_gap`, `evaluate_next`,
`evaluate_action`, traversal, gap evaluation, action selection,
construction intent, worker invocation, evidence admission, fulfilment,
liveness, closure, re-entry, public query or live proof, the causally
applicable members of this axiom set and the constitutional equation below
are the controlling acceptance constraints for the selected Product
outcome and the affected published boundary. Unchanged accepted relations
cite their accepted basis and are not proved again. The axiom family
authorises no horizontal realisation growth, creates no Product work and
does not widen the selected outcome (P6, P2).

Ticket-local closure wording, test names, source-grep checks, compact CLI
summaries and implementation notes cannot weaken the constitutional loop.
A ticket that looks complete by its local checklist but leaves a rival
traversal-consequence path is not constitutionally complete; the lawful
result is to request lawful re-entry, keep the gap as a closure blocker,
or admit separately bounded paydown under an independently selected
Product outcome or prerequisite basis (P6, P2).

These artifacts may provide evidence, diagnostics or read-model context
only; they must not independently close an edge, select a next action, or
route retry, repair or re-entry (P6):

```text
gap dossier
postflight report
assurance report
materialization manifest
runtime liveness projection
run summary
worker prose
screen or PTY transcript
prompt package
harness target argument
source-grep test
CLI branch or compact output
public query or gaps view
service method output
```

If any of them conflicts with the admitted `EdgeFulfillmentLedger`,
`EdgeClosureDecision` or `NextActionProjection`, the ledger, decision and
projection chain wins. If that chain is absent, the edge has not
constitutionally closed and the next action has not been constitutionally
selected (P6).

The constitutional equation is (P6, P4a):

```text
let U = (selected_product_outcome_ref, optional_admitted_bounded_basis_ref)
let L = project_intent_lineage_from_event_log(source_intent_refs, prior_intent_refs)
let M0 = synthesize_model(L, prior_model, admitted_product_truth)
let G0 = eval_gap(M0, RuntimeEventLog, RuntimeProjection, Worksite)
let O = G0.observation
let B0 = bind(U, G0.pressures, ActionCatalog, target obligations)
let Q0 = initial_selection(L, M0)
let N0 = evaluate_next(Q0, G0, B0, ActionCatalog, Policy)
let I = admit_construction_intent(L, B0, N0.selected_action, N0.next_action_projection)
let E = admit_evidence(invoke(I))
let A = evaluate_action(I, E, B0, Policy)
let M1 = synthesize_model(L, M0, admitted_product_truth)
let G1 = eval_gap(M1, RuntimeEventLog, RuntimeProjection, Worksite)
let B1 = bind(U, G1.pressures, ActionCatalog, target obligations)
let Q1 = next_action_basis_from(A.decision)
let N1 = evaluate_next(Q1, G1, B1, ActionCatalog, Policy)

return N1
```

where (P5):

```text
A.ledger = EdgeFulfillmentLedger
A.decision = EdgeClosureDecision
A.decision.disposition in {close, yield, retry, repair, re-enter, reprice, block}
Q0.kind = initial_selection
Q1.kind in {
  post_yield_resume,
  post_close_graph_continuation,
  post_retry,
  post_repair,
  post_reenter,
  post_reprice,
  post_block
}
Q1.kind = post_reprice and no separately admitted constitutional basis
  => N1 = typed no-action pending re-entry
```

The implementation is correct only when the next work decision is derived
from that equation, `U` stays causally reachable through the target
binding and the construction intent, and no other path can decide what
work happens next (P6, P2).
```


### Row `ODD_METHOD.md#116-product-specific-semantics-sit-above-the-shared-carrier` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#116-product-specific-semantics-sit-above-the-shared-carrier` at rc.2:

```text
### 11.6 Product-Specific Semantics Sit Above The Shared Carrier

ODD method gives the product shape, not the domain semantics.

That means:

- the same ODD structural law can build many different domain products
- each product defines its own asset meanings, proof lanes, and query overlays

Do not confuse:

- structural GTL law
- product-specific semantic law
```

Successor, `ODD.md#116-product-specific-semantics-sit-above-the-shared-carrier`:

```text
### 11.6 Product-specific semantics sit above the shared carrier

This profile gives the product shape, not the domain semantics. The same
ODD structural law can build many different domain products, and each
product defines its own asset meanings, proof lanes and query overlays.
Structural GTL law and product-specific semantic law are never confused
(P1).
```


### Row `ODD_METHOD.md#117-manual-walkthrough-must-still-be-lawful` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#117-manual-walkthrough-must-still-be-lawful` at rc.2:

```text
### 11.7 Manual Walkthrough Must Still Be Lawful

Automation must remain true for a manual walkthrough.

A human operator, using only the declared authority surfaces, should be able to:

1. identify the current asset state (current typed asset or node)
2. identify the next lawful vector and its public graph-function carrier (vector is the constitutional transition contract; the graph function is the published constructive program that realizes it — see §5.2 and §5.3)
3. determine the required inputs, evaluators, output contract, and carried environment
4. construct or assess the next asset (produced asset or checkpoint)
5. repeat until target-relative closure is reached

Automation may make this faster, safer, or more repeatable. It may not invent a different process.

**Automation is lawful** when it:

- renders prompts
- scaffolds artifacts
- selects the next traversal step
- runs workers
- collects evidence
- assesses closure

**Automation is unlawful** when it:

- skips undeclared nodes
- fabricates authority not present in the declared surfaces
- collapses multiple constitutional transitions into one opaque step without declaring the refinement
- depends on implementation-carrier knowledge that the installed product should not have
- collapses the installed builder and the product under development into one authority surface during self-host work

If the team cannot explain the manual traversal, the automation is not yet method-safe. If automation cannot be explained in these terms, it is ahead of the method.
```

Successor, `ODD.md#117-manual-walkthrough-must-still-be-lawful`:

```text
### 11.7 Manual walkthrough must still be lawful

Automation must stay true for a manual walkthrough. A human operator using
only the declared authority surfaces should be able to (P0, P6):

1. identify the current asset state, the current typed asset or node;
2. identify the next lawful vector and its public graph-function carrier,
   the vector being the constitutional transition contract and the graph
   function the published constructive program that realises it (§5
   Vectors and Graph functions);
3. determine the required inputs, evaluators, output contract and carried
   environment;
4. construct or assess the next asset, a produced asset or checkpoint;
5. repeat until target-relative closure is reached.

Automation may make this faster, safer or more repeatable; it may not
invent a different process. Automation is lawful when it renders prompts,
scaffolds artifacts, selects the next traversal step, runs workers,
collects evidence and assesses closure. Automation is unlawful when it
skips undeclared nodes; fabricates authority absent from the declared
surfaces; collapses several constitutional transitions into one opaque
step without declaring the refinement; depends on implementation-carrier
knowledge the installed product should not have; or collapses the
installed builder and the product under development into one authority
surface during self-host work (P0, P6).

If the team cannot explain the manual traversal, the automation is not yet
method-safe. Automation that cannot be explained in these terms is ahead
of the method (P0, P6).
```


### Row `ODD_METHOD.md#117a-conforming-agentic-development` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#117a-conforming-agentic-development` at rc.2:

```text
### 11.7A Conforming Agentic Development

ODD method is the premise for conforming agentic development over the graph-native worksite. An agentic coder produces governed work by following the constitutional process over a minimal declared authority packet, with the artifacts it produces gated by admission. `SPEC_METHOD.md` governs the general constitutional process and `TICKET_METHOD.md` governs artifact admission; this section names the ODD specialization and composes that law rather than re-declaring it.

Conformance has two halves: an F_P proof that the process is followable, and an F_D gate that admits the produced artifacts.

**The walkthrough is the conformance proof.**

§11.7 requires automation to remain true for a manual walkthrough. The agentic form of that law is a conformance test of the method itself: an agentic coder executes the constitutional process end-to-end on real work — intake triage, smallest lawful re-entry, the spec/requirement/design/ticket chain, the constructive evaluation loop of §11.5D, and closure proof — using only the declared authority surfaces. The agentic coder is F_P over the constitutional process.

The agent works from a minimal declared authority packet, not from memory and not from wholesale hidden context. `SPEC_METHOD.md` already requires declared context — input/output contract, required context, role, evaluator regime, and provenance — for any agentic work unit. The ODD addition is that the packet carries only the smallest declared authority sufficient to decide the step, with its source refs, and that conformance is enforced by admitting the produced artifact rather than by enlarging what the agent must hold. Compression is prompt input, never the deciding authority.

The walkthrough proves at two levels:

- the work it produces must be lawful: correct change-class, traceable, admitted
- a point where the walkthrough cannot proceed is a method defect only when a competent agent, correctly configured and using the declared authority, still cannot decide — ambiguity, a missing step, contradictory authority, or an un-decidable change-class in an owning surface. That defect is repriced into the owning authority surface, the same way a failed manual traversal is a graph defect under §11.7.

An agent that ignored the declared authority, relied on stale memory, or reasoned badly has produced agent error, not a method defect. Admission rejects the malformed artifact either way, so a bad agent turn neither becomes law nor silently indicts the method.

This proof is independent of any automated runtime. A live lane that depends on external execution conditions — an overloaded model API, a flaky transport — cannot prove the constitutional process is sound, because it conflates process validity with runtime availability. The walkthrough proves the process; the runtime only executes it.

**The validator is the conformance gate.**

The constitutional process is an interface contract, and interface conformance is enforced by validating artifacts against the contract, not by the conformer holding the contract.

ODD does not re-declare the artifact rules. Tickets, change-class declarations, design-module derivations, and execution contracts are admitted under `SPEC_METHOD.md` and `TICKET_METHOD.md`, which already require that a drafted classification be admitted or rejected against deterministic criteria rather than taken as automatic truth. ODD requires only that agentic development pass through that admission: the agentic coder produces the artifact; the declared admission gates it deterministically, fail-closed, naming the violated rule — exactly as a typed asset is enforced by its constructor (§11.1).

This preserves the F_P/F_D split at the method layer. The agentic coder is F_P: it reasons, drafts, and proposes within the declared packet. Admission is F_D: it decides whether the produced artifact conforms. The walkthrough establishes that the process is followable; admission establishes that each act of following it conforms.

**Conformance is not approval-by-usage.**

A passed admission and a completed walkthrough are conformance evidence, not ratification. Shared method change still follows §9: grey work is not made constitutional by repeated agentic execution. The agentic coder conforms to the method; it does not amend the method by acting.
```

Successor, `ODD.md#117a-conforming-agentic-development`:

```text
### 11.7A Conforming agentic development

This profile is the premise for conforming agentic development over the
graph-native worksite. An agentic coder produces governed work by
following the constitutional process over a minimal declared authority
packet, and admission gates the artifacts it produces. SPEC_METHOD governs
the general constitutional process and [TICKETS](TICKETS.md) governs
artifact admission; this section names the ODD specialisation and composes
that law without declaring it again (P6, P0).

Conformance has two halves: an F_P proof that the process can be followed,
and an F_D gate that admits the produced artifacts (P6).

The walkthrough is the conformance proof. §11.7 requires automation to
stay true for a manual walkthrough; its agentic form is a conformance test
of the method itself. An agentic coder executes the constitutional process
end to end on real work, using only the declared authority surfaces:
intake triage, the smallest lawful re-entry, the specification,
requirement, design and ticket chain, the constructive evaluation loop of
§11.5D, and closure proof. The agentic coder is F_P over the
constitutional process (P0, P6).

The agent works from a minimal declared authority packet, not from memory
and not from wholesale hidden context. The general method already requires
declared context for any agentic work unit: input and output contract,
required context, role, evaluator regime and provenance (SPEC_METHOD;
[ACTIVATION §1](ACTIVATION.md#1-the-step)). The ODD addition is that the
packet carries only the smallest declared authority sufficient to decide
the step, with its source refs, and that conformance is enforced by
admitting the produced artifact rather than by enlarging what the agent
must hold. Compression is prompt input and never the deciding authority
(P0, P6). What a derived surface may decide is owned by
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Acquisition and Standalone scope; this section adds only the ODD limit
that follows. A derived surface or projected frame of the general method may
orient the agent to source precedence, lawful re-entry and traceability;
it must not be used to decide product-specific behaviour, which must come
from the current product authority packet (P6, P1; provenance rc.2
authority_compressions/spec_method.compressed.md, a claim no rc.2 body
states).

The walkthrough proves at two levels. The work it produces must be lawful:
correct change class, traceable, admitted. A point where the walkthrough
cannot proceed is a method defect only when a competent agent, correctly
configured and using the declared authority, still cannot decide because
of ambiguity, a missing step, contradictory authority or an undecidable
change class in an owning surface. That defect is repriced into the owning
authority surface, as a failed manual traversal is a graph defect under
§11.7 (P6, P5).

An agent that ignored the declared authority, relied on stale memory or
reasoned badly has produced agent error, not a method defect. Admission
rejects the malformed artifact either way, so a bad agent turn neither
becomes law nor silently indicts the method (P6).

This proof is independent of any automated runtime. A live lane that
depends on external execution conditions, such as an overloaded model API
or a flaky transport, cannot prove the constitutional process sound,
because it conflates process validity with runtime availability. The
walkthrough proves the process; the runtime only executes it (P6, P5).

The validator is the conformance gate. The constitutional process is an
interface contract, and interface conformance is enforced by validating
artifacts against the contract, not by the conformer holding the contract.
This profile does not declare the artifact rules again: tickets,
change-class declarations, design-module derivations and execution
contracts are admitted under SPEC_METHOD and TICKETS, which already require
a drafted classification to be admitted or rejected against deterministic
criteria rather than taken as automatic truth. This profile requires only
that agentic development pass through that admission. The agentic coder
produces the artifact; the declared admission gates it deterministically,
fail-closed and naming the violated rule, exactly as a typed asset is
enforced by its constructor (§11.1) (P6, P3).

This keeps the F_P and F_D split at the method layer. The agentic coder is
F_P: it reasons, drafts and proposes within the declared packet. Admission
is F_D: it decides whether the produced artifact conforms. The walkthrough
establishes that the process can be followed; admission establishes that
each act of following it conforms (P6, P0).

Conformance is not approval by usage. A passed admission and a completed
walkthrough are conformance evidence, not ratification. Shared method
change still follows §9: repeated agentic execution does not make grey
work constitutional. The agentic coder conforms to the method; it does not
amend the method by acting (P6).
```


### Row `ODD_METHOD.md#117b-real-authority-path-negative-proof-stdo-up-010` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#117b-real-authority-path-negative-proof-stdo-up-010` at rc.2:

```text
### 11.7B Real Authority-Path Negative Proof (`STDO-UP-010`)

Negative proof for an ODD or graph-native boundary exercises the supported
Product authority path. It must not manufacture the refusal state, blocked
event, gap, or verdict that the system is supposed to derive.

Closure-grade negative evidence identifies the supported entry and governing
authority, invalidates the real authority-bearing input, exercises the
supported path, proves refusal before the prohibited effect, and establishes
that no legacy, fallback, reconstruction, or parallel path succeeds. Source,
packaged, installed, and runtime absence are distinct claims.

Where these identities apply, the supported relation is:

```text
public entry
  -> admitted GTL composition owns traversal topology
  -> named GraphFunction supplies the callable work contract
  -> implementation or plugin binding realizes only its admitted seam
  -> ABG owns traversal, event, continuation, and replay truth
  -> replay-derived projection
  -> typed Product outcome or continuation
```

No CLI, SDK, service, adapter, plugin, fixture, query, or projection may become
a rival traversal controller. The consumer owns the concrete test and evidence
mechanism; this section owns the property that mechanism must prove.
```

Successor, `ODD.md#117b-real-authority-path-negative-proof-stdo-up-010`:

```text
### 11.7B Real authority-path negative proof (STDO-UP-010)

Negative proof for an ODD or graph-native boundary exercises the supported
Product authority path. It must not manufacture the refusal state, blocked
event, gap or verdict that the system is supposed to derive (P6, P5;
provenance rc.2 #117b-real-authority-path-negative-proof-stdo-up-010).

Closure-grade negative evidence identifies the supported entry and the
governing authority; invalidates the real authority-bearing input;
exercises the supported path; proves refusal before the prohibited
effect; and establishes that no legacy, fallback, reconstruction or
parallel path succeeds. Source, packaged, installed and runtime absence
are distinct claims (P6, P3).

Where these identities apply, the supported relation is (P6, P4a):

```text
public entry
  -> admitted GTL composition owns traversal topology
  -> named GraphFunction supplies the callable work contract
  -> implementation or plugin binding realizes only its admitted seam
  -> ABG owns traversal, event, continuation, and replay truth
  -> replay-derived projection
  -> typed Product outcome or continuation
```

No CLI, SDK, service, adapter, plugin, fixture, query or projection may
become a rival traversal controller. The consumer owns the concrete test
and evidence mechanism; this section owns the property that mechanism
must prove (P6).
```


### Row `ODD_METHOD.md#118-cumulative-environment-law-is-mandatory` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#118-cumulative-environment-law-is-mandatory` at rc.2:

```text
### 11.8 Cumulative Environment Law Is Mandatory

Do not model composition as "the last output feeds the next input".

The real ODD law is cumulative typed environment.

Each retained `GraphFunction` should declare:

- `environment.requires`
- `environment.provides`
- `environment.carries`

Later functions may require any typed binding available in the cumulative carried environment, not only the immediately previous output.

If a product publishes graph functions without this cumulative environment law, the line is graph-shaped but structurally wrong.
```

Successor, `ODD.md#118-cumulative-environment-law-is-mandatory`:

```text
### 11.8 Cumulative environment law is mandatory

Composition is not modelled as "the last output feeds the next input".
The ODD law is a cumulative typed environment (P4a, P4b).

Each retained `GraphFunction` should declare `environment.requires`,
`environment.provides` and `environment.carries`. A later function may
require any typed binding available in the cumulative carried
environment, not only the immediately previous output (P4a, P4b).

A product that publishes graph functions without this cumulative
environment law has a line that is graph-shaped but structurally wrong
(P4a, P6).
```


### Row `ODD_METHOD.md#119-global-convergence-must-be-stable-under-zoom` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#119-global-convergence-must-be-stable-under-zoom` at rc.2:

```text
### 11.9 Global Convergence Must Be Stable Under Zoom

Local green arcs are not enough.

If an outer public carrier is refined into inner executable structure, then:

- the refined inner chain must close lawfully
- the enclosing coarse contract must also remain true after fold-back
- zoomed and unzoomed views must agree on whether the enclosing carrier is open or closed

For current product closure, live current requirements that lack an executable proof witness keep the enclosing carrier open until they are:

- realized
- explicitly deferred
- explicitly repriced out of the active branch

For the active software line, the immediate pressure is usually realized testcase or archived test evidence, but the governing law is proof-lane aware: the witness must be a governed realized proof surface appropriate to the requirement class.

---
```

Successor, `ODD.md#119-global-convergence-must-be-stable-under-zoom`:

```text
### 11.9 Global convergence must be stable under zoom

Local green arcs are not enough. When an outer public carrier is refined
into inner executable structure, the refined inner chain must close
lawfully; the enclosing coarse contract must also stay true after
fold-back; and zoomed and unzoomed views must agree on whether the
enclosing carrier is open or closed (P4a, P2).

For current product closure, live current requirements that lack an
executable proof witness keep the enclosing carrier open until they are
realised, explicitly deferred, or explicitly repriced out of the active
branch. For the active software line the immediate pressure is usually a
realised testcase or archived test evidence, but the governing law is
proof-lane aware: the witness must be a governed realised proof surface
appropriate to the requirement class (P2, P6).
```


### Row `ODD_METHOD.md#12-scenario-rule` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#12-scenario-rule` at rc.2:

```text
## 12. Scenario Rule

Scenarios are graph-native proving surfaces.

They are not only test documentation.

A scenario bundle should make clear:

- which feature or use-case boundary is being exercised
- which assets are expected to exist before the scenario starts
- which vectors are expected to be traversed
- which significant paths are expected to be exercised
- what evidence closes the scenario

The best proving paths come from declared scenarios and use cases because they pressure both feature intent and design decisions.

That makes them the best source for selecting the significant code and control paths the system must exercise.

---
```

Successor, `ODD.md#12-scenario-rule`:

```text
## 12. Scenario rule

Scenarios are graph-native proving surfaces, not only test
documentation. A scenario bundle should make clear which feature or
use-case boundary is exercised; which assets are expected to exist before
the scenario starts; which vectors are expected to be traversed; which
significant paths are expected to be exercised; and what evidence closes
the scenario (P2, P6).

The best proving paths come from declared scenarios and use cases,
because they pressure both feature intent and design decisions. That makes
them the best source for selecting the significant code and control paths
the system must exercise (P2).
```


### Row `ODD_METHOD.md#13-installed-dev-rule` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#13-installed-dev-rule` at rc.2:

```text
## 13. Installed-Dev Rule

Where the product has an installable development form, decisive proof runs against that installed development form in an isolated environment.

For a graph-native ODD product, this means the proving lane should exercise:

1. install
2. project bootstrap
3. graph traversal
4. evidence collection
5. target-relative closure

Direct source checks remain useful. They do not replace installed-dev proof.

---
```

Successor, `ODD.md#13-installed-dev-rule`:

```text
## 13. Installed-dev rule

Where the product has an installable development form, decisive proof
runs against that installed development form in an isolated environment.
For a graph-native ODD product the proving lane should exercise install,
project bootstrap, graph traversal, evidence collection and
target-relative closure. Direct source checks stay useful and do not
replace installed-dev proof (P6, P3). This rule is the profile's binding of
[ASSURANCE §5 Installed dev proof](ASSURANCE.md#5-installed-dev-proof), which
owns it.
```


### Row `ODD_METHOD.md#14-dogfooding-rule` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#14-dogfooding-rule` at rc.2:

```text
## 14. Dogfooding Rule

The product should be developed through the same graph-native method it claims to provide.

Where the product provides ODD framework behavior, it must build that behavior
through ODD graph functions. It must not merely publish ODD-shaped artifacts
after imperative execution has already decided the work.

That means the project should increasingly describe and build itself through:

- explicit assets
- explicit vectors
- explicit graph functions
- explicit scenario bundles
- explicit target-relative closure

The method is stronger when the product can walk itself.

---
```

Successor, `ODD.md#14-dogfooding-rule`:

```text
## 14. Dogfooding rule

The product should be developed through the same graph-native method it
claims to provide. Where the product provides ODD framework behaviour, it
must build that behaviour through ODD graph functions and must not merely
publish ODD-shaped artifacts after imperative execution has already
decided the work. The project should therefore increasingly describe and
build itself through explicit assets, explicit vectors, explicit graph
functions, explicit scenario bundles and explicit target-relative closure.
The method is stronger when the product can walk itself (P0, P6).
```


### Row `ODD_METHOD.md#15-release-boundary` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#15-release-boundary` at rc.2:

```text
## 15. Release Boundary

Release version is not constitutional graph truth.

Release version belongs to the release process and release metadata.

The graph-native method concerns:

- current assets
- current vectors
- current closures
- current authority

Immutable RC publication, version-line selector advancement, and exact-cut
acceptance remain a separate process surface.

---
```

Successor, `ODD.md#15-release-boundary`:

```text
## 15. Release boundary

A release version is not constitutional graph truth; it belongs to the
release process and release metadata. The graph-native method concerns
current assets, current vectors, current closures and current authority.
Immutable RC publication, version-line selector advancement and exact-cut
acceptance stay a separate process surface, [RELEASE](RELEASE.md) (P3,
P6).
```


### Row `ODD_METHOD.md#16-failure-pattern` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#16-failure-pattern` at rc.2:

```text
## 16. Failure Pattern

The method is being violated when any of these are true:

1. a claimed product step has no corresponding node or vector
2. a graph function exists with no clear outer contract
3. automation performs work that cannot be described as a manual traversal
4. the installed product depends on authoring-carrier knowledge that a clean target project should not contain
5. scenarios cannot name the significant paths they intend to prove
6. the project claims closure without target-relative evidence
7. the cumulative environment law is bypassed by "last-output feeds next-input" wiring
8. zoomed and unzoomed views disagree about whether a carrier is closed
9. imperative service code owns an operative transition that has no published graph-function outcome contract
10. framework behavior is implemented as workspace orchestration first and only later described with GTL vocabulary
11. imperative code decides closure, continuation, semantic target movement, or lineage truth outside declared graph-function, ABG runtime, or product-owned carrier truth
12. a GTL/ABG product or plugin carries hidden execution authority for
    traversal loops, actor invocation, process supervision, retry,
    continuation, runtime events, projection, or closure folds
13. yield or lawful iteration is flattened into retry, block, timeout, local
    waiting state, or a hidden CLI loop instead of being represented as
    replay-visible closure disposition
14. a public query, gaps view, postflight string, service method, or installed
    operator summary can decide next work outside the constructive evaluation
    loop
15. a constitutional process cannot be followed end-to-end by an agentic coder
    from the declared authority, or a produced constitutional artifact is
    accepted without passing deterministic admission (§11.7A)

---
```

Successor, `ODD.md#16-failure-pattern`:

```text
## 16. Failure pattern

This profile is violated when any of these holds (P6):

1. a claimed product step has no corresponding node or vector;
2. a graph function exists with no clear outer contract;
3. automation performs work that cannot be described as a manual
   traversal;
4. the installed product depends on authoring-carrier knowledge that a
   clean target project should not contain;
5. scenarios cannot name the significant paths they intend to prove;
6. the project claims closure without target-relative evidence;
7. "last-output feeds next-input" wiring bypasses the cumulative
   environment law;
8. zoomed and unzoomed views disagree about whether a carrier is closed;
9. imperative service code owns an operative transition that has no
   published graph-function outcome contract;
10. framework behaviour is implemented as workspace orchestration first
    and described with GTL vocabulary only later;
11. imperative code decides closure, continuation, semantic target
    movement or lineage truth outside declared graph-function, ABG runtime
    or product-owned carrier truth;
12. a GTL/ABG product or plugin carries hidden execution authority for
    traversal loops, actor invocation, process supervision, retry,
    continuation, runtime events, projection or closure folds;
13. yield or lawful iteration is flattened into retry, block, timeout, a
    local waiting state or a hidden CLI loop instead of being represented
    as a replay-visible closure disposition;
14. a public query, gaps view, postflight string, service method or
    installed operator summary can decide next work outside the
    constructive evaluation loop;
15. a constitutional process cannot be followed end to end by an agentic
    coder from the declared authority, or a produced constitutional
    artifact is accepted without passing deterministic admission
    (§11.7A).
```


### Row `ODD_METHOD.md#17-invocation-rule` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#17-invocation-rule` at rc.2:

```text
## 17. Invocation Rule

When an agent or designer is instructed:

`using ODD_METHOD, build this product`

the expected sequence is:

1. read `SPEC_METHOD.md` and keep the constitutional chain intact
2. read the product-specific method if one exists
3. read the local product authority surfaces:
   - `INTENT.md`
   - `PRODUCT.md`
   - relevant requirement families
   - active design surfaces
4. identify the product's semantic chain from source to published outcome
5. identify the domain-specific typed assets or nodes
6. identify the public graph-function carriers
7. define the machine-readable function catalog
8. define or update the GTL module, including outer callable carriers and live traversal boundaries
9. define how coarse carriers, refined inner carriers, and executable proof lanes close together without scale contradiction
10. complete the execution-authority audit for affected runtime, plugin,
    worker, event, projection, assurance, closure, or continuation surfaces
11. define the constructive evaluation loop from intent lineage and model
    synthesis through observation, target binding, lawful action selection,
    admitted evidence, fulfillment ledger, closure decision, and next-action
    projection
12. define the closure decision vocabulary, including `yield` as lawful
    iteration rather than retry, block, timeout, or local waiting state
13. define the projection/query lane as projection over admitted constructive
    history, including the structural coherence rule between the read model and
    its source carrier
14. only then implement code, policy, and transport surfaces

The instruction does **not** mean:

- start from imperative scripts and add GTL words later
- treat graph functions as documentation wrappers
- let service code become the hidden real carrier

---
```

Successor, `ODD.md#17-invocation-rule`:

```text
## 17. Invocation rule

When an agent or designer is told `using ODD, build this product`, the
expected sequence is (P2, P0):

1. read SPEC_METHOD and keep the constitutional chain intact;
2. read the product-specific method if one exists;
3. read the local product authority surfaces: `INTENT.md`, `PRODUCT.md`,
   the relevant requirement families and the active design surfaces;
4. identify the product's semantic chain from source to published outcome;
5. identify the domain-specific typed assets or nodes;
6. identify the public graph-function carriers;
7. define the machine-readable function catalogue;
8. define or update the GTL module, including the outer callable carriers
   and the live traversal boundaries;
9. define how coarse carriers, refined inner carriers and executable proof
   lanes close together without scale contradiction;
10. complete the execution-authority audit for the affected runtime,
    plugin, worker, event, projection, assurance, closure or continuation
    surfaces;
11. define the constructive evaluation loop from intent lineage and model
    synthesis through observation, target binding, lawful action
    selection, admitted evidence, fulfilment ledger, closure decision and
    next-action projection;
12. define the closure decision vocabulary, including `yield` as lawful
    iteration and not retry, block, timeout or a local waiting state;
13. define the projection and query lane as a projection over admitted
    constructive history, including the structural coherence rule between
    the read model and its source carrier;
14. only then implement code, policy and transport surfaces.

The instruction does not mean starting from imperative scripts and adding
GTL words later, treating graph functions as documentation wrappers, or
letting service code become the hidden real carrier (P0, P6).
```


### Row `ODD_METHOD.md#18-cold-start-reading-order` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#18-cold-start-reading-order` at rc.2:

```text
## 18. Cold-Start Reading Order

When starting cold in a concrete ODD product, use this order.

### General ODD Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. the product's `stdo_<label>.json` definition
4. the applicable bound project reference-frame basis and authorized agent
   activation packet
5. the bound product Intent
6. the bound Product definition
7. relevant bound product requirements
8. active bound design surfaces
9. GTL module, function catalog, and query surfaces

### World-Model Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. `WORLD_MODEL_METHOD.md`
4. the product's `stdo_<label>.json` definition
5. the applicable bound project reference-frame basis and authorized agent
   activation packet
6. the bound product Intent
7. the bound Product definition
8. relevant bound requirement families
9. current bound design surfaces
10. GTL module, function catalog, query surfaces, and proof lane

The practical rule is:

- `ODD_METHOD.md` sets the structural expectation
- the product-specific method sets the domain law
- the local product surfaces set the current build line

If an LLM skips that ordering, it will usually either:

- understand the paradigm but miss the domain
- or understand the domain but realize it through the wrong carrier

---
```

Successor, `ODD.md#18-cold-start-reading-order`:

```text
## 18. Cold-start reading order

Starting cold in a concrete ODD product, read in the order below (P1, P2).

### General ODD product

1. SPEC_METHOD;
2. this profile;
3. the product's `stdo_<label>.json` definition;
4. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
5. the bound product Intent;
6. the bound Product definition;
7. the relevant bound product requirements;
8. the active bound design surfaces;
9. the GTL module, function catalogue and query surfaces.

### World-model product

1. SPEC_METHOD;
2. this profile;
3. the world-model profile (WORLD_MODEL);
4. the product's `stdo_<label>.json` definition;
5. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
6. the bound product Intent;
7. the bound Product definition;
8. the relevant bound requirement families;
9. the current bound design surfaces;
10. the GTL module, function catalogue, query surfaces and proof lane.

In practice this profile sets the structural expectation, the
product-specific method sets the domain law, and the local product
surfaces set the current build line. An LLM that skips the order will
usually either understand the paradigm but miss the domain, or understand
the domain but realise it through the wrong carrier (P1, P2).
```


### Row `ODD_METHOD.md#19-ramp-up-checklist` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#19-ramp-up-checklist` at rc.2:

```text
## 19. Ramp-Up Checklist

An LLM ramping into an ODD product should quickly answer:

1. What is the product's semantic chain from source to published outcome?
2. What are the typed domain assets or nodes?
3. What are the public graph functions?
4. Where is the machine-readable function catalog?
5. Where is the GTL module?
6. What belongs to ABG versus the product?
7. What is the projection/query lane?
8. What admitted carrier, runtime, event, or source truth does each projection
   derive from, and how does it fail closed on structural drift?
9. What proves that execution authority has not escaped ABG into product or
   plugin code?
10. What is the product's constructive evaluation loop from observation to next
    lawful action?
11. What are the closure decision dispositions, and how is `yield` represented
    as replay-visible lawful iteration?
12. What proof surfaces close the current capabilities?
13. What outer carrier remains open if a refined inner lane is green but live requirements still lack executable proof?
14. Can an agentic coder follow the constitutional process from the declared authority alone, and do the artifacts it produces pass deterministic admission?

If those questions cannot be answered quickly, the product is not yet sufficiently ODD-shaped.

---
```

Successor, `ODD.md#19-ramp-up-checklist`:

```text
## 19. Ramp-up checklist

An LLM ramping into an ODD product should quickly answer (P0, P2):

1. What is the product's semantic chain from source to published outcome?
2. What are the typed domain assets or nodes?
3. What are the public graph functions?
4. Where is the machine-readable function catalogue?
5. Where is the GTL module?
6. What belongs to ABG and what to the product?
7. What is the projection and query lane?
8. Which admitted carrier, runtime, event or source truth does each
   projection derive from, and how does it fail closed on structural
   drift?
9. What proves that execution authority has not escaped ABG into product
   or plugin code?
10. What is the product's constructive evaluation loop from observation to
    the next lawful action?
11. What are the closure decision dispositions, and how is `yield`
    represented as replay-visible lawful iteration?
12. Which proof surfaces close the current capabilities?
13. Which outer carrier stays open if a refined inner lane is green but
    live requirements still lack executable proof?
14. Can an agentic coder follow the constitutional process from the
    declared authority alone, and do the artifacts it produces pass
    deterministic admission?

If those questions cannot be answered quickly, the product is not yet
sufficiently ODD-shaped (P0, P2).
```


### Row `ODD_METHOD.md#2-method-role` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#2-method-role` at rc.2:

```text
## 2. Method Role

`SPEC_METHOD.md` defines the general constitutional method.

`ODD_METHOD.md` defines the graph-native ODD product-authoring method that uses GTL-defined graph functions as the primary constructive carrier.

The role split is:

- `SPEC_METHOD.md` — constitutional baseline for goals, intent, product, requirements, design, and lawful re-entry
- `ODD_METHOD.md` — constitutional law for graph-native traversal governance (assets, vectors, traversal, graph functions) AND product-authoring law for building an ODD product correctly over that substrate

This method does not replace product-specific domain methods such as `WORLD_MODEL_METHOD.md`.

Where a product is ODD and world-model-driven:

- `ODD_METHOD.md` governs graph-native structure and ODD product shape
- `WORLD_MODEL_METHOD.md` governs world-model semantics, publication, and composition law

Those methods compose.

---
```

Successor, `ODD.md#2-method-role`:

```text
## 2. Method role

[SPEC_METHOD](SPEC_METHOD.md) is the general constitutional method: the
baseline for goals, intent, product, requirements, design and lawful
re-entry. This profile is the graph-native ODD product-authoring method
whose primary constructive carrier is GTL-defined graph functions. It holds
two kinds of law: constitutional law for graph-native traversal governance
(assets, vectors, traversal, graph functions), and product-authoring law
for building an ODD product correctly over that substrate (P1, P6).

The profile does not replace a product-specific domain method such as the
world-model profile (WORLD_MODEL, tier 3). Where a product is both ODD and
world-model-driven, this profile governs graph-native structure and ODD
product shape and the world-model profile governs world-model semantics,
publication and composition law. The two compose (P1, P4a).
```


### Row `ODD_METHOD.md#20-canonical-compression` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#20-canonical-compression` at rc.2:

```text
## 20. Canonical Compression

ODD method is the graph-native product-authoring method for building GTL/ABG domain products. It requires typed domain assets, named graph functions, a published function catalog, a GTL module as the operative carrier, ABG-owned execution authority, one constructive evaluation loop from observation to next lawful action, projection/query surfaces that expose current state as projection over constructive history, and automation that remains explainable as a lawful manual traversal of the same graph. Operative framework behavior must be built outcome-first: outcome traversals first, declarative GTL/ABG carrier structure second, and minimal imperative adapter code last. Yield is the lawful iteration boundary, not retry, block, timeout, or a hidden local loop. Agentic development conforms by following the constitutional process from a minimal declared authority packet, with produced artifacts passing deterministic admission: the agentic walkthrough proves the process is followable, and admission proves each act conforms.
```

Successor, `ODD.md#20-canonical-compression`:

```text
## 20. Canonical compression

This profile is the graph-native product-authoring method for building
GTL/ABG domain products. It requires typed domain assets, named graph
functions, a published function catalogue, a GTL module as the operative
carrier, ABG-owned execution authority, one constructive evaluation loop
from observation to the next lawful action, projection and query surfaces
that expose current state as a projection over constructive history, and
automation that stays explainable as a lawful manual traversal of the same
graph. Operative framework behaviour must be built outcome-first: outcome
traversals first, declarative GTL/ABG carrier structure second, minimal
imperative adapter code last. Yield is the lawful iteration boundary, not
retry, block, timeout or a hidden local loop. Agentic development conforms
by following the constitutional process from a minimal declared authority
packet, with produced artifacts passing deterministic admission: the
agentic walkthrough proves the process can be followed, and admission
proves each act conforms (P0, P6).

This section is a compression of this member, a derived surface in the
sense of [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Acquisition. Its sources are §1, §2, §11.1 to §11.5D, §11.7 and §11.7A of
this member at the same digest, and it owns no determination. Where it and
a source section differ, the source section decides
([ACTIVATION §2 Staleness of derived surfaces](ACTIVATION.md#staleness-of-derived-surfaces))
(P1, P6).
```


### Row `ODD_METHOD.md#3-method-composition` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#3-method-composition` at rc.2:

```text
## 3. Method Composition

`ODD_METHOD.md` is not meant to be sufficient on its own for domain-correct product work.

It gives the structural law for how a graph-native ODD product should be built.

It does not, by itself, give:

- the product's domain semantics
- the product's current intent and product-definition line
- the product's local capability and constraint requirements
- the product's currently ratified design surfaces

So the composition rule is:

- `ODD_METHOD.md` tells you how to build the product as a graph-native ODD product
- domain methods tell you what semantic law the product must honor
- local `INTENT.md`, `PRODUCT.md`, requirements, and design tell you the currently ratified local line

Examples:

- for a graph-native software-development ODD product
  - `ODD_METHOD.md` provides the graph-native substrate and ODD structural law
  - product-local `INTENT.md`, `PRODUCT.md`, requirements, ADRs, and GTL surfaces provide the local product line

- for a world-model product
  - `ODD_METHOD.md` provides the graph-native substrate and ODD structural law
  - `WORLD_MODEL_METHOD.md` provides world-model semantic law
  - product-local `INTENT.md`, `PRODUCT.md`, requirements, and design provide the local product line

If an agent reads only `ODD_METHOD.md`, it should understand the paradigm.

If it needs to build one concrete product correctly, it must then read the product-specific method and local authority surfaces.

---
```

Successor, `ODD.md#3-method-composition`:

```text
## 3. Method composition

This profile alone does not suffice for domain-correct product work. It
gives the structural law for how a graph-native ODD product should be
built. It does not give the product's domain semantics, its current intent
and product-definition line, its local capability and constraint
requirements, or its currently ratified design surfaces (P1, P2).

The composition rule: this profile says how to build the product as a
graph-native ODD product; domain methods say what semantic law the product
must honour; the local `INTENT.md`, `PRODUCT.md`, requirements and design say
what the currently ratified local line is. For a graph-native
software-development ODD product, this profile provides the substrate and
structural law and the product's local `INTENT.md`, `PRODUCT.md`,
requirements, design records and GTL surfaces provide the local line. For
a world-model product, this profile provides the substrate and structural
law, the world-model profile provides the semantic law, and the product's
local `INTENT.md`, `PRODUCT.md`, requirements and design provide the local
line (P1, P2).

An agent that reads only this profile should understand the paradigm.
To build one concrete product correctly it must then read the
product-specific method and the local authority surfaces (P1, P2).
```


### Row `ODD_METHOD.md#4-method-folder-semantics` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#4-method-folder-semantics` at rc.2:

```text
## 4. Method Folder Semantics

The methodology library has two roles. Mutable source authors a future release;
consumers select one complete immutable release.

- `specification/standards/` in the `specification_methodology` source
  repository is the **authoring library** for the next method cut. Mutable
  source does not govern a consumer before publication and explicit selection.
- the shared versioned STDO store contains each **installed distribution** of
  one selected immutable RC cut. A Product Definition addresses it through an
  exact logical release URI and installed-manifest digest, independent of the
  machine-local store path. A project-local copy is optional, not the default.

The selected immutable RC is consumer authority. Installed bytes must match
that cut; mutable source and the moving version-line selector cannot silently
repair, replace, or outrank it. A mismatch is an adoption defect resolved by
selecting and installing one complete released cut, not by mixing source and
installed members.

Both roots contain three classes of document:

- `*_METHOD.md` — constitutional method surfaces
- `*_GUIDE.md` — operational guides and application standards
- `*_TEMPLATE.md` — reusable starter forms and examples

Only `*_METHOD.md` documents are constitutional method surfaces.

`*_GUIDE.md` documents refine application of the method.

`*_TEMPLATE.md` documents are convenience artifacts only.

When an installed distribution disagrees with its selected immutable release,
the selected release wins and the installation must be repaired. Mutable source
authors a future cut; it does not govern the installed consumer.

---
```

Successor, `ODD.md#4-method-library-classes`:

```text
## 4. Method library classes

The method library has two roles: mutable source authors a future release,
and consumers select one complete immutable release. The source library in
the methodology's source repository is the authoring library for the next
method cut; mutable source governs no consumer before publication and
explicit selection. The shared versioned STDO store holds each installed
distribution of one selected immutable RC cut. A product definition
addresses that distribution by an exact logical release URI and
installed-manifest digest, independent of the machine-local store path; a
project-local copy is optional and is not the default (P6, P3;
[PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)).

The selected immutable RC is consumer authority. Installed bytes must
match that cut; mutable source and the moving version-line selector cannot
silently repair, replace or outrank it. A mismatch is an adoption defect,
resolved by selecting and installing one complete released cut and not
by mixing source and installed members. When an installed distribution
disagrees with its selected immutable release, the selected release wins
and the installation must be repaired. Mutable source authors a future
cut; it does not govern the installed consumer (P6, P3;
[RELEASE §4](RELEASE.md#4-selector-and-consumer-adoption)).

Both the authoring library and an installed distribution contain three
classes of document. Method members are the constitutional method
surfaces; in the predecessor library they are the `*_METHOD.md` members,
and in this corpus they are the members that [README](README.md#documents)
names as method members: the tier 1 and tier 2 standards and, when a
project selects them, the tier 3 profiles. Guides (`*_GUIDE.md`) are operational guides and application standards
that refine application of the method. Templates (`*_TEMPLATE.md`) are
reusable starter forms and examples and are convenience artifacts only.
Only method members are constitutional method surfaces (P6, P3).
```


### Row `ODD_METHOD.md#5-graph-model` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#5-graph-model` at rc.2:

```text
## 5. Graph Model

The product is expressed as a declared asset graph over state-transitions relevant to the product's work.

### Nodes

Nodes are durable truth surfaces or product assets. Each node names a bounded state of truth.

Examples from a software-development ODD product:

- `intent`
- `product`
- `requirements`
- `design`
- `module_decomp`
- `code`
- `uat_testcases`
- `integration_tests`
- `bootloader`
- build targets

These are illustrative asset names from one concrete product. The method law is that nodes name bounded states; specific node names are product-local.

### Vectors

Vectors are lawful transitions between nodes.

Each vector declares:

- required upstream assets
- target asset
- governing evaluators and gates
- output contract

Vectors are the admissible transitions of the product.

### Probabilistic Compute

In ODD method, probabilistic compute is bounded constructive work over one
declared vector or edge traversal where the worker's internal solution path is
not fully determined by the graph or runtime.

One vector or edge traversal is the bounded unit of probabilistic compute.

The vector declares the admissible external traversal space:

- required upstream assets
- target asset or output contract
- required context
- role or capability expectation
- governing evaluators and gates
- provenance obligation
- lawful stop, hold, gap, continuation, or completion states

ABG may govern, invoke, observe, and classify the traversal. It does not own the
worker's hidden constructive path.

Anything not constrained by the traversal boundary remains worker-internal HOW:

- hidden LLM reasoning
- heuristic search
- domain implementation strategy
- tool-local execution detail
- product-specific business choice

`F_P` (`urn:stdo:concept:graph-native-odd:f-p`) is the graph/runtime shorthand
for this bounded probabilistic worker turn.
It is an ODD specialization of substrate-neutral lawful probabilistic
processing: it preserves bounded non-human construction under declared policy
and narrows that meaning to one graph traversal contract.

`F_D` (`urn:stdo:concept:graph-native-odd:f-d`) is the graph/runtime shorthand
for deterministic evaluation or proof over declared properties of the
traversal. F_D may optimize or validate a domain-local path where the domain can
make part of the work precise, but it does not move domain HOW into GTL, ABG,
or the framework.

`F_H` (`urn:stdo:concept:graph-native-odd:f-h`) is the graph/runtime shorthand
for explicit human adjudication invoked under the traversal's declared
authority and ambiguity policy. It specializes the substrate-neutral
human-adjudication concept without granting a human ambient traversal,
semantic, or closure authority.

The F_P specialization is directional from
`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing` to
`urn:stdo:concept:graph-native-odd:f-p`. The F_H specialization is directional
from `urn:stdo:concept:ambiguity-governance:human-adjudication` to
`urn:stdo:concept:graph-native-odd:f-h`. The source concepts and context are
owned by `SPEC_METHOD.md#ambiguity-governance-rule`; this standard owns the
targets in the graph-native ODD context.

Both relations preserve the source meaning and authority, narrow scope to a
declared ODD traversal, and add graph-contract and runtime-control coordinates.
They exclude processing or adjudication outside that traversal, refuse ambient
worker or human authority, and have no implied inverse. Their source and target
basis is the selected complete STDO release, their governed scope is ODD
traversal, and this clause is their provenance carrier. A change to either
concept or context, the basis, scope, preserved or narrowed meaning, or control
contract invalidates the affected specialization until reevaluated.

The method governs the traversal contract, evidence, provenance, and control
truth. It does not make the framework the executor of the domain's internal
solution strategy.

### Graph Functions

Graph functions are named constructive programs that realize vectors.

A graph function may:

- realize one outer vector directly
- refine one outer vector into a small inner workflow
- act as a reusable higher-order library function

The outer vector remains the constitutional contract. The graph function is the constructive realization of that contract.

### Traversal

The workflow is a traversal over the graph. Traversal means:

- bind the current target
- locate the next admissible vectors
- traverse one vector
- materialize the next asset
- prove the vector closed
- continue until the selected target closes

The graph is the declared program space of the product.

---
```

Successor, `ODD.md#5-graph-model`:

```text
## 5. Graph model

The product is expressed as a declared asset graph over the state
transitions relevant to the product's work (P0, P3).

### Nodes

Nodes are durable truth surfaces or product assets; each names a bounded
state of truth. In one software-development ODD product the nodes include
`intent`, `product`, `requirements`, `design`, `module_decomp`, `code`,
`uat_testcases`, `integration_tests`, `bootloader` and build targets. Those
names are illustrative and product-local; the law is that nodes name
bounded states (P3).

### Vectors

Vectors are the lawful transitions between nodes and are the admissible
transitions of the product. Each vector declares its required upstream
assets, its target asset, its governing evaluators and gates, and its
output contract (P4a, P6).

### Probabilistic compute

Probabilistic compute in this profile is bounded constructive work over
one declared vector or edge traversal, where the graph or runtime does not
fully determine the worker's internal solution path. One vector or edge
traversal is the bounded unit of probabilistic compute (P0).

Binding of the bounded step, new in this corpus. FOUNDATIONS P0 lets a
profile bind the bounded step to its own traversal unit and names
[PROFILES §2](PROFILES.md#2-graph-execution), which indexes this profile,
as the keeper of that binding. Direction: from the step of
FOUNDATIONS P0 to one declared ODD vector or edge traversal. Preserved
meaning: the step's selected context fits the actor's envelope, the
actor's internal path within the step is its own, and the traversal is
the admissible external space. Narrowed scope: one declared vector or edge
traversal of a published graph. Invalidation: a change to FOUNDATIONS P0,
to the vector's declaration or to the selected basis invalidates the
binding until it is evaluated again (P0, P1).

The vector declares the admissible external traversal space: required
upstream assets; target asset or output contract; required context; role
or capability expectation; governing evaluators and gates; provenance
obligation; and the lawful stop, hold, gap, continuation or completion
states. ABG may govern, invoke, observe and classify the traversal; it
does not own the worker's hidden constructive path. Whatever the traversal
boundary does not constrain remains worker-internal HOW: hidden LLM
reasoning, heuristic search, domain implementation strategy, tool-local
execution detail and product-specific business choice (P0, P6).

Three shorthands name the graph and runtime classifications of work inside
one traversal. They are concepts of this bounded context; the a_c functor
kinds of AXIOMATIC_CALCULUS §5 are different concepts and are not imported
by spelling (P1, P3):

- `F_P` (`urn:stdo:concept:graph-native-odd:f-p`) is the shorthand for the
  bounded probabilistic worker turn. It specialises substrate-neutral
  lawful probabilistic processing: it keeps bounded non-human construction
  under declared policy and narrows that meaning to one graph traversal
  contract.
- `F_D` (`urn:stdo:concept:graph-native-odd:f-d`) is the shorthand for
  deterministic evaluation or proof over declared properties of the
  traversal. F_D may optimise or validate a domain-local path where the
  domain can make part of the work precise; it does not move domain HOW
  into GTL, ABG or the framework.
- `F_H` (`urn:stdo:concept:graph-native-odd:f-h`) is the shorthand for
  explicit human adjudication invoked under the traversal's declared
  authority and ambiguity policy. It specialises the substrate-neutral
  human-adjudication concept and grants a human no ambient traversal,
  semantic or closure authority.

These are the two declared bindings that PROFILES §1 requires. The F_P
specialisation runs from
`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing` to
`urn:stdo:concept:graph-native-odd:f-p`; the F_H specialisation runs from
`urn:stdo:concept:ambiguity-governance:human-adjudication` to
`urn:stdo:concept:graph-native-odd:f-h`. The source concepts and their
context are owned by
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle); this
profile owns the targets in the graph-native ODD context (P1, P6).

Both relations preserve the source meaning and authority, narrow scope to
a declared ODD traversal, and add graph-contract and runtime-control
coordinates. They exclude processing or adjudication outside that
traversal, refuse ambient worker or human authority, and have no implied
inverse. Their source and target basis is the selected complete STDO
release, their governed scope is ODD traversal, and this clause is their
provenance carrier. A change to either concept or context, to the basis,
to the scope, to the preserved or narrowed meaning or to the control
contract invalidates the affected specialisation until it is evaluated
again (P1, P3, P6).

The profile governs the traversal contract, its evidence, its provenance
and its control truth. It does not make the framework the executor of the
domain's internal solution strategy (P0, P6).

### Graph functions

Graph functions are named constructive programs that realise vectors. A
graph function may realise one outer vector directly, refine one outer
vector into a small inner workflow, or act as a reusable higher-order
library function. The outer vector remains the constitutional contract;
the graph function is the constructive realisation of that contract (P4a,
P0).

Binding of refinement, new in this corpus.
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) generalises the
refinement of one outer vector into an inner workflow to any realisation,
lets a refinement carry an earlier output to a later step only through a
declared adapter or specialised contract whose declared domain names it,
and names [PROFILES §2](PROFILES.md#2-graph-execution), which indexes this
profile, as the keeper of the ODD binding. This profile declares the
cumulative carried environment of
[§11.8](#118-cumulative-environment-law-is-mandatory) as that specialised
contract; §11.8 is conserved as profile law and is not generalised into
the core. Direction: from the typed refinement of ACTIVATION §4 to a graph
function that refines one outer vector, with the §11.8 environment as its
specialised contract. Preserved meaning: the outer vector stays the
callable contract; the inner steps conserve it and every applicable
invariant; and each inner function's input satisfies its declared domain
and preconditions, as AC-016 requires. Narrowed scope: one published outer
vector and its declared inner workflow, whose retained functions should
declare `environment.requires`, `environment.provides` and
`environment.carries` (§11.8); a later function's declared domain is its
`environment.requires`, which may require any typed binding available in
the cumulative carried environment, not only the immediately previous
output. Invalidation: a change to ACTIVATION §4, to §11.8, to the outer
vector or to a function's environment declaration invalidates the binding
until it is evaluated again (P4a, P4b, P1).

### Traversal

The workflow is a traversal over the graph: bind the current target;
locate the next admissible vectors; traverse one vector; materialise the
next asset; prove the vector closed; continue until the selected target
closes. The graph is the declared program space of the product (P0, P5).
```


### Row `ODD_METHOD.md#6-product-boundary` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#6-product-boundary` at rc.2:

```text
## 6. Product Boundary

The graph-native product and the project built with it are distinct.

The installed product provides the method, runtime, and carrier surfaces. It does not provide the target project's business domain.

A clean install means:

1. install the graph-native ODD product
2. author the target project's intent, product definition, requirements, and realization root
3. traverse the product graph to build the target project's domain outputs

The installed product owns:

- the graph-native method and its traversal-control substrate
- runtime and control surfaces
- command surfaces
- release-managed methodology surfaces
- project scaffold templates

The target project owns:

- one `stdo_<label>.json` definition for each distinct product `WHAT`,
  locating its constitutional, local, collective reference-frame basis,
  realization, work, and composition surfaces
- constitutional surfaces per `SPEC_METHOD.md`; `GOALS.md`, `INTENT.md`,
  `PRODUCT.md`, and `requirements/` are the default software-development
  scaffold rather than mandatory names
- one or more realization roots bound through `how.build_tenants`;
  `build_tenants/` is the default root name for software-development ODD
  products, while existing projects and other domain types may use their own
  locations
- domain outputs and evidence (for a software-development ODD product these are design, code, tests, docs, and proof surfaces; other domains name their produced artifacts accordingly)

The installed product must not assume prior knowledge of the target project's domain.

---
```

Successor, `ODD.md#6-product-boundary`:

```text
## 6. Product boundary

The graph-native product and the project built with it are distinct. The
installed product provides the method, the runtime and the carrier
surfaces; it does not provide the target project's business domain. The
installed product must not assume prior knowledge of the target project's
domain (P6, P3).

A clean install means: install the graph-native ODD product; author the
target project's intent, product definition, requirements and realisation
root; traverse the product graph to build the target project's domain
outputs (P0, P6).

The installed product owns the graph-native method and its
traversal-control substrate, the runtime and control surfaces, the command
surfaces, the release-managed methodology surfaces and the project
scaffold templates (P6).

The target project owns (P6, P3;
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)):

- one `stdo_<label>.json` definition for each distinct product WHAT,
  locating its constitutional, local and collective reference-frame
  basis, realisation, work and composition surfaces;
- its constitutional surfaces under SPEC_METHOD, where `GOALS.md`,
  `INTENT.md`, `PRODUCT.md` and `requirements/` are the default
  software-development scaffold and not mandatory names;
- one or more realisation roots bound through `how.build_tenants`, where
  `build_tenants/` is the default root name for software-development ODD
  products and existing projects and other domain types may use their own
  locations;
- its domain outputs and evidence: design, code, tests, documents and
  proof surfaces for a software-development ODD product, and each other
  domain's own produced artifacts named accordingly.
```


### Row `ODD_METHOD.md#7-self-host-boundary-rule` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#7-self-host-boundary-rule` at rc.2:

```text
## 7. Self-Host Boundary Rule

Self-hosting is lawful only when the installed product under use remains distinct from the product under development.

A released installed product may help build the next version of itself, but the two must not collapse into one mixed authority surface.

The required distinction is:

- installed released builder
- in-development product being built

This is the same boundary preserved when one compiler release builds the next compiler release.

The framework must preserve distinct:

- territories
- authority surfaces
- runtime state
- project-owned specification and build-tenant surfaces

If automation, runtime resolution, or qualification silently merges those surfaces, the framework is violating the method.

---
```

Successor, `ODD.md#7-self-host-boundary`:

```text
## 7. Self-host boundary

Self-hosting is lawful only while the installed product in use stays
distinct from the product under development. A released installed product
may help build the next version of itself, but the two must not collapse
into one mixed authority surface. The distinction is between the installed
released builder and the in-development product being built, the same
boundary one compiler release keeps when it builds the next (P6, P3).

The framework must preserve distinct territories, authority surfaces,
runtime state, and project-owned specification and build-tenant surfaces. If
automation, runtime resolution or qualification silently merges those
surfaces, the framework violates this profile (P6, P3).
```


### Row `ODD_METHOD.md#8-responsibility-layers-and-local-binding` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#8-responsibility-layers-and-local-binding` at rc.2:

```text
## 8. Responsibility Layers And Local Binding

`ODD_METHOD.md` governs structural responsibility layers and their required publication shape.

It does not freeze one product's local asset names as universal ODD doctrine.

The method-level expectation is:

- a responsibility layer expresses one capability class
- the product binds that capability to its own local domain semantics
- the GTL carrier publishes the lawful transitions for that bound capability

Examples of capability classes may include:

- bootstrap or intake
- design
- implementation
- qualification
- release
- operational transition
- retrofit

Those are responsibility-layer ideas, not mandatory universal instance names.

For one concrete product, each active layer should bind explicitly to:

- local typed assets or typed nodes
- public graph-function carriers
- required carried environment
- proof or closure surfaces
- projection or query surfaces

That means an audit should distinguish clearly between:

- shared ODD structural law
- local product semantic bindings

If a product copies another product's local asset names without semantic need, that is not reuse of method. It is accidental doctrine transfer.

If a product declares a capability in prose but does not bind it into typed assets, graph functions, and proof lanes, that capability is under-built.

---
```

Successor, `ODD.md#8-responsibility-layers-and-local-binding`:

```text
## 8. Responsibility layers and local binding

This profile governs structural responsibility layers and their required
publication shape. It does not freeze one product's local asset names as
universal ODD doctrine. A responsibility layer expresses one capability
class; the product binds that capability to its own local domain
semantics; the GTL carrier publishes the lawful transitions for that bound
capability (P1, P3).

Capability classes may include bootstrap or intake, design,
implementation, qualification, release, operational transition and
retrofit. They are responsibility-layer ideas, not mandatory universal
instance names (P1).

In one concrete product each active layer should bind explicitly to local
typed assets or typed nodes, public graph-function carriers, the required
carried environment, proof or closure surfaces, and projection or query
surfaces. An audit should therefore distinguish clearly between shared
ODD structural law and local product semantic bindings (P3, P6).

A product that copies another product's local asset names without
semantic need is not reusing the method; that is accidental doctrine
transfer. A product that declares a capability in prose but does not bind
it into typed assets, graph functions and proof lanes has under-built that
capability (P1, P2).
```


### Row `ODD_METHOD.md#9-method-governance-and-audit` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#9-method-governance-and-audit` at rc.2:

```text
## 9. Method Governance And Audit

Products governed under `ODD_METHOD.md` should be audited against this method as the shared constitutional surface.

That audit should ask at minimum:

- what responsibility layer or capability class is being implemented
- what local typed assets or nodes bind that capability into the product
- what public graph functions carry the constructive transition
- what proof or closure lane justifies the capability
- what projected/query state is exposed without replacing ABG runtime truth
- whether any product command, service, or query surface is trying to replace
  ABG continuation with tenant-local orchestration
- whether the execution-authority audit proves that traversal loops, actor
  invocation, process supervision, retry/continuation, runtime events, and
  closure folds remain owned by ABG

The governance rule is:

- approved shared-pattern work must update `ODD_METHOD.md` when it changes or clarifies the reusable structural law
- product-local work may remain local if it does not change shared structural law

Grey work must not be silently absorbed into the line.

When an implementation or design move is not clearly covered by the current method, it must be evaluated against `ODD_METHOD.md` and resolved as one of:

- compliant with the current method
- non-compliant with the current method
- valid and worth incorporation into `ODD_METHOD.md`

If the result is incorporation, the implementation is not fully approved until the method surface is updated accordingly.

If the result is non-compliance, the implementation should be repriced, repaired, or rejected rather than normalized by repetition.

The practical rule is:

- no shared structural pattern becomes "approved by usage"
- no grey pattern becomes constitutional by drift
- reusable structural law is ratified in `ODD_METHOD.md`
- local product law is ratified in the product's own authority surfaces

---
```

Successor, `ODD.md#9-method-governance-and-audit`:

```text
## 9. Method governance and audit

Products governed under this profile should be audited against it as the
shared constitutional surface. The audit should ask at minimum (P6):

- which responsibility layer or capability class is being implemented;
- which local typed assets or nodes bind that capability into the product;
- which public graph functions carry the constructive transition;
- which proof or closure lane justifies the capability;
- which projected or query state is exposed without replacing ABG runtime
  truth;
- whether any product command, service or query surface is trying to
  replace ABG continuation with tenant-local orchestration;
- whether the execution-authority audit (§11.5B) proves that traversal
  loops, actor invocation, process supervision, retry and continuation,
  runtime events and closure folds remain owned by ABG.

Approved shared-pattern work must update this profile when it changes or
clarifies the reusable structural law; product-local work may stay local
when it changes no shared structural law. Grey work must not be silently
absorbed into the line (P6, P2).

An implementation or design move that the current profile does not
clearly cover must be evaluated against this profile and resolved as one
of: compliant with the current profile; non-compliant with it; or valid
and worth incorporating into it. If the result is incorporation, the
implementation is not fully approved until this profile is updated. If the
result is non-compliance, the implementation should be repriced, repaired
or rejected, not normalised by repetition (P6).

Mapping of the audit outcome to the core result algebra, new in this
corpus. Purpose: [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) states
the outcome of every evaluation in the core. Material relation: a design,
ticket or proof that consumes the audit reads incorporation as neither
compliance nor failure. Each outcome maps for the predicate "the move
complies with the current profile" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| compliant | satisfied | the move meets the law of the current profile |
| non-compliant | falsified | the law of this profile that the move violates is the counterexample |
| valid and worth incorporating | out_of_frame | the current profile does not declare the law the move needs; the outcome names that law, this profile as its owner and the update it requires, which is the reconfiguration pressure of out_of_frame ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or indeterminate) |

In practice no shared structural pattern becomes approved by usage; no
grey pattern becomes constitutional by drift; reusable structural law is
ratified in this profile; and local product law is ratified in the
product's own authority surfaces (P6, P3).
```


### Row `ODD_METHOD.md#abg` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#abg` at rc.2:

```text
### ABG

ABG owns:

- traversal
- dispatch
- actor invocation
- process supervision
- graph-call realization
- runtime facts
- runtime event emission and replay
- frames
- continuations
- retry and correction control
- closure folds over runtime truth
- re-entry after publish boundaries
- lineage and provenance
```

Successor, `ODD.md#abg`:

```text
### ABG

ABG owns traversal; dispatch; actor invocation; process supervision;
graph-call realisation; runtime facts; runtime event emission and replay;
frames; continuations; retry and correction control; closure folds over
runtime truth; re-entry after publish boundaries; lineage and provenance
(P6).
```


### Row `ODD_METHOD.md#general-odd-product` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#general-odd-product` at rc.2:

```text
### General ODD Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. the product's `stdo_<label>.json` definition
4. the applicable bound project reference-frame basis and authorized agent
   activation packet
5. the bound product Intent
6. the bound Product definition
7. relevant bound product requirements
8. active bound design surfaces
9. GTL module, function catalog, and query surfaces
```

Successor, `ODD.md#general-odd-product`:

```text
### General ODD product

1. SPEC_METHOD;
2. this profile;
3. the product's `stdo_<label>.json` definition;
4. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
5. the bound product Intent;
6. the bound Product definition;
7. the relevant bound product requirements;
8. the active bound design surfaces;
9. the GTL module, function catalogue and query surfaces.
```


### Row `ODD_METHOD.md#graph-functions` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#graph-functions` at rc.2:

```text
### Graph Functions

Graph functions are named constructive programs that realize vectors.

A graph function may:

- realize one outer vector directly
- refine one outer vector into a small inner workflow
- act as a reusable higher-order library function

The outer vector remains the constitutional contract. The graph function is the constructive realization of that contract.
```

Successor, `ODD.md#graph-functions`:

```text
### Graph functions

Graph functions are named constructive programs that realise vectors. A
graph function may realise one outer vector directly, refine one outer
vector into a small inner workflow, or act as a reusable higher-order
library function. The outer vector remains the constitutional contract;
the graph function is the constructive realisation of that contract (P4a,
P0).

Binding of refinement, new in this corpus.
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) generalises the
refinement of one outer vector into an inner workflow to any realisation,
lets a refinement carry an earlier output to a later step only through a
declared adapter or specialised contract whose declared domain names it,
and names [PROFILES §2](PROFILES.md#2-graph-execution), which indexes this
profile, as the keeper of the ODD binding. This profile declares the
cumulative carried environment of
[§11.8](#118-cumulative-environment-law-is-mandatory) as that specialised
contract; §11.8 is conserved as profile law and is not generalised into
the core. Direction: from the typed refinement of ACTIVATION §4 to a graph
function that refines one outer vector, with the §11.8 environment as its
specialised contract. Preserved meaning: the outer vector stays the
callable contract; the inner steps conserve it and every applicable
invariant; and each inner function's input satisfies its declared domain
and preconditions, as AC-016 requires. Narrowed scope: one published outer
vector and its declared inner workflow, whose retained functions should
declare `environment.requires`, `environment.provides` and
`environment.carries` (§11.8); a later function's declared domain is its
`environment.requires`, which may require any typed binding available in
the cumulative carried environment, not only the immediately previous
output. Invalidation: a change to ACTIVATION §4, to §11.8, to the outer
vector or to a function's environment declaration invalidates the binding
until it is evaluated again (P4a, P4b, P1).
```


### Row `ODD_METHOD.md#nodes` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#nodes` at rc.2:

```text
### Nodes

Nodes are durable truth surfaces or product assets. Each node names a bounded state of truth.

Examples from a software-development ODD product:

- `intent`
- `product`
- `requirements`
- `design`
- `module_decomp`
- `code`
- `uat_testcases`
- `integration_tests`
- `bootloader`
- build targets

These are illustrative asset names from one concrete product. The method law is that nodes name bounded states; specific node names are product-local.
```

Successor, `ODD.md#nodes`:

```text
### Nodes

Nodes are durable truth surfaces or product assets; each names a bounded
state of truth. In one software-development ODD product the nodes include
`intent`, `product`, `requirements`, `design`, `module_decomp`, `code`,
`uat_testcases`, `integration_tests`, `bootloader` and build targets. Those
names are illustrative and product-local; the law is that nodes name
bounded states (P3).
```


### Row `ODD_METHOD.md#odd-product` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#odd-product` at rc.2:

```text
### ODD Product

The ODD product owns:

- domain asset meaning
- graph-function meaning
- published function catalog
- policy overlays
- domain query projections
- closure and gap interpretation for its domain
```

Successor, `ODD.md#odd-product`:

```text
### ODD product

The ODD product owns domain asset meaning, graph-function meaning, the
published function catalogue, policy overlays, domain query projections,
and closure and gap interpretation for its domain (P6, P1).
```


### Row `ODD_METHOD.md#probabilistic-compute` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#probabilistic-compute` at rc.2:

```text
### Probabilistic Compute

In ODD method, probabilistic compute is bounded constructive work over one
declared vector or edge traversal where the worker's internal solution path is
not fully determined by the graph or runtime.

One vector or edge traversal is the bounded unit of probabilistic compute.

The vector declares the admissible external traversal space:

- required upstream assets
- target asset or output contract
- required context
- role or capability expectation
- governing evaluators and gates
- provenance obligation
- lawful stop, hold, gap, continuation, or completion states

ABG may govern, invoke, observe, and classify the traversal. It does not own the
worker's hidden constructive path.

Anything not constrained by the traversal boundary remains worker-internal HOW:

- hidden LLM reasoning
- heuristic search
- domain implementation strategy
- tool-local execution detail
- product-specific business choice

`F_P` (`urn:stdo:concept:graph-native-odd:f-p`) is the graph/runtime shorthand
for this bounded probabilistic worker turn.
It is an ODD specialization of substrate-neutral lawful probabilistic
processing: it preserves bounded non-human construction under declared policy
and narrows that meaning to one graph traversal contract.

`F_D` (`urn:stdo:concept:graph-native-odd:f-d`) is the graph/runtime shorthand
for deterministic evaluation or proof over declared properties of the
traversal. F_D may optimize or validate a domain-local path where the domain can
make part of the work precise, but it does not move domain HOW into GTL, ABG,
or the framework.

`F_H` (`urn:stdo:concept:graph-native-odd:f-h`) is the graph/runtime shorthand
for explicit human adjudication invoked under the traversal's declared
authority and ambiguity policy. It specializes the substrate-neutral
human-adjudication concept without granting a human ambient traversal,
semantic, or closure authority.

The F_P specialization is directional from
`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing` to
`urn:stdo:concept:graph-native-odd:f-p`. The F_H specialization is directional
from `urn:stdo:concept:ambiguity-governance:human-adjudication` to
`urn:stdo:concept:graph-native-odd:f-h`. The source concepts and context are
owned by `SPEC_METHOD.md#ambiguity-governance-rule`; this standard owns the
targets in the graph-native ODD context.

Both relations preserve the source meaning and authority, narrow scope to a
declared ODD traversal, and add graph-contract and runtime-control coordinates.
They exclude processing or adjudication outside that traversal, refuse ambient
worker or human authority, and have no implied inverse. Their source and target
basis is the selected complete STDO release, their governed scope is ODD
traversal, and this clause is their provenance carrier. A change to either
concept or context, the basis, scope, preserved or narrowed meaning, or control
contract invalidates the affected specialization until reevaluated.

The method governs the traversal contract, evidence, provenance, and control
truth. It does not make the framework the executor of the domain's internal
solution strategy.
```

Successor, `ODD.md#probabilistic-compute`:

```text
### Probabilistic compute

Probabilistic compute in this profile is bounded constructive work over
one declared vector or edge traversal, where the graph or runtime does not
fully determine the worker's internal solution path. One vector or edge
traversal is the bounded unit of probabilistic compute (P0).

Binding of the bounded step, new in this corpus. FOUNDATIONS P0 lets a
profile bind the bounded step to its own traversal unit and names
[PROFILES §2](PROFILES.md#2-graph-execution), which indexes this profile,
as the keeper of that binding. Direction: from the step of
FOUNDATIONS P0 to one declared ODD vector or edge traversal. Preserved
meaning: the step's selected context fits the actor's envelope, the
actor's internal path within the step is its own, and the traversal is
the admissible external space. Narrowed scope: one declared vector or edge
traversal of a published graph. Invalidation: a change to FOUNDATIONS P0,
to the vector's declaration or to the selected basis invalidates the
binding until it is evaluated again (P0, P1).

The vector declares the admissible external traversal space: required
upstream assets; target asset or output contract; required context; role
or capability expectation; governing evaluators and gates; provenance
obligation; and the lawful stop, hold, gap, continuation or completion
states. ABG may govern, invoke, observe and classify the traversal; it
does not own the worker's hidden constructive path. Whatever the traversal
boundary does not constrain remains worker-internal HOW: hidden LLM
reasoning, heuristic search, domain implementation strategy, tool-local
execution detail and product-specific business choice (P0, P6).

Three shorthands name the graph and runtime classifications of work inside
one traversal. They are concepts of this bounded context; the a_c functor
kinds of AXIOMATIC_CALCULUS §5 are different concepts and are not imported
by spelling (P1, P3):

- `F_P` (`urn:stdo:concept:graph-native-odd:f-p`) is the shorthand for the
  bounded probabilistic worker turn. It specialises substrate-neutral
  lawful probabilistic processing: it keeps bounded non-human construction
  under declared policy and narrows that meaning to one graph traversal
  contract.
- `F_D` (`urn:stdo:concept:graph-native-odd:f-d`) is the shorthand for
  deterministic evaluation or proof over declared properties of the
  traversal. F_D may optimise or validate a domain-local path where the
  domain can make part of the work precise; it does not move domain HOW
  into GTL, ABG or the framework.
- `F_H` (`urn:stdo:concept:graph-native-odd:f-h`) is the shorthand for
  explicit human adjudication invoked under the traversal's declared
  authority and ambiguity policy. It specialises the substrate-neutral
  human-adjudication concept and grants a human no ambient traversal,
  semantic or closure authority.

These are the two declared bindings that PROFILES §1 requires. The F_P
specialisation runs from
`urn:stdo:concept:ambiguity-governance:lawful-probabilistic-processing` to
`urn:stdo:concept:graph-native-odd:f-p`; the F_H specialisation runs from
`urn:stdo:concept:ambiguity-governance:human-adjudication` to
`urn:stdo:concept:graph-native-odd:f-h`. The source concepts and their
context are owned by
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle); this
profile owns the targets in the graph-native ODD context (P1, P6).

Both relations preserve the source meaning and authority, narrow scope to
a declared ODD traversal, and add graph-contract and runtime-control
coordinates. They exclude processing or adjudication outside that
traversal, refuse ambient worker or human authority, and have no implied
inverse. Their source and target basis is the selected complete STDO
release, their governed scope is ODD traversal, and this clause is their
provenance carrier. A change to either concept or context, to the basis,
to the scope, to the preserved or narrowed meaning or to the control
contract invalidates the affected specialisation until it is evaluated
again (P1, P3, P6).

The profile governs the traversal contract, its evidence, its provenance
and its control truth. It does not make the framework the executor of the
domain's internal solution strategy (P0, P6).
```


### Row `ODD_METHOD.md#product-realization-software-development-topology` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#product-realization-software-development-topology` at rc.2:

```text
### Product Realization (software-development topology)

The Product Definition Overlay's `how` bindings locate the authoritative `HOW`.
`build_tenants/` is the default software-development location.

It carries:

- design
- GTL publications
- code
- tests
- local proof surfaces
```

Successor, `ODD.md#product-realisation-software-development-topology`:

```text
### Product realisation (software-development topology)

The product definition's `how` bindings locate the authoritative HOW;
`build_tenants/` is the default software-development location. It carries
design, GTL publications, code, tests and local proof surfaces (P6).
```


### Row `ODD_METHOD.md#product-specification-software-development-topology` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#product-specification-software-development-topology` at rc.2:

```text
### Product Specification (software-development topology)

The Product Definition Overlay's `what` bindings locate the authoritative `WHAT`.
`specification/` is the default software-development location.

It defines:

- intent
- product position
- goals
- requirements
- scenarios
```

Successor, `ODD.md#product-specification-software-development-topology`:

```text
### Product specification (software-development topology)

The product definition's `what` bindings locate the authoritative WHAT;
`specification/` is the default software-development location. It defines
intent, product position, goals, requirements and scenarios (P6).
```


### Row `ODD_METHOD.md#query-and-service-layers` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#query-and-service-layers` at rc.2:

```text
### Query And Service Layers

Service or query layers may own:

- transport
- sessions
- routing
- browser-safe projection
- API surfaces

They do not own runtime truth.

They also do not own continuation truth.

Do not hide the real constructive carrier behind the word `service`.

---
```

Successor, `ODD.md#query-and-service-layers`:

```text
### Query and service layers

Service or query layers may own transport, sessions, routing,
browser-safe projection and API surfaces. They own neither runtime truth
nor continuation truth. The real constructive carrier is never hidden
behind the word service (P6).
```


### Row `ODD_METHOD.md#traversal` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#traversal` at rc.2:

```text
### Traversal

The workflow is a traversal over the graph. Traversal means:

- bind the current target
- locate the next admissible vectors
- traverse one vector
- materialize the next asset
- prove the vector closed
- continue until the selected target closes

The graph is the declared program space of the product.

---
```

Successor, `ODD.md#traversal`:

```text
### Traversal

The workflow is a traversal over the graph: bind the current target;
locate the next admissible vectors; traverse one vector; materialise the
next asset; prove the vector closed; continue until the selected target
closes. The graph is the declared program space of the product (P0, P5).
```


### Row `ODD_METHOD.md#vectors` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#vectors` at rc.2:

```text
### Vectors

Vectors are lawful transitions between nodes.

Each vector declares:

- required upstream assets
- target asset
- governing evaluators and gates
- output contract

Vectors are the admissible transitions of the product.
```

Successor, `ODD.md#vectors`:

```text
### Vectors

Vectors are the lawful transitions between nodes and are the admissible
transitions of the product. Each vector declares its required upstream
assets, its target asset, its governing evaluators and gates, and its
output contract (P4a, P6).
```


### Row `ODD_METHOD.md#world-model-product` (disposition `conserved`)

Predecessor, `ODD_METHOD.md#world-model-product` at rc.2:

```text
### World-Model Product

1. `SPEC_METHOD.md`
2. `ODD_METHOD.md`
3. `WORLD_MODEL_METHOD.md`
4. the product's `stdo_<label>.json` definition
5. the applicable bound project reference-frame basis and authorized agent
   activation packet
6. the bound product Intent
7. the bound Product definition
8. relevant bound requirement families
9. current bound design surfaces
10. GTL module, function catalog, query surfaces, and proof lane

The practical rule is:

- `ODD_METHOD.md` sets the structural expectation
- the product-specific method sets the domain law
- the local product surfaces set the current build line

If an LLM skips that ordering, it will usually either:

- understand the paradigm but miss the domain
- or understand the domain but realize it through the wrong carrier

---
```

Successor, `ODD.md#world-model-product`:

```text
### World-model product

1. SPEC_METHOD;
2. this profile;
3. the world-model profile (WORLD_MODEL);
4. the product's `stdo_<label>.json` definition;
5. the applicable bound project reference-frame basis and the authorised
   agent activation packet;
6. the bound product Intent;
7. the bound Product definition;
8. the relevant bound requirement families;
9. the current bound design surfaces;
10. the GTL module, function catalogue, query surfaces and proof lane.

In practice this profile sets the structural expectation, the
product-specific method sets the domain law, and the local product
surfaces set the current build line. An LLM that skips the order will
usually either understand the paradigm but miss the domain, or understand
the domain but realise it through the wrong carrier (P1, P2).
```


### Row `POSTING_GUIDE.md#boundary` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#boundary` at rc.2:

```text
## Boundary

Use a post when the content is:

- provisional
- investigative
- comparative
- argumentative
- not yet ratified

Do not use a post for:

- live requirements
- live design decisions
- active process law

Those belong in the applicable bound `WHAT` or ratified design surfaces.

---
```

Successor, `POSTING_GUIDE.md#2-boundary`:

```text
## 2. Boundary

Use a post when the content is provisional, investigative, comparative,
argumentative or not yet ratified (P6; rc.2 #boundary).

Do not use a post for live requirements, live design decisions or active
process law. Those belong in the applicable bound WHAT surfaces or the
ratified design surfaces (P6, P3).
```


### Row `POSTING_GUIDE.md#carrier-identity` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#carrier-identity` at rc.2:

```text
## Carrier Identity

For the default local-file carrier, use:

```text
YYYYMMDDTHHMMSS_CATEGORY_SUBJECT.md
```

Example:

```text
20260327T120000_REVIEW_bootloader-boundary.md
```

The subject should be short, specific, and stable enough to scan later. A
non-file carrier must preserve an equivalent stable post identity, publication
time, category, subject, author, discussion state, and supersession history.

---
```

Successor, `POSTING_GUIDE.md#4-carrier-identity`:

```text
## 4. Carrier identity

On the default local-file carrier a post is named (P3; rc.2
#carrier-identity):

```text
YYYYMMDDTHHMMSS_CATEGORY_SUBJECT.md
```

For example:

```text
20260327T120000_REVIEW_bootloader-boundary.md
```

The subject should be short, specific and stable enough to scan later
(P3). A carrier that is not a file must preserve an equivalent stable post
identity, publication time, category, subject, author, discussion state
and supersession history (P3, P4b).
```


### Row `POSTING_GUIDE.md#categories` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#categories` at rc.2:

```text
## Categories

Use these categories:

- `REVIEW` for critique of code, spec, design, or another post
- `STRATEGY` for a proposed technical or methodological direction
- `GAP` for a precise insufficiency or contradiction
- `SCHEMA` for data model, event model, interface, or contract shape
- `HANDOFF` for bounded transfer of context or task state
- `MATRIX` for explicit decision comparison across options

---
```

Successor, `POSTING_GUIDE.md#5-categories`:

```text
## 5. Categories

A post takes one of these categories (P3; rc.2 #categories):

- `REVIEW`: critique of code, specification, design or another post;
- `STRATEGY`: a proposed technical or methodological direction;
- `GAP`: a precise insufficiency or contradiction;
- `SCHEMA`: the shape of a data model, event model, interface or contract;
- `HANDOFF`: a bounded transfer of context or task state; and
- `MATRIX`: an explicit comparison of options for a decision.
```


### Row `POSTING_GUIDE.md#discussion-state-and-mutability` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#discussion-state-and-mutability` at rc.2:

```text
## Discussion State And Mutability

Posts are mutable while they are part of an open discussion.

Use `Status` to make the discussion state explicit:

- `Draft` for a post still being shaped by its author
- `Open` for a post published into an active discussion
- `Closed` for a post whose discussion has concluded

While a post is `Draft` or `Open`, update the same post when the change is
still part of the same bounded discussion. This includes:

- correcting mistakes
- incorporating replies
- refining recommendations
- repricing confidence
- adding new evidence that belongs to the same subject

When updating an open post, preserve the original `Date` as the first
publication time. Add or update `Updated` when useful.

Once a post is `Closed`, updating it is discouraged. Prefer a new post when a
later change would materially alter a closed conclusion, reopen an old dispute,
or start a new bounded subject.

Closed posts are not constitutional truth. They are stable commentary records
unless and until their content is adopted into a bound `WHAT` surface,
ratified design, or accepted implementation.

---
```

Successor, `POSTING_GUIDE.md#7-discussion-state-and-mutability`:

```text
## 7. Discussion state and mutability

A post is mutable while it is part of an open discussion. Use `Status` to
make the discussion state explicit (P3, P4b; rc.2
#discussion-state-and-mutability):

- `Draft`: the author is still shaping the post;
- `Open`: the post is published into an active discussion; and
- `Closed`: the discussion has concluded.

While a post is `Draft` or `Open`, the same post is updated when the
change still belongs to the same bounded discussion: correcting
mistakes, incorporating replies, refining recommendations, repricing
confidence, or adding new evidence on the same subject (P3). An update to
an open post keeps the original `Date` as the first publication time and
adds or updates `Updated` when useful (P3, P4b).

Updating a `Closed` post is discouraged. Prefer a new post when a later
change would materially alter a closed conclusion, reopen an old
dispute or start a new bounded subject (P4b, P3).

A closed post is not constitutional truth either. It is a stable
commentary record unless and until its content is adopted into a bound
WHAT surface, ratified design or accepted implementation (P6).
```


### Row `POSTING_GUIDE.md#location` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#location` at rc.2:

```text
## Location

Posts live at the Product Definition Overlay's `ticketing.comments.root`
binding.

The default local-file binding is:

```text
.ai-workspace/comments/<agent>/
```

Capability example:

- `.ai-workspace/comments/<agent-id>/`

An existing project may bind another directory, repository resource, message
board, API collection, or product-scoped query. The bound carrier must preserve
the commentary-versus-authority distinction in this guide. Its location or
visibility cannot turn a post into ticket, Product, requirement, or design
truth.

---
```

Successor, `POSTING_GUIDE.md#3-location`:

```text
## 3. Location

Posts live at the location the product definition binds as
`ticketing.comments.root` (P6, P3; rc.2 #location). The default local-file
binding is:

```text
.ai-workspace/comments/<agent>/
```

For example, `.ai-workspace/comments/<agent-id>/` (P3).

An existing project may bind another directory, a repository resource, a
message board, an API collection or a product-scoped query instead. The
bound carrier must preserve the distinction between commentary and
authority that this guide draws. Its location and its visibility cannot
turn a post into ticket, Product, requirement or design truth (P6, P3).
```


### Row `POSTING_GUIDE.md#posting-rules` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#posting-rules` at rc.2:

```text
## Posting Rules

1. State whether the post describes current reality, target direction, or both.
2. Separate findings from recommendations.
3. Use exact file or requirement references when making claims.
4. Do not present a post as if it were already ratified.
5. Do not rewrite closed history by stealth. Open posts may be revised in
   place; closed posts should normally be superseded by a new post.
6. Keep one post to one bounded subject.

---
```

Successor, `POSTING_GUIDE.md#8-posting-rules`:

```text
## 8. Posting rules

1. State whether the post describes current reality, target direction or
   both (P1).
2. Keep findings separate from recommendations (P6).
3. Make claims with exact file or requirement references (P3, P6).
4. Do not present a post as if it were already ratified (P6).
5. Do not rewrite closed history by stealth. An open post may be revised
   in place; a closed post should normally be superseded by a new post
   (P4b, P3).
6. Keep each post to one bounded subject (P2).

Provenance rc.2 #posting-rules.
```


### Row `POSTING_GUIDE.md#ratification` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#ratification` at rc.2:

```text
## Ratification

A post becomes consequential only when its content is explicitly adopted into:

- a bound `WHAT` surface
- ratified design
- accepted implementation

Until then it is commentary, not law.
```

Successor, `POSTING_GUIDE.md#9-ratification`:

```text
## 9. Ratification

A post becomes consequential only when its content is explicitly adopted
into a bound WHAT surface, ratified design or accepted implementation.
Until then it is commentary, not law (P6; rc.2 #ratification).
```


### Row `POSTING_GUIDE.md#shared-method-adoption-and-propagation-stdo-up-012` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#shared-method-adoption-and-propagation-stdo-up-012` at rc.2:

```text
## Shared Method Adoption And Propagation (`STDO-UP-012`)

Reusable method change preserves this authority relation:

```text
incident or review evidence
  -> shared-method intake
  -> one owning standard
  -> consistency and independent review
  -> human-authority acceptance
  -> one complete released STDO version
  -> explicit consumer selection
  -> consumer-owned realization and evidence
```

This is authority causality, not a prescribed intake workflow or artifact set.
An executable tool, runtime, carrier schema, or assurance implementation cannot
enter STDO merely because it accompanies a method lesson; it requires separate
Product authorization. Other standards consume admitted law by reference, and
consumers select complete released versions rather than mixing members from
different cuts.
```

Successor, `SPEC_METHOD.md#shared-method-adoption-and-propagation-stdo-up-012`:

```text
### Shared method adoption and propagation (STDO-UP-012)

A reusable change to this method keeps one authority relation from the
evidence that prompts it to the consumer that realises it (P6, P3;
provenance rc.2 POSTING_GUIDE
#shared-method-adoption-and-propagation-stdo-up-012):

```text
incident or review evidence
  -> shared-method intake
  -> one owning standard
  -> consistency and independent review
  -> human-authority acceptance
  -> one complete released STDO version
  -> explicit consumer selection
  -> consumer-owned realisation and evidence
```

The chain states authority causality. It prescribes no intake workflow and
no artifact set (P2). An executable tool, runtime, carrier schema or
assurance implementation cannot enter the method merely because it
accompanies a method lesson; it requires its own Product authorisation
(P6). Other standards consume admitted law by reference (P3, P6), and a
consumer selects a complete released version rather than mixing members from different cuts (P3;
the release version boundary above,
[PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager)).
```

Successor, `POSTING_GUIDE.md#10-shared-method-adoption`:

```text
## 10. Shared method adoption

How a reusable method lesson travels from incident or review evidence to
a consumer's realisation, STDO-UP-012, is stated once in
[SPEC_METHOD §6](SPEC_METHOD.md#shared-method-adoption-and-propagation-stdo-up-012).
A post that carries such evidence or proposes such a change does not
adopt it (§9) (P6; provenance rc.2
#shared-method-adoption-and-propagation-stdo-up-012).
```


### Row `POSTING_GUIDE.md#structure` (disposition `conserved`)

Predecessor, `POSTING_GUIDE.md#structure` at rc.2:

```text
## Structure

Use this base shape:

```markdown
# {CATEGORY}: {Subject}

**Author**: {agent}
**Date**: {ISO 8601}
**Addresses**: {artifact, issue, or boundary under discussion}
**Status**: Draft
**Updated**: {ISO 8601, optional}

## Summary
{short summary}

## Analysis
{main content}

## Recommended Action
{next step}
```

If `MATRIX` is used, the central section is a decision table rather than free prose.

---
```

Successor, `POSTING_GUIDE.md#6-structure`:

```text
## 6. Structure

A post uses this base shape (P3, P6; rc.2 #structure):

```markdown
# {CATEGORY}: {Subject}

**Author**: {agent}
**Date**: {ISO 8601}
**Addresses**: {artifact, issue, or boundary under discussion}
**Status**: Draft
**Updated**: {ISO 8601, optional}

## Summary
{short summary}

## Analysis
{main content}

## Recommended Action
{next step}
```

In a `MATRIX` post the central section is a decision table rather than
free prose (P3).
```


### Row `README.md#standards-library` (disposition `conserved`)

Predecessor, `README.md#standards-library` at rc.2:

```text
# Standards Library

This tree authors the normative shared specification methodology. One complete
immutable released RC cut of this tree is the constitutional member set of the
selectable STDO Product; the release may also carry subordinate executable and
interaction tooling:

- constitutional method surfaces such as `REFERENCE_FRAME_METHOD.md`,
  `SPEC_METHOD.md`, `ODD_METHOD.md`, `IDENTITY_METHOD.md`, and
  `WORLD_MODEL_METHOD.md`
- the fundamental carrier-neutral `AXIOMATIC_CALCULUS.md`, whose `a_c` theory
  remains separate from interpreted subject models and carrier encodings
- the application-neutral `TRAVERSAL_OCCURRENCE_PROFILE.md`, which instantiates
  one closed model-family signature under an exact `a_c` basis without changing
  the calculus or selecting a consumer; adoption remains optional;
- derived application profiles such as `STDO_REFERENCE_FRAME_BASELINE.md`
- companion governance and operating surfaces such as `POSTING_GUIDE.md`,
  `WRITING_GUIDE.md`, `RELEASE_METHOD.md`, `TICKET_METHOD.md`, and
  `DESIGN_MODULE_METHOD.md`
- the non-deciding semantic locator index `GLOSSARY_GUIDE.md`, whose rows point
  to context-declaring owning clauses and never define a shared default
- source-maintained compressed read models under `authority_compressions/` for
  prompt-construction installs that need compact shared-method authority
- normative interoperability schemas under `schemas/`, including the
  layout-neutral STDO Product Definition Overlay and deterministic installed-
  release manifest
- starter templates under `templates/`, including the single per-product
  `PRODUCT_DEFINITION_TEMPLATE.json`, project specification templates, and
  `PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md`, plus agent bootstrap templates
  such as `CLAUDE_TEMPLATE.md` and `AGENTS_TEMPLATE.md`

The STDO toolchain manager installs complete immutable cuts once in a shared
versioned store and resolves logical release URIs without putting machine-local
paths in Product Definitions. Project-local copies remain possible when
explicitly bound and verified, but are not the default. Installed bytes derive
authority from the exact RC cut, Product Definition basis URI, manifest digest,
and member inventory. Neither mutable authoring head nor the moving version-line
selector silently replaces that consumer basis.
```

Successor, `README.md#library-and-installed-basis`:

```text
## Library and installed basis

One complete immutable released RC cut of this standards tree is the
constitutional member set of the selectable STDO Product. The release may
also carry subordinate executable and interaction tooling (P6, P3;
provenance rc.2 README #standards-library). A cut carries (P3, P2):

- the constitutional members of tiers 1 and 2 above;
- the carrier-neutral [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md), whose
  a_c theory stays separate from interpreted subject models and carrier
  encodings ([AC-020](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation));
- the application-neutral traversal occurrence profile
  [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md), which instantiates
  one closed model-family signature under an exact a_c basis without
  changing the calculus or selecting a consumer, and whose adoption stays
  optional;
- derived application profiles such as
  [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md);
- the companion guides [POSTING_GUIDE](POSTING_GUIDE.md) and
  [WRITING_GUIDE](WRITING_GUIDE.md);
- the non-deciding semantic locator index [GLOSSARY](GLOSSARY.md), whose
  rows point to the clauses that own each indexed concept and the contexts
  that hold it, and never define a shared default;
- compact read models for activations that need a compact method basis;
  their carrier awaits the ruling on the rc.2 compression rows;
- normative interoperability schemas under `schemas/`, among them the
  layout-neutral product definition overlay and the deterministic
  installed-release manifest; and
- starter templates under `templates/`: the single per-product product
  definition template, project specification templates, the project
  reference-frame basis template and agent bootstrap templates.

The STDO toolchain manager installs each complete immutable cut once in a
shared versioned store and resolves logical release URIs, so a product
definition names its basis by logical URI and manifest digest and carries
no machine-local path
([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager))
(P3, P6). A project-local copy stays possible when it is explicitly bound
and verified; it is not the default
([PRODUCT_DEFINITION §12](PRODUCT_DEFINITION.md#12-bootstrap)) (P6, P3).
Installed bytes take their authority from the exact RC cut, the product
definition's basis URI, the manifest digest and the member inventory
([PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager),
[RELEASE §3](RELEASE.md#exact-cut-qualification)) (P3, P6). Neither the
mutable authoring head nor the moving version-line selector silently
replaces that consumer basis
([RELEASE §4](RELEASE.md#4-selector-and-consumer-adoption)) (P6, P3).
```

Successor, `PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`:

```text
## 4. Shared installed release basis and toolchain manager

Within the product-definition-routing context an Installed Release Basis
is the pair (P3; rc.2
#shared-installed-release-basis-and-toolchain-manager):

```text
(immutable stdo://releases/<cut>/ URI, installed-manifest SHA-256)
```

The URI identifies one immutable annotated RC cut. The digest identifies
the deterministic installed-release manifest, which binds the cut's tag
object, commit, repository tree, standards subtree, exact standards
inventory, member bytes and admitted auxiliary payloads. The manifest shape
is owned by `schemas/installed-release-manifest.schema.json`. The manifest
is transport and integrity evidence, not a replacement constitution (P6).

An Adoption Plan is the read-only, deterministic acceptance object that
binds one current Product Definition's identity and bytes to its current
basis and to one resolved immutable target's cut, annotated tag object,
commit, tree and installed-manifest digest. Its SHA-256 is the
operator-presentable acceptance token. Possession of the token alone grants
no authority; a mismatch proves that the presented subject is no longer the
subject being mutated (P6, P3). A Fleet Adoption Plan binds an authorised
fleet root and the complete ordered set of per-definition plan digests
under the same law.

Plan hashing covers the acceptance object only: local installation status
and machine-local install paths are excluded. The canonical bytes are UTF-8
JSON with recursively sorted object keys, two-space indentation, LF line
endings and one final LF. Fleet order is deterministic discovery-path
order. These rules make a presented digest independently reproducible
rather than an opaque session token (P3, P6).

The STDO Toolchain Manager is the bounded executable realisation that (P2,
P3):

- installs each immutable cut once in a shared, versioned release store;
- resolves logical `stdo://releases/...` URIs to verified installed bytes;
- inventories and verifies complete installed distributions;
- synchronises the exact basis already selected by a Product Definition;
- emits an exact digest-bound adoption plan from a mutable version-line
  selector and performs adoption only when that plan is explicitly
  accepted;
- manages the stable marker-bounded bootstrap in declared agent files; and
- applies those operations to an explicitly discovered fleet of Product
  Definitions.

The store may live at any machine-local path. Its registry maps logical
release URIs to installed paths and manifest digests and owns neither
Product selection nor method meaning. A consumer repository therefore needs
no project-local standards copy and no prescribed folder structure, and
several Product Definitions on one machine may select different installed
cuts concurrently (P3, P6). Every manager-owned component from the
configured store root downward is a physical directory or regular file of
its declared type; a symlink, junction, reparse point, device, socket or
other redirection or special entry fails closed. Verification inventories
every filesystem entry type, directories included, rejects any entry not
derived from the manifest's exact file paths, and never follows an
unmanifested alias (P5, P3).

`constitution.stdo.source.repository` identifies the transport source.
`constitution.stdo.selector` is a mutable `stdo://channels/<version>`
discovery selector whose alias semantics are owned by the release law (the
[RELEASE](RELEASE.md) member). Neither is operative authority.
`constitution.stdo.basis.uri` and `constitution.stdo.basis.manifest_sha256`
are the sole authored STDO selection for that Product Definition (P6, P3).

The manager observes these command boundaries (P6, P5):

- `install` admits one explicitly named immutable RC cut without changing
  any Product Definition;
- `sync` installs and verifies only the exact basis already selected by
  the Product Definition and never consults its mutable selector;
- `adopt --dry-run` resolves the annotated selector and immutable RC, and
  presents the target cut, tag object, commit, tree, manifest digest,
  current Product-Definition byte digest and a deterministic
  adoption-plan digest, without mutation;
- mutating `adopt` requires that exact prior plan digest as explicit
  acceptance, re-derives it before installation, installs only the bound
  target, rechecks the Product Definition bytes, and atomically changes
  only its basis and its basis-relative schema locator; any drift refuses
  mutation;
- `status`, `verify`, `list`, `manifest` and `resolve` are read-only with
  respect to Product Definitions; and
- fleet adoption emits, and requires explicit acceptance of, one aggregate
  plan digest over every per-definition plan; all fleet writes require
  explicit whole-selection authorisation and infer no composition or
  inheritance from directory nesting.

Missing cuts, moved immutable tags, tag-to-commit mismatch, manifest-digest
mismatch, missing, extra or changed installed members, ambiguous Product
Definition discovery, unaccepted or stale adoption plans, URI escape,
physical store redirection, undeclared filesystem entry types and malformed
bootstrap markers fail closed (P5). Every `stdo:` schema locator is parsed
before schema loading under URI scheme case-insensitivity and names the
same immutable cut as `constitution.stdo.basis`; spelling variation cannot
cross that basis. No cache, registry entry, source checkout, version alias,
schema or agent file may silently replace the basis selected in the
Product Definition (P6, P3).

`constitution.agent_bootstrap` embeds no other constitution. It names one
basis-qualified bootstrap entrypoint and the local instruction files (such
as `AGENTS.md` or `CLAUDE.md` targets) whose small discovery block the
manager owns between explicit markers. Each target is a portable relative
path resolved against `product.source_project`; absolute paths, parent
traversal, redirected path components and escape from that boundary fail
closed. A fleet additionally confines every resolved source project to its
explicitly authorised fleet root and preflights every target before the
first write. Exactly one correctly ordered marker span may be replaced;
the bytes before and after it, trailing whitespace included, stay
project-owned and byte-identical, and appending a new span preserves all
existing bytes as an exact prefix. The bootstrap routes agents to the
applicable Product Definition, the exact installed basis and the owning
sources; it can neither restate nor override them (P6, P3, P5).

Recursive fleet discovery prunes these exact directory names as
version-control, dependency, generated, cache or managed-store internals:
`.git`, `.hg`, `.svn`, `.bzr`, `.venv`, `venv`, `node_modules`, `vendor`,
`site-packages`, `build`, `dist`, `out`, `target`, `.gradle`, `.tox`,
`.nox`, `.cache`, `.ruff_cache`, `.mypy_cache`, `.pytest_cache`,
`__pycache__`, `.genesis` and `.stdo`. A discovered Product Definition may
not itself be a symlink. These exclusions are discovery law, not evidence
that an excluded tree lacks another independently governed Product (P5,
P6).

### Explicit complete consumer update

A Complete Consumer Update Plan binds one explicitly selected Product
Definition and the complete companion population of one exact upstream
release-matched cohort to the consumer bindings selected by the
invocation's owner. The Product Definition continues to own composition;
the upstream cohort and each Product's release record own release and
member identity. An invocation selection and its derived plan and result
are operation evidence, not another persistent dependency declaration,
registry or lock. The caller selects every native route and derived context
for the claimed update scope; directory proximity or an empty discovery
result cannot supply that selection, and an empty derived-context
population means the owner selected none, not that the manager established
the absence of semantic context (P6, P3; rc.2
#explicit-complete-consumer-update).

The separate `cohort-update` operation presents the whole plan without
consumer effects. Unlike the basis-only Adoption Plan above, its acceptance
object also binds the physical effect destinations and binding preimages,
the exact selected cohort bytes, the companion annotated tags, commits,
subtrees and inventories, the replacement dependency locators, the native
routes and the declared derived-source observations. It uses the same
canonical JSON hashing rule. Already-installed status supplies no
additional authority and does not change the digest. Mutation requires
explicit acceptance of this exact plan and re-derives it; possession of its
digest alone grants no operation authority. The `adopt`, `sync` and fleet
contracts above keep their narrower boundaries (P6, P3).

The complete operation verifies the selected cohort's dependency closure
and each exact companion's definition, release record and admitted members
before relying on them. It stages absent immutable installs, verifies
existing installs without repairing them in place, and preflights every
consumer target. Only the selected basis and schema, the existing
composition locators and contracts, and the selected native and install
links may change; historical installs and unrelated consumer content stay
available and unchanged. It creates no consumer-local checker and changes
no Product meaning or local semantic map (P3, P6, P2).

For each selected derived context, missing, ambiguous, changed or
unavailable program, map or source evidence holds the complete update
before any consumer effect. The source owner performs any semantic re-entry
that is needed; the manager cannot mechanically relabel an older map as
current. Exact source freshness is integrity evidence, not semantic
conformance and not an independent semantic verdict (P1, P6). After
immutable staging the manager rechecks the consumer preimages and the
source evidence. It reports completion only after verifying every selected
resulting binding and companion. Refusal before consumer effects retains
the prior state; a caught application failure restores the affected
consumer preimages and does not report completion; newly staged immutable
installs may stay unused. The operation requires an exclusive consumer
write scope during application. It claims no crash-atomic transaction
across independent filesystem paths: abrupt process or host loss, or
unavailable rollback storage, requires recovery from the presented
preimages before the complete relation can be claimed (P5, P4b).

Outcomes as results. The outcomes of the manager's operations in §4,
its refusals, its reported completion and the recovery that
loss requires, are stated in the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) through the refinements
of [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), each
for its own predicate; the cause of an outcome selects its value, and the
mapping adds no core value (P5, P6):

- Effect. An operation that writes, such as `install`, `sync`, a mutating
  `adopt`, fleet adoption or the complete consumer update, has an
  intended external effect, recorded under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) for the predicate "the
  intended effect occurred". Reported completion is `completed`
  (`satisfied`) only where evidence about the subject establishes the
  effect in full, as the complete update's verification of every
  selected resulting binding and companion does. The cause selects the
  other values. A refusal before any effect, with the retained prior
  state as the evidence about the subject, is `not_effected`
  (`falsified`), and the effect has ended. A caught application failure
  is also `not_effected` (`falsified`): the failure observed on the
  subject establishes that the complete update is not attained, and the
  operation applies no later part of it, so no later completion of this
  effect can attain it. Whether its restored preimages are verified
  decides only whether the effect's end is established, never the value:
  verified, the effect has ended; a restoration not verified, or rollback
  storage unavailable after the failure, leaves the end not established,
  recorded beside the value as a residual naming the verification that
  would establish it. Newly staged immutable installs left unused are
  named with the value as the part that did occur. Abrupt process or
  host loss, where no caught failure establishes that the update fell
  short, is `completion_unknown` (`indeterminate`), never `completed` or
  `not_effected`. `completion_unknown`, and `not_effected` with its end
  not established, are effects of uncertain completion under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects): recovery from the
  presented preimages reconciles them, as
  [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) states, before
  any repetition or claim of the complete relation.
- Refusal. A refusal also answers whether the operation may apply its
  effect on the exact subject and basis it binds. Found before the
  operation begins, it is an outcome of
  [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation),
  for "the step is lawfully admitted and activated on the exact subject
  and basis"; found after it has begun, as by the recheck after immutable
  staging, it is a value of
  [construction availability](ACTIVATION.md#construction-availability),
  for "a candidate is available". A missing explicit acceptance of the
  exact plan, or missing whole-selection authorisation of a fleet write,
  is missing operation authority: `admission_refused(authority)`
  (`out_of_frame`), naming the acceptance or authorisation needed and
  its owner. Every other refusal has a basis cause: drift of the Product
  Definition bytes or of a consumer preimage; a stale plan; each other
  condition of the fail-closed list above, ambiguous discovery included
  because it leaves no exact subject; a path, locator or marker span that
  escapes or breaks its boundary; and missing, ambiguous, changed or
  unavailable derived-context evidence, which holds the complete update.
  It is `admission_refused(basis)` before the operation begins and
  `re_entry_requested(basis)` after, `invalid_basis` in both, and names
  the basis coordinate that fails and, for derived-context evidence, the
  source owner whose re-entry repairs it.
- Command without an intended effect. A command without an intended
  external effect, such as `verify` or `adopt --dry-run`, has no value
  under Effects, and its refusal maps by cause as above. A condition it
  reports about the subject it evaluates, such as a member that `verify`
  finds missing, extra or changed, is a counterexample to that command's
  own predicate, `falsified`, not a refusal.

Purpose and material relation: a consumer that combines the manager's
outcomes with other results cannot read a refused or failed operation as
completed, an operation whose value is `completion_unknown` as either
completed or not effected, a caught failure whose restoration is not
verified as undecided when the update is known to have fallen short, or
a refusal for missing acceptance as one for a defective basis (P5, P6).
This mapping is new in this corpus.
```

Successor, `PRODUCT_DEFINITION.md#12-bootstrap`:

```text
## 12. Bootstrap

Every product defined under this method begins from
`templates/PRODUCT_DEFINITION_TEMPLATE.json`, copied to the product's
definition root as `stdo_default.json` for a singleton default project or
as `stdo_<label>.json` for a named product definition. An existing project
fills the URI bindings over its current layout; adoption requires no
moving, renaming or duplicating of existing authority or realisation
surfaces (P2, P3; rc.2 #bootstrap-rule).

The default scaffold binds:

- a shared versioned STDO store, addressed through the exact
  `constitution.stdo.basis`, as the installed distribution of the selected
  process constitution;
- `specification/GOALS.md` as current work-wave orientation;
- `specification/INTENT.md` as domain direction;
- `specification/PRODUCT.md` as the current product-definition surface;
- `specification/requirements/` as the live requirement surface;
- `build_tenants/` as the root for shared and tenant-local realisation
  surfaces; and
- `.ai-workspace/` as the sprint, ticket and comment carrier root.

These are template defaults, not universal path law; the definition's URI
bindings select the actual project carriers (P2).

The authority split is (P6, P3):

- mutable methodology authoring lives in the method's own source workspace
  (the standards of its source project) and governs only a future
  candidate cut;
- released methodology authority is the exact immutable STDO version
  selected by the consumer;
- installed methodology distribution lives in the toolchain manager's
  shared versioned store by default and matches the basis URI and manifest
  digest;
- project-owned constitutional surfaces live at the definition's `what`
  bindings; and
- project-owned realisation and work surfaces live at its `how` and
  `ticketing` bindings.

A project creates no competing local methodology root, such as a default
`specification/standards/`, and binds no mutable or partial method source
as if it were the selected immutable release (P6).

Method authority is singular: the selected immutable STDO release
authority, projected into the installed distribution located by the
overlay; and the project constitutional authority at the definition's
bound WHAT surfaces (P6). When editing or repricing methodology, the
mutable source path is authoring authority for the candidate being
constructed; it is not operative consumer law before release and explicit
selection (P3, P6). When operating inside a governed workspace, the
resolved installed basis is the operative distribution of the selected
immutable release until the consumer explicitly adopts another cut. A
project-local exact copy stays lawful when explicitly bound and verified;
it is not the default, and file proximity cannot select it (P6, P3).

The corresponding default folder shape is:

```text
stdo_default.json

specification/
├── GOALS.md
├── INTENT.md
├── PRODUCT.md
└── requirements/
    └── *.md

build_tenants/
├── common/
└── default/

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
```

This is a starter topology, not a conformance requirement. A monorepo may
place several `stdo_<label>.json` definitions at one root and bind each to
a different WHAT. A hierarchical repository may place one or more
definitions at any nested project root. Recursive discovery (§9) finds both
shapes; explicit composition, never directory nesting, relates their
products (P3, P2).

A project need not start with a complete `requirements/` tree on day zero.
Requirements may be sourced from any legitimate constitutional input
regardless of its path, including `GOALS.md`, `INTENT.md`, `PRODUCT.md`,
existing requirement documents, imported standards or policy material,
prior project versions, and migration or repricing source material. Most
projects begin by deriving `INTENT.md` from `GOALS.md`, then `PRODUCT.md`
from `INTENT.md`, then the first requirement surface from the product
definition; that is the usual starting point, not the only lawful source
(P2).

The bootstrap sequence is (P3, P6, P2):

1. Install the STDO toolchain manager once, resolve one version-line
   selector, and explicitly select one immutable RC cut.
2. Install that complete cut in the shared release store and retain its
   deterministic installed-manifest digest.
3. Copy `PRODUCT_DEFINITION_TEMPLATE.json` from that exact cut to the
   product definition root as `stdo_default.json` or `stdo_<label>.json`.
4. Assign the stable `product.definition_id` for the mutable WHAT
   definition line, its source-project locator and its bounded-context
   declaration; keep it distinct from every immutable Product and release
   identity.
5. Bind `constitution.stdo.source`, its non-operative selector, the exact
   basis URI and manifest digest, every additional constitutional
   authority and the relevant basis-qualified entrypoints; confirm that
   the set collectively defines axioms, ontology, epistemology, taxonomy
   and semantics for the governed scope (§3).
6. Bind the agent bootstrap entrypoint and portable targets relative to
   the resolved `product.source_project`, then let the manager preflight
   every target and install or refresh only their marker-bounded
   discovery blocks.
7. Bind, or explicitly empty, the local axiom, override and
   disambiguation collections (§6).
8. Bind at least one accepted collective reference-frame basis, its
   admitting authorities and its exact governed scope (§7).
9. Write or confirm the current Goals carrier, run the goals to intent to
   product steps, and bind the resulting Intent and Product entrypoints.
10. Gather, derive, classify and bind the live specification or
    requirement surfaces without creating a co-equal rival.
11. Bind at least one build tenant, including its root, design and
    implementation surfaces, and bind any shared realisation law (§8).
12. Bind the Goals carrier, the ticket lanes, the comments root and the
    optional sprint root.
13. Bind every known product-composition edge explicitly, including its
    target definition identity, relation authority and non-empty contract
    set (§9).
14. Validate the JSON shape, assert URI and URI-reference syntax,
    synchronise and verify the exact installed basis, then resolve every
    URI and perform the cross-definition identity, composition,
    constitutional-sufficiency and authority-congruence checks.

Once a bound requirement set is the live constitutional surface, no rival
monolithic requirements document should remain co-equal authority with it. This
keeps requirement truth structurally clear, derivable and non-monolithic
without prescribing its folder (P6, P2).
```

Successor, `RELEASE.md#exact-cut-qualification`:

```text
### Exact-cut qualification

Qualification binds (P6, P3; rc.2 #exact-cut-qualification):

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree,
  and declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts and unresolved gaps; and
- the complete successor relation to the declared predecessor (§9).

Evidence matches the claim. Source success does not prove packaged or
installed behaviour; packaging equivalence does not prove semantic
behaviour; artifact presence does not prove usability unless presence is
the exact claim (P6, P1; EVALUATION §1 is the generic claim law).

An RC is accepted only when the required exact-cut review and operator
checks are complete and the human authority accepts that exact subject. If
review requires any qualifying-byte change, the verdict remains attached
to the old RC and a higher RC is published. The selector already
advertises the highest published RC; acceptance does not move it, rewrite
it or create another final carrier (P6, P3).
```

Successor, `RELEASE.md#4-selector-and-consumer-adoption`:

```text
## 4. Selector and consumer adoption

The version-line selector answers only (P6, P3;
rc.2 #selector-and-consumer-adoption):

> Which highest-ordinal published immutable RC cut currently exists on
> this version line?

It never answers:

> Which exact STDO cut governs this consumer?

A Product Definition may retain `stdo://channels/<version>` as its
discovery selector, but its operative basis is the exact
`stdo://releases/v<version>-rc.<n>/` URI and installed-manifest digest,
the installed release basis of PRODUCT_DEFINITION §4. Moving the Git
version-line selector does not update any consumer. Adoption is a separate
explicit Product-Definition transition that resolves, presents, installs,
verifies and pins the selected immutable RC. Resolution requires an
annotated selector with a distinct peeled commit; absence of a peeled
selector ref fails closed and cannot be interpreted as a lightweight
selector whose tag object is its commit (P6, P3, P5).

Channel resolution enumerates the published RC tags for the selected
Project Release Namespace, including preserved unqualified historical cuts
during a namespace transition, selects the greatest positive ordinal,
requires that cut and the current selector to be annotated tags peeling to
the same commit, and fails closed when the selector lags or points
elsewhere. Channel adoption also refuses a same-line target whose ordinal
is below the Product Definition's current exact basis. A consumer that
intentionally retains an older cut names that immutable RC URI and digest
explicitly and uses exact-basis operations such as `sync`; it does not
express that choice through the latest-version channel (P5, P6).

Presentation and mutation are separate invocations. The read-only plan,
the Adoption Plan of PRODUCT_DEFINITION §4, binds the current Product
Definition bytes and basis to the target immutable cut, annotated tag
object, peeled commit, tree and installed-manifest digest, then emits a
deterministic plan digest. Mutation requires that exact digest as the
operator's acceptance and re-derives it before changing any Product
Definition. Selector, target, manifest or definition drift invalidates the
acceptance. A fleet uses the same law with one aggregate digest over all
exact per-definition plans. Planning inside a mutating invocation is not
external presentation and cannot authorise itself. The plan's hashing rule
and the manager's command boundaries are PRODUCT_DEFINITION §4 (P6, P3).

This split lets operators refer to `v<version>` for the latest published
RC without repeatedly incrementing the version line, while every governed
project retains reproducible exact-cut authority and changes only through
explicit adoption (P2, P3, P6).
```
