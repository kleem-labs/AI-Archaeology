# Excavation 085 — Denoising — Predicting What the Noise Hid

[Previous: Excavation 084](../084-diffusion/README.md)

## Take the First Step Yourself

> **Your problem:** At one diffusion step, what should the network predict?

> **Try your first idea:** Ask it to recreate the entire clean image directly from every noise level.

> **Now try to break your idea:** The task changes dramatically across noise strengths.

> Stop here. State the missing requirement without naming the repair.

## The Observation

At one diffusion step, what should the network predict?

## Your First Attempt

Ask it to recreate the entire clean image directly from every noise level.

## Break Your First Attempt

The task changes dramatically across noise strengths.

## Repair Your Attempt

Tell the model the noise level and predict the added noise or equivalent clean direction.

## What You Have Just Invented

**Tell the model the noise level and predict the added noise or equivalent clean direction.**

## Rebuild the Discovery with a Concrete Case

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

## Real-World Limit

Prediction parameterization and schedule affect stability and quality.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 086](../086-rewards/README.md)
