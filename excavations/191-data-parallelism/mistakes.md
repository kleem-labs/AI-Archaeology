# Mistakes — Excavation 191

## Tempting idea

Send the same mini-batch to every worker and average their gradients.

## Evidence that breaks it

All workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.

## Requirement carried forward

Replicate the current model view, give each worker a different slice of the global batch, average their gradients, and apply one logically shared update.

The wrong idea remains because its failure exposes information the successful design must preserve.
