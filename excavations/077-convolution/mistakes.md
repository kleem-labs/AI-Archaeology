# Mistakes — 077

## First idea

Learn a separate edge detector for every location.

## Counterexample

The model relearns the same pattern thousands of times and fails when it moves.

## Repair

Slide one small learned filter across all positions and reuse its weights.
