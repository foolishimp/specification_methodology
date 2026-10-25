# STDO 3.0.0 RC1 publication presentation correction

The owner previously stated that every published cut is a proper release. The
Executive selects the same metadata presentation correction already applied to
3.0.1, now for this original 3.0.0 publication. This is a metadata-only GitHub
release edit; no native source, tag, selector, branch, payload or asset is changed.
The current 3.0.2 release work and all frozen method/Skills subjects are unchanged.

## Actual before record

Read-only command: `gh api repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.0.0-rc.1`.
The exact returned API bytes are [before.json](before.json), SHA256 `dfe8d9a0a2ad08881dd9bebe6f50a365ccfad5ee3fbabc7cc5d1730db3923675`.
Release ID: `418547214`. Public URL: https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology/v3.0.0-rc.1.
Original title: `STDO v3.0.0 RC1 — standalone test candidate`; `draft = false`;
`prerelease = true`.
The decoded original body is preserved verbatim as the suffix of
[notes.md](notes.md), after the clearly separated publication clarification and
historical-notes heading. Original body UTF-8 SHA256: `74d2bf18de5e9cf91f19a1242c93b9153fc73139edd41a045201b51e294a6932`.
Prepared notes SHA256: `775cbf9e9b445f085a16207eac2f72881fe5d9a22de1bfab265aefe248c891c5`.

## Selected metadata patch

- Title: `STDO 3.0.0 RC1`.
- `prerelease`: `false`; `draft` remains `false`.
- `make_latest`: `false`; the selected new 3.0.2 release becomes Latest instead.
- Body: exact `notes.md` bytes. No asset upload, removal or replacement.

Only the separately bound Git Writer performs the remote patch. It should target
release ID `418547214`, verify the expected original title/prerelease/body and
asset identities before mutation, and retain the returned response. A changed
subject requires reconciliation rather than overwriting newly authored notes.
Afterward, verify title, normal published classification, exact notes body, unchanged
release ID/tag/asset identity set and unchanged direct tag objects/peels below.
Do not infer semantic acceptance from this metadata correction or from the RC suffix.

## Observed refs and asset identities

Read-only ref command: `git --no-optional-locks ls-remote --tags https://github.com/foolishimp/specification_methodology.git refs/tags/specification_methodology/v3.0.0-rc.1 refs/tags/specification_methodology/v3.0.0-rc.1^{} refs/tags/specification_methodology/v3.0.0 refs/tags/specification_methodology/v3.0.0^{}`.

```json
{
  "refs/tags/specification_methodology/v3.0.0": "8054d00ed22a6e9433ef13b3e4b0d6ae7a68ec58",
  "refs/tags/specification_methodology/v3.0.0-rc.1": "dde3e5f70d36f95369f88cc3b4130c6909678326",
  "refs/tags/specification_methodology/v3.0.0-rc.1^{}": "0a04feb788c080183b58cf4a162e88372be1d87e",
  "refs/tags/specification_methodology/v3.0.0^{}": "0a04feb788c080183b58cf4a162e88372be1d87e"
}
```

Asset identity set from the same actual API record (API digests are retained as
reported; null is not a computed content digest). Download counters are excluded
because they are observations, not asset identities.

```json
[
  {
    "id": 659674426,
    "node_id": "RA_kwDOR7M92c4nUdU6",
    "name": "a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz",
    "label": "",
    "content_type": "application/x-gtar",
    "size": 10089542,
    "digest": "sha256:989c0efbbba90c1d444c6a1c24def4174ef8519bec5f63d9bef021f27dd75e2b",
    "created_at": "2026-10-20T15:17:14Z",
    "updated_at": "2026-10-20T15:17:26Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz"
  },
  {
    "id": 659674446,
    "node_id": "RA_kwDOR7M92c4nUdVO",
    "name": "a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256",
    "label": "",
    "content_type": "application/octet-stream",
    "size": 114,
    "digest": "sha256:39c3d997f3a75f38b9599cf970ba962df76a3d42ee0beb8825e7e4527a9bcb76",
    "created_at": "2026-10-20T15:17:15Z",
    "updated_at": "2026-10-20T15:17:15Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824-packaging-r1.tar.gz.sha256"
  },
  {
    "id": 659674434,
    "node_id": "RA_kwDOR7M92c4nUdVC",
    "name": "a_c-stdo-v3-common-35fb4824.tar.gz",
    "label": "",
    "content_type": "application/x-gtar",
    "size": 10087425,
    "digest": "sha256:2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386",
    "created_at": "2026-10-20T15:17:15Z",
    "updated_at": "2026-10-20T15:17:26Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824.tar.gz"
  },
  {
    "id": 659674521,
    "node_id": "RA_kwDOR7M92c4nUdWZ",
    "name": "a_c-stdo-v3-common-35fb4824.tar.gz.sha256",
    "label": "",
    "content_type": "application/octet-stream",
    "size": 101,
    "digest": "sha256:404a13688fb014fdd83483f2bd33c8b8d35cb3347ff98dd682f37887d6cf0bb5",
    "created_at": "2026-10-20T15:17:17Z",
    "updated_at": "2026-10-20T15:17:17Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/a_c-stdo-v3-common-35fb4824.tar.gz.sha256"
  },
  {
    "id": 659674450,
    "node_id": "RA_kwDOR7M92c4nUdVS",
    "name": "stdo-v3.0.0-rc.1-manifest.json",
    "label": "",
    "content_type": "application/json",
    "size": 13478,
    "digest": "sha256:069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232",
    "created_at": "2026-10-20T15:17:15Z",
    "updated_at": "2026-10-20T15:17:15Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/stdo-v3.0.0-rc.1-manifest.json"
  },
  {
    "id": 659674438,
    "node_id": "RA_kwDOR7M92c4nUdVG",
    "name": "stdo-v3.0.0-rc.1-manifest.json.sha256",
    "label": "",
    "content_type": "application/octet-stream",
    "size": 97,
    "digest": "sha256:22d6b0ecafb0ca1789df87b477d0c0c31d46d2114df83a18de273fcd0acaf849",
    "created_at": "2026-10-20T15:17:15Z",
    "updated_at": "2026-10-20T15:17:15Z",
    "browser_download_url": "https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology/v3.0.0-rc.1/stdo-v3.0.0-rc.1-manifest.json.sha256"
  }
]
```

Publication/after-state verification is not yet performed by this preparation.
