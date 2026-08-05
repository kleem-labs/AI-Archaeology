# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

[Previous excavation](../020-entropy/README.md)

## Problem

A model predicts tiger 90% and deer 10%, but a deer appears. We need a loss that distinguishes this dangerous confidence from a cautious 55–45 mistake.

## Naive Attempt

Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

## Why It Fails

The attempt either throws away uncertainty, measures the wrong thing, or repeats work that the next step must preserve. We need a procedure whose parts answer the failure directly.

## Better Attempt

Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

## Why It Still Fails

The verbal procedure is now useful, but it is too long to repeat consistently and too vague to implement at scale. Every operation has earned a precise role; only now should notation compress it.

## Key Insight

**Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.**

## Mathematics Emerges

## Walk It Once with Concrete Values

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

## Why Every Term Must Exist Before the Equation

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
