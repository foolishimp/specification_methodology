# STRATEGY: Draft STDO 3.0.1 change proposal

**Author**: Codex
**Date**: 2026-10-24T07:07:35Z
**Updated**: 2026-10-24T10:08:50Z
**Addresses**: Shared deterministic regime; continuation-sensitive observations; qualified references; preservation claims; comparison guidance; compatibility and release preparation
**Status**: Draft
**Target release**: 3.0.1

## Summary

Propose one substantive semantic amendment and five supporting clarification, example and migration items for STDO 3.0.1. The substantive amendment gives `F_D` one total deterministic closed-processing meaning, while evaluation purpose, judged subject, writes and admission remain explicit operation contracts. The remaining items make existing preservation and evidence obligations easier to apply and test.

The [ABIogenesis worked case](../../../../../../abiogenesis/.ai-workspace/comments/codex/20261024T045334Z_STRATEGY_gtl_abg_stdo3_formal_model.md) motivates the proposal: one candidate identity can conceal different assessment and continuation states, but its existing qualified views/references preserve the required distinctions. It establishes neither a need for new annotation architecture nor emergence. The generic lesson concerns consumer-required information, operation contracts and evidence.

This draft changes no standard, work selection, version, channel or consumer basis. Quoted clauses below are proposed ratification text. Construction, qualification, release and adoption remain separate decisions.

## Analysis

### Basis and change boundary

Source-project basis: `9092a2f8eaa885d5ab6e8099a317186aa887b1a4`, scoped to `specification_methodology/v3`. The [Definition](../../../stdo_3.json) retains governing builder `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. Its [Product](../../../specification/PRODUCT.md#product-boundary), [Goals](../../../specification/GOALS.md#current-selection) and [frame basis](../../../specification/REFERENCE_FRAME_BASIS.md#activations-and-owners) retain C3-I5-06 ratification and the T-003 standalone common-candidate selection. The builder's [posting](stdo://releases/v2.5.1-rc.2/standards/POSTING_GUIDE.md#boundary) and [writing](stdo://releases/v2.5.1-rc.2/standards/WRITING_GUIDE.md#core-rule) guides govern this carrier.

The clause analysis uses the exact installed `v3.0.0-rc.1` corpus, manifest `069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232`. A published final 3.0.0 predecessor identity has not been established in this session. Before construction/qualification, bind the exact predecessor and rebase this section map against it. That unresolved identity does not prevent reviewing these draft amendments. The analysis corpus is not substituted for the selected builder.

### Owning clauses and before/after meaning

| Item | Exact analysis-baseline owner | Before → proposed meaning; classification |
|---|---|---|
| P301-01 | [AXIOMATIC_CALCULUS §5 / AC-015](stdo://releases/v3.0.0-rc.1/standards/AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds) | Evaluation/proof-only `F_D` → shared deterministic regime admitting construction while strengthening totality/dependency obligations; operation contracts retain authority and restrictions. **Substantive semantic change**, including the ODD binding below. |
| P301-02 | [FOUNDATIONS §4, Observation sufficiency](stdo://releases/v3.0.0-rc.1/standards/FOUNDATIONS.md#4-algebra) | Static deciding-observation criterion → explicit continuation-sensitive application. **Derived clarification.** |
| P301-03 | [ACTIVATION §2](stdo://releases/v3.0.0-rc.1/standards/ACTIVATION.md#2-context-construction-under-an-envelope) | Existing context/reference obligations → qualified-reference examples and discriminator. **Guidance**, consuming AC-003/AC-011. |
| P301-04 | [FOUNDATIONS §4, Formal fragment](stdo://releases/v3.0.0-rc.1/standards/FOUNDATIONS.md#4-algebra) | Category/map demonstration → explicit distinction between functor laws and claimed consumer adequacy. **Clarification plus worked guidance.** |
| P301-05 | [EVALUATION §6, Comparison](stdo://releases/v3.0.0-rc.1/standards/EVALUATION.md#6-conformance-of-realisations) | Existing scoped comparison → optional information-equivalent experimental design. **Guidance.** |
| P301-06 | [CONFORMANCE §5](stdo://releases/v3.0.0-rc.1/standards/CONFORMANCE.md#5-discriminator-coverage), [RELEASE §9](stdo://releases/v3.0.0-rc.1/standards/RELEASE.md#9-successor-baseline-conservation-stdo-up-015) | Existing coverage/conservation → affected examples, disposition map and migration evidence. **Conformance/example and derived-asset updates.** |

Each definition has one owner. Consumers cross-reference that owner; examples and release records acquire no parallel law. Clarification/guidance classifications hold only while they add no mandatory field, evidence condition, refusal or profile-selection rule. Any such addition is an explicit normative delta requiring its own ratification.

### P301-01: a common deterministic kind

Replace the `F_D` definition in §5 with:

> `F_D` classifies total deterministic processing under an exact traversal contract. An application declares `f_B:D_B->Outcome_B`, its closed logical domain, exact basis, all material computational state/dependencies, and its termination argument. For every domain input it terminates with exactly one declared outcome. Closed domains may be infinite when termination and outcome determination are established. Open-world semantic choice and undeclared clock, filesystem or global dependencies are outside this contract.
>
> State-dependent processing declares input state and the meaning of its returned next state/value. Refusal and exhaustion retain their cause and evaluated predicate. The signature and traversal bind each stop to exactly one core value, never satisfied; an exhausted tag alone supplies no mapping. Construction availability and assessment retain their separate predicates and results, and an unperformed assessment has no result. A fuel-bounded operation is distinct from the potentially divergent operation it bounds. A deterministic decision or effect proposal does not establish physical completion, runtime admission, permission or quality.

Add an evaluation-operation contract in the same owning section:

> An operation declared to evaluate an unchanged subject identifies that subject, admissible reads, witness/log outputs, permitted writes, stops/results, authority and invalidation conditions. It preserves the judged subject and does not perform the domain construction it judges. Separately authorized persistence of a witness does not perform the judged domain construction. A construction or mutation needs its own operation contract and grant; reporting a changed subject's property as the original subject's property violates the evaluation contract.

Closedness concerns dependencies material to the computation, not complete world knowledge. AC-015 continues to require one kind and exact traversal identity per application. AC-016 retains separate traversal identities, intermediate results, judgments and stops when a constructor feeds an evaluator. `F_P`, `F_H`, their authority boundaries and the five core results remain unchanged. Unbounded work is not automatically relabeled `F_P` to escape a missing totality argument.

The ODD migration is part of this amendment. [ODD §5](stdo://releases/v3.0.0-rc.1/standards/ODD.md#probabilistic-compute) replaces its separately defined `F_D` shorthand with an exact-edition import of the common kind. Existing evaluation/proof operations retain their evaluation profiles; admission operations retain their own grants and evidence contracts. Their use of the common kind is conditional on P301-06's eligibility assessment. Replace [ODD §11.5D, A5](stdo://releases/v3.0.0-rc.1/standards/ODD.md#115d-constructive-evaluation-and-yield-loop), preserving A4a's separation of functions and A6/A8's evidence and closure duties:

> A5 Bounded construction and declared authority. F_P may inspect, discover, reason, draft, transform and propose within the bounded action. F_P must not close the edge, emit runtime events, mutate ledgers or decide re-entry. Durable evidence and closure truth are established by the declared evaluation, ABG and Product admission/closure operations under their respective contracts and grants. Each operation names its authority, admissible evidence and permitted consequences; its use of the common F_D regime requires the total deterministic contract. F_D classification grants no assessment, runtime admission, ledger-writing or closure authority. An F_P worker must not be given an F_D-authored semantic extraction recipe when the edge requires F_P judgment.

Negative authority discriminator: the finite constructor below returns `{n:2,double:4}` under a construction-only grant. Its candidate is available, but presenting that value or its `F_D` classification as an assessment, admission or closure must establish none of those claims. The corresponding owner operations, evidence and grants are still required.

The initial operation discriminators are:

| Case | Required result |
|---|---|
| Constructor `n∈{0,1,2}` | Exactly `{n:0,double:0}`, `{n:1,double:2}`, `{n:2,double:4}`. A total domain construction qualifies under the proposed kind. |
| Sortedness on lists of length at most three over `{0,1,2}` | `[2,1]` yields falsified with `{index:0,left:2,right:1}`; original unchanged. A separately granted witness log is compatible. |
| Logical `put_A`, state `absent/A/B`, grant `allow/deny` | Allow maps each state to modeled A plus `put_A` request; deny preserves each state plus refusal. These six cells establish only the closed core. Physical failure/uncertainty stays with the effect owner. |
| In-place sort followed by “original passed” | Sorting `[2,1]` to `[1,2]` can be deterministic, but fails the evaluate-original/read-only contract. It needs a construction grant and successor-subject attribution. |

The complete logical store oracle is:

| Input state | Allow → modeled next state / decision | Deny → preserved state / outcome |
|---|---|---|
| absent | A / request put_A | absent / refusal |
| A | A / request put_A | A / refusal |
| B | A / request put_A | B / refusal |

Exhaustion discriminator. Fix two finite traversals: `v_copy` copies one element per fuel unit from lists of length at most two over `{0,1}`; only a complete copy is its candidate. `v_sorted` inspects one adjacent pair per fuel unit on lists of length at most three over `{0,1}`. It returns falsified on an observed inversion, satisfied when all pairs have been checked, and a closed indeterminate assessment when the inspected pairs cannot decide the whole-list predicate. Fuel is an input in `{0,1,2}`. Both algorithms terminate within their declared bounds. The assessing step's declared output is the closed assessment report with its exact basis, inspected-pair evidence and residual, including an indeterminate report.

| Selected application and domain outcome | Evaluated predicate and result | Applicable work result | a_c stop binding |
|---|---|---|---|
| `v_copy([0,1],1)` exhausts after prefix `[0]`; the complete candidate is absent | A complete copy is available: falsified | `incomplete` → falsified for candidate availability | The example signature declares `copy_exhausted`, parent core value falsified, cause fuel ended before the required output. The traversal binds that stop and predicate. |
| `v_sorted([0,1,0],1)` inspects `(0,1)` and exhausts with the second pair unexamined | The complete list is sorted: indeterminate on the admitted inspected-pair evidence | The closed assessment report and transition evidence are available: `candidate_ready` → satisfied for report availability only | The signature separately declares `assessment_exhausted`, parent core value indeterminate, cause performed assessment has insufficient evidence. The traversal binds that stop and predicate. |
| A lawfully activated assessing step spends its budget in setup before invoking `v_sorted`; no assessment report exists | Sortedness assessment not performed: no assessment result | `incomplete` → falsified for the assessing step's output availability; the planned assessment remains a residual | No `v_sorted` application occurred, so it has neither a result nor a stop. The enclosing step retains its own stop. |

These are distinct signature stop values refining the named core values under [a_c §5](stdo://releases/v3.0.0-rc.1/standards/AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), with no change to the meanings or parent mappings of `hold`, `gap` or `refusal`. [ACTIVATION §3](stdo://releases/v3.0.0-rc.1/standards/ACTIVATION.md#construction-availability) owns the work-result mappings; [FOUNDATIONS Results](stdo://releases/v3.0.0-rc.1/standards/FOUNDATIONS.md#results) owns assessment standing and non-performance. Producing the exhaustion report establishes neither the missing copy nor sortedness. A retained counterexample would keep its falsified assessment even if other work later exhausted its budget.

Before implementation inventory every use: a_c §5/AC-015; TRAVERSAL_OCCURRENCE's `b_ac`/FunctorKind binding; the specified ODD §5/§11.5D migration and §11.7 consumers; PROFILES §1; DESIGN_MODULE; GLOSSARY; README and affected frame examples. Review SPEC_METHOD §11 and EVALUATION's operation/outcome consumers even where `F_D` is absent literally. Check cross-member derivation tables and CONFORMANCE §5 discriminators 22 (domain/preconditions) and 51 (categorical claims when asserted). One canonical definition replaces duplicate global meanings; existing evaluation guarantees survive as enforceable operation profiles. No silent alias certifies current uses.

### P301-02: continuation-sensitive sufficiency

Add under FOUNDATIONS §4 Observation sufficiency:

> Where a representation is claimed sufficient for subsequent decisions, identify the consumer-required observations/readouts and material applicability conditions, directly or by reference to the consuming contract. Identify input/policy scope and horizon where the claim depends on them. Retain the standing, obligations, currentness/invalidation, causal producer and authority distinctions those consumers require. If two cases have the same representation but require incompatible decisions under those fixed conditions, the sufficiency claim is falsified. This requires no anticipation of all future uses.
>
> When a chosen functional formal account claims decision preservation, define its functions and domain and demonstrate the claimed factorization `delta=delta_hat o alpha`. When that account claims transition preservation, also demonstrate `alpha(T(s,u))≈T_hat(alpha(s),u)` and the declared readout preservation on that domain/horizon. Other frames preserve their consumer-required relational distinctions under the owning contracts; these equations impose no universal functional model or executable decision procedure. Mandatory authority and hold distinctions remain exact where their contracts require exactness. Approximation needs explicit latitude and a justified horizon bound; a one-step bound alone supplies no multi-step guarantee.

AC-011 projection, AC-016 composition and [ACTIVATION §7 reuse](stdo://releases/v3.0.0-rc.1/standards/ACTIVATION.md#7-closed-result-and-reuse) reference this owner. Reuse preserves applicable unaffected facts; role changes alone require no full-history scan. Projection establishes no Markov or categorical-functor property.

Oracle, under a declared one-assessment protocol: unassessed `U` and indeterminate `I` both answer false to “satisfied assessment exists.” A first valid assessment is permitted from U and refused as already assessed from I. Retaining null versus disposition repairs this query/transition distinction. In a human handover, an unevaluated application and an application with a closed undecidable assessment require different next work under the declared policy, even if both lack approval. A fresh assessment or follow-up remains lawful where its own contract/re-entry permits it. No event log or code is required for that distinction.

The repaired four-state abstraction is a sufficiency witness for that fixed protocol: it preserves every modeled state distinction and demonstrates no state aggregation. This example establishes neither optimal compression nor general context selection. A claim of smallest or cheapest sufficient material, or selection across new tasks, needs its own objective, scope and evidence; representation size and total operating cost are distinct quantities.

### P301-03: qualified references

Add guidance in ACTIVATION §2, referencing existing closure/projection law:

> A reference can supply sufficient context when its accessible target and qualifications preserve the consuming contract. Check the required subject/basis, assessment standing, provenance, active obligation/version and invalidators, rather than candidate identity alone. A typed annotation is not evidence of sufficiency by itself. Preserve the required body or a qualified resolvable reference; select no mandatory carrier or registry.

Positive case: share a complete assessed record through an exact local reference qualified by its material identity and applicable provenance. Resolution preserves the required record. Negative case: candidate bytes/digest remain constant while satisfied and indeterminate assessment differ; a candidate-only pointer merges incompatible continuations. Hash-based matching states its collision/access assumptions. Unknown semantic relations return the owning gap or result, not one blanket error classification. Declared but unperformed evaluation has no assessment result; an undeclared required capability is a different condition.

### P301-04: formal claim versus useful preservation

Add to FOUNDATIONS §4 Formal fragment:

> A claim of semantic preservation or adequacy names the consumer observations and required distinctions and demonstrates their preservation. Category/functor laws establish their stated structural claim; they do not alone establish that the chosen interpretation or projection is sufficient for the intended use. A background lemma is applied only after its source/target objects, arrows, equality and actual maps are bound to the subject.

EVALUATION §6 consumes this rule by reference. Keep H1 unresolved; the example below does not discharge it or replace existing a_c representation requirements for categorical claims.

Worked neutral example: fix one review subject, a policy allowing advance only on S, and admissible reports `X={S,F,I}`. Let `H={hS,hF,hI}` be qualified records and `V={vS,vF,vI}` retain their subject, basis and standing. Policy readouts are `D={advance,block_falsified,block_indeterminate}`. Define `build:X->H`, `view:H->V`, `j:H->D` and `h:V->D` by this complete table:

| Report | `build` | `view` | Both `j` and `h` read out |
|---|---|---|---|
| S | hS | vS | advance |
| F | hF | vF | block_falsified |
| I | hI | vI | block_indeterminate |

Pointwise the three rows establish `j=h o view`; arrow equality is pointwise function equality, with ordinary finite-function identities/composition. The constant subject-only projection cannot factor j because S and I share its value but require different readouts. A functor to a terminal category can satisfy functor laws while losing that distinction. This supports a finite example, not a requirement that every consumer use FinSet or ABG topology.

### P301-05: comparisons that decide the right question

Add optional guidance under EVALUATION §6 Comparison:

> When evaluating a representation benefit, compare equivalent substantive information and access. Independently vary relevant counterexamples retained, absent, or stale/out of scope where material. Include the existing contract and simplest adequate qualified plain-text fix. State outcome oracles, units and boundaries for acquisition, rendering, reasoning, repair and assurance cost. Scale trials to the claim, risk and resources; prescribe no universal count or new review cycle.

Representation benefit under information equivalence can support an architecture decision. Retention benefit supports context-selection policy. Stale-material failure targets provenance/invalidation. No benefit or higher total cost supports retaining the existing construction. Required outcome correctness and unresolved obligations remain visible. Harness-style Propose–Probe–Compose is one possible experiment strategy, not a dependency or acceptance oracle.

### P301-06: compatibility and affected evidence

Add the preceding positive/negative cases to CONFORMANCE §5's existing coverage relation, with applicability and their source obligations. Include the ODD constructor-without-authority case and all three exhaustion cases, preserving their different predicates and result mappings. Include human, mixed and code bindings: a manual handover preserves U/I and witness-write limits just as a software binding must. An existing 3.0.0 evaluation operation must retain its unchanged-subject guarantee after migration; every operation claiming the new `F_D` kind must establish the new total-domain contract. Hidden material dependencies or missing termination evidence leave that qualification unestablished; broader write, admission or closure authority violates the preserved operation contract. Examples in the release carry their own contracts and oracles; the ABI paper is supporting provenance, not a required checkout.

The requested 3.0.1 target requires a documented version-policy/compatibility assessment. [RELEASE §10](stdo://releases/v3.0.0-rc.1/standards/RELEASE.md#10-open-questions) leaves the general version-line rule open. P301-01 extends operation purposes and strengthens totality, dependency and evidence obligations; it is not solely semantic widening or automatically patch-compatible. The old kind-level evaluation/proof definition supplies no general termination argument. [ACTIVATION §4](stdo://releases/v3.0.0-rc.1/standards/ACTIVATION.md#4-totality-and-refinement) also distinguishes total handling from an invoked provider's termination. Preserve existing evaluation guarantees through explicit profiles and assess each proposed import:

| Existing operation's evidence | Successor disposition |
|---|---|
| Establishes the new totality, closed-dependency and outcome contract | Map to common `F_D` plus the unchanged-subject/read/write/result/authority profile and exact traversal binding. Preserve the operation's evidence and grants. |
| Needs additional evidence or an explicitly changed bounded implementation | Keep new-kind qualification pending until the missing obligations are established. A narrower domain or fuel-bounded implementation has its own contract, identity, exhaustion outcomes and affected preservation evidence; it does not retroactively prove the old operation total or preserve every old continuation. |
| Successor classification remains unresolved | Retain the exact legacy meaning/evidence and an explicit successor obligation until its owner disposes it. Grant neither new `F_D` standing nor an automatic `F_P` label. An affected successor claim remains open. |

Negative migration discriminator: an old deterministic evaluator with unestablished termination or an undeclared material dependency does not qualify merely by adding the unchanged-subject profile. Its evidence must select the second or third row. The version assessment accounts for these cases and for the ODD authority and exhaustion mappings above.

Immutable 3.0.0 consumers keep their selected meaning. New consumers explicitly select the complete successor and its operation profiles. A stable concept URN is distinct from its [immutable calculus edition](stdo://releases/v3.0.0-rc.1/standards/AXIOMATIC_CALCULUS.md#8-calculus-identity). Record the old release, manifest, member and clauses. Only an established mapping above licenses migration; current URN lookup never reinterprets history. Versioned imports/aliases record justified supersession and grant no broader permission. Preserve historical claims and disposition affected predecessor obligations under RELEASE §9.

### Ownership, re-entry and bounded release sequence

STDO owns generic definitions and examples; common v3 WHAT owns any amended obligations; accepted tenant HOW realizes them. ABI/GTL adoption remains with that consumer's Product and tenant. Harness algorithms and application runtimes stay outside STDO law. The Definition's declared Axiom Indexer dependency remains intact. Additional Graphify/tools enter only through explicit selection; no cohort follows from the existing dependency.

Future intake uses the governing builder's change classes. P301-01 needs `requirement_reprice`, with earlier `product_reprice` where Product truth must change; stable direction alone does not justify editing below those owners. P301-02–05 can use `design_reframe` only after confirming they clarify existing WHAT; any changed obligation returns through `requirement_reprice`. Pure coherence regeneration can use `realization_refactor` when it changes no upstream meaning. No source mutation follows from this draft.

| Phase | Readiness condition and deciding evidence |
|---|---|
| Bind predecessor/delta | Exact immutable 3.0.0 origin, selected profile/cohort and clause/consumer inventory; rebase the RC1 map and dispose affected claims. |
| Ratify minimal amendments | Owner decisions on the common F_D contract, operation profiles and compatibility, with precise WHAT/HOW re-entry. |
| Construct one common candidate | Use the accepted v3 workflow, preserving unrelated work and scope; carry required a_c representations and imports consistently. |
| Assess affected relations | Focused independent semantic review; the listed positive/negative and human/mixed/code discriminators meet their independently stated oracles. |
| Regenerate included assets | Included derived frames, interpretations or plugins match exact sources; source/derived coherence and publication closure hold. |
| Qualify and decide | Exact installed qualification under the selected profile, preserved functional scope and owner release acceptance for 3.0.1. |
| Publish/adopt | Publish one immutable cut through RELEASE owners; consumer adoption follows explicitly afterward. |

Use the selected 3.0.1 profile/cohort, not an assumed v2 five-asset cohort or sibling Graphify dependency. Proposal ratification, installed qualification, publication and consumer adoption remain distinct.

### Source pins and open decisions

| Input | Exact pin |
|---|---|
| Source Definition | SHA256 `b38a8fde935b6403704fc51fe7518887b738a1fb510a6e84a6faf3de538a0aad` at the Git basis above |
| Analysis AXIOMATIC_CALCULUS | `2b24d3679cac3dd7a383c9ef382232acc8e99055709dc1a330e6f18a7b4cebbf` |
| Analysis FOUNDATIONS | `3e85b8d01360dfae6758566fd3aca309c977e7d9e15cdd2f9e8f2904f18f2545` |
| Analysis EVALUATION | `4c87b1286d9c721b6e050b64adb8f6804327c0d8e3dad67f7c3973cbef389fd6` |
| Analysis ODD | `1f6afec9017d115ce1ad4cef1397a5504b6e7710ebd7dc74d66a6cdedcf6344f` |
| Analysis ACTIVATION | `7ad7b69b5ad8ec20678b3ef866a26fb328f2fa6f60c4d1d06ca0b926845b89bf` |
| Analysis CONFORMANCE | `7db0c1f67160ca5e96aa7e39dbdb79cacf1b41b58c93cf84600670f6ad6a88c0` |
| Source Product | `4d6a43c25c58e76ea1283b1e2cacae5d40e3fba939681f188d99378bfadcc1d5` |
| Analysis RELEASE | `53f465d4d25b097c7da0df0e1f18805d273b032f6fe849b59a457b29b1349992` |
| ABI motivating paper | `b8cdec093950d4c36b9397d71d8fcd7b3b9ac24b6bc8407cbc7981ad74482cb7` |

Owner decisions remain: exact predecessor and clause rebase; shared-kind/profile ratification; version-policy compatibility; included release profile/assets; and whether/when to select construction. No schedule or release execution is inferred.

## Recommended Action

Review these six items as a bounded 3.0.1 proposal, deciding P301-01's semantic contract first. Retain supporting clarifications only where they improve an actual consumer or discriminator without duplicating ownership. Once the owner selects work and binds the predecessor/profile, prepare the smallest coherent common amendment and its affected evidence through the existing v3 workflow. Keep current Goals, builder selection, sibling projects and immutable releases unchanged during proposal review.
