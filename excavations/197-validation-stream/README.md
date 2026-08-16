# Excavation 197 — A Validation Stream — Ask Whether Learning Survives Outside the Current Batch

Loss-spike monitoring protects the training process from obvious instability. A smooth training curve can still improve mainly on repeated or overrepresented training domains.

At first we evaluate only the next training batch because it is already available.

Reality objects. The same data mixture and duplicates that shaped the update also judge it. Training loss can fall while held-out language or a rare domain becomes worse.

That evidence forces a repair. Maintain versioned, deduplicated, contamination-checked validation streams by domain and evaluate them at recorded token intervals without using them to update weights.

## Let one run decide

After every million training tokens, the station measures held-out field reports, science, books, code, and web text separately. A lower global average cannot hide that field-report loss rose.

## The arithmetic we have earned

The validation stream contains N honest next-token events. The model assigns the observed token x_i a conditional probability from its earlier context. Negative log turns confident neglect into positive cost, and L_val averages that cost across the stream.

### Why these operations are forced

[Logarithms](../../MATHEMATICAL_MOVES.md#logarithm) turn multiplied sequence probabilities into additive token costs. [Negative signs](../../MATHEMATICAL_MOVES.md#negative-sign) make lower assigned probability cost more. [Summation](../../MATHEMATICAL_MOVES.md#summation) lets every event contribute, and [division](../../MATHEMATICAL_MOVES.md#division) makes streams of different lengths comparable.

Only now can we compress the procedure:

$$
L_{\text{val}}=-\frac1N\sum_{i=1}^{N}\log p_\theta(x_i\mid x_{<i})
$$

## What this repair cannot do

Validation detects only the distributions and behaviors represented in its finite streams; repeatedly tuning against it can eventually overfit it.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: A Memorization Audit — Did the Model Learn a Pattern or Store a Passage?](../198-memorization-audit/README.md)
