# Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

[Previous: Excavation 041](../041-logits/README.md)


## Take the First Step Yourself

> **Your problem:** The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

> **Try your first idea:** Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

The output head gives arbitrary positive and negative logits. We need comparable probabilities and a training loss.

## Your First Attempt

Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Divide each logit by their sum. Negative values break probability and shifting all scores changes the result.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.

## Why It Still Fails

A probability distribution expresses model confidence, not truth. Poor calibration and biased data remain possible.

## What You Have Just Invented

**Exponentiate relative scores, normalize them, then charge the negative log probability of the observed next token.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

For logits [1,2], softmax gives about [0.27,0.73]. If the observed token is the second, loss is -log(0.73), about 0.31. Assigning it 0.01 would cost about 4.61.

### Give Short Names Only After We Know the Pieces

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
