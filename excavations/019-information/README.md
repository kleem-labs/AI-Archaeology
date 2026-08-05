# Excavation 019 — Information — Why Surprise Needs a Number

[Previous excavation](../018-likelihood/README.md)

## Problem

A messenger can report either “the sun rose” or “a tiger entered camp.” Both are one sentence, but they do not teach us equally much.

## Naive Attempt

Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **P(x)** measures how expected observation x was.
- The logarithm is needed because independent probabilities multiply while information from independent messages should add.
- Probabilities below one have negative logs, so the minus sign makes information nonnegative.
- A certain event has P=1 and therefore zero information; rarer events receive more.

Only now can we compress that reasoning:

$$
I(x)=-\log P(x)
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

## Limits

Information depends on the probability model. A surprise to one observer may be expected to another.

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
