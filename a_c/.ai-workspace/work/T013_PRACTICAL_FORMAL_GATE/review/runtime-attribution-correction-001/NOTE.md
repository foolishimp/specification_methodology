# Narrow correction of runtime attribution

This addendum corrects two sentences while preserving their closed original records:

- `review/frozen-scaling-001/REVIEW.md:5`, closure `571e171bf4a8e890f136e4b3e79702a70284ee8adb4db826ed7324d2f0045fc9`: replace “at actual runtime serialization” with “at the actual-runtime stage”.
- `review/reuse-design-002/REVIEW.md:13`, closure `2a017b576a06dec913269f7c9536bcde9d0f89bea53ecf075aba7326de7b87ef`: replace “at runtime serialization” with “at the actual-runtime stage”.

The public result established `actual-runtime exceeded selected time limit`. It did not isolate serialization as the cause. My return and the two sentences attributed more than that evidence established.

The subsequently completed author probes distinguish the operations: initialization passed in 1.214 seconds, complete `modelJson` serialization passed in 1.284 seconds, and evaluating `checkModel` alone timed out at 90.045 seconds. Their inspected source calls show that `checkModel` is a sufficient blocker under this limit. They do not establish that it is the only remaining expensive operation. The full public invocation's 13,050,642,432-byte aggregate child high-water RSS cannot be assigned to runtime serialization, `checkModel`, or any single stage from that observation.

The original verdicts are otherwise unchanged: the new proof construction had no blocking structural finding; the public command remained incomplete; reuse R1–R3 were discharged only at design level. No proof or runtime execution was performed for this correction. Exact retained probe and review pins are in `CLOSED.json`.
