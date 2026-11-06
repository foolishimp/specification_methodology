# Stable complete-cohort checker profile

`check_stack_release.py` dispatches schema 1 to its original RC implementation
and schema 2 to `stable_stack_release.py`. The retained schema-1 fixture is
byte-identical to the previous root manifest. The current schema-2 manifest
remains `assembling`; it cannot pass a release gate while required subjects or
evidence are absent.

The stable profile selects exactly the five Product namespaces and eleven
required components in `RELEASE_PRODUCTS.md`. Product and component versions
must equal the stable cohort version. Actual native plugin metadata, each
peer Product's delivered `VERSION`, and manager wheel metadata/runtime source
are checked. Third-party versions retain their independent exact pins.

Each `subject` contains sorted unique repository-relative `scope` entries,
complete `members` (`path`, `bytes`, `sha256`), `member_count` and `sha256` of
the compact canonical member vector. Scopes select the owner's current
canonical release inventory, not its historical project tree. The checker
re-enumerates every selected scope and rejects missing, extra or changed
members. Payloads and parents must be regular contained files; discovery
symlinks stay outside the distributed inventory. Components must be exact
subsets of their owning Product subject. Dependency edges additionally pin
the provider's subject digest.

The `source` field pins the accepted semantic record and source identity. Its
standards and native contract closure is rederived from the candidate. The
`native` field pins `manifest` and `source_selection` records from the existing
native-release tool. Its annotated tag, sole native predecessor, Git trees,
producer source tree, complete installed inventory and current candidate
payload must agree. Generated documentation and tooling are mandatory native
members even though excluded from semantic identity.

A component's `evidence` maps every required claim to a pinned
`stdo.cohort-evidence/1` record. Every record binds current semantic source,
actual Product subject digests, claim, passed status and limits. Whole-cohort
claims bind all five Product subjects. Derived claims additionally bind the
current Representation subject.

Execution evidence is consumed by `stable_release_evidence.py` through fixed
owner adapters. Each adapter prescribes the exact producer, command, current
inputs and result schema. The retained stdout must equal the result; input,
output and transcript files are dereferenced. Caller-provided JSON pointers,
operation labels, CLI help and a generic `status: verified` have no qualification
meaning. The selected Python invocation remains distinct from its pinned
physical executable, so a virtual environment is not lost by resolving its
symlink before execution.

Every installed claim binds a `stdo.installed-cohort/1` record. It maps every
selected member of all five Products to an actual regular file in a separate
qualification workspace. The gate reads those bytes, the complete installed
native population and native manifest, the real manager's selected source
modules and version, and a fresh read-only manager verification. Its retained
install operation must name the selected public repository, cut, store and
native digest and return `installed`. Both host Skills use the owner's actual
receipt, `verify` and `check-runtime` outputs. Graphify uses the owner's
`ac_upstream.py` current model/carrier/selection roundtrip, exact private runtime,
loaded modules, retained graph and views. The whole-cohort record is an
`installed_aggregate`: every required current component result must refer to
that same installed record. One Product's success cannot satisfy this set.

The exact Lean claim requires model and request/view inputs actually consumed
by the CLI. S reaches that model through the separately checked source/model
owner relation and independent semantic review; S is not falsely added as an
unconsumed Lean execution input. The gate requires the five named owner
obligations, dereferences the full proof bundle, and invokes the formal owner's
`inspect-evidence --bundle ... --request ...`. This read-only adapter rederives
proof sources, selected runtime/support, theorem/axiom audits, current output,
closure selections and supplied views. `consistent` is not a new kernel verdict.
The original cold run has seven dynamic elaborations, one kernel replay and
one runtime execution. Installed qualification selects either an actual
`check-evidence --fresh` with the same machinery or a new `verify` under its
own exact runtime after support re-establishment. Both execute the current
model/selections/views with the same 7/1/1 counts. The latter pins the generated
support profile separately and must conserve every other selected machinery
source pin; it makes no portable support equivalence or old-verdict reuse
claim. `installed_verification` may bind either actual installed result from
the exact-candidate record. A separate construction `replay` remains supported
only when it really is a same-runtime fresh replay. No duplicate cold run is
required solely to attach the word replay. Public origin selection bytes
are retained separately from publishable machinery source; no private origin
key or cache supplies release authority.

Browser behavior uses a separately bound observer, current installed page and
model identities, prescribed 3D/2D/layered and source/files observations, exact
screenshots and an attributed report. These are observational assessments;
file hashes alone do not establish rendering or interaction.

An independent assessment instead names its assessor and authors, exact
report, satisfied conclusion, no open required findings and the Executive's
accepted disposition. The checker checks evidence identity and declared
boundaries; it does not independently judge semantics or invent assessment
from green structural checks. The reviewed producer and independent assessment
must establish the adequacy of each operation and its observations.

The selected 3.0.5 push set is main plus five immutable Product tags. Generic
schema support permits an explicitly selected optional `release_branch`;
null selects none. Ref qualification emits an exact object-ID atomic push
vector with one lease per destination and a plan digest. All historical
immutable release refs and their peels are preserved. Same-version RC tags
refuse in both qualified and historical bare namespaces even if included in
the preservation snapshot; other-version RC history remains allowed. Stable/RC collisions,
partial expectation sets, changed remote objects or wrong tag peels refuse.

The external cohort manifest is published as `stack-release-v3.0.5.json`.
Its own digest and subsequent readback stay outside its frozen contents.
`--phase public --public-receipt <path> --public-receipt-sha256 <digest>` takes
that later receipt explicitly. It requires the exact current native manifest
and manager wheel plus every selected component asset, checks all five
Products and current component results against the declared fresh store, and
reacquires every selected release asset anonymously. A staged local copy does
not substitute for this public read.

The registered `common-tools/native_release.py` accepts
`--cohort-manifest <path> --cohort-manifest-sha256 <digest>` before its command.
The manifest's `native_preparation` selects stable version, native lineage,
output territory, manager wheel and scope. Its exact configuration is retained
in preparation evidence. Historical invocation without those options keeps
the original 3.0.4 profile. A cohort-configured invocation refuses standalone
native publication; only the complete root cohort checker can qualify that
push. The tool never writes Git, installs a package or performs publication.
