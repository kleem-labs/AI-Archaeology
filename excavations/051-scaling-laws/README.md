# Excavation 051 — Scaling Laws — What Improves When We Add More?

[Previous: Excavation 050](../050-data-quality/README.md)

Should limited resources buy a larger model, more data, or more training computation?

A reasonable place to begin is: Make the model as large as possible and assume capability follows parameter count.

Now place that proposal under pressure: A huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. What information did the attempt lose? Write that requirement before continuing.

What broke tells us what the replacement must preserve: Run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.

## Build each piece from what just happened

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Give Short Names Only After We Know the Pieces

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

Only now can we compress the exact procedure:

$$
L(N)=A N^{-\alpha}+B
$$

## Where your new idea still breaks

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
