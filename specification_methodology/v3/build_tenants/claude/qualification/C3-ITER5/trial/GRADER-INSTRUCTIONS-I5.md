# Addendum to the grader's instructions, iteration 5

You follow [`../../C3-ITER4/trial/GRADER-INSTRUCTIONS.md`](../../C3-ITER4/trial/GRADER-INSTRUCTIONS.md)
with these additions. Two tags are new: `W` and `A`.

1. **`W` items** are graded exactly like `M` items. Do not treat them
   differently; their purpose is decided after grading, not by you.
2. **`A` items** carry an `admissible` field naming one point of the
   return and two returns, one marked correct, that read the same at that
   point. Read the whole return, then grade the item at the named point
   only:
   - the return reads as either of the two recorded returns at that
     point: `indeterminate`, reason "the observation does not separate the
     admissible answers", quoting the words at the point;
   - the return says nothing at that point: `indeterminate`, reason
     "silent";
   - the return reads as neither recorded return at that point:
     `indeterminate`, reason "outside the described ambiguity", quoting
     the words; add the item's id to a `diagnose` list in the run's record.

   Never return `satisfied` or `falsified` on an `A` item: at the recorded
   point the observation supports neither.
3. **Record.** Beside each value record the item's `tag`, and for every
   `indeterminate` a `reason`; a run's record carries its `diagnose` list,
   empty when nothing is listed:

```json
{"E15": {"value": "indeterminate", "tag": "A", "reason": "the observation does not separate the admissible answers", "evidence": "..."}}
```

   Print the counts per tag per run.
