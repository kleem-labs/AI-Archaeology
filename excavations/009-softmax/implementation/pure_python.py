"""Stage 1 — softmax, with lists and loops visible."""

from math import exp
def discover(scores):
 m=max(scores); e=[exp(x-m) for x in scores]; return [x/sum(e) for x in e]
