# STDO 3.0.3 local native release proof

The exact reviewed source and locally created native release pass the selected
local gates. This return precedes the atomic publication plan and public
reacquisition; no remote publication is claimed here.

| Coordinate | Identity |
| --- | --- |
| Source A | `b90789488237094ae2f29241c58ce71f12450a59` |
| Source/native payload tree | `2c8be59c79bb00371253204b48b7c896bb4260ad` |
| Native C | `07bdb34a2d472a3b5e678f60584fd02b24a388f4` |
| Sole native parent | `23ca9c0929d7be8570edafaf30542e3daeb8dc1f` |
| Native root tree | `e2a76c02ad6d20673ebc32e74020fb2109372609` |
| Annotated tag T | `c0905d8c022abd1387828b4837de1b0515e49fbb` |
| Manifest M | `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| SOURCE_SELECTION SHA-256 | `8a522037ea6d315aa1534a46a9999343683220165692a7f9e0854fe19e9c4bf8` |
| Released manager wheel SHA-256 | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |
| Four-asset inventory SHA-256 | `fbca37bc17b6849f0893981a047996caa1d39711fa7910257139ce360f694506` |

`git-local-operations.json` records a fresh alternate index, exact native
commit, create-only annotated `specification_methodology/v3.0.3` tag and
`release/specification_methodology/3.0.3` branch, and registered attestation.
The native root contains exactly the 106 selected payload files; no source
work records entered it. No RC selector or old-ref rewrite was performed.

The [source preparation](../source-preparation-001/source.json),
[native identity](../source-preparation-001/native.json) and
[sealed selection](../source-preparation-001/SOURCE_SELECTION.json) bind the
same source, native predecessor, payload and manifest. The helper independently
reconstructs the expected manifest from the exact native inventory.

`MANAGER_LOCAL.json` and `manager-local-operations.json` bind the exact
released 0.1.6 wheel and a fresh isolated virtual environment. All 13 installed
production Python members match the wheel. PYTHONPATH and PYTHONHOME were
removed; manager imports came from that environment's site-packages.
`installed-local.json` in the preparation directory checks all 106 native
members plus the canonical manifest: **107 exact installed files**.

`URI_CHECKS_LOCAL.json` and `entry-asset-local-operations.json` establish nine
actual manager resolutions with native-source byte equality. The installed
materializer checked its fixed archive, extracted all 191 source files into a
separate ignored workspace and verified that pristine tree. The proof-reader
checker reproduced the installed eleven-member proof payload, including eight
exact sources and its historical report. The manager's final verification
remained valid after these operations. No new Lean proof or browser session ran.

The [asset inventory](../source-preparation-001/assets.json) seals exactly the
canonical 3.0.3 manifest and released manager wheel plus their two generated
checksum sidecars. [PUBLIC_NOTES.md](PUBLIC_NOTES.md) is separate publication
metadata with absolute immutable-source/download links and concrete manager
commands; it does not modify the frozen native release note.

Runtime environments, installed stores and materialized workspaces are ignored.
Portable commands/results, source/native records, assets and evidence remain
visible for the main carrier checkpoint. The sole historical failed-log EOF
whitespace exception remains as recorded in [PREPARED.md](../../PREPARED.md).

The owner authorized completion after the required checks. The Executive must
consume the exact guarded atomic plan before the Writer performs publication.
GitHub staging/publication, all four fresh downloads and exact public-manager
reacquisition follow; shared installation and consumer adoption remain outside
this release operation.
