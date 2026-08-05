# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

[Previous: Excavation 054](../054-retrieval-augmented-generation/README.md)

## Take the First Step Yourself

> **Your problem:** A model can describe checking weather, calculating totals, or querying a database, but description alone does not obtain the result.

> **Try your first idea:** Ask the language model to simulate every tool from memory.

> **Now try to break your idea:** It invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

> Stop here. State what the repair must accomplish in ordinary language. Do not name a standard technique.

## The Observation

A model can describe checking weather, calculating totals, or querying a database, but description alone does not obtain the result.

## Your First Attempt

Ask the language model to simulate every tool from memory.

## Break Your First Attempt

It invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

What information did the attempt lose? Write that requirement before continuing.

## Repair Your Attempt

Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

## What You Have Just Invented

**Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.**

## Rebuild the Discovery with a Concrete Case

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Real-World Limit

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

A tool-using agent can affect the world. The next arc must excavate authority, memory, planning, verification, and safety before adding more autonomy.

[Next: Authority](../056-authority/README.md)
