from pathlib import Path
import json,hashlib
r=Path('/Users/jim/src/apps/specification_methodology/.ai-workspace/work');c=Path('/Users/jim/src/apps/specification_methodology-3.1-release');w=r/'STDO_3_1_RELEASE_2026-11-15';f=Path(__file__).resolve().parent
packet_path=w/'context/final-use-01/semantic-packet/PACKET.json';p=json.loads(packet_path.read_text());native=Path(p['native']['root'])
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
intro='''# Independent final Purpose Context and retained SDLC-use assessment

Assess both exact final purpose/index/query subjects against their full governing source closure below and preserved source-first expectations. The source-first expectations were authored by a prior actual Claude activation BEFORE candidate exposure. This session authors no candidate. Current release Writers and packet operator are OpenAI/Codex-family; actual CLI metadata binds your Claude identity. No tools, candidate repair, owner acceptance or publication action is requested. Do not call any advisor. Ordinary CLI is not a guaranteed clean room.

Bounded claims: governing-constraint sufficiency for the two COMPLETE queries and purpose families, exact native-A source binding, SDLC default and ticket/carrier/context owner placement, Skill/context composition and applicability of retained finite observed decisions. Source-relative coverage is not future code/behavior/typing/task acceptance. Current installed delivery operations are fresh mechanical observations. Consumer observations below are historical original subjects, reused only with established applicability; no current native actor trial occurred. Whole-method/C3, universal productivity/repair efficacy, complete-host context fit, automatic host pickup, general visual utility and consumer adoption are not claimed.

All12 ticket-trial source-owner bytes and the native work/coordination instructions received then match A exactly. The39 SDLC rule meanings except W01 remain exact; W01 replaces development-only source-role wording by actual native binding duties. Earlier9-case trial predates ticket continuity expansion and W12 first-attempt applicability repair; exact deltas and raw outputs are supplied, so do not call it a clean successor pass. Preserve TC03 staged measurement versus missing initial whole-boundary preflight, later source-currentness corroboration, original clipping/failures and fixture-provider limits.

Judge: (1) source sufficiency and exclusions/unknown handling for each exact query, reading the complete current index and actual delivered Markdown; all selected source owners are supplied IN FULL; (2) C04/TICKETS clarification and W01/source-role changes; (3) which prior finite decisions remain applicable, naming unperformed cases and requiring new trial ONLY if a material changed causal path defeats reuse; (4) default/ticket/Skills ownership and cross-Product context interaction; (5) finite material findings/counterexamples/residuals and a NEW supported/falsified/unknown semantic judgment for EACH query. Do not infer supported from zero mechanical gaps. Prior Python judgment is context only with retained low residuals; neither its verdict nor old SDLC unknown judgment transfers.

Coverage concerns declared method constraints, not fabricated separately selected Product law. Fixture Product/requirement/design/frame/grant inputs explicitly exclude exception requests, ODD/UX and live/release actions. Query facts assert no future success. B/tags/assets/publication closure happens later and is not judged here.

A prior visual CLI result reports contextWindow1,000,000. This packet is byte-measured with all selected files complete; hidden host input and adequate attention are not claimed. Return unknown if receipt or attention proves insufficient. No silent clipping or source replacement was performed.

End with ONE fenced JSON object containing: subjects (two objects with name,index_sha256,corpus_sha256,query_sha256,status,evaluator,evidence,scope,residuals), findings, source_owner_placement, prior_evidence_applicability, required_new_trials, unperformed_or_excluded. Status supported/falsified/unknown must be your actual exact-subject judgment. Canonical coordinates are in PACKET.json below. No release/acceptance/publication verdict.
'''
paths=[w/'assessment/source-first/CLAUDE_EXPECTATIONS.md',w/'ACTIVATION.md',packet_path,f/'INPUT_READBACK.json',w/'context/final-use-01/INPUT_FREEZE.json',w/'context/final-use-01/semantic-packet/BEHAVIOR_REUSE_MAP.json',w/'assessment/final/SOURCE_CONSERVATION.json',w/'assessment/final/PRIOR_SOURCE_DELTA.patch',w/'assessment/final/REUSE_CUSTODY_AND_DELTA.json',c/'releases/3.1.0-rc.1/RELEASE.md',c/'releases/3.1.0-rc.1/MIGRATION.md']
for rel in ['purpose_context/specification/requirements/README.md','purpose_context/specification/requirements/SDLC-WORKFLOW.md','stdo_skills/specification/requirements/SCENARIOS.md','stdo_skills/specification/requirements/PURPOSE-INDEX-CONSUMPTION.md','purpose_context/skills/stdo-context/SKILL.md','purpose_context/skills/stdo-context/references/authoring.md','stdo_skills/skills/stdo-context/SKILL.md','specification_methodology/v3/specification/requirements/SDLC_DEFAULTS.md']:
 paths.append(c/rel)
paths += [native/'plugins/spec/skills'/skill/'SKILL.md' for skill in ['stdo-work','stdo-review','stdo-ticket']]
paths += sorted((w/'context/final-use-01/fixture').glob('*'))
for s in p['subjects']:
 paths += [Path(s[k]) for k in ['source_declaration_path','purpose_path','index_path','query_path','markdown_path','provenance_path','source_delta_path']]
 paths += [native/row['path'] for row in json.loads(Path(s['source_declaration_path']).read_text())['files']]
standing=c/'purpose_context/skills/stdo-context/indexes/stdo-3.0.5-rc.1-python-pure-refactor-v2/COVERAGE-STANDING.json';paths.append(standing);v=json.loads(standing.read_text())
for key in ['full_native_judgment','producer_provenance','execution_qualifications']:
 rec=v['external_assessment'][key];q=Path('/Users/jim/src/apps/specification_methodology/purpose_context')/rec['source_product_relative_path'];assert sha(q)==rec['sha256'];paths.append(q)
s=r/'SDLC_DEFAULTS_2026-11-14/actual-use';t=r/'TICKET_CONTEXT_CONSTITUTION_2026-11-14';tf=t/'review/consumer-frozen'
paths += [s/'RESULT.json',t/'trial/CONTROL.md',t/'trial/SCOPE.md',t/'trial/TASK.md',tf/'actual-use/RESULT.json',t/'review/BEHAVIOR_REVIEW.md']
paths += sorted((s/'inputs').glob('S0*.md'));paths += sorted((s/'decisions').glob('*.json'));paths += sorted((tf/'cases').glob('TC*/RETURN.json'))
paths += [tf/'actual-use/048-tc02-public-status.stdout']
for q in sorted((t/'trial/cases').rglob('*')):
 if q.is_file() and q.name not in ['RETURN.json','TICKET.md'] and q.stat().st_size<50000:paths.append(q)
parts=[intro];seen=set();rows=[]
for q in paths:
 if q in seen or not q.is_file():continue
 seen.add(q);raw=q.read_bytes();rows.append({'path':str(q),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()});parts.append('\n\n## Exact file '+str(q)+'\nSHA256 '+rows[-1]['sha256']+'; '+str(len(raw))+' bytes\n\n'+raw.decode())
(f/'PACKET.md').write_text('\n'.join(parts));(f/'PACKET_MANIFEST.json').write_text(json.dumps({'files':rows,'packet_sha256':sha(f/'PACKET.md'),'packet_bytes':(f/'PACKET.md').stat().st_size},indent=2)+'\n');print(json.dumps({'files':len(rows),'bytes':(f/'PACKET.md').stat().st_size}))
