# Excavation 072 — Linear Probes

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality)
>
> **Applied territory:** Learning in the world and interpretability

Internal-feature analysis asks what distinctions a hidden layer already makes. A simple probe may decode “tiger” from that layer, but decodability does not prove the original model uses that information.

At the Living Watchgarden, the field naturalist returns to the weathered observation slate. Yesterday's instrument still lies open, so the first move asks for no new magic: train a powerful classifier on hidden states and call any success evidence.

For a moment the mark looks complete. Then the evidence refuses to fit: the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The field naturalist sketches the break before changing it:*

```text
observation
    │
    ▼
[train a powerful classifier on hidden…]
    │
    ╳  the trouble appears immediately: the…
    │
    ▼
[use a deliberately limited probe and…]
```

The field naturalist lays two translucent sheets over the weathered observation slate. The first is inscribed, “train a powerful classifier on hidden states and call any success evidence.” Its path ends where the trouble appears immediately: the probe learns the task itself even if the representation did not make it simple. The second receives the same evidence but is allowed to use a deliberately limited probe and compare layers, controls, and baselines. Held to the light, the sheets separate at exactly one decision.

No one reaches for a linear probes formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The field naturalist changes only that one responsibility: use a deliberately limited probe and compare layers, controls, and baselines. When the ink dries, the name **Linear Probes** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The weathered observation slate keeps both histories. Its older mark still says, ‘train a powerful classifier on hidden states and call any success evidence’; beside it, the newer mark says, ‘use a deliberately limited probe and compare layers, controls, and baselines.’ The distance between those sentences is the exact shape of linear probes: no larger than the failure required, and no smaller than reality permits.

## Understanding linear probes

A linear probe succeeds at layer 8 but random-label controls fail, suggesting species became linearly accessible there.

## Where linear probes runs out

Decodable information is not proof the model uses it.

At the Living Watchgarden, the field naturalist leaves a blank beneath the new mark. Linear Probes has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the weathered observation slate

Rebuild the linear probes scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 073](../073-attribution/README.md)
