# Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

[Previous excavation](../017-probability/README.md)

## Problem

Two trackers propose different worlds. One says tigers usually leave deep round prints; another says deer do. We have observed one print and must compare the stories.

## Naive Attempt

Ask which story is generally more believable. That ignores the actual print. Or ask for the probability of the story directly, although the story is what we are trying to judge.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Reverse the question: if this story were true, how expected would the observed evidence be? That score is likelihood.**

## Mathematics Emerges

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A detective compares suspects by asking how well each suspect explains the clues, not how common the suspect is in the population.

## Limits

Likelihood compares explanations for fixed evidence; it is not itself a normalized probability over explanations. Priors will matter later.

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
