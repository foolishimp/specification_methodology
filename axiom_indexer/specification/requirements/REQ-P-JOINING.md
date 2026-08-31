# REQ-P-JOINING — Exact Labeled-Text Joining

Family: `REQ-P-JOINING-*`
Status: Active

Derives from: `../PRODUCT.md#prompt-joining`

**REQ-P-JOINING-001**: The caller shall supply one ordered JSON array whose
rows contain exactly `label: string` and `text: string`.

**REQ-P-JOINING-002**: The joiner shall emit each `label`, one newline, and its
`text`, with two newlines between rows and no added terminal newline.

**REQ-P-JOINING-003**: The joiner shall preserve caller order, repeated labels,
empty strings, Unicode, and multiline text. It shall not trim, sort, select,
resolve, interpret, rewrite, budget, truncate, or orchestrate.

**REQ-P-JOINING-004**: Malformed shape, non-string fields, invalid UTF-8, or an
input/output path alias shall refuse before writing output.

**REQ-P-JOINING-005**: Acting as Executive, the LLM shall self-use the logical
map and selected reference frames to author one request. For visibility and
debugging, that request shall show each selected frame URI, its purpose, and
its source route.
