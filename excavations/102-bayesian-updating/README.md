# Excavation 102 — Bayesian Updating

Separating uncertainty in the observation from uncertainty in the model's knowledge tells us what kind of ignorance we face. New evidence must then revise several plausible stories without erasing what was believed before it arrived.

Perhaps we discard the old belief and use only the newest clue.

The trouble appears immediately: one noisy footprint can overpower years of evidence.

So we combine prior plausibility with how expected the clue is under each story, then normalize across stories.

## Let the case decide

Tiger starts at 10%, but a deep paw print is far more likely under tiger than wind; the belief rises without becoming certainty.

## The arithmetic we have earned

Before seeing tracks, a ranger considers tiger less common than deer: perhaps tiger receives prior share 1 and deer share 4. A deep round print is far more expected under tiger—say likelihood 8—than deer—say likelihood 1. Multiplying gives supports 8 for tiger and 4 for deer. Dividing each by total support 12 turns them into revised shares: two thirds tiger, one third deer. The print overcame the prior, but did not erase it.

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

## The boundary of the discovery

Results depend on priors and likelihood assumptions.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 103](../103-ensembles/README.md)
