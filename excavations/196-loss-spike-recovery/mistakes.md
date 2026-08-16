# Mistakes — Excavation 196

## Tempting idea

Declare any loss larger than the previous loss a failure and restore immediately.

## Evidence that breaks it

Ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

## Requirement carried forward

Compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.

The wrong idea remains because its failure exposes information the successful design must preserve.
