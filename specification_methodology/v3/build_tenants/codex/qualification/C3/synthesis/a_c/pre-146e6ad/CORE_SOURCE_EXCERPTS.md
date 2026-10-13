## Foundational commitments

This section is the owning locus of F1–F6 in this method realization; the
Product authority declared above is the context's semantic authority.
They do not rename the separately scoped authority concepts imported below.

| Commitment | Premise and standing | Distinction retained |
|---|---|---|
| F1 Purpose | Adopt a selected outcome and adequacy relation for purposeful construction. Value choices come from the purpose owner. | A local successful operation need not satisfy the selected outcome. |
| F2 Interpretation | Claims are interpreted on a declared subject and basis; unsupported interpretation remains unresolved. | Encoding or structural validity is not semantic evidence. |
| F3 Identity and current state | Work has scoped identity and observable persistent state; representation and historical observation are separate. | Re-entry need not recreate completed work, and history need not describe current effects. |
| F4 Typed composition | A composite conserves its outer contract's material relations under declared compatibility and loss. | Shared machinery does not merge owners, findings or authority. |
| F5 Finite capacity and total handling | Actor resources are finite; the selected control domain admits truthful handling of unknown, inadequate and interrupted conditions. | Total handling is not omniscience, universal idempotence or guaranteed solution. |
| F6 Evidence and authority | Evidence supports claims; operation and decision authority come from their bound owners. | A judgment or available tool is not permission. |

For this domain, these premises require a transformation contract to explain
what counts as an adequate result, which subject and interpretation it uses,
what state and material relations survive, which unknown outcomes it admits,
and which effects or dispositions are authorized. Only material bindings are
required by the selected instance. The contract vocabulary is defined once in
[the library's foundational contract](TRANSFORMATION_LIBRARY.md#foundational-contract).
A function in another domain retains its own dependencies; these commitments do
not add a purpose field or a mandatory record to every calculus entity.

A specialization fixes additional types, predicates, policy and adoption
conditions without discarding its selected generic contract's guarantees. The
[work/recovery argument](TRANSFORMATION_LIBRARY.md#workrecovery-specialization)
shows the premises, consequences and independent choices for one complete chain.
Each deciding family states the corresponding premises, consequences and
additional choices at its own use contract. A family without that argument
remains an unsupported specialisation.


## Result algebra

A result makes a claim about one predicate on one subject and basis. Its core
record contains the predicate, exact subject and basis, verdict, performance,
original qualified domain outcome, supporting evidence and citations, unresolved
obligations and material effect observations. A reference can carry these when
its resolution preserves their meaning and availability. This is a semantic
contract, not a mandatory serialization format or additional work carrier.

The verdict has exactly these values:

| Value | Meaning for the bound predicate |
|---|---|
| `satisfied` | Admissible evidence establishes the predicate under its declared evaluation rule. |
| `falsified` | Admissible evidence establishes a counterexample or failure of that predicate. |
| `indeterminate` | The available admissible evidence does not decide the predicate. |
| `out_of_frame` | The predicate is outside the evaluation's bound scope or capability; it is not silently omitted from the wider obligation. |
| `invalid_basis` | The subject, governing basis or required interpretation is invalid for the claimed evaluation. |

Performance records whether the named predicate's declared evaluation was
actually undertaken; it is `performed`, `not_performed` or `unconfirmed`.
The activation identifies that evaluation separately from dispatch, admission
or the work being assessed. Retain the observed extent, interruption and
conclusion in its outcome and evidence. The legal pairs are:

| Performance | Permitted verdicts | Meaning |
|---|---|---|
| `performed` | Any of the five verdicts | Evidence establishes that the evaluation was undertaken, including a scoped basis or capability diagnosis. Its extent and conclusion remain separate facts. |
| `not_performed` | Any except `satisfied`, with the evidence condition below | Evidence establishes that the evaluation was not undertaken. Dispatch or admission alone does not establish performance. |
| `unconfirmed` | Any except `satisfied`, with the evidence condition below | Whether the evaluation was undertaken is not established. |

An interruption does not erase evaluation already undertaken or admissible
evidence obtained. A suite aborted after a witnessed failure is performed with
that partial extent and falsifies “all tests pass”. A completed load test that
cannot generate its required load is performed but indeterminate on the
requested service-performance predicate. Neither case is a never-run test.
Satisfaction still requires all evidence and completion conditions selected by
the predicate's evaluation rule; performed alone proves none of them.

When the selected evaluation was not undertaken or its performance is
unconfirmed, separately admissible counterevidence to its bound predicate can
still establish falsified; an established basis or scope diagnosis can likewise
establish invalid_basis or out_of_frame. The result identifies that independent
support without inventing execution. Without deciding support it is
indeterminate. An absent return establishes neither non-performance nor an
undecidable evaluation: retain the missing slot and what is actually known.

A missing required judgment stays an absent coverage slot, with the known
performance fact or its uncertainty; it is not a fabricated child result. A
performed but undecidable evaluation differs from a known unperformed one and
from unconfirmed execution. A failed admission check can conclude while
downstream work does not. The plan fixes which predicates are required; a
precondition is evidence for its dependent evaluation unless the plan separately
requires that precondition as a predicate. A concluding basis/scope diagnosis
on P reports invalid_basis/out_of_frame on P with its supporting evidence; a
different admission predicate is not silently substituted for P. An aborted
procedure does not erase separately authenticated counterexamples observed
during the attempt. Every result projection preserves these
coordinates and the original predicate; a verdict alone is an insufficient
handoff where performance is material.

An effect observation is `not_requested`, `not_started`, `completed`, `partial`,
`reverted` or `unknown`, on its declared observation boundary. These values describe the selected effect and observation
boundary, not the predicate verdict. `not_started` needs evidence that the selected effect did not begin, including
an authenticated rejection before mutation. Transport dispatch alone proves
neither effect completion nor absence; `unknown` includes a lost acknowledgment
after possible execution.
`reverted` means that at least one part began and every begun part is observed to have been reversed within
the declared boundary, with the reversal and any unstarted remainder retained
as evidence. For every effect value, the boundary includes each material part
the operation may have affected under its supported operating model and any
observed departure, whether requested or unintended. Irreversible messages or
other material external effects cannot be omitted to improve a result.
`partial` means an observed
completed part and an observed unexecuted or reverted remainder.
If any material remainder has unknown completion, the state is `unknown`,
retaining the completed parts as evidence. An effect can be completed while
the intended product outcome is falsified.
An empty local log or discarded context does not establish no effect.
`not_requested` states an established effect-free scope under that operating
model; lack of a request alone is insufficient. A material possible unintended
effect without sufficient observation is `unknown`.

A refined value is the pair of original domain outcome and cause in its
declared reason domain, including an explicit missing-reason case. A domain
refinement preserves that qualified original outcome and supplies a
total, reason-sensitive map into this record. If the original outcome is too
coarse to determine a verdict, its required reason distinguishes the cases; a
consumer cannot guess from a word such as `refused`, `ready` or `accepted`.
A missing required reason maps the claimed predicate to indeterminate and
leaves that contribution inadmissible as deciding support for its slot;
retain its raw outcome and unresolved authentication. Its claimed predicate
remains indeterminate until admissible evidence decides it. Independently
established counterevidence or a basis/scope diagnosis uses the legal pairs above
on that same bound predicate; it does not invent execution or completion.
Requested or material possible unintended effects without sufficient observation
are unknown, never defaulted to not_requested. Unconfirmed evaluation performance
stays unconfirmed. Domain meaning stays with its domain owner.
No refinement turns failure, undecidability, non-performance or unknown effect
completion into greater standing. A new result over a different predicate does
not overwrite the earlier result.

Candidate availability, candidate fitness and authorised acceptance are three
predicates. `candidate_ready` can satisfy availability while fitness remains
falsified or unassessed. A lawful yield can satisfy the selected yielding
contract while product completion remains unresolved. A decision result binds
the predicate “disposition D on subject S at basis B was made under mandate M
by its bound authority”. A lawful rejection can satisfy that predicate while
candidate fitness remains undecided. Recording the decision is not its authority.
A not-applicable classification needs a supported applicability judgment; it is
never a synonym for a missing evaluation.

A stop reports the actual destination or task predicate through this record,
with its reason, observed effects and outstanding obligations. Its verdict
is indeterminate when the outcome remains undecided, falsified when admissible
evidence defeats that predicate, or the established scope/basis diagnosis.
Lawfulness of stopping is a separate decision predicate.

## Result conjunction

Conjunction evaluates whether all required predicates and their material joins
hold on the declared composite subject and basis. It retains the contributing
results, their authentication and predicate mapping, known failures and their
citations, uncovered required coverage, uncertain effects and invalidators.
The aggregate is another result in the same algebra, with those components
available through sufficient references. Its summary never replaces them.

The aggregate evaluation has performance performed when its combining rule is
applied; this does not change component performance. The composite declares its
effect boundary and the selected effect parts within it. First resolve a current
observation for each part, retaining the contributing observations, identities,
ordering and any supported supersession. A later timestamp alone is no
supersession argument. Conflicting or insufficient observations leave the part
unknown. Every material part that may have been affected, including an
unrequested part or one owned by an absent evaluation slot, is unknown without
sufficient observation unless evidence establishes not_started. Only an
established effect-free scope gives not_requested; no request is not that proof.

Sequential stages can affect the same part. Their local completion labels are
not inputs to the composite join until mapped onto that part's observed state
at the composite boundary. A completed deployment followed by its completed
rollback is reverted for the deployment effect; a subsequent completed
reapplication is completed there. The historical rollback remains evidence.
The declarations retain every material external part, including irreversible
ones; a local reversal cannot silently remove them from the scope.

Over the resulting disjoint part observations: any unknown gives unknown;
all not_requested gives not_requested; completed with only completed or
not_requested gives completed; not_started with only not_started or
not_requested gives not_started; reverted with only reverted, not_started or
not_requested gives reverted; every remaining fully observed mixture gives
partial. Retain each observation's part and contributing components. The combining
operation's own lack of mutation cannot label an effectful composite not_requested.

First authenticate each contribution against its producer, subject, basis and
required plan membership. An unauthenticated claim cannot discharge an
obligation. A missing planned judgment remains an absent slot with its known performance
fact or uncertainty; required coverage outside an authenticated plan remains
uncovered. These are separate
conditions. An invalid contribution does not erase an independently
authenticated finding.

For an interpretable composite predicate and governing basis:

1. Any authenticated, applicable falsification of a required predicate or material join makes
   the conjunction `falsified`. Missing or undecidable other coverage remains
   explicit alongside it.
2. With no such falsification, an invalid required basis prevents satisfaction
   and yields `invalid_basis`; a required out-of-frame judgment yields
   `out_of_frame` when no invalid basis applies.
3. Otherwise any unresolved applicability, missing evaluation, undecidable
   predicate or undecided material join yields `indeterminate`.
4. `satisfied` requires every applicable obligation and material join to be
   authentically satisfied, with coverage itself established. An empty list
   proves nothing unless the declared required set is established as empty.

The composite declaration distinguishes its admission conditions from the
material joins of the predicate being evaluated. Each relation has one of
those roles in that evaluation. A failed admission condition prevents an
interpretation; a false required join is counterevidence within an admitted
interpretation. The result names that declared role instead of reclassifying a
known failed join as a missing basis. If the composite subject or governing basis itself cannot be interpreted, the
aggregate is `invalid_basis`; independently valid component failures and their
scope remain exposed. This does not pronounce them false or forgotten.
Effect uncertainty prevents satisfaction where the predicate requires a known
effect state. An unrelated effect does not automatically invalidate a different
predicate; the dependency relation must justify its relevance.

A declared operator states its truth and falsity conditions over exact leaf
predicates and joins. On its fully decided admitted domain, those conditions
are disjoint and exhaustive, including failure of a required join. An
overlapping, incomplete or uninterpretable operator declaration is invalid_basis.
Unresolved well-formedness makes the operator result indeterminate and supplies
neither satisfaction nor falsification; independently valid leaf results remain
visible. Once well-formedness is established, its result can be satisfied only when authenticated
evidence establishes its truth condition and the material joins and coverage
needed for that condition. It can be falsified only on an established falsity
condition. Otherwise a material invalid_basis yields invalid_basis, a material
out_of_frame yields out_of_frame when no invalid basis applies, and every
remaining undecided case is indeterminate. Only dependencies needed to decide
the bound predicate enter that ordering. Authentication, original failure
retention, performance and effect composition remain the rules above. Negation
or disjunction evaluates a different predicate; it cannot erase a failed leaf
or pass that result off as conjunction of all leaves. A first-nonfailure rule
cannot turn an undecided fallback into success.

Sequential composition records an unreturned dependent evaluation as an absent
slot, retaining its observed performance, extent and missing conclusion. A lawful regrouping requires the same interpretable composite basis, required
leaf predicates, joins, normalized effect parts and authentication, with no intermediate basis failure
hidden by the grouping. On that fixed domain, retained component sets combine
by union, the conjunction precedence is associative, and the effect join over
normalized disjoint parts is associative. This grants no associativity to an
arbitrary declared operator; regrouping it requires preservation of the same
outer predicate and its own demonstrated associativity law. An invalid
intermediate join is a failed premise of that rewrite, not evidence that every
arbitrary grouping is equivalent. Reordering
operations additionally needs an effect-independence law; associativity alone
supplies no such permission.

Sequential operations compose under their applicable owning contracts:
[UP-016/017](DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)
for design composition and [AC-016](AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
within a_c. Their returned result applies the operator rule above to the
declared outer predicate using
its preservation argument and the retained component results. For a pipeline
whose contract requires every stage postcondition, this is the conjunction
above; a recovery path need not require a failed earlier test to become true.
Unexecuted stages remain coverage facts, with no invented evaluations. A
sequence without an established outer interpretation or join returns the
applicable unresolved or invalid-basis result rather than a guessed success.

## Workspace and context

The workspace is the continuing material state of the construction, including
its authoritative requirements, work products and durable records. Material
external state is observed through its owning interface. The actor's context is
a bounded account acquired from these sources. It is fallible and disposable.
Acquisition observes the subject and basis the activation actually binds,
including frozen snapshots where selected. Admissible contrary current evidence
reopens affected claims through their drift and re-entry rules; it does not
silently select a different basis. Current observations correct stale beliefs;
they do not grant permission to
change a requirement to match the implementation. What exists and what must
exist remain different questions on the same truth surface.

Acquisition binds the current task, subject, destination constraints, authority
and relevant observations. It includes known material dependencies directly or
through declared available inputs, and excludes irrelevant material unless
needed to establish irrelevance. A rule packet without its current subject is
insufficient. A digest without accessible meaning is insufficient. A summary
without supported freshness cannot override its owner. Absence from a partial
projection, sparse checkout or empty local record is not evidence of absence
in the bound subject; acquire its authoritative source or retain indeterminacy.

An observation binds its source and observation time or version. Where the
subject may change between observation and effect, the binding supplies the
material freshness or concurrency condition: re-observe, compare a revision,
use a protected snapshot or return uncertainty. No universal isolation scheme
follows. The selected operation cannot assume a stale read is still current.

The cycle is acquisition from current state, a bounded authorised operation,
observation of its result, and acquisition for the next operation. Results use
[the result algebra](#result-algebra). The cycle can stop after any operation
without inventing completion. Private context can be discarded between cycles;
resumption reconstructs sufficient context from the continuing workspace and
authoritative inputs. It neither erases progress nor requires a transcript of
every earlier activation.

Reuse requires supported applicability: the same claim scope, adequate current
basis and evidence, valid dependencies and required independent authorship.
Changed support reopens the affected dependent claims. Unchanged independent
work remains usable; when dependency independence cannot be established, inspect the
wider affected scope. A stored green label is not a validity argument.

Before repeating an operation with uncertain effects, observe or reconcile
sufficiently to decide the next dependent action. A granted idempotent operation
may be retried where its idempotence is established for that subject and effect.
Otherwise select another permitted action or return the unresolved result.
A workspace that retains partial progress does not make every operation
idempotent. An event log may support observation, audit or domain-specific
reconstruction; it is not universally the work state or a compulsory recovery
algorithm.

## Bounded construction

A describes current material state and what is justified about it. Z is the
selected set of constraints and acceptance conditions; many states may satisfy
it. Intent, Product and Specification refine Z under their owning authority.
Write material intermediate states as S0 → S1 → …, reserving Z for the
destination constraint set and naming a satisfying endpoint separately. A
transition binds its preconditions, permitted effects, result predicate and
outer obligations. Where finite context or attention prevents one adequate
activation, refine the task into supported transitions over those states.

Finite capacity motivates bounded acquisition. Purpose chooses the outcome;
identity identifies the work; compatibility and assurance determine which
transitions compose. These are additional premises, not consequences of a
resource bound. Decomposition preserves all material outer obligations and
the joins between parts. Local success establishes the outer outcome only
when the required coverage and preservation argument hold.

A total control contract supplies a response for every admitted control state,
including unavailable input, unknown world conditions, failed preconditions,
partial effects, exhausted capability and revoked or exhausted authority. Its
outcomes use the core result algebra. Its alternatives may include repair,
re-entry, refusal, yielding or termination under the actual grant. It does not
promise to solve every problem or make an external process terminate.
Deterministic, probabilistic and human operations retain their selected outcome
models; their enclosing control handles the observed result truthfully.

Progress is supported movement toward the selected destination. Useful discovery
can enlarge the known frontier; counts alone are no distance metric. Stopping
can be lawful without completion. Completion needs the required evidence and
acceptance conditions on the current candidate. Changing Z follows its owner
and cannot establish that the old destination was reached. Repeating a failed
relation needs a supported causal change; elapsed activity is no repair.

## Configuration

A configuration allocates operations and information to capable actors and
declares the material dependencies between their frames. It assigns effects
only within grants the allocator holds and may delegate. Its existing design
or frame record explains the allocation against operations, dependencies,
capabilities, assurance, resource limits and failure assumptions.
Finite context and attention, actor fallibility, communication costs and required
assurance constrain that allocation. They do not uniquely derive a hierarchy
or a fixed inventory of roles. An adequate configuration can use one actor,
peers, a hierarchy or supported adaptive allocation.

Producing, checking and accepting remain different responsibilities even where
one actor is permitted to perform several. Required independent review retains
its authorship and evidence conditions; a new context alone does not supply it.
Roles acquire authority from their grants, never from their names. Functional
decomposition, communication, authority and evaluation dependency are distinct.

The optional [Executive arrangement](STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action)
specialises this contract for longer-term delivery through bounded worker
results. Its procedure and grants belong to that profile. Every allocation and reconfiguration, fixed or adaptive, preserves material
dependencies, outstanding obligations, observed and uncertain effects, admitted
authority and required independence. A claim that one arrangement is optimal names its
objective, constraints, comparison scope and evidence.

## Core contract derivations

| Deciding family | Foundational premises | Conditional consequence | Additional choice and owner |
|---|---|---|---|
| Result record | F1 selects the predicate; F2 binds interpreted evidence; F6 separates judgment from authority | A useful handoff must retain which claim was actually decided and cannot infer permission from success | This member chooses five verdicts plus explicit performance and effect coordinates; domain owners supply finer predicates and evidence rules |
| Result conjunction | F2 authenticates claims; F4 preserves all required relations | A failed required predicate defeats conjunction; missing coverage cannot supply success; failures and uncertainty must remain available | This member chooses the stated aggregation precedence and effect join for interpretable conjunction; other operators retain their declared predicates |
| Workspace and context | F3 supplies persistent observed state; F2 makes the account revisable; F5 bounds context and attention | Continuity requires sufficient reacquisition, not preservation of a private belief; stale support must be reconsidered | Domain owners choose observation/freshness protocols and any stronger replay duties; the execution binding selects measurement |
| Bounded construction | F1 supplies Z; F3 identifies changing work; F4 requires preserved outer obligations; F5 bounds an activation | Large work needs supported refinement or an explicit stop; local success alone does not prove the destination | Spec Method owns re-entry and Product progress, Design owns concrete total control domains, and grants bound permitted responses |
| Configuration | F4 supplies task dependencies; F5 bounds actors; F6 supplies grants; the task supplies fallibility and assurance assumptions | Allocation must conserve dependencies and required checks within capability; no unique hierarchy follows | Operational profiles and tenant designs choose topology, allocation, communication and assurance mechanisms |

These are conditional arguments in the selected methodology domain. The table
neither proves completeness for the world nor selects a universal executor.
