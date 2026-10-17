"""Closure and bootstrap check of a declared package (I5-10, after review finding R1 of candidate 1).
Materialises, from git at the commit the manifest names, only the files the manifest admits, in the
installed layout (standards/, plugins/spec/, LICENSE, release/release-note.md, manifest.json); lists every
relative Markdown link whose target falls outside that set or whose anchor is missing; and checks the
bootstrap inputs PRODUCT_DEFINITION §12 names. No installer is run.
Usage, from the tenant root: python3 -I release/check_install.py <scratch dir>   (writes release/INSTALL_CHECK.json)
"""
import json, os, re, shutil, subprocess, sys
T = 'specification_methodology/v3/build_tenants/claude'
m = json.load(open('release/manifest.json')); commit = m['release']['commit']
out = sys.argv[1]; shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
def put(dst, src):
    os.makedirs(os.path.dirname(os.path.join(out, dst)) or out, exist_ok=True)
    open(os.path.join(out, dst), 'wb').write(subprocess.check_output(['git', 'show', f'{commit}:{T}/{src}']))
for x in m['standards']['members']: put('standards/' + x['path'], 'standards/' + x['path'])
for x in m['auxiliary']['plugin']['members']: put('plugins/spec/' + x['path'], 'plugins/spec/' + x['path'])
put('LICENSE', 'LICENSE'); put('release/release-note.md', 'release/release-note.md')
shutil.copy('release/manifest.json', os.path.join(out, 'manifest.json'))
def slug(h): return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
anchors = {}
for dp, _, fs in os.walk(out):
    for f in fs:
        if f.endswith('.md'):
            p = os.path.join(dp, f); seen = {}; a = set(); code = False
            for line in open(p, encoding='utf-8'):
                if line.startswith('```'): code = not code
                mm = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
                if mm:
                    s = slug(mm.group(2)); n = seen.get(s, 0); seen[s] = n + 1; a.add(s if n == 0 else f'{s}-{n}')
            anchors[os.path.abspath(p)] = a
outside, bad_anchor = [], []
for p in anchors:
    for mm in re.finditer(r'\]\(([^)\s]+)\)', open(p, encoding='utf-8').read()):
        t = mm.group(1)
        if re.match(r'^[a-z][a-z0-9+.-]*:', t): continue
        path, _, frag = t.partition('#')
        tgt = os.path.abspath(os.path.join(os.path.dirname(p), path)) if path else p
        rel = os.path.relpath(p, out)
        if not os.path.exists(tgt): outside.append((rel, t)); continue
        if frag and tgt.endswith('.md') and frag not in anchors.get(tgt, set()): bad_anchor.append((rel, t))
boot = {}
for name in ('standards/templates/PRODUCT_DEFINITION_TEMPLATE.json', 'standards/schemas/product-definition.schema.json'):
    q = os.path.join(out, name); boot[name] = {'present': os.path.exists(q)}
    if os.path.exists(q):
        try: json.load(open(q)); boot[name]['parses'] = True
        except Exception as e: boot[name]['parses'] = f'no: {e}'
import jsonschema
sch = json.load(open(os.path.join(out, 'standards/schemas/product-definition.schema.json')))
V = jsonschema.validators.validator_for(sch)
try: V.check_schema(sch); boot['schema_is_valid_json_schema'] = True
except Exception as e: boot['schema_is_valid_json_schema'] = f'no: {str(e)[:200]}'
tpl = json.load(open(os.path.join(out, 'standards/templates/PRODUCT_DEFINITION_TEMPLATE.json')))
errs = list(V(sch).iter_errors(tpl))
boot['template_against_schema'] = ('validates as it stands' if not errs else
    f'{len(errs)} errors as it stands (a fill-in template with placeholders; not a filled definition)')
boot['template_first_errors'] = [f'{list(e.path)}: {e.message[:120]}' for e in errs[:5]]
rec = {'kind': 'claude-install-closure-and-bootstrap-check', 'commit': commit, 'installed_files': sum(len(fs) for _, _, fs in os.walk(out)),
       'links_outside_package': outside, 'links_with_missing_anchor': bad_anchor, 'bootstrap_inputs': boot,
       'limits': 'Built from git at the commit, with only the manifest-admitted files; no installer, toolchain manager or network was used; template validation is reported as found, not claimed.'}
json.dump(rec, open('release/INSTALL_CHECK.json', 'w'), indent=1)
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in rec.items() if k != 'bootstrap_inputs'}), json.dumps(boot)[:700])
for r, t in outside: print('OUTSIDE', r, t)
for r, t in bad_anchor: print('ANCHOR', r, t)
fail = bool(bad_anchor) or boot.get('schema_is_valid_json_schema') is not True or any(not v.get('present') or v.get('parses') is not True for k, v in boot.items() if k.startswith('standards/'))
sys.exit(1 if fail else 0)  # a missing anchor or an absent, unparseable or invalid bootstrap input fails the check
