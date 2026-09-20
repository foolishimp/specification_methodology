# STRATEGY: STDO 2.5.1 consolidation and independent project-local repair

**Author**: Codex, bounded commentary Writer

**Date**: 2026-09-20T04:48:37Z

**Revised**: 2026-09-20 after Claude's review and the owner's correction that STDO 2.5.1 is independent of T-288; postmortem-derived qualification cases remain applicable.

**Addresses**: ABIogenesis March–September postmortem; shared STDO revision; project-local axioms, reference frames and qualification

**Status**: Revised proposal. STDO 2.5.1 has its own amendment, qualification and release scope; T-288 is not a dependency or release gate. This revision changes recommendations only. It selects no new constitutional, ABI implementation/Git, release or adoption effects.

## Summary

Keep the diagnosis and ownership table. Validity was replaced by repetition;
local reviews missed accumulated work. Bounded contexts amplified the failure.
ABI already owns sufficient runtime, incremental-projection and installed-proof
law for much of the repair, which proceeds under RC7.

**Adopted refinements:** retention bears the burden; audit the acceptance
predicates that turned excluded threats into deliverables. Apply reuse and
proportionality to STDO's own work. Add the missing local placements and withdraw
the misattribution of the postmortem's convergence concern.

**Next direction:** consolidate and qualify STDO 2.5.1 against its admitted
amendments and relevant postmortem counterexamples. Independently, recommend
ABI's bootstrap correction, an explicitly unaccepted checkpoint and standing
per-handoff regression evidence. T-288 observations may inform method checks;
its progress or closure does not control STDO work or release. C2/event/payload
changes keep their local owners. The detailed material supports these scopes;
it is not a request for sixteen separate dispositions.

## Analysis

### 1. Authority, scope and evidence

The original owner request selected strategy recommendations for STDO revision
and project-local law. The present instruction is “evaluate and adopt any
refinements” to that proposal after Claude's solo review.

The subsequent owner correction is “stdo 2.5.1 is completely independent of t288
unless you mean there are post mortem checks to prove proposals”. This revision
withdraws the adopted T-288 closure dependency. Postmortem cases qualify the
method proposals within STDO's own scope; a downstream ticket supplies no gate.

`STDO-POSTMORTEM-STRATEGY-W02` succeeds W01 for this commentary revision. The
actor explicitly leaves coordination/evaluation and acts as Writer before the
effect. Its grant covers this file and a disposable comparison copy; it excludes
standards, Product Definitions, frames, tickets, ABI files, indexes, other posts,
Git effects, publication and consumer adoption. It uses the accepted
[source-project frame basis](../../../specification/REFERENCE_FRAME_BASIS.md)
with Product/Owner/Proof concerns and self-check. No independent qualification
of this revised proposal is claimed.

The [STDO authoring Definition](../../../stdo_default.json) still selects RC4,
manifest `4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`.
ABIogenesis separately selects RC7, manifest
`1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae`.
Both installed cuts were verified. RC7 is a reviewed subject, not substituted
authority for the authoring project.

Evidence:

- [Postmortem](../../../../../abiogenesis/.ai-workspace/comments/claude/20260920T041441Z_REVIEW_postmortem_march_to_september_week_by_week.md) and [reader returns](../../../../../abiogenesis/.ai-workspace/comments/claude/20260920T041441Z_POSTMORTEM_READER_RETURNS/README.md), with their stated sampling limits. Structured/prose returns are the same evidence.
- Founding commit `21f6fea92f33de849927dc952aeba33b54d9a24d`, checked during original authoring; selected RC7 admission, design, frame, ticket and release clauses.
- Current [ABI realization constitution](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/design/ABI5_REALIZATION_CONSTITUTION.md), [frame basis](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/design/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md), [T-288](../../../../../abiogenesis/.ai-workspace/tickets/active/T-288-remove-duplicated-runtime-construction.md), and the specific requirements, sampled tests and retained log cited in §5.

This is a synthesis with selected source checks, not a complete historical audit
or new runtime/paid-actor qualification. The reported 68 test files and 54M-token
comparison were not reproduced. ABI HEAD remained
`adaeede022a105cbc358799029d4e063cfa55426`; at 2026-09-20T06:44Z Git reported
470 status entries, rather than the earlier 456. Mutable links locate owners;
they do not freeze evidence.

### 2. Lessons and necessary corrections to the postmortem

1. **Validity was replaced by repetition.** The founding stale-success defect
   needed evidence tied to the current subject. Unconditional re-execution
   repaired it locally while leaving the validity relation implicit.
2. **Local success did not establish path adequacy.** Correct bounded reviews
   missed cumulative work across the combined execution path. Small contexts
   amplified this; they did not originate it.
3. **Acceptance shaped implementation.** Negative predicates made guards into
   deliverables; structural metrics missed equivalent computation under
   different names. Retention and addition need an applicable obligation.
4. **Restrictions lost their positive counterpart.** ABI permits subordinate
   caches and requires incremental projection. Blanket prohibitions in derived
   instructions are fidelity/application defects.
5. **Repricing lost continuity.** Selected obligations and useful work need
   recoverable dispositions and checkpoints, not merely recorded rulings.
6. **Progress requires outcome evidence.** Installed usable paths expose the
   real constraints; assurance inventories alone do not.

Retain the review's conceded corrections: validity is finer than “once per
process”; validation extends beyond serialization to mutable resources, rollback
and changed authority; deleted lines are a proxy; and the defensible cost finding
is missing effective path-level operational qualification, not absence of every
cost provision. Framework overhead and transport faults can coexist.

The postmortem did not claim that absence of a final tag meant no delivery.
That attribution is withdrawn. Its concern was the missing convergence point
at which a line stopped adding. R6/R8 address closure and contraction. Required
cold reconstruction can remain; calling a superseded production path an oracle
or compatibility layer cannot justify indefinite duplicate computation.

### 3. Where each kind of correction belongs

| Layer | Owns | Excludes |
|---|---|---|
| Shared STDO | Reusable relations for authority, validity, composition, proportional evaluation, fidelity and evidence | ABG event kinds, runtime topology, timeout constants, concrete counters or algorithms |
| Project Product/requirements | Supported outcomes, operating/threat model, retained behavior and material operational constraints | Method reinterpretation through implementation precedent |
| Accepted project design/local axioms | Domain-specific owners, basis/invalidation relations, realization constraints and foundation choices | Silent overrides of Product, requirements or selected STDO |
| Project reference-frame basis | Which evaluations activate, their subjects, capability, exclusions, results, invalidation and conjunction | New runtime truth or semantic authority merely from a role label |
| Code, tests and work carriers | Realization, executable checks, selected work and durable evidence | Creating law because a guard, test or ticket already exists |
| Representation, indexes and skills | Faithful source-linked retrieval, projection and native guidance | Independent meaning, a second fact registry or proof of correct application merely from retrieval |

A local axiom is adopted in its existing owning Product, requirement or accepted
design surface. A Product Definition may locate it; an index may expose it.
Neither listing creates authority. Use references to one deciding clause rather
than copy the same rule into a new local-law file, every ticket and every prompt.

### 4. Shared STDO revision recommendations

These are amendment candidates to be reduced against repair evidence, not eight
selected tickets or review rounds. Most underlying law already exists.

#### R1 — Make validity-preserving reuse explicit

**Owner:** [SPEC_METHOD](../../../specification/standards/SPEC_METHOD.md),
Complete Enclosing-Relation Admission (`STDO-UP-021`) and Reconstruction Litmus;
[DMM](../../../specification/standards/DESIGN_MODULE_METHOD.md) consumes the relation.

An admission owner remains responsible for its complete governing relation. It
may consume established facts whose subject, basis, scope, provenance and
validity still apply. A function boundary alone invalidates none of these;
material mutation, changed authority/basis or a real trust boundary requires the
applicable validation before effect. Reconstructability requires a correct
reconstruction route, not reconstruction at every use. Preserve the original
stale-success falsifier and independent semantic responsibility.

Apply this to the method itself: reuse classification, source acquisition,
computed facts, judgments and rulings on their material basis. A role,
conversation or status update is not an invalidator. RC7 `TICKET_METHOD` already
states judgment/ruling continuity. Correct contrary practice first; add no fact
registry or proof class per fact.

#### R2 — Bind a dedicated computational whole-path evaluation

**Owner:** optional [reference-frame baseline](../../../specification/standards/STDO_REFERENCE_FRAME_BASELINE.md),
consuming DMM Computational Realization Projection (`STDO-UP-019`) and recurrence
law.

A material composition/recurrence change receives an identifiable result for
one complete producer-to-consumer path: fact establishment, consumers,
invalidators, effects, retained alternatives and total work. Detect equivalent
computation across names without assuming semantic equivalence. The Executive
consumes this result; a collection of local successes cannot replace it.

Protect attention without requiring another permanent agent or per-helper
review. Distinguish Worker read scope from write territory: inspect the causal
cone, mutate only the grant, return cross-boundary repairs to their owner. Use
existing Operator, Owner, Reuse/Foundation, Proof and end-to-end frames. Preserve
[accepted T-031](../../tickets/completed/T-031-bind-end-to-end-interface-integration-frame.md)
and its source-only acceptance boundary; it is not already in released RC7.
Reuse valid unchanged results.

#### R3 — Qualify the material operational envelope

**Owner:** DMM computational realization; SPEC_METHOD qualification consumes the
design assumptions. Products own workloads and numerical limits.

For material algorithmic work, declare the input dimensions and operational
assumptions required for the outcome, then challenge them on representative
supported paths and relevant growth. Bind limits before qualification. Measure
work directly where time cannot localize it, without repeating the operation to
count it. Separate startup, framework processing, external compute, transport
and assurance. No universal O(1), token quota or human baseline is proposed.

Include method cost: repeated context acquisition, preimage hashing, activation
preparation, status recording, review and evidence regeneration. Name the change
or decision each repeated operation serves. Exact checkpoint identity may
justify a preimage; unchanged status does not require rehashing everything. The
reported token total needs a measured basis before supporting a limit or causal
claim. Existing proportionality law should govern this correction too.

#### R4 — Make threat-model and requirement ownership constrain findings

**Owner:** Reviewer applicability/exclusions in the reference-frame baseline,
under SPEC_METHOD's Product/requirement/design separation.

Findings identify a violated property, supported entry/state, operating model
and credible causal path. A repair mechanism becomes a requirement only through
its owner. Apply this to existing tests as well as new findings: an excluded
threat alone gives a guard or acceptance predicate no retention claim.

Retain justified untrusted-input, mutable-state, effect and authority checks at
their actual boundaries. In-process location alone does not prove trust;
hypothetical hostility alone does not establish applicability. New threat
assumptions require explicit repricing. ABI's desktop threat model remains local.

#### R5 — Qualify semantic fidelity through compression and activation

**Owner:** existing STDO compression/frame law; Representation owns source-linked
interpretation and guidance; Axiom Indexer owns generic mechanical validation.

Derived instructions preserve applicability, obligations, permissions,
exclusions, decision owners and invalidators. They cannot turn a conditional
prohibition into an absolute one. For changed shared guidance, use native tasks
with source-derived expectations; digests and maps cannot prove usable meaning.
Test affected chains and retain any calculus limitation explicitly.

A direct local sentence correction is smaller work. Restore ABI's bootstrap
permission now from existing law; no shared re-authoring or native-UAT campaign
is prerequisite merely to correct it. References work only when the actor can
resolve them; closed-prompt lanes need the relevant content. Access to `a_c`
establishes access, not correct application.

#### R6 — Close replacements by disposing of superseded responsibility

**Owner:** SPEC_METHOD core-interface migration and DMM recurrence/commonization.

Retirement is the default for superseded production responsibility. Retention
bears the burden: current supported obligation, owner, purpose, execution scope,
cost and retirement condition. Temporary compatibility or comparison machinery
needs a bounded expiry/removal trigger. Existing tests, safety labels and nominal
demotion do not justify duplicate production work.

Cold reconstruction and independent test oracles can serve distinct supported
purposes, separately from the ordinary hot path. Required replay is not a
predecessor that must expire. Where an obligation survives replacement, locate
its surviving owner; where the alleged obligation is excluded, do not invent a
replacement guard. Prove retained behavior, not unsupported threats. Do not defer
deletion until unrelated whole-Product completion. Judge removed work and
maintenance burden; names, shared algorithms and deleted lines are diagnostics.

#### R7 — Conserve rulings, obligations and durable work through repricing

**Owner:** [TICKET_METHOD](../../../specification/standards/TICKET_METHOD.md) and
SPEC_METHOD continuation/repricing.

Retain, supersede, defer or withdraw affected obligations in the existing work
carrier, preserving authority/evidence links. Copy no unaffected history and
create no parallel ledger. Present owner decisions as a short consequence delta;
preserve original wording separately. “Continue” does not accept an undisclosed
architectural change.

Recommend an immediate ABI preservation commit, explicitly WIP and unaccepted,
with parent and included territory recoverable. Coordinate concurrent Writers
and retain evidence outside Git. Preservation needs no claim of independent
acceptance and does not publish or promote. This revision performs no commit.

Examine the mutation lock's operational cost. Current role separation governs;
a bounded Writer grant may cover its declared status/checkpoint sequence. RC7
permits sufficient direct Writer entry and condition-based result recording,
without a new Executive appointment per update. Record actual role transitions
in the existing carrier and reuse valid grants. If the rule itself remains a
measured obstacle after those permissions are used, return it to its owner;
neither silent waiver nor manufactured ceremony resolves the concern.

#### R8 — Keep delivery and method evolution anchored to usable paths

**Owner:** SPEC_METHOD proportional delivery/qualification; project Goals select
the supported path.

Each increment advances a supported outcome against a standing runnable baseline.
A prerequisite names its blocked claim and return condition. Qualification uses
the ordinary entry; genericity and actor usability need their own witnesses.
A restart explains why retained-subject repair is insufficient, what survives,
and which causal assumptions change. Re-derivability alone does not select it.

Keep the selected method basis through the bounded delivery increment unless
its owner changes it. STDO 2.5.1 proceeds on its own amendment and qualification
basis while T-288 proceeds under ABI's selected authority. Reuse relevant repair
evidence without waiting for that ticket or coupling the release to it.
Publication, acceptance and consumer adoption remain separate; no additional
final cut is required.

### 5. Recommended project-local axioms and bindings

These recommendations specialize the shared principles without installing
ABIogenesis architecture into STDO. The identifiers below are discussion labels,
not assigned requirement IDs. Ratification edits the existing deciding clause;
frames and indexes refer to it.

#### ABI-L1 — Separate runtime history, active derivation and mutable worksite

**Owner:** ABI Product and relevant event/Run requirements; realization
constitution §§3 and 5.7; mutable-worksite frame.

**Recommended local relation:** admitted events retain runtime causal and audit
truth. A live operation consumes applicable current derived state and current
workspace observations. Cold reconstruction and incremental execution obey the
same ABG-owned semantics. Historical workspace observations are evidence; they
do not recreate or replace the physical mutable workspace.

Incremental projection is already required by §5.7. Implementing that arm is a
repair under existing authority, not a new Product feature. A failed Run remains
historical evidence; a later authorized occurrence can inspect surviving work
and consume applicable evidence without rewriting the failed Run. This does
not select general graph re-entry, automatic resume or the deferred executive
consequence capability.

**Telemetry placement:** keep diagnostics with no causal/admission purpose out
of the truth log; justify each retained source observation by its supported
runtime use. A blanket “liveness observations are not truth events” conflicts
with current [EVENTS-013 and EVENTS-022/023](../../../../../abiogenesis/specification/requirements/abg/REQ-R-ABG3-EVENTS.md),
which require actor source facts and consequential activity probes. Removing
those requirements needs `requirement_reprice`; reducing redundant work within
them does not. Reconcile the minimal durable supervision facts, diagnostic
storage and replay behavior locally rather than leaving the volume unexamined.

A read-only recount of retained LIVE03 verified 6,464 events, of which 3,102
stdout observations and 3,224 activity probes comprise 97.8651%. That is an
event-count share, not a CPU attribution. The log SHA-256 is
`680c6712b358e803a5a7089b4e4c44408195f0f67e9695c491e4b1c6c92a1f81`;
the [retained log](</Users/jim/Library/Application Support/ABIogenesis/candidates/T287-MGMT04-LIVE03-hN38UR/resources/events/runtime.events.jsonl>)
is the measured subject, not the repaired runtime.

**Payload placement:** use the external-body permission already in
[PAYLOAD-004](../../../../../abiogenesis/specification/requirements/abg/REQ-R-ABG3-PAYLOAD.md)
to design reference-and-digest carriage for bulky immutable artifacts, locks and
declaration inventories. Keep compact causal fields in the event. Specify the
body owner, immutable availability, retention, admission and cold-replay
resolution before replacing embedded bodies; otherwise the change relocates
reconstruction cost or makes history unreadable. A universal ban on event bodies
is not existing law and is not adopted here.

The same LIVE03 log embeds 2,227,866 bytes of artifact and 2,238,797 bytes of
resolved lock in ordinal 1, measured as compact UTF-8 JSON; ordinal 2 repeats
the lock. This verifies the material population without reusing the historical
218 KB figures as current. Choose the smallest local design change that removes
repeated bulky carriage while conserving admission and replay; no history is
rewritten by this recommendation.

#### ABI-L2 — Carry established facts along the actual native call path

**Owner:** accepted prefix/transaction/native-boundary design and the relevant
owners, under the realization constitution; T-288 owns selected repairs.

**Recommended local relation:** preserve an owner's applicable derived value
from production through its consumers. Revalidate at actual ingress, append,
physical-effect or invalidation boundaries. Raw and foreign inputs retain their
required admission checks. Whole-prefix identity, selected-scope identity and
physical-file identity remain distinct where the contract distinguishes them.

Review prefix projections, native instruction assembly, joined CCall outcomes
and Public read context by their complete paths. T-288 already identifies these
families; do not create a competing backlog or freeze its current status here.
Any new carrier abstraction first proves a missing relation and a smaller
realization. No generic proof framework is preselected.

**Bootstrap correction now:** [ABI CLAUDE.md](../../../../../abiogenesis/CLAUDE.md)
and [ABI AGENTS.md](../../../../../abiogenesis/AGENTS.md) omit the positive
permission beside their process-local-authority prohibition. Add its existing
[Product](../../../../../abiogenesis/specification/PRODUCT.md#hog) relation:

> HoG may derive invocation-local frames, cursors, queues, resolved bindings and
> caches subordinate to one admitted Program and invocation. These values cannot
> alter Program meaning or become an independently published or resumed Program.
> Product-owned catalogs and views remain discardable constructions over their
> exact basis; ABG events own runtime truth.

This is a local fidelity correction under existing authority, not a new cache
design. T-288's current D17 “no cache” restriction narrows that implementation
grant; it is not a universal ban and this wording repair does not widen it.

#### ABI-L3 — Give ABG's supported path an explicit work profile

**Owner:** ABI's applicable Product qualification requirement, accepted
computational design and existing installed proof harness.

**Recommended local relation:** report native work per meaningful handoff,
startup separately, with the dimensions that drive it: prefix acquisition,
bytes visited/encoded, structural traversal, derivation entries versus actual
derivations, and actor/transport intervals. Exercise representative longer
history and retained payload sizes. Identify justified cold work separately.

Bind any acceptance limits to the supported workload and retained behavior;
this post chooses no seconds, ratios or one-read quota. A semantic operation
that needs a complete history scan declares that need. Adding diagnostic events
does not justify multiplying unrelated admission work by the full history.
Event retention and telemetry representation changes need their actual local
contract decision; this post authorizes no event deletion or store redesign.

Carry T-288's work counters into the existing installed regression lane as a
standing gate for its named removed responsibilities. Bind the workload and
expected allowed work before qualification, retain a representative longer
history, and require an explicit obligation/cost disposition for a regression.
Do not choose a quota to fit the last result or count work by repeating it.
Semantic/refusal and actual-path checks remain conjoined with the work gate;
wall-clock improvements alone cannot close it. This strengthens the persistence
of existing accounting rather than introducing another measurement framework.

#### ABI-L4 — Bind the trusted-desktop threat model to review and tests

**Owner:** existing ABI Product threat model, propagated into the project
reference-frame basis and affected assurance cases.

**Recommended local relation:** separate untrusted agent proposals and external
inputs from applicable values constructed through trusted deterministic owners.
Preserve physical freshness, path/effect confinement, stale-basis and accidental
misuse checks required for the supported desktop. A hostile in-process actor is
not silently added to the Product threat model by a test.

Audit the acceptance predicates that retain defensive computation. Retention
requires an applicable supported entry/state, owned obligation and relevant
counterexample. A predicate whose only counterexample is an excluded hostile
local threat has no standing as an acceptance gate. Remove that unsupported
obligation rather than requiring a replacement guard to inherit it. Where a
supported obligation survives, identify its surviving owner. Temporary retention
needs a purpose, cost and retirement condition.

Any conflicting live requirement returns to its owner; a test cannot create one.

The [C-Algebra operating model](../../../../../abiogenesis/specification/requirements/gtl/REQ-L-GTL3-C-ALGEBRA.md)
explicitly excludes reflected private fields and forged local objects, while
retaining malformed authored GTL and external `F_P` admission. The sampled
[reconstruction-conservation tests](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/test_env/tests/t287-reconstruction-conservation.test.mjs)
and [authenticated-owner-value tests](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/test_env/tests/t287-authenticated-owner-values.test.mjs)
copy private receipt descriptors and warrant this audit. By contrast,
[rival-authority-mutations](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/test_env/tests/rival-authority-mutations.test.mjs)
also contains raw-schema refusal, actual-path fault injection and positive
rehydration cases. Classify predicates and their production consequences; do
not delete a file because of its name or a “forged” word count. This is a bounded
sample, not a completed audit of the reported 68 files. Audit each affected
repair cone without turning unrelated predicates into new T-288 blockers.

#### ABI-L5 — Supervision preserves output and reports cause truthfully

**Owner:** ABI worker/Run contracts, actor-adapter design and the existing
supervision owner; T-287 retains its separate live-actor issue.

**Recommended local relation:** silence on one transport channel is not a
semantic verdict on an actor. Declared supervision uses observations that the
selected adapter can actually supply, preserves available output and distinguishes
actor failure, transport fault, native processing, deadline and cancellation
through leaf, workflow foldback and Public projection.

Lease policies and probes are ABG/adapter realization. Their semantic outcome
and causal reporting belong in ABI's requirements where not already sufficient.
Keep this repair separate from the reconstruction-cost diagnosis. Do not infer
that eliminating overhead fixes every actor timeout, or that extending a timer
fixes overhead.

#### ABI-L6 — Context is usable, current and proportionate

**Owner:** [instruction-assembly requirements](../../../../../abiogenesis/specification/requirements/abg/REQ-R-ABG3-INSTRUCTION-ASSEMBLY.md),
GTL context declarations, accepted assembly design and the existing end-to-end
interface/worksite frames.

**Recommended local relation:** the actor receives its task, applicable
reference frame, exact selected constitutional binding, usable contract domains,
relevant current workspace observations and sufficient predecessor evidence.
Passing complete predecessor documents is not a default proof of sufficiency.
Closed-prompt lanes receive required content; tool-capable lanes can receive
resolvable references and the means to acquire it.

For a run selecting STDO, its declared environment binds the STDO version and
applicable `a_c` access. Generic GTL/ABG/HoG mechanics remain independent of STDO
interpretation. Admission rules cannot require information withheld from the
actor. A successful `a_c` call supplies access evidence, not an assurance that
the actor applied the law. No post-5.0 optimizing compiler is required for this
bounded correction.

#### ABI-L7 — Preserve framework and builder ownership

**Owner:** ABI Product/accepted GTL–HoG–ABG design and odd_glc's own Product and
GTL lifecycle definitions, through their explicit composition relation.

**Recommended local relation:** the CLI/API remain supported entry/projection
surfaces; they do not introduce a second orchestration truth. HoG retains its
graph-function traversal role and ABG retains its event/admission mechanics.
odd_glc owns the generic development policy and declared workflow. Concrete job
data belongs to the authorized job/workspace binding, not a Hello-specific
installed generic Product.

Coder-native facilities are reused where the required perimeter and effects can
be governed. Recursion and graph evaluation serving independent responsibilities
remain lawful computational tools. Neither resemblance to a coding agent nor
shared algorithms alone justifies deletion. Preserve the accepted C1/C0 effect
chain while evaluating the actual computation at each C2 boundary.
Qualify generic builder claims with two materially different ordinary jobs on
the same installed bytes and supported Public path.

**F_D/F_P placement:** classify total mechanical work and semantic work under
existing [Instruction Assembly-007](../../../../../abiogenesis/specification/requirements/abg/REQ-R-ABG3-INSTRUCTION-ASSEMBLY.md)
and Product compute law. A retained worker capability does not justify routing
an otherwise total mechanical step through an LLM. The current C2 prompt relays
one exact Bash command and its unchanged acknowledgment, but the
[accepted C2 design](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/design/T287_W2_R3_C2_WORKSITE_COMMAND_EXECUTION_DESIGN.md)
explicitly selects `F_P`/`worker_executes`. Reconcile that choice through its
local design owner. A fixed command does not by itself prove the complete
external operation is a total `F_D` function; preserve effect authority, observed
failures and downstream semantic interpretation. The blanket instruction to
preserve C2's existing posture is withdrawn; it must earn retention on this basis.

**Framework scope:** “fix the framework” applies when the missing obligation
belongs to the generic runtime. Before admitting a downstream repair into ABG,
identify the reusable runtime relation and why the existing GTL function,
implementation owner, adapter or odd_glc policy cannot own it. Job-specific
instructions, validators and development policy do not become kernel law because
a scenario exposed them. Route an actual Product-boundary conflict to its owner;
the reported slogans do not override that ownership test. This is the proposed
boundary on framework growth, not permission to evade a generic runtime defect
with scenario-specific glue.

#### ABI-L8 — Bind the dedicated reviewer and durable continuation locally

**Owner:** [ABI project frame basis](../../../../../abiogenesis/build_tenants/abiogenesis/typescript/design/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md),
existing realization frames and current work selection.

**Recommended binding:** compose the end-to-end interface frame with Operator,
Owner, Reuse and Proof for a dedicated computational path result. Its bounded
subject can cross files and owners while its question remains narrow. Trigger
it for material handoff/basis changes, recurrence, replacement and known
whole-path regression; consume still-valid prior results for unaffected work.

The Executive maintains accepted outcomes, unresolved path-level defects and
the next dependency-ready work. It does not repeatedly inspect an unchanged
running actor or edit the worktree. Separately granted Writers preserve source
checkpoints and material evidence outside disposable temporary storage without
claiming acceptance. Existing work carriers retain the distinction.

### 6. Other project owners

| Project | Recommended responsibility | Boundary |
|---|---|---|
| STDO source project | Consolidate owning clauses and relevant frame/guidance projections; qualify the changed meaning against postmortem cases | Preserve its selected authoring basis and accepted T-031 work; no T-288 dependency; release and adoption retain their own selection |
| STDO Representation | Re-author affected source-linked chains, permissions and frame indexes; regenerate derived outputs; run changed-chain native UAT | No index entry becomes law; unchanged chains reuse valid evidence; regeneration alone is not semantic qualification |
| Axiom Indexer | Validate and index the admitted representations with existing generic mechanics | No ABG-specific prover/consumer graph, runtime cache manager or semantic decision engine is added by implication |
| ABIogenesis | Ratify only missing domain refinements and frame bindings; implement existing obligations through current owners and proof paths | Existing T-288 repair proceeds under RC7 where sufficient; no dependence on finishing a new method release |
| odd_glc | Keep the installed builder generic and declare the supported lifecycle/context/correction policy | Job content, supported graph behavior and reuse choices are not silently promoted into ABG kernel or universal STDO law |

If a fact → owner → producer → consumer → basis/invalidation relation is useful
in `a_c.ABI`, project it from accepted ABI design. The index helps a small
context find the relation before adding a guard. It remains a derived read
model, not a second authored registry or a runtime proof engine.

### 7. Qualification of the proposed method revision

Qualify STDO 2.5.1's admitted amendments using bounded cases derived from the
postmortem. Each case binds an owning clause or projection, expected lawful
behavior, the historical failure it must prevent and appropriate evidence.
Distinguish existing-law enforcement, local fidelity defects and missing shared
meaning before selecting the amendment.

Retained evidence, bounded reproductions and native tasks can supply these
checks. T-288 observations are usable inputs where their subject and basis apply;
neither its progress nor its closure is a prerequisite. If a particular method
claim needs an operational witness, specify that bounded witness within STDO
qualification rather than importing the downstream ticket. ABI's repair and
closure obligations remain independently owned.

Q1–Q7 are a case bank for the actual shared delta and its material counterexamples.
Use existing native-use/UAT machinery for changed guidance and claimed outcomes.
Bind expected decisions to the owning source clauses before presenting cases to
the actor. Mechanically decidable facts use independent executable checks;
native tasks establish whether ordinary actors can apply the rule and reach the
supported outcome. Independent semantic judgment can assess semantic work, but
an LLM agreeing with another LLM does not establish runtime performance or
mechanical conformance. Do not supply answer-shaped hints naming seeded defects.

| Case | Positive discriminator | Negative/counterexample discriminator |
|---|---|---|
| Q1 Validity and reuse | Reuse an applicable owner fact through internal consumers | Changed basis/workspace or foreign input triggers the required validation |
| Q2 Whole-path attention | Find repeated derivation across differently named owners | Preserve distinct effect, scope and physical-freshness checks |
| Q3 Compression fidelity | Source and guidance permit the same lawful projection | Detect blanket cache bans, stale mapping and admission-changing caches |
| Q4 Applicable threat model | Justify retained guards/tests through supported obligations | Existing tests cannot promote excluded threats into requirements |
| Q5 Replacement closure | Remove superseded work; justify retained purpose, cost and retirement | An oracle label cannot justify hot-path duplication; required cold replay remains |
| Q6 Reprice and preservation | Conserve obligations/evidence and preserve an unaccepted checkpoint | Reject dropped obligations, widened “continue” and preservation-as-release claims |
| Q7 Ownership and context | Place runtime law locally and supply usable current context | Detect consumer-specific STDO law, hidden validator domains, inaccessible references and Hello-specific generic Products |

These are proposed changed-relation cases, not executed results. Select only
cases covering the actual admitted revision and its material counterexamples;
reuse valid unchanged evidence. A failed case returns to its owning clause or
projection rather than opening another full campaign. Observe the qualification
work itself under R3 so that the proposed remedy does not recreate the cost loop.

ABI runtime qualification remains separate: retained semantic/refusal controls,
incremental/cold-replay agreement where claimed, complete installed path and
observed work under its declared workload. No LLM opinion qualifies those
mechanical properties. Conversely, doubles that already know private validator
rules do not qualify ordinary actor usability.

## Recommended Action

STDO qualification and ABI repair are independently scoped work.

1. **Consolidate and qualify STDO 2.5.1 independently.** Use the postmortem to
   select justified amendments and bounded positive/counterexample checks.
   Relevant T-288 evidence may be reused without waiting for its completion.
   R1/R3 may need normative re-entry; R2 primarily concerns profile application;
   much of R4–R8 already has law. Preserve accepted T-031 and reuse its unchanged
   work. Qualify changed relations and native use where claimed; no downstream
   repair ticket becomes a method-release gate.
2. **Keep local corrections with ABI's owners.**
   Recommend the paired bootstrap edit, an explicitly unaccepted preservation
   commit and a standing per-handoff regression gate in the existing installed
   lane. Audit affected guard/test predicates as T-288 removes work. Keep the
   separate supervision issue under T-287. C2 compute routing, event semantics,
   payload representation and kernel scope return to their actual owners where
   current law or accepted design must change; this proposal does not add them
   all as T-288 blockers or authorize their implementation.
3. **Release and adopt only through their existing selections.** If a subsequent
   release instruction selects `2.5.1-rc.1`, follow the complete
   [coordinated cohort procedure](../../../../STACK_RELEASE.md): STDO, distributed
   skills/plugin, Axiom Indexer, Representation and `a_c.STDO` program/map must
   remain exact and matched. Re-author changed meaning before regeneration;
   verify inventories, qualification, refs, publication and public reacquisition.
   Preserve earlier cuts. Consumer adoption separately selects each exact basis
   and removes or redirects superseded local copies; publication never retargets
   a consumer automatically.

Success is a governed actor making the correct bounded decision, and a governed
Product completing its supported path with justified work. More constraints,
larger indexes, more reviews, fewer lines or another version label establish
none of those outcomes on their own.
