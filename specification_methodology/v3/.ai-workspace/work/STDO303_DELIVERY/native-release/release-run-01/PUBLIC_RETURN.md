# STDO 3.0.3 public release proof

STDO 3.0.3 is published as a normal, non-prerelease GitHub Latest release.
The selected PUBLIC-phase checks pass. This return precedes the final
continuing-source status/bookkeeping checkpoint and changes no native payload.

Public release: https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.3

| Coordinate | Verified identity |
| --- | --- |
| Source A | `b90789488237094ae2f29241c58ce71f12450a59` |
| Published carrier B on main | `de3443d7c9fc54b70dcd899586c47853aafdc9b5` |
| Native C / release branch | `07bdb34a2d472a3b5e678f60584fd02b24a388f4` |
| Immutable annotated tag T | `c0905d8c022abd1387828b4837de1b0515e49fbb` |
| Manifest M | `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| GitHub exact-tag / Latest release ID | `430743607` |
| Public notes SHA-256 | `5336df792f8369838d5ca9a59e529bf4630ca1354ba8d70ebd3b4bfd8a74f773` |
| Downloaded manager wheel SHA-256 | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |

The [frozen publication plan](../source-preparation-001/publication-plan.json),
`ATOMIC_PUSH.json` and [published-ref proof](../source-preparation-001/published-refs.json)
bind the exact atomic push of main, stable tag and release branch. The initial
orchestration guard included Git's `HEAD` pseudo-ref when comparing a
`refs/*`-only plan; it stopped before invoking push. The retained
`attempt-001-prepush-guard.json` records this correction. No real remote ref
had changed. The Executive consumed it, and the unchanged exact push argv
then succeeded. No non-atomic fallback, RC selector or retarget was used.

`github-publication/VERIFIED.json` binds draft creation, four fully verified
uploads and publication of the **same release ID** as normal Latest. No
duplicate draft or asset was created. Both the exact tag endpoint and Latest
endpoint agree. The notes use absolute GitHub/download links and actual
manager commands, separately from the frozen installed release note.

`DOWNLOADS.json` and [public-download-proof.json](../source-preparation-001/public-download-proof.json)
establish four fresh unauthenticated HTTPS asset downloads and exact checksum
sidecars. `MANAGER_PUBLIC.json` records a new isolated manager installed from
the downloaded wheel; all 13 production Python members match it. Public
Git acquisition disabled inherited global/system Git configuration and
credential prompts, used the explicit public HTTPS repository, and reproduced
the same canonical manifest M. No originating source tree or manager
PYTHONPATH supplied the installation.

The [installed-public proof](../source-preparation-001/installed-public.json)
checks **107 exact files**, comprising all 106 native payload members and the
manifest. `URI_CHECKS_PUBLIC.json` records nine actual entry/bootstrap/schema,
documentation and tooling resolutions with native byte equality. The installed
materializer checked its fixed archive, extracted all 191 source files into a
separate writable workspace and verified that pristine tree. The installed
proof-reader payload reproduced exactly. Final ordinary-manager verification
remained valid after these operations.

`PUBLIC_FINAL_REFS.json` confirms every unselected pre-existing remote ref
unchanged. `PUBLIC_RELEASE_READBACK.json` confirms all four pre-existing
releases retain their names, bodies, classification, target identities and
asset identities/digests. Only the new 3.0.3 release became Latest.
`CARRIER_REMOTE_PARITY.json` records direct remote main B and tracking parity
`0/0`; new public evidence still awaits its authorized bookkeeping commit.

`PUBLIC_PROOF.json` freezes these substantive observations and verifies all
28 members of the earlier local proof unchanged. Runtime environments,
installed stores and writable extracted trees remain ignored. No shared
installation, a_c/Skills source/basis change, old-release metadata edit,
new Lean proof or browser/WebGL qualification was performed. Semantic and
actual-use limits remain those stated in the published notes and independent
review. The historical failed-log EOF whitespace exception remains preserved.

The Writer returns the closed public result for the Executive's final readback
before the continuing-source status/bookkeeping checkpoint.
