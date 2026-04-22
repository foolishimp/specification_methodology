# Design Module Method

**Status**: Approved
**Date**: 2026-04-22
**Governance**: Maintained by the methodology author.
**Scope**: Realization-level design method for projects that want low coupling,
modular composition, immutable carriers, explicit effect management, and
minimal semantic bleed between interfaces.
**Relation**: Complements `SPEC_METHOD.md` and `ODD_METHOD.md`. This method is
not constitutional process law. It is a realization-method surface that a
project may adopt in design surfaces, ADRs, tickets, and reviews. Once adopted
for a project or boundary, it is binding realization law for that scope.

Use `GLOSSARY_GUIDE.md` for shared recursive-product terminology unless this
method explicitly narrows a term.

---

## 1. Purpose

This method exists for projects that want a stronger implementation discipline
than "write code that passes."

Its bias is toward:

- low coupling
- modular composition
- immutable typed carriers
- total or nearly-total semantic transforms
- explicit effect boundaries

The goal is not language ideology.

The goals are:

- reduce ambiguity
- reduce entropy
- eliminate avoidable tech debt
- increase refactorability
- reduce hidden authority, hidden mutation, and semantic drift in realization
  code

This method is therefore about implementation shape.

It does not replace constitutional authority from `SPEC_METHOD.md`.

It does not replace graph-native law from `ODD_METHOD.md`.

It governs how realization modules should be structured once the project has
already decided what it is building.

---

## 2. Position

The preferred realization shape is functionally biased.

That means:

- semantic meaning should live in typed carriers and explicit transforms
- imperative coordination should be subordinate to admitted truth
- side effects should be isolated to explicit boundary modules
- mutable shared state should be minimized and justified

This method does **not** require a functional programming language.

It does require a functional design discipline.

A Python, Scala, TypeScript, Kotlin, or Java implementation may all satisfy
this method if they keep semantic law in explicit carriers and transforms rather
than hidden orchestration.

---

## 3. Core Rule

The core rule is:

**semantic steps should read as transforms over admitted truth; effects should
be explicit and pushed to the edge**

If a reader must inspect orchestration code, mutable workspace state, service
methods, or fallback defaults to determine what the system means, the design is
too imperative and too coupled.

---

## 4. Functional Bias Without Language Mandate

Projects using this method must prefer:

- immutable data carriers over mutable shared objects
- closed typed carriers over open dict or string protocols
- explicit return values over hidden mutation
- explicit failure carriers over ambient exception-driven control flow where
  practical
- composition of small transforms over long controller procedures

Projects using this method must avoid:

- one giant mutable workspace object
- one orchestration method that owns semantic law
- hidden read/write coupling through globals, shared registries, or mutable
  service state
- effectful helpers that both decide meaning and perform writes
- proxy interfaces that partially imitate a new design while preserving the old
  authority path

---

## 5. Prime Law

New functions should be introduced only when they are structurally prime.

A function is **prime** when it introduces one irreducible new semantic or
topological boundary that cannot be honestly expressed as composition of
existing functions.

Typical lawful reasons to introduce a new function are:

- a new feature topology or branch in the admitted work graph
- a new typed carrier transformation
- a new effect boundary
- a new validation or admission boundary
- a new projection boundary

A function is **not** prime when it exists only to:

- shorten a call site without creating a new semantic boundary
- aggregate unrelated behavior for convenience
- preserve an old interface behind a new name
- shuttle data through one more wrapper layer
- hide mutation, fallback, or orchestration that should remain explicit

This is Occam's razor for design modules:

- prefer composition over convenience extraction
- prefer existing lawful functions over new wrappers
- prefer fewer sharper boundaries over many vague helper functions

The purpose of the Prime Law is not to minimize line count.

The purpose is to stop semantic fragmentation and helper sprawl from becoming
architecture.

## 6. Design Module Taxonomy

When this method governs a realization boundary, modules should be classified by
role.

Recommended roles are:

- **Carrier module**: defines typed immutable inputs, outputs, contracts,
  transitions, records, or envelopes
- **Semantic kernel module**: implements the main transforms over carriers
  without performing side effects
- **Effect shell module**: performs event emission, file publication, network
  calls, subprocess execution, persistence, or operator delivery
- **Projection module**: derives read models or reports from authoritative
  source truth
- **Binding or adapter module**: converts between external boundaries and the
  project's internal carriers without inventing semantic law
- **Constructor or materialization module**: writes generated or built artifacts
  from admitted carriers and explicit plans

The point of the taxonomy is not naming ceremony.

The point is to stop semantic law from being smeared across modules with mixed
authority.

---

## 7. Immutable Carrier Rule

Source truth should be carried in typed immutable values unless mutation is
materially necessary.

Preferred shape:

- constructor or parser produces a typed carrier
- transforms consume one carrier and return another carrier or a closed result
- projections read those carriers without mutating them

Mutable carrier state requires explicit justification when it is:

- performance-critical
- required by the host runtime or framework
- modeling a genuinely stateful boundary rather than semantic truth

Convenience is not sufficient justification.

---

## 8. Totality Rule

Semantic functions should be total or as close to total as the language and
problem allow.

Preferred shape:

- invalid input is rejected at the boundary
- semantic kernels consume admitted carriers only
- failure is returned in a typed and explicit form when practical

Projects using this method should prefer:

- `Result`-like or closed outcome carriers
- explicit validation stages
- explicit "unsupported" or "rejected" outcomes

Projects using this method should avoid:

- partial functions that assume hidden preconditions
- semantic `.get(...)` fallback chains
- controller code that reconstructs missing truth from defaults

---

## 9. Effect-Edge Rule

Effects should be explicit and isolated.

Typical effect edges include:

- file writes
- network calls
- subprocess execution
- event append
- manifest publication
- prompt delivery
- database mutation

Semantic kernels should not perform these effects while also deciding the law.

The preferred sequence is:

1. admit or parse the authoritative input
2. transform it into a typed plan or outcome
3. apply effects at the edge using that plan or outcome
4. publish resulting events or projections downstream

If a function both decides the semantic meaning and directly performs the write,
the design should be treated as suspect.

---

## 10. No Semantic Center Rule

No controller, manager, service method, runtime loop, or public wrapper should
be the hidden semantic center of the system.

That includes:

- deciding meaning procedurally in orchestration code
- rebuilding truth from payload fragments
- rehydrating current law from legacy files or fallbacks
- flattening typed meaning into ad hoc dict handling and `.get(...)` chains

A module is acting as an unlawful semantic center when reviewers must read it to
discover:

- what counts as closure
- what identity means
- what failure means
- what work is next
- what the current truth is

Those meanings should already exist in carriers, contracts, or explicit design
modules.

---

## 11. Coupling Rule

Coupling should be reduced by dependency shape, not only by file count.

Preferred dependency direction is:

`carriers -> semantic kernels -> effect shells -> projections`

Not:

`controllers -> service helpers -> mutable runtime state -> projections`

Design is too coupled when:

- many modules read and mutate the same object
- projections must inspect implementation state to infer truth
- a consumer can silently rebuild source truth from raw artifacts
- tests pass only because multiple modules still carry the same meaning

Reducing coupling means reducing the number of places where meaning can be
invented.

---

## 12. Interface Bleed Prohibition

No interface should bleed semantic authority into another interface family.

Interface bleed exists when:

- one interface reconstructs another interface's source truth
- projection logic becomes closure logic
- report or prompt logic becomes admission logic
- public wrappers decide kernel semantics
- adapters invent meaning instead of translating boundaries

The required shape is:

- each interface family has one authoritative source truth
- downstream interfaces consume that truth
- crossing an interface boundary does not create a new semantic center

Low coupling requires semantic non-bleed, not only small functions.

---

## 13. Proxy Interface Prohibition

Projects using this method must not use proxy or partial interface
implementation as a substitute for real migration or real design completion.

A proxy interface is a new-looking surface that:

- forwards to the old authority path
- reconstructs missing truth from the old path
- keeps the old path executable behind a new name
- allows proofs to stay green while the old law still governs

This is bridge debt, not progress.

If compatibility is intentionally retained, it must be treated as an explicit
feature with its own bounded authority and proof.

Otherwise the proxy path must be removed.

---

## 14. Design Review Questions

When reviewing code under this method, ask:

1. Does semantic law live in typed carriers or in orchestration code?
2. Are the main steps readable as transforms over admitted truth?
3. Are effects isolated to explicit edge modules?
4. Can projections or reports invent closure independently?
5. Is mutation justified, bounded, and local?
6. Can consumers pattern-match the source carrier directly?
7. Is any proxy or compatibility surface still silently authoritative?
8. Would removing the authoritative carrier make the system fail closed rather
   than silently rebuilding truth?
9. Is each new function structurally prime, or is it convenience aggregation?
10. Does any interface bleed semantic authority into another interface family?

If these questions cannot be answered cleanly, the realization is too coupled
or too imperative.

---

## 15. Adoption Guidance

Projects may adopt this method by:

- citing it in ADRs or design surfaces
- naming it in `AGENTS.md` as the preferred realization discipline
- using it as review criteria for implementation-migration tickets
- classifying implementation modules by the taxonomy in this method

When a project adopts this method, it must apply it consistently across the
named boundary:

- design modules
- runtime or execution kernels
- prompt assembly and reporting paths
- constructors and materializers
- projection and query surfaces

Partial adoption is allowed, but the adopted boundary should be named
explicitly.

---

## 16. Relationship To Other Method Surfaces

- `SPEC_METHOD.md` governs constitutional process, authority flow, repricing,
  and migration law
- `ODD_METHOD.md` governs graph-native constructive carrier law
- `DESIGN_MODULE_METHOD.md` governs preferred realization structure inside
  implementation and design modules

So:

- `SPEC_METHOD.md` answers what is lawful process
- `ODD_METHOD.md` answers what is lawful graph-native product shape
- `DESIGN_MODULE_METHOD.md` answers what is the preferred implementation design
  discipline when you want low coupling, no interface bleed, and explicit effect
  management

---

## 17. Non-Goals

This method does not require:

- one specific programming language
- elimination of all imperative code
- monadic or category-theory vocabulary
- replacing every exception with a custom algebraic type

It does require that the implementation shape remain readable, modular, and
honest about where meaning lives and where effects happen.
