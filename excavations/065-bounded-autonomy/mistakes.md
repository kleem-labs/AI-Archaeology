# Mistakes — 065

## First idea

Give the agent a broad goal and let it continue until it believes the goal is complete.

## Counterexample

A mistaken assumption triggers a long plan, repeated actions increase damage, and no one notices until after an irreversible step.

## Repair

Create an explicit operating envelope: allowed goal, tools, budgets, states, approval gates, verification requirements, stop conditions, and escalation path.
