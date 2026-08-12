# Excavation 094 — Low-Rank Adaptation

Audio models extend the assistant's senses and enlarge the already expensive system. Adapting the whole model for each ranger station, language, or task would duplicate billions of parameters.

Using what we have, we copy and fine-tune all parameters for every task.

The world refuses to cooperate: storage and training cost multiply, and the base model is harder to preserve.

So we freeze the base and learn a small low-rank correction to selected matrices.

## Let the case decide

Instead of a million-value update, two narrow matrices produce a constrained correction with far fewer trainable values.

## The arithmetic we have earned

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

## The boundary of the discovery

Low rank may be insufficient for large behavioral changes.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 095](../095-quantization/README.md)
