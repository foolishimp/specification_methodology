"""Actual isolated offline browser checks of the selected generated viewer."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import platform
import tempfile
import time
from urllib.parse import quote
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parents[6]
WORK = Path(__file__).resolve().parent
PAGE = REPO / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5/explorer.html'
BROWSER = Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
SEED = 'urn:a-c:generation:ba37e2825e4e3c758a5cfaec:record:e17777d4ad97c92bf9f2402e9341ee1c'


def main(out):
    out.mkdir(exist_ok=False); started = time.time_ns()
    profile = Path(tempfile.mkdtemp(prefix='stdo305-offline-viewer-')).resolve()
    result = {'schema': 'stdo305.offline-viewer-browser/1', 'status': 'incomplete',
              'artifact': str(PAGE), 'artifact_sha256': hashlib.sha256(PAGE.read_bytes()).hexdigest(),
              'browser_executable': str(BROWSER), 'browser_sha256': hashlib.sha256(BROWSER.read_bytes()).hexdigest(),
              'driver': {'playwright': importlib.metadata.version('playwright'), 'python': platform.python_version()},
              'isolated_profile': str(profile), 'selected_record': SEED, 'checks': [], 'requests': [], 'console': [], 'page_errors': []}
    page = None
    try:
        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(str(profile), executable_path=str(BROWSER), headless=True,
                viewport={'width': 1920, 'height': 1200}, service_workers='block', accept_downloads=False,
                args=['--disable-background-networking', '--disable-component-update', '--disable-sync', '--no-first-run'])
            result['browser_version'] = context.browser.version if context.browser else None
            context.set_offline(True)
            def route(request):
                url = request.request.url
                result['requests'].append(url)
                if url.split('#')[0] == PAGE.as_uri(): request.continue_()
                else: request.abort()
            context.route('**/*', route)
            page = context.pages[0]
            page.on('console', lambda message: result['console'].append({'type': message.type, 'text': message.text}))
            page.on('pageerror', lambda error: result['page_errors'].append(str(error)))
            page.goto(PAGE.as_uri() + '#' + quote(SEED, safe=''), wait_until='load')
            page.locator('#details h2').wait_for()
            selected = page.url.split('#', 1)[1]
            result['initial_title'] = page.locator('#details h2').inner_text()
            info = json.loads(page.locator('#model-info').text_content())
            result['model_info'] = info
            assert info['model']['sha256'] == 'ceea71dd812d9168ee173d279383e7d557333601c2aa05244cea79afce703a02'
            assert not page.locator('#mode2').is_disabled(), page.locator('#renderer-status').inner_text()
            page.locator('#mode2').click()
            # The force layout runs eighty ticks before automatic framing. Wait
            # for that bounded animation, then exercise the visible Fit control.
            page.wait_for_timeout(2500); page.locator('#fit').click(); page.wait_for_timeout(600)
            page.wait_for_function("document.querySelector('#node-labels .map-label.selected:not([hidden])') !== null", timeout=20000)
            assert page.locator('#mode2').get_attribute('aria-pressed') == 'true'
            assert page.url.split('#', 1)[1] == selected
            labels = page.locator('#node-labels .map-label:not([hidden])').all_inner_texts()
            assert labels
            result['visible_2d_labels'] = labels
            page.screenshot(path=str(out / '2d-labels.png'))
            result['checks'].append('current-model-2d-visible-labels-and-selection')
            page.locator('#mode-layered').click()
            page.locator('.tracks-node').first.wait_for()
            assert page.url.split('#', 1)[1] == selected
            selected_card = page.locator('.tracks-node[data-id="' + SEED + '"]')
            assert selected_card.count() == 1
            boxes = page.locator('.tracks-node').evaluate_all('(nodes) => nodes.map(n => ({id:n.dataset.id,x:n.offsetLeft,y:n.offsetTop,width:n.offsetWidth,height:n.offsetHeight}))')
            assert len({row['x'] for row in boxes}) > 1
            result['layered_nodes'] = boxes
            page.screenshot(path=str(out / 'layered.png'))
            result['checks'].append('layered-layout-and-selection-preservation')
            page.locator('#details .grounding .source-link').first.click()
            assert page.locator('#source-dialog').is_visible()
            assert page.locator('#source-text .selected-line').count() > 0
            result['source_title'] = page.locator('#source-title').inner_text()
            result['source_digest'] = page.locator('#source-digest').inner_text()
            page.screenshot(path=str(out / 'source-lines.png'))
            page.locator('#source-close').click()
            result['checks'].append('embedded-source-and-selected-grounding-lines')
            page.locator('#details .record-source button').first.click()
            assert page.locator('#file-scope').is_visible()
            assert page.locator('#file-tree [aria-current="true"]').count() == 1
            assert page.url.split('#', 1)[1] == selected
            result['file_scope'] = page.locator('#file-scope').inner_text()
            page.locator('#file-scope').get_by_role('button', name='Read file', exact=True).click()
            assert page.locator('#source-dialog').is_visible()
            assert len(page.locator('#source-text').inner_text()) > 100
            page.locator('#source-close').click()
            result['checks'].append('file-reveal-and-full-embedded-source-navigation')
            page.locator('#file-scope').get_by_role('button', name='All files', exact=True).click()
            connection = page.locator('#details .connection[data-layer="required"]').first
            connection.click()
            assert page.url.split('#', 1)[1] != selected
            assert not page.locator('#back').is_disabled()
            page.locator('#back').click()
            assert page.url.split('#', 1)[1] == selected
            result['checks'].append('required-dependency-traversal-and-reading-trail-return')
            page.locator('#mode3').click()
            assert page.locator('#mode3').get_attribute('aria-pressed') == 'true'
            assert page.url.split('#', 1)[1] == selected
            result['checks'].append('3d-switch-preserves-selected-record')
            assert not result['page_errors'], result['page_errors']
            assert all(url.split('#')[0] == PAGE.as_uri() for url in result['requests']), result['requests']
            result['status'] = 'passed'
            context.close()
    except Exception as error:
        result['error'] = type(error).__name__ + ': ' + str(error)
        if page is not None:
            try: page.screenshot(path=str(out / 'failure.png'))
            except Exception: pass
    result['elapsed_seconds'] = (time.time_ns() - started) / 1e9
    (out / 'result.json').write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'checks': result['checks'], 'error': result.get('error'), 'result': str(out / 'result.json')}))
    return 0 if result['status'] == 'passed' else 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--output', type=Path, required=True)
    raise SystemExit(main(parser.parse_args().output.absolute()))
