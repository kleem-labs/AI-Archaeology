# Excavation 067 — Online Learning

[Previous: Excavation 066](../066-feedback-loops/README.md)

## Take the First Step Yourself

> **Your problem:** A fraud pattern changes today, but the deployed model learned only from last year.

> **Try your first idea:** Retrain immediately on every new labeled event.

> **Now try to break your idea:** One mislabeled transaction can move the model before anyone notices.

> Stop here. State the missing requirement without naming the repair.

## The Observation

A fraud pattern changes today, but the deployed model learned only from last year.

## Your First Attempt

Retrain immediately on every new labeled event.

## Break Your First Attempt

One mislabeled transaction can move the model before anyone notices.

## Repair Your Attempt

Update from controlled batches with validation, rollback, and limits on how quickly behavior may change.

## What You Have Just Invented

**Update from controlled batches with validation, rollback, and limits on how quickly behavior may change.**

## Rebuild the Discovery with a Concrete Case

A new batch reduces recent fraud loss but doubles errors on the stable validation set; the update is rejected.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Real-World Limit

Fast adaptation also creates fast corruption.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 068](../068-distribution-drift/README.md)
