"""See why temperature is a confidence control rather than a magic symbol."""
from math import exp

def softmax(scores, temperature=1.0):
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    adjusted = [score / temperature for score in scores]
    peak = max(adjusted)
    evidence = [exp(score - peak) for score in adjusted]
    return [value / sum(evidence) for value in evidence]

def run(scores=(1.0, 2.0)):
    for temperature in (0.5, 1.0, 2.0):
        weights = softmax(scores, temperature)
        print(f"T={temperature}: {[round(x, 4) for x in weights]}")
    assert max(softmax(scores, .5)) > max(softmax(scores, 1.0))
    assert max(softmax(scores, 2.0)) < max(softmax(scores, 1.0))

if __name__ == "__main__":
    run()

