# Book and Laboratory Completion Standard

An excavation is not complete because its files exist. It is complete only when
the reader can **discover, calculate, implement, vary, and test** the idea.

## Book gate

Every finished chapter must contain:

1. A named observation from the real world.
2. A decision handed to the reader before the solution is revealed.
3. A plausible attempt and a concrete case that breaks it.
4. A repair the reader can state in ordinary language.
5. A worked example using named objects and actual values.
6. Symbols introduced only as nicknames for understood pieces.
7. Every operation justified in human terms: why add rather than multiply,
   divide rather than merely count, log rather than use raw probability, and
   so on.
8. Each operation linked to its reusable mental model in
   [Mathematical Moves](MATHEMATICAL_MOVES.md).
9. A limitation that creates the next excavation.
10. Direct links to code, lab, mistakes, exercises, and references.

## Laboratory gate

Every executable mathematical chapter must provide:

1. Pure Python with visible loops and intermediate values.
2. NumPy expressing the same operation as arrays.
3. PyTorch expressing it with differentiable tensors.
4. A runnable experiment with adjustable inputs.
5. Assertions that demonstrate both the failed and repaired methods.
6. Expected observations and questions asking the reader to explain them.

## Evidence gate

A chapter marked complete must pass structural checks, implementation tests,
local-link checks, and manual reading review. Placeholder code, generic diagrams,
and unverified references fail this gate.
