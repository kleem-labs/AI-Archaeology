# Mistakes — Excavation 194

## Tempting idea

Let every worker write its local tensors and call the directory a checkpoint.

## Evidence that breaks it

A worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.

## Requirement carried forward

Write versioned shards to temporary locations, record hashes and ownership in a checkpoint manifest, and publish one atomic completion marker only after every required shard is durable.

The wrong idea remains because its failure exposes information the successful design must preserve.
