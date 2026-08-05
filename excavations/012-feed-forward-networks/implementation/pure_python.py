"""Stage 1 — feed-forward network, with lists and loops visible."""

def mv(m,v): return [sum(a*b for a,b in zip(r,v)) for r in m]
def discover(x,w1,w2): return mv(w2,[max(0,v) for v in mv(w1,x)])
