"""Scaled dot-product attention using only Python's standard library."""

from math import exp, sqrt


def dot(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return sum(a * b for a, b in zip(left, right))


def softmax(scores):
    largest = max(scores)
    exponentials = [exp(score - largest) for score in scores]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def weighted_sum(weights, vectors):
    return [sum(weight * vector[index]
                for weight, vector in zip(weights, vectors))
            for index in range(len(vectors[0]))]


def scaled_dot_product_attention(queries, keys, values, causal=False):
    """Return contextual outputs and the attention weight matrix."""
    if not queries or not keys or len(keys) != len(values):
        raise ValueError("queries, keys, and values must be non-empty and aligned")
    key_size = len(keys[0])
    if key_size == 0 or any(len(key) != key_size for key in keys):
        raise ValueError("keys must share a non-zero dimension")
    if any(len(query) != key_size for query in queries):
        raise ValueError("query and key dimensions must match")
    if any(len(value) != len(values[0]) for value in values):
        raise ValueError("values must share a dimension")

    all_weights = []
    outputs = []
    for query_index, query in enumerate(queries):
        scores = [dot(query, key) / sqrt(key_size) for key in keys]
        if causal:
            scores = [score if key_index <= query_index else float("-inf")
                      for key_index, score in enumerate(scores)]
        weights = softmax(scores)
        all_weights.append(weights)
        outputs.append(weighted_sum(weights, values))
    return outputs, all_weights


if __name__ == "__main__":
    tokens = ["the", "animal", "rested"]
    queries = [[1.0, 0.0], [0.2, 0.8], [0.9, 0.1]]
    keys = [[0.2, 0.1], [1.0, 0.0], [0.1, 0.9]]
    values = [[0.1, 0.1], [1.0, 0.2], [0.2, 1.0]]
    outputs, attention = scaled_dot_product_attention(queries, keys, values)
    for token, weights, output in zip(tokens, attention, outputs):
        print(f"{token:>6} weights:", [round(w, 3) for w in weights],
              "output:", [round(v, 3) for v in output])
