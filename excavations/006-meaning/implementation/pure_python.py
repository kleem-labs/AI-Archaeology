"""Stage 1 — distributional meaning, with lists and loops visible."""

from collections import Counter
def discover(sentences,target): return Counter(w for s in sentences if target in s for w in s if w!=target)
