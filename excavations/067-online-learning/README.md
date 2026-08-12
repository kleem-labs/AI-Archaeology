# Excavation 067 — Online Learning

A feedback loop reveals that deployment is part of the data-generating process. When the world changes for legitimate reasons, a frozen model grows stale and needs a controlled way to learn online.

We first try to retrain immediately on every new labeled event.

The trouble appears immediately: one mislabeled transaction can move the model before anyone notices.

We need to update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

## Let the case decide

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

## The boundary of the discovery

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
