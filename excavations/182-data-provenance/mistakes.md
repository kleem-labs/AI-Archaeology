# Mistakes — Excavation 182

## Tempting idea

Save only the final cleaned text because intermediate metadata costs storage.

## Evidence that breaks it

A rights request, filtering bug, or benchmark contamination report arrives, but the final shard cannot be mapped back to the source record or processing rule that produced it.

## Requirement carried forward

Assign stable document identities and record a lineage edge for every fetch, normalization, filter, redaction, deduplication group, and output shard.

The wrong idea remains because its failure exposes information the successful design must preserve.
