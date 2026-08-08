# Excavation 091 — Multimodal Alignment

[Previous: Excavation 090](../090-policy-gradients/README.md)

How can an image and its caption meet in one representation?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Compare raw pixels directly with token IDs.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Their coordinates have unrelated meanings and shapes.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Use separate encoders and train paired image-text examples to become nearby.

Only after that reasoning may we give your discovery its inherited name.

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
