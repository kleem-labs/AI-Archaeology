"""Stage 1 — feature engineering, with lists and loops visible."""

ORDER=("weight","speed","age")
def encode(x): return [x[k] for k in ORDER]
