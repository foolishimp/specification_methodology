# Reader Unicode boundary repair

Construction candidate under existing CS-09 / OP-02. Predecessor is main
`0aa00244602293d8e0fd384b7a280ae443afcd7d` and source freeze
`86afcb8a1d9e0d73297414fc935125dfb107f3cfad732be4694ec96ce8ce8c2b`.
The existing freeze, seals, native traces and historical reviews are unchanged.
The Executive bound a Writer realization refactor; no Git or release effects
are selected in this activation. Independent test/review is still required.

[CommonMark 0.31.2 §2.1](https://spec.commonmark.org/0.31.2/#characters-and-lines)
uses LF, CRLF and CR line endings; blank lines contain only space/tab.
[ATX headings](https://spec.commonmark.org/0.31.2/#atx-headings) and
[setext underlines](https://spec.commonmark.org/0.31.2/#setext-headings) also use
explicit space/tab boundaries. [Closing fences](https://spec.commonmark.org/0.31.2/#fenced-code-blocks)
permit only space/tab after the marker. Python's broader Unicode character
classes do not supply those structural rules.

The reader now shares one LF/CRLF/CR segmentation function between scanning
and extraction, retains original endings and UTF-8 section bytes, and uses
explicit space/tab structural checks. The same correction covers ATX empty
headings, comment/container heading guards and setext/blank-line guards. An
ASCII-only empty heading is recognized before nonempty content. Unsupported
Markdown forms retain their prior closed-domain refusals.

The [probe](probe.py) uses the existing isolated manager-interface fixture and
invokes the public reader subprocess. It is not a real-manager or actor trial.

| Discriminator | [Before](BEFORE.json) | [After](AFTER.json) |
|---|---|---|
| U+2028 inside a physical line followed by `## False` | `checked`, invented section | `refused`, section absent |
| U+00A0 after a would-be closing fence, then `## False` | `checked`, invented section | `refused`, unsupported unfinished fence |

All 33 reader/gate tests pass. New CLI cases cover eight non-Markdown line
separators, invalid Unicode fence suffixes, later valid space/tab closure,
LF/CRLF/CR/mixed endings with and without a final ending, exact section bytes,
line coordinates, non-ASCII ATX separators and nonblank Unicode setext input.
One initial positive control exposed the ASCII empty-heading priority case;
it was repaired before the final passing run.

`SOURCE_DELTA.json` pins the three changed files, their predecessor hashes and
these compact evidence inputs. The remaining predecessor-pinned inputs are
verified unchanged. This is a successor delta, not a rewrite of the old seal
or an assertion of renewed native-host qualification.
