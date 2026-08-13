# Mistakes — Excavation 159

## Tempting idea

Return immediately to one KV head per query head.

## Evidence that breaks it

Quality recovers, but so does the full cache and bandwidth cost that forced sharing.

## Requirement carried forward

Partition query heads into groups; queries remain distinct while each group shares one key-value head.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
