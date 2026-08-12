# Excavation 080 — Vision Transformers

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

One tempting answer is to treat every pixel as a token.

But the sequence becomes enormous and individual pixels carry little stable structure.

Now we can see what is missing: we must group pixels into patches, embed them as tokens, add position, and apply attention.

## Let the case decide

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

## The boundary of the discovery

Patch size trades detail for cost and needs substantial data.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 081](../081-autoencoders/README.md)
