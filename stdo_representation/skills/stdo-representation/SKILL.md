---
name: stdo-representation
description: Use the exact STDO 2.5.0 semantic compression and its logical constraint index to frame source-grounded work for an Executive, Worker, or Reviewer. Use when Codex or Claude needs STDO guidance without loading the whole standards corpus, when selecting visible reference frames for an assignment, when re-entering exact STDO source, or when joining an ordered agent request. Do not use as proof of semantic truth or runtime authority.
---

# Use STDO Representation

Work from the STDO Representation repository root.

First determine whether the skill came from mutable source or an immutable
Product Install. Discovery through a repository symlink proves neither release
nor acceptance. When the task requires a released Representation, verify its
external release record, profile-qualified immutable tag, and complete member
inventory before calling it released.

In a source checkout, read `releases/v2.5.0.md` for the current status, exact
eight-member inventory, claim boundary, and planned Product-local refs.
Recompute its member rows from bytes and symlink targets. If the declared
immutable tag is absent, or the record still says candidate, use the skill only
as a source-project convenience and report that boundary.

1. Preserve the layer order: Source STDO is semantic authority; the Axiomatic
   Program is canonical `a_c.STDO` compression; the Logical Constraint Map is
   the deterministic index over that unchanged compression.
2. Verify the exact inputs before use:
   - compression file SHA-256:
     `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783`;
   - compression canonical SHA-256:
     `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`;
   - index file SHA-256:
     `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`;
   - index intrinsic SHA-256:
     `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`;
   - accepted project frame-basis SHA-256:
     `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`;
   - frame-basis acceptance-decision SHA-256:
     `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`;
   - Axiom Indexer `v0.1.0-rc.1` tag object `e7afc8a42a7123aebe91cb7582cb037b1aae612d`,
     commit `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
     `8c9ad5f5e99a60c18fb8c1802471753afb226272`, member inventory
     `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
     and `ac.py` SHA-256
     `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
   In the Specification Stack monorepo, acquire that immutable dependency from
   the child root with this root-forced sequence:

   ```sh
   stack_root="$(git rev-parse --show-toplevel)"
   axiom_ref=refs/tags/legacy/axiom_indexer/v0.1.0-rc.1
   axiom_root="$(mktemp -d "${TMPDIR:-/tmp}/axiom-indexer-v0.1.0-rc.1.XXXXXX")"
   test "$(git -C "$stack_root" cat-file -t "$axiom_ref")" = tag
   test "$(git -C "$stack_root" rev-parse "$axiom_ref")" = e7afc8a42a7123aebe91cb7582cb037b1aae612d
   test "$(git -C "$stack_root" rev-parse "$axiom_ref^{}")" = \
     dc3e00998da36dae6ac7b76b340431a85096c83c
   test "$(git -C "$stack_root" rev-parse "$axiom_ref^{}^{tree}")" = \
     8c9ad5f5e99a60c18fb8c1802471753afb226272
   git -C "$stack_root" archive --format=tar "$axiom_ref" | tar -xf - -C "$axiom_root"
   test -f "$axiom_root/build_tenants/core/code/ac.py"
   test "$(shasum -a 256 "$axiom_root/build_tenants/core/code/ac.py" | cut -d ' ' -f 1)" = \
     dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
   ```

   Recompute the extracted seven-member inventory and require
   `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`.
   Use `$axiom_root` as `<axiom-indexer-root>` below. Never substitute the
   mutable `axiom_indexer/` sibling. The final file test is mandatory because a
   child-scoped empty archive can otherwise exit successfully.
3. Read
   `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json`.
   Start from the index, not the full STDO corpus. Verify that its `program_uri`
   and `program_sha256` bind the exact compression before relying on it.
4. Identify the requested role and outcome. The LLM remains the Executive,
   Worker, or Reviewer; the index does not choose for it.
5. Preserve the role boundary:
   - Executive binds the task and evidence, selects frames and role, and
     receives and disposes the closed return;
   - Worker performs one bounded construction, self-validates, and returns to
     Executive without promoting its result, creating Reviewer independence,
     or choosing continuation; and
   - Reviewer evaluates the exact subject and evidence without repair while
     retaining the Reviewer claim, then returns findings to Executive.
6. Select the smallest relevant frame only from the map's top-level
   `frame_refs`. A frame's STDO URI is its source route. Select supporting
   clauses or residuals separately and use their `source_routes` entries. Never
   label a clause, residual, symbol, or digest as a reference frame. Show each
   selected frame's URI, purpose, and source route so the choice is inspectable.
7. Follow the selected constraints. Re-enter exact Source STDO through an index
   source route when the task, a residual, or an unresolved meaning requires it.
8. Keep uncertainty explicit. Do not turn a structural index into semantic truth,
   acceptance, authority, or a runtime fact.
9. If the compression, index, dependency, selected frame, source route, evidence boundary, or
   task does not resolve exactly, stop and return a visible hold or source
   re-entry request. Do not guess context.
10. For Codex, read [the Codex layout](references/codex.md). For Claude Fable 5,
   read [the Claude layout](references/claude.md).
11. To construct a request, author a bare ordered JSON array of
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
answer. Do not load unrelated index regions merely because they are available.
