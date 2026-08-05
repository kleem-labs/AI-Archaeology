"""Stage 1 — Learning Rate — How Large Should the Next Step Be?, with operations visible."""

def update(parameters,gradient,rate): return [p-rate*g for p,g in zip(parameters,gradient)]
