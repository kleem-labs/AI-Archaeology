# Excavation 054 — Retrieval-Augmented Generation — Let the Model Look Before It Speaks

[Previous: Excavation 053](../053-preference-learning/README.md)

## Take the First Step Yourself

> **Your problem:** The model’s weights are stale and cannot reliably store every private or changing fact.

> **Try your first idea:** Retrain the whole model whenever one document changes.

> **Now try to break your idea:** A price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

The model’s weights are stale and cannot reliably store every private or changing fact.

## Your First Attempt

Retrain the whole model whenever one document changes.

## Break Your First Attempt

A price changes today, a policy changes tomorrow, and private documents cannot all be baked into public weights. Retraining is slow and still hides the source.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.

## What You Have Just Invented

**Search an external collection for evidence relevant to the question, place that evidence in context, and generate an answer grounded in what was retrieved.**

## Rebuild the Discovery with a Concrete Case

The user asks for today’s return policy. Retrieval selects the current policy document, not an old blog post. The answer quotes the 30-day rule and links it to that document.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Real-World Limit

Retrieval can miss the right document or return misleading text. Generation must distinguish evidence from instructions embedded inside evidence.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 055](../055-tool-using-agents/README.md)
