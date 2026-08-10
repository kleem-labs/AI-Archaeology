# Excavation 085 — Denoising — Predicting What the Noise Hid

[Previous: Excavation 084](../084-diffusion/README.md)

At one diffusion step, what should the network predict?

The first solution that suggests itself is this: Ask it to recreate the entire clean image directly from every noise level.

The idea survives only until we test it against reality: The task changes dramatically across noise strengths.

The failure gives us a precise requirement: Tell the model the noise level and predict the added noise or equivalent clean direction.

## Now work a case you can see

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

## Where your new idea still breaks

Prediction parameterization and schedule affect stability and quality.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 086](../086-rewards/README.md)
