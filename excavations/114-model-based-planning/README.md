# Excavation 114 — Model-Based Planning

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Continual learning, reasoning, and research

Counterfactual reasoning compares unrealized alternatives for one case. Planning extends that question across a sequence, where each imagined action changes which choices and states can follow.

The table of mirrored maps at the Hall of Possible Worlds still carries the marks of the previous discovery. The keeper of unfinished questions follows them as far as they seem willing to go: commit to the first sequence imagined.

For a moment the mark looks complete. Then the evidence refuses to fit: one forecast may exploit model error or miss better branches. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The keeper of unfinished questions sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ commit to the first sequence imagined ──▶ blurred: one forecast may exploit model error…
      │
      └── new lens ──▶ simulate multiple candidate… ──▶ distinction survives
```

The keeper of unfinished questions lays two translucent sheets over the table of mirrored maps. The first is inscribed, “commit to the first sequence imagined.” Its path ends where one forecast may exploit model error or miss better branches. The second receives the same evidence but is allowed to simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. Held to the light, the sheets separate at exactly one decision.

No one reaches for a model-based planning formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The keeper of unfinished questions changes only that one responsibility: simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. When the ink dries, the name **Model-Based Planning** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The repaired line crosses the old one at a single point. Before that crossing, both methods see the same evidence. After it, one still suffers because one forecast may exploit model error or miss better branches, while the other can simulate multiple candidate sequences, score outcomes, act briefly, observe reality, and plan again. That fork—not the vocabulary—is where model-based planning lives.

## Understanding model-based planning

A robot simulates left-right paths, takes one safe step, then updates after detecting an obstacle.

## Where model-based planning runs out

Planning cost grows with horizon and branching.

At the Hall of Possible Worlds, the keeper of unfinished questions leaves a blank beneath the new mark. Model-Based Planning has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the table of mirrored maps

Rebuild the model-based planning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 115](../115-tree-search/README.md)
