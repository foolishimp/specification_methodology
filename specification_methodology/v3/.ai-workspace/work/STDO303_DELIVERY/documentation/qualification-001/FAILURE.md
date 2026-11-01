# Initial qualification harness failure

The first driver invoked `python -m stdo_toolchain`. That package has no
`__main__.py`; the attempt stopped before manifest generation or installation.
The corrected public CLI module is `python -m stdo_toolchain.cli`.
No delivered payload failed in this attempt. The synthetic repository remains
an ignored local fixture; it is not a release or a source dependency.

Qualification-002 passed after that correction. Qualification-003 adds actual
installed tamper rejection and restoration and is the selected final run.
