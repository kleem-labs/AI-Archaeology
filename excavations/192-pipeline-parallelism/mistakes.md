# Mistakes — Excavation 192

## Tempting idea

Send one complete batch through stage one, then stage two, then stage three.

## Evidence that breaks it

While stage two works, stage one and stage three wait. The model fits, but most devices are idle for most of the step.

## Requirement carried forward

Split the batch into micro-batches and stagger them through the layer stages so different stages work on different micro-batches concurrently.

The wrong idea remains because its failure exposes information the successful design must preserve.
