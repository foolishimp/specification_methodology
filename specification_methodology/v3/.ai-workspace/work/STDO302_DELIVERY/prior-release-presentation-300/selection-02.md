# STDO 3.0.0 RC1 presentation correction — successor 02

The Executive selected this literal publication-wording correction before the
Git Writer applies the metadata patch. It supersedes only the prepared body in
[selection.md](selection.md): use [notes-02.md](notes-02.md), not `notes.md`.
The original preparation, API record and first proposed body are unchanged.

The corrected body removes the original current-heading/opening misclassification
rather than displaying it beneath a clarification. It changes only the title,
publication classification language and the implication that an additional GA/final
cut might be needed. It retains the original identities, six assets, commands,
evidence descriptions, `not_ready`/unaccepted source status and all semantic and
actual-use qualification limits. The concise clarification links to the original
API bytes at immutable source commit `44448b14ecc9c5636d0e7972c7a4f1a80a07c623`.

## Exact content and metadata

- New body UTF-8 SHA256: `ee3c3bbb1ea0d6fac110f9b292c8c5285ed799030c681997376ba79fc8713e3e`.
- Original API bytes: `dfe8d9a0a2ad08881dd9bebe6f50a365ccfad5ee3fbabc7cc5d1730db3923675`.
- Original decoded body UTF-8 SHA256: `74d2bf18de5e9cf91f19a1242c93b9153fc73139edd41a045201b51e294a6932`.
- Original selection record SHA256: `bbf39f7d128fac5e4c49acfdec7482c6e819060fc3384fb76081887e5f1be200`.
- Original first notes proposal SHA256: `775cbf9e9b445f085a16207eac2f72881fe5d9a22de1bfab265aefe248c891c5`.
- Release ID `418547214`; exact tag `specification_methodology/v3.0.0-rc.1`.
- Title `STDO 3.0.0 RC1`; `draft:false`; `prerelease:false`; `make_latest:false`.

No tag, ref, payload or asset mutation is selected. Preserve the exact tag/selector
objects and peels and complete six-asset identity set in original `selection.md`.
That asset set's SHA256, using UTF-8 JSON with sorted keys, two-space indentation
and one final LF over its ordered array, is `c492ace8eea31e5b01f10d465db9e2aa6c3a22458915a87fb845bf71120bb4ba`.
Before patching, independently read the live release and compare the original
title, prerelease/body, ID/tag and asset identity preconditions; drift requires
reconciliation. After patching, verify the exact new body bytes/hash and metadata,
unchanged refs/assets and release ID. No remote effect has been performed by this
preparation. Existing 3.0.2 native proof and frozen source subjects are untouched.

## Complete literal body diff

```diff
--- before.json decoded body
+++ notes-02.md
@@ -1,8 +1,12 @@
-# STDO v3.0.0 RC1 — standalone test candidate
+# STDO 3.0.0 RC1
 
-STDO **v3.0.0-rc.1** is available here as a public standalone prerelease/test
-candidate. Install the exact method and supplied `spec` plugin payload from
-this repository:
+Publication clarification follows the owner's direction: an RC-labelled cut is a
+proper release; this presentation change supplies no new semantic acceptance or
+qualification. The [original API record](https://github.com/foolishimp/specification_methodology/blob/44448b14ecc9c5636d0e7972c7a4f1a80a07c623/specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/prior-release-presentation-300/before.json)
+is preserved with its original notes and qualification snapshot.
+
+STDO **v3.0.0-rc.1** is a proper published immutable standalone release.
+Install the exact method and supplied `spec` plugin payload from this repository:
 
 ```sh
 stdo install v3.0.0-rc.1 --repository https://github.com/foolishimp/specification_methodology.git --manifest-sha256 069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232
@@ -31,9 +35,9 @@
 
 The embedded release note describes the original private/local test and its
 qualification snapshot. This later public publication adds availability of
-that **unchanged exact cut**. It does not re-tag RC1, create a GA version,
-change the recorded qualification scope or turn the frozen source into an
-accepted method. Source checkpoint `35fb4824a064a84df5af214a0d0e2da597c18ac6` remains `not_ready` and
+that **unchanged exact cut**. The exact RC1 tag is preserved; no additional
+final cut is required. Publication does not change the recorded qualification
+scope or turn the frozen source into an accepted method. Source checkpoint `35fb4824a064a84df5af214a0d0e2da597c18ac6` remains `not_ready` and
 unaccepted; open source-review/owner decisions and whole-method/actual-use
 qualification are not closed by this publication. The governing builder was
 the installed STDO v2.5.1-rc.2.
```
