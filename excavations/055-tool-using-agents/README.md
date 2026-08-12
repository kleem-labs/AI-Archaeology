# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

We first try to ask the language model to simulate every tool from memory.

But it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

We need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

## Let the case decide

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

## The boundary of the discovery

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

## Next Need

A tool-using agent can affect the world. The next arc must excavate authority, memory, planning, verification, and safety before adding more autonomy.

[Next: Authority](../056-authority/README.md)
