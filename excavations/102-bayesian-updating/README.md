# Excavation 102 — Bayesian Updating

[Previous: Excavation 101](../101-two-kinds-uncertainty/README.md)

A tracker begins with prior beliefs about tiger, deer, and wind, then observes a deep paw print.

Without knowing the inherited method, we might try this: Discard the old belief and use only the newest clue.

Its hidden assumption appears in the following case: One noisy footprint can overpower years of evidence.

Remove that assumption and the needed repair becomes clear: Combine prior plausibility with how expected the clue is under each story, then normalize across stories.

## Now work a case you can see

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build each piece from what just happened

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

## Where your new idea still breaks

Results depend on priors and likelihood assumptions.

This is not an unrelated warning. The construction can combine prior plausibility with how expected the clue is under each story, then normalize across stories. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 103](../103-ensembles/README.md)
