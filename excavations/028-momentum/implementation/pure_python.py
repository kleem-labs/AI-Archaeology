"""Stage 1 — Momentum — Remembering Which Way Downhill Persists, with operations visible."""

def momentum(previous,gradient,beta=.9): return [beta*v+g for v,g in zip(previous,gradient)]
