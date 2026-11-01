# Exact grounding line-ending repair

The first actual ABIogenesis application refused a valid base quotation that
included the final LF of its declared line range. The initial code-overlay
checker used `splitlines()` and inserted separators, losing that terminal LF.
The original authoring contract in `ac_generate.author_check` preserves source
line endings. The application Worker retains the failed attempt unchanged.

The only runtime repair is in `ac_code.grounding_check`: slice
`splitlines(keepends=True)` and join with the empty string. The supplied quote is
compared exactly; it is not trimmed, normalized or rewritten. The original base
model, source, signature and manifest remain unchanged.

[SOURCE_FREEZE.json](SOURCE_FREEZE.json) supersedes the implementation freeze
for this repaired source. Backend SHA-256 is
`1c9a9b14de30f039727708da1c48ce4ba60effdd885b4a62392415c3673e0ed7`.
[VALIDATION.json](VALIDATION.json) records three affected tests passing with no
failures or skips: public CLI terminal-LF preparation/build and extra-LF refusal,
existing false base-grounding controls, and false trace quote/range/endpoint
controls. The earlier 23-test suite remains predecessor evidence; it was not
represented as freshly repeated by this repair.

The actual retained ABIogenesis model `19d435c8…` passes the repaired base import
against all 86 frozen and current nominated source files. That check traversed
1,636 grounding occurrences, including 887 with terminal LF, counting repeated
quotations repeatedly. The public ABI application build remains the application
Worker's next result. Acquisition confinement, reader code and other runtime
behavior are unchanged by this repair. No Git, installation or release effects
were performed.
