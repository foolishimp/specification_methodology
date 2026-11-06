# Isolated reader performance result

The one-function prototype produces the exact retained current010 `PROOFS.json`
and `index.html` bytes. Its full catalog call took **2.797193 seconds**, including
the unchanged retained-evidence validation. The lexical `source_catalog` portion
took **1.912404 seconds**; catalog encoding took 0.210866 seconds and HTML rendering
0.114839 seconds. The corpus is all 14 selected files: 15,177,421 UTF-8 bytes,
12,527 declarations and 89,214 retained references.

This is an isolated performance investigation under Root's bounded assignment.
No production or test source was edited. The C0 checkpoint subject is unchanged.
No full slow baseline, Lean proof, native actor, download or Git operation ran.

## Cause and delta

The original reference pass splits a complete masked source file again for every
declaration. Across this exact corpus that asks `splitlines` to traverse
96,325,183,513 characters in 12,527 repeated calls. GateData alone contributes
7,999 repeated splits and 91,722,405,266 characters.

The original token loop also copies and counts each body's entire prefix for
every token. The exact selected bodies contain 600,923 token matches and ask the
old prefix counter to scan 2,014,842,519 characters. Counting successive ranges
instead scans 5,866,117 characters. These are measured loop-work counts computed
without performing the slow repeated splits or prefix copies; they are not
separate timings of those old phases.

The prototype changes only `proof_reader.py:source_catalog`:

1. Retain the already computed masked `splitlines(keepends=True)` result per file
   and reuse it in the reference pass.
2. Start a declaration's line counter at its original start line, then add
   `body.count("\n", previous_match_start, current_match_start)` in token order.

The cached list has exactly the elements the unchanged split operation would
produce again. Neither pass mutates its elements. Token starts are monotonic;
the disjoint successive ranges telescope to the original prefix count. Candidate
resolution, reference deduplication, order, declaration boundaries, statements,
imports, masking and rendering are unchanged. The saved patch and prefix/suffix
digests bind the complete one-function delta.

## Equality and measurements

`FULL_COMPARISON.json` binds the 14 exact source files, selected Python, prototype
and unchanged dependency copies, retained oracle catalog/HTML, and measured phases.
Full catalog byte equality covers every declaration, reference, order and line;
full HTML byte equality also checks the complete rendered carrier.

Twelve direct old/new comparisons also agree: the six actual library files,
nested namespaces and ambiguous suffixes, comments/strings and anonymous command
boundaries, duplicate tokens across lines, escaped/multiline strings, CRLF,
CR/Unicode line breaks, empty/final lines, a long reference body, duplicate-name
refusal, and unterminated comment/string refusals. The long-body control took
0.034227 seconds before and 0.009605 seconds after; this is a small supporting
measurement, not the full-corpus speedup.

The retained baseline build receipt records 770.438870 seconds for a complete
successful reader build. That operation also performs owner inspection and
build/check work; it is **not directly comparable** to one catalog timing.
The optimized complete public build was not run. The observed removal of the
repeated catalog work supports a bounded production cost repair, followed by
the required actual public check when authorized.

Peak RSS during the full comparison was 912,408,576 bytes on Darwin. This includes
the original payload, archive parts, oracle bytes and generated catalog/HTML.
No old-run memory comparison was made. The cache retains split line objects
instead of one masked string per file; its memory tradeoff remains bounded by
the selected source corpus.

These results establish equality for the actual selected corpus and the finite
controls, with the stated algorithmic equivalence argument. They do not establish
new Lean semantics, source faithfulness, final installed qualification or release
acceptance. Production adoption remains with Root and the common Writer; the C0
checkpoint takes precedence.
