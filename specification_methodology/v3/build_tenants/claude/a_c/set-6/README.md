# a_c interpretation of the twenty-three-member set (Claude tenant, set-6)

Status: the successor of [set-5/](../set-5/README.md), derived by the W27
Writer activation. It corrects every set-5 clause the fidelity pass in
[FIDELITY.md](FIDELITY.md) flagged, re-derives the bootstrap frame,
encodes the TRAVERSAL_OCCURRENCE mapping from the W28 correction and the
ACTIVATION section 3 indeterminate case from `9be9f57`, adds one
ODD clause a task needs, and projects sixteen frames: the fifteen task
frames of F-01, F-02 and F-03 and the bootstrap frame. The program
validates with zero diagnostics against the byte-verified pinned Axiom
Indexer. Every task frame is under the 100,000-byte limit; the bootstrap
frame, at 33,579 bytes, is over its 10,000-byte target. It is still a partial encoding. The
fidelity pass is a Writer self-check, not an author-independent judgment;
nothing here is accepted, and set-5/ is frozen history that this
derivation did not edit.

## Frozen subject

The twenty-three Markdown members under `standards/` at `9be9f57` on
`tenant/claude/c3-v3`. Twenty-one of them are byte-identical to
`4425993`, the commit the Executive froze for this round. Two changed
during this derivation, and the Executive directed this Writer to encode
their affected clauses last, from the newest commit: TRAVERSAL_OCCURRENCE
at `188bc81` (W28, "TRAVERSAL refusal mapping from the rc.2 constraint
table") and ACTIVATION at `9be9f57` ("ACTIVATION section 3: indeterminate
restated from rc.2 RF-012"). `git status --porcelain --
standards/` was empty before encoding and at each validation.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/ACTIVATION.md` | `eac7dbd7d9519dcd8cb5acfd9e153833a7375797f29e8a5d5a8129a6c65b2ec9` |
| `standards/ASSURANCE.md` | `6821ef04c1584dcdeb1bbe4dc62b07eb35807b856ced9c26f730ced27aed85e8` |
| `standards/AXIOMATIC_CALCULUS.md` | `fc2bda4d09c2f70c0d63bda6a3c6addb3d4119ea94e62c175fc1bd01ceb0391e` |
| `standards/CONFORMANCE.md` | `be1b88f98e24f3d9c655948191f5cd87d28e7941f0a4bb8028010004eef1dd05` |
| `standards/DESIGN_MODULE.md` | `d0edd09d71dc2033ff8f347614ebc109a545eeadc32b91463192dcb4980883dc` |
| `standards/EVALUATION.md` | `bea4a6372ebc7cf2ba7b6dcf42396d0a8f521a8abf48e8fc239dccfb32632375` |
| `standards/EXECUTIVE_BASELINE.md` | `478acc9c681b339384d7ae411190cea928fb323246f9eba590cf99893a344476` |
| `standards/FOUNDATIONS.md` | `b6ac5dadb2504cd0240fe9f7995c06077e68499864674e836e198a4ca4ecb2d2` |
| `standards/GLOSSARY.md` | `8eaf48056fe242a14efd2e9961968db9263d2c8e8bd3006460125796bcb9d182` |
| `standards/IDENTITY.md` | `03150e390768bf92d7bc66068ffad9ecfb3acce69e5188552316d2e049027f53` |
| `standards/ODD.md` | `630a48f4b0cf17e94c306f67d2392b29d42dcad07ea9963a01554496690910bc` |
| `standards/POSTING_GUIDE.md` | `e784c72ab18d3386d4aa28f9eed43aef675d01f1a03ec8ec2bcc440f33edfb86` |
| `standards/PRODUCT_DEFINITION.md` | `95f788b49f7fea128bf32bd6d47d6ef269ff1c67421d96b0a36f3710e46437b3` |
| `standards/PROFILES.md` | `506d353ec9252f2a567f9db159156a63b553a2b5cf716caaa354de48402fbb54` |
| `standards/README.md` | `79cb0f1c9ab9c54edcfb5e7bc344ca9af6507b412274e39f1879258b6b9fa6a4` |
| `standards/REFERENCE_FRAME.md` | `ef9a6a62d2b949a448d8c6bdd0c28bae7c33548fa2febf12e50f39cbb99f9495` |
| `standards/RELEASE.md` | `3d442f9eaffb4019447892ff9e46862eb63ebd312da2e4baa26e42a5fba8a886` |
| `standards/SPEC_METHOD.md` | `993b93376deaf519198ac0c7410738fa5ddfe8718501386c4196012102cf56ef` |
| `standards/TICKETS.md` | `9f6821e3ee43976ec986e9381f84483462a54d65d5517b0c8ef742ba3f6ade81` |
| `standards/TRAVERSAL_OCCURRENCE.md` | `79f758457cd552e6a2374386e52a005b2eb619d2d711c7c720933305433ce14a` |
| `standards/UX.md` | `095840e5bb99c4b1c32b2cdd94e1d7cbdcaef6b3799bc280435112619b29b978` |
| `standards/WORLD_MODEL.md` | `41760ae07fcd91df6fa3683ea64a267e3266e9ad6e9db502a28c1401ed2da9fa` |
| `standards/WRITING_GUIDE.md` | `d4c647a8d7ce59521069d1d311f2fa59f86cdc79bb01dd919a8f9bf57aba6106` |
<!-- /subject -->

## Mechanical subject

Unchanged from set-5: tag `refs/tags/axiom_indexer/v2.5.1-rc.2` (tag
object `9bff233c…`, commit `9a9c4797…`), `axiom_indexer/build_tenants/core/code/ac.py`
read from that tag with `git show`, SHA-256
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`,
invoked from a scratch copy with `python3 -I`. `calculus_ref` stays
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `858009be137170f4a6bd8e9932bc4134d3f9a04050c723a6353c3e61e61fad97` | the authored a_c.text program `urn:stdo-3:claude:program:a-c-text:set-6`; canonical program digest `sha256:d8a1d086508c96036641f13d21e6f1e923d2a65de56d1a8c3814983e5c1bbc83` |
| `logical-constraint-map.json` | `09257fc7f72710939400a579e7ded87fe98238e852bb34f7a12517623b632e5b` | deterministic index over the program; intrinsic digest `sha256:4789fee708a5f10f598c54d81c07a8e58ecda27b086e2ca10f2ed3c1cc2ad697` |
| `validation-report.json` | `8ed4247e35c61c1d55dd37b92b2a3bfaadc17cdab788ecc78abba5624f10396d` | status `valid`, 0 diagnostics; 302 symbols, 423 clauses, 6 residuals; 216 resolved sources |
| `projection-frame-declaration-and-activation-materialized.json` | `f4a8fb6bbf617dde7a1f7b3ec5794906124ebc90098e6644f4b577076e858a80` | frame `frame-declaration-and-activation`, materialized; projection digest `sha256:e91920bd2032ebdb37769f51c74143282eaa3f9d093bd96fe2b1da3fd67bd7be` |
| `projection-frame-declaration-and-activation-reference-only.json` | `dca49c522d4a16e70a3b18c2bb66ec0b70bbfe5a0f76139438e0cc639ce4cc5a` | frame `frame-declaration-and-activation`, reference-only; projection digest `sha256:735603423420fbe840e6747f82f2fba84cffc773a385fe9761980c6a3d7ac3a2` |
| `projection-coverage-and-revision-materialized.json` | `1ccc9c8663a51bc613fd22571808fc1bc791dc58f1475335fbc952198656d0bb` | frame `coverage-and-revision`, materialized; projection digest `sha256:644d64546a38ea5aae1a8f31febd76e3221da7bda5b7930e2f5d29440b7688e2` |
| `projection-coverage-and-revision-reference-only.json` | `fe87582613d0a596c570e477ec88b858b10f74f63da046c3f7ae0f179784e3eb` | frame `coverage-and-revision`, reference-only; projection digest `sha256:ebdf086dcd4ca6386654f84319d604613f99555d75249c8b779b6975801c9b40` |
| `projection-transformation-and-judgment-materialized.json` | `03417731c067d63cd91b9febee09db43aed88551711d47ea230071e35af3dacf` | frame `transformation-and-judgment`, materialized; projection digest `sha256:dc83e175b2b32010e39593439c993ea72228665ac471a8a167ac4ec007301e00` |
| `projection-transformation-and-judgment-reference-only.json` | `82090c8b8f4c203c16b4307ff6e99e5fea9b24b63f22d8269296a565a7a3971f` | frame `transformation-and-judgment`, reference-only; projection digest `sha256:09f061cb86f42239db9d5a54ed252ee5a18fac2035e3f1409e66d1ff042bad40` |
| `projection-triage-and-reentry-materialized.json` | `5d79b49b7530739444ee6fab451b8cc0377592223298cfb5cebf40afb1a84619` | frame `triage-and-reentry`, materialized; projection digest `sha256:54d9078f39597e243db93ffc8d8c962bc0cf8e495409ae4559b38fe63b5e4c7f` |
| `projection-triage-and-reentry-reference-only.json` | `7cace69b1374a6baaa2669ba920516e37fe08a6e14ab0443e26d6ff96ad81643` | frame `triage-and-reentry`, reference-only; projection digest `sha256:8d515068e7f308e1338e3ddaa8cd2645409104a31634cb5e44a8f4215be4cd95` |
| `projection-carrier-and-admission-materialized.json` | `764e0e3a88775ed32ebdf8d4ec2555659a1473ec62f208a60fccd771b2add7f9` | frame `carrier-and-admission`, materialized; projection digest `sha256:d0daa90bec6faf086a43fa8ecbf9040d80ebb455f4d603f89eb253c213a45084` |
| `projection-carrier-and-admission-reference-only.json` | `5583c78baefc2545bd27bec400e35ff3dddc5b3786da22721c77de44d82722d4` | frame `carrier-and-admission`, reference-only; projection digest `sha256:ce81ec06cd20be31b9284ca481096ea37c0c80074850e685989d9848e0b6069a` |
| `projection-executive-disposition-materialized.json` | `4dc07e6693b96177ab2899362bf5b0b1667b1be8875df7d2a9b90357988c1dc2` | frame `executive-disposition`, materialized; projection digest `sha256:445d78d480a988a1e5a619e164ab9be563f88718015f690df845f34c3619a51f` |
| `projection-executive-disposition-reference-only.json` | `503329f8f8f2261998822ab53a99f39e027afdd49b7d4c07a395c88df3c85612` | frame `executive-disposition`, reference-only; projection digest `sha256:e4295dfaba0e57d4cebeaac29fb0451efe0c79fc9e9e7bf0e08c521a02d0a288` |
| `projection-carrier-retention-materialized.json` | `f5143057f1165f4bce9e26abf5e14fe6cf56d76d9cbb8546587e501c3c924252` | frame `carrier-retention`, materialized; projection digest `sha256:bea3c9057e10bffe9e76e0eeaad336ecb71d388b5132f12cf5eec39b14e1cafe` |
| `projection-carrier-retention-reference-only.json` | `99d9bc85f656e0f70c33cf37fdb829b889c9499a1497b36cffd2e21c427c017f` | frame `carrier-retention`, reference-only; projection digest `sha256:62e870a6d6df94bb206c8bb180bec54703100a77cbb1056a38b2b8dd18b72c51` |
| `projection-release-and-successor-materialized.json` | `af39df59999a78c2bfd9d298b5fdc45859a7c4550c945e3f5c560d076e9e4313` | frame `release-and-successor`, materialized; projection digest `sha256:a02be452b3d2395199a0b247336c0cc9adb5ff8b5909bb56c48ffbe4e93f48d5` |
| `projection-release-and-successor-reference-only.json` | `52254b0b20ad97f4f26ad0fc5c44156c81cf28309bac98bf35d7646b88a06b0f` | frame `release-and-successor`, reference-only; projection digest `sha256:c28dc7c9b45452de55e4d9a0cfe3a27c09962b1da32fc2e34b5f51cbb49cf0da` |
| `projection-identity-scoped-materialized.json` | `527e964a5bb8244c70e5ef3c40e0e13ce50d601cb4feb2560a1613fc0e4a63b6` | frame `identity-scoped`, materialized; projection digest `sha256:eb5db7a5b30dbdcbe549c387a0bd68173bee0d1919198d945ab7de96a91c3326` |
| `projection-identity-scoped-reference-only.json` | `92914caafef4b4aff60bb6f1823a5f9390b05e1f504648490593a52ca5b3be99` | frame `identity-scoped`, reference-only; projection digest `sha256:76465799a6667f30615c145139cf262e1ba91bcd5c300326f36ce312b8b8a399` |
| `projection-design-gate-materialized.json` | `1597668f08b330a18abc2edc9919a6f5389fce71fb5308379f5b8cfb54a0b9a2` | frame `design-gate`, materialized; projection digest `sha256:50cdb695497f62a4edf720086d8beb3abd3c1c3745b1048bb62eaeffee6ebf59` |
| `projection-design-gate-reference-only.json` | `a245798fd011aae5fa7aae6568493178ee36391a76a51508efba00dade90e4e7` | frame `design-gate`, reference-only; projection digest `sha256:cbe47dc230f10c15ddc1dba063de8ae4558213ad96fc8c8d2c0d6ab01564612c` |
| `projection-odd-closure-materialized.json` | `6469ff43ecf78cd825b7181dda34b9fe72f7c08644d64ae249a84f02f78bd81d` | frame `odd-closure`, materialized; projection digest `sha256:79f6e7f793631ee22c933ef29a47aa96289d1cf6857f0c7869e21d609f2b7fa6` |
| `projection-odd-closure-reference-only.json` | `aa2d3a36948ff378396b5dd9387603327d17be648a517cb8f03fabe76aa1d25d` | frame `odd-closure`, reference-only; projection digest `sha256:c83c2447e62fa33b747d53ad2625da8b085fe41c0cebf6477537e4bde9da6a77` |
| `projection-traversal-lineage-materialized.json` | `55c8a9ee1ddcfbd29db99b2e70fb4e0d75498a7e513ed58da505239dfd696cd9` | frame `traversal-lineage`, materialized; projection digest `sha256:7b22e62a95ce60ba0afc190488f0a5477395ac3202812dbd3f7afcffe8724fff` |
| `projection-traversal-lineage-reference-only.json` | `87a5348592a9f7613a0e11a6a2c8869144131b4aaf83579cec711ad68d9a8c03` | frame `traversal-lineage`, reference-only; projection digest `sha256:48761ee1ed0cb77578d112a00221f00dae9aad9b269250846794d12725c1f12d` |
| `projection-ux-replay-materialized.json` | `a187d82fb7c8ed98a377c489c1d7d86e8c70e3aecad97f4c3407fee22a57c512` | frame `ux-replay`, materialized; projection digest `sha256:91171a2b4ffaf8a5d54beb1ce66b40984815b165a4fc6bd3f57a9bd913ca4420` |
| `projection-ux-replay-reference-only.json` | `b5ec58a8f00ef4dfc17922ee415e2da3cb7b6483da5e734a8310c338a4848485` | frame `ux-replay`, reference-only; projection digest `sha256:9ea813d6775b861db6bdb59451bcbdf10056dc0778fe49263f9cc2ff106c242f` |
| `projection-world-model-cut-materialized.json` | `a36d998a6de19985e7d617be9ec62fdef3d71fbf1c0f1a5598d56a62034741e6` | frame `world-model-cut`, materialized; projection digest `sha256:27c8133aacd582f6754b3675f4b8d8af6bc758722ea8c26064254a12664304be` |
| `projection-world-model-cut-reference-only.json` | `371006b876b5fcc0b8ece69fb30056b62e58ebc733c39f3155fc7b58c8cdc1da` | frame `world-model-cut`, reference-only; projection digest `sha256:171664e44d7a5683e773b8970107f9c19a08479e2769822af48283c465472150` |
| `projection-bind-and-resolve-materialized.json` | `90e1819c22d763f6d4bc9ab98d19361f92ead6929653f34ce7b425ffb5bb6193` | frame `bind-and-resolve`, materialized; projection digest `sha256:9f84131b33e906b5bdf84a7ab939b4fcdba413376d1cb1e8393ab4bb68741f0a` |
| `projection-bind-and-resolve-reference-only.json` | `afb23888fb018e941a95663b4ba8f9cae318ccb7b3cae7e2aad8ce9f18205666` | frame `bind-and-resolve`, reference-only; projection digest `sha256:d3e71f82de359c11a447acd3192c267c2d163221a0e875472236fa3430c8a202` |
| `projection-bootstrap-materialized.json` | `ab2bc8c57852efe56ef758b974f64609e37a73526bf169ccec3480b02cce5433` | frame `bootstrap`, materialized; projection digest `sha256:cfc3f9e9aead8f3b08dcbc155d47564950507b00e18b5efc1a7c8d3dc7ef72f1` |
| `projection-bootstrap-reference-only.json` | `c2e5e18314a08a79f12397b76ec77a4d0e675435e36562516e184594ac2889c5` | frame `bootstrap`, reference-only; projection digest `sha256:b13b24199c7edb1a76a6f0dd365ed07bf73f4835ddb9e80fbf28de2782c586ab` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | byte-identical to set-5's |
| `FIDELITY.md` | | the W27 fidelity self-check over set-5 |

## Frames

Each frame was projected from its own frame index and measured with the
file size after projection, before any actor read it. The limit for the
fifteen task frames is 100,000 bytes materialized, met by selecting
clauses, never by truncating them.


| Frame | Task | Materialized bytes | SHA-256 (materialized file) | Reference-only bytes | Closure (symbols, clauses, residuals) | Under 100,000 |
|---|---|---|---|---|---|---|
| `frame-declaration-and-activation` | F-01 A | 98,438 | `f4a8fb6bbf617dde7a1f7b3ec5794906124ebc90098e6644f4b577076e858a80` | 49,546 | 38, 27, 2 | yes |
| `coverage-and-revision` | F-01 B | 94,166 | `1ccc9c8663a51bc613fd22571808fc1bc791dc58f1475335fbc952198656d0bb` | 48,117 | 33, 25, 0 | yes |
| `transformation-and-judgment` | F-02 A | 57,023 | `03417731c067d63cd91b9febee09db43aed88551711d47ea230071e35af3dacf` | 29,680 | 16, 19, 0 | yes |
| `triage-and-reentry` | F-02 B | 68,419 | `5d79b49b7530739444ee6fab451b8cc0377592223298cfb5cebf40afb1a84619` | 36,313 | 16, 21, 0 | yes |
| `carrier-and-admission` | F-02 C | 66,596 | `764e0e3a88775ed32ebdf8d4ec2555659a1473ec62f208a60fccd771b2add7f9` | 35,046 | 20, 19, 2 | yes |
| `executive-disposition` | F-02 D | 94,970 | `4dc07e6693b96177ab2899362bf5b0b1667b1be8875df7d2a9b90357988c1dc2` | 50,000 | 28, 24, 0 | yes |
| `carrier-retention` | F-03 A | 56,917 | `f5143057f1165f4bce9e26abf5e14fe6cf56d76d9cbb8546587e501c3c924252` | 30,324 | 14, 17, 0 | yes |
| `release-and-successor` | F-03 B | 63,667 | `af39df59999a78c2bfd9d298b5fdc45859a7c4550c945e3f5c560d076e9e4313` | 34,244 | 14, 12, 0 | yes |
| `identity-scoped` | F-03 C | 38,689 | `527e964a5bb8244c70e5ef3c40e0e13ce50d601cb4feb2560a1613fc0e4a63b6` | 21,003 | 11, 11, 0 | yes |
| `design-gate` | F-03 D | 83,896 | `1597668f08b330a18abc2edc9919a6f5389fce71fb5308379f5b8cfb54a0b9a2` | 43,398 | 24, 19, 2 | yes |
| `odd-closure` | F-03 E | 86,307 | `6469ff43ecf78cd825b7181dda34b9fe72f7c08644d64ae249a84f02f78bd81d` | 43,574 | 30, 24, 1 | yes |
| `traversal-lineage` | F-03 F | 67,499 | `55c8a9ee1ddcfbd29db99b2e70fb4e0d75498a7e513ed58da505239dfd696cd9` | 35,652 | 21, 15, 0 | yes |
| `ux-replay` | F-03 G | 46,356 | `a187d82fb7c8ed98a377c489c1d7d86e8c70e3aecad97f4c3407fee22a57c512` | 24,994 | 12, 11, 0 | yes |
| `world-model-cut` | F-03 H | 40,333 | `a36d998a6de19985e7d617be9ec62fdef3d71fbf1c0f1a5598d56a62034741e6` | 21,954 | 10, 10, 0 | yes |
| `bind-and-resolve` | F-03 I | 54,126 | `90e1819c22d763f6d4bc9ab98d19361f92ead6929653f34ce7b425ffb5bb6193` | 28,928 | 10, 11, 0 | yes |
| `bootstrap` | none | 33,579 | `ab2bc8c57852efe56ef758b974f64609e37a73526bf169ccec3480b02cce5433` | 18,801 | 2, 10, 0 | yes |

F-02 and F-03 frames keep their set-4 and set-5 roots; their bytes and
closures moved only where corrected clauses changed length or support.
`odd-closure` gains `odd-graph-function-binding-declares-the-environment-contract`
(ODD section 5 Graph functions, binding of refinement, rewritten at W25):
F-03 task E asks whether a later graph function may obtain an earlier
output, and the member now answers through a declared adapter or
specialised contract, with ODD section 11.8 declared as that contract. Its support
references pull in `faithful-refinement-definition` (ACTIVATION section 4,
corrected here) and the P4a and result-algebra cluster, which takes the
frame from 47,936 to 86,307 bytes. `world-model-cut` carries the new WORLD_MODEL
section 14 row (inconclusive verification maps to indeterminate) through the
corrected `world-model-verdicts-map-to-core`. `traversal-lineage` carries
the W28 mapping (below).

### F-01 frames reselected

The F-01 frames had 59 and 47 roots and measured 271,966 and 223,594 bytes
from set-3. Set-6 keeps the frame names and selects roots against the
F-01 task instructions only (no expectations were read):

- `frame-declaration-and-activation` (task A), 14 roots, 27 clauses in
  closure: minimal-frame-declaration-sections, basis-is-immutable-or-moving-with-declared-detection (task A's subject moves reads to a replica), minimal-activation-binding-shape,
  minimal-evaluation-result-fields, result-algebra-has-five-members,
  indeterminate-result-names-the-deciding-evidence, nothing-is-coerced-to-success,
  rf-012-every-evaluation-returns-an-algebra-member,
  activation-binds-the-declaration-and-loads-the-packet,
  rf-005-every-result-binds-exact-basis-and-coordinates,
  frame-is-bound-when-every-coordinate-resolves,
  closed-result-identifies-its-coordinates,
  evaluator-applies-the-frame-and-records-assumptions; support pulls in
  activation-packet-minimum-contents, frame-tuple-specifies-the-relation,
  missing-capability-is-out-of-frame (the three cases of ACTIVATION section 3)
  and the FOUNDATIONS principle and premise rows. Left out as roots, of the
  relations the F-01 claim names: out-of-frame-result-names-the-missing-declaration
  and unexercised-declared-capability-yields-no-evaluation-result (ACTIVATION
  section 3; the cases themselves stay in by support), intake-names-its-fields and
  intake-is-sufficient-without-history (ACTIVATION section 1 intake),
  step-is-the-activation-of-one-frame, context-fit-is-measured-before-read
  and fit-test-against-envelope (ACTIVATION section 2), the FOUNDATIONS section 2
  frame-object and authority-kind rows (the basis row is kept), RF-001 to RF-004, RF-006 to RF-008
  and RF-013 to RF-016, frame-violations-enumerated and
  frame-qualification-asks-nine-tests. The last root cut was
  out-of-frame-result-names-the-missing-declaration, at 103,936 bytes.
- `coverage-and-revision` (task B), 19 roots, 25 clauses in closure:
  coverage-ledger-fields, coverage-statuses-are-seven,
  coverage-is-relative-to-its-tuple, diagnostic-order-is-eight-questions-in-order,
  question-one-is-answered-by-family-inclusion, revision-actions-enumerated,
  revision-reopens-every-result-bound-to-the-prior-revision,
  material-revision-changes-identity-and-names-reevaluation,
  missing-frame-signals-enumerated, decision-rule-states-its-terms,
  mandatory-unresolved-result-survives-aggregate-green,
  authority-coverage-closes-only-with-owners-named,
  inventory-is-derived-from-every-material-source-with-provenance,
  artifact-presence-proves-no-coverage, frame-set-declaration-records-its-fields,
  uncovered-coverage-is-r-minus-c, failure-and-uncovered-obligation-survive-join,
  rf-011-topology-mutation-forces-reevaluation-before-reuse,
  coverage-stays-falsifiable-and-challengeable. Left out: frame relations
  (REFERENCE_FRAME section 7), frame-set selection and operational full
  coverage, coverage dimensions, interaction, failure and high-risk
  coverage, the completeness boundary row on undiscovered evaluations,
  method functions, the minimal frame-set declaration, method
  self-qualification, RF-003, RF-009, RF-015, RF-017, and the FOUNDATIONS
  authority-kind and independence rows.

## Bootstrap

`bootstrap` (frame ref PRODUCT_DEFINITION `#12-bootstrap`) is not a task
frame. Set-5's three clauses are replaced: `bootstrap-basis` said "only
adopt, given the exact plan digest, changes it", which no member states
(PRODUCT_DEFINITION section 4 bounds what mutating `adopt` changes, and the
explicit complete consumer update also changes a consumer's basis);
`bootstrap-discovery` omitted the definition-selection rule; and
`bootstrap-routes` stitched three README rows into one order. Set-6 has
ten clauses, each literal made of member sentences (the route rows
abridged to their member references), two symbols and no residuals:
bootstrap-discovery, bootstrap-select-exactly-one-definition,
bootstrap-basis, bootstrap-sync-and-adopt, bootstrap-entrypoint,
bootstrap-agent-targets,
bootstrap-routes, bootstrap-staleness-binding,
bootstrap-standalone-scope-and-prompt-construction and
bootstrap-executive-attention.

The Writer wrote these clauses itself, so after the reviewers finished it
put them through the same rubric with a sentence-boundary check: a first
version spliced the SPEC_METHOD bootstrapping sentence onto
PRODUCT_DEFINITION text, stopped the marker-span sentence before its
byte-preservation rule and dropped qualifiers from four statements. Those
are fixed (FIDELITY.md, "Self-check").

Size: 33,579 bytes materialized, 18,801 reference-only, against the
10,000-byte target, which it misses. A materialized frame carries each
literal twice (in `clauses` and `clause_relations`) plus about 1.5 KB of
URIs and routes per clause, so ten claims stated in member sentences
cannot meet 10,000 bytes. Set-5 met 9,571 bytes with three clauses whose
literals were the Writer's compression, which is where the unfaithful
"only adopt" claim came from. Meeting the target means carrying fewer
claims or relaxing verbatim literals; that choice is not this Writer's.

Coverage of rc.2 `standards/authority_compressions/stdo_bootstrap.md`
claim by claim (same split as set-5; loci at `188bc81`):

| rc.2 bootstrap claim | Carried | Tenant locus |
|---|---|---|
| 1. discover `stdo_<label>.json` recursively; prune list; refuse symlinked definitions; nesting creates no inheritance or composition | yes | PRODUCT_DEFINITION section 9 (recursive discovery, nesting) and section 4 (prune list, stated for recursive fleet discovery; symlink); `bootstrap-discovery` |
| 2. select exactly one applicable definition; zero or multiple unresolved fail closed | yes | PRODUCT_DEFINITION section 9 (added by `8f5276b`); `bootstrap-select-exactly-one-definition` |
| 3. basis URI and manifest digest are the sole operative selection; source and selector are discovery inputs only | yes | PRODUCT_DEFINITION section 4 ("sole authored STDO selection", "Neither is operative authority"); `bootstrap-basis` |
| 4. sync and verify through the manager; no mutable source, other cut, alias, cache or proximity copy | in part: sync, cache, registry, source checkout, version alias, schema or agent file, proximity; "another installed cut" and the mutable authoring source are not in the clause | PRODUCT_DEFINITION section 4 and section 12; `bootstrap-basis`, `bootstrap-sync-and-adopt`; the mutable source rule is PRODUCT_DEFINITION section 12, not carried |
| 5. resolve the declared bootstrap entrypoint against its named basis; load raw owning standards when the projection is insufficient or stale | yes | SPEC_METHOD section 4 Procedures and PRODUCT_DEFINITION section 4 (basis-qualified entrypoint); PRODUCT_DEFINITION section 11 Staleness binding; ACTIVATION section 2 Prompt construction; `bootstrap-entrypoint`, `bootstrap-agent-targets`, `bootstrap-staleness-binding`, `bootstrap-standalone-scope-and-prompt-construction` |
| 6. reference-frame basis; direct versus Executive entry; smallest frontier; unknown applicability unresolved; a role grants no effects; Executive performs no mutation; event-driven attention | in part: event-driven attention as a clause; direct versus coordinated entry as a route only | EXECUTIVE_BASELINE section 6 Event-driven attention (`bootstrap-executive-attention`); README Routes to EXECUTIVE_BASELINE sections 3, 6, 12 and 16 (`bootstrap-routes`); not carried though stated: PRODUCT_DEFINITION section 7 (collective basis), EXECUTIVE_BASELINE's smallest dependency-ready activation set and no-mutation rule, ACTIVATION section 1 Applicability |
| 7. load WHAT, HOW and carriers only as required; a summary or prior result routes but never replaces source authority; the end-to-end interface frame | in part: route-not-override and standalone scope | PRODUCT_DEFINITION section 4 (`bootstrap-routes`), ACTIVATION section 2 Standalone scope; not carried: PRODUCT_DEFINITION section 8 loading, and no tenant locus was established for the end-to-end interface frame |
| 8. reuse computed facts, judgments and rulings by route; refresh on invalidation; closure by condition | in part: as a route only | README Routes "resume work" row to ACTIVATION sections 5 and 7 and TICKETS section 7 (`bootstrap-routes`) |
| derived guidance preserves permissions and conditions; a digest does not establish fidelity; retirement default | in part: the first two | PRODUCT_DEFINITION section 11 ("derived instructions preserve ... permissions ...", "A matching digest establishes identity, not fidelity or sufficiency"); `bootstrap-staleness-binding`; no tenant locus found for the retirement default |
| sync, adopt dry-run, plan digest; adopt the sole operation that changes a basis; selector alone never changes a consumer | in part: sync, dry-run and mutating adopt with the plan digest; the selector is not operative | PRODUCT_DEFINITION section 4 command boundaries (`bootstrap-sync-and-adopt`, `bootstrap-basis`); not carried because no member states it: adopt as the sole basis-changing operation; not carried though stated: the fleet aggregate plan digest (PRODUCT_DEFINITION section 4); the lagging-selector and downgrade refusals have no locus established in this pass |
| bootstrap targets relative to the source project; fleet confinement; marker spans | yes | PRODUCT_DEFINITION section 4 (`constitution.agent_bootstrap`, including the marker-span byte rule); `bootstrap-agent-targets` |

The four rules the Executive named are carried: definition selection and
exactly one applicable definition (claim 2), the staleness binding of
derived surfaces (PRODUCT_DEFINITION section 11) and prompt-construction
routing (ACTIVATION section 2). Nothing in the frame states that adopt alone
changes a basis.

## TRAVERSAL

`traversal-stops-and-decisions-map-to-core` and
`structural-refusal-and-partial-effect-losses` were encoded last, from
TRAVERSAL_OCCURRENCE at `188bc81` (`git log -1` on that file at encoding
time). Both set-5 clauses were already stale at `4425993`: `partial_effect`
and `partial` had become falsified or indeterminate by the effect
evidence. W28 then changed refusal: a refusal maps to falsified, including a
structural refusal and the refusal closing the `unresolved_scope`
re-entry, and to invalid_basis only when it carries
`refuse_invalid_basis` or is emitted with an `invalid_basis` decision.
The set-5 clauses mapped a structural refusal to invalid_basis.

## ACTIVATION section 3

`missing-capability-is-out-of-frame` (ACTIVATION `#3-result-algebra`) was
encoded last, from ACTIVATION at `9be9f57` (`git log -1` on that file at
encoding time). The member now states indeterminate "when the available
admissible evidence cannot decide the claim" (rc.2 RF-012), without the
earlier precondition that every required relation and capability be
declared and exercised, and adds that where the claim also depends on an
undeclared relation or capability, out_of_frame and indeterminate each
have a lawful ground and the result names the member it returns and that
ground. The clause carries both. The other ACTIVATION section 3 clauses
were checked for the removed precondition by search; none other carried
it. `traversal-stops-and-decisions-map-to-core` still says, for stop
`hold`, that every required relation and capability is declared and
exercised, because TRAVERSAL_OCCURRENCE's own row says so.

## Changes between set-5 and set-6

Counts: symbols 301 to 302 (one added: `derived-surface`; five labels
rewritten: `bootstrap-route`, `formal-fragment`, `minimal-evaluation-result`,
`scoped-identity-kind`, `coverage-ledger`), clauses 417 to 423 (106
corrected in place, 2 removed, 8 added), residuals 6 unchanged, frame
indexes 21 unchanged. The program URI is
`urn:stdo-3:claude:program:a-c-text:set-6`.

- Corrected in place: the 106 clauses in FIDELITY.md, each to its member
  sentences. Three of them also gained a source anchor where a literal
  sentence sits under a different heading.
- Removed: `conservation-is-semantic` and
  `successor-disposes-every-predecessor-claim` (SPEC_METHOD section 6 no
  longer states them; it points to RELEASE section 9, which
  `release-successor-disposes-every-predecessor-claim` encodes). No frame
  index or support reference cited them.
- Added: seven bootstrap clauses (above) and
  `odd-graph-function-binding-declares-the-environment-contract`.
- Frame indexes: the two F-01 frames reselected (above), `odd-closure`
  one root added, `bootstrap` re-rooted on ten clauses with its sources.

Newly conserved member text not encoded, because no task needs it: the
DESIGN_MODULE preference for one algebraic primitive and its prompt
sentence, the GLOSSARY index watch (named in the staleness clause only by
its effect), the SPEC_METHOD neutral-examples and closure sentences, the
TICKETS insufficient-frame and review-findings sentences, the UX prompt
sentence, the ODD F_P-recipe and general-method-surface sentences, and
the FOUNDATIONS formal fragment beyond the corrected clause.

## What validation proves

Validation proves structure, URI resolution, reference closure, the
grounding of every anchor in a heading of the resolved file, and the
canonical digest. It does not prove the clauses faithful, complete or
uniquely interpreted. FIDELITY.md is a Writer self-check; the
author-independent judgment has not been made.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in frame-declaration-and-activation coverage-and-revision \
    transformation-and-judgment triage-and-reentry carrier-and-admission \
    executive-disposition carrier-retention release-and-successor identity-scoped \
    design-gate odd-closure traversal-lineage ux-replay world-model-cut \
    bind-and-resolve bootstrap; do
  for M in materialized reference-only; do
    python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
      --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
      --mode $M --output projection-$FI-$M.json
  done
done
```

The derivation from set-5 was performed by uncommitted scratch scripts:
apply the reviewer corrections, merge the bootstrap, ODD and TRAVERSAL
fragments, set the frame roots, add the three source anchors and the
label rewrites, then validate and project. The program is the artefact;
this file and FIDELITY.md record every class of change.
