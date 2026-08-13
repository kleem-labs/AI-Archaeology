# Mistakes — Excavation 164

## Tempting idea

Let both matrices learn independently because reading a token and predicting it are different jobs.

## Evidence that breaks it

The model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

## Requirement carried forward

Reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
