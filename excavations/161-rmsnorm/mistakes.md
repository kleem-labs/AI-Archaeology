# Mistakes — Excavation 161

## Tempting idea

Delete normalization because each individual operation appears cheap.

## Evidence that breaks it

Deep residual streams drift in scale and training destabilizes; the repeated control was doing essential work.

## Requirement carried forward

Keep rescaling invariance by dividing by root-mean-square magnitude, while testing whether explicit recentering is dispensable.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
