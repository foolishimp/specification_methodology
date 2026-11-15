# RC2 final identity and pre-push assessment (identity-01)

## Verdict

The bounded prepublication identity of native A `21a9d4b9…`, source B `4a7f7cdf…` and ref graph `3c891905…` is **supported**, with the limits listed below. Every identity I checked across the supplied records agrees, and I found no material counterexample.

I recomputed no hashes. Every digest, equality and test outcome below was computed by the operator or a Writer, and Writer records count as claims. My contribution is checking that those records agree with each other and with the governing law.

The prior actual Claude semantic result (session `004386e3…`) still applies to its exact six bindings. The three unknown-boundary queries are still refused and uncovered. Publication, public acquisition, adoption and human acceptance of the exact cut have not happened, and this report authorizes none of them.

## Standing

- **Who I am.** A Claude-family assessor, cross-family to the Codex Writers. I am the same family as the earlier source-first and semantic assessors, so confirmation bias is possible.
- **Tools.** I used none. An advisor tool was exposed in this session; I did not call it, because the instructions say not to use tools.
- **Host context.** The host added an account reminder, which I did not use. Any other hidden host context is unmeasured.
- **Reading order.** Sources and candidate arrived in one packet. The only expectations recorded before the candidate was exposed are the two fixed source-first reports.

## 1. Product, member, dependency and version identities

**Supported.**

- **Six Products.** The six namespaces in `REF_PLAN`, `COHORT_DRAFT`, the operator readback and `COHORT_INPUTS` are the same set, and `ref_transaction.NAMES` refuses any other population.
- **Construction basis.** All six Product Definitions pin `stdo://releases/v3.0.4/`, manifest `102817a3…`. `cohort_record.py` enforces this.
- **Companion member counts.** I counted the members myself:
  - Purpose Context: 51 (49 byte-equal to source, plus `PUBLIC_MANIFEST.json` and `SOURCE_RELATION.json`)
  - Skills: 35 (34 listed files plus `INVENTORY.json`, which does not list itself)
  - Representation Tools (`a_c`): 48
  - STDO Representation: 67
  - Axiom Indexer: 24
  - Total 225, which matches `PRODUCT_EXTRACTION` and `PREPUBLICATION`. Purpose Context plus Skills (51 + 35) gives the Writer's figure of 86.
- **Native cut.** The native has 94 members and manifest `b691b024…`. That manifest is named identically in `NATIVE_BINDING`, the cohort, the companion inventory, Purpose Context's `SOURCE_RELATION.native_method`, Skills' `INVENTORY.release.native_method` and STDO Representation's embedded `source/manifest.json`.
- **Version suffix.** The `VERSION` files of the three visual Products share digest `1a992ade…` (11 bytes, consistent with `3.1.0-rc.2\n`). The manager version is the PEP 440 equivalent `3.1.0rc2`.
- **Dependency pins.**
  - Skills' portable `DEPENDENCIES.json` pins Purpose Context `adb0f592…` and `a_c` `6810997f…`. These equal the archive identity files and the cohort's dependency edges.
  - STDO Representation's edges pin `a_c` `6810997f…` and Axiom Indexer `f03c5982…`, which also equal the inventory.
  - The cohort edges were produced by string replacement on the RC1 draft. I spot-checked every edge selection against the inventory and found no leftover `rc.1` value. No mechanical check of this exists beyond my reading.

**Declared transformations:**

- **Purpose Context: supported, with complete accounting.** I reconciled every Purpose Context file in `FINAL_FREEZE` against `SOURCE_RELATION`. Each one is either a byte-equal member, one of the 46 enumerated exclusions (historical indexes, test scripts, the development corpus), the declared filtered catalog (`5ce764b2…` to `1f9beecd…`), or the replaced public manifest (`a5f9479a…` to `adb0f592…`).
- **Skills: partly declared.** The `DEPENDENCIES.json` change (`6e966661…` to `803ce52a…`) is declared in `INVENTORY.source_transformations`. However, four source members in `FINAL_FREEZE` are absent from the portable package and are declared nowhere in the supplied bytes:
  - `release/3.0.5/README.md`
  - `release/3.0.5/manifest.json`
  - `release/3.0.5-rc.1/README.md`
  - `release/3.0.5-rc.1/manifest.json`

  `package.py` may define the selection, but it was not supplied (finding F2).

## 2. Native A and source B

**Supported.**

- **Native A.** Commit `21a9d4b9`, repository-root tree `2c44fdca`, Product subtree `specification_methodology/v3` with tree `61efe71a`. Annotated tag `fb85e1b7` peels to A (operator-verified), and A's parent is RC1 `c1e0faaa`.
- **Source of A.** A's subtree tree equals the `build_tenants/common` tree of source checkpoint `31e6f40e`. The cohort records this as `native_source_tree`.
- **Source B.** The five derived Products sit at B (`4a7f7cdf`), and all five subtree trees were verified by the operator.
- **Remote main.** `prepare` requires remote `main` (`f84ef0af`, the start of the admitted continuation) to be an ancestor of B.
- **Definition versus subject.** The `specification_methodology` Product Definition is read from B (`stdo_3.json`), while its release subject is A. This split is declared and lawful: a Product Definition is a source-project surface, not the released artifact.
- **Gaps.** Nothing supplied shows that `31e6f40e` is an ancestor of B, or that B's `build_tenants/common` still equals `61efe71a` (that is, no source drift after A was cut). Neither undermines A's identity. Both bear on the claim that the source freeze is still current (G1).

## 3. Mapping the prior assessment onto the packaged context

**Reuse applies to the six bindings.**

- **Index bytes.** The packaged raw `INDEX.json` bytes (`84a4043c…` and `e307802e…`) equal source B. Their canonical hashes `e6a71a11…` and `39f2432c…` are the ones the assessment bound.
- **Context bodies.** `FINAL_PACKAGE_SEMANTIC_READBACK_02` (78 operations) shows that all six JSON and Markdown context pairs equal the frozen bodies on both hosts. The Markdown digests are exactly the ones the assessment cites (for example acceptance `45b4ba3f…`). This closes the prior unperformed item "Claude-host delivery".
- **Assessed archive replay.** In the extracted-archive run (80 operations; I counted 40 per host), each envelope is consumed with `covered:true` and the selected-rule counts match the assessment: 94 / 20 / 31 / 31 / 31 / 26.
- **Refusals in that run.** The RC1 Python assessment is refused against RC2, so no relabelling occurs. A wrong public pin, a wrong native selection, overflow, collision and tampering are all refused.
- **Residual RM1.** The assessed Markdown bodies (for example `3b067c9a…`) differ from the frozen bodies I judged. The operator's claim of unchanged semantic payload covers JSON fields plus the four annotation fields. Nothing shows the Markdown difference is annotation-only. This is plausible if the Markdown is a deterministic rendering, but it is not demonstrated.
- **Unknown-boundary refusals.** All three still refuse on both hosts with exit code 3, status `incomplete`, `covered:false` and no delivery. Two caveats:
  - Their output bytes (`4d80b07a…`, `80bd7dea…`, `102c1820…`) differ from the refusal records I judged earlier (`203f6455…`, `74c52540…`, `ab30b694…`). My earlier finding that the refusals were correct applies to those earlier bytes.
  - That earlier finding relied on the catalog `family_guard`. The catalog has since been filtered to `1f9beecd…`, and nothing supplied shows the RC2 SDLC entry's guard is unchanged (G2).

## 4. Current release claims and predecessor conservation

- **Ledger counts.** I counted 153 claims: 113 Python plus 40 SDLC. 152 are conserved with identical rule digests, and W35 is `superseded` with only its `when` field changed.
- **Conserved rules.** For the 152 byte-identical rules, `conserved` meets the reuse condition of RELEASE §9 ¶2 (owner text and consumer bindings unchanged). This depends on the claimed equality of the runtime, which I did not see compared against RC1.
- **W35.** RELEASE §9 defines `superseded` by an *accepted* successor relation. Before human acceptance of the exact cut, this disposition is a claim that qualification evaluates, not a closed result. The ledger states as much itself (F3).
- **Disposition category.** "Stale 35-rule guides: `not applicable`" mislabels the category. The RC1 claim, corrected guides with 52 passing tests, is in substance retained, which makes it `conserved`. The predicate is sound; only the value name is wrong (F4, minor).
- **Manager.** The claim of "unchanged behaviour" is still unverified. The manager result shows that the 13 modules match source and that third-party bytes are conserved, but gives no RC1-to-RC2 behaviour comparison (G3).
- **Native release note: prospective claims (condition C1).** Each of the following must be true at publication:
  - an atomic, guarded 25-ref transaction takes place;
  - the GitHub download URLs on tag `specification_methodology/v3.1.0-rc.2` resolve;
  - the cohort "distinguishes … installed adapter checks".

  The draft cohort's committed evidence includes `context/RESULT.json` (the unassessed 78-operation run). It does not include `assessed-packaged/RESULT.json` or `PRODUCT_EXTRACTION.json`, which are reachable only through a `PREPUBLICATION.md` link and a hash in the ref plan's `qualified_files` (F1). A is immutable, so if C1 fails the only remedy is a higher RC.

## 5. Tags, peels, the 25-ref graph and remote expectations

**Supported.**

- **Ref count.** 25 = `main` + 6 × (cut, selector, rc branch, release branch).
- **Cut tags.** The six cut tags are annotated, create-only, and expect remote absence (`--force-with-lease=<ref>:` with an empty value means the ref must not exist).
- **Selectors.** All six selectors are new annotated objects, separate from the cut tags. They peel to the same commit as their cut and are leased against the RC1 selector objects (for example `9bdc0ab4…`). `prepare` verified that each RC1 selector peels to the RC1 commit, so this is a move from a lower ordinal.
- **Branches.** The rc and release branches are leased against `c1e0faaa` (native) or `f68e8f47` (derived).
- **Protected refs.** The 12 protected entries (6 RC1 tags and their peels) match `ACTIVATION`: `fca8d5e9…` peels to `c1e0faaa…`, and the other five peel to `f68e8f47…`.
- **Agreement across records.** The values in `REF_PLAN`, `COHORT_DRAFT` and the operator readback agree field for field. The graph hash `3c891905…` was computed by the operator, and its scope correctly excludes `qualified_files`.

## 6. Release helper and its finite tests

The helper is proportionate and fails closed.

**What it does:**

- `check` re-reads the remote at publish time, so the post-tag, pre-push gate is re-run immediately before the push.
- It verifies the population, a 25-ref count with no duplicates, the destination set, annotation, mutability flags, Product trees, local objects, an exact remote expectation for every destination, and the `qualified_files` digests.
- `publish` makes a single `git push --atomic` with a per-ref lease and no fallback, then reads back every object, peel and protected ref.

**Fixture results.** Eight scenarios pass against a real local Git transport, using the same tool digest `b3efdcdb…`:

- a higher ordinal refuses before any mutation;
- a missing predecessor destination refuses;
- an incomplete graph refuses;
- evidence drift refuses;
- lease drift refuses, and no partial RC2 appears;
- a pre-receive rejection leaves the remote unchanged;
- a successful publish writes exactly 25 refs and preserves RC1.

**Limits (F5):**

- The higher-ordinal check scans only project-qualified namespaces, not unqualified historical `refs/tags/v3.1.0-rc.N`.
- `check` does not verify a tag object's internal name or message.
- `check` does not compare the plan's own digest. Publication must use plan bytes `882bb34f…`.
- `qualified_files` are hashed from the working tree, which says nothing about whether they are committed.
- In the fixture, `native_predecessor == source_predecessor`, so a swap between the native and derived roles in the predecessor check would go undetected.
- The fixture runs over local file transport only. Atomic-push support on GitHub is not tested.

## 7. Atomic publication and RC1 preservation

Atomic publication and RC1 preservation are shown only in the local fixture. Production publication has not been performed.

## 8. Avoiding self-referencing digests in the external cohort

**Supported.**

- The cohort asset is excluded from its own asset list.
- The native links to the cohort by URL, not by digest.
- `INVENTORY.json` and the Purpose Context public manifest do not inventory themselves.
- The cohort's `post_tag_review` field embeds this report, and this report contains no cohort digest.

**Tension with the law (F6).** The RC-profile step 4, in both the 3.0.4 and the RC2 RELEASE text, lists "cohort record" among the content frozen in commit B. In this release, B freezes `COHORT_INPUTS` and the evidence, while the final binding of tags and assets is an external asset. That is necessary, because the record binds B's own tags. The RC2 text explicitly endorses external binding only for the stable, embedded-asset case. The release authority should state this reading in `RELEASED.md`. I do not judge it a blocker.

## Local construction versus what still has to happen

What is supported now is **local construction and prepublication qualification of identity** only.

Still required before any public claim can be made:

- the fresh-fetch re-check and the atomic push;
- public readback of the refs;
- a normal GitHub release with all six assets;
- downloading those assets and comparing their hashes;
- a fresh isolated install and replay;
- verifying condition C1.

Human acceptance of the exact cut and consumer adoption remain separate decisions after that.

```json
{
  "subject": {"native_commit": "21a9d4b93c5adef1e84a369360a99176b98793c5", "source_carrier": "4a7f7cdfcd724d6b2e47b3d790fa88030b70d84a", "ref_graph_sha256": "3c8919055f70f0c9d099daa2459947aeaff78ee220ef4154696ee0c1937ce4ce"},
  "status": "supported",
  "status_scope": "Bounded prepublication identity only, by cross-record consistency of operator/Writer-computed digests; no hash recomputed; not publication, acquisition, acceptance or adoption",
  "claim_results": [
    {"claim": "Six-Product membership, 225 companion members (51/35/48/67/24), 94-member native, manifest b691b024..., 3.0.4 construction basis on all definitions, version suffix 3.1.0-rc.2 / 3.1.0rc2", "result": "supported"},
    {"claim": "Dependency pins PC adb0f592, a_c 6810997f, axiom f03c5982, native b691 across Skills, PC, cohort edges and inventory", "result": "supported", "limit": "edges derived by string replacement; only my reading checks them; Representation-owned pin contracts not supplied"},
    {"claim": "PC portable projection fully declared (49 equal, catalog filtered, manifest replaced, 46 exclusions)", "result": "supported"},
    {"claim": "Skills portable projection fully declared", "result": "unknown", "basis": "DEPENDENCIES transform declared; four release/3.0.5* source members omitted without declaration in supplied bytes (F2)"},
    {"claim": "Native A / source B distinction and subtree identities", "result": "supported", "gap": "G1: checkpoint 31e6f40e ancestry to B and absence of build_tenants/common drift in B not shown"},
    {"claim": "Prior assessment maps onto packaged contexts on both hosts", "result": "supported", "residual": "RM1: assessed Markdown differs from judged bodies; annotation-only delta not demonstrated"},
    {"claim": "Predecessor dispositions: 152 conserved, W35 superseded", "result": "supported_as_claims", "basis": "RELEASE 9 para 2 retain condition for byte-identical rules; W35 superseded pending accepted successor relation (F3); guides disposition mislabelled (F4)"},
    {"claim": "25-ref annotated graph, peels, create-only absence, leases to RC1 objects, 12 protected refs", "result": "supported"},
    {"claim": "Guarded atomic publication preserving RC1", "result": "supported_local_fixture_only"},
    {"claim": "External cohort without a self-referencing digest", "result": "supported", "note": "F6 tension with step 4 wording"},
    {"claim": "Native release-note prospective claims", "result": "unknown", "condition": "C1"},
    {"claim": "Manager behaviour unchanged from RC1", "result": "unknown", "gap": "G3"}
  ],
  "semantic_reuse": {
    "source": "assessment/semantic-01/ASSESSMENT.md e7636ede..., session 004386e3-1178-4a56-9456-1fa4fbde5ce4",
    "applies": true,
    "bindings": [
      {"name": "acceptance", "index": "39f2432c...", "corpus": "f281ac7a...", "query": "58ce3e20...", "status": "supported"},
      {"name": "qualification", "index": "39f2432c...", "corpus": "f281ac7a...", "query": "0049b6e2...", "status": "supported"},
      {"name": "release", "index": "39f2432c...", "corpus": "f281ac7a...", "query": "428f2d98...", "status": "supported"},
      {"name": "work", "index": "39f2432c...", "corpus": "f281ac7a...", "query": "650ed9ed...", "status": "supported"},
      {"name": "sdlc", "index": "39f2432c...", "corpus": "f281ac7a...", "query": "9e81574d...", "status": "supported"},
      {"name": "python", "index": "e6a71a11...", "corpus": "108aa791...", "query": "84b5d4b9...", "status": "supported"}
    ],
    "refused_uncovered": ["missing-boundary", "null-boundary", "ill-typed-boundary"],
    "refusal_note": "Current refusal bytes differ from the judged ones; standing is mechanical (incomplete, no delivery); catalog family_guard equality after filtering not shown (G2)",
    "retained_residuals": ["R1", "R2", "R3", "R4", "R6", "A1", "A2", "RC1-F1/F2/F3/F4/F5/F7", "visual limits"],
    "not_relabelled": "RC1 judgments keep their original subjects; predecessor assessment refused at runtime"
  },
  "findings": [
    {"id": "F1", "class": "bounded", "summary": "Draft cohort does not bind assessed-packaged/RESULT.json (953e9408) or PRODUCT_EXTRACTION.json (0aba0945) as evidence, yet the native note claims the cohort distinguishes installed adapter checks", "smallest_correction": "Bind both into the final cohort evidence by digest (committed, if they are in B)"},
    {"id": "F2", "class": "bounded", "summary": "Skills portable package omits four release/3.0.5* source members without a declared exclusion"},
    {"id": "F3", "class": "bounded", "summary": "W35 'superseded' presupposes an accepted successor relation; it remains a claim until qualification and acceptance"},
    {"id": "F4", "class": "minor", "summary": "Retained guide repairs disposed 'not applicable' where the retained claim is in substance 'conserved'"},
    {"id": "F5", "class": "limit", "summary": "Helper: unqualified-namespace ordinal not scanned; tag name/message not checked; plan digest not self-checked; working-tree hashing; fixture does not discriminate predecessor roles; local transport only"},
    {"id": "F6", "class": "interpretation", "summary": "External final cohort versus RC-profile step 4 'cohort record frozen in commit B'; to be stated by the release authority"}
  ],
  "residuals": ["G1 source-freeze currency in B", "G2 catalog family_guard after filtering", "G3 manager behaviour", "RM1 Markdown annotation delta", "PREPUBLICATION_QUALIFICATION.json (53a70421) content not supplied", "All digests operator-computed", "Same-family confirmation-bias risk", "Hidden host context unmeasured; no adequate-attention or clean-room claim"],
  "unperformed": ["Fresh ls-remote and production atomic push", "Remote readback", "GitHub release", "Public download and hash comparison", "Fresh isolated install and replay (manager, native, both adapters, visual)", "Final cohort binding", "C1 verification", "Human exact-cut acceptance", "Consumer adoption"],
  "publication_conditions": [
    "Publish only from REF_PLAN bytes 882bb34f with ref graph 3c891905; check re-run on fresh remote; any lease or remote mismatch stops publication, followed by refetch and full requalification",
    "qualified_files unchanged, including PREPUBLICATION_QUALIFICATION.json 53a70421",
    "Remote must accept --atomic; otherwise refuse with no sequential fallback",
    "Post-push readback: 25 objects and peels exact; 12 RC1 protected refs unchanged",
    "Normal GitHub release on tag specification_methodology/v3.1.0-rc.2 with the six COHORT_INPUTS asset names; five digests as drafted; cohort digest bound by expected-assets record and advertised digest",
    "Final cohort identity fields and ref_graph_sha256 equal the draft except review/qualification fields",
    "Public reacquisition and fresh isolated install reproduce manifest b691, Product membership and the six contexts on both hosts",
    "C1 release-note assertions verified true, otherwise a higher RC is required; record in RESULT.json and RELEASED.md",
    "No publication authorization, acceptance or adoption is created by this report; Root remains the effect owner"
  ]
}
```
