# Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

[Previous excavation](../127-experimental-design/README.md)

One training run beats the baseline. Has the system discovered an improvement?

Before inheriting a technique, make the first decision yourself. Keep the best checkpoint and report its score.

For a moment, the idea appears sufficient. Then reality supplies the case it cannot explain: Changing only the random seed makes the gain disappear.

The failure tells you what the repair must accomplish. Record code, data, configuration, environment, seeds, and variation across repeated runs.

Only now have you earned the chapter's name: **Reproducibility**.

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
