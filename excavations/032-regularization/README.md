# Excavation 032 — Regularization — Making Memorization More Expensive

[Previous: Excavation 031](../031-overfitting/README.md)

The model can reduce training loss by building fragile rules around tiny accidental details.

Without knowing the inherited method, we might try this: Forbid complexity by making the model too small; it may lose real structure too. Stop training at an arbitrary time without observing unseen performance.

Remove that assumption and the needed repair becomes clear: Add a cost for large weights, remove random paths during training, or stop when validation performance stops improving.

## From procedure to notation

The repair solves the immediate failure, but regularization expresses a preference, not a universal truth. Too much causes underfitting and different tasks need different biases.



## Build each piece from what just happened

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Give Short Names Only After We Know the Pieces

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.


Every operation records a need established above; the equation is the fossil, not the living discovery.

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
