# STRATEGY: Categorical groundwork for the Specification Methodology

**Author**: Dimitar Popov
**Date**: 2026-10-13T01:27:45Z
**Addresses**: the direction of STDO Specification Methodology v3.0.0; the [Intent and Product review](20261012T230613Z_REVIEW_intent_and_product_definitions.md)
**Status**: Draft, for review before work begins

## Summary

The overall intent of v3.0.0 is to lay the groundwork for using algebraic
representation and calculus to build processes and software by defining and
joining categories, such as a category of algorithms joined with a category
of computation. Axiomatic here means building blocks and layers: declared
laws are the blocks, refinement layers stack them, and the laws constrain
what any construction may do. This is constraint-based and requirements-based
programming in which the specification is the program.

The reference design is the 2026-10-01 strategy, a category of algorithms
with computation, [attached](assets/20261001T133903Z_STRATEGY_a-category-of-algorithms-with-computation.compressed.md).
It maps a domain calculus by a faithful functor into a category of
algorithms, compiles algorithms to computation plans by rewrites that
preserve meaning, licenses each rewrite by a declared law, and binds plans to
technology as handlers of one effect signature. Correctness is the
denotation, unchanged under every plan and every binding.

The method does not yet carry this direction. The way forward has four steps.
First, write the direction into the Intent. Second, prove it on one thin
categorical steel thread. Third, amend and release v3.0.0 from what the
thread shows. Fourth, build the full categorical product on the released
method.

## Analysis

### The reference design

The attached file is a compressed form written for LLM readers. Its
bibliography is not included. A reader's account:

- **Five layers.** L1 is the domain calculus: algorithms, laws and a structure
  record. L2 is the computational algebra: sorts and operations of
  distributed compute, a cost grade on each arrow, and a label, size and
  change rate on each datum. L3 is the computational calculus: lawful plans
  and rewrites with stated preservation conditions. L4 is the workload:
  volumes, arrival, change rate per input, service level and observer
  freshness, which together select a plan. L5 is the binding: a technology
  stack paired with an operational model, with measured constants and
  owner-weighted judgments. Any algorithm family that supplies a structure
  record reuses L2 to L5 unchanged.
- **Declared laws license construction.** Each property in the structure
  record licenses specific rewrites. A monoid homomorphism over a partition
  licenses reducing before moving data. A derivative licenses incremental
  update. Refusal as an absorbing value licenses parallel reduction in any
  order. Inputs with different change rates license staging. An undeclared
  property licenses only universally valid rewrites.
- **Dependency is not workflow.** Dependency is a partial order over values
  that the algorithm owns. A workflow is one realisation of it, lawful when
  every sequence it admits respects that order.
- **Effects.** A step returns its result inside an effect; a workflow is
  Kleisli composition, whose laws make regrouping preserve meaning. Refusal
  is semantic and never retried; operational failure is transient and
  retried. Parallel branches need commuting effects, a Freyd category; costs
  make the effect a graded monad. A durable workflow engine, a cloud state
  machine, a batch scheduler and a stream processor are handlers of the same
  signature.
- **Grades.** Latency, bytes moved, peak memory and width each compose by a
  stated rule in sequence and in parallel. The domain side copies values
  freely; the compute side charges for each copy. Planning finds the least
  graded plan that preserves meaning.
- **Sheaves.** One gluing condition governs distribution, reconciliation and
  view consistency. A sum glues across partitions; a quantile does not, but
  shared-boundary histograms do. Two systems that define one thing
  differently show a gluing failure, which a ruling resolves.
- **Rate of change.** Recompute at the lower of the input's change rate and
  the observer's freshness need. Staging holds the slow part of a function as
  a residual, which is partial evaluation with binding times from measured
  rates. Placement chooses the cheapest storage tier that meets the
  consumer's latency.
- **Policy.** Labels form a lattice and an output carries the join of its
  inputs' labels. Running needs permission to execute and to read every
  input; seeing needs clearance for the output's label. Policy decides
  whether a value is computed or shown, never what it is.
- **Estate mapping and selection.** The same model audits an organisation's
  systems for overlap, gap, crack, manual step and rate mismatch, ranks the
  findings, and orders a roadmap by dependency. Technology selection takes
  the non-dominated set on measured axes, then applies owner-weighted
  judgment per role.
- **Stated limits.** Change rates are distributions. Contention needs a
  queueing model and failure needs failure rates, both outside the grade
  algebra. Generality is unproven until a second domain calculus reuses L2
  to L5 unchanged. Owed: a record schema, formal rewrites, a reference
  interpreter as the oracle for every binding, and measured worked examples.

### Correspondence with the method's own terms

| Method direction | Reference design |
|---|---|
| Axioms constrain the admissible construction space (Working Product Definition, 2026-10-06) | The structure record licenses rewrites; an undeclared property licenses only universal ones |
| Building blocks and layers | L1 to L5, with L2 to L5 reused by any family that supplies a record |
| An outer contract A to X preserved through bounded steps | Correctness is the denotation under every plan and binding |
| Bounded traversal, truthful stops, recovery | Kleisli steps; refusal distinct from failure; deterministic replay from event history |
| Evidence and judgment kept separate | A reference interpreter as oracle; measured axes distinct from owner-judged axes |
| Algorithmic descriptions, informational interpretation, computational realisation over architecture H, and the maps between them (common principles, proposed formalisation) | The category of algorithms, the domain denotation, plans bound at L5, and compile-and-bind |

### What the method must supply

The [Intent and Product review](20261012T230613Z_REVIEW_intent_and_product_definitions.md)
found no carrier for this direction in the common definitions. The groundwork
the method owes, stated as its demonstration standard:

1. Objects and arrows for the method's own constructs. Specification
   artifacts are objects; derivations and refinements are arrows; identity
   and associative composition are shown.
2. Preservation obligations per layer. Each refinement layer states what it
   preserves of the layer above and discharges that obligation, as the
   reference design's rewrites state their preservation conditions.
3. Declared laws as licences. A construction step is admissible under the
   laws declared for its subject; with nothing declared, only universally
   valid steps are admissible.
4. Joins. Specifications compose, and each map between categories
   demonstrates its functor laws before any functor is claimed.
5. A representation. a_c is the language in which the laws, records and maps
   are written and checked, with a_c, its interpretations and its carriers
   keeping separate identities.
6. One worked join. An algorithm category joined with a computation category,
   as the acceptance instance.

### Why this order

- Method-first has failed before. From March to September the ABG work
  restarted eight times while the method grew without a consumer forcing a
  cost term. The 2026-10-06 coverage matrix states the same condition: self
  application establishes nothing until usefulness is shown.
- Build-first without the method loses the generalisation. One product's
  particulars would become method law by precedent, which the Product
  forbids.
- The reference design names the same condition for itself: generality is
  unproven until a second domain reuses its layers. The method's categorical
  groundwork is unproven until one real product is built on it.
- The restatement of the v2.5.1-rc.2 corpus on the axioms is the conservation
  half of v3.0.0 and is not wasted. The categorical half is derived from a
  real consumer.

## Recommended Action

The way forward, for review before work begins:

1. **Intent and Product change.** The common pen drafts it, Codex reviews it,
   and Jim accepts it. The Intent states the categorical direction,
   axiomatic programming as the computational model, and the demonstration
   standard above. The Product names categorical construction as a
   capability. Change class: Intent change, then Product.
2. **One thin categorical steel thread as the method's proving consumer.**
   One domain calculus, one record schema, two rewrites with stated
   preservation conditions, one licensed by a law and one by a stated
   tolerance, a reference interpreter as oracle, and two bindings with
   measured grades. It runs under the installed method. Every gap it hits in
   the method is recorded as a finding the method owns.
3. **Amend the v3.0.0 foundations from the thread's findings, then release.**
   Reconcile the amendment with the tenant candidates and close the open
   release decisions.
4. **Build the full categorical product on the released method.**

Questions for review before work begins:

- Which subject carries the thread: the neutral sum-and-quantile example,
  or a fragment of a real domain calculus?
- Which tenant candidate or candidates carry forward into step 3, given that
  the common definitions hold no common axioms?
- What spend and time envelope bounds step 2?
- Is the attached reference design the right instance?
