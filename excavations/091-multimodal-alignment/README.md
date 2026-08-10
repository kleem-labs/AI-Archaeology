# Excavation 091 — Multimodal Alignment

[Previous: Excavation 090](../090-policy-gradients/README.md)

How can an image and its caption meet in one representation?

A reasonable place to begin is: Compare raw pixels directly with token IDs.

Now place that proposal under pressure: Their coordinates have unrelated meanings and shapes.

What broke tells us what the replacement must preserve: Use separate encoders and train paired image-text examples to become nearby.

## Now work a case you can see

A tiger photo and “striped big cat” move together; mismatched captions move apart.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Pairs can contain weak, biased, or incomplete descriptions.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 092](../092-contrastive-learning/README.md)
