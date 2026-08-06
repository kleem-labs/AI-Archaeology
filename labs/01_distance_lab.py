"""Break signed comparison, repair it, then expose feature-scale problems."""
from math import sqrt

TIGER_A = {"weight": 220.0, "speed": 65.0, "age": 6.0}
TIGER_B = {"weight": 225.0, "speed": 66.0, "age": 5.0}

def signed_sum(left, right, features):
    return sum(right[name] - left[name] for name in features)

def distance(left, right, features):
    parts = {name: right[name] - left[name] for name in features}
    squared = {name: value * value for name, value in parts.items()}
    return sqrt(sum(squared.values())), parts, squared

def run():
    features = ["weight", "speed", "age"]
    naive = signed_sum(TIGER_A, TIGER_B, features)
    repaired, differences, squared = distance(TIGER_A, TIGER_B, features)
    print("same-feature differences:", differences)
    print("naive signed sum:", naive)
    print("squared contributions:", squared)
    print("distance:", round(repaired, 4))
    assert signed_sum({"a": 0, "b": 0}, {"a": 100, "b": -100}, ["a", "b"]) == 0
    assert distance({"a": 0, "b": 0}, {"a": 100, "b": -100}, ["a", "b"])[0] > 0
    return repaired

if __name__ == "__main__":
    run()

