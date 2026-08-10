# Excavation 096 — Distributed Training

[Previous: Excavation 095](../095-quantization/README.md)

One machine cannot hold the model, data, and optimizer state.

A reasonable place to begin is: Let many machines train independent copies and combine them occasionally.

Now place that proposal under pressure: Their parameters drift and duplicated work wastes computation.

What broke tells us what the replacement must preserve: Partition data or model work, synchronize required results, and preserve one coherent update.

## Now work a case you can see

Two workers compute gradients on different batches, average them, then apply the same update.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Communication, failure recovery, and numerical nondeterminism become bottlenecks.

The repair is explicit: partition data or model work, synchronize required results, and preserve one coherent update. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 097](../097-inference-serving/README.md)
