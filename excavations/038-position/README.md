# Excavation 038 — Position — Why Order Must Enter the Model

[Previous: Excavation 037](../037-input-embeddings/README.md)

dog bites man and man bites dog retrieve the same token vectors. Attention compares content, but content alone does not say which occurrence came first.

At first, the simplest answer is tempting: Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

But the simplicity has discarded something important: Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

The missing information determines the next move: Add a position-specific vector to each token vector before attention. Content says what; position says where.

## Why It Still Fails

A fixed learned table cannot extend beyond trained positions, and absolute location is not always the relationship language needs.

## Compress your discovery into mathematics


## Build each piece from what just happened

Tiger at position 0 retrieves content [0.8,0.2] and position [0.1,-0.1], producing [0.9,0.1]. The same tiger at position 2 adds a different position vector, so content stays recognizable while order changes.

### Give Short Names Only After We Know the Pieces

- **token_i** is the vocabulary address appearing at sequence location i.
- **E[token_i]** retrieves what that token currently represents.
- **P_i** represents where the occurrence sits.
- Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
- **z_i** is the combined input at position i.

Only now can we compress that reasoning:

$$
z_i=E[token_i]+P_i
$$


The equation arrives after every operation has a job.

## Carry the idea back into the world

Seat numbers do not describe passengers, but they preserve who sat where.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 039](../039-causal-mask/README.md)
