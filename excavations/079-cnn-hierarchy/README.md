# Excavation 079 — CNN Hierarchies

Pooling keeps strong local evidence while shrinking the map. Edges and spots are still not eyes, stripes, or tigers; later detectors must compose simple evidence into larger structures.

We first try to classify directly from isolated edge responses.

The world refuses to cooperate: one edge has no object-level meaning.

We need to stack local detectors so later layers combine earlier patterns over wider regions.

## Let the case decide

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

## The boundary of the discovery

The hierarchy is learned, not guaranteed to match human parts.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 080](../080-vision-transformers/README.md)
