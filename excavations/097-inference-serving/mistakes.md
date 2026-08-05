# Mistakes — 097

## First idea

Run one request at a time on one full model.

## Counterexample

Hardware sits idle between small operations and traffic spikes create queues.

## Repair

Batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.
