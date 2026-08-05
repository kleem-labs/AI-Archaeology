# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

[Previous: Excavation 041](../041-logits/README.md)

## Problem

The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

## Naive Attempt

Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

## Why It Still Fails

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

## Key Insight

**Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **ℓ_i** is candidate i's raw score.
- Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
- **y** is the observed next-token index, so p_y is the probability assigned to what happened.
- The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

Only now can we compress that reasoning:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}},\qquad L=-\log p_y
$$


The equation arrives after every operation has a job.

## Real-World Analogy

A race score becomes odds only after every competitor is considered together.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 043](../043-sampling/README.md)
