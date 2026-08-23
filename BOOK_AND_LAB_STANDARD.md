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

## Narrative gate

A chapter may satisfy every item above and still read like assembled notes. It
is book-ready only when:

1. The previous excavation creates the opening pressure for this one.
2. Observation, attempt, counterexample, and repair form one uninterrupted
   causal argument rather than a repeated lesson template.
3. The reader can remove the proposed repair, watch the original failure
   return, restore only the missing responsibility, and thereby test why the
   invention is necessary.
4. Section headings describe this chapter's actual question; generic headings
   such as “Problem,” “Naive Attempt,” and “Mathematics Emerges” are authoring
   scaffolds and do not appear in finished prose.
5. Term definitions and operation choices read as connected sentences. A
   glossary or checklist may support the narrative, but may not replace it.
6. A displayed equation arrives only after a named case has supplied every
   object, value, sign, and operation in that equation.
7. The limitation follows causally from what the method receives and does. It
   is not a detached warning added at the end.
8. Repeated editorial sentences are treated as a defect even when the facts
   inside each chapter differ. The book has one voice, not one template.

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
