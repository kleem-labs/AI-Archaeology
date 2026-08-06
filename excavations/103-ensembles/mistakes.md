# Mistakes — 103

## First idea

Trust one training run as the unique learned truth.

## Counterexample

Different initialization and data order produce different boundaries.

## Repair

Train several diverse models and combine predictions while inspecting disagreement.
