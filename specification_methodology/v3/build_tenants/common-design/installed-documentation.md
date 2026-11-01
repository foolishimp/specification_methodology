# Installed documentation design

Implements [DOC-01–DOC-06](../../specification/requirements/INSTALLED_DOCUMENTATION.md).

The existing native package and manager already copy every manifest-listed
`standards/` member into the exact immutable cut. Put the documentation under
`standards/documentation/`, explicitly marked non-normative. This conserves
the current manager schema and install/verify/resolve path; no optional
supplement installer or viewer runtime dependency is introduced.

`documentation/index.html` is the release-facing local entry. It states the
distributing version and the historical graph subject, then links to the exact
selected offline explorer in `constraint-explorer/index.html`, the reading
guide and the installed current standards. The viewer retains its own source
identity and all source passages. `DOCUMENTATION.json` identifies the imported
artifact and hashes every other documentation member.

`../common-tools/documentation.py` owns repeatable bundling and checking.
Its contract pins the current presentation and exact represented model/source.
The November 2 review repair regenerates the T-014 model and corpus using the
current unified renderer, conserving the entire embedded view-data payload,
including initial focus. The original T-014 HTML remains historical evidence.
The installed reader supplies Files and 3D/2D/Layered switching; the repaired
2D label projection is on this consumer path. Updating this selection requires
an explicit contract change. The verifier
checks embedded data, the finite local link closure, required member set and
hashes independently of the import route. It accepts a package root or a
complete installed release root. The local qualification uses the unchanged
manager through a synthetic stable 3.0.3 tag in an isolated repository, then
opens the result from the disposable store. That tag is not a release tag in
the main repository.

`package_tools.py` and `native_release.py` now live beside `documentation.py`
under the registered `common-tools/` implementation route. Documentation uses
the single package checker's route semantics. The old working-record entry
paths are compatibility launchers; the package launcher checks its fixed target
digest before execution. No working record is an executable dependency of the
registered tools. Missing required siblings yield a refusal. Native preparation
continues to confine its outputs to the same `STDO303_DELIVERY/native-release/`
territory; moving code does not widen that permission.

Native release construction must run the documentation check before freezing its payload.
The release manifest then covers these documentation files normally, and
installed verification detects their deletion or modification. The 3.0.3
asset set requires the exact native manifest and manager wheel, with generated
checksums. A separately supplied supplemental archive is optional; installed
documentation has no such download dependency. The tag describes installed
documentation. The release plan retains a separate exact published-install
check. The local qualification selects the installed manager executable
explicitly and uses disposable repositories and stores. Its observations name
their actual subject; earlier browser evidence does not qualify changed HTML.
