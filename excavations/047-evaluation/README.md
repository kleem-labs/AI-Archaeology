# Excavation 047 — Evaluation — What Does “Better” Actually Mean?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Perplexity measures how surprised a model is by held-out language. A lower surprise does not automatically mean a safer answer, a truer claim, or a more useful assistant.

Inside the Hall of Voices, the old method is given an honest chance. The public archivist places the evidence on the listening table and tries to choose one benchmark score and call it intelligence.

Nothing about this first move is careless. To choose one benchmark score and call it intelligence is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: the trouble appears immediately: a calculator can ace arithmetic while failing conversation; a fluent model can pass style tests while inventing facts. One number silently chooses which failures do not matter.

The important discovery is not merely that trying to choose one benchmark score and call it intelligence failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the listening table, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to name the intended job, create separate tests for its required abilities and risks, and inspect real failures rather than averaging them away. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Evaluation**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## What Does “Better” Actually Mean

For a travel assistant, test factual date retrieval, instruction following, refusal when information is missing, citation accuracy, latency, and cost separately. A single average must not let perfect tone hide fabricated flight times.

## Where evaluation runs out

Every evaluation is a model of future use. Benchmarks can leak into training and become targets rather than measurements.

Here the new path ends honestly. Evaluation can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the listening table

Rebuild the evaluation scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 048](../048-hallucination/README.md)
