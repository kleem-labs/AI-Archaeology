# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

[Previous excavation](../019-information/README.md)

## Problem

One bag contains ten red stones. Another contains five red and five blue. Before drawing, which bag leaves us more uncertain?

## Naive Attempt

Count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Average the information of every possible outcome, weighted by how often that outcome occurs.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Average the information of every possible outcome, weighted by how often that outcome occurs.**

## Mathematics Emerges

## Walk It Once with Concrete Values

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

## Why Every Term Must Exist Before the Equation

- **pᵢ** is the probability of possible outcome i.
- **−log pᵢ** is the information received if i occurs.
- Multiplying by pᵢ weights that surprise by how often it is expected to occur.
- Summing over every i computes average surprise before the outcome is known.
- **H(P)** names uncertainty of the whole distribution P.

Only now can we compress that reasoning:

$$
H(P)=-\sum_i p_i\log p_i
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

## Limits

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

## Implementation

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## Connections

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
