# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

[Previous excavation](../019-information/README.md)

One bag contains ten red stones. Another contains five red and five blue. Before drawing, which bag leaves us more uncertain?

The first solution that suggests itself is this: Count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

The failure gives us a precise requirement: Average the information of every possible outcome, weighted by how often that outcome occurs.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Give Short Names Only After We Know the Pieces

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

## Carry the idea back into the world

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

## Limits

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

The boundary follows from the mechanism itself. We designed it to average the information of every possible outcome, weighted by how often that outcome occurs. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

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
