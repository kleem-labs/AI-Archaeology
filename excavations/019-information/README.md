# Excavation 019 — Information — Why Surprise Needs a Number

[Previous excavation](../018-likelihood/README.md)


## Take the First Step Yourself

> **Your problem:** A messenger can report either “the sun rose” or “a tiger entered camp.” Both are one sentence, but they do not teach us equally much.

> **Try your first idea:** Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

A messenger can report either “the sun rose” or “a tiger entered camp.” Both are one sentence, but they do not teach us equally much.

## Your First Attempt

Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## What You Have Just Invented

**Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

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
