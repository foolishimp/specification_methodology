# STDO 3.0.2 public release proof

STDO 3.0.2 is publicly released as normal GitHub Latest. All selected PUBLIC-phase
checks have passed. This record precedes the final continuing-source status
bookkeeping; it does not alter the immutable native cut.

Public URL: https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.2

| Coordinate | Verified identity |
|---|---|
| Source A | `44448b14ecc9c5636d0e7972c7a4f1a80a07c623` |
| Published carrier B on main | `d89b69471082f006cec116879049735706d6da1e` |
| Native C and release branch | `23ca9c0929d7be8570edafaf30542e3daeb8dc1f` |
| Immutable annotated tag object T | `d03b00a7fdf8972dc236b52eb09f3eccba7f62cb` |
| Native manifest M | `f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477` |
| GitHub exact-tag and Latest release ID | `423535606` |
| Downloaded manager wheel | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |
| Downloaded supplement | `d402887043fde5c16e951eb7dcb8d9f44750c54b83df74bc68705338adf86139` |

`publication-plan.json`, `ATOMIC_PUSH.json` and `published-refs.json` bind the
checked atomic publication of main, the stable tag and release branch. The final
direct remote readback is `PUBLIC_FINAL_REFS.json`. No RC selector/branch was
created, and the native tag was never retargeted.

`github-publication/VERIFIED.json` binds the normal, non-draft, non-prerelease
release and its matching Latest endpoint. All six uploaded asset names, sizes
and server digests match the frozen inventory. The private draft initially returned
404 through the published-tag endpoint. Its retained creation response and
`COMMANDS-publication-recovery.json` show recovery through the release list/ID,
verification of that same sole draft and publication of that ID; no duplicate
release or upload was created. Exact API observations are retained.

`public-download-proof.json` establishes all six fresh downloads and sidecars.
`MANAGER_PUBLIC.json` proves a new isolated environment installed the downloaded
wheel, imports 0.1.6 from its own site-packages, and matches all 13 production Python
members to the wheel. The actual commands clear PYTHONPATH/PYTHONHOME. Public
HTTPS manifest acquisition reproduces M. `installed-public.json` and
`URI_CHECKS_PUBLIC.json` establish all 86 payload members plus manifest.json and
four concrete entry/bootstrap/schema/template URI matches. No global manager or
consumer basis was changed.

`PUBLIC_SUPPLEMENT.json` records safe extraction of the downloaded 24-member
archive and the extracted portable verifier run from a separate empty directory.
Both carriers recover the same reviewed JSON model values and same native
selection. Its 32-record coverage and semantic/whole-method limits remain intact.

`prior300-correction/VERIFIED.json` records the separately authorized metadata-only
correction: release 418547214 is STDO 3.0.0 RC1, normal published, with exact notes-02
body SHA256 `ee3c3bbb1ea0d6fac110f9b292c8c5285ed799030c681997376ba79fc8713e3e`.
All six original assets and eight 300/301 tag objects/peels remain unchanged;
3.0.1's body, metadata and two-asset identity set remain unchanged. The correction
occurred before 3.0.2 became Latest.

The Executive separately reported matching live API/Latest/server-asset and
remote-ref observations around 17:02 UTC. Those are Executive-reported observations,
not additional worker-authored probes. The retained worker receipts above stand
on their own actual operations. No broad test campaign or adoption was added.

PUBLIC_PROOF.json freezes these substantive observations and assets, preserving
all 195 members of the prior LOCAL_PROOF. Runtime machinery remains ignored.
The Git Writer stops for the Executive's final bounded readback before the
continuing-source status/bookkeeping commit.
