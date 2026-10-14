import json,re,sys
SP='/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/d981044e-6161-45df-a96b-ed922fafa91b/scratchpad/'
d=json.load(open(SP+'frontier_changes.json'))
p='frontier/PREDECESSOR_CLAIMS.md'
L=open(p,encoding='utf-8').read().split('\n')
log=[]
def cols(n): return L[n-1].split(' | ')
def setc(n,c): L[n-1]=' | '.join(c)
def dispidx(c): return 3 if len(c)==5 else 4
def add_locus(n,loc):
    c=cols(n); loc=loc.strip('`')
    tail=c[-1]; assert tail.endswith('|'),(n,tail[-20:])
    body=tail[:-1].rstrip()
    if loc in body: return
    body=(body+'; ' if body else '')+f'`{loc}`'
    c[-1]=body+' |'; setc(n,c); log.append((n,'locus+',loc))
def set_cell(n,new):
    c=cols(n); i=dispidx(c); c[i]=new; setc(n,c); log.append((n,'cell',new[:50]))
def app_cell(n,suffix):
    c=cols(n); i=dispidx(c); c[i]=c[i].rstrip()+suffix; setc(n,c); log.append((n,'cell+',suffix[:50]))
def sub_cell(n,a,b):
    c=cols(n); i=dispidx(c); assert a in c[i],(n,a[:40]); c[i]=c[i].replace(a,b,1); setc(n,c); log.append((n,'sub',b[:50]))
skip={439,481,593,606,610,517,511,526,556,516,569,668,683,794,162,820,821,141,444,607,423}
for o in d:
    n=o['row']; a=o['anchor']
    if a.startswith('`#'): assert a in L[n-1],(n,a)
    if o.get('proposed_locus'):
        for loc in re.split(r';\s*',o['proposed_locus']):
            if loc.strip(): add_locus(n,loc)
    if n in skip or not o.get('proposed_cell'): continue
    pc=o['proposed_cell']
    if pc.startswith(';'): app_cell(n,pc)
    else: set_cell(n,pc)
# substring replacements from the extraction
by={(o['row'],o['delta'][:5]):o for o in d}
sub_cell(444,"the proxy limits also at EVALUATION §5",by[(444,'I3-2a')]['proposed_cell'])
c=cols(607)[4]; i=c.index('ACTIVATION §7')+len('ACTIVATION §7')
cc=cols(607); cc[4]=c[:i]+', '+by[(607,'I3-2c')]['proposed_cell']+c[i:]; setc(607,cc); log.append((607,'ins',''))
sub_cell(423,"and abrupt loss, unavailable rollback or an unverified restoration is `completion_unknown`",by[(423,'I3-2c')]['proposed_cell'])
c=cols(141)[4]; s=c.index("`satisfied` for `not_applicable` never establishes"); e=c.index("under ACTIVATION §1 Applicability",s)+len("under ACTIVATION §1 Applicability")
cc=cols(141); cc[4]=c[:s]+by[(141,'I3-3b')]['proposed_cell']+c[e:]; setc(141,cc); log.append((141,'span',''))
# overrides for cells made stale by I3-2r
app_cell(439,"; material advance, prerequisite readiness, preservation and regression are stated as refinements of the progress categories of ACTIVATION §5, regression mapping to evidence that is not new progress with the promotion block added to it")
set_cell(481,"conserved; the eight rules, three classifications, seven steps and three migration conditions; for an inherited requirement, the relation of the four migration classes (the adoption decision) to the legacy classifications of §2 (live-surface standing) is stated, a requirement whose adoption is deferred staying outside the live surface with no authority until adopted, and their relation to the successor dispositions of RELEASE §9 is stated (new, with its purpose stated where it is written)")
sub_cell(593,"the six classifications consume the item's review results and stay separate from them, like a disposition of ACTIVATION §3","the close review makes the six classifications under the sprint authority; each consumes the item's review results, stays separate from them and uses ACTIVATION §3 only for its result mapping, `remove` matching no disposition")
set_cell(606,"conserved; the four blocking conditions and the outside-observation rule are EVALUATION §5 When a finding blocks promotion, which this carrier applies; what counts as independent, the reviewer not being the author included, and the generic assessment protocol are EVALUATION §3; the boundaries that require independent review are kept here as this method's policy, which EVALUATION §3 names in its body")
app_cell(610,"; recording a result without review is ACTIVATION §1, applied with the ticket as the existing carrier; this section is named the owner of the closure condition, which SPEC_METHOD §4 Consistency gate applies and SPEC_METHOD §9 supplies evidence for; the invalidators are named as instances of the reuse rule of ACTIVATION §7, the stated revising observation of a recorded J among them, as §7 Recorded judgment and owner-ruling continuity already required")
add_locus(610,"ACTIVATION.md#roles-and-delegation")
# parents of new child rows
for n,word in ((511,'clause'),(526,'clause'),(556,'order')):
    c=cols(n); i=dispidx(c); assert c[i].startswith('conserved; '),n
    c[i]=f'conserved, save the {word} split to the child row below; '+c[i][len('conserved; '):]; setc(n,c); log.append((n,'parent',''))
# proposed supersessions
PS="superseded, proposed and pending the product owner's acceptance"
set_cell(668,PS+", by PRODUCT_DEFINITION §7, under which only Product authority adopts an available profile, a product definition, ticket, design module or review being where the adoption is recorded; the rest conserved: sole UX realisation authority, ADRs choose the stack and may not weaken the model, the seven evidence-only kinds, fail closed with its three exits, now mapped to ACTIVATION §3 Ambiguity outcome; ambiguity governance is SPEC_METHOD §5, pointed to")
add_locus(668,"PRODUCT_DEFINITION.md#7-collective-reference-frame-basis")
set_cell(683,PS+", by PRODUCT_DEFINITION §7, under which Product authority adopts the profile for a project and the nine steps record the adoption; the rest conserved: the nine adoption steps, per-project adoption at \"may\" with the scope recorded; step 3's structural carrier diagram is pointed to DESIGN_MODULE §6 and §7")
add_locus(683,"PRODUCT_DEFINITION.md#7-collective-reference-frame-basis")
set_cell(794,PS+", by the SPEC_METHOD §2 Specification surface rule, which states the rule at mandatory force and names superseded material among the label uses; the guide keeps the six preferred terms. The predecessor's SPEC_METHOD already bound the same surfaces at mandatory force")
add_locus(794,"SPEC_METHOD.md#specification-surface-rule")
set_cell(162,PS+", by PRODUCT_DEFINITION §7, under which only Product authority adopts an available profile; DESIGN_MODULE §12 Adoption keeps rc.2 #15's four \"may\" means as the means by which that authority records its adoption, and keeps the rest of #15 unchanged")
sub_cell(820,"every placeholder, section and instruction restated","every placeholder, section and instruction restated, with owner citations")
c=cols(821); i=3; assert 'section 6' in c[i]; c[i]=c[i].replace('section 6','section 5 (corrected from section 6)',1); setc(821,c); log.append((821,'sub','section 5'))
# mark existing supersessions proposed
for n in (517,524,546,564,570):
    c=cols(n); i=dispidx(c)
    for a,b in (("superseded by the common single result algebra requirement, item 3, applied by ACTIVATION §3 Construction availability",PS+", by ACTIVATION §3 Construction availability, which applies the common single result algebra requirement, item 3"),("superseded by the common single result algebra requirement, item 3:",PS+", by ACTIVATION §3 Construction availability, which applies the common single result algebra requirement, item 3:")):
        if c[i].startswith(a): c[i]=b+c[i][len(a):]; break
    else: raise SystemExit(n)
    setc(n,c); log.append((n,'proposed',''))
for n,a,b in ((210,"superseded; ",PS+"; "),(657,"superseded by AXIOMATIC_CALCULUS §8",PS+", by AXIOMATIC_CALCULUS §8")):
    c=cols(n); i=dispidx(c); assert c[i].startswith(a),n; c[i]=b+c[i][len(a):]; setc(n,c); log.append((n,'proposed',''))
# new child rows, inserted bottom-up
P=open('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md',encoding='utf-8').read()
def nbytes(s): return f"{len(s.encode()):,}"
kids={
556:("Missing-Frame And Re-Entry Application: order","#missing-frame-and-re-entry-application-order",nbytes("5. verify required specialist-frame inputs;"),PS+", by REFERENCE_FRAME §10 Diagnostic order, read with this profile's two readings: the Executive asks all eight questions in order, verifying the specialist-frame inputs before question 5","`EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application`; `REFERENCE_FRAME.md#diagnostic-order`"),
526:("Derived Generic Specialist Frame Set: seam result","#derived-generic-specialist-frame-set-seam-result",nbytes("A missing or non-commuting seam returns the applicable `falsified`, `indeterminate`, `out_of_frame`, or `invalid_basis` result."),PS+", by the common single result algebra requirement, item 3, applied by FOUNDATIONS §4 Conjunction of results, Gaps: a seam with no applicable closed result is a planned assessment without a closed result, and a seam no assessment addresses is uncovered coverage, each a gap with no value of its own","`EXECUTIVE_BASELINE.md#11-derived-generic-specialist-frame-set`; `FOUNDATIONS.md#conjunction-of-results`"),
511:("Executive Drift Locks: stale held result","#executive-drift-locks-stale-held-result",nbytes("A stale or substituted basis is `invalid_basis`."),PS+", by FOUNDATIONS §4 Conjunction of results, Stale results: a result already held when the basis lock fails is a gap for the disposition's conjunction, never relabelled `invalid_basis` and never counted as returned","`EXECUTIVE_BASELINE.md#drift-locks`; `FOUNDATIONS.md#conjunction-of-results`"),
}
for n in sorted(kids,reverse=True):
    t,a,b,cell,loc=kids[n]
    L.insert(n,f"| &nbsp;&nbsp;&nbsp;&nbsp;{t} | `{a}` |  | {b} | {cell} | {loc} |"); log.append((n+1,'child',a))
open(p,'w',encoding='utf-8').write('\n'.join(L))
print(len(log)); 
