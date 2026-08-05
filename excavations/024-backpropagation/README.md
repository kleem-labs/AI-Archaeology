# Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

[Previous excavation](../023-chain-rule/README.md)


## Take the First Step Yourself

> **Your problem:** A network has millions of weights and shared intermediate results. The chain rule gives a path, but following every path independently repeats the same downstream calculations.

> **Try your first idea:** Perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

A network has millions of weights and shared intermediate results. The chain rule gives a path, but following every path independently repeats the same downstream calculations.

## Your First Attempt

Perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Perturb each weight and rerun the model. This needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## What You Have Just Invented

**Compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Suppose x feeds two children. The first returns blame 3 through a local sensitivity 2, contributing 6. The second returns blame 4 through sensitivity 5, contributing 20. Total blame reaching x is 26, so both paths must be added.

### Give Short Names Only After We Know the Pieces

- **x̄** means accumulated sensitivity of final loss to intermediate x.
- A node can influence several child results y, so every downstream path must contribute.
- **ȳ** is blame already accumulated at child y.
- **∂y/∂x** says how strongly x affected that child locally.
- Multiplication passes blame through one edge; summation combines all outgoing paths.

Only now can we compress that reasoning:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

## Limits

Backpropagation computes gradients; it does not choose the update size or guarantee a good minimum.

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
