"""Separate who is relevant from what that source contributes."""
from math import exp

def dot(left, right):
    return sum(a * b for a, b in zip(left, right))

def attend(query, keys, values):
    scores = [dot(query, key) for key in keys]
    peak = max(scores)
    evidence = [exp(score - peak) for score in scores]
    weights = [item / sum(evidence) for item in evidence]
    output = [
        sum(weight * value[column] for weight, value in zip(weights, values))
        for column in range(len(values[0]))
    ]
    return {"scores": scores, "weights": weights, "output": output}

def run():
    query = [1.0, 2.0]
    keys = [[1.0, 2.0], [2.0, -1.0]]
    values = [[10.0, 0.0], [0.0, 20.0]]
    result = attend(query, keys, values)
    print(result)
    assert result["scores"][0] > result["scores"][1]
    assert result["output"] != keys[0]
    return result

if __name__ == "__main__":
    run()

