# Excavation 041 — Logits — Let Every Vocabulary Token Compete

[Previous: Excavation 040](../040-next-token-examples/README.md)

## Problem

The Transformer produces one contextual vector per position. A vector is not yet a prediction such as tiger, river, or runs.

## Naive Attempt

Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

## Why It Fails

The attempt either gives the model forbidden information, discards useful structure, or performs repeated work without solving the actual representation problem.

## Better Attempt

Use a learned linear map to produce one raw score for every vocabulary item.

## Why It Still Fails

Logits have no standalone probability meaning and can shift together without changing the final distribution.

## Key Insight

**Use a learned linear map to produce one raw score for every vocabulary item.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$


The equation arrives after every operation has a job.

## Real-World Analogy

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 042](../042-vocabulary-probabilities/README.md)
