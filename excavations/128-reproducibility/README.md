# Excavation 128 — Reproducibility — Can the Discovery Survive Another Run?

Experimental design isolates one suspected cause and provides a control. A single successful run can still be a favorable random seed rather than a discovery that will survive repetition.

One tempting answer is to keep the best checkpoint and report its score.

That confidence lasts only until changing only the random seed makes the gain disappear.

Now we can see what is missing: we must record code, data, configuration, environment, seeds, and variation across repeated runs.

## Let the case decide

Run five seeds; compare the distribution of gains rather than celebrating the luckiest one.

## The boundary of the discovery

Repeated agreement does not remove a shared bias in all runs.

## Enter the laboratory

Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md).

## Carry the discovery forward

- [The wrong ideas worth preserving](mistakes.md)
- [Diagram and dependency path](diagram.md)
- [Invention exercises](exercises.md)
- [References and reading trail](references.md)
- [Visual asset brief](images/README.md)

[Next: Benchmarks — Building a Ruler Before Measuring Progress](../129-benchmarks/README.md)
