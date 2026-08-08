# Excavation 096 — Distributed Training

[Previous: Excavation 095](../095-quantization/README.md)

One machine cannot hold the model, data, and optimizer state.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Let many machines train independent copies and combine them occasionally.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Their parameters drift and duplicated work wastes computation.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Partition data or model work, synchronize required results, and preserve one coherent update.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Two workers compute gradients on different batches, average them, then apply the same update.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 097](../097-inference-serving/README.md)
