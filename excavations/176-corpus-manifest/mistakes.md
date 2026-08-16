# Mistakes — Excavation 176

## Tempting idea

Copy every available text file into one large folder and begin tokenizing.

## Evidence that breaks it

A file is replaced upstream, another is silently skipped, and a third appears twice under different paths. The same training command now describes a different body of evidence.

## Requirement carried forward

Create an immutable manifest that records each source, version, content hash, license or usage basis, processing stage, and document count before any training shard exists.

The wrong idea remains because its failure exposes information the successful design must preserve.
