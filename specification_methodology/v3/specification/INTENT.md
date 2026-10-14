# Intent

## Mission

To define a precise method for constructing software and processes from a coherent core of principles, expressed as constraints within which people and computational actors can work. The method uses categorical relationships and an axiomatic representation to make its logic explicit, check its constructions and apply the method to itself.

The method defines the current state A, the constraints on an acceptable destination Z, and the transitions that can carry work between them. People and computational actors make those transitions within finite resources. Intent, Product and Specification refine the destination; construction and evaluation establish whether it has been reached. The method separates what must be achieved from the choices made to realise it.

## What The Product Is

The product is a standalone body of method documents and their formal representation in the axiomatic calculus, a_c. It reduces the accumulated method to the principles and shared laws needed to define, construct, evaluate and release a product. Earlier rules and experience supply obligations and counterexamples; their previous document boundaries do not determine the successor's architecture.

The reduction accounts for specification and build tenancy, objects and their boundaries, algebraic calculus, functional design, outcome-driven development, information and interpretation, reference frames, computational calculus and its real-world bindings, evidence and authority, and axiomatic representation. The [pillars](PRODUCT.md#foundational-reduction) state what each contributes. The algebraic and computational calculi are parts of this core; neither accounts for the whole method alone.

Foundations state the shared commitments from which the method is built. Its deciding rules identify their foundational premises, the consequences that follow, and any additional domain or policy choices. Shared laws replace repeated determinations in the consumers that use them. The Spec Method applies those commitments through Intent, Product, Specification and Realisation. Profiles specialise the method for particular kinds of construction. Their roles are defined in [Product](PRODUCT.md#method-structure).

Shared meaning has one owner. The Spec Method and profiles use the shared contracts where work is performed and evaluated. Results use one algebra: a common set of outcomes and rules for combining them. Its refinements preserve domain meaning, failures and uncertainty. The precise obligations are [single ownership](requirements/README.md#single-ownership-requirement) and the [single result algebra](requirements/README.md#single-result-algebra-requirement).

## Direction

Category theory supplies a precise language for objects, transformations and their composition. The method distinguishes three accounts of a construction: what an algorithm does, what its information means, and how people, machines or combinations of them carry out the work. A mapping between accounts states what it preserves and how that preservation is established. Categorical claims require the [declared demonstration](requirements/README.md#categorical-demonstration-standard); claims without it remain hypotheses.

Axiomatic programming expresses the laws and constraints that permitted constructions satisfy. The a_c interpretation compresses the prose's logic into explicit objects, constraints and dependencies, retaining permitted choices and unresolved conditions. These form a [constraint surface](requirements/README.md#constraint-surfaces-and-logic-compression): an actor can determine what governs its work while choosing a solution within the remaining freedom. A compressed representation must preserve the distinctions needed for that determination.

Refinement adds detail within those obligations until a realisation can be built and evaluated. Each [build tenant](PRODUCT.md#build-tenant-binding) binds the common requirements to a computational calculus and its concrete execution environment, including human processes. The binding establishes how the realisation preserves the required meaning and constraints. The axiomatic representation distinguishes foundational premises, derived rules and declared choices; the tenant supplies the execution binding. Mechanical structure checks, mathematical arguments, semantic assessment and evidence from use support their respective claims.

The method applies its own construction and evaluation process to its successor. [Categorical Construction](PRODUCT.md#categorical-construction) defines how a bounded example tests the direction and how its findings feed back into the method.

## What It Achieves

Actors have finite context and finite attention. Context limits what an activation can hold; attention limits what it can effectively use for its task. Context management selects a sufficient reference frame: the task's purpose, subject, governing rules, required material, authority and result, within the actor's capability. It retains material dependencies and excludes irrelevant material. Work that exceeds one frame is refined into bounded transitions, with lawful continuation or an explicit stop when necessary.

Task dependencies, actor capabilities and required assurance constrain how work and information are distributed across frames. Roles and coordination structures emerge from that allocation. Different configurations can satisfy the same outcome; they can adapt as work and capabilities change within the governing constraints. The [frame requirement](requirements/README.md#bounded-transitions-and-reference-frames) connects these choices to context, attention, authority and evidence. Each realisation explains its configuration rather than assuming a fixed inventory of roles.

The workspace persists while each actor acquires a bounded account of it. That account can be discarded and rebuilt against current reality. Resumption uses the current workspace as the next starting state and retains valid progress. Recorded results are reusable while they remain applicable and their validity conditions hold. Changed dependencies and observations that invalidate a claim reopen the affected work. A change to the destination follows its owning authority and re-entry rules.

Producing a candidate, checking it and accepting it remain distinct acts. Results record their basis, evidence and unresolved matters so that later work can use them without depending on an earlier actor's private memory. The released method stands alone, with the predecessor's material claims accounted for under the [successor requirements](requirements/README.md#standalone-successor-requirement).
