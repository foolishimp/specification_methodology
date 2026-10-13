# Intent

## Mission

We are building a specification methodology in which a product is constructed from its declared laws. A product, whether a process, a piece of software or this methodology itself, is defined by its purpose, the meaning of its parts, the constraints on them and the evidence that shows they hold. Building it means deriving a realisation from those laws by steps the laws permit. Every claim about the result names the evidence that supports it.

Without such a method, construction is steered by implementation momentum, by what an agent happens to remember, by local convention and by accumulated commentary. The same question is answered differently in different places, a result cannot be trusted without redoing the work, and a change cannot be traced to what it affects. The method replaces these with one explicit body of law that every step is checked against.

The work is done by finite actors: people and language models with limited context, attention, time and capability, whose constructive steps are probabilistic. No actor can hold a whole product, or the whole method, at once. The method therefore carries an outer contract, from intent A to realisation X, through bounded steps A → B → … → X. Each step receives only the context it needs and preserves the meaning and obligations of the outer contract. The path may branch, join or refine recursively.

## What The Product Is

The product is a methodology written as documents, with an axiomatic representation of its laws. Its parts:

- Foundations: the laws any method needs. They define what things are and how they are identified, how a claim is justified, who may decide what, how results are stated and combined, and how a bounded actor is given work and returns a result.
- Spec Method: the specification method built on the foundations. A product is defined in four stages. Intent states its purpose, beneficiaries and desired outcomes. Product states what the thing is, its capabilities, concepts and boundaries. Specification states the required meaning and behaviour, constraints, contracts and evaluation criteria. Realisation is the concrete design, documents and implementation, with evidence against the specification. The sequence recurs wherever a part needs its own account, and the method applies it to itself. The method also governs how work is carried and triaged, how a change re-enters at the first stage it affects, how results are assured and how releases are cut.
- Profiles that bind the method to particular kinds of construction, such as outcome-driven development over published graph functions, user experience and world models.
- An axiomatic calculus, a_c, in which the laws, records and maps are written so that their structure can be checked mechanically.
- Reference frames: projections of the method onto one task. A frame is the unit an actor works from. It carries the clauses the task needs and nothing else.

Every determination of the method has one owner. Foundations own what holds for any method. Spec Method is one method built on them. A domain or operational profile owns only its own bindings. A lower tier refers to or refines an owner's determination; it never defines a second one. The precise obligation is the [single ownership requirement](requirements/README.md#single-ownership-requirement).

The method has one result algebra. Every tier, profile and frame states its outcomes in it or as a refinement of it.

The method lays the groundwork for building processes and software by defining categories and joining them, such as a category of algorithms joined with a category of computation. The computational model is axiomatic programming. Declared laws are the building blocks. Refinement layers stack them. The laws constrain what any construction may do. The specification is the program: construction is constraint-based and requirements-based.

## What It Achieves

- An actor given a task and its reference frame completes the task, or stops with a truthful account of why, using only the frame and the task's subject. It never needs the whole method or another actor's private memory.
- Every result carries its basis, assumptions, evidence and dependencies, so later work resumes from it and a reviewer can check it.
- A valid result is reused until its basis changes. A change re-opens only the results that depend on what changed.
- A construction step is admissible only under the laws declared for its subject. An exact step preserves meaning; an approximate step states its adequacy relation and an end-to-end bound.
- Producing a candidate, checking it mechanically and judging it remain separate results. Producing a candidate never counts as its assessment or its acceptance.
- Nothing the method already establishes is lost. Each existing rule is kept, replaced by a named successor, deliberately removed or shown not to apply. Kept rules are restated on the axioms, so the method is complete on its own.

## Demonstration Standard

The categorical direction holds only where it is demonstrated:

- the method's constructs are objects and arrows, with identity and associative composition shown;
- each refinement layer states what it preserves of the layer above and discharges that obligation. An exact step preserves meaning; an approximate step states its adequacy relation and an end-to-end bound;
- a construction step is admissible under the laws declared for its subject, and with none declared only universally valid steps are admissible;
- a map between categories shows its functor laws before a functor is claimed;
- a_c is the representation of laws, records and maps, and each claim names its evidence class;
- one algorithm category joined with one computation category is the acceptance instance.

A categorical statement without that demonstration is a hypothesis. The precise standard is the [categorical demonstration standard](requirements/README.md#categorical-demonstration-standard).

## Direction

The method is built with its own installed earlier release, as a compiler is built with its previous version.

The categorical direction is proved by a real consumer before it is generalised. One thin steel thread, joining an algorithm category with a computation category, is built under the installed release. The method is amended from what the thread shows, and the full categorical product is then built on the released method. Restating the existing method on the axioms continues alongside.

## Standing

Jim owns this Intent and decides acceptance. Nothing here is released or adopted yet, and no universal mathematical claim is made.
