# REQ-P-NATIVE-FRAME-USE — LLM-Selected Context

Family: `REQ-P-NATIVE-*`
Status: Active
Category: Capability / Constraint

Derives from: `../INTENT.md#native-agent-use`,
`../PRODUCT.md#native-frame-use-relation`, and exact Source STDO
`STDO_REFERENCE_FRAME_BASELINE.md`

## Purpose

Let Codex and Claude use the STDO logical constraint index natively while keeping semantic
selection in the LLM and deterministic code limited to the released Axiom
Indexer joiner.

## Role bindings

Executive, Worker, and Reviewer meanings come from exact Source STDO
`STDO_REFERENCE_FRAME_BASELINE.md`. Equal labels do not collapse their task,
evidence, mutation, independence, stop, or return relations.

## Native surface

```text
skills/stdo-representation/
  SKILL.md
  agents/openai.yaml
  references/codex.md
  references/claude.md
```

Codex and Claude discover that same canonical skill through relative repository
symlinks. The target references stay concise and contain only material native
instruction differences.

## Frame-use relation

```text
LLMSelect(index_over_compression, task, role, evidence_boundary)
  -> selected frames + ordered labeled sections | hold

AxiomJoin(ordered labeled sections)
  -> exact request bytes | refusal
```

For every selected frame, the LLM exposes its URI, task-specific purpose, and
Source STDO route. Selection remains visible and reviewable. The joiner performs
no semantic work.

## Requirements

**REQ-P-NATIVE-001**: The canonical skill shall tell the agent to verify the
exact compression, index binding, and dependency; load the index before broad
source prose; and re-enter exact Source STDO when a task, residual,
disagreement, or unresolved route requires it.

**REQ-P-NATIVE-002**: The LLM shall select frames explicitly. No similarity,
retrieval rank, graph distance, validator, fixed-point closure, or hidden model
instruction shall be presented as the uniquely correct selection.

**REQ-P-NATIVE-003**: Each joined request shall visibly include selected frame
URIs, purposes, and source routes plus the bounded task, role, authority and
effect boundary, evidence, material constraints, stops, and return relation.

**REQ-P-NATIVE-004**: The LLM shall supply every join row, label, text value,
and order. Axiom Indexer shall preserve those strings under its released newline
and refusal law. It shall not trim mandatory context or add instructions.

**REQ-P-NATIVE-005**: Codex-specific and Claude-specific references may change
instruction ordering, tool-call syntax, progressive-disclosure advice, and
return formatting. They shall not change Source STDO meaning, selected frame
identity, role boundaries, or source routes invisibly.

**REQ-P-NATIVE-006**: An Executive may prepare Worker or Reviewer context and
receives their closed return. A Worker shall not create Reviewer independence or
promote its own result. A Reviewer shall not repair while retaining the Reviewer
claim.

**REQ-P-NATIVE-007**: Skill pickup, map visibility, or a role label grants no
semantic, operation, decision, review, acceptance, publication, or runtime
authority.

**REQ-P-NATIVE-008**: Failure to resolve the map, dependency, selected frame,
source route, evidence boundary, or task shall produce a visible hold or
re-entry request rather than guessed context.

**REQ-P-NATIVE-009**: This release shall not claim a GTL composition,
GraphFunction, deterministic assignment packet, tokenizer-budget engine,
renderer, skill generator, model invocation, or ABG runtime.
