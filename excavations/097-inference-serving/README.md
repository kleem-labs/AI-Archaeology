# Excavation 097 — Inference Serving

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

The previous discovery reaches the Road of Consequences carrying one unfinished problem. Beside the map of branching journeys, the expedition leader first tries to run one request at a time on one full model.

There is good reason to begin this way. If we run one request at a time on one full model, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

This failure cannot be repaired by performing the instruction to run one request at a time on one full model more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the map of branching journeys; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Inference Serving**. The name is simply a handle for the distinction already reconstructed.

## Understanding inference serving

Four prompts share one matrix operation while each retains separate token state.

## Where inference serving runs out

Batching improves throughput but can worsen individual latency.

The map of branching journeys answers today's question and falls silent at the next. That silence is precise: Inference Serving was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the map of branching journeys

Rebuild the inference serving scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 098](../098-red-teaming/README.md)
