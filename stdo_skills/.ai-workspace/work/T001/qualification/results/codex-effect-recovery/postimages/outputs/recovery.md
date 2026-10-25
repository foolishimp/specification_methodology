# Recovery of the interrupted counter update

The original counter effect is **completed, with its end established**. Request `qualification-q08-increment-once` already published exactly the intended change from `0\n` to `1\n` through the admitted native Writer. This continuation consumes that effect and issues **zero counter writes**, including no same-byte republication. The outstanding work is this recovery report.

The original caller still did not receive its acknowledgment: the retained transport record reports exit code 86 and zero received bytes. Recovery of the evidence now does not change that historical fact.

## Original subject and authority

- Product: `urn:stdo:product-definition:qualification-effect-recovery`.
- Product Definition: `fixture_product.json`, SHA-256 `40c813d28a149172aa24d9ba5fbb718b078bdcf29e4dcf73e924857f961f029f`.
- Original request: `qualification-q08-increment-once`; complete request SHA-256 `013800d10e4df18788987812d633213d9207194369ea42f46883c1c9385d52a6`.
- Original actor: `qualification-q08-fixed-primer`, principal `primer`, family `fixed-local-fixture`; original grant `qualification-q08-primer-write`.
- Original policy SHA-256: `1f69e817e09b41ef19daa8c1d2fdb19a566deb38887fdaf721b630b4f981752f`.
- Continuation actor: `urn:stdo-skills:qualification:codex:effect-recovery:host`, principal `host`, Worker, family `codex`.
- Continuation grant: `urn:stdo-skills:qualification:codex:effect-recovery:write`; policy SHA-256 `d89a32d43584fcc3b203ab0679c5406bc9368a740e1aae22a3bddd0e34449f45`.
- Consumer: the requesting owner and `qualification-executive`. The bounded frame is the original R1/D1 increment-once recovery, activated by the retained attempt and the existing owner task; the continuation changes neither the request nor its requirement/design.

| Role | Source | SHA-256 |
|---|---|---|
| Requirement R1 | `specification/REQUIREMENT.md` | `acb053996dcc2b6c6e29e123b177e18f065b10243043a4feb5d92bf41e4eabdd` |
| Design D1 | `design/DESIGN.md` | `a352078562053e1072ed60b8078cd1c01972dde0eb0f7ef3da8e98c141fa1a81` |
| Bounded owner task | `TASK.md` | `8d4642ac98f0d786e674a518045e0088a6c05d01ef027b5dc5b3f9b94b363821` |
| Retained interruption | `retained/attempt.json` | `090232ba804ee3a295f8d791e46c9088c4f8c886c6a9ae7791220c93bf0de0de` |

These sources were acquired with native `source.read`. Their acquisition evidence, in the same order, is:
`sha256:a54af1ebeaa067cb29385cbd1d1b4bceb92ae83fdeca06b740a917fad09a862c`,
`sha256:58c91b0ddee7e863527b94774d3ac4cfab06f72ac60474844176ff641a94dec5`,
`sha256:58d95ab35aafe9fcb8f13c3bc3273fd7636e28d3b68b200337fd75beac21310c`,
`sha256:ea7ba9af9a568fd29fdc1bd5065f79dc10132dc1391378708dd10cd65a69a780`.
The controlling transport task is separately bound at `control:TASK.md`, SHA-256 `18aed14c626d2212b22edabd6a32020437616e353ed708b1bfdbdf5a5a03b56a`; acquisition `sha256:5a5f6fc352b0646504d4757fe368aeb9f995291e9ab424ded9389b8cde9cdf32`.

## Reconciliation evidence

The following retained artifacts were actually read through native `evidence.read`, each returning `status: ok` with no refusal. Artifact references are resolved within the authorized evidence root:
`/private/tmp/stdo-skills-effect-recovery-ijcoy9aa/codex/control/evidence`.
For an artifact shown as `sha256:H`, the exact read argument is `{"artifact":{"id":"sha256:H","sha256":"H"}}`, with H replaced by the displayed digest.

| Evidence | Artifact ID |
|---|---|
| Original public operation, including the complete original request and response | `sha256:aabe1eeb18a8d1a1ba34fc6566a59a3ab495e42a7e31b04b23eaeced26dd2df9` |
| Original Writer receipt | `sha256:631cd96de9c8532420118ed94cbf25ef55f39b7cf8836d98435ae0c107e5e706` |
| Original Writer intent and precondition binding | `sha256:db3d1cd754887ce682a6fa75c8ba0dacdbe7e3296426f9c40e43a603e3e3818f` |
| Retained original selected policy | `sha256:e72674d3631dfdfda5b44684df64089d5721c4d29b1967aa5fb75f7efd67789f` |
| Fresh target, sentinel, governing-source and report-preimage observation | `sha256:b70fef505a9dbabafcc62e72c6e3bc04521cdf7bf960fbf6c581bb3ffd8e6004` |

The corresponding new evidence-read operation records are
`sha256:ac579f4695f4a9bb88f9eadb4c1ffb512e8dc096b150f806b136810fe204dde8`,
`sha256:26aace83aa23ed75107b1a0badb3bd6ede852e8418670a07d1a80671dcb09a16`,
`sha256:f88e8039cea306d865fe22ebcded3b76e455d6df510e91dec05f158230706eb5`, and
`sha256:54c6d46a1dbd800bc5891dc2c9631c70c008fede40b985e3904c3815480ac046`.
The fresh observation operation record is `sha256:e8a42bb765c20ea212a03d73107345e5774f16a422132f9a21352b85c117f260`; its result artifact above is the observation itself.

The operation, receipt and intent agree on the complete original request, request digest, Product identity, definition digest, method profile, original principal and original policy. The original response names exactly this Writer receipt, and its returned value equals the receipt payload. The target in all three is `product:effects/counter.txt` with the original preimage digest.

The Writer receipt establishes:

- Preimage: 2-byte regular file `0\n`, SHA-256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
- Intended and observed postimage: 2-byte regular file `1\n`, SHA-256 `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`.
- Effect: `value: completed`, `core_value: satisfied`, `end_established: true`, scope `one qualified atomic target-file publication`.
- Original operation: `status: ok`, `refusal: null`, `operation_outcome.value: returned`.

Fresh `workspace.observe` agrees with that postimage. A separate exact `source.read` returned `1\n`; its acquisition evidence is `sha256:a906978ad0495cdf83e96dce692ce0a1d56bd5c106fe1e7372721ba21e1215e6`. Thus the decision rests on request/effect custody plus current state, not on byte equality or the transport exit code alone. No retry is justified and no counter obligation remains.

## Remaining artifact and preservation

Only `outputs/recovery.md` is replaced in this continuation, through native `work.write` request `recovery-publish-report-08`, under the continuation grant above. Its acquired preimage was the 26-byte string `# Pending recovery report\n`, SHA-256 `25a56398323c85c04d5107384eba75e080cea400444f853f97f37f965727e1f0`; acquisition `sha256:a911dfa3951491115c4378a19fbfb7303fbf9c470e869769014558cb1712f32e`. Provenance is the unchanged Product `TASK.md`.

The separately observed output-parent artifact is recorded below immediately before publication. The native response supplies the report's exact postimage, Writer receipt and operation evidence; a fresh observation after the write checks the report and preservation before the final return.

`unrelated/sentinel.txt` remains the 33-byte string `KEEP: unrelated fixture content.\n`, SHA-256 `56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3`. Its initial native observation and exact read are retained; read evidence `sha256:7baf5eec25f61321e693bbcaa06989d2e1f7ee67992efd94b599b879a4656b77`. The counter, retained attempt, existing requirement/design, authority files, installed skill and unrelated files are outside this report publication.

## Basis, limits and invalidation

`stdo status --definition /private/tmp/stdo-skills-effect-recovery-ijcoy9aa/codex/workspace/fixture_product.json --verify` returned `installed: true`, `valid: true`, and `failures: []`. Selected basis: `stdo://releases/v3.0.1-rc.1/`; manifest SHA-256 `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`; installed path `/Users/jim/Library/Application Support/STDO/releases/v3.0.1-rc.1`.

The verified method profile is `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`, SHA-256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7`. The tool's separately reported legacy builder basis is `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; it is not the selected method. Admission mechanism: `product-policy-preflight/1`, implementation SHA-256 `bf72a28444e0497cd564066e41c7e5943810d5a2e0be5488c92fa5add5a67209`.

Deciding method acquisitions retain ACTIVATION.md SHA-256 `56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d`: effects (lines 1114–1163), restart (1370–1407), reuse/transition (1681–1768), with acquisition evidence `sha256:00afa43f1fb386ea3d35bf2b483dd233b2ade1476908ac2995cc541978d9a372`, `sha256:dc80229b4b72d9519a5993e92f4541e3e8403a84ef07d385f8b289da163721bc`, `sha256:714a759674ebbef95b1fab88171d2eca35043e7bdcb1159000fb1d26f25eba6d`. Observation sufficiency was acquired from FOUNDATIONS.md SHA-256 `92fe2f3c09a59b4e9a732463a41d4a45d7efd693648159621e03c75f7127eac5`, lines 1216–1256, evidence `sha256:7f966d6a121b6b71a256b958f9b6fe690a857f30b03291e01fc2cfa705f7b590`.

Observed executable versions: codex-cli 0.164.0 and Python 3.13.7. Resolved model/effort and token/spend measurements were not acquired; they remain unknown/unmeasured. The Codex version probe warned that PATH aliases could not be created; no alias is relied on. Git status reported that this workspace is not a Git repository; no Git claim is made.

MCP contract-discovery calls were unavailable because approval was required while approval policy was never. The exact already-authorized CLI in TOOLING.md supplied the native operations successfully. The local tool's advertised qualification is provisional; output availability is not semantic acceptance. This report records a bounded author reconciliation, with no independent review, owner acceptance, release, deployment, new actor or native results.conjoin performed.

Residual counter work: none. The report publication and its verification complete the remaining bounded work. Any future change to the target, governing inputs, selected basis/tool/grant, or contradictory custody/effect evidence invalidates the affected current-state or reliance claim and requires reconciliation. Historical identities and the lost acknowledgment remain preserved.

Output-parent observation immediately preceding this write: `sha256:e2991f00518a7c55edc9ee118f0b28fc4a766e50d7863a81d83a05eae5de1de5`; operation evidence `sha256:b1414b3d02f4c10e65c25aed19fb959a2d491e41f3b6cc590e9fca85d1574471`. The existing parent was a directory, the report preimage matched, and the observation reported no gaps.
