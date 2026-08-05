"""Stage 1 — Logits — Let Every Vocabulary Token Compete, with operations visible."""

def logits(hidden,weights,bias): return [sum(x*w for x,w in zip(hidden,column))+b for column,b in zip(zip(*weights),bias)]
