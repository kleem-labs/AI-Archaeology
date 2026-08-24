"""Walk one observation through the mathematical roots beneath the machine."""

import math


def logsumexp(scores):
    maximum = max(scores)
    return maximum + math.log(sum(math.exp(score - maximum) for score in scores))


def run_lab():
    observed = {"tiger", "deer", "otter"}
    near_water = {"tiger", "otter", "frog"}
    overlap = observed & near_water
    assert overlap == {"tiger", "otter"}

    sightings = {("tiger", "river"), ("otter", "river")}
    assert ("tiger", "river") in sightings
    weights = {"tiger": 220, "deer": 90, "otter": 12}
    assert weights["tiger"] == 220

    track = (3, 2)
    east = (1, 0)
    scale = sum(a * b for a, b in zip(track, east)) / sum(a * b for a, b in zip(east, east))
    shadow = tuple(scale * value for value in east)
    assert shadow == (3, 0)

    prior = {"tiger": .1, "deer": .9}
    likelihood = {"tiger": .8, "deer": .1}
    evidence = sum(prior[story] * likelihood[story] for story in prior)
    posterior = {story: prior[story] * likelihood[story] / evidence for story in prior}
    assert math.isclose(posterior["tiger"], 8 / 17)

    bridge_actions = {"cross": 2 + .9 * 8, "wait": 1 + .9 * 6}
    chosen = max(bridge_actions, key=bridge_actions.get)
    assert chosen == "cross"

    stable_log_total = logsumexp([1000, 999, 998])
    assert math.isfinite(stable_log_total)

    return {
        "set overlap": overlap,
        "relation": sightings,
        "function output": weights["tiger"],
        "projected track": shadow,
        "posterior tiger belief": posterior["tiger"],
        "best bridge action": chosen,
        "stable log total": stable_log_total,
    }


if __name__ == "__main__":
    for name, value in run_lab().items():
        print(f"{name}: {value}")
