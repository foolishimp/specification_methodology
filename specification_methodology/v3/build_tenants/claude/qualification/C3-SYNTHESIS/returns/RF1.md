# Return, activation RF1

result: `candidate_ready`; no acceptance claimed. R =
`standards/REFERENCE_FRAME.md`, SHA-256 `8b73ca27…5c394ef394`.

- Removed R:867–870: "A non-material revision, for example one that
  clarifies an activation or acquires evidence without changing any
  declaration, produces no new coordinate and reopens no result". R:867–872
  now labels the default reopening a tightening, matching §15.
- New R:874–890: "A revision that changes no declaration of the frame needs
  no new coordinate. That answer decides nothing about any result". ACTIVATION
  §7 decides validity.
- R:170 had the same clause ("reopens nothing"); I treated it as covered by
  "any wording" and now refer it to ACTIVATION §7.
- Predecessor: the nine-action list and "Every material revision changes
  frame identity or revision coordinates and states which prior activations,
  results, and coverage claims require reevaluation." No non-material
  clause; validity sits in Return A Closed Result.
- No delta (frontier row 364 unchanged). Residual: frames are stale
  (`rf-task-b.md:817–820`); `generate_frames.py --check` fails until
  regenerated.
