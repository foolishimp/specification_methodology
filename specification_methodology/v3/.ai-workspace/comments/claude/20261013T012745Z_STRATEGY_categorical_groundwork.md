# STRATEGY: Categorical groundwork for the Specification Methodology

**Author**: Dimitar Popov
**Date**: 2026-10-13T01:27:45Z
**Updated**: 2026-10-13T02:07:46Z
**Addresses**: the direction of STDO Specification Methodology v3.0.0; the [Intent and Product review](20261012T230613Z_REVIEW_intent_and_product_definitions.md); [Codex's review of this strategy](../codex/20261013T014000Z_REVIEW_CATEGORICAL_GROUNDWORK.md)
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
It maps a domain calculus into a category of algorithms, compiles algorithms
to computation plans by rewrites, licenses each rewrite by a declared law,
and binds plans to technology as handlers of one effect signature. An exact
rewrite preserves the denotation. An approximate rewrite satisfies a declared
adequacy relation with an end-to-end bound. This strategy corrects several
claims of the attached design; the corrections are listed below.

The common principles carry the proposed categorical maps and their proof
conditions only as hypotheses. No Product capability or construction method
carries them. The way forward has four steps. First, write the direction
into the Intent and Product. Second, prove it on one thin categorical steel
thread. Third, amend the method from the thread's findings and complete the
existing review and release obligations. Fourth, build the full categorical
product on the released method.

## Analysis

### The reference design

The attached file is a compressed form written for LLM readers. Its
bibliography is not included. A reader's account, with the review's
corrections applied:

- **Five layers.** L1 is the domain calculus: algorithms, laws and a structure
  record. L2 is the computational algebra: sorts and operations of
  distributed compute, a cost grade on each arrow, and a label, size and
  change rate on each datum. L3 is the computational calculus: lawful plans
  and rewrites with stated preservation conditions. L4 is the workload:
  volumes, arrival, change rate per input, service level and observer
  freshness, which together select a plan. L5 is the binding: a technology
  stack paired with an operational model, with measured constants and
  owner-weighted judgments. Any algorithm family that supplies a structure
  record is intended to reuse L2 to L5 unchanged; that is unproven until a
  second domain does so.
- **Declared laws license construction.** Each property in the structure
  record licenses specific rewrites. A monoid homomorphism over a partition
  licenses reducing before moving data. A derivative licenses incremental
  update. Inputs with different change rates license staging. Reduction in
  any order needs an associative and commutative combination; an absorbing
  refusal alone does not supply it. An undeclared property licenses only
  universally valid rewrites.
- **Exact and approximate rewrites.** A partition sum is exact by
  additivity. A quantile merged from histograms with shared bucket boundaries
  is within one bucket width under a fixed quantile convention and bucket
  coverage. The first preserves the denotation. The second satisfies an
  adequacy relation that the service level must state. Fixed-tolerance
  closeness is not transitive, so approximate steps carry an end-to-end
  bound, not a per-step one.
- **Dependency is not workflow.** Dependency is a partial order over values
  that the algorithm owns. A workflow is one realisation of it, lawful when
  every sequence it admits respects that order.
- **Effects.** A step returns its result inside an effect; a workflow is
  Kleisli composition, whose laws make regrouping preserve meaning.
  Regrouping, reordering and effect independence are different laws.
  Reordering parallel branches needs effects shown to commute, such as a
  commutative monad or demonstrably central arrows; a Freyd category is the
  setting for effects that need not commute. A rewrite preserves the
  observable result, the state changes and the material diagnostics. A
  handler preserves meaning only when it satisfies the effect equations; a
  shared signature alone does not establish that.
- **Recovery.** Disposition follows the observed state, the known effects,
  the applicable authority and the operation's retry conditions. A refusal on
  an unchanged basis is not retried; a changed input, repaired workspace or
  new authority can justify re-entry. An operational failure can be
  persistent. An unknown outcome after an effect is observed or reconciled
  before any dependent action. Replay from event history is one
  implementation, not the recovery rule.
- **Grades.** Latency, bytes moved, peak memory and width each compose by a
  stated rule in sequence and in parallel, within a declared measurement
  boundary. Peak memory measured on isolated steps does not bound a whole
  invocation without the live inputs, retained outputs and resident state.
  The domain side copies values freely; the compute side charges for each
  copy. Several cost dimensions give a set of non-dominated plans; the
  owner's declared criteria select among them.
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
- **Open claims.** One gluing condition for distribution, reconciliation and
  view consistency is a research claim until a base of contexts, restriction
  maps and unique gluing are supplied. A faithful map from the domain
  calculus is unclaimed until arrow equality is defined and injectivity on
  each hom-set is shown.
- **Stated limits.** Change rates are distributions. Contention needs a
  queueing model and failure needs failure rates, both outside the grade
  algebra. Owed: a record schema, formal rewrites, a reference interpreter as
  the oracle for every binding, and measured worked examples.

### Corrections to the attached design

Adopted from [Codex's review](../codex/20261013T014000Z_REVIEW_CATEGORICAL_GROUNDWORK.md).
The attached design is kept as written; where it differs, this list governs.

| Attached design | Correction |
|---|---|
| Strict refusal licenses order-free parallel reduction | Absorption does not give commutativity. Refusals with material reasons need a defined combination of findings or a preserved order. |
| Parallel branches need commuting effects, therefore a Freyd category | A Freyd category accommodates effects that do not commute. Reordering needs effects shown to commute. |
| Refusal is never retried; operational failure is transient and retried | An instance policy, not a law. Disposition follows observed state, known effects, authority and retry conditions. Unknown effects are observed before dependent action. |
| The durable engine's replay separates the pure core from logged effects | One binding's implementation, not the recovery requirement. |
| Planning finds the least graded plan | Several cost dimensions give non-dominated plans; owner criteria select. |
| Correctness is the denotation for every plan and binding | Exact rewrites preserve the denotation. Approximate rewrites satisfy a declared adequacy relation with an end-to-end bound. |
| One gluing condition governs distribution, reconciliation and views | Open claim. |
| The domain calculus maps by a faithful functor | Unclaimed until shown. |

### Correspondence with the method's own terms

| Method direction | Reference design |
|---|---|
| Axioms constrain the admissible construction space (Working Product Definition, 2026-10-06) | The structure record licenses rewrites; an undeclared property licenses only universal ones |
| Building blocks and layers | L1 to L5 |
| An outer contract A to X preserved through bounded steps | Exact rewrites preserve the denotation; approximate rewrites meet a declared adequacy relation end to end |
| Bounded traversal, truthful stops, recovery | Kleisli steps; refusal distinct from failure; disposition from observed state and known effects |
| Evidence and judgment kept separate | A reference interpreter as oracle; measured axes distinct from owner-judged axes |
| Algorithmic descriptions, informational interpretation, computational realisation over architecture H, and the maps between them (common principles, proposed formalisation) | The category of algorithms, the domain denotation, plans bound at L5, and compile-and-bind. Each layer can require all three accounts; the layers do not replace them. |

### What the method must supply

The [Intent and Product review](20261012T230613Z_REVIEW_intent_and_product_definitions.md)
found that the common definitions carry this direction only as hypothesis.
The groundwork the method owes, stated as its demonstration standard:

1. Objects and arrows for the method's own constructs. Specification
   artifacts are objects; derivations and refinements are arrows; identity
   and associative composition are shown.
2. Preservation obligations per layer. Each refinement layer states what it
   preserves of the layer above and discharges that obligation. An exact
   step preserves meaning; an approximate step states its adequacy relation
   and the end-to-end bound.
3. Declared laws as licences. A construction step is admissible under the
   laws declared for its subject; with nothing declared, only universally
   valid steps are admissible.
4. Joins. Specifications compose, and each map between categories
   demonstrates its functor laws before any functor is claimed.
   Conformance, equivalence and functorial preservation are different claims.
5. A representation and separate evidence. a_c is the language in which the
   laws, records and maps are written, with a_c, its interpretations and its
   carriers keeping separate identities. Its validation checks structure.
   Each claim names its evidence class: mechanically checked, established by
   mathematical argument, tested against an independently specified oracle,
   or unresolved.
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
   standard above. The Product names categorical construction as a generic
   method capability. The five-layer computational design is not adopted as
   method machinery. Change class: Intent change, then Product.
2. **One thin categorical steel thread as the method's proving consumer.**
   Its subject is the neutral sum-and-histogram example, a test subject
   outside the constitutional corpus. It runs under the installed method.
   Its minimum contract:
   1. A declared purpose, input and result meanings, the exact sum law, the
      approximate-quantile adequacy relation with its quantile convention,
      bucket coverage and output rule, and the material failure outcomes.
   2. Concrete objects and arrows of the example's categories, their
      equality, identity and composition, and the specific maps claimed,
      related to the algorithmic, informational and computational accounts.
   3. One exact partition and reduction rewrite and one bounded
      approximation, each with explicit conditions and an end-to-end
      adequacy argument.
   4. An independently specified exact oracle, two concrete execution
      bindings, and comparison of returned meaning, required effects and
      diagnostics. A refusal case and an interruption or uncertain-effect
      case run beside normal completion.
   5. Measured latency, bytes moved and memory over a declared workload,
      with measurement boundaries and the activation's context, time and
      spend envelope. Only the cost and generality claims those observations
      support are made.
   6. The thread's own chain from Intent through Product and Specification
      to Realisation is written with the method's proposed constructs. Each
      derivation step is an arrow with a stated and discharged preservation
      obligation, so a failure there is a finding against the method, not
      the example.
3. **Amend the method from the thread's evidence.** Each finding returns to
   its actual owner; a failure becomes a method finding only when
   triangulation establishes that owner. The affected method clauses are
   amended and independently reviewed. The standalone successor, member
   acceptance and release obligations remain in force; the thread supports
   its own join, not qualification of the whole method.
4. **Build the full categorical product on the released method.** The sheaf
   account, a universal grade algebra and second-domain generality stay
   unresolved until an instance requires and supports them.

Questions for review before work begins:

- Which tenant candidate or candidates carry forward into step 3, given that
  the common definitions hold no common axioms?
- What spend and time envelope bounds step 2?
