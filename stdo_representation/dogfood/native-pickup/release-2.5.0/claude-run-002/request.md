/stdo-representation

Act as a fresh Claude Reviewer using the native STDO Representation skill. Work
only from the current frozen candidate at commit
`2849d52fa5fe299d11b96ce28a4e322f23f3cfd9`. Do not inspect any prior
`dogfood/` run, review, commentary, or expected answer.

Evaluate this bounded claim: “A passing Axiom Indexer validation makes the
STDO logical constraint map semantically true and authoritative.” Construct a
concise, ordered Claude Fable 5 request for that review and return it closed to
the Executive. Write only these two repository files:

- `dogfood/native-pickup/release-2.5.0/claude-run-002/sections.json`
- `dogfood/native-pickup/release-2.5.0/claude-run-002/joined-request.txt`

Requirements:

1. Before opening the on-disk skill, inspect the instruction supplied by the
   native slash expansion. Explicitly report whether it preserves the literal
   shell fragment `cut -d ' ' -f 1`; do not silently repair a changed fragment.
2. Verify and separately label:
   - skill SHA-256 `ba7b83bce4a3a437ec78fcd6a1b5745d080bda23d93236d20067bfa14f1158d0`;
   - Claude reference SHA-256 `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164`;
   - eight-member inventory SHA-256 `e5155655497ad3021b33fc90a3e105031d5b199be7c3245fd26a9da6a27eb45b`;
   - project frame-basis SHA-256 `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`;
   - acceptance-decision SHA-256 `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.
3. From this child root, root-force acquisition of immutable Axiom Indexer
   `refs/tags/legacy/axiom_indexer/v0.1.0-rc.1`; verify tag object
   `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
   `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
   `8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
   `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
   and `ac.py` SHA-256
   `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
   Do not read or use the mutable `../axiom_indexer` sibling.
4. Open the logical constraint map first. Verify its `program_uri` and
   `program_sha256` binding before using it. Select exactly one actual reference
   frame, and only from the map's top-level `frame_refs`. The selected frame's
   STDO URI is its source route. If useful, select one supporting clause or
   residual separately through `source_routes`; label it as a clause or
   residual, never as a frame. Never call a digest or decision a frame.
5. Show the selected frame URI, purpose, and source route. Re-enter only the
   bounded Source STDO passages needed to evaluate the claim and list every
   opened repository path. Preserve Reviewer independence and distinguish
   mechanical validation, publication, and semantic acceptance.
6. Author a bare ordered JSON section array using the Claude layout, then join
   it with the extracted immutable `ac.py`. Verify that the joined output is an
   exact ordered concatenation of the section text. Do not hand-join or use
   local deterministic code.
7. Return: invocation observations; exact identities; map/program binding;
   selected frame details; supporting item if any; Source STDO re-entry;
   validation, publication, and acceptance disposition; unresolved residuals;
   output paths; and a final `PASS` or `HOLD`. Do not edit the candidate or
   repair any failure.
