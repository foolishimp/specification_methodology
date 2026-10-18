# Records mechanism repair return

Work result: `candidate_ready` for the bounded records mechanism. This is author construction evidence; independent review, owner decisions and candidate qualification remain open.

The two edits are `records/build_records.py` and `records/README.md`. `refs()` now preserves the frozen `plugins/spec/LICENSE` receiving column. `validate()` requires a locus for each proposed `conserved` or `superseded` relation and rejects every unresolved selected locus. `build()` calls that validator before constructing a passing proof or returning artifacts, and `main()` writes only after `build()` succeeds.

The isolated exact `d60dead4` package and records copy passes build and `--check`: 705 identities, 815 resolved loci and all 20 controls. The prior validator accepts each missing-locus defect; the repaired validator rejects both. Removing the actual plugin LICENSE file or a selected heading from the isolated package refuses the full build before any of its four output files is written. An unresolved proposal with an unresolved selected locus also fails.

All original source bytes, 705 IDs, raw seed dispositions, proposed dispositions and existing pending decisions are preserved. All effective dispositions remain unresolved and acceptance pending. The other 704 projected rows are unchanged. `LOAN_ROW_INDEX.json` and `CLAIM_DIGEST_RECOVERY.json` are byte-identical to the preimage. Full observations, exact mechanism digests and fixture coordinates are in [records-return.json](records-return.json).

No API or schema change is required. Root should complete D1-D4 and candidate/rule integration, then run `build_records.py` and `build_records.py --check`. The live generated files, `RULES.json`, candidate members and Git are untouched by this Writer. Existing artifacts are not rewritten on failed builds; a current `--check` refuses an invalid subject. These fixture results do not qualify the concurrently edited integrated candidate.
