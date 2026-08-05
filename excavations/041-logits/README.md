# Excavation 041 — Logits — Let Every Vocabulary Token Compete

[Previous: Excavation 040](../040-next-token-examples/README.md)


## Take the First Step Yourself

> **Your problem:** The Transformer produces one contextual vector per position. A vector is not yet a prediction such as tiger, river, or runs.

> **Try your first idea:** Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

The Transformer produces one contextual vector per position. A vector is not yet a prediction such as tiger, river, or runs.

## Your First Attempt

Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Choose the nearest input embedding directly. That restricts the scoring rule and hides how every vocabulary candidate should compete.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Use a learned linear map to produce one raw score for every vocabulary item.

## Why It Still Fails

Logits have no standalone probability meaning and can shift together without changing the final distribution.

## What You Have Just Invented

**Use a learned linear map to produce one raw score for every vocabulary item.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Let hidden state be [2,1]. One candidate column [3,0] scores 6; another [0,4] scores 4. Adding each candidate bias adjusts its baseline. These raw comparisons are logits.

### Give Short Names Only After We Know the Pieces

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$


The equation arrives after every operation has a job.

## Real-World Analogy

Judges first assign unconstrained scores to every contestant before those scores are converted into shares.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 042](../042-vocabulary-probabilities/README.md)
