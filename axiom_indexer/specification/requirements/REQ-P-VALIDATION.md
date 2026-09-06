# REQ-P-VALIDATION — Basic Consistency Validation

Family: `REQ-P-VALIDATION-*`
Status: Active

Derives from: `../PRODUCT.md#validation-boundary`

**REQ-P-VALIDATION-001**: Validation shall check closed shapes, unique absolute
URIs, source grounding, symbolic resolution, local reference closure, clause
operand shape, and residual re-entry closure.

**REQ-P-VALIDATION-002**: The MVP shall resolve every selected frame URI and
record its observed digest. Machine interpretation of frame-declared operator,
arity, or type rules is deferred until a separate exact frame-rule contract is
selected; the validator shall not infer those rules from prose.

The separately selected frame-index projection contract checks authored
membership, reference closure and source freshness only. It does not select
machine interpretation of frame-declared operator, arity, type or logical rules.

**REQ-P-VALIDATION-003**: Diagnostics shall identify affected program items,
fields, and references by symbolic URI. Array positions or line numbers may be
included only as display hints.

**REQ-P-VALIDATION-004**: Diagnostics shall be deterministically ordered and
machine-readable so an LLM can repair more than one defect per iteration.

**REQ-P-VALIDATION-005**: Validation and instantiation shall not mutate the
program. Equal program bytes and resolved bindings shall reproduce equal
results and derived content digests.

**REQ-P-VALIDATION-006**: Validation shall not claim semantic fidelity, truth,
completeness, satisfiability, acceptance, authority, or useful compression.

**REQ-P-VALIDATION-007**: MVP tests shall include a valid self-program plus
dangling-reference, duplicate-identity, unresolved-source, malformed-clause,
ungrounded-item, and physical-relocation cases.
