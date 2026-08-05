"""Stage 1: visible lists, loops, and scalar operations."""

from math import log2
def entropy(probabilities): return -sum(p*log2(p) for p in probabilities if p)
