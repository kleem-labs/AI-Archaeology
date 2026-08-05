# Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

[Previous: Excavation 049](../049-calibration/README.md)

## Take the First Step Yourself

> **Your problem:** The architecture is correct, but the model repeats contradictions, private data, spam, and prejudice found in its training text.

> **Try your first idea:** Collect as much text as possible and assume scale washes out bad examples.

> **Now try to break your idea:** Duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

The architecture is correct, but the model repeats contradictions, private data, spam, and prejudice found in its training text.

## Your First Attempt

Collect as much text as possible and assume scale washes out bad examples.

## Break Your First Attempt

Duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

## What You Have Just Invented

**Treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.**

## Rebuild the Discovery with a Concrete Case

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Real-World Limit

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 051](../051-scaling-laws/README.md)
