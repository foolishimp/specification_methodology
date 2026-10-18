"""Share of a candidate's paragraphs that occur verbatim in the predecessor's standards."""
import os, re, sys
def paras(text):
    out = []
    for block in re.split(r'\n\s*\n', text):
        b = ' '.join(block.split())
        if len(b) >= 80: out.append(b)
    return out
def corpus(d):
    ps = []
    for f in sorted(os.listdir(d)):
        if f.endswith('.md'): ps += paras(open(os.path.join(d, f), encoding='utf-8').read())
    return ps
pred = set(corpus(sys.argv[1]))
for label, d in zip(sys.argv[2::2], sys.argv[3::2]):
    ps = corpus(d)
    same = [p for p in ps if p in pred]
    b_all = sum(len(p) for p in ps); b_same = sum(len(p) for p in same)
    print('%-7s paragraphs %5d  verbatim-from-rc.2 %5d (%.0f%%)  bytes %8d  verbatim bytes %8d (%.0f%%)' % (label, len(ps), len(same), 100*len(same)/len(ps), b_all, b_same, 100*b_same/b_all))
