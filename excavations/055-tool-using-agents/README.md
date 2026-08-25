# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete) · [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability)
>
> **Applied territory:** Language models and useful answers

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

Inside the Hall of Voices, the old method is given an honest chance. The public archivist places the evidence on the listening table and tries to ask the language model to simulate every tool from memory.

Nothing about this first move is careless. To ask the language model to simulate every tool from memory is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

The important discovery is not merely that trying to ask the language model to simulate every tool from memory failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the listening table, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Tool-Using Agents**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## When Words Must Cause Verified Actions

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

## Where tool-using agents runs out

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

The listening table answers today's question and falls silent at the next. That silence is precise: Tool-Using Agents was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the listening table

Rebuild the tool-using agents scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Authority](../056-authority/README.md)
