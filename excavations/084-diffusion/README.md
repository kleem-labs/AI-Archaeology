# Excavation 084 — Diffusion — Learning by Destroying

Autoregressive image generation chooses one piece after another, making an arbitrary generation order part of the model. Diffusion offers another route: destroy a complete image gradually so that generation can learn to reverse each small corruption.

Perhaps we map one random vector directly to a finished image in one jump.

The world refuses to cooperate: one enormous jump is difficult to learn and unstable across diverse images.

Now we can see what is missing: we must gradually add noise to real images, then learn the smaller reverse step at every noise level.

## Let the case decide

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

## The arithmetic we have earned

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

## The boundary of the discovery

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
