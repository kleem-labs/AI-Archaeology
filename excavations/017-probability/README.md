# Excavation 017 — Probability — Counting What We Do Not Know

> **PART III — LEARNING FROM ERROR**
>
> The machine can move information. It still cannot admit uncertainty, measure a mistake, or use that mistake to change itself.


[Previous excavation](../016-emergence/README.md)

The tribe hears movement behind tall grass. It may be a tiger, deer, or wind. A yes-or-no answer pretends to know more than the observations allow.

Without knowing the inherited method, we might try this: Choose the most common cause and declare certainty. This works until the rare tiger arrives. Refusing to decide is safer intellectually but useless when the camp must act.

Remove that assumption and the needed repair becomes clear: Keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

### Give Short Names Only After We Know the Pieces

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

## Carry the idea back into the world

Probability is a weather forecast: not a promise, but an honest description of uncertainty that can still guide action.

## Limits

Probabilities depend on evidence and assumptions. When new evidence arrives, the shares must change.

This is not an unrelated warning. The construction can keep every plausible outcome and give each a share of belief. Count comparable past observations, then divide the count for one outcome by the total. It cannot infer or control information that never enters that construction.

## Enter the laboratory

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Test what you believe

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## What this discovery now makes possible

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
