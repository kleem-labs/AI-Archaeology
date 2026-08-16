# Mistakes — Excavation 193

## Tempting idea

Increase whichever parallel technique was introduced most recently until the model fits.

## Evidence that breaks it

More pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

## Requirement carried forward

Compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

The wrong idea remains because its failure exposes information the successful design must preserve.
