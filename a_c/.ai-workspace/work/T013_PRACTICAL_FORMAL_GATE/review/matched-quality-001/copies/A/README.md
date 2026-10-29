# Saved gate result report

Requires Python 3.11+ and only its standard library.

```sh
python3 -B gate_report.py inputs/examples/verified.json
python3 -B -m unittest -v
```

The command writes one JSON report and newline. Exit 0 means reporting succeeded,
including refused, unsupported and incomplete saved results. Invalid or unreadable
input exits 2 with empty stdout and an error on stderr; these are report command
codes, distinct from gate exit codes. The command only reads the named file.

For example, reporting `inputs/examples/view-mismatch.json` preserves the four
checked claims and five requested claims and labels the category
`supplied_view_mismatch`. This helps identify the unchecked supplied-view claim
without treating the entire parent model as invalid.

The full parsed source, including identities, evidence, unknown fields and limits,
is retained in `reported`. Its raw byte digest records custody only. Saved labels
are not authenticated, the gate is not run, and this report grants no authority,
semantic acceptance, prose fidelity, complete calculus conformance or owner closure.
Paths and evidence references in the input are data and are never followed.

Only the gate's reported total elapsed interval is summarized. Missing or null
elapsed time stays unknown, zero stays zero, and invalid observations are retained
but marked invalid in the cost summary. Stage times are not totaled. Token and
money costs remain unknown even if extension fields suggest accounting values;
elapsed time is not total delivery cost. Historical examples remain historical.
