# Mistakes — Excavation 174

## Tempting idea

Let a cheap draft model emit several tokens and return them directly.

## Evidence that breaks it

Speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

## Requirement carried forward

Let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
