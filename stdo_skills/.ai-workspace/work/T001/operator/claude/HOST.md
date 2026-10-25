# Claude host mechanics

Verified local version: Claude Code 2.1.306. Configured fable/high remains inherited; actual resolution is recorded only from the run.

Official documentation inspected 2026-10-25: [Extend Claude with skills](https://code.claude.com/docs/en/skills). Repository skills live in .claude/skills/<name>/SKILL.md. Project skill search includes parents up to the worktree root. Description supplies automatic selection; /skill-name explicitly invokes the entry. Default invocation permits both user and model. disable-model-invocation:true removes automatic selection and is not selected here. Optional frontmatter and supporting files can specialize mechanics. Plugin skills use a namespace; names can collide across project/personal/plugin scopes, so verify the actual selected path. Some newer documented behavior requires versions after 2.1.306; do not assume it applies. This task selects a repository-local install first and requires actual discovery evidence.

Tenant algorithm and prompt design remain your own; this file is sourced host input, not a donor design. Your construction host exposes only configured a_c MCP tools. Executable tests unavailable in this activation remain explicitly unperformed for Root's later proof.
