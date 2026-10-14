# Return, activation TL (Writer, revision 2b)

result: `candidate_ready`; no acceptance claimed. FOUNDATIONS lines at `8b42994`.

F4. New properties from Reported value: P6 value ∈ returned non-satisfied (916–921); P7 gap with all returned satisfied → `indeterminate` (925–929); P8 only `falsified` returned → `falsified` (914–919). Mixed values stay the declared rule's (919–921). Value-only mutants, record intact, all detected: swap `falsified`/`out_of_frame` 284, M3 142, M1 201, M2 307 cases; record mutants 206 each. 34,241 assertions; `--check` 0.

Domain: one to three mandatory components, agreeing bases, each contributed by its own evaluation; no non-mandatory results or outside counterexample (929–930, 930–933 excluded).

F5. Relative and `#a` destinations rebased; scheme, `/`, fenced and inline code unchanged; digests over owner bytes. 42 tests pass.

Residuals: regenerate frames (`--check` 1); rerun `check.py` after FOUNDATIONS or generator changes; CROSS_SYNTHESIS row 5 and `kind` still say verbatim.

Files: `generate_frames.py`, `test_generate_frames.py`, `finite_oracle/{README.md,template.py}`, `conjunction/{check.py,mutants.py,FINITE_RESULT.json}`.
