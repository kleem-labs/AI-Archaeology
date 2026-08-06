"""A transparent tokenize → score → sample → append loop."""
import random
from math import exp

VOCAB = ["tiger", "sleeps", "runs", "."]

def probabilities(logits):
    peak = max(logits)
    evidence = [exp(value - peak) for value in logits]
    return [value / sum(evidence) for value in evidence]

def sample(logits, rng):
    weights = probabilities(logits)
    return rng.choices(range(len(weights)), weights=weights, k=1)[0], weights

def generate(prompt, score_next, steps=3, seed=7):
    tokens = prompt.split()
    rng = random.Random(seed)
    trace = []
    for _ in range(steps):
        logits = score_next(tokens)
        token_id, weights = sample(logits, rng)
        token = VOCAB[token_id]
        trace.append({"context": tokens[:], "logits": logits, "weights": weights, "chosen": token})
        tokens.append(token)
    return tokens, trace

def run():
    def tiny_model(tokens):
        return [0.0, 2.0 if tokens[-1] == "tiger" else 0.0, 1.0, -1.0]
    tokens, trace = generate("tiger", tiny_model)
    for step in trace:
        print(step)
    assert len(tokens) == 4
    return tokens

if __name__ == "__main__":
    run()

