# Independent Unicode-boundary reproduction

Predecessor: `0aa00244602293d8e0fd384b7a280ae443afcd7d`.
Reader SHA256: `a2dabd893dacf893d30ba35d91f6f2356084301175ba5bd01e98cfdd1976d3fb`.
The exact Git bytes were copied to scratch; the concurrently repaired worktree
reader was not used. Expectations were frozen before successor exposure:
`e11c66f1d8fb87fed66f07b6a84ce69af3786af3dfbe3984ecba403e57874c7d`.

The 23 raw specimens produce 69 real reader CLI calls. Each checks exact
section text, physical line coordinates and digest, exact catalog entries, or
refusal without either projection field. The manager is an explicit synthetic
fixture supplying internally consistent exact identities/digests; these calls
test projection/refusal semantics, not an actual installed STDO release.

There are 44 baseline expectation failures and 25 successful controls/checks:

- U+2028 and seven adjacent Python splitlines separators (VT, FF, FS, GS, RS,
  NEL, PS) inside a paragraph become false heading boundaries. Selecting the
  nonexistent Phantom section incorrectly returns checked; the One projection
  and heading catalog are also wrong.
- NBSP, EM SPACE, NARROW NBSP and IDEOGRAPHIC SPACE after a closing-looking
  fence are incorrectly accepted as closing whitespace. Without a later real
  close, the predecessor incorrectly returns checked projections. With a later
  valid close, it incorrectly returns unterminated refusal for valid projection
  and catalog requests.
- CR, LF, CRLF, mixed physical endings and ASCII space/tab closing controls
  preserve the expected bytes and coordinates.

`baseline/RESULTS.json` retains every exact raw source as UTF-8 hex, actual
command, exit, stdout/stderr and structured result. `baseline/SOURCE.json`
binds the Git blob, commit and copied reader. No source changes, native model
trials, global configuration, install, commit or push were performed.

For successor compatibility, reuse the retained input extraction/comparison
from the prior `testing/final_replay/replay.py` in this new evidence territory;
do not edit or rerun the old frozen script in place. Its retained 33 result
objects comprise 32 actual native calls and one mechanical EF03 reproduction.
The prior live path remains Claude revision4 with direct skill-file loading
after denied native Skill calls; revision5 supplies replay only. The declared
harness supplied dispatch and durable recording.
