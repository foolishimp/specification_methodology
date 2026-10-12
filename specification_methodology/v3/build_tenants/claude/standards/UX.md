# UX

Tier 3. An optional profile for realising UX surfaces: the Elm process
model with typed State, Msg, Update, View, Cmd and Sub; the boundary
between UX messages and admitted product carriers; the state transition
law; the effect membrane; carrier binding; view continuation and the
Msg-replay proof; view shape; type sharing; the accessibility minimum;
realisation discretion; adoption with the scaffold and exemption law and
UX sprint compliance escrow; the failure patterns; the review questions;
and the mapping of this profile's results to the core algebra. It refines
[DESIGN_MODULE](DESIGN_MODULE.md) for modules that realise a UX surface
and imports [FOUNDATIONS](FOUNDATIONS.md), [ACTIVATION](ACTIVATION.md),
[EVALUATION](EVALUATION.md), [SPEC_METHOD](SPEC_METHOD.md) and
[TICKETS](TICKETS.md) by reference, defining none of their objects again:
the result algebra is ACTIVATION §3; ambiguity governance SPEC_METHOD §5;
the sprint boundary SPEC_METHOD §4; sprint mechanics, compliance escrow
and close classification TICKETS §3; functional bias without language
mandate DESIGN_MODULE §4; the effect edge and the other realisation rules
DESIGN_MODULE §10. The graph-execution profile is named through
[PROFILES §2](PROFILES.md#2-graph-execution); its member is not on this
branch and is not linked (P6, P2).

This profile's own terms are UX surface, State, Msg, Update, View,
ViewTree, Cmd and Sub (§4), view-local ephemera (§5), effect membrane
(§6), product-truth-changing message and admitted product carrier (§3),
Msg-replay test and Msg-replay proof (§8), scaffold and exemption record
(§12) and UX sprint (§12). AssetSurface, graph function, workorder and ABG
are the graph-execution profile's terms, used here as that profile names
them. Binding declared under PROFILES §1 (new; it reads TICKETS' tier-2
generalisation back to this profile's objects so the escrow law has an
exact subject on a UX surface): where TICKETS §3 Compliance escrow names
"replay proof for product-meaningful user-interface interactions" and
"changed public published-function or public carrier contracts", a UX
surface governed by this profile binds them to the Msg-replay proof of §8
and to the AssetSurface contract or equivalent typed product contract of
§7. Direction: profile to tier 2; preserved meaning: the tier-2 escrow law
applies unchanged to the bound objects; narrowed scope: UX surfaces this
profile governs; invalidation: a change of this profile's definition of
the replay proof or of the bound contract re-evaluates the binding (P1,
P6).

Every clause names the principle that requires it (P0 to P6, FOUNDATIONS
§3; C is proposed as P0). The predecessor's "must" is written in the
indicative; its "should", "may", "may not", "recommended", "typically",
"mandatory", "optional", "allowed", "at least" and "non-normative" keep
their force. A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/UX_METHOD.md` and is provenance
only; every predecessor row received here is restated in this text, and
nothing here depends on that cut to be applied.

## 1. Position

This profile exists to make one instruction precise: "using the UX
profile, build this UI surface" (P2; rc.2 #1-position). It adopts the Elm
Architecture (TEA) as its constitutional process model: the view is a
pure projection of typed state; state transitions are pure reductions
over typed messages; side effects are values the reducer describes and a
declared effect membrane interprets; the runtime owns lifecycle and the
view does not own continuation (P0, P1). The view is not a state owner.
Stateful local mutation in views, two-way bindings without action
emission, and effect handlers used as controllers are violations of this
profile even when the surrounding ecosystem conventionally accepts them
(P6).

### Authority

When a product, ticket, design module or review adopts this profile for a
UX surface, this profile is the sole UX realisation authority for that
surface (P6; rc.2 #1a-constitutional-authority-rule). Project-local ADRs
may choose the stack; they may not weaken the process model. Existing
code, component-library convention, screenshots, comments, design
history, prototype behaviour and generated artifacts are evidence only
and do not override this profile (P6). If this profile appears ambiguous
in a concrete case, the surface fails closed under SPEC_METHOD §5: the
work either satisfies the stricter interpretation, reprices through the
governing constitutional method, or records a scoped exemption in the
design module before implementation proceeds (P5, P6; §15 states the
result).

## 2. Role and composition

SPEC_METHOD defines constitutional process and lawful re-entry; the
graph-execution profile defines graph-native constructive carrier law;
DESIGN_MODULE defines deterministic module-level realisation discipline
(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
additional rules a module needs when it realises a UX surface (render
purity, state-transition algebra, effect-membrane discipline and
accessibility minimums) under the Elm process model. It does not
duplicate DESIGN_MODULE: where the parent already governs (immutability,
totality, effect-edge discipline, no semantic centre, coupling;
DESIGN_MODULE §10), this profile cites and extends it; where UX has
concerns the parent does not address (render lifecycle, browser events,
layout, accessibility), this profile is authoritative (P6, P4a).

This profile composes with the upstream members per surface (P4a, P0;
rc.2 #3-method-composition):

- when a module realises a UX surface, DESIGN_MODULE and this profile both
  apply, and its design module reads both;
- when a module realises a non-UX surface, only DESIGN_MODULE applies, and
  its design module ignores this profile;
- when a graph-execution product publishes a projection or query surface
  that includes UX, this profile governs that surface's realisation.

The composition rule: the graph-execution profile answers what
graph-native shape the product takes; DESIGN_MODULE what realisation
discipline the modules follow; this profile what additional discipline UX
surfaces follow (P6).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).

### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).

## 3. Product truth and admitted carriers

UX surfaces are projection and control surfaces: they render admitted
truth and emit typed messages (P6, P0;
rc.2 #3a-ux-projection-and-constructive-carrier-boundary). A UX-local Msg
may govern view-local concerns such as expansion state, sort order,
filter text, focus movement or draft input. A Msg that changes product
truth is not merely a UX concern. Product-truth changes include:

- writing, creating, moving or deleting assets;
- changing Context, selection authority, pinning or global product state;
- spawning, attaching or resuming sessions;
- dispatching agents, jobs, workorders, graph calls or runtime commands;
- changing closure, approval, continuation, lineage, provenance or
  evidence;
- publishing, accepting, rejecting or superseding product records.

Such a message maps to one admitted product carrier (P6, P4a):

- an AssetSurface action;
- a published graph function or lawful graph-function composition;
- a workorder, job or runtime command admitted by the product's design;
- an ABG event or command boundary where ABG is the runtime authority;
- another typed product contract named by the design module.

The UX layer does not become the hidden constructive carrier. If no
admitted carrier exists for a product-truth-changing message, the UX
surface is blocked until the carrier is authored or the requirement is
repriced (P6, P5; §15 states the result).

## 4. Process model

The constitutional process model is the Elm Architecture (P0, P1;
rc.2 #4-process-model-elm-architecture):

- State: the typed state shape, held by the runtime, not by the view;
- Msg: the typed message algebra naming every action a user or system can
  emit;
- Update: the pure reducer of signature `(Msg, State) → (State, Cmd)`; it
  describes side effects as Cmd values and does not perform them;
- View: the pure function of signature `State → ViewTree`; given the same
  state, it produces the same output;
- Cmd and Sub: typed descriptions of side effects to schedule and of
  external sources to subscribe to, interpreted by the runtime at the
  effect membrane.

The runtime owns the loop (P0):

`current State → render View → user emits Msg → Update produces new State and Cmds → runtime interprets Cmds → repeat`

This loop is the Elm Architecture and the constitutional process model of
UX work under this profile (P1).

### Process model without stack mandate

The process model is the Elm Architecture; the implementation stack is
the project's choice, recorded in its design module. This mirrors
DESIGN_MODULE §4 Functional bias without language mandate: the process
model is constitutional and not negotiable; the stack is project-local
and free, provided it preserves the model (P1, P6;
rc.2 #4a-process-model-without-language-or-framework-mandate). Any
realisation that preserves §4 to §8 is compliant with this profile.
Examples (non-normative):

- a language-integrated reducer runtime, which enables typed state,
  message, update, command and view relations as native runtime
  capabilities;
- a typed reducer with an effect interpreter, which enables a
  host-language UI stack to preserve pure update and an explicit effect
  membrane;
- a reactive-signal realisation behind a reducer, which enables reactive
  projection while forbidding signal mutation outside the reducer;
- a server-rendered hypermedia realisation, which enables server-side
  state derivation as the reducer and uses the request and response
  boundary as the effect membrane.

Constitutionally rejected: any realisation that lets the view own state
continuation, performs side effects in render code, mutates state outside
a typed reducer, or carries multi-step view-local state machines that
bypass Msg. Two-way binding without Msg emission, imperative DOM
manipulation in render code, and effect handlers used as controllers are
violations regardless of stack (P6). A project that selects a framework
records the choice in its design module with a short justification of how
the framework preserves the §4 process model. The profile does not rank
frameworks; it tests realisations against §4 to §8 (P1).

### Realisation discretion

The profile is opinionated about the process model and not about the
realisation stack (P1, P2; rc.2 #12-realization-discretion). The project
chooses:

- the language;
- the framework or runtime;
- the state-container library, if any;
- the effect-interpreter mechanism;
- the runtime validator, if any;
- the build, bundling and deployment toolchain.

The project records its choices in the design module with a short
justification of how each choice preserves the §4 Elm process model and
the §6 effect-membrane rule. The profile does not rank stacks; it tests
realisations. A realisation is compliant with this profile when §4 to §10
hold under inspection and the §13 failure patterns are absent (P6, P1).

## 5. State transitions

State changes through typed messages applied by the pure reducer, the
Update of §4 (P4a, P1; rc.2 #5-state-transition-law). A UX surface
declares:

- its State shape;
- its Msg algebra;
- its `Update : (Msg, State) → (State, Cmd)`;
- its Cmd algebra;
- its Sub algebra when the surface subscribes to external or runtime
  events.

Each Cmd declaration names (P5, P4b):

- the effect kind;
- the typed input payload;
- the admitted carrier or external boundary it targets;
- the success Msg emitted back to the reducer;
- the failure Msg emitted back to the reducer;
- any deterministic correlation key required for replay.

The reducer is pure: it does not perform I/O, log to side channels or
mutate global state. Effects scheduled by Cmd are interpreted by the
runtime at the effect membrane (§6) (P0, P1).

View-local ephemera (open or closed flags, hover state, draft input) may
be held in implementation-local state cells where the framework provides
them, but only when the value is genuinely view-local: not observed by
other views, not part of the product's state surface, and not
consequential after the view unmounts. Product-meaningful state goes
through the reducer without exception (P6, P3). The discipline test for
whether state belongs in the reducer or in view-local ephemera: if losing
the value on unmount changes the product's behaviour or another part of
the UI's view, it belongs in the reducer (P3).

## 6. Effect membrane

Side effects are isolated to a declared effect membrane, which refines
DESIGN_MODULE §10 Effect edge for UX surfaces (P0, P5;
rc.2 #6-effect-membrane-rule). The membrane interprets Cmd values
produced by the reducer and translates side-effect outcomes back into Msg
values delivered to the reducer. Inside the membrane, I/O, subscriptions
to external sources, and imperative interop with the host platform (DOM,
file system, native APIs) are allowed. Outside it, in render code, in
pure helpers consumed by render, and in the reducer, there is no I/O, no
subscription and no imperative platform manipulation (P0).

The membrane has one job: interpret declared Cmd values. It is not where
logic lives. Branching, conditional state derivation and multi-step
business decisions belong in the reducer; the membrane interprets a
single declared Cmd per effect (P6). A platform-specific effect handler,
whatever name the chosen framework gives it (`useEffect`,
`createEffect`, `onMount`, `subscribe`, a server-action handler), is part
of the membrane only when it interprets a declared Cmd. A handler that
contains conditional logic deciding state transitions is a violation: the
logic moves to the reducer, and the handler interprets one Cmd (P6, P1).

## 7. Carrier binding

When the product publishes typed asset surfaces under the graph-execution
profile's carrier law and the local product's design, a UX surface binds
to one or more AssetSurface contracts as its data source and action
target (P6, P3; rc.2 #7-assetsurface-binding-rule). Binding requirements:

- the surface's State is derived from AssetSurface projections, not from
  a UX-local re-declaration of the asset shape;
- its product-truth-changing Msg variants map one to one to AssetSurface
  action-registry entries, or wrap them through a documented projection
  with no hidden semantic change;
- UX-local Msg variants are reserved for view-local concerns (open or
  closed, sort order, filter input);
- selection within the surface emits a Context update, or equivalent,
  consistent with the product's selection contract;
- writes from the surface go through the AssetSurface action registry,
  not through direct file or service calls.

This is the rule that produces strong functional consistency between
front end and back end: the same typed contract is the ground truth on
both sides (P1, P3). If the product does not publish AssetSurface
contracts, the design module names the equivalent typed contract and
applies the same binding law to that contract. Absence of an admitted
contract blocks product-truth-changing UX actions (P6, P5).

A prompt for UI or operator-surface work must carry the governing UX law
as a derived surface or projected frame of this member, rather than
require the worker to rediscover it from the raw member. If a worker
changes product truth through UI behaviour, the prompt must name the
admitted carrier and action path. If the prompt cannot identify that
carrier and action path, the correct result is a block or re-entry, not
local UI invention (P6, P5; provenance rc.2
authority_compressions/ux_method.compressed.md, a claim no rc.2 body
states; prompt construction is
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).

## 8. Continuation and replay

In the graph-execution profile the runtime owns continuation (PROFILES
§2) and the product is a cooperative bounded-step subsystem. The UX
twin: the view does not own state continuation (P0, P6;
rc.2 #8-ux-twin-of-odd-115a-view-does-not-own-continuation). State
transitions flow through declared Msg actions interpreted by the reducer.
A view does not:

- decide on its own what the next state will be after a user event;
- chain several state updates locally without emitting them as separate
  Msg values;
- carry hidden inter-event state in refs, closures or module-level
  variables.

If a view appears to need a multi-step local state machine, that machine
belongs in the reducer as part of State, with explicit Msg transitions
between phases; the view becomes a pure projection of which phase it is
in (P1). The discipline test is the Msg-replay test: can the view's
behaviour be replayed by replaying its Msg log against an empty State? If
the answer is no, continuation has leaked into the view (P4b).

### Msg-replay proof

Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement). A
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

## 9. View shape

A view is a pure function from typed state to a view tree (P1;
rc.2 #9-view-shape-rule). The view:

- accepts typed input (state, props, context);
- returns a typed view tree;
- declares its consumed inputs explicitly;
- does not capture mutable state in closures across renders;
- does not read from sources outside its declared input.

Whether the implementation expresses this as a function, a function
component, a template, a server-rendered handler, a signal-derived
expression or another framework-specific shape is a stack decision
recorded in the design module. The constitutional rule is the function
signature `State → ViewTree` and the absence of side effects in the body
(P1, P0). A view that depends on out-of-render mutation, for example a
ref written from inside an effect handler and read during render,
violates §6 unless the mutation is part of the declared effect membrane,
for example a platform handle for imperative interop already named in the
design module (P6).

## 10. Type sharing

UX-consumed types come from the shared front-end and back-end contract
(P3, P1; rc.2 #10-type-sharing-rule). A UX surface does not re-declare
back-end record shapes; it imports them from the shared contract module,
typically the same package or a dedicated `contracts/` package.

Runtime validation is mandatory at every untrusted or out-of-process seam
(P6; it makes DESIGN_MODULE §4's preference for parsing and admitting
foreign data once at ingress an obligation at these seams):

- HTTP or RPC responses;
- MCP payloads;
- file-loaded records;
- websocket or event-stream messages;
- agent or worker outputs;
- URL, storage, clipboard or browser integration payloads.

The project uses a typed-schema mechanism so that the same type
definition is the source of both compile-time types and runtime
validators; the mechanism choice is project-local. Compile-time
TypeScript alone is not sufficient at these seams (P6, P1). UX-local types
are allowed for view-local concerns: form input draft state, sort order
enums, filter strings. UX-local types do not shadow back-end types (P3).

## 11. Accessibility minimum

A UX surface that is the public face of a product capability declares
(P2, P6; rc.2 #11-accessibility-minimum):

- semantic structure (heading levels, landmarks, lists, or
  platform-equivalent affordances);
- keyboard or platform-equivalent navigability for every action that has
  a pointer interaction;
- focus management on dynamic content changes;
- accessibility annotations for any custom interactive element that lacks
  a native semantic equivalent;
- colour contrast at the project's declared accessibility standard (WCAG
  AA is the recommended default for web).

Accessibility is not optional for product capabilities. It is optional
for internal-only debug surfaces, and the design module records the
exemption (P2, P6). This section is intentionally minimal. Projects with
stricter accessibility obligations (regulated industry, public-sector
procurement) author a project-local accessibility refinement and cite it
from their design modules (P2).

## 12. Adoption

A project adopts this profile by (P6, P4b; rc.2 #13-adoption-guidance):

1. naming the profile in the project's UX-related design modules;
2. recording the realisation stack choice (§4 Realisation discretion) and
   the justification;
3. declaring the irreducible architectural carrier set and the structural
   carrier diagram the design profile requires (DESIGN_MODULE §6 and §7);
4. declaring the State, Msg, Update, Cmd and Sub shapes for each UX
   surface in the design module before implementation;
5. declaring the AssetSurface or equivalent typed-contract bindings (§7)
   the surface consumes and emits to;
6. naming the effect-membrane mechanism (§6) and the Cmd algebra it
   interprets;
7. naming the executable Msg-replay proof surface required by §8;
8. naming any §11 accessibility refinement the project requires;
9. noting any §9 view-shape or §6 effect-membrane exemptions explicitly.

Adoption is per project. A project may adopt this profile only for some
UX surfaces, for example the production UI but not internal debug tools,
with the scope recorded in the design module (P2, P6).

### Scaffold and exemption

A UX surface is governed by this profile by default when any of these are
true (P6, P5; rc.2 #13a-scaffold-and-exemption-law):

- it is reachable from the product shell;
- it is used as proof for a ticket, requirement, design module, release or
  review;
- it can mutate product truth;
- it can spawn, attach, resume or dispatch work;
- it can change Context, selection authority, closure, continuation,
  evidence or provenance.

A scaffold, prototype, debug pane or temporary proof surface may be
exempt only when the design module or ticket records (P6, P4b):

- the exemption scope;
- the permitted operations;
- whether mutation is forbidden or explicitly bounded;
- a visible scaffold or debug label where user-facing;
- the authoritative surface that will supersede it;
- the retirement condition and owning ticket;
- the non-closure condition preventing release if the scaffold remains.

An exempt scaffold cannot become the production UX by accumulation. It is
retired, repriced into a governed UX surface, or kept outside product
closure (P4b, P6).

### UX sprint compliance escrow

UX is the primary governed use case for sprint compliance escrow. This
subsection is the profile's statement, which SPEC_METHOD §4 Sprint
execution boundary admits, of when that escrow is an appropriate cost
optimisation for UX; the generic escrow law and the close mechanics are
TICKETS §3 Compliance escrow and Close review (P2, P6;
rc.2 #13b-ux-sprint-compliance-escrow). A UX sprint may defer local UX
compliance proof during a short iteration window when per-change proof
cost is higher than expected correction cost. This is a cost-optimisation
rule; it does not weaken the UX process model (P2).

A UX sprint may escrow (P2, P4b):

- screenshots or walkthrough capture;
- visual review;
- copy, spacing, density and layout cleanup;
- accessibility review and remediation;
- Msg-replay proof updates for product-meaningful interaction families;
- design-module wording cleanup;
- trace cleanup between changed UX states and governing authority.

A UX sprint may not escrow (P6):

- product-truth-changing Msg variants that lack an admitted carrier;
- new or changed AssetSurface contracts or equivalent typed product
  contracts;
- new navigation, information architecture or selection authority that
  changes product meaning;
- runtime, governance, closure, continuation, lineage, provenance or
  evidence semantics;
- release criteria or method law.

If one of those appears, the sprint records the finding and the work
exits the UX sprint path through standalone repricing or sprint
supersession. The UX layer still does not become the hidden constructive
carrier (P6; §3).

A UX sprint should close when continued iteration is more expensive or
less trustworthy than review. Valid close triggers include (P2, P6):

- the declared timebox ends;
- accumulated changed states are too numerous for casual review;
- screenshots or walkthrough evidence no longer explain the current
  surface;
- interaction behaviour changed beyond visual polish;
- reviewer uncertainty makes more iteration unsafe without
  reconciliation.

UX sprint close is a forensic walkthrough: it reviews each changed
screen, state and product-meaningful interaction against the cited
authority (P6). Each finding takes one of the six classifications of
TICKETS §3 Close review (`accepted`, `local_paydown`, `design_reframe`,
`requirement_reprice`, `product_reprice`, `remove`); for a UX finding,
`accepted` reads as compliant with this profile and the cited design,
and `local_paydown` as local UX debt captured by a paydown ticket (P6,
P5). The sprint may close with explicit local paydown tickets only where
the debt is local to UX realisation and the governing method allows
follow-up. It may not close while product-truth carrier gaps, hidden
state continuation or authority drift remain unclassified (P6, P4b).

Closure under this profile for a product UX surface still requires the
§8 Msg-replay proof and the §11 accessibility obligations unless an
explicit exemption is recorded. The sprint can defer those obligations
during iteration; it cannot erase them (P4b, P6).

## 13. Failure patterns

A UX surface violates this profile when any of these are true (P6, P5;
rc.2 #14-failure-pattern):

1. render code mutates state directly (assignments inside the render
   body, mutating a prop or context value);
2. view-local state cells carry product-meaningful state instead of
   view-local ephemera;
3. an effect handler contains conditional logic that decides state
   transitions;
4. multi-step state machines live in the view rather than in the reducer;
5. mutable refs are read during render outside the declared effect
   membrane;
6. UX-local types shadow or re-declare back-end types instead of
   importing from the shared contract;
7. selection or action emission writes to file or network without going
   through an AssetSurface action;
8. view-shape exemptions (§9) are taken without a recorded design-module
   entry;
9. accessibility is omitted on a public product capability without a
   recorded exemption;
10. two-way binding emits no typed Msg action and the reducer is
    bypassed;
11. logic that should be a Cmd is implemented imperatively inside an
    effect handler;
12. the view's behaviour cannot be replayed by replaying its Msg log
    against an empty State;
13. a product-truth-changing UX message has no admitted carrier, graph
    function, runtime command or typed product contract;
14. external data crosses into UX state without runtime validation;
15. a scaffold or debug surface is reachable, mutating or used as proof
    without the exemption record of §12 Scaffold and exemption;
16. a project-local ADR, component convention or existing code pattern is
    used to weaken this profile;
17. a UX sprint claims closure while deferred proof, accessibility,
    carrier, scaffold or authority debt remains unclassified or
    un-ticketed.

Any of these is a violation of this profile. Repeated violations are not
normalised by usage; they are repaired or the surface is repriced (P6,
P4b).

## 14. Review questions

A UX surface review under this profile should answer (P6, P2;
rc.2 #15-review-questions):

1. What is the surface's State, Msg and Update?
2. What is the surface's Cmd and Sub algebra?
3. Which AssetSurface or equivalent typed contracts does it bind to?
4. Which product-truth-changing messages map to admitted carriers?
5. Where is the effect membrane, and what Cmd values does it interpret?
6. Is `View = f(State)` provably pure for this surface?
7. Can the surface's behaviour be replayed from a Msg log (the Msg-replay
   proof of §8)?
8. Are all UX-consumed types imported from the shared contract?
9. Are all out-of-process payloads runtime-validated before entering UX
   state?
10. Are view-shape, effect-membrane, accessibility, scaffold or debug
    exemptions documented?
11. What realisation stack is chosen, and how does it preserve the §4 Elm
    process model?
12. Does the surface honour the §8 rule that the view does not own
    continuation under user replay?
13. Does the design module include the design profile's carrier set and
    structural carrier diagram required for closure (DESIGN_MODULE §6 and
    §7)?
14. If the work used a UX sprint, did close review classify every deferred
    proof, accessibility, carrier, scaffold and authority finding?

If any of these cannot be answered, the design module is incomplete (P6,
P5).

## 15. Results of this profile

New clause. Purpose: the one-algebra rule of ACTIVATION §3, under which a
profile's own result or stop vocabulary declares a total mapping to the
five core members and adds none; the material relation is that this
profile's verdicts decide closure of a UX surface and enter composites
that consume only core members (P5, P6). Each verdict below answers its own question and maps as stated;
nothing is coerced to satisfied.

| Profile verdict | Question | Core member |
|---|---|---|
| compliant | do §4 to §10 hold under inspection with no §13 failure pattern present (§4 Realisation discretion) | satisfied; this row applies the stricter of the two compliance tests the predecessor states, which disagree (§4 Realisation discretion against the §12 compliance criterion); the choice is pending Jim's ruling and is not settled by this mapping |
| violation, including "constitutionally rejected" (§4) | is a §13 failure pattern present | falsified; the pattern present is the counterexample |
| replay proof passes or fails (§8) | does the proof reproduce the expected final State and Cmd sequence without a dependency §8 lists | satisfied when it passes; falsified when it fails |
| closure claimed without the §8 proof or the §11 obligations (§12) | does every product-meaningful interaction family carry its proof and the surface its accessibility declarations, absent a recorded exemption | falsified; the family or obligation without proof is the counterexample; inside an open UX sprint the gap is escrow and closure is not claimed |
| blocked for want of a carrier (§3, §7) | does a product-truth-changing message or action have an admitted carrier or typed contract | the surface's evaluation is falsified (§13 pattern 13); the construction step stops as ACTIVATION §3's `re_entry_requested`, core out_of_frame, naming the missing carrier, its owner in the product's design, and the re-entry (author the carrier or reprice the requirement) |
| fails closed (§1 Authority) | is the surface compliant where this profile is ambiguous for the case | the result of the stricter interpretation where that reading is fixed, satisfied or falsified; out_of_frame where the ambiguity leaves a term the claim depends on undefined, naming the term and its owner (ACTIVATION §3, first case); indeterminate only where the stricter reading is fixed and the admissible evidence cannot decide, naming the evidence that would; never satisfied by the ambiguity alone |
| design module incomplete (§14) | can each review question be answered from the design module | invalid_basis: the design module cannot support the review evaluation |

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of ACTIVATION §3, and "design module
incomplete" is not the construction availability member `incomplete`. An
exempt scaffold is a recorded scope (§12), not a result; evaluations
outside its recorded scope proceed under this table. The six close
classifications of §12 belong to TICKETS §3 and are not mapped here (P6).

## 16. Source dispositions

Rows of rc.2 UX_METHOD.md received by this member. Anchors are into rc.2
UX_METHOD.md; a locus is a section of this file unless another member is
named. Every conserved row is restated in this member's own text; a route
is provenance only. Generalisations recorded here: "UX_METHOD.md" and
"this method" are written "this profile"; "DESIGN_MODULE_METHOD.md",
"SPEC_METHOD.md" and "TICKET_METHOD.md" as DESIGN_MODULE, SPEC_METHOD and
TICKETS; "ODD_METHOD.md" as the graph-execution profile (PROFILES §2),
whose own terms (AssetSurface, graph function, workorder, ABG) this
tier-3 profile keeps; "WORLD_MODEL_METHOD.md" as WORLD_MODEL;
"method-compliant", "method violation" and "method closure" as compliant
with, a violation of, and closure under this profile. The predecessor's
section numbers are written as this member's: §4 to §10 keep their
numbers; §12 is §4 Realisation discretion; §13, §13A and §13B are §12 and
its subsections; §14 is §13; §15 is §14; §8A is §8 Msg-replay proof.

| Anchor | Disposition | Locus |
|---|---|---|
| #1-position | conserved; the one instruction, the four TEA statements, the view not a state owner, the three violations even where conventionally accepted | §1 |
| #1a-constitutional-authority-rule | conserved; sole UX realisation authority, ADRs choose the stack and may not weaken the model, the seven evidence-only kinds, fail closed with its three exits; ambiguity governance is SPEC_METHOD §5, pointed to | §1 Authority; §15 |
| #2-method-role | conserved; the three roles, the refinement with its four additions, no duplication with the five parent rules, the four UX-only concerns | §2 |
| #3-method-composition | conserved; the three per-surface cases, the three-answer composition rule | §2 |
| #3a-ux-projection-and-constructive-carrier-boundary | conserved; projection and control surfaces, the five view-local concerns, the six product-truth changes, the five admitted carriers, no hidden constructive carrier, blocked until authored or repriced | §3; §15 |
| #4-process-model-elm-architecture | conserved; the five elements with both signatures, the runtime-owned loop | §4 |
| #4a-process-model-without-language-or-framework-mandate | conserved; model constitutional and stack free, the DESIGN_MODULE §4 mirror, compliance for preserving §4 to §8, the four non-normative examples, the four rejected realisations and three stack-independent violations, framework choice recorded with justification, no ranking | §4 Process model without stack mandate |
| #5-state-transition-law | conserved; the five declarations, the six Cmd fields, the pure reducer, view-local ephemera with its three conditions at "may" force, product-meaningful state without exception, the unmount discipline test | §5 |
| #6-effect-membrane-rule | conserved; the membrane's two translations, the three allowed inside, the three forbidden outside, one job, logic in the reducer, the named handlers, the violation and its repair; stated as the UX refinement of DESIGN_MODULE §10 Effect edge | §6 |
| #7-assetsurface-binding-rule | conserved; the five binding requirements, the same contract on both sides, the equivalent typed contract, absence blocks | §7 |
| #8-ux-twin-of-odd-115a-view-does-not-own-continuation | conserved; the parent rule named through PROFILES §2, the three prohibitions, the state machine in the reducer, the Msg-replay test | §8 |
| #8a-msg-replay-proof-requirement | conserved; at least one proof per product-meaningful interaction family before closure, the six contents, the four failure dependencies, the no-effect proof at "may" force | §8 Msg-replay proof; §15 |
| #9-view-shape-rule | conserved; the five view properties, shape as a stack decision, the signature and no side effects, the out-of-render mutation violation and its membrane exception | §9 |
| #10-type-sharing-rule | conserved; shared contract, no re-declaration, "typically", mandatory runtime validation at the six seams, the typed-schema mechanism, compile-time TypeScript not sufficient, UX-local types allowed and not shadowing | §10 |
| #11-accessibility-minimum | conserved; the five declarations with WCAG AA as the recommended default, not optional for product capabilities, optional for debug surfaces with the exemption recorded, intentionally minimal, project-local refinement | §11 |
| #12-realization-discretion | conserved; opinionated about the model only, the six choices, recorded with justification against §4 and §6, no ranking, the compliance test over §4 to §10 and the failure patterns | §4 Realisation discretion; §15 |
| #13-adoption-guidance | conserved; the nine adoption steps, per-project adoption at "may" with the scope recorded; step 3's structural carrier diagram is pointed to DESIGN_MODULE §6 and §7 | §12 |
| #13a-scaffold-and-exemption-law | conserved; the five default-governance conditions, the seven exemption record items at "may be exempt only when", no production UX by accumulation and its three exits | §12 Scaffold and exemption |
| #13b-ux-sprint-compliance-escrow | conserved; the primary use case, the cost condition at "may", not weakening the model, the seven escrowable and five non-escrowable items, the exit and the hidden-carrier rule, the "should close" condition and five triggers, the forensic walkthrough, the six classifications pointed to TICKETS §3 with the UX reading of `accepted`, the paydown and no-close conditions, defer but not erase; the generic escrow law is TICKETS §3 and SPEC_METHOD §4, pointed to | §12 UX sprint compliance escrow; TICKETS §3 |
| #14-failure-pattern | conserved; the seventeen patterns, any one a violation, repair or reprice | §13; §15 |
| #15-review-questions | conserved; the fourteen questions at "should answer", an unanswerable question makes the design module incomplete | §14; §15 |
| #16-relationship-to-other-method-surfaces | conserved; the five relationships, the escrow condition, the world-model binding through §7, the read and ignore rule | §2 Relationship to other members; §2 |
| #17-non-goals | conserved; the six non-goals and their product-local home | §2 Non-goals |
| #18-canonical-compression | conserved; every determination of the compression is stated once where it governs: Elm model and DESIGN_MODULE refinement §1, §2; the model §4; view continuation and the replay test §8; stack recorded with justification and tested against §4 to §10 and the failure patterns §4, §13; sole authority §1; carriers and no hidden carrier §3; runtime validation §10; scaffolds §12; escrow and close review §12 | §1 to §13 |
