# Excavation 082 — Latent Space — Coordinates for Hidden Causes

An autoencoder learns to compress and reconstruct. Its bottleneck is only a list of numbers until changes in those coordinates correspond to useful hidden causes such as pose, lighting, or identity.

Using what we have, we assume any compressed coordinates form a smooth useful space.

The trouble appears immediately: tiny code changes can cause abrupt unrelated outputs.

So we shape the latent distribution and train nearby codes to decode coherently.

## Let the case decide

Moving one latent coordinate gradually changes image brightness while another changes pose.

## The boundary of the discovery

Latent directions need not be independent or human-readable.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 083](../083-autoregressive-generation/README.md)
