"""Stage 1 — abstraction and compression, with lists and loops visible."""

def shared(observations): return set.intersection(*(set(x) for x in observations))
