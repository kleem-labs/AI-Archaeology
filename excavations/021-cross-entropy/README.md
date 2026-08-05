# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

[Previous excavation](../020-entropy/README.md)


## Take the First Step Yourself

> **Your problem:** A model predicts tiger 90% and deer 10%, but a deer appears. We need a loss that distinguishes this dangerous confidence from a cautious 55–45 mistake.

> **Try your first idea:** Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

## Problem

A model predicts tiger 90% and deer 10%, but a deer appears. We need a loss that distinguishes this dangerous confidence from a cautious 55–45 mistake.

## Your First Attempt

Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

## Break Your First Attempt

Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

## Repair Your Attempt

Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## What You Have Just Invented

**Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.**

## Only Now Give the Discovery a Mathematical Name

## Build Every Piece from the Concrete Example

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

### Give Short Names Only After We Know the Pieces

- **P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
- **Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
- **−log qᵢ** makes confident neglect extremely costly.
- Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

Only now can we compress that reasoning:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

## Real-World Analogy

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

## Limits

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

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
