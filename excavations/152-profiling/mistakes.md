# Mistakes — Excavation 152

## Tempting idea

Optimize the largest-looking matrix because attention is famous for being expensive.

## Evidence that breaks it

The device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.

## Requirement carried forward

Measure data loading, computation, communication, and idle time separately before choosing a repair.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
