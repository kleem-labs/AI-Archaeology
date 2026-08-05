"""Look up embeddings and compare them with cosine similarity."""

from math import sqrt


def dot(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return sum(a * b for a, b in zip(left, right))


def cosine(left, right):
    denominator = sqrt(dot(left, left) * dot(right, right))
    if denominator == 0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return dot(left, right) / denominator


def nearest(word, embeddings):
    return sorted(
        ((other, cosine(embeddings[word], vector))
         for other, vector in embeddings.items() if other != word),
        key=lambda item: item[1],
        reverse=True,
    )


if __name__ == "__main__":
    embeddings = {
        "cat": [0.9, 0.8, 0.1],
        "dog": [0.8, 0.9, 0.1],
        "car": [0.1, 0.0, 0.9],
        "truck": [0.1, 0.1, 0.8],
    }
    for word, score in nearest("cat", embeddings):
        print(f"cosine(cat, {word}) = {score:.3f}")
