# Iteration 3 Check Scripts

The scripts behind the exit proofs of iteration 3, kept here so that
another actor can rerun them. Run them from the tenant root with `python3 -I`
or `bash`. They read; only `apply_frontier.py` wrote, once, in I3-3e, and it is
kept as the record of that integration. It reads an extraction JSON that is
kept at `../returns/I3-3e-frontier-changes.json`; its hard-coded scratch path
must be pointed there to rerun it.

| Script | Proof it supports |
|---|---|
| `frontier_check.py <common inventory> <tenant frontier>` | every keyed row of the common inventory is present once in the tenant frontier; lists the tenant child rows (I3-3e, I3-3r, I3-8r) |
| `locus_check.py` | every `member#anchor` locus in the frontier resolves to a heading in `standards/` (I3-3e) |
| `links.py standards` | every relative link and anchor under `standards/` resolves; its known false positives are math notation (`X_v`) and the anchor into the common conformance file, which it does not index |
| `verify_ai.sh <scratch dir>` | materialises the pinned Axiom Indexer from its tag and prints tag, commit, tree and subtree; the seven member digests and the aggregate are then checked as in `a_c/i3/README.md` (I3-5k) |
| `run_ac.sh <ac.py> <output dir>` | runs `validate` and the four projections in both modes, logging commands and exit codes (I3-5k) |
