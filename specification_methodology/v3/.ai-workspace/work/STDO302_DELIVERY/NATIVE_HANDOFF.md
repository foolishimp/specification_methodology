# STDO 3.0.2 native publication handoff

The owner has reaffirmed release of STDO 3.0.2 through the prescribed process,
including pushing remote. The release remains standalone and normal (not an RC,
draft or prerelease). This record supplies the Git Writer's concrete next effects;
it is not evidence that they have occurred.

Method02, bounded representation01 and native tools01 passed the independent
[source-first release subset review](../../comments/codex/20261025T160612Z_REVIEW_stdo302_release_subsets.md).
The review SHA256 is `8b6ab0d11e20e5c9ff3309a713aaf82bc56bed74589800f9ce650c0d2fb1019a`.
The later external review's High recipient-route finding and Medium fragment
findings were repaired independently of those unchanged method/representation
subjects. a_c05's independent review is
[the provider readback](../../comments/codex/20261025T161554Z_REVIEW_ac_composition_05.md),
SHA256 `21f3e7ff60be58f6460b4d8ab1e2f21e035ee2c1106372f45db9379d8b3c3be0`.
Manager and Skills05 final independent readback are now closed with no actionable
issues: [manager review](../../comments/codex/20261025T162632Z_REVIEW_stdo302_manager_final.md),
SHA256 `2a2b4ed5c123f9c59a9783a448073cb871ecc88fda96146a242411c81e5e192b`, and
[Skills05 review](../../comments/codex/20261025T162958Z_REVIEW_skills_composition_05_final.md),
SHA256 `968cd0928c61dc1b009a251a9ee4dd2070dc015cf6fc2cd014e0e01f24547c16`.
The Executive selects the reviewed integrated source for source A and native C.
Original04 evidence and the earlier closed reviews retain their historical subjects.
The active publication instructions below incorporate [PUBLICATION_SELECTION](PUBLICATION_SELECTION.md);
[the documentation successor record](native-documentation-02/CHANGE.json) preserves
the previous recipe/handoff and identifies this doc-only correction.

Exact current inputs:

| Subject | SHA256 |
|---|---|
| `method/METHOD-02.json` | `7c3928c6d31d08cee9d1d0da4a2f062bd191fa04c08925a551b80a4e98a3f1b9` |
| `REPRESENTATION-01.json` | `827ad7ec3b76b6416381f6415065817e85d425fb6819172110f58f66093e0b41` |
| `NATIVE_TOOLS-02.json` | Current documentation successor inventory; unchanged code inherits the NATIVE_TOOLS-01 review |
| `manager/CANDIDATE-repair1.json` | `e3c5302012ac9cfdc2413096976a9ba2ae49e408b0d01f47320edd21ae1fd50d` |
| a_c `source-freeze-05.json` | `25c6f674d003f4632a647cf7e385b936dae7e817e96a3e637d50af0cf252aef9` |
| a_c `provider-files-05.json` | `cd20f63cc21a953fc6aeb0b01dafc93aa2386df729a53c8ad430be0289028967` |
| Skills `COMPOSITION_01/CANDIDATE-05.json` | `9c153e0942e28900b53651c5fb875f5fb5639adc5610e11f16c03dba1a2ba7ee` |
| `manager/package-03/stdo_toolchain-0.1.6-py3-none-any.whl` | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |

The manager's final wheel passed 121 affected tests and two identical builds.
Skills05 uses the actual installed wheel under an isolated interpreter with
PYTHONPATH/PYTHONHOME removed, retains the actual module path/version and verifies
the selected edge plus a narrow-root refusal. Its six native provider calls passed
with the same Writer/history; unknown provenance remains unknown. Those are bounded
consumer observations, not new host qualification or constitutional adoption.

## Source A and native C — sole Git Writer

With the selected independent reviews closed, commit the integrated reviewed source as A.
Do not reuse checkpoint88305 as A: that is the pre-3.0.2 source. Then use these
commands with the actual full A SHA. All subsequent generated records are new.

```sh
set -euo pipefail
repo='/Users/jim/src/apps/specification_methodology'
delivery="$repo/specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY"
native_dir="$delivery/native-release"
native_tool="$native_dir/native_release.py"
native_run="$native_dir/release-run-01"
source_commit='<full reviewed source-A commit from the Git Writer>'
predecessor='fe4941f56a52ed3697a2b516d8d68948b0ea65d9'
python3 -I -S -B "$native_tool" prepare --repo "$repo" --run "$native_run" \
  --source-commit "$source_commit" --source-path specification_methodology/v3/build_tenants/common
source_sha256="$(python3 -c 'import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())' "$native_run/source.json")"
index_dir="$(mktemp -d "$native_run/git-index.XXXXXX")"
GIT_INDEX_FILE="$index_dir/index" git -C "$repo" read-tree --empty
GIT_INDEX_FILE="$index_dir/index" git -C "$repo" update-index -z --index-info < "$native_run/native-index-info.z"
native_tree="$(GIT_INDEX_FILE="$index_dir/index" git -C "$repo" write-tree)"
native_commit="$(git -C "$repo" commit-tree "$native_tree" -p "$predecessor" -F "$native_run/native-commit-message.txt")"
git -C "$repo" tag -a specification_methodology/v3.0.2 "$native_commit" -F "$native_run/tag-message.txt"
git -C "$repo" update-ref refs/heads/release/specification_methodology/3.0.2 "$native_commit" 0000000000000000000000000000000000000000
python3 -I -S -B "$native_tool" attest --repo "$repo" --run "$native_run" \
  --source-sha256 "$source_sha256" --native-commit "$native_commit"
```

The separate index leaves the checkout/index unchanged. The native tree has only
86 declared payload members under `specification_methodology/v3`; its sole parent
is the actual preceding native301 commit. The tag is create-only, annotated with
exact stable-v1 source trailers. No second selector or RC branch is created.

## Local installed evidence and assets

Use the exact wheel above. Create a fresh `release-run-01/manager-local` virtual
environment and record installation output, wheel hash, Python version and actual
imported manager file/digest. Run every manager command with
`env -u PYTHONPATH -u PYTHONHOME "$manager_python" -I -m stdo_toolchain.cli`.
The existing global manager remains unchanged. The complete command sequence is
in [native-release/README.md](native-release/README.md), using the emitted source
and native receipt digests rather than guessed values.

Expected actual output locations:

| Operation | New output under `native-release/release-run-01/` |
|---|---|
| prepare/attest | `source.json`, native Git input/messages, `native.json` |
| wheel install/import | `manager-local/`, retained wheel/import/installation evidence |
| manifest/seal | `manifest-report.json`, `SOURCE_SELECTION.json`, `stdo-v3.0.2-manifest.json`, checksum |
| local install/verify | `local-store/`, `install-local.json`, `verify-local.json`, `installed-local.json` |
| bounded supplement | `supplement-bundle/`, `stdo-v3.0.2-composition-release-supplement.tar.gz` |
| public-asset selection | `assets.json`, `asset-checksums/` |
| atomic plan/readback | `publication-plan.json`, `published-refs.json` |
| public download/install | new downloaded-assets and manager-public environment, `public-store/`, `public-download-proof.json`, `installed-public.json` |

The supplement builder refuses archive output inside its bundle. It verifies the
real sealed native identity and exact selected source against the bounded model;
its extracted verifier needs no originating workspace. Public claims use actual
native/install/download records, not the synthetic controls retained with the recipe.

## Carrier B and publication

After the exact native identity, local installed proof, supplement and assets are
sealed and assessed, checkpoint their carrier as B on main. B descends from A;
C stays the native payload commit. Run `publication-plan` with exact B and the
selection/assets digests. Only the Git Writer executes its returned atomic leased
push: main at B, immutable stable tag and release branch at C. Verify remote refs
with `published`, preserving every unrelated ref and all legacy RC selectors.

Publish the exact existing tag through GitHub using `--verify-tag`,
`--prerelease=false`, `--latest=true` and the complete selected asset paths.
Release completion requires all of the following actual observations:

1. The exact-tag API release is normal published: `draft:false`, `prerelease:false`,
   the intended tag and native target, and the complete selected asset identity set.
2. `repos/foolishimp/specification_methodology/releases/latest` returns that same
   release ID and `tag_name = "specification_methodology/v3.0.2"`, also not draft
   or prerelease. Latest changes discovery metadata, not consumer authority.
3. Every expected asset is downloaded afresh and passes the complete frozen
   inventory/checksum comparison; a missing or extra asset is not success.
4. The downloaded manager wheel is installed in another fresh isolated environment,
   its actual module/distribution identity is retained with PYTHONPATH cleared,
   and the exact native cut is installed from the public repository into a fresh
   store. The manifest/complete member verification and `installed --label public`
   proof both pass.

A push or release-create response alone establishes none of the remaining
predicates. Preserve the actual receipts and state any incomplete predicate
explicitly rather than calling the release process complete.

A final continuing-source record may follow publication; it cannot move the stable
tag. No Skills301 adoption, a_c profile migration, global installation or old-v2
cohort update follows from this sequence. The full earlier whole-method representation
remains incomplete; only the explicit bounded supplement accompanies this release.
