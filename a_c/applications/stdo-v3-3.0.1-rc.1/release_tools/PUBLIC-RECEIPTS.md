# Public receipt contract for this successor representation

This application contract binds public construction and bounded-review accounts
to the actual frozen inputs. It is packaging HOW, not a Product requirement,
methodology rule, semantic acceptance contract or proof of issuer legitimacy.
The constructor and portable bundle checker apply the same contract.

## Obtain coordinates without generating an account

From the application or extracted bundle directory:

```sh
python3 -B package_release.py receipt-bindings --proposal /path/to/closed/proposal --graph /path/to/exact/upstream/graph.json
```

The command checks the frozen successor source/model relationship and prints a
`bindings` object. It emits no construction or review receipt, performs no F_P
authoring and makes no semantic judgment. Each responsible actor supplies its
own honest account and copies the unchanged `bindings` object into its receipt.
The optional `--graph` argument is unnecessary when the export is the proposal
directory's `graph.json`.

The exact `bindings` object has three members:

| Member | Exact content |
|---|---|
| `source` | `subject_id`, immutable `commit`, `package_tree`, raw `source_manifest_sha256`, `semantic_files_sha256`, `section_inventory_sha256`, and `source_reentry_sha256`. The latter three bind the model's exact current ordered file selection and section inventory and file/section re-entry commitment. |
| `model` | Supplied absolute model `id` and canonical codec `sha256`. This is separate from the model file's raw SHA256. |
| `artifacts` | Exactly `model.json`, `carrier.json`, `graph.json`, `coverage.json`, `result.json`; each maps to its actual integer `bytes` count and raw `sha256`. An externally stored export is still named `graph.json` in this declared bundle contract. |

These values are derived from the actual checked model and raw inputs. They
are not inferred from the receipt's claims. A change to any bound artifact
requires an explicitly updated account from its responsible actor; the
packager never refreshes receipt hashes or silently retargets a review.

## Construction JSON

All and only these top-level fields are required:

| Field | Type and required meaning |
|---|---|
| `kind` | Exactly `a_c.common.public-construction-receipt/1`. |
| `receipt_id` | Absolute identity of this recorded account. |
| `issuer` | Absolute identity naming the actor reporting construction; this coordinate does not prove that actor's authority. |
| `bindings` | Exact object described above. |
| `scope` | Nonempty text stating the construction scope and limits. |
| `details` | Nonempty JSON object retaining the actual public construction account: selected attempts/answer hashes, reported settings/usage, checked properties, failures and qualification limits as applicable. |
| `construction_state` | Exactly `complete`: processing of the supplied proposal is reported complete. It does not mean semantic completeness or acceptance. |
| `private_material_included` | Exactly `false`. Raw invocation bodies, event streams, native configuration and hidden reasoning are excluded. This declaration is not independent authentication of the account's contents. |

Pass this JSON file through `--public-evidence`. It is copied unchanged to
`evidence/authoring-public.json`. The account's reported private custody remains
externally held; opaque hashes do not make those private files independently
replayable by a recipient.

## Bounded-review JSON

All and only these top-level fields are required:

| Field | Type and required meaning |
|---|---|
| `kind` | Exactly `a_c.common.bounded-review-receipt/1`. |
| `receipt_id` | Absolute identity of this bounded review account; distinct from construction and other review receipts. |
| `issuer` | Absolute identity naming the reporting reviewer. |
| `bindings` | Exact object described above, including all five raw artifacts. |
| `scope` | Nonempty text identifying the actual bounded review contribution and limits. |
| `details` | Nonempty JSON object containing the reported assessment, predicates, evidence and remaining limits, or routes to the explicitly bound readable reports. |
| `review_state` | Exactly `closed`: the actor reports its bounded review completed. An incomplete review must remain explicitly incomplete and cannot be passed as the closed review input to this packager. |
| `outcome` | Nonempty text reporting that bounded review's actual result. The checker does not decide whether the reported result is correct or sufficient for release. |
| `independence` | Nonempty JSON object disclosing the actual authorship relation, exposure and independence limits. The checker does not authenticate those claims. |
| `reports` | Explicit list of UTF-8 Markdown/text report bindings; `[]` is permitted when the complete readable account is in the JSON itself. |

Each `reports` element has exactly `path`, `bytes`, `sha256`. Its path is a
canonical relative POSIX path from the review JSON's directory, with `.md` or
`.txt` extension. Absolute paths, traversal, symlink components, duplicate
paths, missing files and changed bytes refuse. The constructor copies the
unchanged receipt and bound reports together beneath
`evidence/reviews/review-NNN/`, preserving those relative routes.

Pass each review JSON through its own `--review` argument. A standalone Markdown
filename or file hash is not an exact-model review receipt and refuses. A
readable Markdown review remains usable when accompanied by this explicit
subject-bound JSON account. No review is manufactured from a report filename.

## Checks and retained limits

Before creating a bundle, the constructor checks both receipt types against
the actual source commitments, canonical model and all raw artifacts. It also
checks explicit readable-report custody and receipt identity uniqueness. The
extracted stdlib checker repeats those comparisons from the bundled bytes and
checks the release evidence index, receipt hashes and complete public-file set.
Missing, stale, wrongly typed, different-source or different-model accounts
refuse, even when a surrounding file inventory has been regenerated.

These checks establish matching coordinates and supplied custody only. They
do not prove receipt truth, reviewer independence, issuer legitimacy, semantic
fidelity, adequate review scope, acceptance or public-distribution permission.
The represented native cut is a scoped test candidate, with inherited common `not_ready`/unaccepted standing;
the representation remains a proposal unless separately accepted by its owner.
