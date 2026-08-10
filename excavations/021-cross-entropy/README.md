# Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

[Previous excavation](../020-entropy/README.md)

A model predicts tiger 90% and deer 10%, but a deer appears. We need a loss that distinguishes this dangerous confidence from a cautious 55–45 mistake.

A reasonable place to begin is: Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

What broke tells us what the replacement must preserve: Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.

## From procedure to notation

The procedure now works in ordinary language. To repeat it consistently and implement it at scale, we give precise names to operations the concrete example has already earned.

## Build each piece from what just happened

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

## Carry the idea back into the world

A bad map that assigns almost no chance to the road you actually encounter deserves a much larger penalty than a map that admitted uncertainty.

## Limits

Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

The repair is explicit: charge the information cost assigned by the predicted distribution to the outcome that actually occurred. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md).

## Test what you believe

Use the [invention exercises](exercises.md), not as a quiz but as a request to rediscover the idea.

## What this discovery now makes possible

- [Mistakes and failed ideas](mistakes.md)
- [Mermaid and ASCII diagram](diagram.md)
- [References](references.md)
- [Visual asset brief](images/README.md)

The limitation in this excavation creates the need for the next one.
