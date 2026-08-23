# Excavation 097 — Inference Serving

<!-- book-prose-v2 -->

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

For a moment, remain loyal to the simplest proposal: run one request at a time on one full model.

Its appeal is not ignorance but economy. Inference Serving should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

Notice what the counterexample has accomplished for inference serving. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

Humanity eventually gathered this problem and its repairs under the name **Inference Serving**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace inference serving with the old instruction to run one request at a time on one full model. The result is again that the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. Put back only the requirement to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when inference serving is introduced. The same evidence that defeated the attempt to run one request at a time on one full model is presented again. Only the ability to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Understanding inference serving

Four prompts share one matrix operation while each retains separate token state.

Run the inference serving scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where inference serving runs out

Batching improves throughput but can worsen individual latency.

Why does that boundary remain? Inference Serving was built for one responsibility: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take inference serving to the workbench

The argument for inference serving is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running inference serving, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the inference serving result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 098](../098-red-teaming/README.md)
