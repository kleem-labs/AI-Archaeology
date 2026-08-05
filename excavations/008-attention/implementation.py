"""Compute a weighted mixture: the final step of attention."""


def weighted_sum(weights, vectors):
    if len(weights) != len(vectors) or not vectors:
        raise ValueError("provide one weight per non-empty vector list")
    if abs(sum(weights) - 1.0) > 1e-9:
        raise ValueError("weights must sum to one")
    width = len(vectors[0])
    if any(len(vector) != width for vector in vectors):
        raise ValueError("all vectors must have the same dimensions")
    return [sum(weight * vector[i] for weight, vector in zip(weights, vectors))
            for i in range(width)]


if __name__ == "__main__":
    tokens = ["animal", "street", "tired"]
    values = [[1.0, 0.2], [0.1, 1.0], [0.8, 0.3]]
    weights = [0.65, 0.05, 0.30]
    print("attention:", dict(zip(tokens, weights)))
    print("contextual result:", weighted_sum(weights, values))
