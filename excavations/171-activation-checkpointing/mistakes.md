# Mistakes — Excavation 171

## Tempting idea

Delete all activations after the forward pass.

## Evidence that breaks it

Backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

## Requirement carried forward

Keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
