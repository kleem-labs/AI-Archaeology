# Excavation 096 — Distributed Training

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

At the Road of Consequences, the expedition leader returns to the map of branching journeys. Yesterday's instrument still lies open, so the first move asks for no new magic: let many machines train independent copies and combine them occasionally.

For a moment the mark looks complete. Then the evidence refuses to fit: their parameters drift and duplicated work wastes computation. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The expedition leader sketches the break before changing it:*

```text
OLD PATH:  request ──▶ let many machines train independent… ──▶ their parameters drift and duplicated…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ partition data or model work,… ──▶ accountable result
```

The expedition leader lays two translucent sheets over the map of branching journeys. The first is inscribed, “let many machines train independent copies and combine them occasionally.” Its path ends where their parameters drift and duplicated work wastes computation. The second receives the same evidence but is allowed to partition data or model work, synchronize required results, and preserve one coherent update. Held to the light, the sheets separate at exactly one decision.

No one reaches for a distributed training formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The expedition leader changes only that one responsibility: partition data or model work, synchronize required results, and preserve one coherent update. When the ink dries, the name **Distributed Training** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The map of branching journeys keeps both histories. Its older mark still says, ‘let many machines train independent copies and combine them occasionally’; beside it, the newer mark says, ‘partition data or model work, synchronize required results, and preserve one coherent update.’ The distance between those sentences is the exact shape of distributed training: no larger than the failure required, and no smaller than reality permits.

## Understanding distributed training

Two workers compute gradients on different batches, average them, then apply the same update.

## Where distributed training runs out

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

At the Road of Consequences, the expedition leader leaves a blank beneath the new mark. Distributed Training has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the map of branching journeys

Rebuild the distributed training scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 097](../097-inference-serving/README.md)
