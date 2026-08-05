# Mistakes — 084

## First idea

Map one random vector directly to a finished image in one jump.

## Counterexample

One enormous jump is difficult to learn and unstable across diverse images.

## Repair

Gradually add noise to real images, then learn the smaller reverse step at every noise level.
