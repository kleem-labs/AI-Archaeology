# Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

[Previous: Excavation 049](../049-calibration/README.md)

The architecture is correct, but the model repeats contradictions, private data, spam, and prejudice found in its training text.

The first solution that suggests itself is this: Collect as much text as possible and assume scale washes out bad examples.

The idea survives only until we test it against reality: Duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them. What information did the attempt lose? Write that requirement before continuing.

The failure gives us a precise requirement: Treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

## Now work a case you can see

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

Filtering encodes human judgments and can erase minority language or useful unusual examples. Quality is task-dependent.

The boundary follows from the mechanism itself. We designed it to treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 051](../051-scaling-laws/README.md)
