"""Stage 1 — vector representation, with lists and loops visible."""

ORDER=("weight","speed","age")
def vector(x): return [x[k] for k in ORDER]
