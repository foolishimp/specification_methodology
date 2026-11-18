# RC3 frozen identity assessment (identity-01)

**Verdict: satisfied.** The frozen identity and qualification record holds together and is enough for the authorized guarded publication gate. I found no material defects. I have four low-severity findings; none of them blocks publication. This is my own judgment, from the records listed below. I did not take the Writer's test counts as the result.

**Reviewer position.** I'm a read-only Claude reviewer, independent of the Codex construction. I am not independent of the earlier Claude-family architectural direction. I edited nothing and published nothing.

## Read limits
- **No tools run.** I ran no hashing, `git`, `ls-remote` or unzip, so every Git object, peel, tree and SHA-256 value here is a Writer observation. I checked that the values agree with each other across records and with the code that produced them, not that they are true.
- **What I read in full or in the relevant part:**
  - installed 3.0.4 `ACTIVATION.md` (only lines 1–772 of 1770);
  - installed `RELEASE.md` §2–§8;
  - RC3 `RELEASE.md`, the current corrective-cut clause of `RELEASE_3_1.md`, and the run's `ACTIVATION.md`;
  - `FREEZE`, `PREPUBLICATION.md`, `SOURCE_CARRIER`, `TAG_INTERNAL_READBACK`, `REF_PLAN`, `REF_PREPARE`, `NATIVE_BINDING`, `COHORT_DRAFT` and its embedded qualification, `PREPUBLICATION_QUALIFICATION`, `COHORT_INPUTS`;
  - the native manifest asset;
  - from the extracted Products: Skills `INVENTORY` and `DEPENDENCIES`, Purpose Context `SOURCE_RELATION`, Representation `PUBLIC_MANIFEST`;
  - semantic-03 `SUBJECTS` and `ASSESSMENT`; the verdict lines of native-01/02 and semantic-01/02;
  - `context/FINAL_RESULT`, plus the summary and host fields of `assessed-packaged`, `visual`, `manager-checks`, `PRODUCT_EXTRACTION_03`, `ref-tests-02`, and `tools/ref_transaction.py`.
- **Section labels.** The labels in your request for installed RELEASE §6/7/8 don't match the actual headings. The actual headings are §6 release-scoped assets and Product subject, §7 coordinated cohorts and the two-commit, one-transaction process, and §8 acceptance; project-qualified refs are §2. I applied the actual sections.

## What I checked
- **Freeze pins.** `FREEZE` pins carrier `be3d4221…` and native `b2e21ad0…`. The same pair appears in `SOURCE_CARRIER`, `TAG_INTERNAL_READBACK`, `PREPUBLICATION_QUALIFICATION` and the cohort's embedded qualification.
  - `REF_PREPARE.plan_sha256` equals the `FREEZE` hash of `REF_PLAN`.
  - The qualification `record_sha256` in the cohort equals the `FREEZE` hash.
  - The base is `2c95df2f`, the published RC2 post-publication commit, as `ACTIVATION.md` requires. It is the lease expected for remote `main`, and the code checks ancestry before preparing the plan.
- **Six Products.** Each has its own Product Definition built on construction basis `stdo://releases/v3.0.4/` with manifest `102817a3…`.
  - Native A: commit `b2e21ad0`, subtree `specification_methodology/v3`, tree `d7caf6e1`. That tree equals the frozen source tree at `d52f6df8:…/build_tenants/common`, matching the tag annotation and the requirements' native-subject clause.
  - The five companions are on B, each with its own subtree tree. The planned, readback and cohort trees agree for all six.
- **Native A before derived B.** Every derived Product pins native manifest `2b3a7391…`. That manifest records the local A tag object `61344ea9`, the commit, the root tree `1432a308` and the subtree, so B can only have been built after A existed. Tagger times also put A first (1794988082, then 1794989650).
- **Native manifest.** 1 license + 21 plugin + 1 release note + 72 standards = **95**, matching `NATIVE_BINDING.file_count`.
- **Companion archive.** 52 + 35 + 48 + 67 + 24 = **226**, matching `PRODUCT_EXTRACTION_03`. Archive `0975b055` is the same digest everywhere it appears.
- **Dependency pins.** All are exact and agree with each other:
  - Skills → Context `5a9ecd76` (distributed); Skills → visual `651e633d`.
  - Representation → visual `651e633d`, → Indexer `9eba50a3`, → native `2b3a7391`.
  - The Context and Skills native pins are `2b3a7391`.
- **Deliberate source→public changes.**
  - Purpose Context: exactly 1 of 50 members differs from source (`CATALOG.json`: source `8091fbf5` → distributed `3670a99f`, restricted to the two RC3 indexes). It also has its own public manifest; the source one is `c2bd656b`. Both values appear in `SOURCE_RELATION` and the cohort.
  - Skills: exactly one declared change. `DEPENDENCIES.json` goes from `5b5e2e77` to `7a4f49d0`, and the only content change is the Context pin `c2bd656b` → `5a9ecd76`; the visual pin is unchanged. The source file in the worktree still pins `c2bd656b`, as the record states.
- **Ref graph: 25 refs.** That is `main` plus 6 × (cut, selector, rc, release).
  - The 6 immutable cuts each have `expected_remote: ""`. With `--force-with-lease=<ref>:` inside `push --atomic`, that makes them create-only.
  - The 19 mutable refs carry explicit leases. Native rc/release branches expect `21a9d4b9` (RC2 native); companion branches expect `4a7f7cdf` (RC2 B).
  - Every tag is annotated and peels to its role commit, and each selector targets the same commit as its cut.
  - The 12 protected RC2 objects and peels are complete. The code checks them before pushing and reads them back afterwards.
  - There is no sequential fallback.
- **Assets.** The descriptor lists six. The five constructed assets are hash-bound. The cohort asset is excluded from its own digest by the stated policy.
- **Prior reports.**
  - native-01 was `falsified` (F1–F4); native-02 found all four resolved and returned `satisfied`.
  - semantic-01 was `satisfied` with low-severity side observations A1–A3; semantic-02 was `falsified` (F1); semantic-03 was `satisfied` with F1 `repaired_verified`.
  - Semantic-03 covers exactly eight subjects. Its `raw_index_sha256` values (`c90881b3`, `dd316407`) equal the shipped `INDEX.json` members. The 100 packaged operations ran against `packaged-products-03`, with no `passed:false`.
  - The visual model `4d457d78` matches the shipped Representation records. Manager checks are limited to macOS arm64 / CPython 3.13.
- **Claim limits.** No record claims whole-method qualification, automatic host pickup, public readback, human acceptance, consumer adoption or global install.

## Findings (all low, none blocking)
- **L1 – two failure reports not hash-bound.** The qualification hash-binds native-02, semantic-01 and semantic-03. It does not bind the retained failure reports native-01 and semantic-02. The statement in `PREPUBLICATION.md` that "no failed report was rewritten" therefore isn't mechanically pinned for those two. They are present in the workspace.
- **L2 – companion root tree not recorded.** For the native Product the cohort records the repository-root tree, but for the five B Products it records only commit and subtree tree. RELEASE §2 lists the root tree as part of cut identity. The commit hash fixes the tree, so the cut can still be reacquired.
- **L3 – stale wording in a context limit.** A limit in `context/FINAL_RESULT` still describes trial-hosts-02/03, but the semantic-03 subjects are the trial-hosts-04 deliveries. This is wording only; the bound digests are consistent.
- **L4 – native tag uses different markers.** The native cut annotation carries `Frozen-Source-*` markers, not the `STDO-Product-Subtree/Tree` markers on the other tags. The manifest and cohort bind the subtree and tree, so identity is complete.

Remaining residual: publication fast-forwards remote `main` from `2c95df2f` to `be3d4221`. The original dirty `main`, with its unpushed Builder commits, stays untouched and will need its own reconciliation later. Public acquisition and fresh isolated installation remain a separate, mandatory later gate.

```json
{
  "kind": "stdo.rc3-identity-assessment/1",
  "result": "satisfied",
  "carrier": "be3d42211130b960d325b0415529405dcc76a375",
  "native": "b2e21ad0a2bab04e59afd5246b990da992417047",
  "findings": [
    {"id": "L1", "severity": "low", "blocking": false, "summary": "Retained failure reports native-01 and semantic-02 are not in the hash-bound qualified_files; the PREPUBLICATION.md non-rewrite claim is narrative for those two."},
    {"id": "L2", "severity": "low", "blocking": false, "summary": "Cohort records the repository-root tree for native A only; for source-B Products the root tree is implied by the commit and not stated (RELEASE §2)."},
    {"id": "L3", "severity": "low", "blocking": false, "summary": "A context/FINAL_RESULT limit still names trial-hosts-02/03; semantic-03 subjects are trial-hosts-04. Wording only, digests consistent."},
    {"id": "L4", "severity": "low", "blocking": false, "summary": "Native cut tag annotation carries Frozen-Source-* markers, not the STDO-Product-Subtree/Tree markers on the other tags; the manifest and cohort bind subtree/tree."}
  ],
  "scope": "Read-only consistency check of the frozen RC3 identity and claims against installed STDO 3.0.4 RELEASE §2-§8, the RC3 RELEASE.md and the RELEASE_3_1 corrective-cut clause: six Products and definitions, native A before B, 95-member native manifest, 226 companion members, exact dependency pins including the Purpose Context and Skills source-to-public changes, the 25-ref leased atomic graph with six create-only cuts, 12 protected RC2 objects, five constructed assets plus the self-excluded cohort asset, and prior report dispositions. Git object, tree and hash values are Writer observations checked only for internal consistency; no hashing or git commands were run. Not a semantic re-review of the method; no publication, public readback, installation, human acceptance or consumer adoption is assessed or implied. Public installation remains a mandatory later gate."
}
```