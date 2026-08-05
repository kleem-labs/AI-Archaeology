"""Stage 1 — scaled dot-product attention, with lists and loops visible."""

from math import exp
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def discover(q,keys,values):
 s=[dot(q,k) for k in keys]; m=max(s); e=[exp(x-m) for x in s]; w=[x/sum(e) for x in e]; return [sum(a*v[i] for a,v in zip(w,values)) for i in range(len(values[0]))]
