# Excavation 083 — Autoregressive Generation Beyond Text

A meaningful latent space gives images coordinates we can navigate. To create a new image, the system still needs a procedure that turns an uncertain starting state into a complete arrangement of pixels.

An obvious shortcut is to predict all pixels independently.

That confidence lasts only until independent pixels produce noise because neighboring colors and shapes constrain one another.

We need to choose an order and predict each piece from previously generated pieces.

## Let the case decide

After generating sky pixels, the model gives blue neighbors higher probability.

## The boundary of the discovery

Sequential generation can be slow and ordering introduces bias.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 084](../084-diffusion/README.md)
