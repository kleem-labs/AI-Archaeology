# Excavation 068 — Distribution Drift

[Previous: Excavation 067](../067-online-learning/README.md)

The world producing inputs changes after deployment.

At first, the simplest answer is tempting: Assume training accuracy remains valid forever.

But the simplicity has discarded something important: A winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

The missing information determines the next move: Monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

## Now work a case you can see

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Not every statistical shift changes the decision that matters.

The reason is visible in the procedure. It knows how to monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 069](../069-controlled-experiments/README.md)
