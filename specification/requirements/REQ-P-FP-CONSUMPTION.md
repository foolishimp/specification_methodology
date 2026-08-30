# REQ-P-FP-CONSUMPTION — `a_c` Probabilistic Index Consumption

Family: `REQ-P-FP-*`
Status: Active
Category: Capability
Design ownership: common traversal boundary owned by WHAT; carrier loading and
invocation realization are owned by each build tenant or external host

Derives from: `../INTENT.md#consumer-relation`,
`../PRODUCT.md#fundamental-traversal-functor-binding`,
`../PRODUCT.md#programmatic-index-boundary`,
`../PRODUCT.md#product-authority`

## Purpose

Define both probabilistic LLM semantic compilation of Source STDO into a
candidate `a_c.STDO` model and direct LLM use of an admitted STDO Programmatic
Semantic Index under the generic `a_c` traversal calculus. The LLM is a
bounded probabilistic compiler or interpreter; it does not execute a GTL
`GtlProgram` or turn either result into deterministic assessment or runtime
truth.

## Exact functor-kind identities

The project imports these Source STDO meanings unchanged:

```text
F_D = urn:stdo:concept:axiomatic-calculus:f-d
F_P = urn:stdo:concept:axiomatic-calculus:f-p
F_H = urn:stdo:concept:axiomatic-calculus:f-h
```

`AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds` remains their semantic owner. The local
terms `F_D`, `F_P`, and `F_H` are qualified references to those identities, not
new concepts inferred from their spelling.

The consistent application notation is:

```text
F_K[v](upstream_v) -> result_v
```

`F_K` is one imported functor-kind identity, while `v` is one exact declared
traversal to which that functor kind is applied. Named domain
operations such as acquisition, encoding, serialization, or measurement are not
aliases for `F_D`, `F_P`, or `F_H`.

For this Product, the traversal-functor allocation is:

| Functor kind | Bounded role | Forbidden substitution |
|---|---|---|
| `F_D` | evaluation or proof of declared deterministic basis, identity, structural-admission, closure, and measurement properties | constructor mechanics, semantic selection, probabilistic judgment, human acceptance |
| `F_P` | one bounded LLM semantic-compilation traversal over exact prose, or one bounded LLM traversal over an admitted index and separately bound inputs | structural or closure truth, semantic authority, acceptance |
| `F_H` | review and selection of an exact compilation candidate, explicit ambiguity adjudication, and acceptance under an exact human or bounded-proxy grant | ambient authority, hidden worker strategy, deterministic proof |

## Semantic compilation relation

The current semantic compiler is a traversal classified by the `F_P` functor
kind:

```text
F_P[v_compile](S_B, b_ac, Sigma_STDO, I_STDO, I_C, R_C, K_C)
  -> Y_B* = (M_B*, P_B*, Sel_B*, U_B*) | hold | gap | refusal

ConstructCandidate(Y_B*, exact_raw_bytes, exact_invocation, exact_provenance)
  -> Q_B* | refusal
```

`S_B` is exact ordered Source STDO prose and bytes, `I_C` is compilation intent,
`R_C` is the selected compilation reference-frame set, `K_C` is the declared model
capability and context budget. `b_ac`, `Sigma_STDO`, and `I_STDO` are the exact
calculus basis, closed signature, and interpretation contract. `Y_B*` is the
proposal payload. Deterministic `ConstructCandidate` binds its unchanged
content to exact invocation and provenance coordinates as `Q_B*`, the immutable
Semantic Compilation Candidate defined by
`REQ-P-SELECTION-AND-ACCEPTANCE.md#semantic-compilation-candidate`; it contains
candidate model `M_B*`, record-provenance relation `P_B*`, candidate selection
rows `Sel_B*`, and compilation uncertainty `U_B*`; material model uncertainty
is retained in `M_B*.X`.

The compiler stops at the carrier-neutral proposal. After candidate
construction, exact structural evaluation, human selection, and external
accepted `J_B` over the unchanged interpreted model, a selected tenant profile
gives the representation a reliable typed, closed, canonical carrier form. A profile
constrains only the later encoder and carrier-admission boundary; it neither
constrains the semantic compiler nor proves that semantic extraction is
correct.

```text
D_Q = F_D[v_candidate_structure](Q_B*, b_ac, Sigma_STDO, I_STDO)
F_H[v_select](Q_B*, S_B, D_Q) -> Ledger_B | rework | reject
F_H[v_accept_interpretation](id(a_c.STDO*), model_content_identity)
  -> J_B | reject
```

## External traversal contract

The compact consumer notation is:

```text
F_P[v_reason](Index_B, W, I, R, K) -> J_reason | hold | gap | refusal
```

It projects this complete external traversal contract:

```text
traversal ref       = one host-owned declared traversal
upstream assets     = immutable Index_B=(M_B,P_B) + acquired W + declared I + selected R + K
target              = explicit J_reason output contract
required context    = basis, authority, source routes, projection boundary
role/capability     = exact F_P identity + declared model capability envelope
evaluators/gates    = host-declared checks that cannot grant semantic authority
provenance          = Product, workspace, intent, frame, model, prompt and time
stop states         = hold | gap | refusal | continuation | completion
```

The consuming host owns this invocation contract and any execution realization.
The immutable semantic index supplies the complete model and total per-record
Source STDO provenance relation; it neither
executes the traversal nor admits its output.

## Requirements

**REQ-P-FP-001**: The primary Product consumer shall be an LLM bound to exact
`a_c` concept `urn:stdo:concept:axiomatic-calculus:f-p`. The programmatic
semantic index shall be optimized to provide that consumer with STDO graph
structure and constraints at materially lower context cost than the complete
Source STDO documents.

**REQ-P-FP-002**: Every invocation claimed as `F_P` shall bind one complete
external traversal contract containing one declared traversal
identity, upstream assets, target/output contract, required context, exact
functor-kind identity, capability envelope, evaluators and gates, provenance
obligations, and lawful stop states. Bare model invocation is probabilistic
processing but is not a claimed `a_c` `F_P` traversal.

**REQ-P-FP-003**: A reasoning invocation shall bind a Product identity,
separately acquired workspace input, reasoning intent, selected frame or frame
projection, and declared model capability/context budget before invocation.
An Executive-, Worker-, or Reviewer-targeted invocation shall additionally bind
the exact Executive Context Assignment and Context Projection Manifest required
by `REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`.

**REQ-P-FP-004**: The complete semantic index shall be reusable across
workspaces and invocations. A workspace path, snapshot, prompt, model, response,
or price shall not be embedded as index semantic truth or alter Product
identity.

**REQ-P-FP-005**: The LLM shall receive exact index topology and applicable
passive constraints as governing context. The Product shall not prescribe a
hidden chain of thought, prompt tactic, business priority, solution sequence,
or deterministic semantic algorithm.

**REQ-P-FP-006**: The index shall preserve enough source identity, authority,
bounded-context, scope, basis, provenance, dependency, and refusal structure for
an `F_P` consumer to distinguish materially different lawful interpretations.

**REQ-P-FP-007**: A bounded projection may be consumed instead of the complete
index only when it declares its intent, frame, budget, included closure, and
exact routes to omitted Source STDO material. A consumer shall not treat a
projection as authority outside that boundary. Role-bound projection shall use
the exact least-closure and assignment contract of
`REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md`.

**REQ-P-FP-008**: When index declarations explicitly leave a decision
underdetermined, the `F_P` consumer may reason within that latitude and shall
retain the declared owner or re-entry route. An undeclared gap shall not be
treated as creative latitude.

**REQ-P-FP-009**: An LLM response is probabilistic output. It may contain
analysis, proposed actions, diagnoses, questions, holds, gaps, refusals, or
source-addressed findings, but it shall not claim semantic, operation,
acceptance, release, runtime, or closure authority merely because it consumed
the index.

**REQ-P-FP-010**: The Programmatic Semantic Index Product shall not embed or own
HoG execution, ABG runtime admission, an event log, a deterministic evaluator,
or a runtime continuation surface. An external consuming Product may bind those
roles under its own authority; their absence from the payload does not remove
the required `a_c` traversal contract. A consuming ODD Product may separately
specialize that traversal under its own authority; this Product imports no ODD
functor identity.

**REQ-P-FP-011**: An `F_D`-classified traversal may admit exact index properties
but shall not replace `F_P` judgment. An `F_H`-classified traversal may select
or accept an exact subject under a declared grant but shall not claim that human presence deterministically
proves semantic completeness. Every durable `F_D` receipt or `F_H` decision
claim shall bind its own declared traversal identity and complete applicable
contract.

Deterministic domain acquisition, construction, canonicalization,
serialization, digesting, and measurement remain mechanics whose declared
properties may be evaluated by an `F_D[v]` traversal; they do not become `F_D`
merely because they are deterministic.

**REQ-P-FP-012**: A host unable to supply the selected index, workspace input,
intent, frame, capability budget, or complete traversal contract shall expose
the missing coordinate and refuse the `F_P` claim.

**REQ-P-FP-013**: Semantic compilation shall be claimed as `F_P` only when its
complete traversal contract binds the exact `a_c` basis, Source STDO subject
basis, `Sigma_STDO`, `I_STDO`, compilation
intent, selected frames, compiler capability envelope, carrier-neutral common
algebra contract, immutable `SemanticCompilationProposal` output contract,
deterministic unchanged-payload candidate construction contract, provenance,
and stop states. A tenant profile shall not be an input. Bare or
source-unbound extraction shall not enter semantic selection.

**REQ-P-FP-014**: An `F_P[v_compile]` semantic-compilation result is a proposal.
It shall retain total `P_B`, source routes, and residual uncertainty and shall
not claim semantic selection, acceptance, completeness, structural admission,
or Product authority. `F_H[v_select]` shall review the exact candidate against
its exact sources; external `J_B` shall then accept the unchanged
interpreted-model identity and model-content digest before carrier construction
is authorized.

**REQ-P-FP-015**: GTL reliability shall mean conformance to the exact selected
typed declaration, raw-admission, closed-reference, canonicalization, and
validation laws. `F_D[v_carrier_admission]` may evaluate those declared
properties after encoding and shall return a separate admission judgment bound
to the unchanged carrier identity and digest. It shall not return, transform,
rewrite, reissue, or rename the carrier. Neither GTL admission nor `F_D`
success shall be represented as proof that the `F_P[v_compile]` semantic
compilation is uniquely correct.
