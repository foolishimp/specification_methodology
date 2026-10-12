# Abandoned run, kept as evidence

Written by the case owner. This run was stopped by the operator after the
calibration step logged 6,907 context tokens on a 235-byte input, against
2,259 for the same calibration outside the repository. Cause, verified by
re-running the calibration from a directory outside any repository after
changing the instrument: the headless CLI loads CLAUDE.md files from its
working directory and its ancestors into the actor's context. The actor
process ran under this run directory, so every step here received the
workspace's CLAUDE.md bootstrap text (about 12 KB across three files, one
of which carries an STDO 2.x method compression) in addition to the measured
context. The six step outputs that completed before the stop are retained
unchanged; no judgment is made of them. The successor run uses the repaired
instrument, whose actor runs in a fresh empty directory outside any
repository and logs that directory.
