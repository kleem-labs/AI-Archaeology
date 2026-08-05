"""Small vector operations using only Python's standard library."""


def add(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return [a + b for a, b in zip(left, right)]


def scale(number, vector):
    return [number * value for value in vector]


def min_max_normalize(rows):
    bounds = [(min(c), max(c)) for c in zip(*rows)]
    return [[0.0 if hi == lo else (v - lo) / (hi - lo)
             for v, (lo, hi) in zip(row, bounds)] for row in rows]


if __name__ == "__main__":
    animals = [[4, 180, 1, 7], [4, 350, 1, 2.5], [4, 90, 0, 1.5]]
    print("raw:", animals)
    print("normalized:")
    for vector in min_max_normalize(animals):
        print([round(value, 3) for value in vector])
