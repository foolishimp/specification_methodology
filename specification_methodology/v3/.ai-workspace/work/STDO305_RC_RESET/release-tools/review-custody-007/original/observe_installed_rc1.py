from pathlib import Path
import hashlib,importlib.metadata,json,platform,time,traceback
from urllib.parse import quote
from playwright.sync_api import sync_playwright
import sys
SELECTION_PATH=Path(sys.argv[1]).resolve()
SELECTED=json.loads(SELECTION_PATH.read_bytes())
OUT=Path(__file__).resolve().parent/SELECTED['output_name'];OUT.mkdir(exist_ok=False)
WORK=Path(SELECTED['workspace'])
assert WORK.is_absolute() and '..' not in WORK.parts
CUT=SELECTED['cut'];VERSION=SELECTED['version']
assert CUT=='v'+VERSION and VERSION=='3.0.5-rc.1'
PAGE=WORK/'source-tools/stdo_representation/build_tenants/a_c/representation'/('stdo-'+CUT)/'explorer.html'
DOC=WORK/'store/releases'/CUT/'standards/documentation'
LANDING=DOC/'index.html';NATIVE=DOC/'constraint-explorer/index.html';PROOF=DOC/'proofs/index.html'
CHROME=Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
SEED='urn:a-c:generation:ba37e2825e4e3c758a5cfaec:record:e17777d4ad97c92bf9f2402e9341ee1c'
MODEL=SELECTED['model']
PINS={PAGE:SELECTED['pins']['explorer'],LANDING:SELECTED['pins']['landing'],NATIVE:SELECTED['pins']['native_explorer'],PROOF:SELECTED['pins']['proof_reader']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in PINS.items():assert sha(p)==h,str(p)
profile=OUT/'isolated-profile';started=time.time_ns()
result={'kind':'stdo.current-browser-observation/1','status':'incomplete','assessor':'/root/stdo305_integration_review','authors':['/root/stdo305_release_tools','/root/stdo305_tools_skills','/root/stdo305_representation'],'page':{'path':str(PAGE),'sha256':PINS[PAGE]},'source_identity_sha256':SELECTED['source_identity_sha256'],'model':MODEL,'errors':[],'observations':{},'documentation_observations':[],'network_requests':[],'blocked_requests':[],'request_failures':[],'console':[],'driver':{'playwright':importlib.metadata.version('playwright'),'python':platform.python_version()},'browser':{'executable':str(CHROME),'sha256':sha(CHROME),'fresh_profile':str(profile),'offline':True,'headless':True},'limits':['Single fresh local Chrome/Playwright session; same-family nonauthor observation, not enforced clean-room independence.','File routes and actual visible browser interaction only; no Lean execution or proof-acceptance inference.','OS/browser background telemetry is not packet-captured; page request events, offline context and route refusal are recorded.'],'selected_record':SEED}
def screenshot(page,name):
 p=OUT/(name+'.png');page.screenshot(path=str(p));return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
def observed(page,key,action,visible):result['observations'][key]={'observed':True,'action':action,'visible_result':visible,'screenshot':screenshot(page,key)}
def docobserved(page,key,action,visible):result['documentation_observations'].append({'id':key,'observed':True,'action':action,'visible_result':visible,'screenshot':screenshot(page,key)})
page=None;context=None
try:
 with sync_playwright()as pw:
  context=pw.chromium.launch_persistent_context(str(profile),executable_path=str(CHROME),headless=True,viewport={'width':1920,'height':1200},service_workers='block',accept_downloads=False,args=['--disable-background-networking','--disable-component-update','--disable-sync','--no-first-run'])
  context.set_offline(True)
  allowed={p.as_uri()for p in PINS}
  def route(r):
   if r.request.url.split('#')[0]in allowed or r.request.url.startswith('data:'):r.continue_()
   else:result['blocked_requests'].append(r.request.url);r.abort()
  context.route('**/*',route)
  context.on('request',lambda r:result['network_requests'].append({'url':r.url,'method':r.method,'resource_type':r.resource_type}))
  context.on('requestfailed',lambda r:result['request_failures'].append({'url':r.url,'failure':r.failure}))
  page=context.pages[0];page.set_default_timeout(20000)
  page.on('console',lambda m:result['console'].append({'type':m.type,'text':m.text}))
  page.on('pageerror',lambda e:result['errors'].append(str(e)))
  result['browser']['version']=context.new_cdp_session(page).send('Browser.getVersion')
  page.goto(PAGE.as_uri()+'#'+quote(SEED,safe=''),wait_until='load');page.locator('#details h2').wait_for();selected=page.url.split('#',1)[1]
  info=json.loads(page.locator('#model-info').text_content());assert info['model']==MODEL
  title=page.locator('#details h2').inner_text();result['selected_title']=title
  assert not page.locator('#mode3').is_disabled(),page.locator('#renderer-status').inner_text()
  page.locator('#mode3').click();page.wait_for_timeout(2500);page.locator('#fit').click();page.wait_for_timeout(500)
  assert page.locator('#mode3').get_attribute('aria-pressed')=='true';assert page.url.split('#',1)[1]==selected
  canvas=page.locator('#graph canvas').first
  if not canvas.count():canvas=page.locator('canvas').first
  box=canvas.bounding_box();assert box and box['width']>0 and box['height']>0
  observed(page,'3d','Opened exact installed materialized file; selected constraint; chose 3D and Fit.',{'selected_title':title,'renderer':page.locator('#renderer-status').inner_text(),'canvas':box,'selection_preserved':True})
  page.locator('#mode2').click();page.wait_for_timeout(2500);page.locator('#fit').click();page.wait_for_timeout(500)
  page.wait_for_function("document.querySelector('#node-labels .map-label.selected:not([hidden])') !== null")
  assert page.locator('#mode2').get_attribute('aria-pressed')=='true'and page.url.split('#',1)[1]==selected
  labels=page.locator('#node-labels .map-label:not([hidden])').all_inner_texts();assert labels
  observed(page,'2d','Switched same selection to 2D and Fit; checked visible selected node label.',{'selected_title':title,'visible_labels':labels,'selection_preserved':True})
  page.locator('#mode-layered').click();page.locator('.tracks-node').first.wait_for();assert page.url.split('#',1)[1]==selected
  cards=page.locator('.tracks-node').evaluate_all('(nodes)=>nodes.map(n=>({id:n.dataset.id,x:n.offsetLeft,y:n.offsetTop,width:n.offsetWidth,height:n.offsetHeight}))');assert len({r['x']for r in cards})>1
  assert page.locator('.tracks-node[data-id="'+SEED+'"]').count()==1
  observed(page,'layered','Switched same selection to Layered; checked selected card and multiple track columns.',{'cards':cards,'selection_preserved':True})
  page.locator('#details .grounding .source-link').first.click();assert page.locator('#source-dialog').is_visible();assert page.locator('#source-text .selected-line').count()>0
  observed(page,'source','Opened selected constraint grounding passage.',{'title':page.locator('#source-title').inner_text(),'digest':page.locator('#source-digest').inner_text(),'highlighted_lines':page.locator('#source-text .selected-line').all_inner_texts()})
  page.locator('#source-close').click();page.locator('#details .record-source button').first.click();assert page.locator('#file-scope').is_visible();assert page.locator('#file-tree [aria-current="true"]').count()==1
  scope=page.locator('#file-scope').inner_text();page.locator('#file-scope').get_by_role('button',name='Read file',exact=True).click();assert page.locator('#source-dialog').is_visible();length=len(page.locator('#source-text').inner_text());assert length>100;page.locator('#source-close').click()
  observed(page,'files','Revealed owning file in Files tree, opened full embedded file, and returned to same constraint.',{'scope':scope,'full_file_characters':length,'selected_file_count':1,'selection_preserved':page.url.split('#',1)[1]==selected})
  page.locator('#file-scope').get_by_role('button',name='All files',exact=True).click();page.locator('#details .connection[data-layer="required"]').first.click();assert page.url.split('#',1)[1]!=selected;target=page.locator('#details h2').inner_text();page.locator('#back').click();assert page.url.split('#',1)[1]==selected
  result['dependency_navigation']={'observed':True,'target':target,'returned_to':title}
  page.goto(LANDING.as_uri(),wait_until='load');assert 'STDO '+VERSION in page.title();docobserved(page,'landing','Opened installed offline documentation landing.',{'title':page.title(),'current_explorer_href':page.get_by_role('link',name='Current constraints →',exact=True).get_attribute('href'),'proof_reader_href':page.get_by_role('link',name='Current model proofs →',exact=True).get_attribute('href')})
  page.get_by_role('link',name='Current constraints →',exact=True).click();page.wait_for_function("document.querySelector('#model-info')?.textContent.trim().startsWith('{')");assert page.url.split('#')[0]==NATIVE.as_uri();assert json.loads(page.locator('#model-info').text_content())['model']==MODEL
  result['documentation_observations'].append({'id':'landing-native-explorer','observed':True,'action':'Clicked Current constraints from installed landing.','visible_result':{'url':page.url,'model':MODEL}})
  page.goto(LANDING.as_uri(),wait_until='load');page.get_by_role('link',name='Current model proofs →',exact=True).click();page.wait_for_function("expected => document.querySelector('#model')?.textContent.includes(expected)",arg=MODEL['sha256']);assert page.url==PROOF.as_uri();assert MODEL['sha256']in page.locator('#model').inner_text()
  binding=json.loads(page.locator('#proof-data').text_content())['catalog'];assert binding['result_sha256']==SELECTED['proof']['result_sha256'];assert binding['runtime_identity']['sha256']==SELECTED['proof']['runtime_sha256'];result['actual_proof_binding']={'result_sha256':binding['result_sha256'],'runtime_sha256':binding['runtime_identity']['sha256'],'limits':binding['observations']['limits']}
  counts=page.locator('#counts').inner_text();assert counts=='7 current elaborations · 1 kernel replay · 1 runtime invocation';docobserved(page,'proof-reader','Clicked Current model proofs from installed landing.',{'url':page.url,'counts':counts,'bounds':page.locator('.boundary').inner_text()})
  theorem='AC.GateData.result0';page.locator('#query').fill(theorem);page.locator('#results').get_by_role('button',name=theorem,exact=True).click();assert page.locator('#reader h2').inner_text()==theorem
  statement=page.locator('#reader > pre').inner_text();assert 'project model seeds0 trace0 21 = .ok'in statement
  docobserved(page,'proof-declaration','Searched and opened current selected-view result theorem.',{'theorem':theorem,'statement':statement,'location':page.locator('#reader > p').inner_text()})
  page.locator('#reader nav').get_by_role('button',name='AC.project (line 65)',exact=True).click();assert page.locator('#reader h2').inner_text()=='AC.project';definition=page.locator('#reader > pre').inner_text();page.locator('#back').click();assert page.locator('#reader h2').inner_text()==theorem
  page.locator('#reader > button').click();assert page.locator('#reader h2').inner_text()=='current/GateViews.lean';selectedline=page.locator('#reader .source-row.selected').inner_text();assert 'theorem result0'in selectedline
  docobserved(page,'proof-source','Followed lexical AC.project reference, returned with Back, then opened full current source at theorem line65.',{'reference_target':'AC.project','reference_statement':definition,'file':'current/GateViews.lean','selected_line':selectedline})
  assert not result['errors'],result['errors'];assert not result['blocked_requests'],result['blocked_requests'];assert not result['request_failures'],result['request_failures']
  result['status']='observed';context.close();result['owned_browser_closed']=True
except Exception as e:
 result['errors'].append(type(e).__name__+': '+str(e));result['traceback']=traceback.format_exc()
 if page is not None:
  try:result['failure_screenshot']=screenshot(page,'failure')
  except Exception as screenshot_error:result['failure_screenshot_error']=str(screenshot_error)
if context is not None and not result.get('owned_browser_closed'):
 try:context.close();result['owned_browser_closed']=True
 except Exception as close_error:result['browser_close_error']=str(close_error)
result['selected_input']={'path':str(SELECTION_PATH),'sha256':sha(SELECTION_PATH),'protocol':'file://'}
result['elapsed_seconds']=(time.time_ns()-started)/1e9
result['pages_unchanged_after']={str(p):sha(p)==h for p,h in PINS.items()}
result['harness']={'path':str(Path(__file__).resolve()),'sha256':sha(Path(__file__))}
(OUT/'OBSERVATION.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':result['status'],'observations':list(result['observations']),'documentation_observations':[x['id']for x in result['documentation_observations']],'errors':result['errors'],'console':result['console'],'page_unchanged':result['pages_unchanged_after'],'report':str(OUT/'OBSERVATION.json')}))
raise SystemExit(0 if result['status']=='observed' else 2)
