# Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

[Previous: Excavation 049](../049-calibration/README.md)

The architecture is correct, but the model repeats contradictions, private data, spam, and prejudice found in its training text.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Collect as much text as possible and assume scale washes out bad examples.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* Duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 051](../051-scaling-laws/README.md)
