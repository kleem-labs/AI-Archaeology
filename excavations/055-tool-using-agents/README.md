# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

[Previous: Excavation 054](../054-retrieval-augmented-generation/README.md)

A model can describe checking weather, calculating totals, or querying a database, but description alone does not obtain the result.

The first solution that suggests itself is this: Ask the language model to simulate every tool from memory.

The idea survives only until we test it against reality: It invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. What information did the attempt lose? Write that requirement before continuing.

The failure gives us a precise requirement: Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

## Now work a case you can see

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

The boundary follows from the mechanism itself. We designed it to Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. That operation solves the failure we had reached, but it contains no step that answers the additional problem above.

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
