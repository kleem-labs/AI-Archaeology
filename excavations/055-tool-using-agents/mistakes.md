# Mistakes — 055

## First idea

Ask the language model to simulate every tool from memory.

## Counterexample

It invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

## Repair

Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.
