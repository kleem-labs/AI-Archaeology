# Excavation 027 — Learning Rate — How Large Should the Next Step Be?

[Previous: Excavation 026](../026-mini-batches/README.md)

The gradient points downhill, but it does not say how far to walk. A correct direction can still produce a disastrous step.

Without knowing the inherited method, we might try this: Always take a huge step: leap across the valley and oscillate. Always take a microscopic step: improve so slowly that the expedition ends first.

Remove that assumption and the needed repair becomes clear: Multiply the gradient by a learning rate, observe whether loss descends, and adjust the rate over time.

## From procedure to notation

The repair solves the immediate failure, but no single learning rate is best throughout training. Scale, curvature, batch noise, and parameter units all matter.



## Build each piece from what just happened

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

### Give Short Names Only After We Know the Pieces

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

## Carry the idea back into the world

A mountain guide chooses shorter steps on steep or uncertain ground and can walk farther on a smooth open slope.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair.

## Test what you believe

Use the [invention challenges](exercises.md).

## What this discovery now makes possible

- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 028](../028-momentum/README.md)
