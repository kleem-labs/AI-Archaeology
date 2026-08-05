# Mistakes — 058

## First idea

Ask the agent to take the next action that sounds useful until the goal appears complete.

## Counterexample

It changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

## Repair

Represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.
