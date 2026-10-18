"""Trial packets (I4-06). Run from the tenant root with python3 -I.

  trial_packets.py writers            -> trial/writers/TT-nn.md: the task sentence and the owning
                                         sections of the frame's routes (whole sections), for the
                                         expectation writer; no frame text
  trial_packets.py actors TT-nn ARM K -> trial/runs/TT-nn/ARM-K.md: the card, the task, the fixture
                                         from trial/expectations/TT-nn.md and, for A1 and A3, the
                                         frame's bytes; prints the supplied byte count
  trial_packets.py copy DIR           -> an isolated read-only copy of standards/ at DIR for A3 and A5
"""
import hashlib, json, os, re, shutil, sys
sys.argv_saved = list(sys.argv); sys.argv = [sys.argv[0], '--whole']
exec(open('qualification/C3-ITER4/tools/modal_batches.py').read().split('rev = json.load')[0])
sys.argv = sys.argv_saved
inputs = json.load(open('standards/frames/FRAME_INPUTS.json'))
frames = {f['id']: f for f in inputs['frames']}
TASKS = ['rf-task-a', 'rf-task-b', 'ac-task-a', 'traversal-task-f', 'eb-task-d', 'dm-task-d', 'configuration', 'binding', 'stale-summary', 'bootstrap', 'acceptance-release', 'member-build-assess']
TT = {f'TT-{i+1:02d}': fid for i, fid in enumerate(TASKS)}
cache = {}
def whole(member_path, anchor):
    if member_path not in cache: cache[member_path] = sections_whole(member_path)
    return cache[member_path].get(anchor)
cmd = sys.argv[1]
if cmd == 'writers':
    os.makedirs('qualification/C3-ITER4/trial/writers', exist_ok=True)
    for tt, fid in TT.items():
        f = frames[fid]; out = [f"# Writer packet {tt} (frame `{fid}`, not included)\n\nTask sentence: {f['task']}\n\nScope: {f['scope']}\n\nOwning sections, verbatim with their subsections:\n"]
        for r in f['routes']:
            if r.get('rows'): continue
            t = whole(r['owner'], r['anchor']); out.append(f"\n\n## `{os.path.basename(r['owner'])}#{r['anchor']}`\n\n```markdown\n{(t or '(not found)').strip()}\n```\n")
        data = ''.join(out); open(f'qualification/C3-ITER4/trial/writers/{tt}.md', 'w').write(data); print(tt, fid, len(data), 'bytes')
elif cmd == 'actors':
    tt, arm, k = sys.argv[2], sys.argv[3], sys.argv[4]; fid = TT[tt]; f = frames[fid]
    exp = open(f'qualification/C3-ITER4/trial/expectations/{tt}.md').read()
    fixture = exp.split('## Fixture', 1)[1].split('## Expectations', 1)[0].strip() if '## Fixture' in exp else '(fixture section not found)'
    card = open('qualification/C3-ITER4/trial/CARD.md').read()
    parts = [card, f"\n\n# Task\n\n{f['task']}\n\n# Fixture\n\n{fixture}\n"]
    if arm in ('A1', 'A3'):
        fb = open(f['path'], encoding='utf-8').read(); parts.append(f"\n\n# Document 1: reference frame `{fid}` ({len(fb.encode())} bytes, sha256 {hashlib.sha256(fb.encode()).hexdigest()})\n\n{fb}")
    if arm == 'A3': parts.append("\n\n# File access\n\nYou may read files, read-only, under the directory the activation names; it is a copy of the method's `standards/` directory. Follow only the `Source:` lines and links of Document 1. List every file you open.\n")
    if arm == 'A5': parts.append("\n\n# File access\n\nYou may read files, read-only, under the directory the activation names; it is a copy of a method's `standards/` directory. Enter it only at its `README.md` and follow only the routes it declares. List every file you open, in order, with its size.\n")
    data = ''.join(parts); os.makedirs(f'qualification/C3-ITER4/trial/runs/{tt}', exist_ok=True); p = f'qualification/C3-ITER4/trial/runs/{tt}/{arm}-{k}.md'; open(p, 'w').write(data)
    print(p, len(data.encode()), 'bytes supplied')
elif cmd == 'copy':
    d = sys.argv[2]; shutil.rmtree(d, ignore_errors=True); shutil.copytree('standards', d)
    for root, _, files in os.walk(d):
        for fn in files: os.chmod(os.path.join(root, fn), 0o444)
    print('copied standards to', d)
