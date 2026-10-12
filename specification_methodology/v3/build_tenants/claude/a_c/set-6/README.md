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
frame is over its 10,000-byte target. It is still a partial encoding. The
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
| `axiomatic-program.json` | `64aa7d208a456511c38356386d6ffb5569bb6e282c192ff7d23b14a3a9d3cff7` | the authored a_c.text program `urn:stdo-3:claude:program:a-c-text:set-6`; canonical program digest `sha256:9aa2e6521fa1a0fcf0262270b3838ef9c5b1064e0f4edb3fed0c1a3ab1537cbb` |
| `logical-constraint-map.json` | `286ea76502567944c8856a5242fc29244a2c4b7b20b4230c595942b10c9ed538` | deterministic index over the program; intrinsic digest `sha256:9dfd22266042132d0cf4b0ed4d23a8ccc3164a0049e4db437d320a981983e98d` |
| `validation-report.json` | `7a63ffab697e39e06e4ffd53e02e22cceb3a159e8622fd186820984f2bba56cc` | status `valid`, 0 diagnostics; 302 symbols, 422 clauses, 6 residuals; 216 resolved sources |
| `projection-frame-declaration-and-activation-materialized.json` | `31484102c53bc81acbef49c56fe83d9345f125988c0ac966b244916670421f41` | frame `frame-declaration-and-activation`, materialized; projection digest `sha256:7267b522591519444d94eb97258523aeae61c61dfda17fce32bbfe9c807fde36` |
| `projection-frame-declaration-and-activation-reference-only.json` | `3cfa7cc208b89d35a5a83488f4c57164aba5f4935c3368b7142617d6f406de5b` | frame `frame-declaration-and-activation`, reference-only; projection digest `sha256:4352758ba341de7323d0b9ed3c9a06f29c30071ac16235662d3db0e4337ba54c` |
| `projection-coverage-and-revision-materialized.json` | `f4f054c94232e6bbbef50bcc1fd0fcf279c1ae7525ca9a156d4aecec65e1db4c` | frame `coverage-and-revision`, materialized; projection digest `sha256:462369156d9660c54bb434a0cc0c8707c04c6d6c2bb5f6e7ccb3ab588730c5ed` |
| `projection-coverage-and-revision-reference-only.json` | `abaf2f6762d4976eddb08170bc12095192075fcec8a6a7c12e68d1f12d1c7f43` | frame `coverage-and-revision`, reference-only; projection digest `sha256:25b1171d6498b7be374a9d5174d546e084a4bf1f5311fd596bab09c70a0d12cc` |
| `projection-transformation-and-judgment-materialized.json` | `b9ad330161ef4fbd6bcaede8c08ae323af1f050b5a849f3b9c81ea14215bb986` | frame `transformation-and-judgment`, materialized; projection digest `sha256:869d9143b8d9c08f1cc48ee4390af223c2bf6333cce9c89af2668c5979758624` |
| `projection-transformation-and-judgment-reference-only.json` | `f9bb0930e8badfb85b5d34f720c949df56432a7f5b846a411204af354b59b464` | frame `transformation-and-judgment`, reference-only; projection digest `sha256:fec4554e7dcf8e3f4c5654e185e803a4f4cb3b632c4abeafd86c97dc6921569d` |
| `projection-triage-and-reentry-materialized.json` | `66e2d166b558b34215e6dd84c4fac7cde1f9d1bb3687ea0b00ea5c3b636a0e4c` | frame `triage-and-reentry`, materialized; projection digest `sha256:bebcfafefafb3ab078472b545dae1fd06bdfa7498853bc439fc78bb617851019` |
| `projection-triage-and-reentry-reference-only.json` | `31136187008c477b03d812c0fa952e759b1b2ccdca8f06ea30c3f1973a13b77c` | frame `triage-and-reentry`, reference-only; projection digest `sha256:6e4e40a698821794a1e4405d65e2407efeb48a18e5451189468d3c4a3ad9bb81` |
| `projection-carrier-and-admission-materialized.json` | `87fc5b9ff9577c3e1afe8d267ce2dc6762460d26cc73c934fa294e089d4b8649` | frame `carrier-and-admission`, materialized; projection digest `sha256:17a5a9bfefb167392675c2163776736da26a9b88c055de3f48697150b16a58a1` |
| `projection-carrier-and-admission-reference-only.json` | `0d7fc4f89f23b0d0a8e97237aedbaa2aa56a4b2274d621d9b8c1efbd392c8092` | frame `carrier-and-admission`, reference-only; projection digest `sha256:16b847e5cba77cf10110300459c2824be757704d2ce45be59d7125dd6f7b74dd` |
| `projection-executive-disposition-materialized.json` | `3a90354277797377bfba02a6fbc840863943aff01df59252fa91227bca698f22` | frame `executive-disposition`, materialized; projection digest `sha256:a4ece427bdaa9d4c0c402aaa78ecd03d07004f59a7ad81c9a77d51b1a1c6eca1` |
| `projection-executive-disposition-reference-only.json` | `b12f57e7e1cc4bac819d6ab58d63f374d379b2ca52f6c18e207fd98e88c9d1eb` | frame `executive-disposition`, reference-only; projection digest `sha256:aa7f6e754feb8c42262f5409d15095255d5d26f550b23f0dd3b1b33b11a6b2e7` |
| `projection-carrier-retention-materialized.json` | `ba23003706d64216c705938b9a85a664b0b062803baa1eeadc347533d8d3d1bb` | frame `carrier-retention`, materialized; projection digest `sha256:5c0b1f0c9b5801a3c15011281b7fc1f510687d38f6b2d40d6a62cb76c0e6d78c` |
| `projection-carrier-retention-reference-only.json` | `c890b0088ab6ae312e76d7d82eba0724b326002ce63a22c0101ada7883f144da` | frame `carrier-retention`, reference-only; projection digest `sha256:8d7a17fdbb85f18e5beaecc7b4a3b0f6cb8e0216d48adaa0be0a767072e65de2` |
| `projection-release-and-successor-materialized.json` | `312e66fde6a68f7d3382992ca8d14353c5dd735ba218c672c171dd56bc2c03bf` | frame `release-and-successor`, materialized; projection digest `sha256:5ecd0f325035fac4bd216b6f0f44cebcb46ec6ee00912a09b2dee3d6ec971704` |
| `projection-release-and-successor-reference-only.json` | `dffc6d7503842de1729785f9e0363c2a11bacde19933f5ddba9fcaf914939b77` | frame `release-and-successor`, reference-only; projection digest `sha256:e59a97c6543d55175e04d482b8ab46a133bfe96fe5c0e5bc1536cfbe695e27fd` |
| `projection-identity-scoped-materialized.json` | `d39d94f047a97b1da9255f66a7b85d27dca6afe61193c543d80d74a77b1bd9ee` | frame `identity-scoped`, materialized; projection digest `sha256:8cd69d62674a133d12111be3193d3e10a86277e69cc8a6d8bd6d2ef74bb5755d` |
| `projection-identity-scoped-reference-only.json` | `9d6c168b6a8476ec95b7ec63d50d77b08a29b3871b10aeaca77609ec4a274118` | frame `identity-scoped`, reference-only; projection digest `sha256:afb786f64a5e928d48869ae80363edb8267ba4d94c9a3ed8dc6beeb6a40dde88` |
| `projection-design-gate-materialized.json` | `a9f281366215a44b4309dc4ff4ef979715c54e4e419d11b386001c9a1830f919` | frame `design-gate`, materialized; projection digest `sha256:8f0b47ed86cf52fe8349e75bc853f0f13007ddab5b17c1aeebebc646246306dc` |
| `projection-design-gate-reference-only.json` | `40753ab72929e2de2bcdfc350e51168924aa39774243530b59ffd9b50a7035c9` | frame `design-gate`, reference-only; projection digest `sha256:00ab5306192a617cfaae094bd338424a6f98acd8107397922123d3b3e6d05d0b` |
| `projection-odd-closure-materialized.json` | `15a9992925613843b86b5e668982250faa4c26b5e5fe14f303177bf7a2c0f7a8` | frame `odd-closure`, materialized; projection digest `sha256:4db90d60c60feef781bff613192cf694b5c75ced474e8d171456a9b5edf89463` |
| `projection-odd-closure-reference-only.json` | `1bbaa4260d491313abd10bddb02b80ede6c917b1154b4ec42bc5246c0a487f28` | frame `odd-closure`, reference-only; projection digest `sha256:45316e61d4dcbacff529487824a1e868083c47372acb329ac2ea876750a62b17` |
| `projection-traversal-lineage-materialized.json` | `a3020d2ede2b390f996c4bd8db9b070266bfe1cad077f7b066e13c4a7e281057` | frame `traversal-lineage`, materialized; projection digest `sha256:962b8573b368659d5bc07cc4cdc986c733a19075aec89921e1679f103ce20d89` |
| `projection-traversal-lineage-reference-only.json` | `e4433b4c7994642c6fe735ab2dcc89be3d3712d5efcbb54698a6175f4d5a8a72` | frame `traversal-lineage`, reference-only; projection digest `sha256:7e70c6b79e1d1ebe75de2ccb289a8286931ca04661ecb5be8c55588a6329bbbd` |
| `projection-ux-replay-materialized.json` | `4a6afe9e69996ce1fbaad2aea3614555e6ef7f9ed61a5db7218b3e0a15a37816` | frame `ux-replay`, materialized; projection digest `sha256:f89db61ca7fd357771007e1d24a5d7901c4b3f85352b2c373b1809466e6566d3` |
| `projection-ux-replay-reference-only.json` | `a2d074c73f90f45f36758cee067ea06f2054598b1f36263e6f25ff9da8cf1e1e` | frame `ux-replay`, reference-only; projection digest `sha256:4104e4d6f656c3cf92976ff1938e9f374864b06d0a3e7bfcb5fef414a9d3f16b` |
| `projection-world-model-cut-materialized.json` | `1682ca9d88fd38f1167e70afec609bf9b5ef8e5e8632e7a9dfa2efafe6c6430c` | frame `world-model-cut`, materialized; projection digest `sha256:c44ce1440bf9f700f969cbed18e26a9db0d82f631829c61447a5af91f9915c93` |
| `projection-world-model-cut-reference-only.json` | `f5f69500063cbda082a9305af25f78a4cc8e135dd62f4dce9e76510d43ee0bc4` | frame `world-model-cut`, reference-only; projection digest `sha256:3d64262fc279d70cc04766878609a299e7a362e1aa6c957f75fd7498cd489acd` |
| `projection-bind-and-resolve-materialized.json` | `9d125ccc66ab161af07340ad1f19bb09f740bd921d0bdba05b734b8e58f04bc6` | frame `bind-and-resolve`, materialized; projection digest `sha256:7df22c9c79c6a4f1a328b59306c771ad45942acc398b0900f40d6cd4a2b715c7` |
| `projection-bind-and-resolve-reference-only.json` | `46bcecc10ad667cc4c2c299a2b57c5662f85bf066b9752455b22732be50f5a27` | frame `bind-and-resolve`, reference-only; projection digest `sha256:3d5f90d9ea880327bb3ab1d58ebbcb51aee11dbf3e9464f9eb7234efb0a2bde8` |
| `projection-bootstrap-materialized.json` | `d7830320595d58923d0f65094125d015c93de627a4e1334287afa6c18b2ca757` | frame `bootstrap`, materialized; projection digest `sha256:1b99cf5adce442651267c88372f984467c90d4d3504863f30acc4263f538b3ca` |
| `projection-bootstrap-reference-only.json` | `6889a95ca2f0c9f3b61509146d12d447dc4c600bf5d0690935830b8685dd18b3` | frame `bootstrap`, reference-only; projection digest `sha256:fad856ae0acf4f66e4f74cbd522fbc59d3e619964d018a2813e32deca2144571` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | byte-identical to set-5's |
| `FIDELITY.md` | | the W27 fidelity self-check over set-5 |

## Frames

Each frame was projected from its own frame index and measured with the
file size after projection, before any actor read it. The limit for the
fifteen task frames is 100,000 bytes materialized, met by selecting
clauses, never by truncating them.


| Frame | Task | Materialized bytes | SHA-256 (materialized file) | Reference-only bytes | Closure (symbols, clauses, residuals) | Under 100,000 |
|---|---|---|---|---|---|---|
| `frame-declaration-and-activation` | F-01 A | 94,689 | `31484102c53bc81acbef49c56fe83d9345f125988c0ac966b244916670421f41` | 47,566 | 38, 25, 2 | yes |
| `coverage-and-revision` | F-01 B | 94,166 | `f4f054c94232e6bbbef50bcc1fd0fcf279c1ae7525ca9a156d4aecec65e1db4c` | 48,117 | 33, 25, 0 | yes |
| `transformation-and-judgment` | F-02 A | 57,023 | `b9ad330161ef4fbd6bcaede8c08ae323af1f050b5a849f3b9c81ea14215bb986` | 29,680 | 16, 19, 0 | yes |
| `triage-and-reentry` | F-02 B | 68,419 | `66e2d166b558b34215e6dd84c4fac7cde1f9d1bb3687ea0b00ea5c3b636a0e4c` | 36,313 | 16, 21, 0 | yes |
| `carrier-and-admission` | F-02 C | 66,596 | `87fc5b9ff9577c3e1afe8d267ce2dc6762460d26cc73c934fa294e089d4b8649` | 35,046 | 20, 19, 2 | yes |
| `executive-disposition` | F-02 D | 94,970 | `3a90354277797377bfba02a6fbc840863943aff01df59252fa91227bca698f22` | 50,000 | 28, 24, 0 | yes |
| `carrier-retention` | F-03 A | 56,917 | `ba23003706d64216c705938b9a85a664b0b062803baa1eeadc347533d8d3d1bb` | 30,324 | 14, 17, 0 | yes |
| `release-and-successor` | F-03 B | 63,667 | `312e66fde6a68f7d3382992ca8d14353c5dd735ba218c672c171dd56bc2c03bf` | 34,244 | 14, 12, 0 | yes |
| `identity-scoped` | F-03 C | 38,689 | `d39d94f047a97b1da9255f66a7b85d27dca6afe61193c543d80d74a77b1bd9ee` | 21,003 | 11, 11, 0 | yes |
| `design-gate` | F-03 D | 83,896 | `a9f281366215a44b4309dc4ff4ef979715c54e4e419d11b386001c9a1830f919` | 43,398 | 24, 19, 2 | yes |
| `odd-closure` | F-03 E | 86,307 | `15a9992925613843b86b5e668982250faa4c26b5e5fe14f303177bf7a2c0f7a8` | 43,574 | 30, 24, 1 | yes |
| `traversal-lineage` | F-03 F | 67,499 | `a3020d2ede2b390f996c4bd8db9b070266bfe1cad077f7b066e13c4a7e281057` | 35,652 | 21, 15, 0 | yes |
| `ux-replay` | F-03 G | 46,356 | `4a6afe9e69996ce1fbaad2aea3614555e6ef7f9ed61a5db7218b3e0a15a37816` | 24,994 | 12, 11, 0 | yes |
| `world-model-cut` | F-03 H | 40,333 | `1682ca9d88fd38f1167e70afec609bf9b5ef8e5e8632e7a9dfa2efafe6c6430c` | 21,954 | 10, 10, 0 | yes |
| `bind-and-resolve` | F-03 I | 54,126 | `9d125ccc66ab161af07340ad1f19bb09f740bd921d0bdba05b734b8e58f04bc6` | 28,928 | 10, 11, 0 | yes |
| `bootstrap` | none | 31,045 | `d7830320595d58923d0f65094125d015c93de627a4e1334287afa6c18b2ca757` | 17,852 | 2, 9, 0 | yes |

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

- `frame-declaration-and-activation` (task A), 13 roots, 25 clauses in
  closure: minimal-frame-declaration-sections, minimal-activation-binding-shape,
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
  frame-object and authority-kind rows, RF-001 to RF-004, RF-006 to RF-008
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
nine clauses, each literal made of member sentences (the route rows
abridged to their member references), two symbols and no residuals:
bootstrap-discovery, bootstrap-select-exactly-one-definition,
bootstrap-basis, bootstrap-sync-and-adopt, bootstrap-entrypoint-and-targets,
bootstrap-routes, bootstrap-staleness-binding,
bootstrap-standalone-scope-and-prompt-construction and
bootstrap-executive-attention.

Size: 31,045 bytes materialized, 17,593 reference-only, against the
10,000-byte target, which it misses. A materialized frame carries each
literal twice (in `clauses` and `clause_relations`) plus about 1.5 KB of
URIs and routes per clause, so nine claims stated in member sentences
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
| 5. resolve the declared bootstrap entrypoint against its named basis; load raw owning standards when the projection is insufficient or stale | yes | SPEC_METHOD section 4 Procedures and PRODUCT_DEFINITION section 4 (basis-qualified entrypoint); PRODUCT_DEFINITION section 11 Staleness binding; ACTIVATION section 2 Prompt construction; `bootstrap-entrypoint-and-targets`, `bootstrap-staleness-binding`, `bootstrap-standalone-scope-and-prompt-construction` |
| 6. reference-frame basis; direct versus Executive entry; smallest frontier; unknown applicability unresolved; a role grants no effects; Executive performs no mutation; event-driven attention | in part: event-driven attention as a clause; direct versus coordinated entry as a route only | EXECUTIVE_BASELINE section 6 Event-driven attention (`bootstrap-executive-attention`); README Routes to EXECUTIVE_BASELINE sections 3, 6, 12 and 16 (`bootstrap-routes`); not carried though stated: PRODUCT_DEFINITION section 7 (collective basis), EXECUTIVE_BASELINE's smallest dependency-ready activation set and no-mutation rule, ACTIVATION section 1 Applicability |
| 7. load WHAT, HOW and carriers only as required; a summary or prior result routes but never replaces source authority; the end-to-end interface frame | in part: route-not-override and standalone scope | PRODUCT_DEFINITION section 4 (`bootstrap-routes`), ACTIVATION section 2 Standalone scope; not carried: PRODUCT_DEFINITION section 8 loading, and no tenant locus was established for the end-to-end interface frame |
| 8. reuse computed facts, judgments and rulings by route; refresh on invalidation; closure by condition | in part: as a route only | README Routes "resume work" row to ACTIVATION sections 5 and 7 and TICKETS section 7 (`bootstrap-routes`) |
| derived guidance preserves permissions and conditions; a digest does not establish fidelity; retirement default | in part: the first two | PRODUCT_DEFINITION section 11 ("derived instructions preserve ... permissions ...", "A matching digest establishes identity, not fidelity or sufficiency"); `bootstrap-staleness-binding`; no tenant locus found for the retirement default |
| sync, adopt dry-run, plan digest; adopt the sole operation that changes a basis; selector alone never changes a consumer | in part: sync, dry-run and mutating adopt with the plan digest; the selector is not operative | PRODUCT_DEFINITION section 4 command boundaries (`bootstrap-sync-and-adopt`, `bootstrap-basis`); not carried because no member states it: adopt as the sole basis-changing operation; not carried though stated: the fleet aggregate plan digest (PRODUCT_DEFINITION section 4); the lagging-selector and downgrade refusals have no locus established in this pass |
| bootstrap targets relative to the source project; fleet confinement; marker spans | yes | PRODUCT_DEFINITION section 4 (`constitution.agent_bootstrap`); `bootstrap-entrypoint-and-targets` |

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
`scoped-identity-kind`, `coverage-ledger`), clauses 417 to 422 (106
corrected in place, 2 removed, 7 added), residuals 6 unchanged, frame
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
- Added: six bootstrap clauses (above) and
  `odd-graph-function-binding-declares-the-environment-contract`.
- Frame indexes: the two F-01 frames reselected (above), `odd-closure`
  one root added, `bootstrap` re-rooted on nine clauses with its sources.

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
