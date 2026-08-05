"""Stage 1 — Euclidean distance, with lists and loops visible."""

from math import sqrt
def discover(a,b): return sqrt(sum((x-y)**2 for x,y in zip(a,b)))
