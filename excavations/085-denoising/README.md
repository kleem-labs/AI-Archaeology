# Excavation 085 — Denoising — Predicting What the Noise Hid

The forward diffusion process tells us exactly how clean image and noise combine at every step. Generation now depends on a network that can inspect the corrupted image and infer what the noise hid.

We first try to ask it to recreate the entire clean image directly from every noise level.

But the task changes dramatically across noise strengths.

That failure tells us to tell the model the noise level and predict the added noise or equivalent clean direction.

## Let the case decide

If known noise [0.2,-0.1] was added, learning to estimate it lets subtraction move toward the clean sample.

## The arithmetic we have earned

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

## The boundary of the discovery

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
