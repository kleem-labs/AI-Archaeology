# Mistakes — Excavation 158

## Tempting idea

Preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.

## Evidence that breaks it

The caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.

## Requirement carried forward

Keep many query heads but share one key head and one value head across them.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
