# Excavation 084 — Diffusion — Learning by Destroying

[Previous: Excavation 083](../083-autoregressive-generation/README.md)

## Take the First Step Yourself

> **Your problem:** How can generation begin without choosing a first meaningful pixel?

> **Try your first idea:** Map one random vector directly to a finished image in one jump.

> **Now try to break your idea:** One enormous jump is difficult to learn and unstable across diverse images.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can generation begin without choosing a first meaningful pixel?

## Your First Attempt

Map one random vector directly to a finished image in one jump.

## Break Your First Attempt

One enormous jump is difficult to learn and unstable across diverse images.

## Repair Your Attempt

Gradually add noise to real images, then learn the smaller reverse step at every noise level.

## What You Have Just Invented

**Gradually add noise to real images, then learn the smaller reverse step at every noise level.**

## Rebuild the Discovery with a Concrete Case

A tiger image becomes slightly grainy, then more noisy, then nearly random; training learns each local cleanup.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build Every Piece from the Concrete Example

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon
$$

## Real-World Limit

Many denoising steps make sampling expensive.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 085](../085-denoising/README.md)
