# Excavation 032 — Regularization — Making Memorization More Expensive

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Learning from uncertainty and error

Overfitting reveals that low training error can be perfect memory wearing the costume of intelligence. The learner therefore needs pressure against fragile, unnecessarily extreme explanations.

At the Lantern Observatory, the keeper of uncertain stories returns to the ring of glass lanterns. Yesterday's instrument still lies open, so the first move asks for no new magic: forbid complexity by making the model too small; it may lose real structure too.

Reality answers without terminology: stop training at an arbitrary time without observing unseen performance. The ring of glass lanterns now holds two situations the old rule cannot keep apart.

*The keeper of uncertain stories sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: forbid complexity by making the model…
possible road B ─┘              └── loses: stop training at an arbitrary time…

same roads ──▶ repaired map ──▶ add a cost for large weights, remove…
```

The ring of glass lanterns is divided down the middle. Left side: “forbid complexity by making the model too small; it may lose real structure too.” Its final mark records stop training at an arbitrary time without observing unseen performance. Right side: the same starting evidence, now allowed to add a cost for large weights, remove random paths during training, or stop when validation performance stops improving. The difference is narrow enough to see and important enough to change the ending.

The broken rule has given regularization a gift: the missing job can now be spoken in ordinary language before symbols make it look inevitable.

The repair can now be stated without mystery: add a cost for large weights, remove random paths during training, or stop when validation performance stops improving. The name **Regularization** arrives afterward, like a title given to a path whose stones are already underfoot.

One boundary in the room is now sharper. On one side lies the promise to forbid complexity by making the model too small; it may lose real structure too; on the other lies the observed fact that stop training at an arbitrary time without observing unseen performance. The bridge called regularization has exactly the planks needed to add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

## The calculation hidden inside regularization

The keeper of uncertain stories carries the regularization scene to the ring of glass lanterns. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Naming what is already on the table

**L_data** rewards fitting observations.
**θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
**λ** expresses how strongly we prefer smaller machinery relative to data fit.
Addition forces training to negotiate prediction accuracy and complexity in one objective.

### Why the melody needs these exact notes

[Addition](../../MATHEMATICAL_MOVES.md#addition) puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.
[The squared norm](../../MATHEMATICAL_MOVES.md#norm) combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.
[λ scales the penalty](../../MATHEMATICAL_MOVES.md#multiplication) because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.

Listen beneath regularization: **the joining river**—separate contributions meet without losing where they came from; and **the lock and key**—one influence matters through another, and either missing factor can close the path. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Nothing remains unnamed in the regularization case on the ring of glass lanterns. We can finally trade the long route for its compact map:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

## Regularization beyond this one case

A map that explains every pebble with a separate rule is less trustworthy than one road system that explains many journeys.

## Return to the ring of glass lanterns

Rebuild the regularization scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 033](../033-validation/README.md)
