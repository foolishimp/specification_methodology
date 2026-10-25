# Deployment report: demo/v1.0.0-rc.1 into deploy-test

Date: 2026-10-25. Outcome: the exact selected retained release is installed in deploy-test and verified byte for byte. This is installation availability and author verification only. It is not owner acceptance, publication, or a new release cut.

## Governing basis

- Product Definition: fixture_product.json (sha256 7a4b9eb49b26f190f0e829070e87565130e1e9a279be6eb5c76e399bf323173e), pinning stdo://releases/v3.0.1-rc.1/ with manifest 60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8.
- Basis check: `stdo status --definition fixture_product.json --verify` returned installed=true, valid=true, failures=[], manifest_sha256 equal to the pin, 64 standards members.
- Requirement R1: specification/REQUIREMENT.md (sha256 27a0059a874367342962057444f66aeb84372613ef43988744a938064eadbf5d).
- Design D1: design/DESIGN.md (sha256 105a9d16d580a97f1e9d6ba7ac219118022bbf299ecd5a87e2c0af541faa4687).
- Grant: TASK.md (sha256 25dfdd5bca9988f67ddc6e649d0b8bc8869b2092c7bf0682ecab14222cd11963), scope grant urn:stdo-skills:qualification:claude:release-deploy-repair-2:write.
- Tool binding: TOOLING.md (sha256 8689777028002d48122ebc38b11e33b725151e073d2696b836f93eefcca8ac91); native a_c via stdo_ac MCP tools; policy sha256 4a09ceb02d9dfb25ab2ab4b0eb4512d03792abad7a8cb3374ea33e206973587f; method profile urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1 (sha256 a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7). Contract discovered with tools.describe (evidence sha256:619e750c538490a06b45b2616ea53d03346ded53c89c59c76ca98169d759585b).

## Selected release, reacquired natively (source.read, root `product`)

| Source | sha256 | bytes | acquisition evidence |
|---|---|---|---|
| retained/SOURCE.json | 7a34839974623e792f9cd5e9a887a1e8231d851ca96b0f71e0b2355f48716ced | 848 | sha256:0ac6542379e788894cffb62e280b467d61b1dd2896b4af53cdd529da393ae5c5 |
| retained/release/manifest.json | ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35 | 200 | sha256:9a2d2781653d77e06ca96d460fb936539ee409fc1ae6f9d5b67bcb9293ba832f |
| retained/release/payload.txt | b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2 | 25 | sha256:08f5d9fb20cc63b669a76cdffd048a3dc1367d914338706a524ff3c3cc18dff0 |

Identity confirmation:

- release_id is `demo/v1.0.0-rc.1` in both retained/SOURCE.json and retained/release/manifest.json. Not renamed.
- SOURCE.json original_manifest.sha256 equals the retained manifest sha256 (ce71758a...).
- SOURCE.json original_payload.sha256 equals manifest.payload.sha256 equals the retained payload sha256 (b31b59c9...).
- SOURCE.json prior_prepared (sha256 95e248c199cc439f3d1e10cc732ae74bc41999eb83aad0ea2fc23fb7ff3c2124) was not reacquired: its recorded path lies outside the product root and is not needed to confirm the deployed identities. Its currentness is therefore unknown here, not confirmed.

## Preimages (native workspace.observe baseline)

Baseline observation deploy-observe-baseline-1: artifact sha256:10a6d87db97098bfcd00398291bb24d7db3fdd3e8e674bfc43e7d75c11e71cc9, evidence sha256:331e148c78f4d581461359d031c0299c3501cb32795d3df143af592d82945b2c.

| Path | preimage sha256 | bytes |
|---|---|---|
| deploy-test/payload.txt | a1959b8fe0e3dbef5bf912f3cff5e3f73f56cb3f2efacfbbc016b0f046f4b1ae | 42 |
| deploy-test/manifest.json | ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356 | 3 |
| deploy-test/unrelated.txt | 77cd8d24e225d961d85580f1e0cd11da86b63c0c691d109d6974178a0b6bac94 | 35 |
| unrelated/sentinel.txt | 56686d9c77cc9592aee6e2e4514fe02a7f59daa3c0befced80b3980bc6cb51b3 | 33 |
| outputs/deployment.md | e4b998929134aea72cc864ae2597f31923ab688c82f2db0bc1120883eae36712 | 28 |

## Effects (native work.write, mode replace, grant urn:stdo-skills:qualification:claude:release-deploy-repair-2:write)

| Request id | Target | Pre-write observation artifact | preimage -> postimage sha256 | bytes | effect | effect evidence | writer artifact |
|---|---|---|---|---|---|---|---|
| deploy-write-payload-1 | deploy-test/payload.txt | sha256:ab274278ab5a3c2fe56f4f6101bd5867c917097ec6ad32c8e5422e1923f02380 | a1959b8f... -> b31b59c929fa045605276ea8b5492a408361288268539ae2b52c1586ba584da2 | 42 -> 25 | completed, end_established=true | sha256:995204894dc8c2ed8bda38608cd8dcd2075a8e50c478d932b5af57cfd7b1d5cc | sha256:f6a1548dd432e78a3d3d510273dfd9eeebec49437945a1be98144214009a3407 |
| deploy-write-manifest-1 | deploy-test/manifest.json | sha256:a36a649935f1ae4d1342ac65ef13f17ae6d07c0449b51db65fa2bc9bf325bdf5 | ca3d163b... -> ce71758abbf18193dfc3a2c588c228668e0b9065ed1b5e3cf96fb80a01acac35 | 3 -> 200 | completed, end_established=true | sha256:a4b809305881c243ff2da6fdfc33bf67e01615a2f5ade086a4f8fab82df928ba | sha256:0eff950d7dca566029c113db520d78601791007b89ee998b59cce26a78979b90 |
| deploy-write-report-1 | outputs/deployment.md (first version) | sha256:d57182c4faf39da36368b6cef13beacd8e2b749823ab8bfdce04f0062a7493b2 | e4b99892... -> 2c0f67774e29dc74783b3dfdf6a0037c994b401582df2aea99283fdfe9dadc96 | 28 -> 8730 | completed, end_established=true | sha256:fce7dd942d0b28f3e0a02b4cef814803b558e84a928ebed98fdc60d68b60a512 | sha256:a32844627803e1730e6b5bec4962dfe3cac2e3de6bfd8b877a05115893948ace |
| deploy-write-report-2 | outputs/deployment.md (this version) | sha256:0b637128b766b98d03541a7990799d92ca73f0b1ddfbe73b2ffaf103cf074160 | 2c0f6777... -> (postimage is in this write's receipt; not reproducible inside the file itself) | 8730 -> n/a | see receipt | see receipt | see receipt |

The two deploy writes used interpretation null and record provenance equal to the exact retained source file (retained/release/payload.txt, retained/release/manifest.json). The two report writes used record provenance retained/SOURCE.json and an authored interpretation whose author authority is TASK.md (sha256 25dfdd5b...). Each write observed its parent directory and target immediately before the effect. Write intervals (unix_ns): payload 1792900744798836000 to 1792900744799153000; manifest 1792900777692602000 to 1792900777694404000; report first version 1792900995329459000 to 1792900995329773000.

Report revision: deploy-write-report-2 supersedes deploy-write-report-1. The first version's effects header stated "interpretation null" for all writes, which was true only for the two deploy writes. This version corrects that statement and adds the first report write's receipt. No other content changed in substance.

## Verification of the installed result

1. Native diff against the baseline over the identical scope (deploy-observe-verify-1; artifact sha256:602c4080e37de71161727bc4193ec6c8fe8343f9a9edeb17663935b00e44d1a2; evidence sha256:513683dfb56308286334905155e64ea25c7a2cc464309550091a7b31c085f305): exactly two entries differ, deploy-test/manifest.json (ca3d163b... -> ce71758a..., 3 -> 200 bytes) and deploy-test/payload.txt (a1959b8f... -> b31b59c9..., 42 -> 25 bytes). deploy-test/unrelated.txt, unrelated/sentinel.txt and outputs/deployment.md (at that time) were unchanged. No gaps.
2. Native source.read of the installed files pinned to the retained hashes succeeded and returned content identical to the retained content: deploy-test/payload.txt b31b59c9... (evidence sha256:45f333dc864962e564b7bf54b4d6a69fc54a92ca931da1593097a43519d68844); deploy-test/manifest.json ce71758a... (evidence sha256:fafaf8b7e22baf8220c5c70035d50e1db46ea9713efe928beb4e44a8e06ef872).
3. Independent local read-only check: `cmp` of retained/release/payload.txt against deploy-test/payload.txt and of retained/release/manifest.json against deploy-test/manifest.json both exited 0 (identical). The installed manifest's payload.sha256 equals the installed payload's sha256; installed release_id is demo/v1.0.0-rc.1.
4. The first report version's on-disk sha256 (2c0f6777...) was checked locally and natively (deploy-observe-report-pre-2) against its write receipt postimage before this revision: equal.

R1 condition "payload.txt and manifest.json must equal retained/release byte for byte": satisfied on the observed paths above.

## Preserved and not touched

deploy-test/unrelated.txt, unrelated/sentinel.txt, retained/*, specification/*, design/*, fixture_product.json, TASK.md, TOOLING.md, CLAUDE.md, AGENTS.md, .claude/*, .qualification/*. No directory was created. No file was deleted or renamed. No scratch files were written; comparisons were done in memory or via native receipts.

## Refusals and anomalies retained

- deploy-observe-payload-pre-1 was refused: code basis_ambiguous, reason "Observation scopes differ" (evidence sha256:21401aab88443de0b3d51ed63856c9364efd47be874e1b342caa4161c18f2594). Cause: a `previous` diff basis was supplied with a narrower scope than the baseline. No effect occurred. Redone as deploy-observe-payload-pre-2 without `previous` (artifact sha256:ab274278...).
- tools.describe lists native results.conjoin as unsupported (operator unqualified). It was not selected or used.
- The report required a second write to correct one inaccurate statement (see Report revision above). Both writes are within the TASK.md grant for outputs/deployment.md.

## Limits

- Every a_c outcome carries the limit "output availability only; no semantic acceptance". The a_c inventory states its own qualification as provisional with independent integrated qualification and owner acceptance pending.
- Per D1 and TASK.md: installation availability and this author verification do not imply owner acceptance or remote publication. No remote publication, Git mutation, global configuration change, new actor, rename, or further stage was performed.
- The stdo basis was verified once at the start of this activation and not re-verified after the writes.
- Tenant-level directories named in fixture_product.json (.ai-workspace/tickets, sprints, comments) do not exist in this workspace; GOALS.md states no durable ticket is required inside this fixture, so none was created.
- Elapsed time and token or cost figures for this activation are unknown to the actor and are not stated.
