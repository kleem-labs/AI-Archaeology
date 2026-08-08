# Excavation 078 — Pooling — Keeping Evidence While Shrinking the Map

[Previous: Excavation 077](../077-convolution/README.md)

Local detectors create large activation maps.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Keep every activation at full resolution through every layer.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Memory explodes and tiny shifts move evidence to neighboring cells.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Summarize small neighborhoods while retaining the strongest or average evidence.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Max pooling [1,7,2,3] keeps 7: an edge existed somewhere in that patch.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

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
