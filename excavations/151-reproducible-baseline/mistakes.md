# Mistakes — Excavation 151

## Tempting idea

Keep the final score and the model file; those should be enough to compare the next idea.

## Evidence that breaks it

A rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

## Requirement carried forward

Freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
