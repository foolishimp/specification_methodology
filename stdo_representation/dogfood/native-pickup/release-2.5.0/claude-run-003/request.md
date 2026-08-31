/stdo-representation

Act as a fresh Claude Reviewer using the native STDO Representation skill. Work
only from the current frozen Product-member checkpoint at commit
`95f7bf2061189e27348695df14b8597c4bc9c0bd`. Do not inspect any prior
`dogfood/` run, `.ai-workspace/` commentary or review, or an expected answer.
Do not use a mutable sibling project.

Evaluate this bounded claim:

> A mutable Product Definition is the immutable Product identity. Once its
> selected bytes are installed, that Install is the Release Cut, so a source
> checkout containing those bytes may be called released without an immutable
> publication ref or separate Product acceptance.

Construct a concise ordered Claude Fable 5 request that reviews that claim and
returns the result closed to the Executive. Write only these two repository
files:

- `dogfood/native-pickup/release-2.5.0/claude-run-003/sections.json`
- `dogfood/native-pickup/release-2.5.0/claude-run-003/joined-request.txt`

Requirements:

1. Before opening the on-disk skill, inspect the instruction supplied by the
   native slash expansion. Explicitly report whether it preserves the literal
   shell fragment `cut -d ' ' -f 1`; do not silently repair a changed fragment.
2. Verify and separately label:
   - skill file SHA-256
     `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6`;
   - Claude reference file SHA-256
     `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164`;
   - exact eight-member Product inventory SHA-256
     `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`;
   - Axiomatic Program file SHA-256
     `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63`
     and canonical SHA-256
     `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`;
   - Logical Constraint Map file SHA-256
     `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`
     and intrinsic SHA-256
     `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`;
   - accepted project frame-basis SHA-256
     `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`;
   - frame-basis acceptance-decision SHA-256
     `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.
3. From this child root, root-force acquisition of immutable Axiom Indexer
   `refs/tags/legacy/axiom_indexer/v0.1.0-rc.1`; verify tag object
   `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
   `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
   `8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
   `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
   and `ac.py` SHA-256
   `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
   Do not read or use the mutable `../axiom_indexer` sibling. The immutable
   archive must supply the pure joiner.
4. Open the Logical Constraint Map before the Axiomatic Program and before
   broad Source STDO. Verify the map's `program_uri` and `program_sha256`
   binding before relying on it. Select exactly one actual reference frame,
   and only from the map's top-level `frame_refs`. The selected frame's STDO URI
   is its source route. You may select one supporting clause or residual
   separately through `source_routes`; label it as a clause or residual, never
   as a frame. Never call a symbol, clause, residual, digest, decision, Product
   Definition, Install, or Release Cut a reference frame.
5. Show the one selected frame's URI, purpose, and source route. Use the map's
   logical source routes to re-enter only the exact Source STDO passages needed
   to distinguish Product Definition, Install, Release Cut, publication, and
   Product acceptance. List every opened repository path. Treat URI references
   and exact identities as governing; do not use line numbers or counts as
   semantic identity.
6. Preserve Reviewer independence. Distinguish structural verification from
   semantic judgment and distinguish the mutable Product Definition, immutable
   Release Cut, installed Product instance, publication, and Product-owner
   acceptance. Do not repair the candidate or promote your result.
7. Author a bare ordered JSON section array using the Claude layout, then join
   it with the extracted immutable `ac.py`. Verify byte-for-byte that the
   joined output is the joiner's exact ordered concatenation with no terminal
   newline. Do not hand-join, template, rewrite, trim, or use local Product
   code.
8. Return: invocation observations; exact identities; map/program binding;
   selected frame details; supporting item if any; bounded Source STDO
   re-entry and every opened path; structural, semantic, publication, and
   acceptance disposition; unresolved residuals; output paths and hashes; the
   explicit closed return relation to Executive; and final `PASS` or `HOLD`.
   `PASS` means this one native invocation satisfied every requirement; any
   unresolved qualification defect is `HOLD`. Do not edit any existing file,
   do not rerun, and do not repair a failure.
