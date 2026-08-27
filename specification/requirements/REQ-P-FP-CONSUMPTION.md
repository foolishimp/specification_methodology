# REQ-P-FP-CONSUMPTION — Probabilistic LLM Consumption

Family: `REQ-P-FP-*`
Status: Active
Category: Capability
Design ownership: common consumer boundary owned by WHAT; carrier loading is
owned independently by each build tenant or external host

Derives from: `../INTENT.md#consumer-relation`,
`../PRODUCT.md#program-boundary`,
`../PRODUCT.md#product-authority`

## Purpose

Define the intended consumer and use of an STDO Reasoning Program without
turning probabilistic LLM reasoning into deterministic assessment or runtime
truth.

## Requirements

**REQ-P-FP-001**: The primary Product consumer shall be an LLM operating in the
probabilistic `F_P` regime. The program shall be optimized to provide that
consumer with STDO graph structure and constraints at materially lower context
cost than the complete Source STDO documents.

**REQ-P-FP-002**: A reasoning invocation shall bind a Product identity,
separately acquired workspace input, reasoning intent, selected frame or frame
projection, and declared model capability/context budget before invocation.

**REQ-P-FP-003**: The complete reasoning program shall be reusable across
workspaces and invocations. A workspace path, snapshot, prompt, model, response,
or price shall not be embedded as program semantic truth or alter Product
identity.

**REQ-P-FP-004**: The LLM shall receive graph topology and applicable passive
constraints as governing context. The Product shall not prescribe a hidden
chain of thought, prompt tactic, business priority, solution sequence, or
deterministic semantic algorithm.

**REQ-P-FP-005**: The program shall preserve enough source identity, authority,
bounded-context, scope, basis, provenance, dependency, and refusal structure for
an `F_P` consumer to distinguish materially different lawful interpretations.

**REQ-P-FP-006**: A bounded projection may be consumed instead of the complete
program only when it declares its intent, frame, budget, included closure, and
exact routes to omitted Source STDO material. A consumer shall not treat a
projection as authority outside that boundary.

**REQ-P-FP-007**: When program declarations explicitly leave a decision
underdetermined, the `F_P` consumer may reason within that latitude and shall
retain the declared owner or re-entry route. An undeclared gap shall not be
treated as creative latitude.

**REQ-P-FP-008**: An LLM response is probabilistic output. It may contain
analysis, proposed actions, diagnoses, questions, refusals, or source-addressed
findings, but it shall not claim semantic, operation, acceptance, release,
runtime, or closure authority merely because it consumed the program.

**REQ-P-FP-009**: This Product shall not require HoG traversal, ABG runtime
admission, an event log, a deterministic evaluator, or a prescribed output
schema to consume the program. An external Product may add those relations under
its own explicit authority.

**REQ-P-FP-010**: A host unable to supply the selected program, workspace input,
intent, frame, or capability budget shall expose that missing input rather than
claim governed STDO reasoning occurred.
