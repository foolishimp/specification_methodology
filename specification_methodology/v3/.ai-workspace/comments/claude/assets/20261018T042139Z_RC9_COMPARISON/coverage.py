"""Section-level interpretation coverage, computed from source files and artifacts."""
import json, re, sys, os, collections
def sections(path):
    """Return list of (level, title, start_line, end_line) for markdown headings ## and ###."""
    lines = open(path, encoding='utf-8').read().split('\n')
    heads = []
    infence = False
    for i, l in enumerate(lines, 1):
        if l.startswith('```'):
            infence = not infence
        if infence: continue
        m = re.match(r'^(#{1,4})\s+(.*)', l)
        if m: heads.append((len(m.group(1)), m.group(2).strip(), i))
    out = []
    for k, (lv, t, s) in enumerate(heads):
        e = len(lines)
        for lv2, t2, s2 in heads[k+1:]:
            if lv2 <= lv: e = s2 - 1; break
        out.append((lv, t, s, e))
    return out, len(lines)
mode = sys.argv[1]
if mode == 'codex':
    root = sys.argv[2]
    acc = json.load(open(os.path.join(root, 'interpretation/source-account.json')))
    spans = collections.defaultdict(list)
    for d in acc['determinations']:
        o = d['owner']
        if 'start_line' in o: spans[o['path']].append((o['start_line'], o['end_line']))
    members = sorted(f for f in os.listdir(os.path.join(root, 'standards')) if f.endswith('.md'))
    tot_lines = cov_lines = 0; rows = []
    for f in members:
        p = 'standards/' + f
        secs, n = sections(os.path.join(root, p))
        covered = set()
        for s, e in spans.get(p, []): covered.update(range(s, e+1))
        # leaf sections (no child heading inside) with any covered line
        leaf = [x for x in secs if not any(y[2] > x[2] and y[2] <= x[3] for y in secs)]
        lc = sum(1 for (_, _, s, e) in leaf if covered & set(range(s, e+1)))
        tot_lines += n; cov_lines += len(covered)
        rows.append((f, len(spans.get(p, [])), lc, len(leaf), len(covered), n))
    for r in rows: print('%-34s dets=%4d leaf_sections_touched=%4d/%-4d lines_in_spans=%6d/%-6d' % r)
    print('TOTAL dets=%d leaf_touched=%d/%d lines=%d/%d (%.0f%%)' % (sum(r[1] for r in rows), sum(r[2] for r in rows), sum(r[3] for r in rows), cov_lines, tot_lines, 100*cov_lines/tot_lines))
