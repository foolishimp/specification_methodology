# REQ-P-RESOLUTION — Symbolic URI Late Binding

Family: `REQ-P-RESOLUTION-*`
Status: Active

Derives from: `../PRODUCT.md#symbolic-resolution`

**REQ-P-RESOLUTION-001**: A Binding Set shall map logical URI prefixes to
physical or immutable resources for one invocation. The longest unambiguous
matching prefix wins.

**REQ-P-RESOLUTION-002**: Source fragments shall resolve under the source
format's declared symbolic-fragment law. A Markdown heading URI shall resolve by
heading identity, not by line number.

**REQ-P-RESOLUTION-003**: Resolved paths shall remain confined to their declared
binding roots. Traversal outside a root shall refuse.

**REQ-P-RESOLUTION-004**: Missing, ambiguous, malformed, or type-incompatible
bindings shall return diagnostics and shall not be guessed.

**REQ-P-RESOLUTION-005**: The MVP shall record observed digests for resolved
calculus, source, and frame bytes. Expected-digest comparison remains an
external caller check until the program contract declares it. Digests do not
replace logical URIs, and member counts remain derived observations.

**REQ-P-RESOLUTION-006**: Relocating physical bytes while preserving the same
logical URI binding shall not require rewriting the program.
