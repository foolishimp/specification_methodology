'use strict';
// Real local Chrome; separate temporary profile, no existing session changed.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const runtime = '/Users/jim/.npm/_npx/9833c18b2d85bc59/node_modules/playwright';
const {chromium} = require(runtime);
const artifact = path.resolve(process.argv[2]);
const out = path.join(__dirname, 'browser-final-001');
fs.mkdirSync(out);
const result = {profile:'stdo.visual-browser-observation/1', artifact,
  playwright:JSON.parse(fs.readFileSync(path.join(runtime,'package.json'))).version,
  browser:null, checks:[], errors:[], requests:[], limitations:[], status:'running'};
let browser;
const check = (name, detail) => result.checks.push({name, detail});
(async()=>{
  try {
    browser = await chromium.launch({channel:'chrome',headless:true});
    result.browser = browser.version();
    const context = await browser.newContext({viewport:{width:1680,height:1050},offline:true});
    const page = await context.newPage();
    page.on('request',req=>result.requests.push(req.url()));
    page.on('pageerror',error=>result.errors.push(String(error)));
    await page.goto(pathToFileURL(artifact).href);
    await page.locator('#details h2').waitFor();
    const data = JSON.parse(await page.locator('#explorer-data').textContent());
    assert.equal(Object.keys(data.sources).length,3);
    assert.equal(data.counts.records,306);
    assert.match(await page.locator('#details').innerText(),/Where no capacity is declared/);
    assert.match(await page.locator('#details').innerText(),/selected envelope declares context capacity/);
    check('full conditional record reading',{records:data.counts.records,initialFamily:'constraints',conditionAndExceptionVisible:true});
    await page.screenshot({path:path.join(out,'01-condition-reader.png'),fullPage:true});

    if (!(await page.locator('#files-pane').isVisible())) await page.locator('#files-toggle').click();
    await page.locator('#file-query').fill('SDLC_DEFAULTS.md');
    await page.locator('#file-tree button').first().click();
    await page.locator('#file-scope').getByRole('button',{name:'Read file',exact:true}).click();
    assert.match(await page.locator('#source-text').innerText(),/Where no\ncapacity is declared, no measurement gate is added/);
    assert.match(await page.locator('#source-title').innerText(),/SDLC_DEFAULTS.md$/);
    check('source file navigation',{path:await page.locator('#source-title').innerText(),sha256:data.sources[Object.keys(data.sources).find(p=>p.endsWith('/SDLC_DEFAULTS.md'))].sha256});
    await page.screenshot({path:path.join(out,'02-exact-source.png'),fullPage:true});
    await page.locator('#source-close').click();
    await page.locator('#file-scope').getByRole('button',{name:'All files',exact:true}).click();
    await page.locator('#family').selectOption('objects');
    await page.locator('#query').fill('Selected work carrier');
    const work = data.nodes.find(n=>n.family==='objects' && n.record.value.label==='Selected work carrier');
    const contextNode = data.nodes.find(n=>n.family==='objects' && n.record.value.label==='Bounded context acquisition');
    await page.locator('#results button').filter({hasText:'Selected work carrier'}).click();
    const link = data.links.find(l=>l.layer==='relation' && l.source===work.id && l.target===contextNode.id);
    assert.ok(link);
    const relationButton = page.locator('#details button').filter({hasText:'Bounded context acquisition'}).filter({has:page.locator('small')});
    const exactLink = page.locator('#details button[data-link]').filter({hasText:'Authored:'}).filter({hasText:'Bounded context acquisition'});
    await exactLink.click();
    assert.equal(await page.locator('#details h2').textContent(),'Bounded context acquisition');
    check('authored relation direction',{source:work.id,target:contextNode.id,link:link.id,targetReached:true});
    await page.locator('#back').click();
    await page.locator('#details').evaluate((node,id)=>{
      const button=[...node.querySelectorAll('button[data-link]')].find(b=>b.dataset.link===id);
      if (!button) throw Error('exact relation is not visible');
      button.nextElementSibling.click();
    },link.id);
    assert.match(await page.locator('#details').innerText(),/creates no additional carrier requirement/);
    assert.match(await page.locator('#details').innerText(),/result\/evidence references and surviving obligations/);
    check('relation qualifications',{conditionAndExceptionVisible:true,recordId:link.record_id});
    await page.screenshot({path:path.join(out,'03-relation-qualifications.png'),fullPage:true});

    await page.locator('#family').selectOption('residuals');
    await page.locator('#query').fill('remainder of this section');
    await page.locator('#results button').first().click();
    const residualText = await page.locator('#details').innerText();
    assert.match(residualText,/not comprehensively represented/);
    assert.match(residualText,/does not establish semantic coverage/);
    check('unrepresented meaning visible',{family:'residuals',sourceReentryConsequenceVisible:true});
    const before = await page.locator('#details').innerText();
    const hashBefore = await page.evaluate(()=>location.hash);
    for (const mode of ['mode2','mode3','mode-layered']) {
      if (await page.locator('#'+mode).isDisabled()) {
        result.limitations.push(mode+' unavailable: '+await page.locator('#renderer-status').innerText());
        continue;
      }
      await page.locator('#'+mode).click();
      assert.equal(await page.locator('#details').innerText(),before);
      assert.equal(await page.evaluate(()=>location.hash),hashBefore);
      const active = await page.locator('#'+mode).getAttribute('aria-pressed');
      if(active !== 'true') result.limitations.push(mode+' did not activate: '+await page.locator('#renderer-status').innerText());
      else check('view state '+mode,{recordAndHashPreserved:true,actualModeActive:true});
    }
    await page.screenshot({path:path.join(out,'04-residual-layered.png'),fullPage:true});
    assert.equal(result.requests.filter(url=>/^https?:/.test(url)).length,0);
    assert.deepEqual(result.errors,[]);
    check('offline browser boundary',{httpRequests:0,pageErrors:0});
    result.status='passed';
  } catch(error) {
    result.status='failed'; result.failure=String(error); result.stack=error.stack;
    process.exitCode=2;
  } finally {
    if(browser) await browser.close();
    fs.writeFileSync(path.join(out,'RESULT.json'),JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify(result));
  }
})();
