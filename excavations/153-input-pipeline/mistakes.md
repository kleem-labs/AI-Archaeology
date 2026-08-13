# Mistakes — Excavation 153

## Tempting idea

Load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

## Evidence that breaks it

Data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

## Requirement carried forward

Prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
