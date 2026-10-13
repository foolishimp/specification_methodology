# Intent

## Mission

To define a precise method for constructing software and processes, with a categorical direction and an axiomatic representation of its laws, so that the method can be mechanically checked and applied to itself.

The method lets people and computational actors turn an explicit purpose into requirements, construct independent realisations, and judge them against those requirements. It separates what a product must achieve from the choices made to build it.

## What The Product Is

The product is a standalone body of method documents and their formal representation in the axiomatic calculus, a_c. The documents state the laws for defining, constructing, evaluating and releasing a product. The formal representation makes those laws and their relationships available to mechanical checks.

Foundations state the shared commitments from which the method is built. Its deciding rules identify their foundational premises, the consequences that follow, and any additional domain or policy choices. The Spec Method applies those commitments through Intent, Product, Specification and Realisation. Profiles specialise the method for particular kinds of construction. Their roles are defined in [Product](PRODUCT.md#method-structure).

Shared meaning has one owner. The Spec Method and profiles use the shared contracts where work is performed and evaluated. Results use one algebra: a common set of outcomes and rules for combining them. Its refinements preserve domain meaning, failures and uncertainty. The precise obligations are [single ownership](requirements/README.md#single-ownership-requirement) and the [single result algebra](requirements/README.md#single-result-algebra-requirement).

## Direction

Category theory supplies a precise language for objects, transformations and their composition. The method distinguishes three accounts of a construction: what an algorithm does, what its information means, and how people, machines or combinations of them carry out the work. A mapping between accounts states what it preserves and how that preservation is established. Categorical claims require the [declared demonstration](requirements/README.md#categorical-demonstration-standard); claims without it remain hypotheses.

Axiomatic programming expresses the laws and constraints that permitted constructions satisfy. Refinement adds detail within those obligations until a realisation can be built and evaluated. Each [build tenant](PRODUCT.md#build-tenant-binding) binds the common requirements to a computational calculus and its concrete execution environment, including human processes. The binding establishes how the realisation preserves the required meaning and constraints. The axiomatic representation distinguishes foundational premises, derived rules and declared choices; the tenant supplies the execution binding. Mechanical structure checks, mathematical arguments, semantic assessment and evidence from use support their respective claims.

The method applies its own construction and evaluation process to its successor. [Categorical Construction](PRODUCT.md#categorical-construction) defines how a bounded example tests the direction and how its findings feed back into the method.

## What It Achieves

Each task has a reference frame: the bounded contract that binds its purpose, subject, governing rules, required material, authority, actor capability and result. The actor can make progress, seek a lawful refinement or continuation, or stop with an explicit reason when the task cannot be completed within that contract.

Resumption uses the current workspace and retains valid progress. Recorded results are reusable while they remain applicable and their validity conditions hold. Changed dependencies and observations that invalidate a claim reopen the affected work. Independent assessment still supplies its own sufficient evidence and judgement.

Producing a candidate, checking it and accepting it remain distinct acts. Results record their basis, evidence and unresolved matters so that later work can use them without depending on an earlier actor's private memory. The released method stands alone, with the predecessor's material claims accounted for under the [successor requirements](requirements/README.md#standalone-successor-requirement).
