# M1 Writer repair return

The supported Markdown literal-anchor repair is implemented and frozen in
`../CANDIDATE-repair1.json` for independent review. No acceptance or release
decision is made here.

## Change and deciding path

The same-line backtick substitution in `composition._check_fragment` is
replaced by a bounded inline scanner. It consumes escaped punctuation, pairs
maximal backtick runs of equal width across line endings, and consumes actual
HTML tags as units. Backticks in a tag attribute therefore do not become code
delimiters. Paragraph/block boundaries keep separate inline spans separate;
indentation within an existing paragraph does not start a new code block.
The original heading-slug function remains byte-identical.

These rules follow the relevant distinctions in CommonMark's
[code spans](https://spec.commonmark.org/0.31.2/#code-spans),
[backslash escapes](https://spec.commonmark.org/0.31.2/#backslash-escapes), and
[raw HTML](https://spec.commonmark.org/0.31.2/#raw-html). The existing fragment
scanner remains a bounded source convention, not a general Markdown renderer.
The resolver/API, file/graph limits, installed Store boundary and unsupported
resource results are unchanged.

Changed files relative to the reviewed eight-file candidate:

- `specification_methodology/v2/src/stdo_toolchain/composition.py`
- `specification_methodology/v2/tests/test_composition.py`
- `specification_methodology/v2/README.md`
- `specification_methodology/v2/design/TOOLCHAIN_MANAGER.md`

## Evidence

- `PREIMAGE.json` and `preimages.zip` preserve all eight reviewed files and
  the original manager evidence, independent review and retained probe before
  repair. `../CANDIDATE.json` and prior proof remain unchanged.
- `test-run-new-cases.json`: initial actual-CLI repair cases passed.
- `test-run-affected.json`: 51 composition/cohort tests passed. During subsequent
  self-check, an indented continuation within a multiline code span exposed a
  further same-class boundary case. The source used for this earlier run is
  retained in `intermediate-before-paragraph-fix.zip`.
- `test-run-final-composition.json`: all 20 composition tests passed after that
  correction, including 10 literal/escape/code negative cases and 11 real-anchor
  positive cases through the public CLI. The 31 cohort checks from the affected
  run remain applicable to their unchanged implementation and shared slug code.
- `reviewer-probe-replay-final.json`: the original retained control passes;
  the review's exact escaped-tag and multiline-code cases both return exit 1,
  `valid: false`, and relation code `missing_fragment`. All three retain the
  review's exact definition and relation bytes. Two real-anchor counterfactual
  controls return exit 0 and `valid: true`. The temporary copies were removed.
- Owned source/test/document `git diff --check` passes.

Final proof binds its source byte inventory. The earlier 51-test run and replay
are retained as earlier evidence, not relabelled as execution on the successor.
No broader suite was rerun. No installed manager/release, repository Git state,
or unrelated Product files were mutated by this repair. Candidate-source CLI
invocation remains necessary until a manager deployment is separately selected.
