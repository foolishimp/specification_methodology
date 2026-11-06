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

An execution record names its exact producer, argv, return code, environment,
input artifacts, stdout/stderr, output artifacts and result artifact. Every
artifact has a repository-relative path and SHA-256. The result must be one
of those actual command outputs, and declared JSON-pointer observations are
compared with its concrete values. CLI help and source-archive operations
cannot establish installed capability. The current Lean claim additionally
requires the exact current model hash, the complete requested/checked claim
set, successful proof stages, seven dynamic proof invocations, one kernel
replay, one runtime invocation, evidence members and exact runtime pins.

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
immutable release refs and their peels are preserved. Stable/RC collisions,
partial expectation sets, changed remote objects or wrong tag peels refuse.

The external cohort manifest is published as `stack-release-v3.0.5.json`.
Its own digest and subsequent readback stay outside its frozen contents.
`--phase public --public-receipt <path> --public-receipt-sha256 <digest>` takes
that later receipt explicitly, checks its fresh installed qualification and
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
