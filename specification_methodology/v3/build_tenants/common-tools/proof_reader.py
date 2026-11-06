#!/usr/bin/env python3
"""Build/check offline documentation for an exact retained Lean source cut."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
import sys

LEGACY_GENERATOR_SHA256 = "37a74b721347635ddfdf1032cbed124c97c46aabbfd5f4fd919aca19f9cdf457"


def current():
    here = str(Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import proof_reader_current
    return proof_reader_current

REPORT_SHA256 = "8b002e3821e99cd88bae0ccf07794d2e99818ba4e5b38d919fc3e3b45c672061"
SOURCES = ("AC.lean", "AC/Audit.lean", "AC/Closure.lean", "AC/Fixture.lean",
           "AC/Model.lean", "AC/Projection.lean", "AC/Run.lean", "AC/Toy.lean")
MEMBERS = {"index.html", "PROOFS.json", "report.json"} | {"sources/" + p for p in SOURCES}
BASIS = {
    "builder": "stdo://releases/v2.5.1-rc.2/",
    "manifest_sha256": "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782",
    "calculus": "stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md",
    "calculus_sha256": "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d",
    "correspondence": "a_c/build_tenants/lean/design/SOURCE_CORRESPONDENCE.md",
}
CLAIMS = [
    {"id": "closure", "title": "Selecting A also retains required B and unresolved C",
     "summary": "If the declared relation is A → B → C, selecting A requires all three. A successful finite certificate establishes the exact reachable set, including the seeds, and its leastness among seed-containing closed sets.",
     "condition": "The relation and seeds are supplied inputs, and the certificate check must succeed. This illustration is not a newly executed fixture or a proof that a source dependency was declared correctly.",
     "owner": "AC-010 Material Closure · FR-003",
     "declarations": ["AC.certificate_exact_reachability", "AC.certificate_seed_inclusion", "AC.certificate_closed", "AC.certificate_least"]},
    {"id": "budget", "title": "A budget of two cannot silently return only A and B",
     "summary": "When the required closure has three records, a budget of two produces refusal. The operation cannot claim success by truncating a required record.",
     "condition": "This theorem assumes a well-formed model and a successful certificate check; the budget counts local records.",
     "owner": "AC-011 budget prohibition · FR-005",
     "declarations": ["AC.insufficient_budget_refuses", "AC.projection_success", "AC.project"]},
    {"id": "records", "title": "Keep the complete record, not just its label",
     "summary": "A selected record is the original record, with its owner, scope, context, basis and payload intact. The projection also retains its parent coordinates.",
     "condition": "Equality preserves the recorded content; it does not establish authority legitimacy or the truth of a predicate.",
     "owner": "Typed Records / AC-011 · FR-002, FR-004",
     "declarations": ["AC.projection_record_conservation", "AC.projection_authority_basis_conservation", "AC.projection_parent_conservation"]},
    {"id": "residuals", "title": "An open question stays visible",
     "summary": "Every original residual is accounted for as an exact retained unresolved record or a named excluded residual. Projection does not resolve the uncertainty.",
     "condition": "The theorem preserves recorded residuals; it cannot discover an uncertainty missing from the source model.",
     "owner": "AC-009 Residual Conservation / AC-011 · FR-004",
     "declarations": ["AC.projection_all_residuals_accounted", "AC.projection_residual_conservation", "AC.projection_excluded_residual_exact"]},
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def mask_noncode(text: str) -> str:
    """Keep offsets/newlines while hiding nested comments and string contents."""
    out = list(text)
    i, depth, string, line_comment = 0, 0, False, False
    while i < len(text):
        pair, c = text[i:i + 2], text[i]
        if line_comment:
            if c == "\n":
                line_comment = False
            else:
                out[i] = " "
        elif depth:
            if pair in ("/-", "-/"):
                depth += 1 if pair == "/-" else -1
                out[i:i + 2] = [" ", " "]
                i += 2
                continue
            if c != "\n":
                out[i] = " "
        elif string:
            if c == "\\" and i + 1 < len(text):
                out[i] = " "
                if text[i + 1] != "\n":
                    out[i + 1] = " "
                i += 2
                continue
            if c == '"':
                string = False
            if c != "\n":
                out[i] = " "
        elif pair in ("/-", "--"):
            depth = int(pair == "/-")
            line_comment = pair == "--"
            out[i:i + 2] = [" ", " "]
            i += 2
            continue
        elif c == '"':
            string = True
            out[i] = " "
        i += 1
    require(not depth and not string, "unterminated comment/string in selected Lean source")
    return "".join(out)


IDENTIFIER = r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*"
DECLARATION = re.compile(
    r"^(?:(?:private|protected|public|noncomputable|unsafe|partial)\s+)*"
    r"(?P<kind>theorem|lemma|def|abbrev|structure|inductive|instance)\s+(?P<name>" + IDENTIFIER + r")\b")
ANONYMOUS_BOUNDARY = re.compile(
    r"^(?:(?:private|protected|public|noncomputable|unsafe|partial)\s+)*(?:instance|example)\b")
KINDS = {"theorem": "Theorem", "lemma": "Theorem", "def": "Definition",
         "abbrev": "Abbreviation", "structure": "Structure", "inductive": "Inductive",
         "instance": "Instance"}
TOKEN = re.compile(IDENTIFIER)


def statement(source: str, masked: str) -> str:
    nesting = 0
    for i, c in enumerate(masked):
        if c in "([{":
            nesting += 1
        elif c in ")]}":
            nesting -= 1
        elif not nesting and masked[i:i + 2] == ":=":
            return source[:i].rstrip()
    return source.rstrip()


def source_catalog(sources: dict[str, str]) -> tuple[list[dict], dict[str, list[str]]]:
    declarations, imports, masked_files = [], {}, {}
    for path, text in sources.items():
        masked = mask_noncode(text)
        masked_files[path] = masked
        lines, clean = text.splitlines(keepends=True), masked.splitlines(keepends=True)
        offsets, offset = [], 0
        for line in lines:
            offsets.append(offset)
            offset += len(line)
        namespace, pending = [], None
        imports[path] = []

        def close(end_line):
            nonlocal pending
            if pending is not None:
                end = end_line
                while end > pending["start_line"] and not clean[end - 1].strip():
                    end -= 1
                pending["end_line"] = end
                start_offset = offsets[pending["start_line"] - 1]
                end_offset = offsets[end] if end < len(offsets) else len(text)
                pending["statement"] = statement(text[start_offset:end_offset], masked[start_offset:end_offset])
                declarations.append(pending)
                pending = None

        for number, line in enumerate(clean, 1):
            match = DECLARATION.match(line)
            opened = re.match(r"^namespace\s+(" + IDENTIFIER + r")", line)
            ended = re.match(r"^end(?:\s|$)", line)
            imported = re.match(r"^(?:public\s+)?(?:meta\s+)?import\s+(.+)", line)
            command = re.match(r"^(?:#|set_option\b|module\b|(?:public\s+)?section\b)", line)
            if match or opened or ended or imported or command or ANONYMOUS_BOUNDARY.match(line):
                close(number - 1)
            if opened:
                namespace.append(opened.group(1))
            elif ended and namespace:
                namespace.pop()
            elif imported:
                imports[path].extend(imported.group(1).split())
            elif match:
                local_name = match.group("name")
                prefix = ".".join(namespace)
                name = prefix + "." + local_name if prefix else local_name
                pending = {"id": name, "name": local_name, "kind": KINDS[match.group("kind")],
                           "file": path, "start_line": number, "namespace": prefix}
        close(len(lines))
    by_name = {d["id"]: d for d in declarations}
    require(len(by_name) == len(declarations), "duplicate named declaration in selected source profile")
    suffixes = {}
    for name in by_name:
        suffixes.setdefault(name.rsplit(".", 1)[-1], []).append(name)
    for declaration in declarations:
        text = masked_files[declaration["file"]]
        lines = text.splitlines(keepends=True)
        body = "".join(lines[declaration["start_line"] - 1:declaration["end_line"]])
        references, seen = [], set()
        for match in TOKEN.finditer(body):
            token = match.group(0)
            candidate = token if token in by_name else None
            scope = declaration["namespace"]
            while not candidate and scope:
                joined = scope + "." + token
                if joined in by_name:
                    candidate = joined
                scope = scope.rpartition(".")[0]
            if not candidate and len(suffixes.get(token, [])) == 1:
                candidate = suffixes[token][0]
            line = declaration["start_line"] + body[:match.start()].count("\n")
            key = (candidate, token, line)
            if candidate and candidate != declaration["id"] and key not in seen:
                seen.add(key)
                references.append({"target": candidate, "token": token, "line": line})
        declaration["references"] = references
    return declarations, imports


def make_catalog(source_bytes: dict[str, bytes], report_raw: bytes) -> tuple[dict, dict[str, str]]:
    require(sha(report_raw) == REPORT_SHA256, "retained proof report identity changed")
    report = json.loads(report_raw)
    require(report.get("status") == "passed", "selected report is not passed")
    require(set(source_bytes) == set(SOURCES), "selected Lean source member set changed")
    for name, raw in source_bytes.items():
        require(sha(raw) == report["source_sha256"][name], "checked Lean source changed: " + name)
    texts = {name: source_bytes[name].decode("utf-8") for name in SOURCES}
    declarations, imports = source_catalog(texts)
    ids = {d["id"] for d in declarations}
    for claim in CLAIMS:
        require(set(claim["declarations"]) <= ids, "curated theorem is missing")
    catalog = {
        "kind": "stdo.proof-reader/1", "distributing_release": "3.0.3",
        "generator_sha256": LEGACY_GENERATOR_SHA256, "basis": BASIS,
        "report": {"path": "report.json", "sha256": REPORT_SHA256, "status": report["status"],
                   "standing": "Retained historical T011 independent check; not a fresh proof execution.",
                   "projection_outputs": report["actual_projection_outputs"],
                   "underbudget_refusals": report["actual_underbudget_refusals"],
                   "audited_declaration_contracts": report["axiom_checked_theorems"],
                   "allowed_axioms": report["allowed_axioms"], "lean": report["lean"],
                   "lean_commit": report["lean_commit"], "mathlib_commit": report["mathlib_commit"],
                   "kernel_replay": report["kernel_replay"], "fixture": report["fixture"], "toy": report["toy"]},
        "source_scope": "Eight exact Lean files from the report. Current importer/generator and other later tooling are not requalified.",
        "reference_scope": "Lexical candidate source references, not a kernel proof-dependency graph.",
        "catalog_scope": "Named declarations in the selected eight-file profile. Anonymous instances and examples remain available in complete source, outside the named catalog.",
        "sources": [{"file": name, "path": "sources/" + name, "sha256": sha(source_bytes[name]),
                     "bytes": len(source_bytes[name]), "lines": len(texts[name].splitlines()),
                     "imports": imports[name]} for name in SOURCES],
        "claims": CLAIMS, "declarations": declarations,
    }
    return catalog, texts


CSS = """
:root{color-scheme:dark;--bg:#101820;--panel:#17232d;--line:#334653;--text:#e8eef0;--muted:#a9bac4;--accent:#acdbbd;font:15px/1.55 system-ui,sans-serif}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text)}a{color:#a7d6ec}button,input,select{font:inherit;color:inherit}button{cursor:pointer;background:#233541;border:1px solid #45606f;border-radius:6px;padding:7px 11px}button:hover{background:#314b58}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid var(--accent);outline-offset:2px}button:disabled{opacity:.4;cursor:default}header{padding:23px 30px;border-bottom:1px solid var(--line)}.topnav{display:flex;gap:20px;flex-wrap:wrap;font-size:13px}.eyebrow{color:var(--accent);font-size:11px;letter-spacing:1.5px;margin:20px 0 4px}h1{font-size:30px;margin:0 0 8px}h2{font-size:20px;margin:12px 0}h3{font-size:14px;margin:23px 0 8px}p{max-width:900px}.muted{color:var(--muted);font-size:13px}.boundary{max-width:1000px;color:#c4d2d9;font-size:13px}.stats{display:flex;gap:10px 22px;flex-wrap:wrap;font-size:13px;color:var(--accent)}.layout{display:grid;grid-template-columns:290px minmax(0,1fr);min-height:60vh}aside{border-right:1px solid var(--line);padding:22px;background:var(--panel)}input,select{width:100%;padding:9px;background:#101a22;border:1px solid #45606f;border-radius:5px;margin:5px 0 13px}label{font-size:12px;color:var(--muted)}#modules button,#results button{display:block;text-align:left;width:100%;margin:5px 0;overflow-wrap:anywhere;font-size:12px}#results small{display:block;color:var(--muted)}#results button[aria-current=true]{border-color:var(--accent);background:#2a4546}main{padding:24px 32px;min-width:0}.claims{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.claim{padding:16px;text-align:left}.claim span{display:block;font-size:11px;color:var(--accent);margin-bottom:5px}.reader-nav{display:flex;gap:12px;align-items:center;margin-top:25px;border-top:1px solid var(--line);padding-top:16px}#trail{display:flex;gap:6px;flex-wrap:wrap}#trail button{font-size:11px;max-width:250px;overflow:hidden;text-overflow:ellipsis}.kind{font-size:11px;color:var(--accent);text-transform:uppercase;letter-spacing:1px}.identity{overflow-wrap:anywhere;font-family:ui-monospace,monospace;font-size:12px;color:#b5cbd6}pre{white-space:pre-wrap;overflow-wrap:anywhere;tab-size:2;font:12px/1.6 ui-monospace,SFMono-Regular,Consolas,monospace;background:#0c141b;border:1px solid var(--line);border-radius:7px;padding:15px;max-height:65vh;overflow:auto}.statement{font-size:14px;line-height:1.7;max-height:42vh}.actions,.references{display:flex;gap:7px;flex-wrap:wrap;margin:12px 0}.references button{font-size:12px;text-align:left}details{margin:16px 0}summary{cursor:pointer;color:#b4d1dd}.source-row{display:block;min-height:1.6em}.source-row.selected{background:#2a493f}.line-number{display:inline-block;min-width:5em;color:#7692a4;user-select:none}.source-text{white-space:pre}.source-box{white-space:pre;overflow:auto}.source-box .source-row{width:max-content;min-width:100%}.report-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.report-card{border:1px solid var(--line);border-radius:7px;padding:14px}.report-card h3{margin-top:0}dialog{background:var(--panel);color:var(--text);border:1px solid #58717d;border-radius:10px;width:min(960px,94vw);max-height:90vh;padding:24px}dialog::backdrop{background:#000b}.dialog-head{display:flex;justify-content:space-between;gap:15px}.file-heading{display:flex;align-items:center;gap:10px;flex-wrap:wrap}#empty{color:var(--muted)}footer{border-top:1px solid var(--line);padding:18px 30px;font-size:12px;color:var(--muted)}@media(max-width:850px){.layout{grid-template-columns:1fr}aside{border-right:0;border-bottom:1px solid var(--line)}#modules{display:flex;flex-wrap:wrap;gap:5px}#modules button{width:auto}.claims,.report-grid{grid-template-columns:1fr}main,header{padding:20px}#results{max-height:240px;overflow:auto}}
"""
APP = r"""
'use strict';
(() => {
 const data=JSON.parse(document.getElementById('proof-data').textContent),c=data.catalog;
 const $=id=>document.getElementById(id),el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
 const declarations=new Map(c.declarations.map(d=>[d.id,d])),sources=new Map(c.sources.map(s=>[s.file,s]));
 let history=[],current=null,limit=60;
 $('report-status').textContent='Retained passed check · '+c.report.projection_outputs+' projection outputs · '+c.report.underbudget_refusals+' budget refusals · '+c.report.audited_declaration_contracts+' audited declaration contracts';
 $('source-scope').textContent=c.source_scope;
 for(const source of c.sources){const b=el('button',source.file);b.dataset.file=source.file;b.onclick=()=>open({type:'file',file:source.file,line:1});$('modules').append(b);const o=el('option',source.file);o.value=source.file;$('module').append(o);}
 for(const kind of [...new Set(c.declarations.map(d=>d.kind))].sort()){const o=el('option',kind);o.value=kind;$('kind').append(o);}
 for(const claim of c.claims){const b=el('button',undefined,'claim');b.dataset.claim=claim.id;b.append(el('span',claim.owner),el('strong',claim.title));b.onclick=()=>open({type:'claim',id:claim.id});$('claims').append(b);}
 function search(){const q=$('query').value.toLowerCase().trim(),kind=$('kind').value,file=$('module').value;
  const matches=c.declarations.filter(d=>(!kind||kind===d.kind)&&(!file||file===d.file)&&(d.id+'\n'+d.statement).toLowerCase().includes(q));
  $('results').replaceChildren();$('matches').textContent=matches.length+' declarations · showing '+Math.min(limit,matches.length);
  for(const d of matches.slice(0,limit)){const b=el('button');b.dataset.declaration=d.id;b.setAttribute('aria-current',String(current?.type==='declaration'&&current.id===d.id));b.append(el('span',d.id),el('small',d.kind+' · '+d.file+':'+d.start_line));b.onclick=()=>open({type:'declaration',id:d.id});$('results').append(b);}
  if(!matches.length)$('results').append(el('p','No declarations match these filters.','muted'));
  $('more').hidden=matches.length<=limit;
 }
 $('query').oninput=$('kind').onchange=$('module').onchange=()=>{limit=60;search();};
 $('more').onclick=()=>{limit+=60;search();};
 function label(view){return view.type==='claim'?c.claims.find(x=>x.id===view.id).title:view.type==='file'?view.file:view.id;}
 function trail(){$('trail').replaceChildren();history.forEach((view,i)=>{const b=el('button',(i+1)+'. '+label(view));b.title=label(view);b.onclick=()=>{history=history.slice(0,i+1);show(view);};$('trail').append(b);});$('back').disabled=history.length<2;}
 function open(view){history.push(view);show(view);}
 function show(view){current=view;location.hash=encodeURIComponent(JSON.stringify(view));render();trail();search();}
 $('back').onclick=()=>{if(history.length>1){history.pop();show(history[history.length-1]);}};
 function declarationButton(id,text){const b=el('button',text||id);b.dataset.target=id;b.onclick=()=>open({type:'declaration',id});return b;}
 function sourceButton(file,line){const b=el('button','Read full source · '+file+':'+line);b.dataset.source=file;b.onclick=()=>open({type:'file',file,line});return b;}
 function render(){const pane=$('reader');pane.replaceChildren();delete pane.dataset.declaration;pane.dataset.view=current.type;
  if(current.type==='claim'){const claim=c.claims.find(x=>x.id===current.id);pane.append(el('p',claim.owner,'kind'),el('h2',claim.title),el('p',claim.summary),el('p',claim.condition,'muted'));const links=el('div',undefined,'references');for(const id of claim.declarations)links.append(declarationButton(id));pane.append(links,el('h3','How to read a theorem'),el('p','Read the parameters and hypotheses first, then the proposition after the colon. The proof follows :=. Follow a source reference to inspect a definition or lemma; use Back to return.'));return;}
  if(current.type==='file'){const source=sources.get(current.file);pane.append(el('p','Complete checked source file','kind'),el('h2',source.file),el('p','SHA-256 '+source.sha256,'identity'));const imports=el('div',undefined,'references');for(const imported of source.imports){const target=imported.replaceAll('.','/')+'.lean';if(sources.has(target)){const b=el('button','Import · '+imported);b.onclick=()=>open({type:'file',file:target,line:1});imports.append(b);}else imports.append(el('span','Import · '+imported+' (source not bundled)','muted'));}pane.append(el('p','Imports and highlighted identifier links are source navigation, not a checked dependency graph.','muted'),imports);
   const pre=el('pre',undefined,'source-box');pre.id='full-source';
   data.sources[source.file].split('\n').forEach((line,i)=>{const row=el('span',undefined,'source-row');row.dataset.line=String(i+1);if(i+1===current.line)row.classList.add('selected');row.append(el('span',String(i+1),'line-number'),el('span',line,'source-text'));pre.append(row);});
   pane.append(pre);pre.querySelector('.selected')?.scrollIntoView({block:'center'});return;
  }
  const d=declarations.get(current.id);pane.dataset.declaration=d.id;pane.append(el('p',d.kind+' · '+d.file+':'+d.start_line+'–'+d.end_line,'kind'),el('h2',d.id),el('pre',d.statement,'statement'));
  pane.append(el('p','This declaration is in the exact retained source cut. The evidence summary applies to the historical report; no separate verdict is assigned here.','muted'));
  const actions=el('div',undefined,'actions');actions.append(sourceButton(d.file,d.start_line));pane.append(actions);
  const proof=el('details');proof.append(el('summary','Complete declaration and proof/body'),el('pre',data.sources[d.file].split('\n').slice(d.start_line-1,d.end_line).join('\n')));pane.append(proof);
  pane.append(el('h3','Source references (lexical)'),el('p','Identifier occurrences resolved against this displayed source catalog. These are not Lean elaborator or kernel proof-dependency edges.','muted'));
  const refs=el('div',undefined,'references');for(const r of d.references)refs.append(declarationButton(r.target,r.target+' · line '+r.line));if(!d.references.length)refs.append(el('p','No linked local identifier occurrence in this declaration.','muted'));pane.append(refs);
  const incoming=c.declarations.filter(x=>x.references.some(r=>r.target===d.id));if(incoming.length){const details=el('details');details.append(el('summary','Referenced in displayed source (lexical) · '+incoming.length));const list=el('div',undefined,'references');incoming.forEach(x=>list.append(declarationButton(x.id)));details.append(list);pane.append(details);}
 }
 const evidence=$('evidence-body');evidence.append(el('p',c.report.standing),el('p',c.source_scope),el('p','Report SHA-256 '+c.report.sha256,'identity'));
 const grid=el('div',undefined,'report-grid');
 const cards=[['Retained result',c.report.projection_outputs+' actual projections and '+c.report.underbudget_refusals+' underbudget refusals. '+c.report.audited_declaration_contracts+' audited declaration contracts, not that many independent mathematical results.'],['Audited allowed axioms',c.report.allowed_axioms.join(', ')+'. These are the allowed axioms in this audit, not an exhaustive inventory of every assumption in an application.'],['Checked subject','32-record STDO 3.0.2 supplement and separate 14-record structural fixture. This is not the later 1,987-record / 29-record-view result.'],['Trusted boundary','The Lean kernel, pinned libraries/toolchain and historical Python custody/import/serialization checks are trust components. Prose predicates remain opaque; preservation proves neither their truth nor source-code correctness.']];
 for(const [title,text]of cards){const box=el('section',undefined,'report-card');box.append(el('h3',title),el('p',text));grid.append(box);}evidence.append(grid);
 evidence.append(el('h3','Compiler, library and builder coordinates'),el('pre',JSON.stringify({lean:c.report.lean,lean_commit:c.report.lean_commit,mathlib_commit:c.report.mathlib_commit,kernel_replay:c.report.kernel_replay,basis:c.basis},null,2)));
 evidence.append(el('h3','Exact retained report'),el('pre',data.report_text));
 const inventory=el('details');inventory.append(el('summary','Eight displayed source identities'),el('pre',JSON.stringify(c.sources,null,2)));evidence.append(inventory);
 $('evidence-open').onclick=()=>$('evidence').showModal();$('evidence-close').onclick=()=>$('evidence').close();
 let initial;try{initial=JSON.parse(decodeURIComponent(location.hash.slice(1)));}catch(_){}
 const valid=v=>v&&(v.type==='declaration'&&declarations.has(v.id)||v.type==='file'&&sources.has(v.file)&&Number.isInteger(v.line)&&v.line>0||v.type==='claim'&&c.claims.some(x=>x.id===v.id));
 open(valid(initial)?initial:{type:'claim',id:'closure'});
 window.addEventListener('hashchange',()=>{let v;try{v=JSON.parse(decodeURIComponent(location.hash.slice(1)));}catch(_){return;}if(valid(v)&&JSON.stringify(v)!==JSON.stringify(current))open(v);});
})();
"""
HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Read the proofs · STDO 3.0.3</title><link rel="icon" href="data:,"><style>@@CSS@@</style></head>
<body><header><nav class="topnav" aria-label="Documentation"><a href="../index.html">Documentation home</a><a href="../constraint-explorer/index.html">Constraints</a><a href="../code-explorer/index.html">Code example</a><span aria-current="page">Proofs</span></nav><p class="eyebrow">STDO 3.0.3 / RETAINED LEAN EVIDENCE</p><h1>Read the proofs</h1><p>See why a declared dependency must be retained, what a projection preserves, and when a budget must refuse.</p><p class="boundary">This reader preserves historical checked source and results. It runs no proof checker. Source-reference links are lexical navigation; opaque prose and application code acquire no correctness proof from this page.</p><div class="stats"><span id="report-status"></span><button id="evidence-open">Evidence and assumptions</button></div></header>
<div class="layout"><aside><h2>Find a declaration</h2><p class="muted">Named declarations are indexed here. Anonymous instances and examples remain in the complete source files.</p><label for="query">Name or statement</label><input id="query" type="search" placeholder="Try closure, budget or residual"><label for="kind">Declaration kind</label><select id="kind"><option value="">All kinds</option></select><label for="module">Source file</label><select id="module"><option value="">All source files</option></select><p id="matches" class="muted" aria-live="polite"></p><nav id="results" aria-label="Declarations"></nav><button id="more">Show more</button><h3>Complete source files</h3><nav id="modules" aria-label="Lean source files"></nav></aside>
<main><h2>Start with a question</h2><div id="claims" class="claims"></div><div class="reader-nav"><button id="back" disabled>Back</button><nav id="trail" aria-label="Reading trail"></nav></div><article id="reader" aria-live="polite"></article></main></div>
<dialog id="evidence"><div class="dialog-head"><h2>Historical check and exact source</h2><button id="evidence-close">Close</button></div><div id="evidence-body"></div></dialog><footer><p id="source-scope"></p><a href="PROOFS.json">Catalog and identities</a> · <a href="report.json">Original report</a></footer>
<script id="proof-data" type="application/json">@@DATA@@</script><script>@@APP@@</script></body></html>
"""


def render(catalog: dict, sources: dict[str, str], report_raw: bytes) -> bytes:
    data = json.dumps({"catalog": catalog, "sources": sources,
                       "report_text": report_raw.decode("utf-8")}, ensure_ascii=True, separators=(",", ":"))
    data = data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    values = {"CSS": CSS, "DATA": data, "APP": APP}
    return re.sub(r"@@(CSS|DATA|APP)@@", lambda m: values[m.group(1)], HTML).encode("utf-8")


def create_payload(source_bytes: dict[str, bytes], report_raw: bytes) -> dict[str, bytes]:
    catalog, texts = make_catalog(source_bytes, report_raw)
    return {"report.json": report_raw, "PROOFS.json": canonical(catalog),
            "index.html": render(catalog, texts, report_raw),
            **{"sources/" + name: raw for name, raw in source_bytes.items()}}


def check_payload(files: dict[str, bytes]) -> dict:
    if json.loads(files.get("PROOFS.json", b"{}")).get("kind") == "stdo.current-proof-reader/1":
        return current().check_files(files)
    require(set(files) == MEMBERS, "proof documentation member set changed")
    require(all(isinstance(v, bytes) for v in files.values()), "proof payload values must be bytes")
    expected = create_payload({name: files["sources/" + name] for name in SOURCES}, files["report.json"])
    for name in sorted(MEMBERS):
        require(files[name] == expected[name], "proof documentation bytes changed: " + name)
    catalog = json.loads(expected["PROOFS.json"])
    return {"status": "checked", "members": len(MEMBERS), "sources": len(SOURCES),
            "declarations": len(catalog["declarations"]), "report_sha256": REPORT_SHA256,
            "standing": "documentation custody/reproduction; no fresh Lean execution"}


def read_payload(root: Path) -> dict[str, bytes]:
    require(root.is_dir() and not root.is_symlink(), "proof directory missing or redirected")
    files = {}
    for path in root.rglob("*"):
        require(not path.is_symlink(), "redirected proof member: " + str(path))
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path.read_bytes()
        else:
            require(path.is_dir(), "nonregular proof member: " + str(path))
    return files


def read_regular(path: Path) -> bytes:
    require(path.is_file() and not path.is_symlink(), "source/report missing or redirected: " + str(path))
    return path.read_bytes()


def build(lean_root: Path, report: Path, output: Path) -> dict:
    require(not output.exists() and not output.is_symlink(), "proof output already exists")
    payload = create_payload({name: read_regular(lean_root / name) for name in SOURCES}, read_regular(report))
    result = check_payload(payload)
    output.mkdir(parents=True)
    for name, raw in payload.items():
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    return {**result, "status": "built", "output": str(output)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    create = commands.add_parser("build")
    create.add_argument("--lean-root", type=Path, required=True)
    create.add_argument("--report", type=Path, required=True)
    create.add_argument("--output", type=Path, required=True)
    create_current = commands.add_parser("build-current")
    create_current.add_argument("--repository", type=Path, required=True)
    create_current.add_argument("--selection", type=Path, required=True)
    create_current.add_argument("--selection-sha256", required=True)
    create_current.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("check")
    check.add_argument("directory", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.operation == "build-current":
            result = current().build(args.repository, args.selection, args.selection_sha256, args.output)
        else:
            result = build(args.lean_root, args.report, args.output) if args.operation == "build" else check_payload(read_payload(args.directory))
        print(json.dumps(result, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
