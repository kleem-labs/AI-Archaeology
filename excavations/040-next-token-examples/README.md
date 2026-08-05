# Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

[Previous: Excavation 039](../039-causal-mask/README.md)


## Take the First Step Yourself

> **Your problem:** We have tokens, positions, and a causal boundary. The model still needs explicit questions and answers.

> **Try your first idea:** Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

We have tokens, positions, and a causal boundary. The model still needs explicit questions and answers.

## Your First Attempt

Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Shift the sequence by one position so every visible prefix predicts the token immediately following it.

## Why It Still Fails

Padding and document boundaries can create false targets unless their losses are masked.

## What You Have Just Invented

**Shift the sequence by one position so every visible prefix predicts the token immediately following it.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Give Short Names Only After We Know the Pieces

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1}),\qquad y=(t_1,\ldots,t_n)
$$


The equation arrives after every operation has a job.

## Real-World Analogy

A reading teacher pauses after every word, not only at the final period.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 041](../041-logits/README.md)
