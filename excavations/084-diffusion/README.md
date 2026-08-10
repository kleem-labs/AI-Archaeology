# Excavation 084 — Diffusion — Learning by Destroying

[Previous: Excavation 083](../083-autoregressive-generation/README.md)

How can generation begin without choosing a first meaningful pixel?

Our first construction is deliberately modest: Map one random vector directly to a finished image in one jump.

It works—right up to this boundary: One enormous jump is difficult to learn and unstable across diverse images.

Crossing that boundary requires one additional idea: Gradually add noise to real images, then learn the smaller reverse step at every noise level.

## Now work a case you can see

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon
$$

## Where your new idea still breaks

Many denoising steps make sampling expensive.

Why does the boundary remain? Our new machinery only knows how to gradually add noise to real images, then learn the smaller reverse step at every noise level. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 085](../085-denoising/README.md)
