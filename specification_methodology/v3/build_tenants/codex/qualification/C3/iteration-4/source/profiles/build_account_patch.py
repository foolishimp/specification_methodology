"""Serialize the Writer's authored arguments as an integration patch, not a model."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
TENANT = OUT.parents[4]
STANDARDS = TENANT / "successor/standards"
PREIMAGE = "199c6d29bc02590a8b7f252043fc43223c09808d"
ACCOUNT = "specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/DETERMINATIONS.json"
raw = subprocess.check_output(["git", "show", PREIMAGE + ":" + ACCOUNT])
account = json.loads(raw)
by_id = {row["id"]: row for row in account["determinations"]}

# These instance premises and scope guards are authored for the changed owners.
bindings = {
    "AXIOMATIC_CALCULUS": {
        "anchor": "fundamental-laws",
        "instance_premises": [
            "A governed symbolic model represents a separately identified subject under a selected signature and interpretation.",
            "Some predicates admit mechanical decision and others require semantic judgment; selection of the finite signature and record families remains calculus policy."
        ],
        "scope_guard": "Arguments apply under each named calculus law, with subject interpretation and application authority separately bound. A constraint supplies its own predicate; a universal purpose field is not added.",
    },
    "DESIGN_MODULE_METHOD": {
        "anchor": "governing-relations",
        "instance_premises": [
            "The governing WHAT owns required Product meaning; a realization can place it in several carriers.",
            "A later actor may act on a boundary without the author's private reasoning, so its governing contracts must be recoverable."
        ],
        "scope_guard": "Generic design-contract law applies where selected; optional Ontology, Prime/IACS, diagrams, language and functional-profile policies keep their separate adoption, modal force and exceptions.",
    },
    "ODD_METHOD": {
        "anchor": "governing-relations",
        "instance_premises": [
            "A Product adopts the graph-native profile and supplies its selected outcome and domain meanings.",
            "Workers may change the workspace; the bound runtime admits evidence and governs traversal, leaving outcome, observation, admission and continuation distinct."
        ],
        "scope_guard": "The graph, ledger and four-function architecture is ODD policy within adoption; operation kind, actor and executor remain distinct. Other profiles retain their own selection.",
    },
    "TRAVERSAL_OCCURRENCE_PROFILE": {
        "anchor": "governing-relations",
        "instance_premises": [
            "The adopting Product selects one exact calculus basis and a compatible occurrence signature.",
            "The external subject can change while retaining a stable subject binding.",
            "Each effect is a separately identified operation requiring its actual owner-issued grant."
        ],
        "scope_guard": "Availability and occurrence construction do not adopt the profile. Its finite signature, immutable history and atomic semantic cut supply no scheduler, lock, transaction, rollback or effect-idempotence guarantee.",
    },
    "WORLD_MODEL_METHOD": {
        "anchor": "governing-relations",
        "instance_premises": [
            "Source systems enact domain function and retain operational sovereignty; records are evidence whose meaning must be recovered.",
            "Only some builders additionally use a metric representation where identity is a geometric direction; that condition selects overlay construction, not ordinary entity recovery."
        ],
        "scope_guard": "Sparse entity-cut publication, optional geometric overlays and the separate unmet statistical promotion predicate retain distinct conditions. ODD execution and Design theory are no implicit prerequisites.",
    },
    "UX_METHOD": {
        "anchor": "governing-relations",
        "instance_premises": [
            "The Product owns admitted truth and action contracts; its governed UX renders that truth and requests changes.",
            "Data can cross seams the UX does not control, and implementation stacks offer different state and effect mechanisms."
        ],
        "scope_guard": "The governing surface follows existing adoption/default-coverage clauses. TEA, accessibility and stack choices are distinct policies. Ambiguity retains exactly the 1A exits, including design-module exemption; 13A scaffold exemptions may use design or ticket.",
    },
}

patches = []
audit_when = "Only when assessing this argument's applicability, consequence, conservation or fidelity against the named consuming clause; this is not an unconditional operational dependency."
for member, binding in bindings.items():
    identity = member + "." + binding["anchor"]
    original = by_id[identity]
    text = (STANDARDS / (member + ".md")).read_text()
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Determination and consuming law |"))
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        assert len(cells) == 3
        family, consequence, policy = cells
        loci = [{"path": "standards/" + member + ".md", "anchor": anchor,
                 "role": "provenance", "required_when": audit_when}
                for anchor in re.findall(r"\]\(#([^)]*)\)", family)]
        rows.append({
            "family": family,
            "premises": sorted(set(re.findall(r"\bF[1-6]\b", consequence))),
            "conditional_consequence": consequence,
            "additional_policy_and_owner": policy,
            "audit_consumer_loci": loci,
            "source_row_sha256": hashlib.sha256(line.encode()).hexdigest(),
            "source_refs": [identity],
            "required_when": audit_when,
        })
    argument = {
        "premises": [{"id": "FOUNDATIONS.foundational-commitments", "kind": "adopted_foundation",
                      "standing": "conditional on the source owner's applicable F1-F6 premises"}],
        "instance_premises": binding["instance_premises"],
        "conditional_consequence": "Each authored source-family row below states the consequence and additional choice for its named consumers; the rows do not add a Boolean gate or confer a grant.",
        "policy_choices": [row["additional_policy_and_owner"] for row in rows],
        "source_family_arguments": rows,
        "source_refs": [identity, "FOUNDATIONS.foundational-commitments"],
        "scope_guard": binding["scope_guard"],
        "standing": "Writer-authored conditional argument; no independent entailment or fidelity proof",
    }
    patches.append({
        "id": identity,
        "owner": {"path": original["owner"]["path"], "anchor": original["owner"]["anchor"]},
        "change_class": "argument_and_consumer_explanation; existing normative predicates and result mappings preserved",
        "set": {"argument": argument},
        "preserve": ["predicate", "obligations", "permissions_exceptions", "dependencies", "consumers", "result_mapping"],
        "coverage_note": "The authored rows bind the displayed material families. They do not assert a fresh read or independent proof of every nested policy in the member.",
    })

identity = "ODD_METHOD.118-cumulative-environment-law-is-mandatory"
original = by_id[identity]
patches.append({
    "id": identity,
    "owner": {"path": original["owner"]["path"], "anchor": original["owner"]["anchor"]},
    "change_class": "explicit shared-composition consumer binding; source modal force preserved; pre-existing interpretation modal error corrected",
    "set": {
        "predicate": "Composition uses a cumulative typed environment in which each material required binding remains available when consumed, including earlier carried bindings; declaring environment.requires/provides/carries is the profile's stated recommendation.",
        "argument": {
            "premises": ["F2", "F4", "F6"],
            "instance_premises": ["A retained graph function may require typed bindings produced before its immediate predecessor."],
            "conditional_consequence": "Last-output-only wiring cannot supply an earlier required binding. At the consuming function, shared composition evaluates every material required input; presence alone does not establish currentness, compatible basis or operation authority.",
            "policy_choices": ["The cumulative environment is ODD policy. The requires/provides/carries declarations retain source should force."],
            "source_refs": [identity, "ODD_METHOD.governing-relations"],
            "standing": "Writer-authored consumer binding; not independent fidelity evidence",
        },
        "obligations": original["obligations"] + ["Apply shared composition at the consuming function to every material required binding, including carried inputs, with its currentness, basis and actual authority."],
        "dependencies": list(dict.fromkeys(original["dependencies"] + ["TRANSFORMATION_LIBRARY.composition-law"])),
    },
    "preserve": ["permissions_exceptions", "consumers", "result_mapping"],
    "prior_interpretation_defect": {
        "old_predicate": original["predicate"],
        "source_condition": "Each retained GraphFunction should declare environment.requires, environment.provides and environment.carries.",
        "reason": "The previous predicate made the recommended declaration unconditional. The source body retains should; the patch restores that distinction while preserving mandatory cumulative composition.",
    },
})

result = {
    "schema": "I4-profile-authored-account-patch-v1",
    "activation": "I4-PROFILE-SOURCE",
    "preimage": PREIMAGE,
    "base_account": ACCOUNT,
    "base_account_sha256": hashlib.sha256(raw).hexdigest(),
    "standing": "authored semantic integration input; current account, program, map and views remain untouched",
    "dependency_policy": "Consumer loci inside family arguments are provenance, conditionally acquired only to assess that argument. Do not promote them into unconditional operational dependencies or native-selector fan-out. Preserve the existing conditional/provenance acquisition machinery.",
    "source_coordinates": "Integration resolves fresh source-block lines/digests at the combined freeze; stable existing heading identities are used here.",
    "patches": patches,
    "remaining_bindings": [
        "Refresh the existing ARGUMENT_ROUTES relation and affected consumer argument fields from these exact rows under the source-specific matching rules; the pre-existing broad-family routes may no longer select the right row.",
        "Audit propagation through changed nested family, policy, applicability and consumer dependencies before interpreting these expanded rows as complete per-determination coverage.",
        "Preserve result/predicate/effect mappings; no source result mapping changes are requested by this patch.",
    ],
}
(OUT / "ACCOUNT_PATCH.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"patches": len(patches), "argument_rows": sum(len(p["set"].get("argument", {}).get("source_family_arguments", [])) for p in patches)}))
