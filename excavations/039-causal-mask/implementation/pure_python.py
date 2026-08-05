"""Stage 1 — Causal Masking — Preventing the Future from Leaking Backward, with operations visible."""

def causal_mask(length): return [[0.0 if column<=row else float("-inf") for column in range(length)] for row in range(length)]
