# Mistakes — 089

## First idea

Replace its value with the immediate reward.

## Counterexample

The update ignores the valuable state reached afterward.

## Repair

Move the estimate toward reward plus the best discounted value available next.
