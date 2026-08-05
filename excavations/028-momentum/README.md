# Excavation 028 — Momentum — Remembering Which Way Downhill Persists

[Previous: Excavation 027](../027-learning-rate/README.md)


## Take the First Step Yourself

> **Your problem:** Mini-batch gradients wobble. One batch points left-down, the next right-down, although both share a persistent downward direction.

> **Try your first idea:** Obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

Mini-batch gradients wobble. One batch points left-down, the next right-down, although both share a persistent downward direction.

## Your First Attempt

Obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Obey only the newest gradient. Sideways noise repeatedly cancels progress. Average every past gradient equally; ancient advice remains influential after the landscape changes.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Keep a fading memory of past gradients and combine it with the new one.

## Why It Still Fails

The repair solves the immediate failure, but momentum can overshoot, and its extra memory introduces another setting. It does not repair a fundamentally bad loss or dataset.

## What You Have Just Invented

**Keep a fading memory of past gradients and combine it with the new one.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Successive gradients are [3,1], [3,-1], [3,1]. The sideways coordinate flips, while the first persists. A fading sum reinforces the repeated 3 direction and partly cancels the wobble.

### Give Short Names Only After We Know the Pieces

- **g_t** is the newest noisy gradient.
- **v_{t−1}** stores direction accumulated previously.
- **β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
- Addition combines memory with new evidence into velocity v_t.
- **η** scales that velocity before it changes θ.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
v_t=\beta v_{t-1}+g_t,\qquad\theta_{t+1}=\theta_t-\eta v_t
$$


## Real-World Analogy

A heavy ball rattles less across a narrow ravine and keeps moving along the valley.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Exercises

Use the [invention challenges](exercises.md).

## Connections

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 029](../029-initialization/README.md)
