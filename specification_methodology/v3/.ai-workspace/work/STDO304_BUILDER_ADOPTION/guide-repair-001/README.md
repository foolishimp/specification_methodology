# Fresh-checkout guide repair

The separately assigned independent review found a severity-3 fresh-checkout
failure. The Executive selected repair because of its material downstream
impact. [The intake](INTAKE.json) preserves the exact relayed finding and
bounded repair grant; [GUIDE_PREIMAGE.md](GUIDE_PREIMAGE.md) preserves the
reviewed guide. The original adoption freeze remains unchanged at
`f8b03f74ea82b90a0de84c2abf8e014ba6bb84eb287300614329d64402a16e18`.

Only the guide's materialization section changed. One block now declares
`STDO_TOOLS` before branching. An absent destination is materialized and then
verified; an existing path or dangling symlink goes directly to verification.
The branch contains no force, replacement or overwrite path.

| Actual command case | Result |
|---|---|
| [Original fresh block](before-fresh-block.json) with `STDO_TOOLS` unset | Exit 1, unbound variable reproduced |
| [Original existing-tree block](before-existing-block.json) on an absent destination | Exit 2, missing materialized tree reproduced |
| [Corrected fresh branch](after-fresh-branch.json) | Exit 0; released archive checked, 191 sources materialized and verified |
| [Corrected existing branch](after-existing-branch.json) | Exit 0; exact 191-source tree verified without materialization |
| [Corrected dangling-symlink branch](after-dangling-refusal.json) | Exit 2; redirected path refused, original dangling symlink retained |

These are actual runs of the exact extracted guide block under `sh`, using
an exclusive new fixture beneath ignored `v3/.stdo/` and the exact installed
3.0.4 materializer. The receipts retain the scripts, hashes, cwd, environment,
stdout, stderr and exit codes. The existing project tool tree and immutable
installation were not changed.

[Focused verification](verification.json) confirms the changed section only,
unchanged prior frozen files apart from the guide, preserved predecessor
freeze, three valid shell blocks, unchanged resolving guide links and clean
whitespace. Prior adoption results remain applicable to their unchanged
subjects; no full adoption or broad suite was rerun.

Writer return: `candidate_ready` for the selected bounded independent recheck.
The successor subject is [REVIEW_FREEZE_02.json](../REVIEW_FREEZE_02.json).
Independent recheck and Executive disposition are not claimed complete here.
