"""Compare vectors using several definitions of distance."""

from math import sqrt


def _check(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")


def euclidean(left, right):
    _check(left, right)
    return sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def manhattan(left, right):
    _check(left, right)
    return sum(abs(a - b) for a, b in zip(left, right))


if __name__ == "__main__":
    query = [4, 200, 1, 6]
    animals = {"tiger": [4, 180, 1, 7], "zebra": [4, 350, 1, 2.5],
               "deer": [4, 90, 0, 1.5]}
    for name, vector in animals.items():
        print(f"{name:>5}: euclidean={euclidean(query, vector):.2f}, "
              f"manhattan={manhattan(query, vector):.2f}")
