#!/usr/bin/env python3
"""Independent exact-input conservation checks. Writes only this asset directory."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import difflib, hashlib, json, re, subprocess

OUT = Path(__file__).resolve().parent
MAIN = Path("/Users/jim/src/apps/specification_methodology")
TENANT = Path("/Users/jim/src/apps/specification_methodology-codex")
INSTALL = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2")
V3 = "specification_methodology/v3/"
ROOT = V3 + "build_tenants/codex/"
BASE = ROOT + "qualification/C3/iteration-5/"
ACCOUNT = "b2ad4d99a9ab6873cded9ffdfbc416ef1e0e23a5"
SOURCE = "1e4bed65fe2216b288903ea553391c45ff90e9c1"
SEMANTIC = "57f711d964cd4eac8ed8523460cecc68bcaa63fb"
I4 = "01b01274b244ae6e5de10bf6bacb60087462cbb5"
HANDOFF = "62318d3b0be35985a0397aa39daee0ec8836eabc"
COMMON = "4c340f7adec9f3c893e3e267b23e4cadeb357854"
DONOR = "c66ed4e0e97ca91ebc26894eaf283ebc6c3a2e20"
MANIFEST = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"

def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(x): return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
@lru_cache(None)
def git(commit, path, repo=TENANT):
    return subprocess.check_output(["git", "show", commit + ":" + path], cwd=repo)
def load(path): return json.loads(git(ACCOUNT, BASE + path))
def write(name, value): (OUT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+"\n")
checks = []
def check(name, condition, details=None):
    checks.append({"check": name, "passed": bool(condition), "details": details})

def slug(text):
    return re.sub(r"[^\w\- ]", "", re.sub(r"<[^>]+>", "", text).lower()).replace(" ", "-")

@lru_cache(None)
def sections(raw):
    lines = raw.decode().splitlines(keepends=True)
    heads, seen, fence = [], Counter(), None
    for i, line in enumerate(lines):
        m = re.match(r"^\s*("+chr(96)+r"{3,}|~{3,})", line)
        if m:
            mark = m.group(1)[0]
            if fence is None: fence = mark
            elif mark == fence: fence = None
            continue
        if fence: continue
        m = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line.rstrip("\r\n"))
        if m:
            base = slug(m.group(1))
            anchor = base if seen[base] == 0 else base+"-"+str(seen[base])
            seen[base] += 1
            heads.append((i,anchor))
    return {anchor:"".join(lines[start:heads[n+1][0] if n+1<len(heads) else len(lines)]).encode()
            for n,(start,anchor) in enumerate(heads)}

def section(raw, route):
    return raw if "#" not in route else sections(raw)[route.split("#",1)[1]]
def source_bytes(commit, route):
    raw = git(commit, ROOT+"successor/"+route.split("#",1)[0])
    return raw, section(raw, route)

a,f,q = (load(n) for n in ("CONSERVATION.json","FRONTIER.json","REPLACEMENT_QUESTIONS.json"))
p,s = (load(n) for n in ("source/account/PROPOSALS.json","source/account/SOURCE_COMPARISON.json"))
old_raw = git(a["preimage"]["commit"],a["preimage"]["path"])
old = json.loads(old_raw)
rows,old_rows,frontier = ({r["id"]:r for r in value["rows"]} for value in (a,old,f))
check("installed_manifest_digest",sha((INSTALL/"manifest.json").read_bytes())==MANIFEST)
v = subprocess.run(["/Users/jim/.local/bin/stdo","verify","v2.5.1-rc.2","--manifest-sha256",MANIFEST],capture_output=True,text=True)
vr = json.loads(v.stdout)
check("installed_release_verification",v.returncode==0 and vr["valid"] and not vr["failures"])
check("exact_bound_subjects",a["input_commit"]==COMMON and a["candidate_source_commit"]==SOURCE and a["candidate_account_commit"]==SEMANTIC)
check("prior_digest_handoff_and_source",sha(old_raw)==a["preimage"]["sha256"] and git(HANDOFF,a["preimage"]["path"])==old_raw and old["candidate_source_commit"]==I4)
check("unique_691_identical_prior_and_frontier_ids",len(a["rows"])==len(rows)==len(old_rows)==len(f["rows"])==len(frontier)==691 and set(rows)==set(old_rows)==set(frontier))
common_raw = git(COMMON,V3+"specification/requirements/PREDECESSOR_CLAIMS.md",MAIN)
common_ids,current_member,table_kind = [],None,None
for line in common_raw.decode().splitlines():
    if line.startswith("## "):
        heading = line[3:]
        if heading.endswith(".md"): current_member = heading
        table_kind = None
    if line.startswith("| Section | Anchor |"): table_kind="section";continue
    if line.startswith("| Member | Kind | SHA-256 |"): table_kind="member";continue
    if not line.startswith("|") or line.startswith("|---"): continue
    cells = [x.strip() for x in line.strip("|").split("|")]
    if table_kind=="section" and len(cells)>1 and cells[1].startswith(chr(96)+"#"):
        common_ids.append(current_member+cells[1].strip(chr(96)))
    elif table_kind=="member" and cells[0].startswith(chr(96)):
        member = cells[0].strip(chr(96))
        if not member.startswith(("standards/","plugins/","LICENSE","release/")): member="standards/"+member
        common_ids.append(member)
check("common_inventory_exact_691_ids",len(common_ids)==len(set(common_ids))==691 and set(common_ids)==set(rows),
      {"common_count":len(common_ids),"missing":sorted(set(common_ids)-set(rows)),"additional":sorted(set(rows)-set(common_ids))})
counts = Counter(r["disposition"] for r in a["rows"])
check("disposition_totals",counts=={"conserved":609,"superseded":81,"not applicable":1},dict(counts))
check("frontier_digest",f["conservation_sha256"]==sha(git(ACCOUNT,BASE+"CONSERVATION.json")))
check("all_691_historical_indeterminate_reviews_retained",all(r["semantic_review"]==old_rows[r["id"]]["semantic_review"] and r["semantic_review"]["result"]=="indeterminate" for r in a["rows"]))
check("no_manufactured_current_review",all(r["current_review"]["standing"]=="independent_I5_assessment_not_performed" and r["current_review"]["dependency_impact"]=="not_assessed" and r["current_review"]["source_commit"]==SOURCE and r["current_review"]["account_commit"]==SEMANTIC for r in a["rows"]))
check("frontier_matches_account",all(frontier[r["id"]]["disposition"]==r["disposition"] and frontier[r["id"]]["relation"]==r.get("successor_relation",{}).get("id") and frontier[r["id"]]["owner_decision"]==r.get("successor_relation",{}).get("owner_decision") and frontier[r["id"]]["inherited_acceptance"]==r.get("acceptance") and frontier[r["id"]]["i5_assessment"]=="not_performed" and frontier[r["id"]]["semantic_reuse"]=="not_assessed" for r in a["rows"]))
superseded = [r for r in a["rows"] if r["disposition"]=="superseded"]
question_rows = [(z["id"],r) for z in q["questions"] for r in z["rows"]]
question_by_claim = {r["claim"]:(qid,r) for qid,r in question_rows}
relation_ids = [r["successor_relation"]["id"] for r in superseded]
check("81_unique_current_relations_and_question_partition",len(relation_ids)==len(set(relation_ids))==len(question_rows)==len(question_by_claim)==81 and {r["id"] for r in superseded}==set(question_by_claim) and all(question_by_claim[r["id"]][1]["relation"]==r["successor_relation"] for r in superseded))
check("23_pending_questions_no_owner_decisions",len(q["questions"])==len({x["id"] for x in q["questions"]})==23 and all(x["decision"]=={"status":"pending","record":None} for x in q["questions"]) and all(r["successor_relation"]["owner_decision"] is None and r["successor_relation"]["standing"]=="proposed_pending_owner_decision" and r["successor_relation"]["predecessor_claim_id"]==r["id"] and r["successor_relation"]["replacement_loci"] for r in superseded))
check("one_R020_successor_with_history",q["proposal_successors"]=={"I3-R2-R020":"I5-ACCOUNT-R012"} and "I3-R2-R020" not in relation_ids and relation_ids.count("I5-ACCOUNT-R012")==1 and rows["SPEC_METHOD.md#universal-intake-triage"]["i5_author_history"]["successor_relation"]["id"]=="I3-R2-R020")
proposal_results = []
for amendment in p["amendments"]:
    claim = amendment["claim_id"]; row,previous=rows[claim],old_rows[claim]; rel=amendment["replacement_relation"]
    valid = sha(canonical(previous))==amendment["original_row_sha256"] and previous["disposition"]==amendment["prior_disposition"] and previous.get("successor_relation",{}).get("id")==amendment["supersedes_proposal_id"] and row["successor_relation"]==rel and row["successor_loci"]==amendment["successor_loci"]==rel["replacement_loci"] and row["disposition"]=="superseded" and row["acceptance"]=="owner_decision_and_current_independent_review_pending" and question_by_claim[claim][0]==amendment["question"]
    history=row["i5_author_history"]
    valid=valid and history["source_commit"]==I4 and history["original_row_sha256"]==amendment["original_row_sha256"] and history["disposition"]==previous["disposition"] and history["successor_loci"]==previous["successor_loci"] and history["acceptance"]==previous.get("acceptance") and history["successor_relation"]==previous.get("successor_relation") and history["replacement_owner_dependencies"]==previous.get("replacement_owner_dependencies",[])
    proposal_results.append({"claim":claim,"relation":rel["id"],"question":amendment["question"],"prior_disposition":amendment["prior_disposition"],"passed":valid})
check("13_exact_amendment_preimages_and_relations",len(proposal_results)==len({x["claim"] for x in proposal_results})==13 and all(x["passed"] for x in proposal_results),proposal_results)
check("12_new_one_revised",Counter(x["prior_disposition"] for x in p["amendments"])=={"conserved":12,"superseded":1})
amended_ids={x["claim_id"] for x in p["amendments"]}
coordinate_fields={"successor_sha256","current_review","inherited_current_review"}
check("678_unamended_rows_preserve_all_noncoordinate_fields",all({k:v for k,v in r.items() if k not in coordinate_fields}=={k:v for k,v in old_rows[r["id"]].items() if k not in coordinate_fields} for r in a["rows"] if r["id"] not in amended_ids))
check("proposal_comparison_binding",p["evidence"]["sha256"]==sha(git(ACCOUNT,BASE+p["evidence"]["path"])) and {x["claim_id"] for x in p["amendments"]}=={x["claim"] for x in s["comparisons"] if x["author_result"]=="proposed_supersession"})
check("declared_semantic_coordinate_exists",subprocess.run(["git","cat-file","-e",SEMANTIC+"^{commit}"],cwd=TENANT).returncode==0)
comparison_results = []
for x in s["comparisons"]:
    member=x["claim"].split("#")[0]; raw=(INSTALL/"standards"/member).read_bytes(); body=section(raw,x["claim"])
    item={"claim":x["claim"],"author_result":x["author_result"]}
    item["predecessor"]=sha(raw)==x["predecessor_member_sha256"] and sha(body)==x["predecessor_section_sha256"] and body.decode()==x["predecessor_body"]
    for label,commit in (("i4",I4),("i5_raw",s["raw_source"])):
        data=x[label];raw,body=source_bytes(commit,data["route"])
        item[label]=data["source_commit"]==commit and sha(raw)==data["member_sha256"] and sha(body)==data["body_sha256"] and body.decode()==data["body"] and len(body)==data["bytes"]
    raw,body=source_bytes(SOURCE,x["i5_raw"]["route"])
    item["final_body_matches_raw"]=body.decode()==x["i5_raw"]["body"]
    item["unchanged_i4_primary_body"]=x["i4"]["body"]==body.decode()
    item["passed"]=all(item[k] for k in ("predecessor","i4","i5_raw","final_body_matches_raw"))
    comparison_results.append(item)
check("20_comparisons_match_actual_exact_sections",len(comparison_results)==20 and all(x["passed"] for x in comparison_results),comparison_results)
check("seven_retained_conservation_rows_without_relations",len([x for x in s["comparisons"] if x["author_result"]=="proposed_conserved"])==7 and all(rows[x["claim"]]["disposition"]=="conserved" and x["claim"] not in question_by_claim for x in s["comparisons"] if x["author_result"]=="proposed_conserved"))
member_results=[]
for x in s["changed_members"]:
    left,right=(git(commit,ROOT+"successor/"+x["path"]) for commit in (I4,SOURCE))
    member_results.append({"path":x["path"],"passed":sha(left)==x["i4_sha256"] and sha(right)==x["i5_sha256"]})
check("nine_changed_member_hashes",len(member_results)==9 and all(x["passed"] for x in member_results),member_results)
changed_paths=subprocess.check_output(["git","diff","--name-only",I4,SOURCE,"--",ROOT+"successor/standards/"],cwd=TENANT,text=True).splitlines()
all_changed_members={x.removeprefix(ROOT+"successor/") for x in changed_paths}
# The declared comparison boundary is the nine raw standard bodies. Generated
# compression/frame/verification surfaces belong to other qualification work.
actual_members={x for x in all_changed_members if x.count("/")==1 and x.endswith(".md")}
check("changed_raw_standard_member_set_complete",actual_members=={x["path"] for x in s["changed_members"]},{"actual":sorted(actual_members),"outside_declared_body_boundary":sorted(all_changed_members-actual_members)})
actual_changed_sections=set()
for member in actual_members:
    before,after=(sections(git(commit,ROOT+"successor/"+member)) for commit in (I4,SOURCE))
    actual_changed_sections.update(member+"#"+anchor for anchor in set(before)|set(after) if before.get(anchor)!=after.get(anchor))
check("changed_raw_body_heading_unit_set_complete",actual_changed_sections=={x["route"] for x in s["changed_sections"]},{"actual_count":len(actual_changed_sections),"unreported":sorted(actual_changed_sections-{x["route"] for x in s["changed_sections"]}),"spurious":sorted({x["route"] for x in s["changed_sections"]}-actual_changed_sections)})
section_results=[]
for x in s["changed_sections"]:
    raw,final=source_bytes(SOURCE,x["route"])
    raw=git(I4,ROOT+"successor/"+x["route"].split("#")[0]);prior=sections(raw).get(x["route"].split("#",1)[1])
    valid=final.decode()==x["i5_body"] and sha(final)==x["i5_body_sha256"] and (prior is None and x["new_section"] and not x["i4_body"] or prior is not None and prior.decode()==x["i4_body"] and sha(prior)==x["i4_body_sha256"])
    section_results.append({"route":x["route"],"passed":valid})
check("37_changed_heading_units_match_actual_source",len(section_results)==37 and all(x["passed"] for x in section_results),section_results)
locus_results=[]
for locus in sorted({l for r in superseded for l in r["successor_relation"]["replacement_loci"]}):
    raw,body=source_bytes(SOURCE,locus);pin=a["successor_locus_pins"][locus]
    locus_results.append({"locus":locus,"passed":sha(body)==pin["sha256"] and len(body)==pin["bytes"] and sha(raw)==pin["member_sha256"]})
check("all_replacement_loci_resolve_to_final_pins",all(x["passed"] for x in locus_results),{"count":len(locus_results),"failures":[x for x in locus_results if not x["passed"]]})
donor_specs=[
 ("standards/RELEASE.md",[(641,699)],"6901b148a0cca05ae85bab6439e9f0178f1a1fa904b49383d83445af57e6f93b"),
 ("standards/CONFORMANCE.md",[(109,126),(193,222)],"e8a3f3faa270a26515a39b4e3bbc8ece946f6ec48b11eadea682426966496f09"),
 ("design/REDUCTION.md",[(1427,1464),(1567,1587)],"8b477a63d76f71cf5c1b0fcae1c6ddb5c722e31979fcd931cb5acbaef28fb849")]
donor_receipts=[]
for path,spans,expected in donor_specs:
    raw=git(DONOR,V3+"build_tenants/claude/"+path,MAIN);lines=raw.decode().splitlines(keepends=True)
    donor_receipts.append({"path":path,"member_sha256":sha(raw),"matched":sha(raw)==expected,
     "selected_excerpts":[{"start_line":lo,"end_line":hi,"body":"".join(lines[lo-1:hi])} for lo,hi in spans]})
check("selected_donor_pins",all(x["matched"] for x in donor_receipts))
retained=[]
for name,expected in [("PORT_ACCOUNT.md","93c26ce5f221d9632712df2f0fa4fcc295889122bc234dfcf387dc2687b7fd02"),("REVIEW_REGISTER.md","8c28bb4f67bf089c770be38adcc60d325b12543570de46c6c8a1eec97f70f275")]:
    raw=git(HANDOFF,ROOT+"qualification/C3/iteration-4/"+name)
    retained.append({"name":name,"sha256":sha(raw),"passed":sha(raw)==expected})
check("receiving_historical_account_pins",all(x["passed"] for x in retained),retained)
inputs=[]
for name in ("CONSERVATION.json","FRONTIER.json","REPLACEMENT_QUESTIONS.json","source/account/PROPOSALS.json","source/account/SOURCE_COMPARISON.json","PORT_ACCOUNT.md","REVIEW_REGISTER.md","tools/carry_conservation.py"):
    raw=git(ACCOUNT,BASE+name);inputs.append({"commit":ACCOUNT,"path":BASE+name,"bytes":len(raw),"sha256":sha(raw)})
result={"kind":"independent_scoped_conservation_reproduction","subject":ACCOUNT,"source":SOURCE,"semantic":SEMANTIC,"common":COMMON,"donor":DONOR,"checks":checks,"all_checks_passed":all(x["passed"] for x in checks),"scope":"Mechanical integrity and exact source checks only; the review supplies the separate bounded semantic judgment."}
write("RESULTS.json",result);write("INPUTS.json",inputs);write("SELECTED_DONOR.json",donor_receipts)
write("COMPARISON_MATRIX.json",comparison_results);write("PROPOSAL_MATRIX.json",proposal_results)
diffs=[]
for x in s["changed_members"]:
    left,right=(git(commit,ROOT+"successor/"+x["path"]).decode() for commit in (I4,SOURCE))
    diffs.append("".join(difflib.unified_diff(left.splitlines(True),right.splitlines(True),fromfile=x["path"]+"@"+I4,tofile=x["path"]+"@"+SOURCE,n=2)))
(OUT/"SOURCE_DIFF.patch").write_text("\n".join(diffs))
# Narrow readback of the caller-observed reporting correction; primary stays ACCOUNT.
METADATA = "0b35955cddbbe5d2adbf91a770921a07d598e227"
inventory_raw=git(ACCOUNT,ROOT+"successor/interpretation/SOURCE_INVENTORY.json")
inventory=json.loads(inventory_raw)
docs={r["path"] for r in inventory["document_members"]}
carrying=set(a["successor_member_pins"])
package={x.removeprefix(ROOT+"successor/") for x in subprocess.check_output(
 ["git","ls-tree","-r","--name-only",ACCOUNT,"--",ROOT+"successor/"],cwd=TENANT,text=True).splitlines()}
interpretation={x for x in package if x.startswith("interpretation/")}
metadata_paths=subprocess.check_output(["git","diff-tree","--no-commit-id","--name-only","-r",METADATA],cwd=TENANT,text=True).splitlines()
unchanged=all(git(ACCOUNT,BASE+n)==git(METADATA,BASE+n) for n in
 ("CONSERVATION.json","FRONTIER.json","REPLACEMENT_QUESTIONS.json","source/account/PROPOSALS.json","source/account/SOURCE_COMPARISON.json","tools/carry_conservation.py"))
metadata={"primary":ACCOUNT,"metadata_successor":METADATA,
 "source_inventory_sha256":sha(inventory_raw),"account_source_members":len(a["source_member_pins"]),
 "claim_carrying_members":len(carrying),"documentary_members":len(docs),"package_members":len(package),
 "interpretation_members":len(interpretation),"documentary_tree_match":docs==package-interpretation,
 "carrying_subset":carrying<=docs,"nine_path_difference":sorted(docs-carrying),
 "metadata_commit_changed_paths":metadata_paths,"primary_account_proposal_helper_unchanged":unchanged}
metadata["satisfied"]=(len(carrying),len(docs),len(package),len(interpretation))==(72,81,90,9) and docs==package-interpretation and carrying<=docs and unchanged and metadata_paths==[BASE+"ACCOUNT_RETURN.md"]
write("METADATA_READBACK.json",metadata)
print(json.dumps({"all_checks_passed":result["all_checks_passed"],"metadata_readback_satisfied":metadata["satisfied"],"check_count":len(checks),
 "failed_checks":[x["check"] for x in checks if not x["passed"]],"totals":dict(counts),
 "current_relations":len(relation_ids),"questions":len(q["questions"]),"replacement_loci":len(locus_results),
 "results_sha256":sha((OUT/"RESULTS.json").read_bytes())},indent=2))

