# Excavation 190 — Gradient Noise Scale — When More Examples Stop Buying More Direction

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Data and pretraining operations

The schedule controls how far one global update moves. We still do not know how many examples should vote in that update before extra devices mostly repeat the same directional evidence.

The doors of the Archive Foundry close against the wind. On the chain-of-custody ledger, the archivist-engineer writes the cheapest rule that might still be true: make the global batch as large as the cluster permits.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: make the global batch as large as the…
possible road B ─┘              └── loses: early doubling reduces disagreement…

same roads ──▶ repaired map ──▶ measure disagreement among…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “make the global batch as large as the cluster permits”; the other knows how to measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. When the failure—early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to gradient noise scale. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target. This problem and its repair will travel under the name **Gradient Noise Scale**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—make the global batch as large as the cluster permits? The answer remains early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

## When More Examples Stop Buying More Direction

Three named micro-batches question the same two weights: the field reports propose [2.0,1.0], science proposes [2.1,0.9], and books propose [1.9,1.1]. The first number is advice to the tiger-before-river weight; the second is advice to a punctuation weight. Their mean [2.0,1.0] is strong and their disagreement around it is small. If the witnesses instead propose [4,−2], [0,4], and [2,1], disagreement is large relative to the same broad direction, so a larger batch can still buy useful certainty.

## The calculation hidden inside gradient noise scale

The archivist-engineer carries the gradient noise scale scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Each g_i is one model micro-batch's gradient advice. The covariance measures how those witnesses disagree; its trace totals disagreement across coordinates. The squared norm of their mean measures the strength of the shared direction; G compares noise with signal.

### Why the melody needs these exact notes

[Covariance](../../MATHEMATICAL_MOVES.md#covariance) keeps variation around the common advice rather than raw gradient size. [Trace](../../MATHEMATICAL_MOVES.md#trace) gathers coordinate variances without inventing cross-coordinate units. [Division](../../MATHEMATICAL_MOVES.md#division) asks disagreement per unit of squared shared direction; subtraction would not remove dependence on signal scale.

The mandala has curved back upon itself. In this chamber we meet **the paired dance**—two quantities reveal whether their departures move together; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. What seemed like a new formula is older mathematical instinct arranged around a new need.

Cover the prose about gradient noise scale and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
G=\frac{\mathrm{tr}(\mathrm{Cov}[g_i])}{\lVert E[g_i]\rVert^2}
$$

## Where gradient noise scale runs out

Gradient noise scale is an empirical guide, not a universal batch-size law; it changes during training and with the task and optimizer.

The gradient noise scale repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the chain-of-custody ledger

Rebuild the gradient noise scale scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Data Parallelism — Let Several Workers Observe Different Evidence](../191-data-parallelism/README.md)
