# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

Convolution slides one local detector across the whole image. The resulting activation maps preserve every detected location and quickly become too large for deeper processing.

Perhaps we keep every activation at full resolution through every layer.

That confidence lasts only until memory explodes and tiny shifts move evidence to neighboring cells.

So we summarize small neighborhoods while retaining the strongest or average evidence.

## Let the case decide

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

## The boundary of the discovery

Pooling discards exact location and can erase subtle patterns.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
