# Mistakes — Excavation 170

## Tempting idea

Reduce the batch until it fits and change nothing else.

## Evidence that breaks it

The gradient becomes noisier and the training regime changes; increasing the learning rate cannot recreate evidence never averaged together.

## Requirement carried forward

Run several micro-batches, sum their unscaled gradients without updating, then divide once and take one optimizer step.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
