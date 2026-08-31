# Claude Fable 5 Layout

Put the source-linked context before the operative request. Use clear labels or
XML-style tags when they make the boundary easier to parse.

Prefer this seven-part order:

1. `<role_and_outcome>`: name the acting role and intended result.
2. `<reference_frame_and_exact_subject>`: list each selected frame URI,
   purpose, and source route; bind the exact subject and evidence boundary.
3. `<hard_constraints>`: state the governing laws, effect boundary, and
   forbidden moves.
4. `<index_context_and_evidence_routes>`: include only selected clauses,
   residuals, evidence, and exact source-re-entry routes.
5. `<open_solution_space>`: name the allowed gaps. Unless a hard constraint
   requires or prohibits one, inspection order, tools, decomposition, source
   re-entry, and realization choices remain with the acting model.
6. `<return_and_stop_contract>`: state the required result, completion evidence,
   residual or hold return, and stop conditions.
7. `<ACTION>`: put the actual requested action last.

Keep the source-linked index excerpt bounded. Keep instructions brief. Do not
prescribe hidden reasoning, ask Claude to reproduce it, or precompute a
solution. This is presentation guidance, not a prompt engine, schema, selector,
or renderer.

This layout follows the Claude Fable 5 guidance for brief steering, explicit
boundaries and purpose, structured long context, and task instructions after
long-form inputs.

Guidance basis:
<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5>
and
<https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices>,
retrieved 2026-08-31.
