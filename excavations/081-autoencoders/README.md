# Excavation 081 — Autoencoders — Compressing and Rebuilding

Vision Transformers let distant patches attend to one another. Classification uses the representation once; reconstruction asks whether a smaller internal code can preserve enough of the image to rebuild it.

At first we copy the input through an unrestricted hidden layer.

Yet a wide hidden layer learns identity without compression.

That failure tells us to force information through a bottleneck and train reconstruction.

## Let the case decide

Four correlated measurements compress to two codes that still rebuild the originals approximately.

## The boundary of the discovery

Good reconstruction may preserve details irrelevant to downstream meaning.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 082](../082-latent-space/README.md)
