# Excavation 038 — Position — Why Order Must Enter the Model

[Previous: Excavation 037](../037-input-embeddings/README.md)

dog bites man and man bites dog retrieve the same token vectors. Attention compares content, but content alone does not say which occurrence came first.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Do not reject your idea because the book says it is wrong. Test what you just proposed:

> Sort tokens by ID or trust their array slot without exposing it to the model. The first invents arbitrary order; the second stores position outside the computation.

Change the example until this rule gives an answer you know cannot be right. Name the exact information that disappeared or the false assumption the rule introduced. That missing requirement—not the name of a standard technique—is what you carry into the repair.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Add a position-specific vector to each token vector before attention. Content says what; position says where.

Only after that reasoning may we give your discovery its inherited name.

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
