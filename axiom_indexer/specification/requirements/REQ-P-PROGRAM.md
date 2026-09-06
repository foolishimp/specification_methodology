# REQ-P-PROGRAM — Symbolic Axiomatic Program

Family: `REQ-P-PROGRAM-*`
Status: Active

Derives from: `../PRODUCT.md#program-law`

**REQ-P-PROGRAM-001**: A program shall contain one absolute program URI, one
exact `a_c` calculus URI, one source-basis URI, zero or more frame URIs,
declared vocabulary URIs, symbols, clauses, and residuals.

The MVP program is the `a_c.text` source-facing authoring surface. Structural
validation does not claim that it is a complete admitted `M_b`.

**REQ-P-PROGRAM-002**: Every symbol, clause, and residual shall have one globally
unique absolute URI and non-empty source references.

**REQ-P-PROGRAM-003**: A clause shall declare `relation | constraint`, one
operator URI, and ordered operands. Each operand contains exactly one symbolic
reference or scalar literal.

**REQ-P-PROGRAM-004**: Every local reference shall resolve exactly once. Every
external kind, operator, role, or frame reference shall be declared in the
program or resolved by a selected frame.

**REQ-P-PROGRAM-005**: Every residual shall declare its kind, affected subjects,
uncertainty, and non-empty source or frame re-entry references.

**REQ-P-PROGRAM-006**: The program shall contain semantic content only. Provider
receipts, grants, acceptance judgments, carrier admissions, timestamps, prices,
and release records are not program fields.

**REQ-P-PROGRAM-007**: Instantiation derives a logical adjacency and constraint
view from unchanged program bytes. The view shall not become rival authority.

**REQ-P-PROGRAM-008**: A program may declare source-grounded frame indexes with
unique identities, one declared frame, exact scope, selected clause identities
and retained residual identities. These declarations shall not replace their
source-owned evaluation contracts or supply task applicability or authority.
Programs without frame-index declarations retain their existing valid behavior.

**REQ-P-PROGRAM-009**: Explicit logical dependencies shall use the existing
role-labelled clause operands and URI references wherever sufficient. The
selected vocabulary owns premise, consequence, condition, exception and support
meaning. Code shall retain ordered roles, references and literal qualifications
without inventing implications or evaluating their truth.
