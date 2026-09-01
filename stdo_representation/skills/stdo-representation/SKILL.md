---
name: stdo-representation
description: Use the exact STDO 2.5.0-rc.4 semantic compression and its logical constraint index to frame source-grounded work for an Executive, Worker, or Reviewer. Use when Codex or Claude needs STDO guidance without loading the whole standards corpus, when selecting visible reference frames for an assignment, when re-entering exact STDO source, or when joining an ordered agent request. Do not use as proof of semantic truth or runtime authority.
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
   - Source STDO release `stdo://releases/v2.5.0-rc.4/`, installed-manifest
     SHA-256
     `4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`,
     and standards member-set SHA-256
     `504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656`;
   - complete source-corpus file SHA-256:
     `074fcb07258792008c31998ed2cf4f4234bec92f9e7be10b177569559387808d`;
   - compression file SHA-256:
     `90400806e79cd09f350f285000c8579af81f621cdbe3753125ed9d74bcb6b466`;
   - compression canonical SHA-256:
     `5b6a5df2e2429f7b1d463e2b9107ca58f5c482e9565e98e792650f41b222a4cf`;
   - index file SHA-256:
     `5237339d919d352944c42ea201ae49c48b885db02255f5ca1a67173c2b0c1c3f`;
   - index intrinsic SHA-256:
     `bdfe3c09fe196a7c1f1634d0441c616e96049961356d41f85bdead2d3a0fa8ce`;
   - accepted project frame-basis SHA-256:
     `e55baf9e244be377140374636b2ec8bde361aec38ee27f260daba02baef2342e`;
   - frame-basis acceptance-decision SHA-256:
     `ecad96e450c97bc3ad276bf1d541bda7fae860a88363451e851be689f6b57a92`;
   - Axiom Indexer exact version `v2.5.0-rc.4`, qualified ref
     `refs/tags/axiom_indexer/v2.5.0-rc.4`, member inventory
     `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
     and `ac.py` SHA-256
     `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
   In the Specification Stack monorepo, acquire that immutable dependency from
   the child root with this root-forced sequence:

   ```sh
   stack_root="$(git rev-parse --show-toplevel)"
   axiom_ref=refs/tags/axiom_indexer/v2.5.0-rc.4
   axiom_root="$(mktemp -d "${TMPDIR:-/tmp}/axiom-indexer-v2.5.0-rc.4.XXXXXX")"
   test "$(git -C "$stack_root" cat-file -t "$axiom_ref")" = tag
   git -C "$stack_root" archive --format=tar "$axiom_ref" | tar -xf - -C "$axiom_root"
   test -f "$axiom_root/build_tenants/core/code/ac.py"
   test "$(shasum -a 256 "$axiom_root/build_tenants/core/code/ac.py" | cut -d ' ' -f 1)" = \
     dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
   ```

   Recompute the extracted seven-member inventory and require
   `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`.
   Use `$axiom_root` as `<axiom-indexer-root>` below. The final file test is
   mandatory because a child-scoped empty archive can otherwise exit
   successfully. Before the coordinated tag exists, only the expressly
   authorized commit-B construction may use the sibling candidate after
   verifying the same seven-member inventory and exact file digests; that use
   is construction evidence and cannot satisfy release qualification or
   ordinary released use.
3. Read
   `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/logical-constraint-map.json`.
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
   - Reviewer evaluates the exact subject and evidence without repair, grades
     evidence-bound technical severity, and returns its result and triage to
     Executive without assigning priority, promotion effect, disposition, or
     continuation. Executive alone consumes the complete Product view and
     assigns those decision coordinates under accepted project policy.
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
11. To construct a request, follow the target reference's seven-section order:
   role and outcome; frame and exact subject; hard constraints; index context
   and evidence routes; open solution space; return and stop contract; then
   `ACTION` last. Include only material constraints and leave every realization
   choice not prohibited by authority or the selected frame open to the target
   LLM. Author a bare ordered JSON array of
   `{"label": string, "text": string}` sections and choose every byte yourself.
   This is caller guidance, not a prompt engine, schema, selector, or renderer.
   Resolve the exact Axiom Indexer `v2.5.0-rc.4` cut, then run its pure
   joiner:

   ```sh
   python3 <axiom-indexer-root>/build_tenants/core/code/ac.py join \
     --input <sections.json> \
     --output <request.txt>
   ```

Return to Executive with the selected frame details, any source re-entry,
validation result, unresolved residuals, and resulting request path or bounded
answer. Do not load unrelated index regions merely because they are available.
