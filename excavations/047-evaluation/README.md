# Excavation 047 — Evaluation — What Does “Better” Actually Mean?

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

An obvious shortcut is to choose one benchmark score and call it intelligence.

The trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter.

We need to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away.

## Let the case decide

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

## The boundary of the discovery

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 048](../048-hallucination/README.md)
