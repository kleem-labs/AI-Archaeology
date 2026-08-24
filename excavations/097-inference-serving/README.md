# Excavation 097 — Inference Serving

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Decision-making, scaling, and accountable systems

Distributed training lets many machines construct one model. Deployment reverses the pressure: thousands of users now expect that model to answer with low latency, bounded cost, and consistent state.

Morning reaches the Road of Consequences before anyone has a name for today's difficulty. Beside the map of branching journeys, the expedition leader tries the smallest continuation of what already works: run one request at a time on one full model.

The rule survives the easy cases. The next case leaves a crack through the middle of it: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. More confidence cannot repair information that never entered the rule.

*The expedition leader sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ run one request at a time on one full… ──▶ blurred: the trouble appears immediately:…
      │
      └── new lens ──▶ batch compatible requests, cache… ──▶ distinction survives
```

Two trails now cross the map of branching journeys. The pale trail bears the instruction “run one request at a time on one full model.” It disappears into the observed failure: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues. The darker trail carries one additional capacity—to batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed inference serving mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the map of branching journeys is altered in exactly one way: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits. Much later, people will call this territory **Inference Serving**. Here the name is only a memory of the failure it can survive.

Nothing is erased from the map of branching journeys. The failed path remains visible beneath the repair, because inference serving is easier to remember when its scar remains attached to it. The scar reads, ‘the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues’; the new line exists only to keep that loss from happening again.

<!-- memory-film-v1:start -->
> **Memory realm 9 of 18 — [Road of Consequences](../../MEMORY_PALACE.md#realm-9)**
>
> **The question carried into this chamber:** What fails if we run one request at a time on one full model?

## When the chamber changes

The Inference Serving chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The lens follows the tempting path—run one request at a time on one full model. Then the evidence answers: the trouble appears immediately: hardware sits idle between small operations and traffic spikes create queues.

Now let the chamber move: The expedition leader changes one moving part. The lens can now batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

The object that should remain after the terminology disappears is **the inference serving lens mounted on the map of branching journeys**.

> **Memory seal — Inference Serving**
>
> Inference Serving keeps the missing power: batch compatible requests, cache repeated state, schedule fairly, and enforce resource limits.

Give the idea a bodily path: Touch the inference serving lens in imagination: hold both hands as the two failed alternatives, then move one hand through the repaired route.
<!-- memory-film-v1:end -->

## Understanding inference serving

Four prompts share one matrix operation while each retains separate token state.

## Where inference serving runs out

Batching improves throughput but can worsen individual latency.

The map of branching journeys answers today's question and falls silent at the next. That silence is precise: Inference Serving was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the map of branching journeys

Rebuild the inference serving scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 098](../098-red-teaming/README.md)
