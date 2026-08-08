# Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

[Previous: Excavation 053](../053-preference-learning/README.md)

The model’s weights are stale and cannot reliably store every private or changing fact.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Retrain the whole model whenever one document changes.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* A price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

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
