# Excavation 067 — Online Learning

[Previous: Excavation 066](../066-feedback-loops/README.md)

A fraud pattern changes today, but the deployed model learned only from last year.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Retrain immediately on every new labeled event.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* One mislabeled transaction can move the model before anyone notices.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

Only after that reasoning may we give your discovery its inherited name.

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
