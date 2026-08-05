# Mistakes — 067

## First idea

Retrain immediately on every new labeled event.

## Counterexample

One mislabeled transaction can move the model before anyone notices.

## Repair

Update from controlled batches with validation, rollback, and limits on how quickly behavior may change.
