# Contributing

AI Archaeology is a book, laboratory, and implementation project with one non-negotiable teaching method.

## Do not begin with the answer

A contribution should normally move through:

```text
observation → concrete question → plausible attempt → visible failure
→ learner insight → verbal procedure → notation → implementation → new limit
```

Do not add a formula merely because it is standard. First make the reader need every operation in it. Do not use an analogy as proof; show where the analogy stops. Preserve a learner's discovery when it genuinely creates the idea.

## Keep the four paths aligned

For each excavation:

- the chapter supplies the causal narrative;
- the diagram makes that causal sequence visible;
- the exercise asks the reader to reinvent or break the idea;
- the implementation exposes the operations without hiding them behind a library too early.

If code introduces a concept not yet earned by the book, either simplify the code or extend the narrative first.

## Check the work

Run:

```bash
python3 -m unittest discover -s tests -v
```

NumPy and PyTorch examples are optional layers. The plain-Python implementation and tests must remain usable without them.
