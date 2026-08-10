# Excavation 019 — Information — Why Surprise Needs a Number

[Previous excavation](../018-likelihood/README.md)

A messenger can report either “the sun rose” or “a tiger entered camp.” Both are one sentence, but they do not teach us equally much.

Our first construction is deliberately modest: Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

The cost of that attempt points to the missing operation: Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

### Give Short Names Only After We Know the Pieces

- **P(x)** measures how expected observation x was.
- The logarithm is needed because independent probabilities multiply while information from independent messages should add.
- Probabilities below one have negative logs, so the minus sign makes information nonnegative.
- A certain event has P=1 and therefore zero information; rarer events receive more.

Only now can we compress that reasoning:

$$
I(x)=-\log P(x)
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Carry the idea back into the world

A locked door code is informative because many alternatives were possible. Learning that a two-sided coin landed on some side is less informative.

## Limits

Information depends on the probability model. A surprise to one observer may be expected to another.

Why does the boundary remain? Our new machinery only knows how to rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs. Solving that problem does not automatically solve every decision built on top of it.

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
