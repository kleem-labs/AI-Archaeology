"""Stage 1 — Vocabulary Probabilities — Turning Scores into a Prediction, with operations visible."""

from math import exp,log
def probabilities(logits):
 m=max(logits); e=[exp(x-m) for x in logits]; return [x/sum(e) for x in e]
def loss(logits,target): return -log(probabilities(logits)[target])
