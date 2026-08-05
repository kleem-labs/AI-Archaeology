# Mistakes — 083

## First idea

Predict all pixels independently.

## Counterexample

Independent pixels produce noise because neighboring colors and shapes constrain one another.

## Repair

Choose an order and predict each piece from previously generated pieces.
