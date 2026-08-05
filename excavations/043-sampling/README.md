# Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

[Previous: Excavation 042](../042-vocabulary-probabilities/README.md)


## Take the First Step Yourself

> **Your problem:** The model predicts several plausible next tokens. Taking only the highest probability makes generation repetitive and brittle.

> **Try your first idea:** Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

The model predicts several plausible next tokens. Taking only the highest probability makes generation repetitive and brittle.

## Your First Attempt

Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Always use argmax. The same prompt follows the same narrow path. Sample raw probabilities blindly. Low-quality tail tokens eventually derail the text.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Control the distribution with temperature and optionally restrict it to a credible top set before sampling.

## Why It Still Fails

Sampling changes expression, not knowledge. No decoding rule can repair a model that assigned poor probabilities.

## What You Have Just Invented

**Control the distribution with temperature and optionally restrict it to a credible top set before sampling.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

For logits [1,2], T=1 keeps the original gap. T=0.5 turns them into [2,4], making the winner much sharper. T=2 turns them into [0.5,1], making alternatives more plausible.

### Give Short Names Only After We Know the Pieces

- **ℓ_i** is candidate i's raw logit.
- **T** is temperature: dividing by T changes score gaps before exponentiation.
- T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
- Exponentiation preserves ranking while making evidence positive.
- Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

Only now can we compress that reasoning:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$


The equation arrives after every operation has a job.

## Real-World Analogy

A musician follows likely notes but sometimes chooses another harmonious option; neither rigid repetition nor random keys make music.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 044](../044-context-window/README.md)
