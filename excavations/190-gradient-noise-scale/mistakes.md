# Mistakes — Excavation 190

## Tempting idea

Make the global batch as large as the cluster permits.

## Evidence that breaks it

Early doubling reduces disagreement and improves the direction, but beyond a workload-dependent point the averaged gradient barely changes while each update consumes twice as many tokens.

## Requirement carried forward

Measure disagreement among micro-batch gradients relative to the strength of their shared direction, and use that noise scale as evidence for the largest useful batch rather than a hardware target.

The wrong idea remains because its failure exposes information the successful design must preserve.
