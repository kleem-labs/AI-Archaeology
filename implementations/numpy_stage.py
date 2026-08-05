"""The same discoveries expressed as arrays once the loops are understood."""

import numpy as np


def distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = left - right
    return float(np.sqrt(np.sum(difference * difference)))


def stable_softmax(scores: np.ndarray, axis: int = -1) -> np.ndarray:
    shifted = scores - np.max(scores, axis=axis, keepdims=True)
    evidence = np.exp(shifted)
    return evidence / np.sum(evidence, axis=axis, keepdims=True)


def scaled_dot_product_attention(
    queries: np.ndarray, keys: np.ndarray, values: np.ndarray,
    causal: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    """Attend every query to every key, optionally hiding future positions."""
    width = queries.shape[-1]
    scores = queries @ keys.swapaxes(-1, -2) / np.sqrt(width)
    if causal:
        future = np.triu(np.ones(scores.shape[-2:], dtype=bool), k=1)
        scores = np.where(future, -np.inf, scores)
    weights = stable_softmax(scores)
    return weights @ values, weights


def layer_norm(
    tokens: np.ndarray, gain: np.ndarray | float = 1.0,
    bias: np.ndarray | float = 0.0, epsilon: float = 1e-5,
) -> np.ndarray:
    mean = tokens.mean(axis=-1, keepdims=True)
    variance = ((tokens - mean) ** 2).mean(axis=-1, keepdims=True)
    return gain * (tokens - mean) / np.sqrt(variance + epsilon) + bias


def transformer_sublayer(tokens: np.ndarray, transformation) -> np.ndarray:
    """A pre-normalized residual step: preserve state, add a proposal."""
    return tokens + transformation(layer_norm(tokens))
