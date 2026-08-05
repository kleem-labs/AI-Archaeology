"""Stage 1 — embedding, with lists and loops visible."""

def discover(sentences,words): return {w:[sum(w in s and c in s for s in sentences) for c in words] for w in words}
