# Excavation 096 — Distributed Training

Quantization reduces the precision and footprint of those weights. Training the largest systems still exceeds the memory and computation of one machine, forcing the work and state to be divided.

Perhaps we let many machines train independent copies and combine them occasionally.

Yet their parameters drift and duplicated work wastes computation.

Now we can see what is missing: we must partition data or model work, synchronize required results, and preserve one coherent update.

## Let the case decide

Two workers compute gradients on different batches, average them, then apply the same update.

## The boundary of the discovery

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
