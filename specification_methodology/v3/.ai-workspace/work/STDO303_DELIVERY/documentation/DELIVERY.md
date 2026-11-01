# STDO 3.0.3 installed documentation

The candidate now carries the constraint explorer as mandatory offline
documentation under `standards/documentation/`. Normal release-manifest
construction includes it, the ordinary manager installs it, and installed
verification covers it. A separate viewer install is unnecessary.

Open the [candidate documentation home](../../../../build_tenants/common/standards/documentation/index.html)
or its [reading guide](../../../../build_tenants/common/standards/documentation/README.md).
After an actual 3.0.3 release installation, the supported entry is:

```sh
stdo resolve stdo://releases/v3.0.3/standards/documentation/index.html
```

Open the returned path in a browser. A host that refuses local HTML can serve
its installed release root on loopback, as described in the reading guide.

## Exact distribution and subject

The [documentation inventory](../../../../build_tenants/common/standards/documentation/DOCUMENTATION.json)
and [assessment input](assessment-input.json) bind the selected payload and
checking machinery. The imported HTML is byte-identical to the reviewed a_c
T-014 artifact, SHA-256
`73f8e39be3b41cfe996a49752b9f167524e122fce945f2a1dd89abc57cc7b738`.
It represents historical common source
`35fb4824a064a84df5af214a0d0e2da597c18ac6`: 1,987 local records, 841 constraints
and 58 embedded source files. The release-facing entry names this scope and
links separately to the current installed method. This is not a source-matched
representation of the 3.0.3 corpus.

## Observed verification

- Eight focused documentation checks pass. They cover omission, changed bytes
  despite refreshed inventory, contradictory source identity, metadata kind,
  unusable or wrong navigation, obsolete resolve URI, fresh bundling and output
  preservation. The native release preparation gate requires this contract.
- Common package checks report 90 payload files, 6,040 local reference checks
  and no failures. Existing generated frames reproduce with `--check`.
- [Qualification-003](qualification-003/qualification.json) used the normal
  manager CLI for manifest, install, verify and resolve in an isolated store.
  All four documentation files matched. Removing the acquiring repository did
  not prevent verification. Altering the installed entry was detected; restoring
  its exact bytes restored successful verification.
- [Installed browser observations](browser-observation.json) and the
  [screenshot](installed-viewer.png) cover Chromium 156.0.8078.79: entry navigation,
  search, full constraint text, embedded source lines, two-step trail and Back,
  2D/3D controls, orbit and zoom, and text use with WebGL disabled. The main
  interaction loaded only the two local HTML documents, with no external
  requests or page errors. A mistaken initial automation selector and an early
  search observation were corrected and retained in the record.

Qualification-003's synthetic manifest SHA-256 is
`9adbbb720cbb1cde70cdeafe6b4769fd57d0ea4022fdc66b697a97b5ba641b79`.
Its test tag exists only in the disposable acquiring repository, which was
removed. It is **not** a published release identity. Qualification-001's
[harness failure](qualification-001/FAILURE.md) and the successful intermediate
[qualification-002](qualification-002/qualification.json) remain recorded.
Disposable stores and repository copies are ignored; retained reports identify
their exact inputs and outcomes.

## Delivery boundary

The [closed independent assessment](REVIEW.md) found no remaining material
defect after the navigation and metadata repairs, and independently verified
the installed result. This completes the selected bounded documentation
integration, not the remaining release work.

The [owning ticket](../../../tickets/active/T-006-STDO-3.0.3-documentation.md)
selects documentation integration and its installed assessment. There has been
no main-branch checkpoint, release tag, public upload, remote push or shared
installation in this increment. The later public release must recheck acquisition
against its actual immutable tag and manifest. Other selected 3.0.3 tooling
bundling remains separately outstanding.

This result does not prove the English constraints, qualify the complete method,
or finish a_c's newly selected reusable user-project workflow. That workflow
extends the existing a_c Product under T-015; STDO is its first documentation
application, with source and distribution identity preserved.
