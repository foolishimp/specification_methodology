# Addendum to the grader's instructions, iteration 5

You follow [`../../C3-ITER4/trial/GRADER-INSTRUCTIONS.md`](../../C3-ITER4/trial/GRADER-INSTRUCTIONS.md)
with these additions.

1. **`W` items** are graded exactly like `M` items. Do not treat them
   differently; their purpose is decided after grading, not by you.
2. **`A` items** observe a point at which two admissible returns read the
   same. For every run, return `indeterminate` on an `A` item with the
   reason "the observation does not separate the admissible answers",
   unless the return is silent on the point, in which case return
   `indeterminate` with the reason "silent". Never return `satisfied` or
   `falsified` on an `A` item: doing so would claim a decision the
   observation cannot support.
3. **Record** the item tags in your JSON beside each value, and print the
   counts per tag per run.
