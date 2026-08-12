# Excavation 032 — Regularization — Making Memorization More Expensive

Overfitting reveals that low training error can be perfect memory wearing the costume of intelligence. The learner therefore needs pressure against fragile, unnecessarily extreme explanations.

One tempting answer is to forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

Now we can see what is missing: we must add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

## From procedure to notation

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.

## The arithmetic we have earned

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Only now do the symbols earn names

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.

### Why these operations are forced

- [Addition](../../MATHEMATICAL_MOVES.md#addition) puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.
- [The squared norm](../../MATHEMATICAL_MOVES.md#norm) combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.
- [λ scales the penalty](../../MATHEMATICAL_MOVES.md#multiplication) because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.

Only now can we compress that reasoning:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

## Carry the idea back into the world

A map that explains every pebble with a separate rule is less trustworthy than one road system that explains many journeys.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 033](../033-validation/README.md)
