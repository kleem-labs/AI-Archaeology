# Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

[Previous excavation](../019-information/README.md)


## Take the First Step Yourself

> **Your problem:** One bag contains ten red stones. Another contains five red and five blue. Before drawing, which bag leaves us more uncertain?

> **Try your first idea:** Count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

One bag contains ten red stones. Another contains five red and five blue. Before drawing, which bag leaves us more uncertain?

## Your First Attempt

Count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Count the number of outcomes. Both bags contain stones, and both have two named colors if we list an absent possibility. Or inspect only the most likely outcome, losing the rest of the distribution.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Average the information of every possible outcome, weighted by how often that outcome occurs.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## What You Have Just Invented

**Average the information of every possible outcome, weighted by how often that outcome occurs.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

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
