# Active one-pass execution choices

2026-10-18, before evaluated V3 model answers. The two-pass prototype and its
successful synthetic smoke remain separate; these choices govern `runs-v2/`.

- Frozen source subjects and source-only private oracle are unchanged.
- Treatments: `graphify-ac` and `direct`, each with one a_c F_P pass per source
  chunk; Graphify additionally supplies actual structural discovery and carrier.
- Model `gpt-6-astra`, reasoning effort `high`, default service tier, Codex CLI
  0.162.1, existing provider/authentication. Freeze/check actual settings and
  configuration identity; no global configuration or new provider.
- Source chunks: 120,000 Unicode source characters, section-aware complete-line
  partitions, packed across files; 11 Codex and 19 Claude chunks. No source
  truncation. Prompt metadata and output add context.
- Complete Graphify author cue: at most 40,000 Unicode characters including
  provenance/omission metadata; structural context is discovery data.
- Per-call wall ceiling: 1,200 seconds. At most four concurrent model calls
  across the study. Native and assisted runs use the same limits and schema.
- A separate one-pass synthetic smoke precedes V3 actors. Its usage is excluded
  from V3 treatment totals, with the two-pass prototype usage separately retained.
- Retain failed first attempts and every retry/repair. Supported repair prompts
  may include the exact failed output and mechanical diagnostics, never the
  private semantic oracle. Record new prompts/answers as distinct attempts and
  include their measured usage. No hidden replacement or silent truncation.
- At most three total attempts per chunk/stage in this initial execution;
  unresolved work remains refused/partial rather than asserted successful.
- Freeze code, source, chunks, schemas, base prompts and oracle before evaluated
  actors in `freeze-v2.json`. Derived graph views/expanded actor prompts are
  bound by the frozen algorithm and retained per invocation.

Source processing, mechanically grounded proposals, bounded semantic probes,
whole-method fidelity and owner acceptance remain separate claims.
