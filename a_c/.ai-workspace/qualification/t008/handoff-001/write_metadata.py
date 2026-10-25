"""Apply only the externally granted eleven factual Markdown edits."""
from pathlib import Path
import hashlib
import json

D = Path(__file__).resolve().parent
P = D.parents[3]
H = ".ai-workspace/qualification/t008/handoff-001"
before_rows = json.loads((D / "SOURCE_BEFORE.json").read_bytes())["sources"]
before = {row["path"]: (D / row["snapshot"]).read_bytes() for row in before_rows}
edits = {path: [] for path in before}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def exact(path, old, new, label):
    old = old.encode()
    assert before[path].count(old) == 1, (path, label)
    start = before[path].index(old)
    edits[path].append({"start": start, "end": start + len(old), "replacement": new, "scope": label})


def span(path, start_marker, end_marker, replacement, label):
    start = before[path].index(start_marker.encode())
    end = before[path].index(end_marker.encode(), start) if end_marker else len(before[path])
    edits[path].append({"start": start, "end": end, "replacement": replacement, "scope": label})


def render(path):
    result = b""
    offset = 0
    for row in sorted(edits[path], key=lambda item: (item["start"], item["end"])):
        assert offset <= row["start"] <= row["end"] <= len(before[path]), path
        result += before[path][offset:row["start"]] + row["replacement"].encode()
        offset = row["end"]
    return result + before[path][offset:]


span("README.md", "The additional [F_D support toolset]", "This is a development candidate", """The additional [F_D support toolset](specification/PRODUCT.md#f_d-support-for-f_p-development-actors)
has a provisional public CLI/MCP implementation in the existing Graphify tenant.
STDO3.0 owns the methodology; a_c supports its exact caller-selected contracts.
[T-008](.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation)
records Root's selection after bounded implementation, independent code review
and technical integration. The [current handoff](.ai-workspace/qualification/t008/handoff-001/README.md)
distinguishes completed technical checks from partial qualification and failed
actor trials. [T-007](.ai-workspace/tickets/active/T-007-executive-lifecycle-tooling.md)
remains the historical specification-only increment; its design-pending status
describes that earlier cut. The installed builder and Product composition are
unchanged. Accepted-result benefit remains Deferred/unqualified, and frozen
methodology models are not a maintained whole-workspace index.

""", "FD progress paragraph only")

span("specification/GOALS.md", "The current implementation increment is", "The completed comparison-preparation increment is", """The current implementation increment is
[T-008](../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation):
the existing Graphify tenant now contains the provisional public F_D support
implementation for F_P Executives, Workers and Reviewers. Root selected its exact
current realization after bounded implementation, independent code review and
technical integration. The [handoff](../.ai-workspace/qualification/t008/handoff-001/README.md)
binds the current sources, fresh versus carried checks and explicit gaps.
T-008 remains active for partial actual-actor/variant qualification; the failed
and partial live trials remain evidence. FDV-003 benefit is Deferred/unqualified.
There is no Product acceptance, installed/RC/release or full-calculus claim.

Jim's work-scoped selection remains exact Claude RC9 source
`c2cfa9b908d1722ae3f26c32fa4ece691083bdc3` and its Executive/software-design
profiles. The [operative tenant HOW](../build_tenants/graphify/design/fd-support.md)
and [exact RC9 profile](../build_tenants/graphify/design/fd-method-claude-rc9.json)
leave the installed v2.5.1-rc.2 builder and empty composition unchanged. Executive,
Writer/Worker, independent assessment and owner disposition retain their roles.

The completed specification increment is
[T-007](../.ai-workspace/tickets/active/T-007-executive-lifecycle-tooling.md):
it authored the common deterministic-support Product requirements and their
[historical source-owner derivation](requirements/fd-source-owner-map.md).
Design, realization and qualification were pending (Deferred) at that exact
specification-only cut. T-008 supplies the later operative work and progress;
this chronology does not rewrite the T-007 instruction or its historical result.
Existing source-to-model authoring and frozen comparison studies are unchanged.

""", "T008 current and T007 historical progress only")

product = "specification/PRODUCT.md"
span(product, "The [deterministic support requirements]", "Qualification separates", """The [deterministic support requirements](requirements/fd-support-tools.md) and
[qualification scenarios](requirements/fd-support-verification.md) specify the
requested Product outcome. Their earlier Deferred/design-pending statements
describe the T-007 specification-only cut. Under
[T-008](../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation),
the Graphify tenant has an operative selected HOW and provisional public
implementation; bounded implementation, independent code review and technical
integration are complete. The FD family is Active for that operative work.
FDV qualification is Active but partial; FDV-003 benefit remains Deferred and
unqualified. The [handoff](../.ai-workspace/qualification/t008/handoff-001/README.md)
retains exact evidence and gaps, including failed/partial ordinary actor trials.
Current frozen dogfood models still represent selected methodology corpora.

""", "delivery status prose only")
exact(product, "Implementation, qualification, acceptance and\nrelease remain downstream work.", "Further qualification, owner acceptance and\nrelease remain open.", "delivery chronology conclusion")
exact(product, "The current\n[T-007 instruction]", "The completed\n[T-007 instruction]", "T007 chronology label")
exact(product, "authorizes Product and requirement authoring for the additional F_D support\ntools.", "authorized Product and requirement authoring for the additional F_D support\ntools.", "T007 historical authoring fact")
exact(product, "Design/implementation requires a subsequent bounded work selection.", """The subsequent [T-008 instruction](../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#owner-instruction)
selected implementation. Root's [current work disposition](../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation)
selects the provisional realization after bounded implementation/review/technical
integration; T-008 remains active for explicit qualification gaps. It supplies
no Product acceptance, release decision or current runtime-call authority.""", "T008 factual work/disposition chronology")

requirements = "specification/requirements/README.md"
exact(requirements,
    "| [REQ-AC-FD-*](fd-support-tools.md) | Capability | Deferred: exact public tool inputs, deterministic output/checks, acquired content, executor observations and evidence interfaces; owning design and realization pending. |",
    "| [REQ-AC-FD-*](fd-support-tools.md) | Capability | Active: T-008's operative HOW and provisional public implementation; bounded implementation/review/technical integration complete, with qualification gaps retained. |", "FD delivery status row")
exact(requirements,
    "| [REQ-AC-FDV-*](fd-support-verification.md) | Verification | Deferred: ordinary actor use, source/evidence-bound refusal/recovery scenarios and accepted-result usefulness/cost; execution and qualification pending. |",
    "| [REQ-AC-FDV-*](fd-support-verification.md) | Verification | Active: qualification begun and partial for FDV-001/002; ordinary actor/variant gaps remain. FDV-003 accepted-result benefit is Deferred/unqualified. |", "FDV partial qualification status row")
exact(requirements, "Deferred records delivery status without withdrawing the owner-requested\nProduct outcome.", """Active records operative work and begun qualification, not satisfaction or
acceptance. Earlier Deferred/design-pending wording is as-at T-007's historical
specification cut. [T-008](../../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation)
and its [handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md)
record current evidence and remaining gaps without withdrawing the requested
Product outcome.""", "status/progress prose only")

fd = "specification/requirements/fd-support-tools.md"
exact(fd, "**Status**: Deferred", "**Status**: Active", "family status only")
exact(fd, "This family specifies additional tools supporting F_P Executives, Workers and\nReviewers. Deferred means owning design and realization are pending; the Product\noutcome is retained.", """This family specifies additional tools supporting F_P Executives, Workers and
Reviewers. Active records T-008's operative HOW and provisional implementation,
with bounded implementation/review/technical integration complete; it asserts
neither requirement satisfaction nor complete qualification. Earlier Deferred
wording describes T-007's specification-only cut. Current evidence and gaps are
in the [handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md).""", "intro delivery status only")

fdv = "specification/requirements/fd-support-verification.md"
exact(fdv, "**Status**: Deferred", "**Status**: Active", "family status only")
exact(fdv, "STDO3.0 methodology or F_P actor judgments. Design, implementation and executed\nqualification remain pending.", """STDO3.0 methodology or F_P actor judgments. Active records begun, partial
qualification under T-008, not a Passed/Implemented or satisfaction claim.
FDV-001/002 retain actual actor, operation/variant and host-boundary gaps;
FDV-003 accepted-result benefit remains Deferred/unqualified. Earlier pending
wording describes T-007's specification-only cut. The
[handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md) retains
current technical evidence and failed/partial live trials.""", "intro qualification status only")

tenant = "build_tenants/graphify/README.md"
span(tenant, "This is provisional construction", "Start with the [read-only public example]", """Root selects the exact current realization for further provisional T-008 dogfood
after bounded implementation, independent code review and technical integration.
The [current code review](../../.ai-workspace/comments/codex/t008-platform-code-review-003/REVIEW.md)
reports scoped E10/E11 satisfied with no actionable supported defect; its limits
do not establish F_P/operator or Product qualification. The operative HOW network
and separate ontology/design/work dispositions remain source-owned.

The current [integration-004](../../.ai-workspace/qualification/t008/interfaces/integration-004/REPORT.md)
passed one full run of 281 tests with no skips, joined strict normal-import typing
of nine files and ten fresh ordinary CLI/MCP demo checks. The nine-check actual
upstream result is retained from integration-003 with its complete dependency
boundary verified unchanged; it was not rerun as a standalone trial. Earlier
242/254/273-test cuts are historical. The [handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md)
binds sources, evidence and gaps, including real Worker/Reviewer timeout and
partial/unconsumable returns. Actual-actor/variant qualification is partial;
Product acceptance, benefit and installed/RC/release qualification remain open.

""", "support-status paragraphs only")

design_readme = "build_tenants/graphify/design/README.md"
exact(design_readme, "This additional design is a candidate; public implementation, operational\nqualification, accepted-result benefit and Product acceptance remain pending.", """This is T-008's operative provisional HOW with a public implementation selected
by Root after bounded implementation/review/technical integration. Current
evidence is 281 tests, strict normal-import checks on nine files, ten fresh
CLI/MCP demo checks and nine retained actual-upstream checks with unchanged
dependency applicability. The [current code review](../../../.ai-workspace/comments/codex/t008-platform-code-review-003/REVIEW.md)
and [handoff](../../../.ai-workspace/qualification/t008/handoff-001/README.md)
retain scope, historical cuts and actual-actor/variant gaps. Qualification is
partial; benefit, Product acceptance and installed/RC/release remain open.""", "final FD support status paragraph only")

how = "build_tenants/graphify/design/fd-support.md"
exact(how, "Status: **provisional HOW, current T-008 construction basis (publication-001)**.",
    "Status: **operative provisional T-008 HOW; bounded implementation/review/technical integration complete**.", "opening standing only")
exact(how, """The existing implementation is still provisional and its three reproduced
deviations remain unrepaired. A separate exact Worker grant is required after
this basis publication. This publication adds no native actor-call budget.
For this published cut, Jim's Product acceptance, installed/RC/release
qualification, runtime F_P qualification and accepted-result benefit remain
unperformed/unaccepted. Earlier actor attempts and checks retain their exact
historical scopes. The codec and source-generation designs keep their existing
checked boundaries.""", """Root's current [work disposition](../../../.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md#current-provisional-implementation)
selects the exact repaired realization for further provisional dogfood. The
published [code review003](../../../.ai-workspace/comments/codex/t008-platform-code-review-003/REVIEW.md)
reports scoped E10/E11 satisfied/no actionable supported defect, preserving the
other prior scoped results and their limits. The [integration-004 proof](../../../.ai-workspace/qualification/t008/interfaces/integration-004/REPORT.md)
records 281 tests/zero skips in one full run, strict normal-import checks on
nine files and ten fresh CLI/MCP demo checks. Its nine actual-upstream checks
are carried from integration-003 with unchanged dependency applicability.
The [handoff](../../../.ai-workspace/qualification/t008/handoff-001/README.md)
binds current code/test identities and preserved evidence. This factual opening
does not amend the complete reviewed body below the boundary.

Bounded implementation/review/technical integration is complete; T-008 remains
active for explicit qualification gaps. Actual F_P paths remain partial or
unconsumable/timeout histories; gate-isolated controls do not qualify a public
operator. Jim's Product acceptance, installed/RC/release qualification and
accepted-result benefit remain unperformed/unaccepted. Binding002 is historical
and stale; no current runtime authority, binding003 or native-call budget is
selected. Original F/I/S subjects and author/co-evolution chronology retain
their exact scopes. The codec and source-generation checked boundaries are
unchanged.""", "opening repaired standing/evidence only")

guide = "build_tenants/graphify/examples/fd-support/LIFECYCLE_QUICKSTART.md"
title_end = before[guide].index(b"\n") + 1
edits[guide].append({"start": title_end, "end": title_end, "scope": "historical-cut note immediately after title only",
    "replacement": """
> Historical guide/trial cut: the status and source identities below describe
> the original guide and trial. See the [current handoff](../../../../.ai-workspace/qualification/t008/handoff-001/README.md)
> and [retained before snapshot](../../../../.ai-workspace/qualification/t008/handoff-001/before/build_tenants/graphify/examples/fd-support/LIFECYCLE_QUICKSTART.md).
> This note is Writer metadata; the original guide and its trial limits remain unchanged.
"""})

ticket = ".ai-workspace/tickets/active/T-008-fd-tenant-implementation.md"
exact(ticket, "Current design state and exact repair routing are owned by\n[Current candidate after reconciliation-008](#current-candidate-after-reconciliation-008) below.",
    "Current implementation standing and remaining qualification are owned by\n[Current provisional implementation](#current-provisional-implementation) below.", "exact Root-selected two navigation lines")
how_after = digest(render(how))
append = f"""
## Current provisional implementation

Root WORK disposition selects the exact repaired realization below for further
provisional T-008 dogfood, after consuming the closed implementation, independent
code review003 and integration-004. This completes bounded implementation,
review and technical integration. T-008 remains **active** for explicit remaining
qualification; this is not Jim's Product acceptance or installed/RC/release,
actual F_P, full-calculus or accepted-result benefit qualification.

| Current source | SHA-256 |
|---|---|
| `code/ac_support_core.py` | `842f3f136478b6948196fdd431f207f236c8c3e6ebb5573503726061c5d7bcc5` |
| `code/ac_support_effects.py` | `23dfafb2d7177d64287fc22002ec039ecc451d03c864a647f3c2deade7b2145c` |
| `code/ac_support.py` | `4d41a2373def237136cefe8b186c196c2e4376137c221ae4675c274abed5ad31` |
| `test_env/test_ac_support_core.py` | `c2ff9be121ee7ccdf6974e257c0d3f0e86b6f92c84a7020d5f2b1f632cd0530f` |
| `test_env/test_ac_support_effects.py` | `d944ba73369d3c672ba1b830419260f239d8d1bbfdc6558461412ae1f8978dda` |
| `test_env/test_ac_support_interfaces.py` | `597f33aae147fdc0ecc7c85638bf77615a59b856f6ee4ffe65041d1e9b82ef9e` |

The operative reviewed HOW network remains
`d08fe97e4920b10030eb0406325503772e678d9ed0391394558cfc358b59ff7b`, with
the separate existing ontology/design dispositions and conditional premises.
The [HOW](../../../build_tenants/graphify/design/fd-support.md) now has only
factual opening updates, whole-document SHA-256 `{how_after}`;
the complete body beginning `## Boundary and method binding` is unchanged from
HOWe3c5 and the reviewed network. Profilebdb, installed builder, common normative
WHAT and Product Definition remain unchanged.

The consumed [review003](../../comments/codex/t008-platform-code-review-003/REVIEW.md)
is `e4d97b80b9973cabfba5019bc93226836733461adfb03143f38f1dd2fc2bbc7c`,
closed publication `a972ca4ccb1fbdad4f837329395507e6dd4ab310d4cfead2f6fc211164c95bbb`.
It reports scoped E10/E11 satisfied and no actionable supported current defect;
other prior scoped results keep their prior limits. Old review002 F remains
bound to its old source. This does not qualify F_P actors or a public operator.

The consumed [integration-004](../../qualification/t008/interfaces/integration-004/CLOSED_RETURN.json)
is `b895994e7c43e6c8da750828fe0899edf221988721430d0fb8a748d5d08a1175`:
one full run passed 281 tests/zero skips in 58.068s; strict normal-import checks
passed nine files and ten fresh ordinary CLI/MCP demo checks passed. Nine actual
upstream checks are retained from integration-003 with exact unchanged boundary
applicability, not a new standalone run. Earlier 242/254/273-test cuts and all
original/repaired failure evidence remain historical.

The [handoff index](../../qualification/t008/handoff-001/README.md) and
[projection](../../qualification/t008/handoff-001/PROJECTION.json) retain the
remaining operation/variant/host limits, ten current owning-witness gaps and
original expectation-source/independence limits. The real Worker timed out
without a closed return; phase1 was partial/indeterminate with an unconsumable
check and phase2 timed out without a final assessment. No later technical S
erases those facts. FD capability work and partial FDV qualification are Active;
FDV-003 accepted-result benefit remains Deferred/unqualified.

Binding002 at original lines785–860 is byte-exact **HISTORICAL/stale**. Its old
HOW/Core/source pins and runtime configurations are not renewed, repinned or
current authority. No binding003, native-call budget, retry, runtime policy or
future real effect is selected. Future effects need separately selected exact
current authority/basis and material preconditions.

The full [before ticket](../../qualification/t008/handoff-001/before/.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md)
retains all original bytes, including the earlier 52,350-byte prefix. Current
ticket differences are exactly the two authorized top navigation lines and this
append; the modified prefix is not claimed byte-exact current. The guide has
only a historical-cut header note; its original `Status:` and remainder are
unchanged. Complete raw-document pins in earlier reviews/integrations now name
their historical documents, while identical code/tests and unchanged normative
requirement/design bodies support only the explicit bounded applicability.
"""
edits[ticket].append({"start": len(before[ticket]), "end": len(before[ticket]), "replacement": append, "scope": "latest Root disposition/work result append only"})

plan = []
for row in before_rows:
    relative = row["path"]
    assert edits[relative], relative
    assert (P / relative).read_bytes() == before[relative], relative
    after = render(relative)
    assert after != before[relative]
    plan.append({"path": relative, "before_sha256": row["sha256"], "after_sha256": digest(after),
        "edits": sorted(edits[relative], key=lambda item: (item["start"], item["end"]))})
with (D / "EDIT_PLAN.json").open("x", encoding="utf-8") as stream:
    json.dump({"scope": "Only externally authorized factual regions; byte offsets refer to retained before files", "sources": plan}, stream, indent=2, sort_keys=True)
    stream.write("\n")
for row in plan:
    (P / row["path"]).write_bytes(render(row["path"]))
print(json.dumps({"changed_existing_sources": len(plan), "HOW_after_sha256": how_after, "tests_or_runtime_calls": 0}))
