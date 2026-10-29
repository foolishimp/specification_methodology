# Independent review of the frozen scaling construction

Reviewed freeze `b1133743613fc6a7ed11d0656e013ea31e32004f1889a9cd63e47bd1bd646ab5`, runtime identity `1290f055bd72891d7a0965f9804e0fd71206e616f9706a3356b920927c9b50fb`. Exact sources and inspected evidence are pinned in `SUBJECT.json`; independent in-memory comparisons are in `CHECKS.json`.

No blocking structural defect found in the character-witness proof construction or its connection to the existing model contract. One S3 custody defect remains in this frozen setup source. Full practical completion is not established: the first public command returned `incomplete` at actual runtime serialization, after its generated proof and replay stages passed.

## Finding

**S3 — Setup checks normalized manifest text where it claims exact raw prior custody.** `build_tenants/lean/scripts/formal_support.py:153–154` reads the selected prior manifest through `read_text()` and hashes its UTF-8 re-encoding. A CRLF transport variant therefore passes the pinned LF digest after universal-newline conversion. An in-memory discriminator on the actual T012 manifest confirmed distinct raw digests, identical normalized digest and identical parsed descriptor. This does not alter any selected member hash or falsify the currently delivered support: its retained prior bytes exactly equal the pinned source. Check raw bytes before decoding. The Executive selected that repair during this review; its successor source and regression are outside this frozen-cut verdict.

## Source argument

`AC/Structure.lean:102–122` proves uniqueness from a strict chain of exact character lists and `String.ofList_injective`. `sortLabeled_perm` preserves the complete list for every fuel value; the generated reconstruction equality supplies the required original order. There is no hash collision or unproved encoding-injectivity premise. A wrong literal, repeated identity, omitted member or incorrect sorting witness must fail a concrete equality/strict-order obligation.

`scripts/gate_codegen.py:104–155` connects those conditions to the actual model. All local and external character blocks reconstruct the model's strings, the sorted labeled list reconstructs their full concatenation, and exact `zip tail` equality binds every adjacent pair to the checked blocks. Independent parsing found all 1,987 local and 1,021 external identities equal to source, all 3,007 adjacent pairs present across 24 blocks, and an exact label permutation restoring source order. This includes block boundaries. Local uniqueness, external uniqueness and separation are derived from that one complete concatenation.

External-reference witnesses also retain their inclusion obligation: `member_of_block_index` requires an actual successful index equality and inclusion in the complete external list (`AC/Structure.lean:150–163`; `gate_codegen.py:59–83`). They are not membership claims about an unrelated producer table. The resulting identities, key range, edge bounds and reference bounds feed the unchanged `wellFormed_of_range`/`checked_of_wellFormed` contract.

The public driver compiles all seven generated data/proof modules, audits the expected theorem axioms and replays all six deciding proof modules (`scripts/formal_gate.py:251–261`). It still requires actual Lean whole-model output, actual selected projection output and the supplied Graphify view to match the source-bound expectations before returning verified (`:262–285`). Merely proving the model cannot bypass those runtime comparisons. The serialization control's retained actual JSON matches its expected C0/DEL, quoting, backslash and Unicode strings; this is finite bridge evidence, not a general serializer theorem.

## Conserved support and execution standing

The exact T012 and successor support manifests have the same 30,405 member names. Independent comparison confirms 30,392 unchanged hashes and exactly the declared 13 changed tenant source/object pins. Original fresh-proof origin material is unchanged. Core Model/Closure/Projection and external support are conserved; the actual frozen direct imports add no external proof dependency. The selected establishment replays Structure, GateProof and GateRuntime and audits 16 generic contracts with only the existing permitted axioms. A new whole-Mathlib replay is not warranted by this delta.

Author result `lean/public-positive-001/result.json` (`f7a77cb2ec7ea2c74ebc506d203726d4293581705a564729abc882b1eba82c25`) records successful generated proof stages and dynamic replay, then `actual-runtime exceeded selected time limit`. Its elapsed time is 341.48 seconds and native child high-water RSS is 13,050,642,432 bytes. The configured Lean `-M4096` is not a physical RSS guarantee. `checked_claims` remains empty and the full public outcome is correctly incomplete. Source correspondence of the completed actual output and supplied-view comparison are therefore still open on this run.

This review used source inspection and standard-library in-memory parsing/hashing only. No reviewer compiler, proof, actor, public gate, cache, candidate or Git operation ran. Writes are confined to this review directory. The later raw-byte repair was detected at closure; the inspected original source is retained here with its frozen SHA. The next review must bind any successor runtime source explicitly.
