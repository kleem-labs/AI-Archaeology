"""Stage 1 — linear transformation, with lists and loops visible."""

def discover(matrix,x): return [sum(a*b for a,b in zip(row,x)) for row in matrix]
