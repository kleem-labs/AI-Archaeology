# Mistakes — Excavation 160

## Tempting idea

Reduce arithmetic by approximating attention, because the n-squared score matrix appears to be the unavoidable cost.

## Evidence that breaks it

Approximation changes the model, while profiling shows much of the time is spent writing and rereading exact intermediate scores rather than multiplying them.

## Requirement carried forward

Tile queries, keys, and values into fast on-chip memory and maintain an online softmax so exact attention never needs the whole score matrix stored at once.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
