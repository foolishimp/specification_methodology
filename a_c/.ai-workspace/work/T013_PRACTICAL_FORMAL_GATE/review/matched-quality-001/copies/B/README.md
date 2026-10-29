# Saved gate report

Run with Python 3.11+ and its standard library:

    python3 -B gate_report.py inputs/examples/verified.json
    python3 -B -m unittest -v

One JSON report and a newline are emitted. Exit 0 means a report was produced,
including refused, unsupported and incomplete results. Exit 2 means invalid
input, an unreadable file or incorrect arguments; stdout is empty and stderr
explains the error. Only the named file is read; embedded paths are inert.
The command makes no filesystem changes.

For example, reporting inputs/examples/view-mismatch.json exposes the distinct
supplied_view_mismatch category while retaining the original identities and
checked/requested claims. Requested claims never count as checked.

All original fields, extensions and limitations survive in reported. Raw-byte
SHA-256 is custody, not truth. This helper reports saved labels without
authentication and grants no authority, semantic acceptance, prose fidelity,
calculus conformance, permission or owner closure. Local tests and candidate
availability are construction evidence, distinct from independent assessment.

Elapsed cost is only the gate's reported interval. Absent/null cost is unknown;
invalid observations remain intact; zero remains zero. Stage timings are not
substitutes. Tokens and money remain unknown regardless of extension fields.
Decimal values are serialized without binary-float rounding.
