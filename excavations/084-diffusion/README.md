# Excavation 084 — Diffusion — Learning by Destroying

[Previous: Excavation 083](../083-autoregressive-generation/README.md)

How can generation begin without choosing a first meaningful pixel?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Map one random vector directly to a finished image in one jump.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* One enormous jump is difficult to learn and unstable across diverse images.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Gradually add noise to real images, then learn the smaller reverse step at every noise level.

Only after that reasoning may we give your discovery its inherited name.

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

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 085](../085-denoising/README.md)
