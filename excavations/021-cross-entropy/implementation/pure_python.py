"""Stage 1: visible lists, loops, and scalar operations."""

from math import log
def cross_entropy(target,predicted): return -sum(p*log(q) for p,q in zip(target,predicted) if p)
