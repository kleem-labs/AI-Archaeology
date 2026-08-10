# Excavation 067 — Online Learning

[Previous: Excavation 066](../066-feedback-loops/README.md)

A fraud pattern changes today, but the deployed model learned only from last year.

Without knowing the inherited method, we might try this: Retrain immediately on every new labeled event.

Its hidden assumption appears in the following case: One mislabeled transaction can move the model before anyone notices.

Remove that assumption and the needed repair becomes clear: Update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

## Now work a case you can see

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

Fast adaptation also creates fast corruption.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 068](../068-distribution-drift/README.md)
