# REQ-P-FP-CONSUMPTION — ODD Probabilistic LLM Traversal

Family: `REQ-P-FP-*`
Status: Active
Category: Capability
Design ownership: common traversal boundary owned by WHAT; carrier loading and
invocation realization are owned by each build tenant or external host

Derives from: `../INTENT.md#consumer-relation`,
`../PRODUCT.md#fundamental-traversal-function-binding`,
`../PRODUCT.md#program-boundary`,
`../PRODUCT.md#product-authority`

## Purpose

Define direct LLM use of an STDO Reasoning Program as the probabilistic function
of Source STDO's fundamental ODD traversal architecture without turning that
reasoning into deterministic assessment or runtime truth.

## Exact function identities

The project imports these Source STDO meanings unchanged:

```text
F_D = urn:stdo:concept:graph-native-odd:f-d
F_P = urn:stdo:concept:graph-native-odd:f-p
F_H = urn:stdo:concept:graph-native-odd:f-h
```

`ODD_METHOD.md#probabilistic-compute` remains their semantic owner. The local
terms `F_D`, `F_P`, and `F_H` are qualified references to those identities, not
new concepts inferred from their spelling.

For this Product, the traversal-function allocation is:

| Function | Bounded role | Forbidden substitution |
|---|---|---|
| `F_D` | exact acquisition, construction, canonicalization, structural validation, digesting, and measurement | semantic selection, probabilistic judgment, human acceptance |
| `F_P` | one bounded LLM traversal over a reasoning program and its separately bound invocation inputs | structural or closure truth, semantic authority, acceptance |
| `F_H` | semantic selection, explicit ambiguity adjudication, and acceptance under an exact human or bounded-proxy grant | ambient authority, hidden worker strategy, deterministic proof |

## External traversal contract

The compact consumer notation is:

```text
F_P(P_B, W, I, F, K) -> J | hold | gap | refusal
```

It projects this complete external ODD traversal contract:

```text
traversal ref       = one host-owned declared ODD vector or edge traversal
upstream assets     = immutable P_B + acquired W + declared I + selected F + K
target              = explicit J output contract
required context    = basis, authority, source routes, projection boundary
role/capability     = exact F_P identity + declared model capability envelope
evaluators/gates    = host-declared checks that cannot grant semantic authority
provenance          = Product, workspace, intent, frame, model, prompt and time
stop states         = hold | gap | refusal | continuation | completion
```

The consuming host owns this invocation contract and any execution realization.
The immutable reasoning program supplies graph and constraint input; it neither
executes the traversal nor admits its output.

## Requirements

**REQ-P-FP-001**: The primary Product consumer shall be an LLM bound to exact
Source STDO concept `urn:stdo:concept:graph-native-odd:f-p`. The program shall be
optimized to provide that consumer with STDO graph structure and constraints at
materially lower context cost than the complete Source STDO documents.

**REQ-P-FP-002**: Every invocation claimed as `F_P` shall bind one complete
external traversal contract containing one declared ODD vector or edge-traversal
identity, upstream assets, target/output contract, required context, exact
function identity, capability envelope, evaluators and gates, provenance
obligations, and lawful stop states. Bare model invocation is probabilistic
processing but is not a claimed ODD `F_P` traversal.

**REQ-P-FP-003**: A reasoning invocation shall bind a Product identity,
separately acquired workspace input, reasoning intent, selected frame or frame
projection, and declared model capability/context budget before invocation.

**REQ-P-FP-004**: The complete reasoning program shall be reusable across
workspaces and invocations. A workspace path, snapshot, prompt, model, response,
or price shall not be embedded as program semantic truth or alter Product
identity.

**REQ-P-FP-005**: The LLM shall receive graph topology and applicable passive
constraints as governing context. The Product shall not prescribe a hidden
chain of thought, prompt tactic, business priority, solution sequence, or
deterministic semantic algorithm.

**REQ-P-FP-006**: The program shall preserve enough source identity, authority,
bounded-context, scope, basis, provenance, dependency, and refusal structure for
an `F_P` consumer to distinguish materially different lawful interpretations.

**REQ-P-FP-007**: A bounded projection may be consumed instead of the complete
program only when it declares its intent, frame, budget, included closure, and
exact routes to omitted Source STDO material. A consumer shall not treat a
projection as authority outside that boundary.

**REQ-P-FP-008**: When program declarations explicitly leave a decision
underdetermined, the `F_P` consumer may reason within that latitude and shall
retain the declared owner or re-entry route. An undeclared gap shall not be
treated as creative latitude.

**REQ-P-FP-009**: An LLM response is probabilistic output. It may contain
analysis, proposed actions, diagnoses, questions, holds, gaps, refusals, or
source-addressed findings, but it shall not claim semantic, operation,
acceptance, release, runtime, or closure authority merely because it consumed
the program.

**REQ-P-FP-010**: The reasoning-program Product shall not embed or own HoG
execution, ABG runtime admission, an event log, a deterministic evaluator, or a
runtime continuation surface. An external consuming Product may bind those
roles under its own authority; their absence from the payload does not remove
the required ODD traversal contract.

**REQ-P-FP-011**: `F_D` structural checks may admit exact program properties but
shall not replace `F_P` judgment. `F_H` may select or accept an exact subject
under a declared grant but shall not claim that human presence deterministically
proves semantic completeness. Every durable `F_D` receipt or `F_H` decision
claim shall bind its own declared traversal identity and complete applicable
contract.

**REQ-P-FP-012**: A host unable to supply the selected program, workspace input,
intent, frame, capability budget, or complete traversal contract shall expose
the missing coordinate and refuse the `F_P` claim.
