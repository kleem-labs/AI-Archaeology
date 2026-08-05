# Mistakes — 063

## First idea

Create many agents for every problem and let them freely edit shared state.

## Counterexample

They duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving.

## Repair

Delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result.
