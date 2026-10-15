"""Author scoped semantic-field amendments; never write an integrated account."""
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
TENANT = OUT.parents[4]
REPO = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
SOURCE_COMMIT = subprocess.check_output(["git", "rev-parse", "cd19955"], text=True).strip()
SOURCE_FREEZE = subprocess.check_output(["git", "rev-parse", "0044d45"], text=True).strip()
PREIMAGE = "199c6d29bc02590a8b7f252043fc43223c09808d"
ACCOUNT = TENANT / "qualification/C3/iteration-4/DETERMINATIONS.json"
EXPECTED_ACCOUNT_SHA = "b8c43489311b387045de129db459ef1bf29c1334724fcccc36474ea9565fedcd"
raw = ACCOUNT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_ACCOUNT_SHA, "Provisional input drift"
current = json.loads(raw)
old_path = TENANT / "qualification/C3/iteration-3/DETERMINATIONS.json"
old_raw = subprocess.check_output(["git", "show", PREIMAGE + ":" + str(old_path.relative_to(REPO))])
old = json.loads(old_raw)
by_id = {row["id"]: row for row in current["determinations"]}
old_by_id = {row["id"]: row for row in old["determinations"]}
MEMBERS = ["AXIOMATIC_CALCULUS", "DESIGN_MODULE_METHOD", "ODD_METHOD", "TRAVERSAL_OCCURRENCE_PROFILE", "WORLD_MODEL_METHOD", "UX_METHOD"]
AUDIT_WHEN = "When assessing the source-family argument, its applicability or fidelity for this exact consumer; not an unconditional operational prerequisite."
family_rows, heading_info, source_pins = {}, {}, []

for member in MEMBERS:
    path = TENANT / "successor/standards" / (member + ".md")
    repo_path = str(path.relative_to(REPO))
    source = subprocess.check_output(["git", "show", SOURCE_COMMIT + ":" + repo_path])
    frozen = subprocess.check_output(["git", "show", SOURCE_FREEZE + ":" + repo_path])
    assert source == frozen == path.read_bytes(), member + " source drift"
    previous = subprocess.check_output(["git", "show", PREIMAGE + ":" + repo_path]).decode()
    text = source.decode()
    prior_heads = list(re.finditer(r"^#{1,6} .+$", previous, re.M))
    heads = list(re.finditer(r"^#{1,6} .+$", text, re.M))
    assert [m.group() for m in heads] == [m.group() for m in prior_heads]
    source_hash = hashlib.sha256(source).hexdigest()
    source_pins.append({"path": repo_path, "sha256": source_hash, "bytes": len(source), "identical_at": [SOURCE_FREEZE, SOURCE_COMMIT]})
    info = {}
    for previous_head, head in zip(prior_heads, heads):
        old_line = previous[:previous_head.start()].count("\n") + 1
        owners = [row for row in old["determinations"] if row["owner"]["path"] == "standards/" + member + ".md" and row["owner"]["start_line"] == old_line]
        if not owners:
            continue
        assert len(owners) == 1
        anchor = owners[0]["owner"]["anchor"]
        level = len(head.group().split(" ", 1)[0])
        end = next((other.start() for other in heads if other.start() > head.start() and len(other.group().split(" ", 1)[0]) <= level), len(text))
        info[anchor] = {"start": head.start(), "end": end, "level": level, "title": head.group()}
    heading_info[member] = info
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Determination and consuming law |"))
    owner_anchor = "fundamental-laws" if member == "AXIOMATIC_CALCULUS" else "governing-relations"
    rows = []
    for offset, line in enumerate(lines[start + 2:], start + 3):
        if not line.startswith("|"):
            break
        family, consequence, policy = [x.strip() for x in line.split("|")[1:-1]]
        anchors = re.findall(r"\]\(#([^)]*)\)", family)
        assert all(anchor in info for anchor in anchors), (member, anchors)
        rows.append({
            "family": family,
            "declared_consumer_scope": family,
            "premises": sorted(set(re.findall(r"\bF[1-6]\b", consequence))),
            "conditional_consequence": consequence,
            "additional_policy_and_owner": policy,
            "source_row": {"path": "standards/" + member + ".md", "anchor": owner_anchor,
                           "line": offset, "sha256": hashlib.sha256(line.encode()).hexdigest(),
                           "source_commit": SOURCE_COMMIT, "member_sha256": source_hash},
            "source_refs": [member + "." + owner_anchor],
            "source_reference_role": "provenance",
            "required_when": AUDIT_WHEN,
            "audit_consumer_loci": [{"path": "standards/" + member + ".md", "anchor": anchor,
                                     "role": "provenance", "required_when": AUDIT_WHEN} for anchor in anchors],
        })
    family_rows[member] = rows
assert sum(map(len, family_rows.values())) == 45

# Explicit policy references and ranges in the current source supplement exact
# linked-heading/descendant matching. Zero-based row indexes are local to the
# frozen member. These bindings are authored, not inferred from old row names.
manual = {}
def bind(member, anchors, rows, reason, *, row_member=None, scope=None, residual=None):
    for anchor in anchors.split():
        manual[member + "." + anchor] = {
            "matches": [(row_member or member, index) for index in rows],
            "kind": "explicit_source_policy_binding",
            "reason": reason,
            "scope": scope or "Only the consumer's already-adopted relation and local conditions; additional local policies and exceptions retain their own force.",
            "residual": residual,
        }

bind("DESIGN_MODULE_METHOD", "3-core-rule 3b-ingress-collapse-rule 4a-python-typing-rule 7-immutable-carrier-rule 10-no-semantic-center-rule 11-coupling-rule 12-interface-bleed-prohibition 13-proxy-interface-prohibition", [6],
     "The current functional-seams row explicitly retains functional preferences, ingress/interface policies, conditional Python duties and effect boundaries; each listed consumer instantiates only that part of the argument. Its own predicate, mutation exceptions, modal force and authority conditions remain unchanged.")
bind("DESIGN_MODULE_METHOD", "3a-odd-alignment-and-escalation-rule", [0, 1],
     "The consumer explicitly selects ODD's published graph carrier and traversal/control ownership before deterministic module realization. The current ODD rows explain those two duties; Design's local escalation and closure conditions remain its own.", row_member="ODD_METHOD",
     scope="Only when Design is used inside an ODD-governed Product and the boundary is an operative graph traversal; this provenance binding does not adopt ODD elsewhere.")
bind("DESIGN_MODULE_METHOD", "5b-promotion-test 5c-boundary-inflation-prohibition prime-semantic-atoms-and-universal-domain whole-family-prime-contraction", [3],
     "The current Prime/carrier-set row names Prime atoms, whole-family contraction, IACS and promotion/boundary-cost tests. The consumers supply the concrete promotion grounds and subordinate-payload distinctions; no numerical minimum or unique realization is inferred.")
bind("DESIGN_MODULE_METHOD", "5d-reference-derived-module-design-rule 6b-module-derived-unit-test-rule 11b-opportunistic-optimization-rule 11c-recurrence-extraction-rule 11d-post-ticket-design-review-rule", [7],
     "The current design-views/proof row names module-derived proof, reference derivation, optimization, recurrence and post-ticket review with their local scope/re-entry limits. Each consumer supplies those limits rather than inheriting every policy of the row.")
bind("DESIGN_MODULE_METHOD", "14-design-review-questions", [7],
     "The source review clause is an evidence route to applicable owning policies, not another definition of them. This row supports assessment/acceptance separation and exact-claim evidence; the review's question-family table continues to select its concrete required owners.",
     residual="This match does not assert that one evidence argument derives every question-family policy. Their existing owning clauses and task applicability remain required.")
bind("DESIGN_MODULE_METHOD", "14a-functional-realization-review-checklist", [6, 7],
     "The source explicitly selects section 4's functional policies and section 14's evidence routes for the exact claim, retains proportional sequencing and unchanged-boundary reuse, and adds no duplicate gate.",
     scope="Only a claim of functional bias, pure transforms, immutable carriers, single-owner truth or low coupling selects this review. Applicable ODD proof remains separately conditional.")
manual["DESIGN_MODULE_METHOD.11a-governancestrategy-separation-rule"] = {
    "matches": [], "kind": "unresolved_applicability",
    "reason": "No current family row explicitly binds the governance-versus-strategy policy and its ratified-strategy-ownership exception. The old broad functional-family copy cannot establish that missing argument.",
    "scope": "The existing local governance/strategy predicate and its declared exception remain operative; only the family-argument coverage claim stays unresolved.",
    "residual": "A source-owned argument must explain this policy and exception before complete argument coverage can be claimed for it.",
}

bind("ODD_METHOD", "111-typed-assets-and-nodes-are-explicit 112-graph-functions-are-the-primary-constructive-carrier 112a-outcome-first-realization-order 113-the-function-catalog-is-published 114-the-gtl-module-is-the-operative-publication-surface", [0],
     "The current row explicitly declares the 11.1–11.4 consumer range; local carrier, catalog and outcome-first realization conditions remain separately owned within that range.")
bind("ODD_METHOD", "5-graph-model nodes vectors graph-functions", [0],
     "The graph model and its nodes/vectors/functions supply the typed assets, operative carriers and composition inputs named by the current published-carrier row. Its later proof and control claims do not follow merely from graph shape.")
bind("ODD_METHOD", "traversal", [0, 2],
     "The source traversal binds a current target, locates lawful vectors, materializes assets and proves closure. These are the typed carrier and outcome/action relations named by the current rows; their detailed runtime and closure laws remain independent obligations.")
bind("ODD_METHOD", "probabilistic-compute", [1],
     "The source separates worker-internal HOW from runtime authority and binds operation kind independently of actor/mechanism, which is the current control-ownership row's limited contribution.",
     scope="Only the operation/actor/control-authority distinction is covered by this match. Preserve the local bounded-compute contract and both directional semantic specialization relations in full.",
     residual="The current family table does not independently explain the complete F_P/F_H directional specialization and all internal-HOW latitude. Those additional source-owned arguments remain outside this row match.")
bind("ODD_METHOD", "115-current-state-is-a-projection-over-constructive-history", [3],
     "The current observation/lineage/recovery row distinguishes the account from mutable reality and requires authenticated current support; the projection clause supplies its exact source and history relation.")
bind("ODD_METHOD", "115a-abg-owns-continuation-and-re-entry 115b-execution-authority-audit", [1],
     "The current control-ownership row names ABG admission/traversal ownership and separate operation grants. These consumers supply the runtime ownership and audit surfaces; audit evidence does not itself transfer a role.")
bind("ODD_METHOD", "116-product-specific-semantics-sit-above-the-shared-carrier 4-method-folder-semantics 6-product-boundary 7-self-host-boundary-rule", [7],
     "The current Product-boundaries row explicitly retains common/domain/local ownership, method-folder conventions and Product/self-host boundaries. Each consumer binds its own local meaning and immutable dependency identity.")
bind("ODD_METHOD", "117-manual-walkthrough-must-still-be-lawful 117a-conforming-agentic-development", [6],
     "The current authority-path/process row explicitly names manual and agentic walkthrough as scoped evidence policies; the exact consumer's admission, evidence and conformance conditions are preserved.")
bind("ODD_METHOD", "12-scenario-rule 13-installed-dev-rule 14-dogfooding-rule 15-release-boundary 16-failure-pattern", [6],
     "The current row explicitly includes sections 12–16 and the scenario/installed-dev/dogfooding/release policies; the failure patterns diagnose those source-owned rules rather than introducing another verdict algebra.")
bind("ODD_METHOD", "19-ramp-up-checklist", [7],
     "The current Product/acquisition row explicitly includes ramp-up questions; actual Product sources, selected profile applicability and operation authority remain necessary.")

def select(identity):
    if identity in manual:
        return manual[identity]
    member, anchor = identity.split(".", 1)
    consumer = heading_info[member][anchor]
    choices = []
    for index, row in enumerate(family_rows[member]):
        for locus in row["audit_consumer_loci"]:
            target = heading_info[member][locus["anchor"]]
            if locus["anchor"] == anchor:
                choices.append((999, index, locus["anchor"], "exact_consumer_link"))
            elif target["start"] <= consumer["start"] < target["end"]:
                choices.append((target["level"], index, locus["anchor"], "scoped_heading_descendant"))
    if not choices:
        return {"matches": [], "kind": "unresolved_applicability", "reason": "No exact current-row link, descendant scope or authored policy binding resolves this prior copy.", "scope": "Local law remains preserved; family support is unresolved.", "residual": "Resolve this consumer's family argument before claiming complete argument coverage."}
    most_specific = max(x[0] for x in choices)
    chosen = [x for x in choices if x[0] == most_specific]
    return {"matches": [(member, index) for index in dict.fromkeys(x[1] for x in chosen)],
            "kind": chosen[0][3], "reason": "Current source selects " + ", ".join(dict.fromkeys(x[2] for x in chosen)) + "; a more-specific linked heading takes precedence over a broader ancestor only for routing this argument.",
            "scope": "Only this consumer's local adopted relation and required portions of the named family; descendant matching neither derives every local policy nor transfers authority.", "residual": None}

patches = {}
coverage = []
def item(identity):
    if identity not in patches:
        row = by_id[identity]
        patches[identity] = {"id": identity, "owner": {"path": row["owner"]["path"], "anchor": row["owner"]["anchor"]}, "set": {}, "preserve_local_semantics": "Unmentioned semantic fields, predicates, local definition payloads, permissions, exceptions, source applicability and result/effect mappings remain byte-equal."}
    return patches[identity]

# Every legacy consumer copy, including the ODD 11.8 copy replaced by the first
# source patch, has a current scoped route or an explicit unresolved relation.
for previous in old["determinations"]:
    identity = previous["id"]
    member = identity.split(".", 1)[0]
    if member not in MEMBERS:
        continue
    for field in ["definition", "argument"]:
        previous_value = previous.get(field)
        if not isinstance(previous_value, dict) or not previous_value.get("source_family_arguments"):
            continue
        current_value = by_id[identity].get(field, {})
        old_rows = previous_value["source_family_arguments"]
        if field == "definition" and identity.endswith(".governing-relations"):
            decision = {"matches": [(member, index) for index in range(len(family_rows[member]))], "kind": "complete_owner_table", "reason": "Definition carries the exact current source-owned family table, as provenance for argument assessment.", "scope": "This is an argument-definition account, not an activation of every consumer.", "residual": None}
        else:
            decision = select(identity)
        selected = []
        for row_member, index in decision["matches"]:
            new_row = copy.deepcopy(family_rows[row_member][index])
            new_row["consumer_binding"] = {"path": by_id[identity]["owner"]["path"], "anchor": by_id[identity]["owner"]["anchor"], "kind": decision["kind"], "reason": decision["reason"], "scope": decision["scope"], "required_when": AUDIT_WHEN}
            selected.append(new_row)
        patch = item(identity)
        patch["set"][field + ".source_family_arguments"] = selected
        patch["set"][field + ".source_family_applicability"] = {
            "standing": "unresolved" if not selected else "scoped_with_residual" if decision["residual"] else "scoped_source_match",
            "kind": decision["kind"], "reason": decision["reason"], "scope": decision["scope"],
            "residual": decision["residual"], "required_when": AUDIT_WHEN,
            "operational_dependency_effect": "No change to local applicability or operational dependency sets; this accounts for source-family explanation only.",
        }
        # Replace only the exact old generated family summaries. Preserve any
        # more-specific authored premises, policy choices and consequences.
        if field == "argument":
            generic = "Apply the exact source-family argument(s) below only in their declared consumer scope. Their consequence does not imply their additional chosen policies."
            generic_current = current_value.get("conditional_consequence") == generic
            old_choices = [x["additional_policy_and_owner"] for x in old_rows]
            policies = current_value.get("policy_choices")
            if generic_current and policies == old_choices:
                patch["set"]["argument.policy_choices"] = list(dict.fromkeys(x["additional_policy_and_owner"] for x in selected))
            previous_premises = sorted(set(p for x in old_rows for p in x.get("premises", [])))
            if generic_current and isinstance(current_value.get("premises"), list) and all(isinstance(x, str) for x in current_value["premises"]) and sorted(current_value["premises"]) == previous_premises and selected:
                patch["set"]["argument.premises"] = sorted(set(p for x in selected for p in x.get("premises", [])))
            if not selected and current_value.get("conditional_consequence") == generic:
                patch["set"]["argument.conditional_consequence"] = "The local governing rule and its exception remain operative. Applicability of the current family arguments to this additional policy is unresolved; no complete argument-coverage conclusion follows from the removed historical copy."
                patch["set"]["argument.policy_choices"] = ["This local owner requires governance truth rather than imperative strategy unless strategy ownership is explicitly part of the boundary's ratified responsibility; the current table does not independently establish that policy argument."]
        coverage.append({"id": identity, "field": field, "prior_rows": len(old_rows), "current_rows": len(selected), "match_kind": decision["kind"], "current_families": [{"member": m, "row_ordinal": i + 1, "family": family_rows[m][i]["family"].split(":", 1)[0]} for m, i in decision["matches"]], "standing": patch["set"][field + ".source_family_applicability"]["standing"], "residual": decision["residual"], "old_source_row_hashes_retired": [x.get("source_row", {}).get("sha256") for x in old_rows]})

# Rebind only the result predicate; preserve the five verdicts, actual
# performance, effects and coverage meanings byte-for-byte.
identity = "ODD_METHOD.118-cumulative-environment-law-is-mandatory"
row = by_id[identity]
patch = item(identity)
assert row["result_mapping"]["bound_predicate"] != row["predicate"]
patch["set"]["result_mapping.bound_predicate"] = row["predicate"]
relation = {
    "id": "TRANSFORMATION_LIBRARY.composition-law", "kind": "composition_contract",
    "required_when": "Within an adopted ODD scope, when a retained graph function consumes material required bindings, including inputs carried across intermediate functions.",
    "binding": "Evaluate each actual required input and material join at the consuming function, including compatible type/basis, current support and the actual operation grant. Merely having a binding is insufficient. The requires/provides/carries declarations remain the source's should recommendation; that recommendation is not a mandatory satisfaction conjunct.",
    "source_refs": ["ODD_METHOD.118-cumulative-environment-law-is-mandatory"],
}
relations = copy.deepcopy(row["dependency_relations"])
existing = [index for index, rel in enumerate(relations) if rel.get("id") == relation["id"]]
assert len(existing) <= 1
if existing:
    relations[existing[0]] = relation
else:
    relations.append(relation)
patch["set"]["dependency_relations"] = relations
patch["set"]["dependencies"] = list(dict.fromkeys(row["dependencies"] + [relation["id"]]))
patch["result_mapping_change"] = "Only bound_predicate changes. All five verdict definitions, performance, effects and coverage remain identical. The source recommendation is retained as latitude, not promoted to a mandatory obligation."

# Audit the already-updated six owner arguments against the exact 45 frozen rows.
owner_audit = []
for member in MEMBERS:
    anchor = "fundamental-laws" if member == "AXIOMATIC_CALCULUS" else "governing-relations"
    identity = member + "." + anchor
    existing = by_id[identity]["argument"]["source_family_arguments"]
    current_hashes = [x["source_row"]["sha256"] for x in family_rows[member]]
    observed_hashes = [x.get("source_row_sha256", x.get("source_row", {}).get("sha256")) for x in existing]
    assert current_hashes == observed_hashes, identity + " current owner rows drift"
    owner_audit.append({"id": identity, "rows": len(existing), "current_source_hashes_verified": True, "modified": False})

profile_origins = [{"path": "standards/" + member + ".md", "anchor": "fundamental-laws" if member == "AXIOMATIC_CALCULUS" else "governing-relations", "id": member + (".fundamental-laws" if member == "AXIOMATIC_CALCULUS" else ".governing-relations")} for member in MEMBERS]
for amendment in patches.values():
    amendment["family_array_scopes"] = {
        dotted: {
            "operation": "replace_matching_origins",
            "origins": profile_origins,
            "match": "Match source_row.path plus source_row.anchor, or an exact owning-table id in source_refs. A row without one of these profile origins is outside this replacement.",
            "preserve_other_current_families": True,
        }
        for dotted in amendment["set"] if dotted.endswith(".source_family_arguments")
    }
    amendment["generated_summary_preimages"] = {
        dotted: {
            "held_preimage": by_id[amendment["id"]]["argument"].get(dotted.split(".")[1]),
            "integration_rule": "Apply this profile-generated summary replacement only while retaining contributions from other current families and any more-specific local argument. If the field changed since the held preimage, merge by family origin rather than overwrite the current field."
        }
        for dotted in amendment["set"] if dotted in ["argument.premises", "argument.policy_choices", "argument.conditional_consequence"]
    }

result = {
    "schema": "I4-profile-routing-dotted-semantic-patch-v1",
    "activation": "I4-PROFILE-ACCOUNT-ROUTES",
    "standing": "Writer-authored account amendments for integration and independent review; not an integrated account or fidelity qualification",
    "subject": {"source_commit": SOURCE_COMMIT, "source_freeze": SOURCE_FREEZE, "source_members": source_pins,
                "provisional_account_path": str(ACCOUNT.relative_to(REPO)), "provisional_account_sha256": EXPECTED_ACCOUNT_SHA,
                "historical_account_commit": PREIMAGE, "historical_account_sha256": hashlib.sha256(old_raw).hexdigest()},
    "application": "Each set key is a dotted semantic-field path under the named determination. Apply after the direct profile patches. Family arrays use family_array_scopes: replace only rows from the six named profile origins and preserve every current foreign/core family. Plain dotted replacement is valid only against the held provisional preimage without foreign additions. Generated summaries use generated_summary_preimages to preserve foreign contributions and more-specific local arguments. Preserve all unmentioned fields. Do not interpret retired hashes in COVERAGE.json as current source hashes.",
    "acquisition_policy": "source_refs and audit_consumer_loci are provenance; family matches are acquired only for argument/applicability/fidelity assessment. They create no blanket mandatory profile acquisition. Only the explicit ODD composition_contract relation adds a typed deciding dependency, conditional on its actual source use.",
    "patches": list(patches.values()),
    "owner_argument_audit": owner_audit,
}
(OUT / "ACCOUNT_PATCH.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
(OUT / "COVERAGE.json").write_text(json.dumps({"activation": result["activation"], "source_commit": SOURCE_COMMIT, "entries": coverage, "owner_argument_audit": owner_audit, "limits": ["Scoped source matches do not independently establish entailment or complete nested-policy coverage.", "Explicit unresolved applicability and scoped residuals remain open; old copied arguments are not retained as current."]}, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"patches": len(patches), "copy_locations": len(coverage), "consumer_copies": sum(x["field"] == "argument" for x in coverage), "owner_definitions": sum(x["field"] == "definition" for x in coverage), "unresolved": [x["id"] for x in coverage if x["standing"] == "unresolved"], "scoped_residuals": [x["id"] for x in coverage if x["standing"] == "scoped_with_residual"]}))
