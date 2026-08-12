# Excavation 050 — Data Quality — What Lessons Did the Model Actually Receive?

Calibration compares stated confidence with observed reliability. When those diverge, the cause often lies upstream in the lessons the model received—duplication, errors, missing groups, or misleading correlations.

One tempting answer is to collect as much text as possible and assume scale washes out bad examples.

But duplicated false claims become louder, rare high-quality explanations become quieter, and sensitive records remain memorized. More observations amplify whatever process produced them.

So we treat data construction as part of the model: trace provenance, remove harmful duplication, filter carefully, preserve valuable diversity, and document choices.

## Let the case decide

A corpus contains one careful correction and 1,000 copied versions of the same false tiger fact. Counting pages makes the falsehood appear overwhelmingly supported; deduplication changes the lesson before training begins.

## The boundary of the discovery

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
