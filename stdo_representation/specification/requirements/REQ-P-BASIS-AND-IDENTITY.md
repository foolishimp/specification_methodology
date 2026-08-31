# REQ-P-BASIS-AND-IDENTITY — Thin Product Coordinates

Family: `REQ-P-BASIS-*`
Status: Active
Category: Constraint / Guarantee

Derives from: `../PRODUCT.md#exact-dependency-bases` and
`../PRODUCT.md#identity-and-provenance`

## Purpose

Bind the STDO authoring map, native skill, and joined requests to exact Source
STDO and Axiom Indexer coordinates without turning physical paths, counts, or
runtime observations into semantic identity.

## Selected bases

```text
Source STDO release:
  stdo://releases/v2.5.0-rc.1/
Source STDO installed manifest SHA-256:
  3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338
Source STDO member-set SHA-256:
  87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5
Axiomatic Calculus SHA-256:
  cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d

Axiom Indexer release tag:
  v0.1.0-rc.1
Axiom Indexer annotated tag object:
  e7afc8a42a7123aebe91cb7582cb037b1aae612d
Axiom Indexer peeled commit:
  dc3e00998da36dae6ac7b76b340431a85096c83c
Axiom Indexer repository tree:
  8c9ad5f5e99a60c18fb8c1802471753afb226272
Axiom Indexer Product member inventory SHA-256:
  7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
```

## Identity law

- Program and logical-map identities use the exact released Axiom Indexer
  canonicalization and digest law.
- Skill identity binds its exact regular-file inventory and symlink target
  strings.
- Joined-request identity is SHA-256 over exact UTF-8 output bytes.
- Logical source, calculus, frame, symbol, clause, residual, operator, and role
  identities are absolute URIs.
- Physical paths occur only in invocation-local Binding Sets or evidence.
- Line numbers, array positions, filenames, path counts, token counts, and
  lexical similarity do not create semantic identity.

## Requirements

**REQ-P-BASIS-001**: Every released program and map shall bind exact Source STDO
and Axiom Indexer coordinates above. A branch, mutable selector, compatible
local checkout, or unverified cache shall not substitute.

**REQ-P-BASIS-002**: The selected Product artifact paths shall be:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/
  axiomatic-program.json
  logical-constraint-map.json
```

Their content digests shall be recorded only after exact bytes exist and shall
not be inferred from the path.

**REQ-P-BASIS-003**: Every program item shall have an absolute identity and at
least one logical Source STDO route. Residuals shall have explicit re-entry
routes. A physical binding shall not enter the program as meaning.

**REQ-P-BASIS-004**: An invocation Binding Set shall resolve every required
logical prefix unambiguously and remain external to the portable Product member
set. Missing, escaped, ambiguous, or mismatched bindings shall refuse.

**REQ-P-BASIS-005**: The logical map shall bind the unchanged valid program,
resolved-source evidence, and intrinsic map digest emitted by the exact Axiom
Indexer dependency. A map from different program or dependency bytes is a
different subject.

**REQ-P-BASIS-006**: The canonical skill shall be exposed through exactly these
relative symlink targets:

```text
.agents/skills/stdo-representation -> ../../skills/stdo-representation
.claude/skills/stdo-representation -> ../../skills/stdo-representation
```

**REQ-P-BASIS-007**: A joined request shall bind the exact ordered input array
and output bytes. Reordering, relabelling, or changing one string creates a new
request identity.

**REQ-P-BASIS-008**: Dogfood observations may bind model, configuration, time,
inputs, outputs, usage, and evidence boundary. They remain observations and do
not enter program, map, skill, or joined-request identity.

**REQ-P-BASIS-009**: Release qualification shall bind the frozen eight-member
Product inventory, dependency bases, claim bytes, evidence, annotated immutable
RC tag object, peeled commit, and tree. Publication or validation alone shall
not imply Product acceptance.
