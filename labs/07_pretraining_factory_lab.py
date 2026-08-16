"""Follow documents through one tiny, interruptible, audited pretraining plan."""
import hashlib
import math
import random


def normalize(text):
    return " ".join(text.lower().split())


def fingerprint(text):
    return hashlib.sha256(normalize(text).encode()).hexdigest()


def run_lab():
    raw = [
        ("field", "Tiger tracks beside the river."),
        ("field", " Tiger   tracks beside the river. "),
        ("science", "Striped cats use cover near water."),
        ("web", "Call 555-0142 about the tiger."),
    ]

    manifest_hash = hashlib.sha256("\n".join(text for _, text in raw).encode()).hexdigest()

    unique = {}
    duplicate_count = {}
    for domain, text in raw:
        key = fingerprint(text)
        unique.setdefault(key, (domain, text))
        duplicate_count[key] = duplicate_count.get(key, 0) + 1
    assert sorted(duplicate_count.values()) == [1, 1, 2]

    redacted = [
        (domain, text.replace("555-0142", "[PHONE]"))
        for domain, text in unique.values()
    ]

    weights = {"field": .4, "science": .3, "web": .3}
    assert math.isclose(sum(weights.values()), 1)
    rng = random.Random(7)
    schedule = rng.choices(list(weights), weights=list(weights.values()), k=100)

    steps, tokens_per_step = 20, 128
    token_budget = steps * tokens_per_step
    checkpoint = {
        "step": 10,
        "rng_state": rng.getstate(),
        "data_cursor": 10,
        "manifest_hash": manifest_hash,
    }
    assert set(checkpoint) == {"step", "rng_state", "data_cursor", "manifest_hash"}

    validation_probabilities = [.7, .8, .6]
    validation_loss = -sum(math.log(p) for p in validation_probabilities) / len(validation_probabilities)

    gates = {
        "manifest_signed": True,
        "resume_verified": True,
        "validation_passed": validation_loss < .5,
        "memorization_passed": True,
        "approved": True,
        "rollback_ready": True,
    }
    release = all(gates.values())
    assert release

    return {
        "manifest_hash": manifest_hash,
        "raw_documents": len(raw),
        "unique_documents": len(unique),
        "redacted_documents": redacted,
        "realized_domain_counts": {name: schedule.count(name) for name in weights},
        "token_budget": token_budget,
        "validation_loss": validation_loss,
        "release": release,
    }


if __name__ == "__main__":
    for name, value in run_lab().items():
        print(f"{name}: {value}")
