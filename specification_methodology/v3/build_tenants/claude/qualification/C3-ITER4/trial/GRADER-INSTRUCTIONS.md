# Instructions for the grader

You grade several anonymised returns of one task against fixed
expectations. You receive the expectations file (fixture and items) and
the returns, labelled only `run-1`, `run-2`, … in a shuffled order. You
do not know which input each run received, and you must not guess or
rank runs by any quality other than the items.

For every item and every run, return exactly one value:

- `satisfied`: the return meets the item; quote the words that meet it
  (at most 25 words);
- `falsified`: the return contradicts the item; quote the words that
  contradict it;
- `indeterminate`: the return neither meets nor contradicts the item,
  or is silent; say which.

Also record, per run, the actor's disclosure line (item 1 of its return)
verbatim, and whether the run's "what you used" list names documents the
task did not list.

Write one JSON file at the path the activation names:

```json
{"task": "TT-nn", "runs": {"run-1": {"disclosure": "...", "used_unlisted": false, "items": {"E1": {"value": "satisfied", "evidence": "..."}}}}}
```

Write nothing else anywhere. Then print, per run, the counts of
satisfied, falsified and indeterminate.
