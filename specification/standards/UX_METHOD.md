# UX Method

**Status**: Draft
**Date**: 2026-04-26
**Amended**: 2026-04-26 — Reframed as constitutional adoption of the Elm Architecture as the UX process model. Removed the architecture tier table; replaced with a process-model-without-stack-mandate clause mirroring `DESIGN_MODULE_METHOD.md` §4. Genericized framework-specific terminology (state cells, effect interpreter, render functions) so the method does not assume React, Elm-the-language, or any other implementation stack.
**Governance**: Maintained by the methodology author.
**Scope**: UX realization method for graph-native ODD products with web, desktop, or thin-client surfaces. Refines `DESIGN_MODULE_METHOD.md` with rendering, state-transition, and effect-membrane rules specific to UI work. Does not govern back-end realization or non-UX module design.
**Relation**: Refines `DESIGN_MODULE_METHOD.md` for UX surfaces. Composes with `ODD_METHOD.md` (the view layer is a projection / query surface in ODD terms). Binds to `AssetSurface`-style contracts when the product publishes them. Does not replace `DESIGN_MODULE_METHOD.md`; an LLM agent or designer working on a non-UX surface need not load this method.

Use `GLOSSARY_GUIDE.md` for shared recursive-product terminology unless this method explicitly narrows a term.

---

## 1. Position

`UX_METHOD.md` exists to make one instruction precise:

`using UX_METHOD, build this UI surface`

The method adopts the **Elm Architecture (TEA)** as its constitutional process model:

- the view is a pure projection of typed state
- state transitions are pure reductions over typed messages
- side effects are values described by the reducer and interpreted at a declared effect membrane
- the runtime owns lifecycle; the view does not own continuation

The view is not a state owner.

Stateful local mutation in views, two-way bindings without action emission, and effect-handlers-as-controllers are method violations even when they are conventionally accepted in the surrounding ecosystem.

---

## 2. Method Role

`SPEC_METHOD.md` defines constitutional process and lawful re-entry.

`ODD_METHOD.md` defines graph-native constructive carrier law.

`DESIGN_MODULE_METHOD.md` defines deterministic module-level realization discipline.

`UX_METHOD.md` refines `DESIGN_MODULE_METHOD.md` with the additional rules required when a module realizes a UX surface — render purity, state-transition algebra, effect-membrane discipline, and accessibility minimums — under the Elm Architecture process model.

`UX_METHOD.md` does not duplicate `DESIGN_MODULE_METHOD.md`. Where the parent method already governs (immutability, totality, effect-edge discipline, no-semantic-center, coupling), `UX_METHOD.md` cites and extends it. Where UX has concerns the parent does not address (render lifecycle, browser events, layout, accessibility), `UX_METHOD.md` is authoritative.

---

## 3. Method Composition

`UX_METHOD.md` composes with the upstream methods on a per-surface basis:

- when a module realizes a UX surface, both `DESIGN_MODULE_METHOD.md` and `UX_METHOD.md` apply
- when a module realizes a non-UX surface, only `DESIGN_MODULE_METHOD.md` applies
- when an ODD product publishes a projection / query surface that includes UX (`§10` of `ODD_METHOD.md`), `UX_METHOD.md` governs that surface's realization

The composition rule is:

- `ODD_METHOD.md` answers what graph-native shape the product takes
- `DESIGN_MODULE_METHOD.md` answers what realization discipline the modules follow
- `UX_METHOD.md` answers what additional discipline UX surfaces follow

---

## 4. Process Model — Elm Architecture

The constitutional process model is the Elm Architecture:

- **State** — typed state shape held by the runtime, not by the view
- **Msg** — typed message algebra naming every action a user or system can emit
- **Update** — pure reducer of signature `(Msg, State) → (State, Cmd)`; describes side effects as `Cmd` values, does not perform them
- **View** — pure function of signature `State → ViewTree`; given the same state, produces the same output
- **Cmd / Sub** — typed descriptions of side effects to schedule and external sources to subscribe to; interpreted by the runtime at the effect membrane

The runtime owns the loop:

`current State → render View → user emits Msg → Update produces new State and Cmds → runtime interprets Cmds → repeat`

This loop is the Elm Architecture. It is the constitutional process model of UX work under this method.

---

## 4A. Process Model Without Language Or Framework Mandate

The process model is the Elm Architecture. The implementation stack is the project's choice, recorded in the project's design module.

This mirrors `DESIGN_MODULE_METHOD.md` §4 ("Functional Bias Without Language Mandate"). The rule is:

- the **process model** is constitutional and not negotiable
- the **stack** is project-local and free, provided it preserves the model

Any realization that preserves §4–§8 is method-compliant. Examples (non-normative):

- **Elm** itself — the canonical realization; the runtime is part of the language.
- **TypeScript with a typed reducer and a typed effect interpreter** — for example React paired with Redux Toolkit (or any pure-reducer state container) plus Effect-TS or a hand-rolled `Cmd` interpreter for the effect membrane.
- **Reactive-signal frameworks** (SolidJS, Vue 3 with Composition API, Svelte 5 runes) — method-compliant when the project layers a typed reducer + Cmd interpreter on top and forbids signal mutation outside the reducer.
- **Server-rendered hypermedia** (HTMX, Phoenix LiveView, Hotwire) — method-compliant when server-side state derivation is the reducer and the effect membrane is the request/response cycle.

What is constitutionally rejected: any realization that lets the view own state continuation, performs side effects in render code, mutates state outside a typed reducer, or carries multi-step view-local state machines that bypass `Msg`. Two-way binding without `Msg` emission, imperative DOM manipulation in render code, and effect-handlers used as controllers are violations regardless of stack.

A project that selects a framework records the choice in its design module along with a short justification of how the framework preserves the §4 process model. The method does not rank frameworks. The method tests realizations against §4–§8.

---

## 5. State Transition Law

State changes through typed messages applied by the pure reducer (`Update` of §4).

A UX surface declares:

- its `State` shape
- its `Msg` algebra
- its `Update : (Msg, State) → (State, Cmd)`

The reducer is pure. It does not perform I/O, log to side channels, or mutate global state. Effects scheduled by `Cmd` are interpreted by the runtime at the effect membrane (see §6).

View-local ephemera (open/closed flags, hover state, draft input) may be held in implementation-local state cells where the framework provides them, but only when the value is genuinely view-local (not observed by other views, not part of the product's state surface, not consequential after the view unmounts). Product-meaningful state goes through the reducer without exception.

The discipline test for whether state belongs in the reducer or in view-local ephemera: if losing the value on unmount changes the product's behavior or another part of the UI's view, it belongs in the reducer.

---

## 6. Effect Membrane Rule

Side effects are isolated to a declared effect membrane.

The membrane interprets `Cmd` values produced by the reducer and translates side-effect outcomes back into `Msg` values delivered to the reducer.

Inside the membrane:

- I/O is allowed
- subscriptions to external sources are allowed
- imperative interop with the host platform is allowed (DOM, file system, native APIs)

Outside the membrane (in render code, in pure helpers consumed by render, in the reducer):

- no I/O
- no subscriptions
- no imperative platform manipulation

The membrane has one job: interpret declared `Cmd` values. It is not where logic lives. Branching, conditional state derivation, and multi-step business decisions belong in the reducer; the membrane interprets a single declared `Cmd` per effect.

A platform-specific effect handler (whatever name the chosen framework gives it: `useEffect`, `createEffect`, `onMount`, `subscribe`, server-action handler) is part of the membrane only when it interprets a declared `Cmd`. A handler that contains conditional logic deciding state transitions is a method violation. Move the logic to the reducer; let the handler interpret one `Cmd`.

---

## 7. AssetSurface Binding Rule

When the product publishes typed asset surfaces (per `ODD_METHOD.md` §11 carrier law and the local product's design), a UX surface binds to one or more `AssetSurface` contracts as its data source and action target.

Binding requirements:

- the UX surface's `State` is derived from `AssetSurface` projections, not from a UX-local re-declaration of the asset shape
- the UX surface's `Msg` algebra reuses the `AssetSurface` action registry; UX-local `Msg` variants are reserved for view-local concerns (open/closed, sort order, filter input)
- selection within the UX surface emits a Context update (or equivalent) consistent with the product's selection contract
- writes from the UX surface go through the `AssetSurface` action registry, not through direct file or service calls

This is the rule that produces strong functional consistency between front-end and back-end: the same typed contract is the ground truth on both sides.

If the product does not publish `AssetSurface` contracts, this rule is moot. UX surfaces then bind to whatever typed contract the product does publish.

---

## 8. UX Twin Of ODD §11.5A — View Does Not Own Continuation

`ODD_METHOD.md` §11.5A states that ABG owns continuation; the product is a cooperative bounded-step subsystem.

The UX twin: **the view does not own state continuation.**

State transitions flow through declared `Msg` actions interpreted by the reducer. A view does not:

- decide on its own what the next state will be after a user event
- chain multiple state updates locally without emitting them as separate `Msg` values
- carry hidden inter-event state in refs, closures, or module-level variables

If a view appears to need a multi-step local state machine, that state machine belongs in the reducer as part of `State`, with explicit `Msg` transitions between phases. The view becomes a pure projection of which phase it is in.

The discipline test is the **Msg-replay test**: can you replay the view's behavior by replaying its `Msg` log against an empty `State`? If the answer is no, continuation has leaked into the view.

---

## 9. View Shape Rule

A view is a pure function from typed state to a view tree.

The view:

- accepts typed input (state, props, context)
- returns a typed view tree
- declares its consumed inputs explicitly
- does not capture mutable state in closures across renders
- does not read from sources outside its declared input

Whether the implementation expresses this as a function, a function component, a template, a server-rendered handler, a signal-derived expression, or another framework-specific shape is a stack decision recorded in the design module. The constitutional rule is the function signature `State → ViewTree` and the absence of side effects in the body.

A view that depends on out-of-render mutation (e.g., a ref written from inside an effect handler and read during render) is a method violation under §6 unless the mutation is part of the declared effect membrane (e.g., a platform handle for imperative interop already named in the design module).

---

## 10. Type Sharing Rule

UX-consumed types come from the shared front-end / back-end contract.

A UX surface does not re-declare back-end record shapes. It imports them from the shared contract module (typically the same package or a dedicated `contracts/` package).

If runtime validation is required (e.g., RPC responses, message-channel payloads), the project uses a typed-schema mechanism so the same type definition is the source of both compile-time types and runtime validators. The mechanism choice is project-local.

UX-local types are allowed for view-local concerns: form input draft state, sort order enums, filter strings. UX-local types do not shadow back-end types.

---

## 11. Accessibility Minimum

A UX surface that is the public face of a product capability declares:

- semantic structure (heading levels, landmarks, lists, or platform-equivalent affordances)
- keyboard or platform-equivalent navigability for every action that has a pointer interaction
- focus management on dynamic content changes
- accessibility annotations for any custom interactive element that lacks a native semantic equivalent
- color contrast at the project's declared accessibility standard (WCAG AA is the recommended default for web)

Accessibility is not optional for product capabilities. It is optional for internal-only debug surfaces; the design module records the exemption.

This section is intentionally minimal. Projects with stricter accessibility obligations (regulated industry, public-sector procurement) author a project-local accessibility refinement and cite it from their design modules.

---

## 12. Realization Discretion

The method is opinionated about the process model. It is not opinionated about the realization stack.

The project chooses:

- the language
- the framework or runtime
- the state-container library (if any)
- the effect-interpreter mechanism
- the runtime validator (if any)
- the build, bundling, and deployment toolchain

The project records its choices in the design module along with a short justification of how each choice preserves the §4 Elm process model and the §6 effect-membrane rule.

The method does not rank stacks. It tests realizations. A realization is method-compliant when §4–§10 hold under inspection and the §14 failure patterns are absent.

---

## 13. Adoption Guidance

A project adopts `UX_METHOD.md` by:

1. naming the method in the project's UX-related design modules
2. recording the realization stack choice (per §12) and the justification
3. declaring the `State`, `Msg`, and `Update` shapes for each UX surface in the design module before implementation
4. declaring the `AssetSurface` bindings (per §7) the surface consumes and emits to
5. naming the effect-membrane mechanism (per §6) and the `Cmd` algebra it interprets
6. naming any §11 accessibility refinement the project requires
7. noting any §9 view-shape or §6 effect-membrane exemptions explicitly

Adoption is per-project. A project may adopt this method only for some UX surfaces (e.g., the production UI but not internal debug tools), with the scope recorded in the design module.

---

## 14. Failure Pattern

A UX surface is violating this method when any of these are true:

1. render code mutates state directly (assignments inside the render body, mutating a prop or context value)
2. view-local state cells carry product-meaningful state instead of view-local ephemera
3. an effect handler contains conditional logic that decides state transitions
4. multi-step state machines live in the view rather than in the reducer
5. mutable refs are read during render outside the declared effect membrane
6. UX-local types shadow or re-declare back-end types instead of importing from the shared contract
7. selection or action emission writes to file or network without going through an `AssetSurface` action
8. view-shape exemptions (per §9) are taken without a recorded design-module entry
9. accessibility is omitted on a public product capability without a recorded exemption
10. two-way binding emits no typed `Msg` action and the reducer is bypassed
11. logic that should be a `Cmd` is implemented imperatively inside an effect handler
12. the view's behavior cannot be replayed by replaying its `Msg` log against an empty `State`

Any of these is a method violation. Repeated violations are not normalized by usage; they are repaired or the surface is repriced.

---

## 15. Review Questions

A UX surface review under this method should answer:

1. What is the surface's `State`, `Msg`, and `Update`?
2. Which `AssetSurface` contracts does it bind to?
3. Where is the effect membrane, and what `Cmd` values does it interpret?
4. Is `View = f(State)` provably pure for this surface?
5. Can the surface's behavior be replayed from a `Msg` log (the §8 Msg-replay test)?
6. Are all UX-consumed types imported from the shared contract?
7. Are view-shape, effect-membrane, or accessibility exemptions documented?
8. What realization stack is chosen, and how does it preserve the §4 Elm process model?
9. Does the surface honor the §8 view-does-not-own-continuation rule under user replay?

If any of these cannot be answered, the design module is incomplete.

---

## 16. Relationship To Other Method Surfaces

- `SPEC_METHOD.md` governs constitutional process, authority flow, repricing, and migration law.
- `ODD_METHOD.md` governs graph-native constructive carrier law. UX surfaces are projection / query surfaces under §10 of that method.
- `DESIGN_MODULE_METHOD.md` governs deterministic realization discipline at the module level. `UX_METHOD.md` refines it for UX modules.
- `TICKET_METHOD.md` governs ticket lifecycle. UX work uses tickets the same way other realization work does.
- `WORLD_MODEL_METHOD.md` governs world-model semantic law for products that have a world-model dimension. UX surfaces over world-model state still bind through `AssetSurface` (or equivalent) per §7.

A UX-touching design module reads `DESIGN_MODULE_METHOD.md` plus `UX_METHOD.md`. A non-UX design module reads `DESIGN_MODULE_METHOD.md` only and ignores this surface.

---

## 17. Non-Goals

`UX_METHOD.md` is not:

- a styling guide or design system specification
- a component library
- a brand or visual-identity surface
- a wireframing or prototyping process
- a research method for user studies
- a stack ranking or framework recommendation

Those are valid concerns; they belong in product-local surfaces, not in this constitutional method.

---

## 18. Canonical Compression

`UX_METHOD.md` adopts the **Elm Architecture** as the constitutional UX process model and refines `DESIGN_MODULE_METHOD.md` for UX surfaces. The model: typed `State` held by the runtime, typed `Msg` algebra, pure `Update : (Msg, State) → (State, Cmd)`, pure `View : State → ViewTree`, side effects as `Cmd` values interpreted at a declared effect membrane that returns `Msg` to the reducer. The view does not own continuation (UX twin of `ODD_METHOD.md` §11.5A); the **Msg-replay test** is the discipline check. The realization stack is the project's choice, recorded in the design module along with justification of model preservation. The method tests realizations against §4–§10 and the §14 failure patterns; it does not rank stacks, languages, or frameworks.
