"""Stage 1 — Initialization — Where Should Learning Begin?, with operations visible."""

import random
def initialize(inputs,outputs,seed=0):
 random.seed(seed); scale=inputs**-.5; return [[random.gauss(0,scale) for _ in range(inputs)] for _ in range(outputs)]
