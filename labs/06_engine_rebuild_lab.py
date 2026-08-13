"""Walk one measured path from a slow baseline to a verified serving engine."""
import math


def run_lab():
    baseline = {"step_ms": 100, "loss": 2.4, "kv_heads": 8, "bits": 32}

    # Profiling first: otherwise a faster matrix may leave the clock unchanged.
    profile = {"data": 35, "compute": 45, "communication": 10, "idle": 10}
    assert sum(profile.values()) == baseline["step_ms"]

    # Overlap data preparation with compute; the slower concurrent stage wins.
    overlapped_step = max(profile["data"], profile["compute"])
    assert overlapped_step == 45

    # Share two KV catalogs among eight query heads rather than storing eight.
    tokens, head_width = 100, 64
    old_cache = tokens * baseline["kv_heads"] * head_width * 2
    grouped_cache = tokens * 2 * head_width * 2
    assert grouped_cache == old_cache / 4

    # Reduced precision halves bulk payload, while the reference values remain.
    activations = 1_000_000
    old_bytes = activations * baseline["bits"] // 8
    mixed_bytes = activations * 16 // 8
    assert mixed_bytes == old_bytes / 2

    # A draft may propose, but acceptance is still determined by target support.
    target_probability, draft_probability = 0.4, 0.8
    acceptance = min(1.0, target_probability / draft_probability)
    assert math.isclose(acceptance, 0.5)

    return {
        "baseline_step_ms": baseline["step_ms"],
        "overlapped_step_ms": overlapped_step,
        "kv_cache_reduction": old_cache / grouped_cache,
        "activation_memory_reduction": old_bytes / mixed_bytes,
        "draft_acceptance": acceptance,
        "quality_authority": "frozen target model",
    }


if __name__ == "__main__":
    for name, value in run_lab().items():
        print(f"{name}: {value}")
