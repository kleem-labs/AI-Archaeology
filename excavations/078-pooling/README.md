# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

[Previous: Excavation 077](../077-convolution/README.md)

Local detectors create large activation maps.

At first, the simplest answer is tempting: Keep every activation at full resolution through every layer.

But the simplicity has discarded something important: Memory explodes and tiny shifts move evidence to neighboring cells.

The missing information determines the next move: Summarize small neighborhoods while retaining the strongest or average evidence.

## Now work a case you can see

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Pooling discards exact location and can erase subtle patterns.

The reason is visible in the procedure. It knows how to summarize small neighborhoods while retaining the strongest or average evidence. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 079](../079-cnn-hierarchy/README.md)
