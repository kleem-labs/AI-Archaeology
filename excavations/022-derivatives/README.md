# Excavation 022 — Derivatives — Asking One Weight What It Changed

[Previous excavation](../021-cross-entropy/README.md)


## Take the First Step Yourself

> **Your problem:** The loss is high. The model has thousands of adjustable numbers. For one weight, should we increase it or decrease it?

> **Try your first idea:** Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

The loss is high. The model has thousands of adjustable numbers. For one weight, should we increase it or decrease it?

## Your First Attempt

Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## What You Have Just Invented

**Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Use L(w)=w² at w=3. Nudge to 3.001: loss changes from 9 to about 9.006001. Dividing the loss change by 0.001 gives about 6; smaller nudges approach the local sensitivity 6.

### Give Short Names Only After We Know the Pieces

- **w** is the one weight whose responsibility we are probing.
- **ε** is a small experimental nudge.
- **L(w+ε)−L(w)** measures the loss change caused by that nudge.
- Dividing by ε turns total change into change per unit of weight.
- The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
- **dL/dw** names that local sensitivity.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A derivative is a local slope on a mountain trail: it says which direction rises and how sharply, only near the current step.

## Limits

A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

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
