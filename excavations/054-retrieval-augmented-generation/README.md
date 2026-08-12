# Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

Preference learning lets reviewers distinguish answers that are all technically possible. Even the preferred answer may rely on stale memory when the question asks about a document or fact that changed after training.

Perhaps we retrain the whole model whenever one document changes.

The world refuses to cooperate: a price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

So we search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

## Let the case decide

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

## The boundary of the discovery

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 055](../055-tool-using-agents/README.md)
