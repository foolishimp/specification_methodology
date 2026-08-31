# Claude Fable 5 Layout

Put the source-linked context before the operative request. Use clear labels or
XML-style tags when they make the boundary easier to parse.

Prefer this section order unless the task gives a better one:

1. `<context>`
2. `<reference_frames>`
3. `<constraints>`
4. `<evidence_and_source_routes>`
5. `<task>`
6. `<success_and_return>`

State why the task matters, the authorized boundary, and the stop condition.
Keep the source-linked index excerpt bounded. Keep instructions brief. Do not prescribe hidden reasoning or ask Claude to
reproduce it. For long source excerpts, keep the query at the end.

This layout follows the Claude Fable 5 guidance for brief steering, explicit
boundaries and purpose, structured long context, and task instructions after
long-form inputs.

Guidance basis:
<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5>
and
<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>,
retrieved 2026-08-31.
