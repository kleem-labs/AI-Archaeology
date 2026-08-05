# Excavation 026 — Mini-Batches — Learning from More Than One Example

[Previous: Excavation 025](../025-gradient-descent/README.md)


## Take the First Step Yourself

> **Your problem:** A hunter updates the danger rule after every single footprint. One muddy print says “tiger”; the next says “deer.” The rule jerks back and forth.

> **Try your first idea:** Use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

A hunter updates the danger rule after every single footprint. One muddy print says “tiger”; the next says “deer.” The rule jerks back and forth.

## Your First Attempt

Use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Use one example per update. It is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

## Why It Still Fails

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

## What You Have Just Invented

**Average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Three examples propose gradients [2,4], [4,2], and [3,3]. Adding gives [9,9]; dividing by three gives [3,3]. Without division, merely enlarging the batch would triple the update.

### Give Short Names Only After We Know the Pieces

- **B** is the selected mini-batch and **|B|** its number of examples.
- **Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
- Summing combines the witnesses.
- Dividing by batch size prevents merely using more examples from making the step proportionally larger.
- **g_B** is the batch's less noisy gradient estimate.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$


## Real-World Analogy

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 027](../027-learning-rate/README.md)
