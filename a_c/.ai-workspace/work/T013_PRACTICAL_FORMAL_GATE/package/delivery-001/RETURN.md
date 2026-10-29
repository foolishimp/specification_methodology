# Local package delivery and installed cold fallback

The selected source package was built with the unchanged reviewed repair-002
packager. All 65 selected files plus SOURCE_PACKAGE.json passed exact bundle,
archive and extraction verification. The pristine extraction reproduced the
archive byte-for-byte, and remains intact for independent review.

- Manifest: `e981245097c06f693fcbe89565d5724db2103982fdb7891e8413a8a6cdc86ee4`
- Archive: `40dbe00cc85d9c1c4a6ec88634a4318d7f9363bd2d68b025d6941872319d7ea0` (22,353,920 bytes)
- Retained archive: `source-package.tar`
- Working trees: `/private/tmp/ac-t013-lean-package-001/{bundle,pristine,operational}`

The operational extraction received exactly the public support manifest's
30,405 selected members: 30,399 absent runtime dependencies copied once, and
six packaged source files matched and preserved. The copy transferred
3,254,927,206 bytes, preserved regular file modes for copied members, and retained
a complete mapping in SUPPORT-CUSTODY.json. All 65 packaged source files still
match. No .cache, origin selection/key/entry/pending, unselected runtime extras,
download, bootstrap, or fresh support establishment was copied or performed.
No temporary cache directory was needed.

The single installed public CLI check-evidence invocation on the retained
small-cold bundle returned verified in 24.436514 seconds whole invocation.
The installed identity is
`07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601`.
Only the fixed origin-selection coordinate differs from the source evidence.
The installed invocation actually took the cold branch: seven generated proof
checks, one dynamic kernel replay and one runtime execution, followed by exact
six-record model/view correspondence and support/currentness rechecks. No origin
or public reuse hint was created. Current result digest:
`f96eec30895f019f230af22ae06854481b7fa5af98d6450f0404b080391ec516`.

The fixed Python 3.12 executable is SHA-256
`a7f5b535d61d1c7326824204ac80f045a97a652abb154421e2c74fcc365a3539`.
The reviewed launcher used -I -S -B, the unchanged 90-second checking limit,
Lean -M4096 and the 600-second public bound. Darwin resource observations were
44,990,464 bytes for the isolated launcher self and 9,798,221,824 bytes for its
reaped-child RUSAGE_CHILDREN high-water field. The child observation is scoped
to this invocation and is not attributed to one proof stage or asserted to be
simultaneous total RSS. Lean -M4096 is not a physical RSS cap. The external wall
includes complete CLI exit and evidence publication; the internal checking time
excludes publication. Raw stdout/stderr and stage observations are retained.

The Executive held the proof invocation while independent public-artifact
hashing finished, then released an exclusive window. The setup copy may have
overlapped that hashing; no performance comparison uses copy time. No repair,
retry, full-model/old-full-fixture run, or actual F_P call occurred.

This qualifies Darwin-arm64 local acquisition with conserved exact support.
It is not fresh-machine onboarding, semantic acceptance, Product acceptance,
or public release. Package Worker closes delivery and returns the heavy window
to the Executive. Prepared trees remain available for independent review.
