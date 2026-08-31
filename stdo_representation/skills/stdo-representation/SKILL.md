---
name: stdo-representation
description: Use the exact STDO logical constraint map to frame source-grounded work for an Executive, Worker, or Reviewer. Use when Codex or Claude needs STDO guidance without loading the whole standards corpus, when selecting visible reference frames for an assignment, when re-entering exact STDO source, or when joining an ordered agent request. Do not use as proof of semantic truth or runtime authority.
---

# Use STDO Representation

Work from the STDO Representation repository root.

1. Verify the exact inputs before use:
   - map file SHA-256:
     `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`;
   - map intrinsic SHA-256:
     `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`;
   - Axiom Indexer `v0.1.0-rc.1` tag object `e7afc8a42a7123aebe91cb7582cb037b1aae612d`,
     commit `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
     `8c9ad5f5e99a60c18fb8c1802471753afb226272`, member inventory
     `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
     and `ac.py` SHA-256
     `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
2. Read
   `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json`.
   Start from the map, not the full STDO corpus.
3. Identify the requested role and outcome. The LLM remains the Executive,
   Worker, or Reviewer; the map does not choose for it.
4. Preserve the role boundary:
   - Executive binds the task and evidence, selects frames and role, and
     receives and disposes the closed return;
   - Worker performs one bounded construction, self-validates, and returns to
     Executive without promoting its result, creating Reviewer independence,
     or choosing continuation; and
   - Reviewer evaluates the exact subject and evidence without repair while
     retaining the Reviewer claim, then returns findings to Executive.
5. Select the smallest relevant frame URIs and linked constraints. Show each
   selected frame's URI, purpose, and source route so the choice is inspectable.
6. Follow the selected constraints. Re-enter exact Source STDO through a map
   source route when the task, a residual, or an unresolved meaning requires it.
7. Keep uncertainty explicit. Do not turn a structural map into semantic truth,
   acceptance, authority, or a runtime fact.
8. If the map, dependency, selected frame, source route, evidence boundary, or
   task does not resolve exactly, stop and return a visible hold or source
   re-entry request. Do not guess context.
9. For Codex, read [the Codex layout](references/codex.md). For Claude Fable 5,
   read [the Claude layout](references/claude.md).
10. To construct a request, author a bare ordered JSON array of
   `{"label": string, "text": string}` sections. Choose every label, text, and
   ordering detail yourself. Resolve the exact Axiom Indexer `v0.1.0-rc.1`
   install, then run its pure joiner:

   ```sh
   python3 <axiom-indexer-root>/build_tenants/core/code/ac.py join \
     --input <sections.json> \
     --output <request.txt>
   ```

Return to Executive with the selected frame details, any source re-entry,
validation result, unresolved residuals, and resulting request path or bounded
answer. Do not load unrelated map regions merely because they are available.
