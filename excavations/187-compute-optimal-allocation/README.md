# Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

An obvious shortcut is to spend nearly the entire budget on parameter count because a larger model can store more patterns.

Then the hidden cost becomes visible. The large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

Crossing that boundary requires one additional guarantee. Estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.

## Let one run decide

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

## The arithmetic we have earned

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

Only now can we compress the procedure:

$$
C\approx 6PD
$$

## What this repair cannot do

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Learning-Rate Warmup — Let Adam Learn the Terrain Before Running](../188-learning-rate-warmup/README.md)
