# Codex STDO 3.0.0 RC1 review bundle

[Download the corrected archive](corrected-bundle/CODEX_STDO_3_0_0_RC1_REVIEW_BUNDLE.tar.gz). The current candidate is `d1b33480b46f45bb46198a2f63ca197e84e40e55`. The [construction return](RETURN.md) records its repairs, evidence and remaining qualification; the [affected readback](AFFECTED_READBACK.md) found no supported remaining defect in the eight selected repair obligations.

SHA-256: `4cb4e442f6195859b53cceb728460bef22759f5aa3e662fa3eecfaaf90f3b4de`.

The archive contains 90 candidate members, 79 pinned dependency members and three acquisition/inventory files. Both plugin manifests identify the `3.0.0-rc.1` candidate target. Extract the archive and start at `codex-rc1-review/README.md`, then `candidate/README.md`. The wrapper explains the runtime prerequisite and exact binding/projection commands. Fresh extraction reproduced all 169 candidate/dependency files and ran the binding command successfully without network access; see [the reacquisition receipt](corrected-bundle/BUNDLE_REACQUISITION.json). Python 3.13 was exercised; runtime provisioning remains outside this bundle.

The complete candidate is ready for inspection. Member/replacement acceptance, complete semantic coverage, shared actual-use/context qualification, candidate selection and publication remain open. The [release preview](corrected-bundle/PREVIEW_RECEIPT.json) records the existing loader's selection of the promoted v3 root and its outstanding release-note and interpretation/cohort dependencies. The full historical and eighteen-projection sweeps were reused within their applicable scopes rather than rerun after these repairs.

The [earlier reviewed archive](CODEX_STDO_3_0_0_RC1_REVIEW_BUNDLE.tar.gz) remains preserved at package `ea27616b93c80b13ee15a9931cd9114275e5de13`, SHA-256 `2831aede7636163aeb1571b7a39e30cac0178dce26acd62cf5f3d1a30836c2d5`. SOURCE, DOMAIN and REPRESENTATION reviews apply to that earlier package; the affected readback applies to the corrected package above. Neither archive is an issued product release.
