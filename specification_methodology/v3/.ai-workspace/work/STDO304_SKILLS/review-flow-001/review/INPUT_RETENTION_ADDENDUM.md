# Raw-input custody addendum

The Executive authorized relocation of exactly the three PNG acquisition copies to external local custody before the local checkpoint. I independently verified the completed relocation against the unchanged original review seal and the Writer's [retention receipt](EXTERNAL_INPUT_RETENTION.json), SHA256 `51ea1fa881714e4157e2d88b32585832e00b2ae59f8a32d554f4cbc671798847`.

The external root is `/Users/jim/.local/share/stdo-review-evidence/STDO304_SKILLS/review-flow-001/`. The receipt maps each original sealed relative path to the same relative path under that root:

| Original sealed path | Bytes | SHA256 |
|---|---:|---|
| inputs/IMG_3377.png | 16,096,861 | `430afb7b1f18b103e507de4c02cd8badc90f230eea6ad33653ce03e1d7533cf8` |
| inputs/IMG_3378.png | 15,189,347 | `2de5184b4d5faa970ee678d77aa9203ccaa9b293aa5425e021c0ad3febc2f529` |
| inputs/IMG_3379.png | 14,362,632 | `2838dd25ef4cd0b6755c2ef6d7bdf848f6b0cf94da72ab9abd1eb6063f050957` |

All three external files match their original sealed sizes and hashes, totaling 45,648,840 bytes. Their former repository copies are absent. Resolving only those three paths through the receipt verifies all 91 original review-seal members; the remaining members and the linked commentary remain unchanged.

The [final review](FINAL_REVIEW.md) remains SHA256 `ac4bb0cd0692b1c50894dad4307d1fe36045603ca2cdcf09e9a8b65164e1d56b`, and [REVIEW_EVIDENCE.json](REVIEW_EVIDENCE.json) remains `e1ad85d923825a8b69d51079e220666e3014d31e23d73535cd1e7fa8f59a056e`. Final source delta `1d76228a44a54e722b0eea2e90bf4e80c88044d23cc450fd5ac7b44987c9a74c` and package inventory `96daff39e127b482d791327ea6c0def270fc8648ea2e1d005503312a7644872d` also match unchanged; all 26 effective source pins and 110 payload pins verify.

**Git alone does not contain these three raw inputs.** Full raw-input reconstruction requires the external files and this explicit custody mapping, with the recorded size/hash checks. The original seal is preserved rather than rewritten to conceal that portability limit. This addendum and the receipt are subsequent custody records, outside the original seal's member population.

Relocation changes no prior finding, expectation, source meaning, review verdict or qualification limit. This was a narrow post-relocation identity check, not a new source review, test or model run. The Reviewer performed no Git effect. Custody verification is complete for the Writer's already-authorized checkpoint; acceptance/disposition remains with the Executive or Product owner.
