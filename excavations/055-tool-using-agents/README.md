# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

[Previous: Excavation 054](../054-retrieval-augmented-generation/README.md)

A model can describe checking weather, calculating totals, or querying a database, but description alone does not obtain the result.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Ask the language model to simulate every tool from memory.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* It invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

What information did the attempt lose? Write that requirement before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

No new equation is needed here. The invention is a procedure and a separation of responsibilities, so forcing symbols into the chapter would hide rather than clarify it.

## Where your new idea still breaks

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
