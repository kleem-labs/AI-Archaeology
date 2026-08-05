"""A numerically stable softmax with optional temperature."""

from math import exp


def softmax(scores, temperature=1.0):
    if not scores:
        raise ValueError("scores cannot be empty")
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    scaled = [score / temperature for score in scores]
    largest = max(scaled)
    exponentials = [exp(score - largest) for score in scaled]
    total = sum(exponentials)
    return [value / total for value in exponentials]


if __name__ == "__main__":
    scores = [2.0, 1.0, -1.0]
    for temperature in (0.5, 1.0, 2.0):
        weights = softmax(scores, temperature)
        print(f"T={temperature}:", [round(value, 4) for value in weights],
              "sum=", round(sum(weights), 10))
