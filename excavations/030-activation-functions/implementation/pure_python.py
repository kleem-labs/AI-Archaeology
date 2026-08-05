"""Stage 1 — Activation Functions — Why a Network Must Bend, with operations visible."""

def relu(values): return [max(0.0,x) for x in values]
def sigmoid(x):
 from math import exp
 return 1/(1+exp(-x))
