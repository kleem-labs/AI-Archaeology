# Mistakes — 049

## First idea

Treat the largest softmax probability as honest confidence.

## Counterexample

Collect ten answers each reported near 80%. If only four are correct, the number is not describing observed reliability.

## Repair

Group predictions with similar confidence and compare their average stated confidence with the fraction actually correct.
