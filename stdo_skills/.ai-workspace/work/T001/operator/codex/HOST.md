# Codex host mechanics

Verified local version: codex-cli 0.164.0. Configured gpt-6-astra/max remains inherited; actual resolution is recorded only from the run.

Official documentation inspected 2026-10-25: [Build skills](https://learn.chatgpt.com/docs/build-skills). A skill folder contains SKILL.md with name and description; optional scripts, references and agents/openai.yaml support it. Codex normally discovers repository .agents/skills directories from the current directory through the repository root. Explicit CLI invocation uses $skill-name or the skills selector. Descriptions support automatic selection and should lead with the relevant task. Only selected skill bodies are loaded. Duplicate names are not merged. Updates are normally detected; restart if discovery is stale. Relative resources must survive installation. User-level and plugin distribution are distinct installation choices. This task selects a repository-local install first. None of these documented mechanisms guarantees model selection or task success; qualify the actual host.

Tenant algorithm and prompt design remain your own; this file is sourced host input, not a donor design.
