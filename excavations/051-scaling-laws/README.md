# Excavation 051 — Scaling Laws — What Improves When We Add More?

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

At first we make the model as large as possible and assume capability follows parameter count.

Yet a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

We need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.

## The arithmetic we have earned

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Only now do the symbols earn names

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

### Why these operations are forced

- [The negative power](../../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
- [A scales that falling term](../../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
- [Adding B](../../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

Only now can we compress the exact procedure:

$$
L(N)=A N^{-\alpha}+B
$$

## The boundary of the discovery

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 052](../052-instruction-tuning/README.md)
