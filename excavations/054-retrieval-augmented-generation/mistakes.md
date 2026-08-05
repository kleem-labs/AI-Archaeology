# Mistakes — 054

## First idea

Retrain the whole model whenever one document changes.

## Counterexample

A price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

## Repair

Search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.
