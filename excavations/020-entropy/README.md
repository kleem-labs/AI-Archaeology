# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

Information gives one surprising observation a numerical weight. Before opening the next envelope, however, the community needs to compare the uncertainty of entire situations, not only the surprise of one event after it happens.

One tempting answer is to count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

Now we can see what is missing: we must average the information of every possible outcome, weighted by how often that outcome occurs.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## The arithmetic we have earned

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Only now do the symbols earn names

- **pᵢ** is the probability of possible outcome i.
- **−log pᵢ** is the information received if i occurs.
- Multiplying by pᵢ weights that surprise by how often it is expected to occur.
- Summing over every i computes average surprise before the outcome is known.
- **H(P)** names uncertainty of the whole distribution P.

Only now can we compress that reasoning:

$$
H(P)=-\sum_i p_i\log p_i
$$

## Carry the idea back into the world

Entropy is the expected surprise before opening a sealed envelope. A guaranteed message brings none; evenly balanced alternatives bring more.

## Limits

Entropy measures uncertainty in a stated distribution, not disorder in every everyday sense.

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
