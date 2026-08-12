# Excavation 068 — Distribution Drift

Online learning adapts quickly and can also absorb noise or attack just as quickly. The system must first distinguish ordinary variation from a genuine change in the source producing its inputs.

One tempting answer is to assume training accuracy remains valid forever.

That confidence lasts only until a winter-trained demand model meets summer behavior and keeps reporting confident old patterns.

Now we can see what is missing: we must monitor input, prediction, and outcome distributions; investigate meaningful shifts before retraining.

## Let the case decide

Average order size moves from $40 to $75 while error doubles. The shift is evidence to inspect, not automatic permission to update.

## The boundary of the discovery

Not every statistical shift changes the decision that matters.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 069](../069-controlled-experiments/README.md)
