# Exact reuse integration 001

The independently reviewed candidate is integrated byte-for-byte into the 11
selected live paths. All 38 live predecessor files matched before integration;
the three new paths were absent. All 41 reviewed candidate pins match afterward,
and all 27 separately pinned Lean theorem/generator/support/configuration source
files outside the delta are unchanged. The exact before/after sets are in
`SOURCE-PINS.json`.

All 117 promised Python controls passed with zero skips: 19 reuse, 10 selected
origin path, 31 compatibility and 57 existing Lean Python tests. Combined stdout
and stderr are retained in the four logs. The first 60 are the same staged
control selection. The additional suite covers importer/fixture reconstruction,
CLI source currentness and bounded Python process cleanup. These are unit and
integration controls; they establish no actual Lean proof or F_P benefit.

`run_controls.py` imports the integrated production modules and test files.
Only temporary storage is redirected: tempfile defaults and TMPDIR select this
record's per-suite tmp directory; explicit TemporaryDirectory requests for the
two live Lean test cache paths are redirected there; mkdir calls on exactly
those two test cache paths are no-ops. All deciding code and path guards remain
the integrated subject. The harness removes optional external control retention
and suppresses bytecode. No temporary files or synthetic keys remain.

The source-only public identity command reports
`07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601`
with 24 exact pins and no origin-selection coordinate. Production origin remains
absent. No compiler, proof, model actor, live-origin setup, prior-result signing,
Git operation, publication or owner acceptance occurred.

Worker integration is closed and live Lean/Graphify source ownership is returned
to the Executive. The exact source is ready for the separately selected Writer
checkpoint. No runtime source mutation or actual qualification is authorized by
this closed activation. Origin setup and fresh cold/reuse trials need their
separate grant; prior cold evidence was not imported or signed.
