"""The first excavation layer: every important operation remains visible."""

from math import exp, sqrt
from typing import Callable, Iterable, Sequence

Vector = list[float]
Matrix = list[Vector]


def require_same_size(left: Sequence[float], right: Sequence[float]) -> None:
    if len(left) != len(right):
        raise ValueError("vectors must describe the same ordered features")


def add(left: Sequence[float], right: Sequence[float]) -> Vector:
    """Excavation 004: independent changes accumulate coordinate by coordinate."""
    require_same_size(left, right)
    return [a + b for a, b in zip(left, right)]


def subtract(destination: Sequence[float], start: Sequence[float]) -> Vector:
    """Recover the change that carries start to destination."""
    require_same_size(destination, start)
    return [end - beginning for end, beginning in zip(destination, start)]


def dot(query: Sequence[float], key: Sequence[float]) -> float:
    """Excavation 010: aligned evidence contributes; disagreement subtracts."""
    require_same_size(query, key)
    return sum(wanted * offered for wanted, offered in zip(query, key))


def euclidean_distance(left: Sequence[float], right: Sequence[float]) -> float:
    """Excavation 003: prevent signed differences from cancelling."""
    require_same_size(left, right)
    squared_disagreements = [(a - b) ** 2 for a, b in zip(left, right)]
    return sqrt(sum(squared_disagreements))


def matrix_vector(matrix: Matrix, vector: Sequence[float]) -> Vector:
    """Excavation 005: each row states how every input shapes one output."""
    if not matrix:
        return []
    if any(len(row) != len(vector) for row in matrix):
        raise ValueError("each matrix row needs one coefficient per input feature")
    return [dot(row, vector) for row in matrix]


def stable_softmax(scores: Sequence[float]) -> Vector:
    """Excavation 009: positive, comparable weights that sum to one."""
    if not scores:
        raise ValueError("softmax needs at least one relevance score")
    peak = max(scores)
    positive_evidence = [exp(score - peak) for score in scores]
    total = sum(positive_evidence)
    return [evidence / total for evidence in positive_evidence]


def weighted_sum(weights: Sequence[float], values: Sequence[Sequence[float]]) -> Vector:
    if len(weights) != len(values) or not values:
        raise ValueError("each weight needs one value vector")
    width = len(values[0])
    if any(len(value) != width for value in values):
        raise ValueError("value vectors must share a width")
    return [
        sum(weight * value[feature] for weight, value in zip(weights, values))
        for feature in range(width)
    ]


def attend_one(
    query: Sequence[float], keys: Sequence[Sequence[float]], values: Sequence[Sequence[float]]
) -> tuple[Vector, Vector]:
    """Excavations 008–010: ask, score each label, then mix actual content."""
    if len(keys) != len(values):
        raise ValueError("each key must label one value")
    scores = [dot(query, key) for key in keys]
    weights = stable_softmax(scores)
    return weighted_sum(weights, values), weights


def relu(vector: Sequence[float]) -> Vector:
    return [max(0.0, value) for value in vector]


def feed_forward(
    vector: Sequence[float], expand: Matrix, contract: Matrix,
    activation: Callable[[Sequence[float]], Vector] = relu,
) -> Vector:
    """Excavation 012: expand candidate features, gate them, recombine."""
    candidates = matrix_vector(expand, vector)
    active_candidates = activation(candidates)
    return matrix_vector(contract, active_candidates)


def residual(vector: Sequence[float], proposed_change: Sequence[float]) -> Vector:
    """Excavation 013: preserve the state and add only a correction."""
    return add(vector, proposed_change)


def layer_norm(vector: Sequence[float], epsilon: float = 1e-5) -> Vector:
    """Excavation 014: preserve relative pattern at a predictable scale."""
    if not vector:
        raise ValueError("layer normalization needs a feature vector")
    mean = sum(vector) / len(vector)
    centered = [value - mean for value in vector]
    variance = sum(value * value for value in centered) / len(centered)
    scale = sqrt(variance + epsilon)
    return [value / scale for value in centered]


def gradient_descent(
    parameter: float, gradient: Callable[[float], float], learning_rate: float, steps: int
) -> list[float]:
    """Excavation 015: repeatedly move opposite the local uphill direction."""
    history = [parameter]
    for _ in range(steps):
        parameter -= learning_rate * gradient(parameter)
        history.append(parameter)
    return history


def _round(vector: Iterable[float]) -> Vector:
    return [round(value, 4) for value in vector]


def demonstrate() -> None:
    tiger_a = [220.0, 65.0, 6.0]
    tiger_b = [225.0, 66.0, 5.0]
    print("distance between comparable tiger features:", round(euclidean_distance(tiger_a, tiger_b), 4))

    query = [1.0, 2.0, 3.0]
    keys = [[2.0, 1.0, 4.0], [0.0, 2.0, 0.0], [-1.0, -1.0, -1.0]]
    values = [[10.0, 0.0], [0.0, 10.0], [-10.0, -10.0]]
    context, weights = attend_one(query, keys, values)
    print("attention weights:", _round(weights))
    print("retrieved context:", _round(context))

    path = gradient_descent(8.0, lambda x: 2 * (x - 3), learning_rate=0.2, steps=6)
    print("learning path toward 3:", _round(path))


if __name__ == "__main__":
    demonstrate()
