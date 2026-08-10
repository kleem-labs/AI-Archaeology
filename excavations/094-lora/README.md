# Excavation 094 — Low-Rank Adaptation

[Previous: Excavation 093](../093-speech-audio/README.md)

How can a huge pretrained model learn a new task without changing every weight?

Our first construction is deliberately modest: Copy and fine-tune all parameters for every task.

It works—right up to this boundary: Storage and training cost multiply, and the base model is harder to preserve.

Crossing that boundary requires one additional idea: Freeze the base and learn a small low-rank correction to selected matrices.

## Now work a case you can see

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Build each piece from what just happened

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

## Where your new idea still breaks

Low rank may be insufficient for large behavioral changes.

Why does the boundary remain? Our new machinery only knows how to freeze the base and learn a small low-rank correction to selected matrices. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 095](../095-quantization/README.md)
