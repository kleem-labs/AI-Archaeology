# Excavation 083 — Autoregressive Generation Beyond Text

[Previous: Excavation 082](../082-latent-space/README.md)

How can a model generate an image one piece at a time?

At first, the simplest answer is tempting: Predict all pixels independently.

But the simplicity has discarded something important: Independent pixels produce noise because neighboring colors and shapes constrain one another.

The missing information determines the next move: Choose an order and predict each piece from previously generated pieces.

## Now work a case you can see

After generating sky pixels, the model gives blue neighbors higher probability.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Sequential generation can be slow and ordering introduces bias.

The reason is visible in the procedure. It knows how to choose an order and predict each piece from previously generated pieces. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 084](../084-diffusion/README.md)
