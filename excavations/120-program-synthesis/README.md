# Excavation 120 — Program Synthesis

Graph neural networks propagate learned messages through relational structure. Some tasks demand more than one answer: they demand a reusable procedure that maps every allowed input to an output.

Perhaps we memorize the provided input-output pairs.

But a new input exposes the absence of an underlying algorithm.

Now we can see what is missing: we must search or generate candidate programs, execute them, and keep those satisfying examples and constraints.

## Let the case decide

Examples 2→4 and 3→6 suggest multiply by two; testing 5 distinguishes it from memorized lookup.

## The boundary of the discovery

Finite examples rarely identify one unique intended program.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 121](../121-formal-verification/README.md)
