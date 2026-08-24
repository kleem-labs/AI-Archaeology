# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

Nothing in the Hall of Voices yet bears today's mathematical name. There is only the public archivist, the listening table, and one plausible action: ask the language model to simulate every tool from memory.

The rule survives the easy cases. The next case leaves a crack through the middle of it: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. More confidence cannot repair information that never entered the rule.

*The public archivist sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: ask the language model to simulate…
                         │
                         └── mismatch: it invents live weather, makes…

reference evidence ──▶ measured repair: we need to let the model choose a…
```

Two trails now cross the listening table. The pale trail bears the instruction “ask the language model to simulate every tool from memory.” It disappears into the observed failure: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. The darker trail carries one additional capacity—to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed tool-using agents mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the listening table is altered in exactly one way: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Much later, people will call this territory **Tool-Using Agents**. Here the name is only a memory of the failure it can survive.

The listening table has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and tool-using agents looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made.

## When Words Must Cause Verified Actions

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

## Where tool-using agents runs out

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

The listening table answers today's question and falls silent at the next. That silence is precise: Tool-Using Agents was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the listening table

Rebuild the tool-using agents scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Authority](../056-authority/README.md)
