# Mistakes — Excavation 157

## Tempting idea

At step t, recompute keys and values for positions 1 through t because the prefix is presented again.

## Evidence that breaks it

Past token representations are unchanged in causal decoding, so the same projections are calculated repeatedly while one new token is added.

## Requirement carried forward

Store each layer's past keys and values once, append only the new pair, and let the new query attend to the cache.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
