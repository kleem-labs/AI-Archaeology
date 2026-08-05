# Mistakes — 039

## Naive idea

Train each prefix in a separate forward pass. It prevents cheating but repeats nearly identical work.

## Failure

A mask prevents direct attention leakage; shifted targets and data pipelines must also align correctly.

## Discovery

Process all positions together while blocking attention from position i to every later position j.
