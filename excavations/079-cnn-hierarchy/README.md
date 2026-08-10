# Excavation 079 — CNN Hierarchies

[Previous: Excavation 078](../078-pooling/README.md)

Edges are not yet eyes, stripes, or tigers.

Our first construction is deliberately modest: Classify directly from isolated edge responses.

It works—right up to this boundary: One edge has no object-level meaning.

Crossing that boundary requires one additional idea: Stack local detectors so later layers combine earlier patterns over wider regions.

## Now work a case you can see

Edges form corners; corners and textures form stripes; repeated stripes plus shape support tiger.

The named objects and arithmetic come first. This chapter introduces no displayed equation unless notation clarifies something the reader has already calculated.

## Where your new idea still breaks

The hierarchy is learned, not guaranteed to match human parts.

Why does the boundary remain? Our new machinery only knows how to stack local detectors so later layers combine earlier patterns over wider regions. Solving that problem does not automatically solve every decision built on top of it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 080](../080-vision-transformers/README.md)
