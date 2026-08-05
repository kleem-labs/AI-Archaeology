"""Stage 1 — Position — Why Order Must Enter the Model, with operations visible."""

def add_position(tokens,positions): return [[a+b for a,b in zip(token,pos)] for token,pos in zip(tokens,positions)]
