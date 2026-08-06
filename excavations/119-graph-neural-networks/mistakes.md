# Mistakes — 119

## First idea

Assign a fixed input slot to every possible neighbor.

## Counterexample

Graphs vary in size and neighbor order should not change meaning.

## Repair

Apply the same message rule to each edge and aggregate neighbor messages without depending on order.
