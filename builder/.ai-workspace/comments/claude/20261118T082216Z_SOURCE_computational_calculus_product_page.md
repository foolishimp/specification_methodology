<!-- Transcribed from four photographs (IMG_3400 to IMG_3403) of
     computational_calculus/specification/PRODUCT.md, lines 1 to 170.
     Words marked [?] were hard to read in the photographs. -->

# Project Product

Basis: the exact STDO cut selected by `../stdo_default.json`
(`constitution.stdo.basis`), verified with
`stdo status --definition stdo_default.json --verify`.

Status: candidate. It realises the owner's direction and decisions of 2026-10-30
and 2026-11-03 recorded in [INTENT](INTENT.md). The owner has not yet admitted this
text, but for the passages CC-002's admission batch restated. Its terms *Structure
record*, *Data annotation* and *Rewrite*, and the third row of its layer table, were
restated on 2026-11-12 in that batch, on the owner's rulings 4 and 5, and they are
admitted by the owner's ruling 12 of 2026-11-13, with the whole calculus (CC-002; the
frame basis, revisions 13, 14 and 19). Its term *Computational requirement* is restated
in CC-002's admission pass to match `REQ-CC-NEED-001`'s lines, and its term
*Operational failure* in CC-002's fix pass of the owner's review to match
`REQ-CC-EFF-002`, each requirement as admitted by the owner's ruling 12 (the frame
basis, revisions 14 and 17). Its surfaces row for `calculus/` records the calculus's
standing, restated in CC-002's final pass to the owner's ruling 12 (the frame basis,
revision 19).

## Product Position

`computational_calculus` is the bridge between an algorithm and the hardware and
software systems that execute it. It is written against algorithms
`a : {inputs} → output` in general. A family of algorithms uses it by declaring
its structure, and a system takes part through a binding that handles the
calculus's effects and reports its measured constants. It supersedes MTS
`computation_calculus` ([SOURCES](../SOURCES.md) S5), whose copy stays in
`trade_journey/inducted/` as a historical record.

It is the computation domain of the owner's ruling of 2026-11-07
(`../../docs/ARCHITECTURE.md` §2.3). Every application is a business
domain realised through it. Its use cases are applications, `pnl_commentary` first
(Goals G5). Like the trade journey, it is open: any family of algorithms can use it.

The layers are the four of the flow (Intent *Purpose*), in flow order:

| Layer | Side | Owned here | Content |
|---|---|---|---|
| 1. The algorithm | algorithm | no: each family's own Product | algorithms, their laws, and the structure record the family fills in against this Product's schema |
| 2. Operational requirements | demand | yes, as a form | the computational requirement: what a family declares for an algorithm it wants computed (term, role, population, input sizes and rates, arrival, service level, effects, policy) |
| 3. The computational algorithm | the bridge | yes, as its rules | the computational algebra (the sorts and operations of computation; grades on arrows; labels, sizes, change rates and lifetimes on data; their composition rules) and the computational calculus (plans and rewrites with their preservation conditions; staging by rate; gluing; the effect signature; the denotation as correctness), from which the derived needs follow, up to feasibility. The plan chosen belongs to the Product that runs it |
| 4. The binding | systems | yes, as a form | a stack with its operational model that delivers the plan's operations within their boundaries, as a handler of the effect signature; measured and judged axes; selection. An LLM interprets the plan and binds it |

A concrete binding belongs to the Product that runs the computation (Intent C5).
The frame paper ([SOURCES](../SOURCES.md) S1) has five layers, and the owner
renumbered them to these four on 2026-11-03: its layer 4, the workload, is layer 2
here; its layers 2 and 3, the computational algebra and calculus, are layer 3; and its
layer 5, the binding, is layer 4.

<a id="product-terms"></a>
## Product Terms

**Bounded context.** `urn:stdo:bounded-context:computational-calculus`, owned by
this document, under the basis selected by `../stdo_default.json`, governing
`urn:stdo:product-definition:computational-calculus`. Where MTS
`computation_calculus`, `pnl_calculus`, `trade_journey` or the commentary app use
the same word differently, that meaning is kept separate and related explicitly.

| Term | Meaning here |
|---|---|
| <a id="term-algorithm"></a>**Algorithm** | A function `a : {inputs} → output` from named, typed inputs to an output. Its meaning is its denotation |
| <a id="term-family"></a>**Family of algorithms** | A set of algorithms closed under the composition a domain calculus defines, with the laws that calculus states. It uses this Product by declaring a structure record |
| <a id="term-domain-calculus"></a>**Domain calculus** | Layer 1: a family of algorithms, its laws and its structure record, owned by the family's own Product. Never "calculus" on its own here |
| <a id="term-operation"></a>**Operation** | One named algorithm of a family, the unit a structure record describes |
| <a id="term-structure-record"></a>**Structure record** | What a family declares per operation: its reads, whether it is a homomorphism and over which monoid, whether its steps are ordered, whether it has a derivative with respect to an input, its shared inputs, whether an external engine computes it, and, where its result is ordered, the total order the result is stated in and its ties. Per input sort, a size and a change rate. The only contract between a family and this Product |
| <a id="term-externally-computed"></a>**Externally computed operation** | An operation the structure record declares is computed by an external engine. It is opaque here: planned, gated and checked by its declared laws, never re-implemented |
| <a id="term-computational-algebra"></a>**Computational algebra** | Part of layer 3, with the computational calculus: the sorts and operations of computation (work, movement, holding, copying, waiting), with their annotations and composition rules |
| <a id="term-grade"></a>**Resource grade** | The annotation on an arrow: latency, bytes moved, peak memory, width. Each combines by its own rule in sequence and in parallel |
| <a id="term-annotation"></a>**Data annotation** | The label, the size, the change rate and the lifetime a datum carries, each with its own composition rule |
| <a id="term-computational-calculus"></a>**Computational calculus** | Layer 3, with the computational algebra: the lawful construction of execution plans from a term and its computational requirement, and the rewrites between plans. "Calculus" on its own means this |
| <a id="term-plan"></a>**Execution plan** | A term of the computational algebra that a binding can execute, constructed by the calculus from a term of a family and its computational requirement |
| <a id="term-computational-algorithm"></a>**Computational algorithm** | The execution plan chosen for a computational requirement: an algorithm in the category of computation. It is what an LLM interprets and binds |
| <a id="term-rewrite"></a>**Rewrite** | A transformation of one plan into another. It is admissible only with its **preservation condition** stated: any stated law (exact), a tolerance a service level states (tolerance-admissible), or the curry isomorphism (staging) |
| <a id="term-staging"></a>**Staging** | The rewrite `f(s, x) = stage(f)(s)(x)` that holds the residual `stage(f)(s)` of the slow inputs `s` and evaluates it on each change of the fast inputs `x` |
| <a id="term-gluing"></a>**Gluing** | Combining local results computed over a cover of the input population into one global result. A result glues when local results that agree on overlaps determine it |
| <a id="term-denotation"></a>**Denotation** | The value an algorithm gives for its inputs. The one correctness criterion for every plan and every binding |
| <a id="term-reference-interpreter"></a>**Reference interpreter** | An evaluator of terms by their denotation, with no plan and no binding. The oracle a binding's output is compared against |
| <a id="term-refusal"></a>**Refusal** | A value meaning the algorithm gives no answer for these inputs. It propagates strictly: every result reading a refused value is refused. Semantic, never retried, never a number |
| <a id="term-operational-failure"></a>**Operational failure** | A transient failure of execution: a timeout, a lost worker, an engine that is down, a data set with no binding. It may be retried where its effect is declared repeatable (`REQ-CC-EFF-002`). It is not a refusal |
| <a id="term-effect-signature"></a>**Effect signature** | The effects a workflow step may perform beyond its pure value: refusal, operational failure with retry, asynchronous wait, checkpoint and state, audit log, and human approval, with reads and writes of the world |
| <a id="term-binding"></a>**Binding** | A technology stack paired with an operational model, acting as a handler of the effect signature. It delivers a plan's operations within the boundaries the plan requires: semantic (the algorithm's laws kept) and operational (each operation within the requirement's limits). An LLM interprets the plan and binds it. "Binding" on its own means this form |
| <a id="term-declared-binding"></a>**Declared binding** | One concrete binding, declared by the Product that runs a computation: its stack, its endpoints or URIs, its operational model. For example the commentary app's binding (`../../pnl_commentary/specification/composition/FULFILMENT.md` §6). Owned by that Product, never by this one |
| <a id="term-configuration-layers"></a>**Configuration layers** | The five layers in which what a run reads, beside the stages it runs, is declared. Each has one owner, which alone declares it and changes it, and no layer states another's contents: the family's declarations; the plan's own lines; the **systems layer**, one for every environment and every build tenant, the system each data set is read from and each output and store is written to, each named by its role and never by an address's value, with each data set's layout and each property the binding declares of a source; the **deployment**, one for each environment, the value there of each address the plan's edges reach, the resources a run is given there, and where each credential comes from, never the credential; and the **tenant's own fixed settings**, one for each build tenant, the stack it binds the plan to, its engine and that engine's declared version among it [?]. The last three are the binding's level, the declared binding's lines that a run reads, each owned by the Product that runs the computation (Intent C5). The layers meet only at what the family and the plan declare, and at the edges' own terms ([`BND-03`](calculus/BINDING_FORM.md#bnd-03), `REQ-CC-EFF-010`). They are numbered apart from the four layers of the flow above |
| <a id="term-computational-requirement"></a>**Computational requirement** | An algorithmic requirement stated in terms of its computational needs: its term and structure lines, role, population, each input's size, change rate, times, label and, where it is kept, lifetime, arrival pattern, service level, effects, with each effect's repeatability, each read's declared outcome and the lifetime of each kind of item its writes keep, and policy (`REQ-CC-NEED-001`). The family declares it; the calculus derives its needs (`REQ-CC-NEED-004`) |
| <a id="term-workload"></a>**Workload** | The demand part of a computational requirement: its term, role, population and volumes, input change rates and arrival pattern, against which a plan is graded |
| <a id="term-computational-need"></a>**Computational need** | What computing a requirement takes, as the calculus derives it: candidate plans, each plan's grade, recompute rates, staging, tiers, consistency and its cost, labels and gates, and feasibility |
| <a id="term-role"></a>**Role** | What a workload does toward a system. A **writer** creates or changes a domain object. A **subscriber** consumes change events and maintains its own projection. A **query** evaluates the denotation at a snapshot |
| <a id="term-service-level"></a>**Service level** | What a workload's observer needs: a deadline, a window or a per-event latency, the observer's frequency, and any tolerance it accepts |
| <a id="term-change-rate"></a>**Change rate** | `λ`, how often a datum changes: a distribution over time, stated at a percentile. "Rate" on its own means this |
| <a id="term-observer-frequency"></a>**Observer frequency** | `μ`, how often an observer needs a result, or its staleness bound `δ = 1/μ` |
| <a id="term-knowledge-time"></a>**Valid time and knowledge time** | The time a value is about, and the time at which it was known. A result is stated at one of each |
| <a id="term-tier"></a>**Tier** | A place data is held: in-process memory, a distributed cache, a local or session cache, a database, an object store or batch extract. Each has an access latency and a cost per byte that a binding measures |
| <a id="term-label"></a>**Label** | An element of a lattice attached to data, saying who may see it. An output's label is the join of its inputs' labels and its algorithm's own |
| <a id="term-declassifier"></a>**Declassifier** | A declared algorithm, itself authorised to run, whose output carries a lower label than its inputs, such as an aggregate shown more widely |
| <a id="term-measured-axis"></a>**Measured and judged axes** | The axes a binding is chosen on. **Measured**: its resource grade at stated volumes and rates, and its running cost. **Judged**: lock-in, licence and price model, maturity, ecosystem, skills fit, support coverage, key-person risk, maintenance burden, each scored with cited evidence |

## Goal Model

[GOALS](GOALS.md) selects which outcome of [INTENT](INTENT.md) the current wave
pursues. A goal never changes what a term means; a new meaning re-enters here.

## Product End State

- The structure-record schema, the computational algebra, the rewrite catalogue
  with every preservation condition, and the effect signature, stated in
  [calculus/](calculus/).
- A reference interpreter that evaluates every worked example.
- The order-processing example and P&L explain each planned, costed, staged and
  gated by the calculus, and bound to a stack, with no change to the calculus.
- The Product in its own repository.

## Acceptance

**The calculus is accepted at a revision when all of these hold:**

1. Every grade and every data annotation states its rule under sequential and
   parallel composition.
2. Every rewrite states its preservation condition.
3. The reference interpreter evaluates every worked example the specification
   states, and every plan of each example gives the interpreter's value, or a
   value within the tolerance its service level states.
4. A second family, from another domain, supplies a structure record and reuses
   the calculus unchanged.

## Current Product Definition

### Surfaces

| Surface | Owns |
|---|---|
| [README](../README.md) | Orientation: the bridge, the four layers, the decisions |
| [SOURCES](../SOURCES.md) | The papers and the superseded MTS Product, by commit and path, and how its requirements map to these |
| [requirements/](requirements/) | `REQ-CC-*`: what the calculus owes |
| [calculus/](calculus/) | The calculus itself (Goals G3). Part 1, the ETL catalogue, and part 2's changes, stated, with the repairs of part 1's text, and admitted by the owner's ruling 12 of 2026-11-13, whole, as CC-002's final pass leaves them; the binding's form, [BINDING_FORM.md](calculus/BINDING_FORM.md), stated and admitted by the owner's ruling 8 of CC-012, 2026-11-17; the rest owed |
| [build_tenants/interpreter/](../build_tenants/interpreter/) | The reference interpreter (Goals G4). Planned |

### Composition

`computational_calculus` composes no Product (Intent C7). A family, an application
or a map of systems composes it, and each edge and its contract belong to the
composer:

- **`pnl_commentary`**, the commentary app, the first test application (Goals G5).
  Its edge is made: `../../pnl_commentary/specification/composition/COMPUTATIONAL_CALCULUS.md`.
  Its needs, plan, stack and binding are its own; `pnl_calculus` supplies its
  algorithm, Σ_pnl, whose §7 structure records are the structure lines.
- **`pnl_calculus`**, the first family. It takes layers 2 to 4 from here in place of
  stating them itself, and supplies Σ_pnl's structure records. Its edge is made
  (2026-11-02, PNC-010):
  `../../pnl_calculus/specification/composition/COMPUTATIONAL_CALCULUS.md`.
- intended, not yet made: `trade_journey`, whose valuation and risk operations are
  externally computed, and whose systems map places systems by this Product's
  roles. Its edge waits until it needs one.

<a id="reference-frame-authority"></a>
### Reference-frame authority

This document admits the Project Reference-Frame Basis at
[REFERENCE_FRAME_BASIS](REFERENCE_FRAME_BASIS.md) for
`urn:stdo:product-definition:computational-calculus`.

### Working assumptions

| ID | Assumption | Replaced by |
|---|---|---|
| A1 | **Supersession is recorded by each owner.** Replaced on 2026-11-02 (PNC-010). The composite's decomposition lists this Product and composes it. `pnl_calculus` takes layers 2 to 4 from here on its own edge. `trade_journey` records the MTS copy as superseded (its `inducted/PROVENANCE.md`, *Dispositions*) | Replaced: PNC-010, applied by each owner |
| A2 | **Repository.** Iterated here and published to its own repository, not yet named | An owner decision |
| A3 | **Interpreter language.** Withdrawn on 2026-11-12: PRODUCT names no language (the owner's ruling 3, decision 8, CC-002). The interpreter's stack is its build tenant's record | Replaced: the build tenant's stack record ([ADR-001](../build_tenants/interpreter/design/adrs/ADR-001-the-stack.md)) |
| A4 | **Sources read.** S1 and S5 are read in full. S2, S3 and S4 are read for their scores against S5's requirements only | The coverage evaluation E2 |
