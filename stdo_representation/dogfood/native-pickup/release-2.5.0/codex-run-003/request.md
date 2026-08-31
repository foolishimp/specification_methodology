# One-shot native Codex qualification

Act as the Executive for one bounded, non-mutating qualification of the current
STDO Representation source checkpoint. Use the canonical
`$stdo-representation` skill discovered natively in this repository. Use its
Codex layout. Do not inspect any path under `dogfood/`, any review or commentary
under `.ai-workspace/comments/`, Git history, or prior qualification evidence.
The only permitted prior-decision read is the exact accepted frame-basis
decision selected by `stdo_representation.json`.

Subject:

- repository root: `/Users/jim/src/apps/specification_stack/stdo_representation`;
- checkpoint: `95f7bf2061189e27348695df14b8597c4bc9c0bd`;
- expected skill SHA-256:
  `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6`;
- expected eight-member Product inventory SHA-256:
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`;
- expected program file SHA-256:
  `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63`;
- expected program canonical SHA-256:
  `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`;
- expected index file SHA-256:
  `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`;
- expected index intrinsic SHA-256:
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`.

Perform all of these checks from current bytes:

1. Verify the checkpoint, canonical skill bytes, exact Product-member rows and
   inventory, program file and canonical identities, index file and intrinsic
   identities, map-to-program binding, accepted frame-basis revision 13 and its
   Product-owner decision, and the candidate status boundary in
   `releases/v2.5.0.md`.
2. From this child root, use the skill's root-forced immutable acquisition for
   Axiom Indexer `v0.1.0-rc.1`. Verify annotated tag object, peeled commit,
   repository tree, seven-member Product inventory, and `ac.py` bytes. Never
   read or substitute the mutable `axiom_indexer/` sibling.
3. Start from the logical constraint map. Select exactly one real reference
   frame from its top-level `frame_refs`. Show that frame's URI, purpose, and
   Source STDO route. Clauses, residuals, symbols, and digests are not frames.
4. Use the smallest relevant map clauses, then perform bounded Source STDO
   re-entry through exact map source route(s) sufficient to settle the distinct
   meanings of Product-Definition Identity, Release Cut, Product, and Install.
   State those distinctions. Do not load the complete standards corpus.
5. Construct a lean, ordered Codex Reviewer request that evaluates this
   deliberately suspect assertion: `stdo_representation.json is itself the
   immutable STDO Representation Product, its Release Cut, and its Install`.
   The request must bind the exact subject and evidence, preserve Reviewer
   independence, prohibit mutation and repair, distinguish mechanical
   validation, publication, and Product-owner acceptance, and require a closed
   findings return to Executive with verdict, evidence, unresolved residuals,
   and the smallest lawful re-entry if held. It must contain exactly the one
   selected top-level frame and separately identify supporting clauses or
   residuals.
6. Author a bare ordered JSON array of `{"label": string, "text": string}`
   sections at
   `dogfood/native-pickup/release-2.5.0/codex-run-003/sections.json`. Choose the
   labels and ordering according to the canonical Codex layout. Run only the
   pure `ac.py join` from the immutable extracted Axiom Product to create
   `dogfood/native-pickup/release-2.5.0/codex-run-003/joined-request.txt`.
   Verify the joined bytes are exactly `label + "\\n" + text` for each section,
   joined by `"\\n\\n"`, with no hidden wrapper, interpretation, or mutation.

Do not modify any existing file. You may write only `sections.json` and
`joined-request.txt` inside `codex-run-003`; use `/tmp` for disposable
acquisition state. Do not invoke another model or execute the joined request.

Return one concise Executive closure. `PASS` requires every check and artifact
above to succeed exactly. Otherwise return `HOLD` with the observed mismatch;
do not repair or rerun. Include the selected frame details, exact Source STDO
re-entry performed, all observed identities, artifact paths and SHA-256 hashes,
unresolved residuals, and confirmation that the Reviewer return route is
closed back to Executive.
