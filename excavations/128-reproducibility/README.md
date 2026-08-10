# Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

[Previous excavation](../127-experimental-design/README.md)

One training run beats the baseline. Has the system discovered an improvement?

At first, the simplest answer is tempting: Keep the best checkpoint and report its score.

But the simplicity has discarded something important: Changing only the random seed makes the gain disappear.

The missing information determines the next move: Record code, data, configuration, environment, seeds, and variation across repeated runs.

Only here do we name the idea: **Reproducibility**.

## Follow one case all the way through

Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.

Write down what changed, what remained fixed, and which observation could have contradicted your belief. The method lives in those jobs; its name is only shorthand.

## Where the discovery still breaks

Repeated agreement does not remove a shared bias in all runs.

That limit is not a footnote. It is the pressure that forces the next excavation.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Benchmarks — Building a Ruler Before Measuring Progress](../129-benchmarks/README.md)
