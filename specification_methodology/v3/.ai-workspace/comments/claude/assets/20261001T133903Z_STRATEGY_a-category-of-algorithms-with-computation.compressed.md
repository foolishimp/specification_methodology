---
kind: post_compression
reader: llm
---

# STRATEGY: A category of algorithms with computation — compressed

**Addresses**: a category of algorithms with computation
**Status**: Draft

Commentary; every layer a proposal. [Key] = author-year citation; bibliography not included.

## Thesis
Algorithm family `a:{inputs}→output` + declared structure record ⇒ compiled to distributed compute by meaning-preserving rewrites; cost, policy, consistency, technology follow from the record. Correctness = denotation, for every plan and binding. Contribution = the combination; open: whether parts compose without conflict.
Scope: families deriving outputs from inputs over more data or higher frequency than one process serves; nothing assumed beyond the record.

## Layers
L1 domain calculus: algorithms, laws, record. L2 computational algebra: distributed-compute sorts/ops; grade on arrows; label, size, λ on data. L3 computational calculus: lawful plans; rewrites with preservation conditions incl. staging by λ. L4 workload: term, role, population/volumes, λ per input, arrival, service level incl. observer freshness μ → plan. L5 binding: stack × operational model; measured constants, price, owner-weighted judged attributes.
Domain calculus →faithful functor→ Alg →compile→ plans; L2–L5 target Alg; any family with a record reuses L2–L5 unchanged.

## Structure record
Per op: reads; homomorphism+monoid; step order; derivative per input; shared inputs. Per input sort (workload): λ, size. Undeclared op ⇒ only universally valid rewrites.
Licenses: monoid hom over partition ⇒ partition, reduce before moving · shared read-mostly input ⇒ broadcast once, cache by version · explicit valid+knowledge time ⇒ memoise by (term, knowledge time), correction invalidates what it touches · derivative ⇒ incremental update · refusal as value, strict ⇒ order-free parallel reduction (refusal absorbs) · steps ordered per item ⇒ sequential within, parallel across · inputs differ in λ ⇒ staging · per-item cost varies by kind ⇒ cost-aware partitioning by population mix.

## Dependency vs workflow
Dependency = partial order over values, owned by algorithm (L1). Workflow = one realisation (L4–5): sequencing, triggers, external waits, retries, checkpoints, state, people; lawful when every admitted sequencing respects dependency order. Domain workflow (object state machine) = L1 law; compute workflow = orchestration; domain events are among compute-workflow triggers.

## Effects
Step `A→M B`; workflow = Kleisli composition; pure arrows via unit; Kleisli laws ⇒ regrouping preserves meaning [Moggi91]. `Value = Quantity|Refused` is already Kleisli for one effect.
Effect signature M (L3): Refused (semantic, never retried); operational failure (transient, retried); async wait; checkpoint/state; audit log; human approval. Refusal ≠ failure; stacking order is policy.
Parallel branches need commuting effects ⇒ Freyd category (pure base, effectful premonoidal, identity-on-objects functor; canonical: Kleisli of strong monad) [Power-Robinson97; arrows Hughes00; arrows–Freyd correspondence Atkey11]. Grades ⇒ graded monad [Katsumata14].
Binding = handler of M [Plotkin-Pretnar09]: durable workflow engine | cloud state machine | batch scheduler | stream processor. Durable engine replays a deterministic workflow from event history = pure core separated from logged effects.

## Grades (seq f;g, par f⊗g)
latency (+, max) · bytes moved (+, +) · peak memory (max, +) · width (max, +). Bandwidth = topology property, bytes→latency per link; concurrency limit = shared-object capacity; both constrain, neither grades.
Domain calculus cartesian (free reuse); computational category monoidal non-cartesian (linear/affine): copy costs memory×replicas + wire bytes; compilation makes implicit reuse an explicit graded broadcast.
Grade order ⇒ preorder-enriched; planning = least-graded meaning-preserving plan [Selinger79]; domain laws supply rewrites.

## Sheaves
One gluing condition governs distribution, view consistency and reconciliation.
Partition plan = cover; worker = local section; sections agreeing on overlaps glue to one global section.
Distribution criterion: glue what forms a sheaf; non-local functionals only after gluing. Sum glues on disjoint cover; list-homomorphism theorems identify which functions glue [Bird87; Gibbons96]; map-reduce executes it [Dean-Ghemawat04]. Quantile does not glue; per-partition histograms/sorted vectors do ⇒ glue then one quantile.
Reconciliation: source = local section over its view; reconciled definition = global section; overlap disagreement = gluing failure; ruling selects a section; cohomology measures obstruction pre-ruling [Robinson17].
View consistency: views of one item agree at a knowledge time; binding guarantee = knowledge times where this holds; re-establishment frequency set by fastest input.

## Worked: sum + quantile (N items, P partitions, R regions, B buckets)
A: gather N; exact sum, exact p95; moves N. B: per partition partial sums + per-region histograms; gather; sum, merge; moves P×R×(B+1). Sum exact both (additivity). B's p95 within one bucket width when bucket boundaries are shared across partitions ⇒ B admissible only if service level states that tolerance. L5 picks P, B, single vs tree gather from measured bandwidth/memory. = law-licensed exact rewrite + tolerance-licensed rewrite, service level decides.

## Workload, roles
Requirement = term + workload (population, volumes, λ/input, arrival) + service level (deadline | window | per-event latency; μ or δ=1/μ). Feasible when grade at workload fits service level within resources; else rewrite or add resources.
- writer: creates/changes object, refusal a value of the write; writes system of record, emits change events; strong (durable, unique, ordered); per-command latency.
- subscriber: consumes change events, maintains own projection incrementally (derivatives, read sets); writes only projection; agrees with state at a knowledge time, possibly lagged; stream, latency at arrival rate.
- query: evaluates denotation at (valid, knowledge) time over snapshot; writes results; snapshot consistency (all sections at one knowledge time glue); deadline or window batch.
= CQS + subscriptions [Meyer88]; subscriber/query split = stream-table duality [Sax18]. Mixed-role component carries strongest consistency ⇒ role separation is first boundary tested.
Shapes (c per-item cost per kind, W workers, K ordered steps):
- deadline batch (reprice 1M/1 min, query): width ∝ N; N·c/W + fixed broadcast + gather; binds width then broadcast latency; slow inputs staged once/run; floor `T ≥ t_bcast + t_gather + N·c/W` (workers stop helping once N·c/W < fixed terms).
- window batch (nightly over 100M, query): width N, depth K; N·K·c work, N·K output rows; binds output bytes/storage then width; one snapshot/run.
- stream (subscriber; notify 1k subscribers): derivative + read sets → affected items; affected/event × c + fan-out; binds latency at arrival rate, shared-state contention; recompute at min(λ, μ).
- writer: write volume, per-command latency.
No sizing: core counts follow from c, measured per binding.

## Estate mapping
Rows: domain stages, refined to ops where valuable. Columns: role, workload shape, population/volume, service level + observer freshness, inputs (λ, tier), stack, operational model, execution mode.
Execution mode ∈ {automated in-system, automated outside any system (script|batch|extract), manual with tool, manual without record, absent}; manual = person-handled effect, no lineage, no agreement guarantee.
Handoffs first-class: dependency order says which must exist; edge = carrier, sort passed, execution mode.
Entities: SYSTEM-occupies→PLACEMENT; STAGE-computed in→PLACEMENT, -refines to→OPERATION; OPERATION-narrows→PLACEMENT; PLACEMENT-runs under→WORKLOAD, -executes on→BINDING(stack, op model), -reads→DATA_INPUT(sort, λ, size, tier, label), -cites→EVIDENCE(tier, provenance, citation); DEPENDENCY_EDGE(stage→stage)-carried by→HANDOFF(sort, mode); SYSTEM-sends/receives→HANDOFF; HANDOFF-cites→EVIDENCE; FINDING(kind, value, effort, op risk)-concerns→PLACEMENT|HANDOFF, -ranks into→ROADMAP_ITEM.
Findings: overlap (>1 system, one op, one population; duplicated work, answers can disagree; gluing failure measurable by output comparison) ⇒ consolidate · gap (computed by nothing, or computed and not stored) ⇒ build · crack (required dependency edge nothing carries) ⇒ close handoff · manual step (person-handled node/edge; cost, control risk, key-person dependency, no audit trail) ⇒ automate · rate mismatch (input held in a tier its λ or its observer's freshness does not fit: slow recomputed per event = waste; fast from periodic extract = stale) ⇒ place/stage. Further finding: breach (a carried handoff breaking a domain-calculus law or a stated requirement).
Non-finding readings: boundary (system boundary cutting an op → target-boundary input, scored via resulting overlap/crack), workload properties, dependency order — these shape target architecture and roadmap order.
Find cracks/manual steps via: record (check every required edge); data markers (adjustments, off-system tables, batch users, unrecorded transitions; confirm before counting); people (runbooks, checklists, end-user tool registers).
Rank on value, effort, operational risk; dependency order sequences roadmap. Manual step/crack = no gate carrier ⇒ also a policy finding.

## Selection (L5)
Binding = stack × operational model (in-house|managed|vendor; on-call, change process, support hours); one stack, two op models = two bindings.
Measured axes: grade at stated volumes/λ, running cost ⇒ non-dominated set [Ehrgott05]. Judged axes, evidence-cited (skills inventory, contract, incident/support record): stack — lock-in, licence/price, maturity, ecosystem; op model — skill fit, support coverage, key-person risk; pair — maintenance burden.
Owner weights per role: high-frequency subscriber may accept lock-in/maintenance for latency; nightly query favours low maintenance, existing skills; writer favours support coverage (strongest consistency on its write path).
Procedure: candidate plans (L3; meaning-preserving rewrites of one another) → grade at volumes/λ, inputs placed by placement rule → bind to each (stack, op model) → non-dominated on measured → score judged → apply role weights. Matrix = today, selection = target, same attributes; cell-wise diff = migration the roadmap orders.

## Policy
run: coeffect on caller [Petricek-Orchard-Mycroft14]; r runs a only if r holds execute(a) and, ∀ input i, read(label(i)); requirements join under a;b.
view: label(out) = ⊔label(inputs) ⊔ label(a); v sees only if label(out) ≤ clearance(v); labels join along pipeline.
obligations (audit, retention, notification): effect, accumulate, discharged, add. cost: effect = grade, add.
Labels: lattice [Denning76], per data type; role → clearance set.
Erasure: policy decides whether computed/shown, never the value; stripping policy leaves denotation unchanged (noninterference [Volpano-Smith-Irvine96]). No implicit declassification: a label is lowered only by a declared declassifier (e.g. an aggregate shown wider than its inputs), itself run-gated [Myers-Liskov97].
Roles: writer passes run gate; subscriber projection carries ⊔ stream labels, view-gated per watcher; query output carries ⊔ snapshot labels; aggregate queries = natural declassifiers.
Binding: run gate = authorisation at job submission; view gate = row/column security on result store; labels = lineage metadata; obligations = audit/event log; cost = scheduler quotas.

## Rate of change (first-class)
Input changes at λ; observer needs μ; λ, μ, ratio decide tier, staging, consistency cost, technology.
Annotations: grade (arrows; seq/par above); label (data; join); λ (data; `λ_out ≤ Σλ_in`, fastest dominates when rates differ by orders of magnitude); size (data; memory cost per tier).
Compounding: output λ = next stage's input λ; propagates like labels; placement reads upstream rates.
Recompute = min(λ_out, μ): λ_out > μ ⇒ sample at μ, coalesce (deferred); μ > λ_out ⇒ compute on change, serve held result (eager) [Gupta-Mumick95]. Incremental computation [Acar05; McSherry13]; record dependency edges decide recomputation as a build graph decides rebuilds [Mokhov-Mitchell-PeytonJones18].
Staging: `f: S×X→Y` (S slow, X fast) ≅ `stage(f): S→(X→Y)`, `f(s,x) = stage(f)(s)(x)`; hold residual `stage(f)(s)`, recompute on S change, evaluate per X change; repeat per rate class, slowest first. = partial evaluation / multi-stage programming [Jones-Gomard-Sestoft93; Taha-Sheard00], binding times from measured λ. Residual has a size grade ⇒ grade decides whether staging pays.
Placement: cheapest tier with propagation delay + access latency ≤ consumer δ; holding cost ≈ size × cost/byte + λ × refresh/invalidation cost; generalises five-minute rule [Gray-Putzolu87] from access frequency to change frequency + freshness.
Tiers (latency order of magnitude, unmeasured; cost/byte; holds): in-process beside stream (<μs; highest; fast inputs + residuals for high-frequency observer) · distributed in-memory cache (<ms; high; fast inputs shared across workers) · DB session/local cache invalidated on change (μs hit, ms miss; low; slow inputs read often) · database (ms; low; system of record; inputs read rarely) · object store/batch extract (≥10s ms; lowest; slow large batch inputs).
Memory sized to fast working set (fast inputs + residuals); slow inputs in cheaper tiers, refreshed on change.
Consistency: slow+fast result = one knowledge time; slow pinned by version, fast by sequence number, snapshot = pair [Snodgrass99]; gluing re-established per served knowledge time, cost ∝ fastest λ.
Example (order value in reporting currency, tier discount, tax; rates illustrative, unmeasured): fast = order events (many/s), price feed (/s); slow = catalogue (~daily), customer profiles (~monthly), tax/currency/calendars (~yearly). Fraud scorer (ms) and dashboard (1 min): slow inputs folded into an in-memory residual (profiles' source record in a session cache), recomputed on slow change, evaluated per fast change; scorer per change in-process, dashboard coalesced via distributed cache. Nightly report: one snapshot, slow inputs read once.
Stack criteria: observer outruns inputs ⇒ event-driven, held results; inputs outrun observer ⇒ sampled; rate-class count ⇒ staging depth; fast working set vs memory budget ⇒ in-process vs distributed cache; fastest λ under consistency requirement ⇒ snapshot-mechanism cost.

## Limits
λ is a distribution: size placement to a stated percentile (bursts; mean understates). Contention = queueing, outside grade algebra; needs a queueing model (Little's law: occupancy = arrival rate × latency [Little61]). Failure cost needs failure rates the algebra lacks. Judged attributes owner-set, underivable. Tolerance rewrites need a stated tolerance; no default. Generality unproven until a second domain calculus reuses L2–L5 unchanged.

## Owed
Record schema; formal rewrites with preservation conditions (law | stated tolerance | curry under strict refusal); reference interpreter as oracle for every binding; second domain calculus; both worked examples on two bindings measuring c, grades, recompute rates.

## Instance (illustrative): retail order calculus
Illustrative, not an implemented calculus. Domain calculus = order lifecycle fragment, three order types (standard, pre-order, return). Record = basket and store sums, shared catalogue and price state, bitemporality (price effective time, time known), sensitivities of order value to price and currency moves, strict refusal (invalid item or failed payment refuses the order), ordered fulfilment steps per order. Domain workflow = order state machine (placed → paid → shipped → delivered | returned). Sum+quantile = store revenue + p95 basket value. Writer/subscriber/query = order capture/stock and fraud projections/sales reporting. Matrix = systems on order lifecycle stages. Reconciliation = definitive product definition glued from catalogue, pricing and warehouse accounts. Staged valuation = order value over catalogue, customer tier, tax and currency calendars (rate-of-change example above).
