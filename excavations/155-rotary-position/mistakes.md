# Mistakes — Excavation 155

## Tempting idea

Learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

## Evidence that breaks it

Moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

## Requirement carried forward

Rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
