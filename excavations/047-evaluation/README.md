# Excavation 047 — Evaluation — What Does “Better” Actually Mean?

[Previous: Excavation 046](../046-perplexity/README.md)

A model improves perplexity but gives worse medical answers and better poetry. Is it better?

Without knowing the inherited method, we might try this: Choose one benchmark score and call it intelligence.

Its hidden assumption appears in the following case: A calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter. What information did the attempt lose? Write that requirement before continuing.

Remove that assumption and the needed repair becomes clear: Name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away.

## Now work a case you can see

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

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
