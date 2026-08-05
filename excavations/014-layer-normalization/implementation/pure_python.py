"""Stage 1 — layer normalization, with lists and loops visible."""

from math import sqrt
def discover(x,eps=1e-5):
 m=sum(x)/len(x); c=[v-m for v in x]; var=sum(v*v for v in c)/len(x); return [v/sqrt(var+eps) for v in c]
