# Native skill onboarding basis

The old Getting Started section assumed the historical coordinated RC
marketplace. A standalone native tag has no such root marketplace. The new
section instead resolves the verified installed plugin root. It documents
Claude `--plugin-dir`, exact-file use in Codex and optional Codex local
marketplace registration, keeping actual loaded-copy verification mandatory.

Observed local `codex plugin marketplace add --help` accepts a local root;
`codex plugin add --help` accepts `PLUGIN@MARKETPLACE`. The marketplace layout
and local source object follow the fetched official OpenAI source:
https://developers.openai.com/plugins/build/plugins (accessed 2026-11-03).
Claude's `--plugin-dir` was established by the retained host research and is
checked again in this preparation. No host plugin installation or model call
was executed here; these are setup instructions, not new discovery or workflow
qualification. Direct exact-file loading remains available without registration.
