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

## Essence gate

Correct narrative structure is necessary but not sufficient. The finished book
must also make mathematics memorable as an inhabited journey:

1. Every part occupies a recurring place with objects that change purpose as
   the mathematics deepens. The setting carries continuity; it is never pasted
   on as fantasy decoration.
2. A chapter shows the old and repaired paths visually inside the reasoning.
   Diagrams must contain the chapter's actual evidence and failure, not generic
   boxes labelled “attempt” and “solution.”
3. Mathematical operations return as recognizable motifs. Summation is many
   witnesses joining one answer; division is judgment per unit; multiplication
   is one influence acting through another; logarithms turn compounded chances
   into accumulated steps. The metaphor must preserve the operation's exact
   job.
4. The prose creates curiosity, tension, silence, and reveal through events. It
   does not announce that the reader is discovering, that a method has been
   earned, or that a paragraph is pedagogically important.
5. At the end of each major arc, earlier discoveries reappear as one connected
   constellation. These codas reveal relationships rather than summarize a
   syllabus.
6. Poetry serves precision. A beautiful sentence fails if its image suggests
   the wrong mathematical behavior; exact mathematics fails as a book chapter
   if the reader cannot feel why it had to appear.

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
