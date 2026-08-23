# Excavation 055 — Tool-Using Agents — When Words Must Cause Verified Actions

<!-- book-prose-v2 -->

Retrieval lets the assistant look for evidence before speaking. Some requests require more than words: send a message, query a database, reserve equipment, or change real state.

Before naming anything new, try to ask the language model to simulate every tool from memory.

Its appeal is not ignorance but economy. Tool-Using Agents should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded.

Notice what the counterexample has accomplished for tool-using agents. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits.

Humanity eventually gathered this problem and its repairs under the name **Tool-Using Agents**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace tool-using agents with the old instruction to ask the language model to simulate every tool from memory. The result is again that it invents live weather, makes arithmetic errors, and cannot know whether an external action succeeded. Put back only the requirement to we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when tool-using agents is introduced. The same evidence that defeated the attempt to ask the language model to simulate every tool from memory is presented again. Only the ability to we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits changes, so the repaired conclusion cannot be credited to a conveniently different example.

## When Words Must Cause Verified Actions

The user asks whether to carry an umbrella. The model requests weather for the named city, receives a 90% rain forecast, and then answers. The forecast is an observation from the tool, not prose invented by the model.

Run the tool-using agents scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where tool-using agents runs out

An agent adds failure modes: bad tool choice, unsafe actions, prompt injection, loops, and ambiguous authority. Tools require permissions, validation, and stopping rules.

Why does that boundary remain? Tool-Using Agents was built for one responsibility: we need to let the model choose a permitted tool, provide structured arguments, observe the real result, and decide the next step under explicit limits. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take tool-using agents to the workbench

The argument for tool-using agents is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tool-using agents, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tool-using agents result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Authority](../056-authority/README.md)
