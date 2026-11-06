# Narrow upstream containment repair candidate003

This successor changes only `ac_upstream.py`, its public regression tests, and its design clarification. All formal, Skills, native-profile and previous repair implementations are unchanged from candidate002. The independently rechecked prior results retain their original exact scope. No additional Lean work was performed.

The source check now resolves the output and each declared input, then refuses either containment direction before any upstream invocation or output effect. Existing equal/nonfresh/symlink-output refusal remains in force. Public controls cover inside, equal, ancestor, input alias, output alias and a normalized parent-path alias; every refusal preserves the complete selected dependency tree, including Git metadata. A legitimate adjacent output remains usable.

The original conversation finding and Executive disposition are transcribed in `repair-upstream-containment/REVIEW_TRANSCRIPTION.md`. `reviewed-ac_upstream.py` preserves the exact candidate002 producer, SHA256 `383f09f7fb6d64522e25f01dcca5b41b0971acbb26895a2235bb6d8d3a320402`.

Actual public reproduction used fresh disposable copies of the pinned upstream and an explicitly relocated control receipt selecting the already bootstrapped private Python. It did not mutate the original runtime or shared project Git. Before repair the command exited2 after adding the output directory and six files; its ordinary Git status also refreshed the disposable copy's index. That failing dependency tree is retained, with no cleanup or retry against it. After repair a separate clean copy exits2 at `Output overlaps an input`, with no added, removed or changed input-tree entries. Exact argv, producer/output hashes, whole-tree snapshots and private custody coordinates are retained under `repair-upstream-containment/{before,after}/`.

This is a source-repair candidate for targeted independent recheck. Current full-model Lean proof, installedA/host qualification and browser work remain required and unperformed. The successor model is held for the Executive's semantic recheck; no expensive work has started against it.
