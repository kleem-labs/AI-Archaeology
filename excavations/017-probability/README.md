# Excavation 017 — Probability — Counting What We Do Not Know

[Previous excavation](../016-emergence/README.md)

## Problem

The tribe hears movement behind tall grass. It may be a tiger, deer, or wind. A yes-or-no answer pretends to know more than the observations allow.

## Naive Attempt

Choose the most common cause and declare certainty. This works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total.**

## Mathematics Emerges

## Why Every Term Must Exist Before the Equation

- **A** is the uncertain event we need to discuss.
- The numerator counts observations where A occurred.
- The denominator counts all comparable opportunities, because an isolated count has no scale.
- Division turns the count into a share between zero and one.
- **P(A)** names that evidence-dependent share, not a guarantee.

Only now can we compress that reasoning:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

Probability is a weather forecast: not a promise, but an honest description of uncertainty that can still guide action.

## Limits

Probabilities depend on evidence and assumptions. When new evidence arrives, the shares must change.

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
