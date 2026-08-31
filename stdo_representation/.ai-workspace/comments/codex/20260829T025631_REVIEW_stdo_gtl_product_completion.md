# REVIEW: STDO.gtl Product Completion

**Author**: Codex
**Date**: 2026-08-29T02:56:31+10:00
**Addresses**: `GOAL-002`, `T-003`, constructed STDO.gtl Product candidate
**Status**: Open; revised against the active Product reprice

## Third Revision — Upstream STDO Bootstrap And ABIogenesis Dogfood Boundary

**Revision date**: 2026-08-29
**STDO comparison cut**: published immutable `v2.4.3-rc.3`, commit
`eb87a20247beeb93de394523ebdf8faecfd71949`
**Live unreleased calculus SHA-256**:
`23ccd77840c8d246b49ce59804c27735739830d9b097342af1ec8c21523b3db8`
**Live STDO Representation Product SHA-256**:
`42b0eb5bc19277b0aefc0aea42a719c00d374f4be825f4c8bde68ab9ab67e1fe`

This revision records the required cross-Product bootstrap before
`stdo_representation` can complete or govern construction of Abiogenesis 5.0.
It does not amend either Product and does not accept a moving candidate.

### Revised disposition

`stdo_representation` is the correct dogfood mechanism for producing bounded,
role-specific reference-frame context from STDO. It is not yet eligible to do
so authoritatively.

The clean dependency order is:

```text
released STDO principles
  -> independently released a_c

a_c + exact successor STDO subject
  -> separately accepted a_c.STDO

accepted a_c.STDO + exact GTL carrier profile
  -> separately admitted a_c.STDO.GTL

a_c.STDO.GTL + role assignment + mutable Abiogenesis workspace W_n
  -> projected ContextPacket
  -> Abiogenesis-hosted traversal through internal HoG
  -> authorized worker effect W_n -> W_n+1
  -> evaluation and a new immutable traversal occurrence
```

`ABI`, `ABG`, and `Abiogenesis` name the Product in this review. `HoG` is its
internal traversal engine. No separate ABI-to-ABG integration boundary exists.
The current upstream use of `ABG` as a generic method-role name therefore needs
an explicit terminology decision before the new STDO cut: either rename that
generic role or state unambiguously that Abiogenesis is its concrete Product
identity. Equal spelling must not create two owners.

### Current release reality

- Abiogenesis 5.0 still selects STDO `v2.2.2`.
- The latest published immutable comparison cut is `v2.4.3-rc.3`, but no human
  acceptance record for RC3 was found; the latest clearly human-accepted cut is
  `v2.4.3-rc.1`.
- `specification_methodology` currently contains an uncommitted T-015
  `AXIOMATIC_CALCULUS.md` candidate. No immutable STDO release contains `a_c`.
- This source project remains pinned to `v2.4.3-rc.3` and has no released STDO
  Representation Product.

Abiogenesis should therefore not first adopt RC3 and then immediately rebase
again. The bounded path is to use RC3 as the comparison subject, complete and
accept one successor STDO release containing the selected global corrections,
then have Abiogenesis adopt that one exact cut.

### What is already global in current STDO

Do not copy these Abiogenesis-local formulations into STDO as new laws:

1. `ODD_METHOD.md` already distinguishes mutable workspace `W` from immutable
   ledger `L` and event/replay spine `E`, and states that probabilistic
   construction acts in `W`.
2. It already makes cumulative workspace state authoritative over
   last-output-feeds-next-input wiring and makes replay-visible yield the lawful
   iteration boundary.
3. `REFERENCE_FRAME_METHOD.md` already defines finite role/capability-bound
   activation, exact basis, material sufficiency, recharting, closed results,
   coverage audit, and historical-failure-driven revision.
4. It already treats long implementation loops, repeated resets, invisible
   violations, and passing local proof that masks an unbound outcome as
   missing-frame signals.
5. `DESIGN_MODULE_METHOD.md` already requires affected-invariant accounting
   through design transformation.

The failure in the recent Abiogenesis work was principally an adoption and
frame-activation failure: the Product remains governed by STDO `v2.2.2`, which
predates the released reference-frame method and workspace-ledger law.

### Candidate global deltas for the successor STDO cut

The upstream review should disposition, rather than automatically accept, the
following narrow candidates:

1. **Traversal occurrence and causal DAG.** State explicitly that a traversal
   definition may be revisited, while every application is a fresh immutable
   occurrence over current terrain. For an effectful ODD specialization:

   ```text
   O_n = F_K[v](W_n, context_n, intent_n)
       -> result_n + effect(W_n, W_n+1)

   cause(O_i, O_j) => i < j
   ```

   Occurrence causation is acyclic even when the declared Product graph or
   lifecycle permits recurrence.

2. **Worker mutation wording.** The released Worker baseline grants inherited
   construction/transformation authority but also says `no mutation`. Clarify
   that a Worker may mutate the exactly authorized workspace and may not mutate
   or self-admit governed event, ledger, acceptance, continuation, or decision
   truth.

3. **Frame-activation lifecycle triggers.** Decide whether the current
   declare/activate/evaluate/revise relations sufficiently require activation
   at material lifecycle checkpoints. If not, add trigger, immutable activation
   identity, closure/refusal/invalidation, and fresh reactivation on changed
   basis. Do not create a runtime frame subsystem.

4. **Invariant representation in `a_c`.** Decide whether invariants are a
   declared `Constraint` specialization or a first-class record. In either
   form, transformation, composition, projection, and traversal occurrence
   must preserve, explicitly change, or refuse each material invariant.

Abiogenesis-specific event kinds, GTL.TypeScript restrictions, HoG internals,
catalog schemas, retry policy, feature families, and workspace-concurrency
mechanics remain local Product law.

### Why the current Product must re-enter after STDO release

The current Product still binds interpretation and encoding too tightly:

- its identity contains tenant/carrier/profile coordinates before an
  independently accepted `a_c.STDO` Product exists;
- its model `P_B = (B,I,V,E,C)` does not yet match the candidate calculus model
  `M_b = (b,I,O,E,C,L,X)`;
- latitude and residual uncertainty are not yet first-class accepted model
  content; and
- implementation remains historical `0.7.0`; there is no current semantic
  compilation candidate, selected `a_c.STDO`, admitted `a_c.STDO.GTL`, complete
  Context Packet, measurement, Product acceptance, or release.

After the successor STDO release, this Product requires `product_reprice`
against that exact immutable basis. Existing RC3 and 0.7.0 artifacts remain
historical evidence; they cannot be relabelled as the new Products.

### Mandatory Abiogenesis dogfood gate

Before Abiogenesis 5.0 construction resumes:

1. Freeze one high-risk Abiogenesis slice containing the mutable-workspace
   effect invariant.
2. Produce separate Executive, Worker, and Reviewer assignments. Each binds the
   exact released parent Product, workspace coordinate, outcome, intent, role,
   actor capability, activated frames, grants, evidence, stop algebra, and
   context budget.
3. Reproduce each least lawful projection, included/omitted identities, carrier
   digest, and token count. A budget may hold; it may not trim a mandatory law.
4. Supply each Context Packet alongside the mutable workspace, never instead of
   it.
5. Prove Executive selection/disposition authority, Worker bounded mutation
   authority, and Reviewer independent read/evaluation authority remain
   distinct.
6. Run falsifiers for omitted workspace-effect law, stale workspace basis,
   cross-bound role grants, missing evidence, insufficient capability, and
   exceeded token budget. Each must refuse, hold, or return an explicit
   residual.
7. Compare full-STDO and projected-context runs on the same model and task.
   Acceptance requires material context reduction without losing the invariant
   or role boundary that would have caught the snapshot-as-state-carrier defect.

Only that result establishes that `stdo_representation` can govern the
Abiogenesis build. ABIogenesis-local Product, requirements, design, source, and
workspace evidence remain separate inputs. Encoding them later would require a
separate `a_c.Abiogenesis` or explicitly governed composite-model Product; they
must not be smuggled into `a_c.STDO.GTL`.

### Clean cut order

1. Complete the exact RC3-versus-Abiogenesis axiom ledger.
2. Repair and independently review only the accepted global STDO deltas.
3. Finish, review, human-accept, and publish one immutable successor STDO cut
   containing `a_c`.
4. Reprice this Product against that release.
5. Construct and accept `a_c.STDO` independently.
6. Encode, structurally admit, and release `a_c.STDO.GTL` independently.
7. Pass the Abiogenesis role-context dogfood gate.
8. Reprice Abiogenesis from STDO `v2.2.2` to the successor cut.
9. Resume Abiogenesis 5.0 construction.

Until those gates close, the current Product remains **NO-GO for release or use
as governing Abiogenesis context**, while its revised algebra remains useful
authoring work.

## Second Revision — Functor Algebra Clarification

**Revision basis**: live `PRODUCT.md` blob
`b8f44ffb13965d0649a4bedce665eb89aa998a36`
**Computed live WHAT identity at review time**:
`sha256:83ea94fb4243e2e23191d7621672d5b205c40cc6c00a8bd9695e582f076070c3`

This section supersedes the first Product-reprice revision immediately below.
The other session has materially corrected the algebra.

### Revised algebra verdict

The functor algebra is now substantially coherent and consumable as
constitutional WHAT.

The Product now distinguishes exactly:

```text
F_K       = one imported functor-kind identity: F_D | F_P | F_H
v         = one exact declared vector or edge-traversal identity
F_K[v]    = classification/application of functor kind F_K to traversal v
operation = domain work realized by the traversal, not an alias for F_K
actor     = the implementation or agent realizing that traversal occurrence
```

The main relation is now closed:

```text
S_B = (B, M_B, D_B)

F_P[v_compile](S_B, I_C, R_C, K_C, A_common)
  -> Q_B* = (P_B*, L_B*, X_B*) | hold | gap | refusal

D_Q = F_D[v_candidate_structure](Q_B*, A_common)
  -> eligible | refuse

F_H[v_select](Q_B*, S_B, D_Q)
  -> (P_B, L_B) | rework | reject

Encode_T(P_B, Profile_T, CarrierBasis_T)
  -> G_{B,T}*
```

`S_B`, its basis/member/byte components, compilation coordinates, candidate
payload, accepted algebra, ledger, tenant coordinate, and star notation are now
defined. `SemanticCompilationCandidate`, `CompilerInvocation`,
`CandidateStructureResult`, `Residual`, `ProposalDisposition`, and
`SelectionLedger` now have closed schemas and content-derived identities.

The prior Product-reprice findings have these new dispositions:

| Earlier revision finding | Current disposition |
|---|---|
| R1 undefined symbols and dropped residual | **Resolved.** `S_B`, `L_B*`, `L_B`, `X_B*`, `Q_B*`, `D_Q`, tenant `T`, and `*` are defined and residuals cannot disappear. |
| R2 generated-source-key temporal cycle | **Resolved.** `F_P[v_compile]` proposes the deterministic preimage/hash, `F_D[v_candidate_structure]` reproduces it, and `F_H[v_select]` accepts or rejects its use. |
| R3 GTL influence on carrier-neutral compilation | **Resolved.** `F_P[v_compile]` takes only `A_common`; `Profile_T` enters after accepted `P_B`. An incapable tenant returns a gap/refusal. |
| R4 missing immutable compiler result and `F_H` lineage | **Resolved in WHAT.** Candidate, invocation, structural result, ledger, proposal dispositions, identities, digests, and provenance are specified. Realization remains open work. |
| R5 denotational/preservation and cross-Product overclaim | **Resolved.** “Declarative” replaces “denotational”; preservation is bounded to accepted records/purposes; generalization is assigned to an owning Product or shared method. |
| R6 token-minimality error | **Resolved.** `P_A` is the least lawful record closure; serialization/token measurement follow, and budget can only admit or hold. |
| R7 consumer/Quickstart role bypass | **Resolved in current text.** Bare index-plus-prompt use is explicitly exploratory and is not an `F_P[v_reason]` traversal, assignment, role activation, or disposition. |
| R8 lifecycle status and candidate-coordinate ambiguity | **Resolved in declared lifecycle.** Prior construction is historical evidence; current subjects are absent; future coordinates include WHAT and compilation-candidate digests. Implementation remains open. |

### Remaining A1 — Carrier admission must return a judgment, not a carrier

One formal defect remains at `PRODUCT.md:140-144`:

```text
F_D[v_carrier_admission](G_{B,T}*, Profile_T, CarrierBasis_T)
  -> G_{B,T} | refuse
```

That notation makes the `F_D` application appear to transform candidate carrier
bytes into different admitted carrier bytes. Elsewhere the Product correctly
states that domain HOW constructs the bytes and `F_D[v]` only evaluates or
proves declared properties.

Use an external judgment while preserving carrier bytes and identity:

```text
Encode_T(P_B, Profile_T, CarrierBasis_T)
  -> G_{B,T}

D_{G,T} =
  F_D[v_carrier_admission](G_{B,T}, Profile_T, CarrierBasis_T)
    -> CarrierAdmissionJudgment(admitted | refuse)
```

Define a closed, content-addressed `CarrierAdmissionJudgment` analogous to
`CandidateStructureResult`. Admission changes the carrier's governed status,
not its bytes, digest, or identity.

Minor notation clarification: the requirement's full `Q_B*` also contains
source, WHAT, frames, invocation, and provenance. Therefore write either
`payload(Q_B*) = (P_B*, L_B*, X_B*)` or show the full
`SemanticCompilationCandidate(...)` constructor rather than equating the whole
candidate to only its semantic payload tuple.

### Current gate status

At this exact read, the constitutional checker fails because `T-003` still
binds stale WHAT identity `sha256:7567d969...`, while the live WHAT computes to
`sha256:83ea94fb...`. This is a live-cut synchronization defect, not an algebra
defect. Recompute and update the ticket only after the authority text stops
changing.

The previous implementation/completion findings remain open where no
realization exists: semantic-compiler execution, artifact-facing decoder,
Context Packet admission, retained role-route proof, measurements, empirical
observations, independent review, Product acceptance, and release. They are now
properly represented as planned construction work rather than missing
constitutional meaning.

## Revision — Product Reprice Review

**Revision date**: 2026-08-29T03:17:15+10:00
**Reviewed Product blob**: `d7234ab2d1eda961ebcfaec6813b4d2586dad5c7`
**Current WHAT identity**:
`sha256:87260884485a2cb861f6e9d645445dd000e4b23ecc7b4c908dda8d00e9c2efc6`
**Repository HEAD**: `81039a876fe854cbb54b422d47cfc7d054f385c7`
**Repository tree**: `d8960511056a1fdb8d49425ab65d94eec1491ccc`

This revision supersedes the original Summary, Current Reality, and finding
dispositions below wherever they conflict. The original review remains in this
post as an audit record of the earlier authority basis.

### Revised verdict

The revised constitutional allocation is directionally correct:

```text
exact Source prose under B
  -> F_P semantic-compilation proposal
  -> F_H review and semantic selection
  -> accepted carrier-neutral algebra P_B
  -> tenant encoding
  -> F_D structural admission
  -> reliable carrier form G_B
```

This resolves the earlier concern that the Product did not explicitly say how
requirements-bearing prose becomes a symbolic programmatic representation. It
also correctly prevents GTL or `F_D` from claiming that probabilistic semantic
extraction is necessarily true.

The re-entry mechanics are now sound. `T-003` declares `product_reprice`, binds
the current WHAT identity exactly, refuses inheritance of the earlier WHAT
acceptance, and treats the retained `stdo.gtl` bytes as prior-basis evidence
rather than a current candidate.

The exact revised text is nevertheless **NO-GO as construction authority** and
the Product remains **NO-GO for completion, Product acceptance, release, or ABI
dependency**. The new semantic compiler is a real new Product capability and
completion cone, not merely explanatory wording. Its algebra, immutable result
contract, tenant boundary, and realization are not yet closed.

The bounded disposition is:

- **GO** for the Product-reprice direction and the `F_P -> F_H -> encoding ->
  F_D` authority order;
- **NO-GO** for freezing the current WHAT until the algebraic corrections below
  are made;
- **NO-GO** for construction until an immutable semantic-compilation candidate
  contract and evidence path exist;
- **NO-GO** for Product completion and release until the unchanged consumer,
  projection, evidence, qualification, and release findings close.

### What the revision resolves

| Prior concern | Revised disposition |
|---|---|
| The Product does not define the relation between Source prose and the symbolic representation | **Resolved in constitutional direction.** Semantic compilation is now an `F_P` proposal, `F_H` owns selection, tenant code owns encoding, and `F_D` owns structural evaluation. |
| The old constructed carrier was being treated as the current candidate after WHAT changed | **Resolved in T-003 and the main/tenant READMEs.** The retained bytes are historical construction evidence for the prior WHAT basis. |
| Re-entry skipped Product authority | **Resolved.** `T-003` now declares `product_reprice` and `re_entry_point: Product`. |
| GTL structural success could be read as semantic truth | **Resolved.** The Product and requirements explicitly limit GTL reliability to typed, closed, canonical, addressable, and structurally rejectable form. |
| Workspace, HoG, or ABG behavior might be pulled into this Product | **Resolved at the Product boundary.** The index remains passive; the consuming host owns workspace acquisition, invocation, events, and continuation. |

### R1 — The algebra is not yet closed or directly consumable

`PRODUCT.md:115-130` names the input `{prose text}_B`, candidate
`(P_B*, L_B*)`, accepted result `(P_B, L_B)`, and carrier `G_B`. Later,
`PRODUCT.md:146-148` refers to `S_B`, but `S_B` is never defined. `L_B*` and
`L_B` are also never defined. The matching requirement returns
`Candidate(P_B*, L_B*, X_B*)` at
`REQ-P-FP-CONSUMPTION.md:49-59`, but `X_B*` disappears from the Product flow.

Define every term once and retain residual uncertainty through selection. A
closed form is:

```text
S_B = exact ordered Source STDO corpus and member inventory under basis B

F_P:SemanticCompile(S_B, I_C, F_C, K_C, A_common)
  -> Q_B* = (P_B*, L_B*, X_B*) | hold | gap | refusal

D_Q = F_D:evaluate_candidate_structure(Q_B*)
  -> eligible | refuse

F_H:review_and_select(Q_B*, S_B, D_Q)
  -> (P_B, L_B) | rework | reject

Encode_T(P_B, Profile_T, CarrierBasis_T)
  -> G_B,T*

F_D:evaluate_T(G_B,T*)
  -> G_B,T | refuse
```

`L_B*` should mean the compiler-proposed selection rows and source bindings.
`L_B` should mean the final accepted Semantic Selection Ledger, including the
disposition of `X_B*`. `Q_B*` needs its own immutable identity; it is not a chat
transcript and is not the final ledger.

The constitutional checker passing does not close this issue. It currently
checks the presence of strings such as `SemanticCompile` and `Encode_GTL`; it
does not type-check the relation or detect an undefined symbol.

### R2 — Candidate record identity is temporally circular

Every `ProgramRecord` identity includes `SemanticAddress.source_key`. Under
`REQ-P-REPRESENTATION-ALGEBRA.md:92-104`, a generated source key is issued by
final `F_H` selection authority only after review of the `F_P` proposal. But the
new compiler relation says `F_P` returns candidate `P_B*` records for that
review. Those records cannot already possess their final identities if a
required identity coordinate does not exist until after the review.

Resolve this explicitly. The cleanest model is:

- `F_P` proposes each exact source-key preimage
  `{primary_source_locator, local_declaration_key}` and its deterministic hash;
- candidate structural admission reproduces the hash but grants it no semantic
  authority;
- `F_H` accepts or rejects use of that routing key in admitted `P_B`; and
- the accepted ledger records the proposal and disposition.

Alternatively define a pre-identity proposal type and mint final
`ProgramRecord` identities after `F_H`. Do not leave construction to guess
whether candidate identities are provisional or authoritative.

### R3 — The compiler currently violates the carrier-neutral boundary

The Product says `P_B` is carrier-independent and that build tenants are
independent HOW realizations. However, the `F_P` Semantic Compiler receives the
exact target GTL profile at `PRODUCT.md:60-63` and
`REQ-P-FP-CONSUMPTION.md:50-59`, before `F_H` selects `P_B`. The accepted algebra
is then encoded through the same profile again.

That ordering permits GTL representability to influence what the compiler
selects as Source meaning. It makes the supposedly common algebra dependent on
one tenant HOW.

The clean boundary is:

1. `F_P` targets only the common representation-algebra contract.
2. `F_H` selects the carrier-neutral `P_B` against exact Source prose.
3. Each tenant maps accepted `P_B` into its carrier profile.
4. A tenant that cannot encode accepted `P_B` returns a profile gap or refusal;
   the semantic compiler does not omit meaning to accommodate the carrier.

If tenant-specific semantic compilation is actually intended, the Product must
instead name `P_(B,T)` and define the cross-tenant preservation obligation. The
current text claims the carrier-neutral model, so the GTL profile should leave
the compiler input.

### R4 — The semantic compiler has no immutable Product-facing result contract

The new requirements declare an abstract `Candidate(P_B*, L_B*, X_B*)`, but no
constitutional or realized contract defines:

- canonical candidate bytes and candidate identity;
- the exact Source member inventory and digests presented to the compiler;
- WHAT/algebra identity, intent, frames, model/capability envelope, and budget;
- traversal identity, invocation provenance, stop state, and output digest;
- exact candidate records, proposed selection rows, and residuals;
- the `F_H` delta from compiler proposal to final accepted ledger; or
- reacquirable evidence binding the final ledger to the exact compiler output.

`REQ-P-SELECT-007` requires the exact proposal and complete traversal provenance
to be retained, but the `SelectionLedger` shape has no compiler-candidate
identity or digest. The current implementation also contains no semantic
compiler, candidate decoder, or candidate admission path. Outside the
constitutional checker, `SemanticCompile` does not occur in build-tenant code;
the existing Python preparer still creates records and selection material from
project-authored rules and policy.

Before construction reopens, define and realize an immutable
`SemanticCompilationCandidateRecord`, then require the final ledger to bind:

```text
candidate_identity
candidate_payload_sha256
compiler_traversal_ref
compiler_invocation_provenance_ref
reviewed_source_basis
F_H_change_set_or_exact_final_disposition
```

If the exact corpus and output cannot fit one actor call, the design must declare
a compilation DAG: immutable shard invocations, exact shard subjects, a closed
composition law, duplicate/omission refusal, and one final candidate identity.
Iteration must not be improvised as mutable conversation state.

### R5 — Two constitutional claims remain stronger than the algebra

First, `denotational reasoning program` and unconditional preservation of
`meanings` assert a denotation and preservation relation that the Product never
defines. `F_H` acceptance can authorize a selected interpretation; it does not
prove equivalence to the prose. Either define the denotation domain and the
preservation relation, or use the narrower claim:

> Semantic compilation preserves the exact records, relations, authorities,
> source routes, and residual uncertainty accepted under `F_H` for the declared
> reasoning purposes. It does not prove complete or unique natural-language
> interpretation.

Second, the cross-product statement at `PRODUCT.md:132-137` generalizes
`prose -> SemanticCompile -> algebra -> carrier` beyond STDO and GTL. That is a
candidate shared method, not current STDO Representation Product law. Ratify it
in `specification_methodology` if it is intended as reusable constitutional
method; otherwise keep this Product statement local to Source STDO.

### R6 — Least closure is not token minimality

`P_A = least_closure(...)` defines a least lawful identity set under the named
closure law. It does not prove a tokenizer-global minimum, and the context
budget does not participate in closure. The budget admits or holds the already
determined projection.

Replace `PRODUCT.md:211-214` with the narrower law:

> For one frozen assignment, seed set, parent index, and closure law, `P_A` is
> the unique least lawful record closure. Its token count is measured after
> carrier serialization. If it exceeds `K_A`, contextualization returns
> `budget_exceeded`; the budget never trims `P_A`.

### R7 — The consumer shorthand still enables a role bypass

`PRODUCT.md:197-201` says the Product is consumed by placing an index or
projection beside workspace input and intent. The Product's own complete
relation additionally requires the exact frame, capability budget, traversal
contract, and—when role-bound—Executive Context Assignment and projection
manifest.

The in-flight Quickstart currently turns that shorthand into an invalid claim:
it says attaching the retained index and workspace files lets an Executive
assign a Reviewer and that the response is `F_P` evidence. No exact assignment,
manifest, activation, grant, capability envelope, gates, provenance, or stop
coordinates exist.

Until the real role-bound path exists, that section must be either removed or
labelled accurately:

> This is an exploratory bare model invocation over retained pre-reprice bytes.
> It is not an Executive Context Assignment, Reviewer activation, Context
> Packet, claimed ODD `F_P` traversal, qualified Product observation, or
> authority-bearing disposition.

Use `Observation: potential falsifier`, not `Disposition: falsified`.

### R8 — Lifecycle text is improved but not yet internally exact

The main README, tenant README, and `T-003` correctly distinguish retained
prior-basis evidence from the absent current candidate. Three residuals remain:

1. `PRODUCT.md:581-586` says neither tenant has constructed an index and calls
   the GTL profile merely proposed and unaccepted. The repository did construct
   a prior-WHAT candidate and did accept the profile for that construction
   basis. State instead that no accepted construction basis or candidate exists
   for the active WHAT.
2. `build_tenants/gtl/representation/README.md:3-6` still calls the old artifact
   a current Product candidate.
3. The hard-coded `candidates/stdo-2.4.3-rc.3` coordinate cannot distinguish a
   second candidate for the same Source STDO release under the new WHAT. The new
   candidate path/identity must include a candidate or WHAT coordinate rather
   than overwrite or ambiguously reuse the prior one.

Prefer `invalidated for current candidacy by Product re-entry; retained as
historical construction evidence` over `superseded`, because Product/release
supersession is a separate release-record relation.

### Prior finding disposition after the reprice

| Original finding | Current disposition |
|---|---|
| P0-1 artifact-facing admission/decoder absent | **Remains.** The revised Product strengthens the need; no decoder, resolver, or released-Product loader was added. |
| P0-2 Context Packet lifecycle absent | **Remains.** Projection still returns only a `ProjectionCandidate`; admission, token measurement, capability holds, manifest, residual, and source re-entry are absent. |
| P0-3 retained role routes fail the real validator | **Remains.** No generator, validator, or retained-route proof changed. |
| P0-4 decision evidence not reacquirable | **Remains, repriced as a renewed-acceptance blocker.** The old candidate is already ineligible, but unchanged finalization would reproduce the defect. |
| P1-1 Quickstart role/`F_P` bypass | **Remains.** A prior-basis warning does not create the missing assignment and traversal contract. |
| P1-2 lifecycle/status contradiction | **Mostly resolved.** Re-entry is now explicit; the Product current boundary, representation README, and candidate coordinate still need correction. |
| P1-3 compression/usefulness evidence absent | **Remains.** |
| P1-4 independent review, acceptance, and release absent | **Remains and now occurs after a new current-WHAT candidate exists.** |
| P2-1 constructor too broad as consumer trust root | **Remains.** |
| P2-2 Unicode and zero-test fail-closed gaps | **Remains.** A plain `npm test` still reports zero tests against stale/absent build output; source tests require a successful build first. |

### Revised completion sequence

1. Close the Product algebra: define `S_B`, `L_B*`, `L_B`, and `X_B*`; resolve
   generated source-key timing; remove GTL from carrier-neutral semantic
   compilation; narrow preservation and closure claims; correct the consumer
   shorthand.
2. Recompute the WHAT identity and update `T-003` only after the text stabilizes.
3. Define and ratify the immutable Semantic Compilation Candidate and `F_H`
   proposal-to-ledger binding, including one-call versus DAG realization.
4. Implement the semantic compiler traversal, candidate admission, provenance,
   and adversarial refusal/omission/duplicate tests.
5. Reacquire and accept the frame basis and GTL profile against the corrected
   boundary, then produce and accept a current-WHAT Semantic Selection Ledger.
6. Construct the current candidate under a unique coordinate; retain all exact
   decision evidence; reproduce and structurally admit it.
7. Implement artifact-facing decode/admission/resolution and consume only the
   immutable carrier, not the build plan.
8. Complete assignment, role, projection, manifest, budget/capability hold, and
   Context Packet realization for Executive, Worker, and Reviewer.
9. Measure exact bytes/tokens/cost, run representative and adversarial `F_P`
   observations, obtain independent exact-subject review, accept the Product,
   then issue a separate release.

This sequence completes STDO Representation without adding ABI, HoG, ABG, or
workspace mutation to this repository.

## Summary

The current `stdo.gtl` is a credible, immutable construction candidate. Its
canonical bytes reproduce, its frozen-GTL structural gates pass, and its
identity and Source STDO basis are explicit. Keep that result.

The Product is not complete and is not ready for acceptance, release, or ABI
integration. The missing cone is bounded:

1. admit and decode the released carrier as the ordinary Product input;
2. construct and admit exact Executive, Worker, and Reviewer Context Packets;
3. retain exact compression measurements and representative/adversarial `F_P`
   observations;
4. repair the decision-evidence chain;
5. perform an independent exact-subject Product review, Product acceptance, and
   a separate release.

This is not a request for new ABI or GTL runtime features. STDO Representation
owns immutable carrier admission, semantic resolution, context projection, and
packet construction. A later consuming host, including ABI, owns workspace
acquisition, actor activation, invocation, events, and runtime continuation.

**Verdict**: **NO-GO** for Product completion, acceptance, release, publication,
or ABI dependency. **GO** for continuing `T-003` and retaining the current
carrier as a reproducible, structurally admitted candidate.

## Reviewed Basis

- Repository HEAD:
  `81039a876fe854cbb54b422d47cfc7d054f385c7`
- Repository tree:
  `d8960511056a1fdb8d49425ab65d94eec1491ccc`
- Branch state: `main`, five commits ahead of `origin/main`
- Concurrent worker delta, reviewed but not modified:
  `QUICKSTART.md`, blob `eaa61c706585829003b01a77d99100e7d5f8dbcc`,
  `+87/-2`
- Source STDO basis: `stdo://releases/v2.4.3-rc.3/`
- Installed STDO manifest:
  `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`
- Frozen GTL basis commit:
  `8d7f965a3fae7d1acea6a9db298798480fd4cc2f`
- Candidate Product identity:
  `urn:stdo-representation:product:sha256:85b1345ccc5b40bb4c482a90b8572d5cfc75c3a64d566aef41257649e286d9a6`
- Candidate content identity:
  `sha256:9c214136067d2873af3ff8db77b7c98903f7dfe700dea82bb166e0213cbab890`
- Candidate size: `153986` bytes
- Candidate population: 125 atoms, 88 typed semantic edges, 113 passive
  constraints, sourced from all 47 installed STDO standards members

The concurrent Quickstart change is in-flight evidence, not part of the pinned
committed tree.

## Current Reality

The following claims are supported:

- the Product Definition resolves and verifies against the exact installed STDO
  cut;
- the GTL representation profile, project frame basis, and Semantic Selection
  Ledger were accepted for this construction attempt;
- the carrier was constructed and reproduced byte-for-byte in a fresh
  directory;
- the retained carrier is canonical, content-addressed, structurally admitted,
  and basis-bound;
- the representation algebra and least structural closure are real
  implementation, not only prose.

The candidate README states the correct lifecycle status at
`build_tenants/gtl/representation/products/stdo-2.4.3-rc.3/README.md:1-4`:
constructed and reproduced, but not Product-accepted and not released. Its
lines 36-40 correctly limit the result to deterministic construction proof.

`T-003:56-79` also states the open work exactly: role assignments and
projections, token and cost measurements, frozen `F_P` observations,
independent Product review, Product acceptance, and release.

## Reference-Frame Results

| Frame | Result | Reason |
|---|---|---|
| Product boundary | **Falsified for completion** | The immutable candidate exists, but the ordinary artifact-facing consumer and release relations do not. |
| Basis and identity | **Satisfied for construction; falsified for decision evidence** | Carrier and Source STDO identities reproduce; acceptance evidence is not deterministically reacquirable from its recorded coordinates. |
| Graph and constraint fidelity | **Structurally satisfied; semantic adequacy indeterminate** | Closure, typed references, and carrier form pass. Independent semantic sampling and adversarial use remain open. |
| Public consumer boundary | **Falsified** | The API reconstructs from build inputs; it cannot admit/decode/query the retained `stdo.gtl` bytes. |
| Role and authority | **Falsified** | No admitted Context Packets exist, retained role routes do not pass the real validator, and role-specific grant prohibitions are unenforced. |
| Compression and usefulness | **Out of frame due missing evidence** | One carrier byte count exists; like-for-like token/cost measurements and frozen `F_P` observations do not. |
| Independent assurance | **Not activated** | No durable independent exact-subject Product-review result exists. |
| Release lifecycle | **Not reached** | Product acceptance, release manifest, release record, publication, and install qualification do not exist. |

## Findings

### P0-1 — The claimed Product cannot be consumed from its immutable artifact

The public package exports constructors, plan validation, encoding, structural
closure, and `constructProjectionCandidate`
(`build_tenants/gtl/code/src/index.ts:1-23`). It exports no artifact-facing
admitter, decoder, semantic resolver, or released-Product loader.

`constructProjectionCandidate` accepts the original `GtlBuildPlan`, all accepted
construction evidence, an assignment, and assignment bytes. It reconstructs
the parent from `plan.records` and projects those pre-encoding records
(`projection.ts:415-453`). It never reads the retained `stdo.gtl` bytes.

The missing ordinary consumer relation is therefore:

```text
admit_stdo_gtl(
  canonical_product_bytes,
  expected_product_identity,
  expected_content_identity,
  accepted_release_descriptor
) -> AdmittedSemanticIndex | invalid_basis
```

Admission must decode the tuple legend and tables, reject malformed or
out-of-range references, reconstruct every `ProgramRecord`, reproduce record,
content, and Product identities, validate closed references, and expose exact
identity/source lookup. A round-trip test must begin with the retained
`product/stdo.gtl`, not the build plan.

Until this exists, ABI would have to depend on STDO Representation's
construction internals rather than consume its Product. That is the wrong
boundary.

### P0-2 — The Context Packet lifecycle is specified but not realized

The requirements already define the required algebra:

- exact `ExecutiveContextAssignment` at
  `REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md:83-164`;
- least declared closure at lines 166-226;
- `ContextProjectionManifest` at lines 228-269;
- Context Packet contents at lines 271-285;
- distinct Executive, Worker, and Reviewer law at lines 287-321;
- budget/capability holds and invalidation at lines 341-414.

The implementation returns only `ProjectionCandidate`
(`contracts.ts:244-256`). That type omits the required manifest identity,
omitted count, tokenizer measurement, source re-entry references, residual
uncertainty, admitted disposition, selected frame declarations/evidence, stop
routes, and explicit `budget_exceeded` or `capability_mismatch` hold.

Assignment validation is also syntactic rather than executable. It verifies
canonical bytes, URI shapes, role spelling, seed membership, and numeric budget
bounds (`projection.ts:162-408`). It does not reacquire frame bytes, prove the
frame digest, resolve the assignment grant or capability envelope, acquire
required evidence, enforce Worker operation authority, or prohibit Reviewer
operation/decision grants. This directly leaves `REQ-P-CONTEXT-001` through
`014` open.

### P0-3 — The retained role routes are incompatible with the validator

`scripts/prepare_stdo_gtl_candidate.py:850-875` adds every constraint under
“Reference Frame Engagement Compression” to every engagement-role route. Each
retained Executive, Worker, and Reviewer route consequently has 15
`role_program_refs`: one role atom and the same 14 aggregate constraints.

`projection.ts:261-279` requires every `role_program_ref` to carry a
`SourceLocator` at the selected exact role fragment of
`STDO_REFERENCE_FRAME_BASELINE.md`. The 14 aggregate constraints cannot satisfy
that rule. The only projection test supplies `[role.id]`
(`carrier.test.ts:402-466`) and therefore never runs a retained route.

This must be resolved as a design choice, not weakened ad hoc. The likely clean
model is:

- `role_program_refs` contains only the exact role-owned records;
- frame material belongs in each activation's authorized
  `mandatory_program_refs`; and
- closure adds declared dependencies and applicable constraints.

Whichever model is selected must be accepted and all three retained routes must
pass the same production admission path.

### P0-4 — Acceptance decision evidence is not deterministically reacquirable

The three retained acceptance records carry relative evidence references such
as:

```text
selection-review.md?sha256=d8474d9c...
selection-policy.json?sha256=bac32a86...
projection-route-candidates.json?sha256=bf25e28e...
publisher/gtl-toolchain-product.json?sha256=b38a9e4a...
```

Those files do not exist relative to
`products/stdo-2.4.3-rc.3/acceptance/`. Their matching current bytes remain only
under the mutable `candidates/` tree. The authorization also cites repository
basis commit `21ee417...`; three of the four recorded evidence digests do not
match those paths at that commit.

The preparer creates digest-bearing strings
(`prepare_stdo_gtl_candidate.py:1287-1294`). The finalizer compares the strings
in the request and decision (`finalize_stdo_gtl_product.py:373-394`) and copies
them into acceptance records (`finalize_stdo_gtl_product.py:193-215`), but does
not resolve and verify the evidence bytes. In an isolated counterexample,
removing `selection-review.md` did not make finalization fail and did not change
the resulting Product or acceptance identities.

Repair the evidence contract so every decision evidence reference resolves
unambiguously from an immutable basis or a retained content-addressed bundle.
Finalization must reacquire every referenced byte, verify its digest, and refuse
missing or mismatched evidence before issuing acceptance records.

### P1-1 — The in-flight Quickstart creates a Reviewer/`F_P` bypass

The new `QUICKSTART.md:162-240` says an Executive can assign a Reviewer by
attaching the whole unreleased index, Product Definition, ticket, and diff to a
prompt. It names frame families and labels the returned text `F_P` evidence.

That is not the Product's declared role-bound invocation path. It omits the
canonical assignment, frame activations and digests, grant, capability,
workspace basis, tokenizer and budget, projection manifest, traversal identity,
output contract, evaluators, provenance, and stop states required by
`REQ-P-FP-002/003` and `REQ-P-CONTEXT-001/002`. Those requirements explicitly
state that a bare model invocation is probabilistic processing, not a claimed
ODD `F_P` traversal, and that a persona or role label does not activate work.

The example response also begins `Disposition: falsified`. A Reviewer returns a
result to Executive; it carries no disposition or next-activation authority
(`REQ-P-CONTEXT-010`).

Do one of two things:

1. remove this shortcut until the real assignment/packet path exists; or
2. label it strictly as an **exploratory whole-index model observation**, not a
   Reviewer activation, not a claimed `F_P` traversal, and not Product
   qualification evidence.

Do not let documentation become the bypass around the missing Product
interface.

### P1-2 — Live authority and lifecycle status contradict the constructed state

`README.md:82-95` and `T-003:56-65` say the GTL profile was accepted for exact
construction and the candidate was constructed and reproduced.

`specification/PRODUCT.md:482-489` still says the profile is proposed and
unaccepted and neither tenant has a constructed Product. The exact-byte accepted
`REFERENCE_FRAME_BASIS.md:244-257` retains “current residuals” saying no accepted
ledger, constructed index, canonical bytes, or post-construction review subject
exists.

The underlying problem is lifecycle state embedded in immutable authority. Do
not silently edit accepted bytes and inherit their acceptance. Separate stable
frame configuration from mutable status projection, or deliberately revise the
WHAT/frame-basis subjects, obtain new exact acceptance, and reconstruct under
the resulting new WHAT identity.

This is the only upstream re-entry in the completion cone. The algebra and
consumer boundary do not need a new ABI feature.

### P1-3 — Compression and usefulness remain claims rather than evidence

Only the 153986-byte carrier count is retained. There is no exact like-for-like
Source STDO inventory, tokenizer identity/version/configuration, token count,
compression ratio, price-bound cost calculation, or role-packet measurement.
These are required by `REQ-P-VERIFY-005` through `008` and `GOAL-002:88-95`.

There are also no frozen representative or adversarial `F_P` observations with
exact workspace task, intent, frame/assignment, source/index identities, model,
configuration, budget, prompt, time, output, and uncertainty. Required coverage
at `REQ-P-VERIFY-009/010` includes semantic-address recovery, authority and
bounded-context distinction, dependency and constraint use, cross-context
refusal, source re-entry, and budget pressure.

One successful prompt is not enough, and deterministic tests cannot replace
probabilistic-use evidence.

### P1-4 — Independent Product assurance, acceptance, and release are absent

No durable independent Reviewer activation/result exists over the exact
candidate and all material claims. No `subject_kind: "product"` authority
acceptance record exists. No release manifest or
`stdo-representation.release` record exists. The package remains `private: true`,
the local branch is not contained by remote `main`, and no release tag exists.

The order is fixed by `PRODUCT.md:285-394` and
`REQ-P-COMPRESSION-VERIFICATION.md:73-81`:

```text
exact candidate
  -> complete evidence
  -> independent exact-subject review
  -> human Product acceptance
  -> release manifest and release record
  -> publication/install qualification
```

Structural admission, token reduction, or one useful model response cannot
substitute for another step.

### P2-1 — The general constructor is too broad to be a trust root

The official finalizer protects the retained candidate through frozen inputs.
The exported generic constructor does not independently pin the exact Source
STDO, profile digest, publisher, authority actor, grant, and evidence bytes.
`validateBuildPlan` pins the profile identity but accepts several caller-provided
coordinates (`validation.ts:320-367`); acceptance validation checks multiple
authority fields only as non-empty strings (`evidence.ts:76-115`).

Keep construction APIs explicitly construction-facing or bind them through an
accepted release descriptor. ABI must consume the admitted immutable Product,
not treat a self-consistent build plan as its trust root.

### P2-2 — Two fail-closed test gaps remain

1. `canonicalJson` sends strings directly to `JSON.stringify`
   (`canonical.ts:15-35`) and accepts a lone UTF-16 surrogate, contrary to the
   Unicode-scalar/I-JSON requirement in `REQ-P-BASIS-AND-IDENTITY.md:48`.
2. `npm test` executes `node --test build/test/*.test.js` without a pretest build
   or zero-test refusal (`package.json:35-38`). With `build/` absent, it exits
   successfully with zero tests.

Neither affects the retained candidate bytes. Both should be fixed before a
published consumer package is trusted.

## Recommended Action

Use one bounded completion wave. Do not expand ABI or add workspace/runtime
behavior to this repository.

### Work package 1 — Reconcile authority and decision evidence

1. Decide whether mutable checkpoint text leaves Product/frame authority or
   whether those exact subjects are revised.
2. If WHAT or the accepted frame basis changes, issue a new exact acceptance and
   reconstruct; do not inherit the prior acceptance.
3. Define immutable, unambiguous evidence coordinates.
4. Make finalization reacquire and digest-check every decision-evidence byte.
5. Add missing, mismatched, wrong-basis, and relocated-evidence counterexamples.

**Gate**: the exact candidate can be reconstructed only when all selection and
acceptance evidence is independently reacquirable; deleting or changing one
evidence member fails before acceptance issuance.

### Work package 2 — Finish the artifact-facing algebra

1. Add `admit/decode` from canonical `stdo.gtl` plus accepted Product/release
   identity.
2. Reconstruct records and exact semantic lookup from carrier tables.
3. Validate canonical bytes, tuple bounds, legend, reference kinds, identities,
   closed references, source routes, content digest, and Product identity.
4. Change projection to consume `AdmittedSemanticIndex`, not `GtlBuildPlan` and
   construction evidence.
5. Keep workspace, prompts, models, events, HoG, and ABG outside this package.

**Gate**: the retained artifact round-trips from bytes to the exact 125/88/113
records and identities; tampered bytes, wrong Product identity, malformed tuple,
bad index, dangling reference, wrong digest, and lone surrogate all refuse.

### Work package 3 — Complete role-bound context construction

1. Resolve the role-route generator/validator contradiction under one accepted
   design.
2. Freeze exact Executive, Worker, and Reviewer assignments.
3. Resolve and verify frame declarations, grants, actor capabilities, required
   evidence, independence, stops, and return routes.
4. Measure the projection with the exact assignment tokenizer.
5. Return either an admitted `ContextProjectionManifest` and Context Packet or
   an explicit `budget_exceeded` / `capability_mismatch` hold.
6. Enforce Worker and Reviewer grant prohibitions.

**Gate**: all three retained role routes pass the production path; frame-digest,
grant, capability, evidence, independence, one-token budget, supersession, and
role-authority falsifiers fail closed.

### Work package 4 — Produce completion evidence

1. Retain exact Source-versus-index and role-projection byte/token inventories.
2. Bind tokenizer, configuration, model limit, price source, date, and cost
   calculation.
3. Run frozen representative and adversarial `F_P` trials through exact
   assignments and packets.
4. Retain prompts, outputs, identities, provenance, holds, gaps, refusals, and
   uncertainty without treating them as deterministic truth.
5. Make the package test command build or fail when it discovers zero tests.

**Gate**: measurements reproduce; trials cover all `REQ-P-VERIFY-009/010`
families; no bare prompt is counted as a claimed Reviewer or `F_P` activation.

### Work package 5 — Review, accept, release

1. Activate an independent Reviewer over the exact unchanged candidate,
   evidence bundle, measurements, and probabilistic observations.
2. Resolve every material finding and reconstruct if any Product coordinate or
   accepted input changes.
3. Have the declared Product owner issue the exact `subject_kind: "product"`
   acceptance record.
4. Create the release manifest and separate release record.
5. Publish the package/carrier, establish remote containment and an immutable
   release tag, then qualify a fresh install.

**Gate**: released bytes equal the reviewed and accepted bytes; the install
consumes only the immutable release artifact through the public consumer API.

## Verification Performed

- `stdo status --definition stdo_representation.json --verify`: passed; exact
  47-member STDO basis resolved.
- `python3 scripts/check_constitution.py`: passed. Its own declared scope excludes
  semantic adequacy and human acceptance.
- Python tests: 13/13 passed.
- Frozen ABI/GTL conformance probe: 11/11 TypeScript tests passed against the
  exact frozen GTL commit/tree.
- Fresh isolated reconstruction: all constructor-produced bytes reproduced.
- Plain package `npm test` with no `build/`: exited zero with 0 tests; recorded as
  a test-runner finding, not a green qualification gate.
- Acceptance-evidence deletion counterexample: finalization still succeeded;
  recorded as P0-4.

## Closure Rule

Close `T-003` only when work packages 1 through 4 are green and an independent
exact-subject Product review has no unresolved material finding. Product
acceptance and release are subsequent authority events; they must not be
backfilled from construction success.

Resume ABI work only against the immutable released consumer surface. Do not
copy the construction plan, selection ledger, ad hoc Quickstart prompt, or
candidate-directory state into ABI as a substitute for that Product boundary.
